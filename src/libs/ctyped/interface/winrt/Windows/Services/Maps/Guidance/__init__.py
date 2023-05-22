from __future__ import annotations

from typing import Callable as _Callable

from ... import Maps as _Windows_Services_Maps
from .... import Foundation as _Windows_Foundation
from ....Devices import Geolocation as _Windows_Devices_Geolocation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IGuidanceAudioNotificationRequestedEventArgs(_inspectable.IInspectable):
    get_AudioNotification: _Callable[[_Pointer[_enum.Windows.Services.Maps.Guidance.GuidanceAudioNotificationKind]],  # value
                                     _type.HRESULT]
    get_AudioFilePaths: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                  _type.HRESULT]
    get_AudioText: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]


class IGuidanceLaneInfo(_inspectable.IInspectable):
    get_LaneMarkers: _Callable[[_Pointer[_enum.Windows.Services.Maps.Guidance.GuidanceLaneMarkers]],  # value
                               _type.HRESULT]
    get_IsOnRoute: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]


class IGuidanceManeuver(_inspectable.IInspectable):
    get_StartLocation: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeopoint]],  # value
                                 _type.HRESULT]
    get_DistanceFromRouteStart: _Callable[[_Pointer[_type.INT32]],  # value
                                          _type.HRESULT]
    get_DistanceFromPreviousManeuver: _Callable[[_Pointer[_type.INT32]],  # value
                                                _type.HRESULT]
    get_DepartureRoadName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    get_NextRoadName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_DepartureShortRoadName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                          _type.HRESULT]
    get_NextShortRoadName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    get_Kind: _Callable[[_Pointer[_enum.Windows.Services.Maps.Guidance.GuidanceManeuverKind]],  # value
                        _type.HRESULT]
    get_StartAngle: _Callable[[_Pointer[_type.INT32]],  # value
                              _type.HRESULT]
    get_EndAngle: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    get_RoadSignpost: _Callable[[_Pointer[IGuidanceRoadSignpost]],  # value
                                _type.HRESULT]
    get_InstructionText: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]


class IGuidanceMapMatchedCoordinate(_inspectable.IInspectable):
    get_Location: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeopoint]],  # value
                            _type.HRESULT]
    get_CurrentHeading: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    get_CurrentSpeed: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    get_IsOnStreet: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_Road: _Callable[[_Pointer[IGuidanceRoadSegment]],  # value
                        _type.HRESULT]


class IGuidanceNavigator(_inspectable.IInspectable):
    StartNavigating: _Callable[[IGuidanceRoute],  # route
                               _type.HRESULT]
    StartSimulating: _Callable[[IGuidanceRoute,  # route
                                _type.INT32],  # speedInMetersPerSecond
                               _type.HRESULT]
    StartTracking: _Callable[[],
                             _type.HRESULT]
    Pause: _Callable[[],
                     _type.HRESULT]
    Resume: _Callable[[],
                      _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    RepeatLastAudioNotification: _Callable[[],
                                           _type.HRESULT]
    get_AudioMeasurementSystem: _Callable[[_Pointer[_enum.Windows.Services.Maps.Guidance.GuidanceAudioMeasurementSystem]],  # value
                                          _type.HRESULT]
    put_AudioMeasurementSystem: _Callable[[_enum.Windows.Services.Maps.Guidance.GuidanceAudioMeasurementSystem],  # value
                                          _type.HRESULT]
    get_AudioNotifications: _Callable[[_Pointer[_enum.Windows.Services.Maps.Guidance.GuidanceAudioNotifications]],  # value
                                      _type.HRESULT]
    put_AudioNotifications: _Callable[[_enum.Windows.Services.Maps.Guidance.GuidanceAudioNotifications],  # value
                                      _type.HRESULT]
    add_GuidanceUpdated: _Callable[[_Windows_Foundation.ITypedEventHandler[IGuidanceNavigator, IGuidanceUpdatedEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_GuidanceUpdated: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    add_DestinationReached: _Callable[[_Windows_Foundation.ITypedEventHandler[IGuidanceNavigator, _inspectable.IInspectable],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_DestinationReached: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_Rerouting: _Callable[[_Windows_Foundation.ITypedEventHandler[IGuidanceNavigator, _inspectable.IInspectable],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_Rerouting: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    add_Rerouted: _Callable[[_Windows_Foundation.ITypedEventHandler[IGuidanceNavigator, IGuidanceReroutedEventArgs],  # handler
                             _Pointer[_struct.EventRegistrationToken]],  # token
                            _type.HRESULT]
    remove_Rerouted: _Callable[[_struct.EventRegistrationToken],  # token
                               _type.HRESULT]
    add_RerouteFailed: _Callable[[_Windows_Foundation.ITypedEventHandler[IGuidanceNavigator, _inspectable.IInspectable],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_RerouteFailed: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_UserLocationLost: _Callable[[_Windows_Foundation.ITypedEventHandler[IGuidanceNavigator, _inspectable.IInspectable],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_UserLocationLost: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    add_UserLocationRestored: _Callable[[_Windows_Foundation.ITypedEventHandler[IGuidanceNavigator, _inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_UserLocationRestored: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    SetGuidanceVoice: _Callable[[_type.INT32,  # voiceId
                                 _type.HSTRING],  # voiceFolder
                                _type.HRESULT]
    UpdateUserLocation: _Callable[[_Windows_Devices_Geolocation.IGeocoordinate],  # userLocation
                                  _type.HRESULT]
    UpdateUserLocationWithPositionOverride: _Callable[[_Windows_Devices_Geolocation.IGeocoordinate,  # userLocation
                                                       _struct.Windows.Devices.Geolocation.BasicGeoposition],  # positionOverride
                                                      _type.HRESULT]


class IGuidanceNavigator2(_inspectable.IInspectable):
    add_AudioNotificationRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IGuidanceNavigator, IGuidanceAudioNotificationRequestedEventArgs],  # value
                                               _Pointer[_struct.EventRegistrationToken]],  # token
                                              _type.HRESULT]
    remove_AudioNotificationRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                 _type.HRESULT]
    get_IsGuidanceAudioMuted: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    put_IsGuidanceAudioMuted: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]


class IGuidanceNavigatorStatics(_inspectable.IInspectable, factory=True):
    GetCurrent: _Callable[[_Pointer[IGuidanceNavigator]],  # result
                          _type.HRESULT]


class IGuidanceNavigatorStatics2(_inspectable.IInspectable, factory=True):
    get_UseAppProvidedVoice: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]


class IGuidanceReroutedEventArgs(_inspectable.IInspectable):
    get_Route: _Callable[[_Pointer[IGuidanceRoute]],  # result
                         _type.HRESULT]


class IGuidanceRoadSegment(_inspectable.IInspectable):
    get_RoadName: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_ShortRoadName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_SpeedLimit: _Callable[[_Pointer[_type.DOUBLE]],  # value
                              _type.HRESULT]
    get_TravelTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                              _type.HRESULT]
    get_Path: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeopath]],  # value
                        _type.HRESULT]
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_IsHighway: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_IsTunnel: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_IsTollRoad: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]


class IGuidanceRoadSegment2(_inspectable.IInspectable):
    get_IsScenic: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]


class IGuidanceRoadSignpost(_inspectable.IInspectable):
    get_ExitNumber: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_Exit: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_BackgroundColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                   _type.HRESULT]
    get_ForegroundColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                   _type.HRESULT]
    get_ExitDirections: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                  _type.HRESULT]


