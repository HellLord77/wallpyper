from __future__ import annotations as _

__version__ = '0.0.1'

import atexit
import contextlib
import io
import itertools
import sys
import threading
import time
import tkinter.messagebox
import types
from typing import Any, Callable, Iterable, Mapping, Union, Sequence, Generator
from typing import Optional

import libs.ctyped as ctyped
import win32._gdiplus as _gdiplus
import win32._utils as _utils


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


def _fill_empty_rect(hdc, out_x, out_y, out_w, out_h, in_x, in_y, in_w, in_h, argb: ctyped.type.ARGB):
    graphics = _gdiplus.Graphics.from_hdc(hdc)
    brush = _gdiplus.SolidFill.from_color(argb)
    if out_x < in_x:
        graphics.fill_rect(brush, out_x, out_y, in_x - out_x, out_h)
    if out_y < in_y:
        graphics.fill_rect(brush, out_x, out_y, out_w, in_y - out_y)
    if in_x + in_w < out_x + out_w:
        graphics.fill_rect(brush, in_x + in_w, out_y, out_x + out_w - (in_x + in_w), out_h)
    if in_y + in_h < out_y + out_h:
        graphics.fill_rect(brush, out_x, in_y + in_h, out_w, out_y + out_h - (in_y + in_h))


def _get_gif_frames(path: str) -> Generator[tuple[int, ctyped.handle.HICON], None, None]:
    bitmap = _gdiplus.Bitmap.from_file(path)
    delays: ctyped.Pointer[ctyped.type.c_long] = bitmap.get_property(ctyped.const.PropertyTagFrameDelay)
    for index in bitmap.iter_frames():
        yield delays[index] * 10, bitmap.get_hicon()


_WM_TASKBARCREATED = ctyped.lib.User32.RegisterWindowMessageW('TaskbarCreated')
_WM_SYS_TRAY = ctyped.const.WM_APP

_TID_SYS_TRAY_ANIMATION = 0
_TID_MENU_ITEM_TOOLTIP = 1


class Event:
    DISPLAY_CHANGE = ctyped.const.WM_DISPLAYCHANGE

    SYS_TRAY_MOVE = ctyped.const.WM_MOUSEMOVE
    SYS_TRAY_LEFT_DOWN = ctyped.const.WM_LBUTTONDOWN
    SYS_TRAY_LEFT_UP = ctyped.const.WM_LBUTTONUP
    SYS_TRAY_LEFT_DOUBLE = ctyped.const.WM_LBUTTONDBLCLK
    SYS_TRAY_RIGHT_DOWN = ctyped.const.WM_RBUTTONDOWN
    SYS_TRAY_RIGHT_UP = ctyped.const.WM_RBUTTONUP
    SYS_TRAY_RIGHT_DOUBLE = ctyped.const.WM_RBUTTONDBLCLK
    SYS_TRAY_MIDDLE_DOWN = ctyped.const.WM_MBUTTONDOWN
    SYS_TRAY_MIDDLE_UP = ctyped.const.WM_MBUTTONUP
    SYS_TRAY_MIDDLE_DOUBLE = ctyped.const.WM_MBUTTONDBLCLK

    BALLOON_QUEUE = ctyped.const.NIN_BALLOONSHOW
    BALLOON_HIDE = ctyped.const.NIN_BALLOONTIMEOUT
    BALLOON_CLICK = ctyped.const.NIN_BALLOONUSERCLICK

    MENU_SHOW = ctyped.const.WM_INITMENUPOPUP
    MENU_HIDE = ctyped.const.WM_UNINITMENUPOPUP

    MENU_ITEM_HIGHLIGHT = ctyped.const.WM_MENUSELECT
    MENU_ITEM_LEFT_UP = ctyped.const.WM_MENUCOMMAND
    MENU_ITEM_RIGHT_UP = ctyped.const.WM_MENURBUTTONUP


class SysTrayIcon:
    NONE = ctyped.const.NIIF_NONE
    INFO = ctyped.const.NIIF_INFO
    WARNING = ctyped.const.NIIF_WARNING
    ERROR = ctyped.const.NIIF_ERROR
    USER = ctyped.const.NIIF_USER


class _MenuItemKind:
    SEPARATOR = 0
    STRING = 1
    CHECK = 2
    RADIO = 3
    IMAGE = 4
    SUBMENU = 5


class MenuItemImage:
    CLOSE = ctyped.const.HBMMENU_POPUP_CLOSE
    RESTORE = ctyped.const.HBMMENU_POPUP_RESTORE
    MINIMIZE = ctyped.const.HBMMENU_POPUP_MINIMIZE
    MAXIMIZE = ctyped.const.HBMMENU_POPUP_MAXIMIZE


class _EventHandler:
    _id: int
    _selves: dict[int, _EventHandler] = None
    _bindings: dict[int, dict[int, tuple[Callable, Iterable, Mapping]]] = None

    # noinspection PyShadowingBuiltins
    def __init__(self, id: int):
        if self._selves is None:
            type(self)._selves = {}
        if self._bindings is None:
            type(self)._bindings = {}
        self._id = id
        self._selves[id] = self
        self._bindings[id] = {}

    def destroy(self) -> bool:
        try:
            del self._selves[self._id]
            del self._bindings[self._id]
        except KeyError:
            return False
        else:
            return True

    def bind(self, event: int, callback: Callable, args: Optional[Iterable] = None, kwargs: Optional[Mapping] = None):
        self._bindings[self._id][event] = callback, () if args is None else args, {} if kwargs is None else kwargs

    def unbind(self, event: int) -> bool:
        try:
            del self._bindings[self._id][event]
        except KeyError:
            return False
        else:
            return True

    def trigger(self, event: int) -> Any:
        try:
            callback, args, kwargs = self._bindings[self._id][event]
        except KeyError:
            pass
        else:
            return callback(event, self, *args, **kwargs)


