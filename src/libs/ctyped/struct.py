from __future__ import annotations as _

import ctypes as _ctypes
import functools as _functools
from dataclasses import dataclass as _struct

from . import const as _const, enum as _enum, type as _type, union as _union
from ._utils import _Globals, _Pointer, _resolve_type

_EMPTY = None
_SIZE = object()
_ASSIGNED = ('__repr__', *_functools.WRAPPER_ASSIGNMENTS)


@_struct
class GdiplusStartupInput:
    GdiplusVersion: _type.UINT32 = 1
    DebugEventCallback: _type.DebugEventProc = _EMPTY
    SuppressBackgroundThread: _type.BOOL = _EMPTY
    SuppressExternalCodecs: _type.BOOL = _EMPTY


@_struct
class RGBTRIPLE:
    rgbBlue: _type.BYTE = _EMPTY
    rgbGreen: _type.BYTE = _EMPTY
    rgbRed: _type.BYTE = _EMPTY


@_struct
class RGBQUAD:
    rgbBlue: _type.BYTE = _EMPTY
    rgbGreen: _type.BYTE = _EMPTY
    rgbRed: _type.BYTE = _EMPTY
    rgbReserved: _type.BYTE = _EMPTY


@_struct
class BITMAPINFOHEADER:
    biSize: _type.DWORD = _EMPTY
    biWidth: _type.LONG = _EMPTY
    biHeight: _type.LONG = _EMPTY
    biPlanes: _type.WORD = 1
    biBitCount: _type.WORD = _EMPTY
    biCompression: _type.DWORD = _EMPTY
    biSizeImage: _type.DWORD = _EMPTY
    biXPelsPerMeter: _type.LONG = _EMPTY
    biYPelsPerMeter: _type.LONG = _EMPTY
    biClrUsed: _type.DWORD = _EMPTY
    biClrImportant: _type.DWORD = _EMPTY


@_struct
class BITMAPINFO:
    bmiHeader: BITMAPINFOHEADER = _EMPTY
    # noinspection PyTypeChecker
    bmiColors: RGBQUAD * 1 = _EMPTY


@_struct
class BITMAP:
    bmType: _type.LONG = _EMPTY
    bmWidth: _type.LONG = _EMPTY
    bmHeight: _type.LONG = _EMPTY
    bmWidthBytes: _type.LONG = _EMPTY
    bmPlanes: _type.WORD = _EMPTY
    bmBitsPixel: _type.WORD = _EMPTY
    bmBits: _type.LPVOID = _EMPTY


@_struct
class DIBSECTION:
    dsBm: BITMAP = _EMPTY
    dsBmih: BITMAPINFOHEADER = _EMPTY
    dsBitfields: _type.DWORD * 3 = _EMPTY
    dshSection: _type.HANDLE = _EMPTY
    dsOffset: _type.DWORD = _EMPTY


@_struct
class CHOOSECOLORA:
    lStructSize: _type.DWORD = _SIZE
    hwndOwner: _type.HWND = _EMPTY
    hInstance: _type.HWND = _EMPTY
    rgbResult: _type.COLORREF = _EMPTY
    lpCustColors: _Pointer[_type.COLORREF] = _EMPTY
    Flags: _type.DWORD = _EMPTY
    lCustData: _type.LPARAM = _EMPTY
    lpfnHook: _type.LPCCHOOKPROC = _EMPTY
    lpTemplateName: _type.LPCSTR = _EMPTY


@_struct
class CHOOSECOLORW:
    lStructSize: _type.DWORD = _SIZE
    hwndOwner: _type.HWND = _EMPTY
    hInstance: _type.HWND = _EMPTY
    rgbResult: _type.COLORREF = _EMPTY
    lpCustColors: _Pointer[_type.COLORREF] = _EMPTY
    Flags: _type.DWORD = _EMPTY
    lCustData: _type.LPARAM = _EMPTY
    lpfnHook: _type.LPCCHOOKPROC = _EMPTY
    lpTemplateName: _type.LPCWSTR = _EMPTY


@_struct
class GUID:
    Data1: _type.c_ulong = _EMPTY
    Data2: _type.c_ushort = _EMPTY
    Data3: _type.c_ushort = _EMPTY
    Data4: _type.c_uchar * 8 = _EMPTY


@_struct
class WALLPAPEROPT:
    dwSize: _type.DWORD = _SIZE
    dwStyle: _type.DWORD = _EMPTY


@_struct
class RECT:
    left: _type.LONG = _EMPTY
    top: _type.LONG = _EMPTY
    right: _type.LONG = _EMPTY
    bottom: _type.LONG = _EMPTY


@_struct
class POINT:
    x: _type.LONG = _EMPTY
    y: _type.LONG = _EMPTY


@_struct
class SIZE:
    cx: _type.LONG = _EMPTY
    cy: _type.LONG = _EMPTY


@_struct
class MENUINFO:
    cbSize: _type.DWORD = _SIZE
    fMask: _type.DWORD = _EMPTY
    dwStyle: _type.DWORD = _EMPTY
    cyMax: _type.UINT = _EMPTY
    hbrBack: _type.HBRUSH = _EMPTY
    dwContextHelpID: _type.DWORD = _EMPTY
    dwMenuData: _type.ULONG_PTR = _EMPTY


@_struct
class SHITEMID:
    cb: _type.USHORT = _EMPTY
    abID: _type.BYTE * 1 = _EMPTY


@_struct
class ITEMIDLIST:
    mkid: SHITEMID = _EMPTY


