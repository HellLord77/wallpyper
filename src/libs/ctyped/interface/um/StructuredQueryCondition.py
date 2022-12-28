from __future__ import annotations as _

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from . import objidl as _objidl
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class IRichChunk(_Unknwnbase.IUnknown):
    GetData: _Callable[[_Pointer[_type.ULONG],  # pFirstPos
                        _Pointer[_type.ULONG],  # pLength
                        _Pointer[_type.LPWSTR],  # ppsz
                        _Pointer[_struct.PROPVARIANT]],  # pValue
                       _type.HRESULT]


class ICondition(_objidl.IPersistStream):
    GetConditionType: _Callable[[_Pointer[_enum.CONDITION_TYPE]],  # pNodeType
                                _type.HRESULT]
    GetSubConditions: _Callable[[_Pointer[_struct.IID],  # riid
                                 _type.c_void_p],  # ppv
                                _type.HRESULT]
    GetComparisonInfo: _Callable[[_Pointer[_type.LPWSTR],  # ppszPropertyName
                                  _Pointer[_enum.CONDITION_OPERATION],  # pcop
                                  _Pointer[_struct.PROPVARIANT]],  # ppropvar
                                 _type.HRESULT]
    GetValueType: _Callable[[_Pointer[_type.LPWSTR]],  # ppszValueTypeName
                            _type.HRESULT]
    GetValueNormalization: _Callable[[_Pointer[_type.LPWSTR]],  # ppszNormalization
                                     _type.HRESULT]
    GetInputTerms: _Callable[[_Pointer[IRichChunk],  # ppPropertyTerm
                              _Pointer[IRichChunk],  # ppOperationTerm
                              _Pointer[IRichChunk]],  # ppValueTerm
                             _type.HRESULT]
    Clone: _Callable[[_Pointer[ICondition]],  # ppc
                     _type.HRESULT]


class ICondition2(ICondition):
    GetLocale: _Callable[[_Pointer[_type.LPWSTR]],  # ppszLocaleName
                         _type.HRESULT]
    GetLeafConditionInfo: _Callable[[_Pointer[_struct.PROPERTYKEY],  # ppropkey
                                     _Pointer[_enum.CONDITION_OPERATION],  # pcop
                                     _Pointer[_struct.PROPVARIANT]],  # ppropvar
                                    _type.HRESULT]
