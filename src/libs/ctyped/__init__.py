__version__ = '0.1.25'  # TODO overload func

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
from . import _macro as macro
from . import _struct as struct
# noinspection PyShadowingBuiltins
from . import _type as type
from . import _union as union
from .__head__ import _CT as CT
from .__head__ import _Pointer as Pointer
from .__head__ import _addressof as addressof
from .__head__ import _byref as byref
from .__head__ import _cast as cast
from .__head__ import _pointer as pointer
from .__head__ import _sizeof as sizeof


def array(type_: _builtins.type[CT] = type.c_void_p, *elements: _Any, size: _Optional[int] = None) -> Pointer[CT]:
    return (type_ * (size or len(elements)))(*elements)


@_typing.overload
def char_array(string: bytes) -> Pointer[type.c_char]:
    pass


@_typing.overload
def char_array(string: str) -> Pointer[type.c_wchar]:
    pass


def char_array(string):
    return ((type.c_char if isinstance(string, bytes) else type.c_wchar) * (len(string) + 1))(*string)


def get_guid(string: str) -> _Optional[CT]:
    guid = struct.GUID()
    func.shell32.GUIDFromStringW(string, byref(guid))
    return guid


@_contextlib.contextmanager
def _prep_com(type_: _builtins.type[CT]) -> \
        _ContextManager[tuple[CT, Pointer[struct.CLSID], tuple[Pointer[struct.IID], Pointer[CT]]]]:
    func.ole32.CoInitialize(None)
    obj = type_()
    try:
        yield obj, byref(get_guid(type_.__CLSID__)) if type_.__CLSID__ else None, macro.IID_PPV_ARGS(obj)
    finally:
        if obj:
            obj.Release()
        func.ole32.CoInitialize(None)


@_contextlib.contextmanager
def create_com(type_: _builtins.type[CT], init: _Optional[bool] = True) -> _ContextManager[_Optional[CT]]:
    with _prep_com(type_) as (obj, clsid_ref, args):
        if not init or macro.SUCCEEDED(func.ole32.CoCreateInstance(clsid_ref, None, const.CLSCTX_ALL, *args)):
            yield obj
        else:
            yield None


# noinspection PyProtectedMember
@_contextlib.contextmanager
def convert_com(type_: _builtins.type[CT], obj: com._IUnknown) -> _ContextManager[_Optional[CT]]:
    with _prep_com(type_) as (obj_, _, args):
        if macro.SUCCEEDED(obj.QueryInterface(*args)):
            yield obj_
        else:
            yield None
