import collections
import configparser
import contextlib
import copy
import functools
import math
import multiprocessing
import os.path
import sys
import tempfile
import threading
import time
import webbrowser
from typing import Any, Callable, Iterable, Mapping, NoReturn, Optional, Union

import consts
import langs
import libs.files as files
import libs.files as paths
import libs.gui as gui
import libs.log as log
import libs.pyinstall as pyinstall
import libs.request as request
import libs.singleton as singleton
import libs.timer as timer
import libs.utils as utils
import modules
import win32

ALL_DISPLAY = 'DISPLAY'
UUID = f'{consts.AUTHOR}.{consts.NAME}'
RES_ICON, RES_TRAY, RES_BUSY = (files.join(os.path.dirname(__file__), 'resources', name)
                                for name in ('icon.ico', 'tray.png', 'busy.gif'))
TEMP_DIR = win32.wallpaper.TEMP_DIR = paths.join(tempfile.gettempdir(), consts.NAME)
CONFIG_PATH = fr'D:\Projects\Wallpyper\{consts.NAME}.ini'  # TODO paths.join(win32.SAVE_DIR, consts.NAME, f'{consts.NAME}.ini')
LOG_PATH = paths.replace_ext(CONFIG_PATH, 'log')
GOOGLE_URL = request.join('https://www.google.com', 'searchbyimage')
GOOGLE_UPLOAD_URL = request.join(GOOGLE_URL, 'upload')
BING_URL = request.join('https://www.bing.com', 'images', 'search')

INTERVALS = 0, 300, 900, 1800, 3600, 10800, 21600
STRINGS = langs.eng
DISPLAYS: list[str] = []
RESTART = threading.Event()
TIMER = timer.Timer.__new__(timer.Timer)
RECENT: collections.deque[files.File] = collections.deque(maxlen=consts.MAX_RECENT)

DEFAULT_CONFIG = {
    consts.CONFIG_LAST: math.inf,
    consts.CONFIG_RECENT: utils.encrypt(RECENT, True),
    consts.CONFIG_DISPLAY: ALL_DISPLAY,
    consts.CONFIG_FIRST: True,
    consts.CONFIG_AUTOSAVE: False,
    consts.CONFIG_SKIP: False,
    consts.CONFIG_NOTIFY: True,
    consts.CONFIG_ANIMATE: True,
    consts.CONFIG_CACHE: False,
    consts.CONFIG_START: False,
    consts.CONFIG_SAVE: False,
    consts.CONFIG_INTERVAL: INTERVALS[0],
    consts.CONFIG_MODULE: next(iter(modules.MODULES.values())).__name__,
    consts.CONFIG_DIR: files.join(win32.PICTURES_DIR, consts.NAME),
    consts.CONFIG_STYLE: win32.wallpaper.Style[win32.wallpaper.Style.FILL],
    consts.CONFIG_ROTATE: win32.wallpaper.Rotate[win32.wallpaper.Rotate.NONE],
    consts.CONFIG_FLIP: win32.wallpaper.Flip[win32.wallpaper.Flip.NONE],
    consts.CONFIG_TRANSITION: win32.wallpaper.Transition[win32.wallpaper.Transition.RANDOM]}
CONFIG = {}


def notify(title: str, text: str):
    if CONFIG[consts.CONFIG_NOTIFY]:
        gui.show_balloon(title, text)


def _fix_config(key: str, itt: Iterable):
    val = CONFIG[key]
    if is_str := isinstance(val, str):
        val = val.casefold()
    for val_ in itt:
        if val == (val_.casefold() if is_str else val_):
            CONFIG[key] = val_
            break
    else:
        CONFIG[key] = DEFAULT_CONFIG[key]


def fix_config(loaded: bool = True):
    _fix_config(consts.CONFIG_STYLE, win32.wallpaper.Style)
    _fix_config(consts.CONFIG_ROTATE, win32.wallpaper.Rotate)
    _fix_config(consts.CONFIG_FLIP, win32.wallpaper.Flip)
    _fix_config(consts.CONFIG_TRANSITION, win32.wallpaper.Transition)
    if loaded:
        CONFIG[consts.CONFIG_RECENT] = f'\n{utils.encrypt(RECENT, True)}'
    _fix_config(consts.CONFIG_DISPLAY, DISPLAYS)
    if CONFIG[consts.CONFIG_LAST] > time.time():
        CONFIG[consts.CONFIG_LAST] = DEFAULT_CONFIG[consts.CONFIG_LAST]
    _fix_config(consts.CONFIG_INTERVAL, INTERVALS)
    if not CONFIG[consts.CONFIG_DIR]:  # TODO is_path_exists_or_creatable
        CONFIG[consts.CONFIG_DIR] = DEFAULT_CONFIG[consts.CONFIG_DIR]
    _fix_config(consts.CONFIG_MODULE, modules.MODULES)


