import collections
import functools
import itertools
import multiprocessing
import os.path
import pickle
import sys
import sysconfig
import tempfile
import threading
import time
import traceback
import uuid
import webbrowser
from typing import Callable, Iterable, NoReturn, Optional, TypedDict

import consts
import gui
import langs
import pipe
import srcs
import validator
import win32
from libs import (callables, config, easings, files, lens, log, pyinstall,
                  request, singleton, spinners, timer, typed, utils)
from win32 import brotli

UUID = srcs.KEY = f'{consts.AUTHOR}.{consts.NAME}'
RES_TEMPLATE = os.path.join(os.path.dirname(__file__), 'res', '{}')
CONFIG_PATH = fr'D:\Projects\wallpyper\{consts.NAME}.json'
# CONFIG_PATH = os.path.join(win32.SAVE_DIR, f'{consts.NAME}.json')  # TODO
LOG_PATH = files.replace_ext(CONFIG_PATH, 'log')
PIPE_PATH = files.replace_ext(pipe.__file__.removesuffix(sysconfig.get_config_var('EXT_SUFFIX')), 'exe')
TEMP_DIR = win32.display.TEMP_WALLPAPER_DIR = os.path.join(tempfile.gettempdir(), consts.NAME)

CHANGE_INTERVALS: tuple[int, int, int, int, int, int, int] = 0, 300, 900, 1800, 3600, 10800, 21600
TRANSITION_DURATIONS: tuple[float, float, float, float, float] = 0.5, 1.0, 2.5, 5.0, 10.0
MAXIMIZED_ACTIONS: tuple[str, str, str] = 'ignore', 'postpone', 'skip'
BLOCKERS: dict[str, str] = {
    'DPPlayer.exe': 'N0va Desktop',
    'Lively.PlayerCefSharp.exe': 'Lively Wallpaper',
    'lwservice.exe': 'Live2DViewerEX',
    'RazerAxon.Player.exe': 'Razer Axon',
    'wallpaper32.exe': 'Wallpaper Engine',
    'wallpaper64.exe': 'Wallpaper Engine'}

win32.display.ANIMATION_POLL_INTERVAL = 0
gui.ANIMATION_PATH = RES_TEMPLATE.format(consts.RES_BUSY)

DISPLAYS: dict[str, tuple[str, tuple[int, int]]] = {}
RESTART = utils.MutableBool()
PROGRESS = utils.MutableFloat()
TIMER = timer.Timer.__new__(timer.Timer)
RECENT: collections.deque[srcs.File] = collections.deque(maxlen=consts.MAX_RECENT_LEN)
PIPE: pipe.StringNamedPipeClient = pipe.StringNamedPipeClient(f'{UUID}.{uuid.uuid4().hex}')

TCONFIG = TypedDict('TCONFIG', {
    consts.CONFIG_FIRST_RUN: bool,
    consts.CONFIG_RECENT_IMAGES: list[typed.type_dataclass_asdict(srcs.ImageFile)],
    consts.CONFIG_ACTIVE_DISPLAY: str,
    consts.CONFIG_ACTIVE_SOURCE: str,
    consts.CONFIG_ANIMATE_ICON: bool,
    consts.CONFIG_AUTOSTART: bool,
    consts.CONFIG_AUTO_SAVE: bool,
    consts.CONFIG_CHANGE_INTERVAL: int,
    consts.CONFIG_CHANGE_START: bool,
    consts.CONFIG_EASE_IN: bool,
    consts.CONFIG_EASE_OUT: bool,
    consts.CONFIG_FIT_STYLE: str,
    consts.CONFIG_FLIP_HORIZONTAL: bool,
    consts.CONFIG_FLIP_VERTICAL: bool,
    consts.CONFIG_KEEP_CACHE: bool,
    consts.CONFIG_MAXIMIZED_ACTION: str,
    consts.CONFIG_MENU_COLOR: str,
    consts.CONFIG_NOTIFY_BLOCKED: bool,
    consts.CONFIG_NOTIFY_ERROR: bool,
    consts.CONFIG_REAPPLY_IMAGE: bool,
    consts.CONFIG_RESTORE_IMAGE: bool,
    consts.CONFIG_ROTATE_BY: str,
    consts.CONFIG_SAVE_CONFIG: bool,
    consts.CONFIG_SAVE_DIR: str,
    consts.CONFIG_SKIP_RECENT: bool,
    consts.CONFIG_TRANSITION_DURATION: float,
    consts.CONFIG_TRANSITION_EASE: str,
    consts.CONFIG_TRANSITION_STYLE: str})
DEFAULT_CONFIG: TCONFIG = {
    consts.CONFIG_FIRST_RUN: consts.FEATURE_FIRST_RUN,
    consts.CONFIG_RECENT_IMAGES: [],
    consts.CONFIG_ACTIVE_DISPLAY: consts.ALL_DISPLAY,
    consts.CONFIG_ACTIVE_SOURCE: next(iter(srcs.SOURCES)),
    consts.CONFIG_ANIMATE_ICON: True,
    consts.CONFIG_AUTOSTART: False,
    consts.CONFIG_AUTO_SAVE: False,
    consts.CONFIG_CHANGE_INTERVAL: CHANGE_INTERVALS[0],
    consts.CONFIG_CHANGE_START: False,
    consts.CONFIG_EASE_IN: True,
    consts.CONFIG_EASE_OUT: True,
    consts.CONFIG_FIT_STYLE: win32.display.Style.FILL.name,
    consts.CONFIG_FLIP_HORIZONTAL: False,
    consts.CONFIG_FLIP_VERTICAL: False,
    consts.CONFIG_KEEP_CACHE: False,
    consts.CONFIG_MAXIMIZED_ACTION: MAXIMIZED_ACTIONS[0],
    consts.CONFIG_MENU_COLOR: win32.ColorMode.AUTO.name,
    consts.CONFIG_NOTIFY_BLOCKED: True,
    consts.CONFIG_NOTIFY_ERROR: True,
    consts.CONFIG_REAPPLY_IMAGE: True,
    consts.CONFIG_RESTORE_IMAGE: False,
    consts.CONFIG_ROTATE_BY: win32.display.Rotate.NONE.name,
    consts.CONFIG_SAVE_CONFIG: False,
    consts.CONFIG_SAVE_DIR: os.path.join(win32.PICTURES_DIR, consts.NAME),
    consts.CONFIG_SKIP_RECENT: False,
    consts.CONFIG_TRANSITION_DURATION: TRANSITION_DURATIONS[2],
    consts.CONFIG_TRANSITION_EASE: easings.Ease.CUBIC.name,
    consts.CONFIG_TRANSITION_STYLE: win32.display.Transition.FADE.name}
