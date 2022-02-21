from __future__ import annotations as _

import ctypes as _ctypes
import functools as _functools
import itertools as _itertools
from dataclasses import dataclass as _struct

from . import const as _const, type as _type, union as _union
from ._head import _Globals, _Pointer, _resolve_type

_DEFAULT = None
_ASSIGNED = ('__repr__', *_functools.WRAPPER_ASSIGNMENTS)


@_struct
class GdiplusStartupInput:
    GdiplusVersion: _type.UINT32 = 1
    DebugEventCallback: _type.DebugEventProc = _DEFAULT
    SuppressBackgroundThread: _type.BOOL = False
    SuppressExternalCodecs: _type.BOOL = False


@_struct
class RGBTRIPLE:
    rgbBlue: _type.BYTE = _DEFAULT
    rgbGreen: _type.BYTE = _DEFAULT
    rgbRed: _type.BYTE = _DEFAULT


@_struct
class RGBQUAD:
    rgbBlue: _type.BYTE = _DEFAULT
    rgbGreen: _type.BYTE = _DEFAULT
    rgbRed: _type.BYTE = _DEFAULT
    rgbReserved: _type.BYTE = 0


@_struct
class BITMAPINFOHEADER:
    biSize: _type.DWORD = _DEFAULT
    biWidth: _type.LONG = _DEFAULT
    biHeight: _type.LONG = _DEFAULT
    biPlanes: _type.WORD = 1
    biBitCount: _type.WORD = _DEFAULT
    biCompression: _type.DWORD = _DEFAULT
    biSizeImage: _type.DWORD = _DEFAULT
    biXPelsPerMeter: _type.LONG = _DEFAULT
    biYPelsPerMeter: _type.LONG = _DEFAULT
    biClrUsed: _type.DWORD = _DEFAULT
    biClrImportant: _type.DWORD = _DEFAULT


@_struct
class BITMAPINFO:
    bmiHeader: BITMAPINFOHEADER = _DEFAULT
    # noinspection PyTypeChecker
    bmiColors: RGBQUAD * 1 = _DEFAULT


@_struct
class BITMAP:
    bmType: _type.LONG = _DEFAULT
    bmWidth: _type.LONG = _DEFAULT
    bmHeight: _type.LONG = _DEFAULT
    bmWidthBytes: _type.LONG = _DEFAULT
    bmPlanes: _type.WORD = _DEFAULT
    bmBitsPixel: _type.WORD = _DEFAULT
    bmBits: _type.LPVOID = _DEFAULT


@_struct
class DIBSECTION:
    dsBm: BITMAP = _DEFAULT
    dsBmih: BITMAPINFOHEADER = _DEFAULT
    dsBitfields: _type.DWORD * 3 = _DEFAULT
    dshSection: _type.HANDLE = _DEFAULT
    dsOffset: _type.DWORD = _DEFAULT


@_struct
class CHOOSECOLORA:
    lStructSize: _type.DWORD = _DEFAULT
    hwndOwner: _type.HWND = _DEFAULT
    hInstance: _type.HWND = _DEFAULT
    rgbResult: _type.COLORREF = _DEFAULT
    lpCustColors: _Pointer[_type.COLORREF] = _DEFAULT
    Flags: _type.DWORD = _DEFAULT
    lCustData: _type.LPARAM = _DEFAULT
    lpfnHook: _type.LPCCHOOKPROC = _DEFAULT
    lpTemplateName: _type.LPCSTR = _DEFAULT


@_struct
class CHOOSECOLORW:
    lStructSize: _type.DWORD = _DEFAULT
    hwndOwner: _type.HWND = _DEFAULT
    hInstance: _type.HWND = _DEFAULT
    rgbResult: _type.COLORREF = _DEFAULT
    lpCustColors: _Pointer[_type.COLORREF] = _DEFAULT
    Flags: _type.DWORD = _DEFAULT
    lCustData: _type.LPARAM = _DEFAULT
    lpfnHook: _type.LPCCHOOKPROC = _DEFAULT
    lpTemplateName: _type.LPCWSTR = _DEFAULT


@_struct
class GUID:
    Data1: _type.c_ulong = _DEFAULT
    Data2: _type.c_ushort = _DEFAULT
    Data3: _type.c_ushort = _DEFAULT
    Data4: _type.c_uchar * 8 = _DEFAULT


