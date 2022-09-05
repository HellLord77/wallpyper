from __future__ import annotations as _

import ctypes as _ctypes
import typing as _typing
from typing import Optional as _Optional

from . import const as _const, enum as _enum, type as _type, union as _union
from ._utils import _CT, _Globals, _Pointer, _fields_repr, _resolve_type

if None:
    from dataclasses import dataclass as _struct
else:
    from ._utils import _dummy as _struct

_CACHE = {}  # FIXME https://github.com/python/mypy/issues/5107
_SIZE = object()


def _bitfield(type_: type[_CT], size: int) -> type[_CT]:
    try:
        return _CACHE[type_, size]
    except KeyError:
        bitfield = type(type_.__name__, (type_,), {'_bitfield': size})
        _CACHE[type_, size] = bitfield
        # noinspection PyTypeChecker
        return bitfield


@_struct
class WINDOWCOMPOSITIONATTRIBDATA:
    Attrib: _enum.WINDOWCOMPOSITIONATTRIB = None
    pvData: _type.PVOID = None
    cbData: _type.SIZE_T = None


@_struct
class FILE:
    _Placeholder: _type.c_void_p = None


@_struct
class COMMPROP:
    wPacketLength: _type.WORD = None
    wPacketVersion: _type.WORD = None
    dwServiceMask: _type.DWORD = None
    dwReserved1: _type.DWORD = None
    dwMaxTxQueue: _type.DWORD = None
    dwMaxRxQueue: _type.DWORD = None
    dwMaxBaud: _type.DWORD = None
    dwProvSubType: _type.DWORD = None
    dwProvCapabilities: _type.DWORD = None
    dwSettableParams: _type.DWORD = None
    dwSettableBaud: _type.DWORD = None
    wSettableData: _type.WORD = None
    wSettableStopParity: _type.WORD = None
    dwCurrentTxQueue: _type.DWORD = None
    dwCurrentRxQueue: _type.DWORD = None
    dwProvSpec1: _type.DWORD = None
    dwProvSpec2: _type.DWORD = None
    wcProvChar: _type.WORD * 1 = None


@_struct
class COMSTAT:
    fCtsHold: _bitfield(_type.DWORD, 1) = None
    fDsrHold: _bitfield(_type.DWORD, 1) = None
    fRlsdHold: _bitfield(_type.DWORD, 1) = None
    fXoffHold: _bitfield(_type.DWORD, 1) = None
    fXoffSent: _bitfield(_type.DWORD, 1) = None
    fEof: _bitfield(_type.DWORD, 1) = None
    fTxim: _bitfield(_type.DWORD, 1) = None
    fReserved: _bitfield(_type.DWORD, 25) = None
    cbInQue: _type.DWORD = None
    cbOutQue: _type.DWORD = None


@_struct
class DCB:
    DCBlength: _type.DWORD = _SIZE
    BaudRate: _type.DWORD = None
    fBinary: _bitfield(_type.DWORD, 1) = None
    fParity: _bitfield(_type.DWORD, 1) = None
    fOutxCtsFlow: _bitfield(_type.DWORD, 1) = None
    fOutxDsrFlow: _bitfield(_type.DWORD, 1) = None
    fDtrControl: _bitfield(_type.DWORD, 2) = None
    fDsrSensitivity: _bitfield(_type.DWORD, 1) = None
    fTXContinueOnXoff: _bitfield(_type.DWORD, 1) = None
    fOutX: _bitfield(_type.DWORD, 1) = None
    fInX: _bitfield(_type.DWORD, 1) = None
    fErrorChar: _bitfield(_type.DWORD, 1) = None
    fNull: _bitfield(_type.DWORD, 1) = None
    fRtsControl: _bitfield(_type.DWORD, 2) = None
    fAbortOnError: _bitfield(_type.DWORD, 1) = None
    fDummy2: _bitfield(_type.DWORD, 17) = None
    wReserved: _type.WORD = None
    XonLim: _type.WORD = None
    XoffLim: _type.WORD = None
    ByteSize: _type.BYTE = None
    Parity: _type.BYTE = None
    StopBits: _type.BYTE = None
    XonChar: _type.c_char = None
    XoffChar: _type.c_char = None
    ErrorChar: _type.c_char = None
    EofChar: _type.c_char = None
    EvtChar: _type.c_char = None
    wReserved1: _type.WORD = None


@_struct
class COMMTIMEOUTS:
    ReadIntervalTimeout: _type.DWORD = None
    ReadTotalTimeoutMultiplier: _type.DWORD = None
    ReadTotalTimeoutConstant: _type.DWORD = None
    WriteTotalTimeoutMultiplier: _type.DWORD = None
    WriteTotalTimeoutConstant: _type.DWORD = None


@_struct
class COMMCONFIG:
    dwSize: _type.DWORD = _SIZE
    wVersion: _type.WORD = None
    wReserved: _type.WORD = None
    dcb: DCB = None
    dwProviderSubType: _type.DWORD = None
    dwProviderOffset: _type.DWORD = None
    dwProviderSize: _type.DWORD = None
    wcProviderData: _type.WCHAR * 1 = None


@_struct
class GdiplusStartupInput:
    GdiplusVersion: _type.UINT32 = 1
    DebugEventCallback: _type.DebugEventProc = None
    SuppressBackgroundThread: _type.BOOL = None
    SuppressExternalCodecs: _type.BOOL = None


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
    rgbReserved: _type.BYTE = None


@_struct
class BITMAPINFOHEADER:
    biSize: _type.DWORD = _SIZE
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
    bmiColors: RGBQUAD * 1 = None  # TODO _array (type hint)


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
    lStructSize: _type.DWORD = _SIZE
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
    lStructSize: _type.DWORD = _SIZE
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
    dwSize: _type.DWORD = _SIZE
    dwStyle: _type.DWORD = None


@_struct
class POINT:
    x: _type.LONG = None
    y: _type.LONG = None


@_struct
class RECT:
    left: _type.LONG = None
    top: _type.LONG = None
    right: _type.LONG = None
    bottom: _type.LONG = None


@_struct
class SIZE:
    cx: _type.LONG = None
    cy: _type.LONG = None


@_struct
class COORD:
    X: _type.SHORT = None
    Y: _type.SHORT = None


# noinspection PyPep8Naming
@_struct
class SMALL_RECT:
    Left: _type.SHORT = None
    Top: _type.SHORT = None
    Right: _type.SHORT = None
    Bottom: _type.SHORT = None


@_struct
class MENUINFO:
    cbSize: _type.DWORD = _SIZE
    fMask: _type.DWORD = None
    dwStyle: _type.DWORD = None
    cyMax: _type.UINT = None
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
    cbSize: _type.UINT = _SIZE
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
    cbSize: _type.UINT = _SIZE
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
    cbSize: _type.DWORD = _SIZE
    hWnd: _type.HWND = None
    uID: _type.UINT = None
    uFlags: _type.UINT = None
    uCallbackMessage: _type.UINT = None
    hIcon: _type.HICON = None
    if _const.NTDDI_VERSION < _const.NTDDI_WIN2K:
        szTip: _type.CHAR * 64 = None
    else:
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
    cbSize: _type.DWORD = _SIZE
    hWnd: _type.HWND = None
    uID: _type.UINT = None
    uFlags: _type.UINT = None
    uCallbackMessage: _type.UINT = None
    hIcon: _type.HICON = None
    if _const.NTDDI_VERSION < _const.NTDDI_WIN2K:
        szTip: _type.WCHAR * 64 = None
    else:
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
class NOTIFYICONIDENTIFIER:
    cbSize: _type.DWORD = _SIZE
    hWnd: _type.HWND = None
    uID: _type.UINT = None
    guidItem: GUID = None


@_struct
class WNDCLASSA:
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


@_struct
class WNDCLASSW:
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


@_struct
class WNDCLASSEXA:
    cbSize: _type.UINT = _SIZE
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
    cbSize: _type.UINT = _SIZE
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
    cb: _type.DWORD = _SIZE
    DeviceName: _type.CHAR * 32 = None
    DeviceString: _type.CHAR * 128 = None
    StateFlags: _type.DWORD = None
    DeviceID: _type.CHAR * 128 = None
    DeviceKey: _type.CHAR * 128 = None


# noinspection PyPep8Naming
@_struct
class DISPLAY_DEVICEW:
    cb: _type.DWORD = _SIZE
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


# noinspection PyPep8Naming
@_struct
class PICTDESC_U_S4:
    hemf: _type.HMETAFILE = None


@_struct
class PICTDESC:
    cbSizeofstruct: _type.UINT = _SIZE
    picType: _type.UINT = None
    U: _union.PICTDESC_U = None


@_struct
class MONITORINFO:
    cbSize: _type.DWORD = _SIZE
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
    cbSize: _type.DWORD = _SIZE
    ClassGuid: GUID = None
    DevInst: _type.DWORD = None
    Reserved: _type.ULONG_PTR = None


# noinspection PyPep8Naming
@_struct
class SP_DEVICE_INTERFACE_DATA:
    cbSize: _type.DWORD = _SIZE
    InterfaceClassGuid: GUID = None
    Flags: _type.DWORD = None
    Reserved: _type.ULONG_PTR = None


# noinspection PyPep8Naming
@_struct
class SP_DEVICE_INTERFACE_DETAIL_DATA_A:
    cbSize: _type.DWORD = _SIZE
    DevicePath: _type.CHAR * _const.ANYSIZE_ARRAY = None


# noinspection PyPep8Naming
@_struct
class SP_DEVICE_INTERFACE_DETAIL_DATA_W:
    cbSize: _type.DWORD = _SIZE
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
class ColorMatrix:
    m: _type.REAL * 5 * 5 = None


@_struct
class EventRegistrationToken:
    value: _type.c_int64 = None


@_struct
class Rational:
    Numerator: _type.UINT32 = None
    Denominator: _type.UINT32 = None


@_struct
class OPENASINFO:
    pcszFile: _type.LPCWSTR = None
    pcszClass: _type.LPCWSTR = None
    oaifInFlags: _enum.OPEN_AS_INFO_FLAGS = None


# noinspection PyPep8Naming
@_struct
class CONSOLE_READCONSOLE_CONTROL:
    nLength: _type.ULONG = None
    nInitialChars: _type.ULONG = None
    dwCtrlWakeupMask: _type.ULONG = None
    dwControlKeyState: _type.ULONG = None


# noinspection PyPep8Naming
@_struct
class CHAR_INFO:
    Char: _union.CHAR_INFO_U = None
    Attributes: _type.WORD = None


# noinspection PyPep8Naming
@_struct
class CONSOLE_FONT_INFO:
    nFont: _type.DWORD = None
    dwFontSize: COORD = None


# noinspection PyPep8Naming
@_struct
class CONSOLE_FONT_INFOEX:
    cbSize: _type.ULONG = _SIZE
    nFont: _type.DWORD = None
    dwFontSize: COORD = None
    FontFamily: _type.UINT = None
    FontWeight: _type.UINT = None
    FaceName: _type.WCHAR * _const.LF_FACESIZE = None


# noinspection PyPep8Naming
@_struct
class CONSOLE_SELECTION_INFO:
    dwFlags: _type.DWORD = None
    dwSelectionAnchor: COORD = None
    srSelection: SMALL_RECT = None


# noinspection PyPep8Naming
@_struct
class CONSOLE_HISTORY_INFO:
    cbSize: _type.UINT = _SIZE
    HistoryBufferSize: _type.UINT = None
    NumberOfHistoryBuffers: _type.UINT = None
    dwFlags: _type.DWORD = None


@_struct
class SHELLEXECUTEINFOA:
    cbSize: _type.DWORD = _SIZE
    fMask: _type.ULONG = None
    hwnd: _type.HWND = None
    lpVerb: _type.LPCSTR = None
    lpFile: _type.LPCSTR = None
    lpParameters: _type.LPCSTR = None
    lpDirectory: _type.LPCSTR = None
    nShow: _type.c_int = None
    hInstApp: _type.HINSTANCE = None
    lpIDList: _type.c_void_p = None
    lpClass: _type.LPCSTR = None
    hkeyClass: _type.HKEY = None
    dwHotKey: _type.DWORD = None
    U: _union.SHELLEXECUTEINFO_U = None
    hProcess: _type.HANDLE = None


@_struct
class SHELLEXECUTEINFOW:
    cbSize: _type.DWORD = _SIZE
    fMask: _type.ULONG = None
    hwnd: _type.HWND = None
    lpVerb: _type.LPCWSTR = None
    lpFile: _type.LPCWSTR = None
    lpParameters: _type.LPCWSTR = None
    lpDirectory: _type.LPCWSTR = None
    nShow: _type.c_int = None
    hInstApp: _type.HINSTANCE = None
    lpIDList: _type.c_void_p = None
    lpClass: _type.LPCWSTR = None
    hkeyClass: _type.HKEY = None
    dwHotKey: _type.DWORD = None
    U: _union.SHELLEXECUTEINFO_U = None
    hProcess: _type.HANDLE = None


