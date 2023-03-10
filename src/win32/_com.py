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

    def __set_name__(self, owner: type[_Interface], name: str):
        # TODO set_name, cached_property, merge setter/getter
        pass


class Getter(_Property):
    def __get__(self, instance: _Interface, owner: type[_Interface]):
        raise NotImplementedError


class Setter(_Property):
    def __set__(self, instance: _Interface, value):
        # noinspection PyProtectedMember
        getattr(instance._obj, self._setter)(value)


class CIntGetter(Getter):
    def __get__(self, instance: _Interface, owner: type[_Interface]) -> int:
        obj = ctyped.type.c_int()
        # noinspection PyProtectedMember
        getattr(instance._obj, self._getter)(ctyped.byref(obj))
        return obj.value


class CIntSetter(Setter):
    pass


class CIntGetterSetter(CIntSetter, CIntGetter):
    pass


class CLongGetter(Getter):
    def __get__(self, instance: _Interface, owner: type[_Interface]) -> int:
        obj = ctyped.type.c_long()
        # noinspection PyProtectedMember
        getattr(instance._obj, self._getter)(ctyped.byref(obj))
        return obj.value


class CLongSetter(Setter):
    pass


class CLongGetterSetter(CLongSetter, CLongGetter):
    pass


class CDoubleGetter(Getter):
    def __get__(self, instance: _Interface, owner: type[_Interface]) -> float:
        obj = ctyped.type.c_double()
        # noinspection PyProtectedMember
        getattr(instance._obj, self._getter)(ctyped.byref(obj))
        return obj.value


class CDoubleSetter(Setter):
    pass


class CDoubleGetterSetter(CDoubleSetter, CDoubleGetter):
    pass


class UINT32Getter(Getter):
    def __get__(self, instance: _Interface, owner: type[_Interface]) -> int:
        obj = ctyped.type.UINT32()
        # noinspection PyProtectedMember
        getattr(instance._obj, self._getter)(ctyped.byref(obj))
        return obj.value


class LPWSTRGetter(Getter):
    def __get__(self, instance: _Interface, owner: type[_Interface]) -> str:
        obj = ctyped.type.LPWSTR()
        # noinspection PyProtectedMember
        getattr(instance._obj, self._getter)(ctyped.byref(obj))
        return obj.value


class LPWSTRSetter(Setter):
    pass


class LPWSTRGetterSetter(LPWSTRSetter, LPWSTRGetter):
    pass


class BOOLGetter(Getter):
    def __get__(self, instance: _Interface, owner: type[_Interface]) -> bool:
        obj = ctyped.type.BOOL()
        # noinspection PyProtectedMember
        getattr(instance._obj, self._getter)(ctyped.byref(obj))
        return bool(obj.value)


class BOOLSetter(Setter):
    pass


class BOOLGetterSetter(BOOLSetter, BOOLGetter):
    pass


class VariantBoolGetter(Getter):
    def __get__(self, instance: _Interface, owner: type[_Interface]) -> bool:
        obj = ctyped.type.VARIANT_BOOL()
        # noinspection PyProtectedMember
        getattr(instance._obj, self._getter)(ctyped.byref(obj))
        return bool(obj.value)


class VariantBoolSetter(Setter):
    pass


class VariantBoolGetterSetter(VariantBoolSetter, VariantBoolGetter):
    pass


class HWNDGetter(Getter):
    def __get__(self, instance: _Interface, owner: type[_Interface]) -> int:
        obj = ctyped.type.HWND()
        # noinspection PyProtectedMember
        getattr(instance._obj, self._getter)(ctyped.byref(obj))
        return obj.value


class HWNDSetter(Setter):
    pass


class HWNDGetterSetter(HWNDSetter, HWNDGetter):
    pass


class RECTGetter(Getter):
    def __get__(self, instance: _Interface, owner: type[_Interface]) -> ctyped.struct.RECT:
        obj = ctyped.struct.RECT()
        # noinspection PyProtectedMember
        getattr(instance._obj, self._getter)(ctyped.byref(obj))
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