def _load_config(getters: dict[type, Callable[[str, str], Union[str, int, float, bool, tuple, list, set]]],
                 section: str, config: dict[str, Union[str, int, float, bool]],
                 default: dict[str, Union[str, int, float, bool]]) -> bool:
    loaded = True
    for option, value in default.items():
        try:
            config[option] = getters[type(value)](section, option)
        except (ValueError, TypeError, configparser.NoSectionError, configparser.NoOptionError):
            config[option] = copy.deepcopy(value)
            loaded = False
    return loaded


def load_config() -> bool:
    parser = configparser.ConfigParser(
        converters={tuple.__name__: utils.to_tuple, list.__name__: utils.to_list,
                    set.__name__: utils.to_set, dict.__name__: utils.to_dict})
    try:
        loaded = bool(parser.read(CONFIG_PATH))
    except configparser.MissingSectionHeaderError:
        loaded = False
    getters = {str: parser.get, int: parser.getint, float: parser.getfloat, bool: parser.getboolean,
               tuple: parser.gettuple, list: parser.getlist, set: parser.getset, dict: parser.getdict}
    loaded = _load_config(getters, consts.NAME, CONFIG, DEFAULT_CONFIG) and loaded
    fix_config(False)
    for name, module in modules.MODULES.items():
        loaded = _load_config(getters, name, module.CONFIG, module.DEFAULT_CONFIG) and loaded
        module.fix_config()
    return loaded


def _strip_config(config: dict[str, Any], default: dict[str, Any]) -> dict[str, Any]:
    return {option: config[option] for option, value in sorted(default.items()) if config[option] != value}


def save_config() -> bool:  # TODO save module generator to restore upon restart (?)
    fix_config()
    parser = configparser.ConfigParser()
    if config := _strip_config(CONFIG, DEFAULT_CONFIG):
        parser[consts.NAME] = config
    for name, module in modules.MODULES.items():
        module.fix_config()
        if config := _strip_config(module.CONFIG, module.DEFAULT_CONFIG):
            parser[name] = config
    with open(CONFIG_PATH, 'w') as file:
        parser.write(file)
    return os.path.isfile(CONFIG_PATH)


@timer.on_thread
def first_run():  # FIXME my icon
    if CONFIG[consts.CONFIG_FIRST]:
        CONFIG[consts.CONFIG_FIRST] = not gui.show_balloon(STRINGS.FIRST_TITLE, STRINGS.FIRST_TEXT, gui.Icon.INFORMATION)


_download_lock = functools.lru_cache(lambda _: threading.Lock())


def download_wallpaper(wallpaper: files.File, query_callback: Optional[Callable[[int, ...], bool]] = None,
                       args: Optional[Iterable] = None, kwargs: Optional[Mapping[str, Any]] = None) -> Optional[str]:
    temp_path = files.join(TEMP_DIR, wallpaper.name)
    with _download_lock(wallpaper.url):
        gui.start_animation(RES_BUSY, STRINGS.STATUS_DOWNLOAD)
        try:
            if request.download(wallpaper.url, temp_path, wallpaper.size, wallpaper.md5, wallpaper.sha256,
                                chunk_count=100, query_callback=query_callback, args=args, kwargs=kwargs):
                return temp_path
        finally:
            gui.stop_animation(STRINGS.STATUS_DOWNLOAD)


def get_next_wallpaper() -> Optional[files.File]:
    module = modules.MODULES[CONFIG[consts.CONFIG_MODULE]]
    config = {key: val for key, val in module.CONFIG.items() if not key.startswith('_')}
    first_wallpaper = None
    while True:
        next_wallpaper = next(module.get_next_wallpaper(**config))
        if not CONFIG[consts.CONFIG_SKIP] or next_wallpaper not in RECENT:
            if first_wallpaper != next_wallpaper:
                return next_wallpaper
            break
        if first_wallpaper is None:
            first_wallpaper = next_wallpaper


