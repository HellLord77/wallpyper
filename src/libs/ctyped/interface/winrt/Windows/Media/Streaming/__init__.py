from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import Storage as _Windows_Storage
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from .....um import Unknwnbase as _Unknwnbase
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class _IConnectionStatusHandler:
    Invoke: _Callable[[IBasicDevice,  # sender
                       _enum.Windows.Media.Streaming.ConnectionStatus],  # arg
                      _type.HRESULT]


class IConnectionStatusHandler(_IConnectionStatusHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IConnectionStatusHandler_impl(_IConnectionStatusHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IDeviceControllerFinderHandler:
    Invoke: _Callable[[IDeviceController,  # sender
                       _type.HSTRING,  # uniqueDeviceName
                       IBasicDevice],  # device
                      _type.HRESULT]


class IDeviceControllerFinderHandler(_IDeviceControllerFinderHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IDeviceControllerFinderHandler_impl(_IDeviceControllerFinderHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IRenderingParametersUpdateHandler:
    Invoke: _Callable[[IMediaRenderer,  # sender
                       _struct.Windows.Media.Streaming.RenderingParameters],  # arg
                      _type.HRESULT]


class IRenderingParametersUpdateHandler(_IRenderingParametersUpdateHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IRenderingParametersUpdateHandler_impl(_IRenderingParametersUpdateHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ITransportParametersUpdateHandler:
    Invoke: _Callable[[IMediaRenderer,  # sender
                       ITransportParameters],  # arg
                      _type.HRESULT]


class ITransportParametersUpdateHandler(_ITransportParametersUpdateHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ITransportParametersUpdateHandler_impl(_ITransportParametersUpdateHandler, _Unknwnbase.IUnknown_impl):
    pass


class IActiveBasicDevice(_inspectable.IInspectable):
    get_MaxVolume: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    get_IsMuteSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_IsSetNextSourceSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    get_IsAudioSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_IsVideoSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_IsImageSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_IsSearchSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    GetCachedSinkProtocolInfo: _Callable[[_Pointer[_type.HSTRING]],  # value
                                         _type.HRESULT]
    SetCachedSinkProtocolInfo: _Callable[[_type.HSTRING],  # value
                                         _type.HRESULT]
    GetCachedExtraSinkProtocolInfo: _Callable[[_Pointer[_type.HSTRING]],  # value
                                              _type.HRESULT]
    GetEffectiveBandwidth: _Callable[[_type.boolean,  # transmitSpeed
                                      _Pointer[_type.UINT64]],  # currentSpeed
                                     _type.HRESULT]
    GetCachedBitrateMeasurement: _Callable[[_struct.GUID,  # physicalNetworkInterface
                                            _Pointer[_type.UINT64]],  # bitrate
                                           _type.HRESULT]
    SetCachedBitrateMeasurement: _Callable[[_struct.GUID,  # physicalNetworkInterface
                                            _type.UINT64],  # bitrate
                                           _type.HRESULT]
    get_LogicalNetworkInterface: _Callable[[_Pointer[_struct.GUID]],  # logicalNetworkInterface
                                           _type.HRESULT]
    get_PhysicalNetworkInterface: _Callable[[_Pointer[_struct.GUID]],  # physicalNetworkInterface
                                            _type.HRESULT]
    NotifyStreamingStatus: _Callable[[_type.boolean],  # fIsStreaming
                                     _type.HRESULT]


class IActiveBasicDeviceStatics(_inspectable.IInspectable):
    CreateBasicDeviceAsync: _Callable[[_type.HSTRING,  # deviceIdentifier
                                       _enum.Windows.Media.Streaming.DeviceTypes,  # type
                                       _Pointer[_Windows_Foundation.IAsyncOperation[IActiveBasicDevice]]],  # value
                                      _type.HRESULT]
    CloneBasicDeviceAsync: _Callable[[IBasicDevice,  # basicDevice
                                      _Pointer[_Windows_Foundation.IAsyncOperation[IActiveBasicDevice]]],  # value
                                     _type.HRESULT]
    GetDevicesOnMatchingNetworkAsync: _Callable[[IActiveBasicDevice,  # server
                                                 IActiveBasicDevice,  # renderer
                                                 _type.boolean,  # optimizeForProxying
                                                 _type.boolean,  # allowChangeRendererNetwork
                                                 _Pointer[_Windows_Foundation.IAsyncOperation[IDevicePair]]],  # operation
                                                _type.HRESULT]
    CreateDevicesOnMatchingNetworkAsync: _Callable[[_type.HSTRING,  # serverUDN
                                                    IActiveBasicDevice,  # renderer
                                                    _type.boolean,  # optimizeForProxying
                                                    _type.boolean,  # allowChangeRendererNetwork
                                                    _Pointer[_Windows_Foundation.IAsyncOperation[IDevicePair]]],  # operation
                                                   _type.HRESULT]

    _factory = True


class IBasicDevice(_inspectable.IInspectable):
    get_FriendlyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    put_FriendlyName: _Callable[[_type.HSTRING],  # value
                                _type.HRESULT]
    get_ManufacturerName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_ManufacturerUrl: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_UniqueDeviceName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_ModelName: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_ModelNumber: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_ModelUrl: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_SerialNumber: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_PresentationUrl: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_RemoteStreamingUrls: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                       _type.HRESULT]
    get_PhysicalAddresses: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                     _type.HRESULT]
    get_IpAddresses: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                               _type.HRESULT]
    get_CanWakeDevices: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    get_DiscoveredOnCurrentNetwork: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]
    get_Type: _Callable[[_Pointer[_enum.Windows.Media.Streaming.DeviceTypes]],  # value
                        _type.HRESULT]
    get_Icons: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IDeviceIcon]]],  # value
                         _type.HRESULT]
    get_ConnectionStatus: _Callable[[_Pointer[_enum.Windows.Media.Streaming.ConnectionStatus]],  # value
                                    _type.HRESULT]
    add_ConnectionStatusChanged: _Callable[[IConnectionStatusHandler,  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_ConnectionStatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]


class IDeviceController(_inspectable.IInspectable):
    get_CachedDevices: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IBasicDevice]]],  # value
                                 _type.HRESULT]
    AddDevice: _Callable[[_type.HSTRING],  # uniqueDeviceName
                         _type.HRESULT]
    RemoveDevice: _Callable[[IBasicDevice],  # device
                            _type.HRESULT]
    add_DeviceArrival: _Callable[[IDeviceControllerFinderHandler,  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_DeviceArrival: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_DeviceDeparture: _Callable[[IDeviceControllerFinderHandler,  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_DeviceDeparture: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]


class IDeviceIcon(_inspectable.IInspectable):
    get_Width: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    get_Height: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    get_ContentType: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Stream: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamWithContentType]],  # value
                          _type.HRESULT]


