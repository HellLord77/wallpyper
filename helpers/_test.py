__version__ = '0.0.1'

import contextlib
import time
from typing import Any, Callable, ContextManager, Generator, Iterable, Mapping, Optional, Union

import libs.ctyped as ctyped
import platforms.win32 as win32

NAME = f'{__name__}-{__version__}'
EVENT_CLOSE = ctyped.const.WM_CLOSE


class _HICON(ctyped.type.HICON):
    def __del__(self):
        ctyped.func.user32.DestroyIcon(self)


@contextlib.contextmanager
def _alloc(size: int) -> ContextManager[int]:
    pointer = ctyped.func.msvcrt.malloc(size)
    try:
        yield pointer
    finally:
        ctyped.func.msvcrt.free(pointer)


@contextlib.contextmanager
def _open_bitmap(path: str) -> ContextManager[ctyped.type.GpBitmap]:
    bitmap = ctyped.type.GpBitmap()
    token = ctyped.type.ULONG_PTR()
    if not ctyped.func.GdiPlus.GdiplusStartup(ctyped.byref(token),
                                              ctyped.byref(ctyped.struct.GdiplusStartupInput()), None):
        ctyped.func.GdiPlus.GdipCreateBitmapFromFile(ctyped.char_array(path), ctyped.byref(bitmap))
    try:
        yield bitmap
    finally:
        ctyped.func.GdiPlus.GdipDisposeImage(bitmap)
        ctyped.func.GdiPlus.GdiplusShutdown(token)


def _get_gif_frames(path: str) -> Generator[tuple[int, _HICON], None, None]:
    frames = []
    with _open_bitmap(path) as bitmap:
        if bitmap:
            size = ctyped.type.UINT()
            ctyped.func.GdiPlus.GdipGetPropertyItemSize(bitmap, ctyped.const.PropertyTagFrameDelay, ctyped.byref(size))
            with _alloc(size.value) as buffer:
                if buffer:
                    properties = ctyped.cast(buffer, ctyped.struct.PropertyItem)
                    ctyped.func.GdiPlus.GdipGetPropertyItem(bitmap,
                                                            ctyped.const.PropertyTagFrameDelay, size, properties)
                    delays = ctyped.cast(properties.contents.value, ctyped.pointer(ctyped.type.UINT))
                    guid = ctyped.struct.GUID()
                    count = ctyped.type.UINT()
                    ctyped.func.GdiPlus.GdipImageGetFrameDimensionsList(bitmap, ctyped.byref(guid), 1)
                    ctyped.func.GdiPlus.GdipImageGetFrameCount(bitmap, ctyped.byref(guid), ctyped.byref(count))
                    for index in range(count.value):
                        hicon = _HICON()
                        ctyped.func.GdiPlus.GdipImageSelectActiveFrame(bitmap, ctyped.byref(guid), index)
                        ctyped.func.GdiPlus.GdipCreateHICONFromBitmap(bitmap, ctyped.byref(hicon))
                        if hicon:
                            # noinspection PyTypeChecker
                            frames.append((delays[index] * 10, hicon))
    while True:
        for frame in frames:
            yield frame


class Event:
    MOVE = ctyped.const.WM_MOUSEMOVE
    LEFT_DOWN = ctyped.const.WM_LBUTTONDOWN
    LEFT_UP = ctyped.const.WM_LBUTTONUP
    LEFT_DOUBLE = ctyped.const.WM_LBUTTONDBLCLK
    RIGHT_DOWN = ctyped.const.WM_RBUTTONDOWN
    RIGHT_UP = ctyped.const.WM_RBUTTONUP
    RIGHT_DOUBLE = ctyped.const.WM_RBUTTONDBLCLK
    MIDDLE_DOWN = ctyped.const.WM_MBUTTONDOWN
    MIDDLE_UP = ctyped.const.WM_MBUTTONUP
    MIDDLE_DOUBLE = ctyped.const.WM_MBUTTONDBLCLK
    BALLOON_QUEUED = ctyped.const.NIN_BALLOONSHOW
    BALLOON_HIDDEN = ctyped.const.NIN_BALLOONTIMEOUT
    BALLOON_CLICK = ctyped.const.NIN_BALLOONUSERCLICK  # FIXME triggers when click tray icon while showing balloon