CURRENT_CONFIG = {}


# noinspection PyShadowingNames
def _fix_config(validator: Callable, key: str, *args, **kwargs) -> bool:
    return validator(CURRENT_CONFIG, DEFAULT_CONFIG, key, *args, **kwargs)


def fix_config(saving: bool = False):
    _fix_config(validator.ensure_unique, consts.CONFIG_RECENT_IMAGES, pickle.dumps)
    _fix_config(validator.ensure_max_len, consts.CONFIG_RECENT_IMAGES, consts.MAX_RECENT_LEN, right=True)
    _fix_config(validator.ensure_iterable, consts.CONFIG_ACTIVE_DISPLAY, DISPLAYS)
    _fix_config(validator.ensure_iterable, consts.CONFIG_ACTIVE_SOURCE, srcs.SOURCES if consts.FEATURE_SOURCE_DEV else (
        name for name, source in srcs.SOURCES.items() if source.VERSION != srcs.Source.VERSION))
    _fix_config(validator.ensure_iterable, consts.CONFIG_CHANGE_INTERVAL, CHANGE_INTERVALS)
    _fix_config(validator.ensure_enum_names, consts.CONFIG_FIT_STYLE, win32.display.Style)
    _fix_config(validator.ensure_iterable, consts.CONFIG_MAXIMIZED_ACTION, MAXIMIZED_ACTIONS)
    _fix_config(validator.ensure_iterable, consts.CONFIG_MENU_COLOR, (
        color.name for color in itertools.islice(win32.ColorMode, 1, None)))
    _fix_config(validator.ensure_enum_names, consts.CONFIG_ROTATE_BY, win32.display.Rotate)
    _fix_config(validator.ensure_truthy, consts.CONFIG_SAVE_DIR)
    _fix_config(validator.ensure_iterable, consts.CONFIG_TRANSITION_DURATION, TRANSITION_DURATIONS)
    _fix_config(validator.ensure_iterable, consts.CONFIG_TRANSITION_EASE, (
        ease.name for ease in itertools.islice(easings.Ease, None, 7)))
    _fix_config(validator.ensure_enum_names, consts.CONFIG_TRANSITION_STYLE, win32.display.Transition)
    if saving:
        CURRENT_CONFIG[consts.CONFIG_RECENT_IMAGES] = [file.asdict() for file in RECENT]
    else:
        RECENT.extend(filter(None, (srcs.ImageFile.fromdict(
            kwargs) for kwargs in CURRENT_CONFIG[consts.CONFIG_RECENT_IMAGES])))


def _text(message: int | str) -> str:
    return langs.to_str(message, langs.DEFAULT) if isinstance(
        message, int) else getattr(langs.DEFAULT, message)


