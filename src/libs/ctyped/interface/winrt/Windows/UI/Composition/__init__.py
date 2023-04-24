from __future__ import annotations

from typing import Callable as _Callable

from .. import Core as _Windows_UI_Core
from ... import Foundation as _Windows_Foundation
from ... import Graphics as _Windows_Graphics
from ... import System as _Windows_System
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Graphics import Effects as _Windows_Graphics_Effects
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IAmbientLight(_inspectable.IInspectable):
    get_Color: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                         _type.HRESULT]
    put_Color: _Callable[[_struct.Windows.UI.Color],  # value
                         _type.HRESULT]


class IAmbientLight2(_inspectable.IInspectable):
    get_Intensity: _Callable[[_Pointer[_type.FLOAT]],  # value
                             _type.HRESULT]
    put_Intensity: _Callable[[_type.FLOAT],  # value
                             _type.HRESULT]


class IAnimationController(_inspectable.IInspectable):
    get_PlaybackRate: _Callable[[_Pointer[_type.FLOAT]],  # value
                                _type.HRESULT]
    put_PlaybackRate: _Callable[[_type.FLOAT],  # value
                                _type.HRESULT]
    get_Progress: _Callable[[_Pointer[_type.FLOAT]],  # value
                            _type.HRESULT]
    put_Progress: _Callable[[_type.FLOAT],  # value
                            _type.HRESULT]
    get_ProgressBehavior: _Callable[[_Pointer[_enum.Windows.UI.Composition.AnimationControllerProgressBehavior]],  # value
                                    _type.HRESULT]
    put_ProgressBehavior: _Callable[[_enum.Windows.UI.Composition.AnimationControllerProgressBehavior],  # value
                                    _type.HRESULT]
    Pause: _Callable[[],
                     _type.HRESULT]
    Resume: _Callable[[],
                      _type.HRESULT]


class IAnimationControllerStatics(_inspectable.IInspectable):
    get_MaxPlaybackRate: _Callable[[_Pointer[_type.FLOAT]],  # value
                                   _type.HRESULT]
    get_MinPlaybackRate: _Callable[[_Pointer[_type.FLOAT]],  # value
                                   _type.HRESULT]

    _factory = True


class IAnimationObject(_inspectable.IInspectable):
    PopulatePropertyInfo: _Callable[[_type.HSTRING,  # propertyName
                                     IAnimationPropertyInfo],  # propertyInfo
                                    _type.HRESULT]


class IAnimationPropertyInfo(_inspectable.IInspectable):
    get_AccessMode: _Callable[[_Pointer[_enum.Windows.UI.Composition.AnimationPropertyAccessMode]],  # value
                              _type.HRESULT]
    put_AccessMode: _Callable[[_enum.Windows.UI.Composition.AnimationPropertyAccessMode],  # value
                              _type.HRESULT]


class IAnimationPropertyInfo2(_inspectable.IInspectable):
    GetResolvedCompositionObject: _Callable[[_Pointer[ICompositionObject]],  # result
                                            _type.HRESULT]
    GetResolvedCompositionObjectProperty: _Callable[[_Pointer[_type.HSTRING]],  # result
                                                    _type.HRESULT]


class IBackEasingFunction(_inspectable.IInspectable):
    get_Mode: _Callable[[_Pointer[_enum.Windows.UI.Composition.CompositionEasingFunctionMode]],  # value
                        _type.HRESULT]
    get_Amplitude: _Callable[[_Pointer[_type.FLOAT]],  # value
                             _type.HRESULT]


class IBooleanKeyFrameAnimation(_inspectable.IInspectable):
    InsertKeyFrame: _Callable[[_type.FLOAT,  # normalizedProgressKey
                               _type.boolean],  # value
                              _type.HRESULT]


class IBounceEasingFunction(_inspectable.IInspectable):
    get_Mode: _Callable[[_Pointer[_enum.Windows.UI.Composition.CompositionEasingFunctionMode]],  # value
                        _type.HRESULT]
    get_Bounces: _Callable[[_Pointer[_type.INT32]],  # value
                           _type.HRESULT]
    get_Bounciness: _Callable[[_Pointer[_type.FLOAT]],  # value
                              _type.HRESULT]


class IBounceScalarNaturalMotionAnimation(_inspectable.IInspectable):
    get_Acceleration: _Callable[[_Pointer[_type.FLOAT]],  # value
                                _type.HRESULT]
    put_Acceleration: _Callable[[_type.FLOAT],  # value
                                _type.HRESULT]
    get_Restitution: _Callable[[_Pointer[_type.FLOAT]],  # value
                               _type.HRESULT]
    put_Restitution: _Callable[[_type.FLOAT],  # value
                               _type.HRESULT]


class IBounceVector2NaturalMotionAnimation(_inspectable.IInspectable):
    get_Acceleration: _Callable[[_Pointer[_type.FLOAT]],  # value
                                _type.HRESULT]
    put_Acceleration: _Callable[[_type.FLOAT],  # value
                                _type.HRESULT]
    get_Restitution: _Callable[[_Pointer[_type.FLOAT]],  # value
                               _type.HRESULT]
    put_Restitution: _Callable[[_type.FLOAT],  # value
                               _type.HRESULT]


class IBounceVector3NaturalMotionAnimation(_inspectable.IInspectable):
    get_Acceleration: _Callable[[_Pointer[_type.FLOAT]],  # value
                                _type.HRESULT]
    put_Acceleration: _Callable[[_type.FLOAT],  # value
                                _type.HRESULT]
    get_Restitution: _Callable[[_Pointer[_type.FLOAT]],  # value
                               _type.HRESULT]
    put_Restitution: _Callable[[_type.FLOAT],  # value
                               _type.HRESULT]


class ICircleEasingFunction(_inspectable.IInspectable):
    get_Mode: _Callable[[_Pointer[_enum.Windows.UI.Composition.CompositionEasingFunctionMode]],  # value
                        _type.HRESULT]


class IColorKeyFrameAnimation(_inspectable.IInspectable):
    get_InterpolationColorSpace: _Callable[[_Pointer[_enum.Windows.UI.Composition.CompositionColorSpace]],  # value
                                           _type.HRESULT]
    put_InterpolationColorSpace: _Callable[[_enum.Windows.UI.Composition.CompositionColorSpace],  # value
                                           _type.HRESULT]
    InsertKeyFrame: _Callable[[_type.FLOAT,  # normalizedProgressKey
                               _struct.Windows.UI.Color],  # value
                              _type.HRESULT]
    InsertKeyFrameWithEasingFunction: _Callable[[_type.FLOAT,  # normalizedProgressKey
                                                 _struct.Windows.UI.Color,  # value
                                                 ICompositionEasingFunction],  # easingFunction
                                                _type.HRESULT]


class ICompositionAnimation(_inspectable.IInspectable):
    ClearAllParameters: _Callable[[],
                                  _type.HRESULT]
    ClearParameter: _Callable[[_type.HSTRING],  # key
                              _type.HRESULT]
    SetColorParameter: _Callable[[_type.HSTRING,  # key
                                  _struct.Windows.UI.Color],  # value
                                 _type.HRESULT]
    SetMatrix3x2Parameter: _Callable[[_type.HSTRING,  # key
                                      _struct.Windows.Foundation.Numerics.Matrix3x2],  # value
                                     _type.HRESULT]
    SetMatrix4x4Parameter: _Callable[[_type.HSTRING,  # key
                                      _struct.Windows.Foundation.Numerics.Matrix4x4],  # value
                                     _type.HRESULT]
    SetQuaternionParameter: _Callable[[_type.HSTRING,  # key
                                       _struct.Windows.Foundation.Numerics.Quaternion],  # value
                                      _type.HRESULT]
    SetReferenceParameter: _Callable[[_type.HSTRING,  # key
                                      ICompositionObject],  # compositionObject
                                     _type.HRESULT]
    SetScalarParameter: _Callable[[_type.HSTRING,  # key
                                   _type.FLOAT],  # value
                                  _type.HRESULT]
    SetVector2Parameter: _Callable[[_type.HSTRING,  # key
                                    _struct.Windows.Foundation.Numerics.Vector2],  # value
                                   _type.HRESULT]
    SetVector3Parameter: _Callable[[_type.HSTRING,  # key
                                    _struct.Windows.Foundation.Numerics.Vector3],  # value
                                   _type.HRESULT]
    SetVector4Parameter: _Callable[[_type.HSTRING,  # key
                                    _struct.Windows.Foundation.Numerics.Vector4],  # value
                                   _type.HRESULT]


class ICompositionAnimation2(_inspectable.IInspectable):
    SetBooleanParameter: _Callable[[_type.HSTRING,  # key
                                    _type.boolean],  # value
                                   _type.HRESULT]
    get_Target: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    put_Target: _Callable[[_type.HSTRING],  # value
                          _type.HRESULT]


class ICompositionAnimation3(_inspectable.IInspectable):
    get_InitialValueExpressions: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, _type.HSTRING]]],  # value
                                           _type.HRESULT]


class ICompositionAnimation4(_inspectable.IInspectable):
    SetExpressionReferenceParameter: _Callable[[_type.HSTRING,  # parameterName
                                                IAnimationObject],  # source
                                               _type.HRESULT]


class ICompositionAnimationBase(_inspectable.IInspectable):
    pass


class ICompositionAnimationFactory(_inspectable.IInspectable):
    pass


class ICompositionAnimationGroup(_inspectable.IInspectable):
    get_Count: _Callable[[_Pointer[_type.INT32]],  # value
                         _type.HRESULT]
    Add: _Callable[[ICompositionAnimation],  # value
                   _type.HRESULT]
    Remove: _Callable[[ICompositionAnimation],  # value
                      _type.HRESULT]
    RemoveAll: _Callable[[],
                         _type.HRESULT]


class ICompositionBackdropBrush(_inspectable.IInspectable):
    pass


class ICompositionBatchCompletedEventArgs(_inspectable.IInspectable):
    pass


class ICompositionBrush(_inspectable.IInspectable):
    pass


class ICompositionBrushFactory(_inspectable.IInspectable):
    pass


class ICompositionCapabilities(_inspectable.IInspectable):
    AreEffectsSupported: _Callable[[_Pointer[_type.boolean]],  # result
                                   _type.HRESULT]
    AreEffectsFast: _Callable[[_Pointer[_type.boolean]],  # result
                              _type.HRESULT]
    add_Changed: _Callable[[_Windows_Foundation.ITypedEventHandler[ICompositionCapabilities, _inspectable.IInspectable],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Changed: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]


class ICompositionCapabilitiesStatics(_inspectable.IInspectable):
    GetForCurrentView: _Callable[[_Pointer[ICompositionCapabilities]],  # result
                                 _type.HRESULT]

    _factory = True


class ICompositionClip(_inspectable.IInspectable):
    pass


class ICompositionClip2(_inspectable.IInspectable):
    get_AnchorPoint: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                               _type.HRESULT]
    put_AnchorPoint: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                               _type.HRESULT]
    get_CenterPoint: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                               _type.HRESULT]
    put_CenterPoint: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                               _type.HRESULT]
    get_Offset: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                          _type.HRESULT]
    put_Offset: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                          _type.HRESULT]
    get_RotationAngle: _Callable[[_Pointer[_type.FLOAT]],  # value
                                 _type.HRESULT]
    put_RotationAngle: _Callable[[_type.FLOAT],  # value
                                 _type.HRESULT]
    get_RotationAngleInDegrees: _Callable[[_Pointer[_type.FLOAT]],  # value
                                          _type.HRESULT]
    put_RotationAngleInDegrees: _Callable[[_type.FLOAT],  # value
                                          _type.HRESULT]
    get_Scale: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                         _type.HRESULT]
    put_Scale: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                         _type.HRESULT]
    get_TransformMatrix: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Matrix3x2]],  # value
                                   _type.HRESULT]
    put_TransformMatrix: _Callable[[_struct.Windows.Foundation.Numerics.Matrix3x2],  # value
                                   _type.HRESULT]


class ICompositionClipFactory(_inspectable.IInspectable):
    pass


class ICompositionColorBrush(_inspectable.IInspectable):
    get_Color: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                         _type.HRESULT]
    put_Color: _Callable[[_struct.Windows.UI.Color],  # value
                         _type.HRESULT]


