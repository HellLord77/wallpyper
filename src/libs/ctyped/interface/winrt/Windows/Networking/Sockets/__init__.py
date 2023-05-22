from __future__ import annotations

from typing import Callable as _Callable

from .. import Connectivity as _Windows_Networking_Connectivity
from ... import Foundation as _Windows_Foundation
from ... import Networking as _Windows_Networking
from ...ApplicationModel import Background as _Windows_ApplicationModel_Background
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Security import Credentials as _Windows_Security_Credentials
from ...Security.Cryptography import Certificates as _Windows_Security_Cryptography_Certificates
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IControlChannelTrigger(_inspectable.IInspectable):
    get_ControlChannelTriggerId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                           _type.HRESULT]
    get_ServerKeepAliveIntervalInMinutes: _Callable[[_Pointer[_type.UINT32]],  # value
                                                    _type.HRESULT]
    put_ServerKeepAliveIntervalInMinutes: _Callable[[_type.UINT32],  # value
                                                    _type.HRESULT]
    get_CurrentKeepAliveIntervalInMinutes: _Callable[[_Pointer[_type.UINT32]],  # value
                                                     _type.HRESULT]
    get_TransportObject: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                   _type.HRESULT]
    get_KeepAliveTrigger: _Callable[[_Pointer[_Windows_ApplicationModel_Background.IBackgroundTrigger]],  # trigger
                                    _type.HRESULT]
    get_PushNotificationTrigger: _Callable[[_Pointer[_Windows_ApplicationModel_Background.IBackgroundTrigger]],  # trigger
                                           _type.HRESULT]
    UsingTransport: _Callable[[_inspectable.IInspectable],  # transport
                              _type.HRESULT]
    WaitForPushEnabled: _Callable[[_Pointer[_enum.Windows.Networking.Sockets.ControlChannelTriggerStatus]],  # channelTriggerStatus
                                  _type.HRESULT]
    DecreaseNetworkKeepAliveInterval: _Callable[[],
                                                _type.HRESULT]
    FlushTransport: _Callable[[],
                              _type.HRESULT]


class IControlChannelTrigger2(_inspectable.IInspectable):
    get_IsWakeFromLowPowerSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]


class IControlChannelTriggerEventDetails(_inspectable.IInspectable):
    get_ControlChannelTrigger: _Callable[[_Pointer[IControlChannelTrigger]],  # value
                                         _type.HRESULT]


class IControlChannelTriggerFactory(_inspectable.IInspectable, factory=True):
    CreateControlChannelTrigger: _Callable[[_type.HSTRING,  # channelId
                                            _type.UINT32,  # serverKeepAliveIntervalInMinutes
                                            _Pointer[IControlChannelTrigger]],  # notificationChannel
                                           _type.HRESULT]
    CreateControlChannelTriggerEx: _Callable[[_type.HSTRING,  # channelId
                                              _type.UINT32,  # serverKeepAliveIntervalInMinutes
                                              _enum.Windows.Networking.Sockets.ControlChannelTriggerResourceType,  # resourceRequestType
                                              _Pointer[IControlChannelTrigger]],  # notificationChannel
                                             _type.HRESULT]


class IControlChannelTriggerResetEventDetails(_inspectable.IInspectable):
    get_ResetReason: _Callable[[_Pointer[_enum.Windows.Networking.Sockets.ControlChannelTriggerResetReason]],  # value
                               _type.HRESULT]
    get_HardwareSlotReset: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    get_SoftwareSlotReset: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]


class IDatagramSocket(_inspectable.IInspectable):
    get_Control: _Callable[[_Pointer[IDatagramSocketControl]],  # value
                           _type.HRESULT]
    get_Information: _Callable[[_Pointer[IDatagramSocketInformation]],  # value
                               _type.HRESULT]
    get_OutputStream: _Callable[[_Pointer[_Windows_Storage_Streams.IOutputStream]],  # value
                                _type.HRESULT]
    ConnectAsync: _Callable[[_Windows_Networking.IHostName,  # remoteHostName
                             _type.HSTRING,  # remoteServiceName
                             _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                            _type.HRESULT]
    ConnectWithEndpointPairAsync: _Callable[[_Windows_Networking.IEndpointPair,  # endpointPair
                                             _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                            _type.HRESULT]
    BindServiceNameAsync: _Callable[[_type.HSTRING,  # localServiceName
                                     _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                    _type.HRESULT]
    BindEndpointAsync: _Callable[[_Windows_Networking.IHostName,  # localHostName
                                  _type.HSTRING,  # localServiceName
                                  _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                 _type.HRESULT]
    JoinMulticastGroup: _Callable[[_Windows_Networking.IHostName],  # host
                                  _type.HRESULT]
    GetOutputStreamAsync: _Callable[[_Windows_Networking.IHostName,  # remoteHostName
                                     _type.HSTRING,  # remoteServiceName
                                     _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IOutputStream]]],  # value
                                    _type.HRESULT]
    GetOutputStreamWithEndpointPairAsync: _Callable[[_Windows_Networking.IEndpointPair,  # endpointPair
                                                     _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IOutputStream]]],  # value
                                                    _type.HRESULT]
    add_MessageReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[IDatagramSocket, IDatagramSocketMessageReceivedEventArgs],  # eventHandler
                                    _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                                   _type.HRESULT]
    remove_MessageReceived: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                      _type.HRESULT]