def create_menu():
    item_change = gui.add_menu_item(_text('LABEL_CHANGE'))
    item_change.set_default()
    item_change.set_icon(RES_TEMPLATE.format(consts.RES_CHANGE))
    item_recent = gui.add_submenu(_text('MENU_RECENT'), False, icon=RES_TEMPLATE.format(consts.RES_RECENT))
    TIMER.__init__(0, functools.partial(
        on_change, item_change.enable, item_recent, utils.call_after(PROGRESS.set)(lambda _: True)), True)
    gui.set_on_click(item_change, functools.partial(on_change, *TIMER.target.args, None, False), on_thread=False)
    gui.add_separator(menu=item_recent)
    gui.add_menu_item(_text('LABEL_CLEAR'), on_click=functools.partial(
        on_clear, item_recent.enable), menu=item_recent).set_icon(RES_TEMPLATE.format(consts.RES_CLEAR))
    _update_recent_menu(item_recent)
    gui.add_separator()
    item_source = gui.add_submenu(_text('MENU_SOURCE_SETTINGS'))
    on_source(item_source, CURRENT_CONFIG[consts.CONFIG_ACTIVE_SOURCE])
    gui.add_separator()
    with gui.set_menu(gui.add_submenu(_text('MENU_ACTIONS'), icon=RES_TEMPLATE.format(consts.RES_ACTIONS))):
        with gui.set_menu(gui.add_submenu(_text('MENU_LINKS'), icon=RES_TEMPLATE.format(consts.RES_LINKS))):
            gui.add_menu_item(_text('LABEL_DESKTOP'), on_click=on_shortcut).set_icon(
                RES_TEMPLATE.format(consts.RES_LINK))
            gui.add_menu_item(_text('LABEL_REMOVE_DESKTOP'), on_click=on_remove_shortcuts).set_icon(
                RES_TEMPLATE.format(consts.RES_UNLINK))
            gui.add_separator()
            gui.add_menu_item(_text('LABEL_START_MENU'), on_click=on_start_shortcut).set_icon(
                RES_TEMPLATE.format(consts.RES_LINK))
            gui.add_menu_item(_text('LABEL_REMOVE_START_MENU'), on_click=on_remove_start_shortcuts).set_icon(
                RES_TEMPLATE.format(consts.RES_UNLINK))
            gui.add_separator()
            gui.add_menu_item(_text('LABEL_PIN'), enable=consts.FEATURE_SYSTRAY_PIN,
                              on_click=on_pin_to_taskbar).set_icon(RES_TEMPLATE.format(consts.RES_PIN))
            gui.add_menu_item(_text('LABEL_UNPIN'), enable=consts.FEATURE_SYSTRAY_PIN,
                              on_click=on_unpin_from_taskbar).set_icon(RES_TEMPLATE.format(consts.RES_UNPIN))
            gui.add_separator()
            item_unpin_start = gui.add_menu_item(
                _text('LABEL_UNPIN_START'), enable=consts.FEATURE_SYSTRAY_PIN, on_click=on_unpin_from_start)
            item_unpin_start.set_icon(RES_TEMPLATE.format(consts.RES_UNPIN))
            gui.add_menu_item(
                _text('LABEL_PIN_START'), enable=consts.FEATURE_SYSTRAY_PIN, on_click=functools.partial(
                    on_pin_to_start, item_unpin_start.enable), args=(gui.MenuItemMethod.ENABLE,),
                position=-1).set_icon(RES_TEMPLATE.format(consts.RES_PIN))
        if consts.FEATURE_CONSOLE_VIEW:
            gui.add_menu_item(_text('LABEL_CONSOLE'), on_click=on_toggle_console).set_icon(
                RES_TEMPLATE.format(consts.RES_CONSOLE))
        gui.add_menu_item(_text('LABEL_ABOUT'), on_click=on_about).set_icon(RES_TEMPLATE.format(consts.RES_ABOUT))
        gui.add_menu_item(_text('LABEL_CLEAR_CACHE'), on_click=on_clear_cache).set_icon(
            RES_TEMPLATE.format(consts.RES_CLEAR_CACHE))
        gui.add_menu_item(_text('LABEL_SETTINGS_RESET'), on_click=on_reset).set_icon(
            RES_TEMPLATE.format(consts.RES_SETTINGS_RESET))
        gui.add_menu_item(_text('LABEL_RESTART'), enable=bool(
            multiprocessing.parent_process()), on_click=on_restart).set_icon(RES_TEMPLATE.format(consts.RES_RESTART))
    with gui.set_menu(gui.add_submenu(_text('MENU_SETTINGS'), icon=RES_TEMPLATE.format(consts.RES_SETTINGS))):
        with gui.set_menu(gui.add_submenu(_text('MENU_AUTO'), icon=RES_TEMPLATE.format(consts.RES_AUTO))):
            gui.add_menu_item_check(_text('LABEL_CHANGE_START'), CURRENT_CONFIG,
                                    consts.CONFIG_CHANGE_START).set_tooltip(_text('TOOLTIP_CHANGE_START'))
            gui.add_separator()
            gui.add_submenu_radio(_text('MENU_AUTO_CHANGE'), {interval: _text(
                f'INTERVAL_{interval}') for interval in CHANGE_INTERVALS},
                                  CURRENT_CONFIG, consts.CONFIG_CHANGE_INTERVAL,
                                  on_click=on_auto_change, icon=RES_TEMPLATE.format(consts.RES_INTERVAL))
            gui.add_submenu_radio(_text('MENU_IF_MAXIMIZED'), {action: _text(
                f'MAXIMIZED_{action}') for action in MAXIMIZED_ACTIONS}, CURRENT_CONFIG,
                                  consts.CONFIG_MAXIMIZED_ACTION, icon=RES_TEMPLATE.format(consts.RES_MAXIMIZED))
            gui.add_separator()
            gui.add_menu_item_check(_text('LABEL_AUTO_SAVE'), CURRENT_CONFIG, consts.CONFIG_AUTO_SAVE).set_tooltip(
                _text('TOOLTIP_AUTO_SAVE'))
            item_dir = gui.add_menu_item(_text('LABEL_SAVE_DIR'), on_click=on_modify_save,
                                         args=(gui.MenuItemMethod.SET_TOOLTIP,))
            item_dir.set_icon(RES_TEMPLATE.format(consts.RES_SAVE_DIR))
            on_modify_save(item_dir.set_tooltip, CURRENT_CONFIG[consts.CONFIG_SAVE_DIR])
        if consts.FEATURE_ROTATE_IMAGE:
            gui.add_submenu_radio(_text('MENU_ROTATE'), {rotate.name: _text(
                f'ROTATE_{rotate.name}') for rotate in win32.display.Rotate},
                                  CURRENT_CONFIG, consts.CONFIG_ROTATE_BY,
                                  on_click=try_reapply_wallpaper, icon=RES_TEMPLATE.format(consts.RES_ROTATE))
        with gui.set_menu(gui.add_submenu(_text('MENU_FLIP'), icon=RES_TEMPLATE.format(consts.RES_FLIP))):
            gui.add_menu_item_check(_text('FLIP_HORIZONTAL'), CURRENT_CONFIG,
                                    consts.CONFIG_FLIP_HORIZONTAL, on_click=try_reapply_wallpaper)
            gui.add_menu_item_check(_text('FLIP_VERTICAL'), CURRENT_CONFIG,
                                    consts.CONFIG_FLIP_VERTICAL, on_click=try_reapply_wallpaper)
        gui.add_submenu_radio(_text('MENU_ALIGNMENT'), {style.name: _text(
            f'ALIGNMENT_{style.name}') for style in win32.display.Style}, CURRENT_CONFIG, consts.CONFIG_FIT_STYLE,
                              on_click=try_reapply_wallpaper, icon=RES_TEMPLATE.format(consts.RES_ALIGNMENT))
        with gui.set_menu(gui.add_submenu(_text('MENU_TRANSITION'), icon=RES_TEMPLATE.format(consts.RES_TRANSITION))):
            item_duration_enable = gui.add_submenu_radio(
                _text('MENU_TRANSITION_DURATION'), {duration: _text(f'DURATION_{int(duration)}')
                                                    for duration in TRANSITION_DURATIONS}, CURRENT_CONFIG, consts.CONFIG_TRANSITION_DURATION,
                CURRENT_CONFIG[consts.CONFIG_TRANSITION_STYLE] != win32.display.Transition.DISABLED.name,
                icon=RES_TEMPLATE.format(consts.RES_TRANSITION_DURATION)).enable
            gui.add_submenu_radio(_text('MENU_TRANSITION_STYLE'), {transition.name: _text(
                f'TRANSITION_{transition.name}') for transition in win32.display.Transition},
                                  CURRENT_CONFIG, consts.CONFIG_TRANSITION_STYLE,
                                  on_click=functools.partial(on_transition_style, item_duration_enable),
                                  position=-1, icon=RES_TEMPLATE.format(consts.RES_TRANSITION_STYLE))
            gui.add_separator()
            item_ease_enable = gui.add_submenu_radio(
                _text('MENU_EASE'), {ease.name: _text(f'EASE_{ease.name}')
                                     for ease in itertools.islice(easings.Ease, None, 7)},
                CURRENT_CONFIG, consts.CONFIG_TRANSITION_EASE, CURRENT_CONFIG[consts.CONFIG_EASE_IN] or CURRENT_CONFIG[
                    consts.CONFIG_EASE_OUT], on_click=try_reapply_wallpaper, icon=RES_TEMPLATE.format(consts.RES_EASE)).enable
            with gui.set_menu(gui.add_submenu(_text('MENU_EASE_TIMING'), position=-1,
                                              icon=RES_TEMPLATE.format(consts.RES_EASE_TIMING))):
                gui.add_menu_item_check(_text('EASE_DIRECTION_IN'), CURRENT_CONFIG, consts.CONFIG_EASE_IN,
                                        on_click=functools.partial(on_easing_direction, item_ease_enable))
                gui.add_menu_item_check(_text('EASE_DIRECTION_OUT'), CURRENT_CONFIG, consts.CONFIG_EASE_OUT,
                                        on_click=functools.partial(on_easing_direction, item_ease_enable))
        item_sources = gui.add_submenu_radio(_text('MENU_SOURCE'), {
            name: source.NAME for name, source in sorted(
                srcs.SOURCES.items(), key=lambda source: source[1].NAME.casefold())},
                                             CURRENT_CONFIG, consts.CONFIG_ACTIVE_SOURCE, on_click=functools.partial(
                on_source, item_source), icon=RES_TEMPLATE.format(consts.RES_SOURCE))
        if not consts.FEATURE_SOURCE_DEV:
            for item_source, source in zip(item_sources.get_submenu(), srcs.SOURCES.values()):
                if source.VERSION == srcs.Source.VERSION:
                    item_source.enable(False)
        item_display = gui.add_submenu(_text('MENU_DISPLAY'), icon=RES_TEMPLATE.format(consts.RES_DISPLAY))
        gui.GUI.bind(gui.GuiEvent.DISPLAY_CHANGE, functools.partial(on_display_change, item_display))
        on_display_change(item_display, 0)
        gui.add_separator()
        with gui.set_menu(gui.add_submenu(_text('MENU_NOTIFICATIONS'), icon=RES_TEMPLATE.format(consts.RES_NOTIFICATION))):
            gui.add_menu_item_check(_text('LABEL_NOTIFY_ERROR'), CURRENT_CONFIG, consts.CONFIG_NOTIFY_ERROR)
            gui.add_menu_item_check(_text('LABEL_NOTIFY_BLOCKED'), CURRENT_CONFIG,
                                    consts.CONFIG_NOTIFY_BLOCKED, on_click=try_notify_blocked)
        gui.add_submenu_radio(_text('MENU_COLORS'), {mode.name: _text(
            f'COLOR_MODE_{mode.name}') for mode in itertools.islice(
            win32.ColorMode, 1, None)}, CURRENT_CONFIG, consts.CONFIG_MENU_COLOR,
                              on_click=win32.set_color_mode, icon=RES_TEMPLATE.format(consts.RES_THEME))
        win32.set_color_mode(CURRENT_CONFIG[consts.CONFIG_MENU_COLOR])
        gui.add_menu_item_check(_text('LABEL_ANIMATE'), CURRENT_CONFIG,
                                consts.CONFIG_ANIMATE_ICON, on_click=gui.enable_animated_icon)
        gui.add_menu_item_check(_text('LABEL_SKIP'), CURRENT_CONFIG, consts.CONFIG_SKIP_RECENT)
        gui.add_menu_item_check(_text('LABEL_REAPPLY'), CURRENT_CONFIG, consts.CONFIG_REAPPLY_IMAGE)
        gui.add_menu_item_check(_text('LABEL_RESTORE'), CURRENT_CONFIG, consts.CONFIG_RESTORE_IMAGE)
        gui.add_menu_item_check(_text('LABEL_CACHE'), CURRENT_CONFIG, consts.CONFIG_KEEP_CACHE)
        gui.add_menu_item_check(_text('LABEL_START'), CURRENT_CONFIG, consts.CONFIG_AUTOSTART)
        gui.add_menu_item_check(_text('LABEL_SETTINGS_AUTO_SAVE'), CURRENT_CONFIG, consts.CONFIG_SAVE_CONFIG)
    gui.add_menu_item(_text('LABEL_QUIT'), on_click=on_quit, on_thread=False).set_icon(
        RES_TEMPLATE.format(consts.RES_QUIT))


