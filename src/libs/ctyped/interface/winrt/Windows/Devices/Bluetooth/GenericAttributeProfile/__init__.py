from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Bluetooth as _Windows_Devices_Bluetooth
from ... import Enumeration as _Windows_Devices_Enumeration
from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ....Storage import Streams as _Windows_Storage_Streams
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IGattCharacteristic(_inspectable.IInspectable):
    GetDescriptors: _Callable[[_struct.GUID,  # descriptorUuid
                               _Pointer[_Windows_Foundation_Collections.IVectorView[IGattDescriptor]]],  # value
                              _type.HRESULT]
    get_CharacteristicProperties: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicProperties]],  # value
                                            _type.HRESULT]
    get_ProtectionLevel: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel]],  # value
                                   _type.HRESULT]
    put_ProtectionLevel: _Callable[[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel],  # value
                                   _type.HRESULT]
    get_UserDescription: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_Uuid: _Callable[[_Pointer[_struct.GUID]],  # value
                        _type.HRESULT]
    get_AttributeHandle: _Callable[[_Pointer[_type.UINT16]],  # value
                                   _type.HRESULT]
    get_PresentationFormats: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IGattPresentationFormat]]],  # value
                                       _type.HRESULT]
    ReadValueAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IGattReadResult]]],  # value
                              _type.HRESULT]
    ReadValueWithCacheModeAsync: _Callable[[_enum.Windows.Devices.Bluetooth.BluetoothCacheMode,  # cacheMode
                                            _Pointer[_Windows_Foundation.IAsyncOperation[IGattReadResult]]],  # value
                                           _type.HRESULT]
    WriteValueAsync: _Callable[[_Windows_Storage_Streams.IBuffer,  # value
                                _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus]]],  # asyncOp
                               _type.HRESULT]
    WriteValueWithOptionAsync: _Callable[[_Windows_Storage_Streams.IBuffer,  # value
                                          _enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteOption,  # writeOption
                                          _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus]]],  # asyncOp
                                         _type.HRESULT]
    ReadClientCharacteristicConfigurationDescriptorAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IGattReadClientCharacteristicConfigurationDescriptorResult]]],  # asyncOp
                                                                    _type.HRESULT]
    WriteClientCharacteristicConfigurationDescriptorAsync: _Callable[[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattClientCharacteristicConfigurationDescriptorValue,  # clientCharacteristicConfigurationDescriptorValue
                                                                      _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus]]],  # asyncOp
                                                                     _type.HRESULT]
    add_ValueChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IGattCharacteristic, IGattValueChangedEventArgs],  # valueChangedHandler
                                 _Pointer[_struct.EventRegistrationToken]],  # valueChangedEventCookie
                                _type.HRESULT]
    remove_ValueChanged: _Callable[[_struct.EventRegistrationToken],  # valueChangedEventCookie
                                   _type.HRESULT]


class IGattCharacteristic2(_inspectable.IInspectable):
    get_Service: _Callable[[_Pointer[IGattDeviceService]],  # value
                           _type.HRESULT]
    GetAllDescriptors: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IGattDescriptor]]],  # descriptors
                                 _type.HRESULT]


class IGattCharacteristic3(_inspectable.IInspectable):
    GetDescriptorsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IGattDescriptorsResult]]],  # operation
                                   _type.HRESULT]
    GetDescriptorsWithCacheModeAsync: _Callable[[_enum.Windows.Devices.Bluetooth.BluetoothCacheMode,  # cacheMode
                                                 _Pointer[_Windows_Foundation.IAsyncOperation[IGattDescriptorsResult]]],  # operation
                                                _type.HRESULT]
    GetDescriptorsForUuidAsync: _Callable[[_struct.GUID,  # descriptorUuid
                                           _Pointer[_Windows_Foundation.IAsyncOperation[IGattDescriptorsResult]]],  # operation
                                          _type.HRESULT]
    GetDescriptorsForUuidWithCacheModeAsync: _Callable[[_struct.GUID,  # descriptorUuid
                                                        _enum.Windows.Devices.Bluetooth.BluetoothCacheMode,  # cacheMode
                                                        _Pointer[_Windows_Foundation.IAsyncOperation[IGattDescriptorsResult]]],  # operation
                                                       _type.HRESULT]
    WriteValueWithResultAsync: _Callable[[_Windows_Storage_Streams.IBuffer,  # value
                                          _Pointer[_Windows_Foundation.IAsyncOperation[IGattWriteResult]]],  # operation
                                         _type.HRESULT]
    WriteValueWithResultAndOptionAsync: _Callable[[_Windows_Storage_Streams.IBuffer,  # value
                                                   _enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteOption,  # writeOption
                                                   _Pointer[_Windows_Foundation.IAsyncOperation[IGattWriteResult]]],  # operation
                                                  _type.HRESULT]
    WriteClientCharacteristicConfigurationDescriptorWithResultAsync: _Callable[[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattClientCharacteristicConfigurationDescriptorValue,  # clientCharacteristicConfigurationDescriptorValue
                                                                                _Pointer[_Windows_Foundation.IAsyncOperation[IGattWriteResult]]],  # operation
                                                                               _type.HRESULT]


class IGattCharacteristicStatics(_inspectable.IInspectable):
    ConvertShortIdToUuid: _Callable[[_type.UINT16,  # shortId
                                     _Pointer[_struct.GUID]],  # characteristicUuid
                                    _type.HRESULT]

    _factory = True


