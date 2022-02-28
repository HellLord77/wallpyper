import concurrent.futures
import contextlib
import os
import random
import sys
import threading
import time
from typing import Union, Optional, Any, Iterable, Callable, Mapping, ContextManager

import libs.ctyped as ctyped
from . import gdiplus

_RETRY = 5
_LOCK = threading.Lock()


class _Enum(type):
    def __new__(mcs, *args, **kwargs):
        self = super().__new__(mcs, *args, **kwargs)
        self._vars = {var: val for var, val in vars(self).items() if not var.startswith('_')}
        return self

    def __contains__(cls, item):
        return item in cls._vars

    def __iter__(self):
        return iter(self._vars)

    def __getitem__(self, var_or_val: Union[int, str]) -> Union[int, str]:
        if isinstance(var_or_val, int):
            for var, val_ in self._vars.items():
                if var_or_val == val_:
                    return var
            raise IndexError
        else:
            return self._vars[var_or_val]

    def _random(self, *ignore: int):
        vals = tuple(self._vars.values())
        while (rand := random.choice(vals)) in ignore:
            pass
        return rand


class Style(metaclass=_Enum):
    DEFAULT = -1
    FILL = ctyped.const.WPSTYLE_CROPTOFIT
    FIT = ctyped.const.WPSTYLE_KEEPASPECT
    STRETCH = ctyped.const.WPSTYLE_STRETCH
    TILE = ctyped.const.WPSTYLE_TILE
    CENTER = ctyped.const.WPSTYLE_CENTER
    SPAN = ctyped.const.WPSTYLE_SPAN


class Transition(metaclass=_Enum):
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
        ctyped.func.gdi32.BitBlt(tmp_dst, 0, 0, dst_w, dst_h, dst_bk, 0, 0, ctyped.const.SRCCOPY)
        ctyped.func.msimg32.AlphaBlend(tmp_dst, 0, 0, dst_w, dst_h, src, 0, 0, dst_w, dst_h, blend)
        ctyped.func.gdi32.BitBlt(dst, dst_x, dst_y, dst_w, dst_h, tmp_dst, 0, 0, ctyped.const.SRCCOPY)
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
    def _slide_vertical(factor: float, dst_w: int, dst_h: int, half_dst_w: float):
        dst_w_ = int(half_dst_w * factor)
        half_dst_w_ = int(half_dst_w)
        yield half_dst_w_ - dst_w_, 0, dst_w_, dst_h, 0, 0
        yield half_dst_w_, 0, dst_w_, dst_h, dst_w - dst_w_, 0

    @staticmethod
    def _horizontal(factor: float, dst_w: int, dst_h: int, half_dst_h: float):
        dst_h_ = int(half_dst_h * (1 - factor))
        yield 0, dst_h_, dst_w, dst_h - dst_h_ * 2, 0, dst_h_

    @staticmethod
    def _slide_horizontal(factor: float, dst_w: int, dst_h: int, half_dst_h: float):
        dst_h_ = int(half_dst_h * factor)
        half_dst_h_ = int(half_dst_h)
        yield 0, half_dst_h_ - dst_h_, dst_w, dst_h_, 0, 0
        yield 0, half_dst_h_, dst_w, dst_h_, 0, dst_h - dst_h_

    @staticmethod
    def _reverse_vertical(factor: float, dst_w: int, dst_h: int, half_dst_w: float):
        dst_w_ = int(half_dst_w * factor)
        yield 0, 0, dst_w_, dst_h, 0, 0
        yield dst_w - dst_w_, 0, dst_w_, dst_h, dst_w - dst_w_, 0

    @staticmethod
    def _slide_reverse_vertical(factor: float, dst_w: int, dst_h: int, half_dst_w: float):
        dst_w_ = int(half_dst_w * factor)
        half_dst_w_ = int(half_dst_w)
        yield 0, 0, dst_w_, dst_h, half_dst_w_ - dst_w_, 0
        yield dst_w - dst_w_, 0, dst_w_, dst_h, half_dst_w_, 0

    @staticmethod
    def _reverse_horizontal(factor: float, dst_w: int, dst_h: int, half_dst_h: float):
        dst_h_ = int(half_dst_h * factor)
        yield 0, 0, dst_w, dst_h_, 0, 0
        yield 0, dst_h - dst_h_, dst_w, dst_h_, 0, dst_h - dst_h_

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


def get_style() -> Optional[int]:
    with ctyped.init_com(ctyped.com.IActiveDesktop) as desktop:
        if desktop:
            opt = ctyped.struct.WALLPAPEROPT(ctyped.sizeof(ctyped.struct.WALLPAPEROPT))
            if ctyped.macro.SUCCEEDED(desktop.GetWallpaperOptions(ctyped.byref(opt), 0)):
                return opt.dwStyle
    return None


