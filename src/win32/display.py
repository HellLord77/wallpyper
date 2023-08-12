from __future__ import annotations

import concurrent.futures
import enum
import functools
import ntpath
import operator
import os
import random
import string
import tempfile
import threading
import time
import winreg
from typing import Callable, Iterable, NamedTuple, Optional

from libs import ctyped
from libs.ctyped import winrt
from libs.ctyped.const import error, runtimeclass
from libs.ctyped.interface.um import ShlObj_core, ShObjIdl_core
from libs.ctyped.interface.winrt.Windows.System import UserProfile as Windows_System_UserProfile
from libs.ctyped.lib import user32, kernel32, gdi32, msimg32, dwmapi, psapi, shell32
from . import _gdiplus, _handle, _utils

_HISTORY_KEY = ntpath.join('Software', 'Microsoft', 'Windows', 'CurrentVersion', 'Explorer', 'Wallpapers')

ANIMATION_POLL_INTERVAL = 0.01
TEMP_WALLPAPER_DIR = tempfile.gettempdir()


class Style(enum.IntEnum):
    FILL = ctyped.const.WPSTYLE_CROPTOFIT
    FIT = ctyped.const.WPSTYLE_KEEPASPECT
    STRETCH = ctyped.const.WPSTYLE_STRETCH
    TILE = ctyped.const.WPSTYLE_TILE
    CENTER = ctyped.const.WPSTYLE_CENTER
    SPAN = ctyped.const.WPSTYLE_SPAN


class Rotate(enum.IntEnum):
    NONE = 0
    RIGHT = 1
    LEFT = 2
    FLIP = 3


class Flip(enum.IntEnum):
    NONE = 0
    HORIZONTAL = 1
    VERTICAL = 2
    BOTH = 3


