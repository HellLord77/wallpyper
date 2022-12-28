from __future__ import annotations as _

import atexit as _atexit
import ctypes as _ctypes
import functools as _functools
import inspect as _inspect
import types as _types
import typing as _typing
from typing import Callable as _Callable, Generic as _Generic, Iterable as _Iterable, Optional as _Optional

from .. import const as _const
from .. import enum as _enum
from .. import handle as _handle
from .. import lib as _lib
from .. import macro as _macro
from .. import struct as _struct
from .. import type as _type
from .._utils import _Pointer, _addressof, _byref, _resolve_type

_K = _typing.TypeVar('_K')
_V = _typing.TypeVar('_V')
_T = _typing.TypeVar('_T')
_TArgs = _typing.TypeVar('_TArgs')
_TProgress = _typing.TypeVar('_TProgress')
_TResult = _typing.TypeVar('_TResult')
_TSender = _typing.TypeVar('_TSender')


@_functools.cache
def _get_item(cls: _Template, key: tuple) -> _Template:
    # noinspection PyUnresolvedReferences
    args = dict(zip(cls.__parameters__, _typing.get_args(
        super(_Template, cls).__class_getitem__(key))))
    name = cls.__name__
    suffix = ''
    if name.endswith('_impl'):
        name = name[:-5]
        suffix = '_impl'
    # noinspection PyTypeChecker
    return type(f'{name}_{"_".join(arg.__name__ for arg in args.values())}{suffix}', (
        cls,), {'__module__': cls.__module__, '_args': args})


@_functools.cache
def _get_vtbl(cls: type[_Interface]) -> type[_ctypes.Structure]:
    fields = []
    args = getattr(cls, '_args', None)
    for base in reversed(cls.__mro__):
        if hints := _typing.get_type_hints(base):
            for name in base.__annotations__:
                args_res = _resolve_type(hints[name], args)
                args_res.insert(1, _type.c_void_p)
                fields.append((name, _ctypes.WINFUNCTYPE(*args_res)))
    # noinspection PyTypeChecker
    return type(cls.__name__, (_ctypes.Structure,), {'_fields_': tuple(fields)})


class _Template:
    def __class_getitem__(cls, key):
        if not isinstance(key, tuple):
            key = (key,)
        return _get_item(cls, key)


class _InterfaceBase(_type.c_void_p):
    def __init_subclass__(cls) -> _Iterable[type]:
        cls._fields: set[str] = set()
        mro = iter(cls.__mro__)
        name = f'{__name__}.'
        for base in mro:
            if base.__module__.startswith(name):
                cls.__module__ = base.__module__
                cls._base = base
                return mro

    def __dir__(self):
        return *self.__dict__, *self._fields


class _Interface(_InterfaceBase):
    def __init_subclass__(cls):
        mro = super().__init_subclass__()
        for interface in reversed((cls._base, *mro)):
            cls._fields.update(_inspect.get_annotations(interface))

    def __getattr__(self, name):
        if name in self._fields:
            # noinspection PyProtectedMember,PyUnresolvedReferences
            struct = _get_vtbl(self._base._base).from_address(_type.c_void_p.from_address(self.value).value)
            for field_name in self._fields:
                func = getattr(struct, field_name)
                func.__name__ = field_name
                setattr(self, field_name, _types.MethodType(func, self))
        return super().__getattribute__(name)


# noinspection PyPep8Naming
class _Interface_impl(_InterfaceBase):
    def __init_subclass__(cls):
        super().__init_subclass__()
        # noinspection PyUnresolvedReferences
        cls._base: type[_Interface] = getattr(_inspect.getmodule(
            cls._base), cls._base.__name__.split('_', 1)[0])
        if hasattr(cls, '_args'):
            # noinspection PyUnresolvedReferences
            cls._base = cls._base[tuple(cls._args.values())]
        # noinspection PyUnresolvedReferences,PyProtectedMember
        cls._fields = cls._base._fields

    def __init__(self):
        struct = _get_vtbl(self._base)
        # noinspection PyProtectedMember
        self._obj = _ctypes.pointer(struct(*(field_type(lambda _, *args, _func=getattr(
            self, field_name): _func(*args)) for field_name, field_type in struct._fields_)))
        super().__init__(_addressof(self._obj))

    def __hash__(self):
        return self.value

    @classmethod
    def _get_iid_refs(cls) -> _Iterable[_Pointer[_struct.IID]]:
        # noinspection PyUnresolvedReferences
        mro = iter(cls._base.__mro__)
        while (base := next(mro)) is not _Interface:
            if issubclass(base, _Interface) and (not issubclass(
                    base, _Template) or hasattr(base, '_args')):
                # noinspection PyProtectedMember
                yield _macro._uuidof(base)


_TInterface = _typing.TypeVar('_TInterface', bound=_Interface)
_UInterface = _typing.TypeVar('_UInterface', bound=_Interface)


