from __future__ import annotations

from typing import Callable as _Callable

from . import GenericAttributeProfile as _Windows_Devices_Bluetooth_GenericAttributeProfile
from . import Rfcomm as _Windows_Devices_Bluetooth_Rfcomm
from .. import Enumeration as _Windows_Devices_Enumeration
from .. import Radios as _Windows_Devices_Radios
from ... import Foundation as _Windows_Foundation
from ... import Networking as _Windows_Networking
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IBluetoothAdapter(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_BluetoothAddress: _Callable[[_Pointer[_type.UINT64]],  # value
                                    _type.HRESULT]
    get_IsClassicSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    get_IsLowEnergySupported: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_IsPeripheralRoleSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    get_IsCentralRoleSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    get_IsAdvertisementOffloadSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                   _type.HRESULT]
    GetRadioAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Devices_Radios.IRadio]]],  # operation
                             _type.HRESULT]


class IBluetoothAdapter2(_inspectable.IInspectable):
    get_AreClassicSecureConnectionsSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                        _type.HRESULT]
    get_AreLowEnergySecureConnectionsSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                          _type.HRESULT]


class IBluetoothAdapter3(_inspectable.IInspectable):
    get_IsExtendedAdvertisingSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                  _type.HRESULT]
    get_MaxAdvertisementDataLength: _Callable[[_Pointer[_type.UINT32]],  # value
                                              _type.HRESULT]


class IBluetoothAdapterStatics(_inspectable.IInspectable):
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IBluetoothAdapter]]],  # operation
                           _type.HRESULT]
    GetDefaultAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IBluetoothAdapter]]],  # operation
                               _type.HRESULT]

    _factory = True


class IBluetoothClassOfDevice(_inspectable.IInspectable):
    get_RawValue: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    get_MajorClass: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.BluetoothMajorClass]],  # value
                              _type.HRESULT]
    get_MinorClass: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.BluetoothMinorClass]],  # value
                              _type.HRESULT]
    get_ServiceCapabilities: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.BluetoothServiceCapabilities]],  # value
                                       _type.HRESULT]


class IBluetoothClassOfDeviceStatics(_inspectable.IInspectable):
    FromRawValue: _Callable[[_type.UINT32,  # rawValue
                             _Pointer[IBluetoothClassOfDevice]],  # classOfDevice
                            _type.HRESULT]
    FromParts: _Callable[[_enum.Windows.Devices.Bluetooth.BluetoothMajorClass,  # majorClass
                          _enum.Windows.Devices.Bluetooth.BluetoothMinorClass,  # minorClass
                          _enum.Windows.Devices.Bluetooth.BluetoothServiceCapabilities,  # serviceCapabilities
                          _Pointer[IBluetoothClassOfDevice]],  # classOfDevice
                         _type.HRESULT]

    _factory = True


class IBluetoothDevice(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_HostName: _Callable[[_Pointer[_Windows_Networking.IHostName]],  # value
                            _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_ClassOfDevice: _Callable[[_Pointer[IBluetoothClassOfDevice]],  # value
                                 _type.HRESULT]
    get_SdpRecords: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Storage_Streams.IBuffer]]],  # value
                              _type.HRESULT]
    RfcommServices: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Devices_Bluetooth_Rfcomm.IRfcommDeviceService]]],  # value
                              _type.HRESULT]
    get_ConnectionStatus: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.BluetoothConnectionStatus]],  # value
                                    _type.HRESULT]
    get_BluetoothAddress: _Callable[[_Pointer[_type.UINT64]],  # value
                                    _type.HRESULT]
    add_NameChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IBluetoothDevice, _inspectable.IInspectable],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_NameChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    add_SdpRecordsChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IBluetoothDevice, _inspectable.IInspectable],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_SdpRecordsChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    add_ConnectionStatusChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IBluetoothDevice, _inspectable.IInspectable],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_ConnectionStatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]


class IBluetoothDevice2(_inspectable.IInspectable):
    get_DeviceInformation: _Callable[[_Pointer[_Windows_Devices_Enumeration.IDeviceInformation]],  # value
                                     _type.HRESULT]


