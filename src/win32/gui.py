from __future__ import annotations as _

import atexit
import collections
import contextlib
import dataclasses
import functools
import itertools
import logging
import threading
from typing import Any
from typing import Callable
from typing import ContextManager
from typing import Iterable
from typing import Iterator
from typing import Optional

from libs import ctyped
from libs.ctyped.lib import shell32
from libs.ctyped.lib import user32
from . import _gdiplus
from . import _handle
from . import _utils

logger = logging.getLogger(__name__)

_NOTIFYICONDATAA_V1_SIZE = ctyped.macro.FIELD_OFFSET(ctyped.struct.NOTIFYICONDATAA, 'szTip', 64)
_NOTIFYICONDATAW_V1_SIZE = ctyped.macro.FIELD_OFFSET(ctyped.struct.NOTIFYICONDATAW, 'szTip', 64)
_NOTIFYICONDATAA_V2_SIZE = ctyped.macro.FIELD_OFFSET(ctyped.struct.NOTIFYICONDATAA, 'guidItem')
_NOTIFYICONDATAW_V2_SIZE = ctyped.macro.FIELD_OFFSET(ctyped.struct.NOTIFYICONDATAW, 'guidItem')
_NOTIFYICONDATAA_V3_SIZE = ctyped.macro.FIELD_OFFSET(ctyped.struct.NOTIFYICONDATAA, 'hBalloonIcon')
_NOTIFYICONDATAW_V3_SIZE = ctyped.macro.FIELD_OFFSET(ctyped.struct.NOTIFYICONDATAW, 'hBalloonIcon')

_WM_TASKBAR_CREATED = user32.RegisterWindowMessageW('TaskbarCreated')
_WM_TASKBAR_BUTTON_CREATED = user32.RegisterWindowMessageW('TaskbarButtonCreated')
_WM_SYS_TRAY_MSG = ctyped.const.WM_APP
_WM_MENU_ITEM_TOOLTIP_HIDE = ctyped.const.WM_APP + 1
_WM_WINDOW_MOUSEWHEEL_FWD = ctyped.const.WM_APP + 2
_WM_WINDOW_MOUSEWHEEL_BWD = ctyped.const.WM_APP + 3

_TID_MENU_ITEM_TOOLTIP = 0
_TOOLTIP_ICON_SIZE = 32
_MENU_ITEM_IMAGE_SIZE = 16
_MENU_ITEM_TOOLTIP_AUTOMATIC = 500
_MENU_ITEM_TOOLTIP_MAX_WIDTH = 32767

_MIM_TO_FIELD = {
    ctyped.const.MIM_BACKGROUND: 'hbrBack',
    ctyped.const.MIM_HELPID: 'dwContextHelpID',
    ctyped.const.MIM_MAXHEIGHT: 'cyMax',
    ctyped.const.MIM_STYLE: 'dwStyle'}
_MIIM_TO_FIELDS = {
    ctyped.const.MIIM_STATE: ('fState',),
    ctyped.const.MIIM_ID: ('wID',),
    ctyped.const.MIIM_SUBMENU: ('hSubMenu',),
    ctyped.const.MIIM_CHECKMARKS: ('hbmpChecked', 'hbmpUnchecked'),
    ctyped.const.MIIM_TYPE: ('fType', 'dwTypeData'),
    ctyped.const.MIIM_DATA: ('dwItemData',),
    ctyped.const.MIIM_STRING: ('dwTypeData', 'cch'),
    ctyped.const.MIIM_BITMAP: ('hbmpItem',),
    ctyped.const.MIIM_FTYPE: ('fType',)}

FLAG_BITMAP_PATH_CACHE = True
FLAG_MENU_ITEM_RESHOW_TOOLTIP = False
WINDOW_MIN_WIDTH = 516
WINDOW_MIN_HEIGHT = 509
MENU_ITEM_TOOLTIP_INITIAL = _MENU_ITEM_TOOLTIP_AUTOMATIC * 1
MENU_ITEM_TOOLTIP_RESHOW = _MENU_ITEM_TOOLTIP_AUTOMATIC // 5


class GuiEvent:
    DISPLAY_CHANGE = ctyped.const.WM_DISPLAYCHANGE
    NC_RENDERING_CHANGED = ctyped.const.WM_DWMNCRENDERINGCHANGED