class Icon:
    NONE = ctyped.const.NIIF_NONE
    INFO = ctyped.const.NIIF_INFO
    WARNING = ctyped.const.NIIF_WARNING
    ERROR = ctyped.const.NIIF_ERROR
    USER = ctyped.const.NIIF_USER


class SysTray:
    _binds: dict[int, dict[int, tuple[Callable, tuple, dict]]] = {0: {}}
    _class = None
    _flags = ctyped.const.NIF_MESSAGE | ctyped.const.NIF_ICON | ctyped.const.NIF_TIP
    _frames_and_on_timer = None
    _hicon = None
    _hwnd = None
    _shown = False
    _uid = ctyped.type.UINT()

    def __new__(cls, *_, **__):
        if not cls._hwnd:
            cls._class = ctyped.struct.WNDCLASSEXW(ctyped.sizeof(ctyped.struct.WNDCLASSEXW),
                                                   lpfnWndProc=ctyped.type.WNDPROC(cls._callback),
                                                   hInstance=ctyped.func.kernel32.GetModuleHandleW(None),
                                                   lpszClassName=NAME)
            ctyped.func.user32.RegisterClassExW(ctyped.byref(cls._class))
            cls._hwnd = ctyped.func.user32.CreateWindowExW(0, cls._class.lpszClassName, None, 0, 0, 0, 0, 0,
                                                           ctyped.const.HWND_MESSAGE, None, None, None)
        cls._uid += 1
        return super().__new__(cls)

    def __init__(self, icon: Optional[Union[str, int]] = None, tooltip: Optional[str] = None):
        self._uid = self._uid.value
        self._data = ctyped.struct.NOTIFYICONDATAW(ctyped.sizeof(ctyped.struct.NOTIFYICONDATAW), self._hwnd, self._uid,
                                                   self._flags, ctyped.const.WM_APP)
        self.set_icon(icon or ctyped.const.IDI_APPLICATION)
        self.set_tooltip(tooltip or '')
        self._binds[self._uid] = {}

    def __del__(self):
        self.hide()
        del self._binds[self._uid]
        if not self._binds:
            ctyped.func.user32.DestroyWindow(self._hwnd)
            ctyped.func.user32.UnregisterClassW(self._class.lpszClassName, ctyped.func.kernel32.GetModuleHandleW(None))
            type(self)._hwnd = 0

    @classmethod
    def _call(cls, uid: int, event: int) -> Any:
        try:
            callback, args, kwargs = cls._binds[uid][event]
        except KeyError:
            print(uid, event)
            return
        else:
            return callback(*args, **kwargs)

    @classmethod
    def _callback(cls, hwnd: ctyped.type.HWND, message: ctyped.type.UINT, wparam: ctyped.type.WPARAM,
                  lparam: ctyped.type.LPARAM) -> ctyped.type.LRESULT:
        if message == ctyped.const.WM_DESTROY:  # FIXME match (3.10)
            ctyped.func.user32.PostQuitMessage(0)
        elif message == ctyped.const.WM_CLOSE:
            try:
                cls._call(0, message)
            finally:
                ctyped.func.user32.DestroyWindow(hwnd)
        elif message == ctyped.const.WM_QUERYENDSESSION:
            ...
        elif message == ctyped.const.WM_APP:
            cls._call(wparam, lparam)
        else:
            return ctyped.func.user32.DefWindowProcW(hwnd, message, wparam, lparam)
        return 0

    @classmethod
    def get_handle(cls) -> int:
        return cls._hwnd

    @classmethod
    def run_at_exit(cls, callback: Callable, args: Optional[Iterable] = None,
                    kwargs: Optional[Mapping[str, Any]] = None):
        cls._binds[0][ctyped.const.WM_CLOSE] = callback, () if args is None else {}, {} if kwargs is None else kwargs

    @classmethod
    def clear_at_exit(cls) -> bool:
        try:
            del cls._binds[0][ctyped.const.WM_CLOSE]
        except KeyError:
            return False
        else:
            return True

    @classmethod
    def mainloop(cls) -> int:
        msg = ctyped.struct.MSG()
        msg_ref = ctyped.byref(msg)
        while ctyped.func.user32.GetMessageW(msg_ref, cls._hwnd, 0, 0) > 0:
            ctyped.func.user32.TranslateMessage(msg_ref)
            ctyped.func.user32.DispatchMessageW(msg_ref)
        return msg.wParam

    @classmethod
    def exit_mainloop(cls) -> bool:
        return not bool(ctyped.func.user32.SendMessageW(cls._hwnd, ctyped.const.WM_CLOSE, 0, 0))

    def is_shown(self) -> bool:
        return self._shown

    def _set_hicon(self, hicon: ctyped.type.HICON) -> bool:
        self._data.hIcon = hicon
        return self._update()

    def set_icon(self, path_or_res: Union[str, int]) -> bool:
        self.stop_animation()
        hicon = ctyped.type.HICON()
        if isinstance(path_or_res, str):
            with _open_bitmap(path_or_res) as bitmap:
                ctyped.func.GdiPlus.GdipCreateHICONFromBitmap(bitmap, ctyped.byref(hicon))
        else:
            hicon = ctyped.func.user32.LoadIconW(None, path_or_res)
        self._hicon = _HICON(hicon.value)
        self._set_hicon(self._hicon)
        return bool(hicon)

    def set_tooltip(self, text: str) -> bool:
        self._data.szTip = text
        return self._update()

    def _next_frame(self, *_):
        frame = next(self._frames_and_on_timer[0])
        self._set_hicon(frame[1])
        ctyped.func.user32.SetTimer(self._hwnd, 0, frame[0], self._frames_and_on_timer[1])

    def set_animation(self, gif_path: str):
        self.stop_animation()
        # noinspection PyTypeChecker
        self._frames_and_on_timer = iter(_get_gif_frames(gif_path)), ctyped.type.TIMERPROC(self._next_frame)
        self._next_frame()

    def stop_animation(self):
        ctyped.func.user32.KillTimer(self._hwnd, 0)
        self._set_hicon(self._hicon)
        self._frames_and_on_timer = None

    def _update(self) -> bool:
        return self._shown and bool(ctyped.func.shell32.Shell_NotifyIconW(ctyped.const.NIM_MODIFY, ctyped.byref(
            self._data)) or ctyped.func.shell32.Shell_NotifyIconW(ctyped.const.NIM_ADD, ctyped.byref(self._data)))

    def show(self) -> bool:
        self._shown = True
        self._shown = self._update()
        return self._shown

    def hide(self) -> bool:
        self._shown = not bool(ctyped.func.shell32.Shell_NotifyIconW(ctyped.const.NIM_DELETE, ctyped.byref(self._data)))
        return not self._shown

    def show_balloon(self, title: str, text: Optional[str] = None, icon: Optional[int] = None,
                     silent: Optional[bool] = None) -> bool:
        hicon = self._data.hIcon
        self._data.uFlags = ctyped.const.NIF_INFO | ctyped.const.NIF_ICON
        self._data.hIcon = self._hicon
        self._data.szInfo = text or title
        self._data.szInfoTitle = title if text else ''
        self._data.dwInfoFlags = (icon or Icon.NONE) | (bool(silent) * ctyped.const.NIIF_NOSOUND)
        shown = self.show()
        self._data.uFlags = self._flags
        self._set_hicon(hicon)
        return shown

    def bind(self, event: int, callback: Callable, args: Optional[Iterable] = None,
             kwargs: Optional[Mapping[str, Any]] = None):
        bind(event, callback, args, kwargs, self._uid)

    def unbind(self, event: int) -> bool:
        return unbind(event, self._uid)