@_struct
class COMPPOS:
    dwSize: _type.DWORD = _SIZE
    iLeft: _type.c_int = None
    iTop: _type.c_int = None
    dwWidth: _type.DWORD = None
    dwHeight: _type.DWORD = None
    izIndex: _type.c_int = None
    fCanResize: _type.BOOL = None
    fCanResizeX: _type.BOOL = None
    fCanResizeY: _type.BOOL = None
    iPreferredLeftPercent: _type.c_int = None
    iPreferredTopPercent: _type.c_int = None


@_struct
class COMPSTATEINFO:
    dwSize: _type.DWORD = _SIZE
    iLeft: _type.c_int = None
    iTop: _type.c_int = None
    dwWidth: _type.DWORD = None
    dwHeight: _type.DWORD = None
    dwItemState: _type.DWORD = None


@_struct
class COMPONENT:
    dwSize: _type.DWORD = _SIZE
    dwID: _type.DWORD = None
    iComponentType: _type.c_int = None
    fChecked: _type.BOOL = None
    fDirty: _type.BOOL = None
    fNoScroll: _type.BOOL = None
    cpPos: COMPPOS = None
    wszFriendlyName: _type.WCHAR * _const.MAX_PATH = None
    wszSource: _type.WCHAR * _const.INTERNET_MAX_URL_LENGTH = None
    wszSubscribedURL: _type.WCHAR * _const.INTERNET_MAX_URL_LENGTH = None
    dwCurItemState: _type.DWORD = None
    csiOriginal: COMPSTATEINFO = None
    csiRestored: COMPSTATEINFO = None


@_struct
class DROPSTRUCT:
    hwndSource: _type.HWND = None
    hwndSink: _type.HWND = None
    wFmt: _type.DWORD = None
    dwData: _type.ULONG_PTR = None
    ptDrop: POINT = None
    dwControlData: _type.DWORD = None


@_struct
class DRAWTEXTPARAMS:
    cbSize: _type.UINT = _SIZE
    iTabLength: _type.c_int = None
    iLeftMargin: _type.c_int = None
    iRightMargin: _type.c_int = None
    uiLengthDrawn: _type.UINT = None


@_struct
class COMPONENTSOPT:
    dwSize: _type.DWORD = _SIZE
    fEnableComponents: _type.BOOL = None
    fActiveDesktop: _type.BOOL = None


@_struct
class TPMPARAMS:
    cbSize: _type.UINT = _SIZE
    rcExclude: RECT = None


@_struct
class MENUITEMTEMPLATEHEADER:
    versionNumber: _type.WORD = None
    offset: _type.WORD = None


@_struct
class MENUITEMTEMPLATE:
    mtOption: _type.WORD = None
    mtID: _type.WORD = None
    mtString: _type.WCHAR * 1 = None


@_struct
class STRING:
    Length: _type.USHORT = None
    MaximumLength: _type.USHORT = None
    Buffer: _type.PCHAR = None


# noinspection PyPep8Naming
@_struct
class UNICODE_STRING:
    Length: _type.USHORT = None
    MaximumLength: _type.USHORT = None
    Buffer: _type.PWSTR = None


@_struct
class ACCEL:
    # noinspection PyProtectedMember
    if not _const._MAC:
        fVirt: _type.BYTE = None
        key: _type.WORD = None
        cmd: _type.WORD = None
    else:
        fVirt: _type.WORD = None
        key: _type.WORD = None
        cmd: _type.DWORD = None


@_struct
class PAINTSTRUCT:
    hdc: _type.HDC = None
    fErase: _type.BOOL = None
    rcPaint: RECT = None
    fRestore: _type.BOOL = None
    fIncUpdate: _type.BOOL = None
    rgbReserved: _type.BYTE * 32 = None


@_struct
class CREATESTRUCTA:
    lpCreateParams: _type.LPVOID = None
    hInstance: _type.HINSTANCE = None
    hMenu: _type.HMENU = None
    hwndParent: _type.HWND = None
    cy: _type.c_int = None
    cx: _type.c_int = None
    y: _type.c_int = None
    x: _type.c_int = None
    style: _type.LONG = None
    lpszName: _type.LPCSTR = None
    lpszClass: _type.LPCSTR = None
    dwExStyle: _type.DWORD = None


@_struct
class CREATESTRUCTW:
    lpCreateParams: _type.LPVOID = None
    hInstance: _type.HINSTANCE = None
    hMenu: _type.HMENU = None
    hwndParent: _type.HWND = None
    cy: _type.c_int = None
    cx: _type.c_int = None
    y: _type.c_int = None
    x: _type.c_int = None
    style: _type.LONG = None
    lpszName: _type.LPCWSTR = None
    lpszClass: _type.LPCWSTR = None
    dwExStyle: _type.DWORD = None


@_struct
class WINDOWPLACEMENT:
    length: _type.UINT = _SIZE
    flags: _type.UINT = None
    showCmd: _type.UINT = None
    ptMinPosition: POINT = None
    ptMaxPosition: POINT = None
    rcNormalPosition: RECT = None
    # noinspection PyProtectedMember
    if _const._MAC:
        rcDevice: RECT = None


@_struct
class NMHDR:
    hwndFrom: _type.HWND = None
    idFrom: _type.UINT_PTR = None
    code: _type.UINT = None


@_struct
class STYLESTRUCT:
    styleOld: _type.DWORD = None
    styleNew: _type.DWORD = None


@_struct
class MEASUREITEMSTRUCT:
    CtlType: _type.UINT = None
    CtlID: _type.UINT = None
    itemID: _type.UINT = None
    itemWidth: _type.UINT = None
    itemHeight: _type.UINT = None
    itemData: _type.ULONG_PTR = None


@_struct
class DRAWITEMSTRUCT:
    CtlType: _type.UINT = None
    CtlID: _type.UINT = None
    itemID: _type.UINT = None
    itemAction: _type.UINT = None
    itemState: _type.UINT = None
    hwndItem: _type.HWND = None
    hDC: _type.HDC = None
    rcItem: RECT = None
    itemData: _type.ULONG_PTR = None


@_struct
class DELETEITEMSTRUCT:
    CtlType: _type.UINT = None
    CtlID: _type.UINT = None
    itemID: _type.UINT = None
    hwndItem: _type.HWND = None
    itemData: _type.ULONG_PTR = None


@_struct
class COMPAREITEMSTRUCT:
    CtlType: _type.UINT = None
    CtlID: _type.UINT = None
    hwndItem: _type.HWND = None
    itemID1: _type.UINT = None
    itemData1: _type.ULONG_PTR = None
    itemID2: _type.UINT = None
    itemData2: _type.ULONG_PTR = None
    dwLocaleId: _type.DWORD = None


@_struct
class INITCOMMONCONTROLSEX:
    dwSize: _type.DWORD = _SIZE
    dwICC: _type.DWORD = None


@_struct
class COLORSCHEME:
    dwSize: _type.DWORD = _SIZE
    clrBtnHighlight: _type.COLORREF = None
    clrBtnShadow: _type.COLORREF = None


@_struct
class DTBGOPTS:
    dwSize: _type.DWORD = _SIZE
    dwFlags: _type.DWORD = None
    rcClip: RECT = None


@_struct
class TEXTMETRICA:
    tmHeight: _type.LONG = None
    tmAscent: _type.LONG = None
    tmDescent: _type.LONG = None
    tmInternalLeading: _type.LONG = None
    tmExternalLeading: _type.LONG = None
    tmAveCharWidth: _type.LONG = None
    tmMaxCharWidth: _type.LONG = None
    tmWeight: _type.LONG = None
    tmOverhang: _type.LONG = None
    tmDigitizedAspectX: _type.LONG = None
    tmDigitizedAspectY: _type.LONG = None
    tmFirstChar: _type.BYTE = None
    tmLastChar: _type.BYTE = None
    tmDefaultChar: _type.BYTE = None
    tmBreakChar: _type.BYTE = None
    tmItalic: _type.BYTE = None
    tmUnderlined: _type.BYTE = None
    tmStruckOut: _type.BYTE = None
    tmPitchAndFamily: _type.BYTE = None
    tmCharSet: _type.BYTE = None


@_struct
class TEXTMETRICW:
    tmHeight: _type.LONG = None
    tmAscent: _type.LONG = None
    tmDescent: _type.LONG = None
    tmInternalLeading: _type.LONG = None
    tmExternalLeading: _type.LONG = None
    tmAveCharWidth: _type.LONG = None
    tmMaxCharWidth: _type.LONG = None
    tmWeight: _type.LONG = None
    tmOverhang: _type.LONG = None
    tmDigitizedAspectX: _type.LONG = None
    tmDigitizedAspectY: _type.LONG = None
    tmFirstChar: _type.WCHAR = None
    tmLastChar: _type.WCHAR = None
    tmDefaultChar: _type.WCHAR = None
    tmBreakChar: _type.WCHAR = None
    tmItalic: _type.BYTE = None
    tmUnderlined: _type.BYTE = None
    tmStruckOut: _type.BYTE = None
    tmPitchAndFamily: _type.BYTE = None
    tmCharSet: _type.BYTE = None


@_struct
class LOGFONTA:
    lfHeight: _type.LONG = None
    lfWidth: _type.LONG = None
    lfEscapement: _type.LONG = None
    lfOrientation: _type.LONG = None
    lfWeight: _type.LONG = None
    lfItalic: _type.BYTE = None
    lfUnderline: _type.BYTE = None
    lfStrikeOut: _type.BYTE = None
    lfCharSet: _type.BYTE = None
    lfOutPrecision: _type.BYTE = None
    lfClipPrecision: _type.BYTE = None
    lfQuality: _type.BYTE = None
    lfPitchAndFamily: _type.BYTE = None
    lfFaceName: _type.CHAR * _const.LF_FACESIZE = None


@_struct
class LOGFONTW:
    lfHeight: _type.LONG = None
    lfWidth: _type.LONG = None
    lfEscapement: _type.LONG = None
    lfOrientation: _type.LONG = None
    lfWeight: _type.LONG = None
    lfItalic: _type.BYTE = None
    lfUnderline: _type.BYTE = None
    lfStrikeOut: _type.BYTE = None
    lfCharSet: _type.BYTE = None
    lfOutPrecision: _type.BYTE = None
    lfClipPrecision: _type.BYTE = None
    lfQuality: _type.BYTE = None
    lfPitchAndFamily: _type.BYTE = None
    lfFaceName: _type.WCHAR * _const.LF_FACESIZE = None


@_struct
class MARGINS:
    cxLeftWidth: _type.c_int = None
    cxRightWidth: _type.c_int = None
    cyTopHeight: _type.c_int = None
    cyBottomHeight: _type.c_int = None


@_struct
class INTLIST:
    iValueCount: _type.c_int = None
    iValues: _type.c_int * _const.MAX_INTLIST_COUNT = None


# noinspection PyPep8Naming
@_struct
class WTA_OPTIONS:
    dwFlags: _type.DWORD = None
    dwMask: _type.DWORD = None


@_struct
class GUITHREADINFO:
    cbSize: _type.DWORD = _SIZE
    flags: _type.DWORD = None
    hwndActive: _type.HWND = None
    hwndFocus: _type.HWND = None
    hwndCapture: _type.HWND = None
    hwndMenuOwner: _type.HWND = None
    hwndMoveSize: _type.HWND = None
    hwndCaret: _type.HWND = None
    rcCaret: RECT = None


@_struct
class DLGTEMPLATE:
    style: _type.DWORD = None
    dwExtendedStyle: _type.DWORD = None
    cdit: _type.WORD = None
    x: _type.c_short = None
    y: _type.c_short = None
    cx: _type.c_short = None
    cy: _type.c_short = None


@_struct
class DLGITEMTEMPLATE:
    style: _type.DWORD = None
    dwExtendedStyle: _type.DWORD = None
    x: _type.c_short = None
    y: _type.c_short = None
    cx: _type.c_short = None
    id: _type.WORD = None


@_struct
class STATSTG:
    pwcsName: _type.LPOLESTR = None
    type: _type.DWORD = None
    cbSize: _union.ULARGE_INTEGER = None
    mtime: FILETIME = None
    ctime: FILETIME = None
    atime: FILETIME = None
    grfMode: _type.DWORD = None
    grfLocksSupported: _type.DWORD = None
    clsid: CLSID = None
    grfStateBits: _type.DWORD = None
    reserved: _type.DWORD = None


@_struct
class TTTOOLINFOA:
    cbSize: _type.UINT = _SIZE
    uFlags: _type.UINT = None
    hwnd: _type.HWND = None
    uId: _type.UINT_PTR = None
    rect: RECT = None
    hinst: _type.HINSTANCE = None
    lpszText: _type.LPSTR = None
    lParam: _type.LPARAM = None
    if _const.NTDDI_VERSION >= _const.NTDDI_WINXP:
        lpReserved: _type.c_void_p = None


@_struct
class TTTOOLINFOW:
    cbSize: _type.UINT = _SIZE
    uFlags: _type.UINT = None
    hwnd: _type.HWND = None
    uId: _type.UINT_PTR = None
    rect: RECT = None
    hinst: _type.HINSTANCE = None
    lpszText: _type.LPWSTR = None
    lParam: _type.LPARAM = None
    if _const.NTDDI_VERSION >= _const.NTDDI_WINXP:
        lpReserved: _type.c_void_p = None


@_struct
class TRACKMOUSEEVENT:
    cbSize: _type.DWORD = _SIZE
    dwFlags: _type.DWORD = None
    hwndTrack: _type.HWND = None
    dwHoverTime: _type.DWORD = None


