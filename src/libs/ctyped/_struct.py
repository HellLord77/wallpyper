from __future__ import annotations as _

import ctypes as _types
import functools as _functools
import itertools as _itertools
from dataclasses import dataclass as _struct

from . import _const
from . import _type
from . import _union
from .__head__ import _Globals
from .__head__ import _Pointer
from .__head__ import _resolve_type

_ASSIGNED = ('__repr__', *_functools.WRAPPER_ASSIGNMENTS)


@_struct
class GdiplusStartupInput:
    GdiplusVersion: _type.UINT32 = 1
    DebugEventCallback: _type.DebugEventProc = None
    SuppressBackgroundThread: _type.BOOL = False
    SuppressExternalCodecs: _type.BOOL = False


@_struct
class RGBTRIPLE:
    rgbBlue: _type.BYTE = None
    rgbGreen: _type.BYTE = None
    rgbRed: _type.BYTE = None


@_struct
class RGBQUAD:
    rgbBlue: _type.BYTE = None
    rgbGreen: _type.BYTE = None
    rgbRed: _type.BYTE = None
    rgbReserved: _type.BYTE = 0


@_struct
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


@_struct
class BITMAPINFO:
    bmiHeader: BITMAPINFOHEADER = None
    # noinspection PyTypeChecker
    bmiColors: RGBQUAD * 1 = None


@_struct
class BITMAP:
    bmType: _type.LONG = None
    bmWidth: _type.LONG = None
    bmHeight: _type.LONG = None
    bmWidthBytes: _type.LONG = None
    bmPlanes: _type.WORD = None
    bmBitsPixel: _type.WORD = None
    bmBits: _type.LPVOID = None


@_struct
class DIBSECTION:
    dsBm: BITMAP = None
    dsBmih: BITMAPINFOHEADER = None
    dsBitfields: _type.DWORD * 3 = None
    dshSection: _type.HANDLE = None
    dsOffset: _type.DWORD = None


@_struct
class CHOOSECOLORA:
    lStructSize: _type.DWORD = None
    hwndOwner: _type.HWND = None
    hInstance: _type.HWND = None
    rgbResult: _type.COLORREF = None
    lpCustColors: _Pointer[_type.COLORREF] = None
    Flags: _type.DWORD = None
    lCustData: _type.LPARAM = None
    lpfnHook: _type.LPCCHOOKPROC = None
    lpTemplateName: _type.LPCSTR = None


@_struct
class CHOOSECOLORW:
    lStructSize: _type.DWORD = None
    hwndOwner: _type.HWND = None
    hInstance: _type.HWND = None
    rgbResult: _type.COLORREF = None
    lpCustColors: _Pointer[_type.COLORREF] = None
    Flags: _type.DWORD = None
    lCustData: _type.LPARAM = None
    lpfnHook: _type.LPCCHOOKPROC = None
    lpTemplateName: _type.LPCWSTR = None


@_struct
class GUID:
    Data1: _type.c_ulong = None
    Data2: _type.c_ushort = None
    Data3: _type.c_ushort = None
    Data4: _type.c_uchar * 8 = None


@_struct
class WALLPAPEROPT:
    dwSize: _type.DWORD = None
    dwStyle: _type.DWORD = None


@_struct
class RECT:
    left: _type.LONG = None
    top: _type.LONG = None
    right: _type.LONG = None
    bottom: _type.LONG = None


@_struct
class POINT:
    x: _type.LONG = None
    y: _type.LONG = None


@_struct
class SIZE:
    cx: _type.LONG = None
    cy: _type.LONG = None


@_struct
class MENUINFO:
    cbSize: _type.DWORD = None
    fMask: _type.DWORD = None
    dwStyle: _type.DWORD = None
    cyMax: _type.UINT = 0
    hbrBack: _type.HBRUSH = None
    dwContextHelpID: _type.DWORD = None
    dwMenuData: _type.ULONG_PTR = None


@_struct
class SHITEMID:
    cb: _type.USHORT = None
    abID: _type.BYTE * 1 = None


@_struct
class ITEMIDLIST:
    mkid: SHITEMID = None


@_struct
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


@_struct
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


@_struct
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
            U: _union.NOTIFYICONDATA_U = None
        szInfoTitle: _type.CHAR * 64 = None
        dwInfoFlags: _type.DWORD = None
    if _const.NTDDI_VERSION >= _const.NTDDI_WINXP:
        guidItem: GUID = None
    if _const.NTDDI_VERSION >= _const.NTDDI_VISTA:
        hBalloonIcon: _type.HICON = None


