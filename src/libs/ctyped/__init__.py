from __future__ import annotations as _

__version__ = '0.5.1'

import builtins as _builtins
import contextlib as _contextlib
import ctypes as _ctypes
import typing as _typing
from types import ModuleType as _ModuleType
from typing import ContextManager as _ContextManager
from typing import MutableSequence as _MutableSequence
from typing import Optional as _Optional

from . import const
from . import enum
from . import interface
from . import lib
from . import macro
from . import struct
from . import type
from . import union
from ._utils import _CT as CT
from ._utils import _Pointer as Pointer
from ._utils import _addressof as addressof
from ._utils import _byref as byref
from ._utils import _cast as cast
from ._utils import _cast_int as cast_int
from ._utils import _is_unsigned as is_unsigned
from ._utils import _pointer as pointer
from ._utils import _sizeof as sizeof
from .const import python as _const_python
from .lib import msvcrt as _msvcrt
from .lib import python as _python
from .lib import shell32 as _shell32


# noinspection PyShadowingBuiltins,PyShadowingNames
def from_address(address: int, type: _builtins.type[CT]) -> CT:
    return type.from_address(address)


@_contextlib.contextmanager
def buffer(size: int = 0) -> _ContextManager[_Optional[int]]:
    ptr = _msvcrt.malloc(size)
    try:
        yield ptr or None
    finally:
        _msvcrt.free(ptr)


# noinspection PyShadowingBuiltins,PyShadowingNames
def array(*elements, type: _Optional[_builtins.type[CT]] = None,
          size: _Optional[int] = None) -> _MutableSequence[CT] | Pointer[CT]:
    if type is None:
        type = _builtins.type(elements[0])
    if size is None:
        size = len(elements)
    return (type * size)(*elements)


@_typing.overload
def char_array(string: bytes = b'', size: _Optional[int] = None) -> Pointer[type.c_char]:
    pass


@_typing.overload
def char_array(string: str = '', size: _Optional[int] = None) -> Pointer[type.c_wchar]:
    pass


def char_array(string='', size=None):
    if size is not None:
        size -= 1
        string = string[:size] + (b'\0' if isinstance(string, bytes) else '\0') * (size - len(string))
    return ((type.c_char if isinstance(string, bytes) else type.c_wchar) * (len(string) + 1))(*string)


# noinspection PyShadowingNames
def resize_array(array: Pointer[CT], size: int) -> Pointer[CT]:
    # noinspection PyProtectedMember
    return (array._type_ * size).from_address(addressof(array))


@_contextlib.contextmanager
def py_buffer(obj) -> _ContextManager[struct.Py_buffer]:
    view = struct.Py_buffer()
    _python.PyObject_GetBuffer(obj, byref(view), _const_python.PyBUF_SIMPLE)
    try:
        yield view
    finally:
        _python.PyBuffer_Release(byref(view))


def get_interface_name(iid: str, base: _builtins.type | _ModuleType = const) -> _Optional[str]:
    for var, val in vars(base).items():
        if isinstance(val, _builtins.type):
            if (name := get_interface_name(iid, val)) is not None:
                return name
        elif iid == val:
            return var.removeprefix('IID_')


def addressof_func(func) -> int:
    return _ctypes.cast(func, _ctypes.c_void_p).value


def get_guid(string: str) -> struct.GUID:  # TODO class GUID
    guid = struct.GUID()
    _shell32.GUIDFromStringW(string, byref(guid))
    return guid


def get_hresult(hresult: int) -> int:
    return type.HRESULT(hresult).value
