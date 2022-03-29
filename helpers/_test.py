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
import typing
from typing import Any, Callable, Generator, Iterable, Mapping, Union
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
EVENT_CLOSE = ctyped.const.WM_CLOSE


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


_WM_TASKBAR_CREATED = ctyped.lib.User32.RegisterWindowMessageW('TaskbarCreated')


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
    _binds: dict[int, dict[int, tuple[Callable, Iterable, Mapping]]] = {0: {}}
    _class = None
    _flags = ctyped.const.NIF_MESSAGE | ctyped.const.NIF_ICON | ctyped.const.NIF_TIP
    _frames = None
    _hicon = None
    _hwnd = None
    _shown = False
    _to_del = True
    _uid_gen = itertools.count(1)
    _selves: dict[int, SysTray] = {}

    def __new__(cls, *args, **kwargs):
        if not cls._hwnd:
            hinstance = ctyped.lib.Kernel32.GetModuleHandleW(None)
            cls._class = ctyped.struct.WNDCLASSEXW(
                ctyped.sizeof(ctyped.struct.WNDCLASSEXW), lpfnWndProc=ctyped.type.WNDPROC(cls._callback),
                hInstance=hinstance, lpszClassName=f'{NAME}-{cls.__name__}')
            ctyped.lib.User32.RegisterClassExW(ctyped.byref(cls._class))
            cls._hwnd = ctyped.lib.User32.CreateWindowExW(0, cls._class.lpszClassName, None, ctyped.const.WS_OVERLAPPED,
                                                          0, 0, 0, 0, None, None, hinstance, None)
        return super().__new__(cls)

    def __init__(self, icon: Optional[Union[str, int]] = None, tooltip: Optional[str] = None):
        self._uid = next(self._uid_gen)
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
                ctyped.lib.User32.DestroyWindow(self._hwnd)
                ctyped.lib.User32.UnregisterClassW(self._class.lpszClassName,
                                                   ctyped.lib.Kernel32.GetModuleHandleW(None))
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
            ctyped.lib.User32.PostQuitMessage(0)
        elif message == ctyped.const.WM_CLOSE:
            try:
                cls._call(0, message)
            finally:
                ctyped.lib.User32.DestroyWindow(hwnd)
        elif message == ctyped.const.WM_QUERYENDSESSION:
            ...
        elif message == ctyped.const.WM_APP:
            cls._call(wparam, lparam)
        elif message == _WM_TASKBAR_CREATED:
            for self in cls._selves.values():
                # noinspection PyUnresolvedReferences
                self._update()
        else:
            return ctyped.lib.User32.DefWindowProcW(hwnd, message, wparam, lparam)
        return 0

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
        while ctyped.lib.User32.GetMessageW(msg_ref, cls._hwnd, 0, 0) > 0:
            ctyped.lib.User32.TranslateMessage(msg_ref)
            ctyped.lib.User32.DispatchMessageW(msg_ref)
        return msg.wParam

    @classmethod
    def exit_mainloop(cls) -> bool:
        return not ctyped.lib.User32.SendMessageW(cls._hwnd, ctyped.const.WM_CLOSE, 0, 0)

    @property
    def shown(self) -> bool:
        return self._shown

    def _set_hicon(self, hicon: Optional[ctyped.type.HICON] = None) -> bool:
        self._data.hIcon = hicon
        return self._update()

    def set_icon(self, res_or_path: Union[int, str]) -> bool:
        self.stop_animation()
        if isinstance(res_or_path, str):
            self._hicon = _gdiplus.Bitmap.from_file(res_or_path).get_hicon()
        else:
            self._hicon = ctyped.handle.HICON.from_res(res_or_path)
        self._set_hicon(self._hicon)
        return bool(self._hicon)

    def set_tooltip(self, text: str) -> bool:
        self._data.szTip = text
        return self._update()

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


