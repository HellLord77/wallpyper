from __future__ import annotations

from typing import Callable as _Callable

from ... import Enumeration as _Windows_Devices_Enumeration
from .... import Foundation as _Windows_Foundation
from .... import Networking as _Windows_Networking
from ....Foundation import Collections as _Windows_Foundation_Collections
from ....Networking import Sockets as _Windows_Networking_Sockets
from ....Storage import Streams as _Windows_Storage_Streams
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IWiFiDirectService(_inspectable.IInspectable):
    get_RemoteServiceInfo: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                     _type.HRESULT]
    get_SupportedConfigurationMethods: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceConfigurationMethod]]],  # value
                                                 _type.HRESULT]
    get_PreferGroupOwnerMode: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    put_PreferGroupOwnerMode: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]
    get_SessionInfo: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                               _type.HRESULT]
    put_SessionInfo: _Callable[[_Windows_Storage_Streams.IBuffer],  # value
                               _type.HRESULT]
    get_ServiceError: _Callable[[_Pointer[_enum.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceError]],  # value
                                _type.HRESULT]
    add_SessionDeferred: _Callable[[_Windows_Foundation.ITypedEventHandler[IWiFiDirectService, IWiFiDirectServiceSessionDeferredEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_SessionDeferred: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    GetProvisioningInfoAsync: _Callable[[_enum.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceConfigurationMethod,  # selectedConfigurationMethod
                                         _Pointer[_Windows_Foundation.IAsyncOperation[IWiFiDirectServiceProvisioningInfo]]],  # result
                                        _type.HRESULT]
    ConnectAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IWiFiDirectServiceSession]]],  # result
                            _type.HRESULT]
    ConnectAsyncWithPin: _Callable[[_type.HSTRING,  # pin
                                    _Pointer[_Windows_Foundation.IAsyncOperation[IWiFiDirectServiceSession]]],  # result
                                   _type.HRESULT]


class IWiFiDirectServiceAdvertiser(_inspectable.IInspectable):
    get_ServiceName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_ServiceNamePrefixes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                       _type.HRESULT]
    get_ServiceInfo: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                               _type.HRESULT]
    put_ServiceInfo: _Callable[[_Windows_Storage_Streams.IBuffer],  # value
                               _type.HRESULT]
    get_AutoAcceptSession: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    put_AutoAcceptSession: _Callable[[_type.boolean],  # value
                                     _type.HRESULT]
    get_PreferGroupOwnerMode: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    put_PreferGroupOwnerMode: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]
    get_PreferredConfigurationMethods: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_enum.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceConfigurationMethod]]],  # value
                                                 _type.HRESULT]
    get_ServiceStatus: _Callable[[_Pointer[_enum.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceStatus]],  # value
                                 _type.HRESULT]
    put_ServiceStatus: _Callable[[_enum.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceStatus],  # value
                                 _type.HRESULT]
    get_CustomServiceStatusCode: _Callable[[_Pointer[_type.UINT32]],  # value
                                           _type.HRESULT]
    put_CustomServiceStatusCode: _Callable[[_type.UINT32],  # value
                                           _type.HRESULT]
    get_DeferredSessionInfo: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                       _type.HRESULT]
    put_DeferredSessionInfo: _Callable[[_Windows_Storage_Streams.IBuffer],  # value
                                       _type.HRESULT]
    get_AdvertisementStatus: _Callable[[_Pointer[_enum.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceAdvertisementStatus]],  # value
                                       _type.HRESULT]
    get_ServiceError: _Callable[[_Pointer[_enum.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceError]],  # value
                                _type.HRESULT]
    add_SessionRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IWiFiDirectServiceAdvertiser, IWiFiDirectServiceSessionRequestedEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_SessionRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    add_AutoAcceptSessionConnected: _Callable[[_Windows_Foundation.ITypedEventHandler[IWiFiDirectServiceAdvertiser, IWiFiDirectServiceAutoAcceptSessionConnectedEventArgs],  # handler
                                               _Pointer[_struct.EventRegistrationToken]],  # token
                                              _type.HRESULT]
    remove_AutoAcceptSessionConnected: _Callable[[_struct.EventRegistrationToken],  # token
                                                 _type.HRESULT]
    add_AdvertisementStatusChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IWiFiDirectServiceAdvertiser, _inspectable.IInspectable],  # handler
                                               _Pointer[_struct.EventRegistrationToken]],  # token
                                              _type.HRESULT]
    remove_AdvertisementStatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                 _type.HRESULT]
    ConnectAsync: _Callable[[_Windows_Devices_Enumeration.IDeviceInformation,  # deviceInfo
                             _Pointer[_Windows_Foundation.IAsyncOperation[IWiFiDirectServiceSession]]],  # result
                            _type.HRESULT]
    ConnectAsyncWithPin: _Callable[[_Windows_Devices_Enumeration.IDeviceInformation,  # deviceInfo
                                    _type.HSTRING,  # pin
                                    _Pointer[_Windows_Foundation.IAsyncOperation[IWiFiDirectServiceSession]]],  # result
                                   _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]


