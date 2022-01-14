__version__ = '0.1.11'  # TODO 0xC0000409 (wx?)
__author__ = 'HellLord'

import atexit
import collections
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
MAX_LENGTH = 32
POLL_TIMEOUT = 0.01

NAME = 'Wallpyper'
ARG_CHANGE = 'change'
ARG_DEBUG = 'debug'
ARG_WAIT = 'wait'
CONFIG_CHANGE = 'auto_change'
CONFIG_INTERVAL = 'auto_change_interval'
CONFIG_CHANGED = 'keep_last_changed'
CONFIG_LAST = 'last_changed'
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
DEFAULT_CONFIG = {
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
}

EXIT_TIMEOUT = EXIT_TIMEOUT_FACTOR * platform.get_max_shutdown_time()
UUID = f'{__author__}.{NAME}'
RES_PATHS = tuple(utils.join_path(utils.dir_name(__file__), 'resources', name) for name in ('icon.png', 'loading.gif'))
TEMP_DIR = utils.join_path(platform.get_temp_dir(), NAME)
CONFIG_PATH = fr'D:\Projects\Wallpyper\{NAME}.ini'  # utils.join_path(platform.SAVE_DIR, f'{NAME}.ini')
LOG_PATH = utils.replace_extension(CONFIG_PATH, 'log')
SEARCH_URL = 'https://www.google.com/searchbyimage/upload'
INTERVALS = '5 Minute', '15 Minute', '30 Minute', '1 Hour', '3 Hour', '6 Hour'

CONFIG = {}
URLS = collections.deque(maxlen=MAX_LENGTH)
URL_INDEX = utils.Int(-1)
ENABLE_PREVIOUS = utils.dummy_func
SET_NEXT_LABEL = utils.dummy_func
SET_PREVIOUS_LABEL = utils.dummy_func
TIMER = utils.timer(utils.dummy_func)


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
    utils.animate(RES_PATHS[1], LANG.CHANGING)
    if progress_callback:
        progress_callback(0, *args or (), **kwargs or {})
    if not url:
        url = MODULE.get_next_url()
        if url:
            URLS.append(url)
    if url:
        temp_path = utils.join_path(TEMP_DIR, utils.file_name(url))
        changed = utils.download_url(
            url, temp_path, chunk_count=100, on_write=progress_callback, args=args,
            kwargs=kwargs) and platform.set_wallpaper(temp_path, fade=not CONFIG[CONFIG_NO_FADE])
    else:
        changed = False
    if progress_callback:
        progress_callback(100, *args or (), **kwargs or {})
    utils.inanimate(LANG.CHANGING)
    return changed


def _get_wallpaper_paths() -> Generator[str, None, None]:
    path = platform.get_wallpaper_path()
    if utils.file_exists(path):
        yield path
    file_name = utils.file_name(path)
    if utils.file_exists(platform.WALLPAPER_PATH):
        temp_path = utils.join_path(TEMP_DIR, file_name)
        if utils.copy_file(platform.WALLPAPER_PATH, temp_path):
            yield temp_path


@utils.single
def save_wallpaper() -> bool:
    utils.animate(RES_PATHS[1], LANG.SAVING)
    saved = any(utils.copy_file(path, utils.join_path(CONFIG[CONFIG_DIR], utils.file_name(path))) for path in
                _get_wallpaper_paths())
    utils.inanimate(LANG.SAVING)
    return saved


@utils.single
def search_wallpaper() -> bool:
    searched = False
    utils.animate(RES_PATHS[1], LANG.SEARCHING)
    for path in _get_wallpaper_paths():
        if location := utils.upload_url(SEARCH_URL, files={'encoded_image': (None, path)}).get_header('location'):
            utils.open_browser(location)
            searched = True
            break
    utils.inanimate(LANG.SEARCHING)
    return searched


