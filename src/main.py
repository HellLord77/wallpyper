import collections
import configparser
import contextlib
import copy
import functools
import itertools
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
from typing import Callable, Iterable, NoReturn, Optional

import consts
import gui
import langs
import pipe
import srcs
import win32
from libs import callables, easings, files, lens, log, pyinstall, singleton, spinners, timer, request, utils

UUID = f'{consts.AUTHOR}.{consts.NAME}'
RES_TEMPLATE = os.path.join(os.path.dirname(__file__), 'res', '{}')
CONFIG_PATH = fr'D:\Projects\wallpyper\{consts.NAME}.ini'
# CONFIG_PATH = os.path.join(win32.SAVE_DIR, f'{consts.NAME}.ini')  # TODO
LOG_PATH = files.replace_ext(CONFIG_PATH, 'log')
PIPE_PATH = files.replace_ext(pipe.__file__.removesuffix(sysconfig.get_config_var('EXT_SUFFIX')), 'exe')
TEMP_DIR = win32.display.TEMP_WALLPAPER_DIR = os.path.join(tempfile.gettempdir(), consts.NAME)

CHANGE_INTERVALS: tuple[int, int, int, int, int, int, int] = 0, 300, 900, 1800, 3600, 10800, 21600
TRANSITION_DURATIONS: tuple[float, float, float, float, float] = 0.5, 1.0, 2.5, 5.0, 10.0
MAXIMIZED_ACTIONS: tuple[
    str, str, str] = consts.MAXIMIZED_ACTION_IGNORE, consts.MAXIMIZED_ACTION_POSTPONE, consts.MAXIMIZED_ACTION_SKIP
EASE_STYLES: tuple[str, str, str, str, str, str, str] = (
    consts.EASE_STYLE_SINE, consts.EASE_STYLE_QUAD, consts.EASE_STYLE_CUBIC,
    consts.EASE_STYLE_QUART, consts.EASE_STYLE_QUINT, consts.EASE_STYLE_EXPO, consts.EASE_STYLE_CIRC)

win32.display.ANIMATION_POLL_INTERVAL = 0
win32.gui.FLAG_CACHE_BITMAP = True
gui.ANIMATION_PATH = RES_TEMPLATE.format(consts.RES_BUSY)

STRINGS = srcs.Source.strings = langs.DEFAULT
DISPLAYS: dict[str, tuple[str, tuple[int, int]]] = {}
RESTART = utils.MutableBool()
PROGRESS = utils.MutableFloat()
TIMER = timer.Timer.__new__(timer.Timer)
RECENT: collections.deque[files.File] = collections.deque(maxlen=consts.MAX_RECENT_LEN)
PIPE: pipe.StringNamedPipeClient = pipe.StringNamedPipeClient(f'{UUID}_{uuid.uuid4().hex}')

DEFAULT_CONFIG: dict[str, int | float | bool | str] = {
    consts.CONFIG_RECENT_LIST: f'\n{utils.encrypt(RECENT, split=True)}',
    consts.CONFIG_ACTIVE_DISPLAYS: consts.ALL_DISPLAY,
    consts.CONFIG_FIRST_RUN: consts.FEATURE_FIRST_RUN,
    consts.CONFIG_AUTO_SAVE: False,
    consts.CONFIG_SKIP_RECENT: False,
    consts.CONFIG_REAPPLY_IMAGE: True,
    consts.CONFIG_RESTORE_IMAGE: False,
    consts.CONFIG_NOTIFY_ERROR: True,
    consts.CONFIG_ANIMATE_ICON: True,
    consts.CONFIG_KEEP_CACHE: False,
    consts.CONFIG_AUTOSTART: False,
    consts.CONFIG_KEEP_SETTINGS: False,
    consts.CONFIG_NOTIFY_BLOCKED: True,
    consts.CONFIG_CHANGE_START: False,
    consts.CONFIG_EASE_IN: True,
    consts.CONFIG_EASE_OUT: True,
    consts.CONFIG_CHANGE_INTERVAL: CHANGE_INTERVALS[0],
    consts.CONFIG_TRANSITION_DURATION: TRANSITION_DURATIONS[2],
    consts.CONFIG_IF_MAXIMIZED: MAXIMIZED_ACTIONS[0],
    consts.CONFIG_TRANSITION_EASE: EASE_STYLES[2],
    consts.CONFIG_ACTIVE_SOURCE: next(iter(srcs.SOURCES)),
    consts.CONFIG_MENU_COLOR: win32.ColorMode[win32.ColorMode.AUTO],
    consts.CONFIG_SAVE_DIR: os.path.join(win32.PICTURES_DIR, consts.NAME),
    consts.CONFIG_FIT_STYLE: win32.display.Style[win32.display.Style.FILL],
    consts.CONFIG_ROTATE_BY: win32.display.Rotate[win32.display.Rotate.NONE],
    consts.CONFIG_FLIP_BY: win32.display.Flip[win32.display.Flip.NONE],
    consts.CONFIG_TRANSITION_STYLE: win32.display.Transition[win32.display.Transition.FADE]}
CURRENT_CONFIG: dict[str, int | float | bool | str] = {}


def update_config():
    CURRENT_CONFIG[consts.CONFIG_RECENT_LIST] = f'\n{utils.encrypt(RECENT, split=True)}'


def _fix_config(key: str, values: Iterable):
    utils.fix_dict_key(CURRENT_CONFIG, key, values, DEFAULT_CONFIG)


