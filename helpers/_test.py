from __future__ import annotations as _

__version__ = '0.0.1'

import atexit
import collections
import contextlib
import io
import itertools
import sys
import threading
import time
import tkinter.messagebox
from typing import Any, Callable, Iterable, Mapping, Union, Sequence, Generator
from typing import Optional

import libs.ctyped as ctyped
import win32
import win32._gdiplus as _gdiplus
import win32._utils as _utils

NOTIFYICONDATAA_V1_SIZE = ctyped.macro.FIELD_OFFSET(ctyped.struct.NOTIFYICONDATAA, 'szTip', 64)
NOTIFYICONDATAW_V1_SIZE = ctyped.macro.FIELD_OFFSET(ctyped.struct.NOTIFYICONDATAW, 'szTip', 64)
NOTIFYICONDATAA_V2_SIZE = ctyped.macro.FIELD_OFFSET(ctyped.struct.NOTIFYICONDATAA, 'guidItem')
NOTIFYICONDATAW_V2_SIZE = ctyped.macro.FIELD_OFFSET(ctyped.struct.NOTIFYICONDATAW, 'guidItem')
NOTIFYICONDATAA_V3_SIZE = ctyped.macro.FIELD_OFFSET(ctyped.struct.NOTIFYICONDATAA, 'hBalloonIcon')
NOTIFYICONDATAW_V3_SIZE = ctyped.macro.FIELD_OFFSET(ctyped.struct.NOTIFYICONDATAW, 'hBalloonIcon')


def exception_handler(excepthook: Callable, *args, **kwargs):
    stderr = sys.stderr
    sys.stderr = io.StringIO()
    excepthook(*args, **kwargs)
    sys.stderr.seek(0)
    root = tkinter.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    while not isinstance(args, type):
        args = args[0]
    tkinter.messagebox.showerror(args.__name__, sys.stderr.read())
    root.destroy()
    sys.stderr = stderr


# sys.excepthook = types.MethodType(exception_handler, sys.excepthook)
# threading.excepthook = types.MethodType(exception_handler, threading.excepthook)

NAME = f'{__name__}-{__version__}'
MENU_ITEM_TOOLTIP_DELAY = ctyped.lib.User32.GetDoubleClickTime() * 3


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
_WM_MENU_ITEM_TOOLTIP_HIDE = ctyped.const.WM_APP + 1

_TID_MENU_ITEM_TOOLTIP = 0

_MIM_FIELD = {
    ctyped.const.MIM_BACKGROUND: 'hbrBack',
    ctyped.const.MIM_HELPID: 'dwContextHelpID',
    ctyped.const.MIM_MAXHEIGHT: 'cyMax',
    ctyped.const.MIM_STYLE: 'dwStyle'}
_MIIM_FIELDS = {
    ctyped.const.MIIM_STATE: ('fState',),
    ctyped.const.MIIM_ID: ('wID',),
    ctyped.const.MIIM_SUBMENU | ctyped.const.MIIM_TYPE: ('hSubMenu', 'dwTypeData'),
    ctyped.const.MIIM_CHECKMARKS: ('hbmpChecked', 'hbmpUnchecked'),
    ctyped.const.MIIM_TYPE: ('fType', 'dwTypeData'),
    ctyped.const.MIIM_DATA: ('dwItemData',),
    ctyped.const.MIIM_STRING: ('dwTypeData', 'cch'),
    ctyped.const.MIIM_BITMAP: ('hbmpItem',),
    ctyped.const.MIIM_FTYPE: ('fType',)}


class GuiEvent:
    DISPLAY_CHANGE = ctyped.const.WM_DISPLAYCHANGE


class SystemTrayIcon:
    NONE = ctyped.const.NIIF_NONE
    INFO = ctyped.const.NIIF_INFO
    WARNING = ctyped.const.NIIF_WARNING
    ERROR = ctyped.const.NIIF_ERROR
    TRAY = ctyped.const.NIIF_USER


class SystemTrayEvent:
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

    BALLOON_SHOW = ctyped.const.NIN_BALLOONSHOW
    BALLOON_HIDE = ctyped.const.NIN_BALLOONTIMEOUT
    BALLOON_CLICK = ctyped.const.NIN_BALLOONUSERCLICK


class MenuBackgroundColor:
    FACE_3D = ctyped.const.COLOR_3DFACE
    ACTIVE_CAPTION = ctyped.const.COLOR_ACTIVECAPTION
    BUTTON_TEXT = ctyped.const.COLOR_BTNTEXT
    GRAY_TEXT = ctyped.const.COLOR_GRAYTEXT
    HIGHLIGHT = ctyped.const.COLOR_HIGHLIGHT
    HIGHLIGHT_TEXT = ctyped.const.COLOR_HIGHLIGHTTEXT
    HOT_LIGHT = ctyped.const.COLOR_HOTLIGHT
    WINDOW_TEXT = ctyped.const.COLOR_WINDOWTEXT


class MenuEvent:
    SHOW = ctyped.const.WM_INITMENUPOPUP
    HIDE = ctyped.const.WM_UNINITMENUPOPUP


class MenuItemType:
    NORMAL = -1
    SEPARATOR = 0
    CHECK = 1
    RADIO = 2


class MenuItemImage:
    CLOSE = ctyped.const.HBMMENU_POPUP_CLOSE
    RESTORE = ctyped.const.HBMMENU_POPUP_RESTORE
    MINIMIZE = ctyped.const.HBMMENU_POPUP_MINIMIZE
    MAXIMIZE = ctyped.const.HBMMENU_POPUP_MAXIMIZE


