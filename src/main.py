__version__ = '0.1.11'  # TODO 0xC0000409 (wx?)
__author__ = 'HellLord'

import atexit
import configparser
import math
import subprocess
import sys
import time
from typing import Any, Callable, Generator, Iterable, Mapping, NoReturn, Optional, Union

import langs
import libs.file
import libs.log
import libs.pyinstall
import libs.singleton
import modules.wallhaven
import platforms.win32 as platform  # TODO sys.platform
import utils

EXIT_TIMEOUT_FACTOR = 0.9
MAX_CACHE = 64 * 1024 * 1024
POLL_TIMEOUT = 0.1

NAME = 'Wallpyper'
ARG_CHANGE = 'change'
ARG_DEBUG = 'debug'
ARG_WAIT = 'wait'
CONFIG_CHANGE = 'auto_change'
CONFIG_INTERVAL = 'auto_change_interval'
CONFIG_CHANGED = 'keep_auto_changed'
CONFIG_LAST = 'auto_changed_at'
CONFIG_AUTOSAVE = 'auto_save'
CONFIG_DIR = 'save_directory'
CONFIG_NOTIFY = 'show_notification'
CONFIG_NO_FADE = 'disable_fading'
CONFIG_ANIMATE = 'animate_icon'
CONFIG_CACHE = 'keep_cache'
CONFIG_START = 'auto_start'
CONFIG_SAVE = 'save_config'

LANG = langs.DEFAULT
MODULES = modules.wallhaven,
MODULE = MODULES[0]
DEFAULT_CONFIG = utils.Dict({
    CONFIG_CHANGE: False,
    CONFIG_INTERVAL: 3600,
    CONFIG_CHANGED: False,
    CONFIG_LAST: math.inf,
    CONFIG_AUTOSAVE: False,
    CONFIG_DIR: utils.join_path(platform.PICTURES_DIR, NAME),
    CONFIG_NOTIFY: True,
    CONFIG_NO_FADE: False,
    CONFIG_ANIMATE: True,
    CONFIG_CACHE: False,
    CONFIG_START: False,
    CONFIG_SAVE: False
})

EXIT_TIMEOUT = EXIT_TIMEOUT_FACTOR * platform.get_max_shutdown_time()
UUID = f'{__author__}.{NAME}'
RES_PATHS = tuple(utils.join_path(utils.dir_name(__file__), 'resources', name) for name in ('icon.png', 'loading.gif'))
TEMP_DIR = utils.join_path(platform.get_temp_dir(), NAME)
CONFIG_PATH = fr'D:\Projects\Wallpyper\{NAME}.ini'  # utils.join_path(platform.SAVE_DIR, f'{NAME}.ini')
LOG_PATH = utils.replace_extension(CONFIG_PATH, 'log')
SEARCH_URL = 'https://www.google.com/searchbyimage/upload'
INTERVALS = '5 Minute', '15 Minute', '30 Minute', '1 Hour', '3 Hour', '6 Hour'


def _is_running() -> bool:
    return change_wallpaper.is_running() or save_wallpaper.is_running() or search_wallpaper.is_running()


def _load_config(getters: dict[type, Callable[[str, str], Union[str, int, float, bool]]], section: str,
                 config: dict[str, Union[str, int, float, bool]],
                 default: dict[str, Union[str, int, float, bool]]) -> bool:
    loaded = True
    for option, value in default.items():
        try:
            config[option] = getters[type(value)](section, option)
        except (ValueError, TypeError, configparser.NoSectionError, configparser.NoOptionError):
            config[option] = value
            loaded = False
    return loaded


def _get_wallpaper_paths() -> Generator[str, None, None]:
    path = platform.get_wallpaper_path()
    if utils.file_exists(path):
        yield path
    file_name = utils.file_name(path)
    if utils.file_exists(platform.WALLPAPER_PATH):
        temp_path = utils.join_path(TEMP_DIR, file_name)
        if utils.copy_file(platform.WALLPAPER_PATH, temp_path):
            yield temp_path


def load_config() -> bool:  # TODO verify config
    parser = configparser.ConfigParser()
    try:
        loaded = bool(parser.read(CONFIG_PATH))
    except configparser.MissingSectionHeaderError:
        loaded = False
    getters = {str: parser.get, int: parser.getint, float: parser.getfloat, bool: parser.getboolean}
    loaded = _load_config(getters, NAME, CONFIG, DEFAULT_CONFIG) and loaded
    for module in MODULES:
        loaded = _load_config(getters, module.NAME, module.CONFIG, module.DEFAULT_CONFIG) and loaded
    return loaded


