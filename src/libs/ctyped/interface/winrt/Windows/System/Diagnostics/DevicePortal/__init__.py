from __future__ import annotations

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from ....ApplicationModel import AppService as _Windows_ApplicationModel_AppService
from ....Foundation import Collections as _Windows_Foundation_Collections
from ....Networking import Sockets as _Windows_Networking_Sockets
from ....Web import Http as _Windows_Web_Http
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IDevicePortalConnection(_inspectable.IInspectable):
    add_Closed: _Callable[[_Windows_Foundation.ITypedEventHandler[IDevicePortalConnection, IDevicePortalConnectionClosedEventArgs],  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Closed: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    add_RequestReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[IDevicePortalConnection, IDevicePortalConnectionRequestReceivedEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_RequestReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]


class IDevicePortalConnectionClosedEventArgs(_inspectable.IInspectable):
    get_Reason: _Callable[[_Pointer[_enum.Windows.System.Diagnostics.DevicePortal.DevicePortalConnectionClosedReason]],  # value
                          _type.HRESULT]


class IDevicePortalConnectionRequestReceivedEventArgs(_inspectable.IInspectable):
    get_RequestMessage: _Callable[[_Pointer[_Windows_Web_Http.IHttpRequestMessage]],  # value
                                  _type.HRESULT]
    get_ResponseMessage: _Callable[[_Pointer[_Windows_Web_Http.IHttpResponseMessage]],  # value
                                   _type.HRESULT]


class IDevicePortalConnectionStatics(_inspectable.IInspectable, factory=True):
    GetForAppServiceConnection: _Callable[[_Windows_ApplicationModel_AppService.IAppServiceConnection,  # appServiceConnection
                                           _Pointer[IDevicePortalConnection]],  # value
                                          _type.HRESULT]


class IDevicePortalWebSocketConnection(_inspectable.IInspectable):
    GetServerMessageWebSocketForRequest: _Callable[[_Windows_Web_Http.IHttpRequestMessage,  # request
                                                    _Pointer[_Windows_Networking_Sockets.IServerMessageWebSocket]],  # result
                                                   _type.HRESULT]
    GetServerMessageWebSocketForRequest2: _Callable[[_Windows_Web_Http.IHttpRequestMessage,  # request
                                                     _enum.Windows.Networking.Sockets.SocketMessageType,  # messageType
                                                     _type.HSTRING,  # protocol
                                                     _Pointer[_Windows_Networking_Sockets.IServerMessageWebSocket]],  # result
                                                    _type.HRESULT]
    GetServerMessageWebSocketForRequest3: _Callable[[_Windows_Web_Http.IHttpRequestMessage,  # request
                                                     _enum.Windows.Networking.Sockets.SocketMessageType,  # messageType
                                                     _type.HSTRING,  # protocol
                                                     _type.UINT32,  # outboundBufferSizeInBytes
                                                     _type.UINT32,  # maxMessageSize
                                                     _enum.Windows.Networking.Sockets.MessageWebSocketReceiveMode,  # receiveMode
                                                     _Pointer[_Windows_Networking_Sockets.IServerMessageWebSocket]],  # result
                                                    _type.HRESULT]
    GetServerStreamWebSocketForRequest: _Callable[[_Windows_Web_Http.IHttpRequestMessage,  # request
                                                   _Pointer[_Windows_Networking_Sockets.IServerStreamWebSocket]],  # result
                                                  _type.HRESULT]
    GetServerStreamWebSocketForRequest2: _Callable[[_Windows_Web_Http.IHttpRequestMessage,  # request
                                                    _type.HSTRING,  # protocol
                                                    _type.UINT32,  # outboundBufferSizeInBytes
                                                    _type.boolean,  # noDelay
                                                    _Pointer[_Windows_Networking_Sockets.IServerStreamWebSocket]],  # result
                                                   _type.HRESULT]


class IDevicePortalWebSocketConnectionRequestReceivedEventArgs(_inspectable.IInspectable):
    get_IsWebSocketUpgradeRequest: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    get_WebSocketProtocolsRequested: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                               _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]