class MenuItemTooltipIcon:
    NONE = ctyped.const.TTI_NONE
    INFO = ctyped.const.TTI_INFO
    WARNING = ctyped.const.TTI_WARNING
    ERROR = ctyped.const.TTI_ERROR
    INFO_LARGE = ctyped.const.TTI_INFO_LARGE
    WARNING_LARGE = ctyped.const.TTI_WARNING_LARGE
    ERROR_LARGE = ctyped.const.TTI_ERROR_LARGE


class MenuItemEvent:
    HIGHLIGHT = ctyped.const.WM_MENUSELECT
    LEFT_UP = ctyped.const.WM_MENUCOMMAND
    RIGHT_UP = ctyped.const.WM_MENURBUTTONUP


class _IDGenerator:
    def __init__(self, start: int = 1):
        self._start = self._last = start - 1
        self._generator = itertools.count(start)
        self._released = collections.deque()

    def __next__(self) -> int:
        try:
            return self._released.popleft()
        except IndexError:
            self._last = next(self._generator)
            return self._last

    # noinspection PyShadowingBuiltins
    def __delitem__(self, id: int) -> bool:
        if self._last >= id > self._start:
            self._released.append(id)
            return True
        else:
            return False


class _EventHandler:
    _id: int
    _selves: dict[int, _EventHandler] = None
    _bindings: dict[int, dict[int, tuple[Callable, Iterable, Mapping[str, Any]]]] = None

    # noinspection PyShadowingBuiltins
    def __init__(self, id: int):
        if self._selves is None:
            type(self)._selves = {}
        if self._bindings is None:
            type(self)._bindings = {}
        self._id = id
        self._selves[id] = self
        self._bindings[id] = {}

    def __eq__(self, other: _EventHandler):
        return type(self) is type(other) and self._id == other._id

    def destroy(self) -> bool:
        try:
            del self._selves[self._id]
            del self._bindings[self._id]
            if hasattr(self, '_id_gen'):
                del self._id_gen[self._id]
        except KeyError:
            return False
        else:
            return True

    def get_id(self) -> int:
        return self._id

    # noinspection PyShadowingBuiltins
    @classmethod
    def get(cls, id: Optional[int] = None, default: Optional = None) -> Optional:
        if id is None:
            with contextlib.suppress(StopIteration):
                return next(reversed(cls._selves.values()))
        else:
            return cls._selves.get(id, default)

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
    _mainloop_thread = 0
    _menu_item_tooltip_proc = None
    _menu_item_tooltip_title = None

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
            ctyped.const.TTS_NOPREFIX, 0, 0, 0, 0, self._hwnd, None, self._hinstance, None))
        self._menu_item_tooltip = ctyped.struct.TTTOOLINFOW(uFlags=ctyped.const.TTF_SUBCLASS, hinst=self._hinstance)
        self._menu_item_tooltip_hwnd.send_message(ctyped.const.TTM_ADDTOOLW,
                                                  lparam=ctyped.addressof(self._menu_item_tooltip))
        self._attached: list[_Control] = []
        self._mainloop_lock = threading.Lock()
        super().__init__(self._hwnd.value)
        atexit.register(self.destroy)

    def destroy(self) -> bool:
        atexit.unregister(self.destroy)
        ctyped.lib.User32.KillTimer(self._hwnd, _TID_MENU_ITEM_TOOLTIP)
        while self._attached:
            self._attached.pop().destroy()
        self._menu_item_tooltip_hwnd = None
        self._hwnd = None
        ctyped.lib.User32.UnregisterClassW(self._class.lpszClassName, self._hinstance)
        return super().destroy()

    def _wnd_proc(self, hwnd: ctyped.type.HWND, message: ctyped.type.UINT,
                  wparam: ctyped.type.WPARAM, lparam: ctyped.type.LPARAM) -> ctyped.type.LRESULT:
        if message == ctyped.const.WM_DESTROY:
            ctyped.lib.User32.PostQuitMessage(0)
        elif message == ctyped.const.WM_CLOSE:
            ctyped.lib.User32.DestroyWindow(hwnd)
        elif message == ctyped.const.WM_QUERYENDSESSION:
            ...
        elif message == _WM_TASKBARCREATED:
            SystemTray.update()
        elif message in (_WM_MENU_ITEM_TOOLTIP_HIDE, ctyped.const.WM_MOUSELEAVE):
            self._menu_item_tooltip_hwnd.send_message(ctyped.const.TTM_TRACKACTIVATE)
            if wparam:
                self._menu_item_tooltip_hwnd.show(ctyped.const.SW_HIDE)
        elif message == ctyped.const.WM_ENTERIDLE:
            ctyped.lib.User32.KillTimer(hwnd, _TID_MENU_ITEM_TOOLTIP)
            if wparam == ctyped.const.MSGF_MENU and (proc := self._menu_item_tooltip_proc) is not None:
                ctyped.lib.User32.SetTimer(hwnd, _TID_MENU_ITEM_TOOLTIP, MENU_ITEM_TOOLTIP_DELAY, proc)
        elif message == ctyped.const.WM_DISPLAYCHANGE:
            self.trigger(message)
        elif message == _WM_SYS_TRAY:
            SystemTray.get(wparam).trigger(lparam)
        elif message in (ctyped.const.WM_INITMENUPOPUP, ctyped.const.WM_UNINITMENUPOPUP):
            Menu.get(wparam).trigger(message)
        elif message in (ctyped.const.WM_MENUSELECT, ctyped.const.WM_MENUCOMMAND, ctyped.const.WM_MENURBUTTONUP):
            is_command = message == ctyped.const.WM_MENUCOMMAND
            self._hwnd.send_message(_WM_MENU_ITEM_TOOLTIP_HIDE, is_command)
            if lparam:
                is_select = message == ctyped.const.WM_MENUSELECT
                item = Menu.get(lparam).get_item(ctyped.macro.LOWORD(wparam), by_pos=not is_select or (
                        ctyped.const.MF_POPUP == ctyped.macro.HIWORD(wparam) & ctyped.const.MF_POPUP))
                if is_select:
                    # noinspection PyProtectedMember
                    self._menu_item_tooltip_proc = item._tooltip_proc if item._tooltip_text else None
                    ctyped.lib.User32.TrackMouseEvent(ctyped.byref(
                        ctyped.struct.TRACKMOUSEEVENT(dwFlags=ctyped.const.TME_LEAVE, hwndTrack=hwnd)))
                if is_command and item.get_type() in (MenuItemType.CHECK, MenuItemType.RADIO):
                    item.check(not item.is_checked())
                item.trigger(message)
        else:
            return ctyped.lib.User32.DefWindowProcW(hwnd, message, wparam, lparam)
        return 0

    def _show_menu_item_tooltip(self, text: str, icon: int, title: str, pos: Optional[tuple[int, int]] = None):
        self._menu_item_tooltip_proc = None
        self._menu_item_tooltip.lpszText = text
        self._menu_item_tooltip_title = ctyped.char_array(title)
        lparam = ctyped.addressof(self._menu_item_tooltip)
        self._hwnd.send_message(_WM_MENU_ITEM_TOOLTIP_HIDE)
        self._menu_item_tooltip_hwnd.send_message(ctyped.const.TTM_UPDATETIPTEXTW, lparam=lparam)
        self._menu_item_tooltip_hwnd.send_message(ctyped.const.TTM_SETTITLEW, icon,
                                                  ctyped.addressof(self._menu_item_tooltip_title))
        self._menu_item_tooltip_hwnd.send_message(ctyped.const.TTM_TRACKACTIVATE, 1, lparam)
        if pos:
            ctyped.lib.User32.SetWindowPos(self._menu_item_tooltip_hwnd, None, *pos, 0, 0,
                                           ctyped.const.SWP_NOACTIVATE | ctyped.const.SWP_NOSIZE)

    def is_mainloop_running(self) -> bool:
        return self._mainloop_lock.locked()

    def is_mainloop_thread(self) -> bool:
        return self.is_mainloop_running() and self._mainloop_thread == threading.get_native_id()

    def mainloop(self) -> Optional[int]:
        with self._mainloop_lock:
            self._mainloop_thread = threading.get_native_id()
            msg = ctyped.struct.MSG()
            msg_ref = ctyped.byref(msg)
            while ctyped.lib.User32.GetMessageW(msg_ref, self._hwnd, 0, 0) > 0:
                ctyped.lib.User32.TranslateMessage(msg_ref)
                ctyped.lib.User32.DispatchMessageW(msg_ref)
            return msg.wParam

    def exit_mainloop(self) -> bool:
        return bool(self._hwnd.send_message(ctyped.const.WM_CLOSE, wait=False))


