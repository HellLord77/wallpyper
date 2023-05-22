from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import Media as _Windows_Media
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Media.Devices import Core as _Windows_Media_Devices_Core
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IKnownCameraIntrinsicsPropertiesStatics(_inspectable.IInspectable, factory=True):
    FocalLength: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    PrincipalPoint: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    RadialDistortion: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    TangentialDistortion: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]


class IKnownPerceptionColorFrameSourcePropertiesStatics(_inspectable.IInspectable, factory=True):
    Exposure: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    AutoExposureEnabled: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    ExposureCompensation: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]


class IKnownPerceptionDepthFrameSourcePropertiesStatics(_inspectable.IInspectable, factory=True):
    MinDepth: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    MaxDepth: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class IKnownPerceptionFrameSourcePropertiesStatics(_inspectable.IInspectable, factory=True):
    Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                  _type.HRESULT]
    PhysicalDeviceIds: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    FrameKind: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    DeviceModelVersion: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    EnclosureLocation: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]


class IKnownPerceptionFrameSourcePropertiesStatics2(_inspectable.IInspectable, factory=True):
    DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class IKnownPerceptionInfraredFrameSourcePropertiesStatics(_inspectable.IInspectable, factory=True):
    Exposure: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    AutoExposureEnabled: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    ExposureCompensation: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    ActiveIlluminationEnabled: _Callable[[_Pointer[_type.HSTRING]],  # value
                                         _type.HRESULT]
    AmbientSubtractionEnabled: _Callable[[_Pointer[_type.HSTRING]],  # value
                                         _type.HRESULT]
    StructureLightPatternEnabled: _Callable[[_Pointer[_type.HSTRING]],  # value
                                            _type.HRESULT]
    InterleavedIlluminationEnabled: _Callable[[_Pointer[_type.HSTRING]],  # value
                                              _type.HRESULT]


class IKnownPerceptionVideoFrameSourcePropertiesStatics(_inspectable.IInspectable, factory=True):
    VideoProfile: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    SupportedVideoProfiles: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    AvailableVideoProfiles: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    IsMirrored: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    CameraIntrinsics: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]


class IKnownPerceptionVideoProfilePropertiesStatics(_inspectable.IInspectable, factory=True):
    BitmapPixelFormat: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    BitmapAlphaMode: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    Width: _Callable[[_Pointer[_type.HSTRING]],  # value
                     _type.HRESULT]
    Height: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    FrameDuration: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]


class IPerceptionColorFrame(_inspectable.IInspectable):
    VideoFrame: _Callable[[_Pointer[_Windows_Media.IVideoFrame]],  # value
                          _type.HRESULT]


class IPerceptionColorFrameArrivedEventArgs(_inspectable.IInspectable):
    RelativeTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    TryOpenFrame: _Callable[[_Pointer[IPerceptionColorFrame]],  # result
                            _type.HRESULT]


class IPerceptionColorFrameReader(_inspectable.IInspectable):
    FrameArrived: _Callable[[_struct.EventRegistrationToken],  # token
                            _type.HRESULT]
    Source: _Callable[[_Pointer[IPerceptionColorFrameSource]],  # value
                      _type.HRESULT]
    IsPaused: _Callable[[_type.boolean],  # value
                        _type.HRESULT]
    TryReadLatestFrame: _Callable[[_Pointer[IPerceptionColorFrame]],  # result
                                  _type.HRESULT]