class IBluetoothDevice3(_inspectable.IInspectable):
    get_DeviceAccessInformation: _Callable[[_Pointer[_Windows_Devices_Enumeration.IDeviceAccessInformation]],  # value
                                           _type.HRESULT]
    RequestAccessAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Devices.Enumeration.DeviceAccessStatus]]],  # value
                                  _type.HRESULT]
    GetRfcommServicesAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Devices_Bluetooth_Rfcomm.IRfcommDeviceServicesResult]]],  # operation
                                      _type.HRESULT]
    GetRfcommServicesWithCacheModeAsync: _Callable[[_enum.Windows.Devices.Bluetooth.BluetoothCacheMode,  # cacheMode
                                                    _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Devices_Bluetooth_Rfcomm.IRfcommDeviceServicesResult]]],  # operation
                                                   _type.HRESULT]
    GetRfcommServicesForIdAsync: _Callable[[_Windows_Devices_Bluetooth_Rfcomm.IRfcommServiceId,  # serviceId
                                            _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Devices_Bluetooth_Rfcomm.IRfcommDeviceServicesResult]]],  # operation
                                           _type.HRESULT]
    GetRfcommServicesForIdWithCacheModeAsync: _Callable[[_Windows_Devices_Bluetooth_Rfcomm.IRfcommServiceId,  # serviceId
                                                         _enum.Windows.Devices.Bluetooth.BluetoothCacheMode,  # cacheMode
                                                         _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Devices_Bluetooth_Rfcomm.IRfcommDeviceServicesResult]]],  # operation
                                                        _type.HRESULT]


class IBluetoothDevice4(_inspectable.IInspectable):
    get_BluetoothDeviceId: _Callable[[_Pointer[IBluetoothDeviceId]],  # value
                                     _type.HRESULT]


class IBluetoothDevice5(_inspectable.IInspectable):
    get_WasSecureConnectionUsedForPairing: _Callable[[_Pointer[_type.boolean]],  # value
                                                     _type.HRESULT]


class IBluetoothDeviceId(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_IsClassicDevice: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_IsLowEnergyDevice: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]


class IBluetoothDeviceIdStatics(_inspectable.IInspectable):
    FromId: _Callable[[_type.HSTRING,  # deviceId
                       _Pointer[IBluetoothDeviceId]],  # result
                      _type.HRESULT]

    _factory = True


class IBluetoothDeviceStatics(_inspectable.IInspectable):
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IBluetoothDevice]]],  # operation
                           _type.HRESULT]
    FromHostNameAsync: _Callable[[_Windows_Networking.IHostName,  # hostName
                                  _Pointer[_Windows_Foundation.IAsyncOperation[IBluetoothDevice]]],  # operation
                                 _type.HRESULT]
    FromBluetoothAddressAsync: _Callable[[_type.UINT64,  # address
                                          _Pointer[_Windows_Foundation.IAsyncOperation[IBluetoothDevice]]],  # operation
                                         _type.HRESULT]
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # deviceSelector
                                 _type.HRESULT]

    _factory = True


class IBluetoothDeviceStatics2(_inspectable.IInspectable):
    GetDeviceSelectorFromPairingState: _Callable[[_type.boolean,  # pairingState
                                                  _Pointer[_type.HSTRING]],  # deviceSelector
                                                 _type.HRESULT]
    GetDeviceSelectorFromConnectionStatus: _Callable[[_enum.Windows.Devices.Bluetooth.BluetoothConnectionStatus,  # connectionStatus
                                                      _Pointer[_type.HSTRING]],  # deviceSelector
                                                     _type.HRESULT]
    GetDeviceSelectorFromDeviceName: _Callable[[_type.HSTRING,  # deviceName
                                                _Pointer[_type.HSTRING]],  # deviceSelector
                                               _type.HRESULT]
    GetDeviceSelectorFromBluetoothAddress: _Callable[[_type.UINT64,  # bluetoothAddress
                                                      _Pointer[_type.HSTRING]],  # deviceSelector
                                                     _type.HRESULT]
    GetDeviceSelectorFromClassOfDevice: _Callable[[IBluetoothClassOfDevice,  # classOfDevice
                                                   _Pointer[_type.HSTRING]],  # deviceSelector
                                                  _type.HRESULT]

    _factory = True


class IBluetoothLEAppearance(_inspectable.IInspectable):
    get_RawValue: _Callable[[_Pointer[_type.UINT16]],  # value
                            _type.HRESULT]
    get_Category: _Callable[[_Pointer[_type.UINT16]],  # value
                            _type.HRESULT]
    get_SubCategory: _Callable[[_Pointer[_type.UINT16]],  # value
                               _type.HRESULT]


