from __future__ import annotations as _

import ctypes as _ctypes
import functools as _functools
import typing as _typing
from typing import Optional as _Optional

from . import const as _const
from . import enum as _enum
from . import type as _type
from . import union as _union
from ._utils import _CT
from ._utils import _Globals
from ._utils import _Pointer
from ._utils import _fields_repr
from ._utils import _resolve_type
from ._utils import _sizeof
from .const import ChromaSDK as _const_ChromaSDK
from .const import iCUESDK as _const_iCUESDK
from .enum import ChromaSDK as _enum_ChromaSDK
from .enum import iCUESDK as _enum_iCUESDK
from .enum import libclang as _enum_libclang

if None:
    from dataclasses import dataclass as _struct
else:
    def _struct(cls: _CT) -> _CT:
        cls._struct = None
        return cls

_SIZE = object()


@_functools.cache
def _bitfield(cls: type[_CT], sz: int) -> type[_CT]:
    # noinspection PyTypeChecker
    return type(cls.__name__, (cls,), {'_bitfield': sz})


# python
# pybuffer
# noinspection PyPep8Naming
@_struct
class Py_buffer:
    buf: _type.c_void_p
    obj: _type.py_object
    len: _type.Py_ssize_t
    itemsize: _type.Py_ssize_t
    readonly: _type.c_int
    ndim: _type.c_int
    format: _type.c_char_p
    shape: _Pointer[_type.Py_ssize_t]
    strides: _Pointer[_type.Py_ssize_t]
    suboffsets: _Pointer[_type.Py_ssize_t]
    internal: _type.c_void_p


@_struct
class WINDOWCOMPOSITIONATTRIBDATA:
    Attrib: _enum.WINDOWCOMPOSITIONATTRIB
    pvData: _type.PVOID
    cbData: _type.SIZE_T


# noinspection PyPep8Naming
@_struct
class ACCENT_POLICY:
    AccentState: _enum.ACCENT_STATE
    AccentFlags: _type.UINT
    GradientColor: _type.COLORREF
    AnimationId: _type.LONG


@_struct
class FILE:
    _Placeholder: _type.c_void_p


@_struct
class COMMPROP:
    wPacketLength: _type.WORD
    wPacketVersion: _type.WORD
    dwServiceMask: _type.DWORD
    dwReserved1: _type.DWORD
    dwMaxTxQueue: _type.DWORD
    dwMaxRxQueue: _type.DWORD
    dwMaxBaud: _type.DWORD
    dwProvSubType: _type.DWORD
    dwProvCapabilities: _type.DWORD
    dwSettableParams: _type.DWORD
    dwSettableBaud: _type.DWORD
    wSettableData: _type.WORD
    wSettableStopParity: _type.WORD
    dwCurrentTxQueue: _type.DWORD
    dwCurrentRxQueue: _type.DWORD
    dwProvSpec1: _type.DWORD
    dwProvSpec2: _type.DWORD
    wcProvChar: _type.WORD * 1


@_struct
class COMSTAT:
    fCtsHold: _bitfield(_type.DWORD, 1)
    fDsrHold: _bitfield(_type.DWORD, 1)
    fRlsdHold: _bitfield(_type.DWORD, 1)
    fXoffHold: _bitfield(_type.DWORD, 1)
    fXoffSent: _bitfield(_type.DWORD, 1)
    fEof: _bitfield(_type.DWORD, 1)
    fTxim: _bitfield(_type.DWORD, 1)
    fReserved: _bitfield(_type.DWORD, 25)
    cbInQue: _type.DWORD
    cbOutQue: _type.DWORD


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
    ReadIntervalTimeout: _type.DWORD
    ReadTotalTimeoutMultiplier: _type.DWORD
    ReadTotalTimeoutConstant: _type.DWORD
    WriteTotalTimeoutMultiplier: _type.DWORD
    WriteTotalTimeoutConstant: _type.DWORD


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
    rgbBlue: _type.BYTE
    rgbGreen: _type.BYTE
    rgbRed: _type.BYTE


@_struct
class RGBQUAD:
    rgbBlue: _type.BYTE
    rgbGreen: _type.BYTE
    rgbRed: _type.BYTE
    rgbReserved: _type.BYTE


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
    bmiHeader: BITMAPINFOHEADER
    # noinspection PyTypeChecker
    bmiColors: RGBQUAD * 1  # TODO _array (type hint)


@_struct
class BITMAP:
    bmType: _type.LONG
    bmWidth: _type.LONG
    bmHeight: _type.LONG
    bmWidthBytes: _type.LONG
    bmPlanes: _type.WORD
    bmBitsPixel: _type.WORD
    bmBits: _type.LPVOID


@_struct
class DIBSECTION:
    dsBm: BITMAP
    dsBmih: BITMAPINFOHEADER
    dsBitfields: _type.DWORD * 3
    dshSection: _type.HANDLE
    dsOffset: _type.DWORD


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
class VALENTA:
    ve_valuename: _type.LPSTR
    ve_valuelen: _type.DWORD
    ve_valueptr: _type.DWORD_PTR
    ve_type: _type.DWORD


@_struct
class VALENTW:
    ve_valuename: _type.LPWSTR
    ve_valuelen: _type.DWORD
    ve_valueptr: _type.DWORD_PTR
    ve_type: _type.DWORD


# noinspection PyPep8Naming
@_struct
class HWPROFILEINFO_A:
    HWPI_ulHWProfile: _type.ULONG
    HWPI_szFriendlyName: _type.CHAR * _const.MAX_PROFILE_LEN
    HWPI_dwFlags: _type.DWORD


# noinspection PyPep8Naming
@_struct
class HWPROFILEINFO_W:
    HWPI_ulHWProfile: _type.ULONG
    HWPI_szFriendlyName: _type.WCHAR * _const.MAX_PROFILE_LEN
    HWPI_dwFlags: _type.DWORD


# noinspection PyPep8Naming
@_struct
class CONFLICT_DETAILS_A:
    CD_ulsize: _type.ULONG
    CD_ulMask: _type.ULONG
    CD_dnDevInst: _type.DEVINST
    CD_rdResDes: _type.RES_DES
    CD_ulFlags: _type.ULONG
    CD_szDescription: _type.CHAR * _const.MAX_PATH


# noinspection PyPep8Naming
@_struct
class CONFLICT_DETAILS_W:
    CD_ulsize: _type.ULONG
    CD_ulMask: _type.ULONG
    CD_dnDevInst: _type.DEVINST
    CD_rdResDes: _type.RES_DES
    CD_ulFlags: _type.ULONG
    CD_szDescription: _type.WCHAR * _const.MAX_PATH


# noinspection PyPep8Naming
@_struct
class HSTRING_HEADER:
    Reserved: _union.HSTRING_HEADER_U


@_struct
class GUID:
    Data1: _type.c_ulong
    Data2: _type.c_ushort
    Data3: _type.c_ushort
    Data4: _type.c_uchar * 8


@_struct
class WALLPAPEROPT:
    dwSize: _type.DWORD = _SIZE
    dwStyle: _type.DWORD = None


@_struct
class POINT:
    x: _type.LONG
    y: _type.LONG


@_struct
class RECT:
    left: _type.LONG
    top: _type.LONG
    right: _type.LONG
    bottom: _type.LONG


@_struct
class SIZE:
    cx: _type.LONG
    cy: _type.LONG


@_struct
class COORD:
    X: _type.SHORT
    Y: _type.SHORT


# noinspection PyPep8Naming
@_struct
class SMALL_RECT:
    Left: _type.SHORT
    Top: _type.SHORT
    Right: _type.SHORT
    Bottom: _type.SHORT


# noinspection PyPep8Naming
@_struct
class COMDLG_FILTERSPEC:
    pszName: _type.LPCWSTR
    pszSpec: _type.LPCWSTR


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
    cb: _type.USHORT
    abID: _type.BYTE * 1


@_struct
class ITEMIDLIST:
    mkid: SHITEMID


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
    style: _type.UINT
    lpfnWndProc: _type.WNDPROC
    cbClsExtra: _type.c_int
    cbWndExtra: _type.c_int
    hInstance: _type.HINSTANCE
    hIcon: _type.HINSTANCE
    hCursor: _type.HCURSOR
    hbrBackground: _type.HBRUSH
    lpszMenuName: _type.LPCSTR
    lpszClassName: _type.LPCSTR


@_struct
class WNDCLASSW:
    style: _type.UINT
    lpfnWndProc: _type.WNDPROC
    cbClsExtra: _type.c_int
    cbWndExtra: _type.c_int
    hInstance: _type.HINSTANCE
    hIcon: _type.HINSTANCE
    hCursor: _type.HCURSOR
    hbrBackground: _type.HBRUSH
    lpszMenuName: _type.LPCWSTR
    lpszClassName: _type.LPCWSTR


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
    x: _type.LONG
    y: _type.LONG


@_struct
class MINMAXINFO:
    ptReserved: POINT
    ptMaxSize: POINT
    ptMaxPosition: POINT
    ptMinTrackSize: POINT
    ptMaxTrackSize: POINT


@_struct
class MSG:
    hwnd: _type.HWND
    message: _type.UINT
    wParam: _type.WPARAM
    lParam: _type.WPARAM
    time: _type.DWORD
    pt: POINT
    lPrivate: _type.DWORD


@_struct
class FILETIME:
    dwLowDateTime: _type.DWORD
    dwHighDateTime: _type.DWORD


# noinspection PyPep8Naming
@_struct
class WIN32_FIND_DATAA:
    dwFileAttributes: _type.DWORD
    ftCreationTime: FILETIME
    ftLastAccessTime: FILETIME
    ftLastWriteTime: FILETIME
    nFileSizeHigh: _type.DWORD
    nFileSizeLow: _type.DWORD
    dwReserved0: _type.DWORD
    dwReserved1: _type.DWORD
    cFileName: _type.CHAR * _const.MAX_PATH
    cAlternateFileName: _type.CHAR * 14
    # noinspection PyProtectedMember
    if _const._MAC:
        dwFileType: _type.DWORD
        dwCreatorType: _type.DWORD
        wFinderFlags: _type.WORD


# noinspection PyPep8Naming
@_struct
class WIN32_FIND_DATAW:
    dwFileAttributes: _type.DWORD
    ftCreationTime: FILETIME
    ftLastAccessTime: FILETIME
    ftLastWriteTime: FILETIME
    nFileSizeHigh: _type.DWORD
    nFileSizeLow: _type.DWORD
    dwReserved0: _type.DWORD
    dwReserved1: _type.DWORD
    cFileName: _type.WCHAR * _const.MAX_PATH
    cAlternateFileName: _type.WCHAR * 14
    # noinspection PyProtectedMember
    if _const._MAC:
        dwFileType: _type.DWORD
        dwCreatorType: _type.DWORD
        wFinderFlags: _type.WORD


@_struct
class PROPERTYKEY:
    fmtid: GUID
    pid: _type.DWORD


@_struct
class CSPLATFORM:
    dwPlatformId: _type.DWORD
    dwVersionHi: _type.DWORD
    dwVersionLo: _type.DWORD
    dwProcessorArch: _type.DWORD


# noinspection PyPep8Naming
@_struct
class DECIMAL_U_S:
    scale: _type.BYTE
    sign: _type.BYTE


# noinspection PyPep8Naming
@_struct
class DECIMAL_U2_S:
    Lo32: _type.ULONG
    Mid32: _type.ULONG


@_struct
class DECIMAL:
    wReserved: _type.USHORT
    U: _union.DECIMAL_U
    Hi32: _type.ULONG
    U2: _union.DECIMAL_U2


# noinspection PyPep8Naming
@_struct
class PROPVARIANT_U_S:
    vt: _type.VARTYPE
    wReserved1: _type.PROPVAR_PAD1
    wReserved2: _type.PROPVAR_PAD2
    wReserved3: _type.PROPVAR_PAD3
    U: _union.PROPVARIANT_U_S_U


@_struct
class PROPVARIANT:
    U: _union.PROPVARIANT_U


@_struct
class MOUSEINPUT:
    dx: _type.LONG
    dy: _type.LONG
    mouseData: _type.DWORD
    dwFlags: _type.DWORD
    time: _type.DWORD
    dwExtraInfo: _type.ULONG_PTR


@_struct
class KEYBDINPUT:
    wVk: _type.WORD
    wScan: _type.WORD
    dwFlags: _type.DWORD
    time: _type.DWORD
    dwExtraInfo: _type.ULONG_PTR


@_struct
class HARDWAREINPUT:
    uMsg: _type.DWORD
    wParamL: _type.WORD
    wParamH: _type.WORD


@_struct
class INPUT:
    type: _type.DWORD
    U: _union.INPUT_U


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
    hwndOwner: _type.HWND
    pidlRoot: _Pointer[_Pointer[ITEMIDLIST]]
    pszDisplayName: _type.LPSTR
    lpszTitle: _type.LPCSTR
    ulFlags: _type.UINT
    lpfn: _type.BFFCALLBACK
    lParam: _type.LPARAM
    iImage: _type.c_int


@_struct
class BROWSEINFOW:
    hwndOwner: _type.HWND
    pidlRoot: _Pointer[_Pointer[ITEMIDLIST]]
    pszDisplayName: _type.LPWSTR
    lpszTitle: _type.LPCWSTR
    ulFlags: _type.UINT
    lpfn: _type.BFFCALLBACK
    lParam: _type.LPARAM
    iImage: _type.c_int


@_struct
class PAINTSTRUCT:
    hdc: _type.HDC
    fErase: _type.BOOL
    rcPaint: RECT
    fRestore: _type.BOOL
    fIncUpdate: _type.BOOL
    rgbReserved: _type.BYTE * 32


# noinspection PyPep8Naming
@_struct
class PICTDESC_U_S:
    hbitmap: _type.HBITMAP
    hpal: _type.HPALETTE


# noinspection PyPep8Naming
@_struct
class PICTDESC_U_S2:
    hmeta: _type.HMETAFILE
    xExt: _type.c_int
    yExt: _type.c_int


# noinspection PyPep8Naming
@_struct
class PICTDESC_U_S3:
    hicon: _type.HICON


# noinspection PyPep8Naming
@_struct
class PICTDESC_U_S4:
    hemf: _type.HMETAFILE


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
    S: MONITORINFO
    szDevice: _type.CHAR * _const.CCHDEVICENAME


@_struct
class MONITORINFOEXW:
    S: MONITORINFO
    szDevice: _type.WCHAR * _const.CCHDEVICENAME


@_struct
class SHFILEINFOA:
    hIcon: _type.HICON
    iIcon: _type.c_int
    dwAttributes: _type.DWORD
    szDisplayName: _type.CHAR * _const.MAX_PATH
    szTypeName: _type.CHAR * 80


@_struct
class SHFILEINFOW:
    hIcon: _type.HICON
    iIcon: _type.c_int
    dwAttributes: _type.DWORD
    szDisplayName: _type.WCHAR * _const.MAX_PATH
    szTypeName: _type.WCHAR * 80


# noinspection PyPep8Naming
@_struct
class VARIANT_U_S:
    vt: _type.VARTYPE
    wReserved1: _type.WORD
    wReserved2: _type.WORD
    wReserved3: _type.WORD
    U: _union.VARIANT_U_S_U


@_struct
class VARIANT:
    U: _union.VARIANT_U


@_struct
class DISPPARAMS:
    rgvarg: _Pointer[VARIANTARG]
    rgdispidNamedArgs: _Pointer[_type.DISPID]
    cArgs: _type.UINT
    cNamedArgs: _type.UINT


