from __future__ import annotations as _

import ctypes as _ctypes
import functools as _functools
import itertools as _itertools
from dataclasses import dataclass as _struct

from . import const as _const, enum as _enum, type as _type, union as _union
from ._head import _Globals, _Pointer, _resolve_type

_NONE = None
_ASSIGNED = ('__repr__', *_functools.WRAPPER_ASSIGNMENTS)


@_struct
class GdiplusStartupInput:
    GdiplusVersion: _type.UINT32 = 1
    DebugEventCallback: _type.DebugEventProc = _NONE
    SuppressBackgroundThread: _type.BOOL = False
    SuppressExternalCodecs: _type.BOOL = False


@_struct
class RGBTRIPLE:
    rgbBlue: _type.BYTE = _NONE
    rgbGreen: _type.BYTE = _NONE
    rgbRed: _type.BYTE = _NONE


@_struct
class RGBQUAD:
    rgbBlue: _type.BYTE = _NONE
    rgbGreen: _type.BYTE = _NONE
    rgbRed: _type.BYTE = _NONE
    rgbReserved: _type.BYTE = 0


@_struct
class BITMAPINFOHEADER:
    biSize: _type.DWORD = _NONE
    biWidth: _type.LONG = _NONE
    biHeight: _type.LONG = _NONE
    biPlanes: _type.WORD = 1
    biBitCount: _type.WORD = _NONE
    biCompression: _type.DWORD = _NONE
    biSizeImage: _type.DWORD = _NONE
    biXPelsPerMeter: _type.LONG = _NONE
    biYPelsPerMeter: _type.LONG = _NONE
    biClrUsed: _type.DWORD = _NONE
    biClrImportant: _type.DWORD = _NONE


@_struct
class BITMAPINFO:
    bmiHeader: BITMAPINFOHEADER = _NONE
    # noinspection PyTypeChecker
    bmiColors: RGBQUAD * 1 = _NONE


@_struct
class BITMAP:
    bmType: _type.LONG = _NONE
    bmWidth: _type.LONG = _NONE
    bmHeight: _type.LONG = _NONE
    bmWidthBytes: _type.LONG = _NONE
    bmPlanes: _type.WORD = _NONE
    bmBitsPixel: _type.WORD = _NONE
    bmBits: _type.LPVOID = _NONE


@_struct
class DIBSECTION:
    dsBm: BITMAP = _NONE
    dsBmih: BITMAPINFOHEADER = _NONE
    dsBitfields: _type.DWORD * 3 = _NONE
    dshSection: _type.HANDLE = _NONE
    dsOffset: _type.DWORD = _NONE


@_struct
class CHOOSECOLORA:
    lStructSize: _type.DWORD = _NONE
    hwndOwner: _type.HWND = _NONE
    hInstance: _type.HWND = _NONE
    rgbResult: _type.COLORREF = _NONE
    lpCustColors: _Pointer[_type.COLORREF] = _NONE
    Flags: _type.DWORD = _NONE
    lCustData: _type.LPARAM = _NONE
    lpfnHook: _type.LPCCHOOKPROC = _NONE
    lpTemplateName: _type.LPCSTR = _NONE


@_struct
class CHOOSECOLORW:
    lStructSize: _type.DWORD = _NONE
    hwndOwner: _type.HWND = _NONE
    hInstance: _type.HWND = _NONE
    rgbResult: _type.COLORREF = _NONE
    lpCustColors: _Pointer[_type.COLORREF] = _NONE
    Flags: _type.DWORD = _NONE
    lCustData: _type.LPARAM = _NONE
    lpfnHook: _type.LPCCHOOKPROC = _NONE
    lpTemplateName: _type.LPCWSTR = _NONE


@_struct
class GUID:
    Data1: _type.c_ulong = _NONE
    Data2: _type.c_ushort = _NONE
    Data3: _type.c_ushort = _NONE
    Data4: _type.c_uchar * 8 = _NONE


@_struct
class WALLPAPEROPT:
    dwSize: _type.DWORD = _NONE
    dwStyle: _type.DWORD = _NONE