def save_config() -> bool:  # TODO save recently set wallpaper (?)
    saved = True
    config_parser = configparser.ConfigParser()
    config_parser[NAME] = CONFIG
    for module in MODULES:
        try:
            config_parser[module.NAME] = module.CONFIG
        except TypeError:
            saved = False
    with open(CONFIG_PATH, 'w') as file:
        config_parser.write(file)
    return saved and utils.file_exists(CONFIG_PATH)


@utils.single
def change_wallpaper(url: Optional[str] = None, progress_callback: Optional[Callable[[int, ...], Any]] = None,
                     args: Optional[Iterable] = None, kwargs: Optional[Mapping[str, Any]] = None) -> bool:
    utils.animate(RES_PATHS[1], LANG.STATUS_CHANGE)
    if progress_callback:
        progress_callback(0, *() if args is None else args, **{} if kwargs is None else kwargs)
    if not url:
        if url := MODULE.get_next_url():
            HISTORY.set_next(url)
    if url:
        temp_path = utils.join_path(TEMP_DIR, utils.file_name(url))
        changed = (url == temp_path or utils.download_url(
            url, temp_path, chunk_count=100, on_write=progress_callback, args=args,
            kwargs=kwargs)) and platform.set_wallpaper(temp_path, fade=not CONFIG[CONFIG_NO_FADE])
    else:
        changed = False
    if progress_callback:
        progress_callback(100, *() if args is None else args, **{} if kwargs is None else kwargs)
    utils.inanimate(LANG.STATUS_CHANGE)
    return changed


@utils.single
def save_wallpaper() -> bool:
    utils.animate(RES_PATHS[1], LANG.STATUS_SAVE)
    saved = any(utils.copy_file(path, utils.join_path(CONFIG[CONFIG_DIR], utils.file_name(path))) for path in
                _get_wallpaper_paths())
    utils.inanimate(LANG.STATUS_SAVE)
    return saved


@utils.single
def search_wallpaper() -> bool:
    searched = False
    utils.animate(RES_PATHS[1], LANG.STATUS_SEARCH)
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
            CONFIG[CONFIG_LAST] = DEFAULT_CONFIG[
                CONFIG_LAST] if TIMER.last_start == utils.Timer.last_start else TIMER.last_start
            if CONFIG[CONFIG_AUTOSAVE]:
                save_wallpaper()
            set_label()
        ENABLE_PREVIOUS(HISTORY.has_previous())
        enable()
    if not changed and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANG.LABEL_PREVIOUS if previous else LANG.LABEL_NEXT, LANG.FAIL_CHANGE)
    return changed


def on_auto_change(checked: bool, enable_submenu: Optional[Callable[[bool], None]] = None):
    CONFIG[CONFIG_CHANGE] = checked
    if enable_submenu:
        enable_submenu(checked)
    TIMER.start(CONFIG[CONFIG_INTERVAL]) if checked else TIMER.stop()


def on_interval(interval: str):
    CONFIG[CONFIG_INTERVAL] = int(utils.TimeDelta(interval))
    on_auto_change(CONFIG[CONFIG_CHANGE])


@utils.thread
def on_save(enable: Callable) -> bool:
    saved = False
    if not save_wallpaper.is_running():
        enable(False)
        saved = save_wallpaper()
        enable()
    if not saved and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANG.LABEL_SAVE, LANG.FAIL_SAVE)
    return saved


def on_modify_save():
    utils.not_implemented(LANG.LABEL_MODIFY_SAVE)


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


@utils.thread
def on_search(enable: Callable) -> bool:
    searched = False
    if not search_wallpaper.is_running():
        enable(False)
        searched = search_wallpaper()
        enable()
    if not searched and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANG.LABEL_SEARCH, LANG.FAIL_SEARCH)
    return searched


def _get_launch_args() -> list[str]:
    argv = [sys.executable]
    if not libs.pyinstall.FROZEN:
        argv.append(utils.abs_path(__file__))
    return argv


def _create_shortcut(dir_: str) -> bool:
    return platform.create_shortcut(utils.join_path(dir_, f'{NAME}.{platform.LINK_EXT}'),
                                    *_get_launch_args(), comment=LANG.DESCRIPTION, aumi=UUID)


def on_shortcut() -> bool:
    if not (created := _create_shortcut(platform.DESKTOP_DIR)) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANG.LABEL_DESKTOP, LANG.FAIL_DESKTOP)
    return created