class ItemKind:
    SEPARATOR = 0
    STRING = 1
    CHECK = 2
    RADIO = 3
    BITMAP = 4
    SUBMENU = 5


class MenuItem:
    _id_gen = itertools.count(1)

    # noinspection PyShadowingBuiltins
    def __init__(self, menu: Menu, id: Optional[int] = None):
        self._menu = menu
        self._id = next(self._id_gen) if id is None else id

    def __eq__(self, other: MenuItem):
        return self._menu == other._menu and self._id == other._id

    def get_menu(self) -> Menu:
        return self._menu

    def get_id(self) -> int:
        return self._id

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


class Menu:
    _mim_field = {
        ctyped.const.MIM_BACKGROUND: 'hbrBack',
        ctyped.const.MIM_HELPID: 'dwContextHelpID',
        ctyped.const.MIM_MAXHEIGHT: 'cyMax',
        ctyped.const.MIM_STYLE: 'dwStyle'}
    _miim_fields = {
        ctyped.const.MIIM_STATE: ('fState',),
        ctyped.const.MIIM_ID: ('wID',),
        ctyped.const.MIIM_SUBMENU: ('hSubMenu',),
        ctyped.const.MIIM_CHECKMARKS: ('hbmpChecked', 'hbmpUnchecked'),
        ctyped.const.MIIM_TYPE: ('fType', 'dwTypeData'),
        ctyped.const.MIIM_DATA: ('dwItemData',),
        ctyped.const.MIIM_STRING: ('dwTypeData', 'cch'),
        ctyped.const.MIIM_BITMAP: ('hbmpItem',),
        ctyped.const.MIIM_FTYPE: ('fType',)}

    def __init__(self):
        self._hmenu = ctyped.handle.HMENU.from_type()

    def __eq__(self, other: Menu):
        return self._hmenu == other._hmenu

    def __contains__(self, id_or_item: Union[int, MenuItem]):
        return self.get_item_pos(id_or_item) != -1

    def __len__(self):
        return self.get_count()

    @typing.overload
    def __getitem__(self, pos: int) -> MenuItem:
        pass

    @typing.overload
    def __getitem__(self, pos: slice) -> tuple[MenuItem]:
        pass

    def __getitem__(self, pos):
        return tuple(self)[pos]

    def __delitem__(self, pos_or_item: Union[int, slice, MenuItem]) -> bool:
        if isinstance(pos_or_item, slice):
            deleted = True
            for item in self[pos_or_item]:
                deleted = self.__delitem__(item) and deleted
            return deleted
        else:
            return self.remove(pos_or_item, True)

    def __iter__(self) -> MenuItem:
        for pos in range(len(self)):
            yield self.get(pos, by_pos=True)

    @classmethod
    def _from_hmenu(cls, hmenu: ctyped.type.HMENU) -> Menu:
        menu = cls.__new__(cls)
        menu._hmenu = ctyped.handle.HMENU(hmenu)
        return menu

    def get_count(self) -> int:
        return self._hmenu.get_item_count()

    def get(self, id_or_pos: int, default: Any = None, by_pos: bool = False) -> MenuItem:
        if by_pos:
            return default if (id_ := self.get_item_id(id_or_pos)) == -1 else MenuItem(self, id_)
        else:
            return MenuItem(self, id_or_pos) if id_or_pos in self else default

    def _append(self, id_or_item: Union[int, MenuItem]) -> bool:
        if isinstance(id_or_item, MenuItem):
            id_or_item = id_or_item.get_id()
        return bool(ctyped.lib.User32.AppendMenuW(self._hmenu, ctyped.const.MF_STRING, id_or_item, None))

    def append(self, text: str = '', image: Optional = None, submenu: Optional[Menu] = None,
               enable: bool = True, highlight: bool = False, check: Optional[bool] = None,
               default: bool = False, kind: int = ItemKind.STRING) -> Optional[MenuItem]:
        item = MenuItem(self)
        if self._append(item.get_id()):
            item.set_text(text)
            item.set_states(enable, highlight, check, default)
            return item

    def remove(self, id_or_pos_or_item: Union[int, MenuItem], by_pos: bool = False) -> bool:
        if isinstance(id_or_pos_or_item, MenuItem):
            id_or_pos_or_item = id_or_pos_or_item.get_id()
            by_pos = False
        return bool(ctyped.lib.User32.RemoveMenu(self._hmenu, id_or_pos_or_item,
                                                 ctyped.const.MF_BYPOSITION if by_pos else ctyped.const.MF_BYCOMMAND))

    def clear(self) -> bool:
        return self.__delitem__(slice(None))

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

    def get_item_id(self, pos_or_item: int) -> int:
        return info[0] if (info := self._get_item_info(pos_or_item, ctyped.const.MIIM_ID, True)) else -1

    def get_item_states(self, id_or_pos_or_item: Union[int, MenuItem],
                        by_pos: bool = False) -> tuple[bool, bool, bool, bool]:
        state = info[0] if (info := self._get_item_info(id_or_pos_or_item, ctyped.const.MIIM_STATE, by_pos)) else -1
        return (ctyped.const.MFS_ENABLED == state & (ctyped.const.MF_GRAYED | ctyped.const.MFS_DISABLED),
                ctyped.const.MFS_HILITE == state & ctyped.const.MFS_HILITE,
                ctyped.const.MFS_CHECKED == state & ctyped.const.MFS_CHECKED,
                ctyped.const.MFS_DEFAULT == state & ctyped.const.MFS_DEFAULT)

    def is_item_enabled(self, id_or_pos_or_item: Union[int, MenuItem], by_pos: bool = False) -> bool:
        return self.get_item_states(id_or_pos_or_item, by_pos)[0]

    def is_item_highlighted(self, id_or_pos_or_item: Union[int, MenuItem], by_pos: bool = False) -> bool:
        return self.get_item_states(id_or_pos_or_item, by_pos)[1]

    def is_item_checked(self, id_or_pos_or_item: Union[int, MenuItem], by_pos: bool = False) -> bool:
        return self.get_item_states(id_or_pos_or_item, by_pos)[2]

    def is_item_default(self, id_or_pos_or_item: Union[int, MenuItem], by_pos: bool = False) -> bool:
        return self.get_item_states(id_or_pos_or_item, by_pos)[3]

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
            return self._from_hmenu(info[0])

    def get_item_pos(self, id_or_item: Union[int, MenuItem]) -> int:
        if isinstance(id_or_item, MenuItem):
            id_or_item = id_or_item.get_id() if id_or_item.get_menu() is self else -1
        if id_or_item != -1:
            for pos, item in enumerate(self):
                if id_or_item == item.get_id():
                    return pos
        return -1

    def _set_item_info(self, id_or_pos_or_item: Union[int, MenuItem],
                       infos: Iterable, miim: int, by_pos: bool) -> bool:
        if isinstance(id_or_pos_or_item, MenuItem):
            id_or_pos_or_item = id_or_pos_or_item.get_id()
            by_pos = False
        item_info = ctyped.struct.MENUITEMINFOW(ctyped.sizeof(ctyped.struct.MENUITEMINFOW), miim)
        for field, info in zip(self._miim_fields[miim], infos):
            setattr(item_info, field, info)
        return bool(ctyped.lib.User32.SetMenuItemInfoW(self._hmenu, id_or_pos_or_item, by_pos, ctyped.byref(item_info)))

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

    def check_item(self, id_or_pos_or_item: Union[int, MenuItem], check: bool = True, by_pos: bool = False) -> bool:
        return self.set_item_states(id_or_pos_or_item, check=check, by_pos=by_pos)

    def set_default_item(self, id_or_pos_or_item: Union[int, MenuItem],
                         default: bool = True, by_pos: bool = False) -> bool:
        return self.set_item_states(id_or_pos_or_item, default=default, by_pos=by_pos)

    def set_item_text(self, id_or_pos_or_item: Union[int, MenuItem], text: str, by_pos: bool = False) -> bool:
        return self._set_item_info(id_or_pos_or_item, (ctyped.const.MIIM_STRING, text), ctyped.const.MIIM_TYPE, by_pos)

    def set_item_submenu(self, id_or_pos_or_item: Union[int, MenuItem], submenu: Menu, by_pos: bool = False) -> bool:
        return self._set_item_info(id_or_pos_or_item, (submenu._hmenu,), ctyped.const.MIIM_SUBMENU, by_pos)