@_struct
class RECT:
    left: _type.LONG = _NONE
    top: _type.LONG = _NONE
    right: _type.LONG = _NONE
    bottom: _type.LONG = _NONE


@_struct
class POINT:
    x: _type.LONG = _NONE
    y: _type.LONG = _NONE


@_struct
class SIZE:
    cx: _type.LONG = _NONE
    cy: _type.LONG = _NONE


@_struct
class MENUINFO:
    cbSize: _type.DWORD = _NONE
    fMask: _type.DWORD = _NONE
    dwStyle: _type.DWORD = _NONE
    cyMax: _type.UINT = 0
    hbrBack: _type.HBRUSH = _NONE
    dwContextHelpID: _type.DWORD = _NONE
    dwMenuData: _type.ULONG_PTR = _NONE


@_struct
class SHITEMID:
    cb: _type.USHORT = _NONE
    abID: _type.BYTE * 1 = _NONE


@_struct
class ITEMIDLIST:
    mkid: SHITEMID = _NONE


@_struct
class MENUITEMINFOA:
    cbSize: _type.UINT = _NONE
    fMask: _type.UINT = _NONE
    fType: _type.UINT = _NONE
    fState: _type.UINT = _NONE
    wID: _type.UINT = _NONE
    hSubMenu: _type.HMENU = _NONE
    hbmpChecked: _type.HBITMAP = _NONE
    hbmpUnchecked: _type.HBITMAP = _NONE
    dwItemData: _type.ULONG_PTR = _NONE
    dwTypeData: _type.LPSTR = _NONE
    cch: _type.UINT = _NONE
    if _const.WINVER >= 0x0500:
        hbmpItem: _type.HBITMAP = _NONE


@_struct
class MENUITEMINFOW:
    cbSize: _type.UINT = _NONE
    fMask: _type.UINT = _NONE
    fType: _type.UINT = _NONE
    fState: _type.UINT = _NONE
    wID: _type.UINT = _NONE
    hSubMenu: _type.HMENU = _NONE
    hbmpChecked: _type.HBITMAP = _NONE
    hbmpUnchecked: _type.HBITMAP = _NONE
    dwItemData: _type.ULONG_PTR = _NONE
    dwTypeData: _type.LPWSTR = _NONE
    cch: _type.UINT = _NONE
    if _const.WINVER >= 0x0500:
        hbmpItem: _type.HBITMAP = _NONE


@_struct
class NOTIFYICONDATAA:
    cbSize: _type.DWORD = _NONE
    hWnd: _type.HWND = _NONE
    uID: _type.UINT = _NONE
    uFlags: _type.UINT = _NONE
    uCallbackMessage: _type.UINT = _NONE
    hIcon: _type.HICON = _NONE
    if _const.NTDDI_VERSION < _const.NTDDI_WIN2K:
        szTip: _type.CHAR * 64 = _NONE
    if _const.NTDDI_VERSION >= _const.NTDDI_WIN2K:
        szTip: _type.CHAR * 128 = _NONE
        dwState: _type.DWORD = _NONE
        dwStateMask: _type.DWORD = _NONE
        szInfo: _type.CHAR * 256 = _NONE
        # noinspection PyProtectedMember
        if not _const._SHELL_EXPORTS_INTERNALAPI_H_:
            U: _union.NOTIFYICONDATA_U = _NONE
        szInfoTitle: _type.CHAR * 64 = _NONE
        dwInfoFlags: _type.DWORD = _NONE
    if _const.NTDDI_VERSION >= _const.NTDDI_WINXP:
        guidItem: GUID = _NONE
    if _const.NTDDI_VERSION >= _const.NTDDI_VISTA:
        hBalloonIcon: _type.HICON = _NONE


