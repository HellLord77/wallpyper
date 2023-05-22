from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IUsbBulkInEndpointDescriptor(_inspectable.IInspectable):
    get_MaxPacketSize: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    get_EndpointNumber: _Callable[[_Pointer[_type.BYTE]],  # value
                                  _type.HRESULT]
    get_Pipe: _Callable[[_Pointer[IUsbBulkInPipe]],  # value
                        _type.HRESULT]


class IUsbBulkInPipe(_inspectable.IInspectable):
    get_MaxTransferSizeBytes: _Callable[[_Pointer[_type.UINT32]],  # value
                                        _type.HRESULT]
    get_EndpointDescriptor: _Callable[[_Pointer[IUsbBulkInEndpointDescriptor]],  # value
                                      _type.HRESULT]
    ClearStallAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                               _type.HRESULT]
    put_ReadOptions: _Callable[[_enum.Windows.Devices.Usb.UsbReadOptions],  # value
                               _type.HRESULT]
    get_ReadOptions: _Callable[[_Pointer[_enum.Windows.Devices.Usb.UsbReadOptions]],  # value
                               _type.HRESULT]
    FlushBuffer: _Callable[[],
                           _type.HRESULT]
    get_InputStream: _Callable[[_Pointer[_Windows_Storage_Streams.IInputStream]],  # value
                               _type.HRESULT]


class IUsbBulkOutEndpointDescriptor(_inspectable.IInspectable):
    get_MaxPacketSize: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    get_EndpointNumber: _Callable[[_Pointer[_type.BYTE]],  # value
                                  _type.HRESULT]
    get_Pipe: _Callable[[_Pointer[IUsbBulkOutPipe]],  # value
                        _type.HRESULT]


class IUsbBulkOutPipe(_inspectable.IInspectable):
    get_EndpointDescriptor: _Callable[[_Pointer[IUsbBulkOutEndpointDescriptor]],  # value
                                      _type.HRESULT]
    ClearStallAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                               _type.HRESULT]
    put_WriteOptions: _Callable[[_enum.Windows.Devices.Usb.UsbWriteOptions],  # value
                                _type.HRESULT]
    get_WriteOptions: _Callable[[_Pointer[_enum.Windows.Devices.Usb.UsbWriteOptions]],  # value
                                _type.HRESULT]
    get_OutputStream: _Callable[[_Pointer[_Windows_Storage_Streams.IOutputStream]],  # value
                                _type.HRESULT]


class IUsbConfiguration(_inspectable.IInspectable):
    get_UsbInterfaces: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IUsbInterface]]],  # value
                                 _type.HRESULT]
    get_ConfigurationDescriptor: _Callable[[_Pointer[IUsbConfigurationDescriptor]],  # value
                                           _type.HRESULT]
    get_Descriptors: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IUsbDescriptor]]],  # value
                               _type.HRESULT]


class IUsbConfigurationDescriptor(_inspectable.IInspectable):
    get_ConfigurationValue: _Callable[[_Pointer[_type.BYTE]],  # value
                                      _type.HRESULT]
    get_MaxPowerMilliamps: _Callable[[_Pointer[_type.UINT32]],  # value
                                     _type.HRESULT]
    get_SelfPowered: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_RemoteWakeup: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]


class IUsbConfigurationDescriptorStatics(_inspectable.IInspectable, factory=True):
    TryParse: _Callable[[IUsbDescriptor,  # descriptor
                         _Pointer[IUsbConfigurationDescriptor],  # parsed
                         _Pointer[_type.boolean]],  # success
                        _type.HRESULT]
    Parse: _Callable[[IUsbDescriptor,  # descriptor
                      _Pointer[IUsbConfigurationDescriptor]],  # parsed
                     _type.HRESULT]


class IUsbControlRequestType(_inspectable.IInspectable):
    get_Direction: _Callable[[_Pointer[_enum.Windows.Devices.Usb.UsbTransferDirection]],  # value
                             _type.HRESULT]
    put_Direction: _Callable[[_enum.Windows.Devices.Usb.UsbTransferDirection],  # value
                             _type.HRESULT]
    get_ControlTransferType: _Callable[[_Pointer[_enum.Windows.Devices.Usb.UsbControlTransferType]],  # value
                                       _type.HRESULT]
    put_ControlTransferType: _Callable[[_enum.Windows.Devices.Usb.UsbControlTransferType],  # value
                                       _type.HRESULT]
    get_Recipient: _Callable[[_Pointer[_enum.Windows.Devices.Usb.UsbControlRecipient]],  # value
                             _type.HRESULT]
    put_Recipient: _Callable[[_enum.Windows.Devices.Usb.UsbControlRecipient],  # value
                             _type.HRESULT]
    get_AsByte: _Callable[[_Pointer[_type.BYTE]],  # value
                          _type.HRESULT]
    put_AsByte: _Callable[[_type.BYTE],  # value
                          _type.HRESULT]


