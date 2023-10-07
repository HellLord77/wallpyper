from __future__ import annotations as _

from typing import Callable as _Callable

from ... import MediaProperties as _Windows_Media_MediaProperties
from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ....Perception import Spatial as _Windows_Perception_Spatial
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class ICameraIntrinsics(_inspectable.IInspectable):
    get_FocalLength: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                               _type.HRESULT]
    get_PrincipalPoint: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                                  _type.HRESULT]
    get_RadialDistortion: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                                    _type.HRESULT]
    get_TangentialDistortion: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                                        _type.HRESULT]
    get_ImageWidth: _Callable[[_Pointer[_type.UINT32]],  # value
                              _type.HRESULT]
    get_ImageHeight: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]
    ProjectOntoFrame: _Callable[[_struct.Windows.Foundation.Numerics.Vector3,  # coordinate
                                 _Pointer[_struct.Windows.Foundation.Point]],  # result
                                _type.HRESULT]
    UnprojectAtUnitDepth: _Callable[[_struct.Windows.Foundation.Point,  # pixelCoordinate
                                     _Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # result
                                    _type.HRESULT]
    ProjectManyOntoFrame: _Callable[[_type.UINT32,  # __coordinatesSize
                                     _Pointer[_struct.Windows.Foundation.Numerics.Vector3],  # coordinates
                                     _type.UINT32,  # __resultsSize
                                     _Pointer[_struct.Windows.Foundation.Point]],  # results
                                    _type.HRESULT]
    UnprojectPixelsAtUnitDepth: _Callable[[_type.UINT32,  # __pixelCoordinatesSize
                                           _Pointer[_struct.Windows.Foundation.Point],  # pixelCoordinates
                                           _type.UINT32,  # __resultsSize
                                           _Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # results
                                          _type.HRESULT]


class ICameraIntrinsics2(_inspectable.IInspectable):
    get_UndistortedProjectionTransform: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Matrix4x4]],  # value
                                                  _type.HRESULT]
    DistortPoint: _Callable[[_struct.Windows.Foundation.Point,  # input
                             _Pointer[_struct.Windows.Foundation.Point]],  # result
                            _type.HRESULT]
    DistortPoints: _Callable[[_type.UINT32,  # __inputsSize
                              _Pointer[_struct.Windows.Foundation.Point],  # inputs
                              _type.UINT32,  # __resultsSize
                              _Pointer[_struct.Windows.Foundation.Point]],  # results
                             _type.HRESULT]
    UndistortPoint: _Callable[[_struct.Windows.Foundation.Point,  # input
                               _Pointer[_struct.Windows.Foundation.Point]],  # result
                              _type.HRESULT]
    UndistortPoints: _Callable[[_type.UINT32,  # __inputsSize
                                _Pointer[_struct.Windows.Foundation.Point],  # inputs
                                _type.UINT32,  # __resultsSize
                                _Pointer[_struct.Windows.Foundation.Point]],  # results
                               _type.HRESULT]


class ICameraIntrinsicsFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_struct.Windows.Foundation.Numerics.Vector2,  # focalLength
                       _struct.Windows.Foundation.Numerics.Vector2,  # principalPoint
                       _struct.Windows.Foundation.Numerics.Vector3,  # radialDistortion
                       _struct.Windows.Foundation.Numerics.Vector2,  # tangentialDistortion
                       _type.UINT32,  # imageWidth
                       _type.UINT32,  # imageHeight
                       _Pointer[ICameraIntrinsics]],  # result
                      _type.HRESULT]