class IBluetoothLEAppearanceCategoriesStatics(_inspectable.IInspectable):
    get_Uncategorized: _Callable[[_Pointer[_type.UINT16]],  # value
                                 _type.HRESULT]
    get_Phone: _Callable[[_Pointer[_type.UINT16]],  # value
                         _type.HRESULT]
    get_Computer: _Callable[[_Pointer[_type.UINT16]],  # value
                            _type.HRESULT]
    get_Watch: _Callable[[_Pointer[_type.UINT16]],  # value
                         _type.HRESULT]
    get_Clock: _Callable[[_Pointer[_type.UINT16]],  # value
                         _type.HRESULT]
    get_Display: _Callable[[_Pointer[_type.UINT16]],  # value
                           _type.HRESULT]
    get_RemoteControl: _Callable[[_Pointer[_type.UINT16]],  # value
                                 _type.HRESULT]
    get_EyeGlasses: _Callable[[_Pointer[_type.UINT16]],  # value
                              _type.HRESULT]
    get_Tag: _Callable[[_Pointer[_type.UINT16]],  # value
                       _type.HRESULT]
    get_Keyring: _Callable[[_Pointer[_type.UINT16]],  # value
                           _type.HRESULT]
    get_MediaPlayer: _Callable[[_Pointer[_type.UINT16]],  # value
                               _type.HRESULT]
    get_BarcodeScanner: _Callable[[_Pointer[_type.UINT16]],  # value
                                  _type.HRESULT]
    get_Thermometer: _Callable[[_Pointer[_type.UINT16]],  # value
                               _type.HRESULT]
    get_HeartRate: _Callable[[_Pointer[_type.UINT16]],  # value
                             _type.HRESULT]
    get_BloodPressure: _Callable[[_Pointer[_type.UINT16]],  # value
                                 _type.HRESULT]
    get_HumanInterfaceDevice: _Callable[[_Pointer[_type.UINT16]],  # value
                                        _type.HRESULT]
    get_GlucoseMeter: _Callable[[_Pointer[_type.UINT16]],  # value
                                _type.HRESULT]
    get_RunningWalking: _Callable[[_Pointer[_type.UINT16]],  # value
                                  _type.HRESULT]
    get_Cycling: _Callable[[_Pointer[_type.UINT16]],  # value
                           _type.HRESULT]
    get_PulseOximeter: _Callable[[_Pointer[_type.UINT16]],  # value
                                 _type.HRESULT]
    get_WeightScale: _Callable[[_Pointer[_type.UINT16]],  # value
                               _type.HRESULT]
    get_OutdoorSportActivity: _Callable[[_Pointer[_type.UINT16]],  # value
                                        _type.HRESULT]

    _factory = True


class IBluetoothLEAppearanceStatics(_inspectable.IInspectable):
    FromRawValue: _Callable[[_type.UINT16,  # rawValue
                             _Pointer[IBluetoothLEAppearance]],  # appearance
                            _type.HRESULT]
    FromParts: _Callable[[_type.UINT16,  # appearanceCategory
                          _type.UINT16,  # appearanceSubCategory
                          _Pointer[IBluetoothLEAppearance]],  # appearance
                         _type.HRESULT]

    _factory = True


