from __future__ import annotations as _

__version__ = '0.0.1'

import atexit
import io
import itertools
import sys
import threading
import time
import tkinter.messagebox
import types
from typing import Any, Callable, Generator, Iterable, Mapping, Union
from typing import Optional

import libs.ctyped as ctyped
import win32._gdiplus as gdiplus


def exception_handler(excepthook: Callable, *args, **kwargs):
    stderr = sys.stderr
    sys.stderr = io.StringIO()
    excepthook(*args, **kwargs)
    sys.stderr.seek(0)
    root = tkinter.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    tkinter.messagebox.showerror(args[0][0].__name__, sys.stderr.read())
    root.destroy()
    sys.stderr = stderr


threading.excepthook = types.MethodType(exception_handler, threading.excepthook)

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
    _wm_taskbar_created = ctyped.func.user32.RegisterWindowMessageW('TaskbarCreated')
    _class = None
    _flags = ctyped.const.NIF_MESSAGE | ctyped.const.NIF_ICON | ctyped.const.NIF_TIP
    _frames = None
    _hicon = None
    _hwnd = None
    _shown = False
    _to_del = True
    _uid = 0
    _selves: dict[int, SysTray] = {}

    def __new__(cls, *args, **kwargs):
        if not cls._hwnd:
            cls._class = ctyped.struct.WNDCLASSEXW(
                ctyped.sizeof(ctyped.struct.WNDCLASSEXW), lpfnWndProc=ctyped.type.WNDPROC(cls._callback),
                hInstance=ctyped.func.kernel32.GetModuleHandleW(None), lpszClassName=f'{NAME}-{cls.__name__}')
            ctyped.func.user32.RegisterClassExW(ctyped.byref(cls._class))
            cls._hwnd = ctyped.func.user32.CreateWindowExW(0, cls._class.lpszClassName, None,
                                                           0, 0, 0, 0, 0, None, None, None, None)
        cls._uid += 1
        return super().__new__(cls)

    def __init__(self, icon: Optional[Union[str, int]] = None, tooltip: Optional[str] = None):
        self._uid = self._uid
        self._data = ctyped.struct.NOTIFYICONDATAW(ctyped.sizeof(ctyped.struct.NOTIFYICONDATAW),
                                                   self._hwnd, self._uid, self._flags, ctyped.const.WM_APP)
        self.set_icon(ctyped.const.IDI_APPLICATION if icon is None else icon)
        if tooltip is not None:
            self.set_tooltip(tooltip)
        self._on_timer = ctyped.type.TIMERPROC(self._next_frame)
        self._binds[self._uid] = {}
        self._selves[self._uid] = self
        atexit.register(self.__del__)

    def __del__(self):
        if self._to_del:
            self.hide()
            del self._selves[self._uid]
            del self._binds[self._uid]
            atexit.unregister(self.__del__)
            self._to_del = False
            if len(self._binds) == 1:
                ctyped.func.user32.DestroyWindow(self._hwnd)
                ctyped.func.user32.UnregisterClassW(self._class.lpszClassName,
                                                    ctyped.func.kernel32.GetModuleHandleW(None))
                type(self)._hwnd = None

    @classmethod
    def _call(cls, uid: int, event: int) -> Any:
        try:
            callback, args, kwargs = cls._binds[uid][event]
        except KeyError:
            # print(uid, event)
            return
        else:
            return callback(None if uid == 0 else cls._selves[uid], event, *args, **kwargs)

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
        elif message == cls._wm_taskbar_created:
            for self in cls._selves.values():
                # noinspection PyUnresolvedReferences
                self._update()
        else:
            return ctyped.func.user32.DefWindowProcW(hwnd, message, wparam, lparam)
        return 0

    @classmethod
    def get_handle(cls) -> int:
        return cls._hwnd

    @classmethod
    def run_at_exit(cls, callback: Optional[Callable[[None, int], Any]] = None, args: Optional[Iterable] = None,
                    kwargs: Optional[Mapping[str, Any]] = None) -> bool:
        if callback is None:
            try:
                del cls._binds[0][ctyped.const.WM_CLOSE]
            except KeyError:
                return False
        else:
            cls._binds[0][ctyped.const.WM_CLOSE] = (callback, () if args is None else args,
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
        delay, hicon = next(self._frames)
        self._set_hicon(hicon)
        ctyped.func.user32.SetTimer(self._hwnd, 0, delay, self._on_timer)

    def set_animation(self, gif_path: str):
        self.stop_animation()
        self._frames = itertools.cycle(_get_gif_frames(gif_path))
        self._next_frame()

    def stop_animation(self):
        ctyped.func.user32.KillTimer(self._hwnd, 0)
        self._set_hicon(self._hicon)
        self._frames = None

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

    def destroy(self):
        self.__del__()

    def show_balloon(self, title: str, text: Optional[str] = None,
                     icon: int = Icon.NONE, silent: bool = False) -> bool:
        hicon = self._hicon
        self._data.uFlags = ctyped.const.NIF_INFO | ctyped.const.NIF_ICON
        self._data.hIcon = self._hicon
        if text is None:
            self._data.szInfo = title
            self._data.szInfoTitle = ''
        else:
            self._data.szInfo = text
            self._data.szInfoTitle = title
        self._data.dwInfoFlags = icon | (silent * ctyped.const.NIIF_NOSOUND)
        shown = self.show()
        self._data.uFlags = self._flags
        self._set_hicon(hicon)
        return shown

    def bind(self, event: int, callback: Callable[[SysTray, int], Any],
             args: Optional[Iterable] = None, kwargs: Optional[Mapping[str, Any]] = None):
        bind(event, callback, args, kwargs, self._uid)

    def unbind(self, event: int) -> bool:
        return unbind(event, self._uid)


def bind(event: int, callback: Callable[[Optional[SysTray], int], Any],
         args: Optional[Iterable] = None, kwargs: Optional[Mapping[str, Any]] = None, _uid: int = 0):
    # noinspection PyProtectedMember
    SysTray._binds[_uid][event] = callback, () if args is None else args, {} if kwargs is None else kwargs


def unbind(event: int, _uid: int = 0) -> bool:
    try:
        # noinspection PyProtectedMember
        del SysTray._binds[_uid][event]
    except KeyError:
        return False
    else:
        return True


def _foo(s: SysTray, e):
    # s.show_balloon('title')
    s.set_animation(r'D:\Projects\Wallpyper\src\resources\busy.gif')
    s.show_balloon('very busy', 'mini text', Icon.INFO)
    print('_foo')
    return 0


def _foo2(s, e):
    s.exit_mainloop()  # s.set_icon(r'E:\Projects\wallpyper\icon.ico')  # s.stop_animation()


def _wait():
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass


def _test_sys_tray():
    p = r'D:\Projects\wallpyper\src\resources\tray.png'
    bind(EVENT_CLOSE, lambda *args: print(6969))
    s = SysTray(p, 'tip')
    s.bind(Event.LEFT_DOUBLE, _foo)
    s.bind(Event.RIGHT_UP, _foo2)
    # _foo3(Event.MOVE, Event.LEFT_DOWN, Event.LEFT_UP, Event.RIGHT_DOWN, Event.BALLOON_HIDDEN)
    s.bind(Event.BALLOON_QUEUED, lambda *args: print('shown'))
    s.bind(Event.BALLOON_HIDDEN - 1, lambda *args: print('show_balloon hide'))
    s.bind(Event.BALLOON_CLICK, lambda *args: print('show_balloon click'))
    s.bind(ctyped.const.NIN_SELECT, lambda *args: print('sel'))
    s.show()
    p2 = r'D:\Projects\wallpyper\src\resources\icon.ico'
    s2 = SysTray(p2, 'no tip')
    s2.bind(Event.LEFT_DOUBLE, lambda *args: print('2nd'))
    s2.bind(Event.RIGHT_UP, lambda *args: s2.hide())
    s2.show()
    # _foo()
    # s2.mainloop()
    SysTray.mainloop()


def _test_():
    info = ctyped.struct.SHELLEXECUTEINFOW(ctyped.sizeof(ctyped.struct.SHELLEXECUTEINFOW), lpVerb='open',
                                           lpFile='ms-settings:mobile-devices', nShow=ctyped.const.SW_NORMAL)
    print(ctyped.func.shell32.ShellExecuteExW(ctyped.byref(info)))


def _test():
    import modules.wallhaven as wallhaven
    print(wallhaven._authenticate('38QakOzgfHIohe1JO0f3aoQIbm1pKYK'))


if __name__ == '__main__':
    _test()
    # _test_sys_tray()
    # _wait()
    sys.exit()
