from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import Networking as _Windows_Networking
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IXboxLiveDeviceAddress(_inspectable.IInspectable):
    add_SnapshotChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IXboxLiveDeviceAddress, _inspectable.IInspectable],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_SnapshotChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    GetSnapshotAsBase64: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    GetSnapshotAsBuffer: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                   _type.HRESULT]
    GetSnapshotAsBytes: _Callable[[_type.UINT32,  # __bufferSize
                                   _Pointer[_type.BYTE],  # buffer
                                   _Pointer[_type.UINT32]],  # bytesWritten
                                  _type.HRESULT]
    Compare: _Callable[[IXboxLiveDeviceAddress,  # otherDeviceAddress
                        _Pointer[_type.INT32]],  # result
                       _type.HRESULT]
    get_IsValid: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_IsLocal: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_NetworkAccessKind: _Callable[[_Pointer[_enum.Windows.Networking.XboxLive.XboxLiveNetworkAccessKind]],  # value
                                     _type.HRESULT]


class IXboxLiveDeviceAddressStatics(_inspectable.IInspectable):
    CreateFromSnapshotBase64: _Callable[[_type.HSTRING,  # base64
                                         _Pointer[IXboxLiveDeviceAddress]],  # value
                                        _type.HRESULT]
    CreateFromSnapshotBuffer: _Callable[[_Windows_Storage_Streams.IBuffer,  # buffer
                                         _Pointer[IXboxLiveDeviceAddress]],  # value
                                        _type.HRESULT]
    CreateFromSnapshotBytes: _Callable[[_type.UINT32,  # __bufferSize
                                        _Pointer[_type.BYTE],  # buffer
                                        _Pointer[IXboxLiveDeviceAddress]],  # value
                                       _type.HRESULT]
    GetLocal: _Callable[[_Pointer[IXboxLiveDeviceAddress]],  # value
                        _type.HRESULT]
    get_MaxSnapshotBytesSize: _Callable[[_Pointer[_type.UINT32]],  # value
                                        _type.HRESULT]

    _factory = True


class IXboxLiveEndpointPair(_inspectable.IInspectable):
    add_StateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IXboxLiveEndpointPair, IXboxLiveEndpointPairStateChangedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_StateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    DeleteAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # action
                           _type.HRESULT]
    GetRemoteSocketAddressBytes: _Callable[[_type.UINT32,  # __socketAddressSize
                                            _Pointer[_type.BYTE]],  # socketAddress
                                           _type.HRESULT]
    GetLocalSocketAddressBytes: _Callable[[_type.UINT32,  # __socketAddressSize
                                           _Pointer[_type.BYTE]],  # socketAddress
                                          _type.HRESULT]
    get_State: _Callable[[_Pointer[_enum.Windows.Networking.XboxLive.XboxLiveEndpointPairState]],  # value
                         _type.HRESULT]
    get_Template: _Callable[[_Pointer[IXboxLiveEndpointPairTemplate]],  # value
                            _type.HRESULT]
    get_RemoteDeviceAddress: _Callable[[_Pointer[IXboxLiveDeviceAddress]],  # value
                                       _type.HRESULT]
    get_RemoteHostName: _Callable[[_Pointer[_Windows_Networking.IHostName]],  # value
                                  _type.HRESULT]
    get_RemotePort: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_LocalHostName: _Callable[[_Pointer[_Windows_Networking.IHostName]],  # value
                                 _type.HRESULT]
    get_LocalPort: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]


class IXboxLiveEndpointPairCreationResult(_inspectable.IInspectable):
    get_DeviceAddress: _Callable[[_Pointer[IXboxLiveDeviceAddress]],  # value
                                 _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.Networking.XboxLive.XboxLiveEndpointPairCreationStatus]],  # value
                          _type.HRESULT]
    get_IsExistingPathEvaluation: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    get_EndpointPair: _Callable[[_Pointer[IXboxLiveEndpointPair]],  # value
                                _type.HRESULT]


class IXboxLiveEndpointPairStateChangedEventArgs(_inspectable.IInspectable):
    get_OldState: _Callable[[_Pointer[_enum.Windows.Networking.XboxLive.XboxLiveEndpointPairState]],  # value
                            _type.HRESULT]
    get_NewState: _Callable[[_Pointer[_enum.Windows.Networking.XboxLive.XboxLiveEndpointPairState]],  # value
                            _type.HRESULT]