def bind(event: int, callback: Callable, args: Optional[Iterable] = None,
         kwargs: Optional[Mapping[str, Any]] = None, _uid: int = 0):
    # noinspection PyProtectedMember
    SysTray._binds[_uid][event] = callback, () if args is None else {}, {} if kwargs is None else kwargs


def unbind(event: int, _uid: int = 0) -> bool:
    try:
        # noinspection PyProtectedMember
        del SysTray._binds[_uid][event]
    except KeyError:
        return False
    else:
        return True


def _foo():
    s.show_balloon('title')
    print('_foo')
    return 0


def _foo2():
    s.exit_mainloop()  # s.set_icon(r'E:\Projects\wallpyper\icon.ico')  # s.stop_animation()


def _foo3(*evt):
    for e in evt:
        s.bind(e, lambda: None)


@contextlib.contextmanager
def _get_hbitmap_dc(hbitmap: ctyped.type.HBITMAP) -> ContextManager[ctyped.type.HDC]:
    hdc = ctyped.func.gdi32.CreateCompatibleDC(None)
    selected = ctyped.func.gdi32.SelectObject(hdc, hbitmap)
    try:
        yield hdc
    finally:
        ctyped.func.gdi32.SelectObject(hdc, selected)
        ctyped.func.gdi32.DeleteDC(hdc)