def _get_monitor_x_y_w_h(dev_path: str) -> tuple[int, int, int, int]:
    rect = ctyped.struct.RECT()
    with ctyped.init_com(ctyped.com.IDesktopWallpaper) as wallpaper:
        if wallpaper:
            if ctyped.macro.SUCCEEDED(wallpaper.GetMonitorRECT(dev_path, ctyped.byref(rect))):
                return rect.left - ctyped.func.user32.GetSystemMetrics(
                    ctyped.const.SM_XVIRTUALSCREEN), rect.top - ctyped.func.user32.GetSystemMetrics(
                    ctyped.const.SM_YVIRTUALSCREEN), rect.right - rect.left, rect.bottom - rect.top
    return 0, 0, 0, 0


def _spawn_workerw():
    ctyped.func.user32.SendMessageW(ctyped.func.user32.FindWindowW('Progman', 'Program Manager'), 0x52C, 0, 0)


@ctyped.type.WNDENUMPROC
def _get_workerw_hwnd_callback(hwnd: ctyped.type.HWND, lparam: ctyped.type.LPARAM):
    if ctyped.func.user32.FindWindowExW(hwnd, None, 'SHELLDLL_DefView', None) is not None:
        if (hwnd_ := ctyped.func.user32.FindWindowExW(None, hwnd, 'WorkerW', None)) is not None:
            ctyped.type.LPARAM.from_address(lparam).value = hwnd_
    return True


def _get_workerw_hwnd() -> Optional[int]:
    hwnd = ctyped.type.LPARAM()
    for _ in range(_RETRY):
        _spawn_workerw()
        ctyped.func.user32.EnumWindows(_get_workerw_hwnd_callback, ctyped.addressof(hwnd))
        if hwnd.value:
            break
    else:
        return None
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


def _get_position(w: int, h: int, src_w: int, src_h: int,
                  pos: int = Style.FILL) -> tuple[int, int, int, int]:
    if pos == Style.CENTER:
        dw = src_w - w
        dh = src_h - h
        return int(dw / 2), int(dh / 2), src_w - dw, src_h - dh
    elif pos in (Style.TILE, Style.STRETCH):
        return 0, 0, src_w, src_h
    elif pos == Style.FIT:
        return _fit_by(src_w, src_h, w, h, w / src_w > h / src_h)
    elif pos == Style.FILL:
        return _fit_by(src_w, src_h, w, h, w / src_w < h / src_h, 3)
    elif pos == Style.SPAN:
        return _fit_by(src_w, src_h, w, h, w / src_w < h / src_h)
    return 0, 0, 0, 0


def _get_temp_hdc(width: int, height: int, color: ctyped.type.ARGB, src: gdiplus.Bitmap,
                  src_x: int, src_y: int, src_w: int, src_h: int) -> ctyped.handle.HDC:
    bitmap = gdiplus.Bitmap.from_dimension(width, height)
    graphics = bitmap.get_graphics()
    graphics.fill_rect_with_color(color, 0, 0, width, height)
    graphics.set_scale(width / src_w, height / src_h)
    with _LOCK:
        src.set_resolution(graphics.dpi_x, graphics.dpi_y)
        graphics.draw_image_from_rect(src, -min(0, src_x), -min(0, src_y), max(0, src_x), max(0, src_y))
    return bitmap.get_hbitmap().get_hdc()


def _draw_on_workerw(image: gdiplus.Bitmap, dst_x: int, dst_y: int, dst_w: int, dst_h: int,
                     src_x: int, src_y: int, src_w: int, src_h: int, color: ctyped.type.ARGB = 0,
                     transition: int = Transition.DISABLED, duration: float = 0, max_steps: int = sys.maxsize) -> bool:
    if hwnd := _get_workerw_hwnd():
        dst = ctyped.handle.HDC.from_hwnd(hwnd)
        src = _get_temp_hdc(dst_w, dst_h, color, image, src_x, src_y, src_w, src_h)
        if transition != Transition.DISABLED:
            if transition == Transition.RANDOM:
                # noinspection PyProtectedMember
                transition = Transition._random(Transition.DISABLED, Transition.RANDOM)
            args = []
            if transition == Transition.FADE:
                dst_bk = ctyped.handle.HBITMAP.from_dimension(dst_w, dst_h).get_hdc()
                ctyped.func.gdi32.BitBlt(dst_bk, 0, 0, dst_w, dst_h, dst, dst_x, dst_y, ctyped.const.SRCPAINT)
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
                    ctyped.func.gdi32.BitBlt(dst, dst_x + dst_ox, dst_y + dst_oy, dst_w_, dst_h_,
                                             src, src_ox, src_oy, ctyped.const.SRCCOPY)
                time.sleep(duration / max_steps)
        return bool(ctyped.func.gdi32.BitBlt(dst, dst_x, dst_y, dst_w, dst_h, src, 0, 0, ctyped.const.SRCCOPY))
    return False


