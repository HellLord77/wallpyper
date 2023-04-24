from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class ITargetedContentAction(_inspectable.IInspectable):
    InvokeAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # asyncAction
                           _type.HRESULT]


class ITargetedContentAvailabilityChangedEventArgs(_inspectable.IInspectable):
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class ITargetedContentChangedEventArgs(_inspectable.IInspectable):
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]
    get_HasPreviousContentExpired: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]


class ITargetedContentCollection(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    ReportInteraction: _Callable[[_enum.Windows.Services.TargetedContent.TargetedContentInteraction],  # interaction
                                 _type.HRESULT]
    ReportCustomInteraction: _Callable[[_type.HSTRING],  # customInteractionName
                                       _type.HRESULT]
    get_Path: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, ITargetedContentValue]]],  # value
                              _type.HRESULT]
    get_Collections: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[ITargetedContentCollection]]],  # value
                               _type.HRESULT]
    get_Items: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[ITargetedContentItem]]],  # value
                         _type.HRESULT]


class ITargetedContentContainer(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_Availability: _Callable[[_Pointer[_enum.Windows.Services.TargetedContent.TargetedContentAvailability]],  # value
                                _type.HRESULT]
    get_Content: _Callable[[_Pointer[ITargetedContentCollection]],  # value
                           _type.HRESULT]
    SelectSingleObject: _Callable[[_type.HSTRING,  # path
                                   _Pointer[ITargetedContentObject]],  # value
                                  _type.HRESULT]


class ITargetedContentContainerStatics(_inspectable.IInspectable):
    GetAsync: _Callable[[_type.HSTRING,  # contentId
                         _Pointer[_Windows_Foundation.IAsyncOperation[ITargetedContentContainer]]],  # asyncOperation
                        _type.HRESULT]

    _factory = True


class ITargetedContentImage(_inspectable.IInspectable):
    get_Height: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    get_Width: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]


class ITargetedContentItem(_inspectable.IInspectable):
    get_Path: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    ReportInteraction: _Callable[[_enum.Windows.Services.TargetedContent.TargetedContentInteraction],  # interaction
                                 _type.HRESULT]
    ReportCustomInteraction: _Callable[[_type.HSTRING],  # customInteractionName
                                       _type.HRESULT]
    get_State: _Callable[[_Pointer[ITargetedContentItemState]],  # value
                         _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, ITargetedContentValue]]],  # value
                              _type.HRESULT]
    get_Collections: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[ITargetedContentCollection]]],  # value
                               _type.HRESULT]


class ITargetedContentItemState(_inspectable.IInspectable):
    get_ShouldDisplay: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_AppInstallationState: _Callable[[_Pointer[_enum.Windows.Services.TargetedContent.TargetedContentAppInstallationState]],  # value
                                        _type.HRESULT]


class ITargetedContentObject(_inspectable.IInspectable):
    get_ObjectKind: _Callable[[_Pointer[_enum.Windows.Services.TargetedContent.TargetedContentObjectKind]],  # value
                              _type.HRESULT]
    get_Collection: _Callable[[_Pointer[ITargetedContentCollection]],  # value
                              _type.HRESULT]
    get_Item: _Callable[[_Pointer[ITargetedContentItem]],  # value
                        _type.HRESULT]
    get_Value: _Callable[[_Pointer[ITargetedContentValue]],  # value
                         _type.HRESULT]


class ITargetedContentStateChangedEventArgs(_inspectable.IInspectable):
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class ITargetedContentSubscription(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    GetContentContainerAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[ITargetedContentContainer]]],  # asyncOperation
                                        _type.HRESULT]
    add_ContentChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ITargetedContentSubscription, ITargetedContentChangedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # cookie
                                  _type.HRESULT]
    remove_ContentChanged: _Callable[[_struct.EventRegistrationToken],  # cookie
                                     _type.HRESULT]
    add_AvailabilityChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ITargetedContentSubscription, ITargetedContentAvailabilityChangedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # cookie
                                       _type.HRESULT]
    remove_AvailabilityChanged: _Callable[[_struct.EventRegistrationToken],  # cookie
                                          _type.HRESULT]
    add_StateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ITargetedContentSubscription, ITargetedContentStateChangedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # cookie
                                _type.HRESULT]
    remove_StateChanged: _Callable[[_struct.EventRegistrationToken],  # cookie
                                   _type.HRESULT]


class ITargetedContentSubscriptionOptions(_inspectable.IInspectable):
    get_SubscriptionId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_AllowPartialContentAvailability: _Callable[[_Pointer[_type.boolean]],  # value
                                                   _type.HRESULT]
    put_AllowPartialContentAvailability: _Callable[[_type.boolean],  # value
                                                   _type.HRESULT]
    get_CloudQueryParameters: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, _type.HSTRING]]],  # value
                                        _type.HRESULT]
    get_LocalFilters: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                _type.HRESULT]
    Update: _Callable[[],
                      _type.HRESULT]


class ITargetedContentSubscriptionStatics(_inspectable.IInspectable):
    GetAsync: _Callable[[_type.HSTRING,  # subscriptionId
                         _Pointer[_Windows_Foundation.IAsyncOperation[ITargetedContentSubscription]]],  # asyncOperation
                        _type.HRESULT]
    GetOptions: _Callable[[_type.HSTRING,  # subscriptionId
                           _Pointer[ITargetedContentSubscriptionOptions]],  # value
                          _type.HRESULT]

    _factory = True


class ITargetedContentValue(_inspectable.IInspectable):
    get_ValueKind: _Callable[[_Pointer[_enum.Windows.Services.TargetedContent.TargetedContentValueKind]],  # value
                             _type.HRESULT]
    get_Path: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_String: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]
    get_Number: _Callable[[_Pointer[_type.DOUBLE]],  # value
                          _type.HRESULT]
    get_Boolean: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_File: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # value
                        _type.HRESULT]
    get_ImageFile: _Callable[[_Pointer[ITargetedContentImage]],  # value
                             _type.HRESULT]
    get_Action: _Callable[[_Pointer[ITargetedContentAction]],  # value
                          _type.HRESULT]
    get_Strings: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                           _type.HRESULT]
    get_Uris: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Foundation.IUriRuntimeClass]]],  # value
                        _type.HRESULT]
    get_Numbers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.DOUBLE]]],  # value
                           _type.HRESULT]
    get_Booleans: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.boolean]]],  # value
                            _type.HRESULT]
    get_Files: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Storage_Streams.IRandomAccessStreamReference]]],  # value
                         _type.HRESULT]
    get_ImageFiles: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[ITargetedContentImage]]],  # value
                              _type.HRESULT]
    get_Actions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[ITargetedContentAction]]],  # value
                           _type.HRESULT]