class WindowEvent:
    ACTIVATE = ctyped.const.WM_ACTIVATE
    ACTIVATE_APP = ctyped.const.WM_ACTIVATEAPP
    CLOSE = ctyped.const.WM_CLOSE
    DESTROY = ctyped.const.WM_DESTROY
    ENABLE = ctyped.const.WM_ENABLE
    ENTER_SIZE_MOVE = ctyped.const.WM_ENTERSIZEMOVE
    EXIT_SIZE_MOVE = ctyped.const.WM_EXITSIZEMOVE
    GET_MIN_MAX_INFO = ctyped.const.WM_GETMINMAXINFO
    MOVE = ctyped.const.WM_MOVE
    PAINT = ctyped.const.WM_PAINT
    SIZE = ctyped.const.WM_SIZE
    WINDOW_POS_CHANGED = ctyped.const.WM_WINDOWPOSCHANGED
    WINDOW_POS_CHANGING = ctyped.const.WM_WINDOWPOSCHANGING
    SET_CURSOR = ctyped.const.WM_SETCURSOR

    MOUSE_MOVE = ctyped.const.WM_MOUSEMOVE
    MOUSE_MOVE_NC = ctyped.const.WM_NCMOUSEMOVE
    MOUSE_LEFT_DOWN = ctyped.const.WM_LBUTTONDOWN
    MOUSE_LEFT_UP = ctyped.const.WM_LBUTTONUP
    MOUSE_LEFT_DOUBLE = ctyped.const.WM_LBUTTONDBLCLK
    MOUSE_RIGHT_DOWN = ctyped.const.WM_RBUTTONDOWN
    MOUSE_RIGHT_UP = ctyped.const.WM_RBUTTONUP
    MOUSE_RIGHT_DOUBLE = ctyped.const.WM_RBUTTONDBLCLK
    MOUSE_MIDDLE_DOWN = ctyped.const.WM_MBUTTONDOWN
    MOUSE_MIDDLE_UP = ctyped.const.WM_MBUTTONUP
    MOUSE_MIDDLE_DOUBLE = ctyped.const.WM_MBUTTONDBLCLK

    MOUSE_HOVER = ctyped.const.WM_MOUSEHOVER
    MOUSE_LEAVE = ctyped.const.WM_MOUSELEAVE
    MOUSE_HOVER_NC = ctyped.const.WM_NCMOUSEHOVER
    MOUSE_LEAVE_NC = ctyped.const.WM_NCMOUSELEAVE

    MOUSE_WHEEL_FORWARD = _WM_WINDOW_MOUSEWHEEL_FWD
    MOUSE_WHEEL_BACKWARD = _WM_WINDOW_MOUSEWHEEL_BWD


class SystemTrayIcon:
    APPLICATION = ctyped.const.IDI_APPLICATION
    HAND = ctyped.const.IDI_HAND
    QUESTION = ctyped.const.IDI_QUESTION
    EXCLAMATION = ctyped.const.IDI_EXCLAMATION
    ASTERISK = ctyped.const.IDI_ASTERISK
    WINLOGO = ctyped.const.IDI_WINLOGO
    SHIELD = ctyped.const.IDI_SHIELD

    BALLOON_NONE = ctyped.const.NIIF_NONE
    BALLOON_INFO = ctyped.const.NIIF_INFO
    BALLOON_WARNING = ctyped.const.NIIF_WARNING
    BALLOON_ERROR = ctyped.const.NIIF_ERROR
    BALLOON_TRAY = ctyped.const.NIIF_USER


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
    NONE = 0
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


@functools.lru_cache
def _bitmap_from_file(path: str) -> _gdiplus.Bitmap:
    return _gdiplus.Bitmap.from_file(path)


def _load_bitmap(path_or_bitmap: str | _gdiplus.Bitmap) -> _gdiplus.Bitmap:
    if not FLAG_BITMAP_PATH_CACHE:
        _bitmap_from_file.cache_clear()
    return _bitmap_from_file(path_or_bitmap) if isinstance(
        path_or_bitmap, str) else path_or_bitmap


@dataclasses.dataclass
class Event:
    control: _EventEmitter
    event: int
    params: Optional[tuple[int, int]] = None

    _skip: bool = False

    @property
    def hiword(self) -> int:
        return ctyped.cast_int(ctyped.macro.HIWORD(self.params[0]), ctyped.type.UINT)

    @property
    def loword(self) -> int:
        return ctyped.macro.LOWORD(self.params[0])

    def skip(self, skip: bool = True) -> bool:
        try:
            return self._skip
        finally:
            self._skip = skip


class _EventEmitter:
    _id: int
    _selves: dict[int, _EventEmitter] = None
    _bindings: dict[int, dict[int, Callable[[Event], Any]]] = None

    def __init_subclass__(cls):
        cls._selves = {}
        cls._bindings = {}

    # noinspection PyShadowingBuiltins
    def __init__(self, id: int):
        self._id = id
        self._selves[id] = self
        self._bindings[id] = {}

    def __eq__(self, other: _EventEmitter):
        return type(self) is type(other) and self._id == other._id

    def destroy(self) -> bool:
        try:
            del self._selves[self._id]
            del self._bindings[self._id]
            if (id_gen := getattr(self, '_id_gen', None)) is not None:
                del id_gen[self._id]
        except KeyError:
            return False
        else:
            return True

    def get_id(self) -> int:
        return self._id

    # noinspection PyShadowingBuiltins
    @classmethod
    def get(cls, id: Optional[int] = None) -> Optional[_EventEmitter]:
        if id is None:
            if cls._selves:
                return next(reversed(cls._selves.values()))
        else:
            return cls._selves.get(id)

    def bind(self, event: int, callback: Callable[[Event], Any], once: bool = False):
        if once:
            @functools.wraps(callback)
            def wrapped(*args, **kwargs):
                self.unbind(event)
                return callback(*args, **kwargs)
        else:
            wrapped = callback
        self._bindings[self._id][event] = wrapped

    def unbind(self, event: int) -> bool:
        try:
            del self._bindings[self._id][event]
        except KeyError:
            return False
        else:
            return True

    def trigger(self, event: int, params: Optional[tuple[int, int]] = None) -> Any:
        try:
            callback = self._bindings[self._id][event]
        except KeyError:
            pass
        else:
            event_ = Event(self, event, params)
            callback(event_)
            return event_.skip()
        return False


