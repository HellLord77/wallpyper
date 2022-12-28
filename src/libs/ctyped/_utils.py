import ctypes as _ctypes
import functools as _functools
import gc as _gc
import inspect as _inspect
import os as _os
import pkgutil as _pkgutil
import sys as _sys
import types as _types
import typing as _typing
from typing import Any as _Any, Generator as _Generator, Generic as _Generic, Optional as _Optional, Sequence as _Sequence

import _ctypes as __ctypes

_CT = _typing.TypeVar('_CT')
# noinspection PyProtectedMember
_SimpleCData = __ctypes._SimpleCData
_PyCSimpleType = type(_SimpleCData)
_CArgObject = type(_ctypes.byref(_ctypes.c_void_p()))


class _Pointer(_Generic[_CT], _Sequence[_CT]):
    _type_: type[_CT]
    contents: _CT
    value: _CT


class _Module(_types.ModuleType):
    __slots__ = '_name'
    _module = None

    # noinspection PyMissingConstructor
    def __init__(self, name: str):
        self._name = name

    def __getattr__(self, name: str):
        if self._module is None:
            del _sys.modules[self._name]
            self._module = __import__(self._name, fromlist=self._name.rsplit('.', 1)[:1])
        _replace_object(self, self._module)
        return getattr(self._module, name)


class _Globals(dict):
    def __init__(self, replace_once: bool = False):
        self.replace_once = replace_once
        self.locals = _inspect.currentframe().f_back.f_locals
        self.vars_ = {var: val for var, val in self.locals.items() if not var.startswith('_')}
        for var in self.vars_:
            del self.locals[var]
        super().__init__(self.locals)
        self.locals['__getattr__'] = self.__getitem__

    def __getitem__(self, item: str):
        try:
            return super().__getitem__(item)
        except KeyError:
            try:
                val = self.locals[item]
            except KeyError:
                if item not in self.vars_:
                    raise AttributeError(f"Module '{self.locals['__name__']}' has no attribute '{item}'")
                val = self.locals['_init'](item)
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
        self.locals[key] = value
        del self.vars_[key]
        super().__setitem__(key, value)

    def iter_vars(self) -> _Generator[str, None, None]:
        for item in tuple(self.vars_):
            if item in self.vars_:
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


def _pointer(obj_or_type: type[_CT]) -> type[_Pointer[_CT]]:
    try:
        # noinspection PyTypeChecker
        return _ctypes.POINTER(obj_or_type)
    except TypeError:
        # noinspection PyTypeChecker
        return _ctypes.pointer(obj_or_type)


# noinspection PyShadowingBuiltins
def _cast(obj: _Any, type: type[_CT]) -> _Pointer[_CT]:
    try:
        return _ctypes.cast(obj, type)
    except _ctypes.ArgumentError:
        return _cast(_byref(obj), type)
    except TypeError:
        return _cast(obj, _ctypes.POINTER(type))


# noinspection PyShadowingBuiltins
@_functools.cache
def _is_unsigned(type: type[_CT]) -> bool:
    # noinspection PyUnresolvedReferences
    return type(-1).value != -1


# noinspection PyShadowingBuiltins
def _cast_int(obj: int, type: _CT) -> int:
    mask = 1 << (_sizeof(type) * 8)
    obj &= mask - 1
    if not _is_unsigned(type) and obj & (mask >> 1):
        obj -= mask
    return obj


def _dummy(arg: _CT) -> _CT:
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


def _func_doc(name: str, restype: _Any, argtypes: _Sequence, annotations: tuple[str]) -> str:
    return _pretty_tuples(annotations, (*(type_.__name__ for type_ in argtypes), getattr(restype, '__name__', restype)), name=name)


def _fields_repr(self: _ctypes.Structure | _ctypes.Union) -> str:
    return f'<{"Struct" if isinstance(self, _ctypes.Structure) else "Union"}: {type(self).__name__}<{", ".join(f"{item_[0]}={getattr(self, item_[0])}" for item_ in self._fields_)}>>'


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


def _resolve_type(annot: _Any, args: _Optional[dict] = None) -> _Any:
    if args is not None and hasattr(annot, '_args'):
        annot = annot.__mro__[1][tuple(args.values())]
    # noinspection PyUnresolvedReferences,PyProtectedMember
    if isinstance(annot, _typing._CallableType):
        annot = [_ctypes.c_void_p]
    elif isinstance(annot, _typing._CallableGenericAlias):
        args_res = _typing.get_args(annot)
        annot = [_resolve_type(args_res[1], args), *(
            _resolve_type(arg, args) for arg in args_res[0])]
    else:
        # noinspection PyUnresolvedReferences,PyProtectedMember
        if isinstance(annot, _typing._UnionGenericAlias):
            annot = _typing.get_args(annot)[0]
        if _typing.get_origin(annot) is _Pointer:
            annot = _ctypes.POINTER(_resolve_type(_typing.get_args(annot)[0], args))
    if isinstance(annot, _typing.TypeVar):
        annot = args.get(annot, annot)
    return annot


# noinspection PyShadowingBuiltins
def _get_winrt_class_name(type: type[_CT]) -> str:  # TODO remove
    namespace, name = type.__qualname__.rsplit('.', 1)
    name = name.removeprefix('I').removesuffix('_impl')
    while name[-1].isdigit():
        name = name[:-1]
    name_ = ''
    while name != name_:
        name_ = name
        for suffix in ('Factory', 'RuntimeClass', 'Statics', 'WithFlyout'):
            name = name.removesuffix(suffix)
    return f'{namespace}.{name}'


def _init():
    globals_ = globals()
    for func in (_addressof, _sizeof, _byref):
        globals_[func.__name__] = getattr(_ctypes, func.__name__[1:])
    for module in _pkgutil.iter_modules((_os.path.dirname(__file__),), f'{__package__}.'):
        if module.name.rsplit('.', 1)[1] not in ('const', 'interface', 'winrt'):  # TODO
            _sys.modules[module.name] = _sys.modules.get(module.name, _Module(module.name))


_init()
