__version__ = '0.1.21'  # TODO overload func

import builtins as _builtins
import contextlib as _contextlib
import typing as _typing
from typing import Any as _Any
from typing import ContextManager as _ContextManager
from typing import Optional as _Optional
from typing import Type as _Type

from . import __head__
from . import _com as com
from . import _const as const
from . import _lib as lib
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


def init_guid(string: str, type_: _Type[CT]) -> _Optional[CT]:
    guid = type_()
    if type_ is struct.GUID:  # FIXME match
        init = lib.shell32.GUIDFromStringW
    elif type_ is struct.IID:
        init = lib.ole32.IIDFromString
    elif type_ is struct.CLSID:
        init = lib.ole32.CLSIDFromString
    else:
        return
    init(string, byref(guid))
    return guid


def _init_com(type_: _builtins.type[CT]) -> tuple[CT, Pointer[struct.CLSID], Pointer[struct.IID]]:
    lib.ole32.CoInitialize(None)
    return type_(), byref(init_guid(type_.__CLSID__, struct.CLSID)) if type_.__CLSID__ else Pointer(), byref(
        init_guid(getattr(const, f'IID_{type_.__name__}'), struct.IID))


# noinspection PyProtectedMember
def _del_com(obj: com._IUnknown) -> None:
    if obj:
        obj.Release()
    lib.ole32.CoInitialize(None)


@_contextlib.contextmanager
def create_com(type_: _builtins.type[CT]) -> _ContextManager[CT]:
    obj, clsid_ref, iid_ref = _init_com(type_)
    lib.ole32.CoCreateInstance(clsid_ref, None, const.CLSCTX_ALL, iid_ref, byref(obj))
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
