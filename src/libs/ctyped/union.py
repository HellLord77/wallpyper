from __future__ import annotations as _

import ctypes as _ctypes
import functools as _functools
from dataclasses import dataclass as _union

from . import const as _const, struct as _struct, type as _type
from ._head import _Globals, _Pointer, _resolve_type


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
class VARIANT_U_S_U:
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
class SHELLEXECUTEINFO_U:
    hIcon: _type.HANDLE
    if _const.NTDDI_VERSION >= _const.NTDDI_WIN2K:
        hMonitor: _type.HANDLE


def _init(item: str) -> type[_ctypes.Union]:
    _globals.check_item(item)

    class Union(_ctypes.Union):
        _fields_ = tuple((name, _resolve_type(type_)) for name, type_ in _globals.get_type_hints(item))

        def __repr__(self):
            return (f'{type(self).__name__}'
                    f'({", ".join(f"{item_[0]}={getattr(self, item_[0])}" for item_ in self._fields_)})')

    return _functools.update_wrapper(Union, _globals.vars_[item], updated=())


_globals = _Globals()