@_struct
class RBHITTESTINFO:
    pt: POINT = None
    flags: _type.UINT = None
    iBand: _type.c_int = None


@_struct
class ACTCTXA:
    cbSize: _type.ULONG = _SIZE
    dwFlags: _type.DWORD = None
    lpSource: _type.LPCSTR = None
    wProcessorArchitecture: _type.USHORT = None
    wLangId: _type.LANGID = None
    lpAssemblyDirectory: _type.LPCSTR = None
    lpResourceName: _type.LPCSTR = None
    lpApplicationName: _type.LPCSTR = None
    hModule: _type.HMODULE = None


@_struct
class ACTCTXW:
    cbSize: _type.ULONG = _SIZE
    dwFlags: _type.DWORD = None
    lpSource: _type.LPCWSTR = None
    wProcessorArchitecture: _type.USHORT = None
    wLangId: _type.LANGID = None
    lpAssemblyDirectory: _type.LPCWSTR = None
    lpResourceName: _type.LPCWSTR = None
    lpApplicationName: _type.LPCWSTR = None
    hModule: _type.HMODULE = None


@_struct
class SYSTEMTIME:
    wYear: _type.WORD = None
    wMonth: _type.WORD = None
    wDayOfWeek: _type.WORD = None
    wDay: _type.WORD = None
    wHour: _type.WORD = None
    wMinute: _type.WORD = None
    wSecond: _type.WORD = None
    wMilliseconds: _type.WORD = None


@_struct
class OSVERSIONINFOA:
    dwOSVersionInfoSize: _type.DWORD = _SIZE
    dwMajorVersion: _type.DWORD = None
    dwMinorVersion: _type.DWORD = None
    dwBuildNumber: _type.DWORD = None
    dwPlatformId: _type.DWORD = None
    szCSDVersion: _type.CHAR * 128 = None


@_struct
class OSVERSIONINFOW:
    dwOSVersionInfoSize: _type.DWORD = _SIZE
    dwMajorVersion: _type.DWORD = None
    dwMinorVersion: _type.DWORD = None
    dwBuildNumber: _type.DWORD = None
    dwPlatformId: _type.DWORD = None
    szCSDVersion: _type.WCHAR * 128 = None


@_struct
class OSVERSIONINFOEXA:
    dwOSVersionInfoSize: _type.DWORD = _SIZE
    dwMajorVersion: _type.DWORD = None
    dwMinorVersion: _type.DWORD = None
    dwBuildNumber: _type.DWORD = None
    dwPlatformId: _type.DWORD = None
    szCSDVersion: _type.CHAR * 128 = None
    wServicePackMajor: _type.WORD = None
    wServicePackMinor: _type.WORD = None
    wSuiteMask: _type.WORD = None
    wProductType: _type.BYTE = None
    wReserved: _type.BYTE = None


@_struct
class OSVERSIONINFOEXW:
    dwOSVersionInfoSize: _type.DWORD = _SIZE
    dwMajorVersion: _type.DWORD = None
    dwMinorVersion: _type.DWORD = None
    dwBuildNumber: _type.DWORD = None
    dwPlatformId: _type.DWORD = None
    szCSDVersion: _type.WCHAR * 128 = None
    wServicePackMajor: _type.WORD = None
    wServicePackMinor: _type.WORD = None
    wSuiteMask: _type.WORD = None
    wProductType: _type.BYTE = None
    wReserved: _type.BYTE = None


@_struct
class DLLVERSIONINFO:
    cbSize: _type.DWORD = _SIZE
    dwMajorVersion: _type.DWORD = None
    dwMinorVersion: _type.DWORD = None
    dwBuildNumber: _type.DWORD = None
    dwPlatformID: _type.DWORD = None


@_struct
class DLLVERSIONINFO2:
    info1: DLLVERSIONINFO = None
    dwFlags: _type.DWORD = None
    ullVersion: _type.ULONGLONG = None


# noinspection PyPep8Naming
@_struct
class SYSTEM_POWER_STATUS:
    ACLineStatus: _type.BYTE = None
    BatteryFlag: _type.BYTE = None
    BatteryLifePercent: _type.BYTE = None
    Reserved1: _type.BYTE = None
    BatteryLifeTime: _type.DWORD = None
    BatteryFullLifeTime: _type.DWORD = None


@_struct
class SHSTOCKICONINFO:
    cbSize: _type.DWORD = _SIZE
    hIcon: _type.HICON = None
    iSysIconIndex: _type.c_int = None
    iIcon: _type.c_int = None
    szPath: _type.WCHAR * _const.MAX_PATH = None


# noinspection PyPep8Naming
@_struct
class LARGE_INTEGER_S:
    LowPart: _type.DWORD = None
    HighPart: _type.LONG = None


# noinspection PyPep8Naming
@_struct
class ULARGE_INTEGER_S:
    LowPart: _type.DWORD = None
    HighPart: _type.DWORD = None


# noinspection PyPep8Naming
@_struct
class DISK_SPACE_INFORMATION:
    ActualTotalAllocationUnits: _type.ULONGLONG = None
    ActualAvailableAllocationUnits: _type.ULONGLONG = None
    ActualPoolUnavailableAllocationUnits: _type.ULONGLONG = None
    CallerTotalAllocationUnits: _type.ULONGLONG = None
    CallerAvailableAllocationUnits: _type.ULONGLONG = None
    CallerPoolUnavailableAllocationUnits: _type.ULONGLONG = None
    UsedAllocationUnits: _type.ULONGLONG = None
    TotalReservedAllocationUnits: _type.ULONGLONG = None
    VolumeStorageReserveAllocationUnits: _type.ULONGLONG = None
    AvailableCommittedAllocationUnits: _type.ULONGLONG = None
    PoolAvailableAllocationUnits: _type.ULONGLONG = None
    SectorsPerAllocationUnit: _type.DWORD = None
    BytesPerSector: _type.DWORD = None


@_struct
class SHQUERYRBINFO:
    cbSize: _type.DWORD = _SIZE
    # noinspection PyProtectedMember
    if not _const._MAC or _const._MAC_INT_64:
        i64Size: _type.c_int64 = None
        i64NumItems: _type.c_int64 = None
    else:
        i64Size: _type.DWORDLONG = None
        i64NumItems: _type.DWORDLONG = None


# noinspection PyPep8Naming
@_struct
class SECURITY_ATTRIBUTES:
    nLength: _type.DWORD = _SIZE
    lpSecurityDescriptor: _type.LPVOID = None
    bInheritHandle: _type.BOOL = None


@_struct
class LUID:
    LowPart: _type.DWORD = None
    HighPart: _type.LONG = None


@_struct
class BSMINFO:
    cbSize: _type.DWORD = _SIZE
    hDesk: _type.HDESK = None
    hwnd: _type.HWND = None
    luid: LUID = None


# noinspection PyPep8Naming
@_struct
class INPUT_MESSAGE_SOURCE:
    deviceType: _enum.INPUT_MESSAGE_DEVICE_TYPE = None
    originId: _enum.INPUT_MESSAGE_ORIGIN_ID = None


# noinspection PyPep8Naming
@_struct
class SECURITY_ATTRIBUTES:
    nLength: _type.DWORD = _SIZE
    lpSecurityDescriptor: _type.LPVOID = None
    bInheritHandle: _type.BOOL = None


@_struct
class EMR:
    iType: _type.DWORD = None
    nSize: _type.DWORD = None


@_struct
class LOGPEN:
    lopnStyle: _type.UINT = None
    lopnWidth: POINT = None
    lopnColor: _type.COLORREF = None


@_struct
class EXTLOGPEN:
    elpPenStyle: _type.DWORD = None
    elpWidth: _type.DWORD = None
    elpBrushStyle: _type.UINT = None
    elpColor: _type.COLORREF = None
    elpHatch: _type.ULONG_PTR = None
    elpNumEntries: _type.DWORD = None
    elpStyleEntry: _type.DWORD * 1 = None


@_struct
class LOGBRUSH:
    lbStyle: _type.UINT = None
    lbColor: _type.COLORREF = None
    lbHatch: _type.ULONG_PTR = None


@_struct
class LOGBRUSH32:
    lbStyle: _type.UINT = None
    lbColor: _type.COLORREF = None
    lbHatch: _type.ULONG = None


# noinspection PyPep8Naming
@_struct
class COMPATIBILITY_CONTEXT_ELEMENT:
    Id: GUID = None
    Type: _enum.ACTCTX_COMPATIBILITY_ELEMENT_TYPE = None
    MaxVersionTested: _type.ULONGLONG = None


# noinspection PyPep8Naming
@_struct
class ACTIVATION_CONTEXT_COMPATIBILITY_INFORMATION:
    ElementCount: _type.DWORD = None
    # noinspection PyTypeChecker
    Elements: COMPATIBILITY_CONTEXT_ELEMENT * 0 = None


# noinspection PyPep8Naming
@_struct
class SUPPORTED_OS_INFO:
    MajorVersion: _type.WORD = None
    MinorVersion: _type.WORD = None


# noinspection PyPep8Naming
@_struct
class MAXVERSIONTESTED_INFO:
    MaxVersionTested: _type.ULONGLONG = None


# noinspection PyPep8Naming
@_struct
class ACTIVATION_CONTEXT_DETAILED_INFORMATION:
    dwFlags: _type.DWORD = None
    ulFormatVersion: _type.DWORD = None
    ulAssemblyCount: _type.DWORD = None
    ulRootManifestPathType: _type.DWORD = None
    ulRootManifestPathChars: _type.DWORD = None
    ulRootConfigurationPathType: _type.DWORD = None
    ulRootConfigurationPathChars: _type.DWORD = None
    ulAppDirPathType: _type.DWORD = None
    ulAppDirPathChars: _type.DWORD = None
    lpRootManifestPath: _type.PCWSTR = None
    lpRootConfigurationPath: _type.PCWSTR = None
    lpAppDirPath: _type.PCWSTR = None


# noinspection PyPep8Naming
@_struct
class HARDWARE_COUNTER_DATA:
    Type: _enum.HARDWARE_COUNTER_TYPE = None
    Reserved: _type.DWORD = None
    Value: _type.DWORD64 = None


# noinspection PyPep8Naming
@_struct
class PERFORMANCE_DATA:
    Size: _type.WORD = _SIZE
    Version: _type.BYTE = None
    HwCountersCount: _type.BYTE = None
    ContextSwitchCount: _type.DWORD = None
    WaitReasonBitMap: _type.DWORD64 = None
    CycleTime: _type.DWORD64 = None
    RetryCount: _type.DWORD = None
    Reserved: _type.DWORD = None
    # noinspection PyUnresolvedReferences
    HardwareCounters: HARDWARE_COUNTER_DATA * _const.MAX_HW_COUNTERS = None


# noinspection PyPep8Naming
@_struct
class ACTIVATION_CONTEXT_ASSEMBLY_DETAILED_INFORMATION:
    ulFlags: _type.DWORD = None
    ulEncodedAssemblyIdentityLength: _type.DWORD = None
    ulManifestPathType: _type.DWORD = None
    ulManifestPathLength: _type.DWORD = None
    liManifestLastWriteTime: _union.LARGE_INTEGER = None
    ulPolicyPathType: _type.DWORD = None
    ulPolicyPathLength: _type.DWORD = None
    liPolicyLastWriteTime: _union.LARGE_INTEGER = None
    ulMetadataSatelliteRosterIndex: _type.DWORD = None
    ulManifestVersionMajor: _type.DWORD = None
    ulManifestVersionMinor: _type.DWORD = None
    ulPolicyVersionMajor: _type.DWORD = None
    ulPolicyVersionMinor: _type.DWORD = None
    ulAssemblyDirectoryNameLength: _type.DWORD = None
    lpAssemblyEncodedAssemblyIdentity: _type.PCWSTR = None
    lpAssemblyManifestPath: _type.PCWSTR = None
    lpAssemblyPolicyPath: _type.PCWSTR = None
    lpAssemblyDirectoryName: _type.PCWSTR = None


# noinspection PyPep8Naming
@_struct
class ACTIVATION_CONTEXT_RUN_LEVEL_INFORMATION:
    ulFlags: _type.DWORD = None
    RunLevel: _enum.ACTCTX_REQUESTED_RUN_LEVEL = None
    UiAccess: _type.DWORD = None


# noinspection PyPep8Naming
@_struct
class ASSEMBLY_FILE_DETAILED_INFORMATION:
    ulFlags: _type.DWORD = None
    ulFilenameLength: _type.DWORD = None
    ulPathLength: _type.DWORD = None
    lpFileName: _type.PCWSTR = None
    lpFilePath: _type.PCWSTR = None


# noinspection PyPep8Naming
@_struct
class HEAP_SUMMARY:
    cb: _type.DWORD = _SIZE
    cbAllocated: _type.SIZE_T = None
    cbCommitted: _type.SIZE_T = None
    cbReserved: _type.SIZE_T = None
    cbMaxReserve: _type.SIZE_T = None


# noinspection PyPep8Naming
@_struct
class PROCESS_HEAP_ENTRY_U_S:
    hMem: _type.HANDLE = None
    dwReserved: _type.DWORD * 3 = None


