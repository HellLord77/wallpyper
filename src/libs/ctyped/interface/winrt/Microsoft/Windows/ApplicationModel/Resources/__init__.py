from __future__ import annotations as _

from typing import Callable as _Callable

from ..... import inspectable as _inspectable
from .....Windows import Foundation as _Windows_Foundation
from .....Windows.Foundation import Collections as _Windows_Foundation_Collections
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IKnownResourceQualifierNameStatics(_inspectable.IInspectable, factory=True):
    get_Contrast: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Custom: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_DeviceFamily: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_HomeRegion: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_Language: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_LayoutDirection: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_Scale: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_TargetSize: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_Theme: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]


class IResourceCandidate(_inspectable.IInspectable):
    get_ValueAsString: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_ValueAsBytes: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                                 _Pointer[_Pointer[_type.BYTE]]],  # value
                                _type.HRESULT]
    get_Kind: _Callable[[_Pointer[_enum.Microsoft.Windows.ApplicationModel.Resources.ResourceCandidateKind]],  # value
                        _type.HRESULT]
    get_QualifierValues: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _type.HSTRING]]],  # value
                                   _type.HRESULT]


class IResourceCandidateFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[_enum.Microsoft.Windows.ApplicationModel.Resources.ResourceCandidateKind,  # kind
                               _type.HSTRING,  # data
                               _Pointer[IResourceCandidate]],  # value
                              _type.HRESULT]
    CreateInstance2: _Callable[[_type.UINT32,  # __dataSize
                                _Pointer[_type.BYTE],  # data
                                _Pointer[IResourceCandidate]],  # value
                               _type.HRESULT]


class IResourceContext(_inspectable.IInspectable):
    get_QualifierValues: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, _type.HSTRING]]],  # value
                                   _type.HRESULT]


class IResourceContext2(_inspectable.IInspectable):
    pass


class IResourceLoader(_inspectable.IInspectable):
    GetString: _Callable[[_type.HSTRING,  # resourceId
                          _Pointer[_type.HSTRING]],  # result
                         _type.HRESULT]
    GetStringForUri: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # resourceUri
                                _Pointer[_type.HSTRING]],  # result
                               _type.HRESULT]


class IResourceLoaderFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[_type.HSTRING,  # fileName
                               _Pointer[IResourceLoader]],  # value
                              _type.HRESULT]
    CreateInstance2: _Callable[[_type.HSTRING,  # fileName
                                _type.HSTRING,  # resourceMap
                                _Pointer[IResourceLoader]],  # value
                               _type.HRESULT]


class IResourceLoaderStatics(_inspectable.IInspectable, factory=True):
    GetDefaultResourceFilePath: _Callable[[_Pointer[_type.HSTRING]],  # result
                                          _type.HRESULT]


class IResourceManager(_inspectable.IInspectable):
    get_MainResourceMap: _Callable[[_Pointer[IResourceMap]],  # value
                                   _type.HRESULT]
    CreateResourceContext: _Callable[[_Pointer[IResourceContext]],  # result
                                     _type.HRESULT]
    add_ResourceNotFound: _Callable[[_Windows_Foundation.ITypedEventHandler[IResourceManager, IResourceNotFoundEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_ResourceNotFound: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]


class IResourceManager2(_inspectable.IInspectable):
    pass


class IResourceManagerFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[_type.HSTRING,  # fileName
                               _Pointer[IResourceManager]],  # value
                              _type.HRESULT]


class IResourceMap(_inspectable.IInspectable):
    get_ResourceCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    GetSubtree: _Callable[[_type.HSTRING,  # reference
                           _Pointer[IResourceMap]],  # result
                          _type.HRESULT]
    TryGetSubtree: _Callable[[_type.HSTRING,  # reference
                              _Pointer[IResourceMap]],  # result
                             _type.HRESULT]
    GetValue: _Callable[[_type.HSTRING,  # resource
                         _Pointer[IResourceCandidate]],  # result
                        _type.HRESULT]
    GetValueWithContext: _Callable[[_type.HSTRING,  # resource
                                    IResourceContext,  # context
                                    _Pointer[IResourceCandidate]],  # result
                                   _type.HRESULT]
    GetValueByIndex: _Callable[[_type.UINT32,  # index
                                _Pointer[_Windows_Foundation_Collections.IKeyValuePair[_type.HSTRING, IResourceCandidate]]],  # result
                               _type.HRESULT]
    GetValueByIndexWithContext: _Callable[[_type.UINT32,  # index
                                           IResourceContext,  # context
                                           _Pointer[_Windows_Foundation_Collections.IKeyValuePair[_type.HSTRING, IResourceCandidate]]],  # result
                                          _type.HRESULT]
    TryGetValue: _Callable[[_type.HSTRING,  # resource
                            _Pointer[IResourceCandidate]],  # result
                           _type.HRESULT]
    TryGetValueWithContext: _Callable[[_type.HSTRING,  # resource
                                       IResourceContext,  # context
                                       _Pointer[IResourceCandidate]],  # result
                                      _type.HRESULT]


class IResourceNotFoundEventArgs(_inspectable.IInspectable):
    get_Context: _Callable[[_Pointer[IResourceContext]],  # value
                           _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    SetResolvedCandidate: _Callable[[IResourceCandidate],  # candidate
                                    _type.HRESULT]
