__version__ = '0.1.11'  # TODO: error handle rather than condition checking; 0xC0000409 (wx?)

import atexit
import collections
import configparser
import subprocess
import sys
import time
from typing import Any, Callable, Generator, Iterable, Mapping, NoReturn, Optional, Union

# iso 639-1
import languages.en
import libraries.file
import libraries.log
import libraries.pyinstall
import libraries.singleton
import modules.wallhaven
# sys.platform
import platforms.win32 as platform
import utils

POLL_TIMEOUT = 0.01
DELETE_TIMEOUT = 3
EXIT_TIMEOUT = 7
MAX_CACHE = 64 * 1024 * 1024
MAX_LENGTH = 64

NAME = 'Wallpyper'
ARG_CHANGE = 'change'
ARG_WAIT = 'wait'
CONFIG_CHANGE = 'auto_change'
CONFIG_INTERVAL = 'change_interval'
CONFIG_SAVE = 'save_wallpaper'
CONFIG_DIR = 'save_dir'
CONFIG_ANIMATE = 'animate'
CONFIG_NOTIFY = 'notify'
CONFIG_CACHE = 'keep_cache'
CONFIG_START = 'auto_start'
CONFIG_CONFIG = 'save_settings'

LANGUAGES = (languages.en,)
LANGUAGE = LANGUAGES[0]
MODULES = (modules.wallhaven,)
MODULE = MODULES[0]
DEFAULT_CONFIG = {
    CONFIG_CHANGE: False,
    CONFIG_INTERVAL: 3600,
    CONFIG_SAVE: False,
    CONFIG_DIR: utils.join_path(platform.PICTURES_DIR, NAME),
    CONFIG_ANIMATE: True,
    CONFIG_NOTIFY: True,
    CONFIG_CACHE: False,
    CONFIG_START: False,
    CONFIG_CONFIG: False
}

UUID = 'a0447fd8-0fea-4bdb-895e-fb83ad817cae'
RES_PATHS = tuple(utils.join_path(utils.dir_name(__file__), 'resources', name) for name in ('icon.png', 'loading.gif'))
TEMP_DIR = utils.join_path(platform.TEMP_DIR, NAME)
CONFIG_PATH = fr'D:\Projects\Wallpyper\{NAME}.ini'  # utils.join_path(platform.APPDATA_DIR, f'{NAME}.ini')
LOG_PATH = utils.replace_extension(CONFIG_PATH, 'log')
SEARCH_URL = 'https://www.google.com/searchbyimage/upload'
INTERVALS = '5 Minute', '15 Minute', '30 Minute', '1 Hour', '3 Hour', '6 Hour'

CONFIG = {}
URLS = collections.deque(maxlen=MAX_LENGTH)
URL_INDEX = [-1]
ENABLE_PREVIOUS = utils.dummy_func
SET_NEXT_LABEL = utils.dummy_func
SET_PREVIOUS_LABEL = utils.dummy_func
TIMER = utils.timer(utils.dummy_func)


def _load_config(getters: dict[type, Callable[[str, str], Union[str, int, float, bool]]],
                 section: str, config: dict[str, Union[str, int, float, bool]],
                 default: dict[str, Union[str, int, float, bool]]) -> bool:
    loaded = True
    for option, value in default.items():
        try:
            config[option] = getters[type(value)](section, option)
        except (ValueError, TypeError, configparser.NoSectionError, configparser.NoOptionError):
            config[option] = value
            loaded = False
    return loaded


def load_config() -> bool:  # TODO: verify config
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


def save_config() -> bool:  # TODO: save recently set wallpaper (?)
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
    utils.animate(RES_PATHS[1], LANGUAGE.CHANGING)
    if progress_callback:
        progress_callback(0, *args or (), **kwargs or {})
    if not url:
        url = MODULE.get_next_url()
        if url:
            URLS.append(url)
    if url:
        temp_path = utils.join_path(TEMP_DIR, utils.file_name(url))
        changed = utils.download_url(url, temp_path, chunk_count=100, on_write=progress_callback,
                                     args=args, kwargs=kwargs) and platform.set_wallpaper_ex(temp_path)
    else:
        changed = False
    if progress_callback:
        progress_callback(100, *args or (), **kwargs or {})
    utils.inanimate(LANGUAGE.CHANGING)
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
    utils.animate(RES_PATHS[1], LANGUAGE.SAVING)
    saved = any(utils.copy_file(path, utils.join_path(CONFIG[CONFIG_DIR], utils.file_name(path))) for path in
                _get_wallpaper_paths())
    utils.inanimate(LANGUAGE.SAVING)
    return saved