@_struct
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
            U: _union.NOTIFYICONDATA_U = None
        szInfoTitle: _type.WCHAR * 64 = None
        dwInfoFlags: _type.DWORD = None
    if _const.NTDDI_VERSION >= _const.NTDDI_WINXP:
        guidItem: GUID = None
    if _const.NTDDI_VERSION >= _const.NTDDI_VISTA:
        hBalloonIcon: _type.HICON = None


@_struct
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


@_struct
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


@_struct
class POINT:
    x: _type.LONG = None
    y: _type.LONG = None


@_struct
class MSG:
    hwnd: _type.HWND = None
    message: _type.UINT = None
    wParam: _type.WPARAM = None
    lParam: _type.WPARAM = None
    time: _type.DWORD = None
    pt: POINT = None
    lPrivate: _type.DWORD = None


@_struct
class PropertyItem:
    id: _type.PROPID = None
    length: _type.ULONG = None
    type: _type.WORD = None
    value: _Pointer[_type.VOID] = None


@_struct
class FILETIME:
    dwLowDateTime: _type.DWORD = None
    dwHighDateTime: _type.DWORD = None


# noinspection PyPep8Naming
@_struct
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
@_struct
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


@_struct
class PROPERTYKEY:
    fmtid: GUID = None
    pid: _type.DWORD = None


@_struct
class CSPLATFORM:
    dwPlatformId: _type.DWORD = None
    dwVersionHi: _type.DWORD = None
    dwVersionLo: _type.DWORD = None
    dwProcessorArch: _type.DWORD = None


# noinspection PyPep8Naming
@_struct
class DECIMAL_U_S:
    scale: _type.BYTE = None
    sign: _type.BYTE = None


# noinspection PyPep8Naming
@_struct
class DECIMAL_U2_S:
    Lo32: _type.ULONG = None
    Mid32: _type.ULONG = None


@_struct
class DECIMAL:
    wReserved: _type.USHORT = None
    U: _union.DECIMAL_U = None
    Hi32: _type.ULONG = None
    U2: _union.DECIMAL_U2 = None


# noinspection PyPep8Naming
@_struct
class PROPVARIANT_U_S:
    vt: _type.VARTYPE = None
    wReserved1: _type.PROPVAR_PAD1 = None
    wReserved2: _type.PROPVAR_PAD2 = None
    wReserved3: _type.PROPVAR_PAD3 = None
    U: _union.PROPVARIANT_U_S_U = None


@_struct
class PROPVARIANT:
    U: _union.PROPVARIANT_U = None


@_struct
class MOUSEINPUT:
    dx: _type.LONG = None
    dy: _type.LONG = None
    mouseData: _type.DWORD = None
    dwFlags: _type.DWORD = None
    time: _type.DWORD = None
    dwExtraInfo: _type.ULONG_PTR = None


@_struct
class KEYBDINPUT:
    wVk: _type.WORD = None
    wScan: _type.WORD = None
    dwFlags: _type.DWORD = None
    time: _type.DWORD = None
    dwExtraInfo: _type.ULONG_PTR = None


@_struct
class HARDWAREINPUT:
    uMsg: _type.DWORD = None
    wParamL: _type.WORD = None
    wParamH: _type.WORD = None


@_struct
class INPUT:
    type: _type.DWORD = None
    U: _union.INPUT_U = None


# noinspection PyPep8Naming
@_struct
class DISPLAY_DEVICEA:
    cb: _type.DWORD = None
    DeviceName: _type.CHAR * 32 = None
    DeviceString: _type.CHAR * 128 = None
    StateFlags: _type.DWORD = None
    DeviceID: _type.CHAR * 128 = None
    DeviceKey: _type.CHAR * 128 = None


# noinspection PyPep8Naming
@_struct
class DISPLAY_DEVICEW:
    cb: _type.DWORD = None
    DeviceName: _type.WCHAR * 32 = None
    DeviceString: _type.WCHAR * 128 = None
    StateFlags: _type.DWORD = None
    DeviceID: _type.WCHAR * 128 = None
    DeviceKey: _type.WCHAR * 128 = None


@_struct
class BROWSEINFOA:
    hwndOwner: _type.HWND = None
    pidlRoot: _Pointer[_Pointer[ITEMIDLIST]] = None
    pszDisplayName: _type.LPSTR = None
    lpszTitle: _type.LPCSTR = None
    ulFlags: _type.UINT = None
    lpfn: _type.BFFCALLBACK = None
    lParam: _type.LPARAM = None
    iImage: _type.c_int = None


@_struct
class BROWSEINFOW:
    hwndOwner: _type.HWND = None
    pidlRoot: _Pointer[_Pointer[ITEMIDLIST]] = None
    pszDisplayName: _type.LPWSTR = None
    lpszTitle: _type.LPCWSTR = None
    ulFlags: _type.UINT = None
    lpfn: _type.BFFCALLBACK = None
    lParam: _type.LPARAM = None
    iImage: _type.c_int = None