def fix_config():
    _fix_config(consts.CONFIG_MENU_COLOR, win32.ColorMode[1:])
    _fix_config(consts.CONFIG_FIT_STYLE, win32.display.Style)
    _fix_config(consts.CONFIG_ROTATE_BY, win32.display.Rotate)
    _fix_config(consts.CONFIG_FLIP_BY, win32.display.Flip)
    _fix_config(consts.CONFIG_TRANSITION_STYLE, win32.display.Transition)
    _fix_config(consts.CONFIG_ACTIVE_DISPLAYS, DISPLAYS)
    _fix_config(consts.CONFIG_CHANGE_INTERVAL, CHANGE_INTERVALS)
    _fix_config(consts.CONFIG_TRANSITION_DURATION, TRANSITION_DURATIONS)
    _fix_config(consts.CONFIG_IF_MAXIMIZED, MAXIMIZED_ACTIONS)
    _fix_config(consts.CONFIG_TRANSITION_EASE, EASE_STYLES)
    if not CURRENT_CONFIG[consts.CONFIG_SAVE_DIR]:
        CURRENT_CONFIG[consts.CONFIG_SAVE_DIR] = DEFAULT_CONFIG[consts.CONFIG_SAVE_DIR]
    _fix_config(consts.CONFIG_ACTIVE_SOURCE, srcs.SOURCES if consts.FEATURE_SOURCE_DEV else tuple(
        name for name, source in srcs.SOURCES.items() if source.VERSION != srcs.Source.VERSION))


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
    for name, source in ({consts.NAME: sys.modules[__name__]} | srcs.SOURCES).items():
        loaded = _load_config(getters, name, source.CURRENT_CONFIG, source.DEFAULT_CONFIG) and loaded
        source.fix_config()
    return loaded


def try_save_config(force: bool = False) -> bool:
    if force or CURRENT_CONFIG[consts.CONFIG_KEEP_SETTINGS]:
        parser = configparser.ConfigParser()
        for name, source in ({consts.NAME: sys.modules[__name__]} | srcs.SOURCES).items():
            source.update_config()
            source.fix_config()
            if config := {option: source.CURRENT_CONFIG[option] for option, value in sorted(
                    source.DEFAULT_CONFIG.items()) if source.CURRENT_CONFIG[option] != value}:
                parser[name] = config
        with open(CONFIG_PATH, 'w') as file:
            parser.write(file)
        return os.path.isfile(CONFIG_PATH)
    return True


def try_remove_temp(force: bool = False) -> bool:
    if force or not CURRENT_CONFIG[consts.CONFIG_KEEP_CACHE]:
        return files.remove(TEMP_DIR, True)
    else:
        files.trim_dir(TEMP_DIR, int(files.get_disk_size(TEMP_DIR) * consts.MAX_CACHE_PC))
        if files.is_only_dirs(TEMP_DIR):
            return try_remove_temp(True)
        return True


def try_show_notification(title: str, text: str, icon: int | str = win32.gui.SystemTrayIcon.BALLOON_NONE, force: bool = False) -> bool:
    if force or CURRENT_CONFIG[consts.CONFIG_NOTIFY_ERROR]:
        end_time = time.monotonic() + consts.MAX_NOTIFY_SEC
        while end_time > time.monotonic() and not gui.SYSTEM_TRAY.is_shown():
            time.sleep(consts.POLL_FAST_SEC)
        return gui.SYSTEM_TRAY.show_balloon(title, utils.shrink_string(text, consts.MAX_NOTIFY_LEN), icon)
    return False


def try_reapply_wallpaper(_: Optional[bool] = None, force: bool = False):
    if (force or CURRENT_CONFIG[consts.CONFIG_REAPPLY_IMAGE]) and RECENT:
        on_change(*TIMER.target.args, RECENT[0], False)


def show_exception(exc: BaseException):
    threading.Thread(target=win32.show_error, args=(type(
        exc), f'Process {multiprocessing.current_process().name}:\n' + ''.join(
        traceback.format_exception(type(exc), exc, exc.__traceback__)))).start()


@timer.on_thread
def on_shown(*_):
    if CURRENT_CONFIG[consts.CONFIG_FIRST_RUN]:
        CURRENT_CONFIG[consts.CONFIG_FIRST_RUN] = not try_show_notification(
            STRINGS.FIRST_TITLE, STRINGS.FIRST_TEXT, RES_TEMPLATE.format(consts.RES_ICON), True)
        if CURRENT_CONFIG[consts.CONFIG_NOTIFY_BLOCKED]:
            time.sleep(consts.POLL_SLOW_SEC)
            on_blocked()
    if CURRENT_CONFIG[consts.CONFIG_CHANGE_START]:
        on_change(*TIMER.target.args)
    elif CURRENT_CONFIG[consts.CONFIG_RESTORE_IMAGE]:
        try_reapply_wallpaper(force=True)


def get_displays() -> Iterable[str]:
    _fix_config(consts.CONFIG_ACTIVE_DISPLAYS, DISPLAYS)
    return DISPLAYS if CURRENT_CONFIG[consts.CONFIG_ACTIVE_DISPLAYS] == consts.ALL_DISPLAY else (
        CURRENT_CONFIG[consts.CONFIG_ACTIVE_DISPLAYS],)


@timer.on_thread
def on_blocked(*_):
    if not CURRENT_CONFIG[consts.CONFIG_FIRST_RUN] and CURRENT_CONFIG[consts.CONFIG_NOTIFY_BLOCKED]:
        displays = get_displays()
        if not all(win32.display.is_desktop_unblocked(*displays).values()):
            count = itertools.count(1)
            text = '\n'.join(f'{langs.to_str(next(count), STRINGS)}. {_get_monitor_name(monitor, DISPLAYS)}'
                             f'{f": {os.path.basename(blocker[1])}" if consts.FEATURE_BLOCKED_NAME else ""}'
                             for monitor, blocker in win32.display.get_desktop_blocker(*displays).items() if
                             blocker is not None)
            try_show_notification(STRINGS.BLOCKED_TITLE, text, force=True)


@timer.on_thread
def print_progress():
    interval, spinner = spinners.get('sand')
    while (progress := PROGRESS.get()) != -1:
        print(f'[{next(spinner)}] [{utils.get_progress(progress, 32)}] {progress * 100:3.0f}%', end='\r', flush=True)
        time.sleep(interval)
    print(f'[#] [{utils.get_progress(1, 32)}] 100%')


_download_lock = functools.lru_cache(lambda _: threading.Lock())


def download_wallpaper(wallpaper: files.File, query_callback: Optional[Callable[[float, ...], bool]] = None) -> Optional[str]:
    try_remove_temp()
    with _download_lock(wallpaper.url), gui.animate(STRINGS.STATUS_DOWNLOAD):
        PROGRESS.clear()
        if PIPE or win32.console.is_present():
            print_progress()
        try:
            if wallpaper.checksum(temp_path := os.path.join(TEMP_DIR, wallpaper.name)) or (
                    request.retrieve(wallpaper.url, temp_path, wallpaper.size, chunk_count=100,
                                     query_callback=query_callback) and wallpaper.checksum(temp_path, True)):
                wallpaper.fill(temp_path)
                return temp_path
        finally:
            PROGRESS.set(-1.0)


