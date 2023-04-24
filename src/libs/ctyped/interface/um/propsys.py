from __future__ import annotations

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from . import objidlbase as _objidlbase
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class IInitializeWithFile(_Unknwnbase.IUnknown):
    Initialize: _Callable[[_type.LPCWSTR,  # pszFilePath
                           _type.DWORD],  # grfMode
                          _type.HRESULT]


class IInitializeWithStream(_Unknwnbase.IUnknown):
    Initialize: _Callable[[_objidlbase.IStream,  # pstream
                           _type.DWORD],  # grfMode
                          _type.HRESULT]


class IPropertyStore(_Unknwnbase.IUnknown):
    GetCount: _Callable[[_Pointer[_type.DWORD]],  # cProps
                        _type.HRESULT]
    GetAt: _Callable[[_type.DWORD,  # iProp
                      _Pointer[_struct.PROPERTYKEY]],  # pkey
                     _type.HRESULT]
    GetValue: _Callable[[_Pointer[_struct.PROPERTYKEY],  # key
                         _Pointer[_struct.PROPVARIANT]],  # pv
                        _type.HRESULT]
    SetValue: _Callable[[_Pointer[_struct.PROPERTYKEY],  # key
                         _Pointer[_struct.PROPVARIANT]],  # propvar
                        _type.HRESULT]
    Commit: _Callable[[],
                      _type.HRESULT]


class INamedPropertyStore(_Unknwnbase.IUnknown):
    GetNamedValue: _Callable[[_type.LPCWSTR,  # pszName
                              _Pointer[_struct.PROPVARIANT]],  # ppropvar
                             _type.HRESULT]
    SetNamedValue: _Callable[[_type.LPCWSTR,  # pszName
                              _Pointer[_struct.PROPVARIANT]],  # propvar
                             _type.HRESULT]
    GetNameCount: _Callable[[_Pointer[_type.DWORD]],  # pdwCount
                            _type.HRESULT]
    GetNameAt: _Callable[[_type.DWORD,  # iProp
                          _Pointer[_type.BSTR]],  # pbstrName
                         _type.HRESULT]


class IObjectWithPropertyKey(_Unknwnbase.IUnknown):
    SetPropertyKey: _Callable[[_Pointer[_struct.PROPERTYKEY]],  # key
                              _type.HRESULT]
    GetPropertyKey: _Callable[[_Pointer[_struct.PROPERTYKEY]],  # pkey
                              _type.HRESULT]


class IPropertyChange(IObjectWithPropertyKey):
    ApplyToPropVariant: _Callable[[_Pointer[_struct.PROPVARIANT],  # propvarIn
                                   _Pointer[_struct.PROPVARIANT]],  # ppropvarOut
                                  _type.HRESULT]


class IPropertyChangeArray(_Unknwnbase.IUnknown):
    GetCount: _Callable[[_Pointer[_type.UINT]],  # pcOperations
                        _type.HRESULT]
    GetAt: _Callable[[_type.UINT,  # iIndex
                      _Pointer[_struct.IID],  # riid
                      _type.c_void_p],  # ppv
                     _type.HRESULT]
    InsertAt: _Callable[[_type.UINT,  # iIndex
                         IPropertyChange],  # ppropChange
                        _type.HRESULT]
    Append: _Callable[[IPropertyChange],  # ppropChange
                      _type.HRESULT]
    AppendOrReplace: _Callable[[IPropertyChange],  # ppropChange
                               _type.HRESULT]
    RemoveAt: _Callable[[_type.UINT],  # iIndex
                        _type.HRESULT]
    IsKeyInArray: _Callable[[_Pointer[_struct.PROPERTYKEY]],  # key
                            _type.HRESULT]


class IPropertyStoreCapabilities(_Unknwnbase.IUnknown):
    IsPropertyWritable: _Callable[[_Pointer[_struct.PROPERTYKEY]],  # key
                                  _type.HRESULT]


