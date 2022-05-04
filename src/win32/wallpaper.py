import collections
import concurrent.futures
import contextlib
import functools
import ntpath
import operator
import os
import random
import tempfile
import threading
import time
import typing
import winreg
from typing import Any, Callable, ContextManager, Iterable, Mapping, Optional, Union

import libs.ctyped as ctyped
from . import _utils, _gdiplus

_HWND_RETRY = 5
_DELETE_AFTER = 0.5
_TEMP_FILE = '{}.jpg'
_HISTORY_KEY = ntpath.join('Software', 'Microsoft', 'Windows', 'CurrentVersion', 'Explorer', 'Wallpapers')

TEMP_DIR = tempfile.gettempdir()


class _IntEnum(type):
    def __new__(mcs, *args, **kwargs):
        self = super().__new__(mcs, *args, **kwargs)
        self._vars = {var: val for var, val in vars(self).items() if not var.startswith('_')}
        return self

    def __contains__(cls, item):
        return item in cls._vars

    def __iter__(self):
        return iter(self._vars)

    @typing.overload
    def __getitem__(self, var_or_val: int) -> str:
        pass

    @typing.overload
    def __getitem__(self, var_or_val: str) -> int:
        pass

    def __getitem__(self, var_or_val):
        if isinstance(var_or_val, int):
            for var, val_ in self._vars.items():
                if var_or_val == val_:
                    return var
            raise IndexError
        else:
            return self._vars[var_or_val]

    def get_random(self, *ignores: int) -> int:
        vals = tuple(self._vars.values())
        while (rand := random.choice(vals)) in ignores:
            pass
        return rand


class Style(metaclass=_IntEnum):
    FILL = ctyped.const.WPSTYLE_CROPTOFIT
    FIT = ctyped.const.WPSTYLE_KEEPASPECT
    STRETCH = ctyped.const.WPSTYLE_STRETCH
    TILE = ctyped.const.WPSTYLE_TILE
    CENTER = ctyped.const.WPSTYLE_CENTER
    SPAN = ctyped.const.WPSTYLE_SPAN