class IXboxLiveEndpointPairStatics(_inspectable.IInspectable):
    FindEndpointPairBySocketAddressBytes: _Callable[[_type.UINT32,  # __localSocketAddressSize
                                                     _Pointer[_type.BYTE],  # localSocketAddress
                                                     _type.UINT32,  # __remoteSocketAddressSize
                                                     _Pointer[_type.BYTE],  # remoteSocketAddress
                                                     _Pointer[IXboxLiveEndpointPair]],  # endpointPair
                                                    _type.HRESULT]
    FindEndpointPairByHostNamesAndPorts: _Callable[[_Windows_Networking.IHostName,  # localHostName
                                                    _type.HSTRING,  # localPort
                                                    _Windows_Networking.IHostName,  # remoteHostName
                                                    _type.HSTRING,  # remotePort
                                                    _Pointer[IXboxLiveEndpointPair]],  # endpointPair
                                                   _type.HRESULT]

    _factory = True


class IXboxLiveEndpointPairTemplate(_inspectable.IInspectable):
    add_InboundEndpointPairCreated: _Callable[[_Windows_Foundation.ITypedEventHandler[IXboxLiveEndpointPairTemplate, IXboxLiveInboundEndpointPairCreatedEventArgs],  # handler
                                               _Pointer[_struct.EventRegistrationToken]],  # token
                                              _type.HRESULT]
    remove_InboundEndpointPairCreated: _Callable[[_struct.EventRegistrationToken],  # token
                                                 _type.HRESULT]
    CreateEndpointPairDefaultAsync: _Callable[[IXboxLiveDeviceAddress,  # deviceAddress
                                               _Pointer[_Windows_Foundation.IAsyncOperation[IXboxLiveEndpointPairCreationResult]]],  # operation
                                              _type.HRESULT]
    CreateEndpointPairWithBehaviorsAsync: _Callable[[IXboxLiveDeviceAddress,  # deviceAddress
                                                     _enum.Windows.Networking.XboxLive.XboxLiveEndpointPairCreationBehaviors,  # behaviors
                                                     _Pointer[_Windows_Foundation.IAsyncOperation[IXboxLiveEndpointPairCreationResult]]],  # operation
                                                    _type.HRESULT]
    CreateEndpointPairForPortsDefaultAsync: _Callable[[IXboxLiveDeviceAddress,  # deviceAddress
                                                       _type.HSTRING,  # initiatorPort
                                                       _type.HSTRING,  # acceptorPort
                                                       _Pointer[_Windows_Foundation.IAsyncOperation[IXboxLiveEndpointPairCreationResult]]],  # operation
                                                      _type.HRESULT]
    CreateEndpointPairForPortsWithBehaviorsAsync: _Callable[[IXboxLiveDeviceAddress,  # deviceAddress
                                                             _type.HSTRING,  # initiatorPort
                                                             _type.HSTRING,  # acceptorPort
                                                             _enum.Windows.Networking.XboxLive.XboxLiveEndpointPairCreationBehaviors,  # behaviors
                                                             _Pointer[_Windows_Foundation.IAsyncOperation[IXboxLiveEndpointPairCreationResult]]],  # operation
                                                            _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_SocketKind: _Callable[[_Pointer[_enum.Windows.Networking.XboxLive.XboxLiveSocketKind]],  # value
                              _type.HRESULT]
    get_InitiatorBoundPortRangeLower: _Callable[[_Pointer[_type.UINT16]],  # value
                                                _type.HRESULT]
    get_InitiatorBoundPortRangeUpper: _Callable[[_Pointer[_type.UINT16]],  # value
                                                _type.HRESULT]
    get_AcceptorBoundPortRangeLower: _Callable[[_Pointer[_type.UINT16]],  # value
                                               _type.HRESULT]
    get_AcceptorBoundPortRangeUpper: _Callable[[_Pointer[_type.UINT16]],  # value
                                               _type.HRESULT]
    get_EndpointPairs: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IXboxLiveEndpointPair]]],  # value
                                 _type.HRESULT]


class IXboxLiveEndpointPairTemplateStatics(_inspectable.IInspectable):
    GetTemplateByName: _Callable[[_type.HSTRING,  # name
                                  _Pointer[IXboxLiveEndpointPairTemplate]],  # namedTemplate
                                 _type.HRESULT]
    get_Templates: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IXboxLiveEndpointPairTemplate]]],  # value
                             _type.HRESULT]

    _factory = True


class IXboxLiveInboundEndpointPairCreatedEventArgs(_inspectable.IInspectable):
    get_EndpointPair: _Callable[[_Pointer[IXboxLiveEndpointPair]],  # value
                                _type.HRESULT]


