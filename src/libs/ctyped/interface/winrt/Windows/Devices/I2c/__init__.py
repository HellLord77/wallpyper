from __future__ import annotations

from typing import Callable as _Callable

from . import Provider as _Windows_Devices_I2c_Provider
from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class II2cConnectionSettings(_inspectable.IInspectable):
    get_SlaveAddress: _Callable[[_Pointer[_type.INT32]],  # value
                                _type.HRESULT]
    put_SlaveAddress: _Callable[[_type.INT32],  # value
                                _type.HRESULT]
    get_BusSpeed: _Callable[[_Pointer[_enum.Windows.Devices.I2c.I2cBusSpeed]],  # value
                            _type.HRESULT]
    put_BusSpeed: _Callable[[_enum.Windows.Devices.I2c.I2cBusSpeed],  # value
                            _type.HRESULT]
    get_SharingMode: _Callable[[_Pointer[_enum.Windows.Devices.I2c.I2cSharingMode]],  # value
                               _type.HRESULT]
    put_SharingMode: _Callable[[_enum.Windows.Devices.I2c.I2cSharingMode],  # value
                               _type.HRESULT]


class II2cConnectionSettingsFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.INT32,  # slaveAddress
                       _Pointer[II2cConnectionSettings]],  # value
                      _type.HRESULT]

    _factory = True


class II2cController(_inspectable.IInspectable):
    GetDevice: _Callable[[II2cConnectionSettings,  # settings
                          _Pointer[II2cDevice]],  # device
                         _type.HRESULT]


class II2cControllerStatics(_inspectable.IInspectable):
    GetControllersAsync: _Callable[[_Windows_Devices_I2c_Provider.II2cProvider,  # provider
                                    _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[II2cController]]]],  # operation
                                   _type.HRESULT]
    GetDefaultAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[II2cController]]],  # operation
                               _type.HRESULT]

    _factory = True


class II2cDevice(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_ConnectionSettings: _Callable[[_Pointer[II2cConnectionSettings]],  # value
                                      _type.HRESULT]
    Write: _Callable[[_type.UINT32,  # __bufferSize
                      _Pointer[_type.BYTE]],  # buffer
                     _type.HRESULT]
    WritePartial: _Callable[[_type.UINT32,  # __bufferSize
                             _Pointer[_type.BYTE],  # buffer
                             _Pointer[_struct.Windows.Devices.I2c.I2cTransferResult]],  # result
                            _type.HRESULT]
    Read: _Callable[[_type.UINT32,  # __bufferSize
                     _Pointer[_type.BYTE]],  # buffer
                    _type.HRESULT]
    ReadPartial: _Callable[[_type.UINT32,  # __bufferSize
                            _Pointer[_type.BYTE],  # buffer
                            _Pointer[_struct.Windows.Devices.I2c.I2cTransferResult]],  # result
                           _type.HRESULT]
    WriteRead: _Callable[[_type.UINT32,  # __writeBufferSize
                          _Pointer[_type.BYTE],  # writeBuffer
                          _type.UINT32,  # __readBufferSize
                          _Pointer[_type.BYTE]],  # readBuffer
                         _type.HRESULT]
    WriteReadPartial: _Callable[[_type.UINT32,  # __writeBufferSize
                                 _Pointer[_type.BYTE],  # writeBuffer
                                 _type.UINT32,  # __readBufferSize
                                 _Pointer[_type.BYTE],  # readBuffer
                                 _Pointer[_struct.Windows.Devices.I2c.I2cTransferResult]],  # result
                                _type.HRESULT]


class II2cDeviceStatics(_inspectable.IInspectable):
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    GetDeviceSelectorFromFriendlyName: _Callable[[_type.HSTRING,  # friendlyName
                                                  _Pointer[_type.HSTRING]],  # value
                                                 _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            II2cConnectionSettings,  # settings
                            _Pointer[_Windows_Foundation.IAsyncOperation[II2cDevice]]],  # operation
                           _type.HRESULT]

    _factory = True