@_struct
class MENUITEMINFOA:
    cbSize: _type.UINT = _SIZE
    fMask: _type.UINT = _EMPTY
    fType: _type.UINT = _EMPTY
    fState: _type.UINT = _EMPTY
    wID: _type.UINT = _EMPTY
    hSubMenu: _type.HMENU = _EMPTY
    hbmpChecked: _type.HBITMAP = _EMPTY
    hbmpUnchecked: _type.HBITMAP = _EMPTY
    dwItemData: _type.ULONG_PTR = _EMPTY
    dwTypeData: _type.LPSTR = _EMPTY
    cch: _type.UINT = _EMPTY
    if _const.WINVER >= 0x0500:
        hbmpItem: _type.HBITMAP = _EMPTY


@_struct
class MENUITEMINFOW:
    cbSize: _type.UINT = _SIZE
    fMask: _type.UINT = _EMPTY
    fType: _type.UINT = _EMPTY
    fState: _type.UINT = _EMPTY
    wID: _type.UINT = _EMPTY
    hSubMenu: _type.HMENU = _EMPTY
    hbmpChecked: _type.HBITMAP = _EMPTY
    hbmpUnchecked: _type.HBITMAP = _EMPTY
    dwItemData: _type.ULONG_PTR = _EMPTY
    dwTypeData: _type.LPWSTR = _EMPTY
    cch: _type.UINT = _EMPTY
    if _const.WINVER >= 0x0500:
        hbmpItem: _type.HBITMAP = _EMPTY


@_struct
class NOTIFYICONDATAA:
    cbSize: _type.DWORD = _SIZE
    hWnd: _type.HWND = _EMPTY
    uID: _type.UINT = _EMPTY
    uFlags: _type.UINT = _EMPTY
    uCallbackMessage: _type.UINT = _EMPTY
    hIcon: _type.HICON = _EMPTY
    if _const.NTDDI_VERSION < _const.NTDDI_WIN2K:
        szTip: _type.CHAR * 64 = _EMPTY
    if _const.NTDDI_VERSION >= _const.NTDDI_WIN2K:
        szTip: _type.CHAR * 128 = _EMPTY
        dwState: _type.DWORD = _EMPTY
        dwStateMask: _type.DWORD = _EMPTY
        szInfo: _type.CHAR * 256 = _EMPTY
        # noinspection PyProtectedMember
        if not _const._SHELL_EXPORTS_INTERNALAPI_H_:
            U: _union.NOTIFYICONDATA_U = _EMPTY
        szInfoTitle: _type.CHAR * 64 = _EMPTY
        dwInfoFlags: _type.DWORD = _EMPTY
    if _const.NTDDI_VERSION >= _const.NTDDI_WINXP:
        guidItem: GUID = _EMPTY
    if _const.NTDDI_VERSION >= _const.NTDDI_VISTA:
        hBalloonIcon: _type.HICON = _EMPTY


@_struct
class NOTIFYICONDATAW:
    cbSize: _type.DWORD = _SIZE
    hWnd: _type.HWND = _EMPTY
    uID: _type.UINT = _EMPTY
    uFlags: _type.UINT = _EMPTY
    uCallbackMessage: _type.UINT = _EMPTY
    hIcon: _type.HICON = _EMPTY
    if _const.NTDDI_VERSION < _const.NTDDI_WIN2K:
        szTip: _type.WCHAR * 64 = _EMPTY
    if _const.NTDDI_VERSION >= _const.NTDDI_WIN2K:
        szTip: _type.WCHAR * 128 = _EMPTY
        dwState: _type.DWORD = _EMPTY
        dwStateMask: _type.DWORD = _EMPTY
        szInfo: _type.WCHAR * 256 = _EMPTY
        # noinspection PyProtectedMember
        if not _const._SHELL_EXPORTS_INTERNALAPI_H_:
            U: _union.NOTIFYICONDATA_U = _EMPTY
        szInfoTitle: _type.WCHAR * 64 = _EMPTY
        dwInfoFlags: _type.DWORD = _EMPTY
    if _const.NTDDI_VERSION >= _const.NTDDI_WINXP:
        guidItem: GUID = _EMPTY
    if _const.NTDDI_VERSION >= _const.NTDDI_VISTA:
        hBalloonIcon: _type.HICON = _EMPTY


@_struct
class WNDCLASSA:
    style: _type.UINT = _EMPTY
    lpfnWndProc: _type.WNDPROC = _EMPTY
    cbClsExtra: _type.c_int = _EMPTY
    cbWndExtra: _type.c_int = _EMPTY
    hInstance: _type.HINSTANCE = _EMPTY
    hIcon: _type.HINSTANCE = _EMPTY
    hCursor: _type.HCURSOR = _EMPTY
    hbrBackground: _type.HBRUSH = _EMPTY
    lpszMenuName: _type.LPCSTR = _EMPTY
    lpszClassName: _type.LPCSTR = _EMPTY


@_struct
class WNDCLASSW:
    style: _type.UINT = _EMPTY
    lpfnWndProc: _type.WNDPROC = _EMPTY
    cbClsExtra: _type.c_int = _EMPTY
    cbWndExtra: _type.c_int = _EMPTY
    hInstance: _type.HINSTANCE = _EMPTY
    hIcon: _type.HINSTANCE = _EMPTY
    hCursor: _type.HCURSOR = _EMPTY
    hbrBackground: _type.HBRUSH = _EMPTY
    lpszMenuName: _type.LPCWSTR = _EMPTY
    lpszClassName: _type.LPCWSTR = _EMPTY