def get_image() -> Optional[srcs.File]:
    source = srcs.SOURCES[CURRENT_CONFIG[consts.CONFIG_ACTIVE_SOURCE]]
    params = {key: val for key, val in source.CURRENT_CONFIG.items() if not key.startswith('_')}
    first_image = None
    while True:
        try:
            next_image = next(source.get_image(**params))
        except:  # NOQA: E722
            source.get_image.reset()
            raise
        if next_image is None or (filter_image(
                next_image) and source.filter_image(next_image)):
            return next_image
        print(f'[❌] Filter: {next_image}')
        if first_image is None:
            first_image = next_image
        elif first_image == next_image:
            # TODO respect CURRENT_CONFIG
            return next_image


def filter_image(image: srcs.File) -> bool:
    if CURRENT_CONFIG[consts.CONFIG_SKIP_RECENT] and image in RECENT:
        return False
    return True


def load_config(path: str = CONFIG_PATH):
    json = config.JSONConfig()
    if os.path.isfile(path):
        try:
            json.load(path)
        except BaseException as exc:
            try_alert_error(exc, True)
    for name, source in ({consts.NAME: sys.modules[__name__]} | srcs.SOURCES).items():
        current_config = json.get(name)
        if isinstance(current_config, dict):
            source.CURRENT_CONFIG.update(current_config)
        typed.intersection_update(source.CURRENT_CONFIG, source.DEFAULT_CONFIG, source.TCONFIG)
        source.fix_config()


def try_save_config(path: str = CONFIG_PATH, force: bool = False) -> bool:
    if force or CURRENT_CONFIG[consts.CONFIG_SAVE_CONFIG]:
        json = config.JSONConfig()
        for name, source in ({consts.NAME: sys.modules[__name__]} | srcs.SOURCES).items():
            source.fix_config(True)
            if section := {option: source.CURRENT_CONFIG[option] for option, value in sorted(
                    source.DEFAULT_CONFIG.items()) if source.CURRENT_CONFIG[option] != value}:
                json[name] = section
        json.dump(path, '\t')
        return os.path.isfile(path)
    return True


def try_remove_temp(force: bool = False) -> bool:
    if force or not CURRENT_CONFIG[consts.CONFIG_KEEP_CACHE]:
        return files.remove(TEMP_DIR, True)
    else:
        files.trim_dir(TEMP_DIR, int(files.get_disk_size(TEMP_DIR) * consts.MAX_CACHE_PC))
        if files.is_only_dirs(TEMP_DIR):
            return try_remove_temp(True)
        return True