@utils.singleton_run
def change_wallpaper(wallpaper: Optional[files.File] = None, query_callback: Optional[Callable[[int, ...], bool]] = None,
                     args: Optional[Iterable] = None, kwargs: Optional[Mapping[str, Any]] = None) -> bool:
    changed = False
    if query_callback:
        query_callback(0, *() if args is None else args, **{} if kwargs is None else kwargs)
    if wallpaper is None:
        wallpaper = get_next_wallpaper()
    if wallpaper is not None:
        with contextlib.suppress(ValueError):
            RECENT.remove(wallpaper)
        RECENT.appendleft(wallpaper)
        wallpaper.name = win32.sanitize_filename(wallpaper.name)
        if path := download_wallpaper(wallpaper, query_callback, args, kwargs):
            # noinspection PyArgumentList
            changed = win32.wallpaper.set_multi(*(win32.wallpaper.Wallpaper(
                path, display, getattr(win32.wallpaper.Style, CONFIG[consts.CONFIG_STYLE]), rotate=getattr(
                    win32.wallpaper.Rotate, CONFIG[consts.CONFIG_ROTATE]), flip=getattr(
                    win32.wallpaper.Flip, CONFIG[consts.CONFIG_FLIP]), transition=getattr(
                    win32.wallpaper.Transition, CONFIG[consts.CONFIG_TRANSITION]))
                for display in (DISPLAYS if CONFIG[consts.CONFIG_DISPLAY] == ALL_DISPLAY else (CONFIG[consts.CONFIG_DISPLAY],))))
    return changed


@utils.singleton_run
def save_wallpaper(path: str) -> bool:
    return files.copy(path, files.join(CONFIG[consts.CONFIG_DIR], os.path.basename(path)))


@utils.singleton_run
def search_wallpaper(path: str) -> bool:
    searched = False
    gui.start_animation(RES_BUSY, STRINGS.STATUS_SEARCH)
    if location := request.upload(GOOGLE_UPLOAD_URL, files={'encoded_image': (None, path)},
                                  redirect=False).getheader('location'):
        searched = webbrowser.open(location)
    gui.stop_animation(STRINGS.STATUS_SEARCH)
    return searched


def on_open_url(url: str) -> bool:
    if not (opened := webbrowser.open(url)):
        notify(STRINGS.LABEL_OPEN_BROWSER, STRINGS.FAIL_OPEN_BROWSER)
    return opened


def on_copy_url(url: str) -> bool:
    if not (copied := win32.clipboard.copy_text(url)):
        notify(STRINGS.LABEL_COPY_URL, STRINGS.FAIL_COPY_URL)
    return copied


def on_google(url: str) -> bool:
    if not (opened := webbrowser.open(request.encode(GOOGLE_URL, {'image_url': url}))):
        notify(STRINGS.LABEL_SEARCH, STRINGS.FAIL_SEARCH)
    return opened


def on_bing(url: str) -> bool:
    if not (opened := webbrowser.open(request.encode(
            BING_URL, {'view': 'detailv2', 'iss': 'sbi', 'q': f'imgurl:{url}'}))):
        notify(STRINGS.LABEL_SEARCH, STRINGS.FAIL_SEARCH)
    return opened


@timer.on_thread
def on_change(enable: Callable, menu_recent, set_label: Callable,
              wallpaper: Optional[files.File] = None, auto_change: bool = True) -> bool:
    changed = False
    if not change_wallpaper.is_running():
        enable(False)
        menu_recent.Enable(False)
        gui.start_animation(RES_BUSY, STRINGS.STATUS_CHANGE)
        if auto_change:
            on_auto_change(CONFIG[consts.CONFIG_INTERVAL])
        CONFIG[consts.CONFIG_LAST] = time.time()
        if (changed := change_wallpaper(wallpaper, set_label)) and CONFIG[consts.CONFIG_AUTOSAVE]:
            on_click(save_wallpaper, RECENT[0], STRINGS.LABEL_SAVE, STRINGS.FAIL_SAVE)
        set_label()
        gui.stop_animation(STRINGS.STATUS_CHANGE)
        _update_recent(menu_recent)
        enable()
    if not changed:
        notify(STRINGS.LABEL_CHANGE, STRINGS.FAIL_CHANGE)
    return changed