class Position:
    CENTER = ctyped.const.DWPOS_CENTER
    TILE = ctyped.const.DWPOS_TILE
    STRETCH = ctyped.const.DWPOS_STRETCH
    FIT = ctyped.const.DWPOS_FIT
    FILL = ctyped.const.DWPOS_FILL
    SPAN = ctyped.const.DWPOS_SPAN


class Transition:
    FADE = 0
    LEFT = 1
    TOP = 2
    RIGHT = 3
    BOTTOM = 4
    TOP_LEFT = 5
    TOP_RIGHT = 6
    BOTTOM_LEFT = 7
    BOTTOM_RIGHT = 8
    VERTICAL = 9
    HORIZONTAL = 10
    EXPLODE = 11
    IMPLODE = 12
    SLIDE_LEFT = 13
    SLIDE_TOP = 14
    SLIDE_RIGHT = 15
    SLIDE_BOTTOM = 16
    SLIDE_TOP_LEFT = 17
    SLIDE_TOP_RIGHT = 18
    SLIDE_BOTTOM_LEFT = 19
    SLIDE_BOTTOM_RIGHT = 20

    @staticmethod
    def _fade(factor, dst_w, dst_h, dst, dst_x, dst_y, src, blend):
        blend.SourceConstantAlpha = int(255 * factor)
        ctyped.func.msimg32.AlphaBlend(dst, dst_x, dst_y, dst_w, dst_h, src, 0, 0, dst_w, dst_h, blend)
        return ()

    @staticmethod
    def _left(factor, dst_w, dst_h):
        yield 0, 0, int(dst_w * factor), dst_h, 0, 0

    @staticmethod
    def _slide_left(factor, dst_w, dst_h):
        dst_w_ = int(dst_w * factor)
        yield 0, 0, dst_w_, dst_h, dst_w - dst_w_, 0

    @staticmethod
    def _top(factor, dst_w, dst_h):
        yield 0, 0, dst_w, int(dst_h * factor), 0, 0

    @staticmethod
    def _slide_top(factor, dst_w, dst_h):
        dst_h_ = int(dst_h * factor)
        yield 0, 0, dst_w, dst_h_, 0, dst_h - dst_h_

    @staticmethod
    def _right(factor, dst_w, dst_h):
        dst_w_ = dst_w - int(dst_w * factor)
        yield dst_w_, 0, dst_w - dst_w_, dst_h, dst_w_, 0

    @staticmethod
    def _slide_right(factor, dst_w, dst_h):
        dst_w_ = dst_w - int(dst_w * factor)
        yield dst_w_, 0, dst_w - dst_w_, dst_h, 0, 0

    @staticmethod
    def _bottom(factor, dst_w, dst_h):
        dst_h_ = dst_h - int(dst_h * factor)
        yield 0, dst_h_, dst_w, dst_h - dst_h_, 0, dst_h_

    @staticmethod
    def _slide_bottom(factor, dst_w, dst_h):
        dst_h_ = dst_h - int(dst_h * factor)
        yield 0, dst_h_, dst_w, dst_h - dst_h_, 0, 0

    @staticmethod
    def _top_left(factor, dst_w, dst_h):
        yield 0, 0, int(dst_w * factor), int(dst_h * factor), 0, 0

    @staticmethod
    def _slide_top_left(factor, dst_w, dst_h):
        dst_w_ = int(dst_w * factor)
        dst_h_ = int(dst_h * factor)
        yield 0, 0, dst_w_, dst_h_, dst_w - dst_w_, dst_h - dst_h_

    @staticmethod
    def _top_right(factor, dst_w, dst_h):
        dst_w_ = dst_w - int(dst_w * factor)
        yield dst_w_, 0, dst_w - dst_w_, int(dst_h * factor), dst_w_, 0

    @staticmethod
    def _slide_top_right(factor, dst_w, dst_h):
        dst_w_ = dst_w - int(dst_w * factor)
        dst_h_ = int(dst_h * factor)
        yield dst_w_, 0, dst_w - dst_w_, dst_h_, 0, dst_h - dst_h_

    @staticmethod
    def _bottom_left(factor, dst_w, dst_h):
        dst_h_ = dst_h - int(dst_h * factor)
        yield 0, dst_h_, int(dst_w * factor), dst_h - dst_h_, 0, dst_h_

    @staticmethod
    def _slide_bottom_left(factor, dst_w, dst_h):
        dst_w_ = int(dst_w * factor)
        dst_h_ = dst_h - int(dst_h * factor)
        yield 0, dst_h_, dst_w_, dst_h - dst_h_, dst_w - dst_w_, 0

    @staticmethod
    def _bottom_right(factor, dst_w, dst_h):
        dst_w_ = dst_w - int(dst_w * factor)
        dst_h_ = dst_h - int(dst_h * factor)
        yield dst_w_, dst_h_, dst_w - dst_w_, dst_h - dst_h_, dst_w_, dst_h_

    @staticmethod
    def _slide_bottom_right(factor, dst_w, dst_h):
        dst_w_ = dst_w - int(dst_w * factor)
        dst_h_ = dst_h - int(dst_h * factor)
        yield dst_w_, dst_h_, dst_w - dst_w_, dst_h - dst_h_, 0, 0

    @staticmethod
    def _vertical(factor, dst_w, dst_h, half_dst_w):
        dst_w_ = int(half_dst_w * (1 - factor))
        yield dst_w_, 0, dst_w - dst_w_ * 2, dst_h, dst_w_, 0

    @staticmethod
    def _horizontal(factor, dst_w, dst_h, half_dst_h):
        dst_h_ = int(half_dst_h * (1 - factor))
        yield 0, dst_h_, dst_w, dst_h - dst_h_ * 2, 0, dst_h_

    @staticmethod
    def _explode(factor, dst_w, dst_h, half_dst_w, half_dst_h):
        dst_w_ = int(half_dst_w * (1 - factor))
        dst_h_ = int(half_dst_h * (1 - factor))
        yield dst_w_, dst_h_, dst_w - dst_w_ * 2, dst_h - dst_h_ * 2, dst_w_, dst_h_

    @staticmethod
    def _implode(factor, dst_w, dst_h):
        half_factor = factor / 2
        dst_w_ = int(dst_w * half_factor)
        dst_h_ = int(dst_h * half_factor)
        dst_dw = dst_w - dst_w_
        dst_dh = dst_h - dst_h_
        yield 0, 0, dst_w_, dst_h, 0, 0
        yield dst_w_, 0, dst_w, dst_h_, dst_w_, 0
        yield dst_dw, dst_h_, dst_w - dst_dw, dst_h, dst_dw, dst_h_
        yield dst_w_, dst_dh, dst_w - dst_h_, dst_h - dst_dh, dst_w_, dst_dh

    _TRANSITIONS = (_fade, _left, _top, _right, _bottom,
                    _top_left, _top_right, _bottom_left, _bottom_right,
                    _vertical, _horizontal, _explode, _implode,
                    _slide_left, _slide_top, _slide_right, _slide_bottom,
                    _slide_top_left, _slide_top_right, _slide_bottom_left, _slide_bottom_right)


