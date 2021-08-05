__version__ = '0.1.3'

import configparser
import functools
import os
import sys
import time
import typing
import webbrowser

import wx

# iso 639-1
import languages.en
import libraries.log
import libraries.pyinstall
import libraries.singleton
import modules.wallhaven
# sys.platform
import platforms.win32 as platform
import utils

NAME = 'wallpyper'
CHANGE = 'auto_change_wallpaper'
INTERVAL = 'auto_change_interval'
SAVE = 'auto_save_wallpaper'
SAVE_DIR = 'save_dir'
NOTIFY = 'notify_on_fail'
KEEP_CACHE = 'keep_cache'
START = 'auto_start'
SAVE_DATA = 'auto_save_config'

LANGUAGES = (languages.en,)
LANGUAGE = LANGUAGES[0]
MODULES = (modules.wallhaven,)
MODULE = MODULES[0]
DEFAULT_CONFIG: dict[str, typing.Union[str, int, float, bool]] = {
    CHANGE: False,
    INTERVAL: 3600,
    SAVE: False,
    SAVE_DIR: utils.join_path(platform.PICTURES_DIR, NAME),
    NOTIFY: False,
    KEEP_CACHE: False,
    START: False,
    SAVE_DATA: False}

RES_PATHS = tuple(utils.join_path(os.path.dirname(__file__), 'resources', name) for name in ('icon.png', 'loading.gif'))
TEMP_DIR = utils.join_path(platform.TEMP_DIR, NAME)  # utils.join_path(platform.APPDATA_DIR, f'{NAME}.ini')
CONFIG_PATH = utils.join_path('E:\\Projects\\wallpyper\\config.ini')
LOG_PATH = utils.join_path(os.path.dirname(CONFIG_PATH), 'debug.log')
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


class Change:
    CALLBACK = None
    TIMER = None


def _load_config(config_parser: configparser.ConfigParser,
                 section: str,
                 config: dict[str, typing.Union[str, int, float, bool]],
                 default_config: dict[str, typing.Union[str, int, float, bool]]) -> bool:
    loaded = True
    getters = {
        str: config_parser.get,
        int: config_parser.getint,
        float: config_parser.getfloat,
        bool: config_parser.getboolean
    }
    config.update(default_config)
    if config_parser.has_section(section):
        for option, value in default_config.items():
            if config_parser.has_option(section, option):
                try:
                    # noinspection PyArgumentList
                    config[option] = getters[type(value)](section, option)
                except TypeError:
                    loaded = False
            else:
                loaded = False
    else:
        loaded = False
    return loaded


def load_config() -> bool:  # TODO: verify config
    loaded = True
    config_parser = configparser.ConfigParser()
    try:
        config_parser.read(CONFIG_PATH)
    except configparser.MissingSectionHeaderError:
        loaded = False
    loaded = _load_config(config_parser, NAME, CONFIG, DEFAULT_CONFIG) and loaded
    for module in MODULES:
        loaded = _load_config(config_parser, module.NAME, module.CONFIG, module.DEFAULT_CONFIG) and loaded
    return loaded


def save_config() -> bool:
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
    return saved and utils.exists_file(CONFIG_PATH)


def update_config(value: typing.Any,
                  key: str) -> None:
    CONFIG.__setitem__(key, value)


@utils.single
def change_wallpaper(callback: typing.Optional[typing.Callable[[int, ...], typing.Any]] = None,
                     callback_args: typing.Optional[tuple] = None,
                     callback_kwargs: typing.Optional[dict[str, typing.Any]] = None) -> bool:
    utils.animate(RES_PATHS[1], LANGUAGE.CHANGING)
    if callback:
        callback(0, *callback_args or (), **callback_kwargs or {})
    url = MODULE.get_next_url()
    name = os.path.basename(url)
    temp_path = utils.join_path(TEMP_DIR, name)
    save_path = utils.join_path(CONFIG[SAVE_DIR], name)
    utils.download_url(url, temp_path, chunk_count=100,
                       callback=callback, callback_args=callback_args, callback_kwargs=callback_kwargs)
    changed = platform.set_wallpaper_ex(temp_path, save_path)
    if callback:
        callback(100, *callback_args or (), **callback_kwargs or {})
    utils.inanimate(LANGUAGE.CHANGING)
    return changed


