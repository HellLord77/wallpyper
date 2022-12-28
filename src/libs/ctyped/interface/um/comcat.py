from __future__ import annotations as _

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class IEnumGUID(_Unknwnbase.IUnknown):
    Next: _Callable[[_type.ULONG,  # celt
                     _Pointer[_struct.GUID],  # rgelt
                     _Pointer[_type.ULONG]],  # pceltFetched
                    _type.HRESULT]
    Skip: _Callable[[_type.ULONG],  # celt
                    _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]
    Clone: _Callable[[_Pointer[IEnumGUID]],  # ppenum
                     _type.HRESULT]


class IEnumCATEGORYINFO(_Unknwnbase.IUnknown):
    Next: _Callable[[_type.ULONG,  # celt
                     _Pointer[_struct.CATEGORYINFO],  # rgelt
                     _Pointer[_type.ULONG]],  # pceltFetched
                    _type.HRESULT]
    Skip: _Callable[[_type.ULONG],  # celt
                    _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]
    Clone: _Callable[[_Pointer[IEnumCATEGORYINFO]],  # ppenum
                     _type.HRESULT]


class ICatRegister(_Unknwnbase.IUnknown):
    RegisterCategories: _Callable[[_type.ULONG,  # cCategories
                                   _Pointer[_struct.CATEGORYINFO]],  # rgCategoryInfo
                                  _type.HRESULT]
    UnRegisterCategories: _Callable[[_type.ULONG,  # cCategories
                                     _Pointer[_struct.CATID]],  # rgcatid
                                    _type.HRESULT]
    RegisterClassImplCategories: _Callable[[_Pointer[_struct.IID],  # rclsid
                                            _type.ULONG,  # cCategories
                                            _Pointer[_struct.CATID]],  # rgcatid
                                           _type.HRESULT]
    UnRegisterClassImplCategories: _Callable[[_Pointer[_struct.IID],  # rclsid
                                              _type.ULONG,  # cCategories
                                              _Pointer[_struct.CATID]],  # rgcatid
                                             _type.HRESULT]
    RegisterClassReqCategories: _Callable[[_Pointer[_struct.IID],  # rclsid
                                           _type.ULONG,  # cCategories
                                           _Pointer[_struct.CATID]],  # rgcatid
                                          _type.HRESULT]
    UnRegisterClassReqCategories: _Callable[[_Pointer[_struct.IID],  # rclsid
                                             _type.ULONG,  # cCategories
                                             _Pointer[_struct.CATID]],  # rgcatid
                                            _type.HRESULT]


class ICatInformation(_Unknwnbase.IUnknown):
    EnumCategories: _Callable[[_type.LCID,  # lcid
                               _Pointer[IEnumCATEGORYINFO]],  # ppenumCategoryInfo
                              _type.HRESULT]
    GetCategoryDesc: _Callable[[_Pointer[_struct.GUID],  # rcatid
                                _type.LCID,  # lcid
                                _Pointer[_type.LPWSTR]],  # pszDesc
                               _type.HRESULT]
    EnumClassesOfCategories: _Callable[[_type.ULONG,  # cImplemented
                                        _Pointer[_struct.CATID],  # rgcatidImpl
                                        _type.ULONG,  # cRequired
                                        _Pointer[_struct.CATID],  # rgcatidReq
                                        _Pointer[IEnumGUID]],  # ppenumClsid
                                       _type.HRESULT]
    IsClassOfCategories: _Callable[[_Pointer[_struct.IID],  # rclsid
                                    _type.ULONG,  # cImplemented
                                    _Pointer[_struct.CATID],  # rgcatidImpl
                                    _type.ULONG,  # cRequired
                                    _Pointer[_struct.CATID]],  # rgcatidReq
                                   _type.HRESULT]
    EnumImplCategoriesOfClass: _Callable[[_Pointer[_struct.IID],  # rclsid
                                          _Pointer[IEnumGUID]],  # ppenumCatid
                                         _type.HRESULT]
    EnumReqCategoriesOfClass: _Callable[[_Pointer[_struct.IID],  # rclsid
                                         _Pointer[IEnumGUID]],  # ppenumCatid
                                        _type.HRESULT]