def try_show_notification(title: str, text: str = '',
                          icon: int | str = win32.gui.SystemTrayIcon.BALLOON_NONE,
                          force: bool = False) -> bool:
    if force or CURRENT_CONFIG[consts.CONFIG_NOTIFY_ERROR]:
        end_time = time.monotonic() + consts.MAX_NOTIFY_SEC
        while end_time > time.monotonic() and not gui.SYSTEM_TRAY.is_shown():
            time.sleep(consts.POLL_FAST_SEC)
        return gui.SYSTEM_TRAY.show_balloon(title, utils.shrink_string(text, consts.MAX_NOTIFY_LEN), icon)
    return False


def try_reapply_wallpaper(_: Optional[bool] = None, force: bool = False):
    if (force or CURRENT_CONFIG[consts.CONFIG_REAPPLY_IMAGE]) and RECENT:
        on_change(*TIMER.target.args, RECENT[0], False)


def try_alert_error(exc: BaseException, force: bool = False):
    if force or (consts.FEATURE_ERROR_HOOK and not pyinstall.FROZEN):
        threading.Thread(target=win32.alert_error, args=(type(
            exc), f'Process {multiprocessing.current_process().name}:\n' + ''.join(
            traceback.format_exception(type(exc), exc, exc.__traceback__)))).start()


@timer.on_thread
def try_notify_blocked(*_, force: bool = False):
    if force or not CURRENT_CONFIG[consts.CONFIG_FIRST_RUN] and CURRENT_CONFIG[consts.CONFIG_NOTIFY_BLOCKED]:
        displays = get_displays()
        if not all(win32.display.is_desktop_unblocked(*displays).values()):
            count = itertools.count(1)
            text = '\n'.join(f'{_text(next(count))}. {_get_monitor_name(monitor, DISPLAYS)}{_get_blocker(blocker[1])}'
                             for monitor, blocker in win32.display.get_desktop_blocker(*displays).items() if
                             blocker is not None)
            try_show_notification(_text('BLOCKED_TITLE'), text, force=True)
        elif force:
            try_show_notification(_text('NO_BLOCKED_TEXT'), force=True)


def _get_blocker(blocker: str) -> str:
    if consts.FEATURE_BLOCKER_NAME:
        blocker = os.path.basename(blocker[1])
        try:
            blocker = BLOCKERS[blocker]
        except KeyError:
            pass
        blocker = f': {blocker}'
    else:
        blocker = ''
    return blocker


@timer.on_thread
def on_shown(_: gui.Event):
    if CURRENT_CONFIG[consts.CONFIG_FIRST_RUN]:
        CURRENT_CONFIG[consts.CONFIG_FIRST_RUN] = not try_show_notification(
            _text('FIRST_TITLE'), _text('FIRST_TEXT'), RES_TEMPLATE.format(consts.RES_ICON), True)
        if CURRENT_CONFIG[consts.CONFIG_NOTIFY_BLOCKED]:
            time.sleep(consts.POLL_SLOW_SEC)
            try_notify_blocked()
    if CURRENT_CONFIG[consts.CONFIG_CHANGE_START]:
        on_change(*TIMER.target.args)
    elif CURRENT_CONFIG[consts.CONFIG_RESTORE_IMAGE]:
        try_reapply_wallpaper(force=True)


def get_displays() -> Iterable[str]:
    _fix_config(validator.ensure_iterable, consts.CONFIG_ACTIVE_DISPLAY, DISPLAYS)
    return DISPLAYS if CURRENT_CONFIG[consts.CONFIG_ACTIVE_DISPLAY] == consts.ALL_DISPLAY else (
        CURRENT_CONFIG[consts.CONFIG_ACTIVE_DISPLAY],)


@timer.on_thread
def print_progress():
    interval, spinner = spinners.get('sand')
    while (progress := PROGRESS.get()) != -1:
        print(f'[{next(spinner)}] [{utils.get_progress(progress, 32)}]'
              f' {progress * 100:3.0f}%', end='\r', flush=True)
        time.sleep(interval)
    print(f'[✅] [{utils.get_progress(1, 32)}] 100%')


_download_lock = functools.lru_cache(lambda _: threading.Lock())


def download_image(image: srcs.File, query_callback: Optional[Callable[[float], bool]] = None) -> Optional[str]:
    try_remove_temp()
    with _download_lock(image.name), gui.try_animate_icon(_text('STATUS_DOWNLOAD')):
        path = os.path.join(TEMP_DIR, image.name)
        PROGRESS.clear()
        print(f'[🌐] Download: {image}')
        if PIPE or win32.console.is_present():
            print_progress()
        try:
            if (image.get_url() == request.from_path(path) or
                (image.checksize(path) and (consts.FEATURE_UNSAFE_CACHE or image.checksum(path))) or
                request.retrieve(image.request, path, image.size, chunk_count=100,
                                 query_callback=query_callback)) and image.fill(path):
                return path
        finally:
            PROGRESS.set(-1.0)


@callables.SingletonCallable
def change_wallpaper(image: Optional[srcs.File] = None,
                     query_callback: Optional[Callable[[float], bool]] = None) -> bool:
    changed = False
    if image is None:
        with gui.try_animate_icon(_text('STATUS_FETCH')):
            try:
                image = get_image()
            except BaseException as exc:
                try_alert_error(exc, True)
    if image is not None:
        try:
            RECENT.remove(image)
        except ValueError:
            pass
        RECENT.appendleft(image)
        if (path := download_image(image, query_callback)) is not None:
            changed = win32.display.set_wallpapers_ex(*(win32.display.Wallpaper(
                path, display, win32.display.Style[CURRENT_CONFIG[
                    consts.CONFIG_FIT_STYLE]], rotate=win32.display.Rotate[
                    CURRENT_CONFIG[consts.CONFIG_ROTATE_BY]], flip=win32.display.Flip(
                    CURRENT_CONFIG[consts.CONFIG_FLIP_HORIZONTAL] * win32.display.Flip.HORIZONTAL +
                    CURRENT_CONFIG[consts.CONFIG_FLIP_VERTICAL] * win32.display.Flip.VERTICAL),
                transition=win32.display.Transition[CURRENT_CONFIG[consts.CONFIG_TRANSITION_STYLE]],
                duration=CURRENT_CONFIG[consts.CONFIG_TRANSITION_DURATION],
                easing=easings.get(CURRENT_CONFIG[consts.CONFIG_TRANSITION_EASE], CURRENT_CONFIG[
                    consts.CONFIG_EASE_IN], CURRENT_CONFIG[consts.CONFIG_EASE_OUT])) for display in get_displays()))
    return changed


