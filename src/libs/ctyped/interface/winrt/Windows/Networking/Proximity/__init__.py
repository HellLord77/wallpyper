from __future__ import annotations

from typing import Callable as _Callable

from .. import Sockets as _Windows_Networking_Sockets
from ... import Foundation as _Windows_Foundation
from ... import Networking as _Windows_Networking
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from .....um import Unknwnbase as _Unknwnbase
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class _IDeviceArrivedEventHandler:
    Invoke: _Callable[[IProximityDevice],  # sender
                      _type.HRESULT]


class IDeviceArrivedEventHandler(_IDeviceArrivedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IDeviceArrivedEventHandler_impl(_IDeviceArrivedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IDeviceDepartedEventHandler:
    Invoke: _Callable[[IProximityDevice],  # sender
                      _type.HRESULT]


class IDeviceDepartedEventHandler(_IDeviceDepartedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IDeviceDepartedEventHandler_impl(_IDeviceDepartedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IMessageReceivedHandler:
    Invoke: _Callable[[IProximityDevice,  # sender
                       IProximityMessage],  # message
                      _type.HRESULT]


class IMessageReceivedHandler(_IMessageReceivedHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IMessageReceivedHandler_impl(_IMessageReceivedHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IMessageTransmittedHandler:
    Invoke: _Callable[[IProximityDevice,  # sender
                       _type.INT64],  # messageId
                      _type.HRESULT]


class IMessageTransmittedHandler(_IMessageTransmittedHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IMessageTransmittedHandler_impl(_IMessageTransmittedHandler, _Unknwnbase.IUnknown_impl):
    pass


class IConnectionRequestedEventArgs(_inspectable.IInspectable):
    get_PeerInformation: _Callable[[_Pointer[IPeerInformation]],  # value
                                   _type.HRESULT]


class IPeerFinderStatics(_inspectable.IInspectable):
    get_AllowBluetooth: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    put_AllowBluetooth: _Callable[[_type.boolean],  # value
                                  _type.HRESULT]
    get_AllowInfrastructure: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_AllowInfrastructure: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_AllowWiFiDirect: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    put_AllowWiFiDirect: _Callable[[_type.boolean],  # value
                                   _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_DisplayName: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_SupportedDiscoveryTypes: _Callable[[_Pointer[_enum.Windows.Networking.Proximity.PeerDiscoveryTypes]],  # value
                                           _type.HRESULT]
    get_AlternateIdentities: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, _type.HSTRING]]],  # value
                                       _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    StartWithMessage: _Callable[[_type.HSTRING],  # peerMessage
                                _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    add_TriggeredConnectionStateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[_inspectable.IInspectable, ITriggeredConnectionStateChangedEventArgs],  # handler
                                                    _Pointer[_struct.EventRegistrationToken]],  # cookie
                                                   _type.HRESULT]
    remove_TriggeredConnectionStateChanged: _Callable[[_struct.EventRegistrationToken],  # cookie
                                                      _type.HRESULT]
    add_ConnectionRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[_inspectable.IInspectable, IConnectionRequestedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # cookie
                                       _type.HRESULT]
    remove_ConnectionRequested: _Callable[[_struct.EventRegistrationToken],  # cookie
                                          _type.HRESULT]
    FindAllPeersAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IPeerInformation]]]],  # asyncOp
                                 _type.HRESULT]
    ConnectAsync: _Callable[[IPeerInformation,  # peerInformation
                             _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Networking_Sockets.IStreamSocket]]],  # asyncOp
                            _type.HRESULT]

    _factory = True


class IPeerFinderStatics2(_inspectable.IInspectable):
    get_Role: _Callable[[_Pointer[_enum.Windows.Networking.Proximity.PeerRole]],  # value
                        _type.HRESULT]
    put_Role: _Callable[[_enum.Windows.Networking.Proximity.PeerRole],  # value
                        _type.HRESULT]
    get_DiscoveryData: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                 _type.HRESULT]
    put_DiscoveryData: _Callable[[_Windows_Storage_Streams.IBuffer],  # value
                                 _type.HRESULT]
    CreateWatcher: _Callable[[_Pointer[IPeerWatcher]],  # watcher
                             _type.HRESULT]

    _factory = True


class IPeerInformation(_inspectable.IInspectable):
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class IPeerInformation3(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_DiscoveryData: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                 _type.HRESULT]