class IPerceptionColorFrameSource(_inspectable.IInspectable):
    AvailableChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    ActiveChanged: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    PropertiesChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                 _type.HRESULT]
    VideoProfileChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    CameraIntrinsicsChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                  _type.HRESULT]
    DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    DeviceKind: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    Available: _Callable[[_Pointer[_type.boolean]],  # value
                         _type.HRESULT]
    Active: _Callable[[_Pointer[_type.boolean]],  # value
                      _type.HRESULT]
    IsControlled: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _inspectable.IInspectable]]],  # value
                          _type.HRESULT]
    SupportedVideoProfiles: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IPerceptionVideoProfile]]],  # value
                                      _type.HRESULT]
    AvailableVideoProfiles: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IPerceptionVideoProfile]]],  # value
                                      _type.HRESULT]
    VideoProfile: _Callable[[_Pointer[IPerceptionVideoProfile]],  # value
                            _type.HRESULT]
    CameraIntrinsics: _Callable[[_Pointer[_Windows_Media_Devices_Core.ICameraIntrinsics]],  # value
                                _type.HRESULT]
    AcquireControlSession: _Callable[[_Pointer[IPerceptionControlSession]],  # value
                                     _type.HRESULT]
    CanControlIndependentlyFrom: _Callable[[_type.HSTRING,  # targetId
                                            _Pointer[_type.boolean]],  # result
                                           _type.HRESULT]
    IsCorrelatedWith: _Callable[[_type.HSTRING,  # targetId
                                 _Pointer[_type.boolean]],  # result
                                _type.HRESULT]
    TryGetTransformTo: _Callable[[_type.HSTRING,  # targetId
                                  _Pointer[_struct.Windows.Foundation.Numerics.Matrix4x4],  # result
                                  _Pointer[_type.boolean]],  # hasResult
                                 _type.HRESULT]
    TryGetDepthCorrelatedCameraIntrinsicsAsync: _Callable[[IPerceptionDepthFrameSource,  # correlatedDepthFrameSource
                                                           _Pointer[_Windows_Foundation.IAsyncOperation[IPerceptionDepthCorrelatedCameraIntrinsics]]],  # result
                                                          _type.HRESULT]
    TryGetDepthCorrelatedCoordinateMapperAsync: _Callable[[_type.HSTRING,  # targetSourceId
                                                           IPerceptionDepthFrameSource,  # correlatedDepthFrameSource
                                                           _Pointer[_Windows_Foundation.IAsyncOperation[IPerceptionDepthCorrelatedCoordinateMapper]]],  # result
                                                          _type.HRESULT]
    TrySetVideoProfileAsync: _Callable[[IPerceptionControlSession,  # controlSession
                                        IPerceptionVideoProfile,  # profile
                                        _Pointer[_Windows_Foundation.IAsyncOperation[IPerceptionFrameSourcePropertyChangeResult]]],  # result
                                       _type.HRESULT]
    OpenReader: _Callable[[_Pointer[IPerceptionColorFrameReader]],  # result
                          _type.HRESULT]


class IPerceptionColorFrameSource2(_inspectable.IInspectable):
    DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class IPerceptionColorFrameSourceAddedEventArgs(_inspectable.IInspectable):
    FrameSource: _Callable[[_Pointer[IPerceptionColorFrameSource]],  # value
                           _type.HRESULT]


class IPerceptionColorFrameSourceRemovedEventArgs(_inspectable.IInspectable):
    FrameSource: _Callable[[_Pointer[IPerceptionColorFrameSource]],  # value
                           _type.HRESULT]


class IPerceptionColorFrameSourceStatics(_inspectable.IInspectable, factory=True):
    CreateWatcher: _Callable[[_Pointer[IPerceptionColorFrameSourceWatcher]],  # watcher
                             _type.HRESULT]
    FindAllAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IPerceptionColorFrameSource]]]],  # result
                            _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # id
                            _Pointer[_Windows_Foundation.IAsyncOperation[IPerceptionColorFrameSource]]],  # result
                           _type.HRESULT]
    RequestAccessAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Devices.Perception.PerceptionFrameSourceAccessStatus]]],  # result
                                  _type.HRESULT]


class IPerceptionColorFrameSourceWatcher(_inspectable.IInspectable):
    SourceAdded: _Callable[[_struct.EventRegistrationToken],  # token
                           _type.HRESULT]
    SourceRemoved: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    Stopped: _Callable[[_struct.EventRegistrationToken],  # token
                       _type.HRESULT]
    EnumerationCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    Status: _Callable[[_Pointer[_enum.Windows.Devices.Enumeration.DeviceWatcherStatus]],  # value
                      _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]


