from __future__ import annotations as _

import ctypes as _ctypes
import typing as _typing

from . import const as _const, struct as _struct, type as _type
from ._utils import _Globals, _Pointer, _fields_repr, _resolve_type

if None:
    from dataclasses import dataclass as _union
else:
    from ._utils import _decorator as _union


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
class PROPVARIANT_U_S_U:  # TODO
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
class VARIANT_U_S_U:  # TODO
    llVal: _type.LONGLONG
    lVal: _type.LONG
    bVal: _type.BYTE
    iVal: _type.SHORT
    fltVal: _type.FLOAT
    dblVal: _type.DOUBLE
    ...
    bstrVal: _type.BSTR
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
    S: _struct.LARGE_INTEGER_S
    QuadPart: _type.LONGLONG


# noinspection PyPep8Naming
@_union
class ULARGE_INTEGER:
    S: _struct.ULARGE_INTEGER_S
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


class _Union(_ctypes.Union):
    __repr__ = _fields_repr


def _init(item: str) -> type:
    return type(item, (_Union,), {'_fields_': tuple((name, _resolve_type(
        annot)) for name, annot in _typing.get_type_hints(_globals.vars_[item], _globals, _globals).items())})


_globals = _Globals()