class Transition(enum.IntEnum):
    DISABLED = -2
    RANDOM = -1
    FADE = 0
    EXPLODE = 1
    IMPLODE = 2
    LEFT = 3
    TOP = 4
    RIGHT = 5
    BOTTOM = 6
    TOP_LEFT = 7
    TOP_RIGHT = 8
    BOTTOM_LEFT = 9
    BOTTOM_RIGHT = 10
    VERTICAL = 11
    HORIZONTAL = 12
    REVERSE_VERTICAL = 13
    REVERSE_HORIZONTAL = 14
    SLIDE_LEFT = 15
    SLIDE_TOP = 16
    SLIDE_RIGHT = 17
    SLIDE_BOTTOM = 18
    SLIDE_TOP_LEFT = 19
    SLIDE_TOP_RIGHT = 20
    SLIDE_BOTTOM_LEFT = 21
    SLIDE_BOTTOM_RIGHT = 22
    SLIDE_VERTICAL = 23
    SLIDE_HORIZONTAL = 24
    SLIDE_REVERSE_VERTICAL = 25
    SLIDE_REVERSE_HORIZONTAL = 26

    @staticmethod
    def _fade(dst: ctyped.type.HDC, dst_x: int, dst_y: int, src: ctyped.type.HDC, blend: ctyped.struct.BLENDFUNCTION,
              dst_bk: ctyped.type.HDC, tmp_dst: ctyped.type.HDC, factor: float, dst_w: int, dst_h: int):
        blend.SourceConstantAlpha = int(255 * factor)
        gdi32.BitBlt(tmp_dst, 0, 0, dst_w, dst_h, dst_bk, 0, 0, ctyped.const.SRCCOPY)
        msimg32.AlphaBlend(tmp_dst, 0, 0, dst_w, dst_h, src, 0, 0, dst_w, dst_h, blend)
        gdi32.BitBlt(dst, dst_x, dst_y, dst_w, dst_h, tmp_dst, 0, 0, ctyped.const.SRCCOPY)
        if None:
            yield

    @staticmethod
    def _left(factor: float, dst_w: int, dst_h: int):
        yield 0, 0, int(dst_w * factor), dst_h, 0, 0

    @staticmethod
    def _slide_left(factor: float, dst_w: int, dst_h: int):
        dst_w_ = int(dst_w * factor)
        yield 0, 0, dst_w_, dst_h, dst_w - dst_w_, 0

    @staticmethod
    def _top(factor: float, dst_w: int, dst_h: int):
        yield 0, 0, dst_w, int(dst_h * factor), 0, 0

    @staticmethod
    def _slide_top(factor: float, dst_w: int, dst_h: int):
        dst_h_ = int(dst_h * factor)
        yield 0, 0, dst_w, dst_h_, 0, dst_h - dst_h_

    @staticmethod
    def _right(factor: float, dst_w: int, dst_h: int):
        dst_w_ = dst_w - int(dst_w * factor)
        yield dst_w_, 0, dst_w - dst_w_, dst_h, dst_w_, 0

    @staticmethod
    def _slide_right(factor: float, dst_w: int, dst_h: int):
        dst_w_ = dst_w - int(dst_w * factor)
        yield dst_w_, 0, dst_w - dst_w_, dst_h, 0, 0

    @staticmethod
    def _bottom(factor: float, dst_w: int, dst_h: int):
        dst_h_ = dst_h - int(dst_h * factor)
        yield 0, dst_h_, dst_w, dst_h - dst_h_, 0, dst_h_

    @staticmethod
    def _slide_bottom(factor: float, dst_w: int, dst_h: int):
        dst_h_ = dst_h - int(dst_h * factor)
        yield 0, dst_h_, dst_w, dst_h - dst_h_, 0, 0

    @staticmethod
    def _top_left(factor: float, dst_w: int, dst_h: int):
        yield 0, 0, int(dst_w * factor), int(dst_h * factor), 0, 0

    @staticmethod
    def _slide_top_left(factor: float, dst_w: int, dst_h: int):
        dst_w_ = int(dst_w * factor)
        dst_h_ = int(dst_h * factor)
        yield 0, 0, dst_w_, dst_h_, dst_w - dst_w_, dst_h - dst_h_

    @staticmethod
    def _top_right(factor: float, dst_w: int, dst_h: int):
        dst_w_ = dst_w - int(dst_w * factor)
        yield dst_w_, 0, dst_w - dst_w_, int(dst_h * factor), dst_w_, 0

    @staticmethod
    def _slide_top_right(factor: float, dst_w: int, dst_h: int):
        dst_w_ = dst_w - int(dst_w * factor)
        dst_h_ = int(dst_h * factor)
        yield dst_w_, 0, dst_w - dst_w_, dst_h_, 0, dst_h - dst_h_

    @staticmethod
    def _bottom_left(factor: float, dst_w: int, dst_h: int):
        dst_h_ = dst_h - int(dst_h * factor)
        yield 0, dst_h_, int(dst_w * factor), dst_h - dst_h_, 0, dst_h_

    @staticmethod
    def _slide_bottom_left(factor: float, dst_w: int, dst_h: int):
        dst_w_ = int(dst_w * factor)
        dst_h_ = dst_h - int(dst_h * factor)
        yield 0, dst_h_, dst_w_, dst_h - dst_h_, dst_w - dst_w_, 0

    @staticmethod
    def _bottom_right(factor: float, dst_w: int, dst_h: int):
        dst_w_ = dst_w - int(dst_w * factor)
        dst_h_ = dst_h - int(dst_h * factor)
        yield dst_w_, dst_h_, dst_w - dst_w_, dst_h - dst_h_, dst_w_, dst_h_

    @staticmethod
    def _slide_bottom_right(factor: float, dst_w: int, dst_h: int):
        dst_w_ = dst_w - int(dst_w * factor)
        dst_h_ = dst_h - int(dst_h * factor)
        yield dst_w_, dst_h_, dst_w - dst_w_, dst_h - dst_h_, 0, 0

    @staticmethod
    def _vertical(factor: float, dst_w: int, dst_h: int):
        dst_w_ = int(dst_w / 2 * (1 - factor))
        yield dst_w_, 0, dst_w - dst_w_ * 2, dst_h, dst_w_, 0

    @staticmethod
    def _reverse_vertical(factor: float, dst_w: int, dst_h: int):
        dst_w_ = int(dst_w / 2 * factor)
        yield 0, 0, dst_w_, dst_h, 0, 0
        yield dst_w - dst_w_, 0, dst_w_, dst_h, dst_w - dst_w_, 0

    @staticmethod
    def _slide_vertical(factor: float, dst_w: int, dst_h: int):
        half_dst_w = dst_w / 2
        dst_w_ = int(half_dst_w * factor)
        half_dst_w_ = int(half_dst_w)
        yield half_dst_w_ - dst_w_, 0, dst_w_, dst_h, 0, 0
        yield half_dst_w_, 0, dst_w_, dst_h, dst_w - dst_w_, 0

    @staticmethod
    def _slide_reverse_vertical(factor: float, dst_w: int, dst_h: int):
        half_dst_w = dst_w / 2
        dst_w_ = int(half_dst_w * factor)
        half_dst_w_ = int(half_dst_w)
        yield 0, 0, dst_w_, dst_h, half_dst_w_ - dst_w_, 0
        yield dst_w - dst_w_, 0, dst_w_, dst_h, half_dst_w_, 0

    @staticmethod
    def _horizontal(factor: float, dst_w: int, dst_h: int):
        dst_h_ = int(dst_h / 2 * (1 - factor))
        yield 0, dst_h_, dst_w, dst_h - dst_h_ * 2, 0, dst_h_

    @staticmethod
    def _reverse_horizontal(factor: float, dst_w: int, dst_h: int):
        dst_h_ = int(dst_h / 2 * factor)
        yield 0, 0, dst_w, dst_h_, 0, 0
        yield 0, dst_h - dst_h_, dst_w, dst_h_, 0, dst_h - dst_h_

    @staticmethod
    def _slide_horizontal(factor: float, dst_w: int, dst_h: int):
        half_dst_h = dst_h / 2
        dst_h_ = int(half_dst_h * factor)
        half_dst_h_ = int(half_dst_h)
        yield 0, half_dst_h_ - dst_h_, dst_w, dst_h_, 0, 0
        yield 0, half_dst_h_, dst_w, dst_h_, 0, dst_h - dst_h_

    @staticmethod
    def _slide_reverse_horizontal(factor: float, dst_w: int, dst_h: int):
        half_dst_h = dst_h / 2
        dst_h_ = int(half_dst_h * factor)
        half_dst_h_ = int(half_dst_h)
        yield 0, 0, dst_w, dst_h_, 0, half_dst_h_ - dst_h_
        yield 0, dst_h - dst_h_, dst_w, dst_h_, 0, half_dst_h_

    @staticmethod
    def _explode(factor: float, dst_w: int, dst_h: int):
        dst_w_ = int(dst_w / 2 * (1 - factor))
        dst_h_ = int(dst_h / 2 * (1 - factor))
        yield dst_w_, dst_h_, dst_w - dst_w_ * 2, dst_h - dst_h_ * 2, dst_w_, dst_h_

    @staticmethod
    def _implode(factor: float, dst_w: int, dst_h: int):
        half_factor = factor / 2
        dst_w_ = int(dst_w * half_factor)
        dst_h_ = int(dst_h * half_factor)
        dst_dw = dst_w - dst_w_
        dst_dh = dst_h - dst_h_
        yield 0, 0, dst_w_, dst_h, 0, 0
        yield dst_w_, 0, dst_w, dst_h_, dst_w_, 0
        yield dst_dw, dst_h_, dst_w - dst_dw, dst_h, dst_dw, dst_h_
        yield dst_w_, dst_dh, dst_w - dst_h_, dst_h - dst_dh, dst_w_, dst_dh