def on_click(callback: utils.SingletonCallable[[str], bool], wallpaper: files.File, title: str, text: str) -> bool:
    success = False
    try:
        running = callback.is_running()
    except AttributeError:
        running = False
    if not running and (path := download_wallpaper(wallpaper)):
        with contextlib.suppress(BaseException):
            success = callback(path)
    if not success:
        notify(title, text)
    return success


def on_clear(enable: Callable):
    RECENT.clear()
    enable(False)


def _update_recent(menu):
    with gui.set_main_menu(menu):
        items = gui.get_menu_items()
        for index, wallpaper in enumerate(RECENT):
            label = f'{langs.to_str(index + 1, STRINGS)}. {utils.shrink_string(wallpaper.name, consts.MAX_LABEL)}'
            if wallpaper in items:
                menu_wallpaper = items[wallpaper.url]
                menu_wallpaper.SetItemLabel(label)
                gui.set_menu_item_position(menu_wallpaper, index)
            else:
                with gui.set_main_menu(gui.add_submenu(label, uid=wallpaper.url, position=index)):
                    gui.add_menu_item(STRINGS.LABEL_SET, on_click=on_change, args=(*TIMER.args, wallpaper),
                                      on_thread=False, change_state=False)
                    gui.add_menu_item(STRINGS.LABEL_SET_LOCK, on_click=on_click, args=(
                        win32.wallpaper.set_lock, wallpaper, STRINGS.LABEL_SET_LOCK, STRINGS.FAIL_CHANGE_LOCK))
                    gui.add_menu_item(STRINGS.LABEL_SAVE, on_click=on_click,
                                      args=(save_wallpaper, wallpaper, STRINGS.LABEL_SAVE, STRINGS.FAIL_SAVE))
                    gui.add_separator()
                    gui.add_menu_item(STRINGS.LABEL_OPEN, on_click=on_click, args=(
                        win32.open_file, wallpaper, STRINGS.LABEL_OPEN, STRINGS.FAIL_OPEN))
                    if consts.FEATURE_OPEN_WITH:
                        gui.add_menu_item(STRINGS.LABEL_OPEN_WITH, on_click=on_click, args=(
                            win32.open_file_with_ex, wallpaper, STRINGS.LABEL_OPEN_WITH, STRINGS.FAIL_OPEN_WITH))
                    gui.add_menu_item(STRINGS.LABEL_OPEN_EXPLORER, on_click=on_click, args=(
                        win32.open_file_path, wallpaper, STRINGS.LABEL_OPEN_EXPLORER, STRINGS.FAIL_OPEN_EXPLORER,))
                    gui.add_menu_item(STRINGS.LABEL_OPEN_BROWSER, on_click=on_open_url, args=(wallpaper.url,))
                    gui.add_separator()
                    gui.add_menu_item(STRINGS.LABEL_COPY_PATH, on_click=on_click, args=(
                        win32.clipboard.copy_text, wallpaper, STRINGS.LABEL_COPY_PATH, STRINGS.FAIL_COPY_PATH))
                    gui.add_menu_item(STRINGS.LABEL_COPY, on_click=on_click, args=(
                        win32.clipboard.copy_image, wallpaper, STRINGS.LABEL_COPY, STRINGS.FAIL_COPY))
                    gui.add_menu_item(STRINGS.LABEL_COPY_URL, on_click=on_copy_url, args=(wallpaper.url,))
                    gui.add_separator()
                    gui.add_menu_item(STRINGS.LABEL_GOOGLE, on_click=on_google, args=(wallpaper.url,))
                    gui.add_menu_item(STRINGS.LABEL_BING, on_click=on_bing, args=(wallpaper.url,))
                    if consts.FEATURE_GOOGLE_SEARCH:
                        gui.add_menu_item(STRINGS.LABEL_SEARCH, on_click=on_click, args=(
                            search_wallpaper, wallpaper, STRINGS.LABEL_SEARCH, STRINGS.FAIL_SEARCH,))
        if menu_items := tuple(menu_wallpaper for uid, menu_wallpaper in items.items() if uid and uid not in RECENT):
            gui.remove_menu_items(menu_items)
    menu.Enable(bool(RECENT))


def on_auto_change(interval: Union[int, str], after: Optional[float] = None):
    if isinstance(interval, str):
        interval = int(interval)
    CONFIG[consts.CONFIG_INTERVAL] = interval
    if interval:
        TIMER.set_next_interval(interval)
        TIMER.start(after)
    else:
        TIMER.stop()


