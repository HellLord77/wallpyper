from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class ICivicAddress(_inspectable.IInspectable):
    get_Country: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_State: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_City: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_PostalCode: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]


class IGeoboundingBox(_inspectable.IInspectable):
    get_NorthwestCorner: _Callable[[_Pointer[_struct.Windows.Devices.Geolocation.BasicGeoposition]],  # value
                                   _type.HRESULT]
    get_SoutheastCorner: _Callable[[_Pointer[_struct.Windows.Devices.Geolocation.BasicGeoposition]],  # value
                                   _type.HRESULT]
    get_Center: _Callable[[_Pointer[_struct.Windows.Devices.Geolocation.BasicGeoposition]],  # value
                          _type.HRESULT]
    get_MinAltitude: _Callable[[_Pointer[_type.DOUBLE]],  # value
                               _type.HRESULT]
    get_MaxAltitude: _Callable[[_Pointer[_type.DOUBLE]],  # value
                               _type.HRESULT]


class IGeoboundingBoxFactory(_inspectable.IInspectable):
    Create: _Callable[[_struct.Windows.Devices.Geolocation.BasicGeoposition,  # northwestCorner
                       _struct.Windows.Devices.Geolocation.BasicGeoposition,  # southeastCorner
                       _Pointer[IGeoboundingBox]],  # value
                      _type.HRESULT]
    CreateWithAltitudeReference: _Callable[[_struct.Windows.Devices.Geolocation.BasicGeoposition,  # northwestCorner
                                            _struct.Windows.Devices.Geolocation.BasicGeoposition,  # southeastCorner
                                            _enum.Windows.Devices.Geolocation.AltitudeReferenceSystem,  # altitudeReferenceSystem
                                            _Pointer[IGeoboundingBox]],  # value
                                           _type.HRESULT]
    CreateWithAltitudeReferenceAndSpatialReference: _Callable[[_struct.Windows.Devices.Geolocation.BasicGeoposition,  # northwestCorner
                                                               _struct.Windows.Devices.Geolocation.BasicGeoposition,  # southeastCorner
                                                               _enum.Windows.Devices.Geolocation.AltitudeReferenceSystem,  # altitudeReferenceSystem
                                                               _type.UINT32,  # spatialReferenceId
                                                               _Pointer[IGeoboundingBox]],  # value
                                                              _type.HRESULT]

    _factory = True


class IGeoboundingBoxStatics(_inspectable.IInspectable):
    TryCompute: _Callable[[_Windows_Foundation_Collections.IIterable[_struct.Windows.Devices.Geolocation.BasicGeoposition],  # positions
                           _Pointer[IGeoboundingBox]],  # value
                          _type.HRESULT]
    TryComputeWithAltitudeReference: _Callable[[_Windows_Foundation_Collections.IIterable[_struct.Windows.Devices.Geolocation.BasicGeoposition],  # positions
                                                _enum.Windows.Devices.Geolocation.AltitudeReferenceSystem,  # altitudeRefSystem
                                                _Pointer[IGeoboundingBox]],  # value
                                               _type.HRESULT]
    TryComputeWithAltitudeReferenceAndSpatialReference: _Callable[[_Windows_Foundation_Collections.IIterable[_struct.Windows.Devices.Geolocation.BasicGeoposition],  # positions
                                                                   _enum.Windows.Devices.Geolocation.AltitudeReferenceSystem,  # altitudeRefSystem
                                                                   _type.UINT32,  # spatialReferenceId
                                                                   _Pointer[IGeoboundingBox]],  # value
                                                                  _type.HRESULT]

    _factory = True


class IGeocircle(_inspectable.IInspectable):
    get_Center: _Callable[[_Pointer[_struct.Windows.Devices.Geolocation.BasicGeoposition]],  # value
                          _type.HRESULT]
    get_Radius: _Callable[[_Pointer[_type.DOUBLE]],  # value
                          _type.HRESULT]


