from __future__ import annotations

from typing import Callable as _Callable

from .. import Playback as _Windows_Media_Playback
from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from .....um import Unknwnbase as _Unknwnbase
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class _IComponentLoadFailedEventHandler:
    Invoke: _Callable[[IMediaProtectionManager,  # sender
                       IComponentLoadFailedEventArgs],  # e
                      _type.HRESULT]


class IComponentLoadFailedEventHandler(_IComponentLoadFailedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IComponentLoadFailedEventHandler_impl(_IComponentLoadFailedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IRebootNeededEventHandler:
    Invoke: _Callable[[IMediaProtectionManager],  # sender
                      _type.HRESULT]


class IRebootNeededEventHandler(_IRebootNeededEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IRebootNeededEventHandler_impl(_IRebootNeededEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IServiceRequestedEventHandler:
    Invoke: _Callable[[IMediaProtectionManager,  # sender
                       IServiceRequestedEventArgs],  # e
                      _type.HRESULT]


class IServiceRequestedEventHandler(_IServiceRequestedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IServiceRequestedEventHandler_impl(_IServiceRequestedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class IComponentLoadFailedEventArgs(_inspectable.IInspectable):
    get_Information: _Callable[[_Pointer[IRevocationAndRenewalInformation]],  # value
                               _type.HRESULT]
    get_Completion: _Callable[[_Pointer[IMediaProtectionServiceCompletion]],  # value
                              _type.HRESULT]


class IComponentRenewalStatics(_inspectable.IInspectable, factory=True):
    RenewSystemComponentsAsync: _Callable[[IRevocationAndRenewalInformation,  # information
                                           _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[_enum.Windows.Media.Protection.RenewalStatus, _type.UINT32]]],  # operation
                                          _type.HRESULT]


class IHdcpSession(_inspectable.IInspectable):
    IsEffectiveProtectionAtLeast: _Callable[[_enum.Windows.Media.Protection.HdcpProtection,  # protection
                                             _Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    GetEffectiveProtection: _Callable[[_Pointer[_Windows_Foundation.IReference[_enum.Windows.Media.Protection.HdcpProtection]]],  # value
                                      _type.HRESULT]
    SetDesiredMinProtectionAsync: _Callable[[_enum.Windows.Media.Protection.HdcpProtection,  # protection
                                             _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Media.Protection.HdcpSetProtectionResult]]],  # value
                                            _type.HRESULT]
    add_ProtectionChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IHdcpSession, _inspectable.IInspectable],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_ProtectionChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]


class IMediaProtectionManager(_inspectable.IInspectable):
    add_ServiceRequested: _Callable[[IServiceRequestedEventHandler,  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # cookie
                                    _type.HRESULT]
    remove_ServiceRequested: _Callable[[_struct.EventRegistrationToken],  # cookie
                                       _type.HRESULT]
    add_RebootNeeded: _Callable[[IRebootNeededEventHandler,  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # cookie
                                _type.HRESULT]
    remove_RebootNeeded: _Callable[[_struct.EventRegistrationToken],  # cookie
                                   _type.HRESULT]
    add_ComponentLoadFailed: _Callable[[IComponentLoadFailedEventHandler,  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # cookie
                                       _type.HRESULT]
    remove_ComponentLoadFailed: _Callable[[_struct.EventRegistrationToken],  # cookie
                                          _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                              _type.HRESULT]


class IMediaProtectionPMPServer(_inspectable.IInspectable):
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # ppProperties
                              _type.HRESULT]


class IMediaProtectionPMPServerFactory(_inspectable.IInspectable, factory=True):
    CreatePMPServer: _Callable[[_Windows_Foundation_Collections.IPropertySet,  # pProperties
                                _Pointer[IMediaProtectionPMPServer]],  # ppObject
                               _type.HRESULT]


class IMediaProtectionServiceCompletion(_inspectable.IInspectable):
    Complete: _Callable[[_type.boolean],  # success
                        _type.HRESULT]


class IMediaProtectionServiceRequest(_inspectable.IInspectable):
    get_ProtectionSystem: _Callable[[_Pointer[_struct.GUID]],  # system
                                    _type.HRESULT]
    get_Type: _Callable[[_Pointer[_struct.GUID]],  # type
                        _type.HRESULT]


class IProtectionCapabilities(_inspectable.IInspectable):
    IsTypeSupported: _Callable[[_type.HSTRING,  # type
                                _type.HSTRING,  # keySystem
                                _Pointer[_enum.Windows.Media.Protection.ProtectionCapabilityResult]],  # value
                               _type.HRESULT]


class IRevocationAndRenewalInformation(_inspectable.IInspectable):
    get_Items: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IRevocationAndRenewalItem]]],  # items
                         _type.HRESULT]


class IRevocationAndRenewalItem(_inspectable.IInspectable):
    get_Reasons: _Callable[[_Pointer[_enum.Windows.Media.Protection.RevocationAndRenewalReasons]],  # reasons
                           _type.HRESULT]
    get_HeaderHash: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_PublicKeyHash: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # name
                        _type.HRESULT]
    get_RenewalId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]


class IServiceRequestedEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IMediaProtectionServiceRequest]],  # value
                           _type.HRESULT]
    get_Completion: _Callable[[_Pointer[IMediaProtectionServiceCompletion]],  # value
                              _type.HRESULT]


class IServiceRequestedEventArgs2(_inspectable.IInspectable):
    get_MediaPlaybackItem: _Callable[[_Pointer[_Windows_Media_Playback.IMediaPlaybackItem]],  # value
                                     _type.HRESULT]