class Gui(_EventHandler):
    _selves: dict[int, Gui]

    _hinstance = ctyped.lib.Kernel32.GetModuleHandleW(None)
    _mainloop_running = False
    _menu_item_tooltip_proc = None

    def __init__(self, name: Optional[str] = None):
        self._class = ctyped.struct.WNDCLASSEXW(lpfnWndProc=ctyped.type.WNDPROC(self._wnd_proc),
                                                hInstance=self._hinstance,
                                                lpszClassName=f'{NAME}-{type(self).__name__}' if name is None else name)
        ctyped.lib.User32.RegisterClassExW(ctyped.byref(self._class))
        self._hwnd = ctyped.handle.HWND(ctyped.lib.User32.CreateWindowExW(0, self._class.lpszClassName, None,
                                                                          ctyped.const.WS_OVERLAPPED, 0, 0, 0, 0, None,
                                                                          None, self._hinstance, None))
        self._menu_item_tooltip_hwnd = ctyped.handle.HWND(ctyped.lib.User32.CreateWindowExW(
            ctyped.const.WS_EX_TOPMOST, ctyped.const.TOOLTIPS_CLASS, None,
            ctyped.const.WS_POPUP | ctyped.const.TTS_NOPREFIX | ctyped.const.TTS_ALWAYSTIP,
            ctyped.const.CW_USEDEFAULT, ctyped.const.CW_USEDEFAULT, ctyped.const.CW_USEDEFAULT,
            ctyped.const.CW_USEDEFAULT, self._hwnd, None, None, None))
        self._menu_item_tooltip = ctyped.struct.TTTOOLINFOW(uFlags=ctyped.const.TTF_SUBCLASS)
        self._attached = []
        self._mainloop_lock = threading.Lock()
        self._menu_item_tooltip_lock = threading.Lock()
        super().__init__(self._hwnd.value)
        atexit.register(self.destroy)

    def destroy(self) -> bool:
        atexit.unregister(self.destroy)
        ctyped.lib.User32.KillTimer(self._hwnd, _TID_MENU_ITEM_TOOLTIP)
        while self._attached:
            self._attached.pop().destroy()
        self._menu_item_tooltip = None
        self._menu_item_tooltip_hwnd.send_message(ctyped.const.TTM_DELTOOLW)
        self._menu_item_tooltip_hwnd = None
        self._hwnd = None
        self._menu_item_tooltip_proc = None
        ctyped.lib.User32.UnregisterClassW(self._class.lpszClassName, self._hinstance)
        return super().destroy()

    @classmethod
    def _wnd_proc(cls: Gui, hwnd: ctyped.type.HWND, message: ctyped.type.UINT,
                  wparam: ctyped.type.WPARAM, lparam: ctyped.type.LPARAM) -> ctyped.type.LRESULT:
        if message == ctyped.const.WM_DESTROY:
            ctyped.lib.User32.PostQuitMessage(0)
        elif message == ctyped.const.WM_CLOSE:
            ctyped.lib.User32.DestroyWindow(hwnd)
        elif message == ctyped.const.WM_QUERYENDSESSION:
            ...
        elif message == _WM_TASKBARCREATED:
            # noinspection PyProtectedMember
            SysTray._update_all()
        elif message == ctyped.const.WM_MOUSELEAVE:
            cls._selves[hwnd]._menu_item_tooltip_hwnd.send_message(ctyped.const.TTM_TRACKACTIVATE, lparam=lparam)
        elif message == ctyped.const.WM_ENTERIDLE:
            ctyped.lib.User32.KillTimer(hwnd, _TID_MENU_ITEM_TOOLTIP)
            if wparam == ctyped.const.MSGF_MENU and (proc := cls._selves[hwnd]._menu_item_tooltip_proc) is not None:
                ctyped.lib.User32.SetTimer(hwnd, _TID_MENU_ITEM_TOOLTIP, 800, proc)
        elif message == ctyped.const.WM_DISPLAYCHANGE:
            cls._selves[hwnd].trigger(message)
        elif message == _WM_SYS_TRAY:
            # noinspection PyProtectedMember
            SysTray._selves[wparam].trigger(lparam)
        elif message in (ctyped.const.WM_INITMENUPOPUP, ctyped.const.WM_UNINITMENUPOPUP):
            # noinspection PyProtectedMember
            Menu._selves[wparam].trigger(message)
        elif message in (ctyped.const.WM_MENUSELECT, ctyped.const.WM_MENUCOMMAND, ctyped.const.WM_MENURBUTTONUP):
            if lparam:
                is_select = message == ctyped.const.WM_MENUSELECT
                # noinspection PyProtectedMember
                item = Menu._selves[lparam].get(ctyped.macro.LOWORD(wparam), by_pos=not is_select or (
                        ctyped.const.MF_POPUP == ctyped.macro.HIWORD(wparam) & ctyped.const.MF_POPUP))
                if is_select:
                    ctyped.handle.HWND.send_message(hwnd, ctyped.const.WM_MOUSELEAVE)
                    cls._selves[hwnd]._menu_item_tooltip_proc = item._tooltip_proc
                    ctyped.lib.User32.TrackMouseEvent(ctyped.byref(
                        ctyped.struct.TRACKMOUSEEVENT(dwFlags=ctyped.const.TME_LEAVE, hwndTrack=hwnd)))
                item.trigger(message)
        else:
            return ctyped.lib.User32.DefWindowProcW(hwnd, message, wparam, lparam)
        return 0

    # noinspection PyShadowingBuiltins
    @classmethod
    def get(cls) -> Optional[Gui]:
        with contextlib.suppress(StopIteration):
            return next(reversed(cls._selves.values()))

    @classmethod
    def attach(cls, obj, gui: Optional[Gui]) -> ctyped.handle.HWND:
        if gui is None:
            gui = cls.get()
            if gui is None:
                raise RuntimeError(f"'{cls.__name__}' not created yet")
        gui._attached.append(obj)
        return gui._hwnd

    def _show_menu_item_tooltip(self, text: str):
        with self._menu_item_tooltip_lock:
            self._menu_item_tooltip.lpszText = text
            lparam = ctyped.addressof(self._menu_item_tooltip)
            self._menu_item_tooltip_hwnd.send_message(ctyped.const.TTM_ADDTOOLW, lparam=lparam)
            self._hwnd.send_message(ctyped.const.WM_MOUSELEAVE, lparam=lparam)
            self._menu_item_tooltip_hwnd.send_message(ctyped.const.TTM_TRACKACTIVATE, 1, lparam)

    def get_name(self) -> str:
        return self._class.lpszClassName

    def is_mainloop_running(self) -> bool:
        return self._mainloop_lock.locked()

    def mainloop(self) -> Optional[int]:
        with self._mainloop_lock:
            msg = ctyped.struct.MSG()
            msg_ref = ctyped.byref(msg)
            while ctyped.lib.User32.GetMessageW(msg_ref, self._hwnd, 0, 0) > 0:
                ctyped.lib.User32.TranslateMessage(msg_ref)
                ctyped.lib.User32.DispatchMessageW(msg_ref)
            return msg.wParam

    def exit_mainloop(self) -> bool:
        return bool(self._hwnd.send_message(ctyped.const.WM_CLOSE, wait=False))