class Gui(_EventEmitter):
    _selves: dict[int, Gui]

    _id = 0
    _mainloop_thread = 0
    _menu_item_tooltip_proc = None
    _menu_item_tooltip_title = None

    def __init__(self, name: Optional[str] = None):
        self._class = ctyped.struct.WNDCLASSEXW(
            style=ctyped.const.CS_DBLCLKS | ctyped.const.CS_HREDRAW | ctyped.const.CS_VREDRAW,
            lpfnWndProc=ctyped.type.WNDPROC(self._wnd_proc), hInstance=_utils.HINSTANCE,
            hIcon=_handle.HICON.from_idi(ctyped.const.IDI_APPLICATION),
            hCursor=_handle.HCURSOR.from_idc(ctyped.const.IDC_ARROW),
            lpszClassName=f'{__name__}-{type(self).__name__}' if name is None else name,
            hbrBackground=_handle.HBRUSH(ctyped.const.COLOR_WINDOW))
        if not user32.RegisterClassExW(ctyped.byref(self._class)):
            raise RuntimeError(f'Cannot initialize {type(self).__name__!r}')
        self._message_window = Window(_gui=self)
        super().__init__(self._message_window.get_id())
        self._menu_item_tooltip_window = Window(
            style=ctyped.const.TTS_NOPREFIX, name=ctyped.const.TOOLTIPS_CLASS,
            ex_style=ctyped.const.WS_EX_TOPMOST, _gui=self)
        self._menu_item_tooltip = ctyped.struct.TTTOOLINFOW(
            uFlags=ctyped.const.TTF_SUBCLASS, hinst=_utils.HINSTANCE)
        self._menu_item_tooltip_window.send_message(
            ctyped.const.TTM_ADDTOOLW, lparam=ctyped.addressof(self._menu_item_tooltip))
        self._menu_item_tooltip_window.send_message(
            ctyped.const.TTM_SETMAXTIPWIDTH, 0, _MENU_ITEM_TOOLTIP_MAX_WIDTH)
        self._attached: list[_Control] = []
        self._mainloop_lock = threading.Lock()

    def _create_window(self, ex_style: int = 0, cls: str = '', wnd: str = '',
                       style: int = ctyped.const.WS_OVERLAPPED, x: int = 0, y: int = 0,
                       w: int = 0, h: int = 0, parent: Optional[int] = None) -> _handle.HWND:
        return _handle.HWND(user32.CreateWindowExW(
            ex_style, cls if cls else self._class.lpszClassName, wnd, style,
            x, y, w, h, self._message_window if parent is None else parent, None, _utils.HINSTANCE, None))

    def destroy(self) -> bool:
        user32.KillTimer(self._id, _TID_MENU_ITEM_TOOLTIP)
        while self._attached:
            self._attached.pop().destroy()
        self._menu_item_tooltip_window = None
        self._message_window = None
        user32.UnregisterClassW(self._class.lpszClassName, _utils.HINSTANCE)
        return super().destroy()

    def _wnd_proc(self, hwnd: ctyped.type.HWND, message: ctyped.type.UINT,
                  wparam: ctyped.type.WPARAM, lparam: ctyped.type.LPARAM) -> ctyped.type.LRESULT:
        if message == ctyped.const.WM_GETMINMAXINFO:
            min_dim = ctyped.struct.MINMAXINFO.from_address(lparam).ptMinTrackSize
            min_dim.x = WINDOW_MIN_WIDTH
            min_dim.y = WINDOW_MIN_HEIGHT
        skipped = False
        if hwnd == self._id:
            if message == ctyped.const.WM_DESTROY:
                user32.PostQuitMessage(0)
            elif message == ctyped.const.WM_CLOSE:
                user32.DestroyWindow(hwnd)
            elif message == _WM_TASKBAR_CREATED:
                SystemTray.update()
            elif message in (_WM_MENU_ITEM_TOOLTIP_HIDE, ctyped.const.WM_MOUSELEAVE):
                self._menu_item_tooltip_window.send_message(ctyped.const.TTM_TRACKACTIVATE)
                if wparam:
                    self._menu_item_tooltip_window.show(False)
            elif message == ctyped.const.WM_ENTERIDLE:
                user32.KillTimer(hwnd, _TID_MENU_ITEM_TOOLTIP)
                if wparam == ctyped.const.MSGF_MENU and self._menu_item_tooltip_proc:
                    user32.SetTimer(
                        hwnd, _TID_MENU_ITEM_TOOLTIP, MENU_ITEM_TOOLTIP_RESHOW
                        if FLAG_MENU_ITEM_RESHOW_TOOLTIP and self._menu_item_tooltip_window.is_visible() else
                        MENU_ITEM_TOOLTIP_INITIAL, self._menu_item_tooltip_proc)
            elif message in (ctyped.const.WM_DISPLAYCHANGE, ctyped.const.WM_DWMNCRENDERINGCHANGED):
                skipped = self.trigger(message, (wparam, lparam))
            elif message == _WM_SYS_TRAY_MSG:
                skipped = SystemTray.get(wparam).trigger(lparam)
            elif message in (ctyped.const.WM_INITMENUPOPUP, ctyped.const.WM_UNINITMENUPOPUP):
                self._message_window.send_message(_WM_MENU_ITEM_TOOLTIP_HIDE, 1)
                skipped = Menu.get(wparam).trigger(message, (wparam, lparam))
            elif message in (ctyped.const.WM_MENUSELECT,
                             ctyped.const.WM_MENUCOMMAND, ctyped.const.WM_MENURBUTTONUP):
                # FIXME WM_MENUSELECT is triggered again after auto closing a submenu (seq: select, close, select)
                is_command = int(message == ctyped.const.WM_MENUCOMMAND)
                self._message_window.send_message(_WM_MENU_ITEM_TOOLTIP_HIDE, is_command)
                if lparam:
                    is_select = message == ctyped.const.WM_MENUSELECT
                    item = Menu.get(lparam).get_item(ctyped.macro.LOWORD(wparam), by_pos=not is_select or (
                            ctyped.const.MF_POPUP == ctyped.macro.HIWORD(wparam) & ctyped.const.MF_POPUP))
                    if is_select:
                        # noinspection PyProtectedMember
                        self._menu_item_tooltip_proc = item._tooltip_proc if item._tooltip_text else None
                        user32.TrackMouseEvent(ctyped.byref(ctyped.struct.TRACKMOUSEEVENT(
                            dwFlags=ctyped.const.TME_LEAVE, hwndTrack=hwnd)))
                    if is_command and item.get_type() in (MenuItemType.CHECK, MenuItemType.RADIO):
                        item.check(not item.is_checked())
                    skipped = item.trigger(message, (wparam, lparam))
        elif (window := Window.get(hwnd)) is not None:
            if message == ctyped.const.WM_MOUSEWHEEL:
                message = _WM_WINDOW_MOUSEWHEEL_FWD if ctyped.macro.GET_Y_LPARAM(
                    wparam) > 0 else _WM_WINDOW_MOUSEWHEEL_BWD
            skipped = window.trigger(message, (wparam, lparam))
        return 0 if skipped else user32.DefWindowProcW(hwnd, message, wparam, lparam)

    def _show_menu_item_tooltip(self, text: str, title: str, icon: int,
                                pos: Optional[tuple[int, int]] = None):
        self._menu_item_tooltip_proc = None
        self._menu_item_tooltip.lpszText = text
        self._menu_item_tooltip_title = ctyped.char_array(title)
        lparam = ctyped.addressof(self._menu_item_tooltip)
        self._message_window.send_message(_WM_MENU_ITEM_TOOLTIP_HIDE)
        self._menu_item_tooltip_window.send_message(
            ctyped.const.TTM_UPDATETIPTEXTW, lparam=lparam)
        self._menu_item_tooltip_window.send_message(
            ctyped.const.TTM_SETTITLEW, icon, ctyped.addressof(
                self._menu_item_tooltip_title))
        self._menu_item_tooltip_window.send_message(
            ctyped.const.TTM_TRACKACTIVATE, 1, lparam)
        if pos:
            self._menu_item_tooltip_window.set_pos(*pos, False)

    def get_name(self) -> str:
        return self._class.lpszClassName

    def is_mainloop_running(self) -> bool:
        return self._mainloop_lock.locked()

    def is_mainloop_thread(self) -> bool:
        return self.is_mainloop_running() and self._mainloop_thread == threading.get_native_id()

    def mainloop(self) -> Optional[int]:
        with self._mainloop_lock:
            self._mainloop_thread = threading.get_native_id()
            msg = ctyped.struct.MSG()
            msg_ref = ctyped.byref(msg)
            while user32.GetMessageW(msg_ref, None, 0, 0) > 0:  # TODO -1
                user32.TranslateMessage(msg_ref)
                user32.DispatchMessageW(msg_ref)
            return msg.wParam

    def exit_mainloop(self) -> bool:
        return bool(self._message_window.send_message(ctyped.const.WM_CLOSE, wait=False))