@_struct
class WNDCLASSEXA:
    cbSize: _type.UINT = _SIZE
    style: _type.UINT = _EMPTY
    lpfnWndProc: _type.WNDPROC = _EMPTY
    cbClsExtra: _type.c_int = _EMPTY
    cbWndExtra: _type.c_int = _EMPTY
    hInstance: _type.HINSTANCE = _EMPTY
    hIcon: _type.HINSTANCE = _EMPTY
    hCursor: _type.HCURSOR = _EMPTY
    hbrBackground: _type.HBRUSH = _EMPTY
    lpszMenuName: _type.LPCSTR = _EMPTY
    lpszClassName: _type.LPCSTR = _EMPTY
    hIconSm: _type.HICON = _EMPTY


@_struct
class WNDCLASSEXW:
    cbSize: _type.UINT = _SIZE
    style: _type.UINT = _EMPTY
    lpfnWndProc: _type.WNDPROC = _EMPTY
    cbClsExtra: _type.c_int = _EMPTY
    cbWndExtra: _type.c_int = _EMPTY
    hInstance: _type.HINSTANCE = _EMPTY
    hIcon: _type.HINSTANCE = _EMPTY
    hCursor: _type.HCURSOR = _EMPTY
    hbrBackground: _type.HBRUSH = _EMPTY
    lpszMenuName: _type.LPCWSTR = _EMPTY
    lpszClassName: _type.LPCWSTR = _EMPTY
    hIconSm: _type.HICON = _EMPTY


@_struct
class POINT:
    x: _type.LONG = _EMPTY
    y: _type.LONG = _EMPTY


@_struct
class MSG:
    hwnd: _type.HWND = _EMPTY
    message: _type.UINT = _EMPTY
    wParam: _type.WPARAM = _EMPTY
    lParam: _type.WPARAM = _EMPTY
    time: _type.DWORD = _EMPTY
    pt: POINT = _EMPTY
    lPrivate: _type.DWORD = _EMPTY


@_struct
class PropertyItem:
    id: _type.PROPID = _EMPTY
    length: _type.ULONG = _EMPTY
    type: _type.WORD = _EMPTY
    value: _Pointer[_type.VOID] = _EMPTY


@_struct
class FILETIME:
    dwLowDateTime: _type.DWORD = _EMPTY
    dwHighDateTime: _type.DWORD = _EMPTY


# noinspection PyPep8Naming
@_struct
class WIN32_FIND_DATAA:
    dwFileAttributes: _type.DWORD = _EMPTY
    ftCreationTime: FILETIME = _EMPTY
    ftLastAccessTime: FILETIME = _EMPTY
    ftLastWriteTime: FILETIME = _EMPTY
    nFileSizeHigh: _type.DWORD = _EMPTY
    nFileSizeLow: _type.DWORD = _EMPTY
    dwReserved0: _type.DWORD = _EMPTY
    dwReserved1: _type.DWORD = _EMPTY
    cFileName: _type.CHAR * _const.MAX_PATH = _EMPTY
    cAlternateFileName: _type.CHAR * 14 = _EMPTY
    # noinspection PyProtectedMember
    if _const._MAC:
        dwFileType: _type.DWORD = _EMPTY
        dwCreatorType: _type.DWORD = _EMPTY
        wFinderFlags: _type.WORD = _EMPTY


# noinspection PyPep8Naming
@_struct
class WIN32_FIND_DATAW:
    dwFileAttributes: _type.DWORD = _EMPTY
    ftCreationTime: FILETIME = _EMPTY
    ftLastAccessTime: FILETIME = _EMPTY
    ftLastWriteTime: FILETIME = _EMPTY
    nFileSizeHigh: _type.DWORD = _EMPTY
    nFileSizeLow: _type.DWORD = _EMPTY
    dwReserved0: _type.DWORD = _EMPTY
    dwReserved1: _type.DWORD = _EMPTY
    cFileName: _type.WCHAR * _const.MAX_PATH = _EMPTY
    cAlternateFileName: _type.WCHAR * 14 = _EMPTY
    # noinspection PyProtectedMember
    if _const._MAC:
        dwFileType: _type.DWORD = _EMPTY
        dwCreatorType: _type.DWORD = _EMPTY
        wFinderFlags: _type.WORD = _EMPTY


@_struct
class PROPERTYKEY:
    fmtid: GUID = _EMPTY
    pid: _type.DWORD = _EMPTY


@_struct
class CSPLATFORM:
    dwPlatformId: _type.DWORD = _EMPTY
    dwVersionHi: _type.DWORD = _EMPTY
    dwVersionLo: _type.DWORD = _EMPTY
    dwProcessorArch: _type.DWORD = _EMPTY


# noinspection PyPep8Naming
@_struct
class DECIMAL_U_S:
    scale: _type.BYTE = _EMPTY
    sign: _type.BYTE = _EMPTY


# noinspection PyPep8Naming
@_struct
class DECIMAL_U2_S:
    Lo32: _type.ULONG = _EMPTY
    Mid32: _type.ULONG = _EMPTY


@_struct
class DECIMAL:
    wReserved: _type.USHORT = _EMPTY
    U: _union.DECIMAL_U = _EMPTY
    Hi32: _type.ULONG = _EMPTY
    U2: _union.DECIMAL_U2 = _EMPTY


