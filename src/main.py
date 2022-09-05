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
import sysconfig
import tempfile
import threading
import time
import traceback
import uuid
import webbrowser
from typing import Any, Callable, Iterable, Mapping, NoReturn, Optional

import consts
import gui
import langs
import libs.files as files
import libs.log as log
import libs.pyinstall as pyinstall
import libs.request as request
import libs.singleton as singleton
import libs.spinners as spinners
import libs.timer as timer
import libs.utils as utils
import modules
import pipe
import win32

ALL_DISPLAY = 'DISPLAY'
UUID = f'{consts.AUTHOR}.{consts.NAME}'
RES_TEMPLATE = os.path.join(os.path.dirname(__file__), 'res', '{}')
gui.ANIMATION_PATH = RES_TEMPLATE.format(consts.RES_BUSY)
CONFIG_PATH = fr'D:\Projects\Wallpyper\{consts.NAME}.ini'
# CONFIG_PATH = os.path.join(win32.SAVE_DIR, f'{consts.NAME}.ini')  # TODO
LOG_PATH = files.replace_ext(CONFIG_PATH, 'log')
PIPE_PATH = files.replace_ext(pipe.__file__.removesuffix(sysconfig.get_config_var('EXT_SUFFIX')), 'exe')
TEMP_DIR = win32.display.TEMP_WALLPAPER_DIR = os.path.join(tempfile.gettempdir(), consts.NAME)
GOOGLE_URL = request.join('https://www.google.com', 'searchbyimage')
GOOGLE_UPLOAD_URL = request.join(GOOGLE_URL, 'upload')
BING_URL = request.join('https://www.bing.com', 'images', 'search')

win32.gui.FLAG_MENU_ITEM_IMAGE_CACHE = True
INTERVALS = 0, 300, 900, 1800, 3600, 10800, 21600
MAXIMIZED_ACTIONS = '', 'POSTPONE', 'CANCEL'
STRINGS = langs.eng
DISPLAYS: dict[str, tuple[str, tuple[int, int]]] = {}
RESTART = threading.Event()
TIMER = timer.Timer.__new__(timer.Timer)
PROGRESS = utils.MutableFloat()
RECENT: collections.deque[files.File] = collections.deque(maxlen=consts.MAX_RECENT_LEN)
PIPE: pipe.StringNamedPipeClient = pipe.StringNamedPipeClient(f'{UUID}_{uuid.uuid4().hex}', True)

DEFAULT_CONFIG = {
    consts.CONFIG_LAST: math.inf,
    consts.CONFIG_RECENT: f'\n{utils.encrypt(RECENT, split=True)}',
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
    consts.CONFIG_MAXIMIZED: MAXIMIZED_ACTIONS[0],
    consts.CONFIG_COLOR: win32.ColorMode.AUTO,
    consts.CONFIG_MODULE: next(iter(modules.MODULES.values())).__name__,
    consts.CONFIG_DIR: os.path.join(win32.PICTURES_DIR, consts.NAME),
    consts.CONFIG_STYLE: win32.display.Style[win32.display.Style.FILL],
    consts.CONFIG_ROTATE: win32.display.Rotate[win32.display.Rotate.NONE],
    consts.CONFIG_FLIP: win32.display.Flip[win32.display.Flip.NONE],
    consts.CONFIG_TRANSITION: win32.display.Transition[win32.display.Transition.FADE]}
CONFIG = {}


def update_config():
    CONFIG[consts.CONFIG_RECENT] = f'\n{utils.encrypt(RECENT, split=True)}'


def _fix_config(key: str, values: Iterable):
    utils.fix_dict_key(CONFIG, key, values, DEFAULT_CONFIG)