class _Control(_EventEmitter):
    def _attach(self, gui: Optional[Gui]) -> int:
        if gui is None:
            gui = Gui.get()
            if gui is None:
                raise RuntimeError(f'Cannot find any {Gui.__name__} instance')
        # noinspection PyProtectedMember
        gui._attached.append(self)
        return gui.get_id()


class Window(_Control):
    def __init__(self, title: str = '', x: int = ctyped.const.CW_USEDEFAULT,
                 y: int = ctyped.const.CW_USEDEFAULT, width: int = ctyped.const.CW_USEDEFAULT,
                 height: int = ctyped.const.CW_USEDEFAULT, style: int = ctyped.const.WS_OVERLAPPEDWINDOW,
                 parent: Optional[Window] = None, name: Optional[str] = None,
                 ex_style: int = 0, *, _gui: Optional[Gui] = None):
        gui = Gui.get(self._attach(_gui)) if _gui is None else _gui
        # noinspection PyProtectedMember
        self._hwnd = _handle.HWND(user32.CreateWindowExW(
            ex_style, gui._class.lpszClassName if name is None else name, title, style, x, y,
            width, height, gui.get_id() if parent is None else parent._hwnd, None, _utils.HINSTANCE, None))
        self.get_message = self._hwnd.get_message
        self.send_message = self._hwnd.send_message
        self.flash = self._hwnd.flash
        self.open_icon = self._hwnd.open_icon
        self.close = self._hwnd.close
        self.is_visible = self._hwnd.is_visible
        self.is_iconic = self._hwnd.is_iconic
        self.bring_to_top = self._hwnd.bring_to_top
        self.is_zoomed = self._hwnd.is_zoomed
        self.update = self._hwnd.update
        self.set_active = self._hwnd.set_active
        self.set_foreground = self._hwnd.set_foreground
        self.set_title = self._hwnd.set_title
        self.invalidate_rect = self._hwnd.invalidate_rect
        self.invalidate_region = self._hwnd.invalidate_region
        super().__init__(self._hwnd.value)

    def destroy(self) -> bool:
        self._hwnd = None
        return super().destroy()

    def show(self, show: bool = True, wait: bool = True) -> bool:
        return self._hwnd.show(ctyped.const.SW_SHOW if show else ctyped.const.SW_HIDE, wait)

    def move(self, x: Optional[int] = None, y: Optional[int] = None,
             width: Optional[int] = None, height: Optional[int] = None, repaint: bool = True) -> bool:
        return self._hwnd.move(x, y, width, height, repaint)

    def set_pos(self, x: Optional[int] = None, y: Optional[int] = None, active: bool = True) -> bool:
        flags = ctyped.const.SWP_NOSIZE
        if not active:
            flags |= ctyped.const.SWP_NOACTIVATE | ctyped.const.SWP_NOZORDER
        return self._hwnd.set_pos(x, y, 0, 0, flags)

    def get_client_rect(self) -> tuple[int, int, int, int]:
        rect = self._hwnd.get_client_rect()
        return rect.left, rect.top, rect.right, rect.bottom

    def get_rect(self) -> tuple[int, int, int, int]:
        rect = self._hwnd.get_rect()
        return rect.left, rect.top, rect.right, rect.bottom

    def get_pos(self) -> tuple[int, int]:
        rect = self.get_rect()
        return rect[0], rect[1]

    def get_parent(self) -> Optional[Window]:
        parent = _handle.HWND.from_child(self._hwnd)
        if parent is not None:
            return Window.get(parent.value)

    def get_hdc(self) -> _handle.HDC:
        return _handle.HDC.from_hwnd(self._hwnd)

    @contextlib.contextmanager
    def paint(self) -> ContextManager[ctyped.type.HDC]:
        struct = ctyped.struct.PAINTSTRUCT()
        user32.BeginPaint(self._hwnd, ctyped.byref(struct))
        try:
            yield struct.hdc
        finally:
            user32.EndPaint(self._hwnd, ctyped.byref(struct))


