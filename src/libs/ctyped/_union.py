import ctypes as _ctypes
import dataclasses as _dataclasses
import functools as _functools
import typing as _typing

from . import _struct
from . import _type
from .__head__ import _Globals
from .__head__ import _resolve_type


# noinspection PyPep8Naming
@_dataclasses.dataclass
class NOTIFYICONDATA_u:
    uTimeout: _type.UINT = None
    uVersion: _type.UINT = None


# noinspection PyPep8Naming
@_dataclasses.dataclass
class DECIMAL_u:
    s: _struct.DECIMAL_u_s = None
    signscale: _type.USHORT = None


# noinspection PyPep8Naming
@_dataclasses.dataclass
class DECIMAL_u2:
    s: _struct.DECIMAL_u2_s = None
    Lo64: _type.ULONGLONG = None


# noinspection PyPep8Naming
@_dataclasses.dataclass
class tag_inner_PROPVARIANT_u:
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
class INPUT_u:
    mi: _struct.MOUSEINPUT = None
    ki: _struct.KEYBDINPUT = None
    hi: _struct.HARDWAREINPUT = None


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
