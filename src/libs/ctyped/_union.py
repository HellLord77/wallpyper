import ctypes as _ctypes
import dataclasses as _dataclasses
import functools as _functools
import typing as _typing

from . import _const
from . import _struct
from . import _type
from .__head__ import _Globals
from .__head__ import _resolve_type


# noinspection PyPep8Naming
@_dataclasses.dataclass
class NOTIFYICONDATA_U:
    uTimeout: _type.UINT = None
    uVersion: _type.UINT = None


# noinspection PyPep8Naming
@_dataclasses.dataclass
class DECIMAL_U:
    S: _struct.DECIMAL_U_S = None
    signscale: _type.USHORT = None


# noinspection PyPep8Naming
@_dataclasses.dataclass
class DECIMAL_U2:
    s: _struct.DECIMAL_U2_S = None
    Lo64: _type.ULONGLONG = None


# noinspection PyPep8Naming
@_dataclasses.dataclass
class PROPVARIANT_U_S_U:
    cVal: _type.CHAR = None
    bVal: _type.UCHAR = None
    iVal: _type.SHORT = None
    uiVal: _type.USHORT = None
    lVal: _type.LONG = None
    ulVal: _type.ULONG = None
    intVal: _type.INT = None
    uintVal: _type.UINT = None
    ...
    fltVal: _type.FLOAT = None
    dblVal: _type.DOUBLE = None
    ...
    pszVal: _type.LPSTR = None
    pwszVal: _type.LPWSTR = None
    ...


# noinspection PyPep8Naming
@_dataclasses.dataclass
class INPUT_U:
    mi: _struct.MOUSEINPUT = None
    ki: _struct.KEYBDINPUT = None
    hi: _struct.HARDWAREINPUT = None


# noinspection PyPep8Naming
@_dataclasses.dataclass
class PICTDESC_U:
    bmp: _struct.PICTDESC_U_S = None
    wmf: _struct.PICTDESC_U_S2 = None
    icon: _struct.PICTDESC_U_S3 = None
    # noinspection PyProtectedMember
    if _const._WIN32:
        emf: _struct.PICTDESC_U_S4 = None


def _init(name: str) -> type[_ctypes.Union]:
    _globals.has_item(name)

    class Wrapper(_ctypes.Union):
        _fields_ = tuple((name_, _resolve_type(type_))
                         for name_, type_ in _typing.get_type_hints(_globals.vars_[name], _globals).items())

        def __repr__(self):
            return f'{type(self).__name__}' \
                   f'({", ".join(f"{item[0]}={getattr(self, item[0])}" for item in self._fields_)})'

    return _functools.update_wrapper(Wrapper, _globals.vars_[name], updated=())


_globals = _Globals()