class IUsbDescriptor(_inspectable.IInspectable):
    get_Length: _Callable[[_Pointer[_type.BYTE]],  # value
                          _type.HRESULT]
    get_DescriptorType: _Callable[[_Pointer[_type.BYTE]],  # value
                                  _type.HRESULT]
    ReadDescriptorBuffer: _Callable[[_Windows_Storage_Streams.IBuffer],  # buffer
                                    _type.HRESULT]


class IUsbDevice(_inspectable.IInspectable):
    SendControlOutTransferAsync: _Callable[[IUsbSetupPacket,  # setupPacket
                                            _Windows_Storage_Streams.IBuffer,  # buffer
                                            _Pointer[_Windows_Foundation.IAsyncOperation[_type.UINT32]]],  # operation
                                           _type.HRESULT]
    SendControlOutTransferAsyncNoBuffer: _Callable[[IUsbSetupPacket,  # setupPacket
                                                    _Pointer[_Windows_Foundation.IAsyncOperation[_type.UINT32]]],  # operation
                                                   _type.HRESULT]
    SendControlInTransferAsync: _Callable[[IUsbSetupPacket,  # setupPacket
                                           _Windows_Storage_Streams.IBuffer,  # buffer
                                           _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IBuffer]]],  # operation
                                          _type.HRESULT]
    SendControlInTransferAsyncNoBuffer: _Callable[[IUsbSetupPacket,  # setupPacket
                                                   _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IBuffer]]],  # operation
                                                  _type.HRESULT]
    get_DefaultInterface: _Callable[[_Pointer[IUsbInterface]],  # value
                                    _type.HRESULT]
    get_DeviceDescriptor: _Callable[[_Pointer[IUsbDeviceDescriptor]],  # value
                                    _type.HRESULT]
    get_Configuration: _Callable[[_Pointer[IUsbConfiguration]],  # value
                                 _type.HRESULT]


class IUsbDeviceClass(_inspectable.IInspectable):
    get_ClassCode: _Callable[[_Pointer[_type.BYTE]],  # value
                             _type.HRESULT]
    put_ClassCode: _Callable[[_type.BYTE],  # value
                             _type.HRESULT]
    get_SubclassCode: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.BYTE]]],  # value
                                _type.HRESULT]
    put_SubclassCode: _Callable[[_Windows_Foundation.IReference[_type.BYTE]],  # value
                                _type.HRESULT]
    get_ProtocolCode: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.BYTE]]],  # value
                                _type.HRESULT]
    put_ProtocolCode: _Callable[[_Windows_Foundation.IReference[_type.BYTE]],  # value
                                _type.HRESULT]


class IUsbDeviceClasses(_inspectable.IInspectable):
    pass


class IUsbDeviceClassesStatics(_inspectable.IInspectable, factory=True):
    get_CdcControl: _Callable[[_Pointer[IUsbDeviceClass]],  # value
                              _type.HRESULT]
    get_Physical: _Callable[[_Pointer[IUsbDeviceClass]],  # value
                            _type.HRESULT]
    get_PersonalHealthcare: _Callable[[_Pointer[IUsbDeviceClass]],  # value
                                      _type.HRESULT]
    get_ActiveSync: _Callable[[_Pointer[IUsbDeviceClass]],  # value
                              _type.HRESULT]
    get_PalmSync: _Callable[[_Pointer[IUsbDeviceClass]],  # value
                            _type.HRESULT]
    get_DeviceFirmwareUpdate: _Callable[[_Pointer[IUsbDeviceClass]],  # value
                                        _type.HRESULT]
    get_Irda: _Callable[[_Pointer[IUsbDeviceClass]],  # value
                        _type.HRESULT]
    get_Measurement: _Callable[[_Pointer[IUsbDeviceClass]],  # value
                               _type.HRESULT]
    get_VendorSpecific: _Callable[[_Pointer[IUsbDeviceClass]],  # value
                                  _type.HRESULT]