class ICompositionColorGradientStop(_inspectable.IInspectable):
    get_Color: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                         _type.HRESULT]
    put_Color: _Callable[[_struct.Windows.UI.Color],  # value
                         _type.HRESULT]
    get_Offset: _Callable[[_Pointer[_type.FLOAT]],  # value
                          _type.HRESULT]
    put_Offset: _Callable[[_type.FLOAT],  # value
                          _type.HRESULT]


class ICompositionColorGradientStopCollection(_inspectable.IInspectable):
    pass


class ICompositionCommitBatch(_inspectable.IInspectable):
    get_IsActive: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_IsEnded: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    add_Completed: _Callable[[_Windows_Foundation.ITypedEventHandler[_inspectable.IInspectable, ICompositionBatchCompletedEventArgs],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_Completed: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]


class ICompositionContainerShape(_inspectable.IInspectable):
    get_Shapes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ICompositionShape]]],  # value
                          _type.HRESULT]


class ICompositionDrawingSurface(_inspectable.IInspectable):
    get_AlphaMode: _Callable[[_Pointer[_enum.Windows.Graphics.DirectX.DirectXAlphaMode]],  # value
                             _type.HRESULT]
    get_PixelFormat: _Callable[[_Pointer[_enum.Windows.Graphics.DirectX.DirectXPixelFormat]],  # value
                               _type.HRESULT]
    get_Size: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                        _type.HRESULT]


class ICompositionDrawingSurface2(_inspectable.IInspectable):
    get_SizeInt32: _Callable[[_Pointer[_struct.Windows.Graphics.SizeInt32]],  # value
                             _type.HRESULT]
    Resize: _Callable[[_struct.Windows.Graphics.SizeInt32],  # sizePixels
                      _type.HRESULT]
    Scroll: _Callable[[_struct.Windows.Graphics.PointInt32],  # offset
                      _type.HRESULT]
    ScrollRect: _Callable[[_struct.Windows.Graphics.PointInt32,  # offset
                           _struct.Windows.Graphics.RectInt32],  # scrollRect
                          _type.HRESULT]
    ScrollWithClip: _Callable[[_struct.Windows.Graphics.PointInt32,  # offset
                               _struct.Windows.Graphics.RectInt32],  # clipRect
                              _type.HRESULT]
    ScrollRectWithClip: _Callable[[_struct.Windows.Graphics.PointInt32,  # offset
                                   _struct.Windows.Graphics.RectInt32,  # clipRect
                                   _struct.Windows.Graphics.RectInt32],  # scrollRect
                                  _type.HRESULT]


class ICompositionDrawingSurfaceFactory(_inspectable.IInspectable):
    pass


class ICompositionEasingFunction(_inspectable.IInspectable):
    pass


class ICompositionEasingFunctionFactory(_inspectable.IInspectable):
    pass


class ICompositionEasingFunctionStatics(_inspectable.IInspectable):
    CreateCubicBezierEasingFunction: _Callable[[ICompositor,  # owner
                                                _struct.Windows.Foundation.Numerics.Vector2,  # controlPoint1
                                                _struct.Windows.Foundation.Numerics.Vector2,  # controlPoint2
                                                _Pointer[ICubicBezierEasingFunction]],  # result
                                               _type.HRESULT]
    CreateLinearEasingFunction: _Callable[[ICompositor,  # owner
                                           _Pointer[ILinearEasingFunction]],  # result
                                          _type.HRESULT]
    CreateStepEasingFunction: _Callable[[ICompositor,  # owner
                                         _Pointer[IStepEasingFunction]],  # result
                                        _type.HRESULT]
    CreateStepEasingFunctionWithStepCount: _Callable[[ICompositor,  # owner
                                                      _type.INT32,  # stepCount
                                                      _Pointer[IStepEasingFunction]],  # result
                                                     _type.HRESULT]
    CreateBackEasingFunction: _Callable[[ICompositor,  # owner
                                         _enum.Windows.UI.Composition.CompositionEasingFunctionMode,  # mode
                                         _type.FLOAT,  # amplitude
                                         _Pointer[IBackEasingFunction]],  # result
                                        _type.HRESULT]
    CreateBounceEasingFunction: _Callable[[ICompositor,  # owner
                                           _enum.Windows.UI.Composition.CompositionEasingFunctionMode,  # mode
                                           _type.INT32,  # bounces
                                           _type.FLOAT,  # bounciness
                                           _Pointer[IBounceEasingFunction]],  # result
                                          _type.HRESULT]
    CreateCircleEasingFunction: _Callable[[ICompositor,  # owner
                                           _enum.Windows.UI.Composition.CompositionEasingFunctionMode,  # mode
                                           _Pointer[ICircleEasingFunction]],  # result
                                          _type.HRESULT]
    CreateElasticEasingFunction: _Callable[[ICompositor,  # owner
                                            _enum.Windows.UI.Composition.CompositionEasingFunctionMode,  # mode
                                            _type.INT32,  # oscillations
                                            _type.FLOAT,  # springiness
                                            _Pointer[IElasticEasingFunction]],  # result
                                           _type.HRESULT]
    CreateExponentialEasingFunction: _Callable[[ICompositor,  # owner
                                                _enum.Windows.UI.Composition.CompositionEasingFunctionMode,  # mode
                                                _type.FLOAT,  # exponent
                                                _Pointer[IExponentialEasingFunction]],  # result
                                               _type.HRESULT]
    CreatePowerEasingFunction: _Callable[[ICompositor,  # owner
                                          _enum.Windows.UI.Composition.CompositionEasingFunctionMode,  # mode
                                          _type.FLOAT,  # power
                                          _Pointer[IPowerEasingFunction]],  # result
                                         _type.HRESULT]
    CreateSineEasingFunction: _Callable[[ICompositor,  # owner
                                         _enum.Windows.UI.Composition.CompositionEasingFunctionMode,  # mode
                                         _Pointer[ISineEasingFunction]],  # result
                                        _type.HRESULT]

    _factory = True


class ICompositionEffectBrush(_inspectable.IInspectable):
    GetSourceParameter: _Callable[[_type.HSTRING,  # name
                                   _Pointer[ICompositionBrush]],  # result
                                  _type.HRESULT]
    SetSourceParameter: _Callable[[_type.HSTRING,  # name
                                   ICompositionBrush],  # source
                                  _type.HRESULT]


class ICompositionEffectFactory(_inspectable.IInspectable):
    CreateBrush: _Callable[[_Pointer[ICompositionEffectBrush]],  # result
                           _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]
    get_LoadStatus: _Callable[[_Pointer[_enum.Windows.UI.Composition.CompositionEffectFactoryLoadStatus]],  # value
                              _type.HRESULT]


class ICompositionEffectSourceParameter(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class ICompositionEffectSourceParameterFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.HSTRING,  # name
                       _Pointer[ICompositionEffectSourceParameter]],  # value
                      _type.HRESULT]

    _factory = True


class ICompositionEllipseGeometry(_inspectable.IInspectable):
    get_Center: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                          _type.HRESULT]
    put_Center: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                          _type.HRESULT]
    get_Radius: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                          _type.HRESULT]
    put_Radius: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                          _type.HRESULT]


class ICompositionGeometricClip(_inspectable.IInspectable):
    get_Geometry: _Callable[[_Pointer[ICompositionGeometry]],  # value
                            _type.HRESULT]
    put_Geometry: _Callable[[ICompositionGeometry],  # value
                            _type.HRESULT]
    get_ViewBox: _Callable[[_Pointer[ICompositionViewBox]],  # value
                           _type.HRESULT]
    put_ViewBox: _Callable[[ICompositionViewBox],  # value
                           _type.HRESULT]


class ICompositionGeometry(_inspectable.IInspectable):
    get_TrimEnd: _Callable[[_Pointer[_type.FLOAT]],  # value
                           _type.HRESULT]
    put_TrimEnd: _Callable[[_type.FLOAT],  # value
                           _type.HRESULT]
    get_TrimOffset: _Callable[[_Pointer[_type.FLOAT]],  # value
                              _type.HRESULT]
    put_TrimOffset: _Callable[[_type.FLOAT],  # value
                              _type.HRESULT]
    get_TrimStart: _Callable[[_Pointer[_type.FLOAT]],  # value
                             _type.HRESULT]
    put_TrimStart: _Callable[[_type.FLOAT],  # value
                             _type.HRESULT]


class ICompositionGeometryFactory(_inspectable.IInspectable):
    pass


class ICompositionGradientBrush(_inspectable.IInspectable):
    get_AnchorPoint: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                               _type.HRESULT]
    put_AnchorPoint: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                               _type.HRESULT]
    get_CenterPoint: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                               _type.HRESULT]
    put_CenterPoint: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                               _type.HRESULT]
    get_ColorStops: _Callable[[_Pointer[ICompositionColorGradientStopCollection]],  # value
                              _type.HRESULT]
    get_ExtendMode: _Callable[[_Pointer[_enum.Windows.UI.Composition.CompositionGradientExtendMode]],  # value
                              _type.HRESULT]
    put_ExtendMode: _Callable[[_enum.Windows.UI.Composition.CompositionGradientExtendMode],  # value
                              _type.HRESULT]
    get_InterpolationSpace: _Callable[[_Pointer[_enum.Windows.UI.Composition.CompositionColorSpace]],  # value
                                      _type.HRESULT]
    put_InterpolationSpace: _Callable[[_enum.Windows.UI.Composition.CompositionColorSpace],  # value
                                      _type.HRESULT]
    get_Offset: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                          _type.HRESULT]
    put_Offset: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                          _type.HRESULT]
    get_RotationAngle: _Callable[[_Pointer[_type.FLOAT]],  # value
                                 _type.HRESULT]
    put_RotationAngle: _Callable[[_type.FLOAT],  # value
                                 _type.HRESULT]
    get_RotationAngleInDegrees: _Callable[[_Pointer[_type.FLOAT]],  # value
                                          _type.HRESULT]
    put_RotationAngleInDegrees: _Callable[[_type.FLOAT],  # value
                                          _type.HRESULT]
    get_Scale: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                         _type.HRESULT]
    put_Scale: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                         _type.HRESULT]
    get_TransformMatrix: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Matrix3x2]],  # value
                                   _type.HRESULT]
    put_TransformMatrix: _Callable[[_struct.Windows.Foundation.Numerics.Matrix3x2],  # value
                                   _type.HRESULT]


class ICompositionGradientBrush2(_inspectable.IInspectable):
    get_MappingMode: _Callable[[_Pointer[_enum.Windows.UI.Composition.CompositionMappingMode]],  # value
                               _type.HRESULT]
    put_MappingMode: _Callable[[_enum.Windows.UI.Composition.CompositionMappingMode],  # value
                               _type.HRESULT]


class ICompositionGradientBrushFactory(_inspectable.IInspectable):
    pass