class SysTray(_EventHandler):
    _selves: dict[int, SysTray]
    _hwnd = None
    _id_gen = itertools.count(1)

    _flags = ctyped.const.NIF_MESSAGE | ctyped.const.NIF_ICON | ctyped.const.NIF_TIP
    _hicon = None
    _shown = False
    _animation_frames = None

    def __init__(self, icon: Union[int, str] = ctyped.const.IDI_APPLICATION,
                 tooltip: Optional[str] = None, *, _gui: Optional[Gui] = None):
        self._hwnd = Gui.attach(self, _gui)
        self._animation_proc = ctyped.type.TIMERPROC(self._set_next_frame)
        super().__init__(next(self._id_gen))
        self._data = ctyped.struct.NOTIFYICONDATAW(hWnd=self._hwnd, uID=self._id,
                                                   uFlags=self._flags, uCallbackMessage=_WM_SYS_TRAY)
        self.set_icon(icon)
        if tooltip is not None:
            self.set_tooltip(tooltip)

    def destroy(self) -> bool:
        self.stop_animation()
        self.hide()
        return super().destroy()

    @classmethod
    def _update_all(cls):
        for self in cls._selves.values():
            self._update()

    def is_shown(self) -> bool:
        return self._shown

    def _set_hicon(self, hicon: Optional[ctyped.type.HICON] = None) -> bool:
        self._data.hIcon = hicon
        return self._update()

    def set_icon(self, res_or_path: Union[int, str]) -> bool:
        self.stop_animation()
        if isinstance(res_or_path, str):
            self._hicon = _gdiplus.Bitmap.from_file(res_or_path).get_hicon()
        else:
            self._hicon = ctyped.handle.HICON.from_idi(res_or_path)
        self._set_hicon(self._hicon)
        return bool(self._hicon)

    def set_tooltip(self, text: str) -> bool:
        self._data.szTip = text
        return self._update()

    def _set_next_frame(self, *_):
        try:
            delay, hicon = next(self._animation_frames)
        except TypeError:
            pass
        else:
            self._set_hicon(hicon)
            ctyped.lib.User32.SetTimer(self._hwnd, _TID_SYS_TRAY_ANIMATION, delay, self._animation_proc)

    def set_animation(self, gif_path: str):
        self.stop_animation()
        self._animation_frames = itertools.cycle(tuple(_get_gif_frames(gif_path)))
        self._set_next_frame()

    def stop_animation(self):
        self._animation_frames = None
        ctyped.lib.User32.KillTimer(self._hwnd, _TID_SYS_TRAY_ANIMATION)
        self._set_hicon(self._hicon)

    def _update(self) -> bool:
        return self._shown and bool(ctyped.lib.Shell32.Shell_NotifyIconW(ctyped.const.NIM_MODIFY, ctyped.byref(
            self._data)) or ctyped.lib.Shell32.Shell_NotifyIconW(ctyped.const.NIM_ADD, ctyped.byref(self._data)))

    def show(self) -> bool:
        self._shown = True
        self._shown = self._update()
        return self._shown

    def hide(self) -> bool:
        self._shown = not bool(ctyped.lib.Shell32.Shell_NotifyIconW(ctyped.const.NIM_DELETE, ctyped.byref(self._data)))
        return not self._shown

    def show_balloon(self, title: str, text: Optional[str] = None,
                     icon: int = SysTrayIcon.NONE, silent: bool = False) -> bool:
        hicon = self._hicon
        self._data.uFlags = ctyped.const.NIF_INFO | ctyped.const.NIF_ICON
        self._data.hIcon = self._hicon
        if text is None:
            self._data.szInfo = title
            self._data.szInfoTitle = ''
        else:
            self._data.szInfo = text
            self._data.szInfoTitle = title
        self._data.dwInfoFlags = icon | ctyped.const.NIIF_RESPECT_QUIET_TIME
        if silent:
            self._data.dwInfoFlags |= ctyped.const.NIIF_NOSOUND
        try:
            return self.show()
        finally:
            self._data.uFlags = self._flags
            self._set_hicon(hicon)


