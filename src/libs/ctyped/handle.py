from __future__ import annotations as _

from typing import Optional as _Optional

from . import const as _const, lib as _lib, macro as _macro, struct as _struct, type as _type
from ._utils import _byref, _sizeof


class HSTRING(_type.HSTRING):
    def __del__(self):
        _lib.Combase.WindowsDeleteString(self)

    def __str__(self):
        return _lib.Combase.WindowsGetStringRawBuffer(self, None)

    @classmethod
    def from_string(cls, string: str = ''):
        self = cls()
        _lib.Combase.WindowsCreateString(string, len(string), _byref(self))
        return self


class HDC(_type.HDC):
    _hwnd = None
    _selected = None

    def __del__(self):
        _lib.User32.ReleaseDC(self._hwnd, self)
        if self._selected:
            _lib.Gdi32.SelectObject(self, self._selected)
            _lib.Gdi32.DeleteDC(self)

    @classmethod
    def from_hwnd(cls, hwnd: _Optional[_type.HWND] = None) -> HDC:
        return cls(_lib.User32.GetDC(hwnd))

    @classmethod
    def from_hbitmap(cls, hbitmap: _type.HBITMAP) -> HDC:
        self = cls(_lib.Gdi32.CreateCompatibleDC(None))
        self._selected = _lib.Gdi32.SelectObject(self, hbitmap)
        return self


class HICON(_type.HICON):
    def __del__(self):
        _lib.User32.DestroyIcon(self)

    @classmethod
    def from_res(cls, idi: int, hinstance: _Optional[_type.HINSTANCE] = None) -> HICON:
        return cls(_lib.User32.LoadIconW(hinstance, _macro.MAKEINTRESOURCEW(idi)))


class HBITMAP(_type.HBITMAP):
    _width = None
    _height = None

    def __del__(self):
        _lib.Gdi32.DeleteObject(self)

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
        return cls(_lib.Gdi32.CreateBitmap(width, height, 1, byte * 8, None))

    def _fill_dimensions(self):
        bitmap = _struct.BITMAP()
        if not _lib.Gdi32.GetObjectW(self, _sizeof(_struct.BITMAP), _byref(bitmap)):
            self._width = bitmap.bmWidth
            self._height = bitmap.bmHeight

    def get_hdc(self) -> HDC:
        return HDC.from_hbitmap(self)


class HMENU(_type.HMENU):
    _by_mf = _const.MF_BYCOMMAND, _const.MF_BYPOSITION

    def __del__(self):
        _lib.User32.DestroyMenu(self)

    @classmethod
    def from_type(cls, popup: bool = True) -> HMENU:
        return cls(_lib.User32.CreatePopupMenu() if popup else _lib.User32.CreateMenu())

    @classmethod
    def from_hwnd(cls, hwnd: _type.HWND) -> HMENU:
        return cls(_lib.User32.GetMenu(hwnd))

    @classmethod
    def from_res(cls, idm: int, hinstance: _Optional[_type.HINSTANCE] = None) -> HMENU:
        return cls(_lib.User32.LoadMenuW(hinstance, _macro.MAKEINTRESOURCEW(idm)))

    def get_item_count(self):
        return _lib.User32.GetMenuItemCount(self)

    def get_item_id(self, pos: int) -> bool:
        return bool(_lib.User32.GetMenuItemID(self, pos))

    def get_item_state(self, id_or_pos: int, by_pos: bool = False) -> int:
        return _lib.User32.GetMenuState(self, id_or_pos, self._by_mf[by_pos])

    def get_item_string(self, id_or_pos: int, by_pos: bool = False) -> str:
        sz = _lib.User32.GetMenuStringW(self, id_or_pos, None, 0, self._by_mf[by_pos]) + 1
        buff = _type.LPWSTR('\0' * sz)
        _lib.User32.GetMenuStringW(self, id_or_pos, buff, sz, self._by_mf[by_pos])
        return buff.value

    def get_item_submenu(self, pos: int) -> HMENU:
        return type(self)(_lib.User32.GetSubMenu(self, pos))

    def check_item(self, id_or_pos: int, check: bool = True, by_pos: bool = False) -> bool:
        return bool(_lib.User32.CheckMenuItem(self, id_or_pos, self._by_mf[by_pos] | (
            _const.MF_CHECKED if check else _const.MF_UNCHECKED)))

    def set_default_item(self, id_or_pos: int, by_pos: bool = False) -> bool:
        return bool(_lib.User32.SetMenuDefaultItem(self, id_or_pos, by_pos))
