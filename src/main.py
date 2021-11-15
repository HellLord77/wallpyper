__version__ = '0.1.9'  # TODO: error, avoid condition

import configparser
import sys
import time
from typing import Any, Callable, Generator, Iterable, Mapping, NoReturn, Optional, Union

import wx  # TODO: hide wx, add updater

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

NAME = 'wallpyper'
CHANGE = 'auto_change'
INTERVAL = 'change_interval'
SAVE = 'save_wallpaper'
SAVE_DIR = 'save_dir'
ANIMATE = 'animate'
NOTIFY = 'notify'
KEEP_CACHE = 'keep_cache'
START = 'auto_start'
SAVE_DATA = 'save_config'

DELAY = 0.01
DELETE_TIMEOUT = 3
EXIT_TIMEOUT = 7
MAX_CACHE = 64 * 1024 * 1024

LANGUAGES = (languages.en,)
LANGUAGE = LANGUAGES[0]
MODULES = (modules.wallhaven,)
MODULE = MODULES[0]
DEFAULT_CONFIG = {
    CHANGE: False,
    INTERVAL: 3600,
    SAVE: False,
    SAVE_DIR: utils.join_path(platform.PICTURES_DIR, NAME),
    ANIMATE: True,
    NOTIFY: True,
    KEEP_CACHE: False,
    START: False,
    SAVE_DATA: False
}

UUID = 'a0447fd8-0fea-4bdb-895e-fb83ad817cae'
RES_PATHS = tuple(utils.join_path(utils.dir_name(__file__), 'resources', name) for name in ('icon.png', 'loading.gif'))
TEMP_DIR = utils.join_path(platform.TEMP_DIR, NAME)
CONFIG_PATH = f'D:\\Projects\\wallpyper\\{NAME}.ini'  # utils.join_path(platform.APPDATA_DIR, f'{NAME}.ini')
LOG_PATH = utils.replace_extension(CONFIG_PATH, 'log')
SEARCH_URL = 'https://www.google.com/searchbyimage/upload'
INTERVALS = {
    '300': '5 Minute',
    '900': '15 Minute',
    '1800': '30 Minute',
    '3600': '1 Hour',
    '10800': '3 Hour',
    '21600': '6 Hour'
}

CONFIG = {}
ON_WRITE = utils.dummy_func
TIMER = utils.timer(ON_WRITE)


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


def load_config() -> bool:  # TODO: verify config
    parser = configparser.ConfigParser()
    try:
        loaded = bool(parser.read(CONFIG_PATH))
    except configparser.MissingSectionHeaderError:
        loaded = False
    getters = {
        str: parser.get,
        int: parser.getint,
        float: parser.getfloat,
        bool: parser.getboolean
    }
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
def change_wallpaper(on_write: Optional[Callable[[int, ...], Any]] = None, args: Optional[Iterable] = None,
                     kwargs: Optional[Mapping[str, Any]] = None) -> bool:
    utils.animate(RES_PATHS[1], LANGUAGE.CHANGING)
    if on_write:
        on_write(0, *args or (), **kwargs or {})
    url = MODULE.get_next_url()
    name = utils.file_name(url)
    temp_path = utils.join_path(TEMP_DIR, name)
    save_path = utils.join_path(CONFIG[SAVE_DIR], name)
    utils.download_url(url, temp_path, chunk_count=100, on_write=on_write, args=args, kwargs=kwargs)
    changed = platform.set_wallpaper_ex(temp_path, save_path)
    if on_write:
        on_write(100, *args or (), **kwargs or {})
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
    saved = any(utils.copy_file(path, utils.join_path(
        CONFIG[SAVE_DIR], utils.file_name(path))) for path in _get_wallpaper_paths())
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
def on_change() -> bool:
    changed = change_wallpaper(ON_WRITE)
    ON_WRITE(-1)
    if changed:
        if CONFIG[SAVE]:
            save_wallpaper()
    elif CONFIG[NOTIFY]:
        utils.notify(LANGUAGE.CHANGE, LANGUAGE.FAILED_CHANGING)
    return changed


