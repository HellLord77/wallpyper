from __future__ import annotations

from typing import Callable as _Callable

from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import type as _type
from ......._utils import _Pointer


class IAdcControllerProvider(_inspectable.IInspectable):
    get_ChannelCount: _Callable[[_Pointer[_type.INT32]],  # value
                                _type.HRESULT]
    get_ResolutionInBits: _Callable[[_Pointer[_type.INT32]],  # value
                                    _type.HRESULT]
    get_MinValue: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    get_MaxValue: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    get_ChannelMode: _Callable[[_Pointer[_enum.Windows.Devices.Adc.Provider.ProviderAdcChannelMode]],  # value
                               _type.HRESULT]
    put_ChannelMode: _Callable[[_enum.Windows.Devices.Adc.Provider.ProviderAdcChannelMode],  # value
                               _type.HRESULT]
    IsChannelModeSupported: _Callable[[_enum.Windows.Devices.Adc.Provider.ProviderAdcChannelMode,  # channelMode
                                       _Pointer[_type.boolean]],  # result
                                      _type.HRESULT]
    AcquireChannel: _Callable[[_type.INT32],  # channel
                              _type.HRESULT]
    ReleaseChannel: _Callable[[_type.INT32],  # channel
                              _type.HRESULT]
    ReadValue: _Callable[[_type.INT32,  # channelNumber
                          _Pointer[_type.INT32]],  # result
                         _type.HRESULT]


class IAdcProvider(_inspectable.IInspectable):
    GetControllers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IAdcControllerProvider]]],  # result
                              _type.HRESULT]