class Transition(metaclass=_IntEnum):
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
    def _fade(factor: float, dst_w: int, dst_h: int, dst: ctyped.type.HDC, dst_x: int, dst_y: int, src: ctyped.type.HDC,
              blend: ctyped.struct.BLENDFUNCTION, dst_bk: ctyped.type.HDC, tmp_dst: ctyped.type.HDC):
        blend.SourceConstantAlpha = int(255 * factor)
        ctyped.lib.Gdi32.BitBlt(tmp_dst, 0, 0, dst_w, dst_h, dst_bk, 0, 0, ctyped.const.SRCCOPY)
        ctyped.lib.Msimg32.AlphaBlend(tmp_dst, 0, 0, dst_w, dst_h, src, 0, 0, dst_w, dst_h, blend)
        ctyped.lib.Gdi32.BitBlt(dst, dst_x, dst_y, dst_w, dst_h, tmp_dst, 0, 0, ctyped.const.SRCCOPY)
        return
        # noinspection PyUnreachableCode
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
    def _vertical(factor: float, dst_w: int, dst_h: int, half_dst_w: float):
        dst_w_ = int(half_dst_w * (1 - factor))
        yield dst_w_, 0, dst_w - dst_w_ * 2, dst_h, dst_w_, 0

    @staticmethod
    def _reverse_vertical(factor: float, dst_w: int, dst_h: int, half_dst_w: float):
        dst_w_ = int(half_dst_w * factor)
        yield 0, 0, dst_w_, dst_h, 0, 0
        yield dst_w - dst_w_, 0, dst_w_, dst_h, dst_w - dst_w_, 0

    @staticmethod
    def _slide_vertical(factor: float, dst_w: int, dst_h: int, half_dst_w: float):
        dst_w_ = int(half_dst_w * factor)
        half_dst_w_ = int(half_dst_w)
        yield half_dst_w_ - dst_w_, 0, dst_w_, dst_h, 0, 0
        yield half_dst_w_, 0, dst_w_, dst_h, dst_w - dst_w_, 0

    @staticmethod
    def _slide_reverse_vertical(factor: float, dst_w: int, dst_h: int, half_dst_w: float):
        dst_w_ = int(half_dst_w * factor)
        half_dst_w_ = int(half_dst_w)
        yield 0, 0, dst_w_, dst_h, half_dst_w_ - dst_w_, 0
        yield dst_w - dst_w_, 0, dst_w_, dst_h, half_dst_w_, 0

    @staticmethod
    def _horizontal(factor: float, dst_w: int, dst_h: int, half_dst_h: float):
        dst_h_ = int(half_dst_h * (1 - factor))
        yield 0, dst_h_, dst_w, dst_h - dst_h_ * 2, 0, dst_h_

    @staticmethod
    def _reverse_horizontal(factor: float, dst_w: int, dst_h: int, half_dst_h: float):
        dst_h_ = int(half_dst_h * factor)
        yield 0, 0, dst_w, dst_h_, 0, 0
        yield 0, dst_h - dst_h_, dst_w, dst_h_, 0, dst_h - dst_h_

    @staticmethod
    def _slide_horizontal(factor: float, dst_w: int, dst_h: int, half_dst_h: float):
        dst_h_ = int(half_dst_h * factor)
        half_dst_h_ = int(half_dst_h)
        yield 0, half_dst_h_ - dst_h_, dst_w, dst_h_, 0, 0
        yield 0, half_dst_h_, dst_w, dst_h_, 0, dst_h - dst_h_

    @staticmethod
    def _slide_reverse_horizontal(factor: float, dst_w: int, dst_h: int, half_dst_h: float):
        dst_h_ = int(half_dst_h * factor)
        half_dst_h_ = int(half_dst_h)
        yield 0, 0, dst_w, dst_h_, 0, half_dst_h_ - dst_h_
        yield 0, dst_h - dst_h_, dst_w, dst_h_, 0, half_dst_h_

    @staticmethod
    def _explode(factor: float, dst_w: int, dst_h: int, half_dst_w: float, half_dst_h: float):
        dst_w_ = int(half_dst_w * (1 - factor))
        dst_h_ = int(half_dst_h * (1 - factor))
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

    # noinspection PyUnresolvedReferences
    _TRANSITIONS = tuple(static.__func__ for static in (
        _fade, _explode, _implode, _left, _top, _right, _bottom, _top_left, _top_right, _bottom_left, _bottom_right,
        _vertical, _horizontal, _reverse_vertical, _reverse_horizontal,
        _slide_left, _slide_top, _slide_right, _slide_bottom,
        _slide_top_left, _slide_top_right, _slide_bottom_left, _slide_bottom_right,
        _slide_vertical, _slide_horizontal, _slide_reverse_vertical, _slide_reverse_horizontal))


def get_monitor_count() -> int:
    num = ctyped.type.c_int()
    ctyped.lib.User32.EnumDisplayMonitors(None, None, ctyped.type.MONITORENUMPROC(lambda *_: operator.iadd(num, 1)), 0)
    return num.value


def get_monitor_ids() -> tuple[str, ...]:
    monitors = []
    with ctyped.init_com(ctyped.interface.IDesktopWallpaper) as wallpaper:
        if wallpaper:
            count = ctyped.type.UINT()
            wallpaper.GetMonitorDevicePathCount(ctyped.byref(count))
            for index in range(count.value):
                with _utils.string_buffer() as buff:
                    wallpaper.GetMonitorDevicePathAt(index, ctyped.byref(buff))
                    monitors.append(buff.value)
    return tuple(monitors)


def get_monitor_name(id_: str) -> Optional[str]:
    dev_id = _utils.get_str_dev_id_prop(id_, ctyped.const.DEVPKEY_Device_InstanceId)
    return _utils.get_str_dev_node_props(dev_id, ctyped.const.DEVPKEY_NAME)[0] if dev_id else None


