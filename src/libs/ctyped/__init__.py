__version__ = '0.2.0'

import builtins as _builtins
import contextlib as _contextlib
import time
import typing as _typing
from typing import Any as _Any
from typing import ContextManager as _ContextManager
from typing import Optional as _Optional
from typing import Union as _Union

from . import __head__
from . import _com as com
from . import _const as const
from . import _func as func
from . import _handle as handle
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


def get_guid(string: str) -> struct.GUID:
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
        func.ole32.CoUninitialize()


@_contextlib.contextmanager
def init_com(type_: _builtins.type[CT], init: _Optional[bool] = True) -> _ContextManager[_Optional[CT]]:
    with _prep_com(type_) as (obj, clsid_ref, args):
        yield obj if not init or macro.SUCCEEDED(
            func.ole32.CoCreateInstance(clsid_ref, None, const.CLSCTX_ALL, *args)) else None


# noinspection PyProtectedMember
@_contextlib.contextmanager
def conv_com(type_: _builtins.type[CT], obj: com._IUnknown) -> _ContextManager[_Optional[CT]]:
    with _prep_com(type_) as (obj_, _, args):
        if macro.SUCCEEDED(obj.QueryInterface(*args)):
            yield obj_
        else:
            yield None


@_contextlib.contextmanager
def _prep_winrt(type_: _builtins.type[CT]) -> \
        _ContextManager[tuple[type.HSTRING, Pointer[struct.IID], Pointer[com.IActivationFactory]]]:
    func.combase.RoInitialize(const.RO_INIT_SINGLETHREADED)
    factory = com.IActivationFactory()
    try:
        yield handle.HSTRING.from_string(type_.__RuntimeClass__), macro.__uuidof(type_.__name__), factory
    finally:
        if factory:
            factory.Release()
        func.combase.RoUninitialize()


@_contextlib.contextmanager
def get_winrt(type_: _builtins.type[CT]) -> _ContextManager[_Optional[_builtins.type[CT]]]:
    with _prep_winrt(type_) as (*args, factory):
        if macro.SUCCEEDED(func.combase.RoGetActivationFactory(*args, byref(factory))):
            with conv_com(type_, factory) as obj:
                yield obj
        else:
            yield None


def wait_for(async_: _Union[com.IAsyncAction, com.IAsyncOperation],
             obj_ref: _Optional[Pointer[CT]] = None, timeout: float = 5) -> bool:
    args = () if obj_ref is None else (obj_ref,)
    end = time.time() + timeout
    while end > time.time():
        try:
            async_.GetResults(*args)
        except OSError:
            pass
        else:
            return True
    return False
