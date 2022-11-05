from __future__ import annotations as _

import ctypes as _ctypes
import typing as _typing

from . import const as _const, struct as _struct, type as _type
from ._utils import _Globals, _Pointer, _fields_repr, _resolve_type

if None:
    from dataclasses import dataclass as _union
else:
    from ._utils import _dummy as _union


# noinspection PyPep8Naming
@_union
class NOTIFYICONDATA_U:
    uTimeout: _type.UINT
    uVersion: _type.UINT


# noinspection PyPep8Naming
@_union
class DECIMAL_U:
    S: _struct.DECIMAL_U_S
    signscale: _type.USHORT


# noinspection PyPep8Naming
@_union
class DECIMAL_U2:
    s: _struct.DECIMAL_U2_S
    Lo64: _type.ULONGLONG


# noinspection PyPep8Naming
@_union
class PROPVARIANT_U_S_U:
    cVal: _type.CHAR
    bVal: _type.UCHAR
    iVal: _type.SHORT
    uiVal: _type.USHORT
    lVal: _type.LONG
    ulVal: _type.ULONG
    intVal: _type.INT
    uintVal: _type.UINT
    ...
    fltVal: _type.FLOAT
    dblVal: _type.DOUBLE
    ...
    pszVal: _type.LPSTR
    pwszVal: _type.LPWSTR
    ...


# noinspection PyPep8Naming
@_union
class PROPVARIANT_U:
    S: _struct.PROPVARIANT_U_S
    decVal: _struct.DECIMAL


# noinspection PyPep8Naming
@_union
class INPUT_U:
    mi: _struct.MOUSEINPUT
    ki: _struct.KEYBDINPUT
    hi: _struct.HARDWAREINPUT


# noinspection PyPep8Naming
@_union
class PICTDESC_U:
    bmp: _struct.PICTDESC_U_S
    wmf: _struct.PICTDESC_U_S2
    icon: _struct.PICTDESC_U_S3
    # noinspection PyProtectedMember
    if _const._WIN32:
        emf: _struct.PICTDESC_U_S4


# noinspection PyPep8Naming
@_union
class CHAR_INFO_U:
    UnicodeChar: _type.WCHAR
    AsciiChar: _type.CHAR


# noinspection PyPep8Naming
@_union
class VARIANT_U_S_U:
    llVal: _type.LONGLONG
    lVal: _type.LONG
    bVal: _type.BYTE
    iVal: _type.SHORT
    fltVal: _type.FLOAT
    dblVal: _type.DOUBLE
    boolVal: _type.VARIANT_BOOL
    VARIANT_BOOL: _type.VARIANT_BOOL
    scode: _type.SCODE
    ...
    bstrVal: _type.BSTR
    punkVal: _type.IUnknown
    pdispVal: _type.IDispatch
    ...
    pbVal: _Pointer[_type.BYTE]
    piVal: _Pointer[_type.SHORT]
    plVal: _Pointer[_type.LONG]
    pllVal: _Pointer[_type.LONGLONG]
    pfltVal: _Pointer[_type.FLOAT]
    pdblVal: _Pointer[_type.DOUBLE]
    ...
    byref: _type.PVOID
    cVal: _type.CHAR
    uiVal: _type.USHORT
    ulVal: _type.ULONG
    ullVal: _type.ULONGLONG
    intVal: _type.INT
    uintVal: _type.UINT
    pdecVal: _Pointer[_struct.DECIMAL]
    pcVal: _Pointer[_type.CHAR]
    puiVal: _Pointer[_type.USHORT]
    pulVal: _Pointer[_type.ULONG]
    pullVal: _Pointer[_type.ULONGLONG]
    pintVal: _Pointer[_type.INT]
    puintVal: _Pointer[_type.UINT]
    ...


# noinspection PyPep8Naming
@_union
class VARIANT_U:
    S: _struct.VARIANT_U_S
    decVal: _struct.DECIMAL


# noinspection PyPep8Naming
@_union
class LARGE_INTEGER:
    u: _struct.LARGE_INTEGER_S
    QuadPart: _type.LONGLONG


# noinspection PyPep8Naming
@_union
class ULARGE_INTEGER:
    u: _struct.ULARGE_INTEGER_S
    QuadPart: _type.ULONGLONG


# noinspection PyPep8Naming
@_union
class IMAGE_SECTION_HEADER_U:
    PhysicalAddress: _type.DWORD
    VirtualSize: _type.DWORD