# noinspection PyProtectedMember
_TRANSITIONS = (
    Transition._fade, Transition._explode, Transition._implode,
    Transition._left, Transition._top, Transition._right, Transition._bottom,
    Transition._top_left, Transition._top_right, Transition._bottom_left, Transition._bottom_right,
    Transition._vertical, Transition._horizontal, Transition._reverse_vertical, Transition._reverse_horizontal,
    Transition._slide_left, Transition._slide_top, Transition._slide_right, Transition._slide_bottom,
    Transition._slide_top_left, Transition._slide_top_right, Transition._slide_bottom_left, Transition._slide_bottom_right,
    Transition._slide_vertical, Transition._slide_horizontal, Transition._slide_reverse_vertical, Transition._slide_reverse_horizontal)


def _spawn_workerw():
    user32.SendMessageW(user32.FindWindowW('Progman', None), 0x52C, 0, 0)


@ctyped.type.WNDENUMPROC
def _get_workerw_hwnd_callback(hwnd: ctyped.type.HWND, lparam: ctyped.type.LPARAM) -> ctyped.type.BOOL:
    if user32.FindWindowExW(hwnd, None, 'SHELLDLL_DefView', None) and (
            hwnd_ := user32.FindWindowExW(None, hwnd, 'WorkerW', None)):
        ctyped.from_address(lparam, ctyped.type.LPARAM).value = hwnd_
        return False
    return True


def _get_workerw_hwnd() -> int:
    hwnd = ctyped.type.LPARAM()
    _spawn_workerw()
    user32.EnumWindows(_get_workerw_hwnd_callback, ctyped.addressof(hwnd))
    return hwnd.value


def _get_drives() -> dict[str, str]:
    drives = {}
    buff = ctyped.char_array(size=ctyped.const.MAX_PATH)
    for letter in string.ascii_uppercase:
        path = f'{letter}:'
        if kernel32.QueryDosDeviceW(path, buff, ctyped.const.MAX_PATH):
            drives[buff.value] = path
    return drives


def get_monitor_count() -> int:
    num = ctyped.type.c_int()
    user32.EnumDisplayMonitors(None, None, ctyped.type.MONITORENUMPROC(
        lambda *_: operator.iadd(num, 1)), 0)
    return num.value


def get_known_monitor_ids() -> tuple[str, ...]:
    monitors = []
    with ctyped.interface.COM[ShObjIdl_core.IDesktopWallpaper](
            ctyped.const.CLSID_DesktopWallpaper) as wallpaper:
        if wallpaper:
            count = ctyped.type.UINT()
            wallpaper.GetMonitorDevicePathCount(ctyped.byref(count))
            for index in range(count.value):
                with _utils.string_buffer() as buff:
                    wallpaper.GetMonitorDevicePathAt(index, ctyped.byref(buff))
                    monitors.append(buff.value)
    return tuple(monitors)


# noinspection PyShadowingBuiltins
def get_monitor_name(id: str) -> Optional[str]:
    dev_id = _utils.get_str_dev_id_prop(id, ctyped.const.DEVPKEY_Device_InstanceId)
    return _utils.get_str_dev_node_props(dev_id, ctyped.const.DEVPKEY_NAME)[0] if dev_id else None