class Menu(_EventHandler):
    _selves: dict[int, Menu]
    _hwnd = None

    _mim_field = {
        ctyped.const.MIM_BACKGROUND: 'hbrBack',
        ctyped.const.MIM_HELPID: 'dwContextHelpID',
        ctyped.const.MIM_MAXHEIGHT: 'cyMax',
        ctyped.const.MIM_STYLE: 'dwStyle'}
    _miim_fields = {
        ctyped.const.MIIM_STATE: ('fState',),
        ctyped.const.MIIM_ID: ('wID',),
        ctyped.const.MIIM_SUBMENU | ctyped.const.MIIM_STRING: ('hSubMenu', 'dwTypeData'),
        ctyped.const.MIIM_CHECKMARKS: ('hbmpChecked', 'hbmpUnchecked'),
        ctyped.const.MIIM_TYPE: ('fType', 'dwTypeData'),
        ctyped.const.MIIM_DATA: ('dwItemData',),
        ctyped.const.MIIM_STRING: ('dwTypeData', 'cch'),
        ctyped.const.MIIM_BITMAP: ('hbmpItem',),
        ctyped.const.MIIM_FTYPE: ('fType',)}

    def __init__(self, *, _gui: Optional[Gui] = None):
        self._hwnd = Gui.attach(self, _gui)
        self._hmenu = ctyped.handle.HMENU.from_type()
        ctyped.lib.User32.SetMenuInfo(self._hmenu, ctyped.byref(
            ctyped.struct.MENUINFO(fMask=ctyped.const.MIM_STYLE, dwStyle=ctyped.const.MNS_NOTIFYBYPOS)))
        self._hmenu.set_hwnd(self._hwnd)
        self._items: list[MenuItem] = []
        super().__init__(self._hmenu.value)

    def destroy(self) -> bool:
        self._items.clear()
        self._hmenu = None
        return super().destroy()

    def __contains__(self, id_or_item: Union[int, MenuItem]):
        return self.get(id_or_item) is not None

    def __len__(self):
        return len(self._items)

    def __getitem__(self, pos: Union[int, slice]) -> Union[MenuItem, tuple[MenuItem]]:
        items = self._items[pos]
        return tuple(items) if isinstance(pos, slice) else items

    def __delitem__(self, pos_or_item: Union[int, slice, MenuItem]) -> bool:
        if isinstance(pos_or_item, slice):
            deleted = True
            for item in self[pos_or_item]:
                deleted = self.__delitem__(item) and deleted
            return deleted
        else:
            return self.remove(pos_or_item, True)

    def __iter__(self) -> MenuItem:
        yield from self._items

    def get_count(self) -> int:
        return self._hmenu.get_item_count()

    def get(self, id_or_pos_or_item: Union[int, MenuItem], default: Any = None, by_pos: bool = False) -> MenuItem:
        if by_pos:
            with contextlib.suppress(IndexError):
                return self[id_or_pos_or_item]
        elif (info := self._get_item_info(id_or_pos_or_item, ctyped.const.MIIM_ID, by_pos)) is not None:
            # noinspection PyProtectedMember
            return MenuItem._selves[info[0]]
        return default

    def append(self, text: str = '', image: Optional = None, submenu: Optional[Menu] = None,
               enable: bool = True, highlight: bool = False, check: Optional[bool] = None,
               default: bool = False, kind: int = _MenuItemKind.STRING) -> Optional[MenuItem]:
        return self.insert(self.get_count(), text, image, submenu, enable, highlight, check, default, kind)

    def insert(self, pos: int, text: str = '', image: Optional = None, submenu: Optional[Menu] = None,
               enable: bool = True, highlight: bool = False, check: Optional[bool] = None,
               default: bool = False, kind: int = _MenuItemKind.STRING) -> Optional[MenuItem]:
        item = MenuItem(self, gui=Gui._selves[self._hwnd.value])
        if ctyped.lib.User32.InsertMenuW(self._hmenu, pos,
                                         ctyped.const.MF_BYPOSITION | ctyped.const.MF_STRING, item.get_id(), None):
            self._items.insert(pos, item)
            item.set_text(text)
            item.set_states(enable, highlight, check, default)
            return item

    def remove(self, id_or_pos_or_item: Union[int, MenuItem], by_pos: bool = False) -> bool:
        if isinstance(id_or_pos_or_item, MenuItem):
            id_or_pos_or_item = id_or_pos_or_item.get_id()
            by_pos = False
        removed = bool(ctyped.lib.User32.RemoveMenu(
            self._hmenu, id_or_pos_or_item, ctyped.const.MF_BYPOSITION if by_pos else ctyped.const.MF_BYCOMMAND))
        if removed:
            self._items.remove(self.get(id_or_pos_or_item, by_pos))
        return removed

    def clear(self) -> bool:
        return self.__delitem__(slice(None))

    def show(self, pos: Optional[Sequence[int, int]] = None, timeout: Optional[float] = None) -> bool:
        if pos is None:
            point = ctyped.struct.POINT()
            ctyped.lib.User32.GetCursorPos(ctyped.byref(point))
            pos = point.x, point.y
        timer = threading.Timer(timeout, self.hide)
        timer.start()
        try:
            return bool(self._hmenu.track(*pos))
        finally:
            timer.cancel()

    def hide(self) -> bool:
        return self._hmenu.untrack()

    def _get_item_props(self, id_or_pos_or_item: Union[int, MenuItem],
                        states: bool, index: int, by_pos: bool) -> Optional[bool]:
        # noinspection PyArgumentList
        return None if (props := (self.get_item_states if states else self.get_item_types)(
            id_or_pos_or_item, by_pos)) is None else props[index]

    def _prep_item_image(self, id_or_pos_or_item: Union[int, MenuItem],
                         res_or_path: Union[int, str], index: int, by_pos: bool) -> int:
        if isinstance(res_or_path, str):
            res_or_path = _gdiplus.Bitmap.from_file(res_or_path).get_hbitmap()
            # noinspection PyProtectedMember
            (id_or_pos_or_item if isinstance(id_or_pos_or_item, MenuItem) else self.get(
                id_or_pos_or_item, by_pos))._hbmps[index] = res_or_path
            return res_or_path.value
        return res_or_path

    def _get_item_info(self, id_or_pos_or_item: Union[int, MenuItem], miim: int, by_pos: bool,
                       item_info: Optional[ctyped.struct.MENUITEMINFOW] = None) -> Optional[tuple]:
        if isinstance(id_or_pos_or_item, MenuItem):
            id_or_pos_or_item = id_or_pos_or_item.get_id()
            by_pos = False
        if item_info is None:
            item_info = ctyped.struct.MENUITEMINFOW()
        item_info.fMask = miim
        if ctyped.lib.User32.GetMenuItemInfoW(self._hmenu, id_or_pos_or_item, by_pos, ctyped.byref(item_info)):
            return tuple(getattr(item_info, field) for field in self._miim_fields[miim])

    def _get_item_image(self, id_or_pos_or_item: Union[int, MenuItem],
                        by_pos: bool = False) -> Optional[ctyped.handle.HBITMAP]:
        if info := self._get_item_info(id_or_pos_or_item, ctyped.const.MIIM_BITMAP, by_pos):
            return ctyped.handle.HBITMAP(info[0])

    def _get_item_check_icons(self, id_or_pos_or_item: Union[int, MenuItem],
                              by_pos: bool = False) -> Optional[tuple[ctyped.handle.HBITMAP, ctyped.handle.HBITMAP]]:
        if info := self._get_item_info(id_or_pos_or_item, ctyped.const.MIIM_CHECKMARKS, by_pos):
            return ctyped.handle.HBITMAP(info[0]), ctyped.handle.HBITMAP(info[1])

    def get_item_types(self, id_or_pos_or_item: Union[int, MenuItem],
                       by_pos: bool = False) -> Optional[tuple[bool, bool, bool, bool]]:
        if info := self._get_item_info(id_or_pos_or_item, ctyped.const.MIIM_TYPE, by_pos):
            return (ctyped.const.MFT_MENUBREAK == info[0] & ctyped.const.MFT_MENUBREAK,
                    ctyped.const.MFT_RADIOCHECK == info[0] & ctyped.const.MFT_RADIOCHECK,
                    ctyped.const.MFT_RIGHTORDER == info[0] & ctyped.const.MFT_RIGHTORDER,
                    ctyped.const.MFT_RIGHTJUSTIFY == info[0] & ctyped.const.MFT_RIGHTJUSTIFY)

    def is_item_broken(self, id_or_pos_or_item: Union[int, MenuItem], by_pos: bool = False) -> Optional[bool]:
        return self._get_item_props(id_or_pos_or_item, False, 0, by_pos)

    def is_item_radio(self, id_or_pos_or_item: Union[int, MenuItem], by_pos: bool = False) -> Optional[bool]:
        return self._get_item_props(id_or_pos_or_item, False, 1, by_pos)

    def is_item_right_ordered(self, id_or_pos_or_item: Union[int, MenuItem], by_pos: bool = False) -> Optional[bool]:
        return self._get_item_props(id_or_pos_or_item, False, 2, by_pos)

    def is_item_right_justified(self, id_or_pos_or_item: Union[int, MenuItem], by_pos: bool = False) -> Optional[bool]:
        return self._get_item_props(id_or_pos_or_item, False, 3, by_pos)

    def get_item_id(self, pos_or_item: Union[int, MenuItem]) -> int:
        return info[0] if (info := self._get_item_info(pos_or_item, ctyped.const.MIIM_ID, True)) else -1

    def get_item_states(self, id_or_pos_or_item: Union[int, MenuItem],
                        by_pos: bool = False) -> Optional[tuple[bool, bool, bool, bool]]:
        if info := self._get_item_info(id_or_pos_or_item, ctyped.const.MIIM_STATE, by_pos):
            return (ctyped.const.MFS_ENABLED == info[0] & (ctyped.const.MF_GRAYED | ctyped.const.MFS_DISABLED),
                    ctyped.const.MFS_HILITE == info[0] & ctyped.const.MFS_HILITE,
                    ctyped.const.MFS_CHECKED == info[0] & ctyped.const.MFS_CHECKED,
                    ctyped.const.MFS_DEFAULT == info[0] & ctyped.const.MFS_DEFAULT)

    def is_item_enabled(self, id_or_pos_or_item: Union[int, MenuItem], by_pos: bool = False) -> Optional[bool]:
        return self._get_item_props(id_or_pos_or_item, True, 0, by_pos)

    def is_item_highlighted(self, id_or_pos_or_item: Union[int, MenuItem], by_pos: bool = False) -> Optional[bool]:
        return self._get_item_props(id_or_pos_or_item, True, 1, by_pos)

    def is_item_checked(self, id_or_pos_or_item: Union[int, MenuItem], by_pos: bool = False) -> Optional[bool]:
        return self._get_item_props(id_or_pos_or_item, True, 2, by_pos)

    def is_item_default(self, id_or_pos_or_item: Union[int, MenuItem], by_pos: bool = False) -> Optional[bool]:
        return self._get_item_props(id_or_pos_or_item, True, 3, by_pos)

    def get_item_text(self, id_or_pos_or_item: Union[int, MenuItem], by_pos: bool = False) -> str:
        item_info = ctyped.struct.MENUITEMINFOW()
        if self._get_item_info(id_or_pos_or_item, ctyped.const.MIIM_STRING, by_pos, item_info) and item_info.cch:
            item_info.cch += 1
            with _utils.string_buffer(item_info.cch) as buff:
                item_info.dwTypeData = buff
                if self._get_item_info(id_or_pos_or_item, ctyped.const.MIIM_STRING, by_pos, item_info):
                    return item_info.dwTypeData
        return ''

    def get_item_submenu(self, id_or_pos_or_item: Union[int, MenuItem], by_pos: bool = False) -> Optional[Menu]:
        if info := self._get_item_info(id_or_pos_or_item, ctyped.const.MIIM_SUBMENU, by_pos):
            return self._selves[info[0]]

    def _set_item_info(self, id_or_pos_or_item: Union[int, MenuItem],
                       infos: Iterable, miim: int, by_pos: bool) -> bool:
        if isinstance(id_or_pos_or_item, MenuItem):
            id_or_pos_or_item = id_or_pos_or_item.get_id()
            by_pos = False
        item_info = ctyped.struct.MENUITEMINFOW(fMask=miim)
        for field, info in zip(self._miim_fields[miim], infos):
            setattr(item_info, field, info)
        return bool(ctyped.lib.User32.SetMenuItemInfoW(self._hmenu, id_or_pos_or_item, by_pos, ctyped.byref(item_info)))

    def _set_item_icon(self, id_or_pos_or_item: Union[int, MenuItem],
                       res_or_path: Union[int, str], by_pos: bool = False) -> bool:
        return self._set_item_info(id_or_pos_or_item, (self._prep_item_image(
            id_or_pos_or_item, res_or_path, 0, by_pos),), ctyped.const.MIIM_BITMAP, by_pos)

    def set_item_check_icons(self, id_or_pos_or_item: Union[int, MenuItem],
                             res_or_path_checked: Optional[Union[int, str]] = None,
                             res_or_path_unchecked: Optional[Union[int, str]] = None, by_pos: bool = False) -> bool:
        return self._set_item_info(id_or_pos_or_item, (
            self._prep_item_image(id_or_pos_or_item, res_or_path_checked, 1, by_pos),
            self._prep_item_image(id_or_pos_or_item, res_or_path_unchecked, 2, by_pos)),
                                   ctyped.const.MIIM_CHECKMARKS, by_pos)

    def _set_item_types(self, id_or_pos_or_item: Union[int, MenuItem], broken: Optional[bool] = None,
                        radio: Optional[bool] = None, right_ordered: Optional[bool] = None,
                        right_justified: Optional[bool] = None, by_pos: bool = False) -> bool:
        types_ = self.get_item_types(id_or_pos_or_item, by_pos)
        flags = 0
        if types_[0] if broken is None else broken:
            flags |= ctyped.const.MF_MENUBREAK
        if types_[1] if radio is None else radio:
            flags |= ctyped.const.MFT_RADIOCHECK
        if types_[2] if right_ordered is None else right_ordered:
            flags |= ctyped.const.MFT_RIGHTORDER
        if types_[3] if right_justified is None else right_justified:
            flags |= ctyped.const.MFT_RIGHTJUSTIFY
        return self._set_item_info(id_or_pos_or_item, (flags,), ctyped.const.MIIM_FTYPE, by_pos)

    def _set_item_broken(self, id_or_pos_or_item: Union[int, MenuItem],
                         broken: bool = True, by_pos: bool = False) -> bool:
        return self._set_item_types(id_or_pos_or_item, broken, by_pos=by_pos)

    def _set_item_radio(self, id_or_pos_or_item: Union[int, MenuItem],
                        radio: bool = True, by_pos: bool = False) -> bool:
        return self._set_item_types(id_or_pos_or_item, radio=radio, by_pos=by_pos)

    def set_item_right_ordered(self, id_or_pos_or_item: Union[int, MenuItem],
                               right_ordered: bool = True, by_pos: bool = False) -> bool:
        return self._set_item_types(id_or_pos_or_item, right_ordered=right_ordered, by_pos=by_pos)

    def _set_item_right_justified(self, id_or_pos_or_item: Union[int, MenuItem],
                                  right_justified: bool = True, by_pos: bool = False) -> bool:
        return self._set_item_types(id_or_pos_or_item, right_justified=right_justified, by_pos=by_pos)

    # noinspection PyShadowingBuiltins
    def _set_item_id(self, id_or_pos_or_item: Union[int, MenuItem], id: int, by_pos: bool = False) -> bool:
        return self._set_item_info(id_or_pos_or_item, (id,), ctyped.const.MIIM_ID, by_pos)

    def set_item_states(self, id_or_pos_or_item: Union[int, MenuItem], enable: Optional[bool] = None,
                        highlight: Optional[bool] = None, check: Optional[bool] = None,
                        default: Optional[bool] = None, by_pos: bool = False) -> bool:
        states = self.get_item_states(id_or_pos_or_item, by_pos)
        flags = ctyped.const.MFS_ENABLED if (states[0] if enable is None else enable) else ctyped.const.MFS_DISABLED
        flags |= ctyped.const.MFS_HILITE if (states[1] if highlight is None else
                                             highlight) else ctyped.const.MFS_UNHILITE
        flags |= ctyped.const.MFS_CHECKED if (states[2] if check is None else check) else ctyped.const.MFS_UNCHECKED
        if states[3] if default is None else default:
            flags |= ctyped.const.MFS_DEFAULT
        return self._set_item_info(id_or_pos_or_item, (flags,), ctyped.const.MIIM_STATE, by_pos)

    def enable_item(self, id_or_pos_or_item: Union[int, MenuItem], enable: bool = True, by_pos: bool = False) -> bool:
        return self.set_item_states(id_or_pos_or_item, enable, by_pos=by_pos)

    def highlight_item(self, id_or_pos_or_item: Union[int, MenuItem],
                       highlight: bool = True, by_pos: bool = False) -> bool:
        return self.set_item_states(id_or_pos_or_item, highlight=highlight, by_pos=by_pos)

    def _check_item(self, id_or_pos_or_item: Union[int, MenuItem], check: bool = True, by_pos: bool = False) -> bool:
        return self._check_item_radio(id_or_pos_or_item, by_pos) if self.is_item_radio(
            id_or_pos_or_item, by_pos) else self.set_item_states(id_or_pos_or_item, check=check, by_pos=by_pos)

    def set_default_item(self, id_or_pos_or_item: Union[int, MenuItem],
                         default: bool = True, by_pos: bool = False) -> bool:
        return self.set_item_states(id_or_pos_or_item, default=default, by_pos=by_pos)

    def set_item_text(self, id_or_pos_or_item: Union[int, MenuItem], text: str, by_pos: bool = False) -> bool:
        return self._set_item_info(id_or_pos_or_item, (ctyped.const.MFT_STRING, text), ctyped.const.MIIM_TYPE, by_pos)

    def _set_item_image(self, id_or_pos_or_item: Union[int, MenuItem],
                        res_or_path: Union[int, str], by_pos: bool = False) -> bool:
        return self._set_item_info(id_or_pos_or_item, (ctyped.const.MFT_BITMAP, ctyped.type.LPWSTR(
            self._prep_item_image(id_or_pos_or_item, res_or_path, 0, by_pos))), ctyped.const.MIIM_TYPE, by_pos)

    def set_item_submenu(self, id_or_pos_or_item: Union[int, MenuItem],
                         submenu: Menu, text: Optional[str] = None, by_pos: bool = False) -> bool:
        return self._set_item_info(id_or_pos_or_item, (
            submenu._hmenu, self.get_item_text(id_or_pos_or_item, by_pos)
            if text is None else text), ctyped.const.MIIM_SUBMENU | ctyped.const.MIIM_STRING, by_pos)

    def get_item_pos(self, id_or_item: Union[int, MenuItem]) -> int:
        if isinstance(id_or_item, MenuItem):
            id_or_item = id_or_item.get_id() if id_or_item.get_menu() is self else -1
        for pos, item in enumerate(self):
            if id_or_item == item.get_id():
                return pos
        return -1

    def _check_item_radio(self, id_or_pos_or_item: Union[int, MenuItem], by_pos: bool = False) -> bool:
        if not by_pos or isinstance(id_or_pos_or_item, MenuItem):
            id_or_pos_or_item = self.get_item_pos(id_or_pos_or_item)
        first_pos = last_pos = id_or_pos_or_item
        while self.is_item_radio(first_pos - 1, True):
            first_pos -= 1
        while self.is_item_radio(last_pos + 1, True):
            last_pos += 1
        return self._hmenu.check_radio_item(id_or_pos_or_item, first_pos, last_pos, True)

    def check_item(self, id_or_pos_or_item: Union[int, MenuItem], check: bool = True, by_pos: bool = False) -> bool:
        return self._check_item_radio(id_or_pos_or_item, by_pos) if self.is_item_radio(
            id_or_pos_or_item, by_pos) else self._check_item(id_or_pos_or_item, check, by_pos)

    def set_item_image(self, id_or_pos_or_item: Union[int, MenuItem],
                       res_or_path: Union[int, str], image_only: bool = False, by_pos: bool = False) -> bool:
        # noinspection PyArgumentList
        return (self._set_item_image if image_only else self._set_item_icon)(id_or_pos_or_item, res_or_path, by_pos)

    def bind_item(self, id_or_pos_or_item: Union[int, MenuItem], event: int, callback: Callable,
                  args: Optional[Iterable] = None, kwargs: Optional[Mapping] = None, by_pos: bool = False):
        self.get(id_or_pos_or_item, by_pos=by_pos).bind(event, callback, args, kwargs)

    def unbind_item(self, id_or_pos_or_item: Union[int, MenuItem], event: int, by_pos: bool = False) -> bool:
        return self.get(id_or_pos_or_item, by_pos=by_pos).unbind(event)

    def trigger_item(self, id_or_pos_or_item: Union[int, MenuItem], event: int, by_pos: bool = False) -> Any:
        return self.get(id_or_pos_or_item, by_pos=by_pos).trigger(event)