class IUsbDeviceDescriptor(_inspectable.IInspectable):
    get_BcdUsb: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    get_MaxPacketSize0: _Callable[[_Pointer[_type.BYTE]],  # value
                                  _type.HRESULT]
    get_VendorId: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    get_ProductId: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    get_BcdDeviceRevision: _Callable[[_Pointer[_type.UINT32]],  # value
                                     _type.HRESULT]
    get_NumberOfConfigurations: _Callable[[_Pointer[_type.BYTE]],  # value
                                          _type.HRESULT]


class IUsbDeviceStatics(_inspectable.IInspectable, factory=True):
    GetDeviceSelector: _Callable[[_type.UINT32,  # vendorId
                                  _type.UINT32,  # productId
                                  _struct.GUID,  # winUsbInterfaceClass
                                  _Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    GetDeviceSelectorGuidOnly: _Callable[[_struct.GUID,  # winUsbInterfaceClass
                                          _Pointer[_type.HSTRING]],  # value
                                         _type.HRESULT]
    GetDeviceSelectorVidPidOnly: _Callable[[_type.UINT32,  # vendorId
                                            _type.UINT32,  # productId
                                            _Pointer[_type.HSTRING]],  # value
                                           _type.HRESULT]
    GetDeviceClassSelector: _Callable[[IUsbDeviceClass,  # usbClass
                                       _Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IUsbDevice]]],  # operation
                           _type.HRESULT]


class IUsbEndpointDescriptor(_inspectable.IInspectable):
    get_EndpointNumber: _Callable[[_Pointer[_type.BYTE]],  # value
                                  _type.HRESULT]
    get_Direction: _Callable[[_Pointer[_enum.Windows.Devices.Usb.UsbTransferDirection]],  # value
                             _type.HRESULT]
    get_EndpointType: _Callable[[_Pointer[_enum.Windows.Devices.Usb.UsbEndpointType]],  # value
                                _type.HRESULT]
    get_AsBulkInEndpointDescriptor: _Callable[[_Pointer[IUsbBulkInEndpointDescriptor]],  # value
                                              _type.HRESULT]
    get_AsInterruptInEndpointDescriptor: _Callable[[_Pointer[IUsbInterruptInEndpointDescriptor]],  # value
                                                   _type.HRESULT]
    get_AsBulkOutEndpointDescriptor: _Callable[[_Pointer[IUsbBulkOutEndpointDescriptor]],  # value
                                               _type.HRESULT]
    get_AsInterruptOutEndpointDescriptor: _Callable[[_Pointer[IUsbInterruptOutEndpointDescriptor]],  # value
                                                    _type.HRESULT]


class IUsbEndpointDescriptorStatics(_inspectable.IInspectable, factory=True):
    TryParse: _Callable[[IUsbDescriptor,  # descriptor
                         _Pointer[IUsbEndpointDescriptor],  # parsed
                         _Pointer[_type.boolean]],  # success
                        _type.HRESULT]
    Parse: _Callable[[IUsbDescriptor,  # descriptor
                      _Pointer[IUsbEndpointDescriptor]],  # parsed
                     _type.HRESULT]


class IUsbInterface(_inspectable.IInspectable):
    get_BulkInPipes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IUsbBulkInPipe]]],  # value
                               _type.HRESULT]
    get_InterruptInPipes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IUsbInterruptInPipe]]],  # value
                                    _type.HRESULT]
    get_BulkOutPipes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IUsbBulkOutPipe]]],  # value
                                _type.HRESULT]
    get_InterruptOutPipes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IUsbInterruptOutPipe]]],  # value
                                     _type.HRESULT]
    get_InterfaceSettings: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IUsbInterfaceSetting]]],  # value
                                     _type.HRESULT]
    get_InterfaceNumber: _Callable[[_Pointer[_type.BYTE]],  # value
                                   _type.HRESULT]
    get_Descriptors: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IUsbDescriptor]]],  # value
                               _type.HRESULT]


class IUsbInterfaceDescriptor(_inspectable.IInspectable):
    get_ClassCode: _Callable[[_Pointer[_type.BYTE]],  # value
                             _type.HRESULT]
    get_SubclassCode: _Callable[[_Pointer[_type.BYTE]],  # value
                                _type.HRESULT]
    get_ProtocolCode: _Callable[[_Pointer[_type.BYTE]],  # value
                                _type.HRESULT]
    get_AlternateSettingNumber: _Callable[[_Pointer[_type.BYTE]],  # value
                                          _type.HRESULT]
    get_InterfaceNumber: _Callable[[_Pointer[_type.BYTE]],  # value
                                   _type.HRESULT]