@callables.SingletonCallable
def save_image(path: str, select: bool = False) -> bool:
    dest = os.path.join(CURRENT_CONFIG[consts.CONFIG_SAVE_DIR], os.path.basename(path))
    if select:
        if (dest := win32.dialog.save_image(dest, _text('LABEL_SAVE_AS'))) is None:
            return True
    return files.copy(path, dest)


on_save_image = functools.partial(save_image, select=True)


@callables.SingletonCallable
def search_image(path: str) -> bool:
    searched = False
    with gui.try_animate_icon(_text('STATUS_SEARCH')):
        response = request.post(consts.URL_GOOGLE, files={
            'encoded_image': path}, allow_redirects=False)
        if response.is_redirect:
            searched = webbrowser.open(response.headers[request.Header.LOCATION])
    return searched


def on_open_url(url: str) -> bool:
    if not (opened := webbrowser.open(url)):
        try_show_notification(_text('LABEL_OPEN_BROWSER'), _text('FAIL_OPEN_BROWSER'))
    return opened


def on_copy_url(url: str) -> bool:
    if not (copied := win32.clipboard.copy_text(url)):
        try_show_notification(_text('LABEL_COPY_URL'), _text('FAIL_COPY_URL'))
    return copied


def on_search(url: str, engine: str) -> bool:
    if not (opened := lens.Engine[engine].open(url)):
        try_show_notification(_text('LABEL_SEARCH'), _text('FAIL_SEARCH'))
    return opened


@timer.on_thread
def on_change(enable: Callable[[bool], bool], item_recent: win32.gui.MenuItem,
              query_callback: Callable[[float], bool],
              image: Optional[srcs.File] = None, auto_change: bool = True) -> bool:
    changed = False
    if auto_change:
        if CURRENT_CONFIG[consts.CONFIG_MAXIMIZED_ACTION] != MAXIMIZED_ACTIONS[0] and all(
                win32.display.get_display_blockers(*get_displays(), full_screen_only=True).values()):
            while (CURRENT_CONFIG[consts.CONFIG_CHANGE_INTERVAL] and CURRENT_CONFIG[
                consts.CONFIG_MAXIMIZED_ACTION] == MAXIMIZED_ACTIONS[1] and
                   all(win32.display.get_display_blockers(*get_displays(), full_screen_only=True).values())):
                time.sleep(consts.POLL_SLOW_SEC)
            if (not CURRENT_CONFIG[consts.CONFIG_CHANGE_INTERVAL] or
                    CURRENT_CONFIG[consts.CONFIG_MAXIMIZED_ACTION] == MAXIMIZED_ACTIONS[2]):
                changed = True
        on_auto_change(CURRENT_CONFIG[consts.CONFIG_CHANGE_INTERVAL])
    if not changed and not change_wallpaper.is_running():
        enable(False)
        item_recent.enable(False)
        with gui.try_animate_icon(_text('STATUS_CHANGE')):
            if ((changed := change_wallpaper(image, query_callback))
                    and CURRENT_CONFIG[consts.CONFIG_AUTO_SAVE] and RECENT):
                on_image_func(save_image, RECENT[0], _text('LABEL_SAVE'), _text('FAIL_SAVE'))
        _update_recent_menu(item_recent)
        enable(True)
    if not changed:
        try_show_notification(_text('LABEL_CHANGE'), _text('FAIL_CHANGE'))
    return changed


def on_image_func(callback: callables.SingletonCallable[[str], bool],
                  image: srcs.File, title: str, text: str) -> bool:
    success = False
    try:
        running = callback.is_running()
    except AttributeError:
        running = False
    if not running and (path := download_image(image)) is not None:
        try:
            success = callback(path)
        except BaseException as exc:
            try_alert_error(exc, True)
    if not success:
        try_show_notification(title, text)
    return success


def on_clear(enable: Callable[[bool], bool]):
    RECENT.clear()
    enable(False)


