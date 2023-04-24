from __future__ import annotations

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IGpioControllerProvider(_inspectable.IInspectable):
    get_PinCount: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    OpenPinProvider: _Callable[[_type.INT32,  # pin
                                _enum.Windows.Devices.Gpio.Provider.ProviderGpioSharingMode,  # sharingMode
                                _Pointer[IGpioPinProvider]],  # gpioPinProvider
                               _type.HRESULT]


class IGpioPinProvider(_inspectable.IInspectable):
    add_ValueChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IGpioPinProvider, IGpioPinProviderValueChangedEventArgs],  # handler
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
    get_SharingMode: _Callable[[_Pointer[_enum.Windows.Devices.Gpio.Provider.ProviderGpioSharingMode]],  # value
                               _type.HRESULT]
    IsDriveModeSupported: _Callable[[_enum.Windows.Devices.Gpio.Provider.ProviderGpioPinDriveMode,  # driveMode
                                     _Pointer[_type.boolean]],  # supported
                                    _type.HRESULT]
    GetDriveMode: _Callable[[_Pointer[_enum.Windows.Devices.Gpio.Provider.ProviderGpioPinDriveMode]],  # value
                            _type.HRESULT]
    SetDriveMode: _Callable[[_enum.Windows.Devices.Gpio.Provider.ProviderGpioPinDriveMode],  # value
                            _type.HRESULT]
    Write: _Callable[[_enum.Windows.Devices.Gpio.Provider.ProviderGpioPinValue],  # value
                     _type.HRESULT]
    Read: _Callable[[_Pointer[_enum.Windows.Devices.Gpio.Provider.ProviderGpioPinValue]],  # value
                    _type.HRESULT]


class IGpioPinProviderValueChangedEventArgs(_inspectable.IInspectable):
    get_Edge: _Callable[[_Pointer[_enum.Windows.Devices.Gpio.Provider.ProviderGpioPinEdge]],  # value
                        _type.HRESULT]


class IGpioPinProviderValueChangedEventArgsFactory(_inspectable.IInspectable):
    Create: _Callable[[_enum.Windows.Devices.Gpio.Provider.ProviderGpioPinEdge,  # edge
                       _Pointer[IGpioPinProviderValueChangedEventArgs]],  # value
                      _type.HRESULT]

    _factory = True


class IGpioProvider(_inspectable.IInspectable):
    GetControllers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IGpioControllerProvider]]],  # result
                              _type.HRESULT]
