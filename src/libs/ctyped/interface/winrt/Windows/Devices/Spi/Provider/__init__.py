from __future__ import annotations

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import type as _type
from ......._utils import _Pointer


class IProviderSpiConnectionSettings(_inspectable.IInspectable):
    get_ChipSelectLine: _Callable[[_Pointer[_type.INT32]],  # value
                                  _type.HRESULT]
    put_ChipSelectLine: _Callable[[_type.INT32],  # value
                                  _type.HRESULT]
    get_Mode: _Callable[[_Pointer[_enum.Windows.Devices.Spi.Provider.ProviderSpiMode]],  # value
                        _type.HRESULT]
    put_Mode: _Callable[[_enum.Windows.Devices.Spi.Provider.ProviderSpiMode],  # value
                        _type.HRESULT]
    get_DataBitLength: _Callable[[_Pointer[_type.INT32]],  # value
                                 _type.HRESULT]
    put_DataBitLength: _Callable[[_type.INT32],  # value
                                 _type.HRESULT]
    get_ClockFrequency: _Callable[[_Pointer[_type.INT32]],  # value
                                  _type.HRESULT]
    put_ClockFrequency: _Callable[[_type.INT32],  # value
                                  _type.HRESULT]
    get_SharingMode: _Callable[[_Pointer[_enum.Windows.Devices.Spi.Provider.ProviderSpiSharingMode]],  # value
                               _type.HRESULT]
    put_SharingMode: _Callable[[_enum.Windows.Devices.Spi.Provider.ProviderSpiSharingMode],  # value
                               _type.HRESULT]


class IProviderSpiConnectionSettingsFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.INT32,  # chipSelectLine
                       _Pointer[IProviderSpiConnectionSettings]],  # value
                      _type.HRESULT]


class ISpiControllerProvider(_inspectable.IInspectable):
    GetDeviceProvider: _Callable[[IProviderSpiConnectionSettings,  # settings
                                  _Pointer[ISpiDeviceProvider]],  # result
                                 _type.HRESULT]


class ISpiDeviceProvider(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_ConnectionSettings: _Callable[[_Pointer[IProviderSpiConnectionSettings]],  # value
                                      _type.HRESULT]
    Write: _Callable[[_type.UINT32,  # __bufferSize
                      _Pointer[_type.BYTE]],  # buffer
                     _type.HRESULT]
    Read: _Callable[[_type.UINT32,  # __bufferSize
                     _Pointer[_type.BYTE]],  # buffer
                    _type.HRESULT]
    TransferSequential: _Callable[[_type.UINT32,  # __writeBufferSize
                                   _Pointer[_type.BYTE],  # writeBuffer
                                   _type.UINT32,  # __readBufferSize
                                   _Pointer[_type.BYTE]],  # readBuffer
                                  _type.HRESULT]
    TransferFullDuplex: _Callable[[_type.UINT32,  # __writeBufferSize
                                   _Pointer[_type.BYTE],  # writeBuffer
                                   _type.UINT32,  # __readBufferSize
                                   _Pointer[_type.BYTE]],  # readBuffer
                                  _type.HRESULT]


class ISpiProvider(_inspectable.IInspectable):
    GetControllersAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[ISpiControllerProvider]]]],  # result
                                   _type.HRESULT]