class ICompositionGraphicsDevice(_inspectable.IInspectable):
    CreateDrawingSurface: _Callable[[_struct.Windows.Foundation.Size,  # sizePixels
                                     _enum.Windows.Graphics.DirectX.DirectXPixelFormat,  # pixelFormat
                                     _enum.Windows.Graphics.DirectX.DirectXAlphaMode,  # alphaMode
                                     _Pointer[ICompositionDrawingSurface]],  # result
                                    _type.HRESULT]
    add_RenderingDeviceReplaced: _Callable[[_Windows_Foundation.ITypedEventHandler[ICompositionGraphicsDevice, IRenderingDeviceReplacedEventArgs],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_RenderingDeviceReplaced: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]


class ICompositionGraphicsDevice2(_inspectable.IInspectable):
    CreateDrawingSurface2: _Callable[[_struct.Windows.Graphics.SizeInt32,  # sizePixels
                                      _enum.Windows.Graphics.DirectX.DirectXPixelFormat,  # pixelFormat
                                      _enum.Windows.Graphics.DirectX.DirectXAlphaMode,  # alphaMode
                                      _Pointer[ICompositionDrawingSurface]],  # result
                                     _type.HRESULT]
    CreateVirtualDrawingSurface: _Callable[[_struct.Windows.Graphics.SizeInt32,  # sizePixels
                                            _enum.Windows.Graphics.DirectX.DirectXPixelFormat,  # pixelFormat
                                            _enum.Windows.Graphics.DirectX.DirectXAlphaMode,  # alphaMode
                                            _Pointer[ICompositionVirtualDrawingSurface]],  # result
                                           _type.HRESULT]


class ICompositionGraphicsDevice3(_inspectable.IInspectable):
    CreateMipmapSurface: _Callable[[_struct.Windows.Graphics.SizeInt32,  # sizePixels
                                    _enum.Windows.Graphics.DirectX.DirectXPixelFormat,  # pixelFormat
                                    _enum.Windows.Graphics.DirectX.DirectXAlphaMode,  # alphaMode
                                    _Pointer[ICompositionMipmapSurface]],  # result
                                   _type.HRESULT]
    Trim: _Callable[[],
                    _type.HRESULT]


class ICompositionGraphicsDevice4(_inspectable.IInspectable):
    CaptureAsync: _Callable[[IVisual,  # captureVisual
                             _struct.Windows.Graphics.SizeInt32,  # size
                             _enum.Windows.Graphics.DirectX.DirectXPixelFormat,  # pixelFormat
                             _enum.Windows.Graphics.DirectX.DirectXAlphaMode,  # alphaMode
                             _type.FLOAT,  # sdrBoost
                             _Pointer[_Windows_Foundation.IAsyncOperation[ICompositionSurface]]],  # operation
                            _type.HRESULT]


class ICompositionLight(_inspectable.IInspectable):
    get_Targets: _Callable[[_Pointer[IVisualUnorderedCollection]],  # value
                           _type.HRESULT]


class ICompositionLight2(_inspectable.IInspectable):
    get_ExclusionsFromTargets: _Callable[[_Pointer[IVisualUnorderedCollection]],  # value
                                         _type.HRESULT]


class ICompositionLight3(_inspectable.IInspectable):
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsEnabled: _Callable[[_type.boolean],  # value
                             _type.HRESULT]


class ICompositionLightFactory(_inspectable.IInspectable):
    pass


class ICompositionLineGeometry(_inspectable.IInspectable):
    get_Start: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                         _type.HRESULT]
    put_Start: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                         _type.HRESULT]
    get_End: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                       _type.HRESULT]
    put_End: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                       _type.HRESULT]


class ICompositionLinearGradientBrush(_inspectable.IInspectable):
    get_EndPoint: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                            _type.HRESULT]
    put_EndPoint: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                            _type.HRESULT]
    get_StartPoint: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                              _type.HRESULT]
    put_StartPoint: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                              _type.HRESULT]


class ICompositionMaskBrush(_inspectable.IInspectable):
    get_Mask: _Callable[[_Pointer[ICompositionBrush]],  # value
                        _type.HRESULT]
    put_Mask: _Callable[[ICompositionBrush],  # value
                        _type.HRESULT]
    get_Source: _Callable[[_Pointer[ICompositionBrush]],  # value
                          _type.HRESULT]
    put_Source: _Callable[[ICompositionBrush],  # value
                          _type.HRESULT]


class ICompositionMipmapSurface(_inspectable.IInspectable):
    get_LevelCount: _Callable[[_Pointer[_type.UINT32]],  # value
                              _type.HRESULT]
    get_AlphaMode: _Callable[[_Pointer[_enum.Windows.Graphics.DirectX.DirectXAlphaMode]],  # value
                             _type.HRESULT]
    get_PixelFormat: _Callable[[_Pointer[_enum.Windows.Graphics.DirectX.DirectXPixelFormat]],  # value
                               _type.HRESULT]
    get_SizeInt32: _Callable[[_Pointer[_struct.Windows.Graphics.SizeInt32]],  # value
                             _type.HRESULT]
    GetDrawingSurfaceForLevel: _Callable[[_type.UINT32,  # level
                                          _Pointer[ICompositionDrawingSurface]],  # result
                                         _type.HRESULT]


class ICompositionNineGridBrush(_inspectable.IInspectable):
    get_BottomInset: _Callable[[_Pointer[_type.FLOAT]],  # value
                               _type.HRESULT]
    put_BottomInset: _Callable[[_type.FLOAT],  # value
                               _type.HRESULT]
    get_BottomInsetScale: _Callable[[_Pointer[_type.FLOAT]],  # value
                                    _type.HRESULT]
    put_BottomInsetScale: _Callable[[_type.FLOAT],  # value
                                    _type.HRESULT]
    get_IsCenterHollow: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    put_IsCenterHollow: _Callable[[_type.boolean],  # value
                                  _type.HRESULT]
    get_LeftInset: _Callable[[_Pointer[_type.FLOAT]],  # value
                             _type.HRESULT]
    put_LeftInset: _Callable[[_type.FLOAT],  # value
                             _type.HRESULT]
    get_LeftInsetScale: _Callable[[_Pointer[_type.FLOAT]],  # value
                                  _type.HRESULT]
    put_LeftInsetScale: _Callable[[_type.FLOAT],  # value
                                  _type.HRESULT]
    get_RightInset: _Callable[[_Pointer[_type.FLOAT]],  # value
                              _type.HRESULT]
    put_RightInset: _Callable[[_type.FLOAT],  # value
                              _type.HRESULT]
    get_RightInsetScale: _Callable[[_Pointer[_type.FLOAT]],  # value
                                   _type.HRESULT]
    put_RightInsetScale: _Callable[[_type.FLOAT],  # value
                                   _type.HRESULT]
    get_Source: _Callable[[_Pointer[ICompositionBrush]],  # value
                          _type.HRESULT]
    put_Source: _Callable[[ICompositionBrush],  # value
                          _type.HRESULT]
    get_TopInset: _Callable[[_Pointer[_type.FLOAT]],  # value
                            _type.HRESULT]
    put_TopInset: _Callable[[_type.FLOAT],  # value
                            _type.HRESULT]
    get_TopInsetScale: _Callable[[_Pointer[_type.FLOAT]],  # value
                                 _type.HRESULT]
    put_TopInsetScale: _Callable[[_type.FLOAT],  # value
                                 _type.HRESULT]
    SetInsets: _Callable[[_type.FLOAT],  # inset
                         _type.HRESULT]
    SetInsetsWithValues: _Callable[[_type.FLOAT,  # left
                                    _type.FLOAT,  # top
                                    _type.FLOAT,  # right
                                    _type.FLOAT],  # bottom
                                   _type.HRESULT]
    SetInsetScales: _Callable[[_type.FLOAT],  # scale
                              _type.HRESULT]
    SetInsetScalesWithValues: _Callable[[_type.FLOAT,  # left
                                         _type.FLOAT,  # top
                                         _type.FLOAT,  # right
                                         _type.FLOAT],  # bottom
                                        _type.HRESULT]


class ICompositionObject(_inspectable.IInspectable):
    get_Compositor: _Callable[[_Pointer[ICompositor]],  # value
                              _type.HRESULT]
    get_Dispatcher: _Callable[[_Pointer[_Windows_UI_Core.ICoreDispatcher]],  # value
                              _type.HRESULT]
    get_Properties: _Callable[[_Pointer[ICompositionPropertySet]],  # value
                              _type.HRESULT]
    StartAnimation: _Callable[[_type.HSTRING,  # propertyName
                               ICompositionAnimation],  # animation
                              _type.HRESULT]
    StopAnimation: _Callable[[_type.HSTRING],  # propertyName
                             _type.HRESULT]


class ICompositionObject2(_inspectable.IInspectable):
    get_Comment: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    put_Comment: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    get_ImplicitAnimations: _Callable[[_Pointer[IImplicitAnimationCollection]],  # value
                                      _type.HRESULT]
    put_ImplicitAnimations: _Callable[[IImplicitAnimationCollection],  # value
                                      _type.HRESULT]
    StartAnimationGroup: _Callable[[ICompositionAnimationBase],  # value
                                   _type.HRESULT]
    StopAnimationGroup: _Callable[[ICompositionAnimationBase],  # value
                                  _type.HRESULT]


class ICompositionObject3(_inspectable.IInspectable):
    get_DispatcherQueue: _Callable[[_Pointer[_Windows_System.IDispatcherQueue]],  # value
                                   _type.HRESULT]


class ICompositionObject4(_inspectable.IInspectable):
    TryGetAnimationController: _Callable[[_type.HSTRING,  # propertyName
                                          _Pointer[IAnimationController]],  # result
                                         _type.HRESULT]


class ICompositionObject5(_inspectable.IInspectable):
    StartAnimationWithController: _Callable[[_type.HSTRING,  # propertyName
                                             ICompositionAnimation,  # animation
                                             IAnimationController],  # animationController
                                            _type.HRESULT]


class ICompositionObjectFactory(_inspectable.IInspectable):
    pass


class ICompositionObjectStatics(_inspectable.IInspectable):
    StartAnimationWithIAnimationObject: _Callable[[IAnimationObject,  # target
                                                   _type.HSTRING,  # propertyName
                                                   ICompositionAnimation],  # animation
                                                  _type.HRESULT]
    StartAnimationGroupWithIAnimationObject: _Callable[[IAnimationObject,  # target
                                                        ICompositionAnimationBase],  # animation
                                                       _type.HRESULT]

    _factory = True


class ICompositionPath(_inspectable.IInspectable):
    pass


class ICompositionPathFactory(_inspectable.IInspectable):
    Create: _Callable[[_Windows_Graphics.IGeometrySource2D,  # source
                       _Pointer[ICompositionPath]],  # value
                      _type.HRESULT]

    _factory = True


class ICompositionPathGeometry(_inspectable.IInspectable):
    get_Path: _Callable[[_Pointer[ICompositionPath]],  # value
                        _type.HRESULT]
    put_Path: _Callable[[ICompositionPath],  # value
                        _type.HRESULT]


class ICompositionProjectedShadow(_inspectable.IInspectable):
    get_BlurRadiusMultiplier: _Callable[[_Pointer[_type.FLOAT]],  # value
                                        _type.HRESULT]
    put_BlurRadiusMultiplier: _Callable[[_type.FLOAT],  # value
                                        _type.HRESULT]
    get_Casters: _Callable[[_Pointer[ICompositionProjectedShadowCasterCollection]],  # value
                           _type.HRESULT]
    get_LightSource: _Callable[[_Pointer[ICompositionLight]],  # value
                               _type.HRESULT]
    put_LightSource: _Callable[[ICompositionLight],  # value
                               _type.HRESULT]
    get_MaxBlurRadius: _Callable[[_Pointer[_type.FLOAT]],  # value
                                 _type.HRESULT]
    put_MaxBlurRadius: _Callable[[_type.FLOAT],  # value
                                 _type.HRESULT]
    get_MinBlurRadius: _Callable[[_Pointer[_type.FLOAT]],  # value
                                 _type.HRESULT]
    put_MinBlurRadius: _Callable[[_type.FLOAT],  # value
                                 _type.HRESULT]
    get_Receivers: _Callable[[_Pointer[ICompositionProjectedShadowReceiverUnorderedCollection]],  # value
                             _type.HRESULT]


class ICompositionProjectedShadowCaster(_inspectable.IInspectable):
    get_Brush: _Callable[[_Pointer[ICompositionBrush]],  # value
                         _type.HRESULT]
    put_Brush: _Callable[[ICompositionBrush],  # value
                         _type.HRESULT]
    get_CastingVisual: _Callable[[_Pointer[IVisual]],  # value
                                 _type.HRESULT]
    put_CastingVisual: _Callable[[IVisual],  # value
                                 _type.HRESULT]


class ICompositionProjectedShadowCasterCollection(_inspectable.IInspectable):
    get_Count: _Callable[[_Pointer[_type.INT32]],  # value
                         _type.HRESULT]
    InsertAbove: _Callable[[ICompositionProjectedShadowCaster,  # newCaster
                            ICompositionProjectedShadowCaster],  # reference
                           _type.HRESULT]
    InsertAtBottom: _Callable[[ICompositionProjectedShadowCaster],  # newCaster
                              _type.HRESULT]
    InsertAtTop: _Callable[[ICompositionProjectedShadowCaster],  # newCaster
                           _type.HRESULT]
    InsertBelow: _Callable[[ICompositionProjectedShadowCaster,  # newCaster
                            ICompositionProjectedShadowCaster],  # reference
                           _type.HRESULT]
    Remove: _Callable[[ICompositionProjectedShadowCaster],  # caster
                      _type.HRESULT]
    RemoveAll: _Callable[[],
                         _type.HRESULT]


class ICompositionProjectedShadowCasterCollectionStatics(_inspectable.IInspectable):
    get_MaxRespectedCasters: _Callable[[_Pointer[_type.INT32]],  # value
                                       _type.HRESULT]

    _factory = True


class ICompositionProjectedShadowReceiver(_inspectable.IInspectable):
    get_ReceivingVisual: _Callable[[_Pointer[IVisual]],  # value
                                   _type.HRESULT]
    put_ReceivingVisual: _Callable[[IVisual],  # value
                                   _type.HRESULT]


