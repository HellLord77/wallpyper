from __future__ import annotations as _

__version__ = '0.0.1'

import itertools
from typing import Any, Callable, Generator, Iterable, Mapping, Union
from typing import Optional

import libs.ctyped as ctyped
import platforms.win32 as win32
import platforms.win32.gdiplus as gdiplus
from platforms.win32.wallpaper import Style, Transition

NAME = f'{__name__}-{__version__}'
EVENT_CLOSE = ctyped.const.WM_CLOSE


def _fill_empty_rect(hdc, out_x, out_y, out_w, out_h, in_x, in_y, in_w, in_h, argb: ctyped.type.ARGB):
    graphics = gdiplus.Graphics.from_hdc(hdc)
    brush = gdiplus.SolidFill.from_color(argb)
    if out_x < in_x:
        graphics.fill_rect(brush, out_x, out_y, in_x - out_x, out_h)
    if out_y < in_y:
        graphics.fill_rect(brush, out_x, out_y, out_w, in_y - out_y)
    if in_x + in_w < out_x + out_w:
        graphics.fill_rect(brush, in_x + in_w, out_y, out_x + out_w - (in_x + in_w), out_h)
    if in_y + in_h < out_y + out_h:
        graphics.fill_rect(brush, out_x, in_y + in_h, out_w, out_y + out_h - (in_y + in_h))


def _get_gif_frames(path: str) -> Generator[tuple[int, ctyped.handle.HICON], None, None]:
    bitmap = gdiplus.Bitmap.from_file(path)
    delays: ctyped.Pointer[ctyped.type.c_long] = bitmap.get_property(ctyped.const.PropertyTagFrameDelay)
    for index in bitmap.iter_frames():
        yield delays[index] * 10, bitmap.get_hicon()


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
    BALLOON_CLICK = ctyped.const.NIN_BALLOONUSERCLICK


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

    def __new__(cls):
        if not cls._hwnd:
            cls._class = ctyped.struct.WNDCLASSEXW(
                ctyped.sizeof(ctyped.struct.WNDCLASSEXW), lpfnWndProc=ctyped.type.WNDPROC(cls._callback),
                hInstance=ctyped.func.kernel32.GetModuleHandleW(None), lpszClassName=f'{NAME}-{cls.__name__}')
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
            # print(uid, event)
            return
        else:
            return callback(*args, **kwargs)

    @classmethod
    def _callback(cls, hwnd: ctyped.type.HWND, message: ctyped.type.UINT, wparam: ctyped.type.WPARAM,
                  lparam: ctyped.type.LPARAM) -> ctyped.type.LRESULT:
        if message == ctyped.const.WM_DESTROY:
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
    def run_at_exit(cls, callback: Optional[Callable] = None, args: Optional[Iterable] = None,
                    kwargs: Optional[Mapping[str, Any]] = None) -> bool:
        if callback is None:
            try:
                del cls._binds[0][ctyped.const.WM_CLOSE]
            except KeyError:
                return False
        else:
            cls._binds[0][ctyped.const.WM_CLOSE] = (callback, () if args is None else {},
                                                    {} if kwargs is None else kwargs)
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
        if isinstance(path_or_res, str):
            self._hicon = gdiplus.Bitmap.from_file(path_or_res).get_hicon()
        else:
            self._hicon = ctyped.handle.HICON.from_system(path_or_res)
        self._set_hicon(self._hicon)
        return bool(self._hicon)

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
        self._frames_and_on_timer = itertools.cycle(_get_gif_frames(gif_path)), ctyped.type.TIMERPROC(self._next_frame)
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
    # s.show_balloon('title')
    s.set_animation(r'D:\Projects\Wallpyper\src\resources\busy.gif')
    print('_foo')
    return 0


def _foo2():
    s.exit_mainloop()  # s.set_icon(r'E:\Projects\wallpyper\icon.ico')  # s.stop_animation()


def _foo3(*evt):
    for e in evt:
        s.bind(e, lambda: None)


def test():
    path = r'C:\Users\ratul\AppData\Local\Temp\Wallpyper\wallhaven-3zyjy9.jpg'
    mon = win32.get_monitor_ids()[1]
    position = Style.DEFAULT
    r = 0
    g = 0
    b = 0
    transition = Transition.LEFT
    duration = 1

    # set(path, mon)


if __name__ == '__main__':
    test()
    exit()

    p = r'D:\Projects\wallpyper\src\resources\tray.png'
    gif = r'D:\Projects\Wallpyper\src\resources\busy.gif'
    bind(EVENT_CLOSE, lambda: print(6969))
    s = SysTray(p, 'tip')
    s.bind(Event.LEFT_DOUBLE, _foo)
    s.bind(Event.RIGHT_UP, _foo2)
    # _foo3(Event.MOVE, Event.LEFT_DOWN, Event.LEFT_UP, Event.RIGHT_DOWN, Event.BALLOON_HIDDEN)
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
    del s
    exit()