@_struct
class NOTIFYICONDATAW:
    cbSize: _type.DWORD = _NONE
    hWnd: _type.HWND = _NONE
    uID: _type.UINT = _NONE
    uFlags: _type.UINT = _NONE
    uCallbackMessage: _type.UINT = _NONE
    hIcon: _type.HICON = _NONE
    if _const.NTDDI_VERSION < _const.NTDDI_WIN2K:
        szTip: _type.WCHAR * 64 = _NONE
    if _const.NTDDI_VERSION >= _const.NTDDI_WIN2K:
        szTip: _type.WCHAR * 128 = _NONE
        dwState: _type.DWORD = _NONE
        dwStateMask: _type.DWORD = _NONE
        szInfo: _type.WCHAR * 256 = _NONE
        # noinspection PyProtectedMember
        if not _const._SHELL_EXPORTS_INTERNALAPI_H_:
            U: _union.NOTIFYICONDATA_U = _NONE
        szInfoTitle: _type.WCHAR * 64 = _NONE
        dwInfoFlags: _type.DWORD = _NONE
    if _const.NTDDI_VERSION >= _const.NTDDI_WINXP:
        guidItem: GUID = _NONE
    if _const.NTDDI_VERSION >= _const.NTDDI_VISTA:
        hBalloonIcon: _type.HICON = _NONE


@_struct
class WNDCLASSEXA:
    cbSize: _type.UINT = _NONE
    style: _type.UINT = _NONE
    lpfnWndProc: _type.WNDPROC = _NONE
    cbClsExtra: _type.c_int = _NONE
    cbWndExtra: _type.c_int = _NONE
    hInstance: _type.HINSTANCE = _NONE
    hIcon: _type.HINSTANCE = _NONE
    hCursor: _type.HCURSOR = _NONE
    hbrBackground: _type.HBRUSH = _NONE
    lpszMenuName: _type.LPCSTR = _NONE
    lpszClassName: _type.LPCSTR = _NONE
    hIconSm: _type.HICON = _NONE


@_struct
class WNDCLASSEXW:
    cbSize: _type.UINT = _NONE
    style: _type.UINT = _NONE
    lpfnWndProc: _type.WNDPROC = _NONE
    cbClsExtra: _type.c_int = _NONE
    cbWndExtra: _type.c_int = _NONE
    hInstance: _type.HINSTANCE = _NONE
    hIcon: _type.HINSTANCE = _NONE
    hCursor: _type.HCURSOR = _NONE
    hbrBackground: _type.HBRUSH = _NONE
    lpszMenuName: _type.LPCWSTR = _NONE
    lpszClassName: _type.LPCWSTR = _NONE
    hIconSm: _type.HICON = _NONE


@_struct
class POINT:
    x: _type.LONG = _NONE
    y: _type.LONG = _NONE


@_struct
class MSG:
    hwnd: _type.HWND = _NONE
    message: _type.UINT = _NONE
    wParam: _type.WPARAM = _NONE
    lParam: _type.WPARAM = _NONE
    time: _type.DWORD = _NONE
    pt: POINT = _NONE
    lPrivate: _type.DWORD = _NONE


@_struct
class PropertyItem:
    id: _type.PROPID = _NONE
    length: _type.ULONG = _NONE
    type: _type.WORD = _NONE
    value: _Pointer[_type.VOID] = _NONE


@_struct
class FILETIME:
    dwLowDateTime: _type.DWORD = _NONE
    dwHighDateTime: _type.DWORD = _NONE


# noinspection PyPep8Naming
@_struct
class WIN32_FIND_DATAA:
    dwFileAttributes: _type.DWORD = _NONE
    ftCreationTime: FILETIME = _NONE
    ftLastAccessTime: FILETIME = _NONE
    ftLastWriteTime: FILETIME = _NONE
    nFileSizeHigh: _type.DWORD = _NONE
    nFileSizeLow: _type.DWORD = _NONE
    dwReserved0: _type.DWORD = _NONE
    dwReserved1: _type.DWORD = _NONE
    cFileName: _type.CHAR * _const.MAX_PATH = _NONE
    cAlternateFileName: _type.CHAR * 14 = _NONE
    # noinspection PyProtectedMember
    if _const._MAC:
        dwFileType: _type.DWORD = _NONE
        dwCreatorType: _type.DWORD = _NONE
        wFinderFlags: _type.WORD = _NONE


