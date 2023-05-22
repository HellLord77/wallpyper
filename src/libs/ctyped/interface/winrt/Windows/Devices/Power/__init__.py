from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IBattery(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    GetReport: _Callable[[_Pointer[IBatteryReport]],  # result
                         _type.HRESULT]
    add_ReportUpdated: _Callable[[_Windows_Foundation.ITypedEventHandler[IBattery, _inspectable.IInspectable],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_ReportUpdated: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]


class IBatteryReport(_inspectable.IInspectable):
    get_ChargeRateInMilliwatts: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                          _type.HRESULT]
    get_DesignCapacityInMilliwattHours: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                                  _type.HRESULT]
    get_FullChargeCapacityInMilliwattHours: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                                      _type.HRESULT]
    get_RemainingCapacityInMilliwattHours: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                                     _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.System.Power.BatteryStatus]],  # value
                          _type.HRESULT]


class IBatteryStatics(_inspectable.IInspectable, factory=True):
    get_AggregateBattery: _Callable[[_Pointer[IBattery]],  # result
                                    _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IBattery]]],  # result
                           _type.HRESULT]
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]
