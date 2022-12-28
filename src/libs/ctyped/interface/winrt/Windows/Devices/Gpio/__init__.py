from __future__ import annotations as _

from typing import Callable as _Callable

from . import Provider as _Windows_Devices_Gpio_Provider
from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IGpioChangeCounter(_inspectable.IInspectable):
    put_Polarity: _Callable[[_enum.Windows.Devices.Gpio.GpioChangePolarity],  # value
                            _type.HRESULT]
    get_Polarity: _Callable[[_Pointer[_enum.Windows.Devices.Gpio.GpioChangePolarity]],  # value
                            _type.HRESULT]
    get_IsStarted: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    Read: _Callable[[_Pointer[_struct.Windows.Devices.Gpio.GpioChangeCount]],  # value
                    _type.HRESULT]
    Reset: _Callable[[_Pointer[_struct.Windows.Devices.Gpio.GpioChangeCount]],  # value
                     _type.HRESULT]


class IGpioChangeCounterFactory(_inspectable.IInspectable):
    Create: _Callable[[IGpioPin,  # pin
                       _Pointer[IGpioChangeCounter]],  # value
                      _type.HRESULT]

    _factory = True


class IGpioChangeReader(_inspectable.IInspectable):
    get_Capacity: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    get_Length: _Callable[[_Pointer[_type.INT32]],  # value
                          _type.HRESULT]
    get_IsEmpty: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_IsOverflowed: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_Polarity: _Callable[[_enum.Windows.Devices.Gpio.GpioChangePolarity],  # value
                            _type.HRESULT]
    get_Polarity: _Callable[[_Pointer[_enum.Windows.Devices.Gpio.GpioChangePolarity]],  # value
                            _type.HRESULT]
    get_IsStarted: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    Clear: _Callable[[],
                     _type.HRESULT]
    GetNextItem: _Callable[[_Pointer[_struct.Windows.Devices.Gpio.GpioChangeRecord]],  # value
                           _type.HRESULT]
    PeekNextItem: _Callable[[_Pointer[_struct.Windows.Devices.Gpio.GpioChangeRecord]],  # value
                            _type.HRESULT]
    GetAllItems: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_struct.Windows.Devices.Gpio.GpioChangeRecord]]],  # value
                           _type.HRESULT]
    WaitForItemsAsync: _Callable[[_type.INT32,  # count
                                  _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                 _type.HRESULT]


class IGpioChangeReaderFactory(_inspectable.IInspectable):
    Create: _Callable[[IGpioPin,  # pin
                       _Pointer[IGpioChangeReader]],  # value
                      _type.HRESULT]
    CreateWithCapacity: _Callable[[IGpioPin,  # pin
                                   _type.INT32,  # minCapacity
                                   _Pointer[IGpioChangeReader]],  # value
                                  _type.HRESULT]

    _factory = True


class IGpioController(_inspectable.IInspectable):
    get_PinCount: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    OpenPin: _Callable[[_type.INT32,  # pinNumber
                        _Pointer[IGpioPin]],  # pin
                       _type.HRESULT]
    OpenPinWithSharingMode: _Callable[[_type.INT32,  # pinNumber
                                       _enum.Windows.Devices.Gpio.GpioSharingMode,  # sharingMode
                                       _Pointer[IGpioPin]],  # pin
                                      _type.HRESULT]
    TryOpenPin: _Callable[[_type.INT32,  # pinNumber
                           _enum.Windows.Devices.Gpio.GpioSharingMode,  # sharingMode
                           _Pointer[IGpioPin],  # pin
                           _Pointer[_enum.Windows.Devices.Gpio.GpioOpenStatus],  # openStatus
                           _Pointer[_type.boolean]],  # succeeded
                          _type.HRESULT]


class IGpioControllerStatics(_inspectable.IInspectable):
    GetDefault: _Callable[[_Pointer[IGpioController]],  # value
                          _type.HRESULT]

    _factory = True


class IGpioControllerStatics2(_inspectable.IInspectable):
    GetControllersAsync: _Callable[[_Windows_Devices_Gpio_Provider.IGpioProvider,  # provider
                                    _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IGpioController]]]],  # operation
                                   _type.HRESULT]
    GetDefaultAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IGpioController]]],  # operation
                               _type.HRESULT]

    _factory = True


class IGpioPin(_inspectable.IInspectable):
    add_ValueChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IGpioPin, IGpioPinValueChangedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_ValueChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    get_DebounceTimeout: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                   _type.HRESULT]
    put_DebounceTimeout: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                   _type.HRESULT]
    get_PinNumber: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]
    get_SharingMode: _Callable[[_Pointer[_enum.Windows.Devices.Gpio.GpioSharingMode]],  # value
                               _type.HRESULT]
    IsDriveModeSupported: _Callable[[_enum.Windows.Devices.Gpio.GpioPinDriveMode,  # driveMode
                                     _Pointer[_type.boolean]],  # supported
                                    _type.HRESULT]
    GetDriveMode: _Callable[[_Pointer[_enum.Windows.Devices.Gpio.GpioPinDriveMode]],  # value
                            _type.HRESULT]
    SetDriveMode: _Callable[[_enum.Windows.Devices.Gpio.GpioPinDriveMode],  # value
                            _type.HRESULT]
    Write: _Callable[[_enum.Windows.Devices.Gpio.GpioPinValue],  # value
                     _type.HRESULT]
    Read: _Callable[[_Pointer[_enum.Windows.Devices.Gpio.GpioPinValue]],  # value
                    _type.HRESULT]


class IGpioPinValueChangedEventArgs(_inspectable.IInspectable):
    get_Edge: _Callable[[_Pointer[_enum.Windows.Devices.Gpio.GpioPinEdge]],  # value
                        _type.HRESULT]