class SystemTray(_Control):
    _selves: dict[int, SystemTray]
    _id_gen = _IDGenerator()

    _show = False
    _hicon: Optional[_handle.HICON] = None
    _balloon_hicon: Optional[_handle.HICON] = None
    _animation_stop = False
    _animation_speed = 1
    _animation_frames = None

    def __init__(self, icon: int | str = SystemTrayIcon.APPLICATION,
                 tooltip: Optional[str] = None, *, _gui: Optional[Gui] = None):
        self._hwnd = self._attach(_gui)
        self._animation_proc = ctyped.type.TIMERPROC(self._set_next_frame)
        super().__init__(next(self._id_gen))
        self._data = ctyped.struct.NOTIFYICONDATAW(
            _NOTIFYICONDATAW_V3_SIZE, self._hwnd, self._id,
            ctyped.const.NIF_MESSAGE | ctyped.const.NIF_ICON | ctyped.const.NIF_TIP, _WM_SYS_TRAY_MSG)
        self.set_icon(icon)
        if tooltip is not None:
            self.set_tooltip(tooltip)

    def destroy(self) -> bool:
        self.stop_animation()
        self.hide()
        self._balloon_hicon = None
        self._hicon = None
        return super().destroy()

    def _force_update(self) -> bool:
        return bool(shell32.Shell_NotifyIconW(ctyped.const.NIM_MODIFY, ctyped.byref(self._data)))

    def _update(self) -> bool:
        return self._show and bool(self._force_update() or shell32.Shell_NotifyIconW(
            ctyped.const.NIM_ADD, ctyped.byref(self._data)))

    @classmethod
    def update(cls):
        for self in cls._selves.values():
            self._update()

    def is_animated(self) -> bool:
        return self._animation_frames is not None

    def is_shown(self, exclude_flyout: bool = True) -> bool:
        return not bool(shell32.Shell_NotifyIconGetRect(ctyped.byref(ctyped.struct.NOTIFYICONIDENTIFIER(
            hWnd=self._hwnd, uID=self._id)), ctyped.byref(ctyped.struct.RECT()))) if exclude_flyout else self._force_update()

    def _set_hicon(self, hicon: Optional[ctyped.type.HICON] = None) -> bool:
        self._data.hIcon = hicon
        return self._update()

    def set_icon(self, res_or_path_or_bitmap: int | str | _gdiplus.Bitmap) -> bool:
        self.stop_animation()
        if isinstance(res_or_path_or_bitmap, int):
            self._hicon = _handle.HICON.from_idi(res_or_path_or_bitmap)
        else:
            self._hicon = _load_bitmap(res_or_path_or_bitmap).get_hicon()
        self._set_hicon(self._hicon)
        return bool(self._hicon)

    def set_tooltip(self, tooltip: str) -> bool:
        self._data.szTip = tooltip
        return self._update()

    def _get_animation_frames(self, bitmap: _gdiplus.Bitmap) -> \
            Iterator[Optional[tuple[int, _handle.HICON]]]:
        delays = _gdiplus.image_get_property(bitmap, ctyped.const.PropertyTagFrameDelay)
        frames = tuple((delays[index] * 10, bitmap.get_hicon())
                       for index in _gdiplus.image_iter_frames(bitmap))
        while not self._animation_stop:
            yield from frames
        self.stop_animation()
        yield

    def _set_next_frame(self, *_):
        try:
            delay, hicon = next(self._animation_frames)
        except TypeError:
            pass
        else:
            self._set_hicon(hicon)
            user32.SetTimer(self._hwnd, self._id, int(
                delay / self._animation_speed), self._animation_proc)

    def start_animation(self, path_or_bitmap: str | _gdiplus.Bitmap):
        self.stop_animation()
        self._animation_stop = False
        self._animation_frames = self._get_animation_frames(_load_bitmap(path_or_bitmap))
        self._set_next_frame()

    def stop_animation(self, force: bool = True):
        self._animation_stop = True
        if force:
            self._animation_frames = None
            user32.KillTimer(self._hwnd, self._id)
            self._set_hicon(self._hicon)

    def set_animation_speed(self, factor: float) -> bool:
        self._animation_speed = factor
        return self._animation_frames is not None

    def show(self) -> bool:
        self._show = True
        self._show = self._update()
        return self._show

    def hide(self) -> bool:
        self._show = not bool(shell32.Shell_NotifyIconW(ctyped.const.NIM_DELETE, ctyped.byref(self._data)))
        return not self._show

    def show_balloon(self, title: str, text: str = '',
                     res_or_path_or_bitmap: int | str | _gdiplus.Bitmap = SystemTrayIcon.BALLOON_NONE,
                     silent: bool = False) -> bool:
        flags = self._data.uFlags
        hicon = self._hicon
        self._data.uFlags = ctyped.const.NIF_INFO | ctyped.const.NIF_ICON
        self._data.hIcon = self._hicon
        if not text:
            text = title
            title = ''
        self._data.szInfo = text
        self._data.szInfoTitle = title
        if not isinstance(res_or_path_or_bitmap, int):
            self._balloon_hicon = self._data.hBalloonIcon = _load_bitmap(res_or_path_or_bitmap).get_hicon()
            res_or_path_or_bitmap = ctyped.const.NIIF_USER
        self._data.dwInfoFlags = res_or_path_or_bitmap | ctyped.const.NIIF_RESPECT_QUIET_TIME
        if silent:
            self._data.dwInfoFlags |= ctyped.const.NIIF_NOSOUND
        try:
            return self.show()
        finally:
            self._data.uFlags = flags
            self._set_hicon(hicon)


