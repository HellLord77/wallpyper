__version__ = '0.1.12'  # TODO 0xC0000409 (wx?)
__author__ = 'HellLord'

import atexit
import configparser
import copy
import subprocess
import sys
import tempfile
import time
from typing import Any, Callable, Generator, Iterable, Mapping, NoReturn, Optional, Union

import langs
import libs.functool as functool
import libs.log as log
import libs.pyinstall as pyinstall
import libs.singleton as singleton
import modules.wallhaven
import platforms.win32 as platform
import utils

FEATURE_FORCE_PIN = False
FEATURE_CHANGED = False

MAX_CACHE = 64 * 1024 * 1024
POLL_TIMEOUT = 0.01

NAME = 'Wallpyper'
ARG_CHANGE = 'change'
ARG_DEBUG = 'debug'
ARG_WAIT = 'wait'
CONFIG_TRANSITION = 'transition'
CONFIG_DISPLAY = 'display'
CONFIG_AUTO_CHANGE = 'auto_change'
CONFIG_LAST = 'changed_at'
CONFIG_AUTOSAVE = 'auto_save'
CONFIG_DIR = 'save_dir'
CONFIG_NOTIFY = 'notify'
CONFIG_ANIMATE = 'animate_icon'
CONFIG_CACHE = 'keep_cache'
CONFIG_START = 'auto_start'
CONFIG_SAVE = 'save_settings'
UID_DISPLAY = 'display'
UID_PREVIOUS = 'previous'

EXIT_TIMEOUT = platform.get_max_shutdown_time()
UUID = f'{__author__}.{NAME}'
SHORTCUT_NAME = f'{NAME}{platform.LINK_EXT}'
RES_ICON, RES_TRAY, RES_BUSY = (utils.join_path(utils.dir_name(__file__), 'resources', name)
                                for name in ('icon.ico', 'tray.png', 'busy.gif'))
TEMP_DIR = utils.join_path(tempfile.gettempdir(), NAME)
INI_PATH = fr'D:\Projects\Wallpyper\{NAME}.ini'  # TODO utils.join_path(platform.SAVE_DIR, NAME, f'{NAME}.ini')
LOG_PATH = utils.replace_extension(INI_PATH, 'log')
SEARCH_URL = utils.join_url('https://www.google.com', 'searchbyimage', 'upload')
INTERVALS = 0, 300, 900, 1800, 3600, 10800, 21600
MODULES = modules.wallhaven,

LANG = langs.DEFAULT
MODULE = MODULES[0]
DEFAULT_CONFIG = utils.Dict({
    CONFIG_TRANSITION: platform.wallpaper.Transition[platform.wallpaper.Transition.FADE],
    CONFIG_DISPLAY: '',
    CONFIG_AUTO_CHANGE: INTERVALS[0],
    CONFIG_LAST: utils.Timer.last_start,
    CONFIG_AUTOSAVE: False,
    CONFIG_DIR: utils.join_path(platform.PICTURES_DIR, NAME),
    CONFIG_NOTIFY: True,
    CONFIG_ANIMATE: True,
    CONFIG_CACHE: False,
    CONFIG_START: False,
    CONFIG_SAVE: False
})


def _is_busy() -> bool:
    return (change_wallpaper.is_running() or save_wallpaper.is_running() or
            search_wallpaper.is_running() or pin_to_start.is_running())


def _get_wallpaper_paths() -> Generator[str, None, None]:
    path = platform.get_wallpaper_path()  # TODO: multi monitor always returns platform.WALLPAPER_PATH (monitor radio?)
    if utils.file_exists(path):
        yield path
    if utils.file_exists(platform.WALLPAPER_PATH):
        temp_path = utils.join_path(TEMP_DIR, utils.file_name(path))
        if utils.copy_file(platform.WALLPAPER_PATH, temp_path):
            yield temp_path


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


def load_config() -> bool:  # TODO verify config
    parser = configparser.ConfigParser(
        converters={tuple.__name__: functool.to_tuple, list.__name__: functool.to_list, set.__name__: functool.to_set})
    try:
        loaded = bool(parser.read(INI_PATH))
    except configparser.MissingSectionHeaderError:
        loaded = False
    getters = {str: parser.get, int: parser.getint, float: parser.getfloat, bool: parser.getboolean,
               tuple: parser.gettuple, list: parser.getlist, set: parser.getset}
    loaded = _load_config(getters, NAME, CONFIG, DEFAULT_CONFIG) and loaded
    fix_config()
    for module in MODULES:
        loaded = _load_config(getters, module.NAME, module.CONFIG, module.DEFAULT_CONFIG) and loaded
    return loaded


