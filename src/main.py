import collections
import configparser
import contextlib
import copy
import functools
import itertools
import math
import multiprocessing
import os.path
import sys
import tempfile
import threading
import time
import webbrowser
from typing import Any, Callable, Iterable, Mapping, NoReturn, Optional

import consts
import gui
import langs
import libs.files as files
import libs.files as paths
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
RES_TEMPLATE = os.path.realpath(os.path.join(os.path.dirname(__file__), 'res', '{}'))
gui.ANIMATION_PATH = RES_TEMPLATE.format(consts.RES_BUSY)
TEMP_DIR = win32.display.TEMP_WALLPAPER_DIR = os.path.join(tempfile.gettempdir(), consts.NAME)
CONFIG_PATH = fr'D:\Projects\Wallpyper\{consts.NAME}.ini'  # TODO paths.join(win32.SAVE_DIR, consts.NAME, f'{consts.NAME}.ini')
LOG_PATH = paths.replace_ext(CONFIG_PATH, 'log')
GOOGLE_URL = request.join('https://www.google.com', 'searchbyimage')
GOOGLE_UPLOAD_URL = request.join(GOOGLE_URL, 'upload')
BING_URL = request.join('https://www.bing.com', 'images', 'search')

win32.gui.FLAG_MENU_ITEM_IMAGE_CACHE = True
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
    consts.CONFIG_FIRST: consts.FEATURE_FIRST_RUN,
    consts.CONFIG_AUTOSAVE: False,
    consts.CONFIG_SKIP: False,
    consts.CONFIG_REAPPLY: True,
    consts.CONFIG_NOTIFY: True,
    consts.CONFIG_ANIMATE: True,
    consts.CONFIG_CACHE: False,
    consts.CONFIG_START: False,
    consts.CONFIG_SAVE: False,
    consts.CONFIG_BLOCKED: True,
    consts.CONFIG_INTERVAL: INTERVALS[0],
    consts.CONFIG_MODULE: next(iter(modules.MODULES.values())).__name__,
    consts.CONFIG_DIR: os.path.join(win32.PICTURES_DIR, consts.NAME),
    consts.CONFIG_STYLE: win32.display.Style[win32.display.Style.FILL],
    consts.CONFIG_ROTATE: win32.display.Rotate[win32.display.Rotate.NONE],
    consts.CONFIG_FLIP: win32.display.Flip[win32.display.Flip.NONE],
    consts.CONFIG_TRANSITION: win32.display.Transition[win32.display.Transition.FADE]}
CONFIG = {}


def notify(title: str, text: str, icon: int | str = win32.gui.SystemTrayIcon.BALLOON_NONE, force: bool = False) -> bool:
    if force or CONFIG[consts.CONFIG_NOTIFY]:
        return gui.SYSTEM_TRAY.show_balloon(title, utils.shrink_string(text, consts.MAX_NOTIFICATION_LEN), icon)
    return False


def reapply_wallpaper(_):
    if CONFIG[consts.CONFIG_REAPPLY] and RECENT:
        on_change(*TIMER.args, RECENT[0], False)


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
    _fix_config(consts.CONFIG_STYLE, win32.display.Style)
    _fix_config(consts.CONFIG_ROTATE, win32.display.Rotate)
    _fix_config(consts.CONFIG_FLIP, win32.display.Flip)
    _fix_config(consts.CONFIG_TRANSITION, win32.display.Transition)
    if loaded:
        CONFIG[consts.CONFIG_RECENT] = f'\n{utils.encrypt(RECENT, True)}'
    _fix_config(consts.CONFIG_DISPLAY, DISPLAYS)
    if CONFIG[consts.CONFIG_LAST] > time.time():
        CONFIG[consts.CONFIG_LAST] = DEFAULT_CONFIG[consts.CONFIG_LAST]
    _fix_config(consts.CONFIG_INTERVAL, INTERVALS)
    if not CONFIG[consts.CONFIG_DIR]:  # TODO is_path_exists_or_creatable
        CONFIG[consts.CONFIG_DIR] = DEFAULT_CONFIG[consts.CONFIG_DIR]
    _fix_config(consts.CONFIG_MODULE, modules.MODULES)