@_struct
class EXCEPINFO:
    wCode: _type.WORD
    wReserved: _type.WORD
    bstrSource: _type.BSTR
    bstrDescription: _type.BSTR
    bstrHelpFile: _type.BSTR
    dwHelpContext: _type.DWORD
    pvReserved: _type.ULONG_PTR
    pfnDeferredFillIn: _type.ULONG_PTR
    scode: _type.SCODE


@_struct
class SAFEARRAYBOUND:
    cElements: _type.ULONG
    lLbound: _type.LONG


@_struct
class TYPEDESC:
    U: _type.TYPEDESC_U
    vt: _type.VARTYPE


@_struct
class ARRAYDESC:
    tdescElem: TYPEDESC
    cDims: _type.USHORT
    # noinspection PyTypeChecker
    rgbounds: SAFEARRAYBOUND * 1


@_struct
class PARAMDESCEX:
    cBytes: _type.ULONG
    varDefaultValue: VARIANTARG


@_struct
class PARAMDESC:
    pparamdescex: _Pointer[PARAMDESCEX]
    wParamFlags: _type.USHORT


@_struct
class IDLDESC:
    dwReserved: _type.ULONG_PTR
    wIDLFlags: _type.USHORT


@_struct
class ELEMDESC:
    tdesc: TYPEDESC
    U: _union.ELEMDESC_U


@_struct
class TYPEATTR:
    guid: GUID
    lcid: _type.LCID
    dwReserved: _type.DWORD
    memidConstructor: _type.MEMBERID
    memidDestructor: _type.MEMBERID
    lpstrSchema: _type.LPOLESTR
    cbSizeInstance: _type.ULONG
    typekind: _enum.TYPEKIND
    cFuncs: _type.WORD
    cVars: _type.WORD
    cImplTypes: _type.WORD
    cbSizeVft: _type.WORD
    cbAlignment: _type.WORD
    wTypeFlags: _type.WORD
    wMajorVerNum: _type.WORD
    wMinorVerNum: _type.WORD
    tdescAlias: TYPEDESC
    idldescType: IDLDESC


@_struct
class FUNCDESC:
    memid: _type.MEMBERID
    lprgscode: _Pointer[_type.SCODE]
    lprgelemdescParam: _Pointer[ELEMDESC]
    funckind: _enum.FUNCKIND
    invkind: _enum.INVOKEKIND
    callconv: _enum.CALLCONV
    cParams: _type.SHORT
    cParamsOpt: _type.SHORT
    oVft: _type.SHORT
    cScodes: _type.SHORT
    elemdescFunc: ELEMDESC
    wFuncFlags: _type.WORD


@_struct
class VARDESC:
    memid: _type.MEMBERID
    lpstrSchema: _type.LPOLESTR
    U: _union.VARDESC_U
    elemdescVar: ELEMDESC
    wVarFlags: _type.WORD
    varkind: _enum.VARKIND


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
    fmtid: DEVPROPGUID
    pid: _type.DEVPROPID


@_struct
class BLENDFUNCTION:
    BlendOp: _type.BYTE
    BlendFlags: _type.BYTE
    SourceConstantAlpha: _type.BYTE
    AlphaFormat: _type.BYTE


@_struct
class ColorMatrix:
    m: _type.REAL * 5 * 5


@_struct
class EventRegistrationToken:
    value: _type.c_int64


@_struct
class Rational:
    Numerator: _type.UINT32
    Denominator: _type.UINT32


# noinspection PyPep8Naming
@_struct
class WNF_TYPE_ID:
    TypeId: GUID


# noinspection PyPep8Naming
@_struct
class WNF_STATE_NAME:
    Data: _type.ULONG * 2


@_struct
class STRING32:
    Length: _type.USHORT
    MaximumLength: _type.USHORT
    Buffer: _type.ULONG


@_struct
class STRING64:
    Length: _type.USHORT
    MaximumLength: _type.USHORT
    Buffer: _type.ULONGLONG


@_struct
class OPENASINFO:
    pcszFile: _type.LPCWSTR
    pcszClass: _type.LPCWSTR
    oaifInFlags: _enum.OPEN_AS_INFO_FLAGS


# noinspection PyPep8Naming
@_struct
class CONSOLE_READCONSOLE_CONTROL:
    nLength: _type.ULONG
    nInitialChars: _type.ULONG
    dwCtrlWakeupMask: _type.ULONG
    dwControlKeyState: _type.ULONG


# noinspection PyPep8Naming
@_struct
class CHAR_INFO:
    Char: _union.CHAR_INFO_U
    Attributes: _type.WORD


# noinspection PyPep8Naming
@_struct
class CONSOLE_FONT_INFO:
    nFont: _type.DWORD
    dwFontSize: COORD


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
    dwFlags: _type.DWORD
    dwSelectionAnchor: COORD
    srSelection: SMALL_RECT


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
    hwndSource: _type.HWND
    hwndSink: _type.HWND
    wFmt: _type.DWORD
    dwData: _type.ULONG_PTR
    ptDrop: POINT
    dwControlData: _type.DWORD


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
    versionNumber: _type.WORD
    offset: _type.WORD


@_struct
class MENUITEMTEMPLATE:
    mtOption: _type.WORD
    mtID: _type.WORD
    mtString: _type.WCHAR * 1


@_struct
class STRING:
    Length: _type.USHORT
    MaximumLength: _type.USHORT
    Buffer: _type.PCHAR


# noinspection PyPep8Naming
@_struct
class UNICODE_STRING:
    Length: _type.USHORT
    MaximumLength: _type.USHORT
    Buffer: _type.PWSTR


@_struct
class ACCEL:
    # noinspection PyProtectedMember
    if not _const._MAC:
        fVirt: _type.BYTE
        key: _type.WORD
        cmd: _type.WORD
    else:
        fVirt: _type.WORD
        key: _type.WORD
        cmd: _type.DWORD


@_struct
class PAINTSTRUCT:
    hdc: _type.HDC
    fErase: _type.BOOL
    rcPaint: RECT
    fRestore: _type.BOOL
    fIncUpdate: _type.BOOL
    rgbReserved: _type.BYTE * 32


@_struct
class CREATESTRUCTA:
    lpCreateParams: _type.LPVOID
    hInstance: _type.HINSTANCE
    hMenu: _type.HMENU
    hwndParent: _type.HWND
    cy: _type.c_int
    cx: _type.c_int
    y: _type.c_int
    x: _type.c_int
    style: _type.LONG
    lpszName: _type.LPCSTR
    lpszClass: _type.LPCSTR
    dwExStyle: _type.DWORD


@_struct
class CREATESTRUCTW:
    lpCreateParams: _type.LPVOID
    hInstance: _type.HINSTANCE
    hMenu: _type.HMENU
    hwndParent: _type.HWND
    cy: _type.c_int
    cx: _type.c_int
    y: _type.c_int
    x: _type.c_int
    style: _type.LONG
    lpszName: _type.LPCWSTR
    lpszClass: _type.LPCWSTR
    dwExStyle: _type.DWORD


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
    hwndFrom: _type.HWND
    idFrom: _type.UINT_PTR
    code: _type.UINT


@_struct
class STYLESTRUCT:
    styleOld: _type.DWORD
    styleNew: _type.DWORD


@_struct
class MEASUREITEMSTRUCT:
    CtlType: _type.UINT
    CtlID: _type.UINT
    itemID: _type.UINT
    itemWidth: _type.UINT
    itemHeight: _type.UINT
    itemData: _type.ULONG_PTR


@_struct
class DRAWITEMSTRUCT:
    CtlType: _type.UINT
    CtlID: _type.UINT
    itemID: _type.UINT
    itemAction: _type.UINT
    itemState: _type.UINT
    hwndItem: _type.HWND
    hDC: _type.HDC
    rcItem: RECT
    itemData: _type.ULONG_PTR


@_struct
class DELETEITEMSTRUCT:
    CtlType: _type.UINT
    CtlID: _type.UINT
    itemID: _type.UINT
    hwndItem: _type.HWND
    itemData: _type.ULONG_PTR


@_struct
class COMPAREITEMSTRUCT:
    CtlType: _type.UINT
    CtlID: _type.UINT
    hwndItem: _type.HWND
    itemID1: _type.UINT
    itemData1: _type.ULONG_PTR
    itemID2: _type.UINT
    itemData2: _type.ULONG_PTR
    dwLocaleId: _type.DWORD


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
class THUMBBUTTON:
    dwMask: _enum.THUMBBUTTONMASK
    iId: _type.UINT
    iBitmap: _type.UINT
    hIcon: _type.HICON
    szTip: _type.WCHAR * 260
    dwFlags: _enum.THUMBBUTTONFLAGS


@_struct
class DTBGOPTS:
    dwSize: _type.DWORD = _SIZE
    dwFlags: _type.DWORD = None
    rcClip: RECT = None


@_struct
class TEXTMETRICA:
    tmHeight: _type.LONG
    tmAscent: _type.LONG
    tmDescent: _type.LONG
    tmInternalLeading: _type.LONG
    tmExternalLeading: _type.LONG
    tmAveCharWidth: _type.LONG
    tmMaxCharWidth: _type.LONG
    tmWeight: _type.LONG
    tmOverhang: _type.LONG
    tmDigitizedAspectX: _type.LONG
    tmDigitizedAspectY: _type.LONG
    tmFirstChar: _type.BYTE
    tmLastChar: _type.BYTE
    tmDefaultChar: _type.BYTE
    tmBreakChar: _type.BYTE
    tmItalic: _type.BYTE
    tmUnderlined: _type.BYTE
    tmStruckOut: _type.BYTE
    tmPitchAndFamily: _type.BYTE
    tmCharSet: _type.BYTE


@_struct
class TEXTMETRICW:
    tmHeight: _type.LONG
    tmAscent: _type.LONG
    tmDescent: _type.LONG
    tmInternalLeading: _type.LONG
    tmExternalLeading: _type.LONG
    tmAveCharWidth: _type.LONG
    tmMaxCharWidth: _type.LONG
    tmWeight: _type.LONG
    tmOverhang: _type.LONG
    tmDigitizedAspectX: _type.LONG
    tmDigitizedAspectY: _type.LONG
    tmFirstChar: _type.WCHAR
    tmLastChar: _type.WCHAR
    tmDefaultChar: _type.WCHAR
    tmBreakChar: _type.WCHAR
    tmItalic: _type.BYTE
    tmUnderlined: _type.BYTE
    tmStruckOut: _type.BYTE
    tmPitchAndFamily: _type.BYTE
    tmCharSet: _type.BYTE


@_struct
class LOGFONTA:
    lfHeight: _type.LONG
    lfWidth: _type.LONG
    lfEscapement: _type.LONG
    lfOrientation: _type.LONG
    lfWeight: _type.LONG
    lfItalic: _type.BYTE
    lfUnderline: _type.BYTE
    lfStrikeOut: _type.BYTE
    lfCharSet: _type.BYTE
    lfOutPrecision: _type.BYTE
    lfClipPrecision: _type.BYTE
    lfQuality: _type.BYTE
    lfPitchAndFamily: _type.BYTE
    lfFaceName: _type.CHAR * _const.LF_FACESIZE


@_struct
class LOGFONTW:
    lfHeight: _type.LONG
    lfWidth: _type.LONG
    lfEscapement: _type.LONG
    lfOrientation: _type.LONG
    lfWeight: _type.LONG
    lfItalic: _type.BYTE
    lfUnderline: _type.BYTE
    lfStrikeOut: _type.BYTE
    lfCharSet: _type.BYTE
    lfOutPrecision: _type.BYTE
    lfClipPrecision: _type.BYTE
    lfQuality: _type.BYTE
    lfPitchAndFamily: _type.BYTE
    lfFaceName: _type.WCHAR * _const.LF_FACESIZE


@_struct
class MARGINS:
    cxLeftWidth: _type.c_int
    cxRightWidth: _type.c_int
    cyTopHeight: _type.c_int
    cyBottomHeight: _type.c_int


@_struct
class INTLIST:
    iValueCount: _type.c_int
    iValues: _type.c_int * _const.MAX_INTLIST_COUNT


# noinspection PyPep8Naming
@_struct
class WTA_OPTIONS:
    dwFlags: _type.DWORD
    dwMask: _type.DWORD


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
    style: _type.DWORD
    dwExtendedStyle: _type.DWORD
    cdit: _type.WORD
    x: _type.c_short
    y: _type.c_short
    cx: _type.c_short
    cy: _type.c_short


@_struct
class DLGITEMTEMPLATE:
    style: _type.DWORD
    dwExtendedStyle: _type.DWORD
    x: _type.c_short
    y: _type.c_short
    cx: _type.c_short
    id: _type.WORD


@_struct
class STATSTG:
    pwcsName: _type.LPOLESTR
    type: _type.DWORD
    cbSize: _union.ULARGE_INTEGER
    mtime: FILETIME
    ctime: FILETIME
    atime: FILETIME
    grfMode: _type.DWORD
    grfLocksSupported: _type.DWORD
    clsid: CLSID
    grfStateBits: _type.DWORD
    reserved: _type.DWORD


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
    pt: POINT
    flags: _type.UINT
    iBand: _type.c_int


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
    wYear: _type.WORD
    wMonth: _type.WORD
    wDayOfWeek: _type.WORD
    wDay: _type.WORD
    wHour: _type.WORD
    wMinute: _type.WORD
    wSecond: _type.WORD
    wMilliseconds: _type.WORD


# noinspection PyPep8Naming
@_struct
class TIME_ZONE_INFORMATION:
    Bias: _type.LONG
    StandardName: _type.WCHAR * 32
    StandardDate: SYSTEMTIME
    StandardBias: _type.LONG
    DaylightName: _type.WCHAR * 32
    DaylightDate: SYSTEMTIME
    DaylightBias: _type.LONG


# noinspection PyPep8Naming
@_struct
class DYNAMIC_TIME_ZONE_INFORMATION:
    Bias: _type.LONG
    StandardName: _type.WCHAR * 32
    StandardDate: SYSTEMTIME
    StandardBias: _type.LONG
    DaylightName: _type.WCHAR * 32
    DaylightDate: SYSTEMTIME
    DaylightBias: _type.LONG
    TimeZoneKeyName: _type.WCHAR * 128
    DynamicDaylightTimeDisabled: _type.BOOLEAN


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
    info1: DLLVERSIONINFO
    dwFlags: _type.DWORD
    ullVersion: _type.ULONGLONG


# noinspection PyPep8Naming
@_struct
class SYSTEM_POWER_STATUS:
    ACLineStatus: _type.BYTE
    BatteryFlag: _type.BYTE
    BatteryLifePercent: _type.BYTE
    Reserved1: _type.BYTE
    BatteryLifeTime: _type.DWORD
    BatteryFullLifeTime: _type.DWORD


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
    LowPart: _type.DWORD
    HighPart: _type.LONG


# noinspection PyPep8Naming
@_struct
class ULARGE_INTEGER_S:
    LowPart: _type.DWORD
    HighPart: _type.DWORD


# noinspection PyPep8Naming
@_struct
class DISK_SPACE_INFORMATION:
    ActualTotalAllocationUnits: _type.ULONGLONG
    ActualAvailableAllocationUnits: _type.ULONGLONG
    ActualPoolUnavailableAllocationUnits: _type.ULONGLONG
    CallerTotalAllocationUnits: _type.ULONGLONG
    CallerAvailableAllocationUnits: _type.ULONGLONG
    CallerPoolUnavailableAllocationUnits: _type.ULONGLONG
    UsedAllocationUnits: _type.ULONGLONG
    TotalReservedAllocationUnits: _type.ULONGLONG
    VolumeStorageReserveAllocationUnits: _type.ULONGLONG
    AvailableCommittedAllocationUnits: _type.ULONGLONG
    PoolAvailableAllocationUnits: _type.ULONGLONG
    SectorsPerAllocationUnit: _type.DWORD
    BytesPerSector: _type.DWORD


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
    LowPart: _type.DWORD
    HighPart: _type.LONG