# noinspection PyPep8Naming
@_struct
class PROPVARIANT_U_S:
    vt: _type.VARTYPE = _EMPTY
    wReserved1: _type.PROPVAR_PAD1 = _EMPTY
    wReserved2: _type.PROPVAR_PAD2 = _EMPTY
    wReserved3: _type.PROPVAR_PAD3 = _EMPTY
    U: _union.PROPVARIANT_U_S_U = _EMPTY


@_struct
class PROPVARIANT:
    U: _union.PROPVARIANT_U = _EMPTY


@_struct
class MOUSEINPUT:
    dx: _type.LONG = _EMPTY
    dy: _type.LONG = _EMPTY
    mouseData: _type.DWORD = _EMPTY
    dwFlags: _type.DWORD = _EMPTY
    time: _type.DWORD = _EMPTY
    dwExtraInfo: _type.ULONG_PTR = _EMPTY


@_struct
class KEYBDINPUT:
    wVk: _type.WORD = _EMPTY
    wScan: _type.WORD = _EMPTY
    dwFlags: _type.DWORD = _EMPTY
    time: _type.DWORD = _EMPTY
    dwExtraInfo: _type.ULONG_PTR = _EMPTY


@_struct
class HARDWAREINPUT:
    uMsg: _type.DWORD = _EMPTY
    wParamL: _type.WORD = _EMPTY
    wParamH: _type.WORD = _EMPTY


@_struct
class INPUT:
    type: _type.DWORD = _EMPTY
    U: _union.INPUT_U = _EMPTY


# noinspection PyPep8Naming
@_struct
class DISPLAY_DEVICEA:
    cb: _type.DWORD = _SIZE
    DeviceName: _type.CHAR * 32 = _EMPTY
    DeviceString: _type.CHAR * 128 = _EMPTY
    StateFlags: _type.DWORD = _EMPTY
    DeviceID: _type.CHAR * 128 = _EMPTY
    DeviceKey: _type.CHAR * 128 = _EMPTY


# noinspection PyPep8Naming
@_struct
class DISPLAY_DEVICEW:
    cb: _type.DWORD = _SIZE
    DeviceName: _type.WCHAR * 32 = _EMPTY
    DeviceString: _type.WCHAR * 128 = _EMPTY
    StateFlags: _type.DWORD = _EMPTY
    DeviceID: _type.WCHAR * 128 = _EMPTY
    DeviceKey: _type.WCHAR * 128 = _EMPTY


@_struct
class BROWSEINFOA:
    hwndOwner: _type.HWND = _EMPTY
    pidlRoot: _Pointer[_Pointer[ITEMIDLIST]] = _EMPTY
    pszDisplayName: _type.LPSTR = _EMPTY
    lpszTitle: _type.LPCSTR = _EMPTY
    ulFlags: _type.UINT = _EMPTY
    lpfn: _type.BFFCALLBACK = _EMPTY
    lParam: _type.LPARAM = _EMPTY
    iImage: _type.c_int = _EMPTY


@_struct
class BROWSEINFOW:
    hwndOwner: _type.HWND = _EMPTY
    pidlRoot: _Pointer[_Pointer[ITEMIDLIST]] = _EMPTY
    pszDisplayName: _type.LPWSTR = _EMPTY
    lpszTitle: _type.LPCWSTR = _EMPTY
    ulFlags: _type.UINT = _EMPTY
    lpfn: _type.BFFCALLBACK = _EMPTY
    lParam: _type.LPARAM = _EMPTY
    iImage: _type.c_int = _EMPTY


@_struct
class PAINTSTRUCT:
    hdc: _type.HDC = _EMPTY
    fErase: _type.BOOL = _EMPTY
    rcPaint: RECT = _EMPTY
    fRestore: _type.BOOL = _EMPTY
    fIncUpdate: _type.BOOL = _EMPTY
    rgbReserved: _type.BYTE * 32 = _EMPTY


# noinspection PyPep8Naming
@_struct
class PICTDESC_U_S:
    hbitmap: _type.HBITMAP = _EMPTY
    hpal: _type.HPALETTE = _EMPTY


# noinspection PyPep8Naming
@_struct
class PICTDESC_U_S2:
    hmeta: _type.HMETAFILE = _EMPTY
    xExt: _type.c_int = _EMPTY
    yExt: _type.c_int = _EMPTY


# noinspection PyPep8Naming
@_struct
class PICTDESC_U_S3:
    hicon: _type.HICON = _EMPTY


# noinspection PyProtectedMember
if _const._WIN32:
    # noinspection PyPep8Naming
    @_struct
    class PICTDESC_U_S4:
        hemf: _type.HMETAFILE = _EMPTY


@_struct
class PICTDESC:
    cbSizeofstruct: _type.UINT = _SIZE
    picType: _type.UINT = _EMPTY
    U: _union.PICTDESC_U = _EMPTY


@_struct
class MONITORINFO:
    cbSize: _type.DWORD = _SIZE
    rcMonitor: RECT = _EMPTY
    rcWork: RECT = _EMPTY
    dwFlags: _type.DWORD = _EMPTY


@_struct
class MONITORINFOEXA:
    S: MONITORINFO = _EMPTY
    szDevice: _type.CHAR * _const.CCHDEVICENAME = _EMPTY


@_struct
class MONITORINFOEXW:
    S: MONITORINFO = _EMPTY
    szDevice: _type.WCHAR * _const.CCHDEVICENAME = _EMPTY