def get_next_wallpaper() -> Optional[files.File]:
    source = srcs.SOURCES[CURRENT_CONFIG[consts.CONFIG_ACTIVE_SOURCE]]
    params = {key: val for key, val in source.CURRENT_CONFIG.items() if not key.startswith('_')}
    first_wallpaper = None
    while True:
        next_wallpaper = next(source.get_next_wallpaper(**params))
        if not CURRENT_CONFIG[consts.CONFIG_SKIP_RECENT] or next_wallpaper not in RECENT:
            return next_wallpaper
        if first_wallpaper is None:
            first_wallpaper = next_wallpaper
        elif first_wallpaper == next_wallpaper:
            return next_wallpaper


@callables.SingletonCallable
def change_wallpaper(wallpaper: Optional[files.File] = None,
                     query_callback: Optional[Callable[[float], bool]] = None) -> bool:
    changed = False
    if wallpaper is None:
        with gui.animate(STRINGS.STATUS_FETCH):
            try:
                wallpaper = get_next_wallpaper()
            except BaseException as exc:
                show_exception(exc)
    if wallpaper is not None:
        wallpaper.name = win32.sanitize_filename(wallpaper.name)
        with contextlib.suppress(ValueError):
            RECENT.remove(wallpaper)
        RECENT.appendleft(wallpaper)
        if path := download_wallpaper(wallpaper, query_callback):
            easing = easings.get(getattr(easings.Ease, CURRENT_CONFIG[
                consts.CONFIG_TRANSITION_EASE]), CURRENT_CONFIG[
                                     consts.CONFIG_EASE_IN], CURRENT_CONFIG[consts.CONFIG_EASE_OUT])
            changed = win32.display.set_wallpapers_ex(*(win32.display.Wallpaper(
                path, display, getattr(win32.display.Style, CURRENT_CONFIG[consts.CONFIG_FIT_STYLE]), rotate=getattr(
                    win32.display.Rotate, CURRENT_CONFIG[consts.CONFIG_ROTATE_BY]), flip=getattr(
                    win32.display.Flip, CURRENT_CONFIG[consts.CONFIG_FLIP_BY]), transition=getattr(
                    win32.display.Transition, CURRENT_CONFIG[consts.CONFIG_TRANSITION_STYLE]), duration=CURRENT_CONFIG[
                    consts.CONFIG_TRANSITION_DURATION], easing=easing) for display in get_displays()))
    return changed


@callables.SingletonCallable
def save_wallpaper(path: str, select: bool = False) -> bool:
    dest = os.path.join(CURRENT_CONFIG[consts.CONFIG_SAVE_DIR], os.path.basename(path))
    if select:
        if (dest := win32.dialog.save_image(dest, STRINGS.LABEL_SAVE_AS)) is None:
            return True
    return files.copy(path, dest)


save_wallpaper_select = functools.partial(save_wallpaper, select=True)


@callables.SingletonCallable
def search_wallpaper(path: str) -> bool:
    searched = False
    with gui.animate(STRINGS.STATUS_SEARCH):
        if location := request.post(consts.URL_GOOGLE, files={'encoded_image': path},
                                    allow_redirects=False).getheader(request.Header.LOCATION):
            searched = webbrowser.open(location)
    return searched


def on_open_url(url: str) -> bool:
    if not (opened := webbrowser.open(url)):
        try_show_notification(STRINGS.LABEL_OPEN_BROWSER, STRINGS.FAIL_OPEN_BROWSER)
    return opened


def on_copy_url(url: str) -> bool:
    if not (copied := win32.clipboard.copy_text(url)):
        try_show_notification(STRINGS.LABEL_COPY_URL, STRINGS.FAIL_COPY_URL)
    return copied


def on_search(url: str, engine: str) -> bool:
    if not (opened := webbrowser.open(lens.get(engine, url))):
        try_show_notification(STRINGS.LABEL_SEARCH, STRINGS.FAIL_SEARCH)
    return opened


@timer.on_thread
def on_change(item_change_enable: Callable, item_recent: win32.gui.MenuItem, query_callback: Callable[[float], bool],
              wallpaper: Optional[files.File] = None, auto_change: bool = True) -> bool:
    changed = False
    if auto_change:
        if CURRENT_CONFIG[consts.CONFIG_IF_MAXIMIZED] and all(win32.display.get_display_blockers(
                *get_displays(), full_screen_only=True).values()):
            while CURRENT_CONFIG[consts.CONFIG_CHANGE_INTERVAL] and CURRENT_CONFIG[
                consts.CONFIG_IF_MAXIMIZED] == consts.MAXIMIZED_ACTION_POSTPONE and all(
                win32.display.get_display_blockers(
                    *get_displays(), full_screen_only=True).values()):
                time.sleep(consts.POLL_SLOW_SEC)
            if not CURRENT_CONFIG[consts.CONFIG_CHANGE_INTERVAL] or \
                    CURRENT_CONFIG[consts.CONFIG_IF_MAXIMIZED] == consts.MAXIMIZED_ACTION_SKIP:
                changed = True
        on_auto_change(CURRENT_CONFIG[consts.CONFIG_CHANGE_INTERVAL])
    if not changed and not change_wallpaper.is_running():
        item_change_enable(False)
        item_recent.enable(False)
        with gui.animate(STRINGS.STATUS_CHANGE):
            if (changed := change_wallpaper(wallpaper, query_callback)) and CURRENT_CONFIG[consts.CONFIG_AUTO_SAVE]:
                on_wallpaper(save_wallpaper, RECENT[0], STRINGS.LABEL_SAVE, STRINGS.FAIL_SAVE)
        _update_recent_menu(item_recent)
        item_change_enable()
    if not changed:
        try_show_notification(STRINGS.LABEL_CHANGE, STRINGS.FAIL_CHANGE)
    return changed


def on_wallpaper(callback: callables.SingletonCallable[[str], bool],
                 wallpaper: files.File, title: str, text: str) -> bool:
    success = False
    try:
        running = callback.is_running()
    except AttributeError:
        running = False
    if not running and (path := download_wallpaper(wallpaper)):
        try:
            success = callback(path)
        except BaseException as exc:
            show_exception(exc)
    if not success:
        try_show_notification(title, text)
    return success