class IDepthCorrelatedCoordinateMapper(_inspectable.IInspectable):
    UnprojectPoint: _Callable[[_struct.Windows.Foundation.Point,  # sourcePoint
                               _Windows_Perception_Spatial.ISpatialCoordinateSystem,  # targetCoordinateSystem
                               _Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # result
                              _type.HRESULT]
    UnprojectPoints: _Callable[[_type.UINT32,  # __sourcePointsSize
                                _Pointer[_struct.Windows.Foundation.Point],  # sourcePoints
                                _Windows_Perception_Spatial.ISpatialCoordinateSystem,  # targetCoordinateSystem
                                _type.UINT32,  # __resultsSize
                                _Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # results
                               _type.HRESULT]
    MapPoint: _Callable[[_struct.Windows.Foundation.Point,  # sourcePoint
                         _Windows_Perception_Spatial.ISpatialCoordinateSystem,  # targetCoordinateSystem
                         ICameraIntrinsics,  # targetCameraIntrinsics
                         _Pointer[_struct.Windows.Foundation.Point]],  # result
                        _type.HRESULT]
    MapPoints: _Callable[[_type.UINT32,  # __sourcePointsSize
                          _Pointer[_struct.Windows.Foundation.Point],  # sourcePoints
                          _Windows_Perception_Spatial.ISpatialCoordinateSystem,  # targetCoordinateSystem
                          ICameraIntrinsics,  # targetCameraIntrinsics
                          _type.UINT32,  # __resultsSize
                          _Pointer[_struct.Windows.Foundation.Point]],  # results
                         _type.HRESULT]


class IFrameControlCapabilities(_inspectable.IInspectable):
    get_Exposure: _Callable[[_Pointer[IFrameExposureCapabilities]],  # value
                            _type.HRESULT]
    get_ExposureCompensation: _Callable[[_Pointer[IFrameExposureCompensationCapabilities]],  # value
                                        _type.HRESULT]
    get_IsoSpeed: _Callable[[_Pointer[IFrameIsoSpeedCapabilities]],  # value
                            _type.HRESULT]
    get_Focus: _Callable[[_Pointer[IFrameFocusCapabilities]],  # value
                         _type.HRESULT]
    get_PhotoConfirmationSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]


class IFrameControlCapabilities2(_inspectable.IInspectable):
    get_Flash: _Callable[[_Pointer[IFrameFlashCapabilities]],  # value
                         _type.HRESULT]


class IFrameController(_inspectable.IInspectable):
    get_ExposureControl: _Callable[[_Pointer[IFrameExposureControl]],  # value
                                   _type.HRESULT]
    get_ExposureCompensationControl: _Callable[[_Pointer[IFrameExposureCompensationControl]],  # value
                                               _type.HRESULT]
    get_IsoSpeedControl: _Callable[[_Pointer[IFrameIsoSpeedControl]],  # value
                                   _type.HRESULT]
    get_FocusControl: _Callable[[_Pointer[IFrameFocusControl]],  # value
                                _type.HRESULT]
    get_PhotoConfirmationEnabled: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.boolean]]],  # value
                                            _type.HRESULT]
    put_PhotoConfirmationEnabled: _Callable[[_Windows_Foundation.IReference[_type.boolean]],  # value
                                            _type.HRESULT]


class IFrameController2(_inspectable.IInspectable):
    get_FlashControl: _Callable[[_Pointer[IFrameFlashControl]],  # value
                                _type.HRESULT]


class IFrameExposureCapabilities(_inspectable.IInspectable):
    get_Supported: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_Min: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                       _type.HRESULT]
    get_Max: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                       _type.HRESULT]
    get_Step: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                        _type.HRESULT]


class IFrameExposureCompensationCapabilities(_inspectable.IInspectable):
    get_Supported: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_Min: _Callable[[_Pointer[_type.FLOAT]],  # value
                       _type.HRESULT]
    get_Max: _Callable[[_Pointer[_type.FLOAT]],  # value
                       _type.HRESULT]
    get_Step: _Callable[[_Pointer[_type.FLOAT]],  # value
                        _type.HRESULT]


class IFrameExposureCompensationControl(_inspectable.IInspectable):
    get_Value: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.FLOAT]]],  # value
                         _type.HRESULT]
    put_Value: _Callable[[_Windows_Foundation.IReference[_type.FLOAT]],  # value
                         _type.HRESULT]