class ICompositionProjectedShadowReceiverUnorderedCollection(_inspectable.IInspectable):
    Add: _Callable[[ICompositionProjectedShadowReceiver],  # value
                   _type.HRESULT]
    get_Count: _Callable[[_Pointer[_type.INT32]],  # value
                         _type.HRESULT]
    Remove: _Callable[[ICompositionProjectedShadowReceiver],  # value
                      _type.HRESULT]
    RemoveAll: _Callable[[],
                         _type.HRESULT]


class ICompositionPropertySet(_inspectable.IInspectable):
    InsertColor: _Callable[[_type.HSTRING,  # propertyName
                            _struct.Windows.UI.Color],  # value
                           _type.HRESULT]
    InsertMatrix3x2: _Callable[[_type.HSTRING,  # propertyName
                                _struct.Windows.Foundation.Numerics.Matrix3x2],  # value
                               _type.HRESULT]
    InsertMatrix4x4: _Callable[[_type.HSTRING,  # propertyName
                                _struct.Windows.Foundation.Numerics.Matrix4x4],  # value
                               _type.HRESULT]
    InsertQuaternion: _Callable[[_type.HSTRING,  # propertyName
                                 _struct.Windows.Foundation.Numerics.Quaternion],  # value
                                _type.HRESULT]
    InsertScalar: _Callable[[_type.HSTRING,  # propertyName
                             _type.FLOAT],  # value
                            _type.HRESULT]
    InsertVector2: _Callable[[_type.HSTRING,  # propertyName
                              _struct.Windows.Foundation.Numerics.Vector2],  # value
                             _type.HRESULT]
    InsertVector3: _Callable[[_type.HSTRING,  # propertyName
                              _struct.Windows.Foundation.Numerics.Vector3],  # value
                             _type.HRESULT]
    InsertVector4: _Callable[[_type.HSTRING,  # propertyName
                              _struct.Windows.Foundation.Numerics.Vector4],  # value
                             _type.HRESULT]
    TryGetColor: _Callable[[_type.HSTRING,  # propertyName
                            _Pointer[_struct.Windows.UI.Color],  # value
                            _Pointer[_enum.Windows.UI.Composition.CompositionGetValueStatus]],  # result
                           _type.HRESULT]
    TryGetMatrix3x2: _Callable[[_type.HSTRING,  # propertyName
                                _Pointer[_struct.Windows.Foundation.Numerics.Matrix3x2],  # value
                                _Pointer[_enum.Windows.UI.Composition.CompositionGetValueStatus]],  # result
                               _type.HRESULT]
    TryGetMatrix4x4: _Callable[[_type.HSTRING,  # propertyName
                                _Pointer[_struct.Windows.Foundation.Numerics.Matrix4x4],  # value
                                _Pointer[_enum.Windows.UI.Composition.CompositionGetValueStatus]],  # result
                               _type.HRESULT]
    TryGetQuaternion: _Callable[[_type.HSTRING,  # propertyName
                                 _Pointer[_struct.Windows.Foundation.Numerics.Quaternion],  # value
                                 _Pointer[_enum.Windows.UI.Composition.CompositionGetValueStatus]],  # result
                                _type.HRESULT]
    TryGetScalar: _Callable[[_type.HSTRING,  # propertyName
                             _Pointer[_type.FLOAT],  # value
                             _Pointer[_enum.Windows.UI.Composition.CompositionGetValueStatus]],  # result
                            _type.HRESULT]
    TryGetVector2: _Callable[[_type.HSTRING,  # propertyName
                              _Pointer[_struct.Windows.Foundation.Numerics.Vector2],  # value
                              _Pointer[_enum.Windows.UI.Composition.CompositionGetValueStatus]],  # result
                             _type.HRESULT]
    TryGetVector3: _Callable[[_type.HSTRING,  # propertyName
                              _Pointer[_struct.Windows.Foundation.Numerics.Vector3],  # value
                              _Pointer[_enum.Windows.UI.Composition.CompositionGetValueStatus]],  # result
                             _type.HRESULT]
    TryGetVector4: _Callable[[_type.HSTRING,  # propertyName
                              _Pointer[_struct.Windows.Foundation.Numerics.Vector4],  # value
                              _Pointer[_enum.Windows.UI.Composition.CompositionGetValueStatus]],  # result
                             _type.HRESULT]


class ICompositionPropertySet2(_inspectable.IInspectable):
    InsertBoolean: _Callable[[_type.HSTRING,  # propertyName
                              _type.boolean],  # value
                             _type.HRESULT]
    TryGetBoolean: _Callable[[_type.HSTRING,  # propertyName
                              _Pointer[_type.boolean],  # value
                              _Pointer[_enum.Windows.UI.Composition.CompositionGetValueStatus]],  # result
                             _type.HRESULT]


class ICompositionRadialGradientBrush(_inspectable.IInspectable):
    get_EllipseCenter: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                                 _type.HRESULT]
    put_EllipseCenter: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                                 _type.HRESULT]
    get_EllipseRadius: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                                 _type.HRESULT]
    put_EllipseRadius: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                                 _type.HRESULT]
    get_GradientOriginOffset: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                                        _type.HRESULT]
    put_GradientOriginOffset: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                                        _type.HRESULT]


class ICompositionRectangleGeometry(_inspectable.IInspectable):
    get_Offset: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                          _type.HRESULT]
    put_Offset: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                          _type.HRESULT]
    get_Size: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                        _type.HRESULT]
    put_Size: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                        _type.HRESULT]


class ICompositionRoundedRectangleGeometry(_inspectable.IInspectable):
    get_CornerRadius: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                                _type.HRESULT]
    put_CornerRadius: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                                _type.HRESULT]
    get_Offset: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                          _type.HRESULT]
    put_Offset: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                          _type.HRESULT]
    get_Size: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                        _type.HRESULT]
    put_Size: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                        _type.HRESULT]


class ICompositionScopedBatch(_inspectable.IInspectable):
    get_IsActive: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_IsEnded: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    End: _Callable[[],
                   _type.HRESULT]
    Resume: _Callable[[],
                      _type.HRESULT]
    Suspend: _Callable[[],
                       _type.HRESULT]
    add_Completed: _Callable[[_Windows_Foundation.ITypedEventHandler[_inspectable.IInspectable, ICompositionBatchCompletedEventArgs],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_Completed: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]


class ICompositionShadow(_inspectable.IInspectable):
    pass


class ICompositionShadowFactory(_inspectable.IInspectable):
    pass


class ICompositionShape(_inspectable.IInspectable):
    get_CenterPoint: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                               _type.HRESULT]
    put_CenterPoint: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                               _type.HRESULT]
    get_Offset: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                          _type.HRESULT]
    put_Offset: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                          _type.HRESULT]
    get_RotationAngle: _Callable[[_Pointer[_type.FLOAT]],  # value
                                 _type.HRESULT]
    put_RotationAngle: _Callable[[_type.FLOAT],  # value
                                 _type.HRESULT]
    get_RotationAngleInDegrees: _Callable[[_Pointer[_type.FLOAT]],  # value
                                          _type.HRESULT]
    put_RotationAngleInDegrees: _Callable[[_type.FLOAT],  # value
                                          _type.HRESULT]
    get_Scale: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                         _type.HRESULT]
    put_Scale: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                         _type.HRESULT]
    get_TransformMatrix: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Matrix3x2]],  # value
                                   _type.HRESULT]
    put_TransformMatrix: _Callable[[_struct.Windows.Foundation.Numerics.Matrix3x2],  # value
                                   _type.HRESULT]


class ICompositionShapeFactory(_inspectable.IInspectable):
    pass


class ICompositionSpriteShape(_inspectable.IInspectable):
    get_FillBrush: _Callable[[_Pointer[ICompositionBrush]],  # value
                             _type.HRESULT]
    put_FillBrush: _Callable[[ICompositionBrush],  # value
                             _type.HRESULT]
    get_Geometry: _Callable[[_Pointer[ICompositionGeometry]],  # value
                            _type.HRESULT]
    put_Geometry: _Callable[[ICompositionGeometry],  # value
                            _type.HRESULT]
    get_IsStrokeNonScaling: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_IsStrokeNonScaling: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    get_StrokeBrush: _Callable[[_Pointer[ICompositionBrush]],  # value
                               _type.HRESULT]
    put_StrokeBrush: _Callable[[ICompositionBrush],  # value
                               _type.HRESULT]
    get_StrokeDashArray: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.FLOAT]]],  # value
                                   _type.HRESULT]
    get_StrokeDashCap: _Callable[[_Pointer[_enum.Windows.UI.Composition.CompositionStrokeCap]],  # value
                                 _type.HRESULT]
    put_StrokeDashCap: _Callable[[_enum.Windows.UI.Composition.CompositionStrokeCap],  # value
                                 _type.HRESULT]
    get_StrokeDashOffset: _Callable[[_Pointer[_type.FLOAT]],  # value
                                    _type.HRESULT]
    put_StrokeDashOffset: _Callable[[_type.FLOAT],  # value
                                    _type.HRESULT]
    get_StrokeEndCap: _Callable[[_Pointer[_enum.Windows.UI.Composition.CompositionStrokeCap]],  # value
                                _type.HRESULT]
    put_StrokeEndCap: _Callable[[_enum.Windows.UI.Composition.CompositionStrokeCap],  # value
                                _type.HRESULT]
    get_StrokeLineJoin: _Callable[[_Pointer[_enum.Windows.UI.Composition.CompositionStrokeLineJoin]],  # value
                                  _type.HRESULT]
    put_StrokeLineJoin: _Callable[[_enum.Windows.UI.Composition.CompositionStrokeLineJoin],  # value
                                  _type.HRESULT]
    get_StrokeMiterLimit: _Callable[[_Pointer[_type.FLOAT]],  # value
                                    _type.HRESULT]
    put_StrokeMiterLimit: _Callable[[_type.FLOAT],  # value
                                    _type.HRESULT]
    get_StrokeStartCap: _Callable[[_Pointer[_enum.Windows.UI.Composition.CompositionStrokeCap]],  # value
                                  _type.HRESULT]
    put_StrokeStartCap: _Callable[[_enum.Windows.UI.Composition.CompositionStrokeCap],  # value
                                  _type.HRESULT]
    get_StrokeThickness: _Callable[[_Pointer[_type.FLOAT]],  # value
                                   _type.HRESULT]
    put_StrokeThickness: _Callable[[_type.FLOAT],  # value
                                   _type.HRESULT]


class ICompositionSupportsSystemBackdrop(_inspectable.IInspectable):
    get_SystemBackdrop: _Callable[[_Pointer[ICompositionBrush]],  # value
                                  _type.HRESULT]
    put_SystemBackdrop: _Callable[[ICompositionBrush],  # value
                                  _type.HRESULT]


class ICompositionSurface(_inspectable.IInspectable):
    pass


class ICompositionSurfaceBrush(_inspectable.IInspectable):
    get_BitmapInterpolationMode: _Callable[[_Pointer[_enum.Windows.UI.Composition.CompositionBitmapInterpolationMode]],  # value
                                           _type.HRESULT]
    put_BitmapInterpolationMode: _Callable[[_enum.Windows.UI.Composition.CompositionBitmapInterpolationMode],  # value
                                           _type.HRESULT]
    get_HorizontalAlignmentRatio: _Callable[[_Pointer[_type.FLOAT]],  # value
                                            _type.HRESULT]
    put_HorizontalAlignmentRatio: _Callable[[_type.FLOAT],  # value
                                            _type.HRESULT]
    get_Stretch: _Callable[[_Pointer[_enum.Windows.UI.Composition.CompositionStretch]],  # value
                           _type.HRESULT]
    put_Stretch: _Callable[[_enum.Windows.UI.Composition.CompositionStretch],  # value
                           _type.HRESULT]
    get_Surface: _Callable[[_Pointer[ICompositionSurface]],  # value
                           _type.HRESULT]
    put_Surface: _Callable[[ICompositionSurface],  # value
                           _type.HRESULT]
    get_VerticalAlignmentRatio: _Callable[[_Pointer[_type.FLOAT]],  # value
                                          _type.HRESULT]
    put_VerticalAlignmentRatio: _Callable[[_type.FLOAT],  # value
                                          _type.HRESULT]