def on_clear(enable: Callable):
    RECENT.clear()
    enable(False)


def _update_recent_menu(item: win32.gui.MenuItem):
    menu = item.get_submenu()
    with gui.set_menu(menu):
        items = gui.get_menu_items()
        for index, wallpaper in enumerate(RECENT):
            if wallpaper in items:
                wallpaper_item = items[wallpaper.url]
                submenu = wallpaper_item.get_submenu()
                menu.remove_item(wallpaper_item)
            else:
                with gui.set_menu(gui.Menu()) as submenu:
                    gui.add_menu_item(STRINGS.LABEL_SET, on_click=functools.partial(on_change, *TIMER.target.args, wallpaper, False),
                                      on_thread=False).set_icon(RES_TEMPLATE.format(consts.RES_SET))
                    gui.add_menu_item(STRINGS.LABEL_SET_LOCK, on_click=functools.partial(
                        on_wallpaper, win32.display.set_lock_background, wallpaper, STRINGS.LABEL_SET_LOCK,
                        STRINGS.FAIL_CHANGE_LOCK)).set_icon(RES_TEMPLATE.format(consts.RES_SET_LOCK))
                    gui.add_menu_item(STRINGS.LABEL_SAVE, on_click=functools.partial(
                        on_wallpaper, save_wallpaper, wallpaper, STRINGS.LABEL_SAVE,
                        STRINGS.FAIL_SAVE)).set_icon(RES_TEMPLATE.format(consts.RES_SAVE))
                    gui.add_menu_item(STRINGS.LABEL_SAVE_AS, on_click=functools.partial(
                        on_wallpaper, save_wallpaper_select, wallpaper, STRINGS.LABEL_SAVE,
                        STRINGS.FAIL_SAVE)).set_icon(RES_TEMPLATE.format(consts.RES_SAVE_AS))
                    gui.add_separator()
                    gui.add_menu_item(STRINGS.LABEL_OPEN, on_click=functools.partial(
                        on_wallpaper, win32.open_file, wallpaper, STRINGS.LABEL_OPEN,
                        STRINGS.FAIL_OPEN)).set_icon(RES_TEMPLATE.format(consts.RES_OPEN))
                    if consts.FEATURE_OPEN_WITH:
                        gui.add_menu_item(STRINGS.LABEL_OPEN_WITH, on_click=functools.partial(
                            on_wallpaper, win32.open_file_with_ex, wallpaper, STRINGS.LABEL_OPEN_WITH,
                            STRINGS.FAIL_OPEN_WITH)).set_icon(RES_TEMPLATE.format(consts.RES_OPEN_WITH))
                    gui.add_menu_item(STRINGS.LABEL_OPEN_EXPLORER, on_click=functools.partial(
                        on_wallpaper, win32.open_file_path, wallpaper, STRINGS.LABEL_OPEN_EXPLORER,
                        STRINGS.FAIL_OPEN_EXPLORER)).set_icon(RES_TEMPLATE.format(consts.RES_OPEN_EXPLORER))
                    gui.add_menu_item(STRINGS.LABEL_OPEN_BROWSER, on_click=functools.partial(
                        on_open_url, wallpaper.url)).set_icon(RES_TEMPLATE.format(consts.RES_OPEN_BROWSER))
                    gui.add_separator()
                    gui.add_menu_item(STRINGS.LABEL_COPY_PATH, on_click=functools.partial(
                        on_wallpaper, win32.clipboard.copy_text, wallpaper, STRINGS.LABEL_COPY_PATH,
                        STRINGS.FAIL_COPY_PATH)).set_icon(RES_TEMPLATE.format(consts.RES_COPY_PATH))
                    gui.add_menu_item(STRINGS.LABEL_COPY, on_click=functools.partial(
                        on_wallpaper, win32.clipboard.copy_image, wallpaper, STRINGS.LABEL_COPY,
                        STRINGS.FAIL_COPY)).set_icon(RES_TEMPLATE.format(consts.RES_COPY))
                    gui.add_menu_item(STRINGS.LABEL_COPY_URL, on_click=functools.partial(
                        on_copy_url, wallpaper.url)).set_icon(RES_TEMPLATE.format(consts.RES_COPY_URL))
                    gui.add_separator()
                    if consts.FEATURE_SEARCH_GOOGLE:
                        gui.add_menu_item(STRINGS.LABEL_GOOGLE, on_click=functools.partial(
                            on_wallpaper, search_wallpaper, wallpaper, STRINGS.LABEL_GOOGLE,
                            STRINGS.FAIL_SEARCH, )).set_icon(RES_TEMPLATE.format(consts.RES_GOOGLE))
                    with gui.set_menu(gui.add_submenu(STRINGS.LABEL_SEARCH, not request.is_path(
                            wallpaper.url), icon=RES_TEMPLATE.format(consts.RES_SEARCH))):
                        for engine in lens.Engine:
                            gui.add_menu_item(getattr(STRINGS, f'LABEL_SEARCH_{engine.name}'), uid=engine.name,
                                              on_click=functools.partial(on_search, wallpaper.url),
                                              args=(gui.MenuItemProperty.UID,)).set_icon(
                                RES_TEMPLATE.format(consts.RES_SEARCH_TEMPLATE.format(engine.name)))
            wallpaper_item = menu.insert_item(index, utils.shrink_string(
                wallpaper.name, consts.MAX_LABEL_LEN), RES_TEMPLATE.format(
                consts.RES_DIGIT_TEMPLATE.format(index + 1)), submenu=submenu)
            wallpaper_item.set_tooltip(wallpaper.url, wallpaper.name, os.path.join(
                TEMP_DIR, wallpaper.name) if consts.FEATURE_TOOLTIP_ICON else gui.MenuItemTooltipIcon.NONE)
            wallpaper_item.set_uid(wallpaper.url)
    for uid, wallpaper_item in items.items():
        if uid and uid not in RECENT:
            menu.remove_item(wallpaper_item)
    item.enable(bool(RECENT))


def on_auto_change(interval: int, after: Optional[float] = None):
    CURRENT_CONFIG[consts.CONFIG_CHANGE_INTERVAL] = interval
    if interval:
        TIMER.set_next_interval(interval)
        TIMER.start(after)
    else:
        TIMER.stop()


