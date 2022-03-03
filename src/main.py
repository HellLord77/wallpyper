__version__ = '0.1.13'  # TODO 0xC0000409 (STATUS_STACK_BUFFER_OVERRUN)
__author__ = 'HellLord'

import atexit
import collections
import configparser
import contextlib
import copy
import functools
import math
import subprocess
import sys
import tempfile
import threading
import time
import webbrowser
from typing import Any, Callable, Iterable, Mapping, NoReturn, Optional, Union

import langs
import libs.functool as functool
import libs.log as log
import libs.paths as paths
import libs.pyinstall as pyinstall
import libs.request as request
import libs.singleton as singleton
import utils
import win32
from modules import bing, wallhaven  # TODO lazy

FEATURE_PIN_PYTHON = False
FEATURE_UPLOAD_GOOGLE = True
FEATURE_OPEN_WITH = False
FEATURE_UPDATE_DISPLAY = True

MAX_CACHE = 64 * 1024 * 1024
MAX_RECENT = 9
POLL_TIMEOUT = 0.01
MAX_LABEL = 25

NAME = 'Wallpyper'
ARG_CHANGE = 'change'
ARG_DEBUG = 'debug'
ARG_WAIT = 'wait'
CONFIG_LAST = '_last_changed'
CONFIG_RECENT = '_recent_list'
CONFIG_TRANSITION = 'wallpaper_transition'
CONFIG_DISPLAY = 'selected_display'
CONFIG_CHANGE = 'auto_change'
CONFIG_AUTOSAVE = 'auto_save'
CONFIG_DIR = 'save_dir'
CONFIG_SKIP = 'skip_recent'
CONFIG_NOTIFY = 'notify_errors'
CONFIG_ANIMATE = 'animate_icon'
CONFIG_CACHE = 'image_cache'
CONFIG_START = 'auto_start'
CONFIG_SAVE = 'save_settings'

EXIT_TIMEOUT = win32.get_max_shutdown_time()
UUID = f'{__author__}.{NAME}'
SHORTCUT_NAME = f'{NAME}{win32.LINK_EXT}'
RES_ICON, RES_TRAY, RES_BUSY = (utils.join_path(utils.get_dir(__file__), 'resources', name)
                                for name in ('icon.ico', 'tray.png', 'busy.gif'))
TEMP_DIR = paths.join(tempfile.gettempdir(), NAME)
INI_PATH = fr'D:\Projects\Wallpyper\{NAME}.ini'  # TODO paths.join(win32.SAVE_DIR, NAME, f'{NAME}.ini')
LOG_PATH = paths.replace_ext(INI_PATH, 'log')
GOOGLE_URL = request.join('https://www.google.com', 'searchbyimage')
GOOGLE_UPLOAD_URL = request.join(GOOGLE_URL, 'upload')
BING_URL = request.join('https://www.bing.com', 'images', 'search')
INTERVALS = 0, 300, 900, 1800, 3600, 10800, 21600
MODULES = bing, wallhaven,

CONFIG = {}
DISPLAYS = []
RECENT: collections.deque[utils.Wallpaper] = collections.deque(maxlen=MAX_RECENT)
TIMER = utils.Timer.__new__(utils.Timer)

STRINGS = langs.LANGUAGE = langs.en
MODULE = MODULES[0]
DEFAULT_CONFIG = utils.Dict({
    CONFIG_LAST: math.inf,
    CONFIG_RECENT: functool.encrypt(RECENT, True),
    CONFIG_TRANSITION: win32.wallpaper.Transition[win32.wallpaper.Transition.RANDOM],
    CONFIG_DISPLAY: '',
    CONFIG_CHANGE: INTERVALS[0],
    CONFIG_AUTOSAVE: False,
    CONFIG_DIR: utils.join_path(win32.PICTURES_DIR, NAME),
    CONFIG_SKIP: False,
    CONFIG_NOTIFY: True,
    CONFIG_ANIMATE: True,
    CONFIG_CACHE: False,
    CONFIG_START: False,
    CONFIG_SAVE: False
})