# noinspection PyPep8Naming
@_struct
class PROCESS_HEAP_ENTRY_U_S2:
    dwCommittedSize: _type.DWORD = None
    dwUnCommittedSize: _type.DWORD = None
    lpFirstBlock: _type.LPVOID = None
    lpLastBlock: _type.LPVOID = None


# noinspection PyPep8Naming
@_struct
class PROCESS_HEAP_ENTRY:
    lpData: _type.PVOID = None
    cbData: _type.DWORD = None
    cbOverhead: _type.BYTE = None
    iRegionIndex: _type.BYTE = None
    wFlags: _type.WORD = None
    U: _union.PROCESS_HEAP_ENTRY_U = None


# noinspection PyPep8Naming
@_struct
class IMAGE_SECTION_HEADER:
    Name: _type.BYTE * _const.IMAGE_SIZEOF_SHORT_NAME = None
    Misc: _union.IMAGE_SECTION_HEADER_U = None
    VirtualAddress: _type.DWORD = None
    SizeOfRawData: _type.DWORD = None
    PointerToRawData: _type.DWORD = None
    PointerToRelocations: _type.DWORD = None
    PointerToLinenumbers: _type.DWORD = None
    NumberOfRelocations: _type.WORD = None
    NumberOfLinenumbers: _type.WORD = None
    Characteristics: _type.DWORD = None


# noinspection PyPep8Naming
@_struct
class IMAGE_DOS_HEADER:
    e_magic: _type.WORD = None
    e_cblp: _type.WORD = None
    e_cp: _type.WORD = None
    e_crlc: _type.WORD = None
    e_cparhdr: _type.WORD = None
    e_minalloc: _type.WORD = None
    e_maxalloc: _type.WORD = None
    e_ss: _type.WORD = None
    e_sp: _type.WORD = None
    e_csum: _type.WORD = None
    e_ip: _type.WORD = None
    e_cs: _type.WORD = None
    e_lfarlc: _type.WORD = None
    e_ovno: _type.WORD = None
    e_res: _type.WORD * 4 = None
    e_oemid: _type.WORD = None
    e_oeminfo: _type.WORD = None
    e_res2: _type.WORD * 10 = None
    e_lfanew: _type.LONG = None


# noinspection PyPep8Naming
@_struct
class IMAGE_OS2_HEADER:
    ne_magic: _type.WORD = None
    ne_ver: _type.CHAR = None
    ne_rev: _type.CHAR = None
    ne_enttab: _type.WORD = None
    ne_cbenttab: _type.WORD = None
    ne_crc: _type.LONG = None
    ne_flags: _type.WORD = None
    ne_autodata: _type.WORD = None
    ne_heap: _type.WORD = None
    ne_stack: _type.WORD = None
    ne_csip: _type.LONG = None
    ne_sssp: _type.LONG = None
    ne_cseg: _type.WORD = None
    ne_cmod: _type.WORD = None
    ne_cbnrestab: _type.WORD = None
    ne_segtab: _type.WORD = None
    ne_rsrctab: _type.WORD = None
    ne_restab: _type.WORD = None
    ne_modtab: _type.WORD = None
    ne_imptab: _type.WORD = None
    ne_nrestab: _type.LONG = None
    ne_cmovent: _type.WORD = None
    ne_align: _type.WORD = None
    ne_cres: _type.WORD = None
    ne_exetyp: _type.BYTE = None
    ne_flagsothers: _type.BYTE = None
    ne_pretthunks: _type.WORD = None
    ne_psegrefbytes: _type.WORD = None
    ne_swaparea: _type.WORD = None
    ne_expver: _type.WORD = None


# noinspection PyPep8Naming
@_struct
class IMAGE_VXD_HEADER:
    e32_magic: _type.WORD = None
    e32_border: _type.BYTE = None
    e32_worder: _type.BYTE = None
    e32_level: _type.DWORD = None
    e32_cpu: _type.WORD = None
    e32_os: _type.WORD = None
    e32_ver: _type.DWORD = None
    e32_mflags: _type.DWORD = None
    e32_mpages: _type.DWORD = None
    e32_startobj: _type.DWORD = None
    e32_eip: _type.DWORD = None
    e32_stackobj: _type.DWORD = None
    e32_esp: _type.DWORD = None
    e32_pagesize: _type.DWORD = None
    e32_lastpagesize: _type.DWORD = None
    e32_fixupsize: _type.DWORD = None
    e32_fixupsum: _type.DWORD = None
    e32_ldrsize: _type.DWORD = None
    e32_ldrsum: _type.DWORD = None
    e32_objtab: _type.DWORD = None
    e32_objcnt: _type.DWORD = None
    e32_objmap: _type.DWORD = None
    e32_itermap: _type.DWORD = None
    e32_rsrctab: _type.DWORD = None
    e32_rsrccnt: _type.DWORD = None
    e32_restab: _type.DWORD = None
    e32_enttab: _type.DWORD = None
    e32_dirtab: _type.DWORD = None
    e32_dircnt: _type.DWORD = None
    e32_fpagetab: _type.DWORD = None
    e32_frectab: _type.DWORD = None
    e32_impmod: _type.DWORD = None
    e32_impmodcnt: _type.DWORD = None
    e32_impproc: _type.DWORD = None
    e32_pagesum: _type.DWORD = None
    e32_datapage: _type.DWORD = None
    e32_preload: _type.DWORD = None
    e32_nrestab: _type.DWORD = None
    e32_cbnrestab: _type.DWORD = None
    e32_nressum: _type.DWORD = None
    e32_autodata: _type.DWORD = None
    e32_debuginfo: _type.DWORD = None
    e32_debuglen: _type.DWORD = None
    e32_instpreload: _type.DWORD = None
    e32_instdemand: _type.DWORD = None
    e32_heapsize: _type.DWORD = None
    e32_res3: _type.BYTE * 12 = None
    e32_winresoff: _type.DWORD = None
    e32_winreslen: _type.DWORD = None
    e32_devid: _type.WORD = None
    e32_ddkver: _type.WORD = None


# noinspection PyPep8Naming
@_struct
class IMAGE_FILE_HEADER:
    Machine: _type.WORD = None
    NumberOfSections: _type.WORD = None
    TimeDateStamp: _type.DWORD = None
    PointerToSymbolTable: _type.DWORD = None
    NumberOfSymbols: _type.DWORD = None
    SizeOfOptionalHeader: _type.WORD = None
    Characteristics: _type.WORD = None


# noinspection PyPep8Naming
@_struct
class IMAGE_DATA_DIRECTORY:
    VirtualAddress: _type.DWORD = None
    Size: _type.DWORD = None


# noinspection PyPep8Naming
@_struct
class IMAGE_OPTIONAL_HEADER32:
    Magic: _type.WORD = None
    MajorLinkerVersion: _type.BYTE = None
    MinorLinkerVersion: _type.BYTE = None
    SizeOfCode: _type.DWORD = None
    SizeOfInitializedData: _type.DWORD = None
    SizeOfUninitializedData: _type.DWORD = None
    AddressOfEntryPoint: _type.DWORD = None
    BaseOfCode: _type.DWORD = None
    BaseOfData: _type.DWORD = None
    ImageBase: _type.DWORD = None
    SectionAlignment: _type.DWORD = None
    FileAlignment: _type.DWORD = None
    MajorOperatingSystemVersion: _type.WORD = None
    MinorOperatingSystemVersion: _type.WORD = None
    MajorImageVersion: _type.WORD = None
    MinorImageVersion: _type.WORD = None
    MajorSubsystemVersion: _type.WORD = None
    MinorSubsystemVersion: _type.WORD = None
    Win32VersionValue: _type.DWORD = None
    SizeOfImage: _type.DWORD = None
    SizeOfHeaders: _type.DWORD = None
    CheckSum: _type.DWORD = None
    Subsystem: _type.WORD = None
    DllCharacteristics: _type.WORD = None
    SizeOfStackReserve: _type.DWORD = None
    SizeOfStackCommit: _type.DWORD = None
    SizeOfHeapReserve: _type.DWORD = None
    SizeOfHeapCommit: _type.DWORD = None
    LoaderFlags: _type.DWORD = None
    NumberOfRvaAndSizes: _type.DWORD = None
    # noinspection PyUnresolvedReferences
    DataDirectory: IMAGE_DATA_DIRECTORY * _const.IMAGE_NUMBEROF_DIRECTORY_ENTRIES = None


# noinspection PyPep8Naming
@_struct
class IMAGE_OPTIONAL_HEADER64:
    Magic: _type.WORD = None
    MajorLinkerVersion: _type.BYTE = None
    MinorLinkerVersion: _type.BYTE = None
    SizeOfCode: _type.DWORD = None
    SizeOfInitializedData: _type.DWORD = None
    SizeOfUninitializedData: _type.DWORD = None
    AddressOfEntryPoint: _type.DWORD = None
    BaseOfCode: _type.DWORD = None
    ImageBase: _type.ULONGLONG = None
    SectionAlignment: _type.DWORD = None
    FileAlignment: _type.DWORD = None
    MajorOperatingSystemVersion: _type.WORD = None
    MinorOperatingSystemVersion: _type.WORD = None
    MajorImageVersion: _type.WORD = None
    MinorImageVersion: _type.WORD = None
    MajorSubsystemVersion: _type.WORD = None
    MinorSubsystemVersion: _type.WORD = None
    Win32VersionValue: _type.DWORD = None
    SizeOfImage: _type.DWORD = None
    SizeOfHeaders: _type.DWORD = None
    CheckSum: _type.DWORD = None
    Subsystem: _type.WORD = None
    DllCharacteristics: _type.WORD = None
    SizeOfStackReserve: _type.ULONGLONG = None
    SizeOfStackCommit: _type.ULONGLONG = None
    SizeOfHeapReserve: _type.ULONGLONG = None
    SizeOfHeapCommit: _type.ULONGLONG = None
    LoaderFlags: _type.DWORD = None
    NumberOfRvaAndSizes: _type.DWORD = None
    # noinspection PyUnresolvedReferences
    DataDirectory: IMAGE_DATA_DIRECTORY * _const.IMAGE_NUMBEROF_DIRECTORY_ENTRIES = None


# noinspection PyPep8Naming
@_struct
class IMAGE_ROM_OPTIONAL_HEADER:
    Magic: _type.WORD = None
    MajorLinkerVersion: _type.BYTE = None
    MinorLinkerVersion: _type.BYTE = None
    SizeOfCode: _type.DWORD = None
    SizeOfInitializedData: _type.DWORD = None
    SizeOfUninitializedData: _type.DWORD = None
    AddressOfEntryPoint: _type.DWORD = None
    BaseOfCode: _type.DWORD = None
    BaseOfData: _type.DWORD = None
    BaseOfBss: _type.DWORD = None
    GprMask: _type.DWORD = None
    CprMask: _type.DWORD * 4 = None
    GpValue: _type.DWORD = None


# noinspection PyPep8Naming
@_struct
class IMAGE_NT_HEADERS32:
    Signature: _type.DWORD = None
    FileHeader: IMAGE_FILE_HEADER = None
    OptionalHeader: IMAGE_OPTIONAL_HEADER32 = None


# noinspection PyPep8Naming
@_struct
class IMAGE_NT_HEADERS64:
    Signature: _type.DWORD = None
    FileHeader: IMAGE_FILE_HEADER = None
    OptionalHeader: IMAGE_OPTIONAL_HEADER64 = None


# noinspection PyPep8Naming
@_struct
class IMAGE_ROM_HEADERS:
    FileHeader: IMAGE_FILE_HEADER = None
    OptionalHeader: IMAGE_ROM_OPTIONAL_HEADER = None


# noinspection PyPep8Naming
@_struct
class SECURITY_ATTRIBUTES:
    nLength: _type.DWORD = None
    lpSecurityDescriptor: _type.LPVOID = None
    bInheritHandle: _type.BOOL = None


# noinspection PyPep8Naming
@_struct
class OVERLAPPED_U_S:
    Offset: _type.DWORD = None
    OffsetHigh: _type.DWORD = None


@_struct
class OVERLAPPED:
    Internal: _type.ULONG_PTR = None
    InternalHigh: _type.ULONG_PTR = None
    U: _union.OVERLAPPED_U = None
    hEvent: _type.HANDLE = None


# noinspection PyPep8Naming
@_struct
class OVERLAPPED_ENTRY:
    lpCompletionKey: _type.ULONG_PTR = None
    lpOverlapped: _Pointer[OVERLAPPED] = None
    Internal: _type.ULONG_PTR = None
    dwNumberOfBytesTransferred: _type.DWORD = None


@_struct
class COLORADJUSTMENT:
    caSize: _type.WORD = _SIZE
    caFlags: _type.WORD = None
    caIlluminantIndex: _type.WORD = None
    caRedGamma: _type.WORD = None
    caGreenGamma: _type.WORD = None
    caBlueGamma: _type.WORD = None
    caReferenceBlack: _type.WORD = None
    caReferenceWhite: _type.WORD = None
    caContrast: _type.SHORT = None
    caBrightness: _type.SHORT = None
    caColorfulness: _type.SHORT = None
    caRedGreenTint: _type.SHORT = None


