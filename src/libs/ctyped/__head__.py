import ctypes as _ctypes
import gc as _gc
import importlib as _importlib
import inspect as _inspect
import os as _os
import pkgutil as _pkgutil
import sys as _sys
import types as _types
import typing as _typing
from typing import Any as _Any
from typing import Generator as _Generator
from typing import Generic as _Generic
from typing import NoReturn as _NoReturn
from typing import Optional as _Optional
from typing import Sequence as _Sequence
from typing import Union as _Union

_INIT = False
_DEBUG = True
_CT = _typing.TypeVar('_CT')


class _Pointer(_Generic[_CT]):
    contents: _CT
    value: _CT


# noinspection PyAbstractClass
class _Array(_Pointer, _Sequence[_CT]):
    pass


class _Module:
    __spec__ = None
    _module = None

    def __init__(self, name: str):
        self._name = name

    def __getattr__(self, name: str):
        if not self._module:
            del _sys.modules[self._name]
            self._module = _importlib.import_module(*_os.path.splitext(self._name)[::-1])
        _replace_object(self, self._module)
        return getattr(self._module, name)


class _Globals(dict):
    annotations = None

    def __init__(self, replace_once: _Optional[bool] = None):
        self.replace_once = replace_once
        # self.module = _inspect.getmodule(_inspect.currentframe().f_back) fixme pyinstaller debug getmodule -> None
        name = _inspect.currentframe().f_back.f_globals['__name__']
        self.module = _sys.modules[name]
        vars_ = vars(self.module)
        if name[-1].isdigit():
            module_ = _sys.modules[name[:-1]]
            vars_.update(
                {var: val for var, val in vars(module_).items() if not _not_internal(var) and var not in vars_})
            # noinspection PyUnresolvedReferences,PyProtectedMember
            self.module._init = _types.FunctionType(module_._init.__code__, vars_)
        self.vars_ = {var: val for var, val in vars_.items() if _not_internal(var)}
        for var in self.vars_:
            delattr(self.module, var)
        super().__init__(vars_)
        self.module.__getattr__ = self.__getitem__
        if _INIT:
            self.module._globals = self
            for var in self.iter_vars():
                getattr(self.module, var)

    def __getitem__(self, item: str):
        try:
            return super().__getitem__(item)
        except KeyError:
            try:
                val = vars(self.module)[item]
            except KeyError:
                # noinspection PyProtectedMember,PyUnresolvedReferences
                val = self.module._init(item)
            else:
                self.vars_[item] = val
            self[item] = val
            return val

    def __setitem__(self, key, value):
        try:
            val = self.vars_[key]
        except KeyError:
            pass
        else:
            if self.replace_once:
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
        if item not in self.vars_:
            raise AttributeError(f"module '{self.module.__name__}' has no attribute '{item}'")

    def get_annotation(self, item: str) -> _Any:
        if not self.annotations:
            self.annotations = _typing.get_type_hints(self.module)
        return self.annotations[item]


def _sizeof(obj: _CT) -> int:
    return _ctypes.sizeof(obj)


def _byref(obj: _CT) -> _Pointer[_CT]:
    # noinspection PyTypeChecker
    return _ctypes.byref(obj)


@_typing.overload
def _pointer(obj: _CT) -> _Pointer[_CT]:
    pass


@_typing.overload
def _pointer(type_: type[_CT]) -> type[_Pointer[type[_CT]]]:
    pass


def _pointer(obj):
    try:
        return _ctypes.pointer(obj)
    except TypeError:
        return _ctypes.POINTER(obj)


def _cast(obj: _Any, type_: _Union[type[_CT], _CT]) -> _Array[_CT]:
    try:
        return _ctypes.cast(obj, type_)
    except _ctypes.ArgumentError:
        return _cast(_ctypes.byref(obj), type_)
    except TypeError:
        return _cast(obj, _ctypes.POINTER(type_))


def _not_internal(name: str) -> bool:
    return not name.startswith('_')


def _get_doc(name: str, restype: _Any, argtypes: tuple) -> str:
    return f'{name}({", ".join(type_.__name__ for type_ in argtypes)}) -> {getattr(restype, "__name__", restype)}'


def _replace_object(old, new):
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


def _resolve_type(type_: _Any) -> _Any:
    # noinspection PyUnresolvedReferences,PyProtectedMember
    if isinstance(type_, _typing._CallableType):
        type_ = [None]
    elif isinstance(type_, _typing._CallableGenericAlias):
        types_ = _typing.get_args(type_)
        type_ = [_resolve_type(types_[1])]
        type_.extend(_resolve_type(type_) for type_ in types_[0])
    else:
        # noinspection PyUnresolvedReferences,PyProtectedMember
        if isinstance(type_, _typing._UnionGenericAlias):
            type_ = _typing.get_args(type_)[0]
        if _typing.get_origin(type_) is type:
            type_ = _typing.get_args(type_)[0]
        if _typing.get_origin(type_) is _Pointer:
            type_ = _ctypes.POINTER(_resolve_type(_typing.get_args(type_)[0]))
    return type_


def _init():
    for module in _pkgutil.iter_modules((_os.path.dirname(__file__),), f'{__package__}.'):
        if module.name not in _sys.modules:
            # noinspection PyTypeChecker
            _sys.modules[module.name] = _Module(module.name)


_init()
