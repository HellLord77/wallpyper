from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IAccelerometer(_inspectable.IInspectable):
    GetCurrentReading: _Callable[[_Pointer[IAccelerometerReading]],  # value
                                 _type.HRESULT]
    get_MinimumReportInterval: _Callable[[_Pointer[_type.UINT32]],  # value
                                         _type.HRESULT]
    put_ReportInterval: _Callable[[_type.UINT32],  # value
                                  _type.HRESULT]
    get_ReportInterval: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]
    add_ReadingChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAccelerometer, IAccelerometerReadingChangedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_ReadingChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_Shaken: _Callable[[_Windows_Foundation.ITypedEventHandler[IAccelerometer, IAccelerometerShakenEventArgs],  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Shaken: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]


class IAccelerometer2(_inspectable.IInspectable):
    put_ReadingTransform: _Callable[[_enum.Windows.Graphics.Display.DisplayOrientations],  # value
                                    _type.HRESULT]
    get_ReadingTransform: _Callable[[_Pointer[_enum.Windows.Graphics.Display.DisplayOrientations]],  # value
                                    _type.HRESULT]


class IAccelerometer3(_inspectable.IInspectable):
    put_ReportLatency: _Callable[[_type.UINT32],  # value
                                 _type.HRESULT]
    get_ReportLatency: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    get_MaxBatchSize: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]


class IAccelerometer4(_inspectable.IInspectable):
    get_ReadingType: _Callable[[_Pointer[_enum.Windows.Devices.Sensors.AccelerometerReadingType]],  # type
                               _type.HRESULT]


class IAccelerometer5(_inspectable.IInspectable):
    get_ReportThreshold: _Callable[[_Pointer[IAccelerometerDataThreshold]],  # value
                                   _type.HRESULT]


class IAccelerometerDataThreshold(_inspectable.IInspectable):
    get_XAxisInGForce: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                 _type.HRESULT]
    put_XAxisInGForce: _Callable[[_type.DOUBLE],  # value
                                 _type.HRESULT]
    get_YAxisInGForce: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                 _type.HRESULT]
    put_YAxisInGForce: _Callable[[_type.DOUBLE],  # value
                                 _type.HRESULT]
    get_ZAxisInGForce: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                 _type.HRESULT]
    put_ZAxisInGForce: _Callable[[_type.DOUBLE],  # value
                                 _type.HRESULT]


class IAccelerometerDeviceId(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]


class IAccelerometerReading(_inspectable.IInspectable):
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_AccelerationX: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                 _type.HRESULT]
    get_AccelerationY: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                 _type.HRESULT]
    get_AccelerationZ: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                 _type.HRESULT]


class IAccelerometerReading2(_inspectable.IInspectable):
    get_PerformanceCount: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                    _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _inspectable.IInspectable]]],  # value
                              _type.HRESULT]


class IAccelerometerReadingChangedEventArgs(_inspectable.IInspectable):
    get_Reading: _Callable[[_Pointer[IAccelerometerReading]],  # value
                           _type.HRESULT]


class IAccelerometerShakenEventArgs(_inspectable.IInspectable):
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]


class IAccelerometerStatics(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[IAccelerometer]],  # result
                          _type.HRESULT]


class IAccelerometerStatics2(_inspectable.IInspectable, factory=True):
    GetDefaultWithAccelerometerReadingType: _Callable[[_enum.Windows.Devices.Sensors.AccelerometerReadingType,  # readingType
                                                       _Pointer[IAccelerometer]],  # result
                                                      _type.HRESULT]


class IAccelerometerStatics3(_inspectable.IInspectable, factory=True):
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IAccelerometer]]],  # operation
                           _type.HRESULT]
    GetDeviceSelector: _Callable[[_enum.Windows.Devices.Sensors.AccelerometerReadingType,  # readingType
                                  _Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]


class IActivitySensor(_inspectable.IInspectable):
    GetCurrentReadingAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IActivitySensorReading]]],  # result
                                      _type.HRESULT]
    get_SubscribedActivities: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_enum.Windows.Devices.Sensors.ActivityType]]],  # value
                                        _type.HRESULT]
    get_PowerInMilliwatts: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                     _type.HRESULT]
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_SupportedActivities: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Devices.Sensors.ActivityType]]],  # value
                                       _type.HRESULT]
    get_MinimumReportInterval: _Callable[[_Pointer[_type.UINT32]],  # value
                                         _type.HRESULT]
    add_ReadingChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IActivitySensor, IActivitySensorReadingChangedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_ReadingChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]


class IActivitySensorReading(_inspectable.IInspectable):
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_Activity: _Callable[[_Pointer[_enum.Windows.Devices.Sensors.ActivityType]],  # value
                            _type.HRESULT]
    get_Confidence: _Callable[[_Pointer[_enum.Windows.Devices.Sensors.ActivitySensorReadingConfidence]],  # value
                              _type.HRESULT]


class IActivitySensorReadingChangeReport(_inspectable.IInspectable):
    get_Reading: _Callable[[_Pointer[IActivitySensorReading]],  # value
                           _type.HRESULT]


class IActivitySensorReadingChangedEventArgs(_inspectable.IInspectable):
    get_Reading: _Callable[[_Pointer[IActivitySensorReading]],  # value
                           _type.HRESULT]