class IWiFiDirectServiceAdvertiserFactory(_inspectable.IInspectable):
    CreateWiFiDirectServiceAdvertiser: _Callable[[_type.HSTRING,  # serviceName
                                                  _Pointer[IWiFiDirectServiceAdvertiser]],  # result
                                                 _type.HRESULT]

    _factory = True


class IWiFiDirectServiceAutoAcceptSessionConnectedEventArgs(_inspectable.IInspectable):
    get_Session: _Callable[[_Pointer[IWiFiDirectServiceSession]],  # value
                           _type.HRESULT]
    get_SessionInfo: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                               _type.HRESULT]


class IWiFiDirectServiceProvisioningInfo(_inspectable.IInspectable):
    get_SelectedConfigurationMethod: _Callable[[_Pointer[_enum.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceConfigurationMethod]],  # value
                                               _type.HRESULT]
    get_IsGroupFormationNeeded: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]


class IWiFiDirectServiceRemotePortAddedEventArgs(_inspectable.IInspectable):
    get_EndpointPairs: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Networking.IEndpointPair]]],  # value
                                 _type.HRESULT]
    get_Protocol: _Callable[[_Pointer[_enum.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceIPProtocol]],  # value
                            _type.HRESULT]


class IWiFiDirectServiceSession(_inspectable.IInspectable):
    get_ServiceName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSessionStatus]],  # value
                          _type.HRESULT]
    get_ErrorStatus: _Callable[[_Pointer[_enum.Windows.Devices.WiFiDirect.Services.WiFiDirectServiceSessionErrorStatus]],  # value
                               _type.HRESULT]
    get_SessionId: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    get_AdvertisementId: _Callable[[_Pointer[_type.UINT32]],  # value
                                   _type.HRESULT]
    get_ServiceAddress: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_SessionAddress: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    GetConnectionEndpointPairs: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Networking.IEndpointPair]]],  # value
                                          _type.HRESULT]
    add_SessionStatusChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IWiFiDirectServiceSession, _inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_SessionStatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    AddStreamSocketListenerAsync: _Callable[[_Windows_Networking_Sockets.IStreamSocketListener,  # value
                                             _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                            _type.HRESULT]
    AddDatagramSocketAsync: _Callable[[_Windows_Networking_Sockets.IDatagramSocket,  # value
                                       _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                      _type.HRESULT]
    add_RemotePortAdded: _Callable[[_Windows_Foundation.ITypedEventHandler[IWiFiDirectServiceSession, IWiFiDirectServiceRemotePortAddedEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_RemotePortAdded: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]


class IWiFiDirectServiceSessionDeferredEventArgs(_inspectable.IInspectable):
    get_DeferredSessionInfo: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                       _type.HRESULT]


class IWiFiDirectServiceSessionRequest(_inspectable.IInspectable):
    get_DeviceInformation: _Callable[[_Pointer[_Windows_Devices_Enumeration.IDeviceInformation]],  # value
                                     _type.HRESULT]
    get_ProvisioningInfo: _Callable[[_Pointer[IWiFiDirectServiceProvisioningInfo]],  # value
                                    _type.HRESULT]
    get_SessionInfo: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                               _type.HRESULT]


class IWiFiDirectServiceSessionRequestedEventArgs(_inspectable.IInspectable):
    GetSessionRequest: _Callable[[_Pointer[IWiFiDirectServiceSessionRequest]],  # value
                                 _type.HRESULT]


class IWiFiDirectServiceStatics(_inspectable.IInspectable):
    GetSelector: _Callable[[_type.HSTRING,  # serviceName
                            _Pointer[_type.HSTRING]],  # serviceSelector
                           _type.HRESULT]
    GetSelectorWithFilter: _Callable[[_type.HSTRING,  # serviceName
                                      _Windows_Storage_Streams.IBuffer,  # serviceInfoFilter
                                      _Pointer[_type.HSTRING]],  # serviceSelector
                                     _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IWiFiDirectService]]],  # asyncOp
                           _type.HRESULT]

    _factory = True