def fix_config():
    _fix_config(consts.CONFIG_STYLE, win32.display.Style)
    _fix_config(consts.CONFIG_ROTATE, win32.display.Rotate)
    _fix_config(consts.CONFIG_FLIP, win32.display.Flip)
    _fix_config(consts.CONFIG_TRANSITION, win32.display.Transition)
    _fix_config(consts.CONFIG_DISPLAY, DISPLAYS)
    if CONFIG[consts.CONFIG_LAST] > time.time():
        CONFIG[consts.CONFIG_LAST] = DEFAULT_CONFIG[consts.CONFIG_LAST]
    _fix_config(consts.CONFIG_INTERVAL, INTERVALS)
    _fix_config(consts.CONFIG_MAXIMIZED, MAXIMIZED_ACTIONS)
    _fix_config(consts.CONFIG_COLOR, (win32.ColorMode[mode] for mode in win32.ColorMode[1:]))
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
    for name, module in ({consts.NAME: sys.modules[__name__]} | modules.MODULES).items():
        loaded = _load_config(getters, name, module.CONFIG, module.DEFAULT_CONFIG) and loaded
        module.fix_config()
    return loaded


def save_config() -> bool:  # TODO save module generator to restore upon restart (?)
    parser = configparser.ConfigParser()
    for name, module in ({consts.NAME: sys.modules[__name__]} | modules.MODULES).items():
        module.update_config()
        module.fix_config()
        parser[name] = {option: module.CONFIG[option] for option, value in sorted(
            module.DEFAULT_CONFIG.items()) if module.CONFIG[option] != value}
    with open(CONFIG_PATH, 'w') as file:
        parser.write(file)
    return os.path.isfile(CONFIG_PATH)


def notify(title: str, text: str, icon: int | str = win32.gui.SystemTrayIcon.BALLOON_NONE, force: bool = False) -> bool:
    if force or CONFIG[consts.CONFIG_NOTIFY]:
        return gui.SYSTEM_TRAY.show_balloon(title, utils.shrink_string(text, consts.MAX_NOTIFY_LEN), icon)
    return False


def reapply_wallpaper(_: Optional[bool]):
    if CONFIG[consts.CONFIG_REAPPLY] and RECENT:
        on_change(*TIMER.args, RECENT[0], False)


@timer.on_thread
def on_shown(*_):
    if CONFIG[consts.CONFIG_FIRST]:
        CONFIG[consts.CONFIG_FIRST] = not notify(
            STRINGS.FIRST_TITLE, STRINGS.FIRST_TEXT, RES_TEMPLATE.format(consts.RES_ICON), True)
    if CONFIG[consts.CONFIG_BLOCKED]:
        time.sleep(consts.POLL_SLO_INTERVAL)
        check_blocked()


def get_displays() -> Iterable[str]:
    _fix_config(consts.CONFIG_DISPLAY, DISPLAYS)
    return DISPLAYS if CONFIG[consts.CONFIG_DISPLAY] == ALL_DISPLAY else (CONFIG[consts.CONFIG_DISPLAY],)


@timer.on_thread
def check_blocked(*_):
    if not CONFIG[consts.CONFIG_FIRST] and CONFIG[consts.CONFIG_BLOCKED]:
        displays = get_displays()
        if not all(win32.display.is_desktop_unblocked(*displays).values()):
            count = itertools.count(1)
            text = '\n'.join(f'{langs.to_str(next(count), STRINGS)}. {_get_monitor_name(monitor, DISPLAYS)}'
                             f'{f": {os.path.basename(blocker[1])}" if consts.FEATURE_BLOCKED_NAME else ""}'
                             for monitor, blocker in win32.display.get_desktop_blocker(*displays).items() if blocker is not None)
            notify(STRINGS.BLOCKED_TITLE, text, force=True)


@timer.on_thread
def print_progress():
    if win32.console.is_present() or PIPE:
        interval, spinner = spinners.get(spinners.Spinner.SAND)
        while (progress := PROGRESS.get()) != -1:
            print(f'[{next(spinner)}] [{utils.get_progress(progress, 1, 32)}] {progress * 100:3.0f}%', end='\r', flush=True)
            time.sleep(interval)
        print(f'[#] [{utils.get_progress(100, 1, 32)}] 100%')


_download_lock = functools.lru_cache(lambda _: threading.Lock())