class IActivitySensorStatics(_inspectable.IInspectable, factory=True):
    GetDefaultAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IActivitySensor]]],  # result
                               _type.HRESULT]
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IActivitySensor]]],  # result
                           _type.HRESULT]
    GetSystemHistoryAsync: _Callable[[_struct.Windows.Foundation.DateTime,  # fromTime
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IActivitySensorReading]]]],  # result
                                     _type.HRESULT]
    GetSystemHistoryWithDurationAsync: _Callable[[_struct.Windows.Foundation.DateTime,  # fromTime
                                                  _struct.Windows.Foundation.TimeSpan,  # duration
                                                  _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IActivitySensorReading]]]],  # result
                                                 _type.HRESULT]


class IActivitySensorTriggerDetails(_inspectable.IInspectable):
    ReadReports: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IActivitySensorReadingChangeReport]]],  # value
                           _type.HRESULT]


class IAdaptiveDimmingOptions(_inspectable.IInspectable):
    get_AllowWhenExternalDisplayConnected: _Callable[[_Pointer[_type.boolean]],  # value
                                                     _type.HRESULT]
    put_AllowWhenExternalDisplayConnected: _Callable[[_type.boolean],  # value
                                                     _type.HRESULT]


class IAltimeter(_inspectable.IInspectable):
    GetCurrentReading: _Callable[[_Pointer[IAltimeterReading]],  # value
                                 _type.HRESULT]
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_MinimumReportInterval: _Callable[[_Pointer[_type.UINT32]],  # value
                                         _type.HRESULT]
    put_ReportInterval: _Callable[[_type.UINT32],  # value
                                  _type.HRESULT]
    get_ReportInterval: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]
    add_ReadingChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAltimeter, IAltimeterReadingChangedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_ReadingChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]


class IAltimeter2(_inspectable.IInspectable):
    put_ReportLatency: _Callable[[_type.UINT32],  # value
                                 _type.HRESULT]
    get_ReportLatency: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    get_MaxBatchSize: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]


class IAltimeterReading(_inspectable.IInspectable):
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_AltitudeChangeInMeters: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                          _type.HRESULT]


class IAltimeterReading2(_inspectable.IInspectable):
    get_PerformanceCount: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                    _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _inspectable.IInspectable]]],  # value
                              _type.HRESULT]


class IAltimeterReadingChangedEventArgs(_inspectable.IInspectable):
    get_Reading: _Callable[[_Pointer[IAltimeterReading]],  # value
                           _type.HRESULT]


class IAltimeterStatics(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[IAltimeter]],  # result
                          _type.HRESULT]


class IBarometer(_inspectable.IInspectable):
    GetCurrentReading: _Callable[[_Pointer[IBarometerReading]],  # value
                                 _type.HRESULT]
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_MinimumReportInterval: _Callable[[_Pointer[_type.UINT32]],  # value
                                         _type.HRESULT]
    put_ReportInterval: _Callable[[_type.UINT32],  # value
                                  _type.HRESULT]
    get_ReportInterval: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]
    add_ReadingChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IBarometer, IBarometerReadingChangedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_ReadingChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]


class IBarometer2(_inspectable.IInspectable):
    put_ReportLatency: _Callable[[_type.UINT32],  # value
                                 _type.HRESULT]
    get_ReportLatency: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    get_MaxBatchSize: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]


class IBarometer3(_inspectable.IInspectable):
    get_ReportThreshold: _Callable[[_Pointer[IBarometerDataThreshold]],  # value
                                   _type.HRESULT]


class IBarometerDataThreshold(_inspectable.IInspectable):
    get_Hectopascals: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    put_Hectopascals: _Callable[[_type.DOUBLE],  # value
                                _type.HRESULT]


class IBarometerReading(_inspectable.IInspectable):
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_StationPressureInHectopascals: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                 _type.HRESULT]


class IBarometerReading2(_inspectable.IInspectable):
    get_PerformanceCount: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                    _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _inspectable.IInspectable]]],  # value
                              _type.HRESULT]


class IBarometerReadingChangedEventArgs(_inspectable.IInspectable):
    get_Reading: _Callable[[_Pointer[IBarometerReading]],  # value
                           _type.HRESULT]


class IBarometerStatics(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[IBarometer]],  # result
                          _type.HRESULT]


class IBarometerStatics2(_inspectable.IInspectable, factory=True):
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IBarometer]]],  # operation
                           _type.HRESULT]
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]


class ICompass(_inspectable.IInspectable):
    GetCurrentReading: _Callable[[_Pointer[ICompassReading]],  # value
                                 _type.HRESULT]
    get_MinimumReportInterval: _Callable[[_Pointer[_type.UINT32]],  # value
                                         _type.HRESULT]
    put_ReportInterval: _Callable[[_type.UINT32],  # value
                                  _type.HRESULT]
    get_ReportInterval: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]
    add_ReadingChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ICompass, ICompassReadingChangedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_ReadingChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]


class ICompass2(_inspectable.IInspectable):
    put_ReadingTransform: _Callable[[_enum.Windows.Graphics.Display.DisplayOrientations],  # value
                                    _type.HRESULT]
    get_ReadingTransform: _Callable[[_Pointer[_enum.Windows.Graphics.Display.DisplayOrientations]],  # value
                                    _type.HRESULT]


class ICompass3(_inspectable.IInspectable):
    put_ReportLatency: _Callable[[_type.UINT32],  # value
                                 _type.HRESULT]
    get_ReportLatency: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    get_MaxBatchSize: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]


class ICompass4(_inspectable.IInspectable):
    get_ReportThreshold: _Callable[[_Pointer[ICompassDataThreshold]],  # value
                                   _type.HRESULT]


