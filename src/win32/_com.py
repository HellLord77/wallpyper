from __future__ import annotations as _

import inspect
import typing
from typing import Callable, Optional

from libs import ctyped
from libs.ctyped.interface.um import Unknwnbase


class _Property:
    def __init__(self, name: str):
        self._name = name


class Getter(_Property):
    def __get__(self, instance: _Interface, owner: type[_Interface]):
        obj = ctyped.type.c_void_p()
        self._getter(instance)(ctyped.byref(obj))
        return obj.value

    def __set__(self, instance: _Interface, value):
        raise AttributeError(f'property {self._name!r} of {type(instance).__name__!r} object has no setter')

    def _getter(self, instance: _Interface) -> Callable:
        # noinspection PyProtectedMember
        return getattr(instance._obj, f'get_{self._name}')


class Setter(_Property):
    def __get__(self, instance: _Interface, owner: type[_Interface]):
        raise AttributeError(f'property {self._name!r} of {owner.__name__!r} object has no getter')

    def __set__(self, instance: _Interface, value):
        self._setter(instance)(value)

    def _setter(self, instance: _Interface) -> Callable:
        # noinspection PyProtectedMember
        return getattr(instance._obj, f'put_{self._name}')


class CIntGetter(Getter):
    def __get__(self, instance: _Interface, owner: type[_Interface]) -> int:
        obj = ctyped.type.c_int()
        self._getter(instance)(ctyped.byref(obj))
        return obj.value


class CIntSetter(Setter):
    pass


class CIntGetterSetter(CIntSetter, CIntGetter):
    pass


class CLongGetter(Getter):
    def __get__(self, instance: _Interface, owner: type[_Interface]) -> int:
        obj = ctyped.type.c_long()
        self._getter(instance)(ctyped.byref(obj))
        return obj.value


class CLongSetter(Setter):
    pass


class CLongGetterSetter(CLongSetter, CLongGetter):
    pass


class CDoubleGetter(Getter):
    def __get__(self, instance: _Interface, owner: type[_Interface]) -> float:
        obj = ctyped.type.c_double()
        self._getter(instance)(ctyped.byref(obj))
        return obj.value


class CDoubleSetter(Setter):
    pass


class CDoubleGetterSetter(CDoubleSetter, CDoubleGetter):
    pass


class UINT32Getter(Getter):
    def __get__(self, instance: _Interface, owner: type[_Interface]) -> int:
        obj = ctyped.type.UINT32()
        self._getter(instance)(ctyped.byref(obj))
        return obj.value


class LPWSTRGetter(Getter):
    def __get__(self, instance: _Interface, owner: type[_Interface]) -> str:
        obj = ctyped.type.LPWSTR()
        self._getter(instance)(ctyped.byref(obj))
        return obj.value


class LPWSTRSetter(Setter):
    pass


class LPWSTRGetterSetter(LPWSTRSetter, LPWSTRGetter):
    pass


class BOOLGetter(Getter):
    def __get__(self, instance: _Interface, owner: type[_Interface]) -> bool:
        obj = ctyped.type.BOOL()
        self._getter(instance)(ctyped.byref(obj))
        return bool(obj.value)


class BOOLSetter(Setter):
    pass


class BOOLGetterSetter(BOOLSetter, BOOLGetter):
    pass


class VariantBoolGetter(Getter):
    def __get__(self, instance: _Interface, owner: type[_Interface]) -> bool:
        obj = ctyped.type.VARIANT_BOOL()
        self._getter(instance)(ctyped.byref(obj))
        return bool(obj.value)


class VariantBoolSetter(Setter):
    pass


class VariantBoolGetterSetter(VariantBoolSetter, VariantBoolGetter):
    pass


class HWNDGetter(Getter):
    def __get__(self, instance: _Interface, owner: type[_Interface]) -> int:
        obj = ctyped.type.HWND()
        self._getter(instance)(ctyped.byref(obj))
        return obj.value


class HWNDSetter(Setter):
    pass


class HWNDGetterSetter(HWNDSetter, HWNDGetter):
    pass


class RECTGetter(Getter):
    def __get__(self, instance: _Interface, owner: type[_Interface]) -> ctyped.struct.RECT:
        obj = ctyped.struct.RECT()
        self._getter(instance)(ctyped.byref(obj))
        return obj


class RECTSetter(Setter):
    pass


class RECTGetterSetter(RECTSetter, RECTGetter):
    pass


class _Interface:
    def __init__(self, interface: Optional[Unknwnbase.IUnknown] = None):
        self._obj = typing.get_type_hints(self, vars(inspect.getmodule(self)))['_obj']()
        if interface:
            interface.QueryInterface(*ctyped.macro.IID_PPV_ARGS(self._obj))

    def __del__(self):
        if self._obj:
            self._obj.Release()

    def __bool__(self):
        return bool(self._obj)


class Unknown(_Interface):
    _obj: Unknwnbase.IUnknown

    def add_ref(self) -> ctyped.type.HRESULT:
        return self._obj.AddRef()

    def release(self) -> ctyped.type.HRESULT:
        return self._obj.Release()