def _update_recent_menu(item: win32.gui.MenuItem):
    menu = item.get_submenu()
    with gui.set_menu(menu):
        items = gui.get_menu_items()
        for index, image in enumerate(RECENT):
            simple = image.is_simple()
            url = image.get_url()
            if image in items:
                item_image = items[image.name]
                submenu = item_image.get_submenu()
                menu.remove_item(item_image)
            else:
                with gui.set_menu(gui.Menu()) as submenu:
                    gui.add_menu_item(_text('LABEL_SET'), on_click=functools.partial(on_change, *TIMER.target.args, image, False),
                                      on_thread=False).set_icon(RES_TEMPLATE.format(consts.RES_SET))
                    gui.add_menu_item(_text('LABEL_SET_LOCK'), on_click=functools.partial(
                        on_image_func, win32.display.set_lock_background, image, _text('LABEL_SET_LOCK'),
                        _text('FAIL_CHANGE_LOCK'))).set_icon(RES_TEMPLATE.format(consts.RES_SET_LOCK))
                    gui.add_menu_item(_text('LABEL_SAVE'), on_click=functools.partial(
                        on_image_func, save_image, image, _text('LABEL_SAVE'),
                        _text('FAIL_SAVE'))).set_icon(RES_TEMPLATE.format(consts.RES_SAVE))
                    gui.add_menu_item(_text('LABEL_SAVE_AS'), on_click=functools.partial(
                        on_image_func, on_save_image, image, _text('LABEL_SAVE'),
                        _text('FAIL_SAVE'))).set_icon(RES_TEMPLATE.format(consts.RES_SAVE_AS))
                    gui.add_separator()
                    gui.add_menu_item(_text('LABEL_OPEN'), on_click=functools.partial(
                        on_image_func, win32.open_file, image, _text('LABEL_OPEN'),
                        _text('FAIL_OPEN'))).set_icon(RES_TEMPLATE.format(consts.RES_OPEN))
                    if consts.FEATURE_OPEN_WITH:
                        gui.add_menu_item(_text('LABEL_OPEN_WITH'), on_click=functools.partial(
                            on_image_func, win32.open_file_with_ex, image, _text('LABEL_OPEN_WITH'),
                            _text('FAIL_OPEN_WITH'))).set_icon(RES_TEMPLATE.format(consts.RES_OPEN_WITH))
                    gui.add_menu_item(_text('LABEL_OPEN_EXPLORER'), on_click=functools.partial(
                        on_image_func, win32.open_file_path, image, _text('LABEL_OPEN_EXPLORER'),
                        _text('FAIL_OPEN_EXPLORER'))).set_icon(RES_TEMPLATE.format(consts.RES_OPEN_EXPLORER))
                    gui.add_menu_item(_text('LABEL_OPEN_BROWSER'), enable=simple, on_click=functools.partial(
                        on_open_url, url)).set_icon(RES_TEMPLATE.format(consts.RES_OPEN_BROWSER))
                    gui.add_separator()
                    gui.add_menu_item(_text('LABEL_COPY_PATH'), on_click=functools.partial(
                        on_image_func, win32.clipboard.copy_text, image, _text('LABEL_COPY_PATH'),
                        _text('FAIL_COPY_PATH'))).set_icon(RES_TEMPLATE.format(consts.RES_COPY_PATH))
                    gui.add_menu_item(_text('LABEL_COPY'), on_click=functools.partial(
                        on_image_func, win32.clipboard.copy_image, image, _text('LABEL_COPY'),
                        _text('FAIL_COPY'))).set_icon(RES_TEMPLATE.format(consts.RES_COPY))
                    gui.add_menu_item(_text('LABEL_COPY_URL'), enable=simple, on_click=functools.partial(
                        on_copy_url, url)).set_icon(RES_TEMPLATE.format(consts.RES_COPY_URL))
                    gui.add_separator()
                    if consts.FEATURE_SEARCH_GOOGLE:
                        gui.add_menu_item(_text('LABEL_GOOGLE'), on_click=functools.partial(
                            on_image_func, search_image, image, _text('LABEL_GOOGLE'),
                            _text('FAIL_SEARCH'))).set_icon(RES_TEMPLATE.format(consts.RES_GOOGLE))
                    with gui.set_menu(gui.add_submenu(_text('LABEL_SEARCH'), simple and not request.is_path(
                            url), icon=RES_TEMPLATE.format(consts.RES_SEARCH))):
                        for engine in lens.Engine:
                            # noinspection PyUnresolvedReferences
                            gui.add_menu_item(_text(f'LABEL_SEARCH_{engine.name}'), uid=engine.name,
                                              on_click=functools.partial(on_search, url),
                                              args=(gui.MenuItemProperty.UID,)).set_icon(
                                RES_TEMPLATE.format(consts.TEMPLATE_RES_SEARCH.format(engine.name)))
            item_image = menu.insert_item(index, utils.shrink_string(
                image.name, consts.MAX_LABEL_LEN), RES_TEMPLATE.format(
                consts.TEMPLATE_RES_DIGIT.format(index + 1)), submenu=submenu)
            tooltip = f'{image.name} ({files.Size(image.size)})'
            item_image.set_tooltip(*(url, tooltip) if simple else (tooltip, ''), os.path.join(
                TEMP_DIR, image.name) if consts.FEATURE_TOOLTIP_ICON else gui.MenuItemTooltipIcon.NONE)
            item_image.set_uid(image.name)
    for uid, item_image in items.items():
        if uid and uid not in RECENT:
            menu.remove_item(item_image)
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
        path = win32.dialog.open_folder(CURRENT_CONFIG[consts.CONFIG_SAVE_DIR], _text('LABEL_SAVE_DIR'))
    if path:
        CURRENT_CONFIG[consts.CONFIG_SAVE_DIR] = path
        set_tooltip(_text('TOOLTIP_TEMPLATE_SAVE_DIR').format(path))
    else:
        try_show_notification(_text('LABEL_SAVE_DIR'), _text('FAIL_SAVE_DIR'))
    return bool(path)


def on_easing_direction(enable_ease: Callable[[bool], bool], _: bool):
    enable_ease(CURRENT_CONFIG[consts.CONFIG_EASE_IN] or CURRENT_CONFIG[consts.CONFIG_EASE_OUT])
    try_reapply_wallpaper()


def _update_display():
    DISPLAYS.clear()
    DISPLAYS.update(win32.display.get_monitors())


def _get_monitor_name(monitor: str, monitors: dict[str, tuple[str, tuple[int, int]]]) -> str:
    return monitors[monitor][0] or win32.display.get_monitor_name(monitor) or _text('DISPLAY')


def on_display_change(item: win32.gui.MenuItem, update: int, _: Optional[gui.Gui] = None):
    if update:
        _update_display()
    submenu = item.get_submenu()
    submenu.clear_items()
    with gui.set_menu(submenu):
        size = win32.display.get_display_size()
        monitors = {consts.ALL_DISPLAY: f'{_text(0)}. {_text("DISPLAY_ALL")}\t'
                                        f'{_text(size[0])} × {_text(size[1])}'}
        for index, monitor in enumerate(DISPLAYS, 1):
            monitors[monitor] = (f'{_text(index)}. {_get_monitor_name(monitor, DISPLAYS)}'
                                 f'\t{_text(DISPLAYS[monitor][1][0])} × {_text(DISPLAYS[monitor][1][1])}')
        gui.add_submenu_radio(item, monitors, CURRENT_CONFIG, consts.CONFIG_ACTIVE_DISPLAY, on_click=try_notify_blocked)
        enable = len(DISPLAYS) > 1
        for submenu_item in submenu:
            submenu_item.enable(enable)
        if consts.FEATURE_DISPLAY_EXTRA:
            gui.add_separator()
            gui.add_menu_item(_text('LABEL_UPDATE_DISPLAY'), on_click=functools.partial(
                on_display_change, item, 1)).set_icon(RES_TEMPLATE.format(consts.RES_DISPLAY_UPDATE))
            gui.add_menu_item(_text('LABEL_BLOCKED_DISPLAY'), on_click=functools.partial(
                try_notify_blocked, force=True)).set_icon(RES_TEMPLATE.format(consts.RES_DISPLAY_BLOCKED))
    try_notify_blocked()


def _create_shortcut(dir_: str) -> bool:
    return files.make_dir(dir_) and win32.create_shortcut(os.path.join(
        dir_, consts.NAME), *pyinstall.get_launch_args(), icon_path='' if pyinstall.FROZEN else RES_TEMPLATE.format(
        consts.RES_ICON), comment=_text('DESCRIPTION'), show=pyinstall.FROZEN, uid=UUID)