def _strip(config: dict[str, Any], default: dict[str, Any]) -> dict[str, Any]:
    stripped = {}
    for option, value in default.items():
        if config[option] != value:
            stripped[option] = config[option]
    return stripped


def save_config() -> bool:  # TODO save recently set wallpaper (?)
    saved = True
    parser = configparser.ConfigParser()
    fix_config()
    parser[NAME] = _strip(CONFIG, DEFAULT_CONFIG)
    for module in MODULES:
        try:
            parser[module.NAME] = _strip(module.CONFIG, module.DEFAULT_CONFIG)
        except TypeError:
            saved = False
    with open(INI_PATH, 'w') as file:
        parser.write(file)
    return saved and utils.file_exists(INI_PATH)


def fix_config():
    if CONFIG[CONFIG_TRANSITION] not in platform.wallpaper.Transition:
        CONFIG[CONFIG_TRANSITION] = DEFAULT_CONFIG[CONFIG_TRANSITION]
    if DISPLAYS and CONFIG[CONFIG_DISPLAY] not in DISPLAYS:
        CONFIG[CONFIG_DISPLAY] = DEFAULT_CONFIG[CONFIG_DISPLAY]
    CONFIG[CONFIG_LAST] = TIMER.last_start if FEATURE_CHANGED else DEFAULT_CONFIG[CONFIG_LAST]
    if CONFIG[CONFIG_AUTO_CHANGE] not in INTERVALS:
        CONFIG[CONFIG_AUTO_CHANGE] = DEFAULT_CONFIG[CONFIG_AUTO_CHANGE]
    if not CONFIG[CONFIG_DIR]:
        CONFIG[CONFIG_DIR] = DEFAULT_CONFIG[CONFIG_DIR]


@utils.single
def change_wallpaper(url: Optional[str] = None, progress_callback: Optional[Callable[[int, ...], Any]] = None,
                     args: Optional[Iterable] = None, kwargs: Optional[Mapping[str, Any]] = None) -> bool:
    utils.animate(RES_BUSY, LANG.STATUS_CHANGE)
    if progress_callback:
        progress_callback(0, *() if args is None else args, **{} if kwargs is None else kwargs)
    if not url:
        if url := MODULE.get_next_url():
            HISTORY.set_next(url)
    if url:
        temp_path = utils.join_path(TEMP_DIR, utils.file_name(url))
        changed = (url == temp_path or utils.download_url(
            url, temp_path, chunk_count=100, on_write=progress_callback, args=args,
            kwargs=kwargs)) and platform.wallpaper.set(
            temp_path, *(CONFIG[CONFIG_DISPLAY],) if CONFIG[CONFIG_DISPLAY] else DISPLAYS,
            transition=getattr(platform.wallpaper.Transition, CONFIG[CONFIG_TRANSITION]))
    else:
        changed = False
    if progress_callback:
        progress_callback(100, *() if args is None else args, **{} if kwargs is None else kwargs)
    utils.inanimate(LANG.STATUS_CHANGE)
    return changed


@utils.single
def save_wallpaper() -> bool:
    utils.animate(RES_BUSY, LANG.STATUS_SAVE)
    saved = any(utils.copy_file(path, utils.join_path(CONFIG[CONFIG_DIR], utils.file_name(path))) for path in
                _get_wallpaper_paths())
    utils.inanimate(LANG.STATUS_SAVE)
    return saved


@utils.single
def search_wallpaper() -> bool:
    searched = False
    utils.animate(RES_BUSY, LANG.STATUS_SEARCH)
    for path in _get_wallpaper_paths():
        if location := utils.upload_url(SEARCH_URL, files={'encoded_image': (None, path)}).get_header('location'):
            utils.open_browser(location)
            searched = True
            break
    utils.inanimate(LANG.STATUS_SEARCH)
    return searched