@_struct
class WALLPAPEROPT:
    dwSize: _type.DWORD = _DEFAULT
    dwStyle: _type.DWORD = _DEFAULT


@_struct
class RECT:
    left: _type.LONG = _DEFAULT
    top: _type.LONG = _DEFAULT
    right: _type.LONG = _DEFAULT
    bottom: _type.LONG = _DEFAULT


@_struct
class POINT:
    x: _type.LONG = _DEFAULT
    y: _type.LONG = _DEFAULT


@_struct
class SIZE:
    cx: _type.LONG = _DEFAULT
    cy: _type.LONG = _DEFAULT


@_struct
class MENUINFO:
    cbSize: _type.DWORD = _DEFAULT
    fMask: _type.DWORD = _DEFAULT
    dwStyle: _type.DWORD = _DEFAULT
    cyMax: _type.UINT = 0
    hbrBack: _type.HBRUSH = _DEFAULT
    dwContextHelpID: _type.DWORD = _DEFAULT
    dwMenuData: _type.ULONG_PTR = _DEFAULT


@_struct
class SHITEMID:
    cb: _type.USHORT = _DEFAULT
    abID: _type.BYTE * 1 = _DEFAULT


@_struct
class ITEMIDLIST:
    mkid: SHITEMID = _DEFAULT


@_struct
class MENUITEMINFOA:
    cbSize: _type.UINT = _DEFAULT
    fMask: _type.UINT = _DEFAULT
    fType: _type.UINT = _DEFAULT
    fState: _type.UINT = _DEFAULT
    wID: _type.UINT = _DEFAULT
    hSubMenu: _type.HMENU = _DEFAULT
    hbmpChecked: _type.HBITMAP = _DEFAULT
    hbmpUnchecked: _type.HBITMAP = _DEFAULT
    dwItemData: _type.ULONG_PTR = _DEFAULT
    dwTypeData: _type.LPSTR = _DEFAULT
    cch: _type.UINT = _DEFAULT
    if _const.WINVER >= 0x0500:
        hbmpItem: _type.HBITMAP = _DEFAULT


@_struct
class MENUITEMINFOW:
    cbSize: _type.UINT = _DEFAULT
    fMask: _type.UINT = _DEFAULT
    fType: _type.UINT = _DEFAULT
    fState: _type.UINT = _DEFAULT
    wID: _type.UINT = _DEFAULT
    hSubMenu: _type.HMENU = _DEFAULT
    hbmpChecked: _type.HBITMAP = _DEFAULT
    hbmpUnchecked: _type.HBITMAP = _DEFAULT
    dwItemData: _type.ULONG_PTR = _DEFAULT
    dwTypeData: _type.LPWSTR = _DEFAULT
    cch: _type.UINT = _DEFAULT
    if _const.WINVER >= 0x0500:
        hbmpItem: _type.HBITMAP = _DEFAULT


@_struct
class NOTIFYICONDATAA:
    cbSize: _type.DWORD = _DEFAULT
    hWnd: _type.HWND = _DEFAULT
    uID: _type.UINT = _DEFAULT
    uFlags: _type.UINT = _DEFAULT
    uCallbackMessage: _type.UINT = _DEFAULT
    hIcon: _type.HICON = _DEFAULT
    if _const.NTDDI_VERSION < _const.NTDDI_WIN2K:
        szTip: _type.CHAR * 64 = _DEFAULT
    if _const.NTDDI_VERSION >= _const.NTDDI_WIN2K:
        szTip: _type.CHAR * 128 = _DEFAULT
        dwState: _type.DWORD = _DEFAULT
        dwStateMask: _type.DWORD = _DEFAULT
        szInfo: _type.CHAR * 256 = _DEFAULT
        # noinspection PyProtectedMember
        if not _const._SHELL_EXPORTS_INTERNALAPI_H_:
            U: _union.NOTIFYICONDATA_U = _DEFAULT
        szInfoTitle: _type.CHAR * 64 = _DEFAULT
        dwInfoFlags: _type.DWORD = _DEFAULT
    if _const.NTDDI_VERSION >= _const.NTDDI_WINXP:
        guidItem: GUID = _DEFAULT
    if _const.NTDDI_VERSION >= _const.NTDDI_VISTA:
        hBalloonIcon: _type.HICON = _DEFAULT