class IDatagramSocket2(_inspectable.IInspectable):
    BindServiceNameAndAdapterAsync: _Callable[[_type.HSTRING,  # localServiceName
                                               _Windows_Networking_Connectivity.INetworkAdapter,  # adapter
                                               _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                              _type.HRESULT]


class IDatagramSocket3(_inspectable.IInspectable):
    CancelIOAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                             _type.HRESULT]
    EnableTransferOwnership: _Callable[[_struct.GUID],  # taskId
                                       _type.HRESULT]
    EnableTransferOwnershipWithConnectedStandbyAction: _Callable[[_struct.GUID,  # taskId
                                                                  _enum.Windows.Networking.Sockets.SocketActivityConnectedStandbyAction],  # connectedStandbyAction
                                                                 _type.HRESULT]
    TransferOwnership: _Callable[[_type.HSTRING],  # socketId
                                 _type.HRESULT]
    TransferOwnershipWithContext: _Callable[[_type.HSTRING,  # socketId
                                             ISocketActivityContext],  # data
                                            _type.HRESULT]
    TransferOwnershipWithContextAndKeepAliveTime: _Callable[[_type.HSTRING,  # socketId
                                                             ISocketActivityContext,  # data
                                                             _struct.Windows.Foundation.TimeSpan],  # keepAliveTime
                                                            _type.HRESULT]


class IDatagramSocketControl(_inspectable.IInspectable):
    get_QualityOfService: _Callable[[_Pointer[_enum.Windows.Networking.Sockets.SocketQualityOfService]],  # value
                                    _type.HRESULT]
    put_QualityOfService: _Callable[[_enum.Windows.Networking.Sockets.SocketQualityOfService],  # value
                                    _type.HRESULT]
    get_OutboundUnicastHopLimit: _Callable[[_Pointer[_type.BYTE]],  # value
                                           _type.HRESULT]
    put_OutboundUnicastHopLimit: _Callable[[_type.BYTE],  # value
                                           _type.HRESULT]


class IDatagramSocketControl2(_inspectable.IInspectable):
    get_InboundBufferSizeInBytes: _Callable[[_Pointer[_type.UINT32]],  # value
                                            _type.HRESULT]
    put_InboundBufferSizeInBytes: _Callable[[_type.UINT32],  # value
                                            _type.HRESULT]
    get_DontFragment: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_DontFragment: _Callable[[_type.boolean],  # value
                                _type.HRESULT]


class IDatagramSocketControl3(_inspectable.IInspectable):
    get_MulticastOnly: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_MulticastOnly: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]


class IDatagramSocketInformation(_inspectable.IInspectable):
    get_LocalAddress: _Callable[[_Pointer[_Windows_Networking.IHostName]],  # value
                                _type.HRESULT]
    get_LocalPort: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_RemoteAddress: _Callable[[_Pointer[_Windows_Networking.IHostName]],  # value
                                 _type.HRESULT]
    get_RemotePort: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]


class IDatagramSocketMessageReceivedEventArgs(_inspectable.IInspectable):
    get_RemoteAddress: _Callable[[_Pointer[_Windows_Networking.IHostName]],  # value
                                 _type.HRESULT]
    get_RemotePort: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_LocalAddress: _Callable[[_Pointer[_Windows_Networking.IHostName]],  # value
                                _type.HRESULT]
    GetDataReader: _Callable[[_Pointer[_Windows_Storage_Streams.IDataReader]],  # dataReader
                             _type.HRESULT]
    GetDataStream: _Callable[[_Pointer[_Windows_Storage_Streams.IInputStream]],  # inputStream
                             _type.HRESULT]