# noinspection PyPep8Naming
@_struct
class VARIANT_U_S:
    vt: _type.VARTYPE = _EMPTY
    wReserved1: _type.WORD = _EMPTY
    wReserved2: _type.WORD = _EMPTY
    wReserved3: _type.WORD = _EMPTY
    U: _union.VARIANT_U_S_U = _EMPTY


@_struct
class VARIANT:
    U: _union.VARIANT_U = _EMPTY


# noinspection PyPep8Naming
@_struct
class SP_DEVINFO_DATA:
    cbSize: _type.DWORD = _SIZE
    ClassGuid: GUID = _EMPTY
    DevInst: _type.DWORD = _EMPTY
    Reserved: _type.ULONG_PTR = _EMPTY


# noinspection PyPep8Naming
@_struct
class SP_DEVICE_INTERFACE_DATA:
    cbSize: _type.DWORD = _SIZE
    InterfaceClassGuid: GUID = _EMPTY
    Flags: _type.DWORD = _EMPTY
    Reserved: _type.ULONG_PTR = _EMPTY


# noinspection PyPep8Naming
@_struct
class SP_DEVICE_INTERFACE_DETAIL_DATA_A:
    cbSize: _type.DWORD = _SIZE
    DevicePath: _type.CHAR * _const.ANYSIZE_ARRAY = _EMPTY


# noinspection PyPep8Naming
@_struct
class SP_DEVICE_INTERFACE_DETAIL_DATA_W:
    cbSize: _type.DWORD = _SIZE
    DevicePath: _type.WCHAR * _const.ANYSIZE_ARRAY = _EMPTY


@_struct
class DEVPROPKEY:
    fmtid: DEVPROPGUID = _EMPTY
    pid: _type.DEVPROPID = _EMPTY


@_struct
class BLENDFUNCTION:
    BlendOp: _type.BYTE = _EMPTY
    BlendFlags: _type.BYTE = _EMPTY
    SourceConstantAlpha: _type.BYTE = _EMPTY
    AlphaFormat: _type.BYTE = _EMPTY


@_struct
class ColorMap:
    oldColor: _type.Color = _EMPTY
    newColor: _type.Color = _EMPTY


@_struct
class ColorMatrix:
    m: _type.REAL * 5 * 5 = _EMPTY


@_struct
class EventRegistrationToken:
    value: _type.c_int64 = _EMPTY


@_struct
class Rational:
    Numerator: _type.UINT32 = _EMPTY
    Denominator: _type.UINT32 = _EMPTY


@_struct
class EncoderParameter:
    Guid: GUID = _EMPTY
    NumberOfValues: _type.ULONG = _EMPTY
    Type: _type.ULONG = _EMPTY
    Value: _Pointer[_type.VOID] = _EMPTY


@_struct
class EncoderParameters:
    Count: _type.UINT = _EMPTY
    # noinspection PyTypeChecker
    Parameter: EncoderParameter * 1 = _EMPTY


@_struct
class ImageCodecInfo:
    Clsid: CLSID = _EMPTY
    FormatID: GUID = _EMPTY
    CodecName: _type.LPWSTR = _EMPTY
    DllName: _type.LPWSTR = _EMPTY
    FormatDescription: _type.LPWSTR = _EMPTY
    FilenameExtension: _type.LPWSTR = _EMPTY
    MimeType: _type.LPWSTR = _EMPTY
    Flags: _type.DWORD = _EMPTY
    Version: _type.DWORD = _EMPTY
    SigCount: _type.DWORD = _EMPTY
    SigSize: _type.DWORD = _EMPTY
    SigPattern: _Pointer[_type.BYTE] = _EMPTY
    SigMask: _Pointer[_type.BYTE] = _EMPTY


@_struct
class OPENASINFO:
    pcszFile: _type.LPCWSTR = _EMPTY
    pcszClass: _type.LPCWSTR = _EMPTY
    oaifInFlags: _enum.OPEN_AS_INFO_FLAGS = _EMPTY


@_struct
class SHELLEXECUTEINFOA:
    cbSize: _type.DWORD = _SIZE
    fMask: _type.ULONG = _EMPTY
    hwnd: _type.HWND = _EMPTY
    lpVerb: _type.LPCSTR = _EMPTY
    lpFile: _type.LPCSTR = _EMPTY
    lpParameters: _type.LPCSTR = _EMPTY
    lpDirectory: _type.LPCSTR = _EMPTY
    nShow: _type.c_int = _EMPTY
    hInstApp: _type.HINSTANCE = _EMPTY
    lpIDList: _type.c_void_p = _EMPTY
    lpClass: _type.LPCSTR = _EMPTY
    hkeyClass: _type.HKEY = _EMPTY
    dwHotKey: _type.DWORD = _EMPTY
    U: _union.SHELLEXECUTEINFO_U = _EMPTY
    hProcess: _type.HANDLE = _EMPTY


@_struct
class SHELLEXECUTEINFOW:
    cbSize: _type.DWORD = _SIZE
    fMask: _type.ULONG = _EMPTY
    hwnd: _type.HWND = _EMPTY
    lpVerb: _type.LPCWSTR = _EMPTY
    lpFile: _type.LPCWSTR = _EMPTY
    lpParameters: _type.LPCWSTR = _EMPTY
    lpDirectory: _type.LPCWSTR = _EMPTY
    nShow: _type.c_int = _EMPTY
    hInstApp: _type.HINSTANCE = _EMPTY
    lpIDList: _type.c_void_p = _EMPTY
    lpClass: _type.LPCWSTR = _EMPTY
    hkeyClass: _type.HKEY = _EMPTY
    dwHotKey: _type.DWORD = _EMPTY
    U: _union.SHELLEXECUTEINFO_U = _EMPTY
    hProcess: _type.HANDLE = _EMPTY