def on_auto_change(checked: bool, change_interval: Optional[wx.MenuItem] = None) -> None:
    CONFIG[CHANGE] = checked
    if change_interval:
        change_interval.Enable(True)
    TIMER.start(CONFIG[INTERVAL]) if checked else TIMER.stop()


def on_change_interval(interval: str) -> None:
    CONFIG[INTERVAL] = int(interval)
    on_auto_change(CONFIG[CHANGE])


@utils.thread
def on_save() -> bool:
    saved = save_wallpaper()
    if not saved and CONFIG[NOTIFY]:
        utils.notify(LANGUAGE.SAVE, LANGUAGE.FAILED_SAVING)
    return saved


def on_modify_save():
    platform.show_balloon(LANGUAGE.MODIFY_SAVE, str(NotImplemented))


def on_copy() -> bool:
    copied = any(platform.copy_image(path) for path in _get_wallpaper_paths())
    if not copied and CONFIG[NOTIFY]:
        utils.notify(LANGUAGE.COPY, LANGUAGE.FAILED_COPYING)
    return copied


def on_copy_path() -> bool:
    copied = any(platform.copy_text(path) for path in _get_wallpaper_paths())
    if not copied and CONFIG[NOTIFY]:
        utils.notify(LANGUAGE.COPY_PATH, LANGUAGE.FAILED_COPYING_PATH)
    return copied


@utils.thread
def on_search() -> bool:
    searched = search_wallpaper()
    if not searched and CONFIG[NOTIFY]:
        utils.notify(LANGUAGE.SEARCH, LANGUAGE.FAILED_SEARCHING)
    return searched


def on_animate(checked: bool) -> None:
    CONFIG[ANIMATE] = checked
    utils.pause_animation(not checked)


def on_auto_start(checked: bool) -> bool:
    CONFIG[START] = checked
    if checked:
        return platform.register_autorun(NAME, sys.argv[0], *('change',) if CONFIG[CHANGE] else ())
    return platform.unregister_autorun(NAME)


def on_save_config(checked: bool) -> None:
    CONFIG[SAVE_DATA] = checked
    save_config() if checked else utils.delete(CONFIG_PATH)


@utils.thread
def on_exit() -> None:
    TIMER.stop()
    utils.disable()
    if change_wallpaper.is_running() or save_wallpaper.is_running() or search_wallpaper.is_running():
        if CONFIG[NOTIFY]:
            utils.notify(LANGUAGE.QUIT, LANGUAGE.FAILED_QUITING)
        end_time = time.time() + EXIT_TIMEOUT
        while end_time > time.time() and (
                change_wallpaper.is_running() or save_wallpaper.is_running() or search_wallpaper.is_running()):
            time.sleep(DELAY)
    utils.stop()