def fix_config(loaded: bool = True):
    if CONFIG[CONFIG_TRANSITION] not in win32.wallpaper.Transition:
        CONFIG[CONFIG_TRANSITION] = DEFAULT_CONFIG[CONFIG_TRANSITION]
    if loaded:
        CONFIG[CONFIG_RECENT] = functool.encrypt(RECENT, True)
    if CONFIG[CONFIG_DISPLAY] not in DISPLAYS:
        CONFIG[CONFIG_DISPLAY] = DEFAULT_CONFIG[CONFIG_DISPLAY]
    if CONFIG[CONFIG_LAST] > time.time():
        CONFIG[CONFIG_LAST] = DEFAULT_CONFIG[CONFIG_LAST]
    if CONFIG[CONFIG_CHANGE] not in INTERVALS:
        CONFIG[CONFIG_CHANGE] = DEFAULT_CONFIG[CONFIG_CHANGE]
    if not CONFIG[CONFIG_DIR]:  # TODO: is_path_exists_or_creatable
        CONFIG[CONFIG_DIR] = DEFAULT_CONFIG[CONFIG_DIR]


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
        converters={tuple.__name__: functool.to_tuple, list.__name__: functool.to_list,
                    set.__name__: functool.to_set, dict.__name__: functool.to_dict})
    try:
        loaded = bool(parser.read(INI_PATH))
    except configparser.MissingSectionHeaderError:
        loaded = False
    getters = {str: parser.get, int: parser.getint, float: parser.getfloat, bool: parser.getboolean,
               tuple: parser.gettuple, list: parser.getlist, set: parser.getset, dict: parser.getdict}
    loaded = _load_config(getters, NAME, CONFIG, DEFAULT_CONFIG) and loaded
    fix_config(False)
    for module in MODULES:
        loaded = _load_config(getters, module.NAME, module.CONFIG, module.DEFAULT_CONFIG) and loaded
        module.fix_config()
    return loaded


def _strip_config(config: dict[str, Any], default: dict[str, Any]) -> dict[str, Any]:
    stripped = {}
    for option, value in sorted(default.items()):
        if config[option] != value:
            stripped[option] = config[option]
    return stripped


def save_config() -> bool:  # TODO save module generator to restore upon restart (?)
    parser = configparser.ConfigParser()
    fix_config()
    parser[NAME] = _strip_config(CONFIG, DEFAULT_CONFIG)
    for module in MODULES:
        module.fix_config()
        parser[module.NAME] = _strip_config(module.CONFIG, module.DEFAULT_CONFIG)
    with open(INI_PATH, 'w') as file:
        parser.write(file)
    return utils.path_exists(INI_PATH)


@functools.lru_cache
def _download_lock(_: str) -> threading.Lock:
    return threading.Lock()


def download_wallpaper(wallpaper: utils.Wallpaper, progress_callback: Optional[Callable[[int, ...], Any]] = None,
                       args: Optional[Iterable] = None, kwargs: Optional[Mapping[str, Any]] = None) -> Optional[str]:
    temp_path = utils.join_path(TEMP_DIR, wallpaper.name)
    with _download_lock(wallpaper.url):
        utils.animate(RES_BUSY, STRINGS.STATUS_DOWNLOAD)
        try:
            return temp_path if request.download(wallpaper.url, temp_path,
                                                 wallpaper.size, wallpaper.md5, chunk_count=100,
                                                 on_write=progress_callback, args=args, kwargs=kwargs) else None
        finally:
            utils.inanimate(STRINGS.STATUS_DOWNLOAD)


@utils.single
def change_wallpaper(wallpaper: Optional[utils.Wallpaper] = None,
                     progress_callback: Optional[Callable[[int, ...], Any]] = None,
                     args: Optional[Iterable] = None, kwargs: Optional[Mapping[str, Any]] = None) -> bool:
    changed = False
    if progress_callback:
        progress_callback(0, *() if args is None else args, **{} if kwargs is None else kwargs)
    if not wallpaper:
        while (wallpaper := MODULE.get_next_wallpaper()) and CONFIG[CONFIG_SKIP] and wallpaper in RECENT:
            pass
    if wallpaper:
        with contextlib.suppress(ValueError):
            RECENT.remove(wallpaper)
        RECENT.appendleft(wallpaper)
        wallpaper.name = win32.sanitize_filename(wallpaper.name)
        if path := download_wallpaper(wallpaper, progress_callback, args, kwargs):
            changed = win32.wallpaper.set(
                path, *(CONFIG[CONFIG_DISPLAY],) if CONFIG[CONFIG_DISPLAY] else DISPLAYS,
                transition=getattr(win32.wallpaper.Transition, CONFIG[CONFIG_TRANSITION]))
    if progress_callback:
        progress_callback(100, *() if args is None else args, **{} if kwargs is None else kwargs)
    return changed


