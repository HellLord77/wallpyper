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
from typing import Any, Callable, Generator, Iterable, Mapping, Union, Sequence
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


_WM_TASKBAR_CREATE = ctyped.lib.User32.RegisterWindowMessageW('TaskbarCreated')
_WM_SYS_TRAY_TRIGGER = ctyped.const.WM_APP


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

    BALLOON_QUEUED = ctyped.const.NIN_BALLOONSHOW
    BALLOON_HIDDEN = ctyped.const.NIN_BALLOONTIMEOUT
    BALLOON_CLICK = ctyped.const.NIN_BALLOONUSERCLICK

    MENU_ITEM_HOVER = ctyped.const.WM_MENUSELECT
    MENU_ITEM_CLICK = ctyped.const.WM_MENUCOMMAND


class Icon:
    NONE = ctyped.const.NIIF_NONE
    INFO = ctyped.const.NIIF_INFO
    WARNING = ctyped.const.NIIF_WARNING
    ERROR = ctyped.const.NIIF_ERROR
    USER = ctyped.const.NIIF_USER


class Gui:
    _binds = {}
    _selves = {}

    _hinstance = ctyped.lib.Kernel32.GetModuleHandleW(None)
    _mainloop_running = False

    def __init__(self, name: Optional[str] = None):
        self._class = ctyped.struct.WNDCLASSEXW(
            ctyped.sizeof(ctyped.struct.WNDCLASSEXW), lpfnWndProc=ctyped.type.WNDPROC(self._wnd_proc),
            hInstance=self._hinstance, lpszClassName=f'{NAME}-{type(self).__name__}' if name is None else name)
        ctyped.lib.User32.RegisterClassExW(ctyped.byref(self._class))
        self._hwnd = ctyped.lib.User32.CreateWindowExW(0, self._class.lpszClassName, None, ctyped.const.WS_OVERLAPPED,
                                                       0, 0, 0, 0, None, None, self._hinstance, None)
        self._attached = []
        self._binds[self._hwnd] = {}
        self._selves[self._hwnd] = self
        atexit.register(self.destroy)

    def destroy(self):
        atexit.unregister(self.destroy)
        del self._selves[self._hwnd]
        del self._binds[self._hwnd]
        while self._attached:
            self._attached.pop().destroy()
        ctyped.lib.User32.DestroyWindow(self._hwnd)
        ctyped.lib.User32.UnregisterClassW(self._class.lpszClassName, self._hinstance)

    @classmethod
    def _wnd_proc(cls, hwnd: ctyped.type.HWND, message: ctyped.type.UINT,
                  wparam: ctyped.type.WPARAM, lparam: ctyped.type.LPARAM) -> ctyped.type.LRESULT:
        if message == ctyped.const.WM_DESTROY:
            ctyped.lib.User32.PostQuitMessage(0)
        elif message == ctyped.const.WM_CLOSE:
            ctyped.lib.User32.DestroyWindow(hwnd)
        elif message == ctyped.const.WM_QUERYENDSESSION:
            ...
        elif message == ctyped.const.WM_DISPLAYCHANGE:
            cls._selves[hwnd].trigger(message)
        elif message == _WM_SYS_TRAY_TRIGGER:
            SysTray.trigger(wparam, lparam)
        elif message == _WM_TASKBAR_CREATE:
            # noinspection PyProtectedMember
            for sys_tray in SysTray._selves.values():
                sys_tray.update()
        elif message in (ctyped.const.WM_MENUSELECT, ctyped.const.WM_MENUCOMMAND):
            if lparam:
                Menu.trigger(Menu.__new__(Menu, lparam), ctyped.macro.LOWORD(wparam), message,
                             message == ctyped.const.WM_MENUCOMMAND or ctyped.const.MF_POPUP == ctyped.macro.HIWORD(
                                 wparam) & ctyped.const.MF_POPUP)
        else:
            return ctyped.lib.User32.DefWindowProcW(hwnd, message, wparam, lparam)
        return 0

    @classmethod
    def get(cls) -> Optional[Gui]:
        with contextlib.suppress(StopIteration):
            return next(reversed(cls._selves.values()))

    @classmethod
    def attach(cls, obj, gui: Optional[Gui]) -> ctyped.type.HWND:
        if gui is None:
            gui = cls.get()
            if gui is None:
                raise RuntimeError(f"No instance of '{cls.__name__}' created yet")
        gui._attached.append(obj)
        return gui._hwnd

    def bind(self, event: int, callback: Callable, args: Optional[Iterable] = None, kwargs: Optional[Mapping] = None):
        self._binds[self._hwnd][event] = callback, () if args is None else args, {} if kwargs is None else kwargs

    def unbind(self, event: int) -> bool:
        try:
            del self._binds[self._hwnd][event]
        except KeyError:
            return False
        else:
            return True

    def trigger(self, event: int) -> Any:
        try:
            callback, args, kwargs = self._binds[self._hwnd][event]
        except KeyError:
            pass
        else:
            return callback(event, self, *args, **kwargs)

    def mainloop(self) -> int:
        self._mainloop_running = True
        msg = ctyped.struct.MSG()
        msg_ref = ctyped.byref(msg)
        while ctyped.lib.User32.GetMessageW(msg_ref, self._hwnd, 0, 0) > 0:
            ctyped.lib.User32.TranslateMessage(msg_ref)
            ctyped.lib.User32.DispatchMessageW(msg_ref)
        self._mainloop_running = False
        return msg.wParam

    def exit_mainloop(self) -> bool:
        return not ctyped.lib.User32.SendMessageW(self._hwnd, ctyped.const.WM_CLOSE, 0, 0)