class IFrameExposureControl(_inspectable.IInspectable):
    get_Auto: _Callable[[_Pointer[_type.boolean]],  # value
                        _type.HRESULT]
    put_Auto: _Callable[[_type.boolean],  # value
                        _type.HRESULT]
    get_Value: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                         _type.HRESULT]
    put_Value: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]],  # value
                         _type.HRESULT]


class IFrameFlashCapabilities(_inspectable.IInspectable):
    get_Supported: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_RedEyeReductionSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    get_PowerSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]


class IFrameFlashControl(_inspectable.IInspectable):
    get_Mode: _Callable[[_Pointer[_enum.Windows.Media.Devices.Core.FrameFlashMode]],  # value
                        _type.HRESULT]
    put_Mode: _Callable[[_enum.Windows.Media.Devices.Core.FrameFlashMode],  # value
                        _type.HRESULT]
    get_Auto: _Callable[[_Pointer[_type.boolean]],  # value
                        _type.HRESULT]
    put_Auto: _Callable[[_type.boolean],  # value
                        _type.HRESULT]
    get_RedEyeReduction: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    put_RedEyeReduction: _Callable[[_type.boolean],  # value
                                   _type.HRESULT]
    get_PowerPercent: _Callable[[_Pointer[_type.FLOAT]],  # value
                                _type.HRESULT]
    put_PowerPercent: _Callable[[_type.FLOAT],  # value
                                _type.HRESULT]


class IFrameFocusCapabilities(_inspectable.IInspectable):
    get_Supported: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_Min: _Callable[[_Pointer[_type.UINT32]],  # value
                       _type.HRESULT]
    get_Max: _Callable[[_Pointer[_type.UINT32]],  # value
                       _type.HRESULT]
    get_Step: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]


class IFrameFocusControl(_inspectable.IInspectable):
    get_Value: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                         _type.HRESULT]
    put_Value: _Callable[[_Windows_Foundation.IReference[_type.UINT32]],  # value
                         _type.HRESULT]


class IFrameIsoSpeedCapabilities(_inspectable.IInspectable):
    get_Supported: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_Min: _Callable[[_Pointer[_type.UINT32]],  # value
                       _type.HRESULT]
    get_Max: _Callable[[_Pointer[_type.UINT32]],  # value
                       _type.HRESULT]
    get_Step: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]


class IFrameIsoSpeedControl(_inspectable.IInspectable):
    get_Auto: _Callable[[_Pointer[_type.boolean]],  # value
                        _type.HRESULT]
    put_Auto: _Callable[[_type.boolean],  # value
                        _type.HRESULT]
    get_Value: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                         _type.HRESULT]
    put_Value: _Callable[[_Windows_Foundation.IReference[_type.UINT32]],  # value
                         _type.HRESULT]


class IVariablePhotoSequenceController(_inspectable.IInspectable):
    get_Supported: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_MaxPhotosPerSecond: _Callable[[_Pointer[_type.FLOAT]],  # value
                                      _type.HRESULT]
    get_PhotosPerSecondLimit: _Callable[[_Pointer[_type.FLOAT]],  # value
                                        _type.HRESULT]
    put_PhotosPerSecondLimit: _Callable[[_type.FLOAT],  # value
                                        _type.HRESULT]
    GetHighestConcurrentFrameRate: _Callable[[_Windows_Media_MediaProperties.IMediaEncodingProperties,  # captureProperties
                                              _Pointer[_Windows_Media_MediaProperties.IMediaRatio]],  # value
                                             _type.HRESULT]
    GetCurrentFrameRate: _Callable[[_Pointer[_Windows_Media_MediaProperties.IMediaRatio]],  # value
                                   _type.HRESULT]
    get_FrameCapabilities: _Callable[[_Pointer[IFrameControlCapabilities]],  # value
                                     _type.HRESULT]
    get_DesiredFrameControllers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IFrameController]]],  # items
                                           _type.HRESULT]