@utils.single
def save_wallpaper(path: str) -> bool:
    return utils.copy_file(path, utils.join_path(CONFIG[CONFIG_DIR], utils.get_filename(path)))


@utils.single
def search_wallpaper(path: str) -> bool:
    searched = False
    utils.animate(RES_BUSY, STRINGS.STATUS_SEARCH)
    if location := utils.upload_url(GOOGLE_UPLOAD_URL, files={'encoded_image': (None, path)},
                                    redirect=False).get_header('location'):
        searched = webbrowser.open(location)
    utils.inanimate(STRINGS.STATUS_SEARCH)
    return searched


def on_open_url(url: str) -> bool:
    if not (opened := webbrowser.open(url)):
        utils.notify(STRINGS.LABEL_OPEN_BROWSER, STRINGS.FAIL_OPEN_BROWSER)
    return opened


def on_copy_url(url: str) -> bool:
    if not (copied := win32.copy_text(url)):
        utils.notify(STRINGS.LABEL_COPY_URL, STRINGS.FAIL_COPY_URL)
    return copied


def on_google(url: str) -> bool:
    if not (opened := webbrowser.open(request.encode(GOOGLE_URL, {'image_url': url}))) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(STRINGS.LABEL_SEARCH, STRINGS.FAIL_SEARCH)
    return opened


def on_bing(url: str) -> bool:
    if not (opened := webbrowser.open(request.encode(
            BING_URL, {'view': 'detailv2', 'iss': 'sbi', 'q': f'imgurl:{url}'}))) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(STRINGS.LABEL_SEARCH, STRINGS.FAIL_SEARCH)
    return opened


@utils.thread
def on_change(enable: Callable, menu_recent, set_label: Callable,
              wallpaper: Optional[utils.Wallpaper] = None, auto_change: bool = True) -> bool:
    changed = False
    if not change_wallpaper.is_running():
        enable(False)
        menu_recent.Enable(False)
        utils.animate(RES_BUSY, STRINGS.STATUS_CHANGE)
        if auto_change:
            on_auto_change(CONFIG[CONFIG_CHANGE])
        CONFIG[CONFIG_LAST] = time.time()
        if changed := change_wallpaper(wallpaper, set_label):
            if CONFIG[CONFIG_AUTOSAVE]:
                on_click(save_wallpaper, utils.join_path(TEMP_DIR, RECENT[0].name),
                         STRINGS.LABEL_SAVE, STRINGS.FAIL_SAVE)
        set_label()
        utils.inanimate(STRINGS.STATUS_CHANGE)
        _update_recent(menu_recent)
        enable()
    if not changed and CONFIG[CONFIG_NOTIFY]:
        utils.notify(STRINGS.LABEL_CHANGE, STRINGS.FAIL_CHANGE)
    return changed


def on_click(callback: Callable[[str], bool], wallpaper: Union[str, utils.Wallpaper], title: str, text: str) -> bool:
    success = False
    try:
        # noinspection PyUnresolvedReferences
        running = callback.is_running()
    except AttributeError:
        running = False
    if not running:
        if path := wallpaper if isinstance(wallpaper, str) else download_wallpaper(wallpaper):
            with contextlib.suppress(BaseException):
                success = callback(path)
    if not success and CONFIG[CONFIG_NOTIFY]:
        utils.notify(title, text)
    return success