class ICompassDataThreshold(_inspectable.IInspectable):
    get_Degrees: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    put_Degrees: _Callable[[_type.DOUBLE],  # value
                           _type.HRESULT]


class ICompassDeviceId(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]


class ICompassReading(_inspectable.IInspectable):
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_HeadingMagneticNorth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                        _type.HRESULT]
    get_HeadingTrueNorth: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                                    _type.HRESULT]


class ICompassReading2(_inspectable.IInspectable):
    get_PerformanceCount: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                    _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _inspectable.IInspectable]]],  # value
                              _type.HRESULT]


class ICompassReadingChangedEventArgs(_inspectable.IInspectable):
    get_Reading: _Callable[[_Pointer[ICompassReading]],  # value
                           _type.HRESULT]


class ICompassReadingHeadingAccuracy(_inspectable.IInspectable):
    get_HeadingAccuracy: _Callable[[_Pointer[_enum.Windows.Devices.Sensors.MagnetometerAccuracy]],  # value
                                   _type.HRESULT]


class ICompassStatics(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[ICompass]],  # result
                          _type.HRESULT]


class ICompassStatics2(_inspectable.IInspectable, factory=True):
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[ICompass]]],  # operation
                           _type.HRESULT]


class IGyrometer(_inspectable.IInspectable):
    GetCurrentReading: _Callable[[_Pointer[IGyrometerReading]],  # value
                                 _type.HRESULT]
    get_MinimumReportInterval: _Callable[[_Pointer[_type.UINT32]],  # value
                                         _type.HRESULT]
    put_ReportInterval: _Callable[[_type.UINT32],  # value
                                  _type.HRESULT]
    get_ReportInterval: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]
    add_ReadingChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IGyrometer, IGyrometerReadingChangedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_ReadingChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]


class IGyrometer2(_inspectable.IInspectable):
    put_ReadingTransform: _Callable[[_enum.Windows.Graphics.Display.DisplayOrientations],  # value
                                    _type.HRESULT]
    get_ReadingTransform: _Callable[[_Pointer[_enum.Windows.Graphics.Display.DisplayOrientations]],  # value
                                    _type.HRESULT]


class IGyrometer3(_inspectable.IInspectable):
    put_ReportLatency: _Callable[[_type.UINT32],  # value
                                 _type.HRESULT]
    get_ReportLatency: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    get_MaxBatchSize: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]


class IGyrometer4(_inspectable.IInspectable):
    get_ReportThreshold: _Callable[[_Pointer[IGyrometerDataThreshold]],  # value
                                   _type.HRESULT]


class IGyrometerDataThreshold(_inspectable.IInspectable):
    get_XAxisInDegreesPerSecond: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                           _type.HRESULT]
    put_XAxisInDegreesPerSecond: _Callable[[_type.DOUBLE],  # value
                                           _type.HRESULT]
    get_YAxisInDegreesPerSecond: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                           _type.HRESULT]
    put_YAxisInDegreesPerSecond: _Callable[[_type.DOUBLE],  # value
                                           _type.HRESULT]
    get_ZAxisInDegreesPerSecond: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                           _type.HRESULT]
    put_ZAxisInDegreesPerSecond: _Callable[[_type.DOUBLE],  # value
                                           _type.HRESULT]


class IGyrometerDeviceId(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]


class IGyrometerReading(_inspectable.IInspectable):
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_AngularVelocityX: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]
    get_AngularVelocityY: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]
    get_AngularVelocityZ: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]


class IGyrometerReading2(_inspectable.IInspectable):
    get_PerformanceCount: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                    _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _inspectable.IInspectable]]],  # value
                              _type.HRESULT]


class IGyrometerReadingChangedEventArgs(_inspectable.IInspectable):
    get_Reading: _Callable[[_Pointer[IGyrometerReading]],  # value
                           _type.HRESULT]


class IGyrometerStatics(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[IGyrometer]],  # result
                          _type.HRESULT]


class IGyrometerStatics2(_inspectable.IInspectable, factory=True):
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IGyrometer]]],  # operation
                           _type.HRESULT]


class IHingeAngleReading(_inspectable.IInspectable):
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_AngleInDegrees: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _inspectable.IInspectable]]],  # value
                              _type.HRESULT]


class IHingeAngleSensor(_inspectable.IInspectable):
    GetCurrentReadingAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IHingeAngleReading]]],  # value
                                      _type.HRESULT]
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_MinReportThresholdInDegrees: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                               _type.HRESULT]
    get_ReportThresholdInDegrees: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                            _type.HRESULT]
    put_ReportThresholdInDegrees: _Callable[[_type.DOUBLE],  # value
                                            _type.HRESULT]
    add_ReadingChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IHingeAngleSensor, IHingeAngleSensorReadingChangedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_ReadingChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]


class IHingeAngleSensorReadingChangedEventArgs(_inspectable.IInspectable):
    get_Reading: _Callable[[_Pointer[IHingeAngleReading]],  # value
                           _type.HRESULT]


class IHingeAngleSensorStatics(_inspectable.IInspectable, factory=True):
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]
    GetDefaultAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IHingeAngleSensor]]],  # result
                               _type.HRESULT]
    GetRelatedToAdjacentPanelsAsync: _Callable[[_type.HSTRING,  # firstPanelId
                                                _type.HSTRING,  # secondPanelId
                                                _Pointer[_Windows_Foundation.IAsyncOperation[IHingeAngleSensor]]],  # result
                                               _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IHingeAngleSensor]]],  # result
                           _type.HRESULT]