def get_style() -> Optional[int]:
    with ctyped.init_com(ctyped.interface.IActiveDesktop) as desktop:
        if desktop:
            opt = ctyped.struct.WALLPAPEROPT()
            if ctyped.macro.SUCCEEDED(desktop.GetWallpaperOptions(ctyped.byref(opt), 0)):
                return opt.dwStyle
    return None


def _get_param() -> str:
    with _utils.string_buffer(ctyped.const.SHRT_MAX) as buff:
        ctyped.lib.User32.SystemParametersInfoW(ctyped.const.SPI_GETDESKWALLPAPER, ctyped.const.SHRT_MAX, buff, 0)
        return buff.value


def _get_iactivedesktop() -> str:
    with _utils.string_buffer(ctyped.const.SHRT_MAX) as buff:
        with ctyped.init_com(ctyped.interface.IActiveDesktop) as desktop:
            if desktop:
                desktop.GetWallpaper(buff, ctyped.const.SHRT_MAX, ctyped.const.AD_GETWP_BMP)
        return buff.value


def _get_idesktopwallpaper(*monitors: str) -> tuple[str, ...]:
    with ctyped.init_com(ctyped.interface.IDesktopWallpaper) as wallpaper:
        if wallpaper:
            with _utils.string_buffer() as buff:
                return tuple(buff.value if ctyped.macro.SUCCEEDED(wallpaper.GetWallpaper(
                    monitor, ctyped.byref(buff))) else '' for monitor in (monitors or get_monitor_ids()))
        else:
            return ()


def get(monitor: Optional[str] = None) -> str:
    return ((_get_param() or _get_iactivedesktop())
            if monitor is None else _get_idesktopwallpaper(monitor)[0])


def _get_monitor_x_y_w_h(dev_path: str) -> tuple[int, int, int, int]:
    rect = ctyped.struct.RECT()
    with ctyped.init_com(ctyped.interface.IDesktopWallpaper) as wallpaper:
        if wallpaper:
            if ctyped.macro.SUCCEEDED(wallpaper.GetMonitorRECT(dev_path, ctyped.byref(rect))):
                return rect.left - ctyped.lib.User32.GetSystemMetrics(
                    ctyped.const.SM_XVIRTUALSCREEN), rect.top - ctyped.lib.User32.GetSystemMetrics(
                    ctyped.const.SM_YVIRTUALSCREEN), rect.right - rect.left, rect.bottom - rect.top
    return 0, 0, 0, 0


def _spawn_workerw():
    ctyped.lib.User32.SendMessageW(ctyped.lib.User32.FindWindowW('Progman', 'Program Manager'), 0x52C, 0, 0)


@ctyped.type.WNDENUMPROC
def _get_workerw_hwnd_callback(hwnd: ctyped.type.HWND, lparam: ctyped.type.LPARAM):
    if ctyped.lib.User32.FindWindowExW(hwnd, None, 'SHELLDLL_DefView', None) and (
            hwnd_ := ctyped.lib.User32.FindWindowExW(None, hwnd, 'WorkerW', None)):
        ctyped.from_address(lparam, ctyped.type.LPARAM).value = hwnd_
    return True


def _get_workerw_hwnd() -> Optional[int]:
    hwnd = ctyped.type.LPARAM()
    for _ in range(_HWND_RETRY):
        _spawn_workerw()
        if ctyped.lib.User32.EnumWindows(_get_workerw_hwnd_callback, ctyped.addressof(hwnd)) and hwnd.value:
            return hwnd.value


def _fit_by(from_w: int, from_h: int, to_w: int, to_h: int,
            by_h: bool = True, div: int = 2) -> tuple[int, int, int, int]:
    ratio = to_w / to_h
    if by_h:
        w = from_h * ratio
        return round((from_w - w) / div), 0, int(w), from_h
    else:
        h = from_w / ratio
        return 0, round((from_h - h) / div), from_w, int(h)