def on_modify_save(set_tooltip: Callable, path: Optional[str] = None) -> bool:
    if path is None:
        path = win32.dialog.open_folder(CURRENT_CONFIG[consts.CONFIG_SAVE_DIR], STRINGS.LABEL_SAVE_DIR)
    if path:
        CURRENT_CONFIG[consts.CONFIG_SAVE_DIR] = path
        set_tooltip(STRINGS.TOOLTIP_SAVE_DIR_TEMPLATE.format(path))
    else:
        try_show_notification(STRINGS.LABEL_SAVE_DIR, STRINGS.FAIL_SAVE_DIR)
    return bool(path)


def on_easing_direction(enable_ease: Callable[[bool], bool], _: bool):
    enable_ease(CURRENT_CONFIG[consts.CONFIG_EASE_IN] or CURRENT_CONFIG[consts.CONFIG_EASE_OUT])
    try_reapply_wallpaper()


def on_flip(vertical_is_checked: Callable[[], bool], horizontal_is_checked: Callable[[], bool]):
    vertical_checked = vertical_is_checked()
    horizontal_checked = horizontal_is_checked()
    if vertical_checked and horizontal_checked:
        CURRENT_CONFIG[consts.CONFIG_FLIP_BY] = win32.display.Flip[win32.display.Flip.BOTH]
    elif vertical_checked:
        CURRENT_CONFIG[consts.CONFIG_FLIP_BY] = win32.display.Flip[win32.display.Flip.VERTICAL]
    elif horizontal_checked:
        CURRENT_CONFIG[consts.CONFIG_FLIP_BY] = win32.display.Flip[win32.display.Flip.HORIZONTAL]
    else:
        CURRENT_CONFIG[consts.CONFIG_FLIP_BY] = win32.display.Flip[win32.display.Flip.NONE]
    try_reapply_wallpaper()


def _update_display():
    DISPLAYS.clear()
    DISPLAYS.update(win32.display.get_monitors())


def _get_monitor_name(monitor: str, monitors: dict[str, tuple[str, tuple[int, int]]]) -> str:
    return monitors[monitor][0] or win32.display.get_monitor_name(monitor) or STRINGS.DISPLAY


def on_display_change(item: win32.gui.MenuItem, update: int, _: Optional[gui.Gui] = None):
    if update:
        _update_display()
    submenu = item.get_submenu()
    submenu.clear_items()
    with gui.set_menu(submenu):
        size = win32.display.get_display_size()
        monitors = {consts.ALL_DISPLAY: f'{langs.to_str(0, STRINGS)}. {STRINGS.DISPLAY_ALL}\t'
                                        f'{langs.to_str(size[0], STRINGS)} × {langs.to_str(size[1], STRINGS)}'}
        for index, monitor in enumerate(DISPLAYS, 1):
            monitors[monitor] = (f'{langs.to_str(index, STRINGS)}. {_get_monitor_name(monitor, DISPLAYS)}'
                                 f'\t{langs.to_str(DISPLAYS[monitor][1][0], STRINGS)} × {DISPLAYS[monitor][1][1]}')
        gui.add_mapped_submenu(item, monitors, CURRENT_CONFIG, consts.CONFIG_ACTIVE_DISPLAYS, on_click=on_blocked)
        enable = len(DISPLAYS) > 1
        for submenu_item in submenu:
            submenu_item.enable(enable)
        if consts.FEATURE_UPDATE_DISPLAY:
            gui.add_separator()
            gui.add_menu_item(STRINGS.LABEL_UPDATE_DISPLAY, on_click=functools.partial(
                on_display_change, item, 1)).set_icon(RES_TEMPLATE.format(consts.RES_DISPLAY_UPDATE))
    on_blocked()


def _create_shortcut(dir_: str) -> bool:
    return files.make_dir(dir_) and win32.create_shortcut(os.path.join(
        dir_, consts.NAME), *pyinstall.get_launch_args(), icon_path='' if pyinstall.FROZEN else RES_TEMPLATE.format(
        consts.RES_ICON), comment=STRINGS.DESCRIPTION, show=pyinstall.FROZEN, uid=UUID)


def on_shortcut() -> bool:
    if not (created := _create_shortcut(win32.DESKTOP_DIR)):
        try_show_notification(STRINGS.LABEL_DESKTOP, STRINGS.FAIL_DESKTOP)
    return created


def on_remove_shortcuts() -> bool:
    if not (removed := win32.remove_shortcuts(win32.DESKTOP_DIR, UUID)):
        try_show_notification(STRINGS.LABEL_REMOVE_DESKTOP, STRINGS.FAIL_DESKTOP_REMOVE)
    return removed


def on_start_shortcut() -> bool:
    if not (created := _create_shortcut(os.path.join(win32.START_DIR, consts.NAME))):
        try_show_notification(STRINGS.LABEL_START_MENU, STRINGS.FAIL_START_MENU)
    return created


def on_remove_start_shortcuts() -> bool:
    if not (removed := win32.remove_shortcuts(win32.START_DIR, UUID)):
        try_show_notification(STRINGS.LABEL_REMOVE_START_MENU, STRINGS.FAIL_START_MENU_REMOVE)
    return removed


def on_pin_to_taskbar() -> bool:
    if not (pinned := win32.add_pin(
            *pyinstall.get_launch_args(), name=consts.NAME,
            icon_path='' if pyinstall.FROZEN else RES_TEMPLATE.format(
                consts.RES_ICON), show=pyinstall.FROZEN)):
        try_show_notification(STRINGS.LABEL_PIN, STRINGS.FAIL_PIN)
    return pinned


def on_unpin_from_taskbar() -> bool:
    if not (unpinned := win32.remove_pins(*pyinstall.get_launch_args())):
        try_show_notification(STRINGS.LABEL_UNPIN, STRINGS.FAIL_UNPIN)
    return unpinned


@callables.SingletonCallable
def pin_to_start() -> bool:
    return win32.add_pin(*pyinstall.get_launch_args(), taskbar=False, name=consts.NAME,
                         icon_path='' if pyinstall.FROZEN else RES_TEMPLATE.format(consts.RES_ICON),
                         show=pyinstall.FROZEN)