class IPerceptionControlSession(_inspectable.IInspectable):
    ControlLost: _Callable[[_struct.EventRegistrationToken],  # token
                           _type.HRESULT]
    TrySetPropertyAsync: _Callable[[_type.HSTRING,  # name
                                    _inspectable.IInspectable,  # value
                                    _Pointer[_Windows_Foundation.IAsyncOperation[IPerceptionFrameSourcePropertyChangeResult]]],  # result
                                   _type.HRESULT]


class IPerceptionDepthCorrelatedCameraIntrinsics(_inspectable.IInspectable):
    UnprojectPixelAtCorrelatedDepth: _Callable[[_struct.Windows.Foundation.Point,  # pixelCoordinate
                                                IPerceptionDepthFrame,  # depthFrame
                                                _Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # result
                                               _type.HRESULT]
    UnprojectPixelsAtCorrelatedDepth: _Callable[[_type.UINT32,  # __sourceCoordinatesSize
                                                 _Pointer[_struct.Windows.Foundation.Point],  # sourceCoordinates
                                                 IPerceptionDepthFrame,  # depthFrame
                                                 _type.UINT32,  # __resultsSize
                                                 _Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # results
                                                _type.HRESULT]
    UnprojectRegionPixelsAtCorrelatedDepthAsync: _Callable[[_struct.Windows.Foundation.Rect,  # region
                                                            IPerceptionDepthFrame,  # depthFrame
                                                            _type.UINT32,  # __resultsSize
                                                            _Pointer[_struct.Windows.Foundation.Numerics.Vector3],  # results
                                                            _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                                           _type.HRESULT]
    UnprojectAllPixelsAtCorrelatedDepthAsync: _Callable[[IPerceptionDepthFrame,  # depthFrame
                                                         _type.UINT32,  # __resultsSize
                                                         _Pointer[_struct.Windows.Foundation.Numerics.Vector3],  # results
                                                         _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                                        _type.HRESULT]


class IPerceptionDepthCorrelatedCoordinateMapper(_inspectable.IInspectable):
    MapPixelToTarget: _Callable[[_struct.Windows.Foundation.Point,  # sourcePixelCoordinate
                                 IPerceptionDepthFrame,  # depthFrame
                                 _Pointer[_struct.Windows.Foundation.Point]],  # result
                                _type.HRESULT]
    MapPixelsToTarget: _Callable[[_type.UINT32,  # __sourceCoordinatesSize
                                  _Pointer[_struct.Windows.Foundation.Point],  # sourceCoordinates
                                  IPerceptionDepthFrame,  # depthFrame
                                  _type.UINT32,  # __resultsSize
                                  _Pointer[_struct.Windows.Foundation.Point]],  # results
                                 _type.HRESULT]
    MapRegionOfPixelsToTargetAsync: _Callable[[_struct.Windows.Foundation.Rect,  # region
                                               IPerceptionDepthFrame,  # depthFrame
                                               _type.UINT32,  # __targetCoordinatesSize
                                               _Pointer[_struct.Windows.Foundation.Point],  # targetCoordinates
                                               _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                              _type.HRESULT]
    MapAllPixelsToTargetAsync: _Callable[[IPerceptionDepthFrame,  # depthFrame
                                          _type.UINT32,  # __targetCoordinatesSize
                                          _Pointer[_struct.Windows.Foundation.Point],  # targetCoordinates
                                          _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                         _type.HRESULT]


class IPerceptionDepthFrame(_inspectable.IInspectable):
    VideoFrame: _Callable[[_Pointer[_Windows_Media.IVideoFrame]],  # value
                          _type.HRESULT]


class IPerceptionDepthFrameArrivedEventArgs(_inspectable.IInspectable):
    RelativeTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    TryOpenFrame: _Callable[[_Pointer[IPerceptionDepthFrame]],  # result
                            _type.HRESULT]


class IPerceptionDepthFrameReader(_inspectable.IInspectable):
    FrameArrived: _Callable[[_struct.EventRegistrationToken],  # token
                            _type.HRESULT]
    Source: _Callable[[_Pointer[IPerceptionDepthFrameSource]],  # value
                      _type.HRESULT]
    IsPaused: _Callable[[_type.boolean],  # value
                        _type.HRESULT]
    TryReadLatestFrame: _Callable[[_Pointer[IPerceptionDepthFrame]],  # result
                                  _type.HRESULT]


class IPerceptionDepthFrameSource(_inspectable.IInspectable):
    AvailableChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    ActiveChanged: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    PropertiesChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                 _type.HRESULT]
    VideoProfileChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    CameraIntrinsicsChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                  _type.HRESULT]
    DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    DeviceKind: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    Available: _Callable[[_Pointer[_type.boolean]],  # value
                         _type.HRESULT]
    Active: _Callable[[_Pointer[_type.boolean]],  # value
                      _type.HRESULT]
    IsControlled: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _inspectable.IInspectable]]],  # value
                          _type.HRESULT]
    SupportedVideoProfiles: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IPerceptionVideoProfile]]],  # value
                                      _type.HRESULT]
    AvailableVideoProfiles: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IPerceptionVideoProfile]]],  # value
                                      _type.HRESULT]
    VideoProfile: _Callable[[_Pointer[IPerceptionVideoProfile]],  # value
                            _type.HRESULT]
    CameraIntrinsics: _Callable[[_Pointer[_Windows_Media_Devices_Core.ICameraIntrinsics]],  # value
                                _type.HRESULT]
    AcquireControlSession: _Callable[[_Pointer[IPerceptionControlSession]],  # result
                                     _type.HRESULT]
    CanControlIndependentlyFrom: _Callable[[_type.HSTRING,  # targetId
                                            _Pointer[_type.boolean]],  # result
                                           _type.HRESULT]
    IsCorrelatedWith: _Callable[[_type.HSTRING,  # targetId
                                 _Pointer[_type.boolean]],  # result
                                _type.HRESULT]
    TryGetTransformTo: _Callable[[_type.HSTRING,  # targetId
                                  _Pointer[_struct.Windows.Foundation.Numerics.Matrix4x4],  # result
                                  _Pointer[_type.boolean]],  # hasResult
                                 _type.HRESULT]
    TryGetDepthCorrelatedCameraIntrinsicsAsync: _Callable[[IPerceptionDepthFrameSource,  # target
                                                           _Pointer[_Windows_Foundation.IAsyncOperation[IPerceptionDepthCorrelatedCameraIntrinsics]]],  # result
                                                          _type.HRESULT]
    TryGetDepthCorrelatedCoordinateMapperAsync: _Callable[[_type.HSTRING,  # targetId
                                                           IPerceptionDepthFrameSource,  # depthFrameSourceToMapWith
                                                           _Pointer[_Windows_Foundation.IAsyncOperation[IPerceptionDepthCorrelatedCoordinateMapper]]],  # result
                                                          _type.HRESULT]
    TrySetVideoProfileAsync: _Callable[[IPerceptionControlSession,  # controlSession
                                        IPerceptionVideoProfile,  # profile
                                        _Pointer[_Windows_Foundation.IAsyncOperation[IPerceptionFrameSourcePropertyChangeResult]]],  # result
                                       _type.HRESULT]
    OpenReader: _Callable[[_Pointer[IPerceptionDepthFrameReader]],  # result
                          _type.HRESULT]