def _fit_by(from_w: int, from_h: int, to_w: int, to_h: int,
            by_h: bool = True, d: int = 2) -> tuple[int, int, int, int]:
    ratio = to_w / to_h
    if by_h:
        w = from_h * ratio
        return int((from_w - w) / d), 0, int(w), from_h
    else:
        h = from_w / ratio
        return 0, int((from_h - h) / d), from_w, int(h)


def _get_position(hbitmap_w: int, hbitmap_h: int, monitor_w: int, monitor_h: int,
                  position: int = Position.FILL) -> tuple[int, int, int, int]:
    if position == Position.CENTER:  # FIXME match (py 3.10)
        dw = hbitmap_w - monitor_w
        dh = hbitmap_h - monitor_h
        return int(dw / 2), int(dh / 2), hbitmap_w - dw, hbitmap_h - dh
    elif position == Position.TILE:
        pass
    elif position == Position.STRETCH:
        return 0, 0, hbitmap_w, hbitmap_h
    elif position == Position.FIT:
        return _fit_by(hbitmap_w, hbitmap_h, monitor_w, monitor_h, monitor_w / hbitmap_w > monitor_h / hbitmap_h)
    elif position == Position.FILL:
        return _fit_by(hbitmap_w, hbitmap_h, monitor_w, monitor_h, monitor_w / hbitmap_w < monitor_h / hbitmap_h, 3)
    return 0, 0, 0, 0