class IDevicePair(_inspectable.IInspectable):
    get_Server: _Callable[[_Pointer[IActiveBasicDevice]],  # value
                          _type.HRESULT]
    get_Renderer: _Callable[[_Pointer[IActiveBasicDevice]],  # value
                            _type.HRESULT]


class IMediaRenderer(_inspectable.IInspectable):
    get_IsAudioSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_IsVideoSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_IsImageSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_ActionInformation: _Callable[[_Pointer[IMediaRendererActionInformation]],  # value
                                     _type.HRESULT]
    SetSourceFromUriAsync: _Callable[[_type.HSTRING,  # URI
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_type.UINT32]]],  # value
                                     _type.HRESULT]
    SetSourceFromStreamAsync: _Callable[[_inspectable.IInspectable,  # stream
                                         _Pointer[_Windows_Foundation.IAsyncOperation[_type.UINT32]]],  # value
                                        _type.HRESULT]
    SetSourceFromMediaSourceAsync: _Callable[[_inspectable.IInspectable,  # mediaSource
                                              _Pointer[_Windows_Foundation.IAsyncOperation[_type.UINT32]]],  # value
                                             _type.HRESULT]
    SetNextSourceFromUriAsync: _Callable[[_type.HSTRING,  # URI
                                          _Pointer[_Windows_Foundation.IAsyncOperation[_type.UINT32]]],  # value
                                         _type.HRESULT]
    SetNextSourceFromStreamAsync: _Callable[[_inspectable.IInspectable,  # stream
                                             _Pointer[_Windows_Foundation.IAsyncOperation[_type.UINT32]]],  # value
                                            _type.HRESULT]
    SetNextSourceFromMediaSourceAsync: _Callable[[_inspectable.IInspectable,  # mediaSource
                                                  _Pointer[_Windows_Foundation.IAsyncOperation[_type.UINT32]]],  # value
                                                 _type.HRESULT]
    PlayAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # value
                         _type.HRESULT]
    PlayAtSpeedAsync: _Callable[[_struct.Windows.Media.Streaming.PlaySpeed,  # playSpeed
                                 _Pointer[_Windows_Foundation.IAsyncAction]],  # value
                                _type.HRESULT]
    StopAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # value
                         _type.HRESULT]
    PauseAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # value
                          _type.HRESULT]
    GetMuteAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # value
                            _type.HRESULT]
    SetMuteAsync: _Callable[[_type.boolean,  # mute
                             _Pointer[_Windows_Foundation.IAsyncAction]],  # value
                            _type.HRESULT]
    GetVolumeAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.UINT32]]],  # value
                              _type.HRESULT]
    SetVolumeAsync: _Callable[[_type.UINT32,  # volume
                               _Pointer[_Windows_Foundation.IAsyncAction]],  # value
                              _type.HRESULT]
    SeekAsync: _Callable[[_struct.Windows.Foundation.TimeSpan,  # target
                          _Pointer[_Windows_Foundation.IAsyncAction]],  # value
                         _type.HRESULT]
    GetTransportInformationAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_struct.Windows.Media.Streaming.TransportInformation]]],  # value
                                            _type.HRESULT]
    GetPositionInformationAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_struct.Windows.Media.Streaming.PositionInformation]]],  # value
                                           _type.HRESULT]
    add_TransportParametersUpdate: _Callable[[ITransportParametersUpdateHandler,  # handler
                                              _Pointer[_struct.EventRegistrationToken]],  # token
                                             _type.HRESULT]
    remove_TransportParametersUpdate: _Callable[[_struct.EventRegistrationToken],  # token
                                                _type.HRESULT]
    add_RenderingParametersUpdate: _Callable[[IRenderingParametersUpdateHandler,  # handler
                                              _Pointer[_struct.EventRegistrationToken]],  # token
                                             _type.HRESULT]
    remove_RenderingParametersUpdate: _Callable[[_struct.EventRegistrationToken],  # token
                                                _type.HRESULT]
    NextAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # value
                         _type.HRESULT]