def on_remove_shortcuts() -> bool:
    if not (removed := platform.remove_shortcuts(platform.DESKTOP_DIR, UUID)) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANG.LABEL_REMOVE_DESKTOP, LANG.FAIL_REMOVE_DESKTOP)
    return removed


def on_start_shortcut() -> bool:
    if not (created := _create_shortcut(platform.START_DIR)) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANG.LABEL_START_MENU, LANG.FAIL_START_MENU)
    return created


def on_remove_start_shortcuts() -> bool:
    if not (removed := platform.remove_shortcuts(platform.START_DIR, UUID)) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANG.LABEL_REMOVE_START_MENU, LANG.FAIL_REMOVE_START_MENU)
    return removed


def on_clear():
    url = HISTORY.peek()
    HISTORY.clear()
    if url is not None:
        HISTORY.set_next(url)
    ENABLE_PREVIOUS(HISTORY.has_previous())


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
        return platform.register_autorun(NAME, *_get_launch_args(),
                                         *(ARG_CHANGE,) if CONFIG[CONFIG_CHANGE] else (), uid=UUID)
    return platform.unregister_autorun(NAME, UUID)


def on_save_config(checked: bool):
    CONFIG[CONFIG_SAVE] = checked
    save_config() if checked else utils.delete(CONFIG_PATH)


def on_about():
    utils.not_implemented(LANG.LABEL_ABOUT)  # TODO MessageBox


@utils.thread
def on_quit():
    TIMER.stop()
    utils.disable()
    if _is_running():
        if CONFIG[CONFIG_NOTIFY]:
            utils.notify(LANG.LABEL_QUIT, LANG.FAIL_QUIT)
        end_time = time.time() + EXIT_TIMEOUT
        while end_time > time.time() and _is_running():
            time.sleep(POLL_TIMEOUT)
    utils.stop()


def create_menu():  # TODO slideshow (smaller timer)
    global ENABLE_PREVIOUS
    update_config = utils.call_after(utils.reverse, True, True)(CONFIG.__setitem__)
    menu_change = utils.add_submenu(LANG.MENU_CHANGE)
    TIMER.args = False, menu_change.Enable, (lambda progress=None: menu_change.SetItemLabel(
        LANG.MENU_CHANGE if progress is None else f'{LANG.MENU_CHANGE} ({langs.to_str(progress, LANG, 3)}%)'))
    utils.add_item(LANG.LABEL_NEXT, on_click=on_change, args=TIMER.args, menu=menu_change)
    ENABLE_PREVIOUS = utils.add_item(LANG.LABEL_PREVIOUS, enable=False, on_click=on_change,
                                     args=(True, *TIMER.args[1:]), menu=menu_change).Enable
    utils.add_item(LANG.LABEL_SAVE, on_click=on_save, menu_args=(utils.set_property.ENABLE,))
    utils.add_item(LANG.LABEL_SEARCH, on_click=on_search, menu_args=(utils.set_property.ENABLE,))
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
    utils.add_item(LANG.LABEL_DESKTOP, on_click=on_shortcut, menu=menu_actions)
    utils.add_item(LANG.LABEL_REMOVE_DESKTOP, on_click=on_remove_shortcuts, menu=menu_actions)
    utils.add_item(LANG.LABEL_START_MENU, on_click=on_start_shortcut, menu=menu_actions)
    utils.add_item(LANG.LABEL_REMOVE_START_MENU, on_click=on_remove_start_shortcuts, menu=menu_actions)
    utils.add_separator(menu_actions)
    utils.add_item(LANG.LABEL_CLEAR, on_click=on_clear, menu=menu_actions)
    utils.add_item(LANG.LABEL_CLEAR_CACHE, on_click=on_clear_cache, menu=menu_actions)
    utils.add_separator(menu_actions)
    utils.add_item(LANG.LABEL_RESET, on_click=on_reset, menu=menu_actions)
    utils.add_item(LANG.LABEL_RESTART, on_click=on_restart, menu=menu_actions)
    menu_auto = utils.add_submenu(LANG.MENU_AUTO)
    menu_interval = utils.add_submenu(LANG.MENU_INTERVAL, CONFIG[CONFIG_CHANGE], menu_auto)
    for interval in INTERVALS:
        utils.add_item(interval, utils.item.RADIO, CONFIG[CONFIG_INTERVAL] == int(utils.TimeDelta(interval)),
                       on_click=on_interval, menu_args=(utils.get_property.LABEL,), menu=menu_interval)
    utils.add_item(LANG.LABEL_AUTO_CHANGE, utils.item.CHECK, CONFIG[CONFIG_CHANGE], on_click=on_auto_change,
                   menu_args=(utils.get_property.CHECKED,), args=(menu_interval.Enable,), position=0, menu=menu_auto)
    utils.add_separator(menu_auto)
    utils.add_item(LANG.LABEL_AUTO_SAVE, utils.item.CHECK, CONFIG[CONFIG_AUTOSAVE], on_click=update_config,
                   menu_args=(utils.get_property.CHECKED,), args=(CONFIG_AUTOSAVE,), menu=menu_auto)
    utils.add_item(LANG.LABEL_MODIFY_SAVE, on_click=on_modify_save, menu=menu_auto)
    menu_config = utils.add_submenu(LANG.MENU_CONFIG)
    utils.add_item(LANG.LABEL_NOTIFY, utils.item.CHECK, CONFIG[CONFIG_NOTIFY], on_click=update_config,
                   menu_args=(utils.get_property.CHECKED,), args=(CONFIG_NOTIFY,), menu=menu_config)
    utils.add_item(LANG.LABEL_NO_FADE, utils.item.CHECK, CONFIG[CONFIG_NO_FADE], on_click=update_config,
                   menu_args=(utils.get_property.CHECKED,), args=(CONFIG_NO_FADE,), menu=menu_config)
    utils.add_item(LANG.LABEL_ANIMATE, utils.item.CHECK, CONFIG[CONFIG_ANIMATE], on_click=on_animate,
                   menu_args=(utils.get_property.CHECKED,), menu=menu_config)
    utils.add_item(LANG.LABEL_CACHE, utils.item.CHECK, CONFIG[CONFIG_CACHE], on_click=update_config,
                   menu_args=(utils.get_property.CHECKED,), args=(CONFIG_CACHE,), menu=menu_config)
    utils.add_item(LANG.LABEL_START, utils.item.CHECK, CONFIG[CONFIG_START], on_click=on_auto_start,
                   menu_args=(utils.get_property.CHECKED,), menu=menu_config)
    utils.add_item(LANG.LABEL_CONFIG, utils.item.CHECK, CONFIG[CONFIG_SAVE], on_click=on_save_config,
                   menu_args=(utils.get_property.CHECKED,), menu=menu_config)
    utils.add_item(LANG.LABEL_ABOUT, on_click=on_about)
    utils.add_item(LANG.LABEL_QUIT, on_click=on_quit)