@_struct
class BSMINFO:
    cbSize: _type.DWORD = _SIZE
    hDesk: _type.HDESK = None
    hwnd: _type.HWND = None
    luid: LUID = None


# noinspection PyPep8Naming
@_struct
class INPUT_MESSAGE_SOURCE:
    deviceType: _enum.INPUT_MESSAGE_DEVICE_TYPE
    originId: _enum.INPUT_MESSAGE_ORIGIN_ID


# noinspection PyPep8Naming
@_struct
class SECURITY_ATTRIBUTES:
    nLength: _type.DWORD = _SIZE
    lpSecurityDescriptor: _type.LPVOID = None
    bInheritHandle: _type.BOOL = None


@_struct
class EMR:
    iType: _type.DWORD
    nSize: _type.DWORD


@_struct
class LOGPEN:
    lopnStyle: _type.UINT
    lopnWidth: POINT
    lopnColor: _type.COLORREF


@_struct
class EXTLOGPEN:
    elpPenStyle: _type.DWORD
    elpWidth: _type.DWORD
    elpBrushStyle: _type.UINT
    elpColor: _type.COLORREF
    elpHatch: _type.ULONG_PTR
    elpNumEntries: _type.DWORD
    elpStyleEntry: _type.DWORD * 1


@_struct
class LOGBRUSH:
    lbStyle: _type.UINT
    lbColor: _type.COLORREF
    lbHatch: _type.ULONG_PTR


@_struct
class LOGBRUSH32:
    lbStyle: _type.UINT
    lbColor: _type.COLORREF
    lbHatch: _type.ULONG


# noinspection PyPep8Naming
@_struct
class COMPATIBILITY_CONTEXT_ELEMENT:
    Id: GUID
    Type: _enum.ACTCTX_COMPATIBILITY_ELEMENT_TYPE
    MaxVersionTested: _type.ULONGLONG


# noinspection PyPep8Naming
@_struct
class ACTIVATION_CONTEXT_COMPATIBILITY_INFORMATION:
    ElementCount: _type.DWORD
    # noinspection PyTypeChecker
    Elements: COMPATIBILITY_CONTEXT_ELEMENT * 0


# noinspection PyPep8Naming
@_struct
class SUPPORTED_OS_INFO:
    MajorVersion: _type.WORD
    MinorVersion: _type.WORD


# noinspection PyPep8Naming
@_struct
class MAXVERSIONTESTED_INFO:
    MaxVersionTested: _type.ULONGLONG


# noinspection PyPep8Naming
@_struct
class ACTIVATION_CONTEXT_DETAILED_INFORMATION:
    dwFlags: _type.DWORD
    ulFormatVersion: _type.DWORD
    ulAssemblyCount: _type.DWORD
    ulRootManifestPathType: _type.DWORD
    ulRootManifestPathChars: _type.DWORD
    ulRootConfigurationPathType: _type.DWORD
    ulRootConfigurationPathChars: _type.DWORD
    ulAppDirPathType: _type.DWORD
    ulAppDirPathChars: _type.DWORD
    lpRootManifestPath: _type.PCWSTR
    lpRootConfigurationPath: _type.PCWSTR
    lpAppDirPath: _type.PCWSTR


# noinspection PyPep8Naming
@_struct
class HARDWARE_COUNTER_DATA:
    Type: _enum.HARDWARE_COUNTER_TYPE
    Reserved: _type.DWORD
    Value: _type.DWORD64


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
    ulFlags: _type.DWORD
    ulEncodedAssemblyIdentityLength: _type.DWORD
    ulManifestPathType: _type.DWORD
    ulManifestPathLength: _type.DWORD
    liManifestLastWriteTime: _union.LARGE_INTEGER
    ulPolicyPathType: _type.DWORD
    ulPolicyPathLength: _type.DWORD
    liPolicyLastWriteTime: _union.LARGE_INTEGER
    ulMetadataSatelliteRosterIndex: _type.DWORD
    ulManifestVersionMajor: _type.DWORD
    ulManifestVersionMinor: _type.DWORD
    ulPolicyVersionMajor: _type.DWORD
    ulPolicyVersionMinor: _type.DWORD
    ulAssemblyDirectoryNameLength: _type.DWORD
    lpAssemblyEncodedAssemblyIdentity: _type.PCWSTR
    lpAssemblyManifestPath: _type.PCWSTR
    lpAssemblyPolicyPath: _type.PCWSTR
    lpAssemblyDirectoryName: _type.PCWSTR


# noinspection PyPep8Naming
@_struct
class ACTIVATION_CONTEXT_RUN_LEVEL_INFORMATION:
    ulFlags: _type.DWORD
    RunLevel: _enum.ACTCTX_REQUESTED_RUN_LEVEL
    UiAccess: _type.DWORD


# noinspection PyPep8Naming
@_struct
class ASSEMBLY_FILE_DETAILED_INFORMATION:
    ulFlags: _type.DWORD
    ulFilenameLength: _type.DWORD
    ulPathLength: _type.DWORD
    lpFileName: _type.PCWSTR
    lpFilePath: _type.PCWSTR


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
    hMem: _type.HANDLE
    dwReserved: _type.DWORD * 3


# noinspection PyPep8Naming
@_struct
class PROCESS_HEAP_ENTRY_U_S2:
    dwCommittedSize: _type.DWORD
    dwUnCommittedSize: _type.DWORD
    lpFirstBlock: _type.LPVOID
    lpLastBlock: _type.LPVOID


# noinspection PyPep8Naming
@_struct
class PROCESS_HEAP_ENTRY:
    lpData: _type.PVOID
    cbData: _type.DWORD
    cbOverhead: _type.BYTE
    iRegionIndex: _type.BYTE
    wFlags: _type.WORD
    U: _union.PROCESS_HEAP_ENTRY_U


# noinspection PyPep8Naming
@_struct
class IMAGE_SECTION_HEADER:
    Name: _type.BYTE * _const.IMAGE_SIZEOF_SHORT_NAME
    Misc: _union.IMAGE_SECTION_HEADER_U
    VirtualAddress: _type.DWORD
    SizeOfRawData: _type.DWORD
    PointerToRawData: _type.DWORD
    PointerToRelocations: _type.DWORD
    PointerToLinenumbers: _type.DWORD
    NumberOfRelocations: _type.WORD
    NumberOfLinenumbers: _type.WORD
    Characteristics: _type.DWORD


# noinspection PyPep8Naming
@_struct
class IMAGE_DOS_HEADER:
    e_magic: _type.WORD
    e_cblp: _type.WORD
    e_cp: _type.WORD
    e_crlc: _type.WORD
    e_cparhdr: _type.WORD
    e_minalloc: _type.WORD
    e_maxalloc: _type.WORD
    e_ss: _type.WORD
    e_sp: _type.WORD
    e_csum: _type.WORD
    e_ip: _type.WORD
    e_cs: _type.WORD
    e_lfarlc: _type.WORD
    e_ovno: _type.WORD
    e_res: _type.WORD * 4
    e_oemid: _type.WORD
    e_oeminfo: _type.WORD
    e_res2: _type.WORD * 10
    e_lfanew: _type.LONG


# noinspection PyPep8Naming
@_struct
class IMAGE_OS2_HEADER:
    ne_magic: _type.WORD
    ne_ver: _type.CHAR
    ne_rev: _type.CHAR
    ne_enttab: _type.WORD
    ne_cbenttab: _type.WORD
    ne_crc: _type.LONG
    ne_flags: _type.WORD
    ne_autodata: _type.WORD
    ne_heap: _type.WORD
    ne_stack: _type.WORD
    ne_csip: _type.LONG
    ne_sssp: _type.LONG
    ne_cseg: _type.WORD
    ne_cmod: _type.WORD
    ne_cbnrestab: _type.WORD
    ne_segtab: _type.WORD
    ne_rsrctab: _type.WORD
    ne_restab: _type.WORD
    ne_modtab: _type.WORD
    ne_imptab: _type.WORD
    ne_nrestab: _type.LONG
    ne_cmovent: _type.WORD
    ne_align: _type.WORD
    ne_cres: _type.WORD
    ne_exetyp: _type.BYTE
    ne_flagsothers: _type.BYTE
    ne_pretthunks: _type.WORD
    ne_psegrefbytes: _type.WORD
    ne_swaparea: _type.WORD
    ne_expver: _type.WORD


# noinspection PyPep8Naming
@_struct
class IMAGE_VXD_HEADER:
    e32_magic: _type.WORD
    e32_border: _type.BYTE
    e32_worder: _type.BYTE
    e32_level: _type.DWORD
    e32_cpu: _type.WORD
    e32_os: _type.WORD
    e32_ver: _type.DWORD
    e32_mflags: _type.DWORD
    e32_mpages: _type.DWORD
    e32_startobj: _type.DWORD
    e32_eip: _type.DWORD
    e32_stackobj: _type.DWORD
    e32_esp: _type.DWORD
    e32_pagesize: _type.DWORD
    e32_lastpagesize: _type.DWORD
    e32_fixupsize: _type.DWORD
    e32_fixupsum: _type.DWORD
    e32_ldrsize: _type.DWORD
    e32_ldrsum: _type.DWORD
    e32_objtab: _type.DWORD
    e32_objcnt: _type.DWORD
    e32_objmap: _type.DWORD
    e32_itermap: _type.DWORD
    e32_rsrctab: _type.DWORD
    e32_rsrccnt: _type.DWORD
    e32_restab: _type.DWORD
    e32_enttab: _type.DWORD
    e32_dirtab: _type.DWORD
    e32_dircnt: _type.DWORD
    e32_fpagetab: _type.DWORD
    e32_frectab: _type.DWORD
    e32_impmod: _type.DWORD
    e32_impmodcnt: _type.DWORD
    e32_impproc: _type.DWORD
    e32_pagesum: _type.DWORD
    e32_datapage: _type.DWORD
    e32_preload: _type.DWORD
    e32_nrestab: _type.DWORD
    e32_cbnrestab: _type.DWORD
    e32_nressum: _type.DWORD
    e32_autodata: _type.DWORD
    e32_debuginfo: _type.DWORD
    e32_debuglen: _type.DWORD
    e32_instpreload: _type.DWORD
    e32_instdemand: _type.DWORD
    e32_heapsize: _type.DWORD
    e32_res3: _type.BYTE * 12
    e32_winresoff: _type.DWORD
    e32_winreslen: _type.DWORD
    e32_devid: _type.WORD
    e32_ddkver: _type.WORD


# noinspection PyPep8Naming
@_struct
class IMAGE_FILE_HEADER:
    Machine: _type.WORD
    NumberOfSections: _type.WORD
    TimeDateStamp: _type.DWORD
    PointerToSymbolTable: _type.DWORD
    NumberOfSymbols: _type.DWORD
    SizeOfOptionalHeader: _type.WORD
    Characteristics: _type.WORD


# noinspection PyPep8Naming
@_struct
class IMAGE_DATA_DIRECTORY:
    VirtualAddress: _type.DWORD
    Size: _type.DWORD


# noinspection PyPep8Naming
@_struct
class IMAGE_OPTIONAL_HEADER32:
    Magic: _type.WORD
    MajorLinkerVersion: _type.BYTE
    MinorLinkerVersion: _type.BYTE
    SizeOfCode: _type.DWORD
    SizeOfInitializedData: _type.DWORD
    SizeOfUninitializedData: _type.DWORD
    AddressOfEntryPoint: _type.DWORD
    BaseOfCode: _type.DWORD
    BaseOfData: _type.DWORD
    ImageBase: _type.DWORD
    SectionAlignment: _type.DWORD
    FileAlignment: _type.DWORD
    MajorOperatingSystemVersion: _type.WORD
    MinorOperatingSystemVersion: _type.WORD
    MajorImageVersion: _type.WORD
    MinorImageVersion: _type.WORD
    MajorSubsystemVersion: _type.WORD
    MinorSubsystemVersion: _type.WORD
    Win32VersionValue: _type.DWORD
    SizeOfImage: _type.DWORD
    SizeOfHeaders: _type.DWORD
    CheckSum: _type.DWORD
    Subsystem: _type.WORD
    DllCharacteristics: _type.WORD
    SizeOfStackReserve: _type.DWORD
    SizeOfStackCommit: _type.DWORD
    SizeOfHeapReserve: _type.DWORD
    SizeOfHeapCommit: _type.DWORD
    LoaderFlags: _type.DWORD
    NumberOfRvaAndSizes: _type.DWORD
    # noinspection PyUnresolvedReferences
    DataDirectory: IMAGE_DATA_DIRECTORY * _const.IMAGE_NUMBEROF_DIRECTORY_ENTRIES


# noinspection PyPep8Naming
@_struct
class IMAGE_OPTIONAL_HEADER64:
    Magic: _type.WORD
    MajorLinkerVersion: _type.BYTE
    MinorLinkerVersion: _type.BYTE
    SizeOfCode: _type.DWORD
    SizeOfInitializedData: _type.DWORD
    SizeOfUninitializedData: _type.DWORD
    AddressOfEntryPoint: _type.DWORD
    BaseOfCode: _type.DWORD
    ImageBase: _type.ULONGLONG
    SectionAlignment: _type.DWORD
    FileAlignment: _type.DWORD
    MajorOperatingSystemVersion: _type.WORD
    MinorOperatingSystemVersion: _type.WORD
    MajorImageVersion: _type.WORD
    MinorImageVersion: _type.WORD
    MajorSubsystemVersion: _type.WORD
    MinorSubsystemVersion: _type.WORD
    Win32VersionValue: _type.DWORD
    SizeOfImage: _type.DWORD
    SizeOfHeaders: _type.DWORD
    CheckSum: _type.DWORD
    Subsystem: _type.WORD
    DllCharacteristics: _type.WORD
    SizeOfStackReserve: _type.ULONGLONG
    SizeOfStackCommit: _type.ULONGLONG
    SizeOfHeapReserve: _type.ULONGLONG
    SizeOfHeapCommit: _type.ULONGLONG
    LoaderFlags: _type.DWORD
    NumberOfRvaAndSizes: _type.DWORD
    # noinspection PyUnresolvedReferences
    DataDirectory: IMAGE_DATA_DIRECTORY * _const.IMAGE_NUMBEROF_DIRECTORY_ENTRIES


# noinspection PyPep8Naming
@_struct
class IMAGE_ROM_OPTIONAL_HEADER:
    Magic: _type.WORD
    MajorLinkerVersion: _type.BYTE
    MinorLinkerVersion: _type.BYTE
    SizeOfCode: _type.DWORD
    SizeOfInitializedData: _type.DWORD
    SizeOfUninitializedData: _type.DWORD
    AddressOfEntryPoint: _type.DWORD
    BaseOfCode: _type.DWORD
    BaseOfData: _type.DWORD
    BaseOfBss: _type.DWORD
    GprMask: _type.DWORD
    CprMask: _type.DWORD * 4
    GpValue: _type.DWORD


# noinspection PyPep8Naming
@_struct
class IMAGE_NT_HEADERS32:
    Signature: _type.DWORD
    FileHeader: IMAGE_FILE_HEADER
    OptionalHeader: IMAGE_OPTIONAL_HEADER32


# noinspection PyPep8Naming
@_struct
class IMAGE_NT_HEADERS64:
    Signature: _type.DWORD
    FileHeader: IMAGE_FILE_HEADER
    OptionalHeader: IMAGE_OPTIONAL_HEADER64