class IUsbInterfaceDescriptorStatics(_inspectable.IInspectable, factory=True):
    TryParse: _Callable[[IUsbDescriptor,  # descriptor
                         _Pointer[IUsbInterfaceDescriptor],  # parsed
                         _Pointer[_type.boolean]],  # success
                        _type.HRESULT]
    Parse: _Callable[[IUsbDescriptor,  # descriptor
                      _Pointer[IUsbInterfaceDescriptor]],  # parsed
                     _type.HRESULT]


class IUsbInterfaceSetting(_inspectable.IInspectable):
    get_BulkInEndpoints: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IUsbBulkInEndpointDescriptor]]],  # value
                                   _type.HRESULT]
    get_InterruptInEndpoints: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IUsbInterruptInEndpointDescriptor]]],  # value
                                        _type.HRESULT]
    get_BulkOutEndpoints: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IUsbBulkOutEndpointDescriptor]]],  # value
                                    _type.HRESULT]
    get_InterruptOutEndpoints: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IUsbInterruptOutEndpointDescriptor]]],  # value
                                         _type.HRESULT]
    get_Selected: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    SelectSettingAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                  _type.HRESULT]
    get_InterfaceDescriptor: _Callable[[_Pointer[IUsbInterfaceDescriptor]],  # value
                                       _type.HRESULT]
    get_Descriptors: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IUsbDescriptor]]],  # value
                               _type.HRESULT]


class IUsbInterruptInEndpointDescriptor(_inspectable.IInspectable):
    get_MaxPacketSize: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    get_EndpointNumber: _Callable[[_Pointer[_type.BYTE]],  # value
                                  _type.HRESULT]
    get_Interval: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    get_Pipe: _Callable[[_Pointer[IUsbInterruptInPipe]],  # value
                        _type.HRESULT]


class IUsbInterruptInEventArgs(_inspectable.IInspectable):
    get_InterruptData: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                 _type.HRESULT]


class IUsbInterruptInPipe(_inspectable.IInspectable):
    get_EndpointDescriptor: _Callable[[_Pointer[IUsbInterruptInEndpointDescriptor]],  # value
                                      _type.HRESULT]
    ClearStallAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                               _type.HRESULT]
    add_DataReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[IUsbInterruptInPipe, IUsbInterruptInEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_DataReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]


class IUsbInterruptOutEndpointDescriptor(_inspectable.IInspectable):
    get_MaxPacketSize: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    get_EndpointNumber: _Callable[[_Pointer[_type.BYTE]],  # value
                                  _type.HRESULT]
    get_Interval: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    get_Pipe: _Callable[[_Pointer[IUsbInterruptOutPipe]],  # value
                        _type.HRESULT]


class IUsbInterruptOutPipe(_inspectable.IInspectable):
    get_EndpointDescriptor: _Callable[[_Pointer[IUsbInterruptOutEndpointDescriptor]],  # value
                                      _type.HRESULT]
    ClearStallAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                               _type.HRESULT]
    put_WriteOptions: _Callable[[_enum.Windows.Devices.Usb.UsbWriteOptions],  # value
                                _type.HRESULT]
    get_WriteOptions: _Callable[[_Pointer[_enum.Windows.Devices.Usb.UsbWriteOptions]],  # value
                                _type.HRESULT]
    get_OutputStream: _Callable[[_Pointer[_Windows_Storage_Streams.IOutputStream]],  # value
                                _type.HRESULT]


class IUsbSetupPacket(_inspectable.IInspectable):
    get_RequestType: _Callable[[_Pointer[IUsbControlRequestType]],  # value
                               _type.HRESULT]
    put_RequestType: _Callable[[IUsbControlRequestType],  # value
                               _type.HRESULT]
    get_Request: _Callable[[_Pointer[_type.BYTE]],  # value
                           _type.HRESULT]
    put_Request: _Callable[[_type.BYTE],  # value
                           _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    put_Value: _Callable[[_type.UINT32],  # value
                         _type.HRESULT]
    get_Index: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    put_Index: _Callable[[_type.UINT32],  # value
                         _type.HRESULT]
    get_Length: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    put_Length: _Callable[[_type.UINT32],  # value
                          _type.HRESULT]


class IUsbSetupPacketFactory(_inspectable.IInspectable, factory=True):
    CreateWithEightByteBuffer: _Callable[[_Windows_Storage_Streams.IBuffer,  # eightByteBuffer
                                          _Pointer[IUsbSetupPacket]],  # value
                                         _type.HRESULT]