def download_wallpaper(wallpaper: files.File, query_callback: Optional[Callable[[float, ...], bool]] = None,
                       args: Optional[Iterable] = None, kwargs: Optional[Mapping[str, Any]] = None) -> Optional[str]:
    temp_path = os.path.join(TEMP_DIR, wallpaper.name)
    with _download_lock(wallpaper.url), gui.animate(STRINGS.STATUS_DOWNLOAD):
        print_progress()
        try:
            if request.download(wallpaper.url, temp_path, wallpaper.size, wallpaper.md5, wallpaper.sha256,
                                chunk_count=100, query_callback=query_callback, args=args, kwargs=kwargs):
                return temp_path
        finally:
            PROGRESS.set(-1.0)


def get_next_wallpaper() -> Optional[files.File]:
    module = modules.MODULES[CONFIG[consts.CONFIG_MODULE]]
    params = {key: val for key, val in module.CONFIG.items() if not key.startswith('_')}
    first_wallpaper = None
    while True:
        next_wallpaper = next(module.get_next_wallpaper(**params))
        if not CONFIG[consts.CONFIG_SKIP] or next_wallpaper not in RECENT:
            if first_wallpaper != next_wallpaper:
                return next_wallpaper
            break
        if first_wallpaper is None:
            first_wallpaper = next_wallpaper


@utils.SingletonCallable
def change_wallpaper(wallpaper: Optional[files.File] = None, query_callback: Optional[Callable[[float, ...], bool]] = None,
                     args: Optional[Iterable] = None, kwargs: Optional[Mapping[str, Any]] = None) -> bool:
    changed = False
    if wallpaper is None:
        with gui.animate(STRINGS.STATUS_FETCH):
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
                    win32.display.Transition, CONFIG[consts.CONFIG_TRANSITION])) for display in get_displays()))
    return changed


@utils.SingletonCallable
def save_wallpaper(path: str) -> bool:
    return files.copy(path, os.path.join(CONFIG[consts.CONFIG_DIR], os.path.basename(path)))


@utils.SingletonCallable
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
def on_change(item_change_enable: Callable, item_recent: win32.gui.MenuItem, query_callback: Callable[[float], bool],
              wallpaper: Optional[files.File] = None, auto_change: bool = True) -> bool:
    changed = False
    if auto_change:
        if CONFIG[consts.CONFIG_MAXIMIZED] and all(win32.display.get_display_blockers(
                *get_displays(), full_screen_only=True).values()):
            while CONFIG[consts.CONFIG_INTERVAL] and CONFIG[consts.CONFIG_MAXIMIZED] == MAXIMIZED_ACTIONS[1] and all(
                    win32.display.get_display_blockers(*get_displays(), full_screen_only=True).values()):
                time.sleep(consts.POLL_SLO_INTERVAL)
            if not CONFIG[consts.CONFIG_INTERVAL] or CONFIG[consts.CONFIG_MAXIMIZED] == MAXIMIZED_ACTIONS[2]:
                changed = True
        on_auto_change(CONFIG[consts.CONFIG_INTERVAL])
    if not changed and not change_wallpaper.is_running():
        item_change_enable(False)
        item_recent.enable(False)
        with gui.animate(STRINGS.STATUS_CHANGE):
            if auto_change:
                CONFIG[consts.CONFIG_LAST] = time.time()
            if (changed := change_wallpaper(wallpaper, query_callback)) and CONFIG[consts.CONFIG_AUTOSAVE]:
                on_wallpaper(save_wallpaper, RECENT[0], STRINGS.LABEL_SAVE, STRINGS.FAIL_SAVE)
        _update_recent(item_recent)
        item_change_enable()
    if not changed:
        notify(STRINGS.LABEL_CHANGE, STRINGS.FAIL_CHANGE)
    return changed