class IGeocircleFactory(_inspectable.IInspectable):
    Create: _Callable[[_struct.Windows.Devices.Geolocation.BasicGeoposition,  # position
                       _type.DOUBLE,  # radius
                       _Pointer[IGeocircle]],  # value
                      _type.HRESULT]
    CreateWithAltitudeReferenceSystem: _Callable[[_struct.Windows.Devices.Geolocation.BasicGeoposition,  # position
                                                  _type.DOUBLE,  # radius
                                                  _enum.Windows.Devices.Geolocation.AltitudeReferenceSystem,  # altitudeReferenceSystem
                                                  _Pointer[IGeocircle]],  # value
                                                 _type.HRESULT]
    CreateWithAltitudeReferenceSystemAndSpatialReferenceId: _Callable[[_struct.Windows.Devices.Geolocation.BasicGeoposition,  # position
                                                                       _type.DOUBLE,  # radius
                                                                       _enum.Windows.Devices.Geolocation.AltitudeReferenceSystem,  # altitudeReferenceSystem
                                                                       _type.UINT32,  # spatialReferenceId
                                                                       _Pointer[IGeocircle]],  # value
                                                                      _type.HRESULT]

    _factory = True


class IGeocoordinate(_inspectable.IInspectable):
    Latitude: _Callable[[_Pointer[_type.DOUBLE]],  # value
                        _type.HRESULT]
    Longitude: _Callable[[_Pointer[_type.DOUBLE]],  # value
                         _type.HRESULT]
    Altitude: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                        _type.HRESULT]
    get_Accuracy: _Callable[[_Pointer[_type.DOUBLE]],  # value
                            _type.HRESULT]
    get_AltitudeAccuracy: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                                    _type.HRESULT]
    get_Heading: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                           _type.HRESULT]
    get_Speed: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                         _type.HRESULT]
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]


class IGeocoordinateSatelliteData(_inspectable.IInspectable):
    get_PositionDilutionOfPrecision: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # ppValue
                                               _type.HRESULT]
    get_HorizontalDilutionOfPrecision: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # ppValue
                                                 _type.HRESULT]
    get_VerticalDilutionOfPrecision: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # ppValue
                                               _type.HRESULT]


class IGeocoordinateSatelliteData2(_inspectable.IInspectable):
    get_GeometricDilutionOfPrecision: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                                                _type.HRESULT]
    get_TimeDilutionOfPrecision: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                                           _type.HRESULT]


class IGeocoordinateWithPoint(_inspectable.IInspectable):
    get_Point: _Callable[[_Pointer[IGeopoint]],  # value
                         _type.HRESULT]


class IGeocoordinateWithPositionData(_inspectable.IInspectable):
    get_PositionSource: _Callable[[_Pointer[_enum.Windows.Devices.Geolocation.PositionSource]],  # pValue
                                  _type.HRESULT]
    get_SatelliteData: _Callable[[_Pointer[IGeocoordinateSatelliteData]],  # ppValue
                                 _type.HRESULT]


class IGeocoordinateWithPositionSourceTimestamp(_inspectable.IInspectable):
    get_PositionSourceTimestamp: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                           _type.HRESULT]


class IGeocoordinateWithRemoteSource(_inspectable.IInspectable):
    get_IsRemoteSource: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]


