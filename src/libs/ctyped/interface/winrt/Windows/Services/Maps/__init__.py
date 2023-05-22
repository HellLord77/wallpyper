from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...Devices import Geolocation as _Windows_Devices_Geolocation
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IEnhancedWaypoint(_inspectable.IInspectable):
    get_Point: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeopoint]],  # value
                         _type.HRESULT]
    get_Kind: _Callable[[_Pointer[_enum.Windows.Services.Maps.WaypointKind]],  # value
                        _type.HRESULT]


class IEnhancedWaypointFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Windows_Devices_Geolocation.IGeopoint,  # point
                       _enum.Windows.Services.Maps.WaypointKind,  # kind
                       _Pointer[IEnhancedWaypoint]],  # value
                      _type.HRESULT]


class IManeuverWarning(_inspectable.IInspectable):
    get_Kind: _Callable[[_Pointer[_enum.Windows.Services.Maps.ManeuverWarningKind]],  # value
                        _type.HRESULT]
    get_Severity: _Callable[[_Pointer[_enum.Windows.Services.Maps.ManeuverWarningSeverity]],  # value
                            _type.HRESULT]


class IMapAddress(_inspectable.IInspectable):
    get_BuildingName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_BuildingFloor: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_BuildingRoom: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_BuildingWing: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_StreetNumber: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_Street: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Neighborhood: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_District: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Town: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Region: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_RegionCode: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_Country: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_CountryCode: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_PostCode: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Continent: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]


class IMapAddress2(_inspectable.IInspectable):
    get_FormattedAddress: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]


class IMapLocation(_inspectable.IInspectable):
    get_Point: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeopoint]],  # value
                         _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Address: _Callable[[_Pointer[IMapAddress]],  # value
                           _type.HRESULT]


class IMapLocationFinderResult(_inspectable.IInspectable):
    get_Locations: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMapLocation]]],  # value
                             _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.Services.Maps.MapLocationFinderStatus]],  # value
                          _type.HRESULT]


class IMapLocationFinderStatics(_inspectable.IInspectable, factory=True):
    FindLocationsAtAsync: _Callable[[_Windows_Devices_Geolocation.IGeopoint,  # queryPoint
                                     _Pointer[_Windows_Foundation.IAsyncOperation[IMapLocationFinderResult]]],  # result
                                    _type.HRESULT]
    FindLocationsAsync: _Callable[[_type.HSTRING,  # searchText
                                   _Windows_Devices_Geolocation.IGeopoint,  # referencePoint
                                   _Pointer[_Windows_Foundation.IAsyncOperation[IMapLocationFinderResult]]],  # result
                                  _type.HRESULT]
    FindLocationsWithMaxCountAsync: _Callable[[_type.HSTRING,  # searchText
                                               _Windows_Devices_Geolocation.IGeopoint,  # referencePoint
                                               _type.UINT32,  # maxCount
                                               _Pointer[_Windows_Foundation.IAsyncOperation[IMapLocationFinderResult]]],  # result
                                              _type.HRESULT]


class IMapLocationFinderStatics2(_inspectable.IInspectable, factory=True):
    FindLocationsAtWithAccuracyAsync: _Callable[[_Windows_Devices_Geolocation.IGeopoint,  # queryPoint
                                                 _enum.Windows.Services.Maps.MapLocationDesiredAccuracy,  # accuracy
                                                 _Pointer[_Windows_Foundation.IAsyncOperation[IMapLocationFinderResult]]],  # result
                                                _type.HRESULT]


class IMapManagerStatics(_inspectable.IInspectable, factory=True):
    ShowDownloadedMapsUI: _Callable[[],
                                    _type.HRESULT]
    ShowMapsUpdateUI: _Callable[[],
                                _type.HRESULT]


class IMapRoute(_inspectable.IInspectable):
    get_BoundingBox: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeoboundingBox]],  # value
                               _type.HRESULT]
    get_LengthInMeters: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    get_EstimatedDuration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                     _type.HRESULT]
    get_Path: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeopath]],  # value
                        _type.HRESULT]
    get_Legs: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMapRouteLeg]]],  # value
                        _type.HRESULT]
    get_IsTrafficBased: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]