class _Control(_EventHandler):
    def _attach(self, gui: Optional[Gui]) -> int:
        if gui is None:
            gui = Gui.get()
            if gui is None:
                raise RuntimeError(
                    f"Could not initialize '{type(self).__name__} (Live instance of '{Gui.__name__}' unavailable)")
        # noinspection PyProtectedMember
        gui._attached.append(self)
        return gui.get_id()


class SystemTray(_Control):
    _selves: dict[int, SystemTray]
    _id_gen = _IDGenerator()

    _show = False
    _hicon = None
    _balloon_hicon = None
    _animation_frames = None
    _animation_speed = 1

    def __init__(self, icon: Union[int, str] = ctyped.const.IDI_APPLICATION,
                 tooltip: Optional[str] = None, *, _gui: Optional[Gui] = None):
        self._hwnd = self._attach(_gui)
        self._animation_proc = ctyped.type.TIMERPROC(self._set_next_frame)
        super().__init__(next(self._id_gen))
        self._data = ctyped.struct.NOTIFYICONDATAW(NOTIFYICONDATAW_V3_SIZE, self._hwnd, self._id,
                                                   ctyped.const.NIF_MESSAGE | ctyped.const.NIF_ICON |
                                                   ctyped.const.NIF_TIP, _WM_SYS_TRAY)
        self.set_icon(icon)
        if tooltip is not None:
            self.set_tooltip(tooltip)

    def destroy(self) -> bool:
        self.stop_animation()
        self.hide()
        return super().destroy()

    @classmethod
    def update(cls):
        for self in cls._selves.values():
            self._update()

    def is_animated(self) -> bool:
        return self._animation_frames is not None

    def is_shown(self) -> bool:
        return not bool(ctyped.lib.Shell32.Shell_NotifyIconGetRect(ctyped.byref(
            ctyped.struct.NOTIFYICONIDENTIFIER(hWnd=self._hwnd, uID=self._id)), ctyped.byref(ctyped.struct.RECT())))

    def _set_hicon(self, hicon: Optional[ctyped.type.HICON] = None) -> bool:
        self._data.hIcon = hicon
        return self._update()

    def set_icon(self, res_or_path: Union[int, str]) -> bool:
        self.stop_animation()
        self._hicon = _gdiplus.Bitmap.from_file(res_or_path).get_hicon() if isinstance(
            res_or_path, str) else ctyped.handle.HICON.from_idi(res_or_path)
        self._set_hicon(self._hicon)
        return bool(self._hicon)

    def set_tooltip(self, tooltip: str) -> bool:
        self._data.szTip = tooltip
        return self._update()

    def _set_next_frame(self, *_):
        try:
            delay, hicon = next(self._animation_frames)
        except TypeError:
            pass
        else:
            self._set_hicon(hicon)
            ctyped.lib.User32.SetTimer(self._hwnd, self._id, int(delay / self._animation_speed), self._animation_proc)

    def start_animation(self, gif_path: str) -> bool:
        self.stop_animation()
        self._animation_frames = itertools.cycle(frames := tuple(_get_gif_frames(gif_path)))
        if frames:
            self._set_next_frame()
        return bool(frames)

    def stop_animation(self):
        self._animation_frames = None
        ctyped.lib.User32.KillTimer(self._hwnd, self._id)
        self._set_hicon(self._hicon)

    def set_animation_speed(self, factor: float) -> bool:
        self._animation_speed = factor
        return bool(self._animation_frames)

    def _update(self) -> bool:
        return self._show and bool(ctyped.lib.Shell32.Shell_NotifyIconW(ctyped.const.NIM_MODIFY, ctyped.byref(
            self._data)) or ctyped.lib.Shell32.Shell_NotifyIconW(ctyped.const.NIM_ADD, ctyped.byref(self._data)))

    def show(self) -> bool:
        self._show = True
        self._show = self._update()
        return self._show

    def hide(self) -> bool:
        self._show = not bool(ctyped.lib.Shell32.Shell_NotifyIconW(ctyped.const.NIM_DELETE, ctyped.byref(self._data)))
        return not self._show

    def show_balloon(self, title: str, text: Optional[str] = None,
                     res_or_path: Union[int, str] = SystemTrayIcon.NONE, silent: bool = False) -> bool:
        flags = self._data.uFlags
        hicon = self._hicon
        self._data.uFlags = ctyped.const.NIF_INFO | ctyped.const.NIF_ICON
        self._data.hIcon = self._hicon
        if text is None:
            text = title
            title = ''
        self._data.szInfo = text
        self._data.szInfoTitle = title
        if isinstance(res_or_path, str):
            self._balloon_hicon = self._data.hBalloonIcon = _gdiplus.Bitmap.from_file(res_or_path).get_hicon()
            res_or_path = ctyped.const.NIIF_USER
        self._data.dwInfoFlags = res_or_path | ctyped.const.NIIF_RESPECT_QUIET_TIME
        if silent:
            self._data.dwInfoFlags |= ctyped.const.NIIF_NOSOUND
        try:
            return self.show()
        finally:
            print(win32.get_error())
            self._data.uFlags = flags
            self._set_hicon(hicon)


