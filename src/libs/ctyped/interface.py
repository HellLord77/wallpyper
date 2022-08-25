from __future__ import annotations as _  # TODO docs

import ctypes as _ctypes
import functools as _functools
import hashlib as _hashlib
import json as _json
import ntpath as _ntpath
import re as _re
import shutil as _shutil
import sys as _sys
import types as _types
import typing as _typing
import warnings as _warnings
# noinspection PyUnresolvedReferences
from typing import Callable as _Callable, Generic as _Generic, Optional as _Optional

# noinspection PyUnresolvedReferences
from . import const as _const, enum as _enum, lib as _lib, macro as _macro, struct as _struct, type as _type, union as _union
# noinspection PyUnresolvedReferences
from ._utils import _Pointer, _get_winrt_class_name, _resolve_type

_LINES: list[str]
_LOCALS: _Locals
_NAME_TEMPLATE = f'{_ntpath.splitext(__file__)[0]}.{{}}'
_K = _typing.TypeVar('_K')
_V = _typing.TypeVar('_V')
_T = _typing.TypeVar('_T')
_TArgs = _typing.TypeVar('_TArgs')
_TProgress = _typing.TypeVar('_TProgress')
_TResult = _typing.TypeVar('_TResult')
_TSender = _typing.TypeVar('_TSender')
_CArgObject = type(_ctypes.byref(_type.c_void_p()))
_PyCSimpleType = type(_ctypes.c_void_p)


class _Template:
    _args = None
    _classes = None

    def __init_subclass__(cls):
        cls._classes = {}
        super().__init_subclass__()

    def __class_getitem__(cls, item):
        if not isinstance(item, tuple):
            item = item,
        if item not in cls._classes:
            # noinspection PyUnresolvedReferences
            args = dict(zip(cls.__parameters__, _typing.get_args(super().__class_getitem__(item))))
            qualname = f'{cls.__qualname__.removesuffix("_impl")}_{"_".join(type_.__name__ for type_ in args.values())}{"_impl" * cls.__qualname__.endswith("_impl")}'
            cls._classes[item] = type(qualname.rsplit('.', 1)[-1], (cls,), {'__qualname__': qualname, '_args': args})
        return cls._classes[item]


class _Interface(_type.c_void_p):
    _vtbl = _ctypes.Structure
    _docs = None

    def __new__(cls):
        if cls._vtbl.__name__ != cls.__name__:
            cls._vtbl = _get_vtbl(cls)
            # annots = {name: annot for base in cls.__mro__ for name, annot in getattr(base, '__annotations__', {}).items()}
            # cls.__doc__ = '\n\n'.join(_func_doc(name, types._restype_, types._argtypes_[1:], _format_annotations(
            #     annots[name])) for name, types in cls._vtbl._fields_) ### docs overriden with child class (same named methods) ###
            # cls._docs = {name: '\n'.join(doc for doc in cls.__doc__.split('\n') if doc.startswith(f'{name}(')) for name, _ in cls._vtbl._fields_}
        return super().__new__(cls)

    def __getattr__(self, name: str):
        # noinspection PyProtectedMember,PyUnresolvedReferences
        for field_name, _ in self._vtbl._fields_:
            if name == field_name:
                # noinspection PyUnresolvedReferences
                funcs = self._vtbl.from_address(_type.c_void_p.from_address(self.value).value)
                # noinspection PyProtectedMember,PyUnresolvedReferences
                for func_name, _ in self._vtbl._fields_:
                    func = getattr(funcs, func_name)
                    func.__name__ = func_name
                    # func.__doc__ = self._docs[name__]
                    setattr(self, func_name, _types.MethodType(func, self))
                break
        return super().__getattribute__(name)


# noinspection PyPep8Naming
class _Interface_impl(_type.c_void_p):
    _iid_refs = None
    _vtbl = _ctypes.Structure
    _c_refs = {}

    def __hash__(self):
        return self.value

    def __new__(cls):
        if cls._vtbl.__name__ != cls.__name__:
            iid_refs = []
            cls_annot = cls
            for base in cls.__mro__[cls.__mro__.index(_Interface_impl)::-1]:
                # noinspection PyProtectedMember
                if __name__ == base.__module__ and not base.__name__.startswith(
                        '_') and not (issubclass(base, _Template) and base._args is None):
                    # noinspection PyTypeChecker,PyProtectedMember
                    iid_refs.append(_ctypes.byref(_macro._uuidof(base)))
                    cls_annot = base
            cls._iid_refs = tuple(iid_refs)
            cls._vtbl = _get_vtbl(cls_annot, cls.__name__)
        return super().__new__(cls)

    def __init__(self):
        # noinspection PyProtectedMember,PyTypeChecker
        self._ptr = _ctypes.pointer(self._vtbl(*(type_(_functools.wraps(func := getattr(self, name))(
            lambda _, *args, _func=func: _func(*args))) for name, type_ in self._vtbl._fields_)))
        super().__init__(_ctypes.addressof(self._ptr))
        self._c_refs[self] = 1