@utils.thread
def on_change(previous: bool, enable: Callable, set_label: Callable) -> bool:
    changed = False
    if not change_wallpaper.is_running():
        enable(False)
        if changed := change_wallpaper(HISTORY.previous() if previous else HISTORY.next(), set_label):
            if CONFIG[CONFIG_AUTOSAVE]:
                save_wallpaper()
            set_label()
        utils.get_item(UID_PREVIOUS).Enable(HISTORY.has_previous())
        enable()
    if not changed and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANG.LABEL_PREVIOUS if previous else LANG.LABEL_NEXT, LANG.FAIL_CHANGE)
    return changed


def on_update_display():
    menu_display = utils.get_item(UID_DISPLAY)
    utils.remove_items(menu=menu_display)
    ids = platform.get_monitor_ids()
    pad = len(str(len(ids)))
    utils.add_item(
        f'[*] {LANG.DISPLAY_ALL}', utils.item.RADIO, CONFIG[CONFIG_DISPLAY] == DEFAULT_CONFIG[CONFIG_DISPLAY],
        uid=DEFAULT_CONFIG[CONFIG_DISPLAY], on_click=CONFIG.__setitem__, menu_args=(utils.get_property.UID,),
        args=(CONFIG_DISPLAY,), pre_menu_args=False, menu=menu_display)
    DISPLAYS.clear()
    for index, id_ in enumerate(ids):
        DISPLAYS.add(id_)
        utils.add_item(f'[{langs.to_str(index, LANG, pad)}] {platform.get_monitor_name(id_) or LANG.DISPLAY}',
                       utils.item.RADIO, CONFIG[CONFIG_DISPLAY] == id_, uid=id_,
                       on_click=CONFIG.__setitem__, menu_args=(utils.get_property.UID,),
                       args=(CONFIG_DISPLAY,), pre_menu_args=False, menu=menu_display)
    utils.add_item(LANG.LABEL_UPDATE_DISPLAY, on_click=on_update_display, menu=menu_display)


def on_auto_change(interval: Union[int, str]):
    CONFIG[CONFIG_AUTO_CHANGE] = int(interval)
    TIMER.start(CONFIG[CONFIG_AUTO_CHANGE]) if CONFIG[CONFIG_AUTO_CHANGE] else TIMER.stop()


def on_save() -> bool:
    saved = False
    if not save_wallpaper.is_running():
        saved = save_wallpaper()
    if not saved and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANG.LABEL_SAVE, LANG.FAIL_SAVE)
    return saved


def on_modify_save() -> bool:
    if path := platform.select_folder(LANG.LABEL_SAVE_DIR, CONFIG[CONFIG_DIR]):
        CONFIG[CONFIG_DIR] = path
    elif CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANG.LABEL_SAVE_DIR, LANG.FAIL_SAVE_DIR)
    return bool(path)


def on_open_explorer() -> bool:
    if not (opened := utils.try_any(_get_wallpaper_paths(), platform.open_file_path)) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANG.LABEL_OPEN_EXPLORER, LANG.FAIL_OPEN_EXPLORER)
    return opened


def on_open() -> bool:
    if not (opened := utils.try_any(_get_wallpaper_paths(), platform.open_file)) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANG.LABEL_OPEN, LANG.FAIL_OPEN)
    return opened


def on_copy_path() -> bool:
    if not (copied := utils.try_any(_get_wallpaper_paths(), platform.copy_text, '"')) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANG.LABEL_COPY_PATH, LANG.FAIL_COPY_PATH)
    return copied


def on_copy() -> bool:
    if not (copied := utils.try_any(_get_wallpaper_paths(), platform.copy_image)) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANG.LABEL_COPY, LANG.FAIL_COPY)
    return copied


def on_search() -> bool:
    searched = False
    if not search_wallpaper.is_running():
        searched = search_wallpaper()
    if not searched and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANG.LABEL_SEARCH, LANG.FAIL_SEARCH)
    return searched


def _get_launch_args() -> list[str]:
    argv = [sys.executable]
    if not pyinstall.FROZEN:
        argv.append(utils.abs_path(__file__))
    return argv


def _create_shortcut(dir_: str) -> bool:
    return utils.make_dirs(dir_) and platform.create_shortcut(
        utils.join_path(dir_, SHORTCUT_NAME), *_get_launch_args(),
        icon_path=RES_ICON * (not pyinstall.FROZEN), comment=LANG.DESCRIPTION, show=pyinstall.FROZEN, uid=UUID)