@utils.single
def search_wallpaper() -> bool:
    searched = False
    utils.animate(RES_PATHS[1], LANGUAGE.SEARCHING)
    for path in _get_wallpaper_paths():
        location = utils.upload_url(SEARCH_URL, files={'encoded_image': (None, path)}).get_header('location')
        if location:
            utils.open_browser(location)
            searched = True
            break
    utils.inanimate(LANGUAGE.SEARCHING)
    return searched


@utils.thread
def on_change(previous: Optional[bool] = None) -> bool:
    if previous:
        index = URL_INDEX[0] - 1
        url = URLS[URL_INDEX[0] - 1]
        set_label = SET_PREVIOUS_LABEL
        label = LANGUAGE.PREVIOUS
    else:
        index = URL_INDEX[0] + 1
        url = None if index == len(URLS) else URLS[index]
        set_label = SET_NEXT_LABEL
        label = LANGUAGE.NEXT
    changed = change_wallpaper(url, set_label)
    set_label(-1)
    ENABLE_PREVIOUS(index > 0)
    if changed:
        URL_INDEX[0] = index
        if CONFIG[CONFIG_SAVE]:
            save_wallpaper()
    elif CONFIG[CONFIG_NOTIFY]:
        utils.notify(label, LANGUAGE.FAILED_CHANGING)
    return changed


def on_auto_change(checked: bool, enable_submenu: Optional[Callable[[bool], None]] = None) -> None:
    CONFIG[CONFIG_CHANGE] = checked
    if enable_submenu is not None:
        enable_submenu(checked)
    TIMER.start(CONFIG[CONFIG_INTERVAL]) if checked else TIMER.stop()


def on_interval(interval: str) -> None:
    CONFIG[CONFIG_INTERVAL] = int(utils.timedelta(interval))
    on_auto_change(CONFIG[CONFIG_CHANGE])


@utils.thread
def on_save() -> bool:
    saved = save_wallpaper()
    if not saved and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANGUAGE.SAVE, LANGUAGE.FAILED_SAVING)
    return saved


def on_modify_save() -> None:
    utils.not_implemented(LANGUAGE.MODIFY_SAVE)


def on_open_explorer() -> bool:
    opened = utils.try_any(_get_wallpaper_paths(), platform.open_file_path)
    if not opened and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANGUAGE.OPEN_EXPLORER, LANGUAGE.FAILED_OPENING_EXPLORER)
    return opened


def on_open() -> bool:
    opened = utils.try_any(_get_wallpaper_paths(), platform.open_file)
    if not opened and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANGUAGE.OPEN, LANGUAGE.FAILED_OPENING)
    return opened


def on_copy_path() -> bool:
    copied = utils.try_any(_get_wallpaper_paths(), platform.copy_text, '"')
    if not copied and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANGUAGE.COPY_PATH, LANGUAGE.FAILED_COPYING_PATH)
    return copied


def on_copy() -> bool:
    copied = utils.try_any(_get_wallpaper_paths(), platform.copy_image)
    if not copied and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANGUAGE.COPY, LANGUAGE.FAILED_COPYING)
    return copied


@utils.thread
def on_search() -> bool:
    searched = search_wallpaper()
    if not searched and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANGUAGE.SEARCH, LANGUAGE.FAILED_SEARCHING)
    return searched


def _get_launch_argv() -> list[str]:
    argv = [sys.executable]
    if not libraries.pyinstall.FROZEN:
        argv.append(utils.abs_path(__file__))
    return argv


def on_shortcut() -> bool:
    created = (platform.create_link(utils.join_path(platform.DESKTOP_DIR, f'{NAME}.lnk'),
                                    *_get_launch_argv(), comment=LANGUAGE.DESCRIPTION))
    if not created and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANGUAGE.SHORTCUT, LANGUAGE.FAILED_SHORTCUT)
    return created


