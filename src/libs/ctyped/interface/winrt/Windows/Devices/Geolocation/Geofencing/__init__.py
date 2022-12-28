from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Geolocation as _Windows_Devices_Geolocation
from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IGeofence(_inspectable.IInspectable):
    get_StartTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_Duration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    get_DwellTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                             _type.HRESULT]
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_MonitoredStates: _Callable[[_Pointer[_enum.Windows.Devices.Geolocation.Geofencing.MonitoredGeofenceStates]],  # value
                                   _type.HRESULT]
    get_Geoshape: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeoshape]],  # value
                            _type.HRESULT]
    get_SingleUse: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]


class IGeofenceFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.HSTRING,  # id
                       _Windows_Devices_Geolocation.IGeoshape,  # geoshape
                       _Pointer[IGeofence]],  # geofence
                      _type.HRESULT]
    CreateWithMonitorStates: _Callable[[_type.HSTRING,  # id
                                        _Windows_Devices_Geolocation.IGeoshape,  # geoshape
                                        _enum.Windows.Devices.Geolocation.Geofencing.MonitoredGeofenceStates,  # monitoredStates
                                        _type.boolean,  # singleUse
                                        _Pointer[IGeofence]],  # geofence
                                       _type.HRESULT]
    CreateWithMonitorStatesAndDwellTime: _Callable[[_type.HSTRING,  # id
                                                    _Windows_Devices_Geolocation.IGeoshape,  # geoshape
                                                    _enum.Windows.Devices.Geolocation.Geofencing.MonitoredGeofenceStates,  # monitoredStates
                                                    _type.boolean,  # singleUse
                                                    _struct.Windows.Foundation.TimeSpan,  # dwellTime
                                                    _Pointer[IGeofence]],  # geofence
                                                   _type.HRESULT]
    CreateWithMonitorStatesDwellTimeStartTimeAndDuration: _Callable[[_type.HSTRING,  # id
                                                                     _Windows_Devices_Geolocation.IGeoshape,  # geoshape
                                                                     _enum.Windows.Devices.Geolocation.Geofencing.MonitoredGeofenceStates,  # monitoredStates
                                                                     _type.boolean,  # singleUse
                                                                     _struct.Windows.Foundation.TimeSpan,  # dwellTime
                                                                     _struct.Windows.Foundation.DateTime,  # startTime
                                                                     _struct.Windows.Foundation.TimeSpan,  # duration
                                                                     _Pointer[IGeofence]],  # geofence
                                                                    _type.HRESULT]

    _factory = True


class IGeofenceMonitor(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Devices.Geolocation.Geofencing.GeofenceMonitorStatus]],  # value
                          _type.HRESULT]
    get_Geofences: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IGeofence]]],  # value
                             _type.HRESULT]
    get_LastKnownGeoposition: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeoposition]],  # value
                                        _type.HRESULT]
    add_GeofenceStateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IGeofenceMonitor, _inspectable.IInspectable],  # eventHandler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_GeofenceStateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    ReadReports: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IGeofenceStateChangeReport]]],  # value
                           _type.HRESULT]
    add_StatusChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IGeofenceMonitor, _inspectable.IInspectable],  # eventHandler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_StatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]


class IGeofenceMonitorStatics(_inspectable.IInspectable):
    get_Current: _Callable[[_Pointer[IGeofenceMonitor]],  # value
                           _type.HRESULT]

    _factory = True


class IGeofenceStateChangeReport(_inspectable.IInspectable):
    get_NewState: _Callable[[_Pointer[_enum.Windows.Devices.Geolocation.Geofencing.GeofenceState]],  # value
                            _type.HRESULT]
    get_Geofence: _Callable[[_Pointer[IGeofence]],  # value
                            _type.HRESULT]
    get_Geoposition: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeoposition]],  # value
                               _type.HRESULT]
    get_RemovalReason: _Callable[[_Pointer[_enum.Windows.Devices.Geolocation.Geofencing.GeofenceRemovalReason]],  # value
                                 _type.HRESULT]
