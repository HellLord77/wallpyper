from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IBackgroundEnergyManagerStatics(_inspectable.IInspectable):
    LowUsageLevel: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    NearMaxAcceptableUsageLevel: _Callable[[_Pointer[_type.UINT32]],  # value
                                           _type.HRESULT]
    MaxAcceptableUsageLevel: _Callable[[_Pointer[_type.UINT32]],  # value
                                       _type.HRESULT]
    ExcessiveUsageLevel: _Callable[[_Pointer[_type.UINT32]],  # value
                                   _type.HRESULT]
    NearTerminationUsageLevel: _Callable[[_Pointer[_type.UINT32]],  # value
                                         _type.HRESULT]
    TerminationUsageLevel: _Callable[[_Pointer[_type.UINT32]],  # value
                                     _type.HRESULT]
    RecentEnergyUsage: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    RecentEnergyUsageLevel: _Callable[[_Pointer[_type.UINT32]],  # value
                                      _type.HRESULT]
    RecentEnergyUsageIncreased: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    RecentEnergyUsageReturnedToLow: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]

    _factory = True


class IForegroundEnergyManagerStatics(_inspectable.IInspectable):
    LowUsageLevel: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    NearMaxAcceptableUsageLevel: _Callable[[_Pointer[_type.UINT32]],  # value
                                           _type.HRESULT]
    MaxAcceptableUsageLevel: _Callable[[_Pointer[_type.UINT32]],  # value
                                       _type.HRESULT]
    ExcessiveUsageLevel: _Callable[[_Pointer[_type.UINT32]],  # value
                                   _type.HRESULT]
    RecentEnergyUsage: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    RecentEnergyUsageLevel: _Callable[[_Pointer[_type.UINT32]],  # value
                                      _type.HRESULT]
    RecentEnergyUsageIncreased: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    RecentEnergyUsageReturnedToLow: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]

    _factory = True


class IPowerManagerStatics(_inspectable.IInspectable):
    get_EnergySaverStatus: _Callable[[_Pointer[_enum.Windows.System.Power.EnergySaverStatus]],  # value
                                     _type.HRESULT]
    add_EnergySaverStatusChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                             _Pointer[_struct.EventRegistrationToken]],  # token
                                            _type.HRESULT]
    remove_EnergySaverStatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                               _type.HRESULT]
    get_BatteryStatus: _Callable[[_Pointer[_enum.Windows.System.Power.BatteryStatus]],  # value
                                 _type.HRESULT]
    add_BatteryStatusChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_BatteryStatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    get_PowerSupplyStatus: _Callable[[_Pointer[_enum.Windows.System.Power.PowerSupplyStatus]],  # value
                                     _type.HRESULT]
    add_PowerSupplyStatusChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                             _Pointer[_struct.EventRegistrationToken]],  # token
                                            _type.HRESULT]
    remove_PowerSupplyStatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                               _type.HRESULT]
    get_RemainingChargePercent: _Callable[[_Pointer[_type.INT32]],  # value
                                          _type.HRESULT]
    add_RemainingChargePercentChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                                 _type.HRESULT]
    remove_RemainingChargePercentChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                    _type.HRESULT]
    get_RemainingDischargeTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                          _type.HRESULT]
    add_RemainingDischargeTimeChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                                 _type.HRESULT]
    remove_RemainingDischargeTimeChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                    _type.HRESULT]

    _factory = True