def _get_wallpaper_paths() -> typing.Generator[str, None, None]:
    path = platform.get_wallpaper_path()
    if utils.exists_file(path):
        yield path
    temp_path = utils.join_path(TEMP_DIR, os.path.basename(path))
    if utils.exists_file(temp_path):
        yield temp_path
    if os.path.isdir(platform.WALLPAPER_DIR):
        for name in os.listdir(platform.WALLPAPER_DIR):
            if utils.copy_file(utils.join_path(platform.WALLPAPER_DIR, name), temp_path):
                yield temp_path


@utils.single
def save_wallpaper() -> bool:
    utils.animate(RES_PATHS[1], LANGUAGE.SAVING)
    saved = any(utils.copy_file(path, utils.join_path(CONFIG[SAVE_DIR], os.path.basename(path))) for path in
                _get_wallpaper_paths())
    utils.inanimate(LANGUAGE.SAVING)
    return saved


@utils.single
def search_wallpaper() -> bool:  # TODO: fix change + search
    searched = False
    utils.animate(RES_PATHS[1], LANGUAGE.SEARCHING)
    for path in _get_wallpaper_paths():
        location = utils.upload_url(SEARCH_URL, files={'encoded_image': (None, path)}).get_header('location')
        if location:
            webbrowser.open(location)
            searched = True
            break
    utils.inanimate(LANGUAGE.SEARCHING)
    return searched


@utils.thread
def on_change() -> bool:
    changed = change_wallpaper(Change.CALLBACK)
    if changed:
        if CONFIG[SAVE]:
            save_wallpaper()
    elif CONFIG[NOTIFY]:
        utils.notify(LANGUAGE.CHANGE, LANGUAGE.FAILED_CHANGING)
    return changed


def on_auto_change(is_checked: bool, change_interval: typing.Optional[wx.MenuItem] = None) -> None:
    CONFIG[CHANGE] = is_checked
    if change_interval:
        change_interval.Enable(True)
    Change.TIMER.start(CONFIG[INTERVAL]) if is_checked else Change.TIMER.stop()


def on_change_interval(interval: str) -> None:
    CONFIG[INTERVAL] = int(interval)
    on_auto_change(CONFIG[CHANGE])


@utils.thread
def on_save() -> bool:
    saved = save_wallpaper()
    if CONFIG[NOTIFY] and not saved:
        utils.notify(LANGUAGE.SAVE, LANGUAGE.FAILED_SAVING)
    return saved


def on_modify_save():
    utils.notify(LANGUAGE.MODIFY_SAVE, 'Unimplemented')


def on_copy() -> bool:
    copied = any(platform.copy_image(path) for path in _get_wallpaper_paths())
    if CONFIG[NOTIFY] and not copied:
        utils.notify(LANGUAGE.COPY, LANGUAGE.FAILED_COPYING)
    return copied


def on_copy_path() -> bool:
    copied = any(platform.copy_text(path) for path in _get_wallpaper_paths())
    if CONFIG[NOTIFY] and not copied:
        utils.notify(LANGUAGE.COPY_PATH, LANGUAGE.FAILED_COPYING_PATH)
    return copied


@utils.thread
def on_search() -> bool:
    searched = search_wallpaper()
    if CONFIG[NOTIFY] and not searched:
        utils.notify(LANGUAGE.SEARCH, LANGUAGE.FAILED_SEARCHING)
    return searched


def on_auto_start(is_checked: bool) -> bool:
    CONFIG[START] = is_checked
    if is_checked:
        args = set(('change',) if CONFIG[CHANGE] else ())
        return platform.register_autorun(NAME, os.path.realpath(sys.argv[0]), *args)
    return platform.unregister_autorun(NAME)


def on_save_config(is_checked: bool) -> None:
    CONFIG[SAVE_DATA] = is_checked
    save_config() if is_checked else utils.delete_file(CONFIG_PATH)


@utils.thread
def on_exit():
    Change.TIMER.stop()
    utils.disable()
    if CONFIG[NOTIFY] and (
            change_wallpaper.is_running() or save_wallpaper.is_running() or search_wallpaper.is_running()):
        utils.notify(LANGUAGE.QUIT, LANGUAGE.FAILED_QUITING)
    while change_wallpaper.is_running() or save_wallpaper.is_running() or search_wallpaper.is_running():
        time.sleep(0.1)
    utils.stop()


