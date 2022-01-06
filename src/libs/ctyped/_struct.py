from __future__ import annotations as _

import ctypes as _ctypes
import dataclasses as _dataclasses
import functools as _functools
import itertools as _itertools
import typing as _typing

from . import _const
from . import _type
from . import _union
from . import _union2
from .__head__ import _Globals
from .__head__ import _resolve_type

_ASSIGNED = ('__repr__', *_functools.WRAPPER_ASSIGNMENTS)


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


@_dataclasses.dataclass
class NOTIFYICONDATAA:
    cbSize: _type.DWORD = None
    hWnd: _type.HWND = None
    uID: _type.UINT = None
    uFlags: _type.UINT = None
    uCallbackMessage: _type.UINT = None
    hIcon: _type.HICON = None
    if _const.NTDDI_VERSION < _const.NTDDI_WIN2K:
        szTip: _type.CHAR * 64 = None
    if _const.NTDDI_VERSION >= _const.NTDDI_WIN2K:
        szTip: _type.CHAR * 128 = None
        dwState: _type.DWORD = None
        dwStateMask: _type.DWORD = None
        szInfo: _type.CHAR * 256 = None
        # noinspection PyProtectedMember
        if not _const._SHELL_EXPORTS_INTERNALAPI_H_:
            u: _union.NOTIFYICONDATA_u = None
        szInfoTitle: _type.CHAR * 64 = None
        dwInfoFlags: _type.DWORD = None
    if _const.NTDDI_VERSION >= _const.NTDDI_WINXP:
        guidItem: GUID = None
    if _const.NTDDI_VERSION >= _const.NTDDI_VISTA:
        hBalloonIcon: _type.HICON = None


@_dataclasses.dataclass
class NOTIFYICONDATAW:
    cbSize: _type.DWORD = None
    hWnd: _type.HWND = None
    uID: _type.UINT = None
    uFlags: _type.UINT = None
    uCallbackMessage: _type.UINT = None
    hIcon: _type.HICON = None
    if _const.NTDDI_VERSION < _const.NTDDI_WIN2K:
        szTip: _type.WCHAR * 64 = None
    if _const.NTDDI_VERSION >= _const.NTDDI_WIN2K:
        szTip: _type.WCHAR * 128 = None
        dwState: _type.DWORD = None
        dwStateMask: _type.DWORD = None
        szInfo: _type.WCHAR * 256 = None
        # noinspection PyProtectedMember
        if not _const._SHELL_EXPORTS_INTERNALAPI_H_:
            u: _union.NOTIFYICONDATA_u = None
        szInfoTitle: _type.WCHAR * 64 = None
        dwInfoFlags: _type.DWORD = None
    if _const.NTDDI_VERSION >= _const.NTDDI_WINXP:
        guidItem: GUID = None
    if _const.NTDDI_VERSION >= _const.NTDDI_VISTA:
        hBalloonIcon: _type.HICON = None


@_dataclasses.dataclass
class WNDCLASSEXA:
    cbSize: _type.UINT = None
    style: _type.UINT = None
    lpfnWndProc: _type.WNDPROC = None
    cbClsExtra: _type.c_int = None
    cbWndExtra: _type.c_int = None
    hInstance: _type.HINSTANCE = None
    hIcon: _type.HINSTANCE = None
    hCursor: _type.HCURSOR = None
    hbrBackground: _type.HBRUSH = None
    lpszMenuName: _type.LPCSTR = None
    lpszClassName: _type.LPCSTR = None
    hIconSm: _type.HICON = None


@_dataclasses.dataclass
class WNDCLASSEXW:
    cbSize: _type.UINT = None
    style: _type.UINT = None
    lpfnWndProc: _type.WNDPROC = None
    cbClsExtra: _type.c_int = None
    cbWndExtra: _type.c_int = None
    hInstance: _type.HINSTANCE = None
    hIcon: _type.HINSTANCE = None
    hCursor: _type.HCURSOR = None
    hbrBackground: _type.HBRUSH = None
    lpszMenuName: _type.LPCWSTR = None
    lpszClassName: _type.LPCWSTR = None
    hIconSm: _type.HICON = None


@_dataclasses.dataclass
class POINT:
    x: _type.LONG = None
    y: _type.LONG = None


@_dataclasses.dataclass
class MSG:
    hwnd: _type.HWND = None
    message: _type.UINT = None
    wParam: _type.WPARAM = None
    lParam: _type.WPARAM = None
    time: _type.DWORD = None
    pt: POINT = None
    lPrivate: _type.DWORD = None