# noinspection PyPep8Naming
@_struct
class DWM_BLURBEHIND:
    dwFlags: _type.DWORD = None
    fEnable: _type.BOOL = None
    hRgnBlur: _type.HRGN = None
    fTransitionOnMaximized: _type.BOOL = None


# noinspection PyPep8Naming
@_struct
class PACKAGE_VERSION_U_S:
    Revision: _type.USHORT = None
    Build: _type.USHORT = None
    Minor: _type.USHORT = None
    Major: _type.USHORT = None


# noinspection PyPep8Naming
@_struct
class PACKAGE_VERSION:
    U: _union.PACKAGE_VERSION_U = None


# noinspection PyPep8Naming
@_struct
class PACKAGE_ID:
    reserved: _type.UINT32 = None
    processorArchitecture: _type.UINT32 = None
    version: PACKAGE_VERSION = None
    name: _type.PWSTR = None
    publisher: _type.PWSTR = None
    resourceId: _type.PWSTR = None
    publisherId: _type.PWSTR = None


@_struct
class MARGINS:
    cxLeftWidth: _type.c_int = None
    cxRightWidth: _type.c_int = None
    cyTopHeight: _type.c_int = None
    cyBottomHeight: _type.c_int = None


@_struct
class TrackerHandle:
    unused: _type.c_int = None


@_struct
class LUID:
    LowPart: _type.DWORD = None
    HighPart: _type.LONG = None


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_RATIONAL:
    Numerator: _type.DWORD = None
    Denominator: _type.DWORD = None


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_2DREGION:
    cx: _type.DWORD = None
    cy: _type.DWORD = None


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_PATH_SOURCE_INFO_U_S:
    cloneGroupId: _bitfield(_type.UINT32, 16) = None
    sourceModeInfoIdx: _bitfield(_type.UINT32, 16) = None


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_PATH_SOURCE_INFO:
    adapterId: LUID = None
    id: _type.UINT32 = None
    U: _union.DISPLAYCONFIG_PATH_SOURCE_INFO_U = None
    statusFlags: _type.UINT32 = None


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_PATH_TARGET_INFO_U_S:
    desktopModeInfoIdx: _bitfield(_type.UINT32, 16) = None
    targetModeInfoIdx: _bitfield(_type.UINT32, 16) = None


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_PATH_TARGET_INFO:
    adapterId: LUID = None
    id: _type.UINT32 = None
    U: _union.DISPLAYCONFIG_PATH_TARGET_INFO_U = None
    outputTechnology: _enum.DISPLAYCONFIG_VIDEO_OUTPUT_TECHNOLOGY = None
    rotation: _enum.DISPLAYCONFIG_ROTATION = None
    scaling: _enum.DISPLAYCONFIG_SCALING = None
    refreshRate: DISPLAYCONFIG_RATIONAL = None
    scanLineOrdering: _enum.DISPLAYCONFIG_SCANLINE_ORDERING = None
    targetAvailable: _type.BOOL = None
    statusFlags: _type.UINT32 = None


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_PATH_INFO:
    sourceInfo: DISPLAYCONFIG_PATH_SOURCE_INFO = None
    targetInfo: DISPLAYCONFIG_PATH_TARGET_INFO = None
    flags: _type.UINT32 = None


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_SOURCE_MODE:
    width: _type.UINT32 = None
    height: _type.UINT32 = None
    pixelFormat: _enum.DISPLAYCONFIG_PIXELFORMAT = None
    position: POINTL = None


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_VIDEO_SIGNAL_INFO_U_S:
    videoStandard: _bitfield(_type.UINT32, 16) = None
    vSyncFreqDivider: _bitfield(_type.UINT32, 6) = None
    reserved: _bitfield(_type.UINT32, 10) = None


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_VIDEO_SIGNAL_INFO:
    pixelRate: _type.UINT64 = None
    hSyncFreq: DISPLAYCONFIG_RATIONAL = None
    vSyncFreq: DISPLAYCONFIG_RATIONAL = None
    activeSize: DISPLAYCONFIG_2DREGION = None
    totalSize: DISPLAYCONFIG_2DREGION = None
    U: _union.DISPLAYCONFIG_VIDEO_SIGNAL_INFO_U = None
    scanLineOrdering: _enum.DISPLAYCONFIG_SCANLINE_ORDERING = None


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_TARGET_MODE:
    targetVideoSignalInfo: DISPLAYCONFIG_VIDEO_SIGNAL_INFO = None


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_DESKTOP_IMAGE_INFO:
    PathSourceSize: POINTL = None
    DesktopImageRegion: RECTL = None
    DesktopImageClip: RECTL = None


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_MODE_INFO:
    infoType: _enum.DISPLAYCONFIG_MODE_INFO_TYPE = None
    id: _type.UINT32 = None
    adapterId: LUID = None
    U: _union.DISPLAYCONFIG_MODE_INFO_U = None


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_DEVICE_INFO_HEADER:
    type: _enum.DISPLAYCONFIG_DEVICE_INFO_TYPE = None
    size: _type.UINT32 = None
    adapterId: LUID = None
    id: _type.UINT32 = None


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_SOURCE_DEVICE_NAME:
    header: DISPLAYCONFIG_DEVICE_INFO_HEADER = None
    viewGdiDeviceName: _type.WCHAR * _const.CCHDEVICENAME = None


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_TARGET_DEVICE_NAME_FLAGS_U_S:
    friendlyNameFromEdid: _bitfield(_type.UINT32, 1) = None
    friendlyNameForced: _bitfield(_type.UINT32, 1) = None
    edidIdsValid: _bitfield(_type.UINT32, 1) = None
    reserved: _bitfield(_type.UINT32, 29) = None


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_TARGET_DEVICE_NAME_FLAGS:
    U: _union.DISPLAYCONFIG_TARGET_DEVICE_NAME_FLAGS_U = None


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_TARGET_DEVICE_NAME:
    header: DISPLAYCONFIG_DEVICE_INFO_HEADER = None
    flags: DISPLAYCONFIG_TARGET_DEVICE_NAME_FLAGS = None
    outputTechnology: _enum.DISPLAYCONFIG_VIDEO_OUTPUT_TECHNOLOGY = None
    edidManufactureId: _type.UINT16 = None
    edidProductCodeId: _type.UINT16 = None
    connectorInstance: _type.UINT32 = None
    monitorFriendlyDeviceName: _type.WCHAR * 64 = None
    monitorDevicePath: _type.WCHAR * 128 = None


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_TARGET_PREFERRED_MODE:
    header: DISPLAYCONFIG_DEVICE_INFO_HEADER = None
    width: _type.UINT32 = None
    height: _type.UINT32 = None
    targetMode: DISPLAYCONFIG_TARGET_MODE = None


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_ADAPTER_NAME:
    header: DISPLAYCONFIG_DEVICE_INFO_HEADER = None
    adapterDevicePath: _type.WCHAR * 128 = None


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_TARGET_BASE_TYPE:
    header: DISPLAYCONFIG_DEVICE_INFO_HEADER = None
    baseOutputTechnology: _enum.DISPLAYCONFIG_VIDEO_OUTPUT_TECHNOLOGY = None


# noinspection PyPep8Naming
@_struct
class D2D1_PIXEL_FORMAT:
    format: _enum.DXGI_FORMAT = None
    alphaMode: _enum.D2D1_ALPHA_MODE = None


# noinspection PyPep8Naming
@_struct
class D2D_POINT_2U:
    x: _type.UINT32 = None
    y: _type.UINT32 = None


# noinspection PyPep8Naming
@_struct
class D2D_POINT_2F:
    x: _type.FLOAT = None
    y: _type.FLOAT = None


# noinspection PyPep8Naming
@_struct
class D2D_VECTOR_2F:
    x: _type.FLOAT = None
    y: _type.FLOAT = None


# noinspection PyPep8Naming
@_struct
class D2D_VECTOR_3F:
    x: _type.FLOAT = None
    y: _type.FLOAT = None
    z: _type.FLOAT = None


# noinspection PyPep8Naming
@_struct
class D2D_VECTOR_4F:
    x: _type.FLOAT = None
    y: _type.FLOAT = None
    z: _type.FLOAT = None
    w: _type.FLOAT = None


# noinspection PyPep8Naming
@_struct
class D2D_RECT_F:
    left: _type.FLOAT = None
    top: _type.FLOAT = None
    right: _type.FLOAT = None
    bottom: _type.FLOAT = None


# noinspection PyPep8Naming
@_struct
class D2D_RECT_U:
    left: _type.UINT32 = None
    top: _type.UINT32 = None
    right: _type.UINT32 = None
    bottom: _type.UINT32 = None


# noinspection PyPep8Naming
@_struct
class D2D_SIZE_F:
    width: _type.FLOAT = None
    height: _type.FLOAT = None


# noinspection PyPep8Naming
@_struct
class D2D_SIZE_U:
    width: _type.UINT32 = None
    height: _type.UINT32 = None


# noinspection PyPep8Naming
@_struct
class D2D_MATRIX_3X2_F_U_S:
    m11: _type.FLOAT = None
    m12: _type.FLOAT = None
    m21: _type.FLOAT = None
    m22: _type.FLOAT = None
    dx: _type.FLOAT = None
    dy: _type.FLOAT = None


# noinspection PyPep8Naming
@_struct
class D2D_MATRIX_3X2_F_U_S2:
    _11: _type.FLOAT = None
    _12: _type.FLOAT = None
    _21: _type.FLOAT = None
    _22: _type.FLOAT = None
    _31: _type.FLOAT = None
    _32: _type.FLOAT = None


# noinspection PyPep8Naming
@_struct
class D2D_MATRIX_3X2_F:
    U: _union.D2D_MATRIX_3X2_F_U = None


# noinspection PyPep8Naming
@_struct
class D2D_MATRIX_4X3_F_U_S:
    _11: _type.FLOAT = None
    _12: _type.FLOAT = None
    _13: _type.FLOAT = None
    _21: _type.FLOAT = None
    _22: _type.FLOAT = None
    _23: _type.FLOAT = None
    _31: _type.FLOAT = None
    _32: _type.FLOAT = None
    _33: _type.FLOAT = None
    _41: _type.FLOAT = None
    _42: _type.FLOAT = None
    _43: _type.FLOAT = None


# noinspection PyPep8Naming
@_struct
class D2D_MATRIX_4X3_F:
    U: _union.D2D_MATRIX_4X3_F_U = None


# noinspection PyPep8Naming
@_struct
class D2D_MATRIX_4X4_F_U_S:
    _11: _type.FLOAT = None
    _12: _type.FLOAT = None
    _13: _type.FLOAT = None
    _14: _type.FLOAT = None
    _21: _type.FLOAT = None
    _22: _type.FLOAT = None
    _23: _type.FLOAT = None
    _24: _type.FLOAT = None
    _31: _type.FLOAT = None
    _32: _type.FLOAT = None
    _33: _type.FLOAT = None
    _34: _type.FLOAT = None
    _41: _type.FLOAT = None
    _42: _type.FLOAT = None
    _43: _type.FLOAT = None
    _44: _type.FLOAT = None


# noinspection PyPep8Naming
@_struct
class D2D_MATRIX_4X4_F:
    U: _union.D2D_MATRIX_4X4_F_U = None


# noinspection PyPep8Naming
@_struct
class D2D_MATRIX_5X4_F_U_S:
    _11: _type.FLOAT = None
    _12: _type.FLOAT = None
    _13: _type.FLOAT = None
    _14: _type.FLOAT = None
    _21: _type.FLOAT = None
    _22: _type.FLOAT = None
    _23: _type.FLOAT = None
    _24: _type.FLOAT = None
    _31: _type.FLOAT = None
    _32: _type.FLOAT = None
    _33: _type.FLOAT = None
    _34: _type.FLOAT = None
    _41: _type.FLOAT = None
    _42: _type.FLOAT = None
    _43: _type.FLOAT = None
    _44: _type.FLOAT = None
    _51: _type.FLOAT = None
    _52: _type.FLOAT = None
    _53: _type.FLOAT = None
    _54: _type.FLOAT = None


# noinspection PyPep8Naming
@_struct
class DXGI_RATIONAL:
    Numerator: _type.UINT = None
    Denominator: _type.UINT = None


# noinspection PyPep8Naming
@_struct
class DXGI_SAMPLE_DESC:
    Count: _type.UINT = None
    Quality: _type.UINT = None


# noinspection PyPep8Naming
@_struct
class D2D_MATRIX_5X4_F:
    U: _union.D2D_MATRIX_5X4_F_U = None


# noinspection PyPep8Naming
@_struct
class DXGI_RGB:
    Red: _type.c_float = None
    Green: _type.c_float = None
    Blue: _type.c_float = None


@_struct
class D3DCOLORVALUE:
    r: _type.c_float = None
    g: _type.c_float = None
    b: _type.c_float = None
    a: _type.c_float = None


# noinspection PyPep8Naming
@_struct
class DXGI_GAMMA_CONTROL:
    Scale: DXGI_RGB = None
    Offset: DXGI_RGB = None
    # noinspection PyTypeChecker
    GammaCurve: DXGI_RGB * 1025 = None


# noinspection PyPep8Naming
@_struct
class DXGI_MODE_DESC:
    Width: _type.UINT = None
    Height: _type.UINT = None
    RefreshRate: DXGI_RATIONAL = None
    Format: _enum.DXGI_FORMAT = None
    ScanlineOrdering: _enum.DXGI_MODE_SCANLINE_ORDER = None
    Scaling: _enum.DXGI_MODE_SCALING = None