def _draw_gp_image(gp_image: ctyped.type.GpImage, dst_x: int, dst_y: int, dst_w: int, dst_h: int,
                   src_x: int, src_y: int, src_w: int, src_h: int, color: ctyped.type.ARGB = 0, steps: int = 1,
                   duration: float = 1, w: Optional[int] = None, h: Optional[int] = None):
    with _create_gp_bitmap(dst_w, dst_h) as tmp_gp_bitmap:
        with _get_gp_graphics(tmp_gp_bitmap) as tmp_gp_graphics:
            with _create_gp_solid_fill(color) as solid_fill:
                ctyped.func.GdiPlus.GdipFillRectangle(tmp_gp_graphics, solid_fill, 0, 0, dst_w, dst_h)
            ctyped.func.GdiPlus.GdipScaleWorldTransform(tmp_gp_graphics, dst_w / src_w, dst_h / src_h,
                                                        ctyped.const.MatrixOrderPrepend)
            ctyped.func.GdiPlus.GdipDrawImagePointRect(
                tmp_gp_graphics, gp_image, -min(0, src_x), -min(0, src_y), max(0, src_x), max(0, src_y),
                _get_gp_image_w(gp_image) if w is None else w, _get_gp_image_h(gp_image) if h is None else h,
                ctyped.const.UnitPixel)
        hbitmap = ctyped.type.HBITMAP()
        ctyped.func.GdiPlus.GdipCreateHBITMAPFromBitmap(tmp_gp_bitmap, ctyped.byref(hbitmap), 0)
    with _get_hbitmap_dc(hbitmap) as src:
        with win32._get_dc(win32._get_workerw_hwnd()) as dst:
            transition = Transition.FADE  # TODO parameterize
            extra = []
            if transition == Transition.FADE:
                extra.extend((dst, dst_x, dst_y, src, ctyped.struct.BLENDFUNCTION()))
            elif transition == Transition.VERTICAL:
                extra.append(dst_w / 2)
            elif transition == Transition.HORIZONTAL:
                extra.append(dst_h / 2)
            elif transition == Transition.EXPLODE:
                extra.extend((dst_w / 2, dst_h / 2))
            for step in range(steps):
                # noinspection PyProtectedMember
                for dst_ox, dst_oy, dst_w_, dst_h_, src_ox, src_oy in Transition._TRANSITIONS[transition].__func__(
                        step / steps, dst_w, dst_h, *extra):
                    ctyped.func.gdi32.BitBlt(dst, dst_x + dst_ox, dst_y + dst_oy, dst_w_, dst_h_,
                                             src, src_ox, src_oy, ctyped.const.SRCCOPY)
                time.sleep(duration / steps)
            ctyped.func.gdi32.BitBlt(dst, dst_x, dst_y, dst_w, dst_h, src, 0, 0, ctyped.const.SRCCOPY)
    ctyped.func.gdi32.DeleteObject(hbitmap)


def _make_argb(a: ctyped.type.BYTE, r: ctyped.type.BYTE, g: ctyped.type.BYTE, b: ctyped.type.BYTE) -> ctyped.type.ARGB:
    return (b << ctyped.const.BlueShift | g << ctyped.const.GreenShift |
            r << ctyped.const.RedShift | a << ctyped.const.AlphaShift)