# noinspection PyPep8Naming
@_struct
class WIN32_FIND_DATAW:
    dwFileAttributes: _type.DWORD = _NONE
    ftCreationTime: FILETIME = _NONE
    ftLastAccessTime: FILETIME = _NONE
    ftLastWriteTime: FILETIME = _NONE
    nFileSizeHigh: _type.DWORD = _NONE
    nFileSizeLow: _type.DWORD = _NONE
    dwReserved0: _type.DWORD = _NONE
    dwReserved1: _type.DWORD = _NONE
    cFileName: _type.WCHAR * _const.MAX_PATH = _NONE
    cAlternateFileName: _type.WCHAR * 14 = _NONE
    # noinspection PyProtectedMember
    if _const._MAC:
        dwFileType: _type.DWORD = _NONE
        dwCreatorType: _type.DWORD = _NONE
        wFinderFlags: _type.WORD = _NONE


@_struct
class PROPERTYKEY:
    fmtid: GUID = _NONE
    pid: _type.DWORD = _NONE


@_struct
class CSPLATFORM:
    dwPlatformId: _type.DWORD = _NONE
    dwVersionHi: _type.DWORD = _NONE
    dwVersionLo: _type.DWORD = _NONE
    dwProcessorArch: _type.DWORD = _NONE


# noinspection PyPep8Naming
@_struct
class DECIMAL_U_S:
    scale: _type.BYTE = _NONE
    sign: _type.BYTE = _NONE


# noinspection PyPep8Naming
@_struct
class DECIMAL_U2_S:
    Lo32: _type.ULONG = _NONE
    Mid32: _type.ULONG = _NONE


@_struct
class DECIMAL:
    wReserved: _type.USHORT = _NONE
    U: _union.DECIMAL_U = _NONE
    Hi32: _type.ULONG = _NONE
    U2: _union.DECIMAL_U2 = _NONE


# noinspection PyPep8Naming
@_struct
class PROPVARIANT_U_S:
    vt: _type.VARTYPE = _NONE
    wReserved1: _type.PROPVAR_PAD1 = _NONE
    wReserved2: _type.PROPVAR_PAD2 = _NONE
    wReserved3: _type.PROPVAR_PAD3 = _NONE
    U: _union.PROPVARIANT_U_S_U = _NONE


@_struct
class PROPVARIANT:
    U: _union.PROPVARIANT_U = _NONE


@_struct
class MOUSEINPUT:
    dx: _type.LONG = _NONE
    dy: _type.LONG = _NONE
    mouseData: _type.DWORD = _NONE
    dwFlags: _type.DWORD = _NONE
    time: _type.DWORD = _NONE
    dwExtraInfo: _type.ULONG_PTR = _NONE


@_struct
class KEYBDINPUT:
    wVk: _type.WORD = _NONE
    wScan: _type.WORD = _NONE
    dwFlags: _type.DWORD = _NONE
    time: _type.DWORD = _NONE
    dwExtraInfo: _type.ULONG_PTR = _NONE


@_struct
class HARDWAREINPUT:
    uMsg: _type.DWORD = _NONE
    wParamL: _type.WORD = _NONE
    wParamH: _type.WORD = _NONE


@_struct
class INPUT:
    type: _type.DWORD = _NONE
    U: _union.INPUT_U = _NONE


# noinspection PyPep8Naming
@_struct
class DISPLAY_DEVICEA:
    cb: _type.DWORD = _NONE
    DeviceName: _type.CHAR * 32 = _NONE
    DeviceString: _type.CHAR * 128 = _NONE
    StateFlags: _type.DWORD = _NONE
    DeviceID: _type.CHAR * 128 = _NONE
    DeviceKey: _type.CHAR * 128 = _NONE


# noinspection PyPep8Naming
@_struct
class DISPLAY_DEVICEW:
    cb: _type.DWORD = _NONE
    DeviceName: _type.WCHAR * 32 = _NONE
    DeviceString: _type.WCHAR * 128 = _NONE
    StateFlags: _type.DWORD = _NONE
    DeviceID: _type.WCHAR * 128 = _NONE
    DeviceKey: _type.WCHAR * 128 = _NONE


