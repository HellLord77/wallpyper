from __future__ import annotations as _

from typing import Callable as _Callable

from . import Provider as _Windows_Devices_Spi_Provider
from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import type as _type
from ......_utils import _Pointer


class ISpiBusInfo(_inspectable.IInspectable):
    get_ChipSelectLineCount: _Callable[[_Pointer[_type.INT32]],  # value
                                       _type.HRESULT]
    get_MinClockFrequency: _Callable[[_Pointer[_type.INT32]],  # value
                                     _type.HRESULT]
    get_MaxClockFrequency: _Callable[[_Pointer[_type.INT32]],  # value
                                     _type.HRESULT]
    get_SupportedDataBitLengths: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.INT32]]],  # value
                                           _type.HRESULT]


class ISpiConnectionSettings(_inspectable.IInspectable):
    get_ChipSelectLine: _Callable[[_Pointer[_type.INT32]],  # value
                                  _type.HRESULT]
    put_ChipSelectLine: _Callable[[_type.INT32],  # value
                                  _type.HRESULT]
    get_Mode: _Callable[[_Pointer[_enum.Windows.Devices.Spi.SpiMode]],  # value
                        _type.HRESULT]
    put_Mode: _Callable[[_enum.Windows.Devices.Spi.SpiMode],  # value
                        _type.HRESULT]
    get_DataBitLength: _Callable[[_Pointer[_type.INT32]],  # value
                                 _type.HRESULT]
    put_DataBitLength: _Callable[[_type.INT32],  # value
                                 _type.HRESULT]
    get_ClockFrequency: _Callable[[_Pointer[_type.INT32]],  # value
                                  _type.HRESULT]
    put_ClockFrequency: _Callable[[_type.INT32],  # value
                                  _type.HRESULT]
    get_SharingMode: _Callable[[_Pointer[_enum.Windows.Devices.Spi.SpiSharingMode]],  # value
                               _type.HRESULT]
    put_SharingMode: _Callable[[_enum.Windows.Devices.Spi.SpiSharingMode],  # value
                               _type.HRESULT]


class ISpiConnectionSettingsFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.INT32,  # chipSelectLine
                       _Pointer[ISpiConnectionSettings]],  # value
                      _type.HRESULT]


class ISpiController(_inspectable.IInspectable):
    GetDevice: _Callable[[ISpiConnectionSettings,  # settings
                          _Pointer[ISpiDevice]],  # device
                         _type.HRESULT]


class ISpiControllerStatics(_inspectable.IInspectable, factory=True):
    GetDefaultAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[ISpiController]]],  # operation
                               _type.HRESULT]
    GetControllersAsync: _Callable[[_Windows_Devices_Spi_Provider.ISpiProvider,  # provider
                                    _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[ISpiController]]]],  # operation
                                   _type.HRESULT]


class ISpiDevice(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_ConnectionSettings: _Callable[[_Pointer[ISpiConnectionSettings]],  # value
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


class ISpiDeviceStatics(_inspectable.IInspectable, factory=True):
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    GetDeviceSelectorFromFriendlyName: _Callable[[_type.HSTRING,  # friendlyName
                                                  _Pointer[_type.HSTRING]],  # value
                                                 _type.HRESULT]
    GetBusInfo: _Callable[[_type.HSTRING,  # busId
                           _Pointer[ISpiBusInfo]],  # busInfo
                          _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # busId
                            ISpiConnectionSettings,  # settings
                            _Pointer[_Windows_Foundation.IAsyncOperation[ISpiDevice]]],  # operation
                           _type.HRESULT]
