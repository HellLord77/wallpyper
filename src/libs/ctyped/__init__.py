from __future__ import annotations as _

__version__ = '0.3.0'

import builtins as _builtins
import contextlib as _contextlib
import ctypes as _ctypes
import functools as _functools
import types as _types
import typing as _typing
from typing import (Any as _Any, Callable as _Callable, ContextManager as _ContextManager,
                    Final as _Final, Iterable as _Iterable,
                    Mapping as _Mapping, MutableSequence as _MutableSequence, Optional as _Optional)

from . import const
from . import enum
from . import handle
from . import interface
from . import lib
from . import macro
from . import struct
from . import type
from . import union
from ._utils import (_CT as CT, _Pointer as Pointer, _get_winrt_class_name, _addressof as addressof,
                     _byref as byref, _cast as cast, _cast_int as cast_int, _pointer as pointer, _sizeof as sizeof)

FLAG_THREADED_COM = False

NULLPTR: _Final = None


# noinspection PyShadowingBuiltins,PyShadowingNames
def from_address(address: int, type: _builtins.type[CT]) -> CT:
    return type.from_address(address)


@_contextlib.contextmanager
def buffer(size: int = 0) -> _ContextManager[_Optional[int]]:
    ptr = lib.msvcrt.malloc(size)
    try:
        yield ptr or None
    finally:
        lib.msvcrt.free(ptr)


# noinspection PyShadowingBuiltins,PyShadowingNames
def array(*elements: _Any, type: _Optional[_builtins.type[CT]] = None,
          size: _Optional[int] = None) -> _MutableSequence[CT] | Pointer[CT]:
    return ((_builtins.type(elements[0]) if type is None else type) * (
        len(elements) if size is None else size))(*elements)


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


def get_interface_name(iid: str, base: _builtins.type | _types.ModuleType = const) -> _Optional[str]:
    for var, val in vars(base).items():
        if isinstance(val, _builtins.type):
            if name := get_interface_name(iid, val):
                return name
        elif iid == val:
            return var.removeprefix('IID_')


# noinspection PyProtectedMember,PyShadowingNames
def set_result_checker(lib: lib._CDLLMeta, callback: _Optional[_Callable[[_Any, _Callable, tuple], _Any]] = None,
                       args: _Optional[_Iterable] = None, kwargs: _Optional[_Mapping[str, _Any]] = None):
    if args is None:
        args = ()
    if kwargs is None:
        kwargs = {}

    @_functools.wraps
    def errcheck(res, *args_):
        callback(res, *args_, *args, **kwargs)
        return res

    lib._errcheck = errcheck
    # noinspection PyUnresolvedReferences
    if lib._funcs:
        # noinspection PyUnresolvedReferences
        for func in set(lib._funcs).intersection(dir(lib)):
            getattr(lib, func).errcheck = errcheck


# noinspection PyShadowingBuiltins,PyShadowingNames
def create_handler(handler: _Callable[[...], type.HRESULT], type: _builtins.type[CT], name: _Optional[str] = None) -> CT:
    args = getattr(type, '_args', None)
    impl_name = type.__name__
    if args is not None:
        impl_name = impl_name.split("_", 1)[0]
    impl_name = f'{impl_name}_impl'
    impl = getattr(type.__module__, impl_name)
    if args is not None:
        impl = impl[tuple(args.values())]
    return cast(_builtins.type(f'{type.__name__}<{handler.__name__}>'
                               if name is None else name, (impl,), {'Invoke': staticmethod(handler)})(), type)


# noinspection PyProtectedMember
def get_lib_path(library: lib._OleDLLMeta | lib._PyDLLMeta | lib._WinDLLMeta) -> str:
    buff = type.LPWSTR('\0' * const.MAX_PATH)
    # noinspection PyUnresolvedReferences
    lib.kernel32.GetModuleFileNameW(library._lib._handle, buff, const.MAX_PATH)
    return buff.value


def addressof_func(func) -> int:
    return _ctypes.cast(func, _ctypes.c_void_p).value


def get_guid(string: str) -> struct.GUID:  # TODO class GUID
    guid = struct.GUID()
    lib.shell32.GUIDFromStringW(string, byref(guid))
    return guid


def get_hresult(hresult: int) -> int:
    return type.HRESULT(hresult).value