@_struct
class BROWSEINFOA:
    hwndOwner: _type.HWND = _NONE
    pidlRoot: _Pointer[_Pointer[ITEMIDLIST]] = _NONE
    pszDisplayName: _type.LPSTR = _NONE
    lpszTitle: _type.LPCSTR = _NONE
    ulFlags: _type.UINT = _NONE
    lpfn: _type.BFFCALLBACK = _NONE
    lParam: _type.LPARAM = _NONE
    iImage: _type.c_int = _NONE


@_struct
class BROWSEINFOW:
    hwndOwner: _type.HWND = _NONE
    pidlRoot: _Pointer[_Pointer[ITEMIDLIST]] = _NONE
    pszDisplayName: _type.LPWSTR = _NONE
    lpszTitle: _type.LPCWSTR = _NONE
    ulFlags: _type.UINT = _NONE
    lpfn: _type.BFFCALLBACK = _NONE
    lParam: _type.LPARAM = _NONE
    iImage: _type.c_int = _NONE


@_struct
class PAINTSTRUCT:
    hdc: _type.HDC = _NONE
    fErase: _type.BOOL = _NONE
    rcPaint: RECT = _NONE
    fRestore: _type.BOOL = _NONE
    fIncUpdate: _type.BOOL = _NONE
    rgbReserved: _type.BYTE * 32 = _NONE


# noinspection PyPep8Naming
@_struct
class PICTDESC_U_S:
    hbitmap: _type.HBITMAP = _NONE
    hpal: _type.HPALETTE = _NONE


# noinspection PyPep8Naming
@_struct
class PICTDESC_U_S2:
    hmeta: _type.HMETAFILE = _NONE
    xExt: _type.c_int = _NONE
    yExt: _type.c_int = _NONE


# noinspection PyPep8Naming
@_struct
class PICTDESC_U_S3:
    hicon: _type.HICON = _NONE


# noinspection PyProtectedMember
if _const._WIN32:
    # noinspection PyPep8Naming
    @_struct
    class PICTDESC_U_S4:
        hemf: _type.HMETAFILE = _NONE


@_struct
class PICTDESC:
    cbSizeofstruct: _type.UINT = _NONE
    picType: _type.UINT = _NONE
    U: _union.PICTDESC_U = _NONE


@_struct
class MONITORINFO:
    cbSize: _type.DWORD = _NONE
    rcMonitor: RECT = _NONE
    rcWork: RECT = _NONE
    dwFlags: _type.DWORD = _NONE


@_struct
class MONITORINFOEXA:
    S: MONITORINFO = _NONE
    szDevice: _type.CHAR * _const.CCHDEVICENAME = _NONE


@_struct
class MONITORINFOEXW:
    S: MONITORINFO = _NONE
    szDevice: _type.WCHAR * _const.CCHDEVICENAME = _NONE


# noinspection PyPep8Naming
@_struct
class VARIANT_U_S:
    vt: _type.VARTYPE = _NONE
    wReserved1: _type.WORD = _NONE
    wReserved2: _type.WORD = _NONE
    wReserved3: _type.WORD = _NONE
    U: _union.VARIANT_U_S_U = _NONE


@_struct
class VARIANT:
    U: _union.VARIANT_U = _NONE


# noinspection PyPep8Naming
@_struct
class SP_DEVINFO_DATA:
    cbSize: _type.DWORD = _NONE
    ClassGuid: GUID = _NONE
    DevInst: _type.DWORD = _NONE
    Reserved: _type.ULONG_PTR = _NONE


# noinspection PyPep8Naming
@_struct
class SP_DEVICE_INTERFACE_DATA:
    cbSize: _type.DWORD = _NONE
    InterfaceClassGuid: GUID = _NONE
    Flags: _type.DWORD = _NONE
    Reserved: _type.ULONG_PTR = _NONE


# noinspection PyPep8Naming
@_struct
class SP_DEVICE_INTERFACE_DETAIL_DATA_A:
    cbSize: _type.DWORD = _NONE
    DevicePath: _type.CHAR * _const.ANYSIZE_ARRAY = _NONE


# noinspection PyPep8Naming
@_struct
class SP_DEVICE_INTERFACE_DETAIL_DATA_W:
    cbSize: _type.DWORD = _NONE
    DevicePath: _type.WCHAR * _const.ANYSIZE_ARRAY = _NONE