class IGattCharacteristicUuidsStatics(_inspectable.IInspectable):
    get_BatteryLevel: _Callable[[_Pointer[_struct.GUID]],  # value
                                _type.HRESULT]
    get_BloodPressureFeature: _Callable[[_Pointer[_struct.GUID]],  # value
                                        _type.HRESULT]
    get_BloodPressureMeasurement: _Callable[[_Pointer[_struct.GUID]],  # value
                                            _type.HRESULT]
    get_BodySensorLocation: _Callable[[_Pointer[_struct.GUID]],  # value
                                      _type.HRESULT]
    get_CscFeature: _Callable[[_Pointer[_struct.GUID]],  # value
                              _type.HRESULT]
    get_CscMeasurement: _Callable[[_Pointer[_struct.GUID]],  # value
                                  _type.HRESULT]
    get_GlucoseFeature: _Callable[[_Pointer[_struct.GUID]],  # value
                                  _type.HRESULT]
    get_GlucoseMeasurement: _Callable[[_Pointer[_struct.GUID]],  # value
                                      _type.HRESULT]
    get_GlucoseMeasurementContext: _Callable[[_Pointer[_struct.GUID]],  # value
                                             _type.HRESULT]
    get_HeartRateControlPoint: _Callable[[_Pointer[_struct.GUID]],  # value
                                         _type.HRESULT]
    get_HeartRateMeasurement: _Callable[[_Pointer[_struct.GUID]],  # value
                                        _type.HRESULT]
    get_IntermediateCuffPressure: _Callable[[_Pointer[_struct.GUID]],  # value
                                            _type.HRESULT]
    get_IntermediateTemperature: _Callable[[_Pointer[_struct.GUID]],  # value
                                           _type.HRESULT]
    get_MeasurementInterval: _Callable[[_Pointer[_struct.GUID]],  # value
                                       _type.HRESULT]
    get_RecordAccessControlPoint: _Callable[[_Pointer[_struct.GUID]],  # value
                                            _type.HRESULT]
    get_RscFeature: _Callable[[_Pointer[_struct.GUID]],  # value
                              _type.HRESULT]
    get_RscMeasurement: _Callable[[_Pointer[_struct.GUID]],  # value
                                  _type.HRESULT]
    get_SCControlPoint: _Callable[[_Pointer[_struct.GUID]],  # value
                                  _type.HRESULT]
    get_SensorLocation: _Callable[[_Pointer[_struct.GUID]],  # value
                                  _type.HRESULT]
    get_TemperatureMeasurement: _Callable[[_Pointer[_struct.GUID]],  # value
                                          _type.HRESULT]
    get_TemperatureType: _Callable[[_Pointer[_struct.GUID]],  # value
                                   _type.HRESULT]

    _factory = True


class IGattCharacteristicUuidsStatics2(_inspectable.IInspectable):
    get_AlertCategoryId: _Callable[[_Pointer[_struct.GUID]],  # value
                                   _type.HRESULT]
    get_AlertCategoryIdBitMask: _Callable[[_Pointer[_struct.GUID]],  # value
                                          _type.HRESULT]
    get_AlertLevel: _Callable[[_Pointer[_struct.GUID]],  # value
                              _type.HRESULT]
    get_AlertNotificationControlPoint: _Callable[[_Pointer[_struct.GUID]],  # value
                                                 _type.HRESULT]
    get_AlertStatus: _Callable[[_Pointer[_struct.GUID]],  # value
                               _type.HRESULT]
    get_GapAppearance: _Callable[[_Pointer[_struct.GUID]],  # value
                                 _type.HRESULT]
    get_BootKeyboardInputReport: _Callable[[_Pointer[_struct.GUID]],  # value
                                           _type.HRESULT]
    get_BootKeyboardOutputReport: _Callable[[_Pointer[_struct.GUID]],  # value
                                            _type.HRESULT]
    get_BootMouseInputReport: _Callable[[_Pointer[_struct.GUID]],  # value
                                        _type.HRESULT]
    get_CurrentTime: _Callable[[_Pointer[_struct.GUID]],  # value
                               _type.HRESULT]
    get_CyclingPowerControlPoint: _Callable[[_Pointer[_struct.GUID]],  # value
                                            _type.HRESULT]
    get_CyclingPowerFeature: _Callable[[_Pointer[_struct.GUID]],  # value
                                       _type.HRESULT]
    get_CyclingPowerMeasurement: _Callable[[_Pointer[_struct.GUID]],  # value
                                           _type.HRESULT]
    get_CyclingPowerVector: _Callable[[_Pointer[_struct.GUID]],  # value
                                      _type.HRESULT]
    get_DateTime: _Callable[[_Pointer[_struct.GUID]],  # value
                            _type.HRESULT]
    get_DayDateTime: _Callable[[_Pointer[_struct.GUID]],  # value
                               _type.HRESULT]
    get_DayOfWeek: _Callable[[_Pointer[_struct.GUID]],  # value
                             _type.HRESULT]
    get_GapDeviceName: _Callable[[_Pointer[_struct.GUID]],  # value
                                 _type.HRESULT]
    get_DstOffset: _Callable[[_Pointer[_struct.GUID]],  # value
                             _type.HRESULT]
    get_ExactTime256: _Callable[[_Pointer[_struct.GUID]],  # value
                                _type.HRESULT]
    get_FirmwareRevisionString: _Callable[[_Pointer[_struct.GUID]],  # value
                                          _type.HRESULT]
    get_HardwareRevisionString: _Callable[[_Pointer[_struct.GUID]],  # value
                                          _type.HRESULT]
    get_HidControlPoint: _Callable[[_Pointer[_struct.GUID]],  # value
                                   _type.HRESULT]
    get_HidInformation: _Callable[[_Pointer[_struct.GUID]],  # value
                                  _type.HRESULT]
    get_Ieee1107320601RegulatoryCertificationDataList: _Callable[[_Pointer[_struct.GUID]],  # value
                                                                 _type.HRESULT]
    get_LnControlPoint: _Callable[[_Pointer[_struct.GUID]],  # value
                                  _type.HRESULT]
    get_LnFeature: _Callable[[_Pointer[_struct.GUID]],  # value
                             _type.HRESULT]
    get_LocalTimeInformation: _Callable[[_Pointer[_struct.GUID]],  # value
                                        _type.HRESULT]
    get_LocationAndSpeed: _Callable[[_Pointer[_struct.GUID]],  # value
                                    _type.HRESULT]
    get_ManufacturerNameString: _Callable[[_Pointer[_struct.GUID]],  # value
                                          _type.HRESULT]
    get_ModelNumberString: _Callable[[_Pointer[_struct.GUID]],  # value
                                     _type.HRESULT]
    get_Navigation: _Callable[[_Pointer[_struct.GUID]],  # value
                              _type.HRESULT]
    get_NewAlert: _Callable[[_Pointer[_struct.GUID]],  # value
                            _type.HRESULT]
    get_GapPeripheralPreferredConnectionParameters: _Callable[[_Pointer[_struct.GUID]],  # value
                                                              _type.HRESULT]
    get_GapPeripheralPrivacyFlag: _Callable[[_Pointer[_struct.GUID]],  # value
                                            _type.HRESULT]
    get_PnpId: _Callable[[_Pointer[_struct.GUID]],  # value
                         _type.HRESULT]
    get_PositionQuality: _Callable[[_Pointer[_struct.GUID]],  # value
                                   _type.HRESULT]
    get_ProtocolMode: _Callable[[_Pointer[_struct.GUID]],  # value
                                _type.HRESULT]
    get_GapReconnectionAddress: _Callable[[_Pointer[_struct.GUID]],  # value
                                          _type.HRESULT]
    get_ReferenceTimeInformation: _Callable[[_Pointer[_struct.GUID]],  # value
                                            _type.HRESULT]
    get_Report: _Callable[[_Pointer[_struct.GUID]],  # value
                          _type.HRESULT]
    get_ReportMap: _Callable[[_Pointer[_struct.GUID]],  # value
                             _type.HRESULT]
    get_RingerControlPoint: _Callable[[_Pointer[_struct.GUID]],  # value
                                      _type.HRESULT]
    get_RingerSetting: _Callable[[_Pointer[_struct.GUID]],  # value
                                 _type.HRESULT]
    get_ScanIntervalWindow: _Callable[[_Pointer[_struct.GUID]],  # value
                                      _type.HRESULT]
    get_ScanRefresh: _Callable[[_Pointer[_struct.GUID]],  # value
                               _type.HRESULT]
    get_SerialNumberString: _Callable[[_Pointer[_struct.GUID]],  # value
                                      _type.HRESULT]
    get_GattServiceChanged: _Callable[[_Pointer[_struct.GUID]],  # value
                                      _type.HRESULT]
    get_SoftwareRevisionString: _Callable[[_Pointer[_struct.GUID]],  # value
                                          _type.HRESULT]
    get_SupportedNewAlertCategory: _Callable[[_Pointer[_struct.GUID]],  # value
                                             _type.HRESULT]
    get_SupportUnreadAlertCategory: _Callable[[_Pointer[_struct.GUID]],  # value
                                              _type.HRESULT]
    get_SystemId: _Callable[[_Pointer[_struct.GUID]],  # value
                            _type.HRESULT]
    get_TimeAccuracy: _Callable[[_Pointer[_struct.GUID]],  # value
                                _type.HRESULT]
    get_TimeSource: _Callable[[_Pointer[_struct.GUID]],  # value
                              _type.HRESULT]
    get_TimeUpdateControlPoint: _Callable[[_Pointer[_struct.GUID]],  # value
                                          _type.HRESULT]
    get_TimeUpdateState: _Callable[[_Pointer[_struct.GUID]],  # value
                                   _type.HRESULT]
    get_TimeWithDst: _Callable[[_Pointer[_struct.GUID]],  # value
                               _type.HRESULT]
    get_TimeZone: _Callable[[_Pointer[_struct.GUID]],  # value
                            _type.HRESULT]
    get_TxPowerLevel: _Callable[[_Pointer[_struct.GUID]],  # value
                                _type.HRESULT]
    get_UnreadAlertStatus: _Callable[[_Pointer[_struct.GUID]],  # value
                                     _type.HRESULT]

    _factory = True


class IGattCharacteristicsResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus]],  # value
                          _type.HRESULT]
    get_ProtocolError: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.BYTE]]],  # value
                                 _type.HRESULT]
    get_Characteristics: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IGattCharacteristic]]],  # value
                                   _type.HRESULT]


class IGattClientNotificationResult(_inspectable.IInspectable):
    get_SubscribedClient: _Callable[[_Pointer[IGattSubscribedClient]],  # value
                                    _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus]],  # value
                          _type.HRESULT]
    get_ProtocolError: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.BYTE]]],  # value
                                 _type.HRESULT]


class IGattClientNotificationResult2(_inspectable.IInspectable):
    get_BytesSent: _Callable[[_Pointer[_type.UINT16]],  # value
                             _type.HRESULT]


class IGattDescriptor(_inspectable.IInspectable):
    get_ProtectionLevel: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel]],  # value
                                   _type.HRESULT]
    put_ProtectionLevel: _Callable[[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel],  # value
                                   _type.HRESULT]
    get_Uuid: _Callable[[_Pointer[_struct.GUID]],  # value
                        _type.HRESULT]
    get_AttributeHandle: _Callable[[_Pointer[_type.UINT16]],  # value
                                   _type.HRESULT]
    ReadValueAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IGattReadResult]]],  # value
                              _type.HRESULT]
    ReadValueWithCacheModeAsync: _Callable[[_enum.Windows.Devices.Bluetooth.BluetoothCacheMode,  # cacheMode
                                            _Pointer[_Windows_Foundation.IAsyncOperation[IGattReadResult]]],  # value
                                           _type.HRESULT]
    WriteValueAsync: _Callable[[_Windows_Storage_Streams.IBuffer,  # value
                                _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus]]],  # action
                               _type.HRESULT]


class IGattDescriptor2(_inspectable.IInspectable):
    WriteValueWithResultAsync: _Callable[[_Windows_Storage_Streams.IBuffer,  # value
                                          _Pointer[_Windows_Foundation.IAsyncOperation[IGattWriteResult]]],  # operation
                                         _type.HRESULT]


class IGattDescriptorStatics(_inspectable.IInspectable):
    ConvertShortIdToUuid: _Callable[[_type.UINT16,  # shortId
                                     _Pointer[_struct.GUID]],  # descriptorUuid
                                    _type.HRESULT]

    _factory = True


