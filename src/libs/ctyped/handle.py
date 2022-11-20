from __future__ import annotations as _

import ctypes as _ctypes
from typing import Optional as _Optional

from . import const as _const, lib as _lib, macro as _macro, struct as _struct, type as _type

_HMENU_MF = _const.MF_BYCOMMAND, _const.MF_BYPOSITION


class HSTRING(_type.HSTRING):
    def __del__(self):
        _lib.ComBase.WindowsDeleteString(self)

    @classmethod
    def from_string(cls, string: str = ''):
        self = cls()
        # noinspection PyTypeChecker
        _lib.ComBase.WindowsCreateString(string, len(string), _ctypes.byref(self))
        return self

    def get_string(self) -> str:
        return _lib.ComBase.WindowsGetStringRawBuffer(self, None)


class HBRUSH(_type.HBRUSH):
    def __del__(self):
        _lib.GDI32.DeleteObject(self)

    @classmethod
    def from_rgb(cls, r: int = 0, g: int = 0, b: int = 0) -> HBRUSH:
        return cls(_lib.GDI32.CreateSolidBrush(_macro.RGB(r, g, b)))

    @classmethod
    def from_color(cls, index: int) -> HBRUSH:
        return cls(_lib.User32.GetSysColorBrush(index))

    def get_rgb(self) -> _Optional[tuple[int, int, int]]:
        brush = _struct.LOGBRUSH()
        # noinspection PyTypeChecker
        if _lib.GDI32.GetObjectW(self, _ctypes.sizeof(brush), _ctypes.byref(brush)):
            return _macro.GetRValue(brush.lbColor), _macro.GetGValue(brush.lbColor), _macro.GetBValue(brush.lbColor)


class HDC(_type.HDC):
    _hwnd = None
    _selected = None

    def __del__(self):
        _lib.User32.ReleaseDC(self._hwnd, self)
        if self._selected:
            _lib.GDI32.SelectObject(self, self._selected)
            _lib.GDI32.DeleteDC(self)

    @classmethod
    def from_hwnd(cls, hwnd: _Optional[_type.HWND] = None) -> HDC:
        return cls(_lib.User32.GetDC(hwnd))

    @classmethod
    def from_hbitmap(cls, hbitmap: _type.HBITMAP) -> HDC:
        self = cls(_lib.GDI32.CreateCompatibleDC(None))
        self._selected = _lib.GDI32.SelectObject(self, hbitmap.value)
        return self


class HCURSOR(_type.HCURSOR):
    def __del__(self):
        _lib.User32.DestroyCursor(self)

    @classmethod
    def from_idc(cls, idc: int, hinstance: _Optional[_type.HINSTANCE] = None) -> HCURSOR:
        return cls(_lib.User32.LoadCursorW(hinstance, _macro.MAKEINTRESOURCEW(idc)))


class HICON(_type.HICON):
    def __del__(self):
        _lib.User32.DestroyIcon(self)

    @classmethod
    def from_idi(cls, idi: int, hinstance: _Optional[_type.HINSTANCE] = None) -> HICON:
        return cls(_lib.User32.LoadIconW(hinstance, _macro.MAKEINTRESOURCEW(idi)))


class HBITMAP(_type.HBITMAP):
    _width = None
    _height = None

    def __del__(self):
        _lib.GDI32.DeleteObject(self.value)

    @property
    def width(self) -> int:
        if self._width is None:
            self._fill_dimensions()
        return self._width

    @property
    def height(self) -> int:
        if self._height is None:
            self._fill_dimensions()
        return self._height

    @classmethod
    def from_dimension(cls, width: int = 0, height: int = 0, byte: int = 4) -> HBITMAP:
        return cls(_lib.GDI32.CreateBitmap(width, height, 1, byte * 8, None))

    def _fill_dimensions(self):
        bitmap = _struct.BITMAP()
        # noinspection PyTypeChecker
        if not _lib.GDI32.GetObjectW(self, _ctypes.sizeof(_struct.BITMAP), _ctypes.byref(bitmap)):
            self._width = bitmap.bmWidth
            self._height = bitmap.bmHeight

    def get_hdc(self) -> HDC:
        return HDC.from_hbitmap(self)