class IGeolocator(_inspectable.IInspectable):
    get_DesiredAccuracy: _Callable[[_Pointer[_enum.Windows.Devices.Geolocation.PositionAccuracy]],  # value
                                   _type.HRESULT]
    put_DesiredAccuracy: _Callable[[_enum.Windows.Devices.Geolocation.PositionAccuracy],  # value
                                   _type.HRESULT]
    get_MovementThreshold: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                     _type.HRESULT]
    put_MovementThreshold: _Callable[[_type.DOUBLE],  # value
                                     _type.HRESULT]
    get_ReportInterval: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]
    put_ReportInterval: _Callable[[_type.UINT32],  # value
                                  _type.HRESULT]
    get_LocationStatus: _Callable[[_Pointer[_enum.Windows.Devices.Geolocation.PositionStatus]],  # value
                                  _type.HRESULT]
    GetGeopositionAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IGeoposition]]],  # value
                                   _type.HRESULT]
    GetGeopositionAsyncWithAgeAndTimeout: _Callable[[_struct.Windows.Foundation.TimeSpan,  # maximumAge
                                                     _struct.Windows.Foundation.TimeSpan,  # timeout
                                                     _Pointer[_Windows_Foundation.IAsyncOperation[IGeoposition]]],  # value
                                                    _type.HRESULT]
    add_PositionChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IGeolocator, IPositionChangedEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_PositionChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    add_StatusChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IGeolocator, IStatusChangedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_StatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]


class IGeolocator2(_inspectable.IInspectable):
    AllowFallbackToConsentlessPositions: _Callable[[],
                                                   _type.HRESULT]


class IGeolocatorStatics(_inspectable.IInspectable):
    RequestAccessAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Devices.Geolocation.GeolocationAccessStatus]]],  # result
                                  _type.HRESULT]
    GetGeopositionHistoryAsync: _Callable[[_struct.Windows.Foundation.DateTime,  # startTime
                                           _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IGeoposition]]]],  # result
                                          _type.HRESULT]
    GetGeopositionHistoryWithDurationAsync: _Callable[[_struct.Windows.Foundation.DateTime,  # startTime
                                                       _struct.Windows.Foundation.TimeSpan,  # duration
                                                       _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IGeoposition]]]],  # result
                                                      _type.HRESULT]

    _factory = True


class IGeolocatorStatics2(_inspectable.IInspectable):
    get_IsDefaultGeopositionRecommended: _Callable[[_Pointer[_type.boolean]],  # value
                                                   _type.HRESULT]
    put_DefaultGeoposition: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Devices.Geolocation.BasicGeoposition]],  # value
                                      _type.HRESULT]
    get_DefaultGeoposition: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Devices.Geolocation.BasicGeoposition]]],  # value
                                      _type.HRESULT]

    _factory = True


class IGeolocatorWithScalarAccuracy(_inspectable.IInspectable):
    get_DesiredAccuracyInMeters: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                                           _type.HRESULT]
    put_DesiredAccuracyInMeters: _Callable[[_Windows_Foundation.IReference[_type.UINT32]],  # value
                                           _type.HRESULT]


class IGeopath(_inspectable.IInspectable):
    get_Positions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_struct.Windows.Devices.Geolocation.BasicGeoposition]]],  # value
                             _type.HRESULT]


class IGeopathFactory(_inspectable.IInspectable):
    Create: _Callable[[_Windows_Foundation_Collections.IIterable[_struct.Windows.Devices.Geolocation.BasicGeoposition],  # positions
                       _Pointer[IGeopath]],  # value
                      _type.HRESULT]
    CreateWithAltitudeReference: _Callable[[_Windows_Foundation_Collections.IIterable[_struct.Windows.Devices.Geolocation.BasicGeoposition],  # positions
                                            _enum.Windows.Devices.Geolocation.AltitudeReferenceSystem,  # altitudeReferenceSystem
                                            _Pointer[IGeopath]],  # value
                                           _type.HRESULT]
    CreateWithAltitudeReferenceAndSpatialReference: _Callable[[_Windows_Foundation_Collections.IIterable[_struct.Windows.Devices.Geolocation.BasicGeoposition],  # positions
                                                               _enum.Windows.Devices.Geolocation.AltitudeReferenceSystem,  # altitudeReferenceSystem
                                                               _type.UINT32,  # spatialReferenceId
                                                               _Pointer[IGeopath]],  # value
                                                              _type.HRESULT]

    _factory = True


