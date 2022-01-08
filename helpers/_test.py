__version__ = '0.0.1'

import contextlib
from typing import Any, Callable, ContextManager, Generator, Iterable, Mapping, Optional, Union

import src.libs.ctyped as ctyped

NAME = f'{__name__}-{__version__}'
EVENT_CLOSE = ctyped.const.WM_CLOSE


class _HICON(ctyped.type.HICON):
    def __del__(self):
        ctyped.lib.user32.DestroyIcon(self)


@contextlib.contextmanager
def _alloc(size: int) -> ContextManager[int]:
    pointer = ctyped.lib.msvcrt.malloc(size)
    try:
        yield pointer
    finally:
        ctyped.lib.msvcrt.free(pointer)


@contextlib.contextmanager
def _open_bitmap(path: str) -> ContextManager[ctyped.type.GpBitmap]:
    bitmap = ctyped.type.GpBitmap()
    token = ctyped.type.ULONG_PTR()
    if not ctyped.lib.GdiPlus.GdiplusStartup(ctyped.byref(token),
                                             ctyped.byref(ctyped.struct.GdiplusStartupInput()), None):
        ctyped.lib.GdiPlus.GdipCreateBitmapFromFile(ctyped.char_array(path), ctyped.byref(bitmap))
    try:
        yield bitmap
    finally:
        ctyped.lib.GdiPlus.GdipDisposeImage(bitmap)
        ctyped.lib.GdiPlus.GdiplusShutdown(token)