def create_menu() -> None:
    change = utils.add_item(LANGUAGE.CHANGE, callback=on_change)

    @functools.wraps(change.SetItemLabel)
    def wrapper(progress: int):
        if progress < 100:
            change.SetItemLabel(f'{LANGUAGE.CHANGING} ({progress:02}%)')
        else:
            change.SetItemLabel(f'{LANGUAGE.CHANGE}')

    Change.CALLBACK = wrapper
    Change.TIMER = utils.timer(on_change, interval=CONFIG[INTERVAL])
    change_interval = utils.add_items(LANGUAGE.CHANGE_INTERVAL, utils.item.RADIO, (str(CONFIG[INTERVAL]),),
                                      CONFIG[CHANGE], INTERVALS, on_change_interval,
                                      builtin_args=(utils.get_property.UID,))
    utils.add_item(LANGUAGE.AUTO_CHANGE, utils.item.CHECK, CONFIG[CHANGE], callback=on_auto_change,
                   callback_args=(change_interval,), builtin_args=(utils.get_property.CHECKED,), position=1)
    utils.add_separator()
    utils.add_item(LANGUAGE.SAVE, callback=on_save)
    utils.add_item(LANGUAGE.AUTO_SAVE, utils.item.CHECK, CONFIG[SAVE],
                   callback=update_config, callback_args=(SAVE,), builtin_args=(utils.get_property.CHECKED,))
    utils.add_item(LANGUAGE.MODIFY_SAVE, callback=on_modify_save)
    utils.add_separator()
    utils.add_item(LANGUAGE.COPY, callback=on_copy)
    utils.add_item(LANGUAGE.COPY_PATH, callback=on_copy_path)
    utils.add_item(LANGUAGE.SEARCH, callback=on_search)
    utils.add_separator()
    MODULE.create_menu()  # TODO: separate left click menu (?)
    utils.add_separator()
    utils.add_item(LANGUAGE.NOTIFY, utils.item.CHECK, CONFIG[NOTIFY],
                   callback=update_config, callback_args=(NOTIFY,), builtin_args=(utils.get_property.CHECKED,))
    utils.add_item(LANGUAGE.KEEP_CACHE, utils.item.CHECK, CONFIG[KEEP_CACHE],
                   callback=update_config, callback_args=(KEEP_CACHE,), builtin_args=(utils.get_property.CHECKED,))
    utils.add_item(LANGUAGE.AUTO_START, utils.item.CHECK, CONFIG[START],
                   callback=on_auto_start, builtin_args=(utils.get_property.CHECKED,))
    utils.add_item(LANGUAGE.SAVE_CONFIG, utils.item.CHECK, CONFIG[SAVE_DATA],
                   callback=on_save_config, builtin_args=(utils.get_property.CHECKED,))
    utils.add_item(LANGUAGE.QUIT, callback=on_exit)


def start() -> None:
    libraries.singleton.init(NAME, 'wait' in sys.argv,
                             crash_callback=print, crash_callback_args=('Crash',),
                             wait_callback=print, wait_callback_args=('Wait',),
                             exit_callback=print, exit_callback_args=('Exit',))
    if 'debug' in sys.argv:
        if libraries.pyinstall.FROZEN:
            libraries.log.redirect_stdio(LOG_PATH)
        libraries.log.init(__file__, utils.__file__, 'languages', 'libraries', 'modules', 'platforms')
    libraries.pyinstall.clean_temp()
    load_config()
    create_menu()
    utils.make_dirs(TEMP_DIR)
    on_auto_change(CONFIG[CHANGE])
    on_auto_start(CONFIG[START])
    on_save_config(CONFIG[SAVE_DATA])
    if 'change' in sys.argv:
        on_change()
    utils.start(RES_PATHS[0], NAME, on_change)


def stop() -> None:
    utils.timer.kill_all()
    on_auto_start(CONFIG[START])
    on_save_config(CONFIG[SAVE_DATA])
    if not CONFIG[KEEP_CACHE] or utils.is_empty_dir(TEMP_DIR):
        utils.delete_dir(TEMP_DIR)


def main() -> typing.NoReturn:
    start()
    stop()
    sys.exit()


if __name__ == '__main__':
    main()