# noinspection PyPep8Naming
@_struct
class IMAGE_ROM_HEADERS:
    FileHeader: IMAGE_FILE_HEADER
    OptionalHeader: IMAGE_ROM_OPTIONAL_HEADER


# noinspection PyPep8Naming
@_struct
class SECURITY_ATTRIBUTES:
    nLength: _type.DWORD
    lpSecurityDescriptor: _type.LPVOID
    bInheritHandle: _type.BOOL


# noinspection PyPep8Naming
@_struct
class OVERLAPPED_U_S:
    Offset: _type.DWORD
    OffsetHigh: _type.DWORD


@_struct
class OVERLAPPED:
    Internal: _type.ULONG_PTR
    InternalHigh: _type.ULONG_PTR
    U: _union.OVERLAPPED_U
    hEvent: _type.HANDLE


# noinspection PyPep8Naming
@_struct
class OVERLAPPED_ENTRY:
    lpCompletionKey: _type.ULONG_PTR
    lpOverlapped: _Pointer[OVERLAPPED]
    Internal: _type.ULONG_PTR
    dwNumberOfBytesTransferred: _type.DWORD


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
    dwFlags: _type.DWORD
    fEnable: _type.BOOL
    hRgnBlur: _type.HRGN
    fTransitionOnMaximized: _type.BOOL


# noinspection PyPep8Naming
@_struct
class PACKAGE_VERSION_U_S:
    Revision: _type.USHORT
    Build: _type.USHORT
    Minor: _type.USHORT
    Major: _type.USHORT


# noinspection PyPep8Naming
@_struct
class PACKAGE_VERSION:
    U: _union.PACKAGE_VERSION_U


# noinspection PyPep8Naming
@_struct
class PACKAGE_ID:
    reserved: _type.UINT32
    processorArchitecture: _type.UINT32
    version: PACKAGE_VERSION
    name: _type.PWSTR
    publisher: _type.PWSTR
    resourceId: _type.PWSTR
    publisherId: _type.PWSTR


@_struct
class MARGINS:
    cxLeftWidth: _type.c_int
    cxRightWidth: _type.c_int
    cyTopHeight: _type.c_int
    cyBottomHeight: _type.c_int


@_struct
class TrackerHandle:
    unused: _type.c_int


@_struct
class LUID:
    LowPart: _type.DWORD
    HighPart: _type.LONG


@_struct
class ACL:
    AclRevision: _type.BYTE
    Sbz1: _type.BYTE
    AclSize: _type.WORD
    AceCount: _type.WORD
    Sbz2: _type.WORD


@_struct
class SAFEARRAYBOUND:
    cElements: _type.ULONG
    lLbound: _type.LONG


@_struct
class SAFEARRAY:
    cDims: _type.USHORT
    fFeatures: _type.USHORT
    cbElements: _type.ULONG
    cLocks: _type.ULONG
    pvData: _type.PVOID
    # noinspection PyTypeChecker
    rgsabound: SAFEARRAYBOUND * 1


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_RATIONAL:
    Numerator: _type.DWORD
    Denominator: _type.DWORD


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_2DREGION:
    cx: _type.DWORD
    cy: _type.DWORD


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_PATH_SOURCE_INFO_U_S:
    cloneGroupId: _bitfield(_type.UINT32, 16)
    sourceModeInfoIdx: _bitfield(_type.UINT32, 16)


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_PATH_SOURCE_INFO:
    adapterId: LUID
    id: _type.UINT32
    U: _union.DISPLAYCONFIG_PATH_SOURCE_INFO_U
    statusFlags: _type.UINT32


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_PATH_TARGET_INFO_U_S:
    desktopModeInfoIdx: _bitfield(_type.UINT32, 16)
    targetModeInfoIdx: _bitfield(_type.UINT32, 16)


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_PATH_TARGET_INFO:
    adapterId: LUID
    id: _type.UINT32
    U: _union.DISPLAYCONFIG_PATH_TARGET_INFO_U
    outputTechnology: _enum.DISPLAYCONFIG_VIDEO_OUTPUT_TECHNOLOGY
    rotation: _enum.DISPLAYCONFIG_ROTATION
    scaling: _enum.DISPLAYCONFIG_SCALING
    refreshRate: DISPLAYCONFIG_RATIONAL
    scanLineOrdering: _enum.DISPLAYCONFIG_SCANLINE_ORDERING
    targetAvailable: _type.BOOL
    statusFlags: _type.UINT32


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_PATH_INFO:
    sourceInfo: DISPLAYCONFIG_PATH_SOURCE_INFO
    targetInfo: DISPLAYCONFIG_PATH_TARGET_INFO
    flags: _type.UINT32


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_SOURCE_MODE:
    width: _type.UINT32
    height: _type.UINT32
    pixelFormat: _enum.DISPLAYCONFIG_PIXELFORMAT
    position: POINTL


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_VIDEO_SIGNAL_INFO_U_S:
    videoStandard: _bitfield(_type.UINT32, 16)
    vSyncFreqDivider: _bitfield(_type.UINT32, 6)
    reserved: _bitfield(_type.UINT32, 10)


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_VIDEO_SIGNAL_INFO:
    pixelRate: _type.UINT64
    hSyncFreq: DISPLAYCONFIG_RATIONAL
    vSyncFreq: DISPLAYCONFIG_RATIONAL
    activeSize: DISPLAYCONFIG_2DREGION
    totalSize: DISPLAYCONFIG_2DREGION
    U: _union.DISPLAYCONFIG_VIDEO_SIGNAL_INFO_U
    scanLineOrdering: _enum.DISPLAYCONFIG_SCANLINE_ORDERING


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_TARGET_MODE:
    targetVideoSignalInfo: DISPLAYCONFIG_VIDEO_SIGNAL_INFO


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_DESKTOP_IMAGE_INFO:
    PathSourceSize: POINTL
    DesktopImageRegion: RECTL
    DesktopImageClip: RECTL


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_MODE_INFO:
    infoType: _enum.DISPLAYCONFIG_MODE_INFO_TYPE
    id: _type.UINT32
    adapterId: LUID
    U: _union.DISPLAYCONFIG_MODE_INFO_U


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_DEVICE_INFO_HEADER:
    type: _enum.DISPLAYCONFIG_DEVICE_INFO_TYPE
    size: _type.UINT32
    adapterId: LUID
    id: _type.UINT32


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_SOURCE_DEVICE_NAME:
    header: DISPLAYCONFIG_DEVICE_INFO_HEADER
    viewGdiDeviceName: _type.WCHAR * _const.CCHDEVICENAME


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_TARGET_DEVICE_NAME_FLAGS_U_S:
    friendlyNameFromEdid: _bitfield(_type.UINT32, 1)
    friendlyNameForced: _bitfield(_type.UINT32, 1)
    edidIdsValid: _bitfield(_type.UINT32, 1)
    reserved: _bitfield(_type.UINT32, 29)


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_TARGET_DEVICE_NAME_FLAGS:
    U: _union.DISPLAYCONFIG_TARGET_DEVICE_NAME_FLAGS_U


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_TARGET_DEVICE_NAME:
    header: DISPLAYCONFIG_DEVICE_INFO_HEADER
    flags: DISPLAYCONFIG_TARGET_DEVICE_NAME_FLAGS
    outputTechnology: _enum.DISPLAYCONFIG_VIDEO_OUTPUT_TECHNOLOGY
    edidManufactureId: _type.UINT16
    edidProductCodeId: _type.UINT16
    connectorInstance: _type.UINT32
    monitorFriendlyDeviceName: _type.WCHAR * 64
    monitorDevicePath: _type.WCHAR * 128


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_TARGET_PREFERRED_MODE:
    header: DISPLAYCONFIG_DEVICE_INFO_HEADER
    width: _type.UINT32
    height: _type.UINT32
    targetMode: DISPLAYCONFIG_TARGET_MODE


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_ADAPTER_NAME:
    header: DISPLAYCONFIG_DEVICE_INFO_HEADER
    adapterDevicePath: _type.WCHAR * 128


# noinspection PyPep8Naming
@_struct
class DISPLAYCONFIG_TARGET_BASE_TYPE:
    header: DISPLAYCONFIG_DEVICE_INFO_HEADER
    baseOutputTechnology: _enum.DISPLAYCONFIG_VIDEO_OUTPUT_TECHNOLOGY


# noinspection PyPep8Naming
@_struct
class D2D1_PIXEL_FORMAT:
    format: _enum.DXGI_FORMAT
    alphaMode: _enum.D2D1_ALPHA_MODE


# noinspection PyPep8Naming
@_struct
class D2D_POINT_2U:
    x: _type.UINT32
    y: _type.UINT32


# noinspection PyPep8Naming
@_struct
class D2D_POINT_2F:
    x: _type.FLOAT
    y: _type.FLOAT


# noinspection PyPep8Naming
@_struct
class D2D_VECTOR_2F:
    x: _type.FLOAT
    y: _type.FLOAT


# noinspection PyPep8Naming
@_struct
class D2D_VECTOR_3F:
    x: _type.FLOAT
    y: _type.FLOAT
    z: _type.FLOAT


# noinspection PyPep8Naming
@_struct
class D2D_VECTOR_4F:
    x: _type.FLOAT
    y: _type.FLOAT
    z: _type.FLOAT
    w: _type.FLOAT


# noinspection PyPep8Naming
@_struct
class D2D_RECT_F:
    left: _type.FLOAT
    top: _type.FLOAT
    right: _type.FLOAT
    bottom: _type.FLOAT


# noinspection PyPep8Naming
@_struct
class D2D_RECT_U:
    left: _type.UINT32
    top: _type.UINT32
    right: _type.UINT32
    bottom: _type.UINT32


# noinspection PyPep8Naming
@_struct
class D2D_SIZE_F:
    width: _type.FLOAT
    height: _type.FLOAT


# noinspection PyPep8Naming
@_struct
class D2D_SIZE_U:
    width: _type.UINT32
    height: _type.UINT32


# noinspection PyPep8Naming
@_struct
class D2D_MATRIX_3X2_F_U_S:
    m11: _type.FLOAT
    m12: _type.FLOAT
    m21: _type.FLOAT
    m22: _type.FLOAT
    dx: _type.FLOAT
    dy: _type.FLOAT


# noinspection PyPep8Naming
@_struct
class D2D_MATRIX_3X2_F_U_S2:
    _11: _type.FLOAT
    _12: _type.FLOAT
    _21: _type.FLOAT
    _22: _type.FLOAT
    _31: _type.FLOAT
    _32: _type.FLOAT


# noinspection PyPep8Naming
@_struct
class D2D_MATRIX_3X2_F:
    U: _union.D2D_MATRIX_3X2_F_U


# noinspection PyPep8Naming
@_struct
class D2D_MATRIX_4X3_F_U_S:
    _11: _type.FLOAT
    _12: _type.FLOAT
    _13: _type.FLOAT
    _21: _type.FLOAT
    _22: _type.FLOAT
    _23: _type.FLOAT
    _31: _type.FLOAT
    _32: _type.FLOAT
    _33: _type.FLOAT
    _41: _type.FLOAT
    _42: _type.FLOAT
    _43: _type.FLOAT


# noinspection PyPep8Naming
@_struct
class D2D_MATRIX_4X3_F:
    U: _union.D2D_MATRIX_4X3_F_U


# noinspection PyPep8Naming
@_struct
class D2D_MATRIX_4X4_F_U_S:
    _11: _type.FLOAT
    _12: _type.FLOAT
    _13: _type.FLOAT
    _14: _type.FLOAT
    _21: _type.FLOAT
    _22: _type.FLOAT
    _23: _type.FLOAT
    _24: _type.FLOAT
    _31: _type.FLOAT
    _32: _type.FLOAT
    _33: _type.FLOAT
    _34: _type.FLOAT
    _41: _type.FLOAT
    _42: _type.FLOAT
    _43: _type.FLOAT
    _44: _type.FLOAT


# noinspection PyPep8Naming
@_struct
class D2D_MATRIX_4X4_F:
    U: _union.D2D_MATRIX_4X4_F_U


# noinspection PyPep8Naming
@_struct
class D2D_MATRIX_5X4_F_U_S:
    _11: _type.FLOAT
    _12: _type.FLOAT
    _13: _type.FLOAT
    _14: _type.FLOAT
    _21: _type.FLOAT
    _22: _type.FLOAT
    _23: _type.FLOAT
    _24: _type.FLOAT
    _31: _type.FLOAT
    _32: _type.FLOAT
    _33: _type.FLOAT
    _34: _type.FLOAT
    _41: _type.FLOAT
    _42: _type.FLOAT
    _43: _type.FLOAT
    _44: _type.FLOAT
    _51: _type.FLOAT
    _52: _type.FLOAT
    _53: _type.FLOAT
    _54: _type.FLOAT


# noinspection PyPep8Naming
@_struct
class DXGI_RATIONAL:
    Numerator: _type.UINT
    Denominator: _type.UINT


# noinspection PyPep8Naming
@_struct
class DXGI_SAMPLE_DESC:
    Count: _type.UINT
    Quality: _type.UINT


# noinspection PyPep8Naming
@_struct
class D2D_MATRIX_5X4_F:
    U: _union.D2D_MATRIX_5X4_F_U


# noinspection PyPep8Naming
@_struct
class DXGI_RGB:
    Red: _type.c_float
    Green: _type.c_float
    Blue: _type.c_float


@_struct
class D3DCOLORVALUE:
    r: _type.c_float
    g: _type.c_float
    b: _type.c_float
    a: _type.c_float


# noinspection PyPep8Naming
@_struct
class DXGI_GAMMA_CONTROL:
    Scale: DXGI_RGB
    Offset: DXGI_RGB
    # noinspection PyTypeChecker
    GammaCurve: DXGI_RGB * 1025


# noinspection PyPep8Naming
@_struct
class DXGI_MODE_DESC:
    Width: _type.UINT
    Height: _type.UINT
    RefreshRate: DXGI_RATIONAL
    Format: _enum.DXGI_FORMAT
    ScanlineOrdering: _enum.DXGI_MODE_SCANLINE_ORDER
    Scaling: _enum.DXGI_MODE_SCALING


# noinspection PyPep8Naming
@_struct
class DXGI_JPEG_DC_HUFFMAN_TABLE:
    CodeCounts: _type.BYTE * 12
    CodeValues: _type.BYTE * 12


# noinspection PyPep8Naming
@_struct
class DXGI_JPEG_AC_HUFFMAN_TABLE:
    CodeCounts: _type.BYTE * 16
    CodeValues: _type.BYTE * 162


# noinspection PyPep8Naming
@_struct
class DXGI_JPEG_QUANTIZATION_TABLE:
    Elements: _type.BYTE * 64


# noinspection PyPep8Naming
@_struct
class DXGI_GAMMA_CONTROL_CAPABILITIES:
    ScaleAndOffsetSupported: _type.BOOL
    MaxConvertedValue: _type.c_float
    MinConvertedValue: _type.c_float
    NumGammaControlPoints: _type.UINT
    ControlPointPositions: _type.c_float * 1025


# noinspection PyPep8Naming
@_struct
class D2D1_BITMAP_PROPERTIES:
    pixelFormat: D2D1_PIXEL_FORMAT
    dpiX: _type.FLOAT
    dpiY: _type.FLOAT


# noinspection PyPep8Naming
@_struct
class D2D1_GRADIENT_STOP:
    position: _type.FLOAT
    color: D2D1_COLOR_F


# noinspection PyPep8Naming
@_struct
class D2D1_BRUSH_PROPERTIES:
    opacity: _type.FLOAT
    transform: D2D1_MATRIX_3X2_F


# noinspection PyPep8Naming
@_struct
class D2D1_BITMAP_BRUSH_PROPERTIES:
    extendModeX: _enum.D2D1_EXTEND_MODE
    extendModeY: _enum.D2D1_EXTEND_MODE
    interpolationMode: _enum.D2D1_BITMAP_INTERPOLATION_MODE