class Menu(_Control):
    _selves: dict[int, Menu]

    _hbrush = None

    def __init__(self, *, _gui: Optional[Gui] = None):
        self._hwnd = self._attach(_gui)
        self._hmenu = ctyped.handle.HMENU.from_type()
        ctyped.lib.User32.SetMenuInfo(self._hmenu, ctyped.byref(
            ctyped.struct.MENUINFO(fMask=ctyped.const.MIM_STYLE, dwStyle=ctyped.const.MNS_NOTIFYBYPOS)))
        self._hmenu.set_hwnd(self._hwnd)
        self._items: list[_MenuItem] = []
        super().__init__(self._hmenu.value)

    def __contains__(self, id_or_item: Union[int, _MenuItem]):
        return self.get_item(id_or_item) is not None

    def __len__(self):
        return len(self._items)

    def __getitem__(self, pos: Union[int, slice]) -> Union[_MenuItem, tuple[_MenuItem]]:
        items = self._items[pos]
        return tuple(items) if isinstance(pos, slice) else items

    def __delitem__(self, pos_or_item: Union[int, slice, _MenuItem]) -> bool:
        if isinstance(pos_or_item, slice):
            deleted = True
            for item in self[pos_or_item]:
                deleted = self.__delitem__(item) and deleted
            return deleted
        else:
            return self.remove_item(pos_or_item, True)

    def __iter__(self) -> _MenuItem:
        yield from self._items

    def destroy(self) -> bool:
        self._items.clear()
        self._hmenu = None
        return super().destroy()

    def get_item_count(self) -> int:
        return self._hmenu.get_item_count()

    def get_item(self, id_or_pos_or_item: Union[int, _MenuItem],
                 default: Any = None, by_pos: bool = False) -> Optional[_MenuItem]:
        if by_pos:
            if id_or_pos_or_item >= 0:
                with contextlib.suppress(IndexError):
                    return self._items[id_or_pos_or_item]
        else:
            if isinstance(id_or_pos_or_item, int):
                id_or_pos_or_item = _MenuItem.get(id_or_pos_or_item)
            if id_or_pos_or_item and self is id_or_pos_or_item.get_menu():
                return id_or_pos_or_item
        return default

    # noinspection PyShadowingBuiltins
    def append_item(self, text: Optional[str] = None, image_res_or_path: Optional[Union[str, None]] = None,
                    submenu: Optional[Menu] = None, enable: bool = True, check: Optional[bool] = None,
                    type: int = MenuItemType.NORMAL) -> Optional[_MenuItem]:
        return self.insert_item(self.get_item_count(), text, image_res_or_path, submenu, enable, check, type)

    # noinspection PyShadowingBuiltins
    def insert_item(self, pos: int, text: Optional[str] = None, image_res_or_path: Optional[Union[int, str]] = None,
                    submenu: Optional[Menu] = None, enable: bool = True, check: Optional[bool] = None,
                    type: int = MenuItemType.NORMAL) -> Optional[_MenuItem]:
        item = _MenuItem(self, type, gui=Gui.get(self._hwnd))
        if ctyped.lib.User32.InsertMenuW(self._hmenu, pos, ctyped.const.MF_BYPOSITION, item.get_id(), None):
            self._items.insert(pos, item)
            if type == MenuItemType.SEPARATOR:
                # noinspection PyProtectedMember
                item._set_separator()
            else:
                if text is not None:
                    item.set_text(text)
                if image_res_or_path is not None:
                    item.set_image(image_res_or_path) if text is None else item.set_icon(image_res_or_path)
                if submenu is not None:
                    item.set_submenu(submenu)
                if type == MenuItemType.RADIO:
                    # noinspection PyProtectedMember
                    item._set_radio()
                    if check is None:
                        check = True
                    item.check(check)
                item.enable(enable)
            return item

    def remove_item(self, id_or_pos_or_item: Union[int, _MenuItem], by_pos: bool = False) -> bool:
        if isinstance(id_or_pos_or_item, _MenuItem):
            id_or_pos_or_item = id_or_pos_or_item.get_id()
            by_pos = False
        removed = self._hmenu.remove_item(id_or_pos_or_item, by_pos)
        if removed:
            self._items.remove(self.get_item(id_or_pos_or_item, by_pos))
        return removed

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

    def _get_data(self, mim: int) -> Optional:
        info = ctyped.struct.MENUINFO(fMask=mim)
        if ctyped.lib.User32.GetMenuInfo(self._hmenu, ctyped.byref(info)):
            return getattr(info, _MIM_FIELD[mim])

    def get_background_color(self) -> Optional[tuple[int, int, int]]:
        if info := self._get_data(ctyped.const.MIM_BACKGROUND):
            return ctyped.handle.HBRUSH.get_rgb(info)

    def get_max_height(self) -> Optional[int]:
        if info := self._get_data(ctyped.const.MIM_MAXHEIGHT):
            return info

    def _get_styles(self) -> Optional[tuple[bool, bool, bool, bool, bool, bool]]:
        if style := self._get_data(ctyped.const.MIM_STYLE):
            return (ctyped.const.MNS_AUTODISMISS == style & ctyped.const.MNS_AUTODISMISS,
                    ctyped.const.MNS_CHECKORBMP == style & ctyped.const.MNS_CHECKORBMP,
                    ctyped.const.MNS_DRAGDROP == style & ctyped.const.MNS_DRAGDROP,
                    ctyped.const.MNS_MODELESS == style & ctyped.const.MNS_MODELESS,
                    ctyped.const.MNS_NOCHECK == style & ctyped.const.MNS_NOCHECK,
                    ctyped.const.MNS_NOTIFYBYPOS == style & ctyped.const.MNS_NOTIFYBYPOS)

    def get_auto_dismiss(self) -> Optional[bool]:
        return self._get_styles()[0]

    def get_no_check(self) -> Optional[bool]:
        return self._get_styles()[4]

    def _set_data(self, mim: int, data, recursive: bool) -> bool:
        info = ctyped.struct.MENUINFO(fMask=(recursive * ctyped.const.MIM_APPLYTOSUBMENUS) | mim)
        setattr(info, _MIM_FIELD[mim], data)
        return bool(ctyped.lib.User32.SetMenuInfo(self._hmenu, ctyped.byref(info)))

    def set_background_color(self, color_or_rgb: Union[int, tuple[int, int, int]], recursive: bool = True) -> bool:
        self._hbrush = ctyped.handle.HBRUSH.from_color(color_or_rgb) if isinstance(
            color_or_rgb, int) else ctyped.handle.HBRUSH.from_rgb(*color_or_rgb)
        return bool(self._hbrush) and self._set_data(ctyped.const.MIM_BACKGROUND, self._hbrush, recursive)

    def set_max_height(self, height: int = 0, recursive: bool = True) -> bool:
        return bool(self._set_data(ctyped.const.MIM_MAXHEIGHT, height, recursive))

    def _set_styles(self, auto_dismiss: Optional[bool] = None, check_or_image: Optional[bool] = None,
                    drag_drop: Optional[bool] = None, modeless: Optional[bool] = None, no_check: Optional[bool] = None,
                    notify_by_pos: Optional[bool] = None, recursive: bool = True) -> bool:
        styles = self._get_styles()
        flags = 0
        if styles[0] if auto_dismiss is None else auto_dismiss:
            flags |= ctyped.const.MNS_AUTODISMISS
        if styles[1] if check_or_image is None else check_or_image:
            flags |= ctyped.const.MNS_CHECKORBMP
        if styles[2] if drag_drop is None else drag_drop:
            flags |= ctyped.const.MNS_DRAGDROP
        if styles[3] if modeless is None else modeless:
            flags |= ctyped.const.MNS_MODELESS
        if styles[4] if no_check is None else no_check:
            flags |= ctyped.const.MNS_NOCHECK
        if styles[5] if notify_by_pos is None else notify_by_pos:
            flags |= ctyped.const.MNS_NOTIFYBYPOS
        return bool(self._set_data(ctyped.const.MIM_STYLE, flags, recursive))

    def set_auto_dismiss(self, auto_dismiss: bool = True) -> bool:
        return self._set_styles(auto_dismiss, recursive=False)

    def set_no_check(self, no_check: bool = True, recursive: bool = True) -> bool:
        return self._set_styles(no_check=no_check, recursive=recursive)