# noinspection PyPep8Naming
@_struct
class DXGI_JPEG_DC_HUFFMAN_TABLE:
    CodeCounts: _type.BYTE * 12 = None
    CodeValues: _type.BYTE * 12 = None


# noinspection PyPep8Naming
@_struct
class DXGI_JPEG_AC_HUFFMAN_TABLE:
    CodeCounts: _type.BYTE * 16 = None
    CodeValues: _type.BYTE * 162 = None


# noinspection PyPep8Naming
@_struct
class DXGI_JPEG_QUANTIZATION_TABLE:
    Elements: _type.BYTE * 64 = None


# noinspection PyPep8Naming
@_struct
class DXGI_GAMMA_CONTROL_CAPABILITIES:
    ScaleAndOffsetSupported: _type.BOOL = None
    MaxConvertedValue: _type.c_float = None
    MinConvertedValue: _type.c_float = None
    NumGammaControlPoints: _type.UINT = None
    ControlPointPositions: _type.c_float * 1025 = None


# noinspection PyPep8Naming
@_struct
class D2D1_BITMAP_PROPERTIES:
    pixelFormat: D2D1_PIXEL_FORMAT = None
    dpiX: _type.FLOAT = None
    dpiY: _type.FLOAT = None


# noinspection PyPep8Naming
@_struct
class D2D1_GRADIENT_STOP:
    position: _type.FLOAT = None
    color: D2D1_COLOR_F = None


# noinspection PyPep8Naming
@_struct
class D2D1_BRUSH_PROPERTIES:
    opacity: _type.FLOAT = None
    transform: D2D1_MATRIX_3X2_F = None


# noinspection PyPep8Naming
@_struct
class D2D1_BITMAP_BRUSH_PROPERTIES:
    extendModeX: _enum.D2D1_EXTEND_MODE = None
    extendModeY: _enum.D2D1_EXTEND_MODE = None
    interpolationMode: _enum.D2D1_BITMAP_INTERPOLATION_MODE = None


# noinspection PyPep8Naming
@_struct
class D2D1_LINEAR_GRADIENT_BRUSH_PROPERTIES:
    startPoint: D2D1_POINT_2F = None
    endPoint: D2D1_POINT_2F = None


# noinspection PyPep8Naming
@_struct
class D2D1_RADIAL_GRADIENT_BRUSH_PROPERTIES:
    center: D2D1_POINT_2F = None
    gradientOriginOffset: D2D1_POINT_2F = None
    radiusX: _type.FLOAT = None
    radiusY: _type.FLOAT = None


# noinspection PyPep8Naming
@_struct
class D2D1_FACTORY_OPTIONS:
    debugLevel: _enum.D2D1_DEBUG_LEVEL = None


# noinspection PyPep8Naming
@_struct
class D2D1_RENDER_TARGET_PROPERTIES:
    type: _enum.D2D1_RENDER_TARGET_TYPE = None
    pixelFormat: D2D1_PIXEL_FORMAT = None
    dpiX: _type.FLOAT = None
    dpiY: _type.FLOAT = None
    usage: _enum.D2D1_RENDER_TARGET_USAGE = None
    minLevel: _enum.D2D1_FEATURE_LEVEL = None


# noinspection PyPep8Naming
@_struct
class D2D1_HWND_RENDER_TARGET_PROPERTIES:
    hwnd: _type.HWND = None
    pixelSize: D2D1_SIZE_U = None
    presentOptions: _enum.D2D1_PRESENT_OPTIONS = None


# noinspection PyPep8Naming
@_struct
class D2D1_CREATION_PROPERTIES:
    threadingMode: _enum.D2D1_THREADING_MODE = None
    debugLevel: _enum.D2D1_DEBUG_LEVEL = None
    options: _enum.D2D1_DEVICE_CONTEXT_OPTIONS = None


# noinspection PyPep8Naming
@_struct
class D2D1_SVG_VIEWBOX:
    x: _type.FLOAT = None
    y: _type.FLOAT = None
    width: _type.FLOAT = None
    height: _type.FLOAT = None


# noinspection PyPep8Naming
@_struct
class DWRITE_FONT_METRICS:
    designUnitsPerEm: _type.UINT16 = None
    ascent: _type.UINT16 = None
    descent: _type.UINT16 = None
    lineGap: _type.INT16 = None
    capHeight: _type.UINT16 = None
    xHeight: _type.UINT16 = None
    underlinePosition: _type.INT16 = None
    underlineThickness: _type.UINT16 = None
    strikethroughPosition: _type.INT16 = None
    strikethroughThickness: _type.UINT16 = None


# noinspection PyPep8Naming
@_struct
class DWRITE_GLYPH_METRICS:
    leftSideBearing: _type.INT32 = None
    advanceWidth: _type.UINT32 = None
    rightSideBearing: _type.INT32 = None
    topSideBearing: _type.INT32 = None
    advanceHeight: _type.UINT32 = None
    bottomSideBearing: _type.INT32 = None
    verticalOriginY: _type.INT32 = None


# noinspection PyPep8Naming
@_struct
class DWRITE_GLYPH_OFFSET:
    advanceOffset: _type.FLOAT = None
    ascenderOffset: _type.FLOAT = None


# noinspection PyPep8Naming
@_struct
class DWRITE_GLYPH_RUN:
    fontFace: _type.IDWriteFontFace = None
    fontEmSize: _type.FLOAT = None
    glyphCount: _type.UINT32 = None
    glyphIndices: _Pointer[_type.UINT16] = None
    glyphAdvances: _Pointer[_type.FLOAT] = None
    glyphOffsets: _Pointer[DWRITE_GLYPH_OFFSET] = None
    isSideways: _type.BOOL = None
    bidiLevel: _type.UINT32 = None


@_struct
class PointF:
    X: _type.REAL = None
    Y: _type.REAL = None


@_struct
class Point:
    X: _type.INT = None
    Y: _type.INT = None


@_struct
class RectF:
    X: _type.REAL = None
    Y: _type.REAL = None
    Width: _type.REAL = None
    Height: _type.REAL = None


@_struct
class Rect:
    X: _type.INT = None
    Y: _type.INT = None
    Width: _type.INT = None
    Height: _type.INT = None


@_struct
class SizeF:
    Width: _type.REAL = None
    Height: _type.REAL = None


@_struct
class Size:
    Width: _type.INT = None
    Height: _type.INT = None


@_struct
class PathData:
    Count: _type.INT = None
    Points: _Pointer[PointF] = None
    Types: _Pointer[_type.BYTE] = None


@_struct
class CharacterRange:
    First: _type.INT = None
    Length: _type.INT = None


@_struct
class Color:
    Value: _type.ARGB = None


@_struct
class ColorMap:
    oldColor: Color = None
    newColor: Color = None


@_struct
class ColorPalette:
    Flags: _type.UINT = None
    Count: _type.UINT = None
    Entries: _type.ARGB * 1 = None


@_struct
class BitmapData:
    Width: _type.UINT = None
    Height: _type.UINT = None
    Stride: _type.INT = None
    PixelFormat: _type.INT = None
    Scan0: _type.PVOID = None
    Reserved: _type.UINT_PTR = None


@_struct
class EncoderParameter:
    Guid: GUID = None
    NumberOfValues: _type.ULONG = None
    Type: _type.ULONG = None
    Value: _type.PVOID = None


@_struct
class EncoderParameters:
    Count: _type.UINT = None
    # noinspection PyTypeChecker
    Parameter: EncoderParameter * 1 = None


@_struct
class ImageCodecInfo:
    Clsid: CLSID = None
    FormatID: GUID = None
    CodecName: _type.LPWSTR = None
    DllName: _type.LPWSTR = None
    FormatDescription: _type.LPWSTR = None
    FilenameExtension: _type.LPWSTR = None
    MimeType: _type.LPWSTR = None
    Flags: _type.DWORD = None
    Version: _type.DWORD = None
    SigCount: _type.DWORD = None
    SigSize: _type.DWORD = None
    SigPattern: _Pointer[_type.BYTE] = None
    SigMask: _Pointer[_type.BYTE] = None


@_struct
class PropertyItem:
    id: _type.PROPID = None
    length: _type.ULONG = None
    type: _type.WORD = None
    value: _type.PVOID = None


@_struct
class ImageItemData:
    Size: _type.UINT = None
    Position: _type.UINT = None
    Desc: _type.PVOID = None
    DescSize: _type.UINT = None
    Data: _Pointer[_type.UINT] = None
    DataSize: _type.UINT = None
    Cookie: _type.UINT = None


@_struct
class METAHEADER:
    mtType: _type.WORD = None
    mtHeaderSize: _type.WORD = None
    mtVersion: _type.WORD = None
    mtSize: _type.DWORD = None
    mtNoObjects: _type.WORD = None
    mtMaxRecord: _type.DWORD = None
    mtNoParameters: _type.WORD = None


@_struct
class ENHMETAHEADER3:
    iType: _type.DWORD = None
    nSize: _type.DWORD = None
    rclBounds: RECTL = None
    rclFrame: RECTL = None
    dSignature: _type.DWORD = None
    nVersion: _type.DWORD = None
    nBytes: _type.DWORD = None
    nRecords: _type.DWORD = None
    nHandles: _type.WORD = None
    sReserved: _type.WORD = None
    nDescription: _type.DWORD = None
    offDescription: _type.DWORD = None
    nPalEntries: _type.DWORD = None
    szlDevice: SIZEL = None
    szlMillimeters: SIZEL = None


@_struct
class PWMFRect16:
    Left: _type.INT16 = None
    Top: _type.INT16 = None
    Right: _type.INT16 = None
    Bottom: _type.INT16 = None


@_struct
class WmfPlaceableFileHeader:
    Key: _type.UINT32 = None
    Hmf: _type.UINT32 = None
    BoundingBox: PWMFRect16 = None
    Inch: _type.INT16 = None
    Reserved: _type.UINT32 = None
    Checksum: _type.INT16 = None


@_struct
class MetafileHeader:
    Type: _enum.MetafileType = None
    Size: _type.UINT = None
    Version: _type.UINT = None
    EmfPlusFlags: _type.UINT = None
    DpiX: _type.REAL = None
    DpiY: _type.REAL = None
    X: _type.INT = None
    Y: _type.INT = None
    Width: _type.INT = None
    Height: _type.INT = None
    U: _union.MetafileHeader_U = None
    EmfPlusHeaderSize: _type.INT = None
    LogicalDpiX: _type.INT = None
    LogicalDpiY: _type.INT = None


GpPointF = PointF
GpPoint = Point
GpRectF = RectF
GpRect = Rect
GpSizeF = SizeF
GpSize = Size
GpPathData = PathData
D2D_POINT_2L = POINT
D2D_RECT_L = RECT
D2D1_POINT_2F = D2D_POINT_2F
D2D1_POINT_2U = D2D_POINT_2U
D2D1_POINT_2L = D2D_POINT_2L
D2D1_RECT_F = D2D_RECT_F
D2D1_RECT_U = D2D_RECT_U
D2D1_RECT_L = D2D_RECT_L
D2D1_SIZE_F = D2D_SIZE_F
D2D1_SIZE_U = D2D_SIZE_U
D2D1_MATRIX_3X2_F = D2D_MATRIX_3X2_F
D2D_COLOR_F = D3DCOLORVALUE
D2D1_COLOR_F = D2D_COLOR_F
POINTL = POINT
RECTL = RECT
SIZEL = SIZE
UUID = GUID
IID = GUID
CLSID = GUID
KNOWNFOLDERID = GUID
DEVPROPGUID = GUID
VARIANTARG = VARIANT
ANSI_STRING = STRING
OEM_STRING = STRING
PATTERN = LOGBRUSH