# noinspection PyPep8Naming
@_union
class PROCESS_HEAP_ENTRY_U:
    Block: _struct.PROCESS_HEAP_ENTRY_U_S
    Region: _struct.PROCESS_HEAP_ENTRY_U_S2


# noinspection PyPep8Naming
@_union
class OVERLAPPED_U:
    S: _struct.OVERLAPPED_U_S
    Pointer: _type.PVOID


# noinspection PyPep8Naming
@_union
class SHELLEXECUTEINFO_U:
    hIcon: _type.HANDLE
    if _const.NTDDI_VERSION >= _const.NTDDI_WIN2K:
        hMonitor: _type.HANDLE


# noinspection PyPep8Naming
@_union
class PACKAGE_VERSION_U:
    Version: _type.UINT64
    S: _struct.PACKAGE_VERSION_U_S


# noinspection PyPep8Naming
@_union
class TYPEDESC_U:
    lptdesc: _Pointer[_struct.TYPEDESC]
    lpadesc: _Pointer[_struct.ARRAYDESC]
    hreftype: _type.HREFTYPE


# noinspection PyPep8Naming
@_union
class ELEMDESC_U:
    idldesc: _struct.IDLDESC
    paramdesc: _struct.PARAMDESC


# noinspection PyPep8Naming
@_union
class VARDESC_U:
    oInst: _type.ULONG
    lpvarValue: _Pointer[_struct.VARIANT]


# noinspection PyPep8Naming
@_union
class DISPLAYCONFIG_PATH_SOURCE_INFO_U:
    modeInfoIdx: _type.UINT32
    S: _struct.DISPLAYCONFIG_PATH_SOURCE_INFO_U_S


# noinspection PyPep8Naming
@_union
class DISPLAYCONFIG_PATH_TARGET_INFO_U:
    modeInfoIdx: _type.UINT32
    S: _struct.DISPLAYCONFIG_PATH_TARGET_INFO_U_S


# noinspection PyPep8Naming
@_union
class DISPLAYCONFIG_VIDEO_SIGNAL_INFO_U:
    AdditionalSignalInfo: _struct.DISPLAYCONFIG_VIDEO_SIGNAL_INFO_U_S
    videoStandard: _type.UINT32


# noinspection PyPep8Naming
@_union
class DISPLAYCONFIG_MODE_INFO_U:
    targetMode: _struct.DISPLAYCONFIG_TARGET_MODE
    sourceMode: _struct.DISPLAYCONFIG_SOURCE_MODE
    desktopImageInfo: _struct.DISPLAYCONFIG_DESKTOP_IMAGE_INFO


# noinspection PyPep8Naming
@_union
class DISPLAYCONFIG_TARGET_DEVICE_NAME_FLAGS_U:
    S: _struct.DISPLAYCONFIG_TARGET_DEVICE_NAME_FLAGS_U_S
    value: _type.UINT32


# noinspection PyPep8Naming
@_union
class MetafileHeader_U:
    WmfHeader: _struct.METAHEADER
    EmfHeader: _struct.ENHMETAHEADER3


# noinspection PyPep8Naming
@_union
class D2D_MATRIX_3X2_F_U:
    S: _struct.D2D_MATRIX_3X2_F_U_S
    S2: _struct.D2D_MATRIX_3X2_F_U_S2
    m: (_type.FLOAT * 2) * 3


# noinspection PyPep8Naming
@_union
class D2D_MATRIX_4X3_F_U:
    S: _struct.D2D_MATRIX_4X3_F_U_S
    m: (_type.FLOAT * 3) * 4


# noinspection PyPep8Naming
@_union
class D2D_MATRIX_4X4_F_U:
    S: _struct.D2D_MATRIX_4X4_F_U_S
    m: (_type.FLOAT * 4) * 4


# noinspection PyPep8Naming
@_union
class D2D_MATRIX_5X4_F_U:
    S: _struct.D2D_MATRIX_5X4_F_U_S
    m: (_type.FLOAT * 4) * 5


class _Union(_ctypes.Union):
    __repr__ = _fields_repr


def _init(item: str) -> type:
    return type(item, (_Union,), {'_fields_': tuple((name, _resolve_type(
        annot)) for name, annot in _typing.get_type_hints(_globals.vars_[item], _globals, _globals).items())})


_globals = _Globals()