def start():  # TODO dark theme
    libs.singleton.init(UUID, NAME, ARG_WAIT in sys.argv, on_crash=print, on_crash_args=('Crash',), on_wait=print,
                        on_wait_args=('Wait',), on_exit=print, on_exit_args=('Exit',))
    if ARG_DEBUG in sys.argv:
        libs.log.redirect_stdout(LOG_PATH, True) if libs.pyinstall.FROZEN else libs.log.write_on_error(LOG_PATH)
        libs.log.init(utils.file_name(__file__), utils.file_name(utils.__file__),
                      utils.re_join_path('libs', r'.*\.py'), utils.re_join_path('modules', r'.*\.py'),
                      utils.re_join_path('platforms', r'.*\.py'), level=libs.log.Level.INFO, check_comp=False)
    libs.pyinstall.clean_temp()
    utils.make_dirs(TEMP_DIR)
    utils.trim_dir(TEMP_DIR, MAX_CACHE)
    load_config()
    create_menu()
    on_animate(CONFIG[CONFIG_ANIMATE])
    on_auto_change(CONFIG[CONFIG_CHANGE])
    on_auto_start(CONFIG[CONFIG_START])
    on_save_config(CONFIG[CONFIG_SAVE])
    for path in _get_wallpaper_paths():
        HISTORY.set_next(path)
        break
    if ARG_CHANGE in sys.argv or (
            CONFIG[CONFIG_CHANGE] and time.time() >= CONFIG[CONFIG_INTERVAL] + CONFIG[CONFIG_LAST]):
        TIMER.last_start = time.time()
        on_change(*TIMER.args)
    utils.start(RES_PATHS[0], NAME, on_change, TIMER.args)


def stop():
    utils.Timer.kill_all()
    if not CONFIG[CONFIG_CHANGED]:
        CONFIG[CONFIG_LAST] = DEFAULT_CONFIG[CONFIG_LAST]
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
HISTORY = utils.List()
ENABLE_PREVIOUS = utils.dummy_func
TIMER = utils.Timer(target=on_change)

if __name__ == '__main__':
    main()