class IGuidanceRoute(_inspectable.IInspectable):
    get_Duration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    get_Distance: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    get_Maneuvers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IGuidanceManeuver]]],  # value
                             _type.HRESULT]
    get_BoundingBox: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeoboundingBox]],  # value
                               _type.HRESULT]
    get_Path: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeopath]],  # value
                        _type.HRESULT]
    get_RoadSegments: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IGuidanceRoadSegment]]],  # value
                                _type.HRESULT]
    ConvertToMapRoute: _Callable[[_Pointer[_Windows_Services_Maps.IMapRoute]],  # result
                                 _type.HRESULT]


class IGuidanceRouteStatics(_inspectable.IInspectable, factory=True):
    CanCreateFromMapRoute: _Callable[[_Windows_Services_Maps.IMapRoute,  # mapRoute
                                      _Pointer[_type.boolean]],  # result
                                     _type.HRESULT]
    TryCreateFromMapRoute: _Callable[[_Windows_Services_Maps.IMapRoute,  # mapRoute
                                      _Pointer[IGuidanceRoute]],  # result
                                     _type.HRESULT]


class IGuidanceTelemetryCollector(_inspectable.IInspectable):
    get_Enabled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Enabled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    ClearLocalData: _Callable[[],
                              _type.HRESULT]
    get_SpeedTrigger: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    put_SpeedTrigger: _Callable[[_type.DOUBLE],  # value
                                _type.HRESULT]
    get_UploadFrequency: _Callable[[_Pointer[_type.INT32]],  # value
                                   _type.HRESULT]
    put_UploadFrequency: _Callable[[_type.INT32],  # value
                                   _type.HRESULT]


class IGuidanceTelemetryCollectorStatics(_inspectable.IInspectable, factory=True):
    GetCurrent: _Callable[[_Pointer[IGuidanceTelemetryCollector]],  # result
                          _type.HRESULT]


class IGuidanceUpdatedEventArgs(_inspectable.IInspectable):
    get_Mode: _Callable[[_Pointer[_enum.Windows.Services.Maps.Guidance.GuidanceMode]],  # value
                        _type.HRESULT]
    get_NextManeuver: _Callable[[_Pointer[IGuidanceManeuver]],  # value
                                _type.HRESULT]
    get_NextManeuverDistance: _Callable[[_Pointer[_type.INT32]],  # value
                                        _type.HRESULT]
    get_AfterNextManeuver: _Callable[[_Pointer[IGuidanceManeuver]],  # value
                                     _type.HRESULT]
    get_AfterNextManeuverDistance: _Callable[[_Pointer[_type.INT32]],  # value
                                             _type.HRESULT]
    get_DistanceToDestination: _Callable[[_Pointer[_type.INT32]],  # value
                                         _type.HRESULT]
    get_ElapsedDistance: _Callable[[_Pointer[_type.INT32]],  # value
                                   _type.HRESULT]
    get_ElapsedTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                               _type.HRESULT]
    get_TimeToDestination: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                     _type.HRESULT]
    get_RoadName: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Route: _Callable[[_Pointer[IGuidanceRoute]],  # result
                         _type.HRESULT]
    get_CurrentLocation: _Callable[[_Pointer[IGuidanceMapMatchedCoordinate]],  # result
                                   _type.HRESULT]
    get_IsNewManeuver: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_LaneInfo: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IGuidanceLaneInfo]]],  # value
                            _type.HRESULT]
