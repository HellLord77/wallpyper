__version__ = '0.1.17'  # TODO: overload func

import builtins as _builtins
import contextlib as _contextlib
import typing as _typing
from typing import Any as _Any
from typing import ContextManager as _ContextManager
from typing import Optional as _Optional

from . import __head__
from . import _com as com
from . import _const as const
from . import _func as func
from . import _lib
from . import _macro as macro
from . import _struct as struct
# noinspection PyShadowingBuiltins
from . import _type as type
from . import _union as union
from .__head__ import _Array as Array
from .__head__ import _CT as CT
from .__head__ import _Pointer as Pointer
from .__head__ import _byref as byref
from .__head__ import _cast as cast
from .__head__ import _pointer as pointer
from .__head__ import _sizeof as sizeof


def array(type_: _builtins.type[CT] = type.c_void_p, *elements: _Any, size: _Optional[int] = None) -> Array[CT]:
    return (type_ * (size or len(elements)))(*elements)


@_typing.overload
def char_array(string: bytes) -> Array[type.c_char]:
    pass


@_typing.overload
def char_array(string: str) -> Array[type.c_wchar]:
    pass


def char_array(string):
    return ((type.c_char if isinstance(string, bytes) else type.c_wchar) * (len(string) + 1))(*string)


def _init_com(type_: _builtins.type[CT]) -> tuple[CT, Pointer[struct.CLSID], Pointer[struct.IID]]:
    clsid_ref = Pointer()
    if type_.__CLSID__:
        clsid_ref = byref(struct.CLSID())
        func.CLSIDFromString(type_.__CLSID__, clsid_ref)
    iid_ref = byref(struct.IID())
    func.IIDFromString(getattr(const, f'IID_{type_.__name__}'), iid_ref)
    func.CoInitialize(None)
    return type_(), clsid_ref, iid_ref


# noinspection PyProtectedMember
def _del_com(obj: com._IUnknown) -> None:
    if obj:
        obj.Release()
    func.CoInitialize(None)


@_contextlib.contextmanager
def create_com(type_: _builtins.type[CT]) -> _ContextManager[CT]:
    obj, clsid_ref, iid_ref = _init_com(type_)
    func.CoCreateInstance(clsid_ref, None, const.CLSCTX_ALL, iid_ref, byref(obj))
    try:
        yield obj
    finally:
        _del_com(obj)


# noinspection PyProtectedMember
@_contextlib.contextmanager
def convert_com(obj: com._IUnknown, to: _builtins.type[CT]) -> _ContextManager[CT]:
    obj_, _, iid_ref = _init_com(to)
    obj.QueryInterface(iid_ref, byref(obj_))
    try:
        yield obj_
    finally:
        _del_com(obj_)