class IPerceptionDepthFrameSource2(_inspectable.IInspectable):
    DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class IPerceptionDepthFrameSourceAddedEventArgs(_inspectable.IInspectable):
    FrameSource: _Callable[[_Pointer[IPerceptionDepthFrameSource]],  # value
                           _type.HRESULT]


class IPerceptionDepthFrameSourceRemovedEventArgs(_inspectable.IInspectable):
    FrameSource: _Callable[[_Pointer[IPerceptionDepthFrameSource]],  # value
                           _type.HRESULT]


class IPerceptionDepthFrameSourceStatics(_inspectable.IInspectable, factory=True):
    CreateWatcher: _Callable[[_Pointer[IPerceptionDepthFrameSourceWatcher]],  # watcher
                             _type.HRESULT]
    FindAllAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IPerceptionDepthFrameSource]]]],  # result
                            _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # id
                            _Pointer[_Windows_Foundation.IAsyncOperation[IPerceptionDepthFrameSource]]],  # result
                           _type.HRESULT]
    RequestAccessAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Devices.Perception.PerceptionFrameSourceAccessStatus]]],  # result
                                  _type.HRESULT]


class IPerceptionDepthFrameSourceWatcher(_inspectable.IInspectable):
    SourceAdded: _Callable[[_struct.EventRegistrationToken],  # token
                           _type.HRESULT]
    SourceRemoved: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    Stopped: _Callable[[_struct.EventRegistrationToken],  # token
                       _type.HRESULT]
    EnumerationCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    Status: _Callable[[_Pointer[_enum.Windows.Devices.Enumeration.DeviceWatcherStatus]],  # value
                      _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]


