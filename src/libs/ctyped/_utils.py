import ctypes as _ctypes
import functools as _functools
import gc as _gc
import importlib as _importlib
import importlib.abc as _importlib_abc
import importlib.machinery as _importlib_machinery
import importlib.util as _importlib_util
import os as _os
import pkgutil as _pkgutil
import sys as _sys
import threading as _threading
import typing as _typing
from types import ModuleType as _ModuleType
from typing import Any as _Any
from typing import Final as _Final
from typing import Generic as _Generic
from typing import Iterator as _Iterator
from typing import Optional as _Optional
from typing import Sequence as _Sequence

import _ctypes as __ctypes

_CT = _typing.TypeVar('_CT')
# noinspection PyProtectedMember,PyUnresolvedReferences
_SimpleCData = __ctypes._SimpleCData
_PyCSimpleType = type(_SimpleCData)
_CArgObject = type(_ctypes.byref(_ctypes.c_void_p()))

_LEGACY_LAZY_MODULE = False


class _Pointer(_Generic[_CT], _Sequence[_CT]):
    _type_: type[_CT]
    contents: _CT
    value: _CT

    NULL: _Final = None


if _LEGACY_LAZY_MODULE:
    def _replace_object(old, new):
        _gc.collect()
        for referrer in _gc.get_referrers(old):
            if isinstance(referrer, dict):
                for key, val in referrer.items():
                    if val is old:
                        referrer[key] = new


    class _LazyModule(_ModuleType):
        _module = None

        def __getattr__(self, name: str):
            if self._module is None:
                del _sys.modules[self.__name__]
                try:
                    self._module = _importlib.import_module(self.__name__)
                except KeyError as exc:  # FIXME https://github.com/cython/cython/issues/3867
                    if self.__name__ == exc.args[0]:
                        self._module = _importlib.import_module(self.__name__)
                    else:
                        raise
            _replace_object(self, self._module)
            return getattr(self._module, name)


    def _iter_modules(path: str = _os.path.dirname(__file__), prefix: str = __package__,
                      recursive: bool = False) -> _Iterator[_pkgutil.ModuleInfo]:
        prefix += '.'
        for module in _pkgutil.iter_modules((path,), prefix):
            yield module
            if recursive and module.ispkg:
                yield from _iter_modules(_os.path.join(
                    path, module.name.removeprefix(prefix)), module.name, recursive)
else:
    _getattribute_lock = _functools.lru_cache(lambda _: _threading.Lock())

    # noinspection PyUnresolvedReferences,PyProtectedMember
    class _LazyModule(_importlib_util._LazyModule):
        def __getattribute__(self, name):  # FIXME cannot handle threaded loading
            spec = object.__getattribute__(self, '__spec__')
            if spec.loader_state['ident'] == _threading.get_ident():
                return super(_importlib_util._LazyModule, self).__getattribute__(name)
            else:
                # noinspection PyTypeChecker
                with _getattribute_lock(self):
                    if type(self) is _LazyModule:
                        spec.loader_state['ident'] = _threading.get_ident()
                        dict_ = spec.loader_state['__dict__']
                        dict__ = object.__getattribute__(self, '__dict__')
                        updated = {}
                        for key, val in dict__.items():
                            if key not in dict_:
                                updated[key] = val
                            elif dict__[key] is dict_[key]:
                                updated[key] = val
                        spec.loader.exec_module(self)
                        dict__.update(updated)
                        self.__class__ = spec.loader_state['__class__']
                    return getattr(self, name)


    class _LazyLoader(_importlib_util.LazyLoader):
        def exec_module(self, module: _ModuleType):
            super().exec_module(module)
            object.__getattribute__(module, '__spec__').loader_state['ident'] = 0
            module.__class__ = _LazyModule


    class _LazyFinder(_importlib_abc.MetaPathFinder):
        _found = set()

        @classmethod
        def find_spec(cls, fullname: str, path: _Optional[_Sequence[str]] = None,
                      target: _Optional[_ModuleType] = None) -> _Optional[_importlib_machinery.ModuleSpec]:
            if fullname.startswith(__package__) and fullname not in cls._found:
                cls._found.add(fullname)
                spec = _importlib_util.find_spec(fullname)
                spec.loader = _LazyLoader(spec.loader)
                return spec


class _Globals(dict):
    def __init__(self, globals_: dict[str, _Any], replace_once: bool = False):
        self.globals = globals_
        self.replace_once = replace_once
        self.vars = {var: val for var, val in self.globals.items() if not var.startswith('_')}
        for var in self.vars:
            del self.globals[var]
        super().__init__(self.globals)
        self.globals['__getattr__'] = self.__getitem__

    def __getitem__(self, key: str):
        try:
            return super().__getitem__(key)
        except KeyError:
            try:
                val = self.globals[key]
            except KeyError:
                if key not in self.vars:
                    raise AttributeError(f"Module {self.globals['__name__']!r} has no attribute {key!r}")
                val = self.globals['_init'](key)
            else:
                self.vars[key] = val
            self[key] = val
            return val

    def __setitem__(self, key, value):
        try:
            val = self.vars[key]
        except KeyError:
            pass
        else:
            if self.replace_once:
                self.setitem(key, value)
            else:
                for key_ in self.iter_vars():
                    if self.vars[key_] is val:
                        self.setitem(key_, value)

    def setitem(self, key: str, value):
        self.globals[key] = value
        del self.vars[key]
        super().__setitem__(key, value)

    def iter_vars(self) -> _Iterator[str]:
        for item in tuple(self.vars):
            if item in self.vars:
                yield item