class IDatagramSocketStatics(_inspectable.IInspectable, factory=True):
    GetEndpointPairsAsync: _Callable[[_Windows_Networking.IHostName,  # remoteHostName
                                      _type.HSTRING,  # remoteServiceName
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_Networking.IEndpointPair]]]],  # operation
                                     _type.HRESULT]
    GetEndpointPairsWithSortOptionsAsync: _Callable[[_Windows_Networking.IHostName,  # remoteHostName
                                                     _type.HSTRING,  # remoteServiceName
                                                     _enum.Windows.Networking.HostNameSortOptions,  # sortOptions
                                                     _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_Networking.IEndpointPair]]]],  # operation
                                                    _type.HRESULT]


class IMessageWebSocket(_inspectable.IInspectable):
    get_Control: _Callable[[_Pointer[IMessageWebSocketControl]],  # value
                           _type.HRESULT]
    get_Information: _Callable[[_Pointer[IWebSocketInformation]],  # value
                               _type.HRESULT]
    add_MessageReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[IMessageWebSocket, IMessageWebSocketMessageReceivedEventArgs],  # eventHandler
                                    _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                                   _type.HRESULT]
    remove_MessageReceived: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                      _type.HRESULT]


class IMessageWebSocket2(_inspectable.IInspectable):
    add_ServerCustomValidationRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IMessageWebSocket, IWebSocketServerCustomValidationRequestedEventArgs],  # eventHandler
                                                    _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                                                   _type.HRESULT]
    remove_ServerCustomValidationRequested: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                                      _type.HRESULT]


class IMessageWebSocket3(_inspectable.IInspectable):
    SendNonfinalFrameAsync: _Callable[[_Windows_Storage_Streams.IBuffer,  # data
                                       _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[_type.UINT32, _type.UINT32]]],  # operation
                                      _type.HRESULT]
    SendFinalFrameAsync: _Callable[[_Windows_Storage_Streams.IBuffer,  # data
                                    _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[_type.UINT32, _type.UINT32]]],  # operation
                                   _type.HRESULT]


class IMessageWebSocketControl(_inspectable.IInspectable):
    get_MaxMessageSize: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]
    put_MaxMessageSize: _Callable[[_type.UINT32],  # value
                                  _type.HRESULT]
    get_MessageType: _Callable[[_Pointer[_enum.Windows.Networking.Sockets.SocketMessageType]],  # value
                               _type.HRESULT]
    put_MessageType: _Callable[[_enum.Windows.Networking.Sockets.SocketMessageType],  # value
                               _type.HRESULT]


class IMessageWebSocketControl2(_inspectable.IInspectable):
    get_DesiredUnsolicitedPongInterval: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                                  _type.HRESULT]
    put_DesiredUnsolicitedPongInterval: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                                  _type.HRESULT]
    get_ActualUnsolicitedPongInterval: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                                 _type.HRESULT]
    get_ReceiveMode: _Callable[[_Pointer[_enum.Windows.Networking.Sockets.MessageWebSocketReceiveMode]],  # value
                               _type.HRESULT]
    put_ReceiveMode: _Callable[[_enum.Windows.Networking.Sockets.MessageWebSocketReceiveMode],  # value
                               _type.HRESULT]
    get_ClientCertificate: _Callable[[_Pointer[_Windows_Security_Cryptography_Certificates.ICertificate]],  # value
                                     _type.HRESULT]
    put_ClientCertificate: _Callable[[_Windows_Security_Cryptography_Certificates.ICertificate],  # value
                                     _type.HRESULT]


class IMessageWebSocketMessageReceivedEventArgs(_inspectable.IInspectable):
    get_MessageType: _Callable[[_Pointer[_enum.Windows.Networking.Sockets.SocketMessageType]],  # value
                               _type.HRESULT]
    GetDataReader: _Callable[[_Pointer[_Windows_Storage_Streams.IDataReader]],  # dataReader
                             _type.HRESULT]
    GetDataStream: _Callable[[_Pointer[_Windows_Storage_Streams.IInputStream]],  # inputStream
                             _type.HRESULT]


class IMessageWebSocketMessageReceivedEventArgs2(_inspectable.IInspectable):
    get_IsMessageComplete: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]