class Menu(_Control):
    _selves: dict[int, Menu]

    _hbrush: Optional[_handle.HBRUSH] = None

    def __init__(self, *, _gui: Optional[Gui] = None):
        self._hwnd = self._attach(_gui)
        self._hmenu = _handle.HMENU.from_type()
        if not user32.SetMenuInfo(self._hmenu, ctyped.byref(ctyped.struct.MENUINFO(
                fMask=ctyped.const.MIM_STYLE, dwStyle=ctyped.const.MNS_NOTIFYBYPOS))):
            raise RuntimeError(f"Cannot initialize {type(self).__name__!r}")
        self._hmenu.set_hwnd(self._hwnd)
        self._items: list[MenuItem] = []
        super().__init__(self._hmenu.value)

    def __contains__(self, id_or_item: int | MenuItem):
        return self.get_item(id_or_item) is not None

    def __bool__(self):
        return bool(self._items)

    def __len__(self):
        return len(self._items)

    def __getitem__(self, pos: int | slice) -> MenuItem | tuple[MenuItem, ...]:
        items: MenuItem | list[MenuItem] = self._items[pos]
        return tuple(items) if isinstance(pos, slice) else items

    def __delitem__(self, pos_or_item: int | slice | MenuItem) -> bool:
        if isinstance(pos_or_item, slice):
            deleted = True
            for item in self[pos_or_item]:
                deleted = self.__delitem__(item) and deleted
            return deleted
        else:
            return self.remove_item(pos_or_item, True)

    def __iter__(self) -> Iterator[MenuItem]:
        return iter(self._items)

    def destroy(self) -> bool:
        self._items.clear()
        self._hmenu = None
        self._hbrush = None
        return super().destroy()

    def get_item_count(self) -> int:
        return self._hmenu.get_item_count()

    def get_item(self, id_or_pos_or_item: int | MenuItem,
                 default=None, by_pos: bool = False) -> Optional[MenuItem]:
        if by_pos:
            if id_or_pos_or_item >= 0:
                try:
                    return self._items[id_or_pos_or_item]
                except IndexError:
                    pass
        else:
            if isinstance(id_or_pos_or_item, int):
                id_or_pos_or_item = MenuItem.get(id_or_pos_or_item)
            if id_or_pos_or_item and self is id_or_pos_or_item.get_menu():
                return id_or_pos_or_item
        return default

    # noinspection PyShadowingBuiltins
    def append_item(self, text: Optional[str] = None, image_res_or_path: Optional[int | str] = None,
                    submenu: Optional[Menu] = None, enable: bool = True, check: Optional[bool] = None,
                    type: int = MenuItemType.NORMAL) -> Optional[MenuItem]:
        return self.insert_item(self.get_item_count(), text, image_res_or_path, submenu, enable, check, type)

    # noinspection PyShadowingBuiltins
    def insert_item(self, pos: int, text: Optional[str] = None, image_res_or_path: Optional[int | str] = None,
                    submenu: Optional[Menu] = None, enable: bool = True, check: Optional[bool] = None,
                    type: int = MenuItemType.NORMAL) -> Optional[MenuItem]:
        item = MenuItem(self, type, gui=Gui.get(self._hwnd))
        if user32.InsertMenuW(self._hmenu, pos, ctyped.const.MF_BYPOSITION, item.get_id(), None):
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
                if type in (MenuItemType.CHECK, MenuItemType.RADIO):
                    if check is None:
                        check = True
                    item.check(check)
                item.enable(enable)
            return item

    def remove_item(self, id_or_pos_or_item: int | MenuItem, by_pos: bool = False) -> bool:
        if isinstance(id_or_pos_or_item, MenuItem):
            id_or_pos_or_item = id_or_pos_or_item.get_id()
            by_pos = False
        removed = self._hmenu.remove_item(id_or_pos_or_item, by_pos)
        if removed:
            self._items.remove(self.get_item(id_or_pos_or_item, by_pos))
        return removed

    def clear_items(self) -> int:
        count = 0
        for item in tuple(self):
            count += self.remove_item(item)
        return count

    def show(self, pos: Optional[Iterable[int, int]] = None, timeout: Optional[float] = None) -> bool:
        if pos is None:
            point = ctyped.struct.POINT()
            user32.GetCursorPos(ctyped.byref(point))
            pos = point.x, point.y
        timer = threading.Timer(timeout, self.hide)
        timer.start()
        try:
            return bool(self._hmenu.track(*pos))
        finally:
            timer.cancel()

    def hide(self) -> bool:
        return self._hmenu.untrack()

    def _get_data(self, mim: int) -> Any:
        info = ctyped.struct.MENUINFO(fMask=mim)
        if user32.GetMenuInfo(self._hmenu, ctyped.byref(info)):
            return getattr(info, _MIM_TO_FIELD[mim])

    def get_background_color(self) -> Optional[tuple[int, int, int]]:
        if info := self._get_data(ctyped.const.MIM_BACKGROUND):
            return _handle.HBRUSH.get_rgb(info)

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
        setattr(info, _MIM_TO_FIELD[mim], data)
        return bool(user32.SetMenuInfo(self._hmenu, ctyped.byref(info)))

    def set_background_color(self, color_or_rgb: int | tuple[int, int, int], recursive: bool = True) -> bool:
        self._hbrush = _handle.HBRUSH.from_color(color_or_rgb) if isinstance(
            color_or_rgb, int) else _handle.HBRUSH.from_rgb(*color_or_rgb)
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