class IPeerInformationWithHostAndService(_inspectable.IInspectable):
    get_HostName: _Callable[[_Pointer[_Windows_Networking.IHostName]],  # value
                            _type.HRESULT]
    get_ServiceName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class IPeerWatcher(_inspectable.IInspectable):
    add_Added: _Callable[[_Windows_Foundation.ITypedEventHandler[IPeerWatcher, IPeerInformation],  # handler
                          _Pointer[_struct.EventRegistrationToken]],  # token
                         _type.HRESULT]
    remove_Added: _Callable[[_struct.EventRegistrationToken],  # token
                            _type.HRESULT]
    add_Removed: _Callable[[_Windows_Foundation.ITypedEventHandler[IPeerWatcher, IPeerInformation],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Removed: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_Updated: _Callable[[_Windows_Foundation.ITypedEventHandler[IPeerWatcher, IPeerInformation],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Updated: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_EnumerationCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IPeerWatcher, _inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_EnumerationCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    add_Stopped: _Callable[[_Windows_Foundation.ITypedEventHandler[IPeerWatcher, _inspectable.IInspectable],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Stopped: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.Networking.Proximity.PeerWatcherStatus]],  # status
                          _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]


class IProximityDevice(_inspectable.IInspectable):
    SubscribeForMessage: _Callable[[_type.HSTRING,  # messageType
                                    IMessageReceivedHandler,  # messageReceivedHandler
                                    _Pointer[_type.INT64]],  # subscriptionId
                                   _type.HRESULT]
    PublishMessage: _Callable[[_type.HSTRING,  # messageType
                               _type.HSTRING,  # message
                               _Pointer[_type.INT64]],  # messageId
                              _type.HRESULT]
    PublishMessageWithCallback: _Callable[[_type.HSTRING,  # messageType
                                           _type.HSTRING,  # message
                                           IMessageTransmittedHandler,  # messageTransmittedHandler
                                           _Pointer[_type.INT64]],  # messageId
                                          _type.HRESULT]
    PublishBinaryMessage: _Callable[[_type.HSTRING,  # messageType
                                     _Windows_Storage_Streams.IBuffer,  # message
                                     _Pointer[_type.INT64]],  # messageId
                                    _type.HRESULT]
    PublishBinaryMessageWithCallback: _Callable[[_type.HSTRING,  # messageType
                                                 _Windows_Storage_Streams.IBuffer,  # message
                                                 IMessageTransmittedHandler,  # messageTransmittedHandler
                                                 _Pointer[_type.INT64]],  # messageId
                                                _type.HRESULT]
    PublishUriMessage: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # message
                                  _Pointer[_type.INT64]],  # messageId
                                 _type.HRESULT]
    PublishUriMessageWithCallback: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # message
                                              IMessageTransmittedHandler,  # messageTransmittedHandler
                                              _Pointer[_type.INT64]],  # messageId
                                             _type.HRESULT]
    StopSubscribingForMessage: _Callable[[_type.INT64],  # subscriptionId
                                         _type.HRESULT]
    StopPublishingMessage: _Callable[[_type.INT64],  # messageId
                                     _type.HRESULT]
    add_DeviceArrived: _Callable[[IDeviceArrivedEventHandler,  # arrivedHandler
                                  _Pointer[_struct.EventRegistrationToken]],  # cookie
                                 _type.HRESULT]
    remove_DeviceArrived: _Callable[[_struct.EventRegistrationToken],  # cookie
                                    _type.HRESULT]
    add_DeviceDeparted: _Callable[[IDeviceDepartedEventHandler,  # departedHandler
                                   _Pointer[_struct.EventRegistrationToken]],  # cookie
                                  _type.HRESULT]
    remove_DeviceDeparted: _Callable[[_struct.EventRegistrationToken],  # cookie
                                     _type.HRESULT]
    get_MaxMessageBytes: _Callable[[_Pointer[_type.UINT32]],  # value
                                   _type.HRESULT]
    get_BitsPerSecond: _Callable[[_Pointer[_type.UINT64]],  # value
                                 _type.HRESULT]
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]


class IProximityDeviceStatics(_inspectable.IInspectable):
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # selector
                                 _type.HRESULT]
    GetDefault: _Callable[[_Pointer[IProximityDevice]],  # proximityDevice
                          _type.HRESULT]
    FromId: _Callable[[_type.HSTRING,  # deviceId
                       _Pointer[IProximityDevice]],  # proximityDevice
                      _type.HRESULT]

    _factory = True


class IProximityMessage(_inspectable.IInspectable):
    get_MessageType: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_SubscriptionId: _Callable[[_Pointer[_type.INT64]],  # value
                                  _type.HRESULT]
    get_Data: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                        _type.HRESULT]
    get_DataAsString: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]


class ITriggeredConnectionStateChangedEventArgs(_inspectable.IInspectable):
    get_State: _Callable[[_Pointer[_enum.Windows.Networking.Proximity.TriggeredConnectState]],  # value
                         _type.HRESULT]
    get_Id: _Callable[[_Pointer[_type.UINT32]],  # value
                      _type.HRESULT]
    get_Socket: _Callable[[_Pointer[_Windows_Networking_Sockets.IStreamSocket]],  # value
                          _type.HRESULT]