class SysTray:
    _hwnd = None
    _binds = {}
    _selves: dict[int, SysTray] = {}

    _id_gen = itertools.count(1)
    _flags = ctyped.const.NIF_MESSAGE | ctyped.const.NIF_ICON | ctyped.const.NIF_TIP
    _frames = None
    _hicon = None
    _shown = False

    def __init__(self, icon: Union[int, str] = ctyped.const.IDI_APPLICATION,
                 tooltip: Optional[str] = None, gui: Optional[Gui] = None):
        self._hwnd = Gui.attach(self, gui)
        self._id = next(self._id_gen)
        self._data = ctyped.struct.NOTIFYICONDATAW(ctyped.sizeof(ctyped.struct.NOTIFYICONDATAW),
                                                   self._hwnd, self._id, self._flags, _WM_SYS_TRAY_TRIGGER)
        self.set_icon(icon)
        if tooltip is not None:
            self.set_tooltip(tooltip)
        self._on_timer = ctyped.type.TIMERPROC(self._next_frame)
        self._binds[self._id] = {}
        self._selves[self._id] = self

    def destroy(self):
        del self._selves[self._id]
        del self._binds[self._id]
        self.hide()

    # noinspection PyShadowingBuiltins
    @classmethod
    def trigger(cls, id: int, event: int) -> Any:
        try:
            callback, args, kwargs = cls._binds[id][event]
        except KeyError:
            # print(id, event)
            pass
        else:
            return callback(event, cls._selves[id], *args, **kwargs)

    @property
    def shown(self) -> bool:
        return self._shown

    def _set_hicon(self, hicon: Optional[ctyped.type.HICON] = None) -> bool:
        self._data.hIcon = hicon
        return self.update()

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
        return self.update()

    def _next_frame(self, *_):
        delay, hicon = next(self._frames)
        self._set_hicon(hicon)
        ctyped.lib.User32.SetTimer(self._hwnd, 0, delay, self._on_timer)

    def set_animation(self, gif_path: str):
        self.stop_animation()
        self._frames = itertools.cycle(_get_gif_frames(gif_path))
        self._next_frame()

    def stop_animation(self):
        ctyped.lib.User32.KillTimer(self._hwnd, 0)
        self._set_hicon(self._hicon)
        self._frames = None

    def update(self, show: bool = False) -> bool:
        updated = False
        if show or self._shown:
            updated = bool(ctyped.lib.Shell32.Shell_NotifyIconW(ctyped.const.NIM_MODIFY, ctyped.byref(
                self._data)) or ctyped.lib.Shell32.Shell_NotifyIconW(ctyped.const.NIM_ADD, ctyped.byref(self._data)))
            if show:
                self._shown = updated
        return updated

    def show(self) -> bool:
        return self.update(True)

    def hide(self) -> bool:
        self._shown = not bool(ctyped.lib.Shell32.Shell_NotifyIconW(ctyped.const.NIM_DELETE, ctyped.byref(self._data)))
        return not self._shown

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

    def bind(self, event: int, callback: Callable,
             args: Optional[Iterable] = None, kwargs: Optional[Mapping[str, Any]] = None):
        self._binds[self._id][event] = callback, () if args is None else args, {} if kwargs is None else kwargs

    def unbind(self, event: int) -> bool:
        try:
            del self._binds[self._id][event]
        except KeyError:
            return False
        else:
            return True


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