class IHumanPresenceFeatures(_inspectable.IInspectable):
    get_SensorId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_SupportedWakeOrLockDistancesInMillimeters: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.UINT32]]],  # value
                                                             _type.HRESULT]
    get_IsWakeOnApproachSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    get_IsLockOnLeaveSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    IsAttentionAwareDimmingSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                _type.HRESULT]


class IHumanPresenceFeatures2(_inspectable.IInspectable):
    get_IsAdaptiveDimmingSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]


class IHumanPresenceSensor(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_MaxDetectableDistanceInMillimeters: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                                                      _type.HRESULT]
    get_MinDetectableDistanceInMillimeters: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                                                      _type.HRESULT]
    GetCurrentReading: _Callable[[_Pointer[IHumanPresenceSensorReading]],  # result
                                 _type.HRESULT]
    add_ReadingChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IHumanPresenceSensor, IHumanPresenceSensorReadingChangedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_ReadingChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]


class IHumanPresenceSensor2(_inspectable.IInspectable):
    get_IsPresenceSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    get_IsEngagementSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]


class IHumanPresenceSensorReading(_inspectable.IInspectable):
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_Presence: _Callable[[_Pointer[_enum.Windows.Devices.Sensors.HumanPresence]],  # value
                            _type.HRESULT]
    get_Engagement: _Callable[[_Pointer[_enum.Windows.Devices.Sensors.HumanEngagement]],  # value
                              _type.HRESULT]
    get_DistanceInMillimeters: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                                         _type.HRESULT]


class IHumanPresenceSensorReadingChangedEventArgs(_inspectable.IInspectable):
    get_Reading: _Callable[[_Pointer[IHumanPresenceSensorReading]],  # value
                           _type.HRESULT]


class IHumanPresenceSensorStatics(_inspectable.IInspectable, factory=True):
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # sensorId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IHumanPresenceSensor]]],  # operation
                           _type.HRESULT]
    GetDefaultAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IHumanPresenceSensor]]],  # operation
                               _type.HRESULT]


class IHumanPresenceSensorStatics2(_inspectable.IInspectable, factory=True):
    FromId: _Callable[[_type.HSTRING,  # sensorId
                       _Pointer[IHumanPresenceSensor]],  # result
                      _type.HRESULT]
    GetDefault: _Callable[[_Pointer[IHumanPresenceSensor]],  # result
                          _type.HRESULT]


class IHumanPresenceSettings(_inspectable.IInspectable):
    get_SensorId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_SensorId: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_IsWakeOnApproachEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    put_IsWakeOnApproachEnabled: _Callable[[_type.boolean],  # value
                                           _type.HRESULT]
    get_WakeOnApproachDistanceInMillimeters: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                                                       _type.HRESULT]
    put_WakeOnApproachDistanceInMillimeters: _Callable[[_Windows_Foundation.IReference[_type.UINT32]],  # value
                                                       _type.HRESULT]
    get_IsLockOnLeaveEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    put_IsLockOnLeaveEnabled: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]
    get_LockOnLeaveDistanceInMillimeters: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                                                    _type.HRESULT]
    put_LockOnLeaveDistanceInMillimeters: _Callable[[_Windows_Foundation.IReference[_type.UINT32]],  # value
                                                    _type.HRESULT]
    get_LockOnLeaveTimeout: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                      _type.HRESULT]
    put_LockOnLeaveTimeout: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                      _type.HRESULT]
    IsAttentionAwareDimmingEnabled: _Callable[[_type.boolean],  # value
                                              _type.HRESULT]


class IHumanPresenceSettings2(_inspectable.IInspectable):
    get_IsAdaptiveDimmingEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_IsAdaptiveDimmingEnabled: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]
    get_WakeOptions: _Callable[[_Pointer[IWakeOnApproachOptions]],  # value
                               _type.HRESULT]
    get_DimmingOptions: _Callable[[_Pointer[IAdaptiveDimmingOptions]],  # value
                                  _type.HRESULT]
    get_LockOptions: _Callable[[_Pointer[ILockOnLeaveOptions]],  # value
                               _type.HRESULT]


class IHumanPresenceSettingsStatics(_inspectable.IInspectable, factory=True):
    GetCurrentSettingsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IHumanPresenceSettings]]],  # operation
                                       _type.HRESULT]
    GetCurrentSettings: _Callable[[_Pointer[IHumanPresenceSettings]],  # result
                                  _type.HRESULT]
    UpdateSettingsAsync: _Callable[[IHumanPresenceSettings,  # settings
                                    _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                   _type.HRESULT]
    UpdateSettings: _Callable[[IHumanPresenceSettings],  # settings
                              _type.HRESULT]
    GetSupportedFeaturesForSensorIdAsync: _Callable[[_type.HSTRING,  # sensorId
                                                     _Pointer[_Windows_Foundation.IAsyncOperation[IHumanPresenceFeatures]]],  # operation
                                                    _type.HRESULT]
    GetSupportedFeaturesForSensorId: _Callable[[_type.HSTRING,  # sensorId
                                                _Pointer[IHumanPresenceFeatures]],  # result
                                               _type.HRESULT]
    GetSupportedLockOnLeaveTimeouts: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_struct.Windows.Foundation.TimeSpan]]],  # result
                                               _type.HRESULT]
    add_SettingsChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_SettingsChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]