def _get_dpi(x: int, y: int) -> tuple[int, int]:
    dpi_x = ctyped.type.UINT()
    dpi_y = ctyped.type.UINT()
    ctyped.func.shcore.GetDpiForMonitor(ctyped.func.user32.MonitorFromPoint(
        ctyped.struct.POINT(x, y), ctyped.const.MONITOR_DEFAULTTOPRIMARY),
        ctyped.enum.MONITOR_DPI_TYPE.MDT_DEFAULT, ctyped.byref(dpi_x), ctyped.byref(dpi_y))
    return dpi_x.value, dpi_y.value


def _get_argb(r: ctyped.type.BYTE, g: ctyped.type.BYTE, b: ctyped.type.BYTE,
              a: ctyped.type.BYTE = 255) -> ctyped.type.ARGB:
    return (b << ctyped.const.BlueShift | g << ctyped.const.GreenShift |
            r << ctyped.const.RedShift | a << ctyped.const.AlphaShift)


def _set_param(path: str) -> bool:
    return bool(ctyped.func.user32.SystemParametersInfoW(ctyped.const.SPI_SETDESKWALLPAPER, 0, path,
                                                         ctyped.const.SPIF_SENDWININICHANGE))


def _set_iactivedesktop(path: str, fade: bool = True) -> bool:
    with ctyped.init_com(ctyped.com.IActiveDesktop) as desktop:
        if desktop:
            if fade:
                _spawn_workerw()
            return ctyped.macro.SUCCEEDED(desktop.SetWallpaper(
                path, 0)) and ctyped.macro.SUCCEEDED(desktop.ApplyChanges(ctyped.const.AD_APPLY_ALL))
    return False


def _set_idesktopwallpaper(path: str, monitor: str, color: Optional[ctyped.type.COLORREF] = None,
                           style: Optional[ctyped.enum.DESKTOP_WALLPAPER_POSITION] = None) -> bool:
    with ctyped.init_com(ctyped.com.IDesktopWallpaper) as wallpaper:
        if wallpaper:
            if color is not None:
                wallpaper.SetBackgroundColor(color)
            if style is not None:
                wallpaper.SetPosition(style)
            if style in (ctyped.const.WPSTYLE_SPAN, ctyped.const.WPSTYLE_TILE):
                return _set_param(path)
            else:
                return ctyped.macro.SUCCEEDED(wallpaper.SetWallpaper(monitor, path))
    return False


# noinspection PyShadowingBuiltins
def set(path: str, *monitors: str, style: int = Style.DEFAULT, r: int = 0,
        g: int = 0, b: int = 0, transition: int = Transition.FADE, duration: int = 1) -> bool:
    try:
        image = gdiplus.Bitmap.from_file(path)
    except gdiplus.GdiplusError:
        return False
    else:
        if style == Style.DEFAULT:
            style = get_style()
        if style is not None:
            if style in (Style.TILE, Style.SPAN):
                monitors_x_y_w_h = (0, 0, ctyped.func.user32.GetSystemMetrics(
                    ctyped.const.SM_CXVIRTUALSCREEN), ctyped.func.user32.GetSystemMetrics(
                    ctyped.const.SM_CYVIRTUALSCREEN)),
                if style == Style.TILE:
                    bitmap = gdiplus.Bitmap.from_dimension(*monitors_x_y_w_h[0][2:])
                    graphics = bitmap.get_graphics()
                    image.set_resolution(graphics.dpi_x, graphics.dpi_y)
                    for x in range(0, bitmap.width, image.width):
                        for y in range(0, bitmap.height, image.height):
                            graphics.draw_image(image, x, y)
                    image = bitmap
            else:
                monitors_x_y_w_h = tuple(_get_monitor_x_y_w_h(monitor) for monitor in monitors)
            with concurrent.futures.ThreadPoolExecutor() as executor:
                for monitor_x_y_w_h in monitors_x_y_w_h:
                    executor.submit(_draw_on_workerw, image, *monitor_x_y_w_h,
                                    *_get_position(*monitor_x_y_w_h[2:], image.width, image.height, style),
                                    _get_argb(r, g, b), transition, duration)
        set_ = True
        for monitor in monitors:
            set_ = _set_idesktopwallpaper(path, monitor, ctyped.macro.RGB(r, g, b), style) and set_
        return set_