class IPropertyStoreCache(IPropertyStore):
    GetState: _Callable[[_Pointer[_struct.PROPERTYKEY],  # key
                         _Pointer[_enum.PSC_STATE]],  # pstate
                        _type.HRESULT]
    GetValueAndState: _Callable[[_Pointer[_struct.PROPERTYKEY],  # key
                                 _Pointer[_struct.PROPVARIANT],  # ppropvar
                                 _Pointer[_enum.PSC_STATE]],  # pstate
                                _type.HRESULT]
    SetState: _Callable[[_Pointer[_struct.PROPERTYKEY],  # key
                         _enum.PSC_STATE],  # state
                        _type.HRESULT]
    SetValueAndState: _Callable[[_Pointer[_struct.PROPERTYKEY],  # key
                                 _Pointer[_struct.PROPVARIANT],  # ppropvar
                                 _enum.PSC_STATE],  # state
                                _type.HRESULT]


class IPropertyEnumType(_Unknwnbase.IUnknown):
    GetEnumType: _Callable[[_Pointer[_enum.PROPENUMTYPE]],  # penumtype
                           _type.HRESULT]
    GetValue: _Callable[[_Pointer[_struct.PROPVARIANT]],  # ppropvar
                        _type.HRESULT]
    GetRangeMinValue: _Callable[[_Pointer[_struct.PROPVARIANT]],  # ppropvarMin
                                _type.HRESULT]
    GetRangeSetValue: _Callable[[_Pointer[_struct.PROPVARIANT]],  # ppropvarSet
                                _type.HRESULT]
    GetDisplayText: _Callable[[_Pointer[_type.LPWSTR]],  # ppszDisplay
                              _type.HRESULT]


class IPropertyEnumType2(IPropertyEnumType):
    GetImageReference: _Callable[[_Pointer[_type.LPWSTR]],  # ppszImageRes
                                 _type.HRESULT]


class IPropertyEnumTypeList(_Unknwnbase.IUnknown):
    GetCount: _Callable[[_Pointer[_type.UINT]],  # pctypes
                        _type.HRESULT]
    GetAt: _Callable[[_type.UINT,  # itype
                      _Pointer[_struct.IID],  # riid
                      _type.c_void_p],  # ppv
                     _type.HRESULT]
    GetConditionAt: _Callable[[_type.UINT,  # nIndex
                               _Pointer[_struct.IID],  # riid
                               _type.c_void_p],  # ppv
                              _type.HRESULT]
    FindMatchingIndex: _Callable[[_Pointer[_struct.PROPVARIANT],  # propvarCmp
                                  _Pointer[_type.UINT]],  # pnIndex
                                 _type.HRESULT]


class IPropertyDescription(_Unknwnbase.IUnknown):
    GetPropertyKey: _Callable[[_Pointer[_struct.PROPERTYKEY]],  # pkey
                              _type.HRESULT]
    GetCanonicalName: _Callable[[_Pointer[_type.LPWSTR]],  # ppszName
                                _type.HRESULT]
    GetPropertyType: _Callable[[_Pointer[_type.VARTYPE]],  # pvartype
                               _type.HRESULT]
    GetDisplayName: _Callable[[_Pointer[_type.LPWSTR]],  # ppszName
                              _type.HRESULT]
    GetEditInvitation: _Callable[[_Pointer[_type.LPWSTR]],  # ppszInvite
                                 _type.HRESULT]
    GetTypeFlags: _Callable[[_enum.PROPDESC_TYPE_FLAGS,  # mask
                             _Pointer[_enum.PROPDESC_TYPE_FLAGS]],  # ppdtFlags
                            _type.HRESULT]
    GetViewFlags: _Callable[[_Pointer[_enum.PROPDESC_VIEW_FLAGS]],  # ppdvFlags
                            _type.HRESULT]
    GetDefaultColumnWidth: _Callable[[_Pointer[_type.UINT]],  # pcxChars
                                     _type.HRESULT]
    GetDisplayType: _Callable[[_Pointer[_enum.PROPDESC_DISPLAYTYPE]],  # pdisplaytype
                              _type.HRESULT]
    GetColumnState: _Callable[[_Pointer[_type.SHCOLSTATEF]],  # pcsFlags
                              _type.HRESULT]
    GetGroupingRange: _Callable[[_Pointer[_enum.PROPDESC_GROUPING_RANGE]],  # pgr
                                _type.HRESULT]
    GetRelativeDescriptionType: _Callable[[_Pointer[_enum.PROPDESC_RELATIVEDESCRIPTION_TYPE]],  # prdt
                                          _type.HRESULT]
    GetRelativeDescription: _Callable[[_Pointer[_struct.PROPVARIANT],  # propvar1
                                       _Pointer[_struct.PROPVARIANT],  # propvar2
                                       _Pointer[_type.LPWSTR],  # ppszDesc1
                                       _Pointer[_type.LPWSTR]],  # ppszDesc2
                                      _type.HRESULT]
    GetSortDescription: _Callable[[_Pointer[_enum.PROPDESC_SORTDESCRIPTION]],  # psd
                                  _type.HRESULT]
    GetSortDescriptionLabel: _Callable[[_type.BOOL,  # fDescending
                                        _Pointer[_type.LPWSTR]],  # ppszDescription
                                       _type.HRESULT]
    GetAggregationType: _Callable[[_Pointer[_enum.PROPDESC_AGGREGATION_TYPE]],  # paggtype
                                  _type.HRESULT]
    GetConditionType: _Callable[[_Pointer[_enum.PROPDESC_CONDITION_TYPE],  # pcontype
                                 _Pointer[_enum.CONDITION_OPERATION]],  # popDefault
                                _type.HRESULT]
    GetEnumTypeList: _Callable[[_Pointer[_struct.IID],  # riid
                                _type.c_void_p],  # ppv
                               _type.HRESULT]
    CoerceToCanonicalValue: _Callable[[_Pointer[_struct.PROPVARIANT]],  # ppropvar
                                      _type.HRESULT]
    FormatForDisplay: _Callable[[_Pointer[_struct.PROPVARIANT],  # propvar
                                 _enum.PROPDESC_FORMAT_FLAGS,  # pdfFlags
                                 _Pointer[_type.LPWSTR]],  # ppszDisplay
                                _type.HRESULT]
    IsValueCanonical: _Callable[[_Pointer[_struct.PROPVARIANT]],  # propvar
                                _type.HRESULT]