class IInclinometer(_inspectable.IInspectable):
    GetCurrentReading: _Callable[[_Pointer[IInclinometerReading]],  # value
                                 _type.HRESULT]
    get_MinimumReportInterval: _Callable[[_Pointer[_type.UINT32]],  # value
                                         _type.HRESULT]
    put_ReportInterval: _Callable[[_type.UINT32],  # value
                                  _type.HRESULT]
    get_ReportInterval: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]
    add_ReadingChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IInclinometer, IInclinometerReadingChangedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_ReadingChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]


class IInclinometer2(_inspectable.IInspectable):
    put_ReadingTransform: _Callable[[_enum.Windows.Graphics.Display.DisplayOrientations],  # value
                                    _type.HRESULT]
    get_ReadingTransform: _Callable[[_Pointer[_enum.Windows.Graphics.Display.DisplayOrientations]],  # value
                                    _type.HRESULT]
    get_ReadingType: _Callable[[_Pointer[_enum.Windows.Devices.Sensors.SensorReadingType]],  # type
                               _type.HRESULT]


class IInclinometer3(_inspectable.IInspectable):
    put_ReportLatency: _Callable[[_type.UINT32],  # value
                                 _type.HRESULT]
    get_ReportLatency: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    get_MaxBatchSize: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]


class IInclinometer4(_inspectable.IInspectable):
    get_ReportThreshold: _Callable[[_Pointer[IInclinometerDataThreshold]],  # value
                                   _type.HRESULT]


class IInclinometerDataThreshold(_inspectable.IInspectable):
    get_PitchInDegrees: _Callable[[_Pointer[_type.FLOAT]],  # value
                                  _type.HRESULT]
    put_PitchInDegrees: _Callable[[_type.FLOAT],  # value
                                  _type.HRESULT]
    get_RollInDegrees: _Callable[[_Pointer[_type.FLOAT]],  # value
                                 _type.HRESULT]
    put_RollInDegrees: _Callable[[_type.FLOAT],  # value
                                 _type.HRESULT]
    get_YawInDegrees: _Callable[[_Pointer[_type.FLOAT]],  # value
                                _type.HRESULT]
    put_YawInDegrees: _Callable[[_type.FLOAT],  # value
                                _type.HRESULT]


class IInclinometerDeviceId(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]


class IInclinometerReading(_inspectable.IInspectable):
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_PitchDegrees: _Callable[[_Pointer[_type.FLOAT]],  # value
                                _type.HRESULT]
    get_RollDegrees: _Callable[[_Pointer[_type.FLOAT]],  # value
                               _type.HRESULT]
    get_YawDegrees: _Callable[[_Pointer[_type.FLOAT]],  # value
                              _type.HRESULT]


class IInclinometerReading2(_inspectable.IInspectable):
    get_PerformanceCount: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                    _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _inspectable.IInspectable]]],  # value
                              _type.HRESULT]


class IInclinometerReadingChangedEventArgs(_inspectable.IInspectable):
    get_Reading: _Callable[[_Pointer[IInclinometerReading]],  # value
                           _type.HRESULT]


class IInclinometerReadingYawAccuracy(_inspectable.IInspectable):
    get_YawAccuracy: _Callable[[_Pointer[_enum.Windows.Devices.Sensors.MagnetometerAccuracy]],  # value
                               _type.HRESULT]


class IInclinometerStatics(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[IInclinometer]],  # result
                          _type.HRESULT]


class IInclinometerStatics2(_inspectable.IInspectable, factory=True):
    GetDefaultForRelativeReadings: _Callable[[_Pointer[IInclinometer]],  # result
                                             _type.HRESULT]


class IInclinometerStatics3(_inspectable.IInspectable, factory=True):
    GetDefaultWithSensorReadingType: _Callable[[_enum.Windows.Devices.Sensors.SensorReadingType,  # sensorReadingtype
                                                _Pointer[IInclinometer]],  # result
                                               _type.HRESULT]


class IInclinometerStatics4(_inspectable.IInspectable, factory=True):
    GetDeviceSelector: _Callable[[_enum.Windows.Devices.Sensors.SensorReadingType,  # readingType
                                  _Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IInclinometer]]],  # operation
                           _type.HRESULT]


class ILightSensor(_inspectable.IInspectable):
    GetCurrentReading: _Callable[[_Pointer[ILightSensorReading]],  # value
                                 _type.HRESULT]
    get_MinimumReportInterval: _Callable[[_Pointer[_type.UINT32]],  # value
                                         _type.HRESULT]
    put_ReportInterval: _Callable[[_type.UINT32],  # value
                                  _type.HRESULT]
    get_ReportInterval: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]
    add_ReadingChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ILightSensor, ILightSensorReadingChangedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_ReadingChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]


class ILightSensor2(_inspectable.IInspectable):
    put_ReportLatency: _Callable[[_type.UINT32],  # value
                                 _type.HRESULT]
    get_ReportLatency: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    get_MaxBatchSize: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]


class ILightSensor3(_inspectable.IInspectable):
    get_ReportThreshold: _Callable[[_Pointer[ILightSensorDataThreshold]],  # value
                                   _type.HRESULT]


class ILightSensorDataThreshold(_inspectable.IInspectable):
    get_LuxPercentage: _Callable[[_Pointer[_type.FLOAT]],  # value
                                 _type.HRESULT]
    put_LuxPercentage: _Callable[[_type.FLOAT],  # value
                                 _type.HRESULT]
    get_AbsoluteLux: _Callable[[_Pointer[_type.FLOAT]],  # value
                               _type.HRESULT]
    put_AbsoluteLux: _Callable[[_type.FLOAT],  # value
                               _type.HRESULT]