# noinspection PyPep8Naming
@_struct
class D2D1_LINEAR_GRADIENT_BRUSH_PROPERTIES:
    startPoint: D2D1_POINT_2F
    endPoint: D2D1_POINT_2F


# noinspection PyPep8Naming
@_struct
class D2D1_RADIAL_GRADIENT_BRUSH_PROPERTIES:
    center: D2D1_POINT_2F
    gradientOriginOffset: D2D1_POINT_2F
    radiusX: _type.FLOAT
    radiusY: _type.FLOAT


# noinspection PyPep8Naming
@_struct
class D2D1_FACTORY_OPTIONS:
    debugLevel: _enum.D2D1_DEBUG_LEVEL


# noinspection PyPep8Naming
@_struct
class D2D1_RENDER_TARGET_PROPERTIES:
    type: _enum.D2D1_RENDER_TARGET_TYPE
    pixelFormat: D2D1_PIXEL_FORMAT
    dpiX: _type.FLOAT
    dpiY: _type.FLOAT
    usage: _enum.D2D1_RENDER_TARGET_USAGE
    minLevel: _enum.D2D1_FEATURE_LEVEL


# noinspection PyPep8Naming
@_struct
class D2D1_HWND_RENDER_TARGET_PROPERTIES:
    hwnd: _type.HWND
    pixelSize: D2D1_SIZE_U
    presentOptions: _enum.D2D1_PRESENT_OPTIONS


# noinspection PyPep8Naming
@_struct
class D2D1_CREATION_PROPERTIES:
    threadingMode: _enum.D2D1_THREADING_MODE
    debugLevel: _enum.D2D1_DEBUG_LEVEL
    options: _enum.D2D1_DEVICE_CONTEXT_OPTIONS


# noinspection PyPep8Naming
@_struct
class D2D1_SVG_VIEWBOX:
    x: _type.FLOAT
    y: _type.FLOAT
    width: _type.FLOAT
    height: _type.FLOAT


# noinspection PyPep8Naming
@_struct
class D2D1_STROKE_STYLE_PROPERTIES:
    startCap: _enum.D2D1_CAP_STYLE
    endCap: _enum.D2D1_CAP_STYLE
    dashCap: _enum.D2D1_CAP_STYLE
    lineJoin: _enum.D2D1_LINE_JOIN
    miterLimit: _type.FLOAT
    dashStyle: _enum.D2D1_DASH_STYLE
    dashOffset: _type.FLOAT


# noinspection PyPep8Naming
@_struct
class D2D1_ELLIPSE:
    point: D2D1_POINT_2F
    radiusX: _type.FLOAT
    radiusY: _type.FLOAT


# noinspection PyPep8Naming
@_struct
class D2D1_ROUNDED_RECT:
    rect: D2D1_RECT_F
    radiusX: _type.FLOAT
    radiusY: _type.FLOAT


# noinspection PyPep8Naming
@_struct
class D2D1_DRAWING_STATE_DESCRIPTION:
    antialiasMode: _enum.D2D1_ANTIALIAS_MODE
    textAntialiasMode: _enum.D2D1_TEXT_ANTIALIAS_MODE
    tag1: _type.D2D1_TAG
    tag2: _type.D2D1_TAG
    transform: D2D1_MATRIX_3X2_F


# noinspection PyPep8Naming
@_struct
class D2D1_LAYER_PARAMETERS:
    contentBounds: D2D1_RECT_F
    geometricMask: _type.ID2D1Geometry
    maskAntialiasMode: _enum.D2D1_ANTIALIAS_MODE
    maskTransform: D2D1_MATRIX_3X2_F
    opacity: _type.FLOAT
    opacityBrush: _type.ID2D1Brush
    layerOptions: _enum.D2D1_LAYER_OPTIONS


# noinspection PyPep8Naming
@_struct
class DWRITE_FONT_METRICS:
    designUnitsPerEm: _type.UINT16
    ascent: _type.UINT16
    descent: _type.UINT16
    lineGap: _type.INT16
    capHeight: _type.UINT16
    xHeight: _type.UINT16
    underlinePosition: _type.INT16
    underlineThickness: _type.UINT16
    strikethroughPosition: _type.INT16
    strikethroughThickness: _type.UINT16


# noinspection PyPep8Naming
@_struct
class DWRITE_GLYPH_METRICS:
    leftSideBearing: _type.INT32
    advanceWidth: _type.UINT32
    rightSideBearing: _type.INT32
    topSideBearing: _type.INT32
    advanceHeight: _type.UINT32
    bottomSideBearing: _type.INT32
    verticalOriginY: _type.INT32


# noinspection PyPep8Naming
@_struct
class DWRITE_GLYPH_OFFSET:
    advanceOffset: _type.FLOAT
    ascenderOffset: _type.FLOAT


# noinspection PyPep8Naming
@_struct
class DWRITE_GLYPH_RUN:
    fontFace: _type.IDWriteFontFace
    fontEmSize: _type.FLOAT
    glyphCount: _type.UINT32
    glyphIndices: _Pointer[_type.UINT16]
    glyphAdvances: _Pointer[_type.FLOAT]
    glyphOffsets: _Pointer[DWRITE_GLYPH_OFFSET]
    isSideways: _type.BOOL
    bidiLevel: _type.UINT32


# noinspection PyPep8Naming
@_struct
class DWRITE_MATRIX:
    m11: _type.FLOAT
    m12: _type.FLOAT
    m21: _type.FLOAT
    m22: _type.FLOAT
    dx: _type.FLOAT
    dy: _type.FLOAT


# noinspection PyPep8Naming
@_struct
class DWRITE_TRIMMING:
    granularity: _enum.DWRITE_TRIMMING_GRANULARITY
    delimiter: _type.UINT32
    delimiterCount: _type.UINT32


# noinspection PyPep8Naming
@_struct
class RO_REGISTRATION_COOKIE:
    pass


@_struct
class WICRect:
    X: _type.INT
    Y: _type.INT
    Width: _type.INT
    Height: _type.INT


@_struct
class PointF:
    X: _type.REAL
    Y: _type.REAL


@_struct
class Point:
    X: _type.INT
    Y: _type.INT


@_struct
class RectF:
    X: _type.REAL
    Y: _type.REAL
    Width: _type.REAL
    Height: _type.REAL


@_struct
class Rect:
    X: _type.INT
    Y: _type.INT
    Width: _type.INT
    Height: _type.INT


@_struct
class SizeF:
    Width: _type.REAL
    Height: _type.REAL


@_struct
class Size:
    Width: _type.INT
    Height: _type.INT


@_struct
class PathData:
    Count: _type.INT
    Points: _Pointer[PointF]
    Types: _Pointer[_type.BYTE]


@_struct
class CharacterRange:
    First: _type.INT
    Length: _type.INT


@_struct
class Color:
    Value: _type.ARGB


@_struct
class ColorMap:
    oldColor: Color
    newColor: Color


@_struct
class ColorPalette:
    Flags: _type.UINT
    Count: _type.UINT
    Entries: _type.ARGB * 1


@_struct
class BitmapData:
    Width: _type.UINT
    Height: _type.UINT
    Stride: _type.INT
    PixelFormat: _type.INT
    Scan0: _type.PVOID
    Reserved: _type.UINT_PTR


@_struct
class EncoderParameter:
    Guid: GUID
    NumberOfValues: _type.ULONG
    Type: _type.ULONG
    Value: _type.PVOID


@_struct
class EncoderParameters:
    Count: _type.UINT
    # noinspection PyTypeChecker
    Parameter: EncoderParameter * 1


@_struct
class ImageCodecInfo:
    Clsid: CLSID
    FormatID: GUID
    CodecName: _type.LPWSTR
    DllName: _type.LPWSTR
    FormatDescription: _type.LPWSTR
    FilenameExtension: _type.LPWSTR
    MimeType: _type.LPWSTR
    Flags: _type.DWORD
    Version: _type.DWORD
    SigCount: _type.DWORD
    SigSize: _type.DWORD
    SigPattern: _Pointer[_type.BYTE]
    SigMask: _Pointer[_type.BYTE]


@_struct
class PropertyItem:
    id: _type.PROPID
    length: _type.ULONG
    type: _type.WORD
    value: _type.PVOID


@_struct
class ImageItemData:
    Size: _type.UINT
    Position: _type.UINT
    Desc: _type.PVOID
    DescSize: _type.UINT
    Data: _Pointer[_type.UINT]
    DataSize: _type.UINT
    Cookie: _type.UINT


@_struct
class METAHEADER:
    mtType: _type.WORD
    mtHeaderSize: _type.WORD
    mtVersion: _type.WORD
    mtSize: _type.DWORD
    mtNoObjects: _type.WORD
    mtMaxRecord: _type.DWORD
    mtNoParameters: _type.WORD


@_struct
class ENHMETAHEADER3:
    iType: _type.DWORD
    nSize: _type.DWORD
    rclBounds: RECTL
    rclFrame: RECTL
    dSignature: _type.DWORD
    nVersion: _type.DWORD
    nBytes: _type.DWORD
    nRecords: _type.DWORD
    nHandles: _type.WORD
    sReserved: _type.WORD
    nDescription: _type.DWORD
    offDescription: _type.DWORD
    nPalEntries: _type.DWORD
    szlDevice: SIZEL
    szlMillimeters: SIZEL


@_struct
class PWMFRect16:
    Left: _type.INT16
    Top: _type.INT16
    Right: _type.INT16
    Bottom: _type.INT16


@_struct
class WmfPlaceableFileHeader:
    Key: _type.UINT32
    Hmf: _type.UINT32
    BoundingBox: PWMFRect16
    Inch: _type.INT16
    Reserved: _type.UINT32
    Checksum: _type.INT16


@_struct
class MetafileHeader:
    Type: _enum.MetafileType
    Size: _type.UINT
    Version: _type.UINT
    EmfPlusFlags: _type.UINT
    DpiX: _type.REAL
    DpiY: _type.REAL
    X: _type.INT
    Y: _type.INT
    Width: _type.INT
    Height: _type.INT
    U: _union.MetafileHeader_U
    EmfPlusHeaderSize: _type.INT
    LogicalDpiX: _type.INT
    LogicalDpiY: _type.INT


POINTL = POINT
RECTL = RECT
SIZEL = SIZE
VARIANTARG = VARIANT
ANSI_STRING = STRING
OEM_STRING = STRING
PATTERN = LOGBRUSH

UUID = GUID
IID = GUID
CATID = GUID
DXGI_DEBUG_ID = GUID
FSRM_OBJECT_ID = GUID
MSPID = GUID
PRODUCTID = GUID
CLSID = GUID
FMTID = GUID
WICPixelFormatGUID = GUID
CLFS_LOG_ID = GUID
DEVPROPGUID = GUID
KNOWNFOLDERID = GUID
SHELLVIEWID = GUID
IPSEC_CRYPTO_MODULE_ID = GUID

GpPointF = PointF
GpPoint = Point
GpRectF = RectF
GpRect = Rect
GpSizeF = SizeF
GpSize = Size
GpPathData = PathData

D2D_COLOR_F = D3DCOLORVALUE
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
D2D1_COLOR_F = D2D_COLOR_F