class IServerMessageWebSocket(_inspectable.IInspectable):
    add_MessageReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[IServerMessageWebSocket, IMessageWebSocketMessageReceivedEventArgs],  # value
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_MessageReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    get_Control: _Callable[[_Pointer[IServerMessageWebSocketControl]],  # value
                           _type.HRESULT]
    get_Information: _Callable[[_Pointer[IServerMessageWebSocketInformation]],  # value
                               _type.HRESULT]
    get_OutputStream: _Callable[[_Pointer[_Windows_Storage_Streams.IOutputStream]],  # value
                                _type.HRESULT]
    add_Closed: _Callable[[_Windows_Foundation.ITypedEventHandler[IServerMessageWebSocket, IWebSocketClosedEventArgs],  # value
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Closed: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    CloseWithStatus: _Callable[[_type.UINT16,  # code
                                _type.HSTRING],  # reason
                               _type.HRESULT]


class IServerMessageWebSocketControl(_inspectable.IInspectable):
    get_MessageType: _Callable[[_Pointer[_enum.Windows.Networking.Sockets.SocketMessageType]],  # value
                               _type.HRESULT]
    put_MessageType: _Callable[[_enum.Windows.Networking.Sockets.SocketMessageType],  # value
                               _type.HRESULT]


class IServerMessageWebSocketInformation(_inspectable.IInspectable):
    get_BandwidthStatistics: _Callable[[_Pointer[_struct.Windows.Networking.Sockets.BandwidthStatistics]],  # value
                                       _type.HRESULT]
    get_Protocol: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_LocalAddress: _Callable[[_Pointer[_Windows_Networking.IHostName]],  # value
                                _type.HRESULT]


class IServerStreamWebSocket(_inspectable.IInspectable):
    get_Information: _Callable[[_Pointer[IServerStreamWebSocketInformation]],  # value
                               _type.HRESULT]
    get_InputStream: _Callable[[_Pointer[_Windows_Storage_Streams.IInputStream]],  # value
                               _type.HRESULT]
    get_OutputStream: _Callable[[_Pointer[_Windows_Storage_Streams.IOutputStream]],  # value
                                _type.HRESULT]
    add_Closed: _Callable[[_Windows_Foundation.ITypedEventHandler[IServerStreamWebSocket, IWebSocketClosedEventArgs],  # value
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Closed: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    CloseWithStatus: _Callable[[_type.UINT16,  # code
                                _type.HSTRING],  # reason
                               _type.HRESULT]


class IServerStreamWebSocketInformation(_inspectable.IInspectable):
    get_BandwidthStatistics: _Callable[[_Pointer[_struct.Windows.Networking.Sockets.BandwidthStatistics]],  # value
                                       _type.HRESULT]
    get_Protocol: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_LocalAddress: _Callable[[_Pointer[_Windows_Networking.IHostName]],  # value
                                _type.HRESULT]


class ISocketActivityContext(_inspectable.IInspectable):
    get_Data: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                        _type.HRESULT]


class ISocketActivityContextFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Windows_Storage_Streams.IBuffer,  # data
                       _Pointer[ISocketActivityContext]],  # context
                      _type.HRESULT]


class ISocketActivityInformation(_inspectable.IInspectable):
    get_TaskId: _Callable[[_Pointer[_struct.GUID]],  # value
                          _type.HRESULT]
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_SocketKind: _Callable[[_Pointer[_enum.Windows.Networking.Sockets.SocketActivityKind]],  # value
                              _type.HRESULT]
    get_Context: _Callable[[_Pointer[ISocketActivityContext]],  # value
                           _type.HRESULT]
    get_DatagramSocket: _Callable[[_Pointer[IDatagramSocket]],  # value
                                  _type.HRESULT]
    get_StreamSocket: _Callable[[_Pointer[IStreamSocket]],  # value
                                _type.HRESULT]
    get_StreamSocketListener: _Callable[[_Pointer[IStreamSocketListener]],  # value
                                        _type.HRESULT]


class ISocketActivityInformationStatics(_inspectable.IInspectable, factory=True):
    get_AllSockets: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, ISocketActivityInformation]]],  # sockets
                              _type.HRESULT]


class ISocketActivityTriggerDetails(_inspectable.IInspectable):
    get_Reason: _Callable[[_Pointer[_enum.Windows.Networking.Sockets.SocketActivityTriggerReason]],  # value
                          _type.HRESULT]
    get_SocketInformation: _Callable[[_Pointer[ISocketActivityInformation]],  # value
                                     _type.HRESULT]