@_struct
class COMPPOS:
    dwSize: _type.DWORD = _SIZE
    iLeft: _type.c_int = _EMPTY
    iTop: _type.c_int = _EMPTY
    dwWidth: _type.DWORD = _EMPTY
    dwHeight: _type.DWORD = _EMPTY
    izIndex: _type.c_int = _EMPTY
    fCanResize: _type.BOOL = _EMPTY
    fCanResizeX: _type.BOOL = _EMPTY
    fCanResizeY: _type.BOOL = _EMPTY
    iPreferredLeftPercent: _type.c_int = _EMPTY
    iPreferredTopPercent: _type.c_int = _EMPTY


@_struct
class COMPSTATEINFO:
    dwSize: _type.DWORD = _SIZE
    iLeft: _type.c_int = _EMPTY
    iTop: _type.c_int = _EMPTY
    dwWidth: _type.DWORD = _EMPTY
    dwHeight: _type.DWORD = _EMPTY
    dwItemState: _type.DWORD = _EMPTY


@_struct
class COMPONENT:
    dwSize: _type.DWORD = _SIZE
    dwID: _type.DWORD = _EMPTY
    iComponentType: _type.c_int = _EMPTY
    fChecked: _type.BOOL = _EMPTY
    fDirty: _type.BOOL = _EMPTY
    fNoScroll: _type.BOOL = _EMPTY
    cpPos: COMPPOS = _EMPTY
    wszFriendlyName: _type.WCHAR * _const.MAX_PATH = _EMPTY
    wszSource: _type.WCHAR * _const.INTERNET_MAX_URL_LENGTH = _EMPTY
    wszSubscribedURL: _type.WCHAR * _const.INTERNET_MAX_URL_LENGTH = _EMPTY
    dwCurItemState: _type.DWORD = _EMPTY
    csiOriginal: COMPSTATEINFO = _EMPTY
    csiRestored: COMPSTATEINFO = _EMPTY


@_struct
class DROPSTRUCT:
    hwndSource: _type.HWND = _EMPTY
    hwndSink: _type.HWND = _EMPTY
    wFmt: _type.DWORD = _EMPTY
    dwData: _type.ULONG_PTR = _EMPTY
    ptDrop: POINT = _EMPTY
    dwControlData: _type.DWORD = _EMPTY


@_struct
class DRAWTEXTPARAMS:
    cbSize: _type.UINT = _SIZE
    iTabLength: _type.c_int = _EMPTY
    iLeftMargin: _type.c_int = _EMPTY
    iRightMargin: _type.c_int = _EMPTY
    uiLengthDrawn: _type.UINT = _EMPTY


@_struct
class COMPONENTSOPT:
    dwSize: _type.DWORD = _SIZE
    fEnableComponents: _type.BOOL = _EMPTY
    fActiveDesktop: _type.BOOL = _EMPTY


@_struct
class TPMPARAMS:
    cbSize: _type.UINT = _SIZE
    rcExclude: RECT = _EMPTY


@_struct
class MENUITEMTEMPLATEHEADER:
    versionNumber: _type.WORD = _EMPTY
    offset: _type.WORD = _EMPTY


@_struct
class MENUITEMTEMPLATE:
    mtOption: _type.WORD = _EMPTY
    mtID: _type.WORD = _EMPTY
    mtString: _type.WCHAR * 1 = _EMPTY


@_struct
class Size:
    Width: _type.FLOAT = _EMPTY
    Height: _type.FLOAT = _EMPTY


@_struct
class Color:
    A: _type.BYTE = _EMPTY
    R: _type.BYTE = _EMPTY
    G: _type.BYTE = _EMPTY
    B: _type.BYTE = _EMPTY


@_struct
class STRING:
    Length: _type.USHORT = _EMPTY
    MaximumLength: _type.USHORT = _EMPTY
    Buffer: _type.PCHAR = _EMPTY


# noinspection PyPep8Naming
@_struct
class UNICODE_STRING:
    Length: _type.USHORT = _EMPTY
    MaximumLength: _type.USHORT = _EMPTY
    Buffer: _type.PWSTR = _EMPTY


@_struct
class INITCOMMONCONTROLSEX:
    dwSize: _type.DWORD = _SIZE
    dwICC: _type.DWORD = _EMPTY


@_struct
class COLORSCHEME:
    dwSize: _type.DWORD = _SIZE
    clrBtnHighlight: _type.COLORREF = _EMPTY
    clrBtnShadow: _type.COLORREF = _EMPTY


@_struct
class DTBGOPTS:
    dwSize: _type.DWORD = _SIZE
    dwFlags: _type.DWORD = _EMPTY
    rcClip: RECT = _EMPTY