@_struct
class NOTIFYICONDATAW:
    cbSize: _type.DWORD = _DEFAULT
    hWnd: _type.HWND = _DEFAULT
    uID: _type.UINT = _DEFAULT
    uFlags: _type.UINT = _DEFAULT
    uCallbackMessage: _type.UINT = _DEFAULT
    hIcon: _type.HICON = _DEFAULT
    if _const.NTDDI_VERSION < _const.NTDDI_WIN2K:
        szTip: _type.WCHAR * 64 = _DEFAULT
    if _const.NTDDI_VERSION >= _const.NTDDI_WIN2K:
        szTip: _type.WCHAR * 128 = _DEFAULT
        dwState: _type.DWORD = _DEFAULT
        dwStateMask: _type.DWORD = _DEFAULT
        szInfo: _type.WCHAR * 256 = _DEFAULT
        # noinspection PyProtectedMember
        if not _const._SHELL_EXPORTS_INTERNALAPI_H_:
            U: _union.NOTIFYICONDATA_U = _DEFAULT
        szInfoTitle: _type.WCHAR * 64 = _DEFAULT
        dwInfoFlags: _type.DWORD = _DEFAULT
    if _const.NTDDI_VERSION >= _const.NTDDI_WINXP:
        guidItem: GUID = _DEFAULT
    if _const.NTDDI_VERSION >= _const.NTDDI_VISTA:
        hBalloonIcon: _type.HICON = _DEFAULT


@_struct
class WNDCLASSEXA:
    cbSize: _type.UINT = _DEFAULT
    style: _type.UINT = _DEFAULT
    lpfnWndProc: _type.WNDPROC = _DEFAULT
    cbClsExtra: _type.c_int = _DEFAULT
    cbWndExtra: _type.c_int = _DEFAULT
    hInstance: _type.HINSTANCE = _DEFAULT
    hIcon: _type.HINSTANCE = _DEFAULT
    hCursor: _type.HCURSOR = _DEFAULT
    hbrBackground: _type.HBRUSH = _DEFAULT
    lpszMenuName: _type.LPCSTR = _DEFAULT
    lpszClassName: _type.LPCSTR = _DEFAULT
    hIconSm: _type.HICON = _DEFAULT


@_struct
class WNDCLASSEXW:
    cbSize: _type.UINT = _DEFAULT
    style: _type.UINT = _DEFAULT
    lpfnWndProc: _type.WNDPROC = _DEFAULT
    cbClsExtra: _type.c_int = _DEFAULT
    cbWndExtra: _type.c_int = _DEFAULT
    hInstance: _type.HINSTANCE = _DEFAULT
    hIcon: _type.HINSTANCE = _DEFAULT
    hCursor: _type.HCURSOR = _DEFAULT
    hbrBackground: _type.HBRUSH = _DEFAULT
    lpszMenuName: _type.LPCWSTR = _DEFAULT
    lpszClassName: _type.LPCWSTR = _DEFAULT
    hIconSm: _type.HICON = _DEFAULT


@_struct
class POINT:
    x: _type.LONG = _DEFAULT
    y: _type.LONG = _DEFAULT


@_struct
class MSG:
    hwnd: _type.HWND = _DEFAULT
    message: _type.UINT = _DEFAULT
    wParam: _type.WPARAM = _DEFAULT
    lParam: _type.WPARAM = _DEFAULT
    time: _type.DWORD = _DEFAULT
    pt: POINT = _DEFAULT
    lPrivate: _type.DWORD = _DEFAULT


@_struct
class PropertyItem:
    id: _type.PROPID = _DEFAULT
    length: _type.ULONG = _DEFAULT
    type: _type.WORD = _DEFAULT
    value: _Pointer[_type.VOID] = _DEFAULT


@_struct
class FILETIME:
    dwLowDateTime: _type.DWORD = _DEFAULT
    dwHighDateTime: _type.DWORD = _DEFAULT