def _get_vtbl(cls: type, name: _Optional[str] = None) -> type[_ctypes.Structure]:
    fields = []
    args = getattr(cls, '_args', None)
    for base in reversed(cls.__mro__):
        if hints := _typing.get_type_hints(base):
            for func_name in base.__annotations__:
                types = _resolve_type(hints[func_name], args)
                types.insert(1, _type.c_void_p)
                fields.append((func_name, _ctypes.WINFUNCTYPE(*types)))
    # noinspection PyTypeChecker
    return type(cls.__name__ if name is None else name, (_ctypes.Structure,), {'_fields_': tuple(fields)})


class _Locals(dict):
    locals: list = [_sys.modules[__name__]]

    def __getitem__(self, key: str):
        try:
            return super().__getitem__(key)
        except KeyError:
            try:
                return getattr(self.locals[-1], key)
            except AttributeError:
                return getattr(self.locals[0], key)


class _NamespaceMeta(type):
    _interfaces: dict[str, tuple[int, int]]

    def __getattr__(self, name):
        try:
            data = self._interfaces[name]
        except KeyError:
            raise AttributeError
        else:
            if not __debug__:
                del self._interfaces[name]  # noqa
            first_line = _LINES[data[0]]
            intend = first_line.index('c')
            _LOCALS.locals.append(self)
            exec('\n'.join(line[intend:] for line in _LINES[data[0]:data[1]]), globals(), _LOCALS)
            _LOCALS.locals.pop()
            setattr(self, name, interface := _LOCALS[name])
            return interface


def _get_hash() -> str:
    md5 = _hashlib.md5()
    with open(_NAME_TEMPLATE.format('pyi'), 'rb') as file:
        # noinspection PyUnresolvedReferences
        while data := file.read(_shutil.COPY_BUFSIZE):
            md5.update(data)
    return md5.hexdigest()


def _get_interfaces(namespace):
    # noinspection PyProtectedMember
    interfaces = namespace._interfaces
    for name, value in vars(namespace).items():
        if isinstance(value, _NamespaceMeta):
            interfaces[name] = _get_interfaces(value)
    return interfaces


def _set_interfaces(namespace, interfaces: dict[str, tuple[int, int] | dict]):
    namespace._interfaces = interfaces
    namespaces = []
    for name, value in interfaces.items():
        if isinstance(value, dict):
            new_namespace = _NamespaceMeta(name, (), {})
            _set_interfaces(new_namespace, value)
            setattr(namespace, name, new_namespace)
            namespaces.append(name)
    for name in namespaces:
        del interfaces[name]


def _dump_cache():
    interfaces = _get_interfaces(_sys.modules[__name__])
    with open(_NAME_TEMPLATE.format('json'), 'w') as file:
        _json.dump({_get_hash(): interfaces}, file, indent=2)


def _load_cache() -> bool:
    path = _NAME_TEMPLATE.format('json')
    if _ntpath.isfile(path):
        with open(path) as file:
            try:
                data = _json.load(file)
            except _json.JSONDecodeError:
                data = {}
        if interfaces := data.get(_get_hash()):
            _set_interfaces(_sys.modules[__name__], interfaces)
            return True
    return False


def _init():
    global _LINES, _LOCALS
    _LOCALS = _Locals()
    with open(_NAME_TEMPLATE.format('pyi')) as file:
        _LINES = file.read().splitlines()
    _module = _sys.modules[__name__]
    if not _load_cache():
        _warnings.warn('Invalid cache')
        re_class = _re.compile(r'\s*class\s(\w*)(?:\((.*)\))?.*:')
        _module._interfaces = {}
        level = 0
        namespaces = [_module]
        interface = None
        for index, line in enumerate(_LINES):
            if match := re_class.fullmatch(line):
                groups = match.groups()
                level = line.index('c') // 4
                if groups[0].startswith('_') or groups[1]:
                    interface = groups[0], index
                else:
                    namespace = _NamespaceMeta(groups[0], (), {})
                    try:
                        namespaces[level + 1] = namespace
                    except IndexError:
                        namespaces.append(namespace)
                    namespace._interfaces = {}
                    setattr(namespaces[level], groups[0], namespace)
            elif not line and interface:
                # noinspection PyProtectedMember
                namespaces[level]._interfaces[interface[0]] = interface[1], index
                interface = None
    _module.__getattr__ = _types.MethodType(_NamespaceMeta.__getattr__, _module)


_init()