def on_modify_save() -> bool:
    if path := win32.select_folder(STRINGS.LABEL_SAVE_DIR, CONFIG[consts.CONFIG_DIR]):
        CONFIG[consts.CONFIG_DIR] = path
    else:
        notify(STRINGS.LABEL_SAVE_DIR, STRINGS.FAIL_SAVE_DIR)
    return bool(path)


def on_flip(vertical, horizontal):
    vertical_checked = vertical.IsChecked()
    horizontal_checked = horizontal.IsChecked()
    if vertical_checked and horizontal_checked:
        CONFIG[consts.CONFIG_FLIP] = win32.wallpaper.Flip[win32.wallpaper.Flip.BOTH]
    elif vertical_checked:
        CONFIG[consts.CONFIG_FLIP] = win32.wallpaper.Flip[win32.wallpaper.Flip.VERTICAL]
    elif horizontal_checked:
        CONFIG[consts.CONFIG_FLIP] = win32.wallpaper.Flip[win32.wallpaper.Flip.HORIZONTAL]
    else:
        CONFIG[consts.CONFIG_FLIP] = win32.wallpaper.Flip[win32.wallpaper.Flip.NONE]


def _update_display():
    DISPLAYS.clear()
    DISPLAYS.extend(win32.wallpaper.get_monitor_ids())


def on_update_display(menu, update: bool = True):
    if update:
        _update_display()
    with gui.set_main_menu(menu):
        gui.remove_menu_items()
        size = win32.wallpaper.get_screen_size()
        gui.add_menu_item(f'{langs.to_str(0, STRINGS)}. {STRINGS.DISPLAY_ALL}\t{langs.to_str(size[0], STRINGS)} × {langs.to_str(size[1], STRINGS)}',
                          gui.Item.RADIO, CONFIG[consts.CONFIG_DISPLAY] == DEFAULT_CONFIG[consts.CONFIG_DISPLAY],
                          uid=DEFAULT_CONFIG[consts.CONFIG_DISPLAY], on_click=CONFIG.__setitem__,
                          menu_args=(gui.Property.UID,), args=(consts.CONFIG_DISPLAY,), pre_menu_args=False)
        monitors = win32.wallpaper.get_monitors()
        gui.add_mapped_submenu(menu, {
            id_: f'{langs.to_str(index, STRINGS)}. {monitors[id_][0] or win32.wallpaper.get_monitor_name(id_) or STRINGS.DISPLAY}'
                 f'\t{langs.to_str(monitors[id_][1][0], STRINGS)} × {monitors[id_][1][1]}'
            for index, id_ in enumerate(DISPLAYS, 1) if id_ in monitors}, CONFIG, consts.CONFIG_DISPLAY)
        if consts.FEATURE_UPDATE_DISPLAY:
            gui.add_separator()
            gui.add_menu_item(STRINGS.LABEL_UPDATE_DISPLAY, on_click=on_update_display, args=(menu,))
    # TODO add lock screen


def _get_launch_args() -> list[str]:
    argv = [sys.executable]
    if not pyinstall.FROZEN:
        argv.append(os.path.realpath(__file__))
    return argv


def _create_shortcut(dir_: str) -> bool:
    return files.make_dir(dir_) and win32.create_shortcut(files.join(dir_, consts.NAME), *_get_launch_args(),
                                                          icon_path=RES_ICON * (not pyinstall.FROZEN),
                                                          comment=STRINGS.DESCRIPTION, show=pyinstall.FROZEN, uid=UUID)


def on_shortcut() -> bool:
    if not (created := _create_shortcut(win32.DESKTOP_DIR)):
        notify(STRINGS.LABEL_DESKTOP, STRINGS.FAIL_DESKTOP)
    return created


def on_remove_shortcuts() -> bool:
    if not (removed := win32.remove_shortcuts(win32.DESKTOP_DIR, UUID)):
        notify(STRINGS.LABEL_REMOVE_DESKTOP, STRINGS.FAIL_REMOVE_DESKTOP)
    return removed


def on_start_shortcut() -> bool:
    if not (created := _create_shortcut(files.join(win32.START_DIR, consts.NAME))):
        notify(STRINGS.LABEL_START_MENU, STRINGS.FAIL_START_MENU)
    return created