def on_wallpaper(callback: utils.SingletonCallable[[str], bool], wallpaper: files.File, title: str, text: str) -> bool:
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
            label = f'{langs.to_str(index + 1, STRINGS)}. {utils.shrink_string(wallpaper.name, consts.MAX_LABEL_LEN)}'
            if wallpaper in items:
                wallpaper_item = items[wallpaper.url]
                submenu = wallpaper_item.get_submenu()
                menu.remove_item(wallpaper_item)
            else:
                with gui.set_main_menu(gui.Menu()) as submenu:
                    gui.add_menu_item(STRINGS.LABEL_SET, on_click=on_change, args=(*TIMER.args, wallpaper, False),
                                      on_thread=False, change_state=False).set_icon(RES_TEMPLATE.format(consts.RES_SET))
                    gui.add_menu_item(STRINGS.LABEL_SET_LOCK, on_click=on_wallpaper, args=(
                        win32.display.set_lock_background, wallpaper, STRINGS.LABEL_SET_LOCK, STRINGS.FAIL_CHANGE_LOCK)).set_icon(
                        RES_TEMPLATE.format(consts.RES_SET_LOCK))
                    gui.add_menu_item(STRINGS.LABEL_SAVE, on_click=on_wallpaper, args=(
                        save_wallpaper, wallpaper, STRINGS.LABEL_SAVE, STRINGS.FAIL_SAVE)).set_icon(
                        RES_TEMPLATE.format(consts.RES_SAVE))
                    gui.add_separator()
                    gui.add_menu_item(STRINGS.LABEL_OPEN, on_click=on_wallpaper, args=(
                        win32.open_file, wallpaper, STRINGS.LABEL_OPEN, STRINGS.FAIL_OPEN)).set_icon(
                        RES_TEMPLATE.format(consts.RES_OPEN))
                    if consts.FEATURE_OPEN_WITH:
                        gui.add_menu_item(STRINGS.LABEL_OPEN_WITH, on_click=on_wallpaper, args=(
                            win32.open_file_with_ex, wallpaper, STRINGS.LABEL_OPEN_WITH, STRINGS.FAIL_OPEN_WITH)).set_icon(
                            RES_TEMPLATE.format(consts.RES_OPEN_WITH))
                    gui.add_menu_item(STRINGS.LABEL_OPEN_EXPLORER, on_click=on_wallpaper, args=(
                        win32.open_file_path, wallpaper, STRINGS.LABEL_OPEN_EXPLORER, STRINGS.FAIL_OPEN_EXPLORER,)).set_icon(
                        RES_TEMPLATE.format(consts.RES_OPEN_EXPLORER))
                    gui.add_menu_item(STRINGS.LABEL_OPEN_BROWSER, on_click=on_open_url, args=(wallpaper.url,)).set_icon(
                        RES_TEMPLATE.format(consts.RES_OPEN_BROWSER))
                    gui.add_separator()
                    gui.add_menu_item(STRINGS.LABEL_COPY_PATH, on_click=on_wallpaper, args=(
                        win32.clipboard.copy_text, wallpaper, STRINGS.LABEL_COPY_PATH, STRINGS.FAIL_COPY_PATH)).set_icon(
                        RES_TEMPLATE.format(consts.RES_COPY_PATH))
                    gui.add_menu_item(STRINGS.LABEL_COPY, on_click=on_wallpaper, args=(
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
                        gui.add_menu_item(STRINGS.LABEL_LENS, on_click=on_wallpaper, args=(
                            search_wallpaper, wallpaper, STRINGS.LABEL_LENS, STRINGS.FAIL_SEARCH,)).set_icon(
                            RES_TEMPLATE.format(consts.RES_LENS))
            wallpaper_item = menu.insert_item(index, label, submenu=submenu)
            wallpaper_item.set_tooltip(wallpaper.url, wallpaper.name, os.path.join(
                TEMP_DIR, wallpaper.name) if consts.FEATURE_TOOLTIP_ICON else gui.MenuItemTooltipIcon.NONE)
            wallpaper_item.set_uid(wallpaper.url)
    for uid, wallpaper_item in items.items():
        if uid and uid not in RECENT:
            menu.remove_item(wallpaper_item)
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


def on_flip(vertical_is_checked: Callable[[], bool], horizontal_is_checked: Callable[[], bool]):
    vertical_checked = vertical_is_checked()
    horizontal_checked = horizontal_is_checked()
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
    DISPLAYS.update(win32.display.get_monitors())


def _get_monitor_name(monitor: str, monitors: dict[str, tuple[str, tuple[int, int]]]) -> str:
    return monitors[monitor][0] or win32.display.get_monitor_name(monitor) or STRINGS.DISPLAY


def on_display_change(update: int, _: Optional[gui.Gui], item: win32.gui.MenuItem):
    if update:
        _update_display()
    submenu = item.get_submenu()
    submenu.clear_items()
    with gui.set_main_menu(submenu):
        size = win32.display.get_display_size()
        gui.add_menu_item(
            f'{langs.to_str(0, STRINGS)}. {STRINGS.DISPLAY_ALL}\t{langs.to_str(size[0], STRINGS)} × {langs.to_str(size[1], STRINGS)}',
            gui.MenuItemType.RADIO, CONFIG[consts.CONFIG_DISPLAY] == DEFAULT_CONFIG[consts.CONFIG_DISPLAY], uid=DEFAULT_CONFIG[consts.CONFIG_DISPLAY],
            on_click=CONFIG.__setitem__, menu_args=(gui.Property.UID,), args=(consts.CONFIG_DISPLAY,), pre_menu_args=False)
        gui.add_mapped_submenu(item, {
            monitor: f'{langs.to_str(index, STRINGS)}. {_get_monitor_name(monitor, DISPLAYS)}'
                     f'\t{langs.to_str(DISPLAYS[monitor][1][0], STRINGS)} × {DISPLAYS[monitor][1][1]}'
            for index, monitor in enumerate(DISPLAYS, 1)}, CONFIG, consts.CONFIG_DISPLAY, on_click=check_blocked)
        enable = len(DISPLAYS) > 1
        for submenu_item in item.get_submenu():
            submenu_item.enable(enable)
        if consts.FEATURE_UPDATE_DISPLAY:
            gui.add_separator()
            gui.add_menu_item(STRINGS.LABEL_UPDATE_DISPLAY, on_click=on_display_change, args=(item,))
    check_blocked()
    # TODO add lock screen


def _create_shortcut(dir_: str) -> bool:
    return files.make_dir(dir_) and win32.create_shortcut(os.path.join(
        dir_, consts.NAME), *pyinstall.get_launch_args(), icon_path=RES_TEMPLATE.format(consts.RES_ICON) * (
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
            *pyinstall.get_launch_args(), name=consts.NAME, icon_path='' if pyinstall.FROZEN else RES_TEMPLATE.format(
                consts.RES_ICON), show=pyinstall.FROZEN)):
        notify(STRINGS.LABEL_PIN, STRINGS.FAIL_PIN)
    return pinned


def on_unpin() -> bool:
    if not (unpinned := win32.remove_pins(*pyinstall.get_launch_args())):
        notify(STRINGS.LABEL_UNPIN, STRINGS.FAIL_UNPIN)
    return unpinned


@utils.SingletonCallable
def pin_to_start() -> bool:
    return win32.add_pin(*pyinstall.get_launch_args(), taskbar=False, name=consts.NAME,
                         icon_path='' if pyinstall.FROZEN else RES_TEMPLATE.format(consts.RES_ICON), show=pyinstall.FROZEN)


def on_pin_start(item_pin_enable: Callable, item_unpin_enable: Callable) -> bool:
    pinned = False
    if not pin_to_start.is_running():
        item_pin_enable(False)
        item_unpin_enable(False)
        pinned = pin_to_start()
        item_unpin_enable()
        item_pin_enable()
    if not pinned:
        notify(STRINGS.LABEL_PIN_START, STRINGS.FAIL_PIN_START)
    return pinned


def on_unpin_start() -> bool:
    if not (unpinned := win32.remove_pins(*pyinstall.get_launch_args(), taskbar=False)):
        notify(STRINGS.LABEL_UNPIN_START, STRINGS.FAIL_UNPIN_START)
    return unpinned


@utils.SingletonCallable
def on_console() -> bool:
    if PIPE:
        if consoled := not PIPE.disconnect():
            notify(STRINGS.LABEL_CONSOLE, STRINGS.FAIL_HIDE_CONSOLE)
    else:
        win32.open_file(PIPE_PATH if pyinstall.FROZEN else sys.executable, *() if pyinstall.FROZEN else (pipe.__file__,), str(PIPE))
        if consoled := PIPE.connect(consts.PIPE_TIMEOUT):
            PIPE.flush()
        else:
            notify(STRINGS.LABEL_CONSOLE, STRINGS.FAIL_SHOW_CONSOLE)
    return consoled


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


def on_blocked(checked: bool):
    if checked:
        check_blocked()


def on_color_mode(mode: str):
    print(mode)


def apply_auto_start(auto_start: bool) -> bool:
    return win32.register_autorun(
        consts.NAME, *pyinstall.get_launch_args(), *((consts.ARG_CHANGE,) if CONFIG[consts.CONFIG_INTERVAL] else ()),
        show=pyinstall.FROZEN, uid=UUID) if auto_start else win32.unregister_autorun(consts.NAME, UUID)


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
            time.sleep(consts.POLL_FST_INTERVAL)
    gui.stop_loop()


def create_menu():  # TODO slideshow (smaller timer)
    item_change = gui.add_menu_item(STRINGS.LABEL_CHANGE)
    item_change.set_default()
    item_change.set_icon(RES_TEMPLATE.format(consts.RES_CHANGE))
    item_recent = gui.add_submenu(STRINGS.MENU_RECENT, False, icon=RES_TEMPLATE.format(consts.RES_RECENT))
    TIMER.__init__(0, on_change, (item_change.enable, item_recent, utils.call_after(PROGRESS.set)(lambda _: True)), once=True)
    gui.set_on_click(item_change, on_change, args=(*TIMER.args, None, False), on_thread=False, change_state=False)
    gui.add_separator(menu=item_recent)
    gui.add_menu_item(STRINGS.LABEL_CLEAR, on_click=on_clear, args=(
        item_recent.enable,), menu=item_recent).set_icon(RES_TEMPLATE.format(consts.RES_CLEAR))
    (timer.on_thread(_update_recent) if consts.FEATURE_THREADED_MENU else _update_recent)(item_recent)
    gui.add_separator()
    item_module = gui.add_submenu('')
    (timer.on_thread(on_module) if consts.FEATURE_THREADED_MENU else on_module)(CONFIG[consts.CONFIG_MODULE], item_module)
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
                STRINGS.LABEL_PIN, enable=consts.FEATURE_SYS_PIN, on_click=on_pin).set_icon(
                RES_TEMPLATE.format(consts.RES_PIN))
            gui.add_menu_item(
                STRINGS.LABEL_UNPIN, enable=consts.FEATURE_SYS_PIN, on_click=on_unpin).set_icon(
                RES_TEMPLATE.format(consts.RES_UNPIN))
            gui.add_separator()
            item_unpin_start = gui.add_menu_item(
                STRINGS.LABEL_UNPIN_START, enable=consts.FEATURE_SYS_PIN, on_click=on_unpin_start)
            item_unpin_start.set_icon(RES_TEMPLATE.format(consts.RES_UNPIN))
            gui.add_menu_item(
                STRINGS.LABEL_PIN_START, enable=consts.FEATURE_SYS_PIN, on_click=on_pin_start,
                menu_args=(gui.Method.ENABLE,), args=(item_unpin_start.enable,), change_state=False, position=9).set_icon(
                RES_TEMPLATE.format(consts.RES_PIN))
        if consts.FEATURE_CONSOLE_VIEW:
            gui.add_menu_item(STRINGS.LABEL_CONSOLE, on_click=on_console).set_icon(RES_TEMPLATE.format(consts.RES_CONSOLE))
        gui.add_menu_item(STRINGS.LABEL_CLEAR_CACHE, on_click=on_clear_cache).set_icon(
            RES_TEMPLATE.format(consts.RES_CLEAR_CACHE))
        gui.add_menu_item(STRINGS.LABEL_RESET, on_click=on_reset).set_icon(RES_TEMPLATE.format(consts.RES_RESET))
        gui.add_menu_item(STRINGS.LABEL_RESTART, enable=bool(
            multiprocessing.parent_process()), on_click=on_restart).set_icon(RES_TEMPLATE.format(consts.RES_RESTART))
        gui.add_menu_item(STRINGS.LABEL_ABOUT, on_click=on_about).set_icon(RES_TEMPLATE.format(consts.RES_ABOUT))
    with gui.set_main_menu(gui.add_submenu(STRINGS.MENU_SETTINGS, icon=RES_TEMPLATE.format(consts.RES_SETTINGS))):
        with gui.set_main_menu(gui.add_submenu(STRINGS.MENU_AUTO, icon=RES_TEMPLATE.format(consts.RES_AUTO))):
            gui.add_mapped_submenu(STRINGS.MENU_AUTO_CHANGE, {interval: getattr(
                STRINGS, f'TIME_{interval}') for interval in INTERVALS}, CONFIG, consts.CONFIG_INTERVAL,
                                   on_click=on_auto_change, icon=RES_TEMPLATE.format(consts.RES_INTERVAL))
            gui.add_mapped_submenu(STRINGS.MENU_IF_MAXIMIZED, {action: getattr(
                STRINGS, f'MAXIMIZED_{action}') for action in MAXIMIZED_ACTIONS}, CONFIG,
                                   consts.CONFIG_MAXIMIZED, icon=RES_TEMPLATE.format(consts.RES_MAXIMIZED))
            gui.add_separator()
            gui.add_mapped_menu_item(STRINGS.LABEL_AUTO_SAVE, CONFIG, consts.CONFIG_AUTOSAVE)
            gui.add_menu_item(STRINGS.LABEL_SAVE_DIR, on_click=on_modify_save).set_icon(RES_TEMPLATE.format(consts.RES_SAVE_DIR))
        gui.add_mapped_submenu(STRINGS.MENU_TRANSITION, {transition: getattr(
            STRINGS, f'TRANSITION_{transition}') for transition in win32.display.Transition}, CONFIG,
                               consts.CONFIG_TRANSITION, icon=RES_TEMPLATE.format(consts.RES_TRANSITION))
        if consts.FEATURE_ROTATE_IMAGE:
            gui.add_mapped_submenu(STRINGS.MENU_ROTATE, {rotate: getattr(
                STRINGS, f'ROTATE_{rotate}') for rotate in win32.display.Rotate},
                                   CONFIG, consts.CONFIG_ROTATE, on_click=reapply_wallpaper)
        with gui.set_main_menu(gui.add_submenu(STRINGS.MENU_FLIP, icon=RES_TEMPLATE.format(consts.RES_FLIP))):
            item_vertical = gui.add_menu_item(STRINGS.FLIP_VERTICAL, gui.MenuItemType.CHECK, getattr(
                win32.display.Flip, CONFIG[consts.CONFIG_FLIP]) in (win32.display.Flip.VERTICAL, win32.display.Flip.BOTH))
            item_horizontal = gui.add_menu_item(STRINGS.FLIP_HORIZONTAL, gui.MenuItemType.CHECK, getattr(
                win32.display.Flip, CONFIG[consts.CONFIG_FLIP]) in (win32.display.Flip.HORIZONTAL, win32.display.Flip.BOTH))
            gui.set_on_click(item_vertical, on_flip, args=(item_vertical.is_checked, item_horizontal.is_checked))
            gui.set_on_click(item_horizontal, on_flip, args=(item_vertical.is_checked, item_horizontal.is_checked))
        gui.add_mapped_submenu(STRINGS.MENU_ALIGNMENT, {style: getattr(
            STRINGS, f'ALIGNMENT_{style}') for style in win32.display.Style}, CONFIG, consts.CONFIG_STYLE,
                               on_click=reapply_wallpaper, icon=RES_TEMPLATE.format(consts.RES_ALIGNMENT))
        gui.add_mapped_submenu(STRINGS.MENU_MODULE, {
            name: f'{name}\t{module.VERSION}' for name, module in modules.MODULES.items()}, CONFIG, consts.CONFIG_MODULE,
                               on_click=on_module, args=(item_module,), icon=RES_TEMPLATE.format(consts.RES_MODULE))
        item_display = gui.add_submenu(STRINGS.MENU_DISPLAY, icon=RES_TEMPLATE.format(consts.RES_DISPLAY))
        gui.GUI.bind(gui.GuiEvent.DISPLAY_CHANGE, on_display_change, (item_display,))
        (timer.on_thread(on_display_change) if consts.FEATURE_THREADED_MENU else on_display_change)(0, None, item_display)
        gui.add_separator()
        with gui.set_main_menu(gui.add_submenu(STRINGS.MENU_NOTIFICATIONS, icon=RES_TEMPLATE.format(consts.RES_NOTIFICATION))):
            gui.add_mapped_menu_item(STRINGS.LABEL_NOTIFY_ERROR, CONFIG, consts.CONFIG_NOTIFY)
            gui.add_mapped_menu_item(STRINGS.LABEL_NOTIFY_BLOCKED, CONFIG, consts.CONFIG_BLOCKED, on_click=on_blocked)
        gui.add_mapped_submenu(STRINGS.MENU_COLORS, {win32.ColorMode[mode]: getattr(
            STRINGS, f'COLOR_MODE_{mode}') for mode in win32.ColorMode[1:]}, CONFIG, consts.CONFIG_COLOR,
                               on_click=win32.set_color_mode, icon=RES_TEMPLATE.format(consts.RES_THEME))
        win32.set_color_mode(CONFIG[consts.CONFIG_COLOR])
        gui.add_mapped_menu_item(STRINGS.LABEL_ANIMATE, CONFIG, consts.CONFIG_ANIMATE, on_click=gui.enable_animation)
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
    files.trim_dir(TEMP_DIR, consts.MAX_CACHE_SZ)
    _update_display()
    load_config()
    sys.modules['files'] = sys.modules['libs.files']  # FIXME https://github.com/cython/cython/issues/3867
    RECENT.extend(utils.decrypt(CONFIG[consts.CONFIG_RECENT], ()))
    gui.init(consts.NAME)
    create_menu()
    gui.enable_animation(CONFIG[consts.CONFIG_ANIMATE])
    apply_auto_start(CONFIG[consts.CONFIG_START])
    apply_save_config(CONFIG[consts.CONFIG_SAVE])
    change_after = CONFIG[consts.CONFIG_INTERVAL] + CONFIG[consts.CONFIG_LAST] - time.time()
    if consts.ARG_CHANGE in sys.argv or (CONFIG[consts.CONFIG_INTERVAL] and change_after <= 0):
        on_change(*TIMER.args)
    else:
        on_auto_change(CONFIG[consts.CONFIG_INTERVAL], None if change_after <= 0 else change_after)
    gui.GUI.bind(gui.GuiEvent.NC_RENDERING_CHANGED, on_shown, once=True)
    gui.start_loop(RES_TEMPLATE.format(consts.RES_TRAY), consts.NAME, on_change, (*TIMER.args, None, False))


def stop():
    timer.Timer.kill_all()
    apply_auto_start(CONFIG[consts.CONFIG_START])
    apply_save_config(CONFIG[consts.CONFIG_SAVE])
    files.trim_dir(TEMP_DIR, consts.MAX_CACHE_SZ) if CONFIG[consts.CONFIG_CACHE] else files.remove(TEMP_DIR, True)
    if os.path.isdir(TEMP_DIR) and files.is_only_dirs(TEMP_DIR, True):
        files.remove(TEMP_DIR, True)
    PIPE.disconnect()


def main() -> NoReturn:
    if consts.FEATURE_EXCEPT_HOOK:
        utils.hook_except(win32.show_error, format=True)
    try:
        start()
        stop()
    except Exception as e:
        if consts.FEATURE_EXCEPT_HOOK and multiprocessing.parent_process():
            thread = threading.Thread(target=win32.show_error, args=(type(
                e), f'Process {multiprocessing.current_process().name}:\n' + ''.join(
                traceback.format_exception(type(e), e, e.__traceback__))))
            thread.start()
        raise
    sys.exit(consts.EX_TEMPFAIL * RESTART.is_set())


if __name__ == '__main__':
    main()
