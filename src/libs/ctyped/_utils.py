import ctypes as _ctypes
import gc as _gc
import importlib as _importlib
import inspect as _inspect
import os as _os
import pkgutil as _pkgutil
import sys as _sys
import types as _types
import typing as _typing
from typing import Any as _Any, Generator as _Generator, Generic as _Generic, ItemsView as _ItemsView, Optional as _Optional, Sequence as _Sequence

_CT = _typing.TypeVar('_CT')


class _Namespace:  # FIXME
    pass


class _Pointer(_Generic[_CT], _Sequence[_CT]):
    contents: _CT
    value: _CT


class _Module(_types.ModuleType):
    __slots__ = '_name', '_module'

    # noinspection PyMissingConstructor
    def __init__(self, name: str):
        self._name = name
        self._module = None

    def __getattr__(self, name: str):
        if self._module is None:
            del _sys.modules[self._name]
            self._module = _importlib.import_module(*_os.path.splitext(self._name)[::-1])
        _replace_object(self, self._module)
        return getattr(self._module, name)


class _Globals(dict):
    def __init__(self, replace_once: bool = False):
        self.replace_once = replace_once
        self.module = _sys.modules[_inspect.currentframe().f_back.f_globals['__name__']]
        vars_ = vars(self.module)
        self.vars_ = {var: val for var, val in vars_.items() if not var.startswith('_')}
        for var in self.vars_:
            delattr(self.module, var)
        super().__init__(vars_)
        self.module.__getattr__ = self.__getitem__

    def __getitem__(self, item: str):
        try:
            return super().__getitem__(item)
        except KeyError:
            try:
                val = vars(self.module)[item]
            except KeyError:
                if item not in self.vars_:
                    raise AttributeError(f"Module '{self.module.__name__}' has no attribute '{item}'")
                val = self.vars_[item]
                if not (isinstance(val, type) and issubclass(val, _Namespace)):
                    # noinspection PyUnresolvedReferences,PyProtectedMember
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

    def setitem(self, key: str, value):
        setattr(self.module, key, value)
        del self.vars_[key]
        super().__setitem__(key, value)

    def iter_vars(self) -> _Generator[str, None, None]:
        for item in tuple(self.vars_):
            if item in self.vars_:
                yield item

    def get_type_hints(self, item: str) -> _ItemsView[str, _Any]:
        return _typing.get_type_hints(self.vars_[item], self, self).items()


def _addressof(obj: _CT) -> int:
    return _ctypes.addressof(obj)


# noinspection PyShadowingBuiltins
def _sizeof(type: _CT) -> int:
    return _ctypes.sizeof(type)


def _byref(obj: _CT) -> _Pointer[_CT]:
    # noinspection PyTypeChecker
    return _ctypes.byref(obj)


def _pointer(obj: type[_CT]) -> type[_Pointer[_CT]]:
    try:
        # noinspection PyTypeChecker
        return _ctypes.POINTER(obj)
    except TypeError:
        # noinspection PyTypeChecker
        return _ctypes.pointer(obj)


# noinspection PyShadowingBuiltins
def _cast(obj: _Any, type: type[_CT]) -> _Pointer[_CT]:
    try:
        return _ctypes.cast(obj, type)
    except _ctypes.ArgumentError:
        return _cast(_ctypes.byref(obj), type)
    except TypeError:
        return _cast(obj, _ctypes.POINTER(type))


# noinspection PyShadowingBuiltins
def _cast_int(obj: int, type: _CT) -> int:
    return obj & (2 ** (_ctypes.sizeof(type) * 8) - 1)


def _decorator(arg: _CT) -> _CT:
    return arg


def _format_annotations(annotations: str) -> tuple[str]:
    if annotations == '_Callable':
        return '_Undefined',
    else:
        index = annotations.rfind(']', 0, -1)
        annotations = f'{annotations[annotations.find("[[") + 2:index]}{annotations[index + 1: - 1]}'.split(', ')
        return tuple(annotations[annotations[0] == '':])


def _pretty_tuples(*itt: tuple[str, ...], name: str = '') -> str:
    if lines := [[] for _ in range(len(itt))]:
        for index in range(len(itt[0]) - 1):
            sz = 0
            for tup in itt:
                sz = max(sz, len(tup[index]))
            for index_ in range(len(itt)):
                lines[index_].append(itt[index_][index].center(sz))
        sz = 0
        for tup in itt:
            sz = max(sz, len(tup[-1]))
        for index in range(len(itt)):
            lines[index].append(itt[index][-1].center(sz))
    return f'\n'.join(f'{name}({", ".join(line[:-1])}) -> {line[-1]}' for line in lines)


def _get_func_doc(name: str, restype: _Any, argtypes: _Sequence, annotations: tuple[str]) -> str:
    return _pretty_tuples(annotations, (*(type_.__name__ for type_ in argtypes), getattr(restype, '__name__', restype)), name=name)


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


def _dataclass_repr(self) -> str:
    return f'{type(self).__name__}({", ".join(f"{item_[0]}={getattr(self, item_[0])}" for item_ in self._fields_)})'


def _resolve_type(annot: _Any, args: _Optional[dict] = None) -> _Any:
    if args and hasattr(annot, '_args'):
        annot = annot.__mro__[1][tuple(args.values())]
    # noinspection PyUnresolvedReferences,PyProtectedMember
    if isinstance(annot, _typing._CallableType):
        annot = [_ctypes.c_void_p]
    elif isinstance(annot, _typing._CallableGenericAlias):
        types = _typing.get_args(annot)
        annot = [_resolve_type(types[1], args), *(_resolve_type(type_, args) for type_ in types[0])]
    else:
        # noinspection PyUnresolvedReferences,PyProtectedMember
        if isinstance(annot, _typing._UnionGenericAlias):
            annot = _typing.get_args(annot)[0]
        # if _typing.get_origin(annot) is type: TODO remove (?)
        #     annot = _typing.get_args(annot)[0]
        if _typing.get_origin(annot) is _Pointer:
            annot = _ctypes.POINTER(_resolve_type(_typing.get_args(annot)[0], args))
    if isinstance(annot, _typing.TypeVar):
        annot = args.get(annot, annot)
    return annot


def _init():
    for module in _pkgutil.iter_modules((_os.path.dirname(__file__),), f'{__package__}.'):
        _sys.modules[module.name] = _sys.modules.get(module.name, _Module(module.name))


_init()