class Windows:
    class ApplicationModel:
        @_struct
        class PackageInstallProgress:
            PercentComplete: _type.UINT32

        @_struct
        class PackageVersion:
            Major: _type.UINT16
            Minor: _type.UINT16
            Build: _type.UINT16
            Revision: _type.UINT16

        class Resources:
            class Core:
                @_struct
                class ResourceLayoutInfo:
                    MajorVersion: _type.UINT32
                    MinorVersion: _type.UINT32
                    ResourceSubtreeCount: _type.UINT32
                    NamedResourceCount: _type.UINT32
                    Checksum: _type.INT32

    class Data:
        class Text:
            @_struct
            class TextSegment:
                StartPosition: _type.UINT32
                Length: _type.UINT32

    class Devices:
        class Display:
            class Core:
                @_struct
                class DisplayPresentationRate:
                    VerticalSyncRate: Windows.Foundation.Numerics.Rational
                    VerticalSyncsPerPresentation: _type.INT32

        class Geolocation:
            @_struct
            class BasicGeoposition:
                Latitude: _type.DOUBLE
                Longitude: _type.DOUBLE
                Altitude: _type.DOUBLE

        class Gpio:
            @_struct
            class GpioChangeCount:
                Count: _type.UINT64
                RelativeTime: Windows.Foundation.TimeSpan

            @_struct
            class GpioChangeRecord:
                RelativeTime: Windows.Foundation.TimeSpan
                Edge: _enum.Windows.Devices.Gpio.GpioPinEdge

        class I2c:
            @_struct
            class I2cTransferResult:
                Status: _enum.Windows.Devices.I2c.I2cTransferStatus
                BytesTransferred: _type.UINT32

            class Provider:
                @_struct
                class ProviderI2cTransferResult:
                    Status: _enum.Windows.Devices.I2c.Provider.ProviderI2cTransferStatus
                    BytesTransferred: _type.UINT32

        class Input:
            @_struct
            class MouseDelta:
                X: _type.INT32
                Y: _type.INT32

            @_struct
            class PointerDeviceUsage:
                UsagePage: _type.UINT32
                Usage: _type.UINT32
                MinLogical: _type.INT32
                MaxLogical: _type.INT32
                MinPhysical: _type.INT32
                MaxPhysical: _type.INT32
                Unit: _type.UINT32
                PhysicalMultiplier: _type.FLOAT

        class PointOfService:
            @_struct
            class SizeUInt32:
                Width: _type.UINT32
                Height: _type.UINT32

        class Scanners:
            @_struct
            class ImageScannerResolution:
                DpiX: _type.FLOAT
                DpiY: _type.FLOAT

        class Sms:
            @_struct
            class SmsEncodedLength:
                SegmentCount: _type.UINT32
                CharacterCountLastSegment: _type.UINT32
                CharactersPerSegment: _type.UINT32
                ByteCountLastSegment: _type.UINT32
                BytesPerSegment: _type.UINT32

    class Foundation:
        @_struct
        class DateTime:
            UniversalTime: _type.INT64

        @_struct
        class Point:
            X: _type.FLOAT
            Y: _type.FLOAT

        @_struct
        class Rect:
            X: _type.FLOAT
            Y: _type.FLOAT
            Width: _type.FLOAT
            Height: _type.FLOAT

        @_struct
        class Size:
            Width: _type.FLOAT
            Height: _type.FLOAT

        @_struct
        class TimeSpan:
            Duration: _type.INT64

        class Numerics:
            @_struct
            class Matrix3x2:
                M11: _type.FLOAT
                M12: _type.FLOAT
                M21: _type.FLOAT
                M22: _type.FLOAT
                M31: _type.FLOAT
                M32: _type.FLOAT

            @_struct
            class Matrix4x4:
                M11: _type.FLOAT
                M12: _type.FLOAT
                M13: _type.FLOAT
                M14: _type.FLOAT
                M21: _type.FLOAT
                M22: _type.FLOAT
                M23: _type.FLOAT
                M24: _type.FLOAT
                M31: _type.FLOAT
                M32: _type.FLOAT
                M33: _type.FLOAT
                M34: _type.FLOAT
                M41: _type.FLOAT
                M42: _type.FLOAT
                M43: _type.FLOAT
                M44: _type.FLOAT

            @_struct
            class Vector3:
                X: _type.FLOAT
                Y: _type.FLOAT
                Z: _type.FLOAT

            @_struct
            class Plane:
                Normal: Windows.Foundation.Numerics.Vector3
                D: _type.FLOAT

            @_struct
            class Quaternion:
                X: _type.FLOAT
                Y: _type.FLOAT
                Z: _type.FLOAT
                W: _type.FLOAT

            @_struct
            class Rational:
                Numerator: _type.UINT32
                Denominator: _type.UINT32

            @_struct
            class Vector2:
                X: _type.FLOAT
                Y: _type.FLOAT

            @_struct
            class Vector4:
                X: _type.FLOAT
                Y: _type.FLOAT
                Z: _type.FLOAT
                W: _type.FLOAT

    class Gaming:
        class Input:
            @_struct
            class ArcadeStickReading:
                Timestamp: _type.UINT64
                Buttons: _enum.Windows.Gaming.Input.ArcadeStickButtons

            @_struct
            class FlightStickReading:
                Timestamp: _type.UINT64
                Buttons: _enum.Windows.Gaming.Input.FlightStickButtons
                HatSwitch: _enum.Windows.Gaming.Input.GameControllerSwitchPosition
                Roll: _type.DOUBLE
                Pitch: _type.DOUBLE
                Yaw: _type.DOUBLE
                Throttle: _type.DOUBLE

            @_struct
            class GamepadReading:
                Timestamp: _type.UINT64
                Buttons: _enum.Windows.Gaming.Input.GamepadButtons
                LeftTrigger: _type.DOUBLE
                RightTrigger: _type.DOUBLE
                LeftThumbstickX: _type.DOUBLE
                LeftThumbstickY: _type.DOUBLE
                RightThumbstickX: _type.DOUBLE
                RightThumbstickY: _type.DOUBLE

            @_struct
            class GamepadVibration:
                LeftMotor: _type.DOUBLE
                RightMotor: _type.DOUBLE
                LeftTrigger: _type.DOUBLE
                RightTrigger: _type.DOUBLE

            @_struct
            class RacingWheelReading:
                Timestamp: _type.UINT64
                Buttons: _enum.Windows.Gaming.Input.RacingWheelButtons
                PatternShifterGear: _type.INT32
                Wheel: _type.DOUBLE
                Throttle: _type.DOUBLE
                Brake: _type.DOUBLE
                Clutch: _type.DOUBLE
                Handbrake: _type.DOUBLE

            @_struct
            class UINavigationReading:
                Timestamp: _type.UINT64
                RequiredButtons: _enum.Windows.Gaming.Input.RequiredUINavigationButtons
                OptionalButtons: _enum.Windows.Gaming.Input.OptionalUINavigationButtons

            class Custom:
                @_struct
                class GameControllerVersionInfo:
                    Major: _type.UINT16
                    Minor: _type.UINT16
                    Build: _type.UINT16
                    Revision: _type.UINT16

                @_struct
                class GipFirmwareUpdateProgress:
                    PercentCompleted: _type.DOUBLE
                    CurrentComponentId: _type.UINT32

    class Graphics:
        @_struct
        class DisplayAdapterId:
            LowPart: _type.UINT32
            HighPart: _type.INT32

        @_struct
        class DisplayId:
            Value: _type.UINT64

        @_struct
        class PointInt32:
            X: _type.INT32
            Y: _type.INT32

        @_struct
        class RectInt32:
            X: _type.INT32
            Y: _type.INT32
            Width: _type.INT32
            Height: _type.INT32

        @_struct
        class SizeInt32:
            Width: _type.INT32
            Height: _type.INT32

        class DirectX:
            class Direct3D11:
                @_struct
                class Direct3DMultisampleDescription:
                    Count: _type.INT32
                    Quality: _type.INT32

                @_struct
                class Direct3DSurfaceDescription:
                    Width: _type.INT32
                    Height: _type.INT32
                    Format: _enum.Windows.Graphics.DirectX.DirectXPixelFormat
                    MultisampleDescription: Windows.Graphics.DirectX.Direct3D11.Direct3DMultisampleDescription

        class Display:
            @_struct
            class NitRange:
                MinNits: _type.FLOAT
                MaxNits: _type.FLOAT
                StepSizeNits: _type.FLOAT

            class Core:
                @_struct
                class HdmiDisplayHdr2086Metadata:
                    RedPrimaryX: _type.UINT16
                    RedPrimaryY: _type.UINT16
                    GreenPrimaryX: _type.UINT16
                    GreenPrimaryY: _type.UINT16
                    BluePrimaryX: _type.UINT16
                    BluePrimaryY: _type.UINT16
                    WhitePointX: _type.UINT16
                    WhitePointY: _type.UINT16
                    MaxMasteringLuminance: _type.UINT16
                    MinMasteringLuminance: _type.UINT16
                    MaxContentLightLevel: _type.UINT16
                    MaxFrameAverageLightLevel: _type.UINT16

        class Holographic:
            @_struct
            class HolographicAdapterId:
                LowPart: _type.UINT32
                HighPart: _type.INT32

            @_struct
            class HolographicFrameId:
                Value: _type.UINT64

            @_struct
            class HolographicStereoTransform:
                Left: Windows.Foundation.Numerics.Matrix4x4
                Right: Windows.Foundation.Numerics.Matrix4x4

        class Imaging:
            @_struct
            class BitmapBounds:
                X: _type.UINT32
                Y: _type.UINT32
                Width: _type.UINT32
                Height: _type.UINT32

            @_struct
            class BitmapPlaneDescription:
                StartIndex: _type.INT32
                Width: _type.INT32
                Height: _type.INT32
                Stride: _type.INT32

            @_struct
            class BitmapSize:
                Width: _type.UINT32
                Height: _type.UINT32

        class Printing:
            @_struct
            class PrintPageDescription:
                PageSize: Windows.Foundation.Size
                ImageableRect: Windows.Foundation.Rect
                DpiX: _type.UINT32
                DpiY: _type.UINT32

        class Printing3D:
            @_struct
            class Printing3DBufferDescription:
                Format: _enum.Windows.Graphics.Printing3D.Printing3DBufferFormat
                Stride: _type.UINT32

    class Management:
        class Deployment:
            @_struct
            class DeploymentProgress:
                state: _enum.Windows.Management.Deployment.DeploymentProgressState
                percentage: _type.UINT32

    class Media:
        @_struct
        class MediaTimeRange:
            Start: Windows.Foundation.TimeSpan
            End: Windows.Foundation.TimeSpan

        class Capture:
            @_struct
            class WhiteBalanceGain:
                R: _type.DOUBLE
                G: _type.DOUBLE
                B: _type.DOUBLE

        class Core:
            @_struct
            class MseTimeRange:
                Start: Windows.Foundation.TimeSpan
                End: Windows.Foundation.TimeSpan

            @_struct
            class TimedTextDouble:
                Value: _type.DOUBLE
                Unit: _enum.Windows.Media.Core.TimedTextUnit

            @_struct
            class TimedTextPadding:
                Before: _type.DOUBLE
                After: _type.DOUBLE
                Start: _type.DOUBLE
                End: _type.DOUBLE
                Unit: _enum.Windows.Media.Core.TimedTextUnit

            @_struct
            class TimedTextPoint:
                X: _type.DOUBLE
                Y: _type.DOUBLE
                Unit: _enum.Windows.Media.Core.TimedTextUnit

            @_struct
            class TimedTextSize:
                Height: _type.DOUBLE
                Width: _type.DOUBLE
                Unit: _enum.Windows.Media.Core.TimedTextUnit

        class Import:
            @_struct
            class PhotoImportProgress:
                ItemsImported: _type.UINT32
                TotalItemsToImport: _type.UINT32
                BytesImported: _type.UINT64
                TotalBytesToImport: _type.UINT64
                ImportProgress: _type.DOUBLE

        class Streaming:
            @_struct
            class PlaySpeed:
                Numerator: _type.INT32
                Denominator: _type.UINT32

            @_struct
            class TrackInformation:
                Track: _type.UINT32
                TrackId: _type.UINT32
                TrackDuration: Windows.Foundation.TimeSpan

            @_struct
            class PositionInformation:
                trackInformation: Windows.Media.Streaming.TrackInformation
                relativeTime: Windows.Foundation.TimeSpan

            @_struct
            class RenderingParameters:
                volume: _type.UINT32
                mute: _type.boolean

            @_struct
            class TransportInformation:
                CurrentTransportState: _enum.Windows.Media.Streaming.TransportState
                CurrentTransportStatus: _enum.Windows.Media.Streaming.TransportStatus
                CurrentSpeed: Windows.Media.Streaming.PlaySpeed

    class Networking:
        class BackgroundTransfer:
            @_struct
            class BackgroundDownloadProgress:
                BytesReceived: _type.UINT64
                TotalBytesToReceive: _type.UINT64
                Status: _enum.Windows.Networking.BackgroundTransfer.BackgroundTransferStatus
                HasResponseChanged: _type.boolean
                HasRestarted: _type.boolean

            @_struct
            class BackgroundTransferFileRange:
                Offset: _type.UINT64
                Length: _type.UINT64

            @_struct
            class BackgroundUploadProgress:
                BytesReceived: _type.UINT64
                BytesSent: _type.UINT64
                TotalBytesToReceive: _type.UINT64
                TotalBytesToSend: _type.UINT64
                Status: _enum.Windows.Networking.BackgroundTransfer.BackgroundTransferStatus
                HasResponseChanged: _type.boolean
                HasRestarted: _type.boolean

        class Connectivity:
            @_struct
            class NetworkUsageStates:
                Roaming: _enum.Windows.Networking.Connectivity.TriStates
                Shared: _enum.Windows.Networking.Connectivity.TriStates

        class NetworkOperators:
            @_struct
            class ESimProfileInstallProgress:
                TotalSizeInBytes: _type.INT32
                InstalledSizeInBytes: _type.INT32

            @_struct
            class ProfileUsage:
                UsageInMegabytes: _type.UINT32
                LastSyncTime: Windows.Foundation.DateTime

        class Sockets:
            @_struct
            class BandwidthStatistics:
                OutboundBitsPerSecond: _type.UINT64
                InboundBitsPerSecond: _type.UINT64
                OutboundBitsPerSecondInstability: _type.UINT64
                InboundBitsPerSecondInstability: _type.UINT64
                OutboundBandwidthPeaked: _type.boolean
                InboundBandwidthPeaked: _type.boolean

            @_struct
            class RoundTripTimeStatistics:
                Variance: _type.UINT32
                Max: _type.UINT32
                Min: _type.UINT32
                Sum: _type.UINT32

    class Perception:
        class People:
            @_struct
            class HandMeshVertex:
                Position: Windows.Foundation.Numerics.Vector3
                Normal: Windows.Foundation.Numerics.Vector3

            @_struct
            class JointPose:
                Orientation: Windows.Foundation.Numerics.Quaternion
                Position: Windows.Foundation.Numerics.Vector3
                Radius: _type.FLOAT
                Accuracy: _enum.Windows.Perception.People.JointPoseAccuracy

        class Spatial:
            @_struct
            class SpatialBoundingBox:
                Center: Windows.Foundation.Numerics.Vector3
                Extents: Windows.Foundation.Numerics.Vector3

            @_struct
            class SpatialBoundingFrustum:
                Near: Windows.Foundation.Numerics.Plane
                Far: Windows.Foundation.Numerics.Plane
                Right: Windows.Foundation.Numerics.Plane
                Left: Windows.Foundation.Numerics.Plane
                Top: Windows.Foundation.Numerics.Plane
                Bottom: Windows.Foundation.Numerics.Plane

            @_struct
            class SpatialBoundingOrientedBox:
                Center: Windows.Foundation.Numerics.Vector3
                Extents: Windows.Foundation.Numerics.Vector3
                Orientation: Windows.Foundation.Numerics.Quaternion

            @_struct
            class SpatialBoundingSphere:
                Center: Windows.Foundation.Numerics.Vector3
                Radius: _type.FLOAT

            @_struct
            class SpatialRay:
                Origin: Windows.Foundation.Numerics.Vector3
                Direction: Windows.Foundation.Numerics.Vector3

    class Security:
        class Isolation:
            @_struct
            class IsolatedWindowsEnvironmentCreateProgress:
                State: _enum.Windows.Security.Isolation.IsolatedWindowsEnvironmentProgressState
                PercentComplete: _type.UINT32

    class Services:
        class Store:
            @_struct
            class StorePackageUpdateStatus:
                PackageFamilyName: _type.HSTRING
                PackageDownloadSizeInBytes: _type.UINT64
                PackageBytesDownloaded: _type.UINT64
                PackageDownloadProgress: _type.DOUBLE
                TotalDownloadProgress: _type.DOUBLE
                PackageUpdateState: _enum.Windows.Services.Store.StorePackageUpdateState

    class Storage:
        class AccessCache:
            @_struct
            class AccessListEntry:
                Token: _type.HSTRING
                Metadata: _type.HSTRING

        class Search:
            @_struct
            class SortEntry:
                PropertyName: _type.HSTRING
                AscendingOrder: _type.boolean

    class UI:
        @_struct
        class Color:
            A: _type.BYTE
            R: _type.BYTE
            G: _type.BYTE
            B: _type.BYTE

        @_struct
        class WindowId:
            Value: _type.UINT64

        class Composition:
            @_struct
            class InkTrailPoint:
                Point: Windows.Foundation.Point
                Radius: _type.FLOAT

        class Core:
            @_struct
            class CorePhysicalKeyStatus:
                RepeatCount: _type.UINT32
                ScanCode: _type.UINT32
                IsExtendedKey: _type.boolean
                IsMenuKeyDown: _type.boolean
                WasKeyDown: _type.boolean
                IsKeyReleased: _type.boolean

            @_struct
            class CoreProximityEvaluation:
                Score: _type.INT32
                AdjustedPoint: Windows.Foundation.Point

        class Input:
            @_struct
            class CrossSlideThresholds:
                SelectionStart: _type.FLOAT
                SpeedBumpStart: _type.FLOAT
                SpeedBumpEnd: _type.FLOAT
                RearrangeStart: _type.FLOAT

            @_struct
            class ManipulationDelta:
                Translation: Windows.Foundation.Point
                Scale: _type.FLOAT
                Rotation: _type.FLOAT
                Expansion: _type.FLOAT

            @_struct
            class ManipulationVelocities:
                Linear: Windows.Foundation.Point
                Angular: _type.FLOAT
                Expansion: _type.FLOAT

            class Preview:
                class Injection:
                    @_struct
                    class InjectedInputPoint:
                        PositionX: _type.INT32
                        PositionY: _type.INT32

                    @_struct
                    class InjectedInputPointerInfo:
                        PointerId: _type.UINT32
                        PointerOptions: _enum.Windows.UI.Input.Preview.Injection.InjectedInputPointerOptions
                        PixelLocation: Windows.UI.Input.Preview.Injection.InjectedInputPoint
                        TimeOffsetInMilliseconds: _type.UINT32
                        PerformanceCount: _type.UINT64

                    @_struct
                    class InjectedInputRectangle:
                        Left: _type.INT32
                        Top: _type.INT32
                        Bottom: _type.INT32
                        Right: _type.INT32

        class Text:
            @_struct
            class FontWeight:
                Weight: _type.UINT16

            class Core:
                @_struct
                class CoreTextRange:
                    StartCaretPosition: _type.INT32
                    EndCaretPosition: _type.INT32

        class UIAutomation:
            class Core:
                @_struct
                class AutomationAnnotationTypeRegistration:
                    LocalId: _type.INT32

                @_struct
                class AutomationRemoteOperationOperandId:
                    Value: _type.INT32

        class Xaml:
            @_struct
            class CornerRadius:
                TopLeft: _type.DOUBLE
                TopRight: _type.DOUBLE
                BottomRight: _type.DOUBLE
                BottomLeft: _type.DOUBLE

            @_struct
            class Duration:
                TimeSpan: Windows.Foundation.TimeSpan
                Type: _enum.Windows.UI.Xaml.DurationType

            @_struct
            class GridLength:
                Value: _type.DOUBLE
                GridUnitType: _enum.Windows.UI.Xaml.GridUnitType

            @_struct
            class Thickness:
                Left: _type.DOUBLE
                Top: _type.DOUBLE
                Right: _type.DOUBLE
                Bottom: _type.DOUBLE

            class Automation:
                class Peers:
                    @_struct
                    class RawElementProviderRuntimeId:
                        Part1: _type.UINT32
                        Part2: _type.UINT32

            class Controls:
                class Maps:
                    @_struct
                    class MapZoomLevelRange:
                        Min: _type.DOUBLE
                        Max: _type.DOUBLE

                class Primitives:
                    @_struct
                    class GeneratorPosition:
                        Index: _type.INT32
                        Offset: _type.INT32

            class Data:
                @_struct
                class LoadMoreItemsResult:
                    Count: _type.UINT32

            class Documents:
                @_struct
                class TextRange:
                    StartIndex: _type.INT32
                    Length: _type.INT32

            class Interop:
                @_struct
                class TypeName:
                    Name: _type.HSTRING
                    Kind: _enum.Windows.UI.Xaml.Interop.TypeKind

            class Markup:
                @_struct
                class XamlBinaryWriterErrorInformation:
                    InputStreamIndex: _type.UINT32
                    LineNumber: _type.UINT32
                    LinePosition: _type.UINT32

                @_struct
                class XmlnsDefinition:
                    XmlNamespace: _type.HSTRING
                    Namespace: _type.HSTRING

            class Media:
                @_struct
                class Matrix:
                    M11: _type.DOUBLE
                    M12: _type.DOUBLE
                    M21: _type.DOUBLE
                    M22: _type.DOUBLE
                    OffsetX: _type.DOUBLE
                    OffsetY: _type.DOUBLE

                class Animation:
                    @_struct
                    class KeyTime:
                        TimeSpan: Windows.Foundation.TimeSpan

                    @_struct
                    class RepeatBehavior:
                        Count: _type.DOUBLE
                        Duration: Windows.Foundation.TimeSpan
                        Type: _enum.Windows.UI.Xaml.Media.Animation.RepeatBehaviorType

                class Media3D:
                    @_struct
                    class Matrix3D:
                        M11: _type.DOUBLE
                        M12: _type.DOUBLE
                        M13: _type.DOUBLE
                        M14: _type.DOUBLE
                        M21: _type.DOUBLE
                        M22: _type.DOUBLE
                        M23: _type.DOUBLE
                        M24: _type.DOUBLE
                        M31: _type.DOUBLE
                        M32: _type.DOUBLE
                        M33: _type.DOUBLE
                        M34: _type.DOUBLE
                        OffsetX: _type.DOUBLE
                        OffsetY: _type.DOUBLE
                        OffsetZ: _type.DOUBLE
                        M44: _type.DOUBLE

    class Web:
        class Http:
            @_struct
            class HttpProgress:  # TODO
                Stage: _enum.Windows.Web.Http.HttpProgressStage
                BytesSent: _type.UINT64
                ...  # TotalBytesToSend: _interface.Windows.Foundation.IReference[_type.UINT64]
                BytesReceived: _type.UINT64
                ...  # TotalBytesToReceive: _interface.Windows.Foundation.IReference[_type.UINT64]
                Retries: _type.UINT32

        class Syndication:
            @_struct
            class RetrievalProgress:
                BytesRetrieved: _type.UINT32
                TotalBytesToRetrieve: _type.UINT32

            @_struct
            class TransferProgress:
                BytesSent: _type.UINT32
                TotalBytesToSend: _type.UINT32
                BytesRetrieved: _type.UINT32
                TotalBytesToRetrieve: _type.UINT32