def _update_recent(menu):  # TODO smart
    utils.clear_menu(menu)
    for index, wallpaper in enumerate(RECENT, 1):
        menu_wallpaper = utils.add_menu(
            f'{langs.to_str(index, STRINGS)}. {functool.shrink_string_end(wallpaper.name, MAX_LABEL)}', menu=menu)
        utils.add_item(STRINGS.LABEL_SET, on_click=on_change, args=(*TIMER.args, wallpaper),
                       on_thread=False, change_state=False, menu=menu_wallpaper)
        utils.add_item(STRINGS.LABEL_SET_LOCK, on_click=on_click,
                       args=(win32.wallpaper.set_lock, wallpaper, STRINGS.LABEL_SET_LOCK, STRINGS.FAIL_CHANGE_LOCK),
                       menu=menu_wallpaper)
        utils.add_item(STRINGS.LABEL_SAVE, on_click=on_click,
                       args=(save_wallpaper, wallpaper, STRINGS.LABEL_SAVE, STRINGS.FAIL_SAVE), menu=menu_wallpaper)
        utils.add_separator(menu_wallpaper)
        utils.add_item(STRINGS.LABEL_OPEN_BROWSER, on_click=on_open_url, args=(wallpaper.url,), menu=menu_wallpaper)
        utils.add_item(STRINGS.LABEL_OPEN_EXPLORER, on_click=on_click, args=(
            win32.open_file_path, wallpaper, STRINGS.LABEL_OPEN_EXPLORER, STRINGS.FAIL_OPEN_EXPLORER,),
                       menu=menu_wallpaper)
        utils.add_item(STRINGS.LABEL_OPEN, on_click=on_click,
                       args=(win32.open_file, wallpaper, STRINGS.LABEL_OPEN, STRINGS.FAIL_OPEN), menu=menu_wallpaper)
        if FEATURE_OPEN_WITH:
            utils.add_item(STRINGS.LABEL_OPEN_WITH, on_click=on_click,
                           args=(win32.open_file_with_ex, wallpaper, STRINGS.LABEL_OPEN_WITH, STRINGS.FAIL_OPEN_WITH),
                           menu=menu_wallpaper)
        utils.add_separator(menu_wallpaper)
        utils.add_item(STRINGS.LABEL_COPY_URL, on_click=on_copy_url, args=(wallpaper.url,), menu=menu_wallpaper)
        utils.add_item(STRINGS.LABEL_COPY_PATH, on_click=on_click,
                       args=(win32.copy_text, wallpaper, STRINGS.LABEL_COPY_PATH, STRINGS.FAIL_COPY_PATH),
                       menu=menu_wallpaper)
        utils.add_item(STRINGS.LABEL_COPY, on_click=on_click,
                       args=(win32.copy_image, wallpaper, STRINGS.LABEL_COPY, STRINGS.FAIL_COPY), menu=menu_wallpaper)
        utils.add_separator(menu_wallpaper)
        utils.add_item(STRINGS.LABEL_GOOGLE, on_click=on_google, args=(wallpaper.url,), menu=menu_wallpaper)
        utils.add_item(STRINGS.LABEL_BING, on_click=on_bing, args=(wallpaper.url,), menu=menu_wallpaper)
        if FEATURE_UPLOAD_GOOGLE:
            utils.add_item(STRINGS.LABEL_SEARCH, on_click=on_click,
                           args=(search_wallpaper, wallpaper, STRINGS.LABEL_SEARCH, STRINGS.FAIL_SEARCH,),
                           menu=menu_wallpaper)
    utils.add_separator(menu)
    utils.add_item(STRINGS.LABEL_CLEAR, on_click=on_clear, args=(menu.Enable,), menu=menu)
    menu.Enable(bool(RECENT))


def on_clear(enable: Callable):
    RECENT.clear()
    enable(False)


def on_auto_change(interval: Union[int, str], after: Optional[float] = None):
    CONFIG[CONFIG_CHANGE] = int(interval)
    if CONFIG[CONFIG_CHANGE]:
        TIMER.set_next_interval(CONFIG[CONFIG_CHANGE])
        TIMER.start(after)
    else:
        TIMER.stop()


def on_modify_save() -> bool:
    if path := win32.select_folder(STRINGS.LABEL_SAVE_DIR, CONFIG[CONFIG_DIR]):
        CONFIG[CONFIG_DIR] = path
    elif CONFIG[CONFIG_NOTIFY]:
        utils.notify(STRINGS.LABEL_SAVE_DIR, STRINGS.FAIL_SAVE_DIR)
    return bool(path)


def _update_display():
    DISPLAYS.clear()
    DISPLAYS.extend(win32.wallpaper.get_monitor_ids())


def on_update_display(menu, update: bool = True):
    if update:
        _update_display()
    pad = len(str(len(DISPLAYS)))
    utils.clear_menu(menu)
    utils.add_item(f'{langs.to_str(0, STRINGS, pad)}. {STRINGS.DISPLAY_ALL}',
                   utils.item.RADIO, CONFIG[CONFIG_DISPLAY] == DEFAULT_CONFIG[CONFIG_DISPLAY],
                   uid=DEFAULT_CONFIG[CONFIG_DISPLAY], on_click=CONFIG.__setitem__,
                   menu_args=(utils.get_property.UID,), args=(CONFIG_DISPLAY,), pre_menu_args=False, menu=menu)
    utils.add_synced_items(menu, {
        id_: f'{langs.to_str(index, STRINGS, pad)}. {win32.wallpaper.get_monitor_name(id_) or STRINGS.DISPLAY}'
        for index, id_ in enumerate(DISPLAYS, 1)}, CONFIG, CONFIG_DISPLAY)
    if FEATURE_UPDATE_DISPLAY:
        utils.add_separator(menu)
        utils.add_item(STRINGS.LABEL_UPDATE_DISPLAY, on_click=on_update_display, args=(menu,), menu=menu)
    # TODO: add lock screen