class ICompositionSurfaceBrush2(_inspectable.IInspectable):
    get_AnchorPoint: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                               _type.HRESULT]
    put_AnchorPoint: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                               _type.HRESULT]
    get_CenterPoint: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                               _type.HRESULT]
    put_CenterPoint: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                               _type.HRESULT]
    get_Offset: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                          _type.HRESULT]
    put_Offset: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                          _type.HRESULT]
    get_RotationAngle: _Callable[[_Pointer[_type.FLOAT]],  # value
                                 _type.HRESULT]
    put_RotationAngle: _Callable[[_type.FLOAT],  # value
                                 _type.HRESULT]
    get_RotationAngleInDegrees: _Callable[[_Pointer[_type.FLOAT]],  # value
                                          _type.HRESULT]
    put_RotationAngleInDegrees: _Callable[[_type.FLOAT],  # value
                                          _type.HRESULT]
    get_Scale: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                         _type.HRESULT]
    put_Scale: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                         _type.HRESULT]
    get_TransformMatrix: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Matrix3x2]],  # value
                                   _type.HRESULT]
    put_TransformMatrix: _Callable[[_struct.Windows.Foundation.Numerics.Matrix3x2],  # value
                                   _type.HRESULT]


class ICompositionSurfaceBrush3(_inspectable.IInspectable):
    get_SnapToPixels: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_SnapToPixels: _Callable[[_type.boolean],  # value
                                _type.HRESULT]


class ICompositionSurfaceFacade(_inspectable.IInspectable):
    GetRealSurface: _Callable[[_Pointer[ICompositionSurface]],  # result
                              _type.HRESULT]


class ICompositionTarget(_inspectable.IInspectable):
    get_Root: _Callable[[_Pointer[IVisual]],  # value
                        _type.HRESULT]
    put_Root: _Callable[[IVisual],  # value
                        _type.HRESULT]


class ICompositionTargetFactory(_inspectable.IInspectable):
    pass


class ICompositionTransform(_inspectable.IInspectable):
    pass


class ICompositionTransformFactory(_inspectable.IInspectable):
    pass


class ICompositionViewBox(_inspectable.IInspectable):
    get_HorizontalAlignmentRatio: _Callable[[_Pointer[_type.FLOAT]],  # value
                                            _type.HRESULT]
    put_HorizontalAlignmentRatio: _Callable[[_type.FLOAT],  # value
                                            _type.HRESULT]
    get_Offset: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                          _type.HRESULT]
    put_Offset: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                          _type.HRESULT]
    get_Size: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                        _type.HRESULT]
    put_Size: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                        _type.HRESULT]
    get_Stretch: _Callable[[_Pointer[_enum.Windows.UI.Composition.CompositionStretch]],  # value
                           _type.HRESULT]
    put_Stretch: _Callable[[_enum.Windows.UI.Composition.CompositionStretch],  # value
                           _type.HRESULT]
    get_VerticalAlignmentRatio: _Callable[[_Pointer[_type.FLOAT]],  # value
                                          _type.HRESULT]
    put_VerticalAlignmentRatio: _Callable[[_type.FLOAT],  # value
                                          _type.HRESULT]


class ICompositionVirtualDrawingSurface(_inspectable.IInspectable):
    Trim: _Callable[[_type.UINT32,  # __rectsSize
                     _Pointer[_struct.Windows.Graphics.RectInt32]],  # rects
                    _type.HRESULT]


class ICompositionVirtualDrawingSurfaceFactory(_inspectable.IInspectable):
    pass


class ICompositionVisualSurface(_inspectable.IInspectable):
    get_SourceVisual: _Callable[[_Pointer[IVisual]],  # value
                                _type.HRESULT]
    put_SourceVisual: _Callable[[IVisual],  # value
                                _type.HRESULT]
    get_SourceOffset: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                                _type.HRESULT]
    put_SourceOffset: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                                _type.HRESULT]
    get_SourceSize: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                              _type.HRESULT]
    put_SourceSize: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                              _type.HRESULT]


class ICompositor(_inspectable.IInspectable):
    CreateColorKeyFrameAnimation: _Callable[[_Pointer[IColorKeyFrameAnimation]],  # result
                                            _type.HRESULT]
    CreateColorBrush: _Callable[[_Pointer[ICompositionColorBrush]],  # result
                                _type.HRESULT]
    CreateColorBrushWithColor: _Callable[[_struct.Windows.UI.Color,  # color
                                          _Pointer[ICompositionColorBrush]],  # result
                                         _type.HRESULT]
    CreateContainerVisual: _Callable[[_Pointer[IContainerVisual]],  # result
                                     _type.HRESULT]
    CreateCubicBezierEasingFunction: _Callable[[_struct.Windows.Foundation.Numerics.Vector2,  # controlPoint1
                                                _struct.Windows.Foundation.Numerics.Vector2,  # controlPoint2
                                                _Pointer[ICubicBezierEasingFunction]],  # result
                                               _type.HRESULT]
    CreateEffectFactory: _Callable[[_Windows_Graphics_Effects.IGraphicsEffect,  # graphicsEffect
                                    _Pointer[ICompositionEffectFactory]],  # result
                                   _type.HRESULT]
    CreateEffectFactoryWithProperties: _Callable[[_Windows_Graphics_Effects.IGraphicsEffect,  # graphicsEffect
                                                  _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # animatableProperties
                                                  _Pointer[ICompositionEffectFactory]],  # result
                                                 _type.HRESULT]
    CreateExpressionAnimation: _Callable[[_Pointer[IExpressionAnimation]],  # result
                                         _type.HRESULT]
    CreateExpressionAnimationWithExpression: _Callable[[_type.HSTRING,  # expression
                                                        _Pointer[IExpressionAnimation]],  # result
                                                       _type.HRESULT]
    CreateInsetClip: _Callable[[_Pointer[IInsetClip]],  # result
                               _type.HRESULT]
    CreateInsetClipWithInsets: _Callable[[_type.FLOAT,  # leftInset
                                          _type.FLOAT,  # topInset
                                          _type.FLOAT,  # rightInset
                                          _type.FLOAT,  # bottomInset
                                          _Pointer[IInsetClip]],  # result
                                         _type.HRESULT]
    CreateLinearEasingFunction: _Callable[[_Pointer[ILinearEasingFunction]],  # result
                                          _type.HRESULT]
    CreatePropertySet: _Callable[[_Pointer[ICompositionPropertySet]],  # result
                                 _type.HRESULT]
    CreateQuaternionKeyFrameAnimation: _Callable[[_Pointer[IQuaternionKeyFrameAnimation]],  # result
                                                 _type.HRESULT]
    CreateScalarKeyFrameAnimation: _Callable[[_Pointer[IScalarKeyFrameAnimation]],  # result
                                             _type.HRESULT]
    CreateScopedBatch: _Callable[[_enum.Windows.UI.Composition.CompositionBatchTypes,  # batchType
                                  _Pointer[ICompositionScopedBatch]],  # result
                                 _type.HRESULT]
    CreateSpriteVisual: _Callable[[_Pointer[ISpriteVisual]],  # result
                                  _type.HRESULT]
    CreateSurfaceBrush: _Callable[[_Pointer[ICompositionSurfaceBrush]],  # result
                                  _type.HRESULT]
    CreateSurfaceBrushWithSurface: _Callable[[ICompositionSurface,  # surface
                                              _Pointer[ICompositionSurfaceBrush]],  # result
                                             _type.HRESULT]
    CreateTargetForCurrentView: _Callable[[_Pointer[ICompositionTarget]],  # result
                                          _type.HRESULT]
    CreateVector2KeyFrameAnimation: _Callable[[_Pointer[IVector2KeyFrameAnimation]],  # result
                                              _type.HRESULT]
    CreateVector3KeyFrameAnimation: _Callable[[_Pointer[IVector3KeyFrameAnimation]],  # result
                                              _type.HRESULT]
    CreateVector4KeyFrameAnimation: _Callable[[_Pointer[IVector4KeyFrameAnimation]],  # result
                                              _type.HRESULT]
    GetCommitBatch: _Callable[[_enum.Windows.UI.Composition.CompositionBatchTypes,  # batchType
                               _Pointer[ICompositionCommitBatch]],  # result
                              _type.HRESULT]


class ICompositor2(_inspectable.IInspectable):
    CreateAmbientLight: _Callable[[_Pointer[IAmbientLight]],  # result
                                  _type.HRESULT]
    CreateAnimationGroup: _Callable[[_Pointer[ICompositionAnimationGroup]],  # result
                                    _type.HRESULT]
    CreateBackdropBrush: _Callable[[_Pointer[ICompositionBackdropBrush]],  # result
                                   _type.HRESULT]
    CreateDistantLight: _Callable[[_Pointer[IDistantLight]],  # result
                                  _type.HRESULT]
    CreateDropShadow: _Callable[[_Pointer[IDropShadow]],  # result
                                _type.HRESULT]
    CreateImplicitAnimationCollection: _Callable[[_Pointer[IImplicitAnimationCollection]],  # result
                                                 _type.HRESULT]
    CreateLayerVisual: _Callable[[_Pointer[ILayerVisual]],  # result
                                 _type.HRESULT]
    CreateMaskBrush: _Callable[[_Pointer[ICompositionMaskBrush]],  # result
                               _type.HRESULT]
    CreateNineGridBrush: _Callable[[_Pointer[ICompositionNineGridBrush]],  # result
                                   _type.HRESULT]
    CreatePointLight: _Callable[[_Pointer[IPointLight]],  # result
                                _type.HRESULT]
    CreateSpotLight: _Callable[[_Pointer[ISpotLight]],  # result
                               _type.HRESULT]
    CreateStepEasingFunction: _Callable[[_Pointer[IStepEasingFunction]],  # result
                                        _type.HRESULT]
    CreateStepEasingFunctionWithStepCount: _Callable[[_type.INT32,  # stepCount
                                                      _Pointer[IStepEasingFunction]],  # result
                                                     _type.HRESULT]


class ICompositor3(_inspectable.IInspectable):
    CreateHostBackdropBrush: _Callable[[_Pointer[ICompositionBackdropBrush]],  # result
                                       _type.HRESULT]


class ICompositor4(_inspectable.IInspectable):
    CreateColorGradientStop: _Callable[[_Pointer[ICompositionColorGradientStop]],  # result
                                       _type.HRESULT]
    CreateColorGradientStopWithOffsetAndColor: _Callable[[_type.FLOAT,  # offset
                                                          _struct.Windows.UI.Color,  # color
                                                          _Pointer[ICompositionColorGradientStop]],  # result
                                                         _type.HRESULT]
    CreateLinearGradientBrush: _Callable[[_Pointer[ICompositionLinearGradientBrush]],  # result
                                         _type.HRESULT]
    CreateSpringScalarAnimation: _Callable[[_Pointer[ISpringScalarNaturalMotionAnimation]],  # result
                                           _type.HRESULT]
    CreateSpringVector2Animation: _Callable[[_Pointer[ISpringVector2NaturalMotionAnimation]],  # result
                                            _type.HRESULT]
    CreateSpringVector3Animation: _Callable[[_Pointer[ISpringVector3NaturalMotionAnimation]],  # result
                                            _type.HRESULT]