class IBluetoothLEAppearanceSubcategoriesStatics(_inspectable.IInspectable):
    get_Generic: _Callable[[_Pointer[_type.UINT16]],  # value
                           _type.HRESULT]
    get_SportsWatch: _Callable[[_Pointer[_type.UINT16]],  # value
                               _type.HRESULT]
    get_ThermometerEar: _Callable[[_Pointer[_type.UINT16]],  # value
                                  _type.HRESULT]
    get_HeartRateBelt: _Callable[[_Pointer[_type.UINT16]],  # value
                                 _type.HRESULT]
    get_BloodPressureArm: _Callable[[_Pointer[_type.UINT16]],  # value
                                    _type.HRESULT]
    get_BloodPressureWrist: _Callable[[_Pointer[_type.UINT16]],  # value
                                      _type.HRESULT]
    get_Keyboard: _Callable[[_Pointer[_type.UINT16]],  # value
                            _type.HRESULT]
    get_Mouse: _Callable[[_Pointer[_type.UINT16]],  # value
                         _type.HRESULT]
    get_Joystick: _Callable[[_Pointer[_type.UINT16]],  # value
                            _type.HRESULT]
    get_Gamepad: _Callable[[_Pointer[_type.UINT16]],  # value
                           _type.HRESULT]
    get_DigitizerTablet: _Callable[[_Pointer[_type.UINT16]],  # value
                                   _type.HRESULT]
    get_CardReader: _Callable[[_Pointer[_type.UINT16]],  # value
                              _type.HRESULT]
    get_DigitalPen: _Callable[[_Pointer[_type.UINT16]],  # value
                              _type.HRESULT]
    get_BarcodeScanner: _Callable[[_Pointer[_type.UINT16]],  # value
                                  _type.HRESULT]
    get_RunningWalkingInShoe: _Callable[[_Pointer[_type.UINT16]],  # value
                                        _type.HRESULT]
    get_RunningWalkingOnShoe: _Callable[[_Pointer[_type.UINT16]],  # value
                                        _type.HRESULT]
    get_RunningWalkingOnHip: _Callable[[_Pointer[_type.UINT16]],  # value
                                       _type.HRESULT]
    get_CyclingComputer: _Callable[[_Pointer[_type.UINT16]],  # value
                                   _type.HRESULT]
    get_CyclingSpeedSensor: _Callable[[_Pointer[_type.UINT16]],  # value
                                      _type.HRESULT]
    get_CyclingCadenceSensor: _Callable[[_Pointer[_type.UINT16]],  # value
                                        _type.HRESULT]
    get_CyclingPowerSensor: _Callable[[_Pointer[_type.UINT16]],  # value
                                      _type.HRESULT]
    get_CyclingSpeedCadenceSensor: _Callable[[_Pointer[_type.UINT16]],  # value
                                             _type.HRESULT]
    get_OximeterFingertip: _Callable[[_Pointer[_type.UINT16]],  # value
                                     _type.HRESULT]
    get_OximeterWristWorn: _Callable[[_Pointer[_type.UINT16]],  # value
                                     _type.HRESULT]
    get_LocationDisplay: _Callable[[_Pointer[_type.UINT16]],  # value
                                   _type.HRESULT]
    get_LocationNavigationDisplay: _Callable[[_Pointer[_type.UINT16]],  # value
                                             _type.HRESULT]
    get_LocationPod: _Callable[[_Pointer[_type.UINT16]],  # value
                               _type.HRESULT]
    get_LocationNavigationPod: _Callable[[_Pointer[_type.UINT16]],  # value
                                         _type.HRESULT]

    _factory = True


class IBluetoothLEConnectionParameters(_inspectable.IInspectable):
    get_LinkTimeout: _Callable[[_Pointer[_type.UINT16]],  # value
                               _type.HRESULT]
    get_ConnectionLatency: _Callable[[_Pointer[_type.UINT16]],  # value
                                     _type.HRESULT]
    get_ConnectionInterval: _Callable[[_Pointer[_type.UINT16]],  # value
                                      _type.HRESULT]


class IBluetoothLEConnectionPhy(_inspectable.IInspectable):
    get_TransmitInfo: _Callable[[_Pointer[IBluetoothLEConnectionPhyInfo]],  # value
                                _type.HRESULT]
    get_ReceiveInfo: _Callable[[_Pointer[IBluetoothLEConnectionPhyInfo]],  # value
                               _type.HRESULT]


class IBluetoothLEConnectionPhyInfo(_inspectable.IInspectable):
    get_IsUncoded1MPhy: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    get_IsUncoded2MPhy: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    get_IsCodedPhy: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]


class IBluetoothLEDevice(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    GattServices: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Devices_Bluetooth_GenericAttributeProfile.IGattDeviceService]]],  # value
                            _type.HRESULT]
    get_ConnectionStatus: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.BluetoothConnectionStatus]],  # value
                                    _type.HRESULT]
    get_BluetoothAddress: _Callable[[_Pointer[_type.UINT64]],  # value
                                    _type.HRESULT]
    GetGattService: _Callable[[_struct.GUID,  # serviceUuid
                               _Pointer[_Windows_Devices_Bluetooth_GenericAttributeProfile.IGattDeviceService]],  # service
                              _type.HRESULT]
    add_NameChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IBluetoothLEDevice, _inspectable.IInspectable],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_NameChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    add_GattServicesChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IBluetoothLEDevice, _inspectable.IInspectable],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_GattServicesChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_ConnectionStatusChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IBluetoothLEDevice, _inspectable.IInspectable],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_ConnectionStatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]