@utils.thread
def on_clear() -> bool:
    cleared = utils.delete(TEMP_DIR, True)
    if not cleared and CONFIG[CONFIG_NOTIFY]:
        utils.notify(LANGUAGE.CLEAR, LANGUAGE.FAILED_CLEARING)
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
        return platform.register_autorun(NAME, *_get_launch_argv(), *(ARG_CHANGE,) if CONFIG[CONFIG_CHANGE] else ())
    return platform.unregister_autorun(NAME)


def on_save_config(checked: bool) -> None:
    CONFIG[CONFIG_CONFIG] = checked
    save_config() if checked else utils.delete(CONFIG_PATH)


def on_about() -> None:
    utils.not_implemented(LANGUAGE.ABOUT)


@utils.thread
def on_exit() -> None:
    TIMER.stop()
    utils.disable()
    if change_wallpaper.is_running() or save_wallpaper.is_running() or search_wallpaper.is_running():
        if CONFIG[CONFIG_NOTIFY]:
            utils.notify(LANGUAGE.QUIT, LANGUAGE.FAILED_QUITING)
        end_time = time.time() + EXIT_TIMEOUT
        while end_time > time.time() and (
                change_wallpaper.is_running() or save_wallpaper.is_running() or search_wallpaper.is_running()):
            time.sleep(POLL_TIMEOUT)
    utils.stop()


def create_menu() -> None:  # TODO: slideshow (smaller timer)
    update_config = utils.call_after(utils.reverse, True, True)(CONFIG.__setitem__)
    next_wallpaper = utils.add_item(LANGUAGE.NEXT, on_click=on_change)
    previous_wallpaper = utils.add_item(LANGUAGE.PREVIOUS, enable=False, on_click=on_change, args=(True,))

    def set_next_label(progress: int) -> None:
        next_wallpaper.SetItemLabel(f'{LANGUAGE.NEXT} ({progress:03}%)' if progress >= 0 else f'{LANGUAGE.NEXT}')

    def set_previous_label(progress: int) -> None:
        previous_wallpaper.SetItemLabel(
            f'{LANGUAGE.PREVIOUS} ({progress:03}%)' if progress >= 0 else f'{LANGUAGE.PREVIOUS}')

    global ENABLE_PREVIOUS, SET_NEXT_LABEL, SET_PREVIOUS_LABEL, TIMER
    ENABLE_PREVIOUS = previous_wallpaper.Enable
    SET_NEXT_LABEL = set_next_label
    SET_PREVIOUS_LABEL = set_previous_label
    TIMER = utils.timer(on_change, interval=CONFIG[CONFIG_INTERVAL])
    utils.add_separator()
    interval_submenu = utils.add_submenu(LANGUAGE.SUBMENU_INTERVAL, CONFIG[CONFIG_CHANGE])
    for interval in INTERVALS:
        utils.add_item(interval, utils.item.RADIO, CONFIG[CONFIG_INTERVAL] == int(utils.timedelta(interval)),
                       on_click=on_interval, extra_args=(utils.get_property.LABEL,), menu=interval_submenu)
    utils.add_item(LANGUAGE.AUTO_CHANGE, utils.item.CHECK, CONFIG[CONFIG_CHANGE], on_click=on_auto_change,
                   args=(interval_submenu.Enable,), extra_args=(utils.get_property.CHECKED,), position=3)
    utils.add_separator()
    utils.add_item(LANGUAGE.SAVE, on_click=on_save)
    utils.add_item(LANGUAGE.AUTO_SAVE, utils.item.CHECK, CONFIG[CONFIG_SAVE], on_click=update_config,
                   args=(CONFIG_SAVE,),
                   extra_args=(utils.get_property.CHECKED,))
    utils.add_item(LANGUAGE.MODIFY_SAVE, on_click=on_modify_save)
    utils.add_separator()
    open_submenu = utils.add_submenu(LANGUAGE.SUBMENU_OPEN)
    utils.add_item(LANGUAGE.OPEN_EXPLORER, on_click=on_open_explorer, menu=open_submenu)
    utils.add_item(LANGUAGE.OPEN, on_click=on_open, menu=open_submenu)
    copy_submenu = utils.add_submenu(LANGUAGE.SUBMENU_COPY)
    utils.add_item(LANGUAGE.COPY_PATH, on_click=on_copy_path, menu=copy_submenu)
    utils.add_item(LANGUAGE.COPY, on_click=on_copy, menu=copy_submenu)
    utils.add_item(LANGUAGE.SEARCH, on_click=on_search)
    utils.add_separator()
    MODULE.create_menu()  # TODO: separate left click menu (?)
    utils.add_separator()
    actions_submenu = utils.add_submenu(LANGUAGE.SUBMENU_ACTIONS)
    utils.add_item(LANGUAGE.SHORTCUT, on_click=on_shortcut, menu=actions_submenu)
    utils.add_item(LANGUAGE.CLEAR, on_click=on_clear, menu=actions_submenu)
    utils.add_item(LANGUAGE.RESET, on_click=on_reset, menu=actions_submenu)
    utils.add_item(LANGUAGE.RESTART, on_click=on_restart, menu=actions_submenu)
    config_submenu = utils.add_submenu(LANGUAGE.SUBMENU_CONFIG)
    utils.add_item(LANGUAGE.ANIMATE, utils.item.CHECK, CONFIG[CONFIG_ANIMATE], on_click=on_animate,
                   extra_args=(utils.get_property.CHECKED,), menu=config_submenu)
    utils.add_item(LANGUAGE.NOTIFY, utils.item.CHECK, CONFIG[CONFIG_NOTIFY], on_click=update_config,
                   args=(CONFIG_NOTIFY,),
                   extra_args=(utils.get_property.CHECKED,), menu=config_submenu)
    utils.add_item(LANGUAGE.KEEP_CACHE, utils.item.CHECK, CONFIG[CONFIG_CACHE], on_click=update_config,
                   args=(CONFIG_CACHE,), extra_args=(utils.get_property.CHECKED,), menu=config_submenu)
    utils.add_item(LANGUAGE.AUTO_START, utils.item.CHECK, CONFIG[CONFIG_START], on_click=on_auto_start,
                   extra_args=(utils.get_property.CHECKED,), menu=config_submenu)
    utils.add_item(LANGUAGE.KEEP_CONFIG, utils.item.CHECK, CONFIG[CONFIG_CONFIG], on_click=on_save_config,
                   extra_args=(utils.get_property.CHECKED,), menu=config_submenu)
    utils.add_item(LANGUAGE.ABOUT, on_click=on_about)
    utils.add_item(LANGUAGE.QUIT, on_click=on_exit)