class Windows:
    class ApplicationModel:
        @_struct
        class PackageInstallProgress:
            PercentComplete: _type.UINT32 = None

        @_struct
        class PackageVersion:
            Major: _type.UINT16 = None
            Minor: _type.UINT16 = None
            Build: _type.UINT16 = None
            Revision: _type.UINT16 = None

        class Resources:
            class Core:
                @_struct
                class ResourceLayoutInfo:
                    MajorVersion: _type.UINT32 = None
                    MinorVersion: _type.UINT32 = None
                    ResourceSubtreeCount: _type.UINT32 = None
                    NamedResourceCount: _type.UINT32 = None
                    Checksum: _type.INT32 = None

    class Data:
        class Text:
            @_struct
            class TextSegment:
                StartPosition: _type.UINT32 = None
                Length: _type.UINT32 = None

    class Devices:
        class Display:
            class Core:
                @_struct
                class DisplayPresentationRate:
                    VerticalSyncRate: Windows.Foundation.Numerics.Rational = None
                    VerticalSyncsPerPresentation: _type.INT32 = None

        class Geolocation:
            @_struct
            class BasicGeoposition:
                Latitude: _type.DOUBLE = None
                Longitude: _type.DOUBLE = None
                Altitude: _type.DOUBLE = None

        class Gpio:
            @_struct
            class GpioChangeCount:
                Count: _type.UINT64 = None
                RelativeTime: Windows.Foundation.TimeSpan = None

            @_struct
            class GpioChangeRecord:
                RelativeTime: Windows.Foundation.TimeSpan = None
                Edge: _enum.Windows.Devices.Gpio.GpioPinEdge = None

        class I2c:
            @_struct
            class I2cTransferResult:
                Status: _enum.Windows.Devices.I2c.I2cTransferStatus = None
                BytesTransferred: _type.UINT32 = None

            class Provider:
                @_struct
                class ProviderI2cTransferResult:
                    Status: _enum.Windows.Devices.I2c.Provider.ProviderI2cTransferStatus = None
                    BytesTransferred: _type.UINT32 = None

        class Input:
            @_struct
            class MouseDelta:
                X: _type.INT32 = None
                Y: _type.INT32 = None

            @_struct
            class PointerDeviceUsage:
                UsagePage: _type.UINT32 = None
                Usage: _type.UINT32 = None
                MinLogical: _type.INT32 = None
                MaxLogical: _type.INT32 = None
                MinPhysical: _type.INT32 = None
                MaxPhysical: _type.INT32 = None
                Unit: _type.UINT32 = None
                PhysicalMultiplier: _type.FLOAT = None

        class PointOfService:
            @_struct
            class SizeUInt32:
                Width: _type.UINT32 = None
                Height: _type.UINT32 = None

        class Scanners:
            @_struct
            class ImageScannerResolution:
                DpiX: _type.FLOAT = None
                DpiY: _type.FLOAT = None

        class Sms:
            @_struct
            class SmsEncodedLength:
                SegmentCount: _type.UINT32 = None
                CharacterCountLastSegment: _type.UINT32 = None
                CharactersPerSegment: _type.UINT32 = None
                ByteCountLastSegment: _type.UINT32 = None
                BytesPerSegment: _type.UINT32 = None

    class Foundation:
        @_struct
        class DateTime:
            UniversalTime: _type.INT64 = None

        @_struct
        class Point:
            X: _type.FLOAT = None
            Y: _type.FLOAT = None

        @_struct
        class Rect:
            X: _type.FLOAT = None
            Y: _type.FLOAT = None
            Width: _type.FLOAT = None
            Height: _type.FLOAT = None

        @_struct
        class Size:
            Width: _type.FLOAT = None
            Height: _type.FLOAT = None

        @_struct
        class TimeSpan:
            Duration: _type.INT64 = None

        class Numerics:
            @_struct
            class Matrix3x2:
                M11: _type.FLOAT = None
                M12: _type.FLOAT = None
                M21: _type.FLOAT = None
                M22: _type.FLOAT = None
                M31: _type.FLOAT = None
                M32: _type.FLOAT = None

            @_struct
            class Matrix4x4:
                M11: _type.FLOAT = None
                M12: _type.FLOAT = None
                M13: _type.FLOAT = None
                M14: _type.FLOAT = None
                M21: _type.FLOAT = None
                M22: _type.FLOAT = None
                M23: _type.FLOAT = None
                M24: _type.FLOAT = None
                M31: _type.FLOAT = None
                M32: _type.FLOAT = None
                M33: _type.FLOAT = None
                M34: _type.FLOAT = None
                M41: _type.FLOAT = None
                M42: _type.FLOAT = None
                M43: _type.FLOAT = None
                M44: _type.FLOAT = None

            @_struct
            class Vector3:
                X: _type.FLOAT = None
                Y: _type.FLOAT = None
                Z: _type.FLOAT = None

            @_struct
            class Plane:
                Normal: Windows.Foundation.Numerics.Vector3 = None
                D: _type.FLOAT = None

            @_struct
            class Quaternion:
                X: _type.FLOAT = None
                Y: _type.FLOAT = None
                Z: _type.FLOAT = None
                W: _type.FLOAT = None

            @_struct
            class Rational:
                Numerator: _type.UINT32 = None
                Denominator: _type.UINT32 = None

            @_struct
            class Vector2:
                X: _type.FLOAT = None
                Y: _type.FLOAT = None

            @_struct
            class Vector4:
                X: _type.FLOAT = None
                Y: _type.FLOAT = None
                Z: _type.FLOAT = None
                W: _type.FLOAT = None

    class Gaming:
        class Input:
            @_struct
            class ArcadeStickReading:
                Timestamp: _type.UINT64 = None
                Buttons: _enum.Windows.Gaming.Input.ArcadeStickButtons = None

            @_struct
            class FlightStickReading:
                Timestamp: _type.UINT64 = None
                Buttons: _enum.Windows.Gaming.Input.FlightStickButtons = None
                HatSwitch: _enum.Windows.Gaming.Input.GameControllerSwitchPosition = None
                Roll: _type.DOUBLE = None
                Pitch: _type.DOUBLE = None
                Yaw: _type.DOUBLE = None
                Throttle: _type.DOUBLE = None

            @_struct
            class GamepadReading:
                Timestamp: _type.UINT64 = None
                Buttons: _enum.Windows.Gaming.Input.GamepadButtons = None
                LeftTrigger: _type.DOUBLE = None
                RightTrigger: _type.DOUBLE = None
                LeftThumbstickX: _type.DOUBLE = None
                LeftThumbstickY: _type.DOUBLE = None
                RightThumbstickX: _type.DOUBLE = None
                RightThumbstickY: _type.DOUBLE = None

            @_struct
            class GamepadVibration:
                LeftMotor: _type.DOUBLE = None
                RightMotor: _type.DOUBLE = None
                LeftTrigger: _type.DOUBLE = None
                RightTrigger: _type.DOUBLE = None

            @_struct
            class RacingWheelReading:
                Timestamp: _type.UINT64 = None
                Buttons: _enum.Windows.Gaming.Input.RacingWheelButtons = None
                PatternShifterGear: _type.INT32 = None
                Wheel: _type.DOUBLE = None
                Throttle: _type.DOUBLE = None
                Brake: _type.DOUBLE = None
                Clutch: _type.DOUBLE = None
                Handbrake: _type.DOUBLE = None

            @_struct
            class UINavigationReading:
                Timestamp: _type.UINT64 = None
                RequiredButtons: _enum.Windows.Gaming.Input.RequiredUINavigationButtons = None
                OptionalButtons: _enum.Windows.Gaming.Input.OptionalUINavigationButtons = None

            class Custom:
                @_struct
                class GameControllerVersionInfo:
                    Major: _type.UINT16 = None
                    Minor: _type.UINT16 = None
                    Build: _type.UINT16 = None
                    Revision: _type.UINT16 = None

                @_struct
                class GipFirmwareUpdateProgress:
                    PercentCompleted: _type.DOUBLE = None
                    CurrentComponentId: _type.UINT32 = None

    class Graphics:
        @_struct
        class DisplayAdapterId:
            LowPart: _type.UINT32 = None
            HighPart: _type.INT32 = None

        @_struct
        class DisplayId:
            Value: _type.UINT64 = None

        @_struct
        class PointInt32:
            X: _type.INT32 = None
            Y: _type.INT32 = None

        @_struct
        class RectInt32:
            X: _type.INT32 = None
            Y: _type.INT32 = None
            Width: _type.INT32 = None
            Height: _type.INT32 = None

        @_struct
        class SizeInt32:
            Width: _type.INT32 = None
            Height: _type.INT32 = None

        class DirectX:
            class Direct3D11:
                @_struct
                class Direct3DMultisampleDescription:
                    Count: _type.INT32 = None
                    Quality: _type.INT32 = None

                @_struct
                class Direct3DSurfaceDescription:
                    Width: _type.INT32 = None
                    Height: _type.INT32 = None
                    Format: _enum.Windows.Graphics.DirectX.DirectXPixelFormat = None
                    MultisampleDescription: Windows.Graphics.DirectX.Direct3D11.Direct3DMultisampleDescription = None

        class Display:
            @_struct
            class NitRange:
                MinNits: _type.FLOAT = None
                MaxNits: _type.FLOAT = None
                StepSizeNits: _type.FLOAT = None

            class Core:
                @_struct
                class HdmiDisplayHdr2086Metadata:
                    RedPrimaryX: _type.UINT16 = None
                    RedPrimaryY: _type.UINT16 = None
                    GreenPrimaryX: _type.UINT16 = None
                    GreenPrimaryY: _type.UINT16 = None
                    BluePrimaryX: _type.UINT16 = None
                    BluePrimaryY: _type.UINT16 = None
                    WhitePointX: _type.UINT16 = None
                    WhitePointY: _type.UINT16 = None
                    MaxMasteringLuminance: _type.UINT16 = None
                    MinMasteringLuminance: _type.UINT16 = None
                    MaxContentLightLevel: _type.UINT16 = None
                    MaxFrameAverageLightLevel: _type.UINT16 = None

        class Holographic:
            @_struct
            class HolographicAdapterId:
                LowPart: _type.UINT32 = None
                HighPart: _type.INT32 = None

            @_struct
            class HolographicFrameId:
                Value: _type.UINT64 = None

            @_struct
            class HolographicStereoTransform:
                Left: Windows.Foundation.Numerics.Matrix4x4 = None
                Right: Windows.Foundation.Numerics.Matrix4x4 = None

        class Imaging:
            @_struct
            class BitmapBounds:
                X: _type.UINT32 = None
                Y: _type.UINT32 = None
                Width: _type.UINT32 = None
                Height: _type.UINT32 = None

            @_struct
            class BitmapPlaneDescription:
                StartIndex: _type.INT32 = None
                Width: _type.INT32 = None
                Height: _type.INT32 = None
                Stride: _type.INT32 = None

            @_struct
            class BitmapSize:
                Width: _type.UINT32 = None
                Height: _type.UINT32 = None

        class Printing:
            @_struct
            class PrintPageDescription:
                PageSize: Windows.Foundation.Size = None
                ImageableRect: Windows.Foundation.Rect = None
                DpiX: _type.UINT32 = None
                DpiY: _type.UINT32 = None

        class Printing3D:
            @_struct
            class Printing3DBufferDescription:
                Format: _enum.Windows.Graphics.Printing3D.Printing3DBufferFormat = None
                Stride: _type.UINT32 = None

    class Management:
        class Deployment:
            @_struct
            class DeploymentProgress:
                state: _enum.Windows.Management.Deployment.DeploymentProgressState = None
                percentage: _type.UINT32 = None

    class Media:
        @_struct
        class MediaTimeRange:
            Start: Windows.Foundation.TimeSpan = None
            End: Windows.Foundation.TimeSpan = None

        class Capture:
            @_struct
            class WhiteBalanceGain:
                R: _type.DOUBLE = None
                G: _type.DOUBLE = None
                B: _type.DOUBLE = None

        class Core:
            @_struct
            class MseTimeRange:
                Start: Windows.Foundation.TimeSpan = None
                End: Windows.Foundation.TimeSpan = None

            @_struct
            class TimedTextDouble:
                Value: _type.DOUBLE = None
                Unit: _enum.Windows.Media.Core.TimedTextUnit = None

            @_struct
            class TimedTextPadding:
                Before: _type.DOUBLE = None
                After: _type.DOUBLE = None
                Start: _type.DOUBLE = None
                End: _type.DOUBLE = None
                Unit: _enum.Windows.Media.Core.TimedTextUnit = None

            @_struct
            class TimedTextPoint:
                X: _type.DOUBLE = None
                Y: _type.DOUBLE = None
                Unit: _enum.Windows.Media.Core.TimedTextUnit = None

            @_struct
            class TimedTextSize:
                Height: _type.DOUBLE = None
                Width: _type.DOUBLE = None
                Unit: _enum.Windows.Media.Core.TimedTextUnit = None

        class Import:
            @_struct
            class PhotoImportProgress:
                ItemsImported: _type.UINT32 = None
                TotalItemsToImport: _type.UINT32 = None
                BytesImported: _type.UINT64 = None
                TotalBytesToImport: _type.UINT64 = None
                ImportProgress: _type.DOUBLE = None

        class Streaming:
            @_struct
            class PlaySpeed:
                Numerator: _type.INT32 = None
                Denominator: _type.UINT32 = None

            @_struct
            class TrackInformation:
                Track: _type.UINT32 = None
                TrackId: _type.UINT32 = None
                TrackDuration: Windows.Foundation.TimeSpan = None

            @_struct
            class PositionInformation:
                trackInformation: Windows.Media.Streaming.TrackInformation = None
                relativeTime: Windows.Foundation.TimeSpan = None

            @_struct
            class RenderingParameters:
                volume: _type.UINT32 = None
                mute: _type.boolean = None

            @_struct
            class TransportInformation:
                CurrentTransportState: _enum.Windows.Media.Streaming.TransportState = None
                CurrentTransportStatus: _enum.Windows.Media.Streaming.TransportStatus = None
                CurrentSpeed: Windows.Media.Streaming.PlaySpeed = None

    class Networking:
        class BackgroundTransfer:
            @_struct
            class BackgroundDownloadProgress:
                BytesReceived: _type.UINT64 = None
                TotalBytesToReceive: _type.UINT64 = None
                Status: _enum.Windows.Networking.BackgroundTransfer.BackgroundTransferStatus = None
                HasResponseChanged: _type.boolean = None
                HasRestarted: _type.boolean = None

            @_struct
            class BackgroundTransferFileRange:
                Offset: _type.UINT64 = None
                Length: _type.UINT64 = None

            @_struct
            class BackgroundUploadProgress:
                BytesReceived: _type.UINT64 = None
                BytesSent: _type.UINT64 = None
                TotalBytesToReceive: _type.UINT64 = None
                TotalBytesToSend: _type.UINT64 = None
                Status: _enum.Windows.Networking.BackgroundTransfer.BackgroundTransferStatus = None
                HasResponseChanged: _type.boolean = None
                HasRestarted: _type.boolean = None

        class Connectivity:
            @_struct
            class NetworkUsageStates:
                Roaming: _enum.Windows.Networking.Connectivity.TriStates = None
                Shared: _enum.Windows.Networking.Connectivity.TriStates = None

        class NetworkOperators:
            @_struct
            class ESimProfileInstallProgress:
                TotalSizeInBytes: _type.INT32 = None
                InstalledSizeInBytes: _type.INT32 = None

            @_struct
            class ProfileUsage:
                UsageInMegabytes: _type.UINT32 = None
                LastSyncTime: Windows.Foundation.DateTime = None

        class Sockets:
            @_struct
            class BandwidthStatistics:
                OutboundBitsPerSecond: _type.UINT64 = None
                InboundBitsPerSecond: _type.UINT64 = None
                OutboundBitsPerSecondInstability: _type.UINT64 = None
                InboundBitsPerSecondInstability: _type.UINT64 = None
                OutboundBandwidthPeaked: _type.boolean = None
                InboundBandwidthPeaked: _type.boolean = None

            @_struct
            class RoundTripTimeStatistics:
                Variance: _type.UINT32 = None
                Max: _type.UINT32 = None
                Min: _type.UINT32 = None
                Sum: _type.UINT32 = None

    class Perception:
        class People:
            @_struct
            class HandMeshVertex:
                Position: Windows.Foundation.Numerics.Vector3 = None
                Normal: Windows.Foundation.Numerics.Vector3 = None

            @_struct
            class JointPose:
                Orientation: Windows.Foundation.Numerics.Quaternion = None
                Position: Windows.Foundation.Numerics.Vector3 = None
                Radius: _type.FLOAT = None
                Accuracy: _enum.Windows.Perception.People.JointPoseAccuracy = None

        class Spatial:
            @_struct
            class SpatialBoundingBox:
                Center: Windows.Foundation.Numerics.Vector3 = None
                Extents: Windows.Foundation.Numerics.Vector3 = None

            @_struct
            class SpatialBoundingFrustum:
                Near: Windows.Foundation.Numerics.Plane = None
                Far: Windows.Foundation.Numerics.Plane = None
                Right: Windows.Foundation.Numerics.Plane = None
                Left: Windows.Foundation.Numerics.Plane = None
                Top: Windows.Foundation.Numerics.Plane = None
                Bottom: Windows.Foundation.Numerics.Plane = None

            @_struct
            class SpatialBoundingOrientedBox:
                Center: Windows.Foundation.Numerics.Vector3 = None
                Extents: Windows.Foundation.Numerics.Vector3 = None
                Orientation: Windows.Foundation.Numerics.Quaternion = None

            @_struct
            class SpatialBoundingSphere:
                Center: Windows.Foundation.Numerics.Vector3 = None
                Radius: _type.FLOAT = None

            @_struct
            class SpatialRay:
                Origin: Windows.Foundation.Numerics.Vector3 = None
                Direction: Windows.Foundation.Numerics.Vector3 = None

    class Security:
        class Isolation:
            @_struct
            class IsolatedWindowsEnvironmentCreateProgress:
                State: _enum.Windows.Security.Isolation.IsolatedWindowsEnvironmentProgressState = None
                PercentComplete: _type.UINT32 = None

    class Services:
        class Store:
            @_struct
            class StorePackageUpdateStatus:
                PackageFamilyName: _type.HSTRING = None
                PackageDownloadSizeInBytes: _type.UINT64 = None
                PackageBytesDownloaded: _type.UINT64 = None
                PackageDownloadProgress: _type.DOUBLE = None
                TotalDownloadProgress: _type.DOUBLE = None
                PackageUpdateState: _enum.Windows.Services.Store.StorePackageUpdateState = None

    class Storage:
        class AccessCache:
            @_struct
            class AccessListEntry:
                Token: _type.HSTRING = None
                Metadata: _type.HSTRING = None

        class Search:
            @_struct
            class SortEntry:
                PropertyName: _type.HSTRING = None
                AscendingOrder: _type.boolean = None

    class UI:
        @_struct
        class Color:
            A: _type.BYTE = None
            R: _type.BYTE = None
            G: _type.BYTE = None
            B: _type.BYTE = None

        @_struct
        class WindowId:
            Value: _type.UINT64 = None

        class Composition:
            @_struct
            class InkTrailPoint:
                Point: Windows.Foundation.Point = None
                Radius: _type.FLOAT = None

        class Core:
            @_struct
            class CorePhysicalKeyStatus:
                RepeatCount: _type.UINT32 = None
                ScanCode: _type.UINT32 = None
                IsExtendedKey: _type.boolean = None
                IsMenuKeyDown: _type.boolean = None
                WasKeyDown: _type.boolean = None
                IsKeyReleased: _type.boolean = None

            @_struct
            class CoreProximityEvaluation:
                Score: _type.INT32 = None
                AdjustedPoint: Windows.Foundation.Point = None

        class Input:
            @_struct
            class CrossSlideThresholds:
                SelectionStart: _type.FLOAT = None
                SpeedBumpStart: _type.FLOAT = None
                SpeedBumpEnd: _type.FLOAT = None
                RearrangeStart: _type.FLOAT = None

            @_struct
            class ManipulationDelta:
                Translation: Windows.Foundation.Point = None
                Scale: _type.FLOAT = None
                Rotation: _type.FLOAT = None
                Expansion: _type.FLOAT = None

            @_struct
            class ManipulationVelocities:
                Linear: Windows.Foundation.Point = None
                Angular: _type.FLOAT = None
                Expansion: _type.FLOAT = None

            class Preview:
                class Injection:
                    @_struct
                    class InjectedInputPoint:
                        PositionX: _type.INT32 = None
                        PositionY: _type.INT32 = None

                    @_struct
                    class InjectedInputPointerInfo:
                        PointerId: _type.UINT32 = None
                        PointerOptions: _enum.Windows.UI.Input.Preview.Injection.InjectedInputPointerOptions = None
                        PixelLocation: Windows.UI.Input.Preview.Injection.InjectedInputPoint = None
                        TimeOffsetInMilliseconds: _type.UINT32 = None
                        PerformanceCount: _type.UINT64 = None

                    @_struct
                    class InjectedInputRectangle:
                        Left: _type.INT32 = None
                        Top: _type.INT32 = None
                        Bottom: _type.INT32 = None
                        Right: _type.INT32 = None

        class Text:
            @_struct
            class FontWeight:
                Weight: _type.UINT16 = None

            class Core:
                @_struct
                class CoreTextRange:
                    StartCaretPosition: _type.INT32 = None
                    EndCaretPosition: _type.INT32 = None

        class UIAutomation:
            class Core:
                @_struct
                class AutomationAnnotationTypeRegistration:
                    LocalId: _type.INT32 = None

                @_struct
                class AutomationRemoteOperationOperandId:
                    Value: _type.INT32 = None

        class Xaml:
            @_struct
            class CornerRadius:
                TopLeft: _type.DOUBLE = None
                TopRight: _type.DOUBLE = None
                BottomRight: _type.DOUBLE = None
                BottomLeft: _type.DOUBLE = None

            @_struct
            class Duration:
                TimeSpan: Windows.Foundation.TimeSpan = None
                Type: _enum.Windows.UI.Xaml.DurationType = None

            @_struct
            class GridLength:
                Value: _type.DOUBLE = None
                GridUnitType: _enum.Windows.UI.Xaml.GridUnitType = None

            @_struct
            class Thickness:
                Left: _type.DOUBLE = None
                Top: _type.DOUBLE = None
                Right: _type.DOUBLE = None
                Bottom: _type.DOUBLE = None

            class Automation:
                class Peers:
                    @_struct
                    class RawElementProviderRuntimeId:
                        Part1: _type.UINT32 = None
                        Part2: _type.UINT32 = None

            class Controls:
                class Maps:
                    @_struct
                    class MapZoomLevelRange:
                        Min: _type.DOUBLE = None
                        Max: _type.DOUBLE = None

                class Primitives:
                    @_struct
                    class GeneratorPosition:
                        Index: _type.INT32 = None
                        Offset: _type.INT32 = None

            class Data:
                @_struct
                class LoadMoreItemsResult:
                    Count: _type.UINT32 = None

            class Documents:
                @_struct
                class TextRange:
                    StartIndex: _type.INT32 = None
                    Length: _type.INT32 = None

            class Interop:
                @_struct
                class TypeName:
                    Name: _type.HSTRING = None
                    Kind: _enum.Windows.UI.Xaml.Interop.TypeKind = None

            class Markup:
                @_struct
                class XamlBinaryWriterErrorInformation:
                    InputStreamIndex: _type.UINT32 = None
                    LineNumber: _type.UINT32 = None
                    LinePosition: _type.UINT32 = None

                @_struct
                class XmlnsDefinition:
                    XmlNamespace: _type.HSTRING = None
                    Namespace: _type.HSTRING = None

            class Media:
                @_struct
                class Matrix:
                    M11: _type.DOUBLE = None
                    M12: _type.DOUBLE = None
                    M21: _type.DOUBLE = None
                    M22: _type.DOUBLE = None
                    OffsetX: _type.DOUBLE = None
                    OffsetY: _type.DOUBLE = None

                class Animation:
                    @_struct
                    class KeyTime:
                        TimeSpan: Windows.Foundation.TimeSpan = None

                    @_struct
                    class RepeatBehavior:
                        Count: _type.DOUBLE = None
                        Duration: Windows.Foundation.TimeSpan = None
                        Type: _enum.Windows.UI.Xaml.Media.Animation.RepeatBehaviorType = None

                class Media3D:
                    @_struct
                    class Matrix3D:
                        M11: _type.DOUBLE = None
                        M12: _type.DOUBLE = None
                        M13: _type.DOUBLE = None
                        M14: _type.DOUBLE = None
                        M21: _type.DOUBLE = None
                        M22: _type.DOUBLE = None
                        M23: _type.DOUBLE = None
                        M24: _type.DOUBLE = None
                        M31: _type.DOUBLE = None
                        M32: _type.DOUBLE = None
                        M33: _type.DOUBLE = None
                        M34: _type.DOUBLE = None
                        OffsetX: _type.DOUBLE = None
                        OffsetY: _type.DOUBLE = None
                        OffsetZ: _type.DOUBLE = None
                        M44: _type.DOUBLE = None

    class Web:
        class Http:
            @_struct
            class HttpProgress:  # TODO
                Stage: _enum.Windows.Web.Http.HttpProgressStage = None
                BytesSent: _type.UINT64 = None
                ...  # TotalBytesToSend: _interface.Windows.Foundation.IReference[_type.UINT64] = None
                BytesReceived: _type.UINT64 = None
                ...  # TotalBytesToReceive: _interface.Windows.Foundation.IReference[_type.UINT64] = None
                Retries: _type.UINT32 = None

        class Syndication:
            @_struct
            class RetrievalProgress:
                BytesRetrieved: _type.UINT32 = None
                TotalBytesToRetrieve: _type.UINT32 = None

            @_struct
            class TransferProgress:
                BytesSent: _type.UINT32 = None
                TotalBytesToSend: _type.UINT32 = None
                BytesRetrieved: _type.UINT32 = None
                TotalBytesToRetrieve: _type.UINT32 = None


