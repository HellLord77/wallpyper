from __future__ import annotations  # TODO: remove if >= 3.11

__version__ = '0.1.0'

import contextlib as _contextlib
import functools as _functools
import typing as _typing

from . import _com as com
from . import _const as const
from . import _ctype as ctype
from . import _func as func
from . import _header
from . import _lib
from . import _macro as macro
from . import _struct as struct
from ._header import byref, cast, POINTER, pointer, sizeof


def array(type_: _header.CT = ctype.c_void_p,
          *elements: _typing.Any,
          size: _typing.Optional[int] = None) -> _header.Array[_header.CT]:
    return (type_ * (size or len(elements)))(*elements)


def char_array(obj: str,
               type_: _header.CT = ctype.c_wchar) -> _header.Array[_header.CT]:
    return (type_ * (len(obj) + 1))(*obj)


@_functools.cache
def _get_refs(type_: type[com.IUnknown]) -> tuple[_header.Pointer[struct.CLSID], _header.Pointer[struct.IID]]:
    clsid_ref = byref(struct.CLSID())
    # noinspection PyProtectedMember
    func.CLSIDFromString(type_._CLSID, clsid_ref)
    iid_ref = byref(struct.IID())
    func.IIDFromString(getattr(const, f'IID_{type_.__name__}'), iid_ref)
    return clsid_ref, iid_ref


@_contextlib.contextmanager
def init_com(type_: type[_header.CT]) -> _typing.ContextManager[_header.CT]:
    obj = type_()
    func.CoInitialize(None)
    try:
        refs = _get_refs(type_)
        func.CoCreateInstance(refs[0], None, const.CLSCTX_ALL, refs[1], byref(obj))
        yield obj
    finally:
        if obj:
            obj.Release()
        func.CoUninitialize()