@utils.thread
def on_change(previous: Optional[bool] = None) -> bool:
    if previous:
        index = URL_INDEX.get() - 1
        url = URLS[URL_INDEX.get() - 1]
        set_label = SET_PREVIOUS_LABEL
        label = LANG.PREVIOUS
    else:
        index = URL_INDEX.get() + 1
        url = None if index == len(URLS) else URLS[index]
        set_label = SET_NEXT_LABEL
        label = LANG.NEXT
    changed = change_wallpaper(url, set_label)
    set_label(-1)
    ENABLE_PREVIOUS(index > 0)
    if changed:
        URL_INDEX.set(index)
        if CONFIG[CONFIG_LAST] > TIMER.last_started:
            CONFIG[CONFIG_LAST] = TIMER.last_started
        if CONFIG[CONFIG_AUTOSAVE]:
            save_wallpaper()
    elif CONFIG[CONFIG_NOTIFY]:
        utils.notify(label, LANG.FAILED_CHANGING)
    return changed


def on_auto_change(checked: bool, enable_submenu: Optional[Callable[[bool], None]] = None) -> None:
    CONFIG[CONFIG_CHANGE] = checked
    if enable_submenu:
        enable_submenu(checked)
    TIMER.start(CONFIG[CONFIG_INTERVAL]) if checked else TIMER.stop()


def on_interval(interval: str) -> None:
    CONFIG[CONFIG_INTERVAL] = int(utils.TimeDelta(interval))
    on_auto_change(CONFIG[CONFIG_CHANGE])


@utils.thread
def on_save() -> bool:
    if not (saved := save_wallpaper()) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANG.SAVE, LANG.FAILED_SAVING)
    return saved


def on_modify_save() -> None:
    utils.not_implemented(LANG.MODIFY_SAVE)


def on_open_explorer() -> bool:
    if not (opened := utils.try_any(_get_wallpaper_paths(), platform.open_file_path)) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANG.OPEN_EXPLORER, LANG.FAILED_OPENING_EXPLORER)
    return opened


def on_open() -> bool:
    if not (opened := utils.try_any(_get_wallpaper_paths(), platform.open_file)) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANG.OPEN, LANG.FAILED_OPENING)
    return opened


def on_copy_path() -> bool:
    if not (copied := utils.try_any(_get_wallpaper_paths(), platform.copy_text, '"')) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANG.COPY_PATH, LANG.FAILED_COPYING_PATH)
    return copied


def on_copy() -> bool:
    if not (copied := utils.try_any(_get_wallpaper_paths(), platform.copy_image)) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANG.COPY, LANG.FAILED_COPYING)
    return copied


@utils.thread
def on_search() -> bool:
    if not (searched := search_wallpaper()) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANG.SEARCH, LANG.FAILED_SEARCHING)
    return searched


def _get_launch_argv() -> list[str]:
    argv = [sys.executable]
    if not libs.pyinstall.FROZEN:
        argv.append(utils.abs_path(__file__))
    return argv


def _create_shortcut(dir_: str) -> bool:
    return platform.create_shortcut(utils.join_path(dir_, f'{NAME}.{platform.LINK_EXT}'),
                                    *_get_launch_argv(), comment=LANG.DESCRIPTION, aumi=UUID)


def on_shortcut() -> bool:
    if not (created := _create_shortcut(platform.DESKTOP_DIR)) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANG.DESKTOP, LANG.FAILED_DESKTOP)
    return created


def on_remove_shortcuts() -> bool:
    if not (removed := platform.remove_shortcuts(platform.DESKTOP_DIR, UUID)) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANG.REMOVE_DESKTOP, LANG.FAILED_REMOVING_DESKTOP)
    return removed


def on_start_shortcut() -> bool:
    if not (created := _create_shortcut(platform.START_DIR)) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANG.START_MENU, LANG.FAILED_START_MENU)
    return created


def on_remove_start_shortcuts() -> bool:
    if not (removed := platform.remove_shortcuts(platform.START_DIR, UUID)) and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANG.REMOVE_START_MENU, LANG.FAILED_REMOVING_START_MENU)
    return removed


@utils.thread
def on_clear() -> bool:
    cleared = utils.delete(TEMP_DIR, True)
    if not cleared and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANG.CLEAR, LANG.FAILED_CLEARING)
    return cleared


def on_reset() -> None:
    on_save_config(False)
    on_restart()


def on_restart() -> None:
    args = _get_launch_argv()
    args.extend(sys.argv[1:])
    if ARG_WAIT not in args:
        args.append(ARG_WAIT)
    atexit.register(subprocess.Popen, args, creationflags=subprocess.CREATE_NEW_CONSOLE)
    on_exit()