def _get_src_x_y_w_h(w: int, h: int, src_w: int, src_h: int,
                     style: int = Style.FILL) -> tuple[int, int, int, int]:
    if style == Style.CENTER:
        dw = src_w - w
        dh = src_h - h
        return int(dw / 2), int(dh / 2), src_w - dw, src_h - dh
    elif style in (Style.TILE, Style.STRETCH):
        return 0, 0, src_w, src_h
    elif style == Style.FIT:
        return _fit_by(src_w, src_h, w, h, w / src_w > h / src_h)
    elif style == Style.FILL:
        return _fit_by(src_w, src_h, w, h, w / src_w < h / src_h, 3)
    elif style == Style.SPAN:
        return _fit_by(src_w, src_h, w, h, w / src_w < h / src_h)
    return 0, 0, 0, 0


def _save_temp_bmp(width: int, height: int, color: ctyped.type.ARGB, src: _gdiplus.Bitmap,
                   src_x: int, src_y: int, src_w: int, src_h: int, temp_path: str) -> ctyped.handle.HDC:
    bitmap = _gdiplus.Bitmap.from_dimension(width, height)
    graphics = bitmap.get_graphics()
    graphics.fill_rect_with_color(color, 0, 0, width, height)
    graphics.set_scale(width / src_w, height / src_h)
    src.set_resolution(graphics.get_dpi_x(), graphics.get_dpi_y())
    graphics.draw_image_from_rect(src, -min(0, src_x), -min(0, src_y), max(0, src_x), max(0, src_y))
    bitmap.save(temp_path)
    return bitmap.get_hbitmap().get_hdc()


def _is_visible(hwnd: ctyped.type.HWND, dst_x: int, dst_y: int, dst_w: int, dst_h: int) -> bool:
    rect = ctyped.struct.RECT()
    fore_hwnd = ctyped.lib.User32.GetForegroundWindow()
    if (fore_hwnd and ctyped.lib.User32.GetClientRect(fore_hwnd, ctyped.byref(rect)) and
            ctyped.lib.User32.MapWindowPoints(fore_hwnd, hwnd, ctyped.cast(rect, ctyped.struct.POINT), 2)):
        rect_ = ctyped.struct.RECT(dst_x, dst_y, dst_x + dst_w, dst_y + dst_h)
        return bool(ctyped.lib.User32.SubtractRect(ctyped.byref(rect_), ctyped.byref(rect_), ctyped.byref(rect)))
    return True


def _draw_on_workerw(image: _gdiplus.Bitmap, dst_x: int, dst_y: int, dst_w: int, dst_h: int,
                     src_x: int, src_y: int, src_w: int, src_h: int, temp_path: str,
                     color: ctyped.type.ARGB = 0, transition: int = Transition.DISABLED, duration: float = 0):
    if (hwnd := _get_workerw_hwnd()) and _is_visible(hwnd, dst_x, dst_y, dst_w, dst_h):
        dst = ctyped.handle.HDC.from_hwnd(hwnd)
        src = _save_temp_bmp(dst_w, dst_h, color, image, src_x, src_y, src_w, src_h, temp_path)
        if transition != Transition.DISABLED:
            if transition == Transition.RANDOM:
                transition = Transition.get_random(Transition.DISABLED, Transition.RANDOM)
            args = []
            if transition == Transition.FADE:
                dst_bk = ctyped.handle.HBITMAP.from_dimension(dst_w, dst_h).get_hdc()
                ctyped.lib.Gdi32.BitBlt(dst_bk, 0, 0, dst_w, dst_h, dst, dst_x, dst_y, ctyped.const.SRCPAINT)
                args.extend((dst, dst_x, dst_y, src, ctyped.struct.BLENDFUNCTION(),
                             dst_bk, ctyped.handle.HBITMAP.from_dimension(dst_w, dst_h).get_hdc()))
            if transition in (Transition.VERTICAL, Transition.REVERSE_VERTICAL,
                              Transition.EXPLODE, Transition.SLIDE_VERTICAL, Transition.SLIDE_REVERSE_VERTICAL):
                args.append(dst_w / 2)
            if transition in (Transition.HORIZONTAL, Transition.REVERSE_HORIZONTAL,
                              Transition.EXPLODE, Transition.SLIDE_HORIZONTAL, Transition.SLIDE_REVERSE_HORIZONTAL):
                args.append(dst_h / 2)
            start = time.time()
            while duration > (passed := time.time() - start):
                # noinspection PyProtectedMember
                for dst_ox, dst_oy, dst_w_, dst_h_, src_ox, src_oy in Transition._TRANSITIONS[transition](
                        passed / duration, dst_w, dst_h, *args):
                    ctyped.lib.Gdi32.BitBlt(dst, dst_x + dst_ox, dst_y + dst_oy, dst_w_, dst_h_,
                                            src, src_ox, src_oy, ctyped.const.SRCCOPY)
        ctyped.lib.Gdi32.BitBlt(dst, dst_x, dst_y, dst_w, dst_h, src, 0, 0, ctyped.const.SRCCOPY)