class IGattDescriptorUuidsStatics(_inspectable.IInspectable):
    get_CharacteristicAggregateFormat: _Callable[[_Pointer[_struct.GUID]],  # value
                                                 _type.HRESULT]
    get_CharacteristicExtendedProperties: _Callable[[_Pointer[_struct.GUID]],  # value
                                                    _type.HRESULT]
    get_CharacteristicPresentationFormat: _Callable[[_Pointer[_struct.GUID]],  # value
                                                    _type.HRESULT]
    get_CharacteristicUserDescription: _Callable[[_Pointer[_struct.GUID]],  # value
                                                 _type.HRESULT]
    get_ClientCharacteristicConfiguration: _Callable[[_Pointer[_struct.GUID]],  # value
                                                     _type.HRESULT]
    get_ServerCharacteristicConfiguration: _Callable[[_Pointer[_struct.GUID]],  # value
                                                     _type.HRESULT]

    _factory = True


class IGattDescriptorsResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus]],  # value
                          _type.HRESULT]
    get_ProtocolError: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.BYTE]]],  # value
                                 _type.HRESULT]
    get_Descriptors: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IGattDescriptor]]],  # value
                               _type.HRESULT]


class IGattDeviceService(_inspectable.IInspectable):
    GetCharacteristics: _Callable[[_struct.GUID,  # characteristicUuid
                                   _Pointer[_Windows_Foundation_Collections.IVectorView[IGattCharacteristic]]],  # value
                                  _type.HRESULT]
    GetIncludedServices: _Callable[[_struct.GUID,  # serviceUuid
                                    _Pointer[_Windows_Foundation_Collections.IVectorView[IGattDeviceService]]],  # value
                                   _type.HRESULT]
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Uuid: _Callable[[_Pointer[_struct.GUID]],  # value
                        _type.HRESULT]
    get_AttributeHandle: _Callable[[_Pointer[_type.UINT16]],  # value
                                   _type.HRESULT]


class IGattDeviceService2(_inspectable.IInspectable):
    Device: _Callable[[_Pointer[_Windows_Devices_Bluetooth.IBluetoothLEDevice]],  # value
                      _type.HRESULT]
    ParentServices: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IGattDeviceService]]],  # value
                              _type.HRESULT]
    GetAllCharacteristics: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IGattCharacteristic]]],  # characteristics
                                     _type.HRESULT]
    GetAllIncludedServices: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IGattDeviceService]]],  # includedServices
                                      _type.HRESULT]


class IGattDeviceService3(_inspectable.IInspectable):
    get_DeviceAccessInformation: _Callable[[_Pointer[_Windows_Devices_Enumeration.IDeviceAccessInformation]],  # value
                                           _type.HRESULT]
    get_Session: _Callable[[_Pointer[IGattSession]],  # value
                           _type.HRESULT]
    get_SharingMode: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSharingMode]],  # value
                               _type.HRESULT]
    RequestAccessAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Devices.Enumeration.DeviceAccessStatus]]],  # value
                                  _type.HRESULT]
    OpenAsync: _Callable[[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSharingMode,  # sharingMode
                          _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattOpenStatus]]],  # operation
                         _type.HRESULT]
    GetCharacteristicsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IGattCharacteristicsResult]]],  # operation
                                       _type.HRESULT]
    GetCharacteristicsWithCacheModeAsync: _Callable[[_enum.Windows.Devices.Bluetooth.BluetoothCacheMode,  # cacheMode
                                                     _Pointer[_Windows_Foundation.IAsyncOperation[IGattCharacteristicsResult]]],  # operation
                                                    _type.HRESULT]
    GetCharacteristicsForUuidAsync: _Callable[[_struct.GUID,  # characteristicUuid
                                               _Pointer[_Windows_Foundation.IAsyncOperation[IGattCharacteristicsResult]]],  # operation
                                              _type.HRESULT]
    GetCharacteristicsForUuidWithCacheModeAsync: _Callable[[_struct.GUID,  # characteristicUuid
                                                            _enum.Windows.Devices.Bluetooth.BluetoothCacheMode,  # cacheMode
                                                            _Pointer[_Windows_Foundation.IAsyncOperation[IGattCharacteristicsResult]]],  # operation
                                                           _type.HRESULT]
    GetIncludedServicesAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IGattDeviceServicesResult]]],  # operation
                                        _type.HRESULT]
    GetIncludedServicesWithCacheModeAsync: _Callable[[_enum.Windows.Devices.Bluetooth.BluetoothCacheMode,  # cacheMode
                                                      _Pointer[_Windows_Foundation.IAsyncOperation[IGattDeviceServicesResult]]],  # operation
                                                     _type.HRESULT]
    GetIncludedServicesForUuidAsync: _Callable[[_struct.GUID,  # serviceUuid
                                                _Pointer[_Windows_Foundation.IAsyncOperation[IGattDeviceServicesResult]]],  # operation
                                               _type.HRESULT]
    GetIncludedServicesForUuidWithCacheModeAsync: _Callable[[_struct.GUID,  # serviceUuid
                                                             _enum.Windows.Devices.Bluetooth.BluetoothCacheMode,  # cacheMode
                                                             _Pointer[_Windows_Foundation.IAsyncOperation[IGattDeviceServicesResult]]],  # operation
                                                            _type.HRESULT]


class IGattDeviceServiceStatics(_inspectable.IInspectable):
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IGattDeviceService]]],  # asyncOp
                           _type.HRESULT]
    GetDeviceSelectorFromUuid: _Callable[[_struct.GUID,  # serviceUuid
                                          _Pointer[_type.HSTRING]],  # selector
                                         _type.HRESULT]
    GetDeviceSelectorFromShortId: _Callable[[_type.UINT16,  # serviceShortId
                                             _Pointer[_type.HSTRING]],  # selector
                                            _type.HRESULT]
    ConvertShortIdToUuid: _Callable[[_type.UINT16,  # shortId
                                     _Pointer[_struct.GUID]],  # serviceUuid
                                    _type.HRESULT]

    _factory = True


