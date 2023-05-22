from __future__ import annotations

from typing import Callable as _Callable

from .. import Advertisement as _Windows_Devices_Bluetooth_Advertisement
from .. import GenericAttributeProfile as _Windows_Devices_Bluetooth_GenericAttributeProfile
from .. import Rfcomm as _Windows_Devices_Bluetooth_Rfcomm
from ... import Bluetooth as _Windows_Devices_Bluetooth
from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ....Networking import Sockets as _Windows_Networking_Sockets
from ....Storage import Streams as _Windows_Storage_Streams
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import type as _type
from ......._utils import _Pointer


class IBluetoothLEAdvertisementPublisherTriggerDetails(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementPublisherStatus]],  # value
                          _type.HRESULT]
    get_Error: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.BluetoothError]],  # value
                         _type.HRESULT]


class IBluetoothLEAdvertisementPublisherTriggerDetails2(_inspectable.IInspectable):
    get_SelectedTransmitPowerLevelInDBm: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT16]]],  # value
                                                   _type.HRESULT]


class IBluetoothLEAdvertisementWatcherTriggerDetails(_inspectable.IInspectable):
    get_Error: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.BluetoothError]],  # value
                         _type.HRESULT]
    get_Advertisements: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Devices_Bluetooth_Advertisement.IBluetoothLEAdvertisementReceivedEventArgs]]],  # value
                                  _type.HRESULT]
    get_SignalStrengthFilter: _Callable[[_Pointer[_Windows_Devices_Bluetooth.IBluetoothSignalStrengthFilter]],  # value
                                        _type.HRESULT]


class IGattCharacteristicNotificationTriggerDetails(_inspectable.IInspectable):
    get_Characteristic: _Callable[[_Pointer[_Windows_Devices_Bluetooth_GenericAttributeProfile.IGattCharacteristic]],  # value
                                  _type.HRESULT]
    get_Value: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                         _type.HRESULT]


class IGattCharacteristicNotificationTriggerDetails2(_inspectable.IInspectable):
    get_Error: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.BluetoothError]],  # value
                         _type.HRESULT]
    get_EventTriggeringMode: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.Background.BluetoothEventTriggeringMode]],  # value
                                       _type.HRESULT]
    get_ValueChangedEvents: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Devices_Bluetooth_GenericAttributeProfile.IGattValueChangedEventArgs]]],  # value
                                      _type.HRESULT]


class IGattServiceProviderConnection(_inspectable.IInspectable):
    get_TriggerId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_Service: _Callable[[_Pointer[_Windows_Devices_Bluetooth_GenericAttributeProfile.IGattLocalService]],  # value
                           _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]


class IGattServiceProviderConnectionStatics(_inspectable.IInspectable, factory=True):
    get_AllServices: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, IGattServiceProviderConnection]]],  # value
                               _type.HRESULT]


class IGattServiceProviderTriggerDetails(_inspectable.IInspectable):
    get_Connection: _Callable[[_Pointer[IGattServiceProviderConnection]],  # value
                              _type.HRESULT]


class IRfcommConnectionTriggerDetails(_inspectable.IInspectable):
    get_Socket: _Callable[[_Pointer[_Windows_Networking_Sockets.IStreamSocket]],  # value
                          _type.HRESULT]
    get_Incoming: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_RemoteDevice: _Callable[[_Pointer[_Windows_Devices_Bluetooth.IBluetoothDevice]],  # value
                                _type.HRESULT]


class IRfcommInboundConnectionInformation(_inspectable.IInspectable):
    get_SdpRecord: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                             _type.HRESULT]
    put_SdpRecord: _Callable[[_Windows_Storage_Streams.IBuffer],  # value
                             _type.HRESULT]
    get_LocalServiceId: _Callable[[_Pointer[_Windows_Devices_Bluetooth_Rfcomm.IRfcommServiceId]],  # value
                                  _type.HRESULT]
    put_LocalServiceId: _Callable[[_Windows_Devices_Bluetooth_Rfcomm.IRfcommServiceId],  # value
                                  _type.HRESULT]
    get_ServiceCapabilities: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.BluetoothServiceCapabilities]],  # value
                                       _type.HRESULT]
    put_ServiceCapabilities: _Callable[[_enum.Windows.Devices.Bluetooth.BluetoothServiceCapabilities],  # value
                                       _type.HRESULT]


class IRfcommOutboundConnectionInformation(_inspectable.IInspectable):
    get_RemoteServiceId: _Callable[[_Pointer[_Windows_Devices_Bluetooth_Rfcomm.IRfcommServiceId]],  # value
                                   _type.HRESULT]
    put_RemoteServiceId: _Callable[[_Windows_Devices_Bluetooth_Rfcomm.IRfcommServiceId],  # value
                                   _type.HRESULT]