def _set_param(path: str) -> bool:
    return bool(ctyped.lib.User32.SystemParametersInfoW(
        ctyped.const.SPI_SETDESKWALLPAPER, 0, path, ctyped.const.SPIF_SENDWININICHANGE))


def _set_iactivedesktop(path: str, fade: bool = True) -> bool:
    with ctyped.init_com(ctyped.interface.IActiveDesktop) as desktop:
        if desktop:
            if fade:
                _spawn_workerw()
            return ctyped.macro.SUCCEEDED(desktop.SetWallpaper(
                path, 0)) and ctyped.macro.SUCCEEDED(desktop.ApplyChanges(ctyped.const.AD_APPLY_ALL))
    return False


def _set_idesktopwallpaper(path: str, monitor: Optional[str], color: Optional[ctyped.type.COLORREF] = None,
                           style: Optional[Union[int, ctyped.enum.DESKTOP_WALLPAPER_POSITION]] = None) -> bool:
    with ctyped.init_com(ctyped.interface.IDesktopWallpaper) as wallpaper:
        if wallpaper:
            if color is not None and ctyped.macro.FAILED(wallpaper.SetBackgroundColor(color)):
                return False
            if style is not None:
                try:
                    if ctyped.macro.FAILED(wallpaper.SetPosition(style)):
                        return False
                except OSError as e:
                    if e.winerror == ctyped.macro.HRESULT_FROM_WIN32(ctyped.const.ERROR_INVALID_PARAMETER):
                        return False
                    else:
                        raise e
            if style in (Style.SPAN, Style.TILE):
                return _set_param(path)
            else:
                try:
                    return ctyped.macro.SUCCEEDED(wallpaper.SetWallpaper(monitor, path))
                except OSError as e:
                    if e.winerror == ctyped.macro.HRESULT_FROM_WIN32(ctyped.const.ERROR_INVALID_PARAMETER):
                        return False
                    else:
                        raise e
    return False


# noinspection PyShadowingBuiltins
def set(path: str, *monitors: str, fade: bool = True):
    return _set_idesktopwallpaper(path, *monitors) if monitors else _set_iactivedesktop(
        path, fade) if fade else _set_param(path)


_temp_lock = functools.lru_cache(lambda _: threading.Lock())