def get_monitors() -> dict[str, tuple[str, tuple[int, int]]]:
    monitors = {}
    path_count = ctyped.type.UINT32()
    mode_count = ctyped.type.UINT32()
    if error.ERROR_SUCCESS == user32.GetDisplayConfigBufferSizes(
            ctyped.const.QDC_ONLY_ACTIVE_PATHS, ctyped.byref(path_count), ctyped.byref(mode_count)):
        modes = ctyped.array(type=ctyped.struct.DISPLAYCONFIG_MODE_INFO, size=mode_count.value)
        if error.ERROR_SUCCESS == user32.QueryDisplayConfig(ctyped.const.QDC_ONLY_ACTIVE_PATHS, ctyped.byref(
                path_count), ctyped.array(type=ctyped.struct.DISPLAYCONFIG_PATH_INFO, size=path_count.value), ctyped.byref(mode_count), modes, None):
            name = ctyped.struct.DISPLAYCONFIG_TARGET_DEVICE_NAME(ctyped.struct.DISPLAYCONFIG_DEVICE_INFO_HEADER(
                ctyped.enum.DISPLAYCONFIG_DEVICE_INFO_TYPE.GET_TARGET_NAME, ctyped.sizeof(ctyped.struct.DISPLAYCONFIG_TARGET_DEVICE_NAME)))
            for mode in modes:
                if mode.infoType == ctyped.enum.DISPLAYCONFIG_MODE_INFO_TYPE.TARGET:
                    name.header.adapterId = mode.adapterId
                    name.header.id = mode.id
                    if error.ERROR_SUCCESS == user32.DisplayConfigGetDeviceInfo(ctyped.byref(name.header)):
                        monitors[name.monitorDevicePath] = name.monitorFriendlyDeviceName, (
                            mode.U.targetMode.targetVideoSignalInfo.activeSize.cx, mode.U.targetMode.targetVideoSignalInfo.activeSize.cy)
    return monitors


def get_display_size() -> tuple[int, int]:
    return user32.GetSystemMetrics(
        ctyped.const.SM_CXVIRTUALSCREEN), user32.GetSystemMetrics(ctyped.const.SM_CYVIRTUALSCREEN)


def _get_monitor_rect(dev_path: str) -> Optional[ctyped.struct.RECT]:
    rect = ctyped.struct.RECT()
    with ctyped.interface.COM[ShObjIdl_core.IDesktopWallpaper](ctyped.const.CLSID_DesktopWallpaper) as wallpaper:
        if wallpaper:
            if ctyped.macro.SUCCEEDED(wallpaper.GetMonitorRECT(dev_path, ctyped.byref(rect))):
                return rect


def _get_monitor_x_y_w_h(dev_path: str) -> tuple[int, int, int, int]:
    rect = _get_monitor_rect(dev_path)
    if rect:
        return rect.left - user32.GetSystemMetrics(
            ctyped.const.SM_XVIRTUALSCREEN), rect.top - user32.GetSystemMetrics(
            ctyped.const.SM_YVIRTUALSCREEN), rect.right - rect.left, rect.bottom - rect.top
    return 0, 0, 0, 0


def _get_window_text(hwnd: ctyped.type.HWND) -> Optional[str]:
    if size := user32.GetWindowTextLengthW(hwnd):
        text = ctyped.char_array(size=size + 1)
        if user32.GetWindowTextW(hwnd, text, ctyped.const.MAX_PATH):
            return text.value


def _get_window_exe_path(hwnd: ctyped.type.HWND, drives: Optional[dict[str, str]] = None) -> str:
    file_name = ''
    pid = ctyped.type.DWORD()
    user32.GetWindowThreadProcessId(hwnd, ctyped.byref(pid))
    if handle := kernel32.OpenProcess(ctyped.const.PROCESS_QUERY_LIMITED_INFORMATION, False, pid):
        buff = ctyped.char_array(size=ctyped.const.MAX_PATH + 1)
        if psapi.GetProcessImageFileNameW(handle, buff, ctyped.const.MAX_PATH):
            file_name = buff.value
        kernel32.CloseHandle(handle)
    if drives:
        for drive, path in drives.items():
            if file_name.startswith(drive):
                file_name = file_name.replace(drive, path, 1)
                break
    return file_name


def _get_window_frame_rect(hwnd: ctyped.type.HWND) -> Optional[ctyped.struct.RECT]:
    rect = ctyped.struct.RECT()
    if ctyped.macro.SUCCEEDED(dwmapi.DwmGetWindowAttribute(
            hwnd, ctyped.enum.DWMWINDOWATTRIBUTE.EXTENDED_FRAME_BOUNDS, ctyped.byref(rect), ctyped.sizeof(rect))):
        return rect