@_struct
class PAINTSTRUCT:
    hdc: _type.HDC = None
    fErase: _type.BOOL = None
    rcPaint: RECT = None
    fRestore: _type.BOOL = None
    fIncUpdate: _type.BOOL = None
    rgbReserved: _type.BYTE * 32 = None


# noinspection PyPep8Naming
@_struct
class PICTDESC_U_S:
    hbitmap: _type.HBITMAP = None
    hpal: _type.HPALETTE = None


# noinspection PyPep8Naming
@_struct
class PICTDESC_U_S2:
    hmeta: _type.HMETAFILE = None
    xExt: _type.c_int = None
    yExt: _type.c_int = None


# noinspection PyPep8Naming
@_struct
class PICTDESC_U_S3:
    hicon: _type.HICON = None


# noinspection PyProtectedMember
if _const._WIN32:
    # noinspection PyPep8Naming
    @_struct
    class PICTDESC_U_S4:
        hemf: _type.HMETAFILE = None


@_struct
class PICTDESC:
    cbSizeofstruct: _type.UINT = None
    picType: _type.UINT = None
    U: _union.PICTDESC_U = None


@_struct
class MONITORINFO:
    cbSize: _type.DWORD = None
    rcMonitor: RECT = None
    rcWork: RECT = None
    dwFlags: _type.DWORD = None


@_struct
class MONITORINFOEXA:
    S: MONITORINFO = None
    szDevice: _type.CHAR * _const.CCHDEVICENAME = None


@_struct
class MONITORINFOEXW:
    S: MONITORINFO = None
    szDevice: _type.WCHAR * _const.CCHDEVICENAME = None


# noinspection PyPep8Naming
@_struct
class VARIANT_U_S:
    vt: _type.VARTYPE = None
    wReserved1: _type.WORD = None
    wReserved2: _type.WORD = None
    wReserved3: _type.WORD = None
    U: _union.VARIANT_U_S_U = None


@_struct
class VARIANT:
    U: _union.VARIANT_U = None


# noinspection PyPep8Naming
@_struct
class SP_DEVINFO_DATA:
    cbSize: _type.DWORD = None
    ClassGuid: GUID = None
    DevInst: _type.DWORD = None
    Reserved: _type.ULONG_PTR = None


# noinspection PyPep8Naming
@_struct
class SP_DEVICE_INTERFACE_DATA:
    cbSize: _type.DWORD = None
    InterfaceClassGuid: GUID = None
    Flags: _type.DWORD = None
    Reserved: _type.ULONG_PTR = None


# noinspection PyPep8Naming
@_struct
class SP_DEVICE_INTERFACE_DETAIL_DATA_A:
    cbSize: _type.DWORD = None
    DevicePath: _type.CHAR * _const.ANYSIZE_ARRAY = None


# noinspection PyPep8Naming
@_struct
class SP_DEVICE_INTERFACE_DETAIL_DATA_W:
    cbSize: _type.DWORD = None
    DevicePath: _type.WCHAR * _const.ANYSIZE_ARRAY = None


@_struct
class DEVPROPKEY:
    fmtid: DEVPROPGUID = None
    pid: _type.DEVPROPID = None


@_struct
class BLENDFUNCTION:
    BlendOp: _type.BYTE = None
    BlendFlags: _type.BYTE = None
    SourceConstantAlpha: _type.BYTE = None
    AlphaFormat: _type.BYTE = None


@_struct
class ColorMap:
    oldColor: _type.Color = None
    newColor: _type.Color = None


@_struct
class ColorMatrix:
    m: _type.REAL * 5 * 5 = None


@_struct
class EventRegistrationToken:
    value: _type.c_int64 = None


@_struct
class Rational:
    Numerator: _type.UINT32 = None
    Denominator: _type.UINT32 = None


UUID = GUID
IID = GUID
CLSID = GUID
KNOWNFOLDERID = GUID
DEVPROPGUID = GUID
VARIANTARG = VARIANT


def _init(name: str) -> type[_types.Structure]:
    _globals.check_item(name)

    class Wrapper(_types.Structure):
        _fields_ = tuple((name_, _resolve_type(type_)) for name_, type_ in _globals.get_type_hints(name))
        __defaults__ = tuple((field[0], getattr(_globals.vars_[name], field[0])) for field in _fields_)

        def __init__(self, *args, **kwargs):
            for name_, val in _itertools.islice(self.__defaults__, len(args), None):
                if val is not None and name_ not in kwargs:
                    kwargs[name_] = val
            super().__init__(*args, **kwargs)

    return _functools.update_wrapper(Wrapper, _globals.vars_[name], _ASSIGNED, ())


_globals = _Globals()