class MenuItem(_Control):
    _selves: dict[int, MenuItem]
    _id_gen = _IDGenerator()

    _tooltip_text: str = ''
    _tooltip_title: str = ''
    _tooltip_icon: Optional[int | _handle.HICON] = None
    _uid: int | str = 0

    def __init__(self, menu: Menu, type_: int, *, gui: Optional[Gui] = None):
        self._hwnd = self._attach(gui)
        self._tooltip_proc = ctyped.type.TIMERPROC(self._show_tooltip)
        self._menu = menu
        self._type = type_
        self._hbmps: list[Optional[_handle.HBITMAP]] = [None] * 3
        super().__init__(next(self._id_gen))

    def destroy(self) -> bool:
        self._menu.remove_item(self)
        self._tooltip_icon = None
        return super().destroy()

    def _show_tooltip(self, *_):
        user32.KillTimer(self._hwnd, _TID_MENU_ITEM_TOOLTIP)
        if self._tooltip_text and self.is_highlighted():
            rect = ctyped.struct.RECT()
            user32.GetMenuItemRect(self._hwnd, self._menu.get_id(),
                                   self.get_pos(), ctyped.byref(rect))
            pt = ctyped.struct.POINT()
            user32.GetCursorPos(ctyped.byref(pt))
            if rect.left <= pt.x <= rect.right and rect.top <= pt.y <= rect.bottom:
                pos = None
            else:
                pos = (rect.left + int((rect.right - rect.left) / 2),
                       rect.top + int((rect.bottom - rect.top) / 2))
            # noinspection PyProtectedMember
            Gui.get(self._hwnd)._show_menu_item_tooltip(
                self._tooltip_text, self._tooltip_title, int(self._tooltip_icon), pos)

    def get_menu(self) -> Menu:
        return self._menu

    def get_type(self) -> int:
        return self._type

    def _get_image(self, res_or_path_or_bitmap: int | str | _gdiplus.Bitmap,
                   index: int, resize: bool) -> int:
        if not isinstance(res_or_path_or_bitmap, int):  # FIXME check item cannot have image/icon
            bitmap = _load_bitmap(res_or_path_or_bitmap)
            if bitmap:
                if resize and not (bitmap.get_width() == bitmap.get_height() == _MENU_ITEM_IMAGE_SIZE):
                    bitmap = _gdiplus.bitmap_from_bitmap(
                        bitmap, _MENU_ITEM_IMAGE_SIZE, _MENU_ITEM_IMAGE_SIZE)
                res_or_path_or_bitmap = bitmap.get_hbitmap()
                self._hbmps[index] = res_or_path_or_bitmap
                res_or_path_or_bitmap = res_or_path_or_bitmap.value
            else:
                res_or_path_or_bitmap = 0
        return res_or_path_or_bitmap

    def _get_datas(self, miim: int, info: Optional[ctyped.struct.MENUITEMINFOW] = None) -> Optional[tuple]:
        if info is None:
            info = ctyped.struct.MENUITEMINFOW()
        info.fMask = miim
        if user32.GetMenuItemInfoW(self._menu.get_id(), self._id, False, ctyped.byref(info)):
            return tuple(getattr(info, field) for field in _MIIM_TO_FIELDS[miim])

    def _get_icon(self) -> Optional[_handle.HBITMAP]:
        if datas := self._get_datas(ctyped.const.MIIM_BITMAP):
            return _handle.HBITMAP(datas[0])

    def _get_check_icons(self) -> Optional[tuple[_handle.HBITMAP, _handle.HBITMAP]]:
        if datas := self._get_datas(ctyped.const.MIIM_CHECKMARKS):
            return _handle.HBITMAP(datas[0]), _handle.HBITMAP(datas[1])

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
        if (datas := self._get_datas(ctyped.const.MIIM_SUBMENU)) and datas[0]:
            return Menu.get(datas[0])

    def _set_datas(self, miim: int, datas: Iterable) -> bool:
        info = ctyped.struct.MENUITEMINFOW(fMask=miim)
        for field, data in zip(_MIIM_TO_FIELDS[miim], datas):
            setattr(info, field, data)
        return bool(user32.SetMenuItemInfoW(self._menu.get_id(), self._id, False, ctyped.byref(info)))

    def set_icon(self, res_or_path_or_bitmap: int | str | _gdiplus.Bitmap, resize: bool = True) -> bool:
        return self._set_datas(ctyped.const.MIIM_BITMAP, (self._get_image(res_or_path_or_bitmap, 0, resize),))

    def _set_check_icons(self, res_or_path_or_bitmap_checked: Optional[int | str | _gdiplus.Bitmap],
                         res_or_path_or_bitmap_unchecked: Optional[int | str | _gdiplus.Bitmap], resize: bool) -> bool:
        return self._set_datas(ctyped.const.MIIM_CHECKMARKS, (
            self._get_image(res_or_path_or_bitmap_checked, 1, resize),
            self._get_image(res_or_path_or_bitmap_unchecked, 2, resize)))

    def _set_types(self, broken: Optional[bool] = None, radio: Optional[bool] = None,
                   right_aligned: Optional[bool] = None, right_justified: Optional[bool] = None) -> bool:
        types_ = self.get_types()
        flags = 0
        if types_[0] if broken is None else broken:
            flags |= ctyped.const.MF_MENUBREAK
        if types_[1] if radio is None else radio:
            flags |= ctyped.const.MFT_RADIOCHECK
        if types_[2] if right_aligned is None else right_aligned:
            flags |= ctyped.const.MFT_RIGHTORDER
        if types_[3] if right_justified is None else right_justified:
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
        if states is not None:
            flags = ctyped.const.MFS_ENABLED if (states[0] if enable is None else enable) else ctyped.const.MFS_DISABLED
            flags |= ctyped.const.MFS_HILITE if (
                states[1] if highlight is None else highlight) else ctyped.const.MFS_UNHILITE
            flags |= ctyped.const.MFS_CHECKED if (states[2] if check is None else check) else ctyped.const.MFS_UNCHECKED
            if states[3] if default is None else default:
                flags |= ctyped.const.MFS_DEFAULT
            return self._set_datas(ctyped.const.MIIM_STATE, (flags,))
        return False

    def enable(self, enable: bool = True) -> bool:
        return self._set_states(enable)

    def highlight(self, highlight: bool = True) -> bool:
        return self._set_states(highlight=highlight)

    def _check(self, check: bool = True) -> bool:
        return self._set_states(check=check)

    def set_default(self, default: bool = True) -> bool:
        return self._set_states(default=default)

    def set_text(self, text: str) -> bool:  # TODO removes icon (?)
        return self._set_datas(ctyped.const.MIIM_TYPE, (ctyped.const.MFT_STRING, text))

    def set_image(self, res_or_path_or_bitmap: int | str | _gdiplus.Bitmap) -> bool:
        return self._set_datas(ctyped.const.MIIM_TYPE, (
            ctyped.const.MFT_BITMAP, ctyped.type.LPWSTR(self._get_image(res_or_path_or_bitmap, 0, False))))

    def _set_separator(self) -> bool:
        return self._set_datas(ctyped.const.MIIM_TYPE, (ctyped.const.MFT_SEPARATOR,))

    def set_submenu(self, submenu: Menu) -> bool:
        return self._set_datas(ctyped.const.MIIM_SUBMENU, (submenu.get_id(),))

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

    def set_checked_icon(self, res_or_path: Optional[int | str] = None, resize: bool = True) -> bool:
        return self._set_check_icons(res_or_path, self._hbmps[2], resize)

    def set_unchecked_icon(self, res_or_path: Optional[int | str] = None, resize: bool = True) -> bool:
        return self._set_check_icons(self._hbmps[1], res_or_path, resize)

    def set_tooltip(self, text: str, title: str = '',  # TODO wrong position with scrollbar
                    icon_res_or_path_or_bitmap: int | str | _gdiplus.Bitmap = MenuItemTooltipIcon.NONE):
        if not text:
            logger.warning('Tooltip text cannot be empty')
        if not title and icon_res_or_path_or_bitmap:
            logger.warning('Tooltip title cannot be empty when icon is set')
        self._tooltip_text = text
        self._tooltip_title = title
        if not isinstance(icon_res_or_path_or_bitmap, int):
            icon_res_or_path_or_bitmap = _gdiplus.bitmap_from_bitmap(
                _load_bitmap(icon_res_or_path_or_bitmap),
                _TOOLTIP_ICON_SIZE, _TOOLTIP_ICON_SIZE, True).get_hicon()
            if not icon_res_or_path_or_bitmap:
                icon_res_or_path_or_bitmap = MenuItemTooltipIcon.NONE
        self._tooltip_icon = icon_res_or_path_or_bitmap

    def set_uid(self, uid: int | str):
        self._uid = uid

    def get_uid(self) -> int | str:
        return self._uid


atexit.register(_bitmap_from_file.cache_clear)