def on_remove_start_shortcuts() -> bool:
    if not (removed := win32.remove_shortcuts(win32.START_DIR, UUID)):
        notify(STRINGS.LABEL_REMOVE_START_MENU, STRINGS.FAIL_REMOVE_START_MENU)
    return removed


def on_pin() -> bool:
    if not (pinned := win32.add_pin(*_get_launch_args(), name=consts.NAME, icon_path='' if pyinstall.FROZEN else RES_ICON,
                                    show=pyinstall.FROZEN)):
        notify(STRINGS.LABEL_PIN, STRINGS.FAIL_PIN)
    return pinned


def on_unpin() -> bool:
    if not (unpinned := win32.remove_pins(*_get_launch_args())):
        notify(STRINGS.LABEL_UNPIN, STRINGS.FAIL_UNPIN)
    return unpinned


@utils.singleton_run
def pin_to_start() -> bool:
    return win32.add_pin(*_get_launch_args(), taskbar=False, name=consts.NAME,
                         icon_path='' if pyinstall.FROZEN else RES_ICON, show=pyinstall.FROZEN)


def on_pin_start(enable: Callable, enable_: Callable) -> bool:
    pinned = False
    if not pin_to_start.is_running():
        enable(False)
        enable_(False)
        pinned = pin_to_start()
        enable_()
        enable()
    if not pinned:
        notify(STRINGS.LABEL_PIN_START, STRINGS.FAIL_PIN_START)
    return pinned


def on_unpin_start() -> bool:
    if not (unpinned := win32.remove_pins(*_get_launch_args(), taskbar=False)):
        notify(STRINGS.LABEL_UNPIN_START, STRINGS.FAIL_UNPIN_START)
    return unpinned


def on_clear_cache() -> bool:
    if not (cleared := files.remove(TEMP_DIR, True)):
        notify(STRINGS.LABEL_CLEAR_CACHE, STRINGS.FAIL_CLEAR)
    return cleared


def on_reset():
    CONFIG[consts.CONFIG_SAVE] = False
    on_restart()


def on_restart():
    RESTART.set()
    on_quit()


def on_module(name: str, menu):
    module = modules.MODULES[name]
    menu.SetItemLabel(module.NAME)
    with gui.set_main_menu(menu):
        gui.remove_menu_items()
        module.create_menu()
        menu.Enable(bool(gui.get_menu_items()))


def on_about():
    gui.show_balloon(STRINGS.LABEL_ABOUT, str(NotImplemented))


def apply_auto_start(start_: bool) -> bool:
    return win32.register_autorun(
        consts.NAME, *_get_launch_args(), *((consts.ARG_CHANGE,) if CONFIG[consts.CONFIG_INTERVAL] else ()),
        show=pyinstall.FROZEN, uid=UUID) if start_ else win32.unregister_autorun(consts.NAME, UUID)


def apply_save_config(save: bool) -> bool:
    return save_config() if save else files.remove(CONFIG_PATH)


def _is_running() -> bool:
    return (change_wallpaper.is_running() or save_wallpaper.is_running() or
            search_wallpaper.is_running() or pin_to_start.is_running())


@timer.on_thread
def on_quit():
    TIMER.stop()
    gui.disable_events()
    if _is_running():
        notify(STRINGS.LABEL_QUIT, STRINGS.FAIL_QUIT)
        end_time = time.time() + win32.get_max_shutdown_time()
        while end_time > time.time() and _is_running():
            time.sleep(consts.POLL_INTERVAL)
    gui.stop_loop()


