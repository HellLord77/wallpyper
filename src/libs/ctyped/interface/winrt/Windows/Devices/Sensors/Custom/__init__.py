from __future__ import annotations as _

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class ICustomSensor(_inspectable.IInspectable):
    GetCurrentReading: _Callable[[_Pointer[ICustomSensorReading]],  # value
                                 _type.HRESULT]
    get_MinimumReportInterval: _Callable[[_Pointer[_type.UINT32]],  # value
                                         _type.HRESULT]
    put_ReportInterval: _Callable[[_type.UINT32],  # value
                                  _type.HRESULT]
    get_ReportInterval: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    add_ReadingChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ICustomSensor, ICustomSensorReadingChangedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_ReadingChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]


class ICustomSensor2(_inspectable.IInspectable):
    put_ReportLatency: _Callable[[_type.UINT32],  # value
                                 _type.HRESULT]
    get_ReportLatency: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    get_MaxBatchSize: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]


class ICustomSensorReading(_inspectable.IInspectable):
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _inspectable.IInspectable]]],  # value
                              _type.HRESULT]


class ICustomSensorReading2(_inspectable.IInspectable):
    get_PerformanceCount: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                    _type.HRESULT]


class ICustomSensorReadingChangedEventArgs(_inspectable.IInspectable):
    get_Reading: _Callable[[_Pointer[ICustomSensorReading]],  # value
                           _type.HRESULT]


class ICustomSensorStatics(_inspectable.IInspectable):
    GetDeviceSelector: _Callable[[_struct.GUID,  # interfaceId
                                  _Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # sensorId
                            _Pointer[_Windows_Foundation.IAsyncOperation[ICustomSensor]]],  # result
                           _type.HRESULT]

    _factory = True
