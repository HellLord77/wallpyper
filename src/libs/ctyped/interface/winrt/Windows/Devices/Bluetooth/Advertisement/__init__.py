from __future__ import annotations

from typing import Callable as _Callable

from ... import Bluetooth as _Windows_Devices_Bluetooth
from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ....Storage import Streams as _Windows_Storage_Streams
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IBluetoothLEAdvertisement(_inspectable.IInspectable):
    get_Flags: _Callable[[_Pointer[_Windows_Foundation.IReference[_enum.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementFlags]]],  # value
                         _type.HRESULT]
    put_Flags: _Callable[[_Windows_Foundation.IReference[_enum.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementFlags]],  # value
                         _type.HRESULT]
    get_LocalName: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_LocalName: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_ServiceUuids: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_struct.GUID]]],  # value
                                _type.HRESULT]
    get_ManufacturerData: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IBluetoothLEManufacturerData]]],  # value
                                    _type.HRESULT]
    get_DataSections: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IBluetoothLEAdvertisementDataSection]]],  # value
                                _type.HRESULT]
    GetManufacturerDataByCompanyId: _Callable[[_type.UINT16,  # companyId
                                               _Pointer[_Windows_Foundation_Collections.IVectorView[IBluetoothLEManufacturerData]]],  # dataList
                                              _type.HRESULT]
    GetSectionsByType: _Callable[[_type.BYTE,  # type
                                  _Pointer[_Windows_Foundation_Collections.IVectorView[IBluetoothLEAdvertisementDataSection]]],  # sectionList
                                 _type.HRESULT]


class IBluetoothLEAdvertisementBytePattern(_inspectable.IInspectable):
    get_DataType: _Callable[[_Pointer[_type.BYTE]],  # value
                            _type.HRESULT]
    put_DataType: _Callable[[_type.BYTE],  # value
                            _type.HRESULT]
    get_Offset: _Callable[[_Pointer[_type.INT16]],  # value
                          _type.HRESULT]
    put_Offset: _Callable[[_type.INT16],  # value
                          _type.HRESULT]
    get_Data: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                        _type.HRESULT]
    put_Data: _Callable[[_Windows_Storage_Streams.IBuffer],  # value
                        _type.HRESULT]


class IBluetoothLEAdvertisementBytePatternFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.BYTE,  # dataType
                       _type.INT16,  # offset
                       _Windows_Storage_Streams.IBuffer,  # data
                       _Pointer[IBluetoothLEAdvertisementBytePattern]],  # value
                      _type.HRESULT]


class IBluetoothLEAdvertisementDataSection(_inspectable.IInspectable):
    get_DataType: _Callable[[_Pointer[_type.BYTE]],  # value
                            _type.HRESULT]
    put_DataType: _Callable[[_type.BYTE],  # value
                            _type.HRESULT]
    get_Data: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                        _type.HRESULT]
    put_Data: _Callable[[_Windows_Storage_Streams.IBuffer],  # value
                        _type.HRESULT]


class IBluetoothLEAdvertisementDataSectionFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.BYTE,  # dataType
                       _Windows_Storage_Streams.IBuffer,  # data
                       _Pointer[IBluetoothLEAdvertisementDataSection]],  # value
                      _type.HRESULT]


