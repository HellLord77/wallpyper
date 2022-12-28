from __future__ import annotations as _

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IGeolocationProvider(_inspectable.IInspectable):
    get_IsOverridden: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    SetOverridePosition: _Callable[[_struct.Windows.Devices.Geolocation.BasicGeoposition,  # newPosition
                                    _enum.Windows.Devices.Geolocation.PositionSource,  # positionSource
                                    _type.DOUBLE,  # accuracyInMeters
                                    _Pointer[_enum.Windows.Devices.Geolocation.Provider.LocationOverrideStatus]],  # result
                                   _type.HRESULT]
    ClearOverridePosition: _Callable[[],
                                     _type.HRESULT]
    add_IsOverriddenChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_IsOverriddenChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
