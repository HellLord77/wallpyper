from __future__ import annotations

from typing import Callable as _Callable

from . import Provider as _Windows_Devices_Pwm_Provider
from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import type as _type
from ......_utils import _Pointer


class IPwmController(_inspectable.IInspectable):
    get_PinCount: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    get_ActualFrequency: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                   _type.HRESULT]
    SetDesiredFrequency: _Callable[[_type.DOUBLE,  # desiredFrequency
                                    _Pointer[_type.DOUBLE]],  # result
                                   _type.HRESULT]
    get_MinFrequency: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    get_MaxFrequency: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    OpenPin: _Callable[[_type.INT32,  # pinNumber
                        _Pointer[IPwmPin]],  # pin
                       _type.HRESULT]


class IPwmControllerStatics(_inspectable.IInspectable, factory=True):
    GetControllersAsync: _Callable[[_Windows_Devices_Pwm_Provider.IPwmProvider,  # provider
                                    _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IPwmController]]]],  # operation
                                   _type.HRESULT]


class IPwmControllerStatics2(_inspectable.IInspectable, factory=True):
    GetDefaultAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IPwmController]]],  # operation
                               _type.HRESULT]


class IPwmControllerStatics3(_inspectable.IInspectable, factory=True):
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]
    GetDeviceSelectorFromFriendlyName: _Callable[[_type.HSTRING,  # friendlyName
                                                  _Pointer[_type.HSTRING]],  # result
                                                 _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IPwmController]]],  # operation
                           _type.HRESULT]


class IPwmPin(_inspectable.IInspectable):
    get_Controller: _Callable[[_Pointer[IPwmController]],  # value
                              _type.HRESULT]
    GetActiveDutyCyclePercentage: _Callable[[_Pointer[_type.DOUBLE]],  # result
                                            _type.HRESULT]
    SetActiveDutyCyclePercentage: _Callable[[_type.DOUBLE],  # dutyCyclePercentage
                                            _type.HRESULT]
    get_Polarity: _Callable[[_Pointer[_enum.Windows.Devices.Pwm.PwmPulsePolarity]],  # value
                            _type.HRESULT]
    put_Polarity: _Callable[[_enum.Windows.Devices.Pwm.PwmPulsePolarity],  # value
                            _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    get_IsStarted: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