class IBluetoothLEAdvertisementDataTypesStatics(_inspectable.IInspectable, factory=True):
    get_Flags: _Callable[[_Pointer[_type.BYTE]],  # value
                         _type.HRESULT]
    get_IncompleteService16BitUuids: _Callable[[_Pointer[_type.BYTE]],  # value
                                               _type.HRESULT]
    get_CompleteService16BitUuids: _Callable[[_Pointer[_type.BYTE]],  # value
                                             _type.HRESULT]
    get_IncompleteService32BitUuids: _Callable[[_Pointer[_type.BYTE]],  # value
                                               _type.HRESULT]
    get_CompleteService32BitUuids: _Callable[[_Pointer[_type.BYTE]],  # value
                                             _type.HRESULT]
    get_IncompleteService128BitUuids: _Callable[[_Pointer[_type.BYTE]],  # value
                                                _type.HRESULT]
    get_CompleteService128BitUuids: _Callable[[_Pointer[_type.BYTE]],  # value
                                              _type.HRESULT]
    get_ShortenedLocalName: _Callable[[_Pointer[_type.BYTE]],  # value
                                      _type.HRESULT]
    get_CompleteLocalName: _Callable[[_Pointer[_type.BYTE]],  # value
                                     _type.HRESULT]
    get_TxPowerLevel: _Callable[[_Pointer[_type.BYTE]],  # value
                                _type.HRESULT]
    get_PeripheralConnectionIntervalRange: _Callable[[_Pointer[_type.BYTE]],  # value
                                                     _type.HRESULT]
    get_ServiceSolicitation16BitUuids: _Callable[[_Pointer[_type.BYTE]],  # value
                                                 _type.HRESULT]
    get_ServiceSolicitation32BitUuids: _Callable[[_Pointer[_type.BYTE]],  # value
                                                 _type.HRESULT]
    get_ServiceSolicitation128BitUuids: _Callable[[_Pointer[_type.BYTE]],  # value
                                                  _type.HRESULT]
    get_ServiceData16BitUuids: _Callable[[_Pointer[_type.BYTE]],  # value
                                         _type.HRESULT]
    get_ServiceData32BitUuids: _Callable[[_Pointer[_type.BYTE]],  # value
                                         _type.HRESULT]
    get_ServiceData128BitUuids: _Callable[[_Pointer[_type.BYTE]],  # value
                                          _type.HRESULT]
    get_PublicTargetAddress: _Callable[[_Pointer[_type.BYTE]],  # value
                                       _type.HRESULT]
    get_RandomTargetAddress: _Callable[[_Pointer[_type.BYTE]],  # value
                                       _type.HRESULT]
    get_Appearance: _Callable[[_Pointer[_type.BYTE]],  # value
                              _type.HRESULT]
    get_AdvertisingInterval: _Callable[[_Pointer[_type.BYTE]],  # value
                                       _type.HRESULT]
    get_ManufacturerSpecificData: _Callable[[_Pointer[_type.BYTE]],  # value
                                            _type.HRESULT]


class IBluetoothLEAdvertisementFilter(_inspectable.IInspectable):
    get_Advertisement: _Callable[[_Pointer[IBluetoothLEAdvertisement]],  # value
                                 _type.HRESULT]
    put_Advertisement: _Callable[[IBluetoothLEAdvertisement],  # value
                                 _type.HRESULT]
    get_BytePatterns: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IBluetoothLEAdvertisementBytePattern]]],  # value
                                _type.HRESULT]


class IBluetoothLEAdvertisementPublisher(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementPublisherStatus]],  # value
                          _type.HRESULT]
    get_Advertisement: _Callable[[_Pointer[IBluetoothLEAdvertisement]],  # value
                                 _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    add_StatusChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IBluetoothLEAdvertisementPublisher, IBluetoothLEAdvertisementPublisherStatusChangedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_StatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]


class IBluetoothLEAdvertisementPublisher2(_inspectable.IInspectable):
    get_PreferredTransmitPowerLevelInDBm: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT16]]],  # value
                                                    _type.HRESULT]
    put_PreferredTransmitPowerLevelInDBm: _Callable[[_Windows_Foundation.IReference[_type.INT16]],  # value
                                                    _type.HRESULT]
    get_UseExtendedAdvertisement: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_UseExtendedAdvertisement: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]
    get_IsAnonymous: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    put_IsAnonymous: _Callable[[_type.boolean],  # value
                               _type.HRESULT]
    get_IncludeTransmitPowerLevel: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    put_IncludeTransmitPowerLevel: _Callable[[_type.boolean],  # value
                                             _type.HRESULT]


class IBluetoothLEAdvertisementPublisherFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[IBluetoothLEAdvertisement,  # advertisement
                       _Pointer[IBluetoothLEAdvertisementPublisher]],  # value
                      _type.HRESULT]


class IBluetoothLEAdvertisementPublisherStatusChangedEventArgs(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementPublisherStatus]],  # value
                          _type.HRESULT]
    get_Error: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.BluetoothError]],  # value
                         _type.HRESULT]


class IBluetoothLEAdvertisementPublisherStatusChangedEventArgs2(_inspectable.IInspectable):
    get_SelectedTransmitPowerLevelInDBm: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT16]]],  # value
                                                   _type.HRESULT]


