from __future__ import annotations as _

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from .... import Storage as _Windows_Storage
from .... import UI as _Windows_UI
from ....Foundation import Collections as _Windows_Foundation_Collections
from ....Storage import Streams as _Windows_Storage_Streams
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class INamedResource(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # uri
                       _type.HRESULT]
    get_Candidates: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IResourceCandidate]]],  # value
                              _type.HRESULT]
    Resolve: _Callable[[_Pointer[IResourceCandidate]],  # result
                       _type.HRESULT]
    ResolveForContext: _Callable[[IResourceContext,  # resourceContext
                                  _Pointer[IResourceCandidate]],  # result
                                 _type.HRESULT]
    ResolveAll: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IResourceCandidate]]],  # result
                          _type.HRESULT]
    ResolveAllForContext: _Callable[[IResourceContext,  # resourceContext
                                     _Pointer[_Windows_Foundation_Collections.IVectorView[IResourceCandidate]]],  # instances
                                    _type.HRESULT]


class IResourceCandidate(_inspectable.IInspectable):
    get_Qualifiers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IResourceQualifier]]],  # value
                              _type.HRESULT]
    get_IsMatch: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_IsMatchAsDefault: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_IsDefault: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_ValueAsString: _Callable[[_Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]
    GetValueAsFileAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage.IStorageFile]]],  # operation
                                   _type.HRESULT]
    GetQualifierValue: _Callable[[_type.HSTRING,  # qualifierName
                                  _Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]


class IResourceCandidate2(_inspectable.IInspectable):
    GetValueAsStreamAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStream]]],  # operation
                                     _type.HRESULT]


class IResourceCandidate3(_inspectable.IInspectable):
    get_Kind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Resources.Core.ResourceCandidateKind]],  # value
                        _type.HRESULT]


class IResourceContext(_inspectable.IInspectable):
    get_QualifierValues: _Callable[[_Pointer[_Windows_Foundation_Collections.IObservableMap[_type.HSTRING, _type.HSTRING]]],  # value
                                   _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]
    ResetQualifierValues: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING]],  # qualifierNames
                                    _type.HRESULT]
    OverrideToMatch: _Callable[[_Windows_Foundation_Collections.IIterable[IResourceQualifier]],  # result
                               _type.HRESULT]
    Clone: _Callable[[_Pointer[IResourceContext]],  # clone
                     _type.HRESULT]
    get_Languages: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                             _type.HRESULT]
    put_Languages: _Callable[[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]],  # languages
                             _type.HRESULT]


class IResourceContextStatics(_inspectable.IInspectable, factory=True):
    CreateMatchingContext: _Callable[[_Windows_Foundation_Collections.IIterable[IResourceQualifier],  # result
                                      _Pointer[IResourceContext]],  # value
                                     _type.HRESULT]


class IResourceContextStatics2(_inspectable.IInspectable, factory=True):
    GetForCurrentView: _Callable[[_Pointer[IResourceContext]],  # value
                                 _type.HRESULT]
    SetGlobalQualifierValue: _Callable[[_type.HSTRING,  # key
                                        _type.HSTRING],  # value
                                       _type.HRESULT]
    ResetGlobalQualifierValues: _Callable[[],
                                          _type.HRESULT]
    ResetGlobalQualifierValuesForSpecifiedQualifiers: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING]],  # qualifierNames
                                                                _type.HRESULT]
    GetForViewIndependentUse: _Callable[[_Pointer[IResourceContext]],  # loader
                                        _type.HRESULT]


class IResourceContextStatics3(_inspectable.IInspectable, factory=True):
    SetGlobalQualifierValueWithPersistence: _Callable[[_type.HSTRING,  # key
                                                       _type.HSTRING,  # value
                                                       _enum.Windows.ApplicationModel.Resources.Core.ResourceQualifierPersistence],  # persistence
                                                      _type.HRESULT]


class IResourceContextStatics4(_inspectable.IInspectable, factory=True):
    GetForUIContext: _Callable[[_Windows_UI.IUIContext,  # context
                                _Pointer[IResourceContext]],  # value
                               _type.HRESULT]


class IResourceManager(_inspectable.IInspectable):
    get_MainResourceMap: _Callable[[_Pointer[IResourceMap]],  # value
                                   _type.HRESULT]
    get_AllResourceMaps: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, IResourceMap]]],  # maps
                                   _type.HRESULT]
    get_DefaultContext: _Callable[[_Pointer[IResourceContext]],  # value
                                  _type.HRESULT]
    LoadPriFiles: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Storage.IStorageFile]],  # files
                            _type.HRESULT]
    UnloadPriFiles: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Storage.IStorageFile]],  # files
                              _type.HRESULT]


class IResourceManager2(_inspectable.IInspectable):
    GetAllNamedResourcesForPackage: _Callable[[_type.HSTRING,  # packageName
                                               _struct.Windows.ApplicationModel.Resources.Core.ResourceLayoutInfo,  # resourceLayoutInfo
                                               _Pointer[_Windows_Foundation_Collections.IVectorView[INamedResource]]],  # table
                                              _type.HRESULT]
    GetAllSubtreesForPackage: _Callable[[_type.HSTRING,  # packageName
                                         _struct.Windows.ApplicationModel.Resources.Core.ResourceLayoutInfo,  # resourceLayoutInfo
                                         _Pointer[_Windows_Foundation_Collections.IVectorView[IResourceMap]]],  # table
                                        _type.HRESULT]


class IResourceManagerStatics(_inspectable.IInspectable, factory=True):
    get_Current: _Callable[[_Pointer[IResourceManager]],  # value
                           _type.HRESULT]
    IsResourceReference: _Callable[[_type.HSTRING,  # resourceReference
                                    _Pointer[_type.boolean]],  # isReference
                                   _type.HRESULT]


class IResourceMap(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # uri
                       _type.HRESULT]
    GetValue: _Callable[[_type.HSTRING,  # resource
                         _Pointer[IResourceCandidate]],  # value
                        _type.HRESULT]
    GetValueForContext: _Callable[[_type.HSTRING,  # resource
                                   IResourceContext,  # context
                                   _Pointer[IResourceCandidate]],  # value
                                  _type.HRESULT]
    GetSubtree: _Callable[[_type.HSTRING,  # reference
                           _Pointer[IResourceMap]],  # map
                          _type.HRESULT]


class IResourceQualifier(_inspectable.IInspectable):
    get_QualifierName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_QualifierValue: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_IsDefault: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_IsMatch: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_Score: _Callable[[_Pointer[_type.DOUBLE]],  # value
                         _type.HRESULT]
