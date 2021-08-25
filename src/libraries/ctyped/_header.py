from __future__ import annotations as _

import ctypes as _ctypes
import typing as _typing
from typing import Any as _Any
from typing import Callable as _Callable
from typing import Generator as _Generator
from typing import Generic as _Generic
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


class Dict(dict):
    def __init__(self, globals_, getattr_):
        self.globals = globals_
        self.getattr = getattr_
        super().__init__(globals_)

    def __getitem__(self, item: str):
        if item not in self:
            self.getattr(item)
        return super().__getitem__(item)

    def __setitem__(self, key: str, value):
        self.globals[key] = value
        super().__setitem__(key, value)


def init(globals_: dict[str, _Any]) -> dict[str, _Any]:
    backup = dict(items(globals_))
    for var in backup:
        del globals_[var]
    return backup


def items(vars_: dict[str, _Any]) -> _Generator[tuple[str, _Any], None, None]:
    for var, val in vars_.items():
        if not var.startswith('_'):
            yield var, val


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


def cast(obj: _Any,
         type_: type[T] | T) -> Pointer[T]:
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