class IMediaRendererActionInformation(_inspectable.IInspectable):
    get_IsMuteAvailable: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_IsPauseAvailable: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_IsPlayAvailable: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_IsSeekAvailable: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_IsSetNextSourceAvailable: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    get_IsStopAvailable: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_IsVolumeAvailable: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    get_PlaySpeeds: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_struct.Windows.Media.Streaming.PlaySpeed]]],  # value
                              _type.HRESULT]


class IMediaRendererFactory(_inspectable.IInspectable):
    CreateMediaRendererAsync: _Callable[[_type.HSTRING,  # deviceIdentifier
                                         _Pointer[_Windows_Foundation.IAsyncOperation[IMediaRenderer]]],  # value
                                        _type.HRESULT]
    CreateMediaRendererFromBasicDeviceAsync: _Callable[[IBasicDevice,  # basicDevice
                                                        _Pointer[_Windows_Foundation.IAsyncOperation[IMediaRenderer]]],  # value
                                                       _type.HRESULT]

    _factory = True


class IStreamSelectorStatics(_inspectable.IInspectable):
    SelectBestStreamAsync: _Callable[[_Windows_Storage.IStorageFile,  # storageFile
                                      _Windows_Foundation_Collections.IPropertySet,  # selectorProperties
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStreamWithContentType]]],  # value
                                     _type.HRESULT]
    GetStreamPropertiesAsync: _Callable[[_Windows_Storage.IStorageFile,  # storageFile
                                         _Windows_Foundation_Collections.IPropertySet,  # selectorProperties
                                         _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_Foundation_Collections.IPropertySet]]]],  # value
                                        _type.HRESULT]
    SelectBestStreamFromStreamAsync: _Callable[[_Windows_Storage_Streams.IRandomAccessStream,  # stream
                                                _Windows_Foundation_Collections.IPropertySet,  # selectorProperties
                                                _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStreamWithContentType]]],  # value
                                               _type.HRESULT]
    GetStreamPropertiesFromStreamAsync: _Callable[[_Windows_Storage_Streams.IRandomAccessStream,  # stream
                                                   _Windows_Foundation_Collections.IPropertySet,  # selectorProperties
                                                   _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_Foundation_Collections.IPropertySet]]]],  # value
                                                  _type.HRESULT]

    _factory = True


class ITransportParameters(_inspectable.IInspectable):
    get_ActionInformation: _Callable[[_Pointer[IMediaRendererActionInformation]],  # value
                                     _type.HRESULT]
    get_TrackInformation: _Callable[[_Pointer[_struct.Windows.Media.Streaming.TrackInformation]],  # value
                                    _type.HRESULT]
    get_TransportInformation: _Callable[[_Pointer[_struct.Windows.Media.Streaming.TransportInformation]],  # value
                                        _type.HRESULT]