_TID_MENU_ITEM_MARQUEE = 100


class _MenuItem(_Control):
    _selves: dict[int, _MenuItem]
    _id_gen = _IDGenerator()

    _tooltip_text: str = ''
    _tooltip_icon: int = MenuItemTooltipIcon.NONE
    _tooltip_title: str = ''

    def __init__(self, menu: Menu, type_: int, *, gui: Optional[Gui] = None):
        self._hwnd = self._attach(gui)
        self._tooltip_proc = ctyped.type.TIMERPROC(self._show_tooltip)
        self._menu = menu
        self._type = type_
        self._hbmps: list[Optional[ctyped.handle.HBITMAP]] = [None] * 3
        super().__init__(next(self._id_gen))

    def destroy(self) -> bool:
        self._menu.remove_item(self)
        return super().destroy()

    def _show_tooltip(self, *_):
        ctyped.lib.User32.KillTimer(self._hwnd, _TID_MENU_ITEM_TOOLTIP)
        if self._tooltip_text and self.is_highlighted():
            rect = ctyped.struct.RECT()
            ctyped.lib.User32.GetMenuItemRect(self._hwnd, self._menu.get_id(), self.get_pos(), ctyped.byref(rect))
            pt = ctyped.struct.POINT()
            ctyped.lib.User32.GetCursorPos(ctyped.byref(pt))
            if rect.left <= pt.x <= rect.right and rect.top <= pt.y <= rect.bottom:
                pos = None
            else:
                pos = rect.left + int((rect.right - rect.left) / 2), rect.top + int((rect.bottom - rect.top) / 2)
            # noinspection PyProtectedMember
            Gui.get(self._hwnd)._show_menu_item_tooltip(
                self._tooltip_text, self._tooltip_icon, self._tooltip_title, pos)

    def get_menu(self) -> Menu:
        return self._menu

    def get_type(self) -> int:
        return self._type

    def _prep_image(self, res_or_path: Union[int, str], index: int, resize: bool) -> int:
        if isinstance(res_or_path, str):
            res_or_path = _gdiplus.Bitmap.from_file(res_or_path)
            if resize:
                res_or_path = res_or_path.get_resized(16, 16)
            res_or_path = res_or_path.get_hbitmap()
            self._hbmps[index] = res_or_path
            return res_or_path.value
        return res_or_path

    def _get_datas(self, miim: int, info: Optional[ctyped.struct.MENUITEMINFOW] = None) -> Optional[tuple]:
        if info is None:
            info = ctyped.struct.MENUITEMINFOW()
        info.fMask = miim
        if ctyped.lib.User32.GetMenuItemInfoW(self._menu.get_id(), self._id, False, ctyped.byref(info)):
            return tuple(getattr(info, field) for field in _MIIM_FIELDS[miim])

    def _get_icon(self) -> Optional[ctyped.handle.HBITMAP]:
        if datas := self._get_datas(ctyped.const.MIIM_BITMAP):
            return ctyped.handle.HBITMAP(datas[0])

    def _get_check_icons(self) -> Optional[tuple[ctyped.handle.HBITMAP, ctyped.handle.HBITMAP]]:
        if datas := self._get_datas(ctyped.const.MIIM_CHECKMARKS):
            return ctyped.handle.HBITMAP(datas[0]), ctyped.handle.HBITMAP(datas[1])

    def get_types(self) -> Optional[tuple[bool, bool, bool, bool]]:
        if datas := self._get_datas(ctyped.const.MIIM_TYPE):
            return (ctyped.const.MFT_MENUBREAK == datas[0] & ctyped.const.MFT_MENUBREAK,
                    ctyped.const.MFT_RADIOCHECK == datas[0] & ctyped.const.MFT_RADIOCHECK,
                    ctyped.const.MFT_RIGHTORDER == datas[0] & ctyped.const.MFT_RIGHTORDER,
                    ctyped.const.MFT_RIGHTJUSTIFY == datas[0] & ctyped.const.MFT_RIGHTJUSTIFY)

    def is_broken(self) -> bool:
        return self.get_types()[0]

    def is_radio(self) -> bool:
        return self.get_types()[1]

    def is_right_ordered(self) -> bool:
        return self.get_types()[2]

    def is_right_justified(self) -> bool:
        return self.get_types()[3]

    def get_states(self) -> Optional[tuple[bool, bool, bool, bool]]:
        if datas := self._get_datas(ctyped.const.MIIM_STATE):
            return (datas[0] & (ctyped.const.MF_GRAYED | ctyped.const.MFS_DISABLED) == 0,
                    ctyped.const.MFS_HILITE == datas[0] & ctyped.const.MFS_HILITE,
                    ctyped.const.MFS_CHECKED == datas[0] & ctyped.const.MFS_CHECKED,
                    ctyped.const.MFS_DEFAULT == datas[0] & ctyped.const.MFS_DEFAULT)

    def is_enabled(self) -> bool:
        return self.get_states()[0]

    def is_highlighted(self) -> bool:
        return self.get_states()[1]

    def is_checked(self) -> bool:
        return self.get_states()[2]

    def is_default(self) -> bool:
        return self.get_states()[3]

    def get_text(self) -> str:
        item_info = ctyped.struct.MENUITEMINFOW()
        if self._get_datas(ctyped.const.MIIM_STRING, item_info) and item_info.cch:
            item_info.cch += 1
            with _utils.string_buffer(item_info.cch) as buff:
                item_info.dwTypeData = buff
                if self._get_datas(ctyped.const.MIIM_STRING, item_info):
                    return item_info.dwTypeData
        return ''

    def get_submenu(self) -> Optional[Menu]:
        if datas := self._get_datas(ctyped.const.MIIM_SUBMENU):
            return Menu.get(datas[0])

    def _set_datas(self, miim: int, datas: Iterable) -> bool:
        info = ctyped.struct.MENUITEMINFOW(fMask=miim)
        for field, data in zip(_MIIM_FIELDS[miim], datas):
            setattr(info, field, data)
        return bool(ctyped.lib.User32.SetMenuItemInfoW(self._menu.get_id(), self._id, False, ctyped.byref(info)))

    def set_icon(self, res_or_path: Union[int, str], resize: bool = True) -> bool:
        return self._set_datas(ctyped.const.MIIM_BITMAP, (self._prep_image(res_or_path, 0, resize),))

    def _set_check_icons(self, res_or_path_checked: Optional[Union[int, str]],
                         res_or_path_unchecked: Optional[Union[int, str]], resize: bool) -> bool:
        return self._set_datas(ctyped.const.MIIM_CHECKMARKS, (
            self._prep_image(res_or_path_checked, 1, resize), self._prep_image(res_or_path_unchecked, 2, resize)))

    def _set_types(self, broken: Optional[bool] = None, radio: Optional[bool] = None,
                   right_aligned: Optional[bool] = None, right_justified: Optional[bool] = None) -> bool:
        types = self.get_types()
        flags = 0
        if types[0] if broken is None else broken:
            flags |= ctyped.const.MF_MENUBREAK
        if types[1] if radio is None else radio:
            flags |= ctyped.const.MFT_RADIOCHECK
        if types[2] if right_aligned is None else right_aligned:
            flags |= ctyped.const.MFT_RIGHTORDER
        if types[3] if right_justified is None else right_justified:
            flags |= ctyped.const.MFT_RIGHTJUSTIFY
        return self._set_datas(ctyped.const.MIIM_FTYPE, (flags,))

    def _set_broken(self, broken: bool = True) -> bool:
        return self._set_types(broken)

    def _set_radio(self, radio: bool = True) -> bool:
        return self._set_types(radio=radio)

    def set_right_aligned(self, right_aligned: bool = True) -> bool:
        return self._set_types(right_aligned=right_aligned)

    def _set_right_justified(self, right_justified: bool = True) -> bool:
        return self._set_types(right_justified=right_justified)

    # noinspection PyShadowingBuiltins
    def _set_id(self, id: int) -> bool:
        return self._set_datas(ctyped.const.MIIM_ID, (id,))

    def _set_states(self, enable: Optional[bool] = None, highlight: Optional[bool] = None,
                    check: Optional[bool] = None, default: Optional[bool] = None) -> bool:
        states = self.get_states()
        flags = ctyped.const.MFS_ENABLED if (states[0] if enable is None else enable) else ctyped.const.MFS_DISABLED
        flags |= ctyped.const.MFS_HILITE if (states[1] if highlight is None else
                                             highlight) else ctyped.const.MFS_UNHILITE
        flags |= ctyped.const.MFS_CHECKED if (states[2] if check is None else check) else ctyped.const.MFS_UNCHECKED
        if states[3] if default is None else default:
            flags |= ctyped.const.MFS_DEFAULT
        return self._set_datas(ctyped.const.MIIM_STATE, (flags,))

    def enable(self, enable: bool = True) -> bool:
        return self._set_states(enable)

    def highlight(self, highlight: bool = True) -> bool:
        return self._set_states(highlight=highlight)

    def _check(self, check: bool = True) -> bool:
        return self._set_states(check=check)

    def set_default(self, default: bool = True) -> bool:
        return self._set_states(default=default)

    def set_text(self, text: str) -> bool:
        return self._set_datas(ctyped.const.MIIM_TYPE, (ctyped.const.MFT_STRING, text))

    def set_image(self, res_or_path: Union[int, str]) -> bool:
        return self._set_datas(ctyped.const.MIIM_TYPE, (
            ctyped.const.MFT_BITMAP, ctyped.type.LPWSTR(self._prep_image(res_or_path, 0, False))))

    def _set_separator(self) -> bool:
        return self._set_datas(ctyped.const.MIIM_TYPE, (ctyped.const.MFT_SEPARATOR,))

    def set_submenu(self, submenu: Menu, text: Optional[str] = None) -> bool:  # TODO image submenu
        return self._set_datas(ctyped.const.MIIM_SUBMENU | ctyped.const.MIIM_TYPE,
                               (submenu.get_id(), self.get_text() if text is None else text))

    def get_pos(self) -> int:
        for pos, item in enumerate(self._menu):
            if self == item:
                return pos
        return -1

    def _check_radio(self) -> bool:
        pos = first_pos = last_pos = self.get_pos()
        while (item := self._menu.get_item(first_pos - 1, by_pos=True)) and item.is_radio():
            first_pos -= 1
        while (item := self._menu.get_item(last_pos + 1, by_pos=True)) and item.is_radio():
            last_pos += 1
        # noinspection PyProtectedMember
        return self._menu._hmenu.check_radio_item(pos, first_pos, last_pos, True)

    def check(self, check: bool = True) -> bool:
        return (self._check_radio() if check else not self.is_checked()) if self.is_radio() else self._check(check)

    def set_checked_icon(self, res_or_path: Optional[Union[int, str]] = None, resize: bool = True) -> bool:
        return self._set_check_icons(res_or_path, self._hbmps[2], resize)

    def set_unchecked_icon(self, res_or_path: Optional[Union[int, str]] = None, resize: bool = True) -> bool:
        return self._set_check_icons(self._hbmps[1], res_or_path, resize)

    def set_tooltip(self, text: str, title: str = '', icon_res_or_path: Union[int, str] = MenuItemTooltipIcon.NONE):
        self._tooltip_text = text
        self._tooltip_title = title
        self._tooltip_icon = _gdiplus.Bitmap.from_file(
            icon_res_or_path).get_hicon() if isinstance(icon_res_or_path, str) else icon_res_or_path