class ISocketErrorStatics(_inspectable.IInspectable, factory=True):
    GetStatus: _Callable[[_type.INT32,  # hresult
                          _Pointer[_enum.Windows.Networking.Sockets.SocketErrorStatus]],  # status
                         _type.HRESULT]


class IStreamSocket(_inspectable.IInspectable):
    get_Control: _Callable[[_Pointer[IStreamSocketControl]],  # value
                           _type.HRESULT]
    get_Information: _Callable[[_Pointer[IStreamSocketInformation]],  # value
                               _type.HRESULT]
    get_InputStream: _Callable[[_Pointer[_Windows_Storage_Streams.IInputStream]],  # value
                               _type.HRESULT]
    get_OutputStream: _Callable[[_Pointer[_Windows_Storage_Streams.IOutputStream]],  # value
                                _type.HRESULT]
    ConnectWithEndpointPairAsync: _Callable[[_Windows_Networking.IEndpointPair,  # endpointPair
                                             _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                            _type.HRESULT]
    ConnectAsync: _Callable[[_Windows_Networking.IHostName,  # remoteHostName
                             _type.HSTRING,  # remoteServiceName
                             _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                            _type.HRESULT]
    ConnectWithEndpointPairAndProtectionLevelAsync: _Callable[[_Windows_Networking.IEndpointPair,  # endpointPair
                                                               _enum.Windows.Networking.Sockets.SocketProtectionLevel,  # protectionLevel
                                                               _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                                              _type.HRESULT]
    ConnectWithProtectionLevelAsync: _Callable[[_Windows_Networking.IHostName,  # remoteHostName
                                                _type.HSTRING,  # remoteServiceName
                                                _enum.Windows.Networking.Sockets.SocketProtectionLevel,  # protectionLevel
                                                _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                               _type.HRESULT]
    UpgradeToSslAsync: _Callable[[_enum.Windows.Networking.Sockets.SocketProtectionLevel,  # protectionLevel
                                  _Windows_Networking.IHostName,  # validationHostName
                                  _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                 _type.HRESULT]


class IStreamSocket2(_inspectable.IInspectable):
    ConnectWithProtectionLevelAndAdapterAsync: _Callable[[_Windows_Networking.IHostName,  # remoteHostName
                                                          _type.HSTRING,  # remoteServiceName
                                                          _enum.Windows.Networking.Sockets.SocketProtectionLevel,  # protectionLevel
                                                          _Windows_Networking_Connectivity.INetworkAdapter,  # adapter
                                                          _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                                         _type.HRESULT]


class IStreamSocket3(_inspectable.IInspectable):
    CancelIOAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                             _type.HRESULT]
    EnableTransferOwnership: _Callable[[_struct.GUID],  # taskId
                                       _type.HRESULT]
    EnableTransferOwnershipWithConnectedStandbyAction: _Callable[[_struct.GUID,  # taskId
                                                                  _enum.Windows.Networking.Sockets.SocketActivityConnectedStandbyAction],  # connectedStandbyAction
                                                                 _type.HRESULT]
    TransferOwnership: _Callable[[_type.HSTRING],  # socketId
                                 _type.HRESULT]
    TransferOwnershipWithContext: _Callable[[_type.HSTRING,  # socketId
                                             ISocketActivityContext],  # data
                                            _type.HRESULT]
    TransferOwnershipWithContextAndKeepAliveTime: _Callable[[_type.HSTRING,  # socketId
                                                             ISocketActivityContext,  # data
                                                             _struct.Windows.Foundation.TimeSpan],  # keepAliveTime
                                                            _type.HRESULT]


class IStreamSocketControl(_inspectable.IInspectable):
    get_NoDelay: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_NoDelay: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_KeepAlive: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_KeepAlive: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    get_OutboundBufferSizeInBytes: _Callable[[_Pointer[_type.UINT32]],  # value
                                             _type.HRESULT]
    put_OutboundBufferSizeInBytes: _Callable[[_type.UINT32],  # value
                                             _type.HRESULT]
    get_QualityOfService: _Callable[[_Pointer[_enum.Windows.Networking.Sockets.SocketQualityOfService]],  # value
                                    _type.HRESULT]
    put_QualityOfService: _Callable[[_enum.Windows.Networking.Sockets.SocketQualityOfService],  # value
                                    _type.HRESULT]
    get_OutboundUnicastHopLimit: _Callable[[_Pointer[_type.BYTE]],  # value
                                           _type.HRESULT]
    put_OutboundUnicastHopLimit: _Callable[[_type.BYTE],  # value
                                           _type.HRESULT]


class IStreamSocketControl2(_inspectable.IInspectable):
    get_IgnorableServerCertificateErrors: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_enum.Windows.Security.Cryptography.Certificates.ChainValidationResult]]],  # value
                                                    _type.HRESULT]


class IStreamSocketControl3(_inspectable.IInspectable):
    get_SerializeConnectionAttempts: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]
    put_SerializeConnectionAttempts: _Callable[[_type.boolean],  # value
                                               _type.HRESULT]
    get_ClientCertificate: _Callable[[_Pointer[_Windows_Security_Cryptography_Certificates.ICertificate]],  # value
                                     _type.HRESULT]
    put_ClientCertificate: _Callable[[_Windows_Security_Cryptography_Certificates.ICertificate],  # value
                                     _type.HRESULT]