def _get_window_monitor(hwnd: ctyped.type.HWND, monitor_rects: Optional[dict[str, ctyped.struct.RECT]] = None) -> Optional[str]:
    if monitor_rects is None:
        monitor_rects = {monitor: _get_monitor_rect(monitor) for monitor in get_monitors()}
    hmonitor = user32.MonitorFromWindow(hwnd, ctyped.const.MONITOR_DEFAULTTONEAREST)
    if hmonitor:
        info = ctyped.struct.MONITORINFO()
        if user32.GetMonitorInfoW(hmonitor, ctyped.byref(info)):
            for monitor, rect in monitor_rects.items():
                if user32.EqualRect(ctyped.byref(rect), ctyped.byref(info.rcMonitor)):
                    return monitor


def _get_window_pid(hwnd: ctyped.type.HWND) -> int:
    pid = ctyped.type.DWORD()
    user32.GetWindowThreadProcessId(hwnd, ctyped.byref(pid))
    return pid.value


def get_display_blockers(*monitors: str, full_screen_only: bool = False,
                         fullscreen: bool = True) -> dict[str, tuple[str, ...]]:
    blockers = {monitor: set() for monitor in monitors}
    rects_or_regions = {monitor: _get_monitor_rect(monitor) for monitor in monitors}
    drives = _get_drives()

    if fullscreen:
        dummy = ctyped.struct.RECT()
        placement = ctyped.struct.WINDOWPLACEMENT()

        def wind_enum_proc(hwnd: ctyped.type.HWND, _: ctyped.type.LPARAM) -> ctyped.type.BOOL:
            if user32.GetWindowPlacement(hwnd, ctyped.byref(
                    placement)) and placement.showCmd == ctyped.const.SW_MAXIMIZE:
                monitor = _get_window_monitor(hwnd, rects_or_regions)
                if monitor and not (full_screen_only and user32.SubtractRect(ctyped.byref(dummy), ctyped.byref(
                        rects_or_regions[monitor]), ctyped.byref(_get_window_frame_rect(hwnd) or ctyped.struct.RECT()))):
                    blockers[monitor].add(_get_window_exe_path(hwnd, drives))
            return True
    else:
        rects_or_regions = {monitor: _handle.HRGN.from_rect(rect) for monitor, rect in rects_or_regions.items()}
        explorer_pid = _get_window_pid(user32.FindWindowW('Shell_TrayWnd', None))

        def wind_enum_proc(hwnd: ctyped.type.HWND, _: ctyped.type.LPARAM) -> ctyped.type.BOOL:
            if explorer_pid != _get_window_pid(hwnd):
                window_region = _handle.HRGN.from_rect(_get_window_frame_rect(hwnd))
                for monitor, region_ in rects_or_regions.items():
                    diff_region = _handle.HRGN.from_combination(region_, window_region, ctyped.const.RGN_DIFF)
                    if not region_.is_equal(diff_region):
                        rects_or_regions[monitor] = diff_region
                        blockers[monitor].add(_get_window_exe_path(hwnd, drives))
            return True

    user32.EnumWindows(ctyped.type.WNDENUMPROC(wind_enum_proc), 0)
    if not fullscreen:
        for monitor, region in rects_or_regions.items():
            if not region.is_empty():
                blockers[monitor].clear()
    for monitor, blockers_ in blockers.items():
        blockers[monitor] = tuple(blockers_)
    return blockers


def is_desktop_unblocked(*monitors: str) -> dict[str, bool]:
    hwnd = _get_workerw_hwnd()
    if hwnd:
        hdc = _handle.HDC.from_hwnd(hwnd)
        return {monitor: bool(gdi32.RectVisible(hdc, ctyped.byref(
            ctyped.struct.RECT(*_get_monitor_x_y_w_h(monitor))))) for monitor in monitors}
    return {monitor: True for monitor in monitors}


def get_desktop_blocker(*monitors: str) -> dict[str, Optional[tuple[str, str]]]:
    blockers = {monitor: None for monitor in monitors}
    rects = {monitor: _get_monitor_rect(monitor) for monitor in monitors}
    drives = _get_drives()

    @ctyped.type.WNDENUMPROC
    def wnd_enum_proc(hwnd: ctyped.type.HWND, _: ctyped.type.LPARAM) -> ctyped.type.BOOL:
        if (monitor := _get_window_monitor(hwnd, rects)) and blockers[monitor] is None:
            blockers[monitor] = _get_window_text(hwnd), _get_window_exe_path(hwnd, drives)
        return not all(blockers.values())

    user32.EnumChildWindows(_get_workerw_hwnd(), wnd_enum_proc, 0)
    return blockers


def get_wallpaper_style() -> Optional[int]:
    with ctyped.interface.COM[ShlObj_core.IActiveDesktop](ctyped.const.CLSID_ActiveDesktop) as desktop:
        if desktop:
            opt = ctyped.struct.WALLPAPEROPT()
            if ctyped.macro.SUCCEEDED(desktop.GetWallpaperOptions(ctyped.byref(opt), 0)):
                return opt.dwStyle


def _get_wallpaper_param() -> str:
    with _utils.string_buffer(ctyped.const.SHRT_MAX) as buff:
        user32.SystemParametersInfoW(ctyped.const.SPI_GETDESKWALLPAPER, ctyped.const.SHRT_MAX, buff, 0)
        return buff.value