class ILightSensorDeviceId(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]


class ILightSensorReading(_inspectable.IInspectable):
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_IlluminanceInLux: _Callable[[_Pointer[_type.FLOAT]],  # value
                                    _type.HRESULT]


class ILightSensorReading2(_inspectable.IInspectable):
    get_PerformanceCount: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                    _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _inspectable.IInspectable]]],  # value
                              _type.HRESULT]


class ILightSensorReadingChangedEventArgs(_inspectable.IInspectable):
    get_Reading: _Callable[[_Pointer[ILightSensorReading]],  # value
                           _type.HRESULT]


class ILightSensorStatics(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[ILightSensor]],  # result
                          _type.HRESULT]


class ILightSensorStatics2(_inspectable.IInspectable, factory=True):
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[ILightSensor]]],  # operation
                           _type.HRESULT]


class ILockOnLeaveOptions(_inspectable.IInspectable):
    get_AllowWhenExternalDisplayConnected: _Callable[[_Pointer[_type.boolean]],  # value
                                                     _type.HRESULT]
    put_AllowWhenExternalDisplayConnected: _Callable[[_type.boolean],  # value
                                                     _type.HRESULT]


class IMagnetometer(_inspectable.IInspectable):
    GetCurrentReading: _Callable[[_Pointer[IMagnetometerReading]],  # value
                                 _type.HRESULT]
    get_MinimumReportInterval: _Callable[[_Pointer[_type.UINT32]],  # value
                                         _type.HRESULT]
    put_ReportInterval: _Callable[[_type.UINT32],  # value
                                  _type.HRESULT]
    get_ReportInterval: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]
    add_ReadingChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMagnetometer, IMagnetometerReadingChangedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_ReadingChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]


class IMagnetometer2(_inspectable.IInspectable):
    put_ReadingTransform: _Callable[[_enum.Windows.Graphics.Display.DisplayOrientations],  # value
                                    _type.HRESULT]
    get_ReadingTransform: _Callable[[_Pointer[_enum.Windows.Graphics.Display.DisplayOrientations]],  # value
                                    _type.HRESULT]


class IMagnetometer3(_inspectable.IInspectable):
    put_ReportLatency: _Callable[[_type.UINT32],  # value
                                 _type.HRESULT]
    get_ReportLatency: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    get_MaxBatchSize: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]


class IMagnetometer4(_inspectable.IInspectable):
    get_ReportThreshold: _Callable[[_Pointer[IMagnetometerDataThreshold]],  # value
                                   _type.HRESULT]


class IMagnetometerDataThreshold(_inspectable.IInspectable):
    get_XAxisMicroteslas: _Callable[[_Pointer[_type.FLOAT]],  # value
                                    _type.HRESULT]
    put_XAxisMicroteslas: _Callable[[_type.FLOAT],  # value
                                    _type.HRESULT]
    get_YAxisMicroteslas: _Callable[[_Pointer[_type.FLOAT]],  # value
                                    _type.HRESULT]
    put_YAxisMicroteslas: _Callable[[_type.FLOAT],  # value
                                    _type.HRESULT]
    get_ZAxisMicroteslas: _Callable[[_Pointer[_type.FLOAT]],  # value
                                    _type.HRESULT]
    put_ZAxisMicroteslas: _Callable[[_type.FLOAT],  # value
                                    _type.HRESULT]


class IMagnetometerDeviceId(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]


class IMagnetometerReading(_inspectable.IInspectable):
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_MagneticFieldX: _Callable[[_Pointer[_type.FLOAT]],  # value
                                  _type.HRESULT]
    get_MagneticFieldY: _Callable[[_Pointer[_type.FLOAT]],  # value
                                  _type.HRESULT]
    get_MagneticFieldZ: _Callable[[_Pointer[_type.FLOAT]],  # value
                                  _type.HRESULT]
    get_DirectionalAccuracy: _Callable[[_Pointer[_enum.Windows.Devices.Sensors.MagnetometerAccuracy]],  # value
                                       _type.HRESULT]


class IMagnetometerReading2(_inspectable.IInspectable):
    get_PerformanceCount: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                    _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _inspectable.IInspectable]]],  # value
                              _type.HRESULT]


class IMagnetometerReadingChangedEventArgs(_inspectable.IInspectable):
    get_Reading: _Callable[[_Pointer[IMagnetometerReading]],  # value
                           _type.HRESULT]


class IMagnetometerStatics(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[IMagnetometer]],  # result
                          _type.HRESULT]


class IMagnetometerStatics2(_inspectable.IInspectable, factory=True):
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IMagnetometer]]],  # operation
                           _type.HRESULT]


class IOrientationSensor(_inspectable.IInspectable):
    GetCurrentReading: _Callable[[_Pointer[IOrientationSensorReading]],  # value
                                 _type.HRESULT]
    get_MinimumReportInterval: _Callable[[_Pointer[_type.UINT32]],  # value
                                         _type.HRESULT]
    put_ReportInterval: _Callable[[_type.UINT32],  # value
                                  _type.HRESULT]
    get_ReportInterval: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]
    add_ReadingChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IOrientationSensor, IOrientationSensorReadingChangedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_ReadingChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]


class IOrientationSensor2(_inspectable.IInspectable):
    put_ReadingTransform: _Callable[[_enum.Windows.Graphics.Display.DisplayOrientations],  # value
                                    _type.HRESULT]
    get_ReadingTransform: _Callable[[_Pointer[_enum.Windows.Graphics.Display.DisplayOrientations]],  # value
                                    _type.HRESULT]
    get_ReadingType: _Callable[[_Pointer[_enum.Windows.Devices.Sensors.SensorReadingType]],  # type
                               _type.HRESULT]


