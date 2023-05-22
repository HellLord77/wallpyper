from __future__ import annotations

import ctypes as _ctypes
from typing import Callable as _Callable

from ..um import Unknwnbase as _Unknwnbase
from ... import const as _const
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer, _addressof
from ...lib import combase as _combase


class _IInspectable:
    GetIids: _Callable[[_Pointer[_type.ULONG],  # iidCount
                        _Pointer[_Pointer[_struct.IID]]],  # iids
                       _type.HRESULT]
    GetRuntimeClassName: _Callable[[_Pointer[_type.HSTRING]],  # className
                                   _type.HRESULT]
    GetTrustLevel: _Callable[[_Pointer[_enum.TrustLevel]],  # trustLevel
                             _type.HRESULT]


class IInspectable(_IInspectable, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IInspectable_impl(_IInspectable, _Unknwnbase.IUnknown_impl):
    _runtime_class_name = ''
    _trust_level = _enum.TrustLevel.BaseTrust

    @classmethod
    def GetIids(cls, iid_count: _Pointer[_type.ULONG], iids: _Pointer[_Pointer[_struct.IID]]) -> _type.HRESULT:
        iid_refs = tuple(cls._get_iid_refs())
        iid_count.contents = len(iid_refs)
        # noinspection PyTypeChecker
        _type.c_void_p.from_address(iids).value = _addressof(  # TODO elegant
            (_ctypes.POINTER(_struct.IID) * iid_count.contents)(*iid_refs)) if iid_refs else None
        return _const.NOERROR

    @classmethod
    def GetRuntimeClassName(cls, class_name: _Pointer[_type.HSTRING]) -> _type.HRESULT:
        return _combase.WindowsCreateString(
            cls._runtime_class_name, len(cls._runtime_class_name), class_name)

    @classmethod
    def GetTrustLevel(cls, trust_level: _Pointer[_enum.TrustLevel]) -> _type.HRESULT:
        trust_level.contents = cls._trust_level
        return _const.NOERROR
