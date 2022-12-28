from __future__ import annotations as _

from typing import Callable as _Callable

from ..... import inspectable as _inspectable
from ....... import type as _type
from ......._utils import _Pointer


class IBackgroundEnergyDiagnosticsStatics(_inspectable.IInspectable):
    DeviceSpecificConversionFactor: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                              _type.HRESULT]
    ComputeTotalEnergyUsage: _Callable[[_Pointer[_type.UINT64]],  # value
                                       _type.HRESULT]
    ResetTotalEnergyUsage: _Callable[[],
                                     _type.HRESULT]

    _factory = True


class IForegroundEnergyDiagnosticsStatics(_inspectable.IInspectable):
    DeviceSpecificConversionFactor: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                              _type.HRESULT]
    ComputeTotalEnergyUsage: _Callable[[_Pointer[_type.UINT64]],  # value
                                       _type.HRESULT]
    ResetTotalEnergyUsage: _Callable[[],
                                     _type.HRESULT]

    _factory = True
