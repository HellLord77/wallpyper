from __future__ import annotations as _

import ctypes as _ctypes
import dataclasses as _dataclasses
import functools as _functools
import typing as _typing

from . import _ctype
from . import _header


@_dataclasses.dataclass
class GdiplusStartupInput:
    GdiplusVersion: _ctype.UINT32 = 1
    DebugEventCallback: _ctype.DebugEventProc = None
    SuppressBackgroundThread: _ctype.BOOL = False
    SuppressExternalCodecs: _ctype.BOOL = False


@_dataclasses.dataclass
class RGBQUAD:
    rgbBlue: _ctype.BYTE = None
    rgbGreen: _ctype.BYTE = None
    rgbRed: _ctype.BYTE = None
    rgbReserved: _ctype.BYTE = 0


@_dataclasses.dataclass
class BITMAPINFOHEADER:
    biSize: _ctype.DWORD = None
    biWidth: _ctype.LONG = None
    biHeight: _ctype.LONG = None
    biPlanes: _ctype.WORD = 1
    biBitCount: _ctype.WORD = None
    biCompression: _ctype.DWORD = None
    biSizeImage: _ctype.DWORD = None
    biXPelsPerMeter: _ctype.LONG = None
    biYPelsPerMeter: _ctype.LONG = None
    biClrUsed: _ctype.DWORD = None
    biClrImportant: _ctype.DWORD = None


@_dataclasses.dataclass
class BITMAPINFO:
    bmiHeader: BITMAPINFOHEADER = None
    # noinspection PyTypeChecker
    bmiColors: RGBQUAD * 1 = None


@_dataclasses.dataclass
class BITMAP:
    bmType: _ctype.LONG = None
    bmWidth: _ctype.LONG = None
    bmHeight: _ctype.LONG = None
    bmWidthBytes: _ctype.LONG = None
    bmPlanes: _ctype.WORD = None
    bmBitsPixel: _ctype.WORD = None
    bmBits: _ctype.LPVOID = None


@_dataclasses.dataclass
class DIBSECTION:
    dsBm: BITMAP = None
    dsBmih: BITMAPINFOHEADER = None
    dsBitfields: _ctype.DWORD * 3 = None
    dshSection: _ctype.HANDLE = None
    dsOffset: _ctype.DWORD = None


@_dataclasses.dataclass
class GUID:
    Data1: _ctype.c_ulong = None
    Data2: _ctype.c_ushort = None
    Data3: _ctype.c_ushort = None
    Data4: _ctype.c_uchar * 8 = None


@_dataclasses.dataclass
class WALLPAPEROPT:
    dwSize: _ctype.DWORD = None
    dwStyle: _ctype.DWORD = None


@_dataclasses.dataclass
class RECT:
    left: _ctype.LONG = None
    top: _ctype.LONG = None
    right: _ctype.LONG = None
    bottom: _ctype.LONG = None


@_dataclasses.dataclass
class MENUINFO:
    cbSize: _ctype.DWORD = None
    fMask: _ctype.DWORD = None
    dwStyle: _ctype.DWORD = None
    cyMax: _ctype.UINT = 0
    hbrBack: _ctype.HBRUSH = None
    dwContextHelpID: _ctype.DWORD = None
    dwMenuData: _ctype.ULONG_PTR = None


UUID = GUID
IID = GUID
CLSID = GUID


def __getattr__(name: str) -> type[_ctypes.Structure]:
    class Wrapper(_ctypes.Structure):
        _fields_ = tuple((field, _header.resolve_type(type_))
                         for field, type_ in _typing.get_type_hints(_struct[name], _globals).items())
        __defaults__ = tuple((field, getattr(_struct[name], field) or type_) for field, type_ in _fields_)

        def __init__(self, *args, **kwargs):
            for i, field in enumerate(self.__defaults__):
                if i >= len(args) and field[0] not in kwargs:
                    kwargs[field[0]] = field[1]() if callable(field[1]) else field[1]
            super().__init__(*args, **kwargs)

    _functools.update_wrapper(Wrapper, _struct[name], ('__repr__', *_functools.WRAPPER_ASSIGNMENTS), ())
    for var, struct in _struct.items():
        if _struct[name] is struct:
            _globals[var] = Wrapper
    return _globals[name]


_struct = _header.init(globals())
_globals = _header.Dict(globals(), __getattr__)
if _header.INIT:
    for _struct_ in _struct:
        __getattr__(_struct_)