@_struct
class TEXTMETRICA:
    tmHeight: _type.LONG = _EMPTY
    tmAscent: _type.LONG = _EMPTY
    tmDescent: _type.LONG = _EMPTY
    tmInternalLeading: _type.LONG = _EMPTY
    tmExternalLeading: _type.LONG = _EMPTY
    tmAveCharWidth: _type.LONG = _EMPTY
    tmMaxCharWidth: _type.LONG = _EMPTY
    tmWeight: _type.LONG = _EMPTY
    tmOverhang: _type.LONG = _EMPTY
    tmDigitizedAspectX: _type.LONG = _EMPTY
    tmDigitizedAspectY: _type.LONG = _EMPTY
    tmFirstChar: _type.BYTE = _EMPTY
    tmLastChar: _type.BYTE = _EMPTY
    tmDefaultChar: _type.BYTE = _EMPTY
    tmBreakChar: _type.BYTE = _EMPTY
    tmItalic: _type.BYTE = _EMPTY
    tmUnderlined: _type.BYTE = _EMPTY
    tmStruckOut: _type.BYTE = _EMPTY
    tmPitchAndFamily: _type.BYTE = _EMPTY
    tmCharSet: _type.BYTE = _EMPTY


@_struct
class TEXTMETRICW:
    tmHeight: _type.LONG = _EMPTY
    tmAscent: _type.LONG = _EMPTY
    tmDescent: _type.LONG = _EMPTY
    tmInternalLeading: _type.LONG = _EMPTY
    tmExternalLeading: _type.LONG = _EMPTY
    tmAveCharWidth: _type.LONG = _EMPTY
    tmMaxCharWidth: _type.LONG = _EMPTY
    tmWeight: _type.LONG = _EMPTY
    tmOverhang: _type.LONG = _EMPTY
    tmDigitizedAspectX: _type.LONG = _EMPTY
    tmDigitizedAspectY: _type.LONG = _EMPTY
    tmFirstChar: _type.WCHAR = _EMPTY
    tmLastChar: _type.WCHAR = _EMPTY
    tmDefaultChar: _type.WCHAR = _EMPTY
    tmBreakChar: _type.WCHAR = _EMPTY
    tmItalic: _type.BYTE = _EMPTY
    tmUnderlined: _type.BYTE = _EMPTY
    tmStruckOut: _type.BYTE = _EMPTY
    tmPitchAndFamily: _type.BYTE = _EMPTY
    tmCharSet: _type.BYTE = _EMPTY


@_struct
class LOGFONTA:
    lfHeight: _type.LONG = _EMPTY
    lfWidth: _type.LONG = _EMPTY
    lfEscapement: _type.LONG = _EMPTY
    lfOrientation: _type.LONG = _EMPTY
    lfWeight: _type.LONG = _EMPTY
    lfItalic: _type.BYTE = _EMPTY
    lfUnderline: _type.BYTE = _EMPTY
    lfStrikeOut: _type.BYTE = _EMPTY
    lfCharSet: _type.BYTE = _EMPTY
    lfOutPrecision: _type.BYTE = _EMPTY
    lfClipPrecision: _type.BYTE = _EMPTY
    lfQuality: _type.BYTE = _EMPTY
    lfPitchAndFamily: _type.BYTE = _EMPTY
    lfFaceName: _type.CHAR * _const.LF_FACESIZE = _EMPTY


@_struct
class LOGFONTW:
    lfHeight: _type.LONG = _EMPTY
    lfWidth: _type.LONG = _EMPTY
    lfEscapement: _type.LONG = _EMPTY
    lfOrientation: _type.LONG = _EMPTY
    lfWeight: _type.LONG = _EMPTY
    lfItalic: _type.BYTE = _EMPTY
    lfUnderline: _type.BYTE = _EMPTY
    lfStrikeOut: _type.BYTE = _EMPTY
    lfCharSet: _type.BYTE = _EMPTY
    lfOutPrecision: _type.BYTE = _EMPTY
    lfClipPrecision: _type.BYTE = _EMPTY
    lfQuality: _type.BYTE = _EMPTY
    lfPitchAndFamily: _type.BYTE = _EMPTY
    lfFaceName: _type.WCHAR * _const.LF_FACESIZE = _EMPTY


@_struct
class MARGINS:
    cxLeftWidth: _type.c_int = _EMPTY
    cxRightWidth: _type.c_int = _EMPTY
    cyTopHeight: _type.c_int = _EMPTY
    cyBottomHeight: _type.c_int = _EMPTY


@_struct
class INTLIST:
    iValueCount: _type.c_int = _EMPTY
    iValues: _type.c_int * _const.MAX_INTLIST_COUNT = _EMPTY


# noinspection PyPep8Naming
@_struct
class WTA_OPTIONS:
    dwFlags: _type.DWORD = _EMPTY
    dwMask: _type.DWORD = _EMPTY


@_struct
class GUITHREADINFO:
    cbSize: _type.DWORD = _SIZE
    flags: _type.DWORD = _EMPTY
    hwndActive: _type.HWND = _EMPTY
    hwndFocus: _type.HWND = _EMPTY
    hwndCapture: _type.HWND = _EMPTY
    hwndMenuOwner: _type.HWND = _EMPTY
    hwndMoveSize: _type.HWND = _EMPTY
    hwndCaret: _type.HWND = _EMPTY
    rcCaret: RECT = _EMPTY


@_struct
class DLGTEMPLATE:
    style: _type.DWORD = _EMPTY
    dwExtendedStyle: _type.DWORD = _EMPTY
    cdit: _type.WORD = _EMPTY
    x: _type.c_short = _EMPTY
    y: _type.c_short = _EMPTY
    cx: _type.c_short = _EMPTY
    cy: _type.c_short = _EMPTY