class IGattDeviceServiceStatics2(_inspectable.IInspectable):
    FromIdWithSharingModeAsync: _Callable[[_type.HSTRING,  # deviceId
                                           _enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSharingMode,  # sharingMode
                                           _Pointer[_Windows_Foundation.IAsyncOperation[IGattDeviceService]]],  # operation
                                          _type.HRESULT]
    GetDeviceSelectorForBluetoothDeviceId: _Callable[[_Windows_Devices_Bluetooth.IBluetoothDeviceId,  # bluetoothDeviceId
                                                      _Pointer[_type.HSTRING]],  # result
                                                     _type.HRESULT]
    GetDeviceSelectorForBluetoothDeviceIdWithCacheMode: _Callable[[_Windows_Devices_Bluetooth.IBluetoothDeviceId,  # bluetoothDeviceId
                                                                   _enum.Windows.Devices.Bluetooth.BluetoothCacheMode,  # cacheMode
                                                                   _Pointer[_type.HSTRING]],  # result
                                                                  _type.HRESULT]
    GetDeviceSelectorForBluetoothDeviceIdAndUuid: _Callable[[_Windows_Devices_Bluetooth.IBluetoothDeviceId,  # bluetoothDeviceId
                                                             _struct.GUID,  # serviceUuid
                                                             _Pointer[_type.HSTRING]],  # result
                                                            _type.HRESULT]
    GetDeviceSelectorForBluetoothDeviceIdAndUuidWithCacheMode: _Callable[[_Windows_Devices_Bluetooth.IBluetoothDeviceId,  # bluetoothDeviceId
                                                                          _struct.GUID,  # serviceUuid
                                                                          _enum.Windows.Devices.Bluetooth.BluetoothCacheMode,  # cacheMode
                                                                          _Pointer[_type.HSTRING]],  # result
                                                                         _type.HRESULT]

    _factory = True


class IGattDeviceServicesResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus]],  # value
                          _type.HRESULT]
    get_ProtocolError: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.BYTE]]],  # value
                                 _type.HRESULT]
    get_Services: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IGattDeviceService]]],  # value
                            _type.HRESULT]


class IGattLocalCharacteristic(_inspectable.IInspectable):
    get_Uuid: _Callable[[_Pointer[_struct.GUID]],  # value
                        _type.HRESULT]
    get_StaticValue: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                               _type.HRESULT]
    get_CharacteristicProperties: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicProperties]],  # value
                                            _type.HRESULT]
    get_ReadProtectionLevel: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel]],  # value
                                       _type.HRESULT]
    get_WriteProtectionLevel: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel]],  # value
                                        _type.HRESULT]
    CreateDescriptorAsync: _Callable[[_struct.GUID,  # descriptorUuid
                                      IGattLocalDescriptorParameters,  # parameters
                                      _Pointer[_Windows_Foundation.IAsyncOperation[IGattLocalDescriptorResult]]],  # operation
                                     _type.HRESULT]
    get_Descriptors: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IGattLocalDescriptor]]],  # value
                               _type.HRESULT]
    get_UserDescription: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_PresentationFormats: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IGattPresentationFormat]]],  # value
                                       _type.HRESULT]
    get_SubscribedClients: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IGattSubscribedClient]]],  # value
                                     _type.HRESULT]
    add_SubscribedClientsChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IGattLocalCharacteristic, _inspectable.IInspectable],  # handler
                                             _Pointer[_struct.EventRegistrationToken]],  # token
                                            _type.HRESULT]
    remove_SubscribedClientsChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                               _type.HRESULT]
    add_ReadRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IGattLocalCharacteristic, IGattReadRequestedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_ReadRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_WriteRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IGattLocalCharacteristic, IGattWriteRequestedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_WriteRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    NotifyValueAsync: _Callable[[_Windows_Storage_Streams.IBuffer,  # value
                                 _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IGattClientNotificationResult]]]],  # operation
                                _type.HRESULT]
    NotifyValueForSubscribedClientAsync: _Callable[[_Windows_Storage_Streams.IBuffer,  # value
                                                    IGattSubscribedClient,  # subscribedClient
                                                    _Pointer[_Windows_Foundation.IAsyncOperation[IGattClientNotificationResult]]],  # operation
                                                   _type.HRESULT]


class IGattLocalCharacteristicParameters(_inspectable.IInspectable):
    put_StaticValue: _Callable[[_Windows_Storage_Streams.IBuffer],  # value
                               _type.HRESULT]
    get_StaticValue: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                               _type.HRESULT]
    put_CharacteristicProperties: _Callable[[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicProperties],  # value
                                            _type.HRESULT]
    get_CharacteristicProperties: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicProperties]],  # value
                                            _type.HRESULT]
    put_ReadProtectionLevel: _Callable[[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel],  # value
                                       _type.HRESULT]
    get_ReadProtectionLevel: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel]],  # value
                                       _type.HRESULT]
    put_WriteProtectionLevel: _Callable[[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel],  # value
                                        _type.HRESULT]
    get_WriteProtectionLevel: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel]],  # value
                                        _type.HRESULT]
    put_UserDescription: _Callable[[_type.HSTRING],  # value
                                   _type.HRESULT]
    get_UserDescription: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_PresentationFormats: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IGattPresentationFormat]]],  # value
                                       _type.HRESULT]


class IGattLocalCharacteristicResult(_inspectable.IInspectable):
    get_Characteristic: _Callable[[_Pointer[IGattLocalCharacteristic]],  # value
                                  _type.HRESULT]
    get_Error: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.BluetoothError]],  # value
                         _type.HRESULT]


class IGattLocalDescriptor(_inspectable.IInspectable):
    get_Uuid: _Callable[[_Pointer[_struct.GUID]],  # value
                        _type.HRESULT]
    get_StaticValue: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                               _type.HRESULT]
    get_ReadProtectionLevel: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel]],  # value
                                       _type.HRESULT]
    get_WriteProtectionLevel: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel]],  # value
                                        _type.HRESULT]
    add_ReadRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IGattLocalDescriptor, IGattReadRequestedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_ReadRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_WriteRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IGattLocalDescriptor, IGattWriteRequestedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_WriteRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]