class IMapRoute2(_inspectable.IInspectable):
    get_ViolatedRestrictions: _Callable[[_Pointer[_enum.Windows.Services.Maps.MapRouteRestrictions]],  # value
                                        _type.HRESULT]
    get_HasBlockedRoads: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]


class IMapRoute3(_inspectable.IInspectable):
    get_DurationWithoutTraffic: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                          _type.HRESULT]
    get_TrafficCongestion: _Callable[[_Pointer[_enum.Windows.Services.Maps.TrafficCongestion]],  # value
                                     _type.HRESULT]


class IMapRoute4(_inspectable.IInspectable):
    get_IsScenic: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]


class IMapRouteDrivingOptions(_inspectable.IInspectable):
    get_MaxAlternateRouteCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                          _type.HRESULT]
    put_MaxAlternateRouteCount: _Callable[[_type.UINT32],  # value
                                          _type.HRESULT]
    get_InitialHeading: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                                  _type.HRESULT]
    put_InitialHeading: _Callable[[_Windows_Foundation.IReference[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    get_RouteOptimization: _Callable[[_Pointer[_enum.Windows.Services.Maps.MapRouteOptimization]],  # value
                                     _type.HRESULT]
    put_RouteOptimization: _Callable[[_enum.Windows.Services.Maps.MapRouteOptimization],  # value
                                     _type.HRESULT]
    get_RouteRestrictions: _Callable[[_Pointer[_enum.Windows.Services.Maps.MapRouteRestrictions]],  # value
                                     _type.HRESULT]
    put_RouteRestrictions: _Callable[[_enum.Windows.Services.Maps.MapRouteRestrictions],  # value
                                     _type.HRESULT]


class IMapRouteDrivingOptions2(_inspectable.IInspectable):
    get_DepartureTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                 _type.HRESULT]
    put_DepartureTime: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                                 _type.HRESULT]


class IMapRouteFinderResult(_inspectable.IInspectable):
    get_Route: _Callable[[_Pointer[IMapRoute]],  # value
                         _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.Services.Maps.MapRouteFinderStatus]],  # value
                          _type.HRESULT]


class IMapRouteFinderResult2(_inspectable.IInspectable):
    get_AlternateRoutes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMapRoute]]],  # value
                                   _type.HRESULT]