def create_menu():  # TODO slideshow (smaller timer)
    item_change = gui.add_menu_item(STRINGS.LABEL_CHANGE)
    menu_recent = gui.add_submenu(STRINGS.MENU_RECENT, False)

    def query_callback(progress: Optional[int] = None) -> bool:  # TODO fix exploding width
        item_change.SetItemLabel(STRINGS.LABEL_CHANGE if progress is None else
                                 f'{STRINGS.LABEL_CHANGE} ({langs.to_str(min(99, progress), STRINGS, 2)}%)')
        return True

    TIMER.__init__(0, on_change, (item_change.Enable, menu_recent, query_callback))
    gui.add_separator(menu=menu_recent)
    gui.add_menu_item(STRINGS.LABEL_CLEAR, on_click=on_clear, args=(menu_recent.Enable,), menu=menu_recent)
    _update_recent(menu_recent)
    gui.set_on_click(item_change, on_change, args=TIMER.args, on_thread=False, change_state=False)
    gui.add_separator()
    menu_module = gui.add_submenu('_')
    on_module(CONFIG[consts.CONFIG_MODULE], menu_module)
    gui.add_separator()
    with gui.set_main_menu(gui.add_submenu(STRINGS.MENU_ACTIONS)):
        with gui.set_main_menu(gui.add_submenu(STRINGS.MENU_LINKS)):
            gui.add_menu_item(STRINGS.LABEL_DESKTOP, on_click=on_shortcut)
            gui.add_menu_item(STRINGS.LABEL_REMOVE_DESKTOP, on_click=on_remove_shortcuts)
            gui.add_separator()
            gui.add_menu_item(STRINGS.LABEL_START_MENU, on_click=on_start_shortcut)
            gui.add_menu_item(STRINGS.LABEL_REMOVE_START_MENU, on_click=on_remove_start_shortcuts)
            gui.add_separator()
            gui.add_menu_item(STRINGS.LABEL_PIN, enable=pyinstall.FROZEN or consts.FEATURE_PIN_PYTHON, on_click=on_pin)
            gui.add_menu_item(STRINGS.LABEL_UNPIN, enable=pyinstall.FROZEN or consts.FEATURE_PIN_PYTHON, on_click=on_unpin)
            gui.add_separator()
            unpin_enable = gui.add_menu_item(STRINGS.LABEL_UNPIN_START, enable=pyinstall.FROZEN or consts.FEATURE_PIN_PYTHON,
                                             on_click=on_unpin_start).Enable
            gui.add_menu_item(STRINGS.LABEL_PIN_START, enable=pyinstall.FROZEN or consts.FEATURE_PIN_PYTHON,
                              on_click=on_pin_start, menu_args=(gui.Method.ENABLE,),
                              args=(unpin_enable,), change_state=False, position=9)
        gui.add_menu_item(STRINGS.LABEL_CLEAR_CACHE, on_click=on_clear_cache)
        gui.add_menu_item(STRINGS.LABEL_RESET, on_click=on_reset)
        gui.add_menu_item(STRINGS.LABEL_RESTART, enable=bool(multiprocessing.parent_process()), on_click=on_restart)
        gui.add_menu_item(STRINGS.LABEL_ABOUT, on_click=on_about)
    with gui.set_main_menu(gui.add_submenu(STRINGS.MENU_SETTINGS)):
        with gui.set_main_menu(gui.add_submenu(STRINGS.MENU_AUTO)):
            gui.add_mapped_submenu(STRINGS.MENU_AUTO_CHANGE,
                                   {str(interval): getattr(STRINGS, f'TIME_{interval}') for interval in INTERVALS},
                                   CONFIG, consts.CONFIG_INTERVAL, on_click=on_auto_change)
            gui.add_separator()
            gui.add_mapped_menu_item(STRINGS.LABEL_AUTO_SAVE, CONFIG, consts.CONFIG_AUTOSAVE)
            gui.add_menu_item(STRINGS.LABEL_SAVE_DIR, on_click=on_modify_save)
        gui.add_mapped_submenu(STRINGS.MENU_TRANSITION,
                               {transition: getattr(STRINGS, f'TRANSITION_{transition}') for transition in
                                win32.wallpaper.Transition}, CONFIG, consts.CONFIG_TRANSITION)
        gui.add_mapped_submenu(STRINGS.MENU_ROTATE,
                               {rotate: getattr(STRINGS, f'ROTATE_{rotate}') for rotate in
                                win32.wallpaper.Rotate}, CONFIG, consts.CONFIG_ROTATE)
        with gui.set_main_menu(gui.add_submenu(STRINGS.MENU_FLIP)):
            item_vertical = gui.add_menu_item(STRINGS.FLIP_VERTICAL, gui.Item.CHECK, getattr(
                win32.wallpaper.Flip, CONFIG[consts.CONFIG_FLIP]) in (win32.wallpaper.Flip.VERTICAL, win32.wallpaper.Flip.BOTH))
            item_horizontal = gui.add_menu_item(STRINGS.FLIP_HORIZONTAL, gui.Item.CHECK, getattr(
                win32.wallpaper.Flip, CONFIG[consts.CONFIG_FLIP]) in (win32.wallpaper.Flip.HORIZONTAL, win32.wallpaper.Flip.BOTH))
            gui.set_on_click(item_vertical, on_flip, args=(item_vertical, item_horizontal))
            gui.set_on_click(item_horizontal, on_flip, args=(item_vertical, item_horizontal))
        gui.add_mapped_submenu(STRINGS.MENU_ALIGNMENT,
                               {style: getattr(STRINGS, f'ALIGNMENT_{style}') for style in win32.wallpaper.Style},
                               CONFIG, consts.CONFIG_STYLE)
        gui.add_mapped_submenu(STRINGS.MENU_MODULE,
                               {name: f'{name}\t{module.VERSION}' for name, module in modules.MODULES.items()},
                               CONFIG, consts.CONFIG_MODULE, on_click=on_module, args=(menu_module,))
        print(*(module.ICON for module in modules.MODULES.values()), sep='\n')  # TODO
        menu_display = gui.add_submenu(STRINGS.MENU_DISPLAY)
        on_update_display(menu_display, False)
        gui.add_separator()
        gui.add_mapped_menu_item(STRINGS.LABEL_ANIMATE, CONFIG, consts.CONFIG_ANIMATE, on_click=gui.enable_animation)
        gui.add_mapped_menu_item(STRINGS.LABEL_NOTIFY, CONFIG, consts.CONFIG_NOTIFY)
        gui.add_mapped_menu_item(STRINGS.LABEL_SKIP, CONFIG, consts.CONFIG_SKIP)
        gui.add_mapped_menu_item(STRINGS.LABEL_CACHE, CONFIG, consts.CONFIG_CACHE)
        gui.add_mapped_menu_item(STRINGS.LABEL_START, CONFIG, consts.CONFIG_START)
        gui.add_mapped_menu_item(STRINGS.LABEL_CONFIG, CONFIG, consts.CONFIG_SAVE)
    gui.add_menu_item(STRINGS.LABEL_QUIT, on_click=on_quit, on_thread=False)