def start() -> None:  # TODO: dark theme
    libraries.singleton.init(NAME, UUID, ARG_WAIT in sys.argv, on_crash=print, on_crash_args=('Crash',), on_wait=print,
                             on_wait_args=('Wait',), on_exit=print, on_exit_args=('Exit',))
    if 'debug' in sys.argv:
        libraries.log.redirect_stdio(LOG_PATH, True) if libraries.pyinstall.FROZEN else libraries.log.dump_on_exception(
            LOG_PATH)
        libraries.log.init(utils.file_name(__file__), utils.file_name(utils.__file__),
                           utils.re_join_path('libraries', r'.*\.py'), utils.re_join_path('modules', r'.*\.py'),
                           utils.re_join_path('platforms', r'.*\.py'), level=libraries.log.Level.INFO, skip_comp=True)
    libraries.pyinstall.clean_temp()
    utils.make_dirs(TEMP_DIR)
    utils.trim_dir(TEMP_DIR, MAX_CACHE)
    load_config()
    create_menu()
    on_auto_change(CONFIG[CONFIG_CHANGE])
    on_animate(CONFIG[CONFIG_ANIMATE])
    on_auto_start(CONFIG[CONFIG_START])
    on_save_config(CONFIG[CONFIG_CONFIG])
    if ARG_CHANGE in sys.argv:  # TODO: store last update, change if now >= last + interval
        on_change()
    utils.start(RES_PATHS[0], NAME, on_change)


def stop() -> None:
    utils.timer.kill_all()
    on_auto_start(CONFIG[CONFIG_START])
    on_save_config(CONFIG[CONFIG_CONFIG])
    utils.trim_dir(TEMP_DIR, MAX_CACHE) if CONFIG[CONFIG_CACHE] else utils.delete(TEMP_DIR, True, DELETE_TIMEOUT)
    if utils.exists_dir(TEMP_DIR) and utils.is_empty_dir(TEMP_DIR, True):
        utils.delete(TEMP_DIR, True)


def main() -> NoReturn:
    start()
    stop()
    sys.exit()


if __name__ == '__main__':
    main()