def _get_launch_args() -> list[str]:
    argv = [sys.executable]
    if not pyinstall.FROZEN:
        argv.append(utils.abspath(__file__))
    return argv


def _create_shortcut(dir_: str) -> bool:
    return utils.make_dirs(dir_) and win32.create_shortcut(
        utils.join_path(dir_, SHORTCUT_NAME), *_get_launch_args(),
        icon_path=RES_ICON * (not pyinstall.FROZEN), comment=STRINGS.DESCRIPTION, show=pyinstall.FROZEN, uid=UUID)


def on_shortcut() -> bool:
    if not (created := _create_shortcut(win32.DESKTOP_DIR)) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(STRINGS.LABEL_DESKTOP, STRINGS.FAIL_DESKTOP)
    return created


def on_remove_shortcuts() -> bool:
    if not (removed := win32.remove_shortcuts(win32.DESKTOP_DIR, UUID)) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(STRINGS.LABEL_REMOVE_DESKTOP, STRINGS.FAIL_REMOVE_DESKTOP)
    return removed


def on_start_shortcut() -> bool:
    if not (created := _create_shortcut(utils.join_path(win32.START_DIR, NAME))) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(STRINGS.LABEL_START_MENU, STRINGS.FAIL_START_MENU)
    return created


def on_remove_start_shortcuts() -> bool:
    if not (removed := win32.remove_shortcuts(win32.START_DIR, UUID)) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(STRINGS.LABEL_REMOVE_START_MENU, STRINGS.FAIL_REMOVE_START_MENU)
    return removed


def on_pin() -> bool:
    if not (pinned := win32.add_pin(*_get_launch_args(), name=NAME, icon_path='' if pyinstall.FROZEN else RES_ICON,
                                    show=pyinstall.FROZEN)) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(STRINGS.LABEL_PIN, STRINGS.FAIL_PIN)
    return pinned


def on_unpin() -> bool:
    if not (unpinned := win32.remove_pins(*_get_launch_args())) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(STRINGS.LABEL_UNPIN, STRINGS.FAIL_UNPIN)
    return unpinned


@utils.single
def pin_to_start() -> bool:
    return win32.add_pin(*_get_launch_args(), taskbar=False, name=NAME,
                         icon_path='' if pyinstall.FROZEN else RES_ICON, show=pyinstall.FROZEN)


def on_pin_start(enable: Callable, enable_: Callable) -> bool:
    pinned = False
    if not pin_to_start.is_running():
        enable(False)
        enable_(False)
        pinned = pin_to_start()
        enable_()
        enable()
    if not pinned and CONFIG[CONFIG_NOTIFY]:
        utils.notify(STRINGS.LABEL_PIN_START, STRINGS.FAIL_PIN_START)
    return pinned


def on_unpin_start() -> bool:
    if not (unpinned := win32.remove_pins(*_get_launch_args(), taskbar=False)) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(STRINGS.LABEL_UNPIN_START, STRINGS.FAIL_UNPIN_START)
    return unpinned


def on_clear_cache() -> bool:
    if not (cleared := utils.delete(TEMP_DIR, True)) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(STRINGS.LABEL_CLEAR_CACHE, STRINGS.FAIL_CLEAR)
    return cleared


def on_reset():
    CONFIG[CONFIG_SAVE] = False
    on_restart()


def on_restart():
    args = _get_launch_args()
    args.extend(sys.argv[1:])
    if ARG_WAIT not in args:
        args.append(ARG_WAIT)
    atexit.register(subprocess.Popen, args, creationflags=subprocess.CREATE_NEW_CONSOLE)
    on_quit()


def on_animate(checked: bool):
    CONFIG[CONFIG_ANIMATE] = checked
    utils.pause_animation(not checked)


