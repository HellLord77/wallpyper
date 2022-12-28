from __future__ import annotations as _

import inspect
import typing
from typing import Optional

from libs import ctyped
from libs.ctyped.interface.um import Unknwnbase


class _Property:
    def __init__(self, name: str):
        self._getter = f'get_{name}'
        self._setter = f'put_{name}'


class Getter(_Property):
    def __get__(self, instance: _Interface, owner: type[_Interface]):
        raise NotImplementedError


class Setter(_Property):
    def __set__(self, instance: _Interface, value):
        getattr(instance.interface, self._setter)(value)


class CIntGetter(Getter):
    def __get__(self, instance: _Interface, owner: type[_Interface]) -> int:
        c_int = ctyped.type.c_int()
        getattr(instance.interface, self._getter)(ctyped.byref(c_int))
        return c_int.value


class CIntSetter(Setter):
    pass


class CIntGetterSetter(CIntSetter, CIntGetter):
    pass


class CLongGetter(Getter):
    def __get__(self, instance: _Interface, owner: type[_Interface]) -> int:
        c_long = ctyped.type.c_long()
        getattr(instance.interface, self._getter)(ctyped.byref(c_long))
        return c_long.value


class CLongSetter(Setter):
    pass


class CLongGetterSetter(CLongSetter, CLongGetter):
    pass


class LPWSTRGetter(Getter):
    def __get__(self, instance: _Interface, owner: type[_Interface]) -> str:
        lpwstr = ctyped.type.LPWSTR()
        getattr(instance.interface, self._getter)(ctyped.byref(lpwstr))
        return lpwstr.value


class LPWSTRSetter(Setter):
    pass


class LPWSTRGetterSetter(LPWSTRSetter, LPWSTRGetter):
    pass


class BOOLGetter(Getter):
    def __get__(self, instance: _Interface, owner: type[_Interface]) -> bool:
        bool_ = ctyped.type.BOOL()
        getattr(instance.interface, self._getter)(ctyped.byref(bool_))
        return bool(bool_.value)


class BOOLSetter(Setter):
    pass


class BOOLGetterSetter(BOOLSetter, BOOLGetter):
    pass


class VariantBoolGetter(Getter):
    def __get__(self, instance: _Interface, owner: type[_Interface]) -> bool:
        variant_bool = ctyped.type.VARIANT_BOOL()
        getattr(instance.interface, self._getter)(ctyped.byref(variant_bool))
        return bool(variant_bool.value)


class VariantBoolSetter(Setter):
    pass


class VariantBoolGetterSetter(VariantBoolSetter, VariantBoolGetter):
    pass


class _Interface:
    def __init__(self, interface: Optional[Unknwnbase.IUnknown] = None):
        self.interface = typing.get_type_hints(self, vars(inspect.getmodule(self)))['interface']()
        if interface:
            interface.QueryInterface(*ctyped.macro.IID_PPV_ARGS(self.interface))

    def __del__(self):
        if self.interface:
            self.interface.Release()


class Unknown(_Interface):
    interface: Unknwnbase.IUnknown