class MenuItem:
    _id_gen = itertools.count(1)

    # noinspection PyShadowingBuiltins
    def __init__(self, menu: Menu, id: Optional[int] = None):
        self._menu = menu
        self._id = next(self._id_gen) if id is None else id
        self._hbmps: list[Optional[ctyped.handle.HBITMAP]] = [None] * 3

    def __eq__(self, other: MenuItem):
        return self._menu == other._menu and self._id == other._id

    def get_menu(self) -> Menu:
        return self._menu

    def get_id(self) -> int:
        return self._id

    def get_pos(self) -> int:
        return self._menu.get_item_pos(self._id)

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

    def bind(self, event: int, callback: Callable, args: Optional[Iterable] = None, kwargs: Optional[Mapping] = None):
        self._menu.bind_item(self._id, event, callback, args, kwargs)

    def unbind(self, event: int) -> bool:
        return self._menu.unbind_item(self._id, event)

    def trigger(self, event: int) -> Any:
        return self._menu.trigger_item(self._id, event)


class Menu:
    _hwnd = None
    _binds = {}
    _selves: dict[int, Menu] = {}

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

    def __new__(cls, hmenu: Optional[ctyped.type.HMENU] = None, *_, **__):
        if hmenu is not None and (self := cls._selves.get(int(hmenu))) is not None:
            return self
        return super().__new__(cls)

    def __init__(self, hmenu: Optional[ctyped.type.HMENU] = None, gui: Optional[Gui] = None):
        self._hwnd = Gui.attach(self, gui)
        self._hmenu = ctyped.handle.HMENU.from_type() if hmenu is None else hmenu
        ctyped.lib.User32.SetMenuInfo(self._hmenu, ctyped.byref(ctyped.struct.MENUINFO(
            ctyped.sizeof(ctyped.struct.MENUINFO), ctyped.const.MIM_STYLE, ctyped.const.MNS_NOTIFYBYPOS)))
        self._hmenu.set_hwnd(self._hwnd)
        self._binds[self._hmenu.value] = {}
        self._selves[self._hmenu.value] = self
        self._items = []

    def __eq__(self, other: Menu):
        return self._hmenu == other._hmenu

    def __contains__(self, id_or_item: Union[int, MenuItem]):
        return id_or_item in self._items if isinstance(id_or_item, MenuItem) else self.get(id_or_item) is not None

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

    def destroy(self):
        del self._selves[self._hmenu.value]
        del self._binds[self._hmenu.value]
        del self._hmenu

    @classmethod
    def trigger(cls, menu: Menu, id_or_pos_or_item: Union[int, MenuItem], event: int, by_pos: bool = False) -> Any:
        if not isinstance(id_or_pos_or_item, MenuItem):
            id_or_pos_or_item = menu.get(id_or_pos_or_item, by_pos=by_pos)
        try:
            callback, args, kwargs = cls._binds[menu._hmenu.value][id_or_pos_or_item.get_id()][event]
        except KeyError:
            pass
        else:
            return callback(event, id_or_pos_or_item, *args, **kwargs)

    def _update(self):
        self._items = []
        for pos in range(self.get_count()):
            item = self.get(id_ := self.get_item_id(pos))
            self._items.append(MenuItem(self, id_) if item is None else item)

    def get_count(self) -> int:
        return self._hmenu.get_item_count()

    def get(self, id_or_pos: int, default: Any = None, by_pos: bool = False) -> MenuItem:
        if by_pos:
            with contextlib.suppress(IndexError):
                return self[id_or_pos]
        else:
            for item in self:
                if id_or_pos == item.get_id():
                    return item
        return default

    def append(self, text: str = '', image: Optional = None, submenu: Optional[Menu] = None,
               enable: bool = True, highlight: bool = False, check: Optional[bool] = None,
               default: bool = False, kind: int = _MenuItemKind.STRING) -> Optional[MenuItem]:
        return self.insert(self.get_count(), text, image, submenu, enable, highlight, check, default, kind)

    def insert(self, pos: int, text: str = '', image: Optional = None, submenu: Optional[Menu] = None,
               enable: bool = True, highlight: bool = False, check: Optional[bool] = None,
               default: bool = False, kind: int = _MenuItemKind.STRING) -> Optional[MenuItem]:
        item = MenuItem(self)
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
        item_info.cbSize = ctyped.sizeof(ctyped.struct.MENUITEMINFOW)
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
            return type(self)(ctyped.handle.HMENU(info[0]))

    def _set_item_info(self, id_or_pos_or_item: Union[int, MenuItem],
                       infos: Iterable, miim: int, by_pos: bool) -> bool:
        if isinstance(id_or_pos_or_item, MenuItem):
            id_or_pos_or_item = id_or_pos_or_item.get_id()
            by_pos = False
        item_info = ctyped.struct.MENUITEMINFOW(ctyped.sizeof(ctyped.struct.MENUITEMINFOW), miim)
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
        if not isinstance(id_or_pos_or_item, MenuItem):
            id_or_pos_or_item = self.get(id_or_pos_or_item, by_pos=by_pos)
        try:
            binds = self._binds[self._hmenu.value][id_or_pos_or_item.get_id()]
        except KeyError:
            binds = self._binds[self._hmenu.value][id_or_pos_or_item.get_id()] = {}
        binds[event] = callback, () if args is None else args, {} if kwargs is None else kwargs

    def unbind_item(self, id_or_pos_or_item: Union[int, MenuItem], event: int, by_pos: bool = False) -> bool:
        if by_pos or isinstance(id_or_pos_or_item, MenuItem):
            id_or_pos_or_item = self.get_item_id(id_or_pos_or_item)
        try:
            del self._binds[self._hmenu.value][id_or_pos_or_item][event]
        except KeyError:
            return False
        else:
            return True

    def trigger_item(self, id_or_pos_or_item: Union[int, MenuItem], event: int, by_pos: bool = False) -> Any:
        return self.trigger(self, id_or_pos_or_item, event, by_pos)

    def show(self, pos: Optional[Sequence[int, int]] = None, timeout: Optional[float] = None) -> bool:
        if timeout is None:
            timer = None
        else:
            timer = threading.Timer(timeout, self.hide)
            timer.start()
        try:
            return bool(self._hmenu.track(pos))
        finally:
            if timer is not None:
                timer.cancel()

    def hide(self) -> bool:
        return self._hmenu.untrack(self._hwnd)