class IPerceptionFrameSourcePropertiesChangedEventArgs(_inspectable.IInspectable):
    CollectionChange: _Callable[[_Pointer[_enum.Windows.Foundation.Collections.CollectionChange]],  # value
                                _type.HRESULT]
    Key: _Callable[[_Pointer[_type.HSTRING]],  # value
                   _type.HRESULT]


class IPerceptionFrameSourcePropertyChangeResult(_inspectable.IInspectable):
    Status: _Callable[[_Pointer[_enum.Windows.Devices.Perception.PerceptionFrameSourcePropertyChangeStatus]],  # value
                      _type.HRESULT]
    NewValue: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                        _type.HRESULT]


class IPerceptionInfraredFrame(_inspectable.IInspectable):
    VideoFrame: _Callable[[_Pointer[_Windows_Media.IVideoFrame]],  # value
                          _type.HRESULT]


class IPerceptionInfraredFrameArrivedEventArgs(_inspectable.IInspectable):
    RelativeTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    TryOpenFrame: _Callable[[_Pointer[IPerceptionInfraredFrame]],  # result
                            _type.HRESULT]


class IPerceptionInfraredFrameReader(_inspectable.IInspectable):
    FrameArrived: _Callable[[_struct.EventRegistrationToken],  # token
                            _type.HRESULT]
    Source: _Callable[[_Pointer[IPerceptionInfraredFrameSource]],  # value
                      _type.HRESULT]
    IsPaused: _Callable[[_type.boolean],  # value
                        _type.HRESULT]
    TryReadLatestFrame: _Callable[[_Pointer[IPerceptionInfraredFrame]],  # result
                                  _type.HRESULT]