class IPropertyDescription2(IPropertyDescription):
    GetImageReferenceForValue: _Callable[[_Pointer[_struct.PROPVARIANT],  # propvar
                                          _Pointer[_type.LPWSTR]],  # ppszImageRes
                                         _type.HRESULT]


class IPropertyDescriptionAliasInfo(IPropertyDescription):
    GetSortByAlias: _Callable[[_Pointer[_struct.IID],  # riid
                               _type.c_void_p],  # ppv
                              _type.HRESULT]
    GetAdditionalSortByAliases: _Callable[[_Pointer[_struct.IID],  # riid
                                           _type.c_void_p],  # ppv
                                          _type.HRESULT]


class IPropertyDescriptionSearchInfo(IPropertyDescription):
    GetSearchInfoFlags: _Callable[[_Pointer[_enum.PROPDESC_SEARCHINFO_FLAGS]],  # ppdsiFlags
                                  _type.HRESULT]
    GetColumnIndexType: _Callable[[_Pointer[_enum.PROPDESC_COLUMNINDEX_TYPE]],  # ppdciType
                                  _type.HRESULT]
    GetProjectionString: _Callable[[_Pointer[_type.LPWSTR]],  # ppszProjection
                                   _type.HRESULT]
    GetMaxSize: _Callable[[_Pointer[_type.UINT]],  # pcbMaxSize
                          _type.HRESULT]


class IPropertyDescriptionRelatedPropertyInfo(IPropertyDescription):
    GetRelatedProperty: _Callable[[_type.LPCWSTR,  # pszRelationshipName
                                   _Pointer[_struct.IID],  # riid
                                   _type.c_void_p],  # ppv
                                  _type.HRESULT]


