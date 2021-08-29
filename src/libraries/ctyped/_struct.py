from __future__ import annotations as _

import ctypes as _ctypes
import dataclasses as _dataclasses
import functools as _functools
import typing as _typing

from . import _const
from . import _header
from . import _type


@_dataclasses.dataclass
class GdiplusStartupInput:
    GdiplusVersion: _type.UINT32 = 1
    DebugEventCallback: _type.DebugEventProc = None
    SuppressBackgroundThread: _type.BOOL = False
    SuppressExternalCodecs: _type.BOOL = False


@_dataclasses.dataclass
class RGBQUAD:
    rgbBlue: _type.BYTE = None
    rgbGreen: _type.BYTE = None
    rgbRed: _type.BYTE = None
    rgbReserved: _type.BYTE = 0


@_dataclasses.dataclass
class BITMAPINFOHEADER:
    biSize: _type.DWORD = None
    biWidth: _type.LONG = None
    biHeight: _type.LONG = None
    biPlanes: _type.WORD = 1
    biBitCount: _type.WORD = None
    biCompression: _type.DWORD = None
    biSizeImage: _type.DWORD = None
    biXPelsPerMeter: _type.LONG = None
    biYPelsPerMeter: _type.LONG = None
    biClrUsed: _type.DWORD = None
    biClrImportant: _type.DWORD = None


@_dataclasses.dataclass
class BITMAPINFO:
    bmiHeader: BITMAPINFOHEADER = None
    # noinspection PyTypeChecker
    bmiColors: RGBQUAD * 1 = None


@_dataclasses.dataclass
class BITMAP:
    bmType: _type.LONG = None
    bmWidth: _type.LONG = None
    bmHeight: _type.LONG = None
    bmWidthBytes: _type.LONG = None
    bmPlanes: _type.WORD = None
    bmBitsPixel: _type.WORD = None
    bmBits: _type.LPVOID = None


@_dataclasses.dataclass
class DIBSECTION:
    dsBm: BITMAP = None
    dsBmih: BITMAPINFOHEADER = None
    dsBitfields: _type.DWORD * 3 = None
    dshSection: _type.HANDLE = None
    dsOffset: _type.DWORD = None


@_dataclasses.dataclass
class GUID:
    Data1: _type.c_ulong = None
    Data2: _type.c_ushort = None
    Data3: _type.c_ushort = None
    Data4: _type.c_uchar * 8 = None


@_dataclasses.dataclass
class WALLPAPEROPT:
    dwSize: _type.DWORD = None
    dwStyle: _type.DWORD = None


@_dataclasses.dataclass
class RECT:
    left: _type.LONG = None
    top: _type.LONG = None
    right: _type.LONG = None
    bottom: _type.LONG = None


@_dataclasses.dataclass
class MENUINFO:
    cbSize: _type.DWORD = None
    fMask: _type.DWORD = None
    dwStyle: _type.DWORD = None
    cyMax: _type.UINT = 0
    hbrBack: _type.HBRUSH = None
    dwContextHelpID: _type.DWORD = None
    dwMenuData: _type.ULONG_PTR = None


# noinspection PyPep8Naming
@_dataclasses.dataclass
class HSTRING__:
    unused: _type.c_int = None


@_dataclasses.dataclass
class SHITEMID:
    cb: _type.USHORT = None
    abID: _type.BYTE * 1 = None


@_dataclasses.dataclass
class ITEMIDLIST:
    mkid: SHITEMID = None


@_dataclasses.dataclass
class MENUITEMINFOA:
    cbSize: _type.UINT = None
    fMask: _type.UINT = None
    fType: _type.UINT = None
    fState: _type.UINT = None
    wID: _type.UINT = None
    hSubMenu: _type.HMENU = None
    hbmpChecked: _type.HBITMAP = None
    hbmpUnchecked: _type.HBITMAP = None
    dwItemData: _type.ULONG_PTR = None
    dwTypeData: _type.LPSTR = None
    cch: _type.UINT = None
    if _const.WINVER >= 0x0500:
        hbmpItem: _type.HBITMAP = None


@_dataclasses.dataclass
class MENUITEMINFOW:
    cbSize: _type.UINT = None
    fMask: _type.UINT = None
    fType: _type.UINT = None
    fState: _type.UINT = None
    wID: _type.UINT = None
    hSubMenu: _type.HMENU = None
    hbmpChecked: _type.HBITMAP = None
    hbmpUnchecked: _type.HBITMAP = None
    dwItemData: _type.ULONG_PTR = None
    dwTypeData: _type.LPWSTR = None
    cch: _type.UINT = None
    if _const.WINVER >= 0x0500:
        hbmpItem: _type.HBITMAP = None


UUID = GUID
IID = GUID
CLSID = GUID


def __getattr__(name: str) -> type[_ctypes.Structure]:
    _globals.hasattr(name)

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
    _globals[name] = Wrapper
    return _globals[name]


_struct = _header.init(globals())
_globals = _header.Globals(_struct, globals(), __getattr__)
if _header.INIT:
    for _struct_ in _struct:
        __getattr__(_struct_)