def set_lock(path: str) -> bool:
    with ctyped.get_winrt(ctyped.com.IStorageFileStatics) as file_statics:
        if file_statics:
            operation = ctyped.Async(ctyped.com.IAsyncOperation)
            if ctyped.macro.SUCCEEDED(file_statics.GetFileFromPathAsync(
                    ctyped.handle.HSTRING.from_string(path), operation.get_ref())) and (
                    file := operation.get(ctyped.com.IStorageFile)):
                with ctyped.get_winrt(ctyped.com.ILockScreenStatics) as lock:
                    if lock:
                        action = ctyped.Async()
                        if ctyped.macro.SUCCEEDED(lock.SetImageFileAsync(file, action.get_ref())):
                            return ctyped.enum.AsyncStatus.Completed == action.wait_for()
    return False


@contextlib.contextmanager
def _get_input_stream(file: ctyped.com.IStorageFile) -> ContextManager[Optional[ctyped.com.IInputStream]]:
    operation = ctyped.Async(ctyped.com.IAsyncOperation)
    if ctyped.macro.SUCCEEDED(file.OpenAsync(ctyped.enum.FileAccessMode.Read, operation.get_ref())) and (
            stream := operation.get(ctyped.com.IRandomAccessStream)):
        with ctyped.init_com(ctyped.com.IInputStream, False) as input_stream:
            if ctyped.macro.SUCCEEDED(stream.GetInputStreamAt(0, ctyped.byref(input_stream))):
                yield input_stream
                return
    yield None


@contextlib.contextmanager
def _get_output_stream(file: ctyped.com.IStorageFile) -> ContextManager[Optional[ctyped.com.IOutputStream]]:
    operation = ctyped.Async(ctyped.com.IAsyncOperation)
    if ctyped.macro.SUCCEEDED(file.OpenAsync(ctyped.enum.FileAccessMode.ReadWrite, operation.get_ref())) and (
            stream := operation.get(ctyped.com.IRandomAccessStream)):
        with ctyped.init_com(ctyped.com.IOutputStream, False) as output_stream:
            if ctyped.macro.SUCCEEDED(stream.GetOutputStreamAt(0, ctyped.byref(output_stream))):
                yield output_stream
                return
    yield None


@contextlib.contextmanager
def _open_file(path: str) -> ContextManager[Optional[ctyped.com.IStorageFile]]:
    with ctyped.get_winrt(ctyped.com.IStorageFileStatics) as file_statics:
        if file_statics:
            operation = ctyped.Async(ctyped.com.IAsyncOperation)
            if ctyped.macro.SUCCEEDED(file_statics.GetFileFromPathAsync(
                    ctyped.handle.HSTRING.from_string(path), operation.get_ref())) and (
                    file := operation.get(ctyped.com.IStorageFile)):
                yield file
                return
    yield None


@contextlib.contextmanager
def _get_wallpaper_lock_input_stream() -> ContextManager[Optional[ctyped.com.IInputStream]]:
    with ctyped.get_winrt(ctyped.com.ILockScreenStatics) as lock_statics:
        if lock_statics:
            with ctyped.init_com(ctyped.com.IRandomAccessStream, False) as stream:
                if ctyped.macro.SUCCEEDED(lock_statics.GetImageStream(ctyped.byref(stream))):
                    with ctyped.init_com(ctyped.com.IInputStream, False) as input_stream:
                        if ctyped.macro.SUCCEEDED(stream.GetInputStreamAt(0, ctyped.byref(input_stream))):
                            yield input_stream
                            return
    yield None


def _copy_stream(input_stream: ctyped.com.IInputStream, output_stream: ctyped.com.IOutputStream,
                 progress_callback: Optional[Callable[[int, ...], Any]],
                 args: Optional[Iterable], kwargs: Optional[Mapping[str, Any]]) -> bool:
    with ctyped.get_winrt(ctyped.com.IRandomAccessStreamStatics) as stream_statics:
        if stream_statics:
            operation = ctyped.Async(ctyped.com.IAsyncOperationWithProgress)
            if ctyped.macro.SUCCEEDED(stream_statics.CopyAndCloseAsync(input_stream, output_stream,
                                                                       operation.get_ref())):
                if progress_callback is not None:
                    operation.put_progress(ctyped.type.UINT64, progress_callback, args, kwargs)
                return ctyped.enum.AsyncStatus.Completed == operation.wait_for()
    return False


def save_lock(path: str, progress_callback: Optional[Callable[[int, ...], Any]] = None,
              args: Optional[Iterable] = None, kwargs: Optional[Mapping[str, Any]] = None) -> bool:
    with _get_wallpaper_lock_input_stream() as input_stream:
        if input_stream:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            open(path, 'w').close()
            with _open_file(path) as file, _get_output_stream(file) as output_stream:
                return output_stream and _copy_stream(input_stream, output_stream, progress_callback, args, kwargs)
    return False