def on_shortcut() -> bool:
    if not (created := _create_shortcut(platform.DESKTOP_DIR)) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANG.LABEL_DESKTOP, LANG.FAIL_DESKTOP)
    return created


def on_remove_shortcuts() -> bool:
    if not (removed := platform.remove_shortcuts(platform.DESKTOP_DIR, UUID)) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANG.LABEL_REMOVE_DESKTOP, LANG.FAIL_REMOVE_DESKTOP)
    return removed


def on_start_shortcut() -> bool:
    if not (created := _create_shortcut(utils.join_path(platform.START_DIR, NAME))) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANG.LABEL_START_MENU, LANG.FAIL_START_MENU)
    return created


def on_remove_start_shortcuts() -> bool:
    if not (removed := platform.remove_shortcuts(platform.START_DIR, UUID)) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANG.LABEL_REMOVE_START_MENU, LANG.FAIL_REMOVE_START_MENU)
    return removed


def on_pin() -> bool:
    if not (pinned := platform.add_pin(*_get_launch_args(), name=NAME, icon_path='' if pyinstall.FROZEN else RES_ICON,
                                       show=pyinstall.FROZEN)) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANG.LABEL_PIN, LANG.FAIL_PIN)
    return pinned


def on_unpin() -> bool:
    if not (unpinned := platform.remove_pins(*_get_launch_args())) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANG.LABEL_UNPIN, LANG.FAIL_UNPIN)
    return unpinned


@utils.single
def pin_to_start() -> bool:
    return platform.add_pin(*_get_launch_args(), taskbar=False, name=NAME,
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
        utils.notify(LANG.LABEL_PIN_START, LANG.FAIL_PIN_START)
    return pinned


def on_unpin_start() -> bool:
    if not (unpinned := platform.remove_pins(*_get_launch_args(), taskbar=False)) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANG.LABEL_UNPIN_START, LANG.FAIL_UNPIN_START)
    return unpinned


def on_clear():
    url = HISTORY.peek()
    HISTORY.clear()
    if url is not None:
        HISTORY.set_next(url)
    utils.get_item(UID_PREVIOUS).Enable(HISTORY.has_previous())


def on_clear_cache() -> bool:
    if not (cleared := utils.delete(TEMP_DIR, True)) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANG.LABEL_CLEAR_CACHE, LANG.FAIL_CLEAR)
    return cleared


def on_reset():
    on_save_config(DEFAULT_CONFIG[CONFIG_SAVE])
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


def on_auto_start(checked: bool) -> bool:
    CONFIG[CONFIG_START] = checked
    if checked:
        return platform.register_autorun(NAME, *_get_launch_args(), *((ARG_CHANGE,) if CONFIG[CONFIG_AUTO_CHANGE]
                                                                      else ()), show=pyinstall.FROZEN, uid=UUID)
    return platform.unregister_autorun(NAME, UUID)


def on_save_config(checked: bool):
    CONFIG[CONFIG_SAVE] = checked
    save_config() if checked else utils.delete(INI_PATH)


def on_about():
    utils.not_implemented(LANG.LABEL_ABOUT)  # TODO MessageBox


@utils.thread
def on_quit():
    TIMER.stop()
    utils.disable()
    if _is_busy():
        if CONFIG[CONFIG_NOTIFY]:
            utils.notify(LANG.LABEL_QUIT, LANG.FAIL_QUIT)
        end_time = time.time() + EXIT_TIMEOUT
        while end_time > time.time() and _is_busy():
            time.sleep(POLL_TIMEOUT)
    utils.stop()