class ICompositor5(_inspectable.IInspectable):
    get_Comment: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    put_Comment: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    get_GlobalPlaybackRate: _Callable[[_Pointer[_type.FLOAT]],  # value
                                      _type.HRESULT]
    put_GlobalPlaybackRate: _Callable[[_type.FLOAT],  # value
                                      _type.HRESULT]
    CreateBounceScalarAnimation: _Callable[[_Pointer[IBounceScalarNaturalMotionAnimation]],  # result
                                           _type.HRESULT]
    CreateBounceVector2Animation: _Callable[[_Pointer[IBounceVector2NaturalMotionAnimation]],  # result
                                            _type.HRESULT]
    CreateBounceVector3Animation: _Callable[[_Pointer[IBounceVector3NaturalMotionAnimation]],  # result
                                            _type.HRESULT]
    CreateContainerShape: _Callable[[_Pointer[ICompositionContainerShape]],  # result
                                    _type.HRESULT]
    CreateEllipseGeometry: _Callable[[_Pointer[ICompositionEllipseGeometry]],  # result
                                     _type.HRESULT]
    CreateLineGeometry: _Callable[[_Pointer[ICompositionLineGeometry]],  # result
                                  _type.HRESULT]
    CreatePathGeometry: _Callable[[_Pointer[ICompositionPathGeometry]],  # result
                                  _type.HRESULT]
    CreatePathGeometryWithPath: _Callable[[ICompositionPath,  # path
                                           _Pointer[ICompositionPathGeometry]],  # result
                                          _type.HRESULT]
    CreatePathKeyFrameAnimation: _Callable[[_Pointer[IPathKeyFrameAnimation]],  # result
                                           _type.HRESULT]
    CreateRectangleGeometry: _Callable[[_Pointer[ICompositionRectangleGeometry]],  # result
                                       _type.HRESULT]
    CreateRoundedRectangleGeometry: _Callable[[_Pointer[ICompositionRoundedRectangleGeometry]],  # result
                                              _type.HRESULT]
    CreateShapeVisual: _Callable[[_Pointer[IShapeVisual]],  # result
                                 _type.HRESULT]
    CreateSpriteShape: _Callable[[_Pointer[ICompositionSpriteShape]],  # result
                                 _type.HRESULT]
    CreateSpriteShapeWithGeometry: _Callable[[ICompositionGeometry,  # geometry
                                              _Pointer[ICompositionSpriteShape]],  # result
                                             _type.HRESULT]
    CreateViewBox: _Callable[[_Pointer[ICompositionViewBox]],  # result
                             _type.HRESULT]
    RequestCommitAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                  _type.HRESULT]


class ICompositor6(_inspectable.IInspectable):
    CreateGeometricClip: _Callable[[_Pointer[ICompositionGeometricClip]],  # result
                                   _type.HRESULT]
    CreateGeometricClipWithGeometry: _Callable[[ICompositionGeometry,  # geometry
                                                _Pointer[ICompositionGeometricClip]],  # result
                                               _type.HRESULT]
    CreateRedirectVisual: _Callable[[_Pointer[IRedirectVisual]],  # result
                                    _type.HRESULT]
    CreateRedirectVisualWithSourceVisual: _Callable[[IVisual,  # source
                                                     _Pointer[IRedirectVisual]],  # result
                                                    _type.HRESULT]
    CreateBooleanKeyFrameAnimation: _Callable[[_Pointer[IBooleanKeyFrameAnimation]],  # result
                                              _type.HRESULT]


class ICompositor7(_inspectable.IInspectable):
    get_DispatcherQueue: _Callable[[_Pointer[_Windows_System.IDispatcherQueue]],  # value
                                   _type.HRESULT]
    CreateAnimationPropertyInfo: _Callable[[_Pointer[IAnimationPropertyInfo]],  # result
                                           _type.HRESULT]
    CreateRectangleClip: _Callable[[_Pointer[IRectangleClip]],  # result
                                   _type.HRESULT]
    CreateRectangleClipWithSides: _Callable[[_type.FLOAT,  # left
                                             _type.FLOAT,  # top
                                             _type.FLOAT,  # right
                                             _type.FLOAT,  # bottom
                                             _Pointer[IRectangleClip]],  # result
                                            _type.HRESULT]
    CreateRectangleClipWithSidesAndRadius: _Callable[[_type.FLOAT,  # left
                                                      _type.FLOAT,  # top
                                                      _type.FLOAT,  # right
                                                      _type.FLOAT,  # bottom
                                                      _struct.Windows.Foundation.Numerics.Vector2,  # topLeftRadius
                                                      _struct.Windows.Foundation.Numerics.Vector2,  # topRightRadius
                                                      _struct.Windows.Foundation.Numerics.Vector2,  # bottomRightRadius
                                                      _struct.Windows.Foundation.Numerics.Vector2,  # bottomLeftRadius
                                                      _Pointer[IRectangleClip]],  # result
                                                     _type.HRESULT]


class ICompositor8(_inspectable.IInspectable):
    CreateAnimationController: _Callable[[_Pointer[IAnimationController]],  # result
                                         _type.HRESULT]


class ICompositorStatics(_inspectable.IInspectable):
    get_MaxGlobalPlaybackRate: _Callable[[_Pointer[_type.FLOAT]],  # value
                                         _type.HRESULT]
    get_MinGlobalPlaybackRate: _Callable[[_Pointer[_type.FLOAT]],  # value
                                         _type.HRESULT]

    _factory = True


class ICompositorWithBlurredWallpaperBackdropBrush(_inspectable.IInspectable):
    TryCreateBlurredWallpaperBackdropBrush: _Callable[[_Pointer[ICompositionBackdropBrush]],  # result
                                                      _type.HRESULT]


class ICompositorWithProjectedShadow(_inspectable.IInspectable):
    CreateProjectedShadowCaster: _Callable[[_Pointer[ICompositionProjectedShadowCaster]],  # result
                                           _type.HRESULT]
    CreateProjectedShadow: _Callable[[_Pointer[ICompositionProjectedShadow]],  # result
                                     _type.HRESULT]
    CreateProjectedShadowReceiver: _Callable[[_Pointer[ICompositionProjectedShadowReceiver]],  # result
                                             _type.HRESULT]


class ICompositorWithRadialGradient(_inspectable.IInspectable):
    CreateRadialGradientBrush: _Callable[[_Pointer[ICompositionRadialGradientBrush]],  # result
                                         _type.HRESULT]


class ICompositorWithVisualSurface(_inspectable.IInspectable):
    CreateVisualSurface: _Callable[[_Pointer[ICompositionVisualSurface]],  # result
                                   _type.HRESULT]


class IContainerVisual(_inspectable.IInspectable):
    get_Children: _Callable[[_Pointer[IVisualCollection]],  # value
                            _type.HRESULT]


class IContainerVisualFactory(_inspectable.IInspectable):
    pass


class ICubicBezierEasingFunction(_inspectable.IInspectable):
    get_ControlPoint1: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                                 _type.HRESULT]
    get_ControlPoint2: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                                 _type.HRESULT]


class IDelegatedInkTrailVisual(_inspectable.IInspectable):
    AddTrailPoints: _Callable[[_type.UINT32,  # __inkPointsSize
                               _Pointer[_struct.Windows.UI.Composition.InkTrailPoint],  # inkPoints
                               _Pointer[_type.UINT32]],  # result
                              _type.HRESULT]
    AddTrailPointsWithPrediction: _Callable[[_type.UINT32,  # __inkPointsSize
                                             _Pointer[_struct.Windows.UI.Composition.InkTrailPoint],  # inkPoints
                                             _type.UINT32,  # __predictedInkPointsSize
                                             _Pointer[_struct.Windows.UI.Composition.InkTrailPoint],  # predictedInkPoints
                                             _Pointer[_type.UINT32]],  # result
                                            _type.HRESULT]
    RemoveTrailPoints: _Callable[[_type.UINT32],  # generationId
                                 _type.HRESULT]
    StartNewTrail: _Callable[[_struct.Windows.UI.Color],  # color
                             _type.HRESULT]


class IDelegatedInkTrailVisualStatics(_inspectable.IInspectable):
    Create: _Callable[[ICompositor,  # compositor
                       _Pointer[IDelegatedInkTrailVisual]],  # result
                      _type.HRESULT]
    CreateForSwapChain: _Callable[[ICompositor,  # compositor
                                   ICompositionSurface,  # swapChain
                                   _Pointer[IDelegatedInkTrailVisual]],  # result
                                  _type.HRESULT]

    _factory = True


class IDistantLight(_inspectable.IInspectable):
    get_Color: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                         _type.HRESULT]
    put_Color: _Callable[[_struct.Windows.UI.Color],  # value
                         _type.HRESULT]
    get_CoordinateSpace: _Callable[[_Pointer[IVisual]],  # value
                                   _type.HRESULT]
    put_CoordinateSpace: _Callable[[IVisual],  # value
                                   _type.HRESULT]
    get_Direction: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                             _type.HRESULT]
    put_Direction: _Callable[[_struct.Windows.Foundation.Numerics.Vector3],  # value
                             _type.HRESULT]


class IDistantLight2(_inspectable.IInspectable):
    get_Intensity: _Callable[[_Pointer[_type.FLOAT]],  # value
                             _type.HRESULT]
    put_Intensity: _Callable[[_type.FLOAT],  # value
                             _type.HRESULT]


class IDropShadow(_inspectable.IInspectable):
    get_BlurRadius: _Callable[[_Pointer[_type.FLOAT]],  # value
                              _type.HRESULT]
    put_BlurRadius: _Callable[[_type.FLOAT],  # value
                              _type.HRESULT]
    get_Color: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                         _type.HRESULT]
    put_Color: _Callable[[_struct.Windows.UI.Color],  # value
                         _type.HRESULT]
    get_Mask: _Callable[[_Pointer[ICompositionBrush]],  # value
                        _type.HRESULT]
    put_Mask: _Callable[[ICompositionBrush],  # value
                        _type.HRESULT]
    get_Offset: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                          _type.HRESULT]
    put_Offset: _Callable[[_struct.Windows.Foundation.Numerics.Vector3],  # value
                          _type.HRESULT]
    get_Opacity: _Callable[[_Pointer[_type.FLOAT]],  # value
                           _type.HRESULT]
    put_Opacity: _Callable[[_type.FLOAT],  # value
                           _type.HRESULT]


class IDropShadow2(_inspectable.IInspectable):
    get_SourcePolicy: _Callable[[_Pointer[_enum.Windows.UI.Composition.CompositionDropShadowSourcePolicy]],  # value
                                _type.HRESULT]
    put_SourcePolicy: _Callable[[_enum.Windows.UI.Composition.CompositionDropShadowSourcePolicy],  # value
                                _type.HRESULT]


class IElasticEasingFunction(_inspectable.IInspectable):
    get_Mode: _Callable[[_Pointer[_enum.Windows.UI.Composition.CompositionEasingFunctionMode]],  # value
                        _type.HRESULT]
    get_Oscillations: _Callable[[_Pointer[_type.INT32]],  # value
                                _type.HRESULT]
    get_Springiness: _Callable[[_Pointer[_type.FLOAT]],  # value
                               _type.HRESULT]


class IExponentialEasingFunction(_inspectable.IInspectable):
    get_Mode: _Callable[[_Pointer[_enum.Windows.UI.Composition.CompositionEasingFunctionMode]],  # value
                        _type.HRESULT]
    get_Exponent: _Callable[[_Pointer[_type.FLOAT]],  # value
                            _type.HRESULT]


class IExpressionAnimation(_inspectable.IInspectable):
    get_Expression: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_Expression: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]


class IImplicitAnimationCollection(_inspectable.IInspectable):
    pass


class IInsetClip(_inspectable.IInspectable):
    get_BottomInset: _Callable[[_Pointer[_type.FLOAT]],  # value
                               _type.HRESULT]
    put_BottomInset: _Callable[[_type.FLOAT],  # value
                               _type.HRESULT]
    get_LeftInset: _Callable[[_Pointer[_type.FLOAT]],  # value
                             _type.HRESULT]
    put_LeftInset: _Callable[[_type.FLOAT],  # value
                             _type.HRESULT]
    get_RightInset: _Callable[[_Pointer[_type.FLOAT]],  # value
                              _type.HRESULT]
    put_RightInset: _Callable[[_type.FLOAT],  # value
                              _type.HRESULT]
    get_TopInset: _Callable[[_Pointer[_type.FLOAT]],  # value
                            _type.HRESULT]
    put_TopInset: _Callable[[_type.FLOAT],  # value
                            _type.HRESULT]


class IKeyFrameAnimation(_inspectable.IInspectable):
    get_DelayTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                             _type.HRESULT]
    put_DelayTime: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                             _type.HRESULT]
    get_Duration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    put_Duration: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                            _type.HRESULT]
    get_IterationBehavior: _Callable[[_Pointer[_enum.Windows.UI.Composition.AnimationIterationBehavior]],  # value
                                     _type.HRESULT]
    put_IterationBehavior: _Callable[[_enum.Windows.UI.Composition.AnimationIterationBehavior],  # value
                                     _type.HRESULT]
    get_IterationCount: _Callable[[_Pointer[_type.INT32]],  # value
                                  _type.HRESULT]
    put_IterationCount: _Callable[[_type.INT32],  # value
                                  _type.HRESULT]
    get_KeyFrameCount: _Callable[[_Pointer[_type.INT32]],  # value
                                 _type.HRESULT]
    get_StopBehavior: _Callable[[_Pointer[_enum.Windows.UI.Composition.AnimationStopBehavior]],  # value
                                _type.HRESULT]
    put_StopBehavior: _Callable[[_enum.Windows.UI.Composition.AnimationStopBehavior],  # value
                                _type.HRESULT]
    InsertExpressionKeyFrame: _Callable[[_type.FLOAT,  # normalizedProgressKey
                                         _type.HSTRING],  # value
                                        _type.HRESULT]
    InsertExpressionKeyFrameWithEasingFunction: _Callable[[_type.FLOAT,  # normalizedProgressKey
                                                           _type.HSTRING,  # value
                                                           ICompositionEasingFunction],  # easingFunction
                                                          _type.HRESULT]