@_struct
class CXString:
    data: _type.c_void_p
    private_flags: _type.c_uint


@_struct
class CXStringSet:
    Strings: _Pointer[CXString]
    Count: _type.c_uint


@_struct
class CXComment:
    ASTNode: _type.c_void_p
    TranslationUnit: _type.CXTranslationUnit


@_struct
class CXUnsavedFile:
    Filename: _type.c_char_p
    Contents: _type.c_char_p
    Length: _type.c_ulong


@_struct
class CXVersion:
    Major: _type.c_int
    Minor: _type.c_int
    Subminor: _type.c_int


@_struct
class CXFileUniqueID:
    data: _type.c_longlong * 3


@_struct
class CXSourceLocation:
    ptr_data: _type.c_void_p * 2
    int_data: _type.c_uint


@_struct
class CXSourceRange:
    ptr_data: _type.c_void_p * 2
    begin_int_data: _type.c_uint
    end_int_data: _type.c_uint


@_struct
class CXSourceRangeList:
    count: _type.c_uint
    ranges: _Pointer[CXSourceRange]


@_struct
class CXTUResourceUsageEntry:
    kind: _enum_libclang.CXTUResourceUsageKind
    amount: _type.c_ulong


@_struct
class CXTUResourceUsage:
    data: _type.c_void_p
    numEntries: _type.c_uint
    entries: _Pointer[CXTUResourceUsageEntry]


@_struct
class CXCursor:
    kind: _enum_libclang.CXCursorKind
    xdata: _type.c_int
    data: _type.c_void_p * 3


@_struct
class CXPlatformAvailability:
    Platform: CXString
    Introduced: CXVersion
    Deprecated: CXVersion
    Obsoleted: CXVersion
    Unavailable: _type.c_int
    Message: CXString


@_struct
class CXType:
    kind: _enum_libclang.CXTypeKind
    data: _type.c_void_p * 2


@_struct
class CXToken:
    int_data: _type.c_uint * 4
    ptr_data: _type.c_void_p


@_struct
class CXCompletionResult:
    CursorKind: _enum_libclang.CXCursorKind
    CompletionString: _type.CXCompletionString


@_struct
class CXCodeCompleteResults:
    Results: _Pointer[CXCompletionResult]
    NumResults: _type.c_uint


@_struct
class CXCursorAndRangeVisitor:
    context: _type.c_void_p
    visit: _type.CXCursorAndRangeVisitor_visit


@_struct
class CXIdxLoc:
    ptr_data: _type.c_void_p * 2
    int_data: _type.c_uint


@_struct
class CXIdxAttrInfo:
    kind: _enum_libclang.CXIdxAttrKind
    cursor: CXCursor
    loc: CXIdxLoc


@_struct
class CXIdxEntityInfo:
    kind: _enum_libclang.CXIdxEntityKind
    templateKind: _enum_libclang.CXIdxEntityCXXTemplateKind
    lang: _enum_libclang.CXIdxEntityLanguage
    name: _type.c_char_p
    USR: _type.c_char_p
    cursor: CXCursor
    attributes: _Pointer[_Pointer[CXIdxAttrInfo]]
    numAttributes: _type.c_uint


@_struct
class CXIdxContainerInfo:
    cursor: CXCursor


@_struct
class CXIdxIBOutletCollectionAttrInfo:
    attrInfo: _Pointer[CXIdxAttrInfo]
    objcClass: _Pointer[CXIdxEntityInfo]
    classCursor: CXCursor
    classLoc: CXIdxLoc


@_struct
class CXIdxDeclInfo:
    entityInfo: _Pointer[CXIdxEntityInfo]
    cursor: CXCursor
    loc: CXIdxLoc
    semanticContainer: _Pointer[CXIdxContainerInfo]
    lexicalContainer: _Pointer[CXIdxContainerInfo]
    isRedeclaration: _type.c_int
    isDefinition: _type.c_int
    isContainer: _type.c_int
    declAsContainer: _Pointer[CXIdxContainerInfo]
    isImplicit: _type.c_int
    attributes: _Pointer[_Pointer[CXIdxAttrInfo]]
    numAttributes: _type.c_uint
    flags: _type.c_uint


@_struct
class CXIdxObjCContainerDeclInfo:
    declInfo: _Pointer[CXIdxDeclInfo]
    kind: _enum_libclang.CXIdxObjCContainerKind


@_struct
class CXIdxBaseClassInfo:
    base: _Pointer[CXIdxEntityInfo]
    cursor: CXCursor
    loc: CXIdxLoc


@_struct
class CXIdxObjCProtocolRefInfo:
    protocol: _Pointer[CXIdxEntityInfo]
    cursor: CXCursor
    loc: CXIdxLoc


@_struct
class CXIdxObjCProtocolRefListInfo:
    protocols: _Pointer[_Pointer[CXIdxObjCProtocolRefInfo]]
    numProtocols: _type.c_uint


@_struct
class CXIdxObjCInterfaceDeclInfo:
    containerInfo: _Pointer[CXIdxObjCContainerDeclInfo]
    superInfo: _Pointer[CXIdxBaseClassInfo]
    protocols: _Pointer[CXIdxObjCProtocolRefListInfo]


@_struct
class CXIdxObjCCategoryDeclInfo:
    containerInfo: _Pointer[CXIdxObjCContainerDeclInfo]
    objcClass: _Pointer[CXIdxEntityInfo]
    classCursor: CXCursor
    classLoc: CXIdxLoc
    protocols: _Pointer[CXIdxObjCProtocolRefListInfo]


@_struct
class CXIdxObjCPropertyDeclInfo:
    declInfo: _Pointer[CXIdxDeclInfo]
    getter: _Pointer[CXIdxEntityInfo]
    setter: _Pointer[CXIdxEntityInfo]


@_struct
class CXIdxCXXClassDeclInfo:
    declInfo: _Pointer[CXIdxDeclInfo]
    bases: _Pointer[_Pointer[CXIdxBaseClassInfo]]
    numBases: _type.c_uint


@_struct
class CXIdxEntityRefInfo:
    kind: _enum_libclang.CXIdxEntityRefKind
    cursor: CXCursor
    loc: CXIdxLoc
    referencedEntity: _Pointer[CXIdxEntityInfo]
    parentEntity: _Pointer[CXIdxEntityInfo]
    container: _Pointer[CXIdxContainerInfo]
    role: _enum_libclang.CXSymbolRole


# brotli
# decode
@_struct
class BrotliDecoderStateStruct:
    pass


BrotliDecoderState = BrotliDecoderStateStruct


# encode
@_struct
class BrotliEncoderStateStruct:
    pass


BrotliEncoderState = BrotliEncoderStateStruct


# iCUESDK
# iCUESDK
@_struct
class CorsairVersion:
    major: _type.c_int
    minor: _type.c_int
    patch: _type.c_int


@_struct
class CorsairSessionDetails:
    clientVersion: CorsairVersion
    serverVersion: CorsairVersion
    serverHostVersion: CorsairVersion


@_struct
class CorsairSessionStateChanged:
    state: _enum_iCUESDK.CorsairSessionState
    details: CorsairSessionDetails


@_struct
class CorsairDeviceInfo:
    type: _enum_iCUESDK.CorsairDeviceType
    id: _type.CorsairDeviceId
    serial: _type.c_char * _const_iCUESDK.CORSAIR_STRING_SIZE_M
    model: _type.c_char * _const_iCUESDK.CORSAIR_STRING_SIZE_M
    ledCount: _type.c_int
    channelCount: _type.c_int


@_struct
class CorsairLedPosition:
    id: _type.CorsairLedLuid
    cx: _type.c_double
    cy: _type.c_double


@_struct
class CorsairDeviceFilter:
    deviceTypeMask: _type.c_int


@_struct
class CorsairDeviceConnectionStatusChangedEvent:
    deviceId: _type.CorsairDeviceId
    isConnected: _type.c_bool


@_struct
class CorsairKeyEvent:
    deviceId: _type.CorsairDeviceId
    keyId: _enum_iCUESDK.CorsairMacroKeyId
    isPressed: _type.c_bool


@_struct
class CorsairEvent:
    id: _enum_iCUESDK.CorsairEventId
    U: _union.CorsairEvent_U


# noinspection PyPep8Naming
@_struct
class CorsairDataType_BooleanArray:
    items: _Pointer[_type.c_bool]
    count: _type.c_uint


# noinspection PyPep8Naming
@_struct
class CorsairDataType_Int32Array:
    items: _Pointer[_type.c_int]
    count: _type.c_uint


# noinspection PyPep8Naming
@_struct
class CorsairDataType_Float64Array:
    items: _Pointer[_type.c_double]
    count: _type.c_uint


# noinspection PyPep8Naming
@_struct
class CorsairDataType_StringArray:
    items: _Pointer[_type.c_char_p]
    count: _type.c_uint


@_struct
class CorsairProperty:
    type: _enum_iCUESDK.CorsairDataType
    value: _union.CorsairDataValue


@_struct
class CorsairLedColor:
    id: _type.CorsairLedLuid
    r: _type.c_uchar
    g: _type.c_uchar
    b: _type.c_uchar
    a: _type.c_uchar


@_struct
class CorsairKeyEventConfiguration:
    keyId: _enum_iCUESDK.CorsairMacroKeyId
    isIntercepted: _type.c_bool


# CgSDK
# CgSDK
@_struct
class CorsairProtocolDetails:
    sdkVersion: _type.c_char_p
    serverVersion: _type.c_char_p
    sdkProtocolVersion: _type.c_int
    serverProtocolVersion: _type.c_int
    breakingChanges: _type.c_bool


# ChromaSDK
# RzChromaSDKTypes
RZEFFECTID = GUID
RZDEVICEID = GUID