def create_menu():  # TODO slideshow (smaller timer)
    menu_change = utils.add_submenu(LANG.MENU_CHANGE)
    TIMER.args = False, menu_change.Enable, (lambda progress=None: menu_change.SetItemLabel(
        LANG.MENU_CHANGE if progress is None else f'{LANG.MENU_CHANGE} ({langs.to_str(progress, LANG, 3)}%)'))
    utils.add_item(LANG.LABEL_NEXT, on_click=on_change, args=TIMER.args,
                   on_thread=False, change_state=False, menu=menu_change)
    utils.add_item(LANG.LABEL_PREVIOUS, enable=False, uid=UID_PREVIOUS, on_click=on_change,
                   args=(True, *TIMER.args[1:]), on_thread=False, change_state=False, menu=menu_change)
    utils.add_item(LANG.LABEL_SAVE, on_click=on_save)
    utils.add_item(LANG.LABEL_SEARCH, on_click=on_search)
    utils.add_separator()
    menu_open = utils.add_submenu(LANG.MENU_OPEN)
    utils.add_item(LANG.LABEL_OPEN_EXPLORER, on_click=on_open_explorer, menu=menu_open)
    utils.add_item(LANG.LABEL_OPEN, on_click=on_open, menu=menu_open)
    menu_copy = utils.add_submenu(LANG.MENU_COPY)
    utils.add_item(LANG.LABEL_COPY_PATH, on_click=on_copy_path, menu=menu_copy)
    utils.add_item(LANG.LABEL_COPY, on_click=on_copy, menu=menu_copy)
    utils.add_separator()
    MODULE.create_menu()  # TODO separate left click menu (?)
    utils.add_separator()
    menu_actions = utils.add_submenu(LANG.MENU_ACTIONS)
    menu_links = utils.add_submenu(LANG.MENU_LINKS, menu=menu_actions)
    utils.add_item(LANG.LABEL_DESKTOP, on_click=on_shortcut, menu=menu_links)
    utils.add_item(LANG.LABEL_REMOVE_DESKTOP, on_click=on_remove_shortcuts, menu=menu_links)
    utils.add_separator(menu_links)
    utils.add_item(LANG.LABEL_START_MENU, on_click=on_start_shortcut, menu=menu_links)
    utils.add_item(LANG.LABEL_REMOVE_START_MENU, on_click=on_remove_start_shortcuts, menu=menu_links)
    utils.add_separator(menu_links)
    utils.add_item(LANG.LABEL_PIN, enable=pyinstall.FROZEN or FEATURE_FORCE_PIN, on_click=on_pin, menu=menu_links)
    utils.add_item(LANG.LABEL_UNPIN, enable=pyinstall.FROZEN or FEATURE_FORCE_PIN, on_click=on_unpin, menu=menu_links)
    utils.add_separator(menu_links)
    unpin = utils.add_item(LANG.LABEL_UNPIN_START, enable=pyinstall.FROZEN or FEATURE_FORCE_PIN,
                           on_click=on_unpin_start, menu=menu_links)
    utils.add_item(LANG.LABEL_PIN_START, enable=pyinstall.FROZEN or FEATURE_FORCE_PIN,
                   on_click=on_pin_start, menu_args=(utils.set_property.ENABLE,),
                   args=(unpin.Enable,), change_state=False, position=9, menu=menu_links)
    utils.add_item(LANG.LABEL_CLEAR, on_click=on_clear, menu=menu_actions)
    utils.add_item(LANG.LABEL_CLEAR_CACHE, on_click=on_clear_cache, menu=menu_actions)
    utils.add_item(LANG.LABEL_RESET, on_click=on_reset, menu=menu_actions)
    utils.add_item(LANG.LABEL_RESTART, on_click=on_restart, menu=menu_actions)
    utils.add_item(LANG.LABEL_ABOUT, on_click=on_about, menu=menu_actions)
    menu_auto = utils.add_submenu(LANG.MENU_AUTO)
    menu_auto_change = utils.add_submenu(LANG.MENU_AUTO_CHANGE, menu=menu_auto)
    for interval in INTERVALS:
        utils.add_item(getattr(LANG, f'TIME_{interval}'), utils.item.RADIO,
                       CONFIG[CONFIG_AUTO_CHANGE] == interval, uid=str(interval),
                       on_click=on_auto_change, menu_args=(utils.get_property.UID,), menu=menu_auto_change)
    utils.add_separator(menu_auto)
    utils.add_item(LANG.LABEL_AUTO_SAVE, utils.item.CHECK, CONFIG[CONFIG_AUTOSAVE],
                   on_click=CONFIG.__setitem__, menu_args=(utils.get_property.CHECKED,),
                   args=(CONFIG_AUTOSAVE,), pre_menu_args=False, menu=menu_auto)
    utils.add_item(LANG.LABEL_SAVE_DIR, on_click=on_modify_save, menu=menu_auto)
    menu_settings = utils.add_submenu(LANG.MENU_SETTINGS)
    menu_transition = utils.add_submenu(LANG.MENU_TRANSITION, menu=menu_settings)
    for transition in platform.wallpaper.Transition:
        utils.add_item(getattr(LANG, f'TRANSITION_{transition}'), utils.item.RADIO,
                       CONFIG[CONFIG_TRANSITION] == transition, uid=transition,
                       on_click=CONFIG.__setitem__, menu_args=(utils.get_property.UID,),
                       args=(CONFIG_TRANSITION,), pre_menu_args=False, menu=menu_transition)
    utils.add_submenu(LANG.MENU_DISPLAY, uid=UID_DISPLAY, menu=menu_settings)
    on_update_display()
    utils.add_item(LANG.LABEL_NOTIFY, utils.item.CHECK, CONFIG[CONFIG_NOTIFY],
                   on_click=CONFIG.__setitem__, menu_args=(utils.get_property.CHECKED,),
                   args=(CONFIG_NOTIFY,), pre_menu_args=False, menu=menu_settings)
    utils.add_item(LANG.LABEL_ANIMATE, utils.item.CHECK, CONFIG[CONFIG_ANIMATE],
                   on_click=on_animate, menu_args=(utils.get_property.CHECKED,), menu=menu_settings)
    utils.add_item(LANG.LABEL_CACHE, utils.item.CHECK, CONFIG[CONFIG_CACHE],
                   on_click=CONFIG.__setitem__, menu_args=(utils.get_property.CHECKED,),
                   args=(CONFIG_CACHE,), pre_menu_args=False, menu=menu_settings)
    utils.add_item(LANG.LABEL_START, utils.item.CHECK, CONFIG[CONFIG_START],
                   on_click=on_auto_start, menu_args=(utils.get_property.CHECKED,), menu=menu_settings)
    utils.add_item(LANG.LABEL_CONFIG, utils.item.CHECK, CONFIG[CONFIG_SAVE],
                   on_click=on_save_config, menu_args=(utils.get_property.CHECKED,), menu=menu_settings)
    utils.add_item(LANG.LABEL_QUIT, on_click=on_quit)


