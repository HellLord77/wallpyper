from __future__ import annotations as _

import ctypes as _ctypes
import inspect as _inspect
import types as _types
import typing as _typing
from typing import Any as _Any
from typing import Callable as _Callable
from typing import Generic as _Generic
from typing import NoReturn as _NoReturn
from typing import Optional as _Optional
from typing import Sequence as _Sequence

INIT = False
T = _typing.TypeVar('T')


class Pointer(_Generic[T]):
    contents: T
    value: T


# noinspection PyAbstractClass
class Array(Pointer, _Sequence[T]):
    pass


class Globals(dict):
    def __init__(self, base: dict[str, _Any], globals_, getattr_):
        self.base = base
        self.globals = globals_
        self.getattr = getattr_
        super().__init__(globals_)

    def __getitem__(self, item: str):
        if item not in self:
            return self.getattr(item)
        return super().__getitem__(item)

    def __setitem__(self, key: str, value):
        val = self.base[key]
        for key_ in tuple(self.base):
            if self.base[key_] is val:
                self.globals[key] = value
                super().__setitem__(key, value)

    def hasattr(self, key: str) -> _NoReturn:
        if key not in getattr(self, 'base', self):
            getattr(_types.ModuleType(_inspect.getmodule(_inspect.currentframe().f_back).__name__), key)


def get_doc(name: str, restype, argtypes: tuple) -> str:
    return f'{name}({", ".join(type_.__name__ for type_ in argtypes)}) -> {getattr(restype, "__name__", restype)}'


def init(globals_: dict[str, _Any]) -> dict[str, _Any]:
    backup = {var: val for var, val in globals_.items() if not var.startswith('_')}
    for var in backup:
        del globals_[var]
    return backup


def resolve_type(type_: _Any) -> _Any:
    if isinstance(type_, type(_Callable)):
        type_ = [None]
    elif isinstance(type_, type(_Callable[[], None])):
        types_ = _typing.get_args(type_)
        type_ = [resolve_type(types_[1])]
        type_.extend(resolve_type(type_) for type_ in types_[0])
    else:
        if isinstance(type_, type(_Optional[object])):
            type_ = _typing.get_args(type_)[0]
        if _typing.get_origin(type_) is Pointer:
            type_ = _ctypes.POINTER(resolve_type(_typing.get_args(type_)[0]))
    return type_


def byref(obj: T) -> Pointer[T]:
    # noinspection PyTypeChecker
    return _ctypes.byref(obj)


def cast(obj: _Any, type_: type[T] | T) -> Pointer[T]:
    try:
        return _ctypes.cast(obj, type_)
    except _ctypes.ArgumentError:
        return cast(_ctypes.byref(obj), type_)
    except TypeError:
        return cast(obj, _ctypes.POINTER(type_))


def pointer(type_: T | type[T]) -> Pointer[T]:
    try:
        # noinspection PyTypeChecker
        return _ctypes.pointer(type_)
    except TypeError:
        # noinspection PyTypeChecker
        return _ctypes.POINTER(type_)


def sizeof(obj: T) -> int:
    return _ctypes.sizeof(obj)