# noinspection PyPep8Naming
@_struct
class WIN32_FIND_DATAA:
    dwFileAttributes: _type.DWORD = _DEFAULT
    ftCreationTime: FILETIME = _DEFAULT
    ftLastAccessTime: FILETIME = _DEFAULT
    ftLastWriteTime: FILETIME = _DEFAULT
    nFileSizeHigh: _type.DWORD = _DEFAULT
    nFileSizeLow: _type.DWORD = _DEFAULT
    dwReserved0: _type.DWORD = _DEFAULT
    dwReserved1: _type.DWORD = _DEFAULT
    cFileName: _type.CHAR * _const.MAX_PATH = _DEFAULT
    cAlternateFileName: _type.CHAR * 14 = _DEFAULT
    # noinspection PyProtectedMember
    if _const._MAC:
        dwFileType: _type.DWORD = _DEFAULT
        dwCreatorType: _type.DWORD = _DEFAULT
        wFinderFlags: _type.WORD = _DEFAULT


# noinspection PyPep8Naming
@_struct
class WIN32_FIND_DATAW:
    dwFileAttributes: _type.DWORD = _DEFAULT
    ftCreationTime: FILETIME = _DEFAULT
    ftLastAccessTime: FILETIME = _DEFAULT
    ftLastWriteTime: FILETIME = _DEFAULT
    nFileSizeHigh: _type.DWORD = _DEFAULT
    nFileSizeLow: _type.DWORD = _DEFAULT
    dwReserved0: _type.DWORD = _DEFAULT
    dwReserved1: _type.DWORD = _DEFAULT
    cFileName: _type.WCHAR * _const.MAX_PATH = _DEFAULT
    cAlternateFileName: _type.WCHAR * 14 = _DEFAULT
    # noinspection PyProtectedMember
    if _const._MAC:
        dwFileType: _type.DWORD = _DEFAULT
        dwCreatorType: _type.DWORD = _DEFAULT
        wFinderFlags: _type.WORD = _DEFAULT


@_struct
class PROPERTYKEY:
    fmtid: GUID = _DEFAULT
    pid: _type.DWORD = _DEFAULT


@_struct
class CSPLATFORM:
    dwPlatformId: _type.DWORD = _DEFAULT
    dwVersionHi: _type.DWORD = _DEFAULT
    dwVersionLo: _type.DWORD = _DEFAULT
    dwProcessorArch: _type.DWORD = _DEFAULT


# noinspection PyPep8Naming
@_struct
class DECIMAL_U_S:
    scale: _type.BYTE = _DEFAULT
    sign: _type.BYTE = _DEFAULT


# noinspection PyPep8Naming
@_struct
class DECIMAL_U2_S:
    Lo32: _type.ULONG = _DEFAULT
    Mid32: _type.ULONG = _DEFAULT


@_struct
class DECIMAL:
    wReserved: _type.USHORT = _DEFAULT
    U: _union.DECIMAL_U = _DEFAULT
    Hi32: _type.ULONG = _DEFAULT
    U2: _union.DECIMAL_U2 = _DEFAULT


# noinspection PyPep8Naming
@_struct
class PROPVARIANT_U_S:
    vt: _type.VARTYPE = _DEFAULT
    wReserved1: _type.PROPVAR_PAD1 = _DEFAULT
    wReserved2: _type.PROPVAR_PAD2 = _DEFAULT
    wReserved3: _type.PROPVAR_PAD3 = _DEFAULT
    U: _union.PROPVARIANT_U_S_U = _DEFAULT


@_struct
class PROPVARIANT:
    U: _union.PROPVARIANT_U = _DEFAULT


@_struct
class MOUSEINPUT:
    dx: _type.LONG = _DEFAULT
    dy: _type.LONG = _DEFAULT
    mouseData: _type.DWORD = _DEFAULT
    dwFlags: _type.DWORD = _DEFAULT
    time: _type.DWORD = _DEFAULT
    dwExtraInfo: _type.ULONG_PTR = _DEFAULT


@_struct
class KEYBDINPUT:
    wVk: _type.WORD = _DEFAULT
    wScan: _type.WORD = _DEFAULT
    dwFlags: _type.DWORD = _DEFAULT
    time: _type.DWORD = _DEFAULT
    dwExtraInfo: _type.ULONG_PTR = _DEFAULT


@_struct
class HARDWAREINPUT:
    uMsg: _type.DWORD = _DEFAULT
    wParamL: _type.WORD = _DEFAULT
    wParamH: _type.WORD = _DEFAULT


@_struct
class INPUT:
    type: _type.DWORD = _DEFAULT
    U: _union.INPUT_U = _DEFAULT