# noinspection PyShadowingNames
def apply_auto_start(start: bool) -> bool:
    return win32.register_autorun(
        NAME, *_get_launch_args(), *((ARG_CHANGE,) if CONFIG[CONFIG_CHANGE] else ()),
        show=pyinstall.FROZEN, uid=UUID) if start else win32.unregister_autorun(NAME, UUID)


def apply_save_config(save: bool) -> bool:
    return save_config() if save else utils.delete(INI_PATH)


def on_about():
    utils.not_implemented(STRINGS.LABEL_ABOUT)


def _is_running() -> bool:
    return (change_wallpaper.is_running() or save_wallpaper.is_running() or
            search_wallpaper.is_running() or pin_to_start.is_running())


@utils.thread
def on_quit():
    TIMER.stop()
    utils.disable()
    if _is_running():
        if CONFIG[CONFIG_NOTIFY]:
            utils.notify(STRINGS.LABEL_QUIT, STRINGS.FAIL_QUIT)
        end_time = time.time() + EXIT_TIMEOUT
        while end_time > time.time() and _is_running():
            time.sleep(POLL_TIMEOUT)
    utils.stop()


def create_menu():  # TODO slideshow (smaller timer)
    item_change = utils.add_item(STRINGS.LABEL_CHANGE)
    menu_recent = utils.add_menu(STRINGS.MENU_RECENT, False)
    TIMER.__init__(0, on_change, (item_change.Enable, menu_recent, (lambda progress=None: item_change.SetItemLabel(
        STRINGS.LABEL_CHANGE if progress is None else f'{STRINGS.LABEL_CHANGE} '  # TODO exploding width
                                                      f'({langs.to_str(progress, STRINGS, 3)}%)'))))
    _update_recent(menu_recent)
    utils.on_item_click(item_change, on_change, args=TIMER.args, on_thread=False, change_state=False)
    utils.add_separator()
    utils.add_item(f'{MODULE.NAME}-{MODULE.__version__}', enable=False)
    MODULE.create_menu()
    utils.add_separator()
    menu_actions = utils.add_menu(STRINGS.MENU_ACTIONS)
    menu_links = utils.add_menu(STRINGS.MENU_LINKS, menu=menu_actions)
    utils.add_item(STRINGS.LABEL_DESKTOP, on_click=on_shortcut, menu=menu_links)
    utils.add_item(STRINGS.LABEL_REMOVE_DESKTOP, on_click=on_remove_shortcuts, menu=menu_links)
    utils.add_separator(menu_links)
    utils.add_item(STRINGS.LABEL_START_MENU, on_click=on_start_shortcut, menu=menu_links)
    utils.add_item(STRINGS.LABEL_REMOVE_START_MENU, on_click=on_remove_start_shortcuts, menu=menu_links)
    utils.add_separator(menu_links)
    utils.add_item(STRINGS.LABEL_PIN, enable=pyinstall.FROZEN or FEATURE_PIN_PYTHON, on_click=on_pin, menu=menu_links)
    utils.add_item(STRINGS.LABEL_UNPIN, enable=pyinstall.FROZEN or FEATURE_PIN_PYTHON, on_click=on_unpin,
                   menu=menu_links)
    utils.add_separator(menu_links)
    unpin = utils.add_item(STRINGS.LABEL_UNPIN_START, enable=pyinstall.FROZEN or FEATURE_PIN_PYTHON,
                           on_click=on_unpin_start, menu=menu_links)
    utils.add_item(STRINGS.LABEL_PIN_START, enable=pyinstall.FROZEN or FEATURE_PIN_PYTHON,
                   on_click=on_pin_start, menu_args=(utils.set_property.ENABLE,),
                   args=(unpin.Enable,), change_state=False, position=9, menu=menu_links)
    utils.add_item(STRINGS.LABEL_CLEAR_CACHE, on_click=on_clear_cache, menu=menu_actions)
    utils.add_item(STRINGS.LABEL_RESET, on_click=on_reset, menu=menu_actions)
    utils.add_item(STRINGS.LABEL_RESTART, on_click=on_restart, menu=menu_actions)
    utils.add_item(STRINGS.LABEL_ABOUT, on_click=on_about, menu=menu_actions)
    menu_auto = utils.add_menu(STRINGS.MENU_AUTO)
    menu_auto_change = utils.add_menu(STRINGS.MENU_AUTO_CHANGE, menu=menu_auto)
    for interval in INTERVALS:
        utils.add_item(getattr(STRINGS, f'TIME_{interval}'), utils.item.RADIO,
                       CONFIG[CONFIG_CHANGE] == interval, uid=str(interval),
                       on_click=on_auto_change, menu_args=(utils.get_property.UID,), menu=menu_auto_change)
    utils.add_separator(menu_auto)
    utils.add_synced_item(STRINGS.LABEL_AUTO_SAVE, CONFIG, CONFIG_AUTOSAVE, menu_auto)
    utils.add_item(STRINGS.LABEL_SAVE_DIR, on_click=on_modify_save, menu=menu_auto)
    menu_settings = utils.add_menu(STRINGS.MENU_SETTINGS)
    utils.add_synced_items(STRINGS.MENU_TRANSITION, {
        str(transition): getattr(STRINGS, f'TRANSITION_{transition}')
        for transition in win32.wallpaper.Transition}, CONFIG, CONFIG_TRANSITION, menu=menu_settings)
    menu_display = utils.add_menu(STRINGS.MENU_DISPLAY, menu=menu_settings)
    on_update_display(menu_display, False)
    utils.add_synced_item(STRINGS.LABEL_SKIP, CONFIG, CONFIG_SKIP, menu_settings)
    utils.add_synced_item(STRINGS.LABEL_NOTIFY, CONFIG, CONFIG_NOTIFY, menu_settings)
    utils.add_item(STRINGS.LABEL_ANIMATE, utils.item.CHECK, CONFIG[CONFIG_ANIMATE],
                   on_click=on_animate, menu_args=(utils.get_property.CHECKED,), menu=menu_settings)
    utils.add_synced_item(STRINGS.LABEL_CACHE, CONFIG, CONFIG_CACHE, menu_settings)
    utils.add_synced_item(STRINGS.LABEL_START, CONFIG, CONFIG_START, menu_settings)
    utils.add_synced_item(STRINGS.LABEL_CONFIG, CONFIG, CONFIG_SAVE, menu_settings)
    utils.add_item(STRINGS.LABEL_QUIT, on_click=on_quit, on_thread=False)