class IXboxLiveQualityOfServiceMeasurement(_inspectable.IInspectable):
    MeasureAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # action
                            _type.HRESULT]
    GetMetricResultsForDevice: _Callable[[IXboxLiveDeviceAddress,  # deviceAddress
                                          _Pointer[_Windows_Foundation_Collections.IVectorView[IXboxLiveQualityOfServiceMetricResult]]],  # value
                                         _type.HRESULT]
    GetMetricResultsForMetric: _Callable[[_enum.Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetric,  # metric
                                          _Pointer[_Windows_Foundation_Collections.IVectorView[IXboxLiveQualityOfServiceMetricResult]]],  # value
                                         _type.HRESULT]
    GetMetricResult: _Callable[[IXboxLiveDeviceAddress,  # deviceAddress
                                _enum.Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetric,  # metric
                                _Pointer[IXboxLiveQualityOfServiceMetricResult]],  # value
                               _type.HRESULT]
    GetPrivatePayloadResult: _Callable[[IXboxLiveDeviceAddress,  # deviceAddress
                                        _Pointer[IXboxLiveQualityOfServicePrivatePayloadResult]],  # value
                                       _type.HRESULT]
    get_Metrics: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_enum.Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetric]]],  # value
                           _type.HRESULT]
    get_DeviceAddresses: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IXboxLiveDeviceAddress]]],  # value
                                   _type.HRESULT]
    get_ShouldRequestPrivatePayloads: _Callable[[_Pointer[_type.boolean]],  # value
                                                _type.HRESULT]
    put_ShouldRequestPrivatePayloads: _Callable[[_type.boolean],  # value
                                                _type.HRESULT]
    get_TimeoutInMilliseconds: _Callable[[_Pointer[_type.UINT32]],  # value
                                         _type.HRESULT]
    put_TimeoutInMilliseconds: _Callable[[_type.UINT32],  # value
                                         _type.HRESULT]
    get_NumberOfProbesToAttempt: _Callable[[_Pointer[_type.UINT32]],  # value
                                           _type.HRESULT]
    put_NumberOfProbesToAttempt: _Callable[[_type.UINT32],  # value
                                           _type.HRESULT]
    get_NumberOfResultsPending: _Callable[[_Pointer[_type.UINT32]],  # value
                                          _type.HRESULT]
    get_MetricResults: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IXboxLiveQualityOfServiceMetricResult]]],  # value
                                 _type.HRESULT]
    get_PrivatePayloadResults: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IXboxLiveQualityOfServicePrivatePayloadResult]]],  # value
                                         _type.HRESULT]


class IXboxLiveQualityOfServiceMeasurementStatics(_inspectable.IInspectable):
    PublishPrivatePayloadBytes: _Callable[[_type.UINT32,  # __payloadSize
                                           _Pointer[_type.BYTE]],  # payload
                                          _type.HRESULT]
    ClearPrivatePayload: _Callable[[],
                                   _type.HRESULT]
    get_MaxSimultaneousProbeConnections: _Callable[[_Pointer[_type.UINT32]],  # value
                                                   _type.HRESULT]
    put_MaxSimultaneousProbeConnections: _Callable[[_type.UINT32],  # value
                                                   _type.HRESULT]
    get_IsSystemOutboundBandwidthConstrained: _Callable[[_Pointer[_type.boolean]],  # value
                                                        _type.HRESULT]
    put_IsSystemOutboundBandwidthConstrained: _Callable[[_type.boolean],  # value
                                                        _type.HRESULT]
    get_IsSystemInboundBandwidthConstrained: _Callable[[_Pointer[_type.boolean]],  # value
                                                       _type.HRESULT]
    put_IsSystemInboundBandwidthConstrained: _Callable[[_type.boolean],  # value
                                                       _type.HRESULT]
    get_PublishedPrivatePayload: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                           _type.HRESULT]
    put_PublishedPrivatePayload: _Callable[[_Windows_Storage_Streams.IBuffer],  # value
                                           _type.HRESULT]
    get_MaxPrivatePayloadSize: _Callable[[_Pointer[_type.UINT32]],  # value
                                         _type.HRESULT]

    _factory = True


class IXboxLiveQualityOfServiceMetricResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Networking.XboxLive.XboxLiveQualityOfServiceMeasurementStatus]],  # value
                          _type.HRESULT]
    get_DeviceAddress: _Callable[[_Pointer[IXboxLiveDeviceAddress]],  # value
                                 _type.HRESULT]
    get_Metric: _Callable[[_Pointer[_enum.Windows.Networking.XboxLive.XboxLiveQualityOfServiceMetric]],  # value
                          _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.UINT64]],  # value
                         _type.HRESULT]


class IXboxLiveQualityOfServicePrivatePayloadResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Networking.XboxLive.XboxLiveQualityOfServiceMeasurementStatus]],  # value
                          _type.HRESULT]
    get_DeviceAddress: _Callable[[_Pointer[IXboxLiveDeviceAddress]],  # value
                                 _type.HRESULT]
    get_Value: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                         _type.HRESULT]
