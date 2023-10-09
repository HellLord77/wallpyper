from __future__ import annotations as _

from typing import Callable as _Callable

from ..... import inspectable as _inspectable
from .....Windows import Foundation as _Windows_Foundation
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IPowerManagerStatics(_inspectable.IInspectable, factory=True):
    get_EnergySaverStatus: _Callable[[_Pointer[_enum.Microsoft.Windows.System.Power.EnergySaverStatus]],  # value
                                     _type.HRESULT]
    add_EnergySaverStatusChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                             _Pointer[_struct.EventRegistrationToken]],  # token
                                            _type.HRESULT]
    remove_EnergySaverStatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                               _type.HRESULT]
    get_BatteryStatus: _Callable[[_Pointer[_enum.Microsoft.Windows.System.Power.BatteryStatus]],  # value
                                 _type.HRESULT]
    add_BatteryStatusChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_BatteryStatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    get_PowerSupplyStatus: _Callable[[_Pointer[_enum.Microsoft.Windows.System.Power.PowerSupplyStatus]],  # value
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
    get_PowerSourceKind: _Callable[[_Pointer[_enum.Microsoft.Windows.System.Power.PowerSourceKind]],  # value
                                   _type.HRESULT]
    add_PowerSourceKindChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_PowerSourceKindChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]
    get_DisplayStatus: _Callable[[_Pointer[_enum.Microsoft.Windows.System.Power.DisplayStatus]],  # value
                                 _type.HRESULT]
    add_DisplayStatusChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_DisplayStatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    add_SystemIdleStatusChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_SystemIdleStatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]
    get_EffectivePowerMode: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Microsoft.Windows.System.Power.EffectivePowerMode]]],  # value
                                      _type.HRESULT]
    add_EffectivePowerModeChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                              _Pointer[_struct.EventRegistrationToken]],  # token
                                             _type.HRESULT]
    remove_EffectivePowerModeChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                _type.HRESULT]
    get_UserPresenceStatus: _Callable[[_Pointer[_enum.Microsoft.Windows.System.Power.UserPresenceStatus]],  # value
                                      _type.HRESULT]
    add_UserPresenceStatusChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                              _Pointer[_struct.EventRegistrationToken]],  # token
                                             _type.HRESULT]
    remove_UserPresenceStatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                _type.HRESULT]
    get_SystemSuspendStatus: _Callable[[_Pointer[_enum.Microsoft.Windows.System.Power.SystemSuspendStatus]],  # value
                                       _type.HRESULT]
    add_SystemSuspendStatusChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                               _Pointer[_struct.EventRegistrationToken]],  # token
                                              _type.HRESULT]
    remove_SystemSuspendStatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                 _type.HRESULT]


class IPowerManagerStatics2(_inspectable.IInspectable, factory=True):
    get_EffectivePowerMode2: _Callable[[_Pointer[_enum.Microsoft.Windows.System.Power.EffectivePowerMode]],  # value
                                       _type.HRESULT]