class IGeopoint(_inspectable.IInspectable):
    get_Position: _Callable[[_Pointer[_struct.Windows.Devices.Geolocation.BasicGeoposition]],  # value
                            _type.HRESULT]


class IGeopointFactory(_inspectable.IInspectable):
    Create: _Callable[[_struct.Windows.Devices.Geolocation.BasicGeoposition,  # position
                       _Pointer[IGeopoint]],  # value
                      _type.HRESULT]
    CreateWithAltitudeReferenceSystem: _Callable[[_struct.Windows.Devices.Geolocation.BasicGeoposition,  # position
                                                  _enum.Windows.Devices.Geolocation.AltitudeReferenceSystem,  # altitudeReferenceSystem
                                                  _Pointer[IGeopoint]],  # value
                                                 _type.HRESULT]
    CreateWithAltitudeReferenceSystemAndSpatialReferenceId: _Callable[[_struct.Windows.Devices.Geolocation.BasicGeoposition,  # position
                                                                       _enum.Windows.Devices.Geolocation.AltitudeReferenceSystem,  # altitudeReferenceSystem
                                                                       _type.UINT32,  # spatialReferenceId
                                                                       _Pointer[IGeopoint]],  # value
                                                                      _type.HRESULT]

    _factory = True


class IGeoposition(_inspectable.IInspectable):
    get_Coordinate: _Callable[[_Pointer[IGeocoordinate]],  # value
                              _type.HRESULT]
    get_CivicAddress: _Callable[[_Pointer[ICivicAddress]],  # value
                                _type.HRESULT]


class IGeoposition2(_inspectable.IInspectable):
    get_VenueData: _Callable[[_Pointer[IVenueData]],  # value
                             _type.HRESULT]


class IGeoshape(_inspectable.IInspectable):
    get_GeoshapeType: _Callable[[_Pointer[_enum.Windows.Devices.Geolocation.GeoshapeType]],  # value
                                _type.HRESULT]
    get_SpatialReferenceId: _Callable[[_Pointer[_type.UINT32]],  # value
                                      _type.HRESULT]
    get_AltitudeReferenceSystem: _Callable[[_Pointer[_enum.Windows.Devices.Geolocation.AltitudeReferenceSystem]],  # value
                                           _type.HRESULT]


class IGeovisit(_inspectable.IInspectable):
    get_Position: _Callable[[_Pointer[IGeoposition]],  # value
                            _type.HRESULT]
    get_StateChange: _Callable[[_Pointer[_enum.Windows.Devices.Geolocation.VisitStateChange]],  # value
                               _type.HRESULT]
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]


class IGeovisitMonitor(_inspectable.IInspectable):
    get_MonitoringScope: _Callable[[_Pointer[_enum.Windows.Devices.Geolocation.VisitMonitoringScope]],  # value
                                   _type.HRESULT]
    Start: _Callable[[_enum.Windows.Devices.Geolocation.VisitMonitoringScope],  # value
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    add_VisitStateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IGeovisitMonitor, IGeovisitStateChangedEventArgs],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_VisitStateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]


class IGeovisitMonitorStatics(_inspectable.IInspectable):
    GetLastReportAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IGeovisit]]],  # value
                                  _type.HRESULT]

    _factory = True


class IGeovisitStateChangedEventArgs(_inspectable.IInspectable):
    get_Visit: _Callable[[_Pointer[IGeovisit]],  # value
                         _type.HRESULT]


class IGeovisitTriggerDetails(_inspectable.IInspectable):
    ReadReports: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IGeovisit]]],  # values
                           _type.HRESULT]


class IPositionChangedEventArgs(_inspectable.IInspectable):
    get_Position: _Callable[[_Pointer[IGeoposition]],  # value
                            _type.HRESULT]


class IStatusChangedEventArgs(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Devices.Geolocation.PositionStatus]],  # value
                          _type.HRESULT]


class IVenueData(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_Level: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
