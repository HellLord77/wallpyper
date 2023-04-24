from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IErrorReceivedEventArgs(_inspectable.IInspectable):
    get_Error: _Callable[[_Pointer[_enum.Windows.Devices.SerialCommunication.SerialError]],  # value
                         _type.HRESULT]


class IPinChangedEventArgs(_inspectable.IInspectable):
    get_PinChange: _Callable[[_Pointer[_enum.Windows.Devices.SerialCommunication.SerialPinChange]],  # value
                             _type.HRESULT]


class ISerialDevice(_inspectable.IInspectable):
    get_BaudRate: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    put_BaudRate: _Callable[[_type.UINT32],  # value
                            _type.HRESULT]
    get_BreakSignalState: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_BreakSignalState: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_BytesReceived: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    get_CarrierDetectState: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    get_ClearToSendState: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_DataBits: _Callable[[_Pointer[_type.UINT16]],  # value
                            _type.HRESULT]
    put_DataBits: _Callable[[_type.UINT16],  # value
                            _type.HRESULT]
    get_DataSetReadyState: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    get_Handshake: _Callable[[_Pointer[_enum.Windows.Devices.SerialCommunication.SerialHandshake]],  # value
                             _type.HRESULT]
    put_Handshake: _Callable[[_enum.Windows.Devices.SerialCommunication.SerialHandshake],  # value
                             _type.HRESULT]
    get_IsDataTerminalReadyEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]
    put_IsDataTerminalReadyEnabled: _Callable[[_type.boolean],  # value
                                              _type.HRESULT]
    get_IsRequestToSendEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_IsRequestToSendEnabled: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    get_Parity: _Callable[[_Pointer[_enum.Windows.Devices.SerialCommunication.SerialParity]],  # value
                          _type.HRESULT]
    put_Parity: _Callable[[_enum.Windows.Devices.SerialCommunication.SerialParity],  # value
                          _type.HRESULT]
    get_PortName: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_ReadTimeout: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                               _type.HRESULT]
    put_ReadTimeout: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                               _type.HRESULT]
    get_StopBits: _Callable[[_Pointer[_enum.Windows.Devices.SerialCommunication.SerialStopBitCount]],  # value
                            _type.HRESULT]
    put_StopBits: _Callable[[_enum.Windows.Devices.SerialCommunication.SerialStopBitCount],  # value
                            _type.HRESULT]
    get_UsbVendorId: _Callable[[_Pointer[_type.UINT16]],  # value
                               _type.HRESULT]
    get_UsbProductId: _Callable[[_Pointer[_type.UINT16]],  # value
                                _type.HRESULT]
    get_WriteTimeout: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                _type.HRESULT]
    put_WriteTimeout: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                _type.HRESULT]
    get_InputStream: _Callable[[_Pointer[_Windows_Storage_Streams.IInputStream]],  # value
                               _type.HRESULT]
    get_OutputStream: _Callable[[_Pointer[_Windows_Storage_Streams.IOutputStream]],  # value
                                _type.HRESULT]
    add_ErrorReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[ISerialDevice, IErrorReceivedEventArgs],  # reportHandler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_ErrorReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_PinChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ISerialDevice, IPinChangedEventArgs],  # reportHandler
                               _Pointer[_struct.EventRegistrationToken]],  # token
                              _type.HRESULT]
    remove_PinChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                 _type.HRESULT]


class ISerialDeviceStatics(_inspectable.IInspectable):
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    GetDeviceSelectorFromPortName: _Callable[[_type.HSTRING,  # portName
                                              _Pointer[_type.HSTRING]],  # result
                                             _type.HRESULT]
    GetDeviceSelectorFromUsbVidPid: _Callable[[_type.UINT16,  # vendorId
                                               _type.UINT16,  # productId
                                               _Pointer[_type.HSTRING]],  # result
                                              _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[ISerialDevice]]],  # result
                           _type.HRESULT]

    _factory = True