def _get_gif_frames(path: str) -> Generator[tuple[int, _HICON], None, None]:
    frames = []
    with _open_bitmap(path) as bitmap:
        if bitmap:
            size = ctyped.type.UINT()
            ctyped.lib.GdiPlus.GdipGetPropertyItemSize(bitmap, ctyped.const.PropertyTagFrameDelay, ctyped.byref(size))
            with _alloc(size.value) as buffer:
                if buffer:
                    properties = ctyped.cast(buffer, ctyped.struct.PropertyItem)
                    ctyped.lib.GdiPlus.GdipGetPropertyItem(bitmap, ctyped.const.PropertyTagFrameDelay,
                                                           size, properties)
                    delays = ctyped.cast(properties.contents.value, ctyped.pointer(ctyped.type.UINT))
                    guid = ctyped.struct.GUID()
                    count = ctyped.type.UINT()
                    ctyped.lib.GdiPlus.GdipImageGetFrameDimensionsList(bitmap, ctyped.byref(guid), 1)
                    ctyped.lib.GdiPlus.GdipImageGetFrameCount(bitmap, ctyped.byref(guid), ctyped.byref(count))
                    for i in range(count.value):
                        hicon = _HICON()
                        ctyped.lib.GdiPlus.GdipImageSelectActiveFrame(bitmap, ctyped.byref(guid), i)
                        ctyped.lib.GdiPlus.GdipCreateHICONFromBitmap(bitmap, ctyped.byref(hicon))
                        if hicon:
                            # noinspection PyTypeChecker
                            frames.append((delays[i] * 10, hicon))
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
    BALLOON_CLICK = ctyped.const.NIN_BALLOONUSERCLICK  # also triggers when click tray icon when balloon shown


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
        # TODO: ctyped.const.WM_QUERYENDSESSION
        if message == ctyped.const.WM_DESTROY:
            ctyped.lib.user32.PostQuitMessage(0)
        elif message == ctyped.const.WM_CLOSE:
            try:
                cls._call(0, message)
            finally:
                ctyped.lib.user32.DestroyWindow(hwnd)
        elif message == ctyped.const.WM_QUERYENDSESSION:
            ...
        elif message == ctyped.const.WM_APP:
            cls._call(wparam, lparam)
        else:
            return ctyped.lib.user32.DefWindowProcW(hwnd, message, wparam, lparam)
        return 0

    @classmethod
    def get_handle(cls) -> int:
        return cls._hwnd

    @classmethod
    def run_at_exit(cls, callback: Callable, args: Optional[Iterable] = None,
                    kwargs: Optional[Mapping[str, Any]] = None) -> None:
        cls._binds[0][ctyped.const.WM_CLOSE] = callback, args or (), kwargs or {}

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
        msg_ref = ctyped.pointer(ctyped.struct.MSG())
        while ctyped.lib.user32.GetMessageW(msg_ref, cls._hwnd, 0, 0) > 0:
            ctyped.lib.user32.TranslateMessage(msg_ref)
            ctyped.lib.user32.DispatchMessageW(msg_ref)
        return msg_ref.contents.wParam

    @classmethod
    def exit_mainloop(cls) -> bool:
        return not bool(ctyped.lib.user32.SendMessageW(cls._hwnd, ctyped.const.WM_CLOSE, 0, 0))

    def __new__(cls, *_, **__):
        if not cls._hwnd:
            cls._class = ctyped.struct.WNDCLASSEXW(ctyped.sizeof(ctyped.struct.WNDCLASSEXW),
                                                   lpfnWndProc=ctyped.type.WNDPROC(cls._callback),
                                                   hInstance=ctyped.lib.kernel32.GetModuleHandleW(None),
                                                   lpszClassName=NAME)
            ctyped.lib.user32.RegisterClassExW(ctyped.byref(cls._class))
            cls._hwnd = ctyped.lib.user32.CreateWindowExW(0, cls._class.lpszClassName, None, 0, 0, 0, 0, 0,
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
            ctyped.lib.user32.DestroyWindow(self._hwnd)
            ctyped.lib.user32.UnregisterClassW(self._class.lpszClassName, ctyped.lib.kernel32.GetModuleHandleW(None))
            type(self)._hwnd = 0

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
                ctyped.lib.GdiPlus.GdipCreateHICONFromBitmap(bitmap, ctyped.byref(hicon))
        else:
            hicon = ctyped.lib.user32.LoadIconW(None, path_or_res)
        self._hicon = _HICON(hicon.value)
        self._set_hicon(self._hicon)
        return bool(hicon)

    def set_tooltip(self, text: str) -> bool:
        self._data.szTip = text
        return self._update()

    def _next_frame(self, *_):
        frame = next(self._frames_and_on_timer[0])
        self._set_hicon(frame[1])
        ctyped.lib.user32.SetTimer(self._hwnd, 0, frame[0], self._frames_and_on_timer[1])

    def set_animation(self, gif_path: str):
        self.stop_animation()
        self._frames_and_on_timer = iter(_get_gif_frames(gif_path)), ctyped.type.TIMERPROC(self._next_frame)
        self._next_frame()

    def stop_animation(self):
        ctyped.lib.user32.KillTimer(self._hwnd, 0)
        self._set_hicon(self._hicon)
        self._frames_and_on_timer = None

    def _update(self) -> bool:
        return self._shown and bool(ctyped.lib.shell32.Shell_NotifyIconW(ctyped.const.NIM_MODIFY, ctyped.byref(
            self._data)) or ctyped.lib.shell32.Shell_NotifyIconW(ctyped.const.NIM_ADD, ctyped.byref(self._data)))

    def show(self) -> bool:
        self._shown = True
        self._shown = self._update()
        return self._shown

    def hide(self) -> bool:
        self._shown = not bool(ctyped.lib.shell32.Shell_NotifyIconW(ctyped.const.NIM_DELETE, ctyped.byref(self._data)))
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
             kwargs: Optional[Mapping[str, Any]] = None) -> None:
        bind(event, callback, args, kwargs, self._uid)

    def unbind(self, event: int) -> bool:
        return unbind(event, self._uid)


def bind(event: int, callback: Callable, args: Optional[Iterable] = None,
         kwargs: Optional[Mapping[str, Any]] = None, _uid: int = 0) -> None:
    # noinspection PyProtectedMember
    SysTray._binds[_uid][event] = callback, args or (), kwargs or {}


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


def _bloop(*evt):
    for e in evt:
        s.bind(e, lambda: None)


if __name__ == '__main__':
    p = r'D:\Projects\wallpyper\src\resources\icon.png'
    bind(EVENT_CLOSE, lambda: print(6969))
    s = SysTray(p, 'tip')
    s.bind(Event.LEFT_DOUBLE, _foo)
    s.bind(Event.RIGHT_UP, _foo2)
    _bloop(Event.MOVE, Event.LEFT_DOWN, Event.LEFT_UP, Event.RIGHT_DOWN, Event.BALLOON_HIDDEN)
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