def start():  # TODO dark theme
    singleton.init(UUID, consts.NAME, consts.ARG_WAIT in sys.argv, on_crash=print, on_crash_args=('Crash',),
                   on_wait=print, on_wait_args=('Wait',), on_exit=print, on_exit_args=('Exit',))
    if consts.ARG_DEBUG in sys.argv:
        log.redirect_stdout(LOG_PATH, True) if pyinstall.FROZEN else log.write_on_exception(LOG_PATH)
        log.init(os.path.basename(__file__),
                 utils.re_join('libs', r'.*\.py'), utils.re_join('modules', r'.*\.py'),
                 utils.re_join('win32', r'.*\.py'), level=log.Level.INFO, check_comp=False)
    pyinstall.clean_temp()
    files.make_dir(TEMP_DIR)
    files.trim_dir(TEMP_DIR, consts.MAX_CACHE)
    _update_display()
    load_config()
    RECENT.extend(utils.decrypt(CONFIG[consts.CONFIG_RECENT], ()))
    create_menu()
    gui.enable_animation(CONFIG[consts.CONFIG_ANIMATE])
    apply_auto_start(CONFIG[consts.CONFIG_START])
    apply_save_config(CONFIG[consts.CONFIG_SAVE])
    after = CONFIG[consts.CONFIG_INTERVAL] + CONFIG[consts.CONFIG_LAST] - time.time()
    if consts.ARG_CHANGE in sys.argv or (CONFIG[consts.CONFIG_INTERVAL] and after <= 0):
        on_change(*TIMER.args, auto_change=False)
    on_auto_change(CONFIG[consts.CONFIG_INTERVAL], None if after <= 0 else after)
    gui.start_loop(RES_TRAY, consts.NAME, on_change, TIMER.args, call_after=first_run)


def stop():
    timer.Timer.kill_all()
    apply_auto_start(CONFIG[consts.CONFIG_START])
    apply_save_config(CONFIG[consts.CONFIG_SAVE])
    files.trim_dir(TEMP_DIR, consts.MAX_CACHE) if CONFIG[consts.CONFIG_CACHE] else files.remove(TEMP_DIR, True)
    if os.path.isdir(TEMP_DIR) and files.is_empty_dir(TEMP_DIR, True):
        files.remove(TEMP_DIR, True)


def main() -> NoReturn:
    start()
    stop()
    sys.exit(consts.EX_TEMPFAIL * RESTART.is_set())  # TODO 0xC0000409 (STATUS_STACK_BUFFER_OVERRUN)


if __name__ == '__main__':
    main()