def on_animate(checked: bool) -> None:
    CONFIG[CONFIG_ANIMATE] = checked
    utils.pause_animation(not checked)


def on_auto_start(checked: bool) -> bool:
    CONFIG[CONFIG_START] = checked
    if checked:
        return platform.register_autorun(NAME, *_get_launch_argv(),
                                         *(ARG_CHANGE,) if CONFIG[CONFIG_CHANGE] else (), uid=UUID)
    return platform.unregister_autorun(NAME, UUID)


def on_save_config(checked: bool) -> None:
    CONFIG[CONFIG_SAVE] = checked
    save_config() if checked else utils.delete(CONFIG_PATH)


def on_about() -> None:
    utils.not_implemented(LANG.ABOUT)


@utils.thread
def on_exit() -> None:
    TIMER.stop()
    utils.disable()
    if change_wallpaper.is_running() or save_wallpaper.is_running() or search_wallpaper.is_running():
        if CONFIG[CONFIG_NOTIFY]:
            utils.notify(LANG.QUIT, LANG.FAILED_QUITING)
        end_time = time.time() + EXIT_TIMEOUT
        while end_time > time.time() and (
                change_wallpaper.is_running() or save_wallpaper.is_running() or search_wallpaper.is_running()):
            time.sleep(POLL_TIMEOUT)
    utils.stop()


def create_menu() -> None:  # TODO slideshow (smaller timer)
    update_config = utils.call_after(utils.reverse, True, True)(CONFIG.__setitem__)
    next_wallpaper = utils.add_item(LANG.NEXT, on_click=on_change)
    previous_wallpaper = utils.add_item(LANG.PREVIOUS, enable=False, on_click=on_change, args=(True,))

    def set_next_label(progress: int) -> None:
        next_wallpaper.SetItemLabel(
            f'{LANG.NEXT} ({langs.str_(progress, LANG, 3)}%)' if progress >= 0 else f'{LANG.NEXT}')

    def set_previous_label(progress: int) -> None:
        previous_wallpaper.SetItemLabel(
            f'{LANG.PREVIOUS} ({langs.str_(progress, LANG, 3)}%)' if progress >= 0 else f'{LANG.PREVIOUS}')

    global ENABLE_PREVIOUS, SET_NEXT_LABEL, SET_PREVIOUS_LABEL
    ENABLE_PREVIOUS = previous_wallpaper.Enable
    SET_NEXT_LABEL = set_next_label
    SET_PREVIOUS_LABEL = set_previous_label
    utils.add_separator()
    menu_interval = utils.add_submenu(LANG.SUBMENU_INTERVAL, CONFIG[CONFIG_CHANGE])
    for interval in INTERVALS:
        utils.add_item(interval, utils.item.RADIO, CONFIG[CONFIG_INTERVAL] == int(utils.TimeDelta(interval)),
                       on_click=on_interval, extra_args=(utils.get_property.LABEL,), menu=menu_interval)
    utils.add_item(LANG.AUTO_CHANGE, utils.item.CHECK, CONFIG[CONFIG_CHANGE], on_click=on_auto_change,
                   args=(menu_interval.Enable,), extra_args=(utils.get_property.CHECKED,), position=3)
    utils.add_separator()
    utils.add_item(LANG.SAVE, on_click=on_save)
    utils.add_item(LANG.AUTO_SAVE, utils.item.CHECK, CONFIG[CONFIG_AUTOSAVE], on_click=update_config,
                   args=(CONFIG_AUTOSAVE,), extra_args=(utils.get_property.CHECKED,))
    utils.add_item(LANG.MODIFY_SAVE, on_click=on_modify_save)
    utils.add_separator()
    menu_open = utils.add_submenu(LANG.SUBMENU_OPEN)
    utils.add_item(LANG.OPEN_EXPLORER, on_click=on_open_explorer, menu=menu_open)
    utils.add_item(LANG.OPEN, on_click=on_open, menu=menu_open)
    menu_copy = utils.add_submenu(LANG.SUBMENU_COPY)
    utils.add_item(LANG.COPY_PATH, on_click=on_copy_path, menu=menu_copy)
    utils.add_item(LANG.COPY, on_click=on_copy, menu=menu_copy)
    utils.add_item(LANG.SEARCH, on_click=on_search)
    utils.add_separator()
    MODULE.create_menu()  # TODO separate left click menu (?)
    utils.add_separator()
    menu_actions = utils.add_submenu(LANG.SUBMENU_ACTIONS)
    utils.add_item(LANG.DESKTOP, on_click=on_shortcut, menu=menu_actions)
    utils.add_item(LANG.REMOVE_DESKTOP, on_click=on_remove_shortcuts, menu=menu_actions)
    utils.add_item(LANG.START_MENU, on_click=on_start_shortcut, menu=menu_actions)
    utils.add_item(LANG.REMOVE_START_MENU, on_click=on_remove_start_shortcuts, menu=menu_actions)
    utils.add_separator(menu_actions)
    utils.add_item(LANG.CLEAR, on_click=on_clear, menu=menu_actions)
    utils.add_item(LANG.RESET, on_click=on_reset, menu=menu_actions)
    utils.add_item(LANG.RESTART, on_click=on_restart, menu=menu_actions)
    menu_config = utils.add_submenu(LANG.SUBMENU_CONFIG)
    utils.add_item(LANG.NOTIFY, utils.item.CHECK, CONFIG[CONFIG_NOTIFY], on_click=update_config, args=(CONFIG_NOTIFY,),
                   extra_args=(utils.get_property.CHECKED,), menu=menu_config)
    utils.add_item(LANG.FADE, utils.item.CHECK, CONFIG[CONFIG_NO_FADE], on_click=update_config, args=(CONFIG_NO_FADE,),
                   extra_args=(utils.get_property.CHECKED,), menu=menu_config)
    utils.add_item(LANG.ANIMATE, utils.item.CHECK, CONFIG[CONFIG_ANIMATE], on_click=on_animate,
                   extra_args=(utils.get_property.CHECKED,), menu=menu_config)
    utils.add_item(LANG.CACHE, utils.item.CHECK, CONFIG[CONFIG_CACHE], on_click=update_config, args=(CONFIG_CACHE,),
                   extra_args=(utils.get_property.CHECKED,), menu=menu_config)
    utils.add_item(LANG.START, utils.item.CHECK, CONFIG[CONFIG_START], on_click=on_auto_start,
                   extra_args=(utils.get_property.CHECKED,), menu=menu_config)
    utils.add_item(LANG.CONFIG, utils.item.CHECK, CONFIG[CONFIG_SAVE], on_click=on_save_config,
                   extra_args=(utils.get_property.CHECKED,), menu=menu_config)
    utils.add_item(LANG.ABOUT, on_click=on_about)
    utils.add_item(LANG.QUIT, on_click=on_exit)