class IKeyFrameAnimation2(_inspectable.IInspectable):
    get_Direction: _Callable[[_Pointer[_enum.Windows.UI.Composition.AnimationDirection]],  # value
                             _type.HRESULT]
    put_Direction: _Callable[[_enum.Windows.UI.Composition.AnimationDirection],  # value
                             _type.HRESULT]


class IKeyFrameAnimation3(_inspectable.IInspectable):
    get_DelayBehavior: _Callable[[_Pointer[_enum.Windows.UI.Composition.AnimationDelayBehavior]],  # value
                                 _type.HRESULT]
    put_DelayBehavior: _Callable[[_enum.Windows.UI.Composition.AnimationDelayBehavior],  # value
                                 _type.HRESULT]


class IKeyFrameAnimationFactory(_inspectable.IInspectable):
    pass


class ILayerVisual(_inspectable.IInspectable):
    get_Effect: _Callable[[_Pointer[ICompositionEffectBrush]],  # value
                          _type.HRESULT]
    put_Effect: _Callable[[ICompositionEffectBrush],  # value
                          _type.HRESULT]


class ILayerVisual2(_inspectable.IInspectable):
    get_Shadow: _Callable[[_Pointer[ICompositionShadow]],  # value
                          _type.HRESULT]
    put_Shadow: _Callable[[ICompositionShadow],  # value
                          _type.HRESULT]


class ILinearEasingFunction(_inspectable.IInspectable):
    pass


class INaturalMotionAnimation(_inspectable.IInspectable):
    get_DelayBehavior: _Callable[[_Pointer[_enum.Windows.UI.Composition.AnimationDelayBehavior]],  # value
                                 _type.HRESULT]
    put_DelayBehavior: _Callable[[_enum.Windows.UI.Composition.AnimationDelayBehavior],  # value
                                 _type.HRESULT]
    get_DelayTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                             _type.HRESULT]
    put_DelayTime: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                             _type.HRESULT]
    get_StopBehavior: _Callable[[_Pointer[_enum.Windows.UI.Composition.AnimationStopBehavior]],  # value
                                _type.HRESULT]
    put_StopBehavior: _Callable[[_enum.Windows.UI.Composition.AnimationStopBehavior],  # value
                                _type.HRESULT]


class INaturalMotionAnimationFactory(_inspectable.IInspectable):
    pass


class IPathKeyFrameAnimation(_inspectable.IInspectable):
    InsertKeyFrame: _Callable[[_type.FLOAT,  # normalizedProgressKey
                               ICompositionPath],  # path
                              _type.HRESULT]
    InsertKeyFrameWithEasingFunction: _Callable[[_type.FLOAT,  # normalizedProgressKey
                                                 ICompositionPath,  # path
                                                 ICompositionEasingFunction],  # easingFunction
                                                _type.HRESULT]


class IPointLight(_inspectable.IInspectable):
    get_Color: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                         _type.HRESULT]
    put_Color: _Callable[[_struct.Windows.UI.Color],  # value
                         _type.HRESULT]
    get_ConstantAttenuation: _Callable[[_Pointer[_type.FLOAT]],  # value
                                       _type.HRESULT]
    put_ConstantAttenuation: _Callable[[_type.FLOAT],  # value
                                       _type.HRESULT]
    get_CoordinateSpace: _Callable[[_Pointer[IVisual]],  # value
                                   _type.HRESULT]
    put_CoordinateSpace: _Callable[[IVisual],  # value
                                   _type.HRESULT]
    get_LinearAttenuation: _Callable[[_Pointer[_type.FLOAT]],  # value
                                     _type.HRESULT]
    put_LinearAttenuation: _Callable[[_type.FLOAT],  # value
                                     _type.HRESULT]
    get_Offset: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                          _type.HRESULT]
    put_Offset: _Callable[[_struct.Windows.Foundation.Numerics.Vector3],  # value
                          _type.HRESULT]
    get_QuadraticAttenuation: _Callable[[_Pointer[_type.FLOAT]],  # value
                                        _type.HRESULT]
    put_QuadraticAttenuation: _Callable[[_type.FLOAT],  # value
                                        _type.HRESULT]


class IPointLight2(_inspectable.IInspectable):
    get_Intensity: _Callable[[_Pointer[_type.FLOAT]],  # value
                             _type.HRESULT]
    put_Intensity: _Callable[[_type.FLOAT],  # value
                             _type.HRESULT]


class IPointLight3(_inspectable.IInspectable):
    get_MinAttenuationCutoff: _Callable[[_Pointer[_type.FLOAT]],  # value
                                        _type.HRESULT]
    put_MinAttenuationCutoff: _Callable[[_type.FLOAT],  # value
                                        _type.HRESULT]
    get_MaxAttenuationCutoff: _Callable[[_Pointer[_type.FLOAT]],  # value
                                        _type.HRESULT]
    put_MaxAttenuationCutoff: _Callable[[_type.FLOAT],  # value
                                        _type.HRESULT]


class IPowerEasingFunction(_inspectable.IInspectable):
    get_Mode: _Callable[[_Pointer[_enum.Windows.UI.Composition.CompositionEasingFunctionMode]],  # value
                        _type.HRESULT]
    get_Power: _Callable[[_Pointer[_type.FLOAT]],  # value
                         _type.HRESULT]


class IQuaternionKeyFrameAnimation(_inspectable.IInspectable):
    InsertKeyFrame: _Callable[[_type.FLOAT,  # normalizedProgressKey
                               _struct.Windows.Foundation.Numerics.Quaternion],  # value
                              _type.HRESULT]
    InsertKeyFrameWithEasingFunction: _Callable[[_type.FLOAT,  # normalizedProgressKey
                                                 _struct.Windows.Foundation.Numerics.Quaternion,  # value
                                                 ICompositionEasingFunction],  # easingFunction
                                                _type.HRESULT]


class IRectangleClip(_inspectable.IInspectable):
    get_Bottom: _Callable[[_Pointer[_type.FLOAT]],  # value
                          _type.HRESULT]
    put_Bottom: _Callable[[_type.FLOAT],  # value
                          _type.HRESULT]
    get_BottomLeftRadius: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                                    _type.HRESULT]
    put_BottomLeftRadius: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                                    _type.HRESULT]
    get_BottomRightRadius: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                                     _type.HRESULT]
    put_BottomRightRadius: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                                     _type.HRESULT]
    get_Left: _Callable[[_Pointer[_type.FLOAT]],  # value
                        _type.HRESULT]
    put_Left: _Callable[[_type.FLOAT],  # value
                        _type.HRESULT]
    get_Right: _Callable[[_Pointer[_type.FLOAT]],  # value
                         _type.HRESULT]
    put_Right: _Callable[[_type.FLOAT],  # value
                         _type.HRESULT]
    get_Top: _Callable[[_Pointer[_type.FLOAT]],  # value
                       _type.HRESULT]
    put_Top: _Callable[[_type.FLOAT],  # value
                       _type.HRESULT]
    get_TopLeftRadius: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                                 _type.HRESULT]
    put_TopLeftRadius: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                                 _type.HRESULT]
    get_TopRightRadius: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                                  _type.HRESULT]
    put_TopRightRadius: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                                  _type.HRESULT]


class IRedirectVisual(_inspectable.IInspectable):
    get_Source: _Callable[[_Pointer[IVisual]],  # value
                          _type.HRESULT]
    put_Source: _Callable[[IVisual],  # value
                          _type.HRESULT]


class IRenderingDeviceReplacedEventArgs(_inspectable.IInspectable):
    get_GraphicsDevice: _Callable[[_Pointer[ICompositionGraphicsDevice]],  # value
                                  _type.HRESULT]


class IScalarKeyFrameAnimation(_inspectable.IInspectable):
    InsertKeyFrame: _Callable[[_type.FLOAT,  # normalizedProgressKey
                               _type.FLOAT],  # value
                              _type.HRESULT]
    InsertKeyFrameWithEasingFunction: _Callable[[_type.FLOAT,  # normalizedProgressKey
                                                 _type.FLOAT,  # value
                                                 ICompositionEasingFunction],  # easingFunction
                                                _type.HRESULT]


class IScalarNaturalMotionAnimation(_inspectable.IInspectable):
    get_FinalValue: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.FLOAT]]],  # value
                              _type.HRESULT]
    put_FinalValue: _Callable[[_Windows_Foundation.IReference[_type.FLOAT]],  # value
                              _type.HRESULT]
    get_InitialValue: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.FLOAT]]],  # value
                                _type.HRESULT]
    put_InitialValue: _Callable[[_Windows_Foundation.IReference[_type.FLOAT]],  # value
                                _type.HRESULT]
    get_InitialVelocity: _Callable[[_Pointer[_type.FLOAT]],  # value
                                   _type.HRESULT]
    put_InitialVelocity: _Callable[[_type.FLOAT],  # value
                                   _type.HRESULT]


class IScalarNaturalMotionAnimationFactory(_inspectable.IInspectable):
    pass


class IShapeVisual(_inspectable.IInspectable):
    get_Shapes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ICompositionShape]]],  # value
                          _type.HRESULT]
    get_ViewBox: _Callable[[_Pointer[ICompositionViewBox]],  # value
                           _type.HRESULT]
    put_ViewBox: _Callable[[ICompositionViewBox],  # value
                           _type.HRESULT]


class ISineEasingFunction(_inspectable.IInspectable):
    get_Mode: _Callable[[_Pointer[_enum.Windows.UI.Composition.CompositionEasingFunctionMode]],  # value
                        _type.HRESULT]


class ISpotLight(_inspectable.IInspectable):
    get_ConstantAttenuation: _Callable[[_Pointer[_type.FLOAT]],  # value
                                       _type.HRESULT]
    put_ConstantAttenuation: _Callable[[_type.FLOAT],  # value
                                       _type.HRESULT]
    get_CoordinateSpace: _Callable[[_Pointer[IVisual]],  # value
                                   _type.HRESULT]
    put_CoordinateSpace: _Callable[[IVisual],  # value
                                   _type.HRESULT]
    get_Direction: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                             _type.HRESULT]
    put_Direction: _Callable[[_struct.Windows.Foundation.Numerics.Vector3],  # value
                             _type.HRESULT]
    get_InnerConeAngle: _Callable[[_Pointer[_type.FLOAT]],  # value
                                  _type.HRESULT]
    put_InnerConeAngle: _Callable[[_type.FLOAT],  # value
                                  _type.HRESULT]
    get_InnerConeAngleInDegrees: _Callable[[_Pointer[_type.FLOAT]],  # value
                                           _type.HRESULT]
    put_InnerConeAngleInDegrees: _Callable[[_type.FLOAT],  # value
                                           _type.HRESULT]
    get_InnerConeColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                  _type.HRESULT]
    put_InnerConeColor: _Callable[[_struct.Windows.UI.Color],  # value
                                  _type.HRESULT]
    get_LinearAttenuation: _Callable[[_Pointer[_type.FLOAT]],  # value
                                     _type.HRESULT]
    put_LinearAttenuation: _Callable[[_type.FLOAT],  # value
                                     _type.HRESULT]
    get_Offset: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                          _type.HRESULT]
    put_Offset: _Callable[[_struct.Windows.Foundation.Numerics.Vector3],  # value
                          _type.HRESULT]
    get_OuterConeAngle: _Callable[[_Pointer[_type.FLOAT]],  # value
                                  _type.HRESULT]
    put_OuterConeAngle: _Callable[[_type.FLOAT],  # value
                                  _type.HRESULT]
    get_OuterConeAngleInDegrees: _Callable[[_Pointer[_type.FLOAT]],  # value
                                           _type.HRESULT]
    put_OuterConeAngleInDegrees: _Callable[[_type.FLOAT],  # value
                                           _type.HRESULT]
    get_OuterConeColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                  _type.HRESULT]
    put_OuterConeColor: _Callable[[_struct.Windows.UI.Color],  # value
                                  _type.HRESULT]
    get_QuadraticAttenuation: _Callable[[_Pointer[_type.FLOAT]],  # value
                                        _type.HRESULT]
    put_QuadraticAttenuation: _Callable[[_type.FLOAT],  # value
                                        _type.HRESULT]