class HMENU(_type.HMENU):
    _hwnd = None

    def __del__(self):
        _lib.User32.DestroyMenu(self)

    @classmethod
    def from_type(cls, popup: bool = True) -> HMENU:
        return cls(_lib.User32.CreatePopupMenu() if popup else _lib.User32.CreateMenu())

    @classmethod
    def from_hwnd(cls, hwnd: _type.HWND, system: bool = False) -> HMENU:
        self = cls(_lib.User32.GetSystemMenu(hwnd, False) if system else _lib.User32.GetMenu(hwnd))
        self._hwnd = hwnd
        return self

    @classmethod
    def from_idm(cls, idm: int, hinstance: _Optional[_type.HINSTANCE] = None) -> HMENU:
        return cls(_lib.User32.LoadMenuW(hinstance, _macro.MAKEINTRESOURCEW(idm)))

    def set_hwnd(self, hwnd: _type.HWND) -> bool:
        self._hwnd = hwnd
        return bool(_lib.User32.SetMenu(hwnd, self))

    def get_item_count(self) -> int:
        return _lib.User32.GetMenuItemCount(self)

    def delete_item(self, id_or_pos: int, by_pos: bool = False) -> bool:
        return bool(_lib.User32.DeleteMenu(self, id_or_pos, _HMENU_MF[by_pos]))

    def remove_item(self, id_or_pos: int, by_pos: bool = False) -> bool:
        return bool(_lib.User32.RemoveMenu(self, id_or_pos, _HMENU_MF[by_pos]))

    def get_item_id(self, pos: int) -> bool:
        return bool(_lib.User32.GetMenuItemID(self, pos))

    def get_item_state(self, id_or_pos: int, by_pos: bool = False) -> int:
        return _lib.User32.GetMenuState(self, id_or_pos, _HMENU_MF[by_pos])

    def get_item_string(self, id_or_pos: int, by_pos: bool = False) -> str:
        sz = _lib.User32.GetMenuStringW(self, id_or_pos, None, 0, _HMENU_MF[by_pos]) + 1
        buff = _type.LPWSTR('\0' * sz)
        _lib.User32.GetMenuStringW(self, id_or_pos, buff, sz, _HMENU_MF[by_pos])
        return buff.value

    def get_item_submenu(self, pos: int) -> HMENU:
        return type(self)(_lib.User32.GetSubMenu(self, pos))

    def enable_item(self, id_or_pos: int, enable: bool = True, gray: bool = True, by_pos: bool = False) -> bool:
        return bool(_lib.User32.EnableMenuItem(self, id_or_pos, _HMENU_MF[by_pos] | (
            _const.MF_ENABLED if enable else (_const.MF_GRAYED if gray else _const.MF_DISABLED))))

    def check_item(self, id_or_pos: int, check: bool = True, by_pos: bool = False) -> bool:
        return bool(_lib.User32.CheckMenuItem(self, id_or_pos, _HMENU_MF[by_pos] | (
            _const.MF_CHECKED if check else _const.MF_UNCHECKED)))

    def set_default_item(self, id_or_pos: int, by_pos: bool = False) -> bool:
        return bool(_lib.User32.SetMenuDefaultItem(self, id_or_pos, by_pos))

    def set_item_bitmaps(self, id_or_pos: int, checked: _Optional[_type.HBITMAP] = None,
                         unchecked: _Optional[_type.HBITMAP] = None, by_pos: bool = False) -> bool:
        return bool(_lib.User32.SetMenuItemBitmaps(self, id_or_pos, _HMENU_MF[by_pos], checked, unchecked))

    def check_radio_item(self, id_or_pos: int, id_or_pos_first: int, id_or_pos_last: int, by_pos: bool = False) -> bool:
        return bool(_lib.User32.CheckMenuRadioItem(
            self, id_or_pos_first, id_or_pos_last, id_or_pos, _HMENU_MF[by_pos]))

    def track(self, x: int, y: int, alignment: int = _const.TPM_LEFTALIGN | _const.TPM_TOPALIGN,
              right_button: bool = False, animation: int = _const.TPM_NOANIMATION) -> int:
        _lib.User32.SetForegroundWindow(self._hwnd)
        return _lib.User32.TrackPopupMenu(self, alignment | (
            _const.TPM_RIGHTBUTTON if right_button else _const.TPM_LEFTBUTTON) | animation, x, y, 0, self._hwnd, None)

    def untrack(self) -> bool:
        return not _lib.User32.SendMessageW(self._hwnd, _const.WM_CANCELMODE, 0, 0)


class HRGN(_type.HRGN):
    def __del__(self):
        _lib.GDI32.DeleteObject(self)

    @classmethod
    def from_corners(cls, x1: int, y1: int, x2: int, y2: int) -> HRGN:
        return cls(_lib.GDI32.CreateRectRgn(x1, y1, x2, y2))

    @classmethod
    def from_rect(cls, rect: _struct.RECT) -> HRGN:
        # noinspection PyTypeChecker
        return cls(_lib.GDI32.CreateRectRgnIndirect(_ctypes.byref(rect)))

    @classmethod
    def from_combination(cls, self: _type.HRGN, other: _type.HRGN, mode: int = _const.RGN_OR) -> HRGN:
        hrgn = cls.from_corners(0, 0, 0, 0)
        _lib.GDI32.CombineRgn(hrgn, self, other, mode)
        return hrgn

    def get_rect(self) -> _struct.RECT:
        rect = _struct.RECT()
        # noinspection PyTypeChecker
        _lib.GDI32.GetRgnBox(self, _ctypes.byref(rect))
        return rect

    def is_empty(self) -> bool:
        # noinspection PyTypeChecker
        return bool(_lib.User32.IsRectEmpty(_ctypes.byref(self.get_rect())))

    def is_equal(self, other: _type.HRGN) -> bool:
        return bool(_lib.GDI32.EqualRgn(self, other))


class HWND(_type.HWND):
    def __del__(self):
        _lib.User32.DestroyWindow(self)

    def is_visible(self) -> bool:
        return bool(_lib.User32.IsWindowVisible(self))

    def send_message(self, msg: int, wparam: int = 0, lparam: int = 0, wait: bool = True) -> int:
        return (_lib.User32.SendMessageW if wait else _lib.User32.PostMessageW)(self, msg, wparam, lparam)

    def show(self, cmd: int = _const.SW_SHOW) -> bool:
        return bool(_lib.User32.ShowWindow(self, cmd))

    def update(self) -> bool:
        return bool(_lib.User32.UpdateWindow(self))