# noinspection PyPep8Naming
@_struct
class DISPLAY_DEVICEA:
    cb: _type.DWORD = _DEFAULT
    DeviceName: _type.CHAR * 32 = _DEFAULT
    DeviceString: _type.CHAR * 128 = _DEFAULT
    StateFlags: _type.DWORD = _DEFAULT
    DeviceID: _type.CHAR * 128 = _DEFAULT
    DeviceKey: _type.CHAR * 128 = _DEFAULT


# noinspection PyPep8Naming
@_struct
class DISPLAY_DEVICEW:
    cb: _type.DWORD = _DEFAULT
    DeviceName: _type.WCHAR * 32 = _DEFAULT
    DeviceString: _type.WCHAR * 128 = _DEFAULT
    StateFlags: _type.DWORD = _DEFAULT
    DeviceID: _type.WCHAR * 128 = _DEFAULT
    DeviceKey: _type.WCHAR * 128 = _DEFAULT


@_struct
class BROWSEINFOA:
    hwndOwner: _type.HWND = _DEFAULT
    pidlRoot: _Pointer[_Pointer[ITEMIDLIST]] = _DEFAULT
    pszDisplayName: _type.LPSTR = _DEFAULT
    lpszTitle: _type.LPCSTR = _DEFAULT
    ulFlags: _type.UINT = _DEFAULT
    lpfn: _type.BFFCALLBACK = _DEFAULT
    lParam: _type.LPARAM = _DEFAULT
    iImage: _type.c_int = _DEFAULT


@_struct
class BROWSEINFOW:
    hwndOwner: _type.HWND = _DEFAULT
    pidlRoot: _Pointer[_Pointer[ITEMIDLIST]] = _DEFAULT
    pszDisplayName: _type.LPWSTR = _DEFAULT
    lpszTitle: _type.LPCWSTR = _DEFAULT
    ulFlags: _type.UINT = _DEFAULT
    lpfn: _type.BFFCALLBACK = _DEFAULT
    lParam: _type.LPARAM = _DEFAULT
    iImage: _type.c_int = _DEFAULT


@_struct
class PAINTSTRUCT:
    hdc: _type.HDC = _DEFAULT
    fErase: _type.BOOL = _DEFAULT
    rcPaint: RECT = _DEFAULT
    fRestore: _type.BOOL = _DEFAULT
    fIncUpdate: _type.BOOL = _DEFAULT
    rgbReserved: _type.BYTE * 32 = _DEFAULT


# noinspection PyPep8Naming
@_struct
class PICTDESC_U_S:
    hbitmap: _type.HBITMAP = _DEFAULT
    hpal: _type.HPALETTE = _DEFAULT


# noinspection PyPep8Naming
@_struct
class PICTDESC_U_S2:
    hmeta: _type.HMETAFILE = _DEFAULT
    xExt: _type.c_int = _DEFAULT
    yExt: _type.c_int = _DEFAULT


# noinspection PyPep8Naming
@_struct
class PICTDESC_U_S3:
    hicon: _type.HICON = _DEFAULT


# noinspection PyProtectedMember
if _const._WIN32:
    # noinspection PyPep8Naming
    @_struct
    class PICTDESC_U_S4:
        hemf: _type.HMETAFILE = _DEFAULT


@_struct
class PICTDESC:
    cbSizeofstruct: _type.UINT = _DEFAULT
    picType: _type.UINT = _DEFAULT
    U: _union.PICTDESC_U = _DEFAULT


@_struct
class MONITORINFO:
    cbSize: _type.DWORD = _DEFAULT
    rcMonitor: RECT = _DEFAULT
    rcWork: RECT = _DEFAULT
    dwFlags: _type.DWORD = _DEFAULT


@_struct
class MONITORINFOEXA:
    S: MONITORINFO = _DEFAULT
    szDevice: _type.CHAR * _const.CCHDEVICENAME = _DEFAULT


@_struct
class MONITORINFOEXW:
    S: MONITORINFO = _DEFAULT
    szDevice: _type.WCHAR * _const.CCHDEVICENAME = _DEFAULT


# noinspection PyPep8Naming
@_struct
class VARIANT_U_S:
    vt: _type.VARTYPE = _DEFAULT
    wReserved1: _type.WORD = _DEFAULT
    wReserved2: _type.WORD = _DEFAULT
    wReserved3: _type.WORD = _DEFAULT
    U: _union.VARIANT_U_S_U = _DEFAULT