def _foo(e, s: SysTray, menu: Menu, item: MenuItem):
    # s.show_balloon('very busy', 'mini text', Icon.USER)
    # s.set_animation(r'D:\Projects\Wallpyper\src\resources\busy.gif')
    menu.show()
    return 0


def _foo2(s, e):
    print(Gui.get().exit_mainloop())  # s.set_icon(r'E:\Projects\wallpyper\icon.ico')  # s.stop_animation()


def _wait():
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass


def test_cb(*args):
    print('test_cb', args)


def _test_sys_tray():
    p = r'D:\Projects\wallpyper\src\resources\tray.png'
    # bind(EVENT_CLOSE, lambda *args: print(6969))
    g = Gui()
    s = SysTray(p, 'tip')
    menu = Menu()
    it = menu.append('dump')
    it.set_right_ordered()
    it.bind(Event.MENU_ITEM_CLICK, test_cb)
    # print(menu.set_item_image(it, p))
    # ctyped.lib.User32.SetMenu(s._hwnd, menu._hmenu)
    item = menu.append('text', check=True)
    # print(item.get_id(), menu.get_item_id(item))
    item.set_text('text2\ntooltip')
    menu2 = Menu()
    menu2.append('gg')
    it7 = menu2.append('69')
    it7.bind(Event.MENU_ITEM_HOVER, lambda *args: print('hover', args))
    menu2.append('new')
    # print(item.set_image(r'D:\Projects\wallpyper\src\resources\tray.png', True))
    menu.set_item_submenu(item, menu2)
    g.bind(Event.DISPLAY_CHANGE, lambda *args: print('display', args))

    s.bind(Event.SYS_TRAY_RIGHT_UP, _foo, (menu, item))
    s.bind(Event.SYS_TRAY_LEFT_DOUBLE, _foo2)
    s.bind(Event.BALLOON_QUEUED, lambda *args: print('shown'))
    s.bind(Event.BALLOON_HIDDEN - 1, lambda *args: print('show_balloon hide'))
    s.bind(Event.BALLOON_CLICK, lambda *args: print('show_balloon click'))
    s.bind(ctyped.const.NIN_SELECT, lambda *args: print('sel'))
    s.show()
    # p2 = r'D:\Projects\wallpyper\src\resources\icon.ico'
    # s2 = SysTray(p2, 'no tip')
    # s2.bind(Event.SYS_TRAY_LEFT_DOUBLE, lambda *args: print('2nd'))
    # s2.bind(Event.RIGHT_UP, lambda *args: s2.hide())
    # s2.show()
    # _foo()
    # s2.mainloop()
    g.mainloop()
    g.destroy()


def _test_():
    info = ctyped.struct.SHELLEXECUTEINFOW(ctyped.sizeof(ctyped.struct.SHELLEXECUTEINFOW), lpVerb='open',
                                           lpFile='ms-settings:mobile-devices', nShow=ctyped.const.SW_NORMAL)
    print(ctyped.lib.Shell32.ShellExecuteExW(ctyped.byref(info)))


def tst():
    try:
        return 69
    finally:
        raise TypeError


if __name__ == '__main__':
    # tst()
    _test_sys_tray()
    # _test()
    # _wait()
    sys.exit()