class _COMBase(_Generic[_TInterface]):
    _type: type[_TInterface]
    _obj: _TInterface

    @classmethod
    @_functools.cache
    def __class_getitem__(cls, interface: type[_TInterface]) -> _COMBase[type[_TInterface]]:
        # noinspection PyProtectedMember,PyTypeChecker
        return type(f'{cls.__name__}<{interface.__name__}>', (cls,), {'_type': interface._base})

    def __new__(cls, _=None, /):
        self = super().__new__(cls)
        self._obj = cls._type()
        return self

    @_typing.overload
    def __init__(self, value: int, /):
        pass

    @_typing.overload
    def __init__(self, com_base: _COMBase[type[_UInterface]], /):
        pass

    @_typing.overload
    def __init__(self, interface: _UInterface, /):
        pass

    def __init__(self, com_base_or_interface=None, /):
        if isinstance(com_base_or_interface, int):
            self._obj.value = com_base_or_interface
        elif com_base_or_interface is not None:
            if isinstance(com_base_or_interface, _COMBase):
                com_base_or_interface = com_base_or_interface._obj
            com_base_or_interface.QueryInterface(*_macro.IID_PPV_ARGS(self._obj))

    def __del__(self):
        # noinspection PyStatementEffect
        -self
        self._obj.value = None

    def __bool__(self):
        return bool(self._obj)

    def __mod__(self, interface: type[_UInterface]) -> _Optional[_UInterface]:
        if self:
            obj = interface()
            if _macro.SUCCEEDED(self._obj.QueryInterface(*_macro.IID_PPV_ARGS(obj))):
                return obj

    def __pos__(self) -> int:
        return self._obj.AddRef() if self else -1

    def __neg__(self) -> int:
        return self._obj.Release() if self else -1

    def __invert__(self) -> _Pointer[_TInterface]:
        return _byref(self._obj)

    def __enter__(self) -> _TInterface:
        return self._obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class COM(_COMBase):
    @_typing.overload
    def __init__(self, /):
        pass

    @_typing.overload
    def __init__(self, value: int, /):
        pass

    @_typing.overload
    def __init__(self, clsid_or_progid: str, /):
        pass

    @_typing.overload
    def __init__(self, com: COM[type[_UInterface]], /):
        pass

    @_typing.overload
    def __init__(self, interface: _UInterface, /):
        pass

    def __init__(self, clsid_or_progid_or_com_or_interface=None, /):
        if isinstance(clsid_or_progid_or_com_or_interface, str):
            clsid_ref = _byref(_struct.CLSID())
            if _macro.SUCCEEDED(_lib.ole32.CLSIDFromString(clsid_or_progid_or_com_or_interface, clsid_ref)):
                _lib.ole32.CoCreateInstance(
                    clsid_ref, None, _const.CLSCTX_SERVER, *_macro.IID_PPV_ARGS(self._obj))
        else:
            super().__init__(clsid_or_progid_or_com_or_interface)

    # noinspection PyTypeChecker
    def __getitem__(self, interface: type[_UInterface]) -> _Optional[COM[_UInterface]]:
        if self:
            return COM[interface](self)


class WinRT(_COMBase):
    @_typing.overload
    def __init__(self, /):
        pass

    @_typing.overload
    def __init__(self, value: int, /):
        pass

    @_typing.overload
    def __init__(self, activatable_class_id: str, /):
        pass

    @_typing.overload
    def __init__(self, winrt: WinRT[type[_UInterface]], /):
        pass

    @_typing.overload
    def __init__(self, interface: _UInterface, /):
        pass

    def __init__(self, activatable_class_id_or_winrt_or_interface=None, /):
        if isinstance(activatable_class_id_or_winrt_or_interface, str):
            activatable_class_id = _handle.HSTRING.from_string(
                activatable_class_id_or_winrt_or_interface)
            # noinspection PyProtectedMember
            if self._type._factory:
                # noinspection PyProtectedMember
                _lib.combase.RoGetActivationFactory(
                    activatable_class_id, _macro._uuidof(self._type), ~self)
            elif _macro.SUCCEEDED(_lib.combase.RoActivateInstance(activatable_class_id, ~self)):
                self._obj.value = (self % self._type).value
                # noinspection PyStatementEffect
                -self
        else:
            super().__init__(activatable_class_id_or_winrt_or_interface)

    # noinspection PyTypeChecker
    def __getitem__(self, interface: type[_UInterface]) -> _Optional[WinRT[_UInterface]]:
        if self:
            return WinRT[interface](self)


def init_com(multi_threaded: bool = True) -> bool:
    init = _macro.SUCCEEDED(_lib.ole32.CoInitializeEx(None, (
        _enum.COINIT.MULTITHREADED if multi_threaded else _enum.COINIT.APARTMENTTHREADED).value))
    if init:
        _atexit.register(_lib.ole32.CoUninitialize)
    return init


def init_winrt(multi_threaded: bool = True) -> bool:
    init = _macro.SUCCEEDED(_lib.combase.RoInitialize(
        _enum.RO_INIT_TYPE.MULTITHREADED if multi_threaded else _enum.RO_INIT_TYPE.SINGLETHREADED))
    if init:
        _atexit.register(_lib.combase.RoUninitialize)
    return init


def create_handler(callback: _Callable[[...], _type.HRESULT], interface: type[_Interface], name: _Optional[str] = None) -> COM[_Interface]:
    impl_name = interface.__name__
    if (args := getattr(interface, '_args', None)) is not None:
        impl_name = impl_name.split("_", 1)[0]
    impl_name = f'{impl_name}_impl'
    cls = getattr(_inspect.getmodule(interface), impl_name)
    if args is not None:
        cls = cls[tuple(args.values())]
    handler = COM[interface](type(f'{interface.__name__}<{callback.__name__}>'
                                  if name is None else name, (cls,), {'Invoke': staticmethod(callback)})())
    # noinspection PyStatementEffect
    -handler
    return handler
