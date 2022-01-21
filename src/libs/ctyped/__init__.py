__version__ = '0.1.22'  # TODO overload func

import builtins as _builtins
import contextlib as _contextlib
import typing as _typing
from typing import Any as _Any
from typing import Callable as _Callable
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
    if type_ is struct.GUID:  # FIXME match (py 3.10)
        init = lib.shell32.GUIDFromStringW
    elif type_ is struct.IID:
        init = lib.ole32.IIDFromString
    elif type_ is struct.CLSID:
        init = lib.ole32.CLSIDFromString
    else:
        return
    init(string, byref(guid))
    return guid


@_contextlib.contextmanager
def _prep_com(type_: _builtins.type[CT]) -> \
        _ContextManager[tuple[CT, Pointer[struct.CLSID], tuple[Pointer[struct.IID], Pointer[CT]]]]:
    lib.ole32.CoInitialize(None)
    obj = type_()
    try:
        yield obj, byref(init_guid(type_.__CLSID__, struct.CLSID)) if type_.__CLSID__ else None, macro.IID_PPV_ARGS(obj)
    finally:
        if obj:
            obj.Release()
        lib.ole32.CoInitialize(None)


@_contextlib.contextmanager
def create_com(type_: _builtins.type[CT], creator: _Optional[_Callable] = lib.ole32.CoCreateInstance,
               first_arg: _Any = None, flag: _Optional[type.DWORD] = const.CLSCTX_ALL) -> _ContextManager[CT]:
    with _prep_com(type_) as (obj, clsid_ref, args):
        if creator is not None:
            creator(clsid_ref if first_arg is None else first_arg, None, *() if flag is None else (flag,), *args)
        yield obj


# noinspection PyProtectedMember
@_contextlib.contextmanager
def convert_com(type_: _builtins.type[CT], obj: com._IUnknown) -> _ContextManager[CT]:
    with _prep_com(type_) as (obj_, _, args):
        obj.QueryInterface(*args)
        yield obj_
