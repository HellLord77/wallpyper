from __future__ import annotations

from typing import Callable as _Callable

from . import Provider as _Windows_Devices_Adc_Provider
from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import type as _type
from ......_utils import _Pointer


class IAdcChannel(_inspectable.IInspectable):
    get_Controller: _Callable[[_Pointer[IAdcController]],  # value
                              _type.HRESULT]
    ReadValue: _Callable[[_Pointer[_type.INT32]],  # result
                         _type.HRESULT]
    ReadRatio: _Callable[[_Pointer[_type.DOUBLE]],  # result
                         _type.HRESULT]


class IAdcController(_inspectable.IInspectable):
    get_ChannelCount: _Callable[[_Pointer[_type.INT32]],  # value
                                _type.HRESULT]
    get_ResolutionInBits: _Callable[[_Pointer[_type.INT32]],  # value
                                    _type.HRESULT]
    get_MinValue: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    get_MaxValue: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    get_ChannelMode: _Callable[[_Pointer[_enum.Windows.Devices.Adc.AdcChannelMode]],  # value
                               _type.HRESULT]
    put_ChannelMode: _Callable[[_enum.Windows.Devices.Adc.AdcChannelMode],  # value
                               _type.HRESULT]
    IsChannelModeSupported: _Callable[[_enum.Windows.Devices.Adc.AdcChannelMode,  # channelMode
                                       _Pointer[_type.boolean]],  # result
                                      _type.HRESULT]
    OpenChannel: _Callable[[_type.INT32,  # channelNumber
                            _Pointer[IAdcChannel]],  # result
                           _type.HRESULT]


class IAdcControllerStatics(_inspectable.IInspectable):
    GetControllersAsync: _Callable[[_Windows_Devices_Adc_Provider.IAdcProvider,  # provider
                                    _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IAdcController]]]],  # operation
                                   _type.HRESULT]

    _factory = True


class IAdcControllerStatics2(_inspectable.IInspectable):
    GetDefaultAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IAdcController]]],  # operation
                               _type.HRESULT]

    _factory = True