class IMapRouteFinderStatics(_inspectable.IInspectable, factory=True):
    GetDrivingRouteAsync: _Callable[[_Windows_Devices_Geolocation.IGeopoint,  # startPoint
                                     _Windows_Devices_Geolocation.IGeopoint,  # endPoint
                                     _Pointer[_Windows_Foundation.IAsyncOperation[IMapRouteFinderResult]]],  # result
                                    _type.HRESULT]
    GetDrivingRouteWithOptimizationAsync: _Callable[[_Windows_Devices_Geolocation.IGeopoint,  # startPoint
                                                     _Windows_Devices_Geolocation.IGeopoint,  # endPoint
                                                     _enum.Windows.Services.Maps.MapRouteOptimization,  # optimization
                                                     _Pointer[_Windows_Foundation.IAsyncOperation[IMapRouteFinderResult]]],  # result
                                                    _type.HRESULT]
    GetDrivingRouteWithOptimizationAndRestrictionsAsync: _Callable[[_Windows_Devices_Geolocation.IGeopoint,  # startPoint
                                                                    _Windows_Devices_Geolocation.IGeopoint,  # endPoint
                                                                    _enum.Windows.Services.Maps.MapRouteOptimization,  # optimization
                                                                    _enum.Windows.Services.Maps.MapRouteRestrictions,  # restrictions
                                                                    _Pointer[_Windows_Foundation.IAsyncOperation[IMapRouteFinderResult]]],  # result
                                                                   _type.HRESULT]
    GetDrivingRouteWithOptimizationRestrictionsAndHeadingAsync: _Callable[[_Windows_Devices_Geolocation.IGeopoint,  # startPoint
                                                                           _Windows_Devices_Geolocation.IGeopoint,  # endPoint
                                                                           _enum.Windows.Services.Maps.MapRouteOptimization,  # optimization
                                                                           _enum.Windows.Services.Maps.MapRouteRestrictions,  # restrictions
                                                                           _type.DOUBLE,  # headingInDegrees
                                                                           _Pointer[_Windows_Foundation.IAsyncOperation[IMapRouteFinderResult]]],  # result
                                                                          _type.HRESULT]
    GetDrivingRouteFromWaypointsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Devices_Geolocation.IGeopoint],  # wayPoints
                                                  _Pointer[_Windows_Foundation.IAsyncOperation[IMapRouteFinderResult]]],  # result
                                                 _type.HRESULT]
    GetDrivingRouteFromWaypointsAndOptimizationAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Devices_Geolocation.IGeopoint],  # wayPoints
                                                                 _enum.Windows.Services.Maps.MapRouteOptimization,  # optimization
                                                                 _Pointer[_Windows_Foundation.IAsyncOperation[IMapRouteFinderResult]]],  # result
                                                                _type.HRESULT]
    GetDrivingRouteFromWaypointsOptimizationAndRestrictionsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Devices_Geolocation.IGeopoint],  # wayPoints
                                                                             _enum.Windows.Services.Maps.MapRouteOptimization,  # optimization
                                                                             _enum.Windows.Services.Maps.MapRouteRestrictions,  # restrictions
                                                                             _Pointer[_Windows_Foundation.IAsyncOperation[IMapRouteFinderResult]]],  # result
                                                                            _type.HRESULT]
    GetDrivingRouteFromWaypointsOptimizationRestrictionsAndHeadingAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Devices_Geolocation.IGeopoint],  # wayPoints
                                                                                    _enum.Windows.Services.Maps.MapRouteOptimization,  # optimization
                                                                                    _enum.Windows.Services.Maps.MapRouteRestrictions,  # restrictions
                                                                                    _type.DOUBLE,  # headingInDegrees
                                                                                    _Pointer[_Windows_Foundation.IAsyncOperation[IMapRouteFinderResult]]],  # result
                                                                                   _type.HRESULT]
    GetWalkingRouteAsync: _Callable[[_Windows_Devices_Geolocation.IGeopoint,  # startPoint
                                     _Windows_Devices_Geolocation.IGeopoint,  # endPoint
                                     _Pointer[_Windows_Foundation.IAsyncOperation[IMapRouteFinderResult]]],  # result
                                    _type.HRESULT]
    GetWalkingRouteFromWaypointsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Devices_Geolocation.IGeopoint],  # wayPoints
                                                  _Pointer[_Windows_Foundation.IAsyncOperation[IMapRouteFinderResult]]],  # result
                                                 _type.HRESULT]


class IMapRouteFinderStatics2(_inspectable.IInspectable, factory=True):
    GetDrivingRouteWithOptionsAsync: _Callable[[_Windows_Devices_Geolocation.IGeopoint,  # startPoint
                                                _Windows_Devices_Geolocation.IGeopoint,  # endPoint
                                                IMapRouteDrivingOptions,  # options
                                                _Pointer[_Windows_Foundation.IAsyncOperation[IMapRouteFinderResult]]],  # result
                                               _type.HRESULT]


class IMapRouteFinderStatics3(_inspectable.IInspectable, factory=True):
    GetDrivingRouteFromEnhancedWaypointsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[IEnhancedWaypoint],  # waypoints
                                                          _Pointer[_Windows_Foundation.IAsyncOperation[IMapRouteFinderResult]]],  # result
                                                         _type.HRESULT]
    GetDrivingRouteFromEnhancedWaypointsWithOptionsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[IEnhancedWaypoint],  # waypoints
                                                                     IMapRouteDrivingOptions,  # options
                                                                     _Pointer[_Windows_Foundation.IAsyncOperation[IMapRouteFinderResult]]],  # result
                                                                    _type.HRESULT]


class IMapRouteLeg(_inspectable.IInspectable):
    get_BoundingBox: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeoboundingBox]],  # value
                               _type.HRESULT]
    get_Path: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeopath]],  # value
                        _type.HRESULT]
    get_LengthInMeters: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    get_EstimatedDuration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                     _type.HRESULT]
    get_Maneuvers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMapRouteManeuver]]],  # value
                             _type.HRESULT]


class IMapRouteLeg2(_inspectable.IInspectable):
    get_DurationWithoutTraffic: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                          _type.HRESULT]
    get_TrafficCongestion: _Callable[[_Pointer[_enum.Windows.Services.Maps.TrafficCongestion]],  # value
                                     _type.HRESULT]