class IStreamSocketControl4(_inspectable.IInspectable):
    get_MinProtectionLevel: _Callable[[_Pointer[_enum.Windows.Networking.Sockets.SocketProtectionLevel]],  # value
                                      _type.HRESULT]
    put_MinProtectionLevel: _Callable[[_enum.Windows.Networking.Sockets.SocketProtectionLevel],  # value
                                      _type.HRESULT]


class IStreamSocketInformation(_inspectable.IInspectable):
    get_LocalAddress: _Callable[[_Pointer[_Windows_Networking.IHostName]],  # value
                                _type.HRESULT]
    get_LocalPort: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_RemoteHostName: _Callable[[_Pointer[_Windows_Networking.IHostName]],  # value
                                  _type.HRESULT]
    get_RemoteAddress: _Callable[[_Pointer[_Windows_Networking.IHostName]],  # value
                                 _type.HRESULT]
    get_RemoteServiceName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    get_RemotePort: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_RoundTripTimeStatistics: _Callable[[_Pointer[_struct.Windows.Networking.Sockets.RoundTripTimeStatistics]],  # value
                                           _type.HRESULT]
    get_BandwidthStatistics: _Callable[[_Pointer[_struct.Windows.Networking.Sockets.BandwidthStatistics]],  # value
                                       _type.HRESULT]
    get_ProtectionLevel: _Callable[[_Pointer[_enum.Windows.Networking.Sockets.SocketProtectionLevel]],  # value
                                   _type.HRESULT]
    get_SessionKey: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                              _type.HRESULT]


class IStreamSocketInformation2(_inspectable.IInspectable):
    get_ServerCertificateErrorSeverity: _Callable[[_Pointer[_enum.Windows.Networking.Sockets.SocketSslErrorSeverity]],  # value
                                                  _type.HRESULT]
    get_ServerCertificateErrors: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Security.Cryptography.Certificates.ChainValidationResult]]],  # value
                                           _type.HRESULT]
    get_ServerCertificate: _Callable[[_Pointer[_Windows_Security_Cryptography_Certificates.ICertificate]],  # value
                                     _type.HRESULT]
    get_ServerIntermediateCertificates: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Security_Cryptography_Certificates.ICertificate]]],  # value
                                                  _type.HRESULT]


class IStreamSocketListener(_inspectable.IInspectable):
    get_Control: _Callable[[_Pointer[IStreamSocketListenerControl]],  # value
                           _type.HRESULT]
    get_Information: _Callable[[_Pointer[IStreamSocketListenerInformation]],  # value
                               _type.HRESULT]
    BindServiceNameAsync: _Callable[[_type.HSTRING,  # localServiceName
                                     _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                    _type.HRESULT]
    BindEndpointAsync: _Callable[[_Windows_Networking.IHostName,  # localHostName
                                  _type.HSTRING,  # localServiceName
                                  _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                 _type.HRESULT]
    add_ConnectionReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[IStreamSocketListener, IStreamSocketListenerConnectionReceivedEventArgs],  # eventHandler
                                       _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                                      _type.HRESULT]
    remove_ConnectionReceived: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                         _type.HRESULT]