class IBluetoothLEDevice2(_inspectable.IInspectable):
    get_DeviceInformation: _Callable[[_Pointer[_Windows_Devices_Enumeration.IDeviceInformation]],  # value
                                     _type.HRESULT]
    get_Appearance: _Callable[[_Pointer[IBluetoothLEAppearance]],  # value
                              _type.HRESULT]
    get_BluetoothAddressType: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.BluetoothAddressType]],  # value
                                        _type.HRESULT]


class IBluetoothLEDevice3(_inspectable.IInspectable):
    get_DeviceAccessInformation: _Callable[[_Pointer[_Windows_Devices_Enumeration.IDeviceAccessInformation]],  # value
                                           _type.HRESULT]
    RequestAccessAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Devices.Enumeration.DeviceAccessStatus]]],  # operation
                                  _type.HRESULT]
    GetGattServicesAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Devices_Bluetooth_GenericAttributeProfile.IGattDeviceServicesResult]]],  # operation
                                    _type.HRESULT]
    GetGattServicesWithCacheModeAsync: _Callable[[_enum.Windows.Devices.Bluetooth.BluetoothCacheMode,  # cacheMode
                                                  _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Devices_Bluetooth_GenericAttributeProfile.IGattDeviceServicesResult]]],  # operation
                                                 _type.HRESULT]
    GetGattServicesForUuidAsync: _Callable[[_struct.GUID,  # serviceUuid
                                            _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Devices_Bluetooth_GenericAttributeProfile.IGattDeviceServicesResult]]],  # operation
                                           _type.HRESULT]
    GetGattServicesForUuidWithCacheModeAsync: _Callable[[_struct.GUID,  # serviceUuid
                                                         _enum.Windows.Devices.Bluetooth.BluetoothCacheMode,  # cacheMode
                                                         _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Devices_Bluetooth_GenericAttributeProfile.IGattDeviceServicesResult]]],  # operation
                                                        _type.HRESULT]


class IBluetoothLEDevice4(_inspectable.IInspectable):
    get_BluetoothDeviceId: _Callable[[_Pointer[IBluetoothDeviceId]],  # value
                                     _type.HRESULT]


class IBluetoothLEDevice5(_inspectable.IInspectable):
    get_WasSecureConnectionUsedForPairing: _Callable[[_Pointer[_type.boolean]],  # value
                                                     _type.HRESULT]


class IBluetoothLEDevice6(_inspectable.IInspectable):
    GetConnectionParameters: _Callable[[_Pointer[IBluetoothLEConnectionParameters]],  # result
                                       _type.HRESULT]
    GetConnectionPhy: _Callable[[_Pointer[IBluetoothLEConnectionPhy]],  # result
                                _type.HRESULT]
    RequestPreferredConnectionParameters: _Callable[[IBluetoothLEPreferredConnectionParameters,  # preferredConnectionParameters
                                                     _Pointer[IBluetoothLEPreferredConnectionParametersRequest]],  # result
                                                    _type.HRESULT]
    add_ConnectionParametersChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IBluetoothLEDevice, _inspectable.IInspectable],  # handler
                                                _Pointer[_struct.EventRegistrationToken]],  # token
                                               _type.HRESULT]
    remove_ConnectionParametersChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                  _type.HRESULT]
    add_ConnectionPhyChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IBluetoothLEDevice, _inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_ConnectionPhyChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]


class IBluetoothLEDeviceStatics(_inspectable.IInspectable):
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IBluetoothLEDevice]]],  # operation
                           _type.HRESULT]
    FromBluetoothAddressAsync: _Callable[[_type.UINT64,  # bluetoothAddress
                                          _Pointer[_Windows_Foundation.IAsyncOperation[IBluetoothLEDevice]]],  # operation
                                         _type.HRESULT]
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]

    _factory = True