@_struct
class TTTOOLINFOA:
    cbSize: _type.UINT = _SIZE
    uFlags: _type.UINT = _EMPTY
    hwnd: _type.HWND = _EMPTY
    uId: _type.UINT_PTR = _EMPTY
    rect: RECT = _EMPTY
    hinst: _type.HINSTANCE = _EMPTY
    lpszText: _type.LPSTR = _EMPTY
    lParam: _type.LPARAM = _EMPTY
    if _const.NTDDI_VERSION >= _const.NTDDI_WINXP:
        lpReserved: _type.c_void_p = _EMPTY


@_struct
class TTTOOLINFOW:
    cbSize: _type.UINT = _SIZE
    uFlags: _type.UINT = _EMPTY
    hwnd: _type.HWND = _EMPTY
    uId: _type.UINT_PTR = _EMPTY
    rect: RECT = _EMPTY
    hinst: _type.HINSTANCE = _EMPTY
    lpszText: _type.LPWSTR = _EMPTY
    lParam: _type.LPARAM = _EMPTY
    if _const.NTDDI_VERSION >= _const.NTDDI_WINXP:
        lpReserved: _type.c_void_p = _EMPTY


@_struct
class TRACKMOUSEEVENT:
    cbSize: _type.DWORD = _SIZE
    dwFlags: _type.DWORD = _EMPTY
    hwndTrack: _type.HWND = _EMPTY
    dwHoverTime: _type.DWORD = _EMPTY


@_struct
class RBHITTESTINFO:
    pt: POINT = _EMPTY
    flags: _type.UINT = _EMPTY
    iBand: _type.c_int = _EMPTY


@_struct
class ACTCTXA:
    cbSize: _type.ULONG = _SIZE
    dwFlags: _type.DWORD = _EMPTY
    lpSource: _type.LPCSTR = _EMPTY
    wProcessorArchitecture: _type.USHORT = _EMPTY
    wLangId: _type.LANGID = _EMPTY
    lpAssemblyDirectory: _type.LPCSTR = _EMPTY
    lpResourceName: _type.LPCSTR = _EMPTY
    lpApplicationName: _type.LPCSTR = _EMPTY
    hModule: _type.HMODULE = _EMPTY


@_struct
class ACTCTXW:
    cbSize: _type.ULONG = _SIZE
    dwFlags: _type.DWORD = _EMPTY
    lpSource: _type.LPCWSTR = _EMPTY
    wProcessorArchitecture: _type.USHORT = _EMPTY
    wLangId: _type.LANGID = _EMPTY
    lpAssemblyDirectory: _type.LPCWSTR = _EMPTY
    lpResourceName: _type.LPCWSTR = _EMPTY
    lpApplicationName: _type.LPCWSTR = _EMPTY
    hModule: _type.HMODULE = _EMPTY


@_struct
class SYSTEMTIME:
    wYear: _type.WORD = _EMPTY
    wMonth: _type.WORD = _EMPTY
    wDayOfWeek: _type.WORD = _EMPTY
    wDay: _type.WORD = _EMPTY
    wHour: _type.WORD = _EMPTY
    wMinute: _type.WORD = _EMPTY
    wSecond: _type.WORD = _EMPTY
    wMilliseconds: _type.WORD = _EMPTY


@_struct
class OSVERSIONINFOA:
    dwOSVersionInfoSize: _type.DWORD = _EMPTY
    dwMajorVersion: _type.DWORD = _EMPTY
    dwMinorVersion: _type.DWORD = _EMPTY
    dwBuildNumber: _type.DWORD = _EMPTY
    dwPlatformId: _type.DWORD = _EMPTY
    szCSDVersion: _type.CHAR * 128 = _EMPTY


@_struct
class OSVERSIONINFOW:
    dwOSVersionInfoSize: _type.DWORD = _EMPTY
    dwMajorVersion: _type.DWORD = _EMPTY
    dwMinorVersion: _type.DWORD = _EMPTY
    dwBuildNumber: _type.DWORD = _EMPTY
    dwPlatformId: _type.DWORD = _EMPTY
    szCSDVersion: _type.WCHAR * 128 = _EMPTY


@_struct
class DLLVERSIONINFO:
    cbSize: _type.DWORD = _SIZE
    dwMajorVersion: _type.DWORD = _EMPTY
    dwMinorVersion: _type.DWORD = _EMPTY
    dwBuildNumber: _type.DWORD = _EMPTY
    dwPlatformID: _type.DWORD = _EMPTY


@_struct
class DLLVERSIONINFO2:
    info1: DLLVERSIONINFO = _EMPTY
    dwFlags: _type.DWORD = _EMPTY
    ullVersion: _type.ULONGLONG = _EMPTY


UUID = GUID
IID = GUID
CLSID = GUID
KNOWNFOLDERID = GUID
DEVPROPGUID = GUID
VARIANTARG = VARIANT
ANSI_STRING = STRING
OEM_STRING = STRING


def _init(item: str) -> type[_ctypes.Structure]:
    _globals.check_item(item)

    class Struct(_ctypes.Structure):
        _fields_ = tuple((name, _resolve_type(type_)) for name, type_ in _globals.get_type_hints(item))

        def __init__(self, *args, **kwargs):
            for name, val in self._defaults[len(args):]:
                if val is not _EMPTY and name not in kwargs:
                    kwargs[name] = val
            super().__init__(*args, **kwargs)

    # noinspection PyProtectedMember
    Struct._defaults = tuple((field[0], _ctypes.sizeof(
        Struct) if (val := getattr(_globals.vars_[item], field[0])) is _SIZE else val) for field in Struct._fields_)
    return _functools.update_wrapper(Struct, _globals.vars_[item], _ASSIGNED, ())


_globals = _Globals()