class MenuItem(_EventHandler):
    _selves: dict[int, MenuItem]
    _id_gen = itertools.count(1)
    tooltip: str = ''

    def __init__(self, menu: Menu, *, gui: Optional[Gui] = None):
        self._hwnd = Gui.attach(self, gui)
        self._tooltip_proc = ctyped.type.TIMERPROC(self._show_tooltip)
        self._menu = menu
        self._hbmps: list[Optional[ctyped.handle.HBITMAP]] = [None] * 3
        super().__init__(next(self._id_gen))

    def _show_tooltip(self, *_):
        gui = Gui._selves[self._hwnd.value]
        gui._menu_item_tooltip_proc = None
        ctyped.lib.User32.KillTimer(self._hwnd, _TID_MENU_ITEM_TOOLTIP)
        if self.tooltip and (pos := self.get_pos()) != -1:
            rect = ctyped.struct.RECT()
            ctyped.lib.User32.GetMenuItemRect(self._hwnd, self._menu._hmenu, pos, ctyped.byref(rect))
            pt = ctyped.struct.POINT()
            ctyped.lib.User32.GetCursorPos(ctyped.byref(pt))
            if rect.left <= pt.x <= rect.right and rect.top <= pt.y <= rect.bottom:
                gui._show_menu_item_tooltip(self.tooltip)

    def get_menu(self) -> Menu:
        return self._menu

    def get_id(self) -> int:
        return self._id

    def get_pos(self) -> int:
        return self._menu.get_item_pos(self)

    def get_types(self) -> tuple[bool, bool, bool, bool]:
        return self._menu.get_item_types(self._id)

    def is_broken(self) -> bool:
        return self._menu.is_item_broken(self._id)

    def is_radio(self) -> bool:
        return self._menu.is_item_radio(self._id)

    def is_right_ordered(self) -> bool:
        return self._menu.is_item_right_ordered(self._id)

    def is_right_justified(self) -> bool:
        return self._menu.is_item_right_justified(self._id)

    def get_states(self) -> tuple[bool, bool, bool, bool]:
        return self._menu.get_item_states(self._id)

    def is_enabled(self) -> bool:
        return self._menu.is_item_enabled(self._id)

    def is_highlighted(self) -> bool:
        return self._menu.is_item_highlighted(self._id)

    def is_checked(self) -> bool:
        return self._menu.is_item_checked(self._id)

    def is_default(self) -> bool:
        return self._menu.is_item_default(self._id)

    def get_text(self) -> str:
        return self._menu.get_item_text(self._id)

    def get_submenu(self) -> Optional[Menu]:
        return self._menu.get_item_submenu(self._id)

    def set_check_icons(self, res_or_path_checked: Optional[Union[int, str]] = None,
                        res_or_path_unchecked: Optional[Union[int, str]] = None) -> bool:
        return self._menu.set_item_check_icons(self._id, res_or_path_checked, res_or_path_unchecked)

    def set_right_ordered(self, right_ordered: bool = True) -> bool:
        return self._menu.set_item_right_ordered(self._id, right_ordered)

    def set_states(self, enable: Optional[bool] = None, highlight: Optional[bool] = None,
                   check: Optional[bool] = None, default: Optional[bool] = None) -> bool:
        return self._menu.set_item_states(self._id, enable, highlight, check, default)

    def enable(self, enable: bool = True) -> bool:
        return self._menu.enable_item(self._id, enable)

    def highlight(self, highlight: bool = True) -> bool:
        return self._menu.highlight_item(self._id, highlight)

    def check(self, check: bool = True) -> bool:
        return self._menu.check_item(self._id, check)

    def set_default(self, default: bool = True) -> bool:
        return self._menu.set_default_item(self._id, default)

    def set_text(self, text: str) -> bool:
        return self._menu.set_item_text(self._id, text)

    def set_submenu(self, submenu: Menu) -> bool:
        return self._menu.set_item_submenu(self._id, submenu)

    def set_image(self, res_or_path: Union[int, str], image_only: bool = False) -> bool:
        return self._menu.set_item_image(self._id, res_or_path, image_only)