# noinspection PyUnusedLocal
def _addressof(obj: _CT, /) -> int:
    pass


# noinspection PyUnusedLocal
def _sizeof(obj_or_type: _CT, /) -> int:
    pass


# noinspection PyUnusedLocal
def _byref(obj: _CT, /) -> _Pointer[_CT]:
    pass


# noinspection PyShadowingBuiltins
@_functools.cache
def _is_unsigned(type: type[_CT]) -> bool:
    # noinspection PyUnresolvedReferences
    return type(-1).value != -1


def _pointer(obj_or_type: type[_CT]) -> type[_Pointer[_CT]]:
    try:
        # noinspection PyTypeChecker
        return _ctypes.POINTER(obj_or_type)
    except TypeError:
        # noinspection PyTypeChecker
        return _ctypes.pointer(obj_or_type)


# noinspection PyShadowingBuiltins
def _cast(obj, type: type[_CT]) -> _Pointer[_CT]:
    try:
        return _ctypes.cast(obj, type)
    except _ctypes.ArgumentError:
        return _cast(_byref(obj), type)
    except TypeError:
        return _cast(obj, _ctypes.POINTER(type))


# noinspection PyShadowingBuiltins
def _cast_int(obj: int, type: _CT) -> int:
    mask = 1 << (_sizeof(type) * 8)
    obj &= mask - 1
    if not _is_unsigned(type) and obj & (mask >> 1):
        obj -= mask
    return obj


def _fmt_annot(annot: str) -> tuple[str, ...]:
    if annot == '_Callable':
        return '_Undefined',
    else:
        index = annot.rfind(']', 0, -1)
        annot = f'{annot[annot.find("[[") + 2:index]}{annot[index + 1: - 1]}'.split(', ')
        return tuple(annot[annot[0] == '':])


def _pretty_tuples(*it: tuple[str, ...], name: str = '') -> str:
    if lines := [[] for _ in range(len(it))]:
        for index in range(len(it[0]) - 1):
            sz = 0
            for tup in it:
                sz = max(sz, len(tup[index]))
            for index_ in range(len(it)):
                lines[index_].append(it[index_][index].center(sz))
        sz = 0
        for tup in it:
            sz = max(sz, len(tup[-1]))
        for index in range(len(it)):
            lines[index].append(it[index][-1].center(sz))
    return f'\n'.join(f'{name}({", ".join(line[:-1])}) -> {line[-1]}' for line in lines)


def _func_doc(name: str, restype, argtypes: _Sequence, annotations: tuple[str]) -> str:
    return _pretty_tuples(annotations, (*(
        type_.__name__ for type_ in argtypes), getattr(restype, '__name__', restype)), name=name)


def _fields_repr(self: _ctypes.Structure | _ctypes.Union) -> str:
    return (f'<{"Struct" if isinstance(self, _ctypes.Structure) else "Union"}: {type(self).__name__}'
            f'<{", ".join(f"{item_[0]}={getattr(self, item_[0])}" for item_ in self._fields_)}>>')


def _resolve_type(annot, _args: _Optional[dict] = None) -> _Any:
    if _args is not None and hasattr(annot, '_args'):
        annot = annot.__mro__[1][tuple(_args.values())]
    # noinspection PyUnresolvedReferences,PyProtectedMember
    if isinstance(annot, _typing._CallableType):
        annot = [_ctypes.c_void_p]
    elif isinstance(annot, _typing._CallableGenericAlias):
        args, res = _typing.get_args(annot)
        annot = [_resolve_type(res, _args), *(
            _resolve_type(arg, _args) for arg in args)]
    else:
        # noinspection PyUnresolvedReferences,PyProtectedMember
        if isinstance(annot, _typing._UnionGenericAlias):
            annot = _typing.get_args(annot)[0]
        if _typing.get_origin(annot) is _Pointer:
            annot = _ctypes.POINTER(_resolve_type(_typing.get_args(annot)[0], _args))
    if isinstance(annot, _typing.TypeVar):
        annot = _args.get(annot, annot)
    return annot


def _init():
    globals_ = globals()
    for func in (_addressof, _sizeof, _byref):
        globals_[func.__name__] = getattr(_ctypes, func.__name__[1:])
    if _LEGACY_LAZY_MODULE:
        for module in _iter_modules(recursive=True):
            if module.name not in _sys.modules:
                _sys.modules[module.name] = _LazyModule(module.name)
    else:
        _sys.meta_path.insert(0, _LazyFinder())


_init()