def start():  # TODO dark theme
    singleton.init(UUID, NAME, ARG_WAIT in sys.argv, on_crash=print, on_crash_args=('Crash',),
                   on_wait=print, on_wait_args=('Wait',), on_exit=print, on_exit_args=('Exit',))
    if ARG_DEBUG in sys.argv:
        log.redirect_stdout(LOG_PATH, True) if pyinstall.FROZEN else log.write_on_exception(LOG_PATH)
        log.init(utils.get_filename(__file__), utils.get_filename(utils.__file__),
                 utils.re_join_path('libs', r'.*\.py'), utils.re_join_path('modules', r'.*\.py'),
                 utils.re_join_path('win32s', r'.*\.py'), level=log.Level.INFO, check_comp=False)
    pyinstall.clean_temp()
    utils.make_dirs(TEMP_DIR)
    utils.trim_dir(TEMP_DIR, MAX_CACHE)
    _update_display()
    load_config()
    RECENT.extend({wallpaper: None for wallpaper in functool.decrypt(CONFIG[CONFIG_RECENT], ())})
    create_menu()
    on_animate(CONFIG[CONFIG_ANIMATE])
    apply_auto_start(CONFIG[CONFIG_START])
    apply_save_config(CONFIG[CONFIG_SAVE])
    after = CONFIG[CONFIG_CHANGE] + CONFIG[CONFIG_LAST] - time.time()
    if ARG_CHANGE in sys.argv or (CONFIG[CONFIG_CHANGE] and after <= 0):
        # noinspection PyTypeChecker
        on_change(*TIMER.args, False)
    on_auto_change(CONFIG[CONFIG_CHANGE], None if after <= 0 else after)
    utils.start(RES_TRAY, NAME, on_change, TIMER.args)


def stop():
    utils.Timer.kill_all()
    apply_auto_start(CONFIG[CONFIG_START])
    apply_save_config(CONFIG[CONFIG_SAVE])
    utils.trim_dir(TEMP_DIR, MAX_CACHE) if CONFIG[CONFIG_CACHE] else utils.delete(TEMP_DIR, True)
    if utils.dir_exists(TEMP_DIR) and utils.is_empty_dir(TEMP_DIR, True):
        utils.delete(TEMP_DIR, True)


def main() -> NoReturn:
    start()
    stop()
    sys.exit()


if __name__ == '__main__':
    main()