def on_pin_to_start(item_unpin_enable: Callable, item_pin_enable: Callable) -> bool:
    pinned = False
    if not pin_to_start.is_running():
        item_pin_enable(False)
        item_unpin_enable(False)
        pinned = pin_to_start()
        item_unpin_enable()
        item_pin_enable()
    if not pinned:
        try_show_notification(STRINGS.LABEL_PIN_START, STRINGS.FAIL_PIN_START)
    return pinned


def on_unpin_from_start() -> bool:
    if not (unpinned := win32.remove_pins(*pyinstall.get_launch_args(), taskbar=False)):
        try_show_notification(STRINGS.LABEL_UNPIN_START, STRINGS.FAIL_UNPIN_START)
    return unpinned


@callables.SingletonCallable
def on_toggle_console() -> bool:
    if PIPE:
        if toggled := not PIPE.disconnect():
            try_show_notification(STRINGS.LABEL_CONSOLE, STRINGS.FAIL_HIDE_CONSOLE)
    else:
        win32.open_file(*(PIPE_PATH,) if pyinstall.FROZEN else (sys.executable, pipe.__file__), str(PIPE))
        if not (toggled := PIPE.connect(consts.MAX_PIPE_SEC)):
            try_show_notification(STRINGS.LABEL_CONSOLE, STRINGS.FAIL_SHOW_CONSOLE)
    return toggled


def on_clear_cache() -> bool:
    if not (cleared := try_remove_temp(True)):
        try_show_notification(STRINGS.LABEL_CLEAR_CACHE, STRINGS.FAIL_CLEAR)
    return cleared


def on_reset():
    files.remove(CONFIG_PATH)
    on_restart()


def on_restart():
    RESTART.set(True)
    on_quit()


def on_transition_style(item_duration_enable: Callable[[bool], bool], transition: str):
    item_duration_enable(transition != win32.display.Transition[win32.display.Transition.DISABLED])


def on_source(item: win32.gui.MenuItem, name: str):
    source = srcs.SOURCES[name]
    icon = os.path.isfile(source.ICON)
    item.set_icon(source.ICON if icon else gui.MenuItemImage.NONE)
    item.set_tooltip(f'{name}-{source.VERSION}\n{source.URL}', source.NAME,
                     source.ICON if icon else gui.MenuItemTooltipIcon.NONE)
    submenu = item.get_submenu()
    submenu.clear_items()
    with gui.set_menu(submenu):
        source.create_menu()
        item.enable(bool(len(submenu)))


def on_about():
    try_show_notification(STRINGS.LABEL_ABOUT, str(NotImplemented), force=True)


@timer.on_thread
def on_quit():
    TIMER.stop()
    gui.disable_events()
    max_threads = 1 + (threading.current_thread() is not threading.main_thread())
    if threading.active_count() > max_threads:
        gui.animate(STRINGS.STATUS_QUIT).__enter__()
        try_show_notification(STRINGS.LABEL_QUIT, STRINGS.FAIL_QUIT)
        end_time = time.monotonic() + win32.get_max_shutdown_time()
        while end_time > time.monotonic() and threading.active_count() > max_threads:
            time.sleep(consts.POLL_FAST_SEC)
    gui.stop_loop()


def apply_auto_start(auto_start: bool) -> bool:
    return win32.register_autorun(
        consts.NAME, *pyinstall.get_launch_args(), show=pyinstall.FROZEN,
        uid=UUID) if auto_start else win32.unregister_autorun(consts.NAME, UUID)


