from __future__ import annotations as _

from typing import Optional as _Optional

from . import _func
from . import _macro
from . import _struct
from . import _type
from .__head__ import _byref
from .__head__ import _sizeof


class HSTRING(_type.HSTRING):
    def __del__(self):
        _func.combase.WindowsDeleteString(self)

    def __str__(self):
        return _func.combase.WindowsGetStringRawBuffer(self, None)

    @staticmethod
    def from_string(string: str = ''):
        self = HSTRING()
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

    @staticmethod
    def from_hwnd(hwnd: _Optional[_type.HWND] = None) -> HDC:
        return HDC(_func.user32.GetDC(hwnd))

    @staticmethod
    def from_hbitmap(hbitmap: _type.HBITMAP) -> HDC:
        self = HDC()
        self.value = _func.gdi32.CreateCompatibleDC(None)
        self._selected = _func.gdi32.SelectObject(self, hbitmap)
        return self


class HICON(_type.HICON):
    def __del__(self):
        _func.user32.DestroyIcon(self)

    @staticmethod
    def from_idi(idi: int):
        return HICON(_func.user32.LoadIconW(None, _macro.MAKEINTRESOURCEW(idi)))


class HBITMAP(_type.HBITMAP):
    _width = None
    _height = None
    _hdc = None

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

    @property
    def hdc(self) -> HDC:
        if self._hdc is None:
            self._hdc = HDC.from_hbitmap(self)
        return self._hdc

    @hdc.deleter
    def hdc(self):
        self._hdc = None

    @staticmethod
    def from_dimension(width: int = 0, height: int = 0, byte: int = 4) -> HBITMAP:
        self = HBITMAP()
        self.value = _func.gdi32.CreateBitmap(width, height, 1, byte * 8, None)
        return self

    def _fill_dimensions(self):
        bitmap = _struct.BITMAP()
        _func.gdi32.GetObjectW(self, _sizeof(_struct.BITMAP), _byref(bitmap))
        self._width = bitmap.bmWidth
        self._height = bitmap.bmHeight