def set_ex(path: str, monitor: Optional[str] = None, style: int = Style.FILL,
           r: int = 0, g: int = 0, b: int = 0, transition: int = Transition.FADE, duration: int = 1) -> bool:
    if image := _gdiplus.Bitmap.from_file(path):
        width = image.get_width()
        height = image.get_height()
        if style in (Style.TILE, Style.SPAN):
            monitor = 'DISPLAY'
            monitor_x_y_w_h = 0, 0, ctyped.lib.User32.GetSystemMetrics(
                ctyped.const.SM_CXVIRTUALSCREEN), ctyped.lib.User32.GetSystemMetrics(
                ctyped.const.SM_CYVIRTUALSCREEN)
            if style == Style.TILE:
                width_ = monitor_x_y_w_h[2]
                height_ = monitor_x_y_w_h[3]
                bitmap = _gdiplus.Bitmap.from_dimension(width_, height_)
                graphics = bitmap.get_graphics()
                image.set_resolution(graphics.get_dpi_x(), graphics.get_dpi_y())
                for x in range(0, width_, width):
                    for y in range(0, height_, height):
                        graphics.draw_image(image, x, y)
                image = bitmap
                width = width_
                height = height_
        else:
            monitor_x_y_w_h = _get_monitor_x_y_w_h(monitor)
        os.makedirs(TEMP_DIR, exist_ok=True)
        temp_path = os.path.join(TEMP_DIR, _TEMP_FILE).format(_utils.sanitize_filename(monitor))
        with _temp_lock(temp_path):
            # noinspection PyTypeChecker
            _draw_on_workerw(image, *monitor_x_y_w_h, *_get_src_x_y_w_h(*monitor_x_y_w_h[2:], width, height, style),
                             temp_path, _gdiplus.Color.from_rgba(r, g, b), transition, duration)
            try:
                return _set_idesktopwallpaper(
                    temp_path, monitor, style=style if style in (Style.TILE, Style.SPAN) else Style.FILL)
            finally:
                threading.Timer(_DELETE_AFTER, ctyped.lib.Kernel32.DeleteFileW, (temp_path,)).start()
    return False


Wallpaper = collections.namedtuple('Wallpaper', ('path', 'monitor', 'style', 'r', 'g', 'b', 'transition', 'duration'),
                                   defaults=(Style.FILL, 0, 0, 0, Transition.FADE, 1))


def set_multi(*wallpapers: Wallpaper):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = tuple(executor.submit(set_ex, *wallpaper) for wallpaper in wallpapers)
    return all(future.result() for future in futures)


def set_lock(path: str) -> bool:
    with ctyped.get_winrt(ctyped.interface.Windows.Storage.IStorageFileStatics) as file_statics:
        if file_statics:
            with ctyped.Async(ctyped.interface.Windows.Foundation.IAsyncOperation[ctyped.interface.Windows.Storage.IStorageFile]) as operation:
                if ctyped.macro.SUCCEEDED(file_statics.GetFileFromPathAsync(
                        ctyped.handle.HSTRING.from_string(path), operation.get_ref())) and (file := operation.get()):
                    with ctyped.get_winrt(ctyped.interface.Windows.System.UserProfile.ILockScreenStatics) as lock:
                        if lock:
                            with ctyped.Async() as action:
                                if ctyped.macro.SUCCEEDED(lock.SetImageFileAsync(file, action.get_ref())):
                                    return ctyped.enum.Windows.Foundation.AsyncStatus.Completed == action.wait_for()
    return False


def set_slideshow(*paths: str) -> bool:
    with _utils.get_itemidlist(*paths) as pidl, ctyped.init_com(ctyped.interface.IDesktopWallpaper) as wallpaper:
        if wallpaper:
            with ctyped.init_com(ctyped.interface.IShellItemArray, False) as shl_arr:
                id_arr = ctyped.array(*pidl)
                return ctyped.macro.SUCCEEDED(
                    ctyped.lib.Shell32.SHCreateShellItemArrayFromIDLists(len(id_arr), ctyped.byref(
                        id_arr[0]), ctyped.byref(shl_arr))) and ctyped.macro.SUCCEEDED(wallpaper.SetSlideshow(shl_arr))
    return False