def _foo(e, s: SystemTray, menu: Menu, item: _MenuItem):
    # s.show_balloon('very busy', 'mini text', Icon.TRAY)
    menu.show()
    return 0


def _foo2(e: int, s: SystemTray):
    print(s.start_animation(r'D:\Projects\Wallpyper\src\resources\busy.gif'))
    # Gui.get().exit_mainloop()  # s.set_icon(r'E:\Projects\wallpyper\icon.ico')  # s.stop_animation()


def foo3(e, m: SystemTray, s: SystemTray):
    s.stop_animation()


def _wait():
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass


def _test_gui():
    p = r'D:\Projects\wallpyper\src\resources\tray.png'
    # bind(EVENT_CLOSE, lambda *args: print(6969))
    g = Gui()
    s = SystemTray(p, 'tip')
    menu = Menu()
    not_hidden = menu.append_item('tray icon shown')
    not_hidden.bind(MenuItemEvent.LEFT_UP, lambda *args: print(s.is_shown()))
    it = menu.append_item('stop animate\tright')
    print(it.is_enabled())
    it.bind(MenuItemEvent.LEFT_UP, foo3, (s,))
    it.set_tooltip('important long text tip', 'tip title', p)
    menu.append_item(type=MenuItemType.SEPARATOR)
    ball = menu.append_item('balloon\tright2')
    ball.set_tooltip('another tip')
    ball.bind(MenuItemEvent.RIGHT_UP, lambda *args: print('balloon button right up'))
    ball.bind(MenuItemEvent.LEFT_UP,
              lambda *args: s.show_balloon('very busy', 'mini text', r'D:\Projects\wallpyper\src\resources\icon.ico'))
    # print(menu.set_item_image(it, p))
    # ctyped.lib.User32.SetMenu(s._hwnd, menu._hmenu)
    item = menu.append_item('text')
    # print(item.get_id(), menu.get_item_id(item))
    menu2 = Menu()
    menu2.append_item('gg', type=MenuItemType.CHECK)
    it_ck = menu.append_item('check', type=MenuItemType.CHECK)
    it_ck.check()
    # it_ck.set_image(p)  # TODO do not die after click
    menu3 = Menu()
    menu.append_item('rad test', submenu=menu3)
    # menu.set_max_height(100)
    # print(menu.get_max_height())
    for i in range(6):
        menu3.append_item('radio' + str(i), type=MenuItemType.RADIO)
    it7 = menu2.append_item('69')
    it7.bind(MenuItemEvent.HIGHLIGHT, lambda *args: print('hover', args))
    menu2.append_item('new')
    ex = menu.append_item('exit', MenuItemImage.CLOSE)
    ex.bind(MenuItemEvent.LEFT_UP, lambda *args: g.exit_mainloop())
    # print(item.set_image(r'D:\Projects\wallpyper\src\resources\tray.png', True))
    # menu.set_item_submenu(item, menu2)
    item.set_submenu(menu2)
    item.set_image(p)
    item.set_tooltip('https://www.google.com')
    g.bind(GuiEvent.DISPLAY_CHANGE, lambda *args: print('display', args))

    s.bind(SystemTrayEvent.RIGHT_UP, _foo, (menu, item))
    s.bind(SystemTrayEvent.LEFT_DOUBLE, _foo2)
    s.bind(SystemTrayEvent.BALLOON_SHOW, lambda *args: print('show_balloon'))
    s.bind(SystemTrayEvent.BALLOON_HIDE, lambda *args: print('show_balloon hide'))
    s.bind(SystemTrayEvent.BALLOON_CLICK, lambda *args: print('show_balloon click'))
    s.bind(ctyped.const.NIN_SELECT, lambda *args: print('sel'))
    s.show()

    # s2 = SysTray(r'D:\Projects\wallpyper\src\resources\tray.png', 'tip2')
    # s2.set_animation_speed(5)
    # s2.start_animation(r'D:\Projects\wallpyper\src\resources\busy.gif')
    # s2.show()

    g.mainloop()
    g.destroy()
    print('exit')