def create_menu() -> None:  # TODO: previous wallpaper, slideshow (smaller timer)
    update_config = utils.call_after(utils.reverse, True, True)(CONFIG.__setitem__)
    change = utils.add_item(LANGUAGE.CHANGE, on_click=on_change)

    def set_item_label(progress: int) -> None:
        change.SetItemLabel(f'{LANGUAGE.CHANGING} ({progress:03}%)' if progress >= 0 else f'{LANGUAGE.CHANGE}')

    global ON_WRITE, TIMER
    ON_WRITE = set_item_label
    TIMER = utils.timer(on_change, interval=CONFIG[INTERVAL])
    change_interval = utils.add_items(LANGUAGE.CHANGE_INTERVAL, utils.item.RADIO, (str(
        CONFIG[INTERVAL]),), CONFIG[CHANGE], INTERVALS, on_change_interval, extra_args=(utils.get_property.UID,))
    utils.add_item(LANGUAGE.AUTO_CHANGE, utils.item.CHECK, CONFIG[CHANGE], on_click=on_auto_change,
                   args=(change_interval,), extra_args=(utils.get_property.CHECKED,), position=1)
    utils.add_separator()
    utils.add_item(LANGUAGE.SAVE, on_click=on_save)
    utils.add_item(LANGUAGE.AUTO_SAVE, utils.item.CHECK, CONFIG[SAVE],
                   on_click=update_config, args=(SAVE,), extra_args=(utils.get_property.CHECKED,))
    utils.add_item(LANGUAGE.MODIFY_SAVE, on_click=on_modify_save)
    utils.add_separator()
    utils.add_item(LANGUAGE.COPY, on_click=on_copy)
    utils.add_item(LANGUAGE.COPY_PATH, on_click=on_copy_path)
    utils.add_item(LANGUAGE.SEARCH, on_click=on_search)
    utils.add_separator()
    MODULE.create_menu()  # TODO: separate left click menu (?)
    utils.add_separator()
    utils.add_item(LANGUAGE.ANIMATE, utils.item.CHECK, CONFIG[ANIMATE],
                   on_click=on_animate, extra_args=(utils.get_property.CHECKED,))
    utils.add_item(LANGUAGE.NOTIFY, utils.item.CHECK, CONFIG[NOTIFY],
                   on_click=update_config, args=(NOTIFY,), extra_args=(utils.get_property.CHECKED,))
    utils.add_item(LANGUAGE.KEEP_CACHE, utils.item.CHECK, CONFIG[KEEP_CACHE],
                   on_click=update_config, args=(KEEP_CACHE,), extra_args=(utils.get_property.CHECKED,))
    utils.add_item(LANGUAGE.AUTO_START, utils.item.CHECK, CONFIG[START],
                   on_click=on_auto_start, extra_args=(utils.get_property.CHECKED,))
    utils.add_item(LANGUAGE.SAVE_CONFIG, utils.item.CHECK, CONFIG[SAVE_DATA],
                   on_click=on_save_config, extra_args=(utils.get_property.CHECKED,))
    utils.add_item(LANGUAGE.QUIT, on_click=on_exit)


def start() -> None:  # TODO: dark theme
    libraries.singleton.init(NAME, UUID, 'wait' in sys.argv, on_crash=print, on_crash_args=('Crash',),
                             on_wait=print, on_wait_args=('Wait',), on_exit=print, on_exit_args=('Exit',))
    if 'debug' in sys.argv:
        libraries.log.redirect_stdio(
            LOG_PATH, True) if libraries.pyinstall.FROZEN else libraries.log.dump_on_exception(LOG_PATH)
        libraries.log.init(utils.file_name(__file__), utils.file_name(utils.__file__),
                           utils.re_join_path('libraries', r'.*\.py'), utils.re_join_path('modules', r'.*\.py'),
                           utils.re_join_path('platforms', r'.*\.py'), level=libraries.log.Level.INFO, skip_comp=True)
    libraries.pyinstall.clean_temp()
    load_config()
    create_menu()
    utils.make_dirs(TEMP_DIR)
    utils.trim_dir(TEMP_DIR, MAX_CACHE)
    on_auto_change(CONFIG[CHANGE])
    on_animate(CONFIG[ANIMATE])
    on_auto_start(CONFIG[START])
    on_save_config(CONFIG[SAVE_DATA])
    if 'change' in sys.argv:  # TODO: store last update, change if now >= last + interval
        on_change()
    utils.start(RES_PATHS[0], NAME, on_change)


def stop() -> None:
    utils.timer.kill_all()
    on_auto_start(CONFIG[START])
    on_save_config(CONFIG[SAVE_DATA])
    utils.trim_dir(TEMP_DIR, MAX_CACHE) if CONFIG[KEEP_CACHE] else utils.delete(TEMP_DIR, True, DELETE_TIMEOUT)
    if utils.exists_dir(TEMP_DIR) and utils.is_empty_dir(TEMP_DIR, True):
        utils.delete(TEMP_DIR, True)


def main() -> NoReturn:
    start()
    stop()
    sys.exit()


if __name__ == '__main__':
    main()
