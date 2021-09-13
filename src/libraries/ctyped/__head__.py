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
DEBUG = True
CT = _typing.TypeVar('CT')


class Pointer(_Generic[CT]):
    contents: CT
    value: CT


# noinspection PyAbstractClass
class Array(Pointer, _Sequence[CT]):
    pass


class Module:
    __spec__ = None
    module = None

    def __init__(self, name: str):
        self.name = name

    def __getattribute__(self, item):
        if item in ('__spec__', '__class__', 'module', 'name'):
            return super().__getattribute__(item)
        if not self.module:
            del _sys.modules[self.name]
            self.module = _importlib.import_module(*_os.path.splitext(self.name)[::-1])
            replace_object(self, self.module)
        return getattr(self.module, item)


class Globals(dict):
    annotations = None

    def __init__(self, once: _Optional[bool] = None):
        self.once = once
        self.module = _inspect.getmodule(_inspect.currentframe().f_back)
        self.vars_ = {var: val for var, val in vars(self.module).items() if not var.startswith('_')}
        for var in self.vars_:
            delattr(self.module, var)
        super().__init__(vars(self.module))
        self.module.__getattr__ = self.__getitem__
        if INIT:
            self.module._globals = self  # TODO: execute after __init__
            for var in self.iter_vars():
                getattr(self.module, var)

    def __getitem__(self, item: str):
        try:
            return super().__getitem__(item)
        except KeyError:
            # noinspection PyProtectedMember,PyUnresolvedReferences
            val = self.module._init(item)
            self[item] = val
            return val

    def __setitem__(self, key, value):
        try:
            val = self.vars_[key]
        except KeyError:
            return
        else:
            if self.once:
                self.setitem(key, value)
            else:
                for key_ in self.iter_vars():
                    if self.vars_[key_] is val:
                        self.setitem(key_, value)

    def setitem(self, key: str, value) -> None:
        setattr(self.module, key, value)
        del self.vars_[key]
        super().__setitem__(key, value)

    def iter_vars(self) -> _Generator[str, None, None]:
        for item in tuple(self.vars_):
            if item in self.vars_:
                yield item

    def has_item(self, item: str) -> _Optional[_NoReturn]:
        try:
            self.vars_[item]
        except KeyError:
            raise AttributeError(f"module '{self.module.__name__}' has no attribute '{item}'")

    def get_annotation(self, item: str) -> _Any:
        val = self.vars_[item]
        try:
            self.annotations.__getattr__
        except AttributeError:
            self.annotations = _typing.get_type_hints(self.module)
        for key in self.iter_vars():
            if self.vars_[key] is val and key in self.annotations:
                return self.annotations[key]


class Globals1(Globals):
    def __setitem__(self, key, value):
        setattr(self.module, key, value)
        del self.vars_[key]


def sizeof(obj: CT) -> int:
    return _ctypes.sizeof(obj)


def byref(obj: CT) -> Pointer[CT]:
    # noinspection PyTypeChecker
    return _ctypes.byref(obj)


@_typing.overload
def pointer(obj: CT) -> Pointer[CT]:
    pass


@_typing.overload
def pointer(type_: type[CT]) -> type[Pointer[type[CT]]]:
    pass


def pointer(obj):
    try:
        return _ctypes.pointer(obj)
    except TypeError:
        return _ctypes.POINTER(obj)


def cast(obj: _Any, type_: _Union[type[CT], CT]) -> Array[CT]:
    try:
        return _ctypes.cast(obj, type_)
    except _ctypes.ArgumentError:
        return cast(_ctypes.byref(obj), type_)
    except TypeError:
        return cast(obj, _ctypes.POINTER(type_))


def get_doc(name: str, restype: _Any, argtypes: tuple) -> str:
    return f'{name}({", ".join(type_.__name__ for type_ in argtypes)}) -> {getattr(restype, "__name__", restype)}'


def replace_object(old, new):
    _gc.collect()
    for referrer in _gc.get_referrers(old):
        try:
            items = referrer.items()
        except AttributeError:
            continue
        else:
            for key, val in items:
                if val is old:
                    referrer[key] = new


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


def init():
    for module in _pkgutil.iter_modules((_os.path.dirname(__file__),), f'{__package__}.'):
        if module.name not in _sys.modules:
            # noinspection PyTypeChecker
            _sys.modules[module.name] = Module(module.name)


init()