def _get_color_matrix(alpha: float = 1) -> ctyped.struct.ColorMatrix:
    color_matrix = ctyped.struct.ColorMatrix()
    for index in range(5):
        color_matrix.m[index][index] = 1
    color_matrix.m[3][3] = alpha
    return color_matrix


@contextlib.contextmanager
def _create_gp_image_attributes(color_matrix: Optional[ctyped.struct.ColorMatrix] = None) -> \
        ContextManager[ctyped.type.GpImageAttributes]:
    gp_image_attributes = ctyped.type.GpImageAttributes()
    with win32._init_gdiplus():
        ctyped.func.GdiPlus.GdipCreateImageAttributes(ctyped.byref(gp_image_attributes))
        if color_matrix is not None:
            ctyped.func.GdiPlus.GdipSetImageAttributesColorMatrix(
                gp_image_attributes, ctyped.const.ColorAdjustTypeDefault, True,
                ctyped.byref(color_matrix), None, ctyped.const.ColorMatrixFlagsDefault)
    try:
        yield gp_image_attributes
    finally:
        ctyped.func.GdiPlus.GdipDisposeImageAttributes(gp_image_attributes)


@contextlib.contextmanager
def _create_gp_image(path: str) -> ContextManager[ctyped.type.GpImage]:
    gp_image = ctyped.type.GpImage()
    with win32._init_gdiplus():
        ctyped.func.GdiPlus.GdipLoadImageFromFile(path, ctyped.byref(gp_image))
        try:
            yield gp_image
        finally:
            ctyped.func.GdiPlus.GdipDisposeImage(gp_image)


@contextlib.contextmanager
def _create_gp_bitmap(w: int, h: int, pixel_format: ctyped.type.PixelFormat = ctyped.const.PixelFormat24bppRGB) -> \
        ContextManager[ctyped.type.GpBitmap]:
    gp_bitmap = ctyped.type.GpBitmap()
    with win32._init_gdiplus():
        ctyped.func.GdiPlus.GdipCreateBitmapFromScan0(w, h, 0, pixel_format, None, ctyped.byref(gp_bitmap))
        try:
            yield gp_bitmap
        finally:
            ctyped.func.GdiPlus.GdipDisposeImage(gp_bitmap)


def _get_gp_image_w(gp_image: ctyped.type.GpImage) -> int:
    w = ctyped.type.UINT()
    ctyped.func.GdiPlus.GdipGetImageWidth(gp_image, ctyped.byref(w))
    return w.value


def _get_gp_image_h(gp_image: ctyped.type.GpImage) -> int:
    h = ctyped.type.UINT()
    ctyped.func.GdiPlus.GdipGetImageHeight(gp_image, ctyped.byref(h))
    return h.value


@contextlib.contextmanager
def _get_gp_graphics(gp_image: ctyped.type.GpImage) -> ContextManager[ctyped.type.GpGraphics]:
    gp_graphics = ctyped.type.GpGraphics()
    ctyped.func.GdiPlus.GdipGetImageGraphicsContext(gp_image, ctyped.byref(gp_graphics))
    try:
        yield gp_graphics
    finally:
        ctyped.func.GdiPlus.GdipDeleteGraphics(gp_graphics)


@contextlib.contextmanager
def _create_gp_solid_fill(argb: ctyped.type.ARGB) -> ContextManager[ctyped.type.GpSolidFill]:
    solid_fill = ctyped.type.GpSolidFill()
    with win32._init_gdiplus():
        ctyped.func.GdiPlus.GdipCreateSolidFill(argb, ctyped.byref(solid_fill))
        try:
            yield solid_fill
        finally:
            ctyped.func.GdiPlus.GdipDeleteBrush(solid_fill)


def _fill_empty_rect(hdc, out_x, out_y, out_w, out_h, in_x, in_y, in_w, in_h, argb: ctyped.type.ARGB):
    with win32._get_gp_graphics(hdc) as gp_graphics:
        with _create_gp_solid_fill(argb) as brush:
            if out_x < in_x:
                ctyped.func.GdiPlus.GdipFillRectangleI(gp_graphics, brush, out_x, out_y, in_x - out_x, out_h)
            if out_y < in_y:
                ctyped.func.GdiPlus.GdipFillRectangleI(gp_graphics, brush, out_x, out_y, out_w, in_y - out_y)
            if in_x + in_w < out_x + out_w:
                ctyped.func.GdiPlus.GdipFillRectangleI(gp_graphics, brush, in_x + in_w, out_y,
                                                       out_x + out_w - (in_x + in_w), out_h)
            if in_y + in_h < out_y + out_h:
                ctyped.func.GdiPlus.GdipFillRectangleI(gp_graphics, brush, out_x, in_y + in_h,
                                                       out_w, out_y + out_h - (in_y + in_h))