class IPerceptionInfraredFrameSource(_inspectable.IInspectable):
    AvailableChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    ActiveChanged: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    PropertiesChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                 _type.HRESULT]
    VideoProfileChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    CameraIntrinsicsChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                  _type.HRESULT]
    DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    DeviceKind: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    Available: _Callable[[_Pointer[_type.boolean]],  # value
                         _type.HRESULT]
    Active: _Callable[[_Pointer[_type.boolean]],  # value
                      _type.HRESULT]
    IsControlled: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _inspectable.IInspectable]]],  # value
                          _type.HRESULT]
    SupportedVideoProfiles: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IPerceptionVideoProfile]]],  # value
                                      _type.HRESULT]
    AvailableVideoProfiles: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IPerceptionVideoProfile]]],  # value
                                      _type.HRESULT]
    VideoProfile: _Callable[[_Pointer[IPerceptionVideoProfile]],  # value
                            _type.HRESULT]
    CameraIntrinsics: _Callable[[_Pointer[_Windows_Media_Devices_Core.ICameraIntrinsics]],  # value
                                _type.HRESULT]
    AcquireControlSession: _Callable[[_Pointer[IPerceptionControlSession]],  # result
                                     _type.HRESULT]
    CanControlIndependentlyFrom: _Callable[[_type.HSTRING,  # targetId
                                            _Pointer[_type.boolean]],  # result
                                           _type.HRESULT]
    IsCorrelatedWith: _Callable[[_type.HSTRING,  # targetId
                                 _Pointer[_type.boolean]],  # result
                                _type.HRESULT]
    TryGetTransformTo: _Callable[[_type.HSTRING,  # targetId
                                  _Pointer[_struct.Windows.Foundation.Numerics.Matrix4x4],  # result
                                  _Pointer[_type.boolean]],  # hasResult
                                 _type.HRESULT]
    TryGetDepthCorrelatedCameraIntrinsicsAsync: _Callable[[IPerceptionDepthFrameSource,  # target
                                                           _Pointer[_Windows_Foundation.IAsyncOperation[IPerceptionDepthCorrelatedCameraIntrinsics]]],  # result
                                                          _type.HRESULT]
    TryGetDepthCorrelatedCoordinateMapperAsync: _Callable[[_type.HSTRING,  # targetId
                                                           IPerceptionDepthFrameSource,  # depthFrameSourceToMapWith
                                                           _Pointer[_Windows_Foundation.IAsyncOperation[IPerceptionDepthCorrelatedCoordinateMapper]]],  # result
                                                          _type.HRESULT]
    TrySetVideoProfileAsync: _Callable[[IPerceptionControlSession,  # controlSession
                                        IPerceptionVideoProfile,  # profile
                                        _Pointer[_Windows_Foundation.IAsyncOperation[IPerceptionFrameSourcePropertyChangeResult]]],  # result
                                       _type.HRESULT]
    OpenReader: _Callable[[_Pointer[IPerceptionInfraredFrameReader]],  # result
                          _type.HRESULT]


class IPerceptionInfraredFrameSource2(_inspectable.IInspectable):
    DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class IPerceptionInfraredFrameSourceAddedEventArgs(_inspectable.IInspectable):
    FrameSource: _Callable[[_Pointer[IPerceptionInfraredFrameSource]],  # value
                           _type.HRESULT]


class IPerceptionInfraredFrameSourceRemovedEventArgs(_inspectable.IInspectable):
    FrameSource: _Callable[[_Pointer[IPerceptionInfraredFrameSource]],  # value
                           _type.HRESULT]


class IPerceptionInfraredFrameSourceStatics(_inspectable.IInspectable, factory=True):
    CreateWatcher: _Callable[[_Pointer[IPerceptionInfraredFrameSourceWatcher]],  # watcher
                             _type.HRESULT]
    FindAllAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IPerceptionInfraredFrameSource]]]],  # result
                            _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # id
                            _Pointer[_Windows_Foundation.IAsyncOperation[IPerceptionInfraredFrameSource]]],  # result
                           _type.HRESULT]
    RequestAccessAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Devices.Perception.PerceptionFrameSourceAccessStatus]]],  # result
                                  _type.HRESULT]


class IPerceptionInfraredFrameSourceWatcher(_inspectable.IInspectable):
    SourceAdded: _Callable[[_struct.EventRegistrationToken],  # token
                           _type.HRESULT]
    SourceRemoved: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    Stopped: _Callable[[_struct.EventRegistrationToken],  # token
                       _type.HRESULT]
    EnumerationCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    Status: _Callable[[_Pointer[_enum.Windows.Devices.Enumeration.DeviceWatcherStatus]],  # value
                      _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]


class IPerceptionVideoProfile(_inspectable.IInspectable):
    BitmapPixelFormat: _Callable[[_Pointer[_enum.Windows.Graphics.Imaging.BitmapPixelFormat]],  # value
                                 _type.HRESULT]
    BitmapAlphaMode: _Callable[[_Pointer[_enum.Windows.Graphics.Imaging.BitmapAlphaMode]],  # value
                               _type.HRESULT]
    Width: _Callable[[_Pointer[_type.INT32]],  # value
                     _type.HRESULT]
    Height: _Callable[[_Pointer[_type.INT32]],  # value
                      _type.HRESULT]
    FrameDuration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                             _type.HRESULT]
    IsEqual: _Callable[[IPerceptionVideoProfile,  # other
                        _Pointer[_type.boolean]],  # result
                       _type.HRESULT]