def _foo(s: SysTray, e, menu: Menu, item: MenuItem):
    # s.show_balloon('very busy', 'mini text', Icon.USER)
    # s.set_animation(r'D:\Projects\Wallpyper\src\resources\busy.gif')
    # print(item.is_enabled())
    # print(item.is_highlighted())
    # print(item.is_checked())
    # print(item.is_default())
    p = ctyped.struct.POINT()
    ctyped.lib.User32.GetCursorPos(ctyped.byref(p))
    # print(ctyped.lib.User32.SetForegroundWindow(s._hwnd))
    ctyped.lib.User32.TrackPopupMenuEx(menu._hmenu, ctyped.const.TPM_TOPALIGN | ctyped.const.TPM_LEFTALIGN,
                                       p.x, p.y, s._hwnd, None)
    return 0


def _foo2(s, e):
    print(s.exit_mainloop())  # s.set_icon(r'E:\Projects\wallpyper\icon.ico')  # s.stop_animation()


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
    with _utils.string_buffer(ctyped.const.MAX_PATH) as buff:
        ctyped.lib.UxTheme.GetCurrentThemeName(buff, ctyped.const.MAX_PATH, None, 0, None, 0)
        print(buff.value)
    htheme = ctyped.lib.UxTheme.GetWindowTheme(s._hwnd)
    print(htheme)
    if htheme:
        with _utils.string_buffer(ctyped.const.MAX_PATH) as buff:
            ctyped.lib.UxTheme.GetThemeSysString(htheme, ctyped.const.TMT_XMLNAME, buff, ctyped.const.MAX_PATH)
            print(buff.value)
    menu = Menu()
    menu.append('dump')
    ctyped.lib.User32.SetMenu(s._hwnd, menu._hmenu)
    item = menu.append('text', check=True)
    # print(item.get_id(), menu.get_item_id(item))
    item.set_text('text2')
    menu2 = Menu()
    it = menu2.append('gg')
    menu2.append('69')
    menu2.append('new')
    print(menu.set_item_submenu(item, menu2))
    s.bind(Event.RIGHT_UP, _foo, (menu, item))
    s.bind(Event.LEFT_DOUBLE, _foo2)
    # _foo3(Event.MOVE, Event.LEFT_DOWN, Event.LEFT_UP, Event.RIGHT_DOWN, Event.BALLOON_HIDDEN)
    s.bind(Event.BALLOON_QUEUED, lambda *args: print('shown'))
    s.bind(Event.BALLOON_HIDDEN - 1, lambda *args: print('show_balloon hide'))
    s.bind(Event.BALLOON_CLICK, lambda *args: print('show_balloon click'))
    s.bind(ctyped.const.NIN_SELECT, lambda *args: print('sel'))
    s.show()
    # p2 = r'D:\Projects\wallpyper\src\resources\icon.ico'
    # s2 = SysTray(p2, 'no tip')
    # s2.bind(Event.LEFT_DOUBLE, lambda *args: print('2nd'))
    # s2.bind(Event.RIGHT_UP, lambda *args: s2.hide())
    # s2.show()
    # _foo()
    # s2.mainloop()
    SysTray.mainloop()


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