class _NamespaceMeta(type):
    def __new__(mcs, *args, **kwargs):
        cls = super().__new__(mcs, *args, **kwargs)
        cls._vars = {}
        for name, val in tuple(vars(cls).items()):
            if not name.startswith('_'):
                cls._vars[name] = val
                delattr(cls, name)
        return cls

    def __getattr__(cls, name):
        if name in cls._vars:
            setattr(cls, name, _init(name, cls._vars[name]))
        return super().__getattribute__(name)


class _Struct(_ctypes.Structure):
    def __init__(self, *args, **kwargs):
        for name, val in self._defaults[len(args):]:
            if val is not None and name not in kwargs:
                kwargs[name] = val
        super().__init__(*args, **kwargs)

    __repr__ = _fields_repr


def _init(item: str, var: _Optional[type] = None) -> type:
    if var is None:
        var = _globals.vars_[item]
    if getattr(var, '__annotations__', None):
        fields = tuple((name, _resolve_type(annot)) for name, annot in _typing.get_type_hints(var, _globals, _globals).items())
        # noinspection PyProtectedMember
        struct = type(item, (_Struct,), {'_fields_': tuple(
            (*field, field[1]._bitfield) if hasattr(field[1], '_bitfield') else field for field in fields)})
        # noinspection PyTypeChecker
        size = _ctypes.sizeof(struct)
        struct._defaults = tuple((field[0], size if (val := getattr(var, field[0])) is _SIZE else val) for field in fields)
        return struct
    else:
        return _NamespaceMeta(item, (), dict(vars(var)))


_globals = _Globals()