@_struct
class VARIANT:
    U: _union.VARIANT_U = _DEFAULT


# noinspection PyPep8Naming
@_struct
class SP_DEVINFO_DATA:
    cbSize: _type.DWORD = _DEFAULT
    ClassGuid: GUID = _DEFAULT
    DevInst: _type.DWORD = _DEFAULT
    Reserved: _type.ULONG_PTR = _DEFAULT


# noinspection PyPep8Naming
@_struct
class SP_DEVICE_INTERFACE_DATA:
    cbSize: _type.DWORD = _DEFAULT
    InterfaceClassGuid: GUID = _DEFAULT
    Flags: _type.DWORD = _DEFAULT
    Reserved: _type.ULONG_PTR = _DEFAULT


# noinspection PyPep8Naming
@_struct
class SP_DEVICE_INTERFACE_DETAIL_DATA_A:
    cbSize: _type.DWORD = _DEFAULT
    DevicePath: _type.CHAR * _const.ANYSIZE_ARRAY = _DEFAULT


# noinspection PyPep8Naming
@_struct
class SP_DEVICE_INTERFACE_DETAIL_DATA_W:
    cbSize: _type.DWORD = _DEFAULT
    DevicePath: _type.WCHAR * _const.ANYSIZE_ARRAY = _DEFAULT


@_struct
class DEVPROPKEY:
    fmtid: DEVPROPGUID = _DEFAULT
    pid: _type.DEVPROPID = _DEFAULT


@_struct
class BLENDFUNCTION:
    BlendOp: _type.BYTE = _DEFAULT
    BlendFlags: _type.BYTE = _DEFAULT
    SourceConstantAlpha: _type.BYTE = _DEFAULT
    AlphaFormat: _type.BYTE = _DEFAULT


@_struct
class ColorMap:
    oldColor: _type.Color = _DEFAULT
    newColor: _type.Color = _DEFAULT


@_struct
class ColorMatrix:
    m: _type.REAL * 5 * 5 = _DEFAULT


@_struct
class EventRegistrationToken:
    value: _type.c_int64 = _DEFAULT


@_struct
class Rational:
    Numerator: _type.UINT32 = _DEFAULT
    Denominator: _type.UINT32 = _DEFAULT


@_struct
class EncoderParameter:
    Guid: GUID = _DEFAULT
    NumberOfValues: _type.ULONG = _DEFAULT
    Type: _type.ULONG = _DEFAULT
    Value: _Pointer[_type.VOID] = _DEFAULT


@_struct
class EncoderParameters:
    Count: _type.UINT = _DEFAULT
    # noinspection PyTypeChecker
    Parameter: EncoderParameter * 1 = _DEFAULT


@_struct
class ImageCodecInfo:
    Clsid: CLSID = _DEFAULT
    FormatID: GUID = _DEFAULT
    CodecName: _type.LPWSTR = _DEFAULT
    DllName: _type.LPWSTR = _DEFAULT
    FormatDescription: _type.LPWSTR = _DEFAULT
    FilenameExtension: _type.LPWSTR = _DEFAULT
    MimeType: _type.LPWSTR = _DEFAULT
    Flags: _type.DWORD = _DEFAULT
    Version: _type.DWORD = _DEFAULT
    SigCount: _type.DWORD = _DEFAULT
    SigSize: _type.DWORD = _DEFAULT
    SigPattern: _Pointer[_type.BYTE] = _DEFAULT
    SigMask: _Pointer[_type.BYTE] = _DEFAULT


UUID = GUID
IID = GUID
CLSID = GUID
KNOWNFOLDERID = GUID
DEVPROPGUID = GUID
VARIANTARG = VARIANT


def _init(item: str) -> type[_ctypes.Structure]:
    _globals.check_item(item)

    class Struct(_ctypes.Structure):
        _fields_ = tuple((name, _resolve_type(type_)) for name, type_ in _globals.get_type_hints(item))
        _defaults = tuple((field[0], getattr(_globals.vars_[item], field[0])) for field in _fields_)

        def __init__(self, *args, **kwargs):
            for name, val in _itertools.islice(self._defaults, len(args), None):
                if val is not _DEFAULT and name not in kwargs:
                    kwargs[name] = val
            super().__init__(*args, **kwargs)

    return _functools.update_wrapper(Struct, _globals.vars_[item], _ASSIGNED, ())


_globals = _Globals()