def _draw_on_graphics(gp_graphics: ctyped.type.GpGraphics, gp_image: ctyped.type.GpImage,
                      dst_w: float, dst_h: float, dst_x: float = 0, dst_y: float = 0, src_w: Optional[float] = None,
                      src_h: Optional[float] = None, src_x: float = 0, src_y: float = 0, alpha: float = 1):
    with _create_gp_image_attributes(_get_color_matrix(alpha)) as gp_attrs:
        draw_image_abort = ctyped.type.DrawImageAbort()
        ctyped.func.GdiPlus.GdipDrawImageRectRect(gp_graphics, gp_image, dst_x, dst_y, dst_w, dst_h, src_x, src_y,
                                                  _get_gp_image_w(gp_image) if src_w is None else src_w,
                                                  _get_gp_image_h(gp_image) if src_h is None else src_h,
                                                  ctyped.const.UnitPixel, gp_attrs, draw_image_abort, None)


def test():
    path = r'C:\Users\ratul\AppData\Local\Temp\Wallpyper\wallhaven-m9r7r1.jpg'
    monitor = win32.get_monitor_ids()[1]
    method = Position.FIT
    r = 0x00
    g = 0x00
    b = 0x00
    steps = 100
    duration = 1

    with _create_gp_image(path) as gp_image:
        if gp_image:
            monitor_x_y_w_h = win32._get_monitor_x_y_w_h(monitor)
            if method == Position.TILE or method == Position.SPAN:
                monitor_x_y_w_h = 0, 0, ctyped.func.user32.GetSystemMetrics(
                    ctyped.const.SM_CXVIRTUALSCREEN), ctyped.func.user32.GetSystemMetrics(
                    ctyped.const.SM_CYVIRTUALSCREEN)
                if method == Position.TILE:
                    pass  # FIXME monitor_x_y_w_h = SystemMetrics + (0000/0000)
                else:
                    method = Position.FILL
            w = _get_gp_image_w(gp_image)
            h = _get_gp_image_h(gp_image)
            _draw_gp_image(gp_image, *monitor_x_y_w_h, *_get_position(
                w, h, *monitor_x_y_w_h[2:], method), _make_argb(255, r, g, b), steps, duration, w, h)
    # win32._set_wallpaper_idesktopwallpaper(path, monitor, color=ctyped.macro.RGB(r, g, b), position=method)


if __name__ == '__main__':
    test()
    exit()

    p = r'D:\Projects\wallpyper\src\resources\tray.png'
    gif = r'D:\Projects\Wallpyper\src\resources\busy.gif'
    bind(EVENT_CLOSE, lambda: print(6969))
    s = SysTray(p, 'tip')
    s.bind(Event.LEFT_DOUBLE, _foo)
    s.bind(Event.RIGHT_UP, _foo2)
    _foo3(Event.MOVE, Event.LEFT_DOWN, Event.LEFT_UP, Event.RIGHT_DOWN, Event.BALLOON_HIDDEN)
    s.bind(Event.BALLOON_QUEUED, lambda: print('shown'))
    s.bind(Event.BALLOON_HIDDEN - 1, lambda: print('show_balloon hide'))
    s.bind(Event.BALLOON_CLICK, lambda: print('show_balloon click'))
    s.bind(ctyped.const.NIN_SELECT, lambda: print('sel'))
    s.show()
    p2 = r'D:\Projects\wallpyper\icon.ico'
    s2 = SysTray(p2, 'no tip')
    s2.bind(Event.LEFT_DOUBLE, lambda: print('2nd'))
    s2.bind(Event.RIGHT_UP, s2.hide)
    # s2.show()
    # _foo()
    # s2.mainloop()
    s.mainloop()
    exit()