def _foo(e, s: SysTray, menu: Menu, item: MenuItem):
    # s.show_balloon('very busy', 'mini text', Icon.USER)
    menu.show()
    return 0


def _foo2(e: int, s: SysTray):
    s.set_animation(r'D:\Projects\Wallpyper\src\resources\busy.gif')
    # Gui.get().exit_mainloop()  # s.set_icon(r'E:\Projects\wallpyper\icon.ico')  # s.stop_animation()


def foo3(e, m: SysTray, s: SysTray):
    s.stop_animation()


def _wait():
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass


def _test_sys_tray():
    p = r'D:\Projects\wallpyper\src\resources\tray.png'
    # bind(EVENT_CLOSE, lambda *args: print(6969))
    g = Gui()
    s = SysTray(p, 'tip')
    menu = Menu()
    menu.bind(Event.MENU_SHOW, lambda *args: print('show menu'))
    menu.bind(Event.MENU_HIDE, lambda *args: print('hide menu'))
    it = menu.append('stop animate\tright')
    it.bind(Event.MENU_ITEM_LEFT_UP, foo3, (s,))
    it.tooltip = 'important long text tip'
    ball = menu.append('balloon\tright2')
    ball.bind(Event.MENU_ITEM_RIGHT_UP, lambda *args: print('balloon button right up'))
    ball.bind(Event.MENU_ITEM_LEFT_UP, lambda *args: s.show_balloon('very busy', 'mini text', SysTrayIcon.USER))
    # print(menu.set_item_image(it, p))
    # ctyped.lib.User32.SetMenu(s._hwnd, menu._hmenu)
    item = menu.append('text', check=True)
    # print(item.get_id(), menu.get_item_id(item))
    menu2 = Menu()
    menu2.append('gg')
    it7 = menu2.append('69')
    it7.bind(Event.MENU_ITEM_HIGHLIGHT, lambda *args: print('hover', args))
    menu2.append('new')
    ex = menu.append('exit')
    ex.bind(Event.MENU_ITEM_LEFT_UP, lambda *args: g.exit_mainloop())
    # print(item.set_image(r'D:\Projects\wallpyper\src\resources\tray.png', True))
    # menu.set_item_submenu(item, menu2)
    item.set_submenu(menu2)
    g.bind(Event.DISPLAY_CHANGE, lambda *args: print('display', args))

    s.bind(Event.SYS_TRAY_RIGHT_UP, _foo, (menu, item))
    s.bind(Event.SYS_TRAY_LEFT_DOUBLE, _foo2)
    s.bind(Event.BALLOON_QUEUE, lambda *args: print('shown balloon'))
    s.bind(Event.BALLOON_HIDE - 1, lambda *args: print('show_balloon hide'))
    s.bind(Event.BALLOON_CLICK, lambda *args: print('show_balloon click'))
    s.bind(ctyped.const.NIN_SELECT, lambda *args: print('sel'))
    s.show()
    g.mainloop()
    g.destroy()
    print('exit')