def start():  # TODO dark theme
    singleton.init(UUID, NAME, ARG_WAIT in sys.argv, on_crash=print, on_crash_args=('Crash',),
                   on_wait=print, on_wait_args=('Wait',), on_exit=print, on_exit_args=('Exit',))
    if ARG_DEBUG in sys.argv:
        log.redirect_stdout(LOG_PATH, True) if pyinstall.FROZEN else log.write_on_error(LOG_PATH)
        log.init(utils.file_name(__file__), utils.file_name(utils.__file__),
                 utils.re_join_path('libs', r'.*\.py'), utils.re_join_path('modules', r'.*\.py'),
                 utils.re_join_path('platforms', r'.*\.py'), level=log.Level.INFO, check_comp=False)
    pyinstall.clean_temp()
    utils.make_dirs(TEMP_DIR)
    utils.trim_dir(TEMP_DIR, MAX_CACHE)
    load_config()
    create_menu()
    on_animate(CONFIG[CONFIG_ANIMATE])
    on_auto_change(CONFIG[CONFIG_AUTO_CHANGE])
    on_auto_start(CONFIG[CONFIG_START])
    on_save_config(CONFIG[CONFIG_SAVE])
    if ARG_CHANGE in sys.argv or (FEATURE_CHANGED and CONFIG[CONFIG_AUTO_CHANGE] and
                                  time.time() >= CONFIG[CONFIG_AUTO_CHANGE] + CONFIG[CONFIG_LAST]):
        TIMER.last_start = time.time()
        on_change(*TIMER.args)
    utils.start(RES_TRAY, NAME, on_change, TIMER.args)


def stop():
    utils.Timer.kill_all()
    on_auto_start(CONFIG[CONFIG_START])
    on_save_config(CONFIG[CONFIG_SAVE])
    utils.trim_dir(TEMP_DIR, MAX_CACHE) if CONFIG[CONFIG_CACHE] else utils.delete(TEMP_DIR, True)
    if utils.exists_dir(TEMP_DIR) and utils.is_empty_dir(TEMP_DIR, True):
        utils.delete(TEMP_DIR, True)


def main() -> NoReturn:
    start()
    stop()
    sys.exit()


CONFIG = {}
DISPLAYS = set()
HISTORY = utils.List(default=None)
TIMER = utils.Timer(0, on_change)

if __name__ == '__main__':
    main()