@contextlib.contextmanager
def _get_input_stream(file: ctyped.interface.Windows.Storage.IStorageFile) -> \
        ContextManager[Optional[ctyped.interface.Windows.Storage.Streams.IInputStream]]:
    with ctyped.Async(ctyped.interface.Windows.Foundation.IAsyncOperation[ctyped.interface.Windows.Storage.Streams.IRandomAccessStream]) as operation:
        if ctyped.macro.SUCCEEDED(file.OpenAsync(ctyped.enum.Windows.Storage.FileAccessMode.Read, operation.get_ref())) and (stream := operation.get()):
            with ctyped.init_com(ctyped.interface.Windows.Storage.Streams.IInputStream, False) as input_stream:
                if ctyped.macro.SUCCEEDED(stream.GetInputStreamAt(0, ctyped.byref(input_stream))):
                    yield input_stream
                    return
    yield


@contextlib.contextmanager
def _get_output_stream(file: ctyped.interface.Windows.Storage.IStorageFile) -> \
        ContextManager[Optional[ctyped.interface.Windows.Storage.Streams.IOutputStream]]:
    with ctyped.Async(ctyped.interface.Windows.Foundation.IAsyncOperation[ctyped.interface.Windows.Storage.Streams.IRandomAccessStream]) as operation:
        if ctyped.macro.SUCCEEDED(file.OpenAsync(ctyped.enum.Windows.Storage.FileAccessMode.ReadWrite, operation.get_ref())) and (stream := operation.get()):
            with ctyped.init_com(ctyped.interface.Windows.Storage.Streams.IOutputStream, False) as output_stream:
                if ctyped.macro.SUCCEEDED(stream.GetOutputStreamAt(0, ctyped.byref(output_stream))):
                    yield output_stream
                    return
    yield


@contextlib.contextmanager
def _get_wallpaper_lock_input_stream() -> \
        ContextManager[Optional[ctyped.interface.Windows.Storage.Streams.IInputStream]]:
    with ctyped.get_winrt(ctyped.interface.Windows.System.UserProfile.ILockScreenStatics) as lock_statics:
        if lock_statics:
            with ctyped.init_com(ctyped.interface.Windows.Storage.Streams.IRandomAccessStream, False) as stream:
                if ctyped.macro.SUCCEEDED(lock_statics.GetImageStream(ctyped.byref(stream))):
                    with ctyped.init_com(
                            ctyped.interface.Windows.Storage.Streams.IInputStream, False) as input_stream:
                        if ctyped.macro.SUCCEEDED(stream.GetInputStreamAt(0, ctyped.byref(input_stream))):
                            yield input_stream
                            return
    yield


def _copy_stream(input_stream: ctyped.interface.Windows.Storage.Streams.IInputStream,
                 output_stream: ctyped.interface.Windows.Storage.Streams.IOutputStream,
                 progress_callback: Optional[Callable[[int, ...], Any]],
                 args: Optional[Iterable], kwargs: Optional[Mapping[str, Any]]) -> bool:
    with ctyped.get_winrt(ctyped.interface.Windows.Storage.Streams.IRandomAccessStreamStatics) as stream_statics:
        if stream_statics:
            with ctyped.Async(ctyped.interface.Windows.Foundation.IAsyncOperationWithProgress[ctyped.type.UINT64, ctyped.type.UINT64]) as operation:
                if ctyped.macro.SUCCEEDED(stream_statics.CopyAndCloseAsync(
                        input_stream, output_stream, operation.get_ref())):
                    if progress_callback is not None:
                        operation.put_progress(progress_callback, args, kwargs)
                    return ctyped.enum.Windows.Foundation.AsyncStatus.Completed == operation.wait_for()
    return False


def save_lock(path: str, progress_callback: Optional[Callable[[int, ...], Any]] = None,
              args: Optional[Iterable] = None, kwargs: Optional[Mapping[str, Any]] = None) -> bool:
    with _get_wallpaper_lock_input_stream() as input_stream:
        if input_stream:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            open(path, 'w').close()
            with _utils.open_file(path) as file:
                if file:
                    with _get_output_stream(file) as output_stream:
                        return output_stream and _copy_stream(
                            input_stream, output_stream, progress_callback, args, kwargs)
    return False


def remove_from_history(*paths: str) -> bool:
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