class IGattLocalDescriptorParameters(_inspectable.IInspectable):
    put_StaticValue: _Callable[[_Windows_Storage_Streams.IBuffer],  # value
                               _type.HRESULT]
    get_StaticValue: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                               _type.HRESULT]
    put_ReadProtectionLevel: _Callable[[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel],  # value
                                       _type.HRESULT]
    get_ReadProtectionLevel: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel]],  # value
                                       _type.HRESULT]
    put_WriteProtectionLevel: _Callable[[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel],  # value
                                        _type.HRESULT]
    get_WriteProtectionLevel: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel]],  # value
                                        _type.HRESULT]


class IGattLocalDescriptorResult(_inspectable.IInspectable):
    get_Descriptor: _Callable[[_Pointer[IGattLocalDescriptor]],  # value
                              _type.HRESULT]
    get_Error: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.BluetoothError]],  # value
                         _type.HRESULT]


class IGattLocalService(_inspectable.IInspectable):
    get_Uuid: _Callable[[_Pointer[_struct.GUID]],  # value
                        _type.HRESULT]
    CreateCharacteristicAsync: _Callable[[_struct.GUID,  # characteristicUuid
                                          IGattLocalCharacteristicParameters,  # parameters
                                          _Pointer[_Windows_Foundation.IAsyncOperation[IGattLocalCharacteristicResult]]],  # operation
                                         _type.HRESULT]
    get_Characteristics: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IGattLocalCharacteristic]]],  # value
                                   _type.HRESULT]


class IGattPresentationFormat(_inspectable.IInspectable):
    get_FormatType: _Callable[[_Pointer[_type.BYTE]],  # value
                              _type.HRESULT]
    get_Exponent: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    get_Unit: _Callable[[_Pointer[_type.UINT16]],  # value
                        _type.HRESULT]
    get_Namespace: _Callable[[_Pointer[_type.BYTE]],  # value
                             _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.UINT16]],  # value
                               _type.HRESULT]


class IGattPresentationFormatStatics(_inspectable.IInspectable):
    get_BluetoothSigAssignedNumbers: _Callable[[_Pointer[_type.BYTE]],  # value
                                               _type.HRESULT]

    _factory = True


class IGattPresentationFormatStatics2(_inspectable.IInspectable):
    FromParts: _Callable[[_type.BYTE,  # formatType
                          _type.INT32,  # exponent
                          _type.UINT16,  # unit
                          _type.BYTE,  # namespaceId
                          _type.UINT16,  # description
                          _Pointer[IGattPresentationFormat]],  # result
                         _type.HRESULT]

    _factory = True


class IGattPresentationFormatTypesStatics(_inspectable.IInspectable):
    get_Boolean: _Callable[[_Pointer[_type.BYTE]],  # value
                           _type.HRESULT]
    get_Bit2: _Callable[[_Pointer[_type.BYTE]],  # value
                        _type.HRESULT]
    get_Nibble: _Callable[[_Pointer[_type.BYTE]],  # value
                          _type.HRESULT]
    get_UInt8: _Callable[[_Pointer[_type.BYTE]],  # value
                         _type.HRESULT]
    get_UInt12: _Callable[[_Pointer[_type.BYTE]],  # value
                          _type.HRESULT]
    get_UInt16: _Callable[[_Pointer[_type.BYTE]],  # value
                          _type.HRESULT]
    get_UInt24: _Callable[[_Pointer[_type.BYTE]],  # value
                          _type.HRESULT]
    get_UInt32: _Callable[[_Pointer[_type.BYTE]],  # value
                          _type.HRESULT]
    get_UInt48: _Callable[[_Pointer[_type.BYTE]],  # value
                          _type.HRESULT]
    get_UInt64: _Callable[[_Pointer[_type.BYTE]],  # value
                          _type.HRESULT]
    get_UInt128: _Callable[[_Pointer[_type.BYTE]],  # value
                           _type.HRESULT]
    get_SInt8: _Callable[[_Pointer[_type.BYTE]],  # value
                         _type.HRESULT]
    get_SInt12: _Callable[[_Pointer[_type.BYTE]],  # value
                          _type.HRESULT]
    get_SInt16: _Callable[[_Pointer[_type.BYTE]],  # value
                          _type.HRESULT]
    get_SInt24: _Callable[[_Pointer[_type.BYTE]],  # value
                          _type.HRESULT]
    get_SInt32: _Callable[[_Pointer[_type.BYTE]],  # value
                          _type.HRESULT]
    get_SInt48: _Callable[[_Pointer[_type.BYTE]],  # value
                          _type.HRESULT]
    get_SInt64: _Callable[[_Pointer[_type.BYTE]],  # value
                          _type.HRESULT]
    get_SInt128: _Callable[[_Pointer[_type.BYTE]],  # value
                           _type.HRESULT]
    get_Float32: _Callable[[_Pointer[_type.BYTE]],  # value
                           _type.HRESULT]
    get_Float64: _Callable[[_Pointer[_type.BYTE]],  # value
                           _type.HRESULT]
    get_SFloat: _Callable[[_Pointer[_type.BYTE]],  # value
                          _type.HRESULT]
    get_Float: _Callable[[_Pointer[_type.BYTE]],  # value
                         _type.HRESULT]
    get_DUInt16: _Callable[[_Pointer[_type.BYTE]],  # value
                           _type.HRESULT]
    get_Utf8: _Callable[[_Pointer[_type.BYTE]],  # value
                        _type.HRESULT]
    get_Utf16: _Callable[[_Pointer[_type.BYTE]],  # value
                         _type.HRESULT]
    get_Struct: _Callable[[_Pointer[_type.BYTE]],  # value
                          _type.HRESULT]

    _factory = True


