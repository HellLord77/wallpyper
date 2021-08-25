__version__ = '0.1.2'  # TODO: disable lazy init

import builtins as _builtins
import contextlib as _contextlib
import functools as _functools
import typing as _typing
from typing import Any as _Any
from typing import ContextManager as _ContextManager
from typing import Optional as _Optional

from . import _com as com
from . import _const as const
# noinspection PyShadowingBuiltins
from . import _ctype as type
from . import _func as func
from . import _header
from . import _lib
from . import _macro as macro
from . import _struct as struct
from ._header import byref
from ._header import cast
from ._header import pointer
from ._header import sizeof


def array(type_: _builtins.type[_header.T] = type.c_void_p,
          *elements: _Any,
          size: _Optional[int] = None) -> _header.Array[_header.T]:
    return (type_ * (size or len(elements)))(*elements)


@_typing.overload
def char_array(string: bytes) -> _header.Array[type.c_char]:
    pass


@_typing.overload
def char_array(string: str) -> _header.Array[type.c_wchar]:
    pass


def char_array(string):
    return ((type.c_char if isinstance(string, bytes) else type.c_wchar) * (len(string) + 1))(*string)


@_functools.cache
def _get_refs(type_: _builtins.type[com.IUnknown]) -> tuple[_header.Pointer[struct.CLSID], _header.Pointer[struct.IID]]:
    clsid_ref = byref(struct.CLSID())
    func.CLSIDFromString(type_.__CLSID__, clsid_ref)
    iid_ref = byref(struct.IID())
    func.IIDFromString(getattr(const, f'IID_{type_.__name__}'), iid_ref)
    return clsid_ref, iid_ref


@_contextlib.contextmanager
def create_com(type_: _builtins.type[_header.T]) -> _ContextManager[_header.T]:
    obj: com.IUnknown = type_()
    func.CoInitialize(None)
    try:
        refs = _get_refs(type_)
        func.CoCreateInstance(refs[0], None, const.CLSCTX_ALL, refs[1], byref(obj))
        yield obj
    finally:
        if obj:
            obj.Release()
        func.CoUninitialize()