def create_menu():
    item_change = gui.add_menu_item(STRINGS.LABEL_CHANGE)
    item_change.set_default()
    item_change.set_icon(RES_TEMPLATE.format(consts.RES_CHANGE))
    item_recent = gui.add_submenu(STRINGS.MENU_RECENT, False, icon=RES_TEMPLATE.format(consts.RES_RECENT))
    TIMER.__init__(0, functools.partial(
        on_change, item_change.enable, item_recent, utils.call_after(PROGRESS.set)(lambda _: True)), True)
    gui.set_on_click(item_change, functools.partial(on_change, *TIMER.target.args, None, False), on_thread=False)
    gui.add_separator(menu=item_recent)
    gui.add_menu_item(STRINGS.LABEL_CLEAR, on_click=functools.partial(
        on_clear, item_recent.enable), menu=item_recent).set_icon(RES_TEMPLATE.format(consts.RES_CLEAR))
    _update_recent_menu(item_recent)
    gui.add_separator()
    item_source = gui.add_submenu(STRINGS.MENU_SOURCE_SETTINGS)
    on_source(item_source, CURRENT_CONFIG[consts.CONFIG_ACTIVE_SOURCE])
    gui.add_separator()
    with gui.set_menu(gui.add_submenu(STRINGS.MENU_ACTIONS, icon=RES_TEMPLATE.format(consts.RES_ACTIONS))):
        with gui.set_menu(gui.add_submenu(STRINGS.MENU_LINKS, icon=RES_TEMPLATE.format(consts.RES_LINKS))):
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
            gui.add_menu_item(STRINGS.LABEL_PIN, enable=consts.FEATURE_SYS_PIN,
                              on_click=on_pin_to_taskbar).set_icon(RES_TEMPLATE.format(consts.RES_PIN))
            gui.add_menu_item(STRINGS.LABEL_UNPIN, enable=consts.FEATURE_SYS_PIN,
                              on_click=on_unpin_from_taskbar).set_icon(RES_TEMPLATE.format(consts.RES_UNPIN))
            gui.add_separator()
            item_unpin_start = gui.add_menu_item(
                STRINGS.LABEL_UNPIN_START, enable=consts.FEATURE_SYS_PIN, on_click=on_unpin_from_start)
            item_unpin_start.set_icon(RES_TEMPLATE.format(consts.RES_UNPIN))
            gui.add_menu_item(
                STRINGS.LABEL_PIN_START, enable=consts.FEATURE_SYS_PIN, on_click=functools.partial(
                    on_pin_to_start, item_unpin_start.enable), args=(gui.MenuItemMethod.ENABLE,),
                position=-1).set_icon(RES_TEMPLATE.format(consts.RES_PIN))
        if consts.FEATURE_CONSOLE_VIEW:
            gui.add_menu_item(STRINGS.LABEL_CONSOLE, on_click=on_toggle_console).set_icon(
                RES_TEMPLATE.format(consts.RES_CONSOLE))
        gui.add_menu_item(STRINGS.LABEL_ABOUT, on_click=on_about).set_icon(RES_TEMPLATE.format(consts.RES_ABOUT))
        gui.add_menu_item(STRINGS.LABEL_CLEAR_CACHE, on_click=on_clear_cache).set_icon(
            RES_TEMPLATE.format(consts.RES_CLEAR_CACHE))
        gui.add_menu_item(STRINGS.LABEL_SETTINGS_RESET, on_click=on_reset).set_icon(
            RES_TEMPLATE.format(consts.RES_SETTINGS_RESET))
        gui.add_menu_item(STRINGS.LABEL_RESTART, enable=bool(
            multiprocessing.parent_process()), on_click=on_restart).set_icon(RES_TEMPLATE.format(consts.RES_RESTART))
    with gui.set_menu(gui.add_submenu(STRINGS.MENU_SETTINGS, icon=RES_TEMPLATE.format(consts.RES_SETTINGS))):
        with gui.set_menu(gui.add_submenu(STRINGS.MENU_AUTO, icon=RES_TEMPLATE.format(consts.RES_AUTO))):
            gui.add_mapped_menu_item(STRINGS.LABEL_CHANGE_START, CURRENT_CONFIG,
                                     consts.CONFIG_CHANGE_START).set_tooltip(STRINGS.TOOLTIP_CHANGE_START)
            gui.add_separator()
            gui.add_mapped_submenu(STRINGS.MENU_AUTO_CHANGE, {interval: getattr(
                STRINGS, f'INTERVAL_{interval}') for interval in CHANGE_INTERVALS}, CURRENT_CONFIG,
                                   consts.CONFIG_CHANGE_INTERVAL,
                                   on_click=on_auto_change, icon=RES_TEMPLATE.format(consts.RES_INTERVAL))
            gui.add_mapped_submenu(STRINGS.MENU_IF_MAXIMIZED, {action: getattr(
                STRINGS, f'MAXIMIZED_{action}') for action in MAXIMIZED_ACTIONS}, CURRENT_CONFIG,
                                   consts.CONFIG_IF_MAXIMIZED, icon=RES_TEMPLATE.format(consts.RES_MAXIMIZED))
            gui.add_separator()
            gui.add_mapped_menu_item(STRINGS.LABEL_AUTO_SAVE, CURRENT_CONFIG, consts.CONFIG_AUTO_SAVE).set_tooltip(
                STRINGS.TOOLTIP_AUTO_SAVE)
            item_dir = gui.add_menu_item(STRINGS.LABEL_SAVE_DIR, on_click=on_modify_save,
                                         args=(gui.MenuItemMethod.SET_TOOLTIP,))
            item_dir.set_icon(RES_TEMPLATE.format(consts.RES_SAVE_DIR))
            on_modify_save(item_dir.set_tooltip, CURRENT_CONFIG[consts.CONFIG_SAVE_DIR])
        if consts.FEATURE_ROTATE_IMAGE:
            gui.add_mapped_submenu(STRINGS.MENU_ROTATE, {rotate: getattr(
                STRINGS, f'ROTATE_{rotate}') for rotate in win32.display.Rotate},
                                   CURRENT_CONFIG, consts.CONFIG_ROTATE_BY,
                                   on_click=try_reapply_wallpaper, icon=RES_TEMPLATE.format(consts.RES_ROTATE))
        with gui.set_menu(gui.add_submenu(STRINGS.MENU_FLIP, icon=RES_TEMPLATE.format(consts.RES_FLIP))):
            item_vertical = gui.add_menu_item(STRINGS.FLIP_VERTICAL, gui.MenuItemType.CHECK, getattr(
                win32.display.Flip, CURRENT_CONFIG[consts.CONFIG_FLIP_BY]) in (
                                                  win32.display.Flip.VERTICAL, win32.display.Flip.BOTH))
            item_horizontal = gui.add_menu_item(STRINGS.FLIP_HORIZONTAL, gui.MenuItemType.CHECK, getattr(
                win32.display.Flip, CURRENT_CONFIG[consts.CONFIG_FLIP_BY]) in (
                                                    win32.display.Flip.HORIZONTAL, win32.display.Flip.BOTH))
            gui.set_on_click(item_vertical, functools.partial(on_flip, item_vertical.is_checked, item_horizontal.is_checked))
            gui.set_on_click(item_horizontal, functools.partial(on_flip, item_vertical.is_checked, item_horizontal.is_checked))
        gui.add_mapped_submenu(STRINGS.MENU_ALIGNMENT, {style: getattr(
            STRINGS, f'ALIGNMENT_{style}') for style in win32.display.Style}, CURRENT_CONFIG, consts.CONFIG_FIT_STYLE,
                               on_click=try_reapply_wallpaper, icon=RES_TEMPLATE.format(consts.RES_ALIGNMENT))
        with gui.set_menu(gui.add_submenu(STRINGS.MENU_TRANSITION, icon=RES_TEMPLATE.format(consts.RES_TRANSITION))):
            item_duration_enable = gui.add_mapped_submenu(
                STRINGS.MENU_TRANSITION_DURATION, {duration: getattr(STRINGS, f'DURATION_{int(duration)}')
                                                   for duration in TRANSITION_DURATIONS}, CURRENT_CONFIG, consts.CONFIG_TRANSITION_DURATION,
                CURRENT_CONFIG[consts.CONFIG_TRANSITION_STYLE] != win32.display.Transition[win32.display.Transition.DISABLED],
                icon=RES_TEMPLATE.format(consts.RES_TRANSITION_DURATION)).enable
            gui.add_mapped_submenu(STRINGS.MENU_TRANSITION_STYLE, {transition: getattr(
                STRINGS, f'TRANSITION_{transition}') for transition in win32.display.Transition}, CURRENT_CONFIG, consts.CONFIG_TRANSITION_STYLE,
                                   on_click=functools.partial(on_transition_style, item_duration_enable),
                                   position=-1, icon=RES_TEMPLATE.format(consts.RES_TRANSITION_STYLE))
            gui.add_separator()
            item_ease_enable = gui.add_mapped_submenu(
                STRINGS.MENU_EASE, {ease: getattr(STRINGS, f'EASE_{ease}') for ease in EASE_STYLES},
                CURRENT_CONFIG, consts.CONFIG_TRANSITION_EASE, CURRENT_CONFIG[consts.CONFIG_EASE_IN] or CURRENT_CONFIG[
                    consts.CONFIG_EASE_OUT], on_click=try_reapply_wallpaper, icon=RES_TEMPLATE.format(consts.RES_EASE)).enable
            with gui.set_menu(gui.add_submenu(STRINGS.MENU_EASE_TIMING, position=-1,
                                              icon=RES_TEMPLATE.format(consts.RES_EASE_TIMING))):
                gui.add_mapped_menu_item(STRINGS.EASE_DIRECTION_IN, CURRENT_CONFIG, consts.CONFIG_EASE_IN,
                                         on_click=functools.partial(on_easing_direction, item_ease_enable))
                gui.add_mapped_menu_item(STRINGS.EASE_DIRECTION_OUT, CURRENT_CONFIG, consts.CONFIG_EASE_OUT,
                                         on_click=functools.partial(on_easing_direction, item_ease_enable))
        item_sources = gui.add_mapped_submenu(STRINGS.MENU_SOURCE, {
            name: source.NAME for name, source in srcs.SOURCES.items()}, CURRENT_CONFIG, consts.CONFIG_ACTIVE_SOURCE,
                                              on_click=functools.partial(on_source, item_source),
                                              icon=RES_TEMPLATE.format(consts.RES_SOURCE))
        if not consts.FEATURE_SOURCE_DEV:
            for item_source, source in zip(item_sources.get_submenu(), srcs.SOURCES.values()):
                if source.VERSION == srcs.Source.VERSION:
                    item_source.enable(False)
        item_display = gui.add_submenu(STRINGS.MENU_DISPLAY, icon=RES_TEMPLATE.format(consts.RES_DISPLAY))
        gui.GUI.bind(gui.GuiEvent.DISPLAY_CHANGE, functools.partial(on_display_change, item_display))
        on_display_change(item_display, 0)
        gui.add_separator()
        with gui.set_menu(gui.add_submenu(STRINGS.MENU_NOTIFICATIONS, icon=RES_TEMPLATE.format(consts.RES_NOTIFICATION))):
            gui.add_mapped_menu_item(STRINGS.LABEL_NOTIFY_ERROR, CURRENT_CONFIG, consts.CONFIG_NOTIFY_ERROR)
            gui.add_mapped_menu_item(STRINGS.LABEL_NOTIFY_BLOCKED, CURRENT_CONFIG,
                                     consts.CONFIG_NOTIFY_BLOCKED, on_click=on_blocked)
        gui.add_mapped_submenu(STRINGS.MENU_COLORS, {mode: getattr(
            STRINGS, f'COLOR_MODE_{mode}') for mode in win32.ColorMode[1:]}, CURRENT_CONFIG, consts.CONFIG_MENU_COLOR,
                               on_click=win32.set_color_mode, icon=RES_TEMPLATE.format(consts.RES_THEME))
        win32.set_color_mode(CURRENT_CONFIG[consts.CONFIG_MENU_COLOR])
        gui.add_mapped_menu_item(STRINGS.LABEL_ANIMATE, CURRENT_CONFIG,
                                 consts.CONFIG_ANIMATE_ICON, on_click=gui.enable_animation)
        gui.add_mapped_menu_item(STRINGS.LABEL_SKIP, CURRENT_CONFIG, consts.CONFIG_SKIP_RECENT)
        gui.add_mapped_menu_item(STRINGS.LABEL_REAPPLY, CURRENT_CONFIG, consts.CONFIG_REAPPLY_IMAGE)
        gui.add_mapped_menu_item(STRINGS.LABEL_RESTORE, CURRENT_CONFIG, consts.CONFIG_RESTORE_IMAGE)
        gui.add_mapped_menu_item(STRINGS.LABEL_CACHE, CURRENT_CONFIG, consts.CONFIG_KEEP_CACHE)
        gui.add_mapped_menu_item(STRINGS.LABEL_START, CURRENT_CONFIG, consts.CONFIG_AUTOSTART)
        gui.add_mapped_menu_item(STRINGS.LABEL_SETTINGS_AUTO_SAVE, CURRENT_CONFIG, consts.CONFIG_KEEP_SETTINGS)
    gui.add_menu_item(STRINGS.LABEL_QUIT, on_click=on_quit, on_thread=False).set_icon(
        RES_TEMPLATE.format(consts.RES_QUIT))