class IGattProtocolErrorStatics(_inspectable.IInspectable):
    get_InvalidHandle: _Callable[[_Pointer[_type.BYTE]],  # value
                                 _type.HRESULT]
    get_ReadNotPermitted: _Callable[[_Pointer[_type.BYTE]],  # value
                                    _type.HRESULT]
    get_WriteNotPermitted: _Callable[[_Pointer[_type.BYTE]],  # value
                                     _type.HRESULT]
    get_InvalidPdu: _Callable[[_Pointer[_type.BYTE]],  # value
                              _type.HRESULT]
    get_InsufficientAuthentication: _Callable[[_Pointer[_type.BYTE]],  # value
                                              _type.HRESULT]
    get_RequestNotSupported: _Callable[[_Pointer[_type.BYTE]],  # value
                                       _type.HRESULT]
    get_InvalidOffset: _Callable[[_Pointer[_type.BYTE]],  # value
                                 _type.HRESULT]
    get_InsufficientAuthorization: _Callable[[_Pointer[_type.BYTE]],  # value
                                             _type.HRESULT]
    get_PrepareQueueFull: _Callable[[_Pointer[_type.BYTE]],  # value
                                    _type.HRESULT]
    get_AttributeNotFound: _Callable[[_Pointer[_type.BYTE]],  # value
                                     _type.HRESULT]
    get_AttributeNotLong: _Callable[[_Pointer[_type.BYTE]],  # value
                                    _type.HRESULT]
    get_InsufficientEncryptionKeySize: _Callable[[_Pointer[_type.BYTE]],  # value
                                                 _type.HRESULT]
    get_InvalidAttributeValueLength: _Callable[[_Pointer[_type.BYTE]],  # value
                                               _type.HRESULT]
    get_UnlikelyError: _Callable[[_Pointer[_type.BYTE]],  # value
                                 _type.HRESULT]
    get_InsufficientEncryption: _Callable[[_Pointer[_type.BYTE]],  # value
                                          _type.HRESULT]
    get_UnsupportedGroupType: _Callable[[_Pointer[_type.BYTE]],  # value
                                        _type.HRESULT]
    get_InsufficientResources: _Callable[[_Pointer[_type.BYTE]],  # value
                                         _type.HRESULT]

    _factory = True


class IGattReadClientCharacteristicConfigurationDescriptorResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus]],  # value
                          _type.HRESULT]
    get_ClientCharacteristicConfigurationDescriptor: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattClientCharacteristicConfigurationDescriptorValue]],  # value
                                                               _type.HRESULT]


class IGattReadClientCharacteristicConfigurationDescriptorResult2(_inspectable.IInspectable):
    get_ProtocolError: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.BYTE]]],  # value
                                 _type.HRESULT]


class IGattReadRequest(_inspectable.IInspectable):
    get_Offset: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    get_Length: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    get_State: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattRequestState]],  # value
                         _type.HRESULT]
    add_StateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IGattReadRequest, IGattRequestStateChangedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_StateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    RespondWithValue: _Callable[[_Windows_Storage_Streams.IBuffer],  # value
                                _type.HRESULT]
    RespondWithProtocolError: _Callable[[_type.BYTE],  # protocolError
                                        _type.HRESULT]


class IGattReadRequestedEventArgs(_inspectable.IInspectable):
    get_Session: _Callable[[_Pointer[IGattSession]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]
    GetRequestAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IGattReadRequest]]],  # operation
                               _type.HRESULT]


class IGattReadResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus]],  # value
                          _type.HRESULT]
    get_Value: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                         _type.HRESULT]


class IGattReadResult2(_inspectable.IInspectable):
    get_ProtocolError: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.BYTE]]],  # value
                                 _type.HRESULT]


class IGattReliableWriteTransaction(_inspectable.IInspectable):
    WriteValue: _Callable[[IGattCharacteristic,  # characteristic
                           _Windows_Storage_Streams.IBuffer],  # value
                          _type.HRESULT]
    CommitAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus]]],  # asyncOp
                           _type.HRESULT]


class IGattReliableWriteTransaction2(_inspectable.IInspectable):
    CommitWithResultAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IGattWriteResult]]],  # operation
                                     _type.HRESULT]


class IGattRequestStateChangedEventArgs(_inspectable.IInspectable):
    get_State: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattRequestState]],  # value
                         _type.HRESULT]
    get_Error: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.BluetoothError]],  # value
                         _type.HRESULT]


class IGattServiceProvider(_inspectable.IInspectable):
    get_Service: _Callable[[_Pointer[IGattLocalService]],  # value
                           _type.HRESULT]
    get_AdvertisementStatus: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderAdvertisementStatus]],  # value
                                       _type.HRESULT]
    add_AdvertisementStatusChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IGattServiceProvider, IGattServiceProviderAdvertisementStatusChangedEventArgs],  # handler
                                               _Pointer[_struct.EventRegistrationToken]],  # token
                                              _type.HRESULT]
    remove_AdvertisementStatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                 _type.HRESULT]
    StartAdvertising: _Callable[[],
                                _type.HRESULT]
    StartAdvertisingWithParameters: _Callable[[IGattServiceProviderAdvertisingParameters],  # parameters
                                              _type.HRESULT]
    StopAdvertising: _Callable[[],
                               _type.HRESULT]


class IGattServiceProviderAdvertisementStatusChangedEventArgs(_inspectable.IInspectable):
    get_Error: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.BluetoothError]],  # value
                         _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderAdvertisementStatus]],  # value
                          _type.HRESULT]


class IGattServiceProviderAdvertisingParameters(_inspectable.IInspectable):
    put_IsConnectable: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_IsConnectable: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_IsDiscoverable: _Callable[[_type.boolean],  # value
                                  _type.HRESULT]
    get_IsDiscoverable: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]


class IGattServiceProviderAdvertisingParameters2(_inspectable.IInspectable):
    put_ServiceData: _Callable[[_Windows_Storage_Streams.IBuffer],  # value
                               _type.HRESULT]
    get_ServiceData: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                               _type.HRESULT]


class IGattServiceProviderResult(_inspectable.IInspectable):
    get_Error: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.BluetoothError]],  # value
                         _type.HRESULT]
    get_ServiceProvider: _Callable[[_Pointer[IGattServiceProvider]],  # value
                                   _type.HRESULT]