def _load_config(getters: dict[type, Callable[[str, str], str | int | float | bool | tuple | list | set]],
                 section: str, config: dict[str, str | int | float | bool],
                 default: dict[str, str | int | float | bool]) -> bool:
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
def first_run():
    if CONFIG[consts.CONFIG_FIRST]:
        while not gui.SYSTEM_TRAY.is_shown(False):
            time.sleep(consts.POLL_INTERVAL)
        CONFIG[consts.CONFIG_FIRST] = not notify(
            STRINGS.FIRST_TITLE, STRINGS.FIRST_TEXT, RES_TEMPLATE.format(consts.RES_ICON), True)


@timer.on_thread
def check_blocked(*_, monitors: Optional[dict[str, str]] = None):
    if CONFIG[consts.CONFIG_BLOCKED]:
        displays = DISPLAYS if CONFIG[consts.CONFIG_DISPLAY] == ALL_DISPLAY else (CONFIG[consts.CONFIG_DISPLAY],)
        if not all(win32.display.is_desktop_unblocked(*displays).values()):
            if monitors is None:
                monitors = win32.display.get_monitors()
            count = itertools.count(1)
            text = '\n'.join(f'{langs.to_str(next(count), STRINGS)}. {_get_monitor_name(monitor, monitors)}'
                             f'{f": {os.path.basename(blocker[1])}" if consts.FEATURE_BLOCKED_NAME else ""}'
                             for monitor, blocker in win32.display.get_desktop_blocker(*displays).items() if blocker is not None)
            while not gui.SYSTEM_TRAY.is_shown(False):
                time.sleep(consts.POLL_INTERVAL)
            if CONFIG[consts.CONFIG_FIRST]:
                end_time = time.time() + consts.MAX_FIRST_NOTIFICATION_TIMEOUT
                while end_time > time.time() and not CONFIG[consts.CONFIG_FIRST]:
                    time.sleep(consts.POLL_INTERVAL)
            notify(STRINGS.BLOCKED_TITLE, STRINGS.BLOCKED_TEXT.format(text), force=True)


_download_lock = functools.lru_cache(lambda _: threading.Lock())