class IPropertySystem(_Unknwnbase.IUnknown):
    GetPropertyDescription: _Callable[[_Pointer[_struct.PROPERTYKEY],  # propkey
                                       _Pointer[_struct.IID],  # riid
                                       _type.c_void_p],  # ppv
                                      _type.HRESULT]
    GetPropertyDescriptionByName: _Callable[[_type.LPCWSTR,  # pszCanonicalName
                                             _Pointer[_struct.IID],  # riid
                                             _type.c_void_p],  # ppv
                                            _type.HRESULT]
    GetPropertyDescriptionListFromString: _Callable[[_type.LPCWSTR,  # pszPropList
                                                     _Pointer[_struct.IID],  # riid
                                                     _type.c_void_p],  # ppv
                                                    _type.HRESULT]
    EnumeratePropertyDescriptions: _Callable[[_enum.PROPDESC_ENUMFILTER,  # filterOn
                                              _Pointer[_struct.IID],  # riid
                                              _type.c_void_p],  # ppv
                                             _type.HRESULT]
    FormatForDisplay: _Callable[[_Pointer[_struct.PROPERTYKEY],  # key
                                 _Pointer[_struct.PROPVARIANT],  # propvar
                                 _enum.PROPDESC_FORMAT_FLAGS,  # pdff
                                 _type.LPWSTR,  # pszText
                                 _type.DWORD],  # cchText
                                _type.HRESULT]
    FormatForDisplayAlloc: _Callable[[_Pointer[_struct.PROPERTYKEY],  # key
                                      _Pointer[_struct.PROPVARIANT],  # propvar
                                      _enum.PROPDESC_FORMAT_FLAGS,  # pdff
                                      _Pointer[_type.LPWSTR]],  # ppszDisplay
                                     _type.HRESULT]
    RegisterPropertySchema: _Callable[[_type.LPCWSTR],  # pszPath
                                      _type.HRESULT]
    UnregisterPropertySchema: _Callable[[_type.LPCWSTR],  # pszPath
                                        _type.HRESULT]
    RefreshPropertySchema: _Callable[[],
                                     _type.HRESULT]


class IPropertyDescriptionList(_Unknwnbase.IUnknown):
    GetCount: _Callable[[_Pointer[_type.UINT]],  # pcElem
                        _type.HRESULT]
    GetAt: _Callable[[_type.UINT,  # iElem
                      _Pointer[_struct.IID],  # riid
                      _type.c_void_p],  # ppv
                     _type.HRESULT]


class IPropertyStoreFactory(_Unknwnbase.IUnknown):
    GetPropertyStore: _Callable[[_enum.GETPROPERTYSTOREFLAGS,  # flags
                                 _Unknwnbase.IUnknown,  # pUnkFactory
                                 _Pointer[_struct.IID],  # riid
                                 _type.c_void_p],  # ppv
                                _type.HRESULT]
    GetPropertyStoreForKeys: _Callable[[_Pointer[_struct.PROPERTYKEY],  # rgKeys
                                        _type.UINT,  # cKeys
                                        _enum.GETPROPERTYSTOREFLAGS,  # flags
                                        _Pointer[_struct.IID],  # riid
                                        _type.c_void_p],  # ppv
                                       _type.HRESULT]


class IDelayedPropertyStoreFactory(IPropertyStoreFactory):
    GetDelayedPropertyStore: _Callable[[_enum.GETPROPERTYSTOREFLAGS,  # flags
                                        _type.DWORD,  # dwStoreId
                                        _Pointer[_struct.IID],  # riid
                                        _type.c_void_p],  # ppv
                                       _type.HRESULT]


class IPersistSerializedPropStorage(_Unknwnbase.IUnknown):
    SetFlags: _Callable[[_type.PERSIST_SPROPSTORE_FLAGS],  # flags
                        _type.HRESULT]
    SetPropertyStorage: _Callable
    GetPropertyStorage: _Callable[[_Pointer[_Pointer[_struct.SERIALIZEDPROPSTORAGE]],  # ppsps
                                   _Pointer[_type.DWORD]],  # pcb
                                  _type.HRESULT]


class IPersistSerializedPropStorage2(IPersistSerializedPropStorage):
    GetPropertyStorageSize: _Callable[[_Pointer[_type.DWORD]],  # pcb
                                      _type.HRESULT]
    GetPropertyStorageBuffer: _Callable[[_Pointer[_struct.SERIALIZEDPROPSTORAGE],  # psps
                                         _type.DWORD,  # cb
                                         _Pointer[_type.DWORD]],  # pcbWritten
                                        _type.HRESULT]


class IPropertySystemChangeNotify(_Unknwnbase.IUnknown):
    SchemaRefreshed: _Callable[[],
                               _type.HRESULT]


class ICreateObject(_Unknwnbase.IUnknown):
    CreateObject: _Callable[[_Pointer[_struct.IID],  # clsid
                             _Unknwnbase.IUnknown,  # pUnkOuter
                             _Pointer[_struct.IID],  # riid
                             _type.c_void_p],  # ppv
                            _type.HRESULT]