class IBluetoothLEAdvertisementReceivedEventArgs(_inspectable.IInspectable):
    get_RawSignalStrengthInDBm: _Callable[[_Pointer[_type.INT16]],  # value
                                          _type.HRESULT]
    get_BluetoothAddress: _Callable[[_Pointer[_type.UINT64]],  # value
                                    _type.HRESULT]
    get_AdvertisementType: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementType]],  # value
                                     _type.HRESULT]
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_Advertisement: _Callable[[_Pointer[IBluetoothLEAdvertisement]],  # value
                                 _type.HRESULT]


class IBluetoothLEAdvertisementReceivedEventArgs2(_inspectable.IInspectable):
    get_BluetoothAddressType: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.BluetoothAddressType]],  # value
                                        _type.HRESULT]
    get_TransmitPowerLevelInDBm: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT16]]],  # value
                                           _type.HRESULT]
    get_IsAnonymous: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_IsConnectable: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_IsScannable: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_IsDirected: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_IsScanResponse: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]


class IBluetoothLEAdvertisementWatcher(_inspectable.IInspectable):
    get_MinSamplingInterval: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                       _type.HRESULT]
    get_MaxSamplingInterval: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                       _type.HRESULT]
    get_MinOutOfRangeTimeout: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                        _type.HRESULT]
    get_MaxOutOfRangeTimeout: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                        _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementWatcherStatus]],  # value
                          _type.HRESULT]
    get_ScanningMode: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.Advertisement.BluetoothLEScanningMode]],  # value
                                _type.HRESULT]
    put_ScanningMode: _Callable[[_enum.Windows.Devices.Bluetooth.Advertisement.BluetoothLEScanningMode],  # value
                                _type.HRESULT]
    get_SignalStrengthFilter: _Callable[[_Pointer[_Windows_Devices_Bluetooth.IBluetoothSignalStrengthFilter]],  # value
                                        _type.HRESULT]
    put_SignalStrengthFilter: _Callable[[_Windows_Devices_Bluetooth.IBluetoothSignalStrengthFilter],  # value
                                        _type.HRESULT]
    get_AdvertisementFilter: _Callable[[_Pointer[IBluetoothLEAdvertisementFilter]],  # value
                                       _type.HRESULT]
    put_AdvertisementFilter: _Callable[[IBluetoothLEAdvertisementFilter],  # value
                                       _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    add_Received: _Callable[[_Windows_Foundation.ITypedEventHandler[IBluetoothLEAdvertisementWatcher, IBluetoothLEAdvertisementReceivedEventArgs],  # handler
                             _Pointer[_struct.EventRegistrationToken]],  # token
                            _type.HRESULT]
    remove_Received: _Callable[[_struct.EventRegistrationToken],  # token
                               _type.HRESULT]
    add_Stopped: _Callable[[_Windows_Foundation.ITypedEventHandler[IBluetoothLEAdvertisementWatcher, IBluetoothLEAdvertisementWatcherStoppedEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Stopped: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]


class IBluetoothLEAdvertisementWatcher2(_inspectable.IInspectable):
    get_AllowExtendedAdvertisements: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]
    put_AllowExtendedAdvertisements: _Callable[[_type.boolean],  # value
                                               _type.HRESULT]


class IBluetoothLEAdvertisementWatcherFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[IBluetoothLEAdvertisementFilter,  # advertisementFilter
                       _Pointer[IBluetoothLEAdvertisementWatcher]],  # value
                      _type.HRESULT]


class IBluetoothLEAdvertisementWatcherStoppedEventArgs(_inspectable.IInspectable):
    get_Error: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.BluetoothError]],  # value
                         _type.HRESULT]


class IBluetoothLEManufacturerData(_inspectable.IInspectable):
    get_CompanyId: _Callable[[_Pointer[_type.UINT16]],  # value
                             _type.HRESULT]
    put_CompanyId: _Callable[[_type.UINT16],  # value
                             _type.HRESULT]
    get_Data: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                        _type.HRESULT]
    put_Data: _Callable[[_Windows_Storage_Streams.IBuffer],  # value
                        _type.HRESULT]


class IBluetoothLEManufacturerDataFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.UINT16,  # companyId
                       _Windows_Storage_Streams.IBuffer,  # data
                       _Pointer[IBluetoothLEManufacturerData]],  # value
                      _type.HRESULT]