def download_wallpaper(wallpaper: files.File, query_callback: Optional[Callable[[float, ...], bool]] = None,
                       args: Optional[Iterable] = None, kwargs: Optional[Mapping[str, Any]] = None) -> Optional[str]:
    temp_path = os.path.join(TEMP_DIR, wallpaper.name)
    with _download_lock(wallpaper.url), gui.animate(STRINGS.STATUS_DOWNLOAD):
        if request.download(wallpaper.url, temp_path, wallpaper.size, wallpaper.md5, wallpaper.sha256,
                            chunk_count=100, query_callback=query_callback, args=args, kwargs=kwargs):
            return temp_path


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
def change_wallpaper(wallpaper: Optional[files.File] = None, query_callback: Optional[Callable[[float, ...], bool]] = None,
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
            changed = win32.display.set_wallpapers_ex(*(win32.display.Wallpaper(
                path, display, getattr(win32.display.Style, CONFIG[consts.CONFIG_STYLE]), rotate=getattr(
                    win32.display.Rotate, CONFIG[consts.CONFIG_ROTATE]), flip=getattr(
                    win32.display.Flip, CONFIG[consts.CONFIG_FLIP]), transition=getattr(
                    win32.display.Transition, CONFIG[consts.CONFIG_TRANSITION]))
                for display in (DISPLAYS if CONFIG[consts.CONFIG_DISPLAY] == ALL_DISPLAY else (CONFIG[consts.CONFIG_DISPLAY],))))
    return changed


@utils.singleton_run
def save_wallpaper(path: str) -> bool:
    return files.copy(path, os.path.join(CONFIG[consts.CONFIG_DIR], os.path.basename(path)))


@utils.singleton_run
def search_wallpaper(path: str) -> bool:
    searched = False
    with gui.animate(STRINGS.STATUS_SEARCH):
        if location := request.upload(GOOGLE_UPLOAD_URL, files={'encoded_image': (None, path)},
                                      redirect=False).getheader('location'):
            searched = webbrowser.open(location)
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
        notify(STRINGS.LABEL_LENS, STRINGS.FAIL_SEARCH)
    return opened


def on_bing(url: str) -> bool:
    if not (opened := webbrowser.open(request.encode(
            BING_URL, {'view': 'detailv2', 'iss': 'sbi', 'q': f'imgurl:{url}'}))):
        notify(STRINGS.LABEL_LENS, STRINGS.FAIL_SEARCH)
    return opened


@timer.on_thread
def on_change(enable: Callable, menu_recent: win32.gui.MenuItem, set_label: Callable,
              wallpaper: Optional[files.File] = None, auto_change: bool = True) -> bool:
    changed = False
    if not change_wallpaper.is_running():
        enable(False)
        menu_recent.enable(False)
        with gui.animate(STRINGS.STATUS_CHANGE):
            if auto_change:
                on_auto_change(CONFIG[consts.CONFIG_INTERVAL])
            CONFIG[consts.CONFIG_LAST] = time.time()
            if (changed := change_wallpaper(wallpaper, set_label)) and CONFIG[consts.CONFIG_AUTOSAVE]:
                on_click(save_wallpaper, RECENT[0], STRINGS.LABEL_SAVE, STRINGS.FAIL_SAVE)
            set_label()
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
        try:
            success = callback(path)
        except BaseException as e:
            print(e)
    if not success:
        notify(title, text)
    return success


def on_clear(enable: Callable):
    RECENT.clear()
    enable(False)


def _update_recent(item: win32.gui.MenuItem):
    menu = item.get_submenu()
    with gui.set_main_menu(menu):
        items = gui.get_menu_items()
        for index, wallpaper in enumerate(RECENT):
            label = f'{langs.to_str(index + 1, STRINGS)}. {utils.shrink_string(wallpaper.name, consts.MAX_LABEL)}'
            if wallpaper in items:
                item_ = items[wallpaper.url]
                submenu = item_.get_submenu()
                menu.remove_item(item_)
            else:
                with gui.set_main_menu(gui.Menu()) as submenu:
                    gui.add_menu_item(STRINGS.LABEL_SET, on_click=on_change, args=(*TIMER.args, wallpaper),
                                      on_thread=False, change_state=False).set_icon(RES_TEMPLATE.format(consts.RES_SET))
                    gui.add_menu_item(STRINGS.LABEL_SET_LOCK, on_click=on_click, args=(
                        win32.display.set_lock_background, wallpaper, STRINGS.LABEL_SET_LOCK, STRINGS.FAIL_CHANGE_LOCK)).set_icon(
                        RES_TEMPLATE.format(consts.RES_SET_LOCK))
                    gui.add_menu_item(STRINGS.LABEL_SAVE, on_click=on_click, args=(
                        save_wallpaper, wallpaper, STRINGS.LABEL_SAVE, STRINGS.FAIL_SAVE)).set_icon(
                        RES_TEMPLATE.format(consts.RES_SAVE))
                    gui.add_separator()
                    gui.add_menu_item(STRINGS.LABEL_OPEN, on_click=on_click, args=(
                        win32.open_file, wallpaper, STRINGS.LABEL_OPEN, STRINGS.FAIL_OPEN)).set_icon(
                        RES_TEMPLATE.format(consts.RES_OPEN))
                    if consts.FEATURE_OPEN_WITH:
                        gui.add_menu_item(STRINGS.LABEL_OPEN_WITH, on_click=on_click, args=(
                            win32.open_file_with_ex, wallpaper, STRINGS.LABEL_OPEN_WITH, STRINGS.FAIL_OPEN_WITH)).set_icon(
                            RES_TEMPLATE.format(consts.RES_OPEN_WITH))
                    gui.add_menu_item(STRINGS.LABEL_OPEN_EXPLORER, on_click=on_click, args=(
                        win32.open_file_path, wallpaper, STRINGS.LABEL_OPEN_EXPLORER, STRINGS.FAIL_OPEN_EXPLORER,)).set_icon(
                        RES_TEMPLATE.format(consts.RES_OPEN_EXPLORER))
                    gui.add_menu_item(STRINGS.LABEL_OPEN_BROWSER, on_click=on_open_url, args=(wallpaper.url,)).set_icon(
                        RES_TEMPLATE.format(consts.RES_OPEN_BROWSER))
                    gui.add_separator()
                    gui.add_menu_item(STRINGS.LABEL_COPY_PATH, on_click=on_click, args=(
                        win32.clipboard.copy_text, wallpaper, STRINGS.LABEL_COPY_PATH, STRINGS.FAIL_COPY_PATH)).set_icon(
                        RES_TEMPLATE.format(consts.RES_COPY_PATH))
                    gui.add_menu_item(STRINGS.LABEL_COPY, on_click=on_click, args=(
                        win32.clipboard.copy_image, wallpaper, STRINGS.LABEL_COPY, STRINGS.FAIL_COPY)).set_icon(
                        RES_TEMPLATE.format(consts.RES_COPY))
                    gui.add_menu_item(STRINGS.LABEL_COPY_URL, on_click=on_copy_url, args=(wallpaper.url,)).set_icon(
                        RES_TEMPLATE.format(consts.RES_COPY_URL))
                    gui.add_separator()
                    gui.add_menu_item(STRINGS.LABEL_GOOGLE, on_click=on_google, args=(
                        wallpaper.url,)).set_icon(RES_TEMPLATE.format(consts.RES_GOOGLE))
                    gui.add_menu_item(STRINGS.LABEL_BING, on_click=on_bing, args=(
                        wallpaper.url,)).set_icon(RES_TEMPLATE.format(consts.RES_BING))
                    if consts.FEATURE_LENS_UPLOAD:
                        gui.add_menu_item(STRINGS.LABEL_LENS, on_click=on_click, args=(
                            search_wallpaper, wallpaper, STRINGS.LABEL_LENS, STRINGS.FAIL_SEARCH,)).set_icon(
                            RES_TEMPLATE.format(consts.RES_LENS))
            item_ = menu.insert_item(index, label, submenu=submenu)
            item_.set_tooltip(wallpaper.url, wallpaper.name, os.path.join(
                TEMP_DIR, wallpaper.name) if consts.FEATURE_TOOLTIP_ICON else gui.MenuItemTooltipIcon.NONE)
            item_.set_uid(wallpaper.url)
    for uid, item_ in items.items():
        if uid and uid not in RECENT:
            menu.remove_item(item_)
    item.enable(bool(RECENT))


def on_auto_change(interval: int, after: Optional[float] = None):
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


def on_flip(vertical: win32.gui.MenuItem, horizontal: win32.gui.MenuItem):
    vertical_checked = vertical.is_checked()
    horizontal_checked = horizontal.is_checked()
    if vertical_checked and horizontal_checked:
        CONFIG[consts.CONFIG_FLIP] = win32.display.Flip[win32.display.Flip.BOTH]
    elif vertical_checked:
        CONFIG[consts.CONFIG_FLIP] = win32.display.Flip[win32.display.Flip.VERTICAL]
    elif horizontal_checked:
        CONFIG[consts.CONFIG_FLIP] = win32.display.Flip[win32.display.Flip.HORIZONTAL]
    else:
        CONFIG[consts.CONFIG_FLIP] = win32.display.Flip[win32.display.Flip.NONE]
    reapply_wallpaper(None)


def _update_display():
    DISPLAYS.clear()
    DISPLAYS.extend(win32.display.get_monitor_ids())


def _get_monitor_name(monitor: str, monitors: dict[str, tuple[str, tuple[int, int]]]) -> str:
    return monitors[monitor][0] or win32.display.get_monitor_name(monitor) or STRINGS.DISPLAY


def on_display_change(update: int, __: Optional[gui.Gui], item: win32.gui.MenuItem):
    if update:
        _update_display()
    submenu = item.get_submenu()
    submenu.clear_items()
    with gui.set_main_menu(submenu):
        size = win32.display.get_display_size()
        gui.add_menu_item(f'{langs.to_str(0, STRINGS)}. {STRINGS.DISPLAY_ALL}\t{langs.to_str(size[0], STRINGS)} × {langs.to_str(size[1], STRINGS)}',
                          gui.MenuItemType.RADIO, CONFIG[consts.CONFIG_DISPLAY] == DEFAULT_CONFIG[consts.CONFIG_DISPLAY],
                          uid=DEFAULT_CONFIG[consts.CONFIG_DISPLAY], on_click=CONFIG.__setitem__,
                          menu_args=(gui.Property.UID,), args=(consts.CONFIG_DISPLAY,), pre_menu_args=False)
        monitors = win32.display.get_monitors()
        gui.add_mapped_submenu(item, {
            id_: f'{langs.to_str(index, STRINGS)}. {_get_monitor_name(id_, monitors)}'
                 f'\t{langs.to_str(monitors[id_][1][0], STRINGS)} × {monitors[id_][1][1]}'
            for index, id_ in enumerate(DISPLAYS, 1) if id_ in monitors}, CONFIG, consts.CONFIG_DISPLAY,
                               on_click=check_blocked, kwargs={'monitors': monitors})
        if consts.FEATURE_UPDATE_DISPLAY:
            gui.add_separator()
            gui.add_menu_item(STRINGS.LABEL_UPDATE_DISPLAY, on_click=on_display_change, args=(item,))
    check_blocked(monitors=monitors)
    # TODO add lock screen


def _get_launch_args() -> list[str]:
    argv = [sys.executable]
    if not pyinstall.FROZEN:
        argv.append(os.path.realpath(__file__))
    return argv


def _create_shortcut(dir_: str) -> bool:
    return files.make_dir(dir_) and win32.create_shortcut(os.path.join(
        dir_, consts.NAME), *_get_launch_args(), icon_path=RES_TEMPLATE.format(consts.RES_ICON) * (
        not pyinstall.FROZEN), comment=STRINGS.DESCRIPTION, show=pyinstall.FROZEN, uid=UUID)


def on_shortcut() -> bool:
    if not (created := _create_shortcut(win32.DESKTOP_DIR)):
        notify(STRINGS.LABEL_DESKTOP, STRINGS.FAIL_DESKTOP)
    return created


def on_remove_shortcuts() -> bool:
    if not (removed := win32.remove_shortcuts(win32.DESKTOP_DIR, UUID)):
        notify(STRINGS.LABEL_REMOVE_DESKTOP, STRINGS.FAIL_REMOVE_DESKTOP)
    return removed


def on_start_shortcut() -> bool:
    if not (created := _create_shortcut(os.path.join(win32.START_DIR, consts.NAME))):
        notify(STRINGS.LABEL_START_MENU, STRINGS.FAIL_START_MENU)
    return created


def on_remove_start_shortcuts() -> bool:
    if not (removed := win32.remove_shortcuts(win32.START_DIR, UUID)):
        notify(STRINGS.LABEL_REMOVE_START_MENU, STRINGS.FAIL_REMOVE_START_MENU)
    return removed


def on_pin() -> bool:
    if not (pinned := win32.add_pin(
            *_get_launch_args(), name=consts.NAME, icon_path='' if pyinstall.FROZEN else RES_TEMPLATE.format(
                consts.RES_ICON), show=pyinstall.FROZEN)):
        notify(STRINGS.LABEL_PIN, STRINGS.FAIL_PIN)
    return pinned


def on_unpin() -> bool:
    if not (unpinned := win32.remove_pins(*_get_launch_args())):
        notify(STRINGS.LABEL_UNPIN, STRINGS.FAIL_UNPIN)
    return unpinned


@utils.singleton_run
def pin_to_start() -> bool:
    return win32.add_pin(*_get_launch_args(), taskbar=False, name=consts.NAME,
                         icon_path='' if pyinstall.FROZEN else RES_TEMPLATE.format(consts.RES_ICON), show=pyinstall.FROZEN)


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


def on_module(name: str, item: win32.gui.MenuItem):
    module = modules.MODULES[name]
    item.set_text(module.NAME)
    item.set_icon(module.ICON if os.path.isfile(module.ICON) else gui.MenuItemImage.NONE)
    submenu = item.get_submenu()
    submenu.clear_items()
    with gui.set_main_menu(submenu):
        module.create_menu()
        item.enable(bool(len(submenu)))


def on_about():
    notify(STRINGS.LABEL_ABOUT, str(NotImplemented), force=True)


def on_blocked(item: gui.MenuItem):
    if item.is_checked():
        check_blocked()


def apply_auto_start(start_: bool) -> bool:
    return win32.register_autorun(
        consts.NAME, *_get_launch_args(), *((consts.ARG_CHANGE,) if CONFIG[consts.CONFIG_INTERVAL] else ()),
        show=pyinstall.FROZEN, uid=UUID) if start_ else win32.unregister_autorun(consts.NAME, UUID)


def apply_save_config(save: bool) -> bool:
    return save_config() if save else files.remove(CONFIG_PATH)


@timer.on_thread
def on_quit():
    TIMER.stop()
    gui.disable_events()
    max_threads = 1 + (threading.current_thread() is not threading.main_thread())
    if threading.active_count() > max_threads:
        gui.animate(STRINGS.STATUS_QUIT).__enter__()
        notify(STRINGS.LABEL_QUIT, STRINGS.FAIL_QUIT)
        end_time = time.time() + win32.get_max_shutdown_time()
        while end_time > time.time() and threading.active_count() > max_threads:
            time.sleep(consts.POLL_INTERVAL)
    gui.stop_loop()


def create_menu():  # TODO slideshow (smaller timer)
    item_change = gui.add_menu_item(STRINGS.LABEL_CHANGE)
    item_change.set_default()
    item_change.set_icon(RES_TEMPLATE.format(consts.RES_CHANGE))
    item_recent = gui.add_submenu(STRINGS.MENU_RECENT, False, icon=RES_TEMPLATE.format(consts.RES_RECENT))

    def query_callback(progress: Optional[float] = None) -> bool:
        if progress is None:
            print()
        else:
            print(f'[{utils.get_progress(progress, 1, 32)}]', end='\r', flush=True)
        # item_change.set_text(STRINGS.LABEL_CHANGE if progress is None else TODO fix exploding width
        #                      f'{STRINGS.LABEL_CHANGE} ({langs.to_str(min(99, progress), STRINGS, 2)}%)')
        return True

    TIMER.__init__(0, on_change, (item_change.enable, item_recent, query_callback))
    gui.add_separator(menu=item_recent)
    gui.add_menu_item(STRINGS.LABEL_CLEAR, on_click=on_clear, args=(
        item_recent.enable,), menu=item_recent).set_icon(RES_TEMPLATE.format(consts.RES_CLEAR))
    _update_recent(item_recent)
    gui.set_on_click(item_change, on_change, args=TIMER.args, on_thread=False, change_state=False)
    gui.add_separator()
    item_module = gui.add_submenu('')
    on_module(CONFIG[consts.CONFIG_MODULE], item_module)
    gui.add_separator()
    with gui.set_main_menu(gui.add_submenu(STRINGS.MENU_ACTIONS, icon=RES_TEMPLATE.format(consts.RES_ACTIONS))):
        item_links = gui.add_submenu(STRINGS.MENU_LINKS)
        item_links.set_icon(RES_TEMPLATE.format(consts.RES_LINKS))
        with gui.set_main_menu(item_links):
            gui.add_menu_item(STRINGS.LABEL_DESKTOP, on_click=on_shortcut).set_icon(
                RES_TEMPLATE.format(consts.RES_LINK))
            gui.add_menu_item(STRINGS.LABEL_REMOVE_DESKTOP, on_click=on_remove_shortcuts).set_icon(
                RES_TEMPLATE.format(consts.RES_UNLINK))
            gui.add_separator()
            gui.add_menu_item(STRINGS.LABEL_START_MENU, on_click=on_start_shortcut).set_icon(
                RES_TEMPLATE.format(consts.RES_LINK))
            gui.add_menu_item(STRINGS.LABEL_REMOVE_START_MENU, on_click=on_remove_start_shortcuts).set_icon(
                RES_TEMPLATE.format(consts.RES_UNLINK))
            gui.add_separator()
            gui.add_menu_item(
                STRINGS.LABEL_PIN, enable=pyinstall.FROZEN or consts.FEATURE_PIN_PYTHON, on_click=on_pin).set_icon(
                RES_TEMPLATE.format(consts.RES_PIN))
            gui.add_menu_item(
                STRINGS.LABEL_UNPIN, enable=pyinstall.FROZEN or consts.FEATURE_PIN_PYTHON, on_click=on_unpin).set_icon(
                RES_TEMPLATE.format(consts.RES_UNPIN))
            gui.add_separator()
            item_unpin_start = gui.add_menu_item(
                STRINGS.LABEL_UNPIN_START, enable=pyinstall.FROZEN or consts.FEATURE_PIN_PYTHON, on_click=on_unpin_start)
            item_unpin_start.set_icon(RES_TEMPLATE.format(consts.RES_UNPIN))
            gui.add_menu_item(
                STRINGS.LABEL_PIN_START, enable=pyinstall.FROZEN or consts.FEATURE_PIN_PYTHON, on_click=on_pin_start,
                menu_args=(gui.Method.ENABLE,), args=(item_unpin_start.enable,), change_state=False, position=9).set_icon(
                RES_TEMPLATE.format(consts.RES_PIN))
        gui.add_menu_item(STRINGS.LABEL_CLEAR_CACHE, on_click=on_clear_cache).set_icon(
            RES_TEMPLATE.format(consts.RES_CLEAR_CACHE))
        gui.add_menu_item(STRINGS.LABEL_RESET, on_click=on_reset).set_icon(RES_TEMPLATE.format(consts.RES_RESET))
        gui.add_menu_item(STRINGS.LABEL_RESTART, enable=bool(
            multiprocessing.parent_process()), on_click=on_restart).set_icon(RES_TEMPLATE.format(consts.RES_RESTART))
        gui.add_menu_item(STRINGS.LABEL_ABOUT, on_click=on_about).set_icon(RES_TEMPLATE.format(consts.RES_ABOUT))
    with gui.set_main_menu(gui.add_submenu(STRINGS.MENU_SETTINGS, icon=RES_TEMPLATE.format(consts.RES_SETTINGS))):
        with gui.set_main_menu(gui.add_submenu(STRINGS.MENU_AUTO)):
            gui.add_mapped_submenu(STRINGS.MENU_AUTO_CHANGE, {interval: getattr(
                STRINGS, f'TIME_{interval}') for interval in INTERVALS},
                                   CONFIG, consts.CONFIG_INTERVAL, on_click=on_auto_change)
            gui.add_separator()
            gui.add_mapped_menu_item(STRINGS.LABEL_AUTO_SAVE, CONFIG, consts.CONFIG_AUTOSAVE)
            gui.add_menu_item(STRINGS.LABEL_SAVE_DIR, on_click=on_modify_save)
        gui.add_mapped_submenu(STRINGS.MENU_TRANSITION, {transition: getattr(
            STRINGS, f'TRANSITION_{transition}') for transition in win32.display.Transition}, CONFIG, consts.CONFIG_TRANSITION)
        if consts.FEATURE_ROTATE_IMAGE:
            gui.add_mapped_submenu(STRINGS.MENU_ROTATE, {rotate: getattr(
                STRINGS, f'ROTATE_{rotate}') for rotate in win32.display.Rotate},
                                   CONFIG, consts.CONFIG_ROTATE, on_click=reapply_wallpaper)
        with gui.set_main_menu(gui.add_submenu(STRINGS.MENU_FLIP)):
            item_vertical = gui.add_menu_item(STRINGS.FLIP_VERTICAL, gui.MenuItemType.CHECK, getattr(
                win32.display.Flip, CONFIG[consts.CONFIG_FLIP]) in (win32.display.Flip.VERTICAL, win32.display.Flip.BOTH))
            item_horizontal = gui.add_menu_item(STRINGS.FLIP_HORIZONTAL, gui.MenuItemType.CHECK, getattr(
                win32.display.Flip, CONFIG[consts.CONFIG_FLIP]) in (win32.display.Flip.HORIZONTAL, win32.display.Flip.BOTH))
            gui.set_on_click(item_vertical, on_flip, args=(item_vertical, item_horizontal))
            gui.set_on_click(item_horizontal, on_flip, args=(item_vertical, item_horizontal))
        gui.add_mapped_submenu(STRINGS.MENU_ALIGNMENT, {style: getattr(
            STRINGS, f'ALIGNMENT_{style}') for style in win32.display.Style},
                               CONFIG, consts.CONFIG_STYLE, on_click=reapply_wallpaper)
        gui.add_mapped_submenu(STRINGS.MENU_MODULE,
                               {name: f'{name}\t{module.VERSION}' for name, module in modules.MODULES.items()},
                               CONFIG, consts.CONFIG_MODULE, on_click=on_module, args=(item_module,))
        item_display = gui.add_submenu(STRINGS.MENU_DISPLAY)
        gui.GUI.bind(gui.GuiEvent.DISPLAY_CHANGE, on_display_change, (item_display,))
        on_display_change(0, None, item_display)
        gui.add_separator()
        gui.add_mapped_menu_item(STRINGS.LABEL_ANIMATE, CONFIG, consts.CONFIG_ANIMATE, on_click=gui.enable_animation)
        gui.add_mapped_menu_item(STRINGS.LABEL_NOTIFY, CONFIG, consts.CONFIG_NOTIFY)
        item_blocked = gui.add_mapped_menu_item(STRINGS.LABEL_BLOCKED, CONFIG, consts.CONFIG_BLOCKED)
        gui.set_on_click(item_blocked, on_blocked, args=(item_blocked,))
        gui.add_mapped_menu_item(STRINGS.LABEL_SKIP, CONFIG, consts.CONFIG_SKIP)
        gui.add_mapped_menu_item(STRINGS.LABEL_REAPPLY, CONFIG, consts.CONFIG_REAPPLY)
        gui.add_mapped_menu_item(STRINGS.LABEL_CACHE, CONFIG, consts.CONFIG_CACHE)
        gui.add_mapped_menu_item(STRINGS.LABEL_START, CONFIG, consts.CONFIG_START)
        gui.add_mapped_menu_item(STRINGS.LABEL_CONFIG, CONFIG, consts.CONFIG_SAVE)
    gui.add_menu_item(STRINGS.LABEL_QUIT, on_click=on_quit, on_thread=False).set_icon(RES_TEMPLATE.format(consts.RES_QUIT))


def start():  # TODO dark theme
    singleton.init(UUID, consts.NAME, consts.ARG_WAIT in sys.argv, on_crash=print, on_crash_args=('Crash',),
                   on_wait=print, on_wait_args=('Wait',), on_exit=print, on_exit_args=('Exit',))
    if consts.ARG_DEBUG in sys.argv:
        log.redirect_stdout(LOG_PATH, True) if pyinstall.FROZEN else log.write_on_exception(LOG_PATH)
        log.init(os.path.basename(__file__), utils.re_join('libs', r'.*\.py'), utils.re_join(
            'modules', r'.*\.py'), utils.re_join('win32', r'.*\.py'), level=log.Level.INFO, check_comp=False)
    pyinstall.clean_temp()
    files.make_dir(TEMP_DIR)
    files.trim_dir(TEMP_DIR, consts.MAX_CACHE)
    _update_display()
    load_config()
    RECENT.extend(utils.decrypt(CONFIG[consts.CONFIG_RECENT], ()))
    gui.init(consts.NAME)
    first_run()
    create_menu()
    gui.enable_animation(CONFIG[consts.CONFIG_ANIMATE])
    apply_auto_start(CONFIG[consts.CONFIG_START])
    apply_save_config(CONFIG[consts.CONFIG_SAVE])
    change_after = CONFIG[consts.CONFIG_INTERVAL] + CONFIG[consts.CONFIG_LAST] - time.time()
    if consts.ARG_CHANGE in sys.argv or (CONFIG[consts.CONFIG_INTERVAL] and change_after <= 0):
        on_change(*TIMER.args, auto_change=False)
    on_auto_change(CONFIG[consts.CONFIG_INTERVAL], None if change_after <= 0 else change_after)
    gui.start_loop(RES_TEMPLATE.format(consts.RES_TRAY), consts.NAME, on_change, TIMER.args)


def stop():
    timer.Timer.kill_all()
    apply_auto_start(CONFIG[consts.CONFIG_START])
    apply_save_config(CONFIG[consts.CONFIG_SAVE])
    files.trim_dir(TEMP_DIR, consts.MAX_CACHE) if CONFIG[consts.CONFIG_CACHE] else files.remove(TEMP_DIR, True)
    if os.path.isdir(TEMP_DIR) and files.is_only_dirs(TEMP_DIR, True):
        files.remove(TEMP_DIR, True)


def main() -> NoReturn:
    print('Start')
    start()
    stop()
    print('Stop')
    sys.exit(consts.EX_TEMPFAIL * RESTART.is_set())


if __name__ == '__main__':
    main()