class IGattServiceProviderStatics(_inspectable.IInspectable):
    CreateAsync: _Callable[[_struct.GUID,  # serviceUuid
                            _Pointer[_Windows_Foundation.IAsyncOperation[IGattServiceProviderResult]]],  # operation
                           _type.HRESULT]

    _factory = True


class IGattServiceUuidsStatics(_inspectable.IInspectable):
    get_Battery: _Callable[[_Pointer[_struct.GUID]],  # value
                           _type.HRESULT]
    get_BloodPressure: _Callable[[_Pointer[_struct.GUID]],  # value
                                 _type.HRESULT]
    get_CyclingSpeedAndCadence: _Callable[[_Pointer[_struct.GUID]],  # value
                                          _type.HRESULT]
    get_GenericAccess: _Callable[[_Pointer[_struct.GUID]],  # value
                                 _type.HRESULT]
    get_GenericAttribute: _Callable[[_Pointer[_struct.GUID]],  # value
                                    _type.HRESULT]
    get_Glucose: _Callable[[_Pointer[_struct.GUID]],  # value
                           _type.HRESULT]
    get_HealthThermometer: _Callable[[_Pointer[_struct.GUID]],  # value
                                     _type.HRESULT]
    get_HeartRate: _Callable[[_Pointer[_struct.GUID]],  # value
                             _type.HRESULT]
    get_RunningSpeedAndCadence: _Callable[[_Pointer[_struct.GUID]],  # value
                                          _type.HRESULT]

    _factory = True


class IGattServiceUuidsStatics2(_inspectable.IInspectable):
    get_AlertNotification: _Callable[[_Pointer[_struct.GUID]],  # value
                                     _type.HRESULT]
    get_CurrentTime: _Callable[[_Pointer[_struct.GUID]],  # value
                               _type.HRESULT]
    get_CyclingPower: _Callable[[_Pointer[_struct.GUID]],  # value
                                _type.HRESULT]
    get_DeviceInformation: _Callable[[_Pointer[_struct.GUID]],  # value
                                     _type.HRESULT]
    get_HumanInterfaceDevice: _Callable[[_Pointer[_struct.GUID]],  # value
                                        _type.HRESULT]
    get_ImmediateAlert: _Callable[[_Pointer[_struct.GUID]],  # value
                                  _type.HRESULT]
    get_LinkLoss: _Callable[[_Pointer[_struct.GUID]],  # value
                            _type.HRESULT]
    get_LocationAndNavigation: _Callable[[_Pointer[_struct.GUID]],  # value
                                         _type.HRESULT]
    get_NextDstChange: _Callable[[_Pointer[_struct.GUID]],  # value
                                 _type.HRESULT]
    get_PhoneAlertStatus: _Callable[[_Pointer[_struct.GUID]],  # value
                                    _type.HRESULT]
    get_ReferenceTimeUpdate: _Callable[[_Pointer[_struct.GUID]],  # value
                                       _type.HRESULT]
    get_ScanParameters: _Callable[[_Pointer[_struct.GUID]],  # value
                                  _type.HRESULT]
    get_TxPower: _Callable[[_Pointer[_struct.GUID]],  # value
                           _type.HRESULT]

    _factory = True


class IGattSession(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_Windows_Devices_Bluetooth.IBluetoothDeviceId]],  # value
                            _type.HRESULT]
    get_CanMaintainConnection: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_MaintainConnection: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    get_MaintainConnection: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    get_MaxPduSize: _Callable[[_Pointer[_type.UINT16]],  # value
                              _type.HRESULT]
    get_SessionStatus: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSessionStatus]],  # value
                                 _type.HRESULT]
    add_MaxPduSizeChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IGattSession, _inspectable.IInspectable],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_MaxPduSizeChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    add_SessionStatusChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IGattSession, IGattSessionStatusChangedEventArgs],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_SessionStatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]


class IGattSessionStatics(_inspectable.IInspectable):
    FromDeviceIdAsync: _Callable[[_Windows_Devices_Bluetooth.IBluetoothDeviceId,  # deviceId
                                  _Pointer[_Windows_Foundation.IAsyncOperation[IGattSession]]],  # operation
                                 _type.HRESULT]

    _factory = True


class IGattSessionStatusChangedEventArgs(_inspectable.IInspectable):
    get_Error: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.BluetoothError]],  # value
                         _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSessionStatus]],  # value
                          _type.HRESULT]


class IGattSubscribedClient(_inspectable.IInspectable):
    get_Session: _Callable[[_Pointer[IGattSession]],  # value
                           _type.HRESULT]
    get_MaxNotificationSize: _Callable[[_Pointer[_type.UINT16]],  # value
                                       _type.HRESULT]
    add_MaxNotificationSizeChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IGattSubscribedClient, _inspectable.IInspectable],  # handler
                                               _Pointer[_struct.EventRegistrationToken]],  # token
                                              _type.HRESULT]
    remove_MaxNotificationSizeChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                 _type.HRESULT]


class IGattValueChangedEventArgs(_inspectable.IInspectable):
    get_CharacteristicValue: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                       _type.HRESULT]
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # timestamp
                             _type.HRESULT]


class IGattWriteRequest(_inspectable.IInspectable):
    get_Value: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                         _type.HRESULT]
    get_Offset: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    get_Option: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteOption]],  # value
                          _type.HRESULT]
    get_State: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattRequestState]],  # value
                         _type.HRESULT]
    add_StateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IGattWriteRequest, IGattRequestStateChangedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_StateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    Respond: _Callable[[],
                       _type.HRESULT]
    RespondWithProtocolError: _Callable[[_type.BYTE],  # protocolError
                                        _type.HRESULT]


class IGattWriteRequestedEventArgs(_inspectable.IInspectable):
    get_Session: _Callable[[_Pointer[IGattSession]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]
    GetRequestAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IGattWriteRequest]]],  # operation
                               _type.HRESULT]


class IGattWriteResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus]],  # value
                          _type.HRESULT]
    get_ProtocolError: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.BYTE]]],  # value
                                 _type.HRESULT]