class IOrientationSensor3(_inspectable.IInspectable):
    put_ReportLatency: _Callable[[_type.UINT32],  # value
                                 _type.HRESULT]
    get_ReportLatency: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    get_MaxBatchSize: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]


class IOrientationSensorDeviceId(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]


class IOrientationSensorReading(_inspectable.IInspectable):
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_RotationMatrix: _Callable[[_Pointer[ISensorRotationMatrix]],  # value
                                  _type.HRESULT]
    get_Quaternion: _Callable[[_Pointer[ISensorQuaternion]],  # value
                              _type.HRESULT]


class IOrientationSensorReading2(_inspectable.IInspectable):
    get_PerformanceCount: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                    _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _inspectable.IInspectable]]],  # value
                              _type.HRESULT]


class IOrientationSensorReadingChangedEventArgs(_inspectable.IInspectable):
    get_Reading: _Callable[[_Pointer[IOrientationSensorReading]],  # value
                           _type.HRESULT]


class IOrientationSensorReadingYawAccuracy(_inspectable.IInspectable):
    get_YawAccuracy: _Callable[[_Pointer[_enum.Windows.Devices.Sensors.MagnetometerAccuracy]],  # value
                               _type.HRESULT]


class IOrientationSensorStatics(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[IOrientationSensor]],  # result
                          _type.HRESULT]


class IOrientationSensorStatics2(_inspectable.IInspectable, factory=True):
    GetDefaultForRelativeReadings: _Callable[[_Pointer[IOrientationSensor]],  # result
                                             _type.HRESULT]


class IOrientationSensorStatics3(_inspectable.IInspectable, factory=True):
    GetDefaultWithSensorReadingType: _Callable[[_enum.Windows.Devices.Sensors.SensorReadingType,  # sensorReadingtype
                                                _Pointer[IOrientationSensor]],  # result
                                               _type.HRESULT]
    GetDefaultWithSensorReadingTypeAndSensorOptimizationGoal: _Callable[[_enum.Windows.Devices.Sensors.SensorReadingType,  # sensorReadingType
                                                                         _enum.Windows.Devices.Sensors.SensorOptimizationGoal,  # optimizationGoal
                                                                         _Pointer[IOrientationSensor]],  # result
                                                                        _type.HRESULT]


class IOrientationSensorStatics4(_inspectable.IInspectable, factory=True):
    GetDeviceSelector: _Callable[[_enum.Windows.Devices.Sensors.SensorReadingType,  # readingType
                                  _Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]
    GetDeviceSelectorWithSensorReadingTypeAndSensorOptimizationGoal: _Callable[[_enum.Windows.Devices.Sensors.SensorReadingType,  # readingType
                                                                                _enum.Windows.Devices.Sensors.SensorOptimizationGoal,  # optimizationGoal
                                                                                _Pointer[_type.HSTRING]],  # result
                                                                               _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IOrientationSensor]]],  # operation
                           _type.HRESULT]


class IPedometer(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_PowerInMilliwatts: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                     _type.HRESULT]
    get_MinimumReportInterval: _Callable[[_Pointer[_type.UINT32]],  # value
                                         _type.HRESULT]
    put_ReportInterval: _Callable[[_type.UINT32],  # value
                                  _type.HRESULT]
    get_ReportInterval: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]
    add_ReadingChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IPedometer, IPedometerReadingChangedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_ReadingChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]


class IPedometer2(_inspectable.IInspectable):
    GetCurrentReadings: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_enum.Windows.Devices.Sensors.PedometerStepKind, IPedometerReading]]],  # value
                                  _type.HRESULT]


class IPedometerDataThresholdFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[IPedometer,  # sensor
                       _type.INT32,  # stepGoal
                       _Pointer[ISensorDataThreshold]],  # threshold
                      _type.HRESULT]


class IPedometerReading(_inspectable.IInspectable):
    get_StepKind: _Callable[[_Pointer[_enum.Windows.Devices.Sensors.PedometerStepKind]],  # value
                            _type.HRESULT]
    get_CumulativeSteps: _Callable[[_Pointer[_type.INT32]],  # value
                                   _type.HRESULT]
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_CumulativeStepsDuration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                           _type.HRESULT]


class IPedometerReadingChangedEventArgs(_inspectable.IInspectable):
    get_Reading: _Callable[[_Pointer[IPedometerReading]],  # value
                           _type.HRESULT]


class IPedometerStatics(_inspectable.IInspectable, factory=True):
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IPedometer]]],  # operation
                           _type.HRESULT]
    GetDefaultAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IPedometer]]],  # operation
                               _type.HRESULT]
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]
    GetSystemHistoryAsync: _Callable[[_struct.Windows.Foundation.DateTime,  # fromTime
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IPedometerReading]]]],  # operation
                                     _type.HRESULT]
    GetSystemHistoryWithDurationAsync: _Callable[[_struct.Windows.Foundation.DateTime,  # fromTime
                                                  _struct.Windows.Foundation.TimeSpan,  # duration
                                                  _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IPedometerReading]]]],  # operation
                                                 _type.HRESULT]


class IPedometerStatics2(_inspectable.IInspectable, factory=True):
    GetReadingsFromTriggerDetails: _Callable[[ISensorDataThresholdTriggerDetails,  # triggerDetails
                                              _Pointer[_Windows_Foundation_Collections.IVectorView[IPedometerReading]]],  # result
                                             _type.HRESULT]


