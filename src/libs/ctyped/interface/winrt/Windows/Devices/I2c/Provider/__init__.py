from __future__ import annotations

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class II2cControllerProvider(_inspectable.IInspectable):
    GetDeviceProvider: _Callable[[IProviderI2cConnectionSettings,  # settings
                                  _Pointer[II2cDeviceProvider]],  # device
                                 _type.HRESULT]


class II2cDeviceProvider(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    Write: _Callable[[_type.UINT32,  # __bufferSize
                      _Pointer[_type.BYTE]],  # buffer
                     _type.HRESULT]
    WritePartial: _Callable[[_type.UINT32,  # __bufferSize
                             _Pointer[_type.BYTE],  # buffer
                             _Pointer[_struct.Windows.Devices.I2c.Provider.ProviderI2cTransferResult]],  # result
                            _type.HRESULT]
    Read: _Callable[[_type.UINT32,  # __bufferSize
                     _Pointer[_type.BYTE]],  # buffer
                    _type.HRESULT]
    ReadPartial: _Callable[[_type.UINT32,  # __bufferSize
                            _Pointer[_type.BYTE],  # buffer
                            _Pointer[_struct.Windows.Devices.I2c.Provider.ProviderI2cTransferResult]],  # result
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
                                 _Pointer[_struct.Windows.Devices.I2c.Provider.ProviderI2cTransferResult]],  # result
                                _type.HRESULT]


class II2cProvider(_inspectable.IInspectable):
    GetControllersAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[II2cControllerProvider]]]],  # operation
                                   _type.HRESULT]


class IProviderI2cConnectionSettings(_inspectable.IInspectable):
    get_SlaveAddress: _Callable[[_Pointer[_type.INT32]],  # value
                                _type.HRESULT]
    put_SlaveAddress: _Callable[[_type.INT32],  # value
                                _type.HRESULT]
    get_BusSpeed: _Callable[[_Pointer[_enum.Windows.Devices.I2c.Provider.ProviderI2cBusSpeed]],  # value
                            _type.HRESULT]
    put_BusSpeed: _Callable[[_enum.Windows.Devices.I2c.Provider.ProviderI2cBusSpeed],  # value
                            _type.HRESULT]
    get_SharingMode: _Callable[[_Pointer[_enum.Windows.Devices.I2c.Provider.ProviderI2cSharingMode]],  # value
                               _type.HRESULT]
    put_SharingMode: _Callable[[_enum.Windows.Devices.I2c.Provider.ProviderI2cSharingMode],  # value
                               _type.HRESULT]