@_struct
class DEVPROPKEY:
    fmtid: DEVPROPGUID = _NONE
    pid: _type.DEVPROPID = _NONE


@_struct
class BLENDFUNCTION:
    BlendOp: _type.BYTE = _NONE
    BlendFlags: _type.BYTE = _NONE
    SourceConstantAlpha: _type.BYTE = _NONE
    AlphaFormat: _type.BYTE = _NONE


@_struct
class ColorMap:
    oldColor: _type.Color = _NONE
    newColor: _type.Color = _NONE


@_struct
class ColorMatrix:
    m: _type.REAL * 5 * 5 = _NONE


@_struct
class EventRegistrationToken:
    value: _type.c_int64 = _NONE


@_struct
class Rational:
    Numerator: _type.UINT32 = _NONE
    Denominator: _type.UINT32 = _NONE


@_struct
class EncoderParameter:
    Guid: GUID = _NONE
    NumberOfValues: _type.ULONG = _NONE
    Type: _type.ULONG = _NONE
    Value: _Pointer[_type.VOID] = _NONE


@_struct
class EncoderParameters:
    Count: _type.UINT = _NONE
    # noinspection PyTypeChecker
    Parameter: EncoderParameter * 1 = _NONE


@_struct
class ImageCodecInfo:
    Clsid: CLSID = _NONE
    FormatID: GUID = _NONE
    CodecName: _type.LPWSTR = _NONE
    DllName: _type.LPWSTR = _NONE
    FormatDescription: _type.LPWSTR = _NONE
    FilenameExtension: _type.LPWSTR = _NONE
    MimeType: _type.LPWSTR = _NONE
    Flags: _type.DWORD = _NONE
    Version: _type.DWORD = _NONE
    SigCount: _type.DWORD = _NONE
    SigSize: _type.DWORD = _NONE
    SigPattern: _Pointer[_type.BYTE] = _NONE
    SigMask: _Pointer[_type.BYTE] = _NONE


@_struct
class OPENASINFO:
    pcszFile: _type.LPCWSTR = _NONE
    pcszClass: _type.LPCWSTR = _NONE
    oaifInFlags: _enum.OPEN_AS_INFO_FLAGS = _NONE


@_struct
class SHELLEXECUTEINFOA:
    cbSize: _type.DWORD = _NONE
    fMask: _type.ULONG = _NONE
    hwnd: _type.HWND = _NONE
    lpVerb: _type.LPCSTR = _NONE
    lpFile: _type.LPCSTR = _NONE
    lpParameters: _type.LPCSTR = _NONE
    lpDirectory: _type.LPCSTR = _NONE
    nShow: _type.c_int = _NONE
    hInstApp: _type.HINSTANCE = _NONE
    lpIDList: _type.c_void_p = _NONE
    lpClass: _type.LPCSTR = _NONE
    hkeyClass: _type.HKEY = _NONE
    dwHotKey: _type.DWORD = _NONE
    U: _union.SHELLEXECUTEINFO_U = _NONE
    hProcess: _type.HANDLE = _NONE


@_struct
class SHELLEXECUTEINFOW:
    cbSize: _type.DWORD = _NONE
    fMask: _type.ULONG = _NONE
    hwnd: _type.HWND = _NONE
    lpVerb: _type.LPCWSTR = _NONE
    lpFile: _type.LPCWSTR = _NONE
    lpParameters: _type.LPCWSTR = _NONE
    lpDirectory: _type.LPCWSTR = _NONE
    nShow: _type.c_int = _NONE
    hInstApp: _type.HINSTANCE = _NONE
    lpIDList: _type.c_void_p = _NONE
    lpClass: _type.LPCWSTR = _NONE
    hkeyClass: _type.HKEY = _NONE
    dwHotKey: _type.DWORD = _NONE
    U: _union.SHELLEXECUTEINFO_U = _NONE
    hProcess: _type.HANDLE = _NONE


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
                if val is not _NONE and name not in kwargs:
                    kwargs[name] = val
            super().__init__(*args, **kwargs)

    return _functools.update_wrapper(Struct, _globals.vars_[item], _ASSIGNED, ())


_globals = _Globals()