class IBluetoothLEDeviceStatics2(_inspectable.IInspectable):
    GetDeviceSelectorFromPairingState: _Callable[[_type.boolean,  # pairingState
                                                  _Pointer[_type.HSTRING]],  # deviceSelector
                                                 _type.HRESULT]
    GetDeviceSelectorFromConnectionStatus: _Callable[[_enum.Windows.Devices.Bluetooth.BluetoothConnectionStatus,  # connectionStatus
                                                      _Pointer[_type.HSTRING]],  # deviceSelector
                                                     _type.HRESULT]
    GetDeviceSelectorFromDeviceName: _Callable[[_type.HSTRING,  # deviceName
                                                _Pointer[_type.HSTRING]],  # deviceSelector
                                               _type.HRESULT]
    GetDeviceSelectorFromBluetoothAddress: _Callable[[_type.UINT64,  # bluetoothAddress
                                                      _Pointer[_type.HSTRING]],  # deviceSelector
                                                     _type.HRESULT]
    GetDeviceSelectorFromBluetoothAddressWithBluetoothAddressType: _Callable[[_type.UINT64,  # bluetoothAddress
                                                                              _enum.Windows.Devices.Bluetooth.BluetoothAddressType,  # bluetoothAddressType
                                                                              _Pointer[_type.HSTRING]],  # deviceSelector
                                                                             _type.HRESULT]
    GetDeviceSelectorFromAppearance: _Callable[[IBluetoothLEAppearance,  # appearance
                                                _Pointer[_type.HSTRING]],  # deviceSelector
                                               _type.HRESULT]
    FromBluetoothAddressWithBluetoothAddressTypeAsync: _Callable[[_type.UINT64,  # bluetoothAddress
                                                                  _enum.Windows.Devices.Bluetooth.BluetoothAddressType,  # bluetoothAddressType
                                                                  _Pointer[_Windows_Foundation.IAsyncOperation[IBluetoothLEDevice]]],  # operation
                                                                 _type.HRESULT]

    _factory = True


class IBluetoothLEPreferredConnectionParameters(_inspectable.IInspectable):
    get_LinkTimeout: _Callable[[_Pointer[_type.UINT16]],  # value
                               _type.HRESULT]
    get_ConnectionLatency: _Callable[[_Pointer[_type.UINT16]],  # value
                                     _type.HRESULT]
    get_MinConnectionInterval: _Callable[[_Pointer[_type.UINT16]],  # value
                                         _type.HRESULT]
    get_MaxConnectionInterval: _Callable[[_Pointer[_type.UINT16]],  # value
                                         _type.HRESULT]


class IBluetoothLEPreferredConnectionParametersRequest(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.BluetoothLEPreferredConnectionParametersRequestStatus]],  # value
                          _type.HRESULT]


class IBluetoothLEPreferredConnectionParametersStatics(_inspectable.IInspectable):
    get_Balanced: _Callable[[_Pointer[IBluetoothLEPreferredConnectionParameters]],  # value
                            _type.HRESULT]
    get_ThroughputOptimized: _Callable[[_Pointer[IBluetoothLEPreferredConnectionParameters]],  # value
                                       _type.HRESULT]
    get_PowerOptimized: _Callable[[_Pointer[IBluetoothLEPreferredConnectionParameters]],  # value
                                  _type.HRESULT]

    _factory = True


class IBluetoothSignalStrengthFilter(_inspectable.IInspectable):
    get_InRangeThresholdInDBm: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT16]]],  # value
                                         _type.HRESULT]
    put_InRangeThresholdInDBm: _Callable[[_Windows_Foundation.IReference[_type.INT16]],  # value
                                         _type.HRESULT]
    get_OutOfRangeThresholdInDBm: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT16]]],  # value
                                            _type.HRESULT]
    put_OutOfRangeThresholdInDBm: _Callable[[_Windows_Foundation.IReference[_type.INT16]],  # value
                                            _type.HRESULT]
    get_OutOfRangeTimeout: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                     _type.HRESULT]
    put_OutOfRangeTimeout: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]],  # value
                                     _type.HRESULT]
    get_SamplingInterval: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                    _type.HRESULT]
    put_SamplingInterval: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]],  # value
                                    _type.HRESULT]


class IBluetoothUuidHelperStatics(_inspectable.IInspectable):
    FromShortId: _Callable[[_type.UINT32,  # shortId
                            _Pointer[_struct.GUID]],  # result
                           _type.HRESULT]
    TryGetShortId: _Callable[[_struct.GUID,  # uuid
                              _Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # result
                             _type.HRESULT]

    _factory = True