class IStreamSocketListener2(_inspectable.IInspectable):
    BindServiceNameWithProtectionLevelAsync: _Callable[[_type.HSTRING,  # localServiceName
                                                        _enum.Windows.Networking.Sockets.SocketProtectionLevel,  # protectionLevel
                                                        _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                                       _type.HRESULT]
    BindServiceNameWithProtectionLevelAndAdapterAsync: _Callable[[_type.HSTRING,  # localServiceName
                                                                  _enum.Windows.Networking.Sockets.SocketProtectionLevel,  # protectionLevel
                                                                  _Windows_Networking_Connectivity.INetworkAdapter,  # adapter
                                                                  _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                                                 _type.HRESULT]


class IStreamSocketListener3(_inspectable.IInspectable):
    CancelIOAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                             _type.HRESULT]
    EnableTransferOwnership: _Callable[[_struct.GUID],  # taskId
                                       _type.HRESULT]
    EnableTransferOwnershipWithConnectedStandbyAction: _Callable[[_struct.GUID,  # taskId
                                                                  _enum.Windows.Networking.Sockets.SocketActivityConnectedStandbyAction],  # connectedStandbyAction
                                                                 _type.HRESULT]
    TransferOwnership: _Callable[[_type.HSTRING],  # socketId
                                 _type.HRESULT]
    TransferOwnershipWithContext: _Callable[[_type.HSTRING,  # socketId
                                             ISocketActivityContext],  # data
                                            _type.HRESULT]


class IStreamSocketListenerConnectionReceivedEventArgs(_inspectable.IInspectable):
    get_Socket: _Callable[[_Pointer[IStreamSocket]],  # value
                          _type.HRESULT]


class IStreamSocketListenerControl(_inspectable.IInspectable):
    get_QualityOfService: _Callable[[_Pointer[_enum.Windows.Networking.Sockets.SocketQualityOfService]],  # value
                                    _type.HRESULT]
    put_QualityOfService: _Callable[[_enum.Windows.Networking.Sockets.SocketQualityOfService],  # value
                                    _type.HRESULT]


class IStreamSocketListenerControl2(_inspectable.IInspectable):
    get_NoDelay: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_NoDelay: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_KeepAlive: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_KeepAlive: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    get_OutboundBufferSizeInBytes: _Callable[[_Pointer[_type.UINT32]],  # value
                                             _type.HRESULT]
    put_OutboundBufferSizeInBytes: _Callable[[_type.UINT32],  # value
                                             _type.HRESULT]
    get_OutboundUnicastHopLimit: _Callable[[_Pointer[_type.BYTE]],  # value
                                           _type.HRESULT]
    put_OutboundUnicastHopLimit: _Callable[[_type.BYTE],  # value
                                           _type.HRESULT]


class IStreamSocketListenerInformation(_inspectable.IInspectable):
    get_LocalPort: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]


class IStreamSocketStatics(_inspectable.IInspectable, factory=True):
    GetEndpointPairsAsync: _Callable[[_Windows_Networking.IHostName,  # remoteHostName
                                      _type.HSTRING,  # remoteServiceName
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_Networking.IEndpointPair]]]],  # operation
                                     _type.HRESULT]
    GetEndpointPairsWithSortOptionsAsync: _Callable[[_Windows_Networking.IHostName,  # remoteHostName
                                                     _type.HSTRING,  # remoteServiceName
                                                     _enum.Windows.Networking.HostNameSortOptions,  # sortOptions
                                                     _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_Networking.IEndpointPair]]]],  # operation
                                                    _type.HRESULT]


class IStreamWebSocket(_inspectable.IInspectable):
    get_Control: _Callable[[_Pointer[IStreamWebSocketControl]],  # value
                           _type.HRESULT]
    get_Information: _Callable[[_Pointer[IWebSocketInformation]],  # value
                               _type.HRESULT]
    get_InputStream: _Callable[[_Pointer[_Windows_Storage_Streams.IInputStream]],  # value
                               _type.HRESULT]


class IStreamWebSocket2(_inspectable.IInspectable):
    add_ServerCustomValidationRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IStreamWebSocket, IWebSocketServerCustomValidationRequestedEventArgs],  # eventHandler
                                                    _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                                                   _type.HRESULT]
    remove_ServerCustomValidationRequested: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                                      _type.HRESULT]


class IStreamWebSocketControl(_inspectable.IInspectable):
    get_NoDelay: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_NoDelay: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class IStreamWebSocketControl2(_inspectable.IInspectable):
    get_DesiredUnsolicitedPongInterval: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                                  _type.HRESULT]
    put_DesiredUnsolicitedPongInterval: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                                  _type.HRESULT]
    get_ActualUnsolicitedPongInterval: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                                 _type.HRESULT]
    get_ClientCertificate: _Callable[[_Pointer[_Windows_Security_Cryptography_Certificates.ICertificate]],  # value
                                     _type.HRESULT]
    put_ClientCertificate: _Callable[[_Windows_Security_Cryptography_Certificates.ICertificate],  # value
                                     _type.HRESULT]