def _get_wallpaper_iactivedesktop() -> str:
    with _utils.string_buffer(ctyped.const.SHRT_MAX) as buff:
        with ctyped.interface.COM[ShlObj_core.IActiveDesktop](ctyped.const.CLSID_ActiveDesktop) as desktop:
            if desktop:
                desktop.GetWallpaper(buff, ctyped.const.SHRT_MAX, ctyped.const.AD_GETWP_BMP)
        return buff.value


def _get_wallpaper_idesktopwallpaper(*monitors: str) -> tuple[str, ...]:
    with ctyped.interface.COM[ShObjIdl_core.IDesktopWallpaper](ctyped.const.CLSID_DesktopWallpaper) as wallpaper:
        if wallpaper:
            with _utils.string_buffer() as buff:
                return tuple(buff.value if ctyped.macro.SUCCEEDED(wallpaper.GetWallpaper(
                    monitor, ctyped.byref(buff))) else '' for monitor in (monitors or get_monitors()))
        else:
            return ()


def get_wallpaper(monitor: Optional[str] = None) -> str:
    return ((_get_wallpaper_param() or _get_wallpaper_iactivedesktop())
            if monitor is None else _get_wallpaper_idesktopwallpaper(monitor)[0])


def _get_rotate_flip(rotate: Rotate, flip: Flip) -> ctyped.enum.RotateFlipType:
    if (rotate is Rotate.RIGHT and flip is Flip.NONE) or (
            rotate is Rotate.LEFT and flip is Flip.BOTH):
        return ctyped.enum.RotateFlipType.Rotate90FlipNone
    elif (rotate is Rotate.FLIP and flip is Flip.NONE) or (
            rotate is Rotate.NONE and flip is Flip.BOTH):
        return ctyped.enum.RotateFlipType.Rotate180FlipNone
    elif (rotate is Rotate.LEFT and flip is Flip.NONE) or (
            rotate is Rotate.RIGHT and flip is Flip.BOTH):
        return ctyped.enum.RotateFlipType.Rotate270FlipNone
    elif (rotate is Rotate.NONE and flip is Flip.HORIZONTAL) or (
            rotate is Rotate.FLIP and flip is Flip.VERTICAL):
        return ctyped.enum.RotateFlipType.RotateNoneFlipX
    elif (rotate is Rotate.RIGHT and flip is Flip.HORIZONTAL) or (
            rotate is Rotate.LEFT and flip is Flip.VERTICAL):
        return ctyped.enum.RotateFlipType.Rotate90FlipX
    elif (rotate is Rotate.FLIP and flip is Flip.HORIZONTAL) or (
            rotate is Rotate.NONE and flip is Flip.VERTICAL):
        return ctyped.enum.RotateFlipType.Rotate180FlipX
    elif (rotate is Rotate.LEFT and flip is Flip.HORIZONTAL) or (
            rotate is Rotate.RIGHT and flip is Flip.VERTICAL):
        return ctyped.enum.RotateFlipType.Rotate270FlipX
    else:
        return ctyped.enum.RotateFlipType.RotateNoneFlipNone


def _get_src_x_y_w_h(w: int, h: int, src_w: int, src_h: int,
                     style: Style = Style.FILL) -> Iterable[int]:
    if style is Style.CENTER:
        dw = src_w - w
        dh = src_h - h
        return int(dw / 2), int(dh / 2), src_w - dw, src_h - dh
    elif style in (Style.TILE, Style.STRETCH):
        return 0, 0, src_w, src_h
    elif style == Style.FIT:
        # noinspection PyProtectedMember
        return map(round, _gdiplus._calc_src_x_y_w_h(src_w, src_h, w, h, w / src_w > h / src_h))
    elif style in (Style.FILL, Style.SPAN):
        # noinspection PyProtectedMember
        return map(round, _gdiplus._calc_src_x_y_w_h(src_w, src_h, w, h, w / src_w < h / src_h))
    return 0, 0, 0, 0


def _save_tmp_bmp(src: _gdiplus.Bitmap, color: ctyped.type.ARGB, width: int, height: int,
                  src_x: int, src_y: int, src_w: int, src_h: int, temp_path: str) -> _handle.HDC:
    bitmap = _gdiplus.bitmap_from_color(color, width, height)
    bitmap.set_resolution(src.get_horizontal_resolution(), src.get_vertical_resolution())
    graphics = _gdiplus.Graphics.from_image(bitmap)
    graphics.scale_transform(width / src_w, height / src_h)
    graphics.draw_image_from_rect(src, -min(0, src_x), -min(0, src_y), max(0, src_x), max(0, src_y))
    _gdiplus.image_save(bitmap, temp_path)
    return bitmap.get_hbitmap().get_hdc()