class IMapRouteManeuver(_inspectable.IInspectable):
    get_StartingPoint: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeopoint]],  # value
                                 _type.HRESULT]
    get_LengthInMeters: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    get_InstructionText: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_Kind: _Callable[[_Pointer[_enum.Windows.Services.Maps.MapRouteManeuverKind]],  # value
                        _type.HRESULT]
    get_ExitNumber: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_ManeuverNotices: _Callable[[_Pointer[_enum.Windows.Services.Maps.MapManeuverNotices]],  # value
                                   _type.HRESULT]


class IMapRouteManeuver2(_inspectable.IInspectable):
    get_StartHeading: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    get_EndHeading: _Callable[[_Pointer[_type.DOUBLE]],  # value
                              _type.HRESULT]
    get_StreetName: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]


class IMapRouteManeuver3(_inspectable.IInspectable):
    get_Warnings: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IManeuverWarning]]],  # value
                            _type.HRESULT]


class IMapServiceStatics(_inspectable.IInspectable, factory=True):
    put_ServiceToken: _Callable[[_type.HSTRING],  # value
                                _type.HRESULT]
    get_ServiceToken: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]


class IMapServiceStatics2(_inspectable.IInspectable, factory=True):
    get_WorldViewRegionCode: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]


class IMapServiceStatics3(_inspectable.IInspectable, factory=True):
    get_DataAttributions: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]


class IMapServiceStatics4(_inspectable.IInspectable, factory=True):
    put_DataUsagePreference: _Callable[[_enum.Windows.Services.Maps.MapServiceDataUsagePreference],  # value
                                       _type.HRESULT]
    get_DataUsagePreference: _Callable[[_Pointer[_enum.Windows.Services.Maps.MapServiceDataUsagePreference]],  # value
                                       _type.HRESULT]


class IPlaceInfo(_inspectable.IInspectable):
    Show: _Callable[[_struct.Windows.Foundation.Rect],  # selection
                    _type.HRESULT]
    ShowWithPreferredPlacement: _Callable[[_struct.Windows.Foundation.Rect,  # selection
                                           _enum.Windows.UI.Popups.Placement],  # preferredPlacement
                                          _type.HRESULT]
    get_Identifier: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_DisplayAddress: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_Geoshape: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeoshape]],  # value
                            _type.HRESULT]


class IPlaceInfoCreateOptions(_inspectable.IInspectable):
    put_DisplayName: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_DisplayAddress: _Callable[[_type.HSTRING],  # value
                                  _type.HRESULT]
    get_DisplayAddress: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]


class IPlaceInfoStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Windows_Devices_Geolocation.IGeopoint,  # referencePoint
                       _Pointer[IPlaceInfo]],  # resultValue
                      _type.HRESULT]
    CreateWithGeopointAndOptions: _Callable[[_Windows_Devices_Geolocation.IGeopoint,  # referencePoint
                                             IPlaceInfoCreateOptions,  # options
                                             _Pointer[IPlaceInfo]],  # resultValue
                                            _type.HRESULT]
    CreateFromIdentifier: _Callable[[_type.HSTRING,  # identifier
                                     _Pointer[IPlaceInfo]],  # resultValue
                                    _type.HRESULT]
    CreateFromIdentifierWithOptions: _Callable[[_type.HSTRING,  # identifier
                                                _Windows_Devices_Geolocation.IGeopoint,  # defaultPoint
                                                IPlaceInfoCreateOptions,  # options
                                                _Pointer[IPlaceInfo]],  # resultValue
                                               _type.HRESULT]
    CreateFromMapLocation: _Callable[[IMapLocation,  # location
                                      _Pointer[IPlaceInfo]],  # resultValue
                                     _type.HRESULT]
    get_IsShowSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]


class IPlaceInfoStatics2(_inspectable.IInspectable, factory=True):
    CreateFromAddress: _Callable[[_type.HSTRING,  # displayAddress
                                  _Pointer[IPlaceInfo]],  # resultValue
                                 _type.HRESULT]
    CreateFromAddressWithName: _Callable[[_type.HSTRING,  # displayAddress
                                          _type.HSTRING,  # displayName
                                          _Pointer[IPlaceInfo]],  # resultValue
                                         _type.HRESULT]