class IWebSocket(_inspectable.IInspectable):
    get_OutputStream: _Callable[[_Pointer[_Windows_Storage_Streams.IOutputStream]],  # value
                                _type.HRESULT]
    ConnectAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                             _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                            _type.HRESULT]
    SetRequestHeader: _Callable[[_type.HSTRING,  # headerName
                                 _type.HSTRING],  # headerValue
                                _type.HRESULT]
    add_Closed: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebSocket, IWebSocketClosedEventArgs],  # eventHandler
                           _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                          _type.HRESULT]
    remove_Closed: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                             _type.HRESULT]
    CloseWithStatus: _Callable[[_type.UINT16,  # code
                                _type.HSTRING],  # reason
                               _type.HRESULT]


class IWebSocketClosedEventArgs(_inspectable.IInspectable):
    get_Code: _Callable[[_Pointer[_type.UINT16]],  # value
                        _type.HRESULT]
    get_Reason: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]


class IWebSocketControl(_inspectable.IInspectable):
    get_OutboundBufferSizeInBytes: _Callable[[_Pointer[_type.UINT32]],  # value
                                             _type.HRESULT]
    put_OutboundBufferSizeInBytes: _Callable[[_type.UINT32],  # value
                                             _type.HRESULT]
    get_ServerCredential: _Callable[[_Pointer[_Windows_Security_Credentials.IPasswordCredential]],  # value
                                    _type.HRESULT]
    put_ServerCredential: _Callable[[_Windows_Security_Credentials.IPasswordCredential],  # value
                                    _type.HRESULT]
    get_ProxyCredential: _Callable[[_Pointer[_Windows_Security_Credentials.IPasswordCredential]],  # value
                                   _type.HRESULT]
    put_ProxyCredential: _Callable[[_Windows_Security_Credentials.IPasswordCredential],  # value
                                   _type.HRESULT]
    get_SupportedProtocols: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                      _type.HRESULT]


class IWebSocketControl2(_inspectable.IInspectable):
    get_IgnorableServerCertificateErrors: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_enum.Windows.Security.Cryptography.Certificates.ChainValidationResult]]],  # value
                                                    _type.HRESULT]


class IWebSocketErrorStatics(_inspectable.IInspectable, factory=True):
    GetStatus: _Callable[[_type.INT32,  # hresult
                          _Pointer[_enum.Windows.Web.WebErrorStatus]],  # status
                         _type.HRESULT]


class IWebSocketInformation(_inspectable.IInspectable):
    get_LocalAddress: _Callable[[_Pointer[_Windows_Networking.IHostName]],  # value
                                _type.HRESULT]
    get_BandwidthStatistics: _Callable[[_Pointer[_struct.Windows.Networking.Sockets.BandwidthStatistics]],  # value
                                       _type.HRESULT]
    get_Protocol: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]


class IWebSocketInformation2(_inspectable.IInspectable):
    get_ServerCertificate: _Callable[[_Pointer[_Windows_Security_Cryptography_Certificates.ICertificate]],  # value
                                     _type.HRESULT]
    get_ServerCertificateErrorSeverity: _Callable[[_Pointer[_enum.Windows.Networking.Sockets.SocketSslErrorSeverity]],  # value
                                                  _type.HRESULT]
    get_ServerCertificateErrors: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Security.Cryptography.Certificates.ChainValidationResult]]],  # value
                                           _type.HRESULT]
    get_ServerIntermediateCertificates: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Security_Cryptography_Certificates.ICertificate]]],  # value
                                                  _type.HRESULT]


class IWebSocketServerCustomValidationRequestedEventArgs(_inspectable.IInspectable):
    get_ServerCertificate: _Callable[[_Pointer[_Windows_Security_Cryptography_Certificates.ICertificate]],  # value
                                     _type.HRESULT]
    get_ServerCertificateErrorSeverity: _Callable[[_Pointer[_enum.Windows.Networking.Sockets.SocketSslErrorSeverity]],  # value
                                                  _type.HRESULT]
    get_ServerCertificateErrors: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Security.Cryptography.Certificates.ChainValidationResult]]],  # value
                                           _type.HRESULT]
    get_ServerIntermediateCertificates: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Security_Cryptography_Certificates.ICertificate]]],  # value
                                                  _type.HRESULT]
    Reject: _Callable[[],
                      _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]