def _is_rect_not_blocked(hwnd: ctyped.type.HWND, dst_x: int, dst_y: int, dst_w: int, dst_h: int) -> bool:
    fore_rect = ctyped.struct.RECT()
    fore_hwnd = user32.GetForegroundWindow()
    if (fore_hwnd and user32.GetClientRect(fore_hwnd, ctyped.byref(fore_rect)) and
            user32.MapWindowPoints(fore_hwnd, hwnd, ctyped.cast(fore_rect, ctyped.struct.POINT), 2)):
        return bool(user32.SubtractRect(ctyped.byref(ctyped.struct.RECT()), ctyped.byref(
            ctyped.struct.RECT(dst_x, dst_y, dst_x + dst_w, dst_y + dst_h)), ctyped.byref(fore_rect)))
    return True


def _draw_on_workerw(image: _gdiplus.Bitmap, dst_x: int, dst_y: int, dst_w: int, dst_h: int,
                     src_x: int, src_y: int, src_w: int, src_h: int, temp_path: str,
                     color: _gdiplus.Color, transition: Transition, duration: float, easing: Callable[[float], float]):
    if (hwnd := _get_workerw_hwnd()) and _is_rect_not_blocked(hwnd, dst_x, dst_y, dst_w, dst_h):
        dst = _handle.HDC.from_hwnd(hwnd)
        src = _save_tmp_bmp(image, color, dst_w, dst_h, src_x, src_y, src_w, src_h, temp_path)
        if transition is not Transition.DISABLED:
            # noinspection PyTypeChecker
            transitioning = random.choice(
                _TRANSITIONS) if transition is Transition.RANDOM else _TRANSITIONS[transition.value]
            # noinspection PyProtectedMember
            if transitioning is Transition._fade:
                dst_bk = _handle.HBITMAP.from_dimension(dst_w, dst_h).get_hdc()
                gdi32.BitBlt(dst_bk, 0, 0, dst_w, dst_h, dst, dst_x, dst_y, ctyped.const.SRCPAINT)
                transitioning = functools.partial(
                    transitioning, dst, dst_x, dst_y, src, ctyped.struct.BLENDFUNCTION(),
                    dst_bk, _handle.HBITMAP.from_dimension(dst_w, dst_h).get_hdc())
            start = time.monotonic()
            while duration > (passed := time.monotonic() - start):
                for dst_ox, dst_oy, dst_ow, dst_oh, src_ox, src_oy in transitioning(
                        easing(passed / duration), dst_w, dst_h):
                    gdi32.BitBlt(dst, dst_x + dst_ox, dst_y + dst_oy, dst_ow, dst_oh,
                                 src, src_ox, src_oy, ctyped.const.SRCCOPY)
                time.sleep(ANIMATION_POLL_INTERVAL)
        gdi32.BitBlt(dst, dst_x, dst_y, dst_w, dst_h, src, 0, 0, ctyped.const.SRCCOPY)


def _set_wallpaper_param(path: str) -> bool:
    return bool(user32.SystemParametersInfoW(
        ctyped.const.SPI_SETDESKWALLPAPER, 0, path, ctyped.const.SPIF_SENDWININICHANGE))


def _set_wallpaper_iactivedesktop(path: str, fade: bool = True) -> bool:
    with ctyped.interface.COM[ShlObj_core.IActiveDesktop](ctyped.const.CLSID_ActiveDesktop) as desktop:
        if desktop:
            if fade:
                _spawn_workerw()
            return ctyped.macro.SUCCEEDED(desktop.SetWallpaper(
                path, 0)) and ctyped.macro.SUCCEEDED(desktop.ApplyChanges(ctyped.const.AD_APPLY_ALL))
    return False


def _set_wallpaper_idesktopwallpaper(path: str, monitor: Optional[str], color: Optional[ctyped.type.COLORREF] = None,
                                     style: Optional[int | ctyped.enum.DESKTOP_WALLPAPER_POSITION | Style] = None) -> bool:
    with ctyped.interface.COM[ShObjIdl_core.IDesktopWallpaper](ctyped.const.CLSID_DesktopWallpaper) as wallpaper:
        if wallpaper:
            if color is not None and ctyped.macro.FAILED(wallpaper.SetBackgroundColor(color)):
                return False
            if style is not None:
                if ctyped.macro.FAILED(wallpaper.SetPosition(style)):
                    return False
            if style in (Style.SPAN, Style.TILE):
                return _set_wallpaper_param(path)
            else:
                return ctyped.macro.SUCCEEDED(wallpaper.SetWallpaper(monitor, path))
    return False


def set_wallpaper(path: str, *monitors: str, fade: bool = True):
    return _set_wallpaper_idesktopwallpaper(path, *monitors) if monitors else _set_wallpaper_iactivedesktop(
        path, fade) if fade else _set_wallpaper_param(path)


_temp_lock = functools.lru_cache(lambda _: threading.Lock())