@_dataclasses.dataclass
class PropertyItem:
    id: _type.PROPID = None
    length: _type.ULONG = None
    type: _type.WORD = None
    value: _type.VOID = None


@_dataclasses.dataclass
class FILETIME:
    dwLowDateTime: _type.DWORD = None
    dwHighDateTime: _type.DWORD = None


# noinspection PyPep8Naming
@_dataclasses.dataclass
class WIN32_FIND_DATAA:
    dwFileAttributes: _type.DWORD = None
    ftCreationTime: FILETIME = None
    ftLastAccessTime: FILETIME = None
    ftLastWriteTime: FILETIME = None
    nFileSizeHigh: _type.DWORD = None
    nFileSizeLow: _type.DWORD = None
    dwReserved0: _type.DWORD = None
    dwReserved1: _type.DWORD = None
    cFileName: _type.CHAR * _const.MAX_PATH = None
    cAlternateFileName: _type.CHAR * 14 = None
    # noinspection PyProtectedMember
    if _const._MAC:
        dwFileType: _type.DWORD = None
        dwCreatorType: _type.DWORD = None
        wFinderFlags: _type.WORD = None


# noinspection PyPep8Naming
@_dataclasses.dataclass
class WIN32_FIND_DATAW:
    dwFileAttributes: _type.DWORD = None
    ftCreationTime: FILETIME = None
    ftLastAccessTime: FILETIME = None
    ftLastWriteTime: FILETIME = None
    nFileSizeHigh: _type.DWORD = None
    nFileSizeLow: _type.DWORD = None
    dwReserved0: _type.DWORD = None
    dwReserved1: _type.DWORD = None
    cFileName: _type.WCHAR * _const.MAX_PATH = None
    cAlternateFileName: _type.WCHAR * 14 = None
    # noinspection PyProtectedMember
    if _const._MAC:
        dwFileType: _type.DWORD = None
        dwCreatorType: _type.DWORD = None
        wFinderFlags: _type.WORD = None


@_dataclasses.dataclass
class PROPERTYKEY:
    fmtid: GUID = None
    pid: _type.DWORD = None


@_dataclasses.dataclass
class CSPLATFORM:
    dwPlatformId: _type.DWORD = None
    dwVersionHi: _type.DWORD = None
    dwVersionLo: _type.DWORD = None
    dwProcessorArch: _type.DWORD = None


# noinspection PyPep8Naming
@_dataclasses.dataclass
class DECIMAL_u_s:
    scale: _type.BYTE = None
    sign: _type.BYTE = None


# noinspection PyPep8Naming
@_dataclasses.dataclass
class DECIMAL_u2_s:
    Lo32: _type.ULONG = None
    Mid32: _type.ULONG = None


@_dataclasses.dataclass
class DECIMAL:
    wReserved: _type.USHORT = None
    u: _union.DECIMAL_u = None
    Hi32: _type.ULONG = None
    u2: _union.DECIMAL_u2 = None


# noinspection PyPep8Naming
@_dataclasses.dataclass
class tag_inner_PROPVARIANT:
    vt: _type.VARTYPE = None
    wReserved1: _type.PROPVAR_PAD1 = None
    wReserved2: _type.PROPVAR_PAD2 = None
    wReserved3: _type.PROPVAR_PAD3 = None
    u: _union.tag_inner_PROPVARIANT_u = None


# noinspection PyPep8Naming
@_dataclasses.dataclass
class PROPVARIANT:
    u: _union2.PROPVARIANT_u = None


UUID = GUID
IID = GUID
CLSID = GUID


def _init(name: str) -> type[_ctypes.Structure]:
    _globals.has_item(name)

    class Wrapper(_ctypes.Structure):
        _fields_ = tuple((name_, _resolve_type(type_))
                         for name_, type_ in _typing.get_type_hints(_globals.vars_[name], _globals).items())
        __defaults__ = tuple((field[0], getattr(_globals.vars_[name], field[0])) for field in _fields_)

        def __init__(self, *args, **kwargs):
            for name_, val in _itertools.islice(self.__defaults__, len(args), None):
                if val is not None and name_ not in kwargs:
                    kwargs[name_] = val
            super().__init__(*args, **kwargs)

    return _functools.update_wrapper(Wrapper, _globals.vars_[name], _ASSIGNED, ())


_globals = _Globals()
