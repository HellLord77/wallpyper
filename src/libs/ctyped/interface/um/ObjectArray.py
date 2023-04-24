from __future__ import annotations

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class IObjectArray(_Unknwnbase.IUnknown):
    GetCount: _Callable[[_Pointer[_type.UINT]],  # pcObjects
                        _type.HRESULT]
    GetAt: _Callable[[_type.UINT,  # uiIndex
                      _Pointer[_struct.IID],  # riid
                      _type.c_void_p],  # ppv
                     _type.HRESULT]


class IObjectCollection(IObjectArray):
    AddObject: _Callable[[_Unknwnbase.IUnknown],  # punk
                         _type.HRESULT]
    AddFromArray: _Callable[[IObjectArray],  # poaSource
                            _type.HRESULT]
    RemoveObjectAt: _Callable[[_type.UINT],  # uiIndex
                              _type.HRESULT]
    Clear: _Callable[[],
                     _type.HRESULT]
