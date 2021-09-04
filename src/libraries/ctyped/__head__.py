import ctypes as _ctypes
import gc as _gc
import importlib as _importlib
import inspect as _inspect
import os as _os
import pkgutil as _pkgutil
import sys as _sys
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


class Module:
    def __init__(self, name: str):
        self.name = name

    def __getattribute__(self, item: str):
        name = super().__getattribute__('name')
        del _sys.modules[name]
        module = _importlib.import_module(*_os.path.splitext(name)[::-1])
        for vars_ in _gc.get_referrers(self):
            for var, val in vars_.items():
                if val is self:
                    vars_[var] = module


class Globals(dict):
    def __init__(self):
        self.annotations = None
        self.module = _inspect.getmodule(_inspect.currentframe().f_back)
        self.vars_ = {var: val for var, val in vars(self.module).items() if not var.startswith('_')}
        for var in self.vars_:
            delattr(self.module, var)
        super().__init__(vars(self.module))
        self.module.__getattr__ = self.__getitem__
        if INIT:
            self.module._globals = self
            for var in self.iter_vars():
                getattr(self.module, var)

    def __getitem__(self, item: str):
        if item not in self:
            # noinspection PyProtectedMember,PyUnresolvedReferences
            self[item] = self.module._init(item)
        return super().__getitem__(item)

    def __setitem__(self, key: str, value: T) -> T:
        val = self.vars_[key]
        for key_ in self.iter_vars():
            if self.vars_[key_] is val:
                setattr(self.module, key_, value)
                del self.vars_[key_]
                super().__setitem__(key_, value)
        return value

    def iter_vars(self) -> _Generator[str, None, None]:
        for item in tuple(self.vars_):
            if item in self.vars_:
                yield item

    def has_item(self, item: str) -> _NoReturn:
        if item not in self.vars_:
            raise AttributeError(f"module '{self.module.__name__}' has no attribute '{item}'")

    def get_annotation(self, item: str) -> _Any:
        if not self.annotations:
            self.annotations = _typing.get_type_hints(self.module)
        val = self.vars_[item]
        for key in self.iter_vars():
            if self.vars_[key] is val and key in self.annotations:
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


def get_doc(name: str, restype: _Any, argtypes: tuple) -> str:
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


def _init():
    for module in _pkgutil.iter_modules((_os.path.dirname(__file__),), f'{__package__}.'):
        if module.name not in _sys.modules:
            # noinspection PyTypeChecker
            _sys.modules[module.name] = Module(module.name)


_init()
