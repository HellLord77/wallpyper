from __future__ import annotations as _

from typing import Optional as _Optional

from . import func as _func, macro as _macro, struct as _struct, type as _type
from ._head import _byref, _sizeof


class HSTRING(_type.HSTRING):
    def __del__(self):
        _func.combase.WindowsDeleteString(self)

    def __str__(self):
        return _func.combase.WindowsGetStringRawBuffer(self, None)

    @classmethod
    def from_string(cls, string: str = ''):
        self = cls()
        _func.combase.WindowsCreateString(string, len(string), _byref(self))
        return self


class HDC(_type.HDC):
    _hwnd = None
    _selected = None

    def __del__(self):
        _func.user32.ReleaseDC(self._hwnd, self)
        if self._selected:
            _func.gdi32.SelectObject(self, self._selected)
            _func.gdi32.DeleteDC(self)

    @classmethod
    def from_hwnd(cls, hwnd: _Optional[_type.HWND] = None) -> HDC:
        return cls(_func.user32.GetDC(hwnd))

    @classmethod
    def from_hbitmap(cls, hbitmap: _type.HBITMAP) -> HDC:
        self = cls(_func.gdi32.CreateCompatibleDC(None))
        self._selected = _func.gdi32.SelectObject(self, hbitmap)
        return self


class HICON(_type.HICON):
    def __del__(self):
        _func.user32.DestroyIcon(self)

    @classmethod
    def from_system(cls, idi: int):
        return cls(_func.user32.LoadIconW(None, _macro.MAKEINTRESOURCEW(idi)))


class HBITMAP(_type.HBITMAP):
    _width = None
    _height = None

    def __del__(self):
        _func.gdi32.DeleteObject(self)

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
        return cls(_func.gdi32.CreateBitmap(width, height, 1, byte * 8, None))

    def _fill_dimensions(self):
        bitmap = _struct.BITMAP()
        _func.gdi32.GetObjectW(self, _sizeof(_struct.BITMAP), _byref(bitmap))
        self._width = bitmap.bmWidth
        self._height = bitmap.bmHeight

    def get_hdc(self) -> HDC:
        return HDC.from_hbitmap(self)