def on_shortcut() -> bool:
    if not (created := _create_shortcut(win32.DESKTOP_DIR)):
        try_show_notification(_text('LABEL_DESKTOP'), _text('FAIL_DESKTOP'))
    return created


def on_remove_shortcuts() -> bool:
    if not (removed := win32.remove_shortcuts(win32.DESKTOP_DIR, UUID)):
        try_show_notification(_text('LABEL_REMOVE_DESKTOP'), _text('FAIL_DESKTOP_REMOVE'))
    return removed


def on_start_shortcut() -> bool:
    if not (created := _create_shortcut(os.path.join(win32.START_DIR, consts.NAME))):
        try_show_notification(_text('LABEL_START_MENU'), _text('FAIL_START_MENU'))
    return created


def on_remove_start_shortcuts() -> bool:
    if not (removed := win32.remove_shortcuts(win32.START_DIR, UUID)):
        try_show_notification(_text('LABEL_REMOVE_START_MENU'), _text('FAIL_START_MENU_REMOVE'))
    return removed


def on_pin_to_taskbar() -> bool:
    if not (pinned := win32.add_pin(
            *pyinstall.get_launch_args(), name=consts.NAME,
            icon_path='' if pyinstall.FROZEN else RES_TEMPLATE.format(
                consts.RES_ICON), show=pyinstall.FROZEN)):
        try_show_notification(_text('LABEL_PIN'), _text('FAIL_PIN'))
    return pinned


def on_unpin_from_taskbar() -> bool:
    if not (unpinned := win32.remove_pins(*pyinstall.get_launch_args())):
        try_show_notification(_text('LABEL_UNPIN'), _text('FAIL_UNPIN'))
    return unpinned


@callables.SingletonCallable
def pin_to_start() -> bool:
    return win32.add_pin(*pyinstall.get_launch_args(), taskbar=False, name=consts.NAME,
                         icon_path='' if pyinstall.FROZEN else RES_TEMPLATE.format(consts.RES_ICON),
                         show=pyinstall.FROZEN)


def on_pin_to_start(enable_unpin: Callable, enable_pin: Callable) -> bool:
    pinned = False
    if not pin_to_start.is_running():
        enable_pin(False)
        enable_unpin(False)
        pinned = pin_to_start()
        enable_unpin()
        enable_pin()
    if not pinned:
        try_show_notification(_text('LABEL_PIN_START'), _text('FAIL_PIN_START'))
    return pinned


def on_unpin_from_start() -> bool:
    if not (unpinned := win32.remove_pins(*pyinstall.get_launch_args(), taskbar=False)):
        try_show_notification(_text('LABEL_UNPIN_START'), _text('FAIL_UNPIN_START'))
    return unpinned


@callables.SingletonCallable
def on_toggle_console() -> bool:
    if PIPE:
        if toggled := not PIPE.disconnect():
            try_show_notification(_text('LABEL_CONSOLE'), _text('FAIL_HIDE_CONSOLE'))
    else:
        win32.open_file(*(PIPE_PATH,) if pyinstall.FROZEN else (sys.executable, pipe.__file__), str(PIPE))
        if not (toggled := PIPE.connect(consts.MAX_PIPE_SEC)):
            try_show_notification(_text('LABEL_CONSOLE'), _text('FAIL_SHOW_CONSOLE'))
    return toggled


def on_clear_cache() -> bool:
    if not (cleared := try_remove_temp(True)):
        try_show_notification(_text('LABEL_CLEAR_CACHE'), _text('FAIL_CLEAR'))
    return cleared


def on_reset():
    files.remove(CONFIG_PATH)
    on_restart()


def on_restart():
    RESTART.set(True)
    on_quit()


def on_transition_style(enable: Callable[[bool], bool], transition: str):
    enable(transition != win32.display.Transition.DISABLED.name)


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
    try_show_notification(_text('LABEL_ABOUT'), str(NotImplemented), force=True)


@timer.on_thread
def on_quit():
    TIMER.stop()
    gui.GUI.unbind(win32.gui.GuiEvent.DISPLAY_CHANGE)
    gui.disable_events()
    max_threads = 1 + (threading.current_thread() is not threading.main_thread())
    time.sleep(consts.POLL_FAST_SEC)
    if threading.active_count() > max_threads:
        gui.try_animate_icon(_text('STATUS_QUIT')).__enter__()
        try_show_notification(_text('LABEL_QUIT'), _text('FAIL_QUIT'), force=True)
        end_time = time.monotonic() + win32.get_max_shutdown_time()
        while end_time > time.monotonic() and threading.active_count() > max_threads:
            time.sleep(consts.POLL_FAST_SEC)
    gui.stop_loop()


def apply_auto_start(auto_start: bool) -> bool:
    return win32.register_autorun(
        consts.NAME, *pyinstall.get_launch_args(), show=pyinstall.FROZEN,
        uid=UUID) if auto_start else win32.unregister_autorun(consts.NAME, UUID)


def start():
    singleton.init(UUID, consts.NAME, consts.ARG_WAIT in sys.argv, functools.partial(print, 'Crash'),
                   functools.partial(print, 'Wait'), on_exit=functools.partial(print, 'Exit'))
    if consts.FEATURE_DEBUG_MODE:
        log.redirect_stdout(LOG_PATH, True) if pyinstall.FROZEN else log.write_on_exception(LOG_PATH)
        log.init((r'[^\\]*\.py', utils.re_join('srcs', r'.*\.py')), level=log.Level.INFO, check_comp=False)
    pyinstall.clean_temp()
    _update_display()
    sys.modules['request'] = sys.modules['libs.request']  # FIXME https://github.com/cython/cython/issues/3867
    load_config()
    gui.init(consts.NAME)
    create_menu()
    gui.enable_animated_icon(CURRENT_CONFIG[consts.CONFIG_ANIMATE_ICON])
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
        utils.hook_except(win32.alert_error, True)
    try:
        start()
        stop()
    except BaseException as exc:
        try_alert_error(exc)
        raise
    sys.exit()


class BrotliDecoder(request.Decoder):
    tokens = 'br',

    def __init__(self):
        self._decoder = brotli.Decompressor()

    def flush(self) -> bytes:
        return self._decoder.unused_data

    def decode(self, data: bytes) -> bytes:
        return self._decoder.decompress(data)


if __name__ == '__main__':
    main()