class IProximitySensor(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_MaxDistanceInMillimeters: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                                            _type.HRESULT]
    get_MinDistanceInMillimeters: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                                            _type.HRESULT]
    GetCurrentReading: _Callable[[_Pointer[IProximitySensorReading]],  # value
                                 _type.HRESULT]
    add_ReadingChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IProximitySensor, IProximitySensorReadingChangedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_ReadingChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    CreateDisplayOnOffController: _Callable[[_Pointer[_Windows_Foundation.IClosable]],  # controller
                                            _type.HRESULT]


class IProximitySensorDataThresholdFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[IProximitySensor,  # sensor
                       _Pointer[ISensorDataThreshold]],  # threshold
                      _type.HRESULT]


class IProximitySensorReading(_inspectable.IInspectable):
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_IsDetected: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_DistanceInMillimeters: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                                         _type.HRESULT]


class IProximitySensorReadingChangedEventArgs(_inspectable.IInspectable):
    get_Reading: _Callable[[_Pointer[IProximitySensorReading]],  # value
                           _type.HRESULT]


class IProximitySensorStatics(_inspectable.IInspectable, factory=True):
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    FromId: _Callable[[_type.HSTRING,  # sensorId
                       _Pointer[IProximitySensor]],  # result
                      _type.HRESULT]


class IProximitySensorStatics2(_inspectable.IInspectable, factory=True):
    GetReadingsFromTriggerDetails: _Callable[[ISensorDataThresholdTriggerDetails,  # triggerDetails
                                              _Pointer[_Windows_Foundation_Collections.IVectorView[IProximitySensorReading]]],  # result
                                             _type.HRESULT]


class ISensorDataThreshold(_inspectable.IInspectable):
    pass


class ISensorDataThresholdTriggerDetails(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_SensorType: _Callable[[_Pointer[_enum.Windows.Devices.Sensors.SensorType]],  # value
                              _type.HRESULT]


class ISensorQuaternion(_inspectable.IInspectable):
    get_W: _Callable[[_Pointer[_type.FLOAT]],  # value
                     _type.HRESULT]
    get_X: _Callable[[_Pointer[_type.FLOAT]],  # value
                     _type.HRESULT]
    get_Y: _Callable[[_Pointer[_type.FLOAT]],  # value
                     _type.HRESULT]
    get_Z: _Callable[[_Pointer[_type.FLOAT]],  # value
                     _type.HRESULT]


class ISensorRotationMatrix(_inspectable.IInspectable):
    get_M11: _Callable[[_Pointer[_type.FLOAT]],  # value
                       _type.HRESULT]
    get_M12: _Callable[[_Pointer[_type.FLOAT]],  # value
                       _type.HRESULT]
    get_M13: _Callable[[_Pointer[_type.FLOAT]],  # value
                       _type.HRESULT]
    get_M21: _Callable[[_Pointer[_type.FLOAT]],  # value
                       _type.HRESULT]
    get_M22: _Callable[[_Pointer[_type.FLOAT]],  # value
                       _type.HRESULT]
    get_M23: _Callable[[_Pointer[_type.FLOAT]],  # value
                       _type.HRESULT]
    get_M31: _Callable[[_Pointer[_type.FLOAT]],  # value
                       _type.HRESULT]
    get_M32: _Callable[[_Pointer[_type.FLOAT]],  # value
                       _type.HRESULT]
    get_M33: _Callable[[_Pointer[_type.FLOAT]],  # value
                       _type.HRESULT]


class ISimpleOrientationSensor(_inspectable.IInspectable):
    GetCurrentOrientation: _Callable[[_Pointer[_enum.Windows.Devices.Sensors.SimpleOrientation]],  # value
                                     _type.HRESULT]
    add_OrientationChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ISimpleOrientationSensor, ISimpleOrientationSensorOrientationChangedEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_OrientationChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]


class ISimpleOrientationSensor2(_inspectable.IInspectable):
    put_ReadingTransform: _Callable[[_enum.Windows.Graphics.Display.DisplayOrientations],  # value
                                    _type.HRESULT]
    get_ReadingTransform: _Callable[[_Pointer[_enum.Windows.Graphics.Display.DisplayOrientations]],  # value
                                    _type.HRESULT]


class ISimpleOrientationSensorDeviceId(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]


class ISimpleOrientationSensorOrientationChangedEventArgs(_inspectable.IInspectable):
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_Orientation: _Callable[[_Pointer[_enum.Windows.Devices.Sensors.SimpleOrientation]],  # value
                               _type.HRESULT]


class ISimpleOrientationSensorStatics(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[ISimpleOrientationSensor]],  # result
                          _type.HRESULT]


class ISimpleOrientationSensorStatics2(_inspectable.IInspectable, factory=True):
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[ISimpleOrientationSensor]]],  # result
                           _type.HRESULT]


class IWakeOnApproachOptions(_inspectable.IInspectable):
    get_AllowWhenExternalDisplayConnected: _Callable[[_Pointer[_type.boolean]],  # value
                                                     _type.HRESULT]
    put_AllowWhenExternalDisplayConnected: _Callable[[_type.boolean],  # value
                                                     _type.HRESULT]
    get_DisableWhenBatterySaverOn: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    put_DisableWhenBatterySaverOn: _Callable[[_type.boolean],  # value
                                             _type.HRESULT]