def start() -> None:  # TODO dark theme
    TIMER.set_callback(on_change)
    libs.singleton.init(UUID, NAME, ARG_WAIT in sys.argv, on_crash=print, on_crash_args=('Crash',), on_wait=print,
                        on_wait_args=('Wait',), on_exit=print, on_exit_args=('Exit',))
    if ARG_DEBUG in sys.argv:
        libs.log.redirect_stdout(LOG_PATH, True) if libs.pyinstall.FROZEN else libs.log.write_on_error(LOG_PATH)
        libs.log.init(utils.file_name(__file__), utils.file_name(utils.__file__),
                      utils.re_join_path('libs', r'.*\.py'), utils.re_join_path('modules', r'.*\.py'),
                      utils.re_join_path('platforms', r'.*\.py'), level=libs.log.Level.INFO, skip_comp=True)
    libs.pyinstall.clean_temp()
    utils.make_dirs(TEMP_DIR)
    utils.trim_dir(TEMP_DIR, MAX_CACHE)
    load_config()
    create_menu()
    on_auto_change(CONFIG[CONFIG_CHANGE])
    on_animate(CONFIG[CONFIG_ANIMATE])
    on_auto_start(CONFIG[CONFIG_START])
    on_save_config(CONFIG[CONFIG_SAVE])
    if ARG_CHANGE in sys.argv or (
            CONFIG[CONFIG_CHANGE] and time.time() >= CONFIG[CONFIG_INTERVAL] + CONFIG[CONFIG_LAST]):
        TIMER.last_started = time.time()
        on_change()
    utils.start(RES_PATHS[0], NAME, on_change)


def stop() -> None:
    utils.timer.kill_all()
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


if __name__ == '__main__':
    main()