class ChromaSDK:
    @_struct
    class Author:
        Name: _type.TCHAR * 256
        Contact: _type.TCHAR * 256

    @_struct
    class APPINFOTYPE:
        Title: _type.TCHAR * 256
        Description: _type.TCHAR * 1024
        Author: ChromaSDK.Author
        SupportedDevice: _type.DWORD
        Category: _type.DWORD

    # noinspection PyPep8Naming
    @_struct
    class DEVICE_INFO_TYPE:
        DeviceType: _enum_ChromaSDK.ChromaSDK.DEVICE_INFO_TYPE.DeviceType
        Connected: _type.DWORD

    # noinspection PyPep8Naming
    @_struct
    class BLINKING_EFFECT_TYPE:
        Size: _type.RZSIZE
        Param: _type.DWORD
        Color: _type.COLORREF

    # noinspection PyPep8Naming
    @_struct
    class BREATHING_EFFECT_TYPE:
        Size: _type.RZSIZE
        Param: _type.DWORD
        Type: _enum_ChromaSDK.ChromaSDK.BREATHING_EFFECT_TYPE.Type
        Color1: _type.COLORREF
        Color2: _type.COLORREF

    # noinspection PyPep8Naming
    @_struct
    class CUSTOM_EFFECT_TYPE:
        Size: _type.RZSIZE
        Param: _type.DWORD
        Color: _type.RZCOLOR * _const_ChromaSDK.ChromaSDK.MAX_ROW * _const_ChromaSDK.ChromaSDK.MAX_COLUMN

    # noinspection PyPep8Naming
    @_struct
    class NO_EFFECT_TYPE:
        Size: _type.RZSIZE
        Param: _type.DWORD

    # noinspection PyPep8Naming
    @_struct
    class REACTIVE_EFFECT_TYPE:
        Size: _type.RZSIZE
        Param: _type.DWORD
        Duration: _enum_ChromaSDK.ChromaSDK.REACTIVE_EFFECT_TYPE.Duration
        Color: _type.COLORREF

    # noinspection PyPep8Naming
    @_struct
    class SPECTRUMCYCLING_EFFECT_TYPE:
        Size: _type.RZSIZE
        Param: _type.DWORD

    # noinspection PyPep8Naming
    @_struct
    class STARLIGHT_EFFECT_TYPE:
        Size: _type.RZSIZE
        Param: _type.DWORD
        Type: _enum_ChromaSDK.ChromaSDK.STARLIGHT_EFFECT_TYPE.Type
        Color1: _type.COLORREF
        Color2: _type.COLORREF
        Duration: _enum_ChromaSDK.ChromaSDK.STARLIGHT_EFFECT_TYPE.Duration

    # noinspection PyPep8Naming
    @_struct
    class STATIC_EFFECT_TYPE:
        Size: _type.RZSIZE
        Param: _type.DWORD
        Color: _type.COLORREF

    # noinspection PyPep8Naming
    @_struct
    class WAVE_EFFECT_TYPE:
        Size: _type.RZSIZE
        Param: _type.DWORD
        Direction: _enum_ChromaSDK.ChromaSDK.WAVE_EFFECT_TYPE.Direction

    class Keyboard:
        # noinspection PyPep8Naming
        @_struct
        class BREATHING_EFFECT_TYPE:
            Type: _enum_ChromaSDK.ChromaSDK.Keyboard.BREATHING_EFFECT_TYPE.Type
            Color1: _type.COLORREF
            Color2: _type.COLORREF

        # noinspection PyPep8Naming
        @_struct
        class CUSTOM_EFFECT_TYPE:
            Color: _type.RZCOLOR * _const_ChromaSDK.ChromaSDK.Keyboard.MAX_ROW * _const_ChromaSDK.ChromaSDK.Keyboard.MAX_COLUMN

        # noinspection PyPep8Naming
        @_struct
        class CUSTOM_KEY_EFFECT_TYPE:
            Color: _type.RZCOLOR * _const_ChromaSDK.ChromaSDK.Keyboard.MAX_ROW * _const_ChromaSDK.ChromaSDK.Keyboard.MAX_COLUMN
            Key: _type.COLORREF * _const_ChromaSDK.ChromaSDK.Keyboard.MAX_ROW * _const_ChromaSDK.ChromaSDK.Keyboard.MAX_COLUMN

        # noinspection PyPep8Naming
        @_struct
        class REACTIVE_EFFECT_TYPE:
            Duration: _enum_ChromaSDK.ChromaSDK.Keyboard.REACTIVE_EFFECT_TYPE.Duration
            Color: _type.COLORREF

        # noinspection PyPep8Naming
        @_struct
        class STARLIGHT_EFFECT_TYPE:
            Type: _enum_ChromaSDK.ChromaSDK.Keyboard.STARLIGHT_EFFECT_TYPE.Type
            Color1: _type.COLORREF
            Color2: _type.COLORREF
            Duration: _enum_ChromaSDK.ChromaSDK.Keyboard.STARLIGHT_EFFECT_TYPE.Duration

        # noinspection PyPep8Naming
        @_struct
        class STATIC_EFFECT_TYPE:
            Color: _type.COLORREF

        # noinspection PyPep8Naming
        @_struct
        class WAVE_EFFECT_TYPE:
            Direction: _enum_ChromaSDK.ChromaSDK.Keyboard.WAVE_EFFECT_TYPE.Direction

        # noinspection PyPep8Naming
        class v2:
            # noinspection PyPep8Naming
            class CUSTOM_EFFECT_TYPE:
                Color: _type.RZCOLOR * _const_ChromaSDK.ChromaSDK.Keyboard.v2.MAX_ROW * _const_ChromaSDK.ChromaSDK.Keyboard.v2.MAX_COLUMN
                Key: _type.COLORREF * _const_ChromaSDK.ChromaSDK.Keyboard.MAX_ROW * _const_ChromaSDK.ChromaSDK.Keyboard.MAX_COLUMN

    class Mouse:
        # noinspection PyPep8Naming
        @_struct
        class STATIC_EFFECT_TYPE:
            LEDId: _enum_ChromaSDK.ChromaSDK.Mouse.RZLED
            Color: _type.COLORREF

        # noinspection PyPep8Naming
        @_struct
        class BLINKING_EFFECT_TYPE:
            LEDId: _enum_ChromaSDK.ChromaSDK.Mouse.RZLED
            Color: _type.COLORREF

        # noinspection PyPep8Naming
        @_struct
        class BREATHING_EFFECT_TYPE:
            LEDId: _enum_ChromaSDK.ChromaSDK.Mouse.RZLED
            Type: _enum_ChromaSDK.ChromaSDK.Mouse.BREATHING_EFFECT_TYPE.Type
            Color1: _type.COLORREF
            Color2: _type.COLORREF

        # noinspection PyPep8Naming
        @_struct
        class CUSTOM_EFFECT_TYPE:
            Color: _type.RZCOLOR * _const_ChromaSDK.ChromaSDK.Mouse.MAX_LEDS

        # noinspection PyPep8Naming
        @_struct
        class CUSTOM_EFFECT_TYPE2:
            Color: _type.RZCOLOR * _const_ChromaSDK.ChromaSDK.Mouse.MAX_ROW * _const_ChromaSDK.ChromaSDK.Mouse.MAX_COLUMN

        # noinspection PyPep8Naming
        @_struct
        class REACTIVE_EFFECT_TYPE:
            LEDId: _enum_ChromaSDK.ChromaSDK.Mouse.RZLED
            Duration: _enum_ChromaSDK.ChromaSDK.Mouse.REACTIVE_EFFECT_TYPE.Duration
            Color: _type.RZCOLOR

        # noinspection PyPep8Naming
        @_struct
        class NO_EFFECT_TYPE:
            LEDId: _enum_ChromaSDK.ChromaSDK.Mouse.RZLED

        # noinspection PyPep8Naming
        @_struct
        class SPECTRUMCYCLING_EFFECT_TYPE:
            LEDId: _enum_ChromaSDK.ChromaSDK.Mouse.RZLED

        # noinspection PyPep8Naming
        @_struct
        class WAVE_EFFECT_TYPE:
            Direction: _enum_ChromaSDK.ChromaSDK.Mouse.WAVE_EFFECT_TYPE.Direction

    class Headset:
        # noinspection PyPep8Naming
        @_struct
        class STATIC_EFFECT_TYPE:
            Color: _type.COLORREF

        # noinspection PyPep8Naming
        @_struct
        class BREATHING_EFFECT_TYPE:
            Color: _type.COLORREF

        # noinspection PyPep8Naming
        @_struct
        class CUSTOM_EFFECT_TYPE:
            Color: _type.RZCOLOR * _const_ChromaSDK.ChromaSDK.Headset.MAX_LEDS

    class Mousepad:
        # noinspection PyPep8Naming
        @_struct
        class BREATHING_EFFECT_TYPE:
            Type: _enum_ChromaSDK.ChromaSDK.Mousepad.BREATHING_EFFECT_TYPE.Type
            Color1: _type.COLORREF
            Color2: _type.COLORREF

        # noinspection PyPep8Naming
        @_struct
        class CUSTOM_EFFECT_TYPE:
            Color: _type.RZCOLOR * _const_ChromaSDK.ChromaSDK.Mousepad.MAX_LEDS

        # noinspection PyPep8Naming
        @_struct
        class STATIC_EFFECT_TYPE:
            Color: _type.COLORREF

        # noinspection PyPep8Naming
        @_struct
        class WAVE_EFFECT_TYPE:
            Direction: _enum_ChromaSDK.ChromaSDK.Mousepad.WAVE_EFFECT_TYPE.Direction

        # noinspection PyPep8Naming
        class v2:
            # noinspection PyPep8Naming
            @_struct
            class CUSTOM_EFFECT_TYPE:
                Color: _type.RZCOLOR * _const_ChromaSDK.ChromaSDK.Mousepad.v2.MAX_LEDS

    class Keypad:
        # noinspection PyPep8Naming
        @_struct
        class BREATHING_EFFECT_TYPE:
            Type: _enum_ChromaSDK.ChromaSDK.Keypad.BREATHING_EFFECT_TYPE.Type
            Color1: _type.COLORREF
            Color2: _type.COLORREF

        # noinspection PyPep8Naming
        @_struct
        class CUSTOM_EFFECT_TYPE:
            Color: _type.RZCOLOR * _const_ChromaSDK.ChromaSDK.Keypad.MAX_ROW * _const_ChromaSDK.ChromaSDK.Keypad.MAX_COLUMN

        # noinspection PyPep8Naming
        @_struct
        class REACTIVE_EFFECT_TYPE:
            Duration: _enum_ChromaSDK.ChromaSDK.Keypad.REACTIVE_EFFECT_TYPE.Duration
            Color: _type.COLORREF

        # noinspection PyPep8Naming
        @_struct
        class STATIC_EFFECT_TYPE:
            Color: _type.RZCOLOR

        # noinspection PyPep8Naming
        @_struct
        class WAVE_EFFECT_TYPE:
            Direction: _enum_ChromaSDK.ChromaSDK.Keypad.WAVE_EFFECT_TYPE.Direction

    class ChromaLink:
        # noinspection PyPep8Naming
        @_struct
        class CUSTOM_EFFECT_TYPE:
            Color: _type.RZCOLOR * _const_ChromaSDK.ChromaSDK.ChromaLink.MAX_LEDS

        # noinspection PyPep8Naming
        @_struct
        class STATIC_EFFECT_TYPE:
            Color: _type.RZCOLOR

    @_struct
    class FChromaSDKGuid:
        Data: RZEFFECTID


class Microsoft:
    class UI:
        @_struct
        class DisplayId:
            Value: _type.UINT64

        @_struct
        class IconId:
            Value: _type.UINT64

        @_struct
        class WindowId:
            Value: _type.UINT64

        class Input:
            @_struct
            class CrossSlideThresholds:
                SelectionStart: _type.FLOAT
                SpeedBumpStart: _type.FLOAT
                SpeedBumpEnd: _type.FLOAT
                RearrangeStart: _type.FLOAT

            @_struct
            class ManipulationDelta:
                Translation: Windows.Foundation.Point
                Scale: _type.FLOAT
                Rotation: _type.FLOAT
                Expansion: _type.FLOAT

            @_struct
            class ManipulationVelocities:
                Linear: Windows.Foundation.Point
                Angular: _type.FLOAT
                Expansion: _type.FLOAT

            @_struct
            class PhysicalKeyStatus:
                RepeatCount: _type.UINT32
                ScanCode: _type.UINT32
                IsExtendedKey: _type.boolean
                IsMenuKeyDown: _type.boolean
                WasKeyDown: _type.boolean
                IsKeyReleased: _type.boolean

        class Xaml:
            @_struct
            class CornerRadius:
                TopLeft: _type.DOUBLE
                TopRight: _type.DOUBLE
                BottomRight: _type.DOUBLE
                BottomLeft: _type.DOUBLE

            @_struct
            class Duration:
                TimeSpan: Windows.Foundation.TimeSpan
                Type: _enum.Microsoft.UI.Xaml.DurationType

            @_struct
            class GridLength:
                Value: _type.DOUBLE
                GridUnitType: _enum.Microsoft.UI.Xaml.GridUnitType

            @_struct
            class Thickness:
                Left: _type.DOUBLE
                Top: _type.DOUBLE
                Right: _type.DOUBLE
                Bottom: _type.DOUBLE

            class Automation:
                class Peers:
                    @_struct
                    class RawElementProviderRuntimeId:
                        Part1: _type.UINT32
                        Part2: _type.UINT32

            class Controls:
                class Primitives:
                    @_struct
                    class GeneratorPosition:
                        Index: _type.INT32
                        Offset: _type.INT32

            class Data:
                @_struct
                class LoadMoreItemsResult:
                    Count: _type.UINT32

            class Documents:
                @_struct
                class TextRange:
                    StartIndex: _type.INT32
                    Length: _type.INT32

            class Markup:
                @_struct
                class XamlBinaryWriterErrorInformation:
                    InputStreamIndex: _type.UINT32
                    LineNumber: _type.UINT32
                    LinePosition: _type.UINT32

                @_struct
                class XmlnsDefinition:
                    XmlNamespace: _type.HSTRING
                    Namespace: _type.HSTRING

            class Media:
                @_struct
                class Matrix:
                    M11: _type.DOUBLE
                    M12: _type.DOUBLE
                    M21: _type.DOUBLE
                    M22: _type.DOUBLE
                    OffsetX: _type.DOUBLE
                    OffsetY: _type.DOUBLE

                class Animation:
                    @_struct
                    class KeyTime:
                        TimeSpan: Windows.Foundation.TimeSpan

                    @_struct
                    class RepeatBehavior:
                        Count: _type.DOUBLE
                        Duration: Windows.Foundation.TimeSpan
                        Type: _enum.Microsoft.UI.Xaml.Media.Animation.RepeatBehaviorType

                class Media3D:
                    @_struct
                    class Matrix3D:
                        M11: _type.DOUBLE
                        M12: _type.DOUBLE
                        M13: _type.DOUBLE
                        M14: _type.DOUBLE
                        M21: _type.DOUBLE
                        M22: _type.DOUBLE
                        M23: _type.DOUBLE
                        M24: _type.DOUBLE
                        M31: _type.DOUBLE
                        M32: _type.DOUBLE
                        M33: _type.DOUBLE
                        M34: _type.DOUBLE
                        OffsetX: _type.DOUBLE
                        OffsetY: _type.DOUBLE
                        OffsetZ: _type.DOUBLE
                        M44: _type.DOUBLE

    class Web:
        class WebView2:
            class Core:
                @_struct
                class CoreWebView2PhysicalKeyStatus:
                    RepeatCount: _type.UINT32
                    ScanCode: _type.UINT32
                    IsExtendedKey: _type.INT32
                    IsMenuKeyDown: _type.INT32
                    WasKeyDown: _type.INT32
                    IsKeyReleased: _type.INT32

    class Windows:
        class ApplicationModel:
            class DynamicDependency:
                @_struct
                class PackageDependencyContextId:
                    Id: _type.UINT64

        class PushNotifications:
            @_struct
            class PushNotificationCreateChannelStatus:
                status: _enum.Microsoft.Windows.PushNotifications.PushNotificationChannelStatus
                extendedError: _type.HRESULT
                retryCount: _type.UINT32

        class Security:
            class AccessControl:
                @_struct
                class AppContainerNameAndAccess:
                    appContainerName: _type.HSTRING
                    accessMask: _type.UINT32


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

    def __dir__(self):
        return self._vars


class _Struct(_ctypes.Structure):
    def __init__(self, *args, **kwargs):
        for name, val in self._defaults[len(args):]:
            if val is not None and name not in kwargs:
                kwargs[name] = val
        super().__init__(*args, **kwargs)

    def __iter__(self):
        return (name for name, *_ in self._fields_)

    def __contains__(self, item):
        return item in self.__iter__()

    def __getitem__(self, item):
        return getattr(self, item)

    def keys(self):
        return self.__iter__()

    def values(self):
        return (self.__getitem__(name) for name in self)

    def items(self):
        return zip(self.keys(), self.values())

    __repr__ = _fields_repr


def _init(item: str, var: _Optional[type] = None) -> type:
    if var is None:
        var = _globals.vars[item]
    if hasattr(var, '_struct'):
        fields = tuple((name, _resolve_type(
            hints)) for name, hints in _typing.get_type_hints(
            var, _globals, _globals).items())
        struct = type(item, (_Struct,), {'_fields_': tuple(field if (bitfield := getattr(
            field[1], '_bitfield', None)) is None else (*field, bitfield) for field in fields)})
        struct._defaults = tuple((field[0], _sizeof(struct) if (val := getattr(
            var, field[0], None)) is _SIZE else val) for field in fields)
        return struct
    else:
        return _NamespaceMeta(item, (), vars(var).copy())


_globals = _Globals(globals())
