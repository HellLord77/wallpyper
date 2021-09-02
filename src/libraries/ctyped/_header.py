import ctypes as _ctypes
import inspect as _inspect
import types as _types
import typing as _typing
from typing import Any as _Any
from typing import Callable as _Callable
from typing import Generator as _Generator
from typing import Generic as _Generic
from typing import NoReturn as _NoReturn
from typing import Optional as _Optional
from typing import Sequence as _Sequence
from typing import Union as _Union

INIT = False
T = _typing.TypeVar('T')


class Pointer(_Generic[T]):
    contents: T
    value: T


# noinspection PyAbstractClass
class Array(Pointer, _Sequence[T]):
    pass


class Globals(dict):
    def __init__(self):
        self.module = _inspect.getmodule(_inspect.currentframe().f_back)
        self.annotations = None
        self.base = {var: val for var, val in vars(self.module).items() if not var.startswith('_')}
        for var in self.base:
            delattr(self.module, var)
        super().__init__(vars(self.module))

    def __getitem__(self, item: str):
        if item not in self:
            return getattr(self.module, item)
        return super().__getitem__(item)

    def __setitem__(self, key: str, value):
        val = self.base[key]
        for key_ in self.iter_base():
            if self.base[key_] is val:
                setattr(self.module, key_, value)
                super().__setitem__(key_, value)
                del self.base[key_]

    def iter_base(self) -> _Generator[str, None, None]:
        for item in tuple(self.base):
            if item in self.base:
                yield item

    def has_item(self, item: str) -> _NoReturn:
        if item not in self.base:
            getattr(_types.ModuleType(_inspect.getmodule(_inspect.currentframe().f_back).__name__), item)

    def get_annotation(self, item: str) -> _Any:
        if not self.annotations:
            self.annotations = _typing.get_type_hints(self.module)
        val = self.base[item]
        for key in self.iter_base():
            if self.base[key] is val and key in self.annotations:
                return self.annotations[key]


def sizeof(obj: T) -> int:
    return _ctypes.sizeof(obj)


def byref(obj: T) -> Pointer[T]:
    # noinspection PyTypeChecker
    return _ctypes.byref(obj)


@_typing.overload
def pointer(obj: T) -> Pointer[T]:
    pass


@_typing.overload
def pointer(type_: type[T]) -> type[Pointer[type[T]]]:
    pass


def pointer(obj):
    try:
        return _ctypes.pointer(obj)
    except TypeError:
        return _ctypes.POINTER(obj)


def cast(obj: _Any, type_: _Union[type[T], T]) -> Pointer[T]:
    try:
        return _ctypes.cast(obj, type_)
    except _ctypes.ArgumentError:
        return cast(_ctypes.byref(obj), type_)
    except TypeError:
        return cast(obj, _ctypes.POINTER(type_))


def get_doc(name: str, restype, argtypes: tuple) -> str:
    return f'{name}({", ".join(type_.__name__ for type_ in argtypes)}) -> {getattr(restype, "__name__", restype)}'


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
        if _typing.get_origin(type_) is type:
            type_ = _typing.get_args(type_)[0]
        if _typing.get_origin(type_) is Pointer:
            type_ = _ctypes.POINTER(resolve_type(_typing.get_args(type_)[0]))
    return type_


'''
def _import(import_, *args, **kwargs):
    print(args[3])
    return import_(*args, **kwargs)


_builtins.__import__ = _types.MethodType(_import, __import__)
'''