def start():
    singleton.init(UUID, consts.NAME, consts.ARG_WAIT in sys.argv, functools.partial(print, 'Crash'),
                   functools.partial(print, 'Wait'), on_exit=functools.partial(print, 'Exit'))
    if consts.FEATURE_DEBUG_MODE:
        log.redirect_stdout(LOG_PATH, True) if pyinstall.FROZEN else log.write_on_exception(LOG_PATH)
        log.init((r'[^\\]*\.py', utils.re_join('srcs', r'.*\.py')), level=log.Level.INFO, check_comp=False)
    pyinstall.clean_temp()
    _update_display()
    load_config()
    sys.modules['files'] = sys.modules['libs.files']  # FIXME https://github.com/cython/cython/issues/3867
    RECENT.extend(utils.decrypt(CURRENT_CONFIG[consts.CONFIG_RECENT_LIST], ()))
    gui.init(consts.NAME)
    create_menu()
    gui.enable_animation(CURRENT_CONFIG[consts.CONFIG_ANIMATE_ICON])
    apply_auto_start(CURRENT_CONFIG[consts.CONFIG_AUTOSTART])
    gui.GUI.bind(gui.GuiEvent.NC_RENDERING_CHANGED, on_shown, True)
    gui.start_loop(RES_TEMPLATE.format(consts.RES_TRAY), consts.NAME,
                   functools.partial(on_change, *TIMER.target.args, None, False))


def stop():
    timer.Timer.kill_all()
    apply_auto_start(CURRENT_CONFIG[consts.CONFIG_AUTOSTART])
    try_save_config()
    try_remove_temp()


def main() -> NoReturn:
    if consts.FEATURE_ERROR_HOOK:
        utils.hook_except(win32.show_error, True)
    try:
        start()
        stop()
    except BaseException as exc:
        if consts.FEATURE_ERROR_HOOK and not pyinstall.FROZEN:
            show_exception(exc)
        raise
    sys.exit()


if __name__ == '__main__':
    main()