def _test_settings():
    info = ctyped.struct.SHELLEXECUTEINFOW(lpVerb='open',
                                           lpFile='ms-settings:mobile-devices', nShow=ctyped.const.SW_NORMAL)
    print(ctyped.lib.Shell32.ShellExecuteExW(ctyped.byref(info)))


class ToastDismiss(ctyped.com_impl.ITypedEventHandler):
    # noinspection PyPep8Naming
    @staticmethod
    def Invoke(This: ctyped.Pointer[ctyped.com_impl.ITypedEventHandler],
               sender: ctyped.com.IToastNotification, args: ctyped.com.IInspectable) -> ctyped.type.HRESULT:
        print('invoke', This, sender, args)
        hs = ctyped.handle.HSTRING()
        args.GetRuntimeClassName(ctyped.byref(hs))
        print(hs.get_string())
        with ctyped.cast_com(args, ctyped.com.IToastDismissedEventArgs) as args_:
            r = ctyped.enum.ToastDismissalReason()
            args_.get_Reason(ctyped.byref(r))
            print(r)
        return 0


def _test_toast():
    ctyped.THREADED_COM = True
    aumi = 'HellLord.Wallpyper'
    xml_data = '''
<toast>
    <visual>
        <binding template="ToastGeneric">
            <text>Sample toast</text>
            <text>Sample content</text>
        </binding>
    </visual>
</toast>'''
    on_dismissed = ToastDismiss()

    with ctyped.get_winrt(ctyped.com.IToastNotificationManagerStatics) as manager:
        with ctyped.init_com(ctyped.com.IToastNotifier, False) as notifier:
            print(manager.CreateToastNotifierWithId(ctyped.handle.HSTRING.from_string(aumi), ctyped.byref(notifier)))
            with ctyped.get_winrt(ctyped.com.IToastNotificationFactory) as factory, win32.xml.loads(
                    xml_data) as xml, ctyped.init_com(ctyped.com.IToastNotification, False) as toast:
                print(factory.CreateToastNotification(xml, ctyped.byref(toast)))
                token = ctyped.struct.EventRegistrationToken()
                threading.Thread(target=toast.add_Dismissed, args=(on_dismissed, ctyped.byref(token))).start()
                print(notifier.Show(toast))
                print('wait')
                _wait()
                if token:
                    toast.remove_Dismissed(token)


def _test_winui():
    g = Gui()
    with ctyped.get_winrt(ctyped.com.IWindowsXamlManagerStatics) as manager_statics:
        manager = ctyped.com.IWindowsXamlManager()
        manager_statics.InitializeForCurrentThread(ctyped.byref(manager))
        with ctyped.get_winrt(ctyped.com.IDesktopWindowXamlSource, True) as source:
            with ctyped.cast_com(source, ctyped.com.IDesktopWindowXamlSourceNative) as source_native:
                print(source_native)


if __name__ == '__main__':
    # _test_toast()
    _test_winui()
    # _test_gui()
    # _test_settings()
    # _wait()
    sys.exit()