def set_wallpaper_ex(path: str, monitor: Optional[str] = None, style: Style = Style.FILL,
                     rgb: tuple[int, int, int] = (0, 0, 0), rotate: Rotate = Rotate.NONE,
                     flip: Flip = Flip.NONE, transition: Transition = Transition.DISABLED,
                     duration: float = 1.0, easing: Callable[[float], float] = lambda x: x) -> bool:
    if image := _gdiplus.Bitmap.from_file(path):
        if rotate is not Rotate.NONE or flip is not Flip.NONE:
            image.rotate_flip(_get_rotate_flip(rotate, flip))
        width = image.get_width()
        height = image.get_height()
        if style in (Style.TILE, Style.SPAN):
            monitor = 'DISPLAY'
            monitor_x_y_w_h = 0, 0, *get_display_size()
            if style is Style.TILE:
                width_ = monitor_x_y_w_h[2]
                height_ = monitor_x_y_w_h[3]
                bitmap = _gdiplus.Bitmap.from_dimension(width_, height_)
                graphics = _gdiplus.Graphics.from_image(bitmap)
                image.set_resolution(graphics.get_dpi_x(), graphics.get_dpi_y())
                for x in range(0, width_, width):
                    for y in range(0, height_, height):
                        graphics.draw_image(image, x, y)
                image = bitmap
                width = width_
                height = height_
        else:
            monitor_x_y_w_h = _get_monitor_x_y_w_h(monitor)
        os.makedirs(TEMP_WALLPAPER_DIR, exist_ok=True)
        temp_path = ntpath.join(TEMP_WALLPAPER_DIR, f'{_utils.sanitize_filename(monitor)}.jpg')
        with _temp_lock(temp_path):
            # noinspection PyTypeChecker
            _draw_on_workerw(image, *monitor_x_y_w_h, *_get_src_x_y_w_h(*monitor_x_y_w_h[2:], width, height, style),
                             temp_path, _gdiplus.Color.from_rgba(*rgb), transition, duration, easing)
            return _set_wallpaper_idesktopwallpaper(
                temp_path, monitor, style=style if style in (Style.TILE, Style.SPAN) else Style.FILL)
    return False


class Wallpaper(NamedTuple):
    path: str
    monitor: Optional[str] = None
    style: Style = Style.FILL
    rgb: tuple[int, int, int] = 0, 0, 0
    rotate: Rotate = Rotate.NONE
    flip: Flip = Flip.NONE
    transition: Transition = Transition.DISABLED
    duration: float = 1.0
    easing: Callable[[float], float] = lambda x: x


def set_wallpapers_ex(*wallpapers: Wallpaper):
    with concurrent.futures.ThreadPoolExecutor(
            thread_name_prefix=set_wallpaper_ex.__name__) as executor:
        futures = tuple(executor.submit(
            set_wallpaper_ex, *wallpaper) for wallpaper in wallpapers)
    return all(future.result() for future in futures)


def set_lock_background(path: str) -> bool:
    if (p_file := _utils.open_file(path)) and (
            p_statics := ctyped.interface.WinRT[Windows_System_UserProfile.ILockScreenStatics](
                runtimeclass.Windows.System.UserProfile.LockScreen)):
        action = winrt.AsyncAction()
        with p_file as file, p_statics as statics:
            if ctyped.macro.SUCCEEDED(statics.SetImageFileAsync(file, ~action)):
                return ctyped.enum.Windows.Foundation.AsyncStatus.Completed == action.wait()
    return False


def set_slideshow(*paths: str) -> bool:
    with _utils.get_itemidlist(*paths) as pidl, ctyped.interface.COM[ShObjIdl_core.IDesktopWallpaper](ctyped.const.CLSID_DesktopWallpaper) as wallpaper:
        if wallpaper:
            with ctyped.interface.COM[ShObjIdl_core.IShellItemArray]() as shl_arr:
                id_arr = ctyped.array(*pidl)
                return ctyped.macro.SUCCEEDED(
                    shell32.SHCreateShellItemArrayFromIDLists(len(id_arr), ctyped.byref(
                        id_arr[0]), ctyped.byref(shl_arr))) and ctyped.macro.SUCCEEDED(wallpaper.SetSlideshow(shl_arr))
    return False


def save_lock_background(path: str) -> bool:
    if p_input_stream := _utils.get_lock_background_input_stream():
        os.makedirs(ntpath.dirname(path), exist_ok=True)
        open(path, 'w').close()
        if p_file := _utils.open_file(path):
            with p_file as file:
                if p_o_stream := _utils.get_output_stream(file):
                    with p_input_stream as i_stream, p_o_stream as o_stream:
                        return _utils.copy_stream(i_stream, o_stream)
    return False


def remove_wallpaper_history(*paths: str) -> bool:
    removed = True
    paths = tuple(path.casefold() for path in paths)
    with winreg.OpenKey(
            winreg.HKEY_CURRENT_USER, _HISTORY_KEY, access=winreg.KEY_QUERY_VALUE | winreg.KEY_SET_VALUE) as key:
        for index in range(5):
            name = f'BackgroundHistoryPath{index}'
            val, type_ = winreg.QueryValueEx(key, name)
            if type_ == winreg.REG_SZ and val.casefold() in paths:
                removed = _utils.delete_key(key, name) and removed
    return removed