def _test_():
    info = ctyped.struct.SHELLEXECUTEINFOW(lpVerb='open',
                                           lpFile='ms-settings:mobile-devices', nShow=ctyped.const.SW_NORMAL)
    print(ctyped.lib.Shell32.ShellExecuteExW(ctyped.byref(info)))


def tst():
    try:
        return 69
    finally:
        raise TypeError


def _enable_visual_styles() -> bool:
    if sz := ctyped.lib.Kernel32.GetSystemDirectoryW(None, 0):
        with _utils.string_buffer(sz) as buff:
            if ctyped.lib.Kernel32.GetSystemDirectoryW(buff, sz):
                ctx = ctyped.struct.ACTCTXW(dwFlags=(
                        ctyped.const.ACTCTX_FLAG_RESOURCE_NAME_VALID |
                        ctyped.const.ACTCTX_FLAG_ASSEMBLY_DIRECTORY_VALID), lpSource='shell32.dll',
                    lpAssemblyDirectory=buff, lpResourceName=ctyped.macro.MAKEINTRESOURCEW(124))
                cookie = ctyped.type.ULONG_PTR()
                return bool(ctyped.lib.Kernel32.ActivateActCtx(
                    ctyped.lib.Kernel32.CreateActCtxW(ctyped.byref(ctx)), ctyped.byref(cookie)))
    return False


if __name__ == '__main__':
    # tst()
    # print(_enable_visual_styles())
    _test_sys_tray()
    # _test_()
    # _wait()
    sys.exit()