class ISpotLight2(_inspectable.IInspectable):
    get_InnerConeIntensity: _Callable[[_Pointer[_type.FLOAT]],  # value
                                      _type.HRESULT]
    put_InnerConeIntensity: _Callable[[_type.FLOAT],  # value
                                      _type.HRESULT]
    get_OuterConeIntensity: _Callable[[_Pointer[_type.FLOAT]],  # value
                                      _type.HRESULT]
    put_OuterConeIntensity: _Callable[[_type.FLOAT],  # value
                                      _type.HRESULT]


class ISpotLight3(_inspectable.IInspectable):
    get_MinAttenuationCutoff: _Callable[[_Pointer[_type.FLOAT]],  # value
                                        _type.HRESULT]
    put_MinAttenuationCutoff: _Callable[[_type.FLOAT],  # value
                                        _type.HRESULT]
    get_MaxAttenuationCutoff: _Callable[[_Pointer[_type.FLOAT]],  # value
                                        _type.HRESULT]
    put_MaxAttenuationCutoff: _Callable[[_type.FLOAT],  # value
                                        _type.HRESULT]


class ISpringScalarNaturalMotionAnimation(_inspectable.IInspectable):
    get_DampingRatio: _Callable[[_Pointer[_type.FLOAT]],  # value
                                _type.HRESULT]
    put_DampingRatio: _Callable[[_type.FLOAT],  # value
                                _type.HRESULT]
    get_Period: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                          _type.HRESULT]
    put_Period: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                          _type.HRESULT]


class ISpringVector2NaturalMotionAnimation(_inspectable.IInspectable):
    get_DampingRatio: _Callable[[_Pointer[_type.FLOAT]],  # value
                                _type.HRESULT]
    put_DampingRatio: _Callable[[_type.FLOAT],  # value
                                _type.HRESULT]
    get_Period: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                          _type.HRESULT]
    put_Period: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                          _type.HRESULT]


class ISpringVector3NaturalMotionAnimation(_inspectable.IInspectable):
    get_DampingRatio: _Callable[[_Pointer[_type.FLOAT]],  # value
                                _type.HRESULT]
    put_DampingRatio: _Callable[[_type.FLOAT],  # value
                                _type.HRESULT]
    get_Period: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                          _type.HRESULT]
    put_Period: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                          _type.HRESULT]


class ISpriteVisual(_inspectable.IInspectable):
    get_Brush: _Callable[[_Pointer[ICompositionBrush]],  # value
                         _type.HRESULT]
    put_Brush: _Callable[[ICompositionBrush],  # value
                         _type.HRESULT]


class ISpriteVisual2(_inspectable.IInspectable):
    get_Shadow: _Callable[[_Pointer[ICompositionShadow]],  # value
                          _type.HRESULT]
    put_Shadow: _Callable[[ICompositionShadow],  # value
                          _type.HRESULT]


class IStepEasingFunction(_inspectable.IInspectable):
    get_FinalStep: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]
    put_FinalStep: _Callable[[_type.INT32],  # value
                             _type.HRESULT]
    get_InitialStep: _Callable[[_Pointer[_type.INT32]],  # value
                               _type.HRESULT]
    put_InitialStep: _Callable[[_type.INT32],  # value
                               _type.HRESULT]
    get_IsFinalStepSingleFrame: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_IsFinalStepSingleFrame: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    get_IsInitialStepSingleFrame: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_IsInitialStepSingleFrame: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]
    get_StepCount: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]
    put_StepCount: _Callable[[_type.INT32],  # value
                             _type.HRESULT]


class IVector2KeyFrameAnimation(_inspectable.IInspectable):
    InsertKeyFrame: _Callable[[_type.FLOAT,  # normalizedProgressKey
                               _struct.Windows.Foundation.Numerics.Vector2],  # value
                              _type.HRESULT]
    InsertKeyFrameWithEasingFunction: _Callable[[_type.FLOAT,  # normalizedProgressKey
                                                 _struct.Windows.Foundation.Numerics.Vector2,  # value
                                                 ICompositionEasingFunction],  # easingFunction
                                                _type.HRESULT]


class IVector2NaturalMotionAnimation(_inspectable.IInspectable):
    get_FinalValue: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.Numerics.Vector2]]],  # value
                              _type.HRESULT]
    put_FinalValue: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                              _type.HRESULT]
    get_InitialValue: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.Numerics.Vector2]]],  # value
                                _type.HRESULT]
    put_InitialValue: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                                _type.HRESULT]
    get_InitialVelocity: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                                   _type.HRESULT]
    put_InitialVelocity: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                                   _type.HRESULT]


class IVector2NaturalMotionAnimationFactory(_inspectable.IInspectable):
    pass


class IVector3KeyFrameAnimation(_inspectable.IInspectable):
    InsertKeyFrame: _Callable[[_type.FLOAT,  # normalizedProgressKey
                               _struct.Windows.Foundation.Numerics.Vector3],  # value
                              _type.HRESULT]
    InsertKeyFrameWithEasingFunction: _Callable[[_type.FLOAT,  # normalizedProgressKey
                                                 _struct.Windows.Foundation.Numerics.Vector3,  # value
                                                 ICompositionEasingFunction],  # easingFunction
                                                _type.HRESULT]


class IVector3NaturalMotionAnimation(_inspectable.IInspectable):
    get_FinalValue: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.Numerics.Vector3]]],  # value
                              _type.HRESULT]
    put_FinalValue: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                              _type.HRESULT]
    get_InitialValue: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.Numerics.Vector3]]],  # value
                                _type.HRESULT]
    put_InitialValue: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                                _type.HRESULT]
    get_InitialVelocity: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                                   _type.HRESULT]
    put_InitialVelocity: _Callable[[_struct.Windows.Foundation.Numerics.Vector3],  # value
                                   _type.HRESULT]


class IVector3NaturalMotionAnimationFactory(_inspectable.IInspectable):
    pass


class IVector4KeyFrameAnimation(_inspectable.IInspectable):
    InsertKeyFrame: _Callable[[_type.FLOAT,  # normalizedProgressKey
                               _struct.Windows.Foundation.Numerics.Vector4],  # value
                              _type.HRESULT]
    InsertKeyFrameWithEasingFunction: _Callable[[_type.FLOAT,  # normalizedProgressKey
                                                 _struct.Windows.Foundation.Numerics.Vector4,  # value
                                                 ICompositionEasingFunction],  # easingFunction
                                                _type.HRESULT]


class IVisual(_inspectable.IInspectable):
    get_AnchorPoint: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                               _type.HRESULT]
    put_AnchorPoint: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                               _type.HRESULT]
    get_BackfaceVisibility: _Callable[[_Pointer[_enum.Windows.UI.Composition.CompositionBackfaceVisibility]],  # value
                                      _type.HRESULT]
    put_BackfaceVisibility: _Callable[[_enum.Windows.UI.Composition.CompositionBackfaceVisibility],  # value
                                      _type.HRESULT]
    get_BorderMode: _Callable[[_Pointer[_enum.Windows.UI.Composition.CompositionBorderMode]],  # value
                              _type.HRESULT]
    put_BorderMode: _Callable[[_enum.Windows.UI.Composition.CompositionBorderMode],  # value
                              _type.HRESULT]
    get_CenterPoint: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                               _type.HRESULT]
    put_CenterPoint: _Callable[[_struct.Windows.Foundation.Numerics.Vector3],  # value
                               _type.HRESULT]
    get_Clip: _Callable[[_Pointer[ICompositionClip]],  # value
                        _type.HRESULT]
    put_Clip: _Callable[[ICompositionClip],  # value
                        _type.HRESULT]
    get_CompositeMode: _Callable[[_Pointer[_enum.Windows.UI.Composition.CompositionCompositeMode]],  # value
                                 _type.HRESULT]
    put_CompositeMode: _Callable[[_enum.Windows.UI.Composition.CompositionCompositeMode],  # value
                                 _type.HRESULT]
    get_IsVisible: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsVisible: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    get_Offset: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                          _type.HRESULT]
    put_Offset: _Callable[[_struct.Windows.Foundation.Numerics.Vector3],  # value
                          _type.HRESULT]
    get_Opacity: _Callable[[_Pointer[_type.FLOAT]],  # value
                           _type.HRESULT]
    put_Opacity: _Callable[[_type.FLOAT],  # value
                           _type.HRESULT]
    get_Orientation: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Quaternion]],  # value
                               _type.HRESULT]
    put_Orientation: _Callable[[_struct.Windows.Foundation.Numerics.Quaternion],  # value
                               _type.HRESULT]
    get_Parent: _Callable[[_Pointer[IContainerVisual]],  # value
                          _type.HRESULT]
    get_RotationAngle: _Callable[[_Pointer[_type.FLOAT]],  # value
                                 _type.HRESULT]
    put_RotationAngle: _Callable[[_type.FLOAT],  # value
                                 _type.HRESULT]
    get_RotationAngleInDegrees: _Callable[[_Pointer[_type.FLOAT]],  # value
                                          _type.HRESULT]
    put_RotationAngleInDegrees: _Callable[[_type.FLOAT],  # value
                                          _type.HRESULT]
    get_RotationAxis: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                                _type.HRESULT]
    put_RotationAxis: _Callable[[_struct.Windows.Foundation.Numerics.Vector3],  # value
                                _type.HRESULT]
    get_Scale: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                         _type.HRESULT]
    put_Scale: _Callable[[_struct.Windows.Foundation.Numerics.Vector3],  # value
                         _type.HRESULT]
    get_Size: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                        _type.HRESULT]
    put_Size: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                        _type.HRESULT]
    get_TransformMatrix: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Matrix4x4]],  # value
                                   _type.HRESULT]
    put_TransformMatrix: _Callable[[_struct.Windows.Foundation.Numerics.Matrix4x4],  # value
                                   _type.HRESULT]


class IVisual2(_inspectable.IInspectable):
    get_ParentForTransform: _Callable[[_Pointer[IVisual]],  # value
                                      _type.HRESULT]
    put_ParentForTransform: _Callable[[IVisual],  # value
                                      _type.HRESULT]
    get_RelativeOffsetAdjustment: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                                            _type.HRESULT]
    put_RelativeOffsetAdjustment: _Callable[[_struct.Windows.Foundation.Numerics.Vector3],  # value
                                            _type.HRESULT]
    get_RelativeSizeAdjustment: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                                          _type.HRESULT]
    put_RelativeSizeAdjustment: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                                          _type.HRESULT]


class IVisual3(_inspectable.IInspectable):
    get_IsHitTestVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_IsHitTestVisible: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]


class IVisual4(_inspectable.IInspectable):
    get_IsPixelSnappingEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_IsPixelSnappingEnabled: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]


class IVisualCollection(_inspectable.IInspectable):
    get_Count: _Callable[[_Pointer[_type.INT32]],  # value
                         _type.HRESULT]
    InsertAbove: _Callable[[IVisual,  # newChild
                            IVisual],  # sibling
                           _type.HRESULT]
    InsertAtBottom: _Callable[[IVisual],  # newChild
                              _type.HRESULT]
    InsertAtTop: _Callable[[IVisual],  # newChild
                           _type.HRESULT]
    InsertBelow: _Callable[[IVisual,  # newChild
                            IVisual],  # sibling
                           _type.HRESULT]
    Remove: _Callable[[IVisual],  # child
                      _type.HRESULT]
    RemoveAll: _Callable[[],
                         _type.HRESULT]


class IVisualElement(_inspectable.IInspectable):
    pass


class IVisualElement2(_inspectable.IInspectable):
    GetVisualInternal: _Callable[[_Pointer[IVisual]],  # result
                                 _type.HRESULT]


class IVisualFactory(_inspectable.IInspectable):
    pass


class IVisualUnorderedCollection(_inspectable.IInspectable):
    get_Count: _Callable[[_Pointer[_type.INT32]],  # value
                         _type.HRESULT]
    Add: _Callable[[IVisual],  # newVisual
                   _type.HRESULT]
    Remove: _Callable[[IVisual],  # visual
                      _type.HRESULT]
    RemoveAll: _Callable[[],
                         _type.HRESULT]
