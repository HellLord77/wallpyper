from __future__ import annotations as _

from typing import Callable as _Callable

from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import type as _type
from ......._utils import _Pointer


class IPwmControllerProvider(_inspectable.IInspectable):
    get_PinCount: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    get_ActualFrequency: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                   _type.HRESULT]
    SetDesiredFrequency: _Callable[[_type.DOUBLE,  # frequency
                                    _Pointer[_type.DOUBLE]],  # result
                                   _type.HRESULT]
    get_MaxFrequency: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    get_MinFrequency: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    AcquirePin: _Callable[[_type.INT32],  # pin
                          _type.HRESULT]
    ReleasePin: _Callable[[_type.INT32],  # pin
                          _type.HRESULT]
    EnablePin: _Callable[[_type.INT32],  # pin
                         _type.HRESULT]
    DisablePin: _Callable[[_type.INT32],  # pin
                          _type.HRESULT]
    SetPulseParameters: _Callable[[_type.INT32,  # pin
                                   _type.DOUBLE,  # dutyCycle
                                   _type.boolean],  # invertPolarity
                                  _type.HRESULT]


class IPwmProvider(_inspectable.IInspectable):
    GetControllers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IPwmControllerProvider]]],  # result
                              _type.HRESULT]
