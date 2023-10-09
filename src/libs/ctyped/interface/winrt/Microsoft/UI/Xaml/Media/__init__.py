from __future__ import annotations as _

from typing import Callable as _Callable

from ..Controls import Primitives as _Microsoft_UI_Xaml_Controls_Primitives
from ... import Composition as _Microsoft_UI_Composition
from ... import Xaml as _Microsoft_UI_Xaml
from ...Composition import SystemBackdrops as _Microsoft_UI_Composition_SystemBackdrops
from ..... import inspectable as _inspectable
from .....Windows import Foundation as _Windows_Foundation
from .....Windows.Foundation import Collections as _Windows_Foundation_Collections
from .....Windows.Storage import Streams as _Windows_Storage_Streams
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IAcrylicBrush(_inspectable.IInspectable):
    get_TintColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    put_TintColor: _Callable[[_struct.Windows.UI.Color],  # value
                             _type.HRESULT]
    get_TintOpacity: _Callable[[_Pointer[_type.DOUBLE]],  # value
                               _type.HRESULT]
    put_TintOpacity: _Callable[[_type.DOUBLE],  # value
                               _type.HRESULT]
    get_TintTransitionDuration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                          _type.HRESULT]
    put_TintTransitionDuration: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                          _type.HRESULT]
    get_AlwaysUseFallback: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    put_AlwaysUseFallback: _Callable[[_type.boolean],  # value
                                     _type.HRESULT]


class IAcrylicBrush2(_inspectable.IInspectable):
    get_TintLuminosityOpacity: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                                         _type.HRESULT]
    put_TintLuminosityOpacity: _Callable[[_Windows_Foundation.IReference[_type.DOUBLE]],  # value
                                         _type.HRESULT]


class IAcrylicBrushFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IAcrylicBrush]],  # value
                              _type.HRESULT]


class IAcrylicBrushStatics(_inspectable.IInspectable, factory=True):
    get_TintColorProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_TintOpacityProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_TintTransitionDurationProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]
    get_AlwaysUseFallbackProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]


class IAcrylicBrushStatics2(_inspectable.IInspectable, factory=True):
    get_TintLuminosityOpacityProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]


class IArcSegment(_inspectable.IInspectable):
    get_Point: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                         _type.HRESULT]
    put_Point: _Callable[[_struct.Windows.Foundation.Point],  # value
                         _type.HRESULT]
    get_Size: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                        _type.HRESULT]
    put_Size: _Callable[[_struct.Windows.Foundation.Size],  # value
                        _type.HRESULT]
    get_RotationAngle: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                 _type.HRESULT]
    put_RotationAngle: _Callable[[_type.DOUBLE],  # value
                                 _type.HRESULT]
    get_IsLargeArc: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    put_IsLargeArc: _Callable[[_type.boolean],  # value
                              _type.HRESULT]
    get_SweepDirection: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Media.SweepDirection]],  # value
                                  _type.HRESULT]
    put_SweepDirection: _Callable[[_enum.Microsoft.UI.Xaml.Media.SweepDirection],  # value
                                  _type.HRESULT]


class IArcSegmentStatics(_inspectable.IInspectable, factory=True):
    get_PointProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_SizeProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]
    get_RotationAngleProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_IsLargeArcProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_SweepDirectionProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]


class IBezierSegment(_inspectable.IInspectable):
    get_Point1: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                          _type.HRESULT]
    put_Point1: _Callable[[_struct.Windows.Foundation.Point],  # value
                          _type.HRESULT]
    get_Point2: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                          _type.HRESULT]
    put_Point2: _Callable[[_struct.Windows.Foundation.Point],  # value
                          _type.HRESULT]
    get_Point3: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                          _type.HRESULT]
    put_Point3: _Callable[[_struct.Windows.Foundation.Point],  # value
                          _type.HRESULT]


class IBezierSegmentStatics(_inspectable.IInspectable, factory=True):
    get_Point1Property: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_Point2Property: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_Point3Property: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]


class IBitmapCache(_inspectable.IInspectable):
    pass


class IBrush(_inspectable.IInspectable):
    get_Opacity: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    put_Opacity: _Callable[[_type.DOUBLE],  # value
                           _type.HRESULT]
    get_Transform: _Callable[[_Pointer[ITransform]],  # value
                             _type.HRESULT]
    put_Transform: _Callable[[ITransform],  # value
                             _type.HRESULT]
    get_RelativeTransform: _Callable[[_Pointer[ITransform]],  # value
                                     _type.HRESULT]
    put_RelativeTransform: _Callable[[ITransform],  # value
                                     _type.HRESULT]


class IBrushFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IBrush]],  # value
                              _type.HRESULT]


class IBrushOverrides(_inspectable.IInspectable):
    PopulatePropertyInfoOverride: _Callable[[_type.HSTRING,  # propertyName
                                             _Microsoft_UI_Composition.IAnimationPropertyInfo],  # animationPropertyInfo
                                            _type.HRESULT]


class IBrushStatics(_inspectable.IInspectable, factory=True):
    get_OpacityProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_TransformProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_RelativeTransformProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]


class ICacheMode(_inspectable.IInspectable):
    pass


class ICacheModeFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ICacheMode]],  # value
                              _type.HRESULT]


class ICompositeTransform(_inspectable.IInspectable):
    get_CenterX: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    put_CenterX: _Callable[[_type.DOUBLE],  # value
                           _type.HRESULT]
    get_CenterY: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    put_CenterY: _Callable[[_type.DOUBLE],  # value
                           _type.HRESULT]
    get_ScaleX: _Callable[[_Pointer[_type.DOUBLE]],  # value
                          _type.HRESULT]
    put_ScaleX: _Callable[[_type.DOUBLE],  # value
                          _type.HRESULT]
    get_ScaleY: _Callable[[_Pointer[_type.DOUBLE]],  # value
                          _type.HRESULT]
    put_ScaleY: _Callable[[_type.DOUBLE],  # value
                          _type.HRESULT]
    get_SkewX: _Callable[[_Pointer[_type.DOUBLE]],  # value
                         _type.HRESULT]
    put_SkewX: _Callable[[_type.DOUBLE],  # value
                         _type.HRESULT]
    get_SkewY: _Callable[[_Pointer[_type.DOUBLE]],  # value
                         _type.HRESULT]
    put_SkewY: _Callable[[_type.DOUBLE],  # value
                         _type.HRESULT]
    get_Rotation: _Callable[[_Pointer[_type.DOUBLE]],  # value
                            _type.HRESULT]
    put_Rotation: _Callable[[_type.DOUBLE],  # value
                            _type.HRESULT]
    get_TranslateX: _Callable[[_Pointer[_type.DOUBLE]],  # value
                              _type.HRESULT]
    put_TranslateX: _Callable[[_type.DOUBLE],  # value
                              _type.HRESULT]
    get_TranslateY: _Callable[[_Pointer[_type.DOUBLE]],  # value
                              _type.HRESULT]
    put_TranslateY: _Callable[[_type.DOUBLE],  # value
                              _type.HRESULT]


class ICompositeTransformStatics(_inspectable.IInspectable, factory=True):
    get_CenterXProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_CenterYProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_ScaleXProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_ScaleYProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_SkewXProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_SkewYProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_RotationProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_TranslateXProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_TranslateYProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]


class ICompositionTarget(_inspectable.IInspectable):
    pass


class ICompositionTargetStatics(_inspectable.IInspectable, factory=True):
    add_Rendering: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_Rendering: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    add_Rendered: _Callable[[_Windows_Foundation.IEventHandler[IRenderedEventArgs],  # handler
                             _Pointer[_struct.EventRegistrationToken]],  # token
                            _type.HRESULT]
    remove_Rendered: _Callable[[_struct.EventRegistrationToken],  # token
                               _type.HRESULT]
    add_SurfaceContentsLost: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_SurfaceContentsLost: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    GetCompositorForCurrentThread: _Callable[[_Pointer[_Microsoft_UI_Composition.ICompositor]],  # result
                                             _type.HRESULT]


class IDesktopAcrylicBackdrop(_inspectable.IInspectable):
    pass


class IDesktopAcrylicBackdropFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IDesktopAcrylicBackdrop]],  # value
                              _type.HRESULT]


class IEllipseGeometry(_inspectable.IInspectable):
    get_Center: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                          _type.HRESULT]
    put_Center: _Callable[[_struct.Windows.Foundation.Point],  # value
                          _type.HRESULT]
    get_RadiusX: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    put_RadiusX: _Callable[[_type.DOUBLE],  # value
                           _type.HRESULT]
    get_RadiusY: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    put_RadiusY: _Callable[[_type.DOUBLE],  # value
                           _type.HRESULT]


class IEllipseGeometryStatics(_inspectable.IInspectable, factory=True):
    get_CenterProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_RadiusXProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_RadiusYProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]


class IFontFamily(_inspectable.IInspectable):
    get_Source: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]


class IFontFamilyFactory(_inspectable.IInspectable):
    CreateInstanceWithName: _Callable[[_type.HSTRING,  # familyName
                                       _inspectable.IInspectable,  # baseInterface
                                       _Pointer[_inspectable.IInspectable],  # innerInterface
                                       _Pointer[IFontFamily]],  # value
                                      _type.HRESULT]


class IFontFamilyStatics(_inspectable.IInspectable, factory=True):
    get_XamlAutoFontFamily: _Callable[[_Pointer[IFontFamily]],  # value
                                      _type.HRESULT]


class IGeneralTransform(_inspectable.IInspectable):
    get_Inverse: _Callable[[_Pointer[IGeneralTransform]],  # value
                           _type.HRESULT]
    TransformPoint: _Callable[[_struct.Windows.Foundation.Point,  # point
                               _Pointer[_struct.Windows.Foundation.Point]],  # result
                              _type.HRESULT]
    TryTransform: _Callable[[_struct.Windows.Foundation.Point,  # inPoint
                             _Pointer[_struct.Windows.Foundation.Point],  # outPoint
                             _Pointer[_type.boolean]],  # returnValue
                            _type.HRESULT]
    TransformBounds: _Callable[[_struct.Windows.Foundation.Rect,  # rect
                                _Pointer[_struct.Windows.Foundation.Rect]],  # result
                               _type.HRESULT]


class IGeneralTransformFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IGeneralTransform]],  # value
                              _type.HRESULT]


class IGeneralTransformOverrides(_inspectable.IInspectable):
    get_InverseCore: _Callable[[_Pointer[IGeneralTransform]],  # value
                               _type.HRESULT]
    TryTransformCore: _Callable[[_struct.Windows.Foundation.Point,  # inPoint
                                 _Pointer[_struct.Windows.Foundation.Point],  # outPoint
                                 _Pointer[_type.boolean]],  # returnValue
                                _type.HRESULT]
    TransformBoundsCore: _Callable[[_struct.Windows.Foundation.Rect,  # rect
                                    _Pointer[_struct.Windows.Foundation.Rect]],  # result
                                   _type.HRESULT]


class IGeometry(_inspectable.IInspectable):
    get_Transform: _Callable[[_Pointer[ITransform]],  # value
                             _type.HRESULT]
    put_Transform: _Callable[[ITransform],  # value
                             _type.HRESULT]
    get_Bounds: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                          _type.HRESULT]


class IGeometryFactory(_inspectable.IInspectable):
    pass


class IGeometryGroup(_inspectable.IInspectable):
    get_FillRule: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Media.FillRule]],  # value
                            _type.HRESULT]
    put_FillRule: _Callable[[_enum.Microsoft.UI.Xaml.Media.FillRule],  # value
                            _type.HRESULT]
    get_Children: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IGeometry]]],  # value
                            _type.HRESULT]
    put_Children: _Callable[[_Windows_Foundation_Collections.IVector[IGeometry]],  # value
                            _type.HRESULT]


class IGeometryGroupStatics(_inspectable.IInspectable, factory=True):
    get_FillRuleProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_ChildrenProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]


class IGeometryStatics(_inspectable.IInspectable, factory=True):
    get_Empty: _Callable[[_Pointer[IGeometry]],  # value
                         _type.HRESULT]
    get_StandardFlatteningTolerance: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                               _type.HRESULT]
    get_TransformProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]


class IGradientBrush(_inspectable.IInspectable):
    get_SpreadMethod: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Media.GradientSpreadMethod]],  # value
                                _type.HRESULT]
    put_SpreadMethod: _Callable[[_enum.Microsoft.UI.Xaml.Media.GradientSpreadMethod],  # value
                                _type.HRESULT]
    get_MappingMode: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Media.BrushMappingMode]],  # value
                               _type.HRESULT]
    put_MappingMode: _Callable[[_enum.Microsoft.UI.Xaml.Media.BrushMappingMode],  # value
                               _type.HRESULT]
    get_ColorInterpolationMode: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Media.ColorInterpolationMode]],  # value
                                          _type.HRESULT]
    put_ColorInterpolationMode: _Callable[[_enum.Microsoft.UI.Xaml.Media.ColorInterpolationMode],  # value
                                          _type.HRESULT]
    get_GradientStops: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IGradientStop]]],  # value
                                 _type.HRESULT]
    put_GradientStops: _Callable[[_Windows_Foundation_Collections.IVector[IGradientStop]],  # value
                                 _type.HRESULT]


class IGradientBrushFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IGradientBrush]],  # value
                              _type.HRESULT]


class IGradientBrushStatics(_inspectable.IInspectable, factory=True):
    get_SpreadMethodProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_MappingModeProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_ColorInterpolationModeProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]
    get_GradientStopsProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]


class IGradientStop(_inspectable.IInspectable):
    get_Color: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                         _type.HRESULT]
    put_Color: _Callable[[_struct.Windows.UI.Color],  # value
                         _type.HRESULT]
    get_Offset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                          _type.HRESULT]
    put_Offset: _Callable[[_type.DOUBLE],  # value
                          _type.HRESULT]


class IGradientStopStatics(_inspectable.IInspectable, factory=True):
    get_ColorProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_OffsetProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]


class IImageBrush(_inspectable.IInspectable):
    get_ImageSource: _Callable[[_Pointer[IImageSource]],  # value
                               _type.HRESULT]
    put_ImageSource: _Callable[[IImageSource],  # value
                               _type.HRESULT]
    add_ImageFailed: _Callable[[_Microsoft_UI_Xaml.IExceptionRoutedEventHandler,  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_ImageFailed: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    add_ImageOpened: _Callable[[_Microsoft_UI_Xaml.IRoutedEventHandler,  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_ImageOpened: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]


class IImageBrushStatics(_inspectable.IInspectable, factory=True):
    get_ImageSourceProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]


class IImageSource(_inspectable.IInspectable):
    pass


class IImageSourceFactory(_inspectable.IInspectable):
    pass


class ILineGeometry(_inspectable.IInspectable):
    get_StartPoint: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                              _type.HRESULT]
    put_StartPoint: _Callable[[_struct.Windows.Foundation.Point],  # value
                              _type.HRESULT]
    get_EndPoint: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    put_EndPoint: _Callable[[_struct.Windows.Foundation.Point],  # value
                            _type.HRESULT]


class ILineGeometryStatics(_inspectable.IInspectable, factory=True):
    get_StartPointProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_EndPointProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]


class ILineSegment(_inspectable.IInspectable):
    get_Point: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                         _type.HRESULT]
    put_Point: _Callable[[_struct.Windows.Foundation.Point],  # value
                         _type.HRESULT]


class ILineSegmentStatics(_inspectable.IInspectable, factory=True):
    get_PointProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]


class ILinearGradientBrush(_inspectable.IInspectable):
    get_StartPoint: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                              _type.HRESULT]
    put_StartPoint: _Callable[[_struct.Windows.Foundation.Point],  # value
                              _type.HRESULT]
    get_EndPoint: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    put_EndPoint: _Callable[[_struct.Windows.Foundation.Point],  # value
                            _type.HRESULT]


class ILinearGradientBrushFactory(_inspectable.IInspectable, factory=True):
    CreateInstanceWithGradientStopCollectionAndAngle: _Callable[[_Windows_Foundation_Collections.IVector[IGradientStop],  # gradientStopCollection
                                                                 _type.DOUBLE,  # angle
                                                                 _Pointer[ILinearGradientBrush]],  # value
                                                                _type.HRESULT]


class ILinearGradientBrushStatics(_inspectable.IInspectable, factory=True):
    get_StartPointProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_EndPointProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]


class ILoadedImageSourceLoadCompletedEventArgs(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Media.LoadedImageSourceLoadStatus]],  # value
                          _type.HRESULT]


class ILoadedImageSurface(_inspectable.IInspectable):
    get_DecodedPhysicalSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                                       _type.HRESULT]
    get_DecodedSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                               _type.HRESULT]
    get_NaturalSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                               _type.HRESULT]
    add_LoadCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[ILoadedImageSurface, ILoadedImageSourceLoadCompletedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_LoadCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]


class ILoadedImageSurfaceStatics(_inspectable.IInspectable, factory=True):
    StartLoadFromUriWithSize: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                         _struct.Windows.Foundation.Size,  # desiredMaxSize
                                         _Pointer[ILoadedImageSurface]],  # result
                                        _type.HRESULT]
    StartLoadFromUri: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                 _Pointer[ILoadedImageSurface]],  # result
                                _type.HRESULT]
    StartLoadFromStreamWithSize: _Callable[[_Windows_Storage_Streams.IRandomAccessStream,  # stream
                                            _struct.Windows.Foundation.Size,  # desiredMaxSize
                                            _Pointer[ILoadedImageSurface]],  # result
                                           _type.HRESULT]
    StartLoadFromStream: _Callable[[_Windows_Storage_Streams.IRandomAccessStream,  # stream
                                    _Pointer[ILoadedImageSurface]],  # result
                                   _type.HRESULT]


class IMatrix3DProjection(_inspectable.IInspectable):
    get_ProjectionMatrix: _Callable[[_Pointer[_struct.Microsoft.UI.Xaml.Media.Media3D.Matrix3D]],  # value
                                    _type.HRESULT]
    put_ProjectionMatrix: _Callable[[_struct.Microsoft.UI.Xaml.Media.Media3D.Matrix3D],  # value
                                    _type.HRESULT]


class IMatrix3DProjectionStatics(_inspectable.IInspectable, factory=True):
    get_ProjectionMatrixProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]


class IMatrixHelper(_inspectable.IInspectable):
    pass


class IMatrixHelperStatics(_inspectable.IInspectable, factory=True):
    get_Identity: _Callable[[_Pointer[_struct.Microsoft.UI.Xaml.Media.Matrix]],  # value
                            _type.HRESULT]
    FromElements: _Callable[[_type.DOUBLE,  # m11
                             _type.DOUBLE,  # m12
                             _type.DOUBLE,  # m21
                             _type.DOUBLE,  # m22
                             _type.DOUBLE,  # offsetX
                             _type.DOUBLE,  # offsetY
                             _Pointer[_struct.Microsoft.UI.Xaml.Media.Matrix]],  # result
                            _type.HRESULT]
    GetIsIdentity: _Callable[[_struct.Microsoft.UI.Xaml.Media.Matrix,  # target
                              _Pointer[_type.boolean]],  # result
                             _type.HRESULT]
    Transform: _Callable[[_struct.Microsoft.UI.Xaml.Media.Matrix,  # target
                          _struct.Windows.Foundation.Point,  # point
                          _Pointer[_struct.Windows.Foundation.Point]],  # result
                         _type.HRESULT]


class IMatrixTransform(_inspectable.IInspectable):
    get_Matrix: _Callable[[_Pointer[_struct.Microsoft.UI.Xaml.Media.Matrix]],  # value
                          _type.HRESULT]
    put_Matrix: _Callable[[_struct.Microsoft.UI.Xaml.Media.Matrix],  # value
                          _type.HRESULT]


class IMatrixTransformStatics(_inspectable.IInspectable, factory=True):
    get_MatrixProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]


class IMediaTransportControlsThumbnailRequestedEventArgs(_inspectable.IInspectable):
    SetThumbnailImage: _Callable[[_Windows_Storage_Streams.IInputStream],  # source
                                 _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IMicaBackdrop(_inspectable.IInspectable):
    get_Kind: _Callable[[_Pointer[_enum.Microsoft.UI.Composition.SystemBackdrops.MicaKind]],  # value
                        _type.HRESULT]
    put_Kind: _Callable[[_enum.Microsoft.UI.Composition.SystemBackdrops.MicaKind],  # value
                        _type.HRESULT]


class IMicaBackdropFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IMicaBackdrop]],  # value
                              _type.HRESULT]


class IMicaBackdropStatics(_inspectable.IInspectable, factory=True):
    get_KindProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]


class IPathFigure(_inspectable.IInspectable):
    get_Segments: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IPathSegment]]],  # value
                            _type.HRESULT]
    put_Segments: _Callable[[_Windows_Foundation_Collections.IVector[IPathSegment]],  # value
                            _type.HRESULT]
    get_StartPoint: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                              _type.HRESULT]
    put_StartPoint: _Callable[[_struct.Windows.Foundation.Point],  # value
                              _type.HRESULT]
    get_IsClosed: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    put_IsClosed: _Callable[[_type.boolean],  # value
                            _type.HRESULT]
    get_IsFilled: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    put_IsFilled: _Callable[[_type.boolean],  # value
                            _type.HRESULT]


class IPathFigureStatics(_inspectable.IInspectable, factory=True):
    get_SegmentsProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_StartPointProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_IsClosedProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_IsFilledProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]


class IPathGeometry(_inspectable.IInspectable):
    get_FillRule: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Media.FillRule]],  # value
                            _type.HRESULT]
    put_FillRule: _Callable[[_enum.Microsoft.UI.Xaml.Media.FillRule],  # value
                            _type.HRESULT]
    get_Figures: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IPathFigure]]],  # value
                           _type.HRESULT]
    put_Figures: _Callable[[_Windows_Foundation_Collections.IVector[IPathFigure]],  # value
                           _type.HRESULT]


class IPathGeometryStatics(_inspectable.IInspectable, factory=True):
    get_FillRuleProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_FiguresProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]


class IPathSegment(_inspectable.IInspectable):
    pass


class IPathSegmentFactory(_inspectable.IInspectable):
    pass


class IPlaneProjection(_inspectable.IInspectable):
    get_LocalOffsetX: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    put_LocalOffsetX: _Callable[[_type.DOUBLE],  # value
                                _type.HRESULT]
    get_LocalOffsetY: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    put_LocalOffsetY: _Callable[[_type.DOUBLE],  # value
                                _type.HRESULT]
    get_LocalOffsetZ: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    put_LocalOffsetZ: _Callable[[_type.DOUBLE],  # value
                                _type.HRESULT]
    get_RotationX: _Callable[[_Pointer[_type.DOUBLE]],  # value
                             _type.HRESULT]
    put_RotationX: _Callable[[_type.DOUBLE],  # value
                             _type.HRESULT]
    get_RotationY: _Callable[[_Pointer[_type.DOUBLE]],  # value
                             _type.HRESULT]
    put_RotationY: _Callable[[_type.DOUBLE],  # value
                             _type.HRESULT]
    get_RotationZ: _Callable[[_Pointer[_type.DOUBLE]],  # value
                             _type.HRESULT]
    put_RotationZ: _Callable[[_type.DOUBLE],  # value
                             _type.HRESULT]
    get_CenterOfRotationX: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                     _type.HRESULT]
    put_CenterOfRotationX: _Callable[[_type.DOUBLE],  # value
                                     _type.HRESULT]
    get_CenterOfRotationY: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                     _type.HRESULT]
    put_CenterOfRotationY: _Callable[[_type.DOUBLE],  # value
                                     _type.HRESULT]
    get_CenterOfRotationZ: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                     _type.HRESULT]
    put_CenterOfRotationZ: _Callable[[_type.DOUBLE],  # value
                                     _type.HRESULT]
    get_GlobalOffsetX: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                 _type.HRESULT]
    put_GlobalOffsetX: _Callable[[_type.DOUBLE],  # value
                                 _type.HRESULT]
    get_GlobalOffsetY: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                 _type.HRESULT]
    put_GlobalOffsetY: _Callable[[_type.DOUBLE],  # value
                                 _type.HRESULT]
    get_GlobalOffsetZ: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                 _type.HRESULT]
    put_GlobalOffsetZ: _Callable[[_type.DOUBLE],  # value
                                 _type.HRESULT]
    get_ProjectionMatrix: _Callable[[_Pointer[_struct.Microsoft.UI.Xaml.Media.Media3D.Matrix3D]],  # value
                                    _type.HRESULT]


class IPlaneProjectionStatics(_inspectable.IInspectable, factory=True):
    get_LocalOffsetXProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_LocalOffsetYProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_LocalOffsetZProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_RotationXProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_RotationYProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_RotationZProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_CenterOfRotationXProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_CenterOfRotationYProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_CenterOfRotationZProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_GlobalOffsetXProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_GlobalOffsetYProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_GlobalOffsetZProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_ProjectionMatrixProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]


class IPolyBezierSegment(_inspectable.IInspectable):
    get_Points: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_struct.Windows.Foundation.Point]]],  # value
                          _type.HRESULT]
    put_Points: _Callable[[_Windows_Foundation_Collections.IVector[_struct.Windows.Foundation.Point]],  # value
                          _type.HRESULT]


class IPolyBezierSegmentStatics(_inspectable.IInspectable, factory=True):
    get_PointsProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]


class IPolyLineSegment(_inspectable.IInspectable):
    get_Points: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_struct.Windows.Foundation.Point]]],  # value
                          _type.HRESULT]
    put_Points: _Callable[[_Windows_Foundation_Collections.IVector[_struct.Windows.Foundation.Point]],  # value
                          _type.HRESULT]


class IPolyLineSegmentStatics(_inspectable.IInspectable, factory=True):
    get_PointsProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]


class IPolyQuadraticBezierSegment(_inspectable.IInspectable):
    get_Points: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_struct.Windows.Foundation.Point]]],  # value
                          _type.HRESULT]
    put_Points: _Callable[[_Windows_Foundation_Collections.IVector[_struct.Windows.Foundation.Point]],  # value
                          _type.HRESULT]


class IPolyQuadraticBezierSegmentStatics(_inspectable.IInspectable, factory=True):
    get_PointsProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]


class IProjection(_inspectable.IInspectable):
    pass


class IProjectionFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IProjection]],  # value
                              _type.HRESULT]


class IQuadraticBezierSegment(_inspectable.IInspectable):
    get_Point1: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                          _type.HRESULT]
    put_Point1: _Callable[[_struct.Windows.Foundation.Point],  # value
                          _type.HRESULT]
    get_Point2: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                          _type.HRESULT]
    put_Point2: _Callable[[_struct.Windows.Foundation.Point],  # value
                          _type.HRESULT]


class IQuadraticBezierSegmentStatics(_inspectable.IInspectable, factory=True):
    get_Point1Property: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_Point2Property: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]


class IRadialGradientBrush(_inspectable.IInspectable):
    get_Center: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                          _type.HRESULT]
    put_Center: _Callable[[_struct.Windows.Foundation.Point],  # value
                          _type.HRESULT]
    get_RadiusX: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    put_RadiusX: _Callable[[_type.DOUBLE],  # value
                           _type.HRESULT]
    get_RadiusY: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    put_RadiusY: _Callable[[_type.DOUBLE],  # value
                           _type.HRESULT]
    get_GradientOrigin: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                                  _type.HRESULT]
    put_GradientOrigin: _Callable[[_struct.Windows.Foundation.Point],  # value
                                  _type.HRESULT]
    get_MappingMode: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Media.BrushMappingMode]],  # value
                               _type.HRESULT]
    put_MappingMode: _Callable[[_enum.Microsoft.UI.Xaml.Media.BrushMappingMode],  # value
                               _type.HRESULT]
    get_InterpolationSpace: _Callable[[_Pointer[_enum.Microsoft.UI.Composition.CompositionColorSpace]],  # value
                                      _type.HRESULT]
    put_InterpolationSpace: _Callable[[_enum.Microsoft.UI.Composition.CompositionColorSpace],  # value
                                      _type.HRESULT]
    get_SpreadMethod: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Media.GradientSpreadMethod]],  # value
                                _type.HRESULT]
    put_SpreadMethod: _Callable[[_enum.Microsoft.UI.Xaml.Media.GradientSpreadMethod],  # value
                                _type.HRESULT]
    get_GradientStops: _Callable[[_Pointer[_Windows_Foundation_Collections.IObservableVector[IGradientStop]]],  # value
                                 _type.HRESULT]


class IRadialGradientBrushFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IRadialGradientBrush]],  # value
                              _type.HRESULT]


class IRadialGradientBrushStatics(_inspectable.IInspectable, factory=True):
    get_CenterProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_RadiusXProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_RadiusYProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_GradientOriginProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_InterpolationSpaceProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_MappingModeProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_SpreadMethodProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]


class IRectangleGeometry(_inspectable.IInspectable):
    get_Rect: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                        _type.HRESULT]
    put_Rect: _Callable[[_struct.Windows.Foundation.Rect],  # value
                        _type.HRESULT]


class IRectangleGeometryStatics(_inspectable.IInspectable, factory=True):
    get_RectProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]


class IRenderedEventArgs(_inspectable.IInspectable):
    get_FrameDuration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                 _type.HRESULT]


class IRenderingEventArgs(_inspectable.IInspectable):
    get_RenderingTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                 _type.HRESULT]


class IRotateTransform(_inspectable.IInspectable):
    get_CenterX: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    put_CenterX: _Callable[[_type.DOUBLE],  # value
                           _type.HRESULT]
    get_CenterY: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    put_CenterY: _Callable[[_type.DOUBLE],  # value
                           _type.HRESULT]
    get_Angle: _Callable[[_Pointer[_type.DOUBLE]],  # value
                         _type.HRESULT]
    put_Angle: _Callable[[_type.DOUBLE],  # value
                         _type.HRESULT]


class IRotateTransformStatics(_inspectable.IInspectable, factory=True):
    get_CenterXProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_CenterYProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_AngleProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]


class IScaleTransform(_inspectable.IInspectable):
    get_CenterX: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    put_CenterX: _Callable[[_type.DOUBLE],  # value
                           _type.HRESULT]
    get_CenterY: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    put_CenterY: _Callable[[_type.DOUBLE],  # value
                           _type.HRESULT]
    get_ScaleX: _Callable[[_Pointer[_type.DOUBLE]],  # value
                          _type.HRESULT]
    put_ScaleX: _Callable[[_type.DOUBLE],  # value
                          _type.HRESULT]
    get_ScaleY: _Callable[[_Pointer[_type.DOUBLE]],  # value
                          _type.HRESULT]
    put_ScaleY: _Callable[[_type.DOUBLE],  # value
                          _type.HRESULT]


class IScaleTransformStatics(_inspectable.IInspectable, factory=True):
    get_CenterXProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_CenterYProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_ScaleXProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_ScaleYProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]


class IShadow(_inspectable.IInspectable):
    pass


class IShadowFactory(_inspectable.IInspectable):
    pass


class ISkewTransform(_inspectable.IInspectable):
    get_CenterX: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    put_CenterX: _Callable[[_type.DOUBLE],  # value
                           _type.HRESULT]
    get_CenterY: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    put_CenterY: _Callable[[_type.DOUBLE],  # value
                           _type.HRESULT]
    get_AngleX: _Callable[[_Pointer[_type.DOUBLE]],  # value
                          _type.HRESULT]
    put_AngleX: _Callable[[_type.DOUBLE],  # value
                          _type.HRESULT]
    get_AngleY: _Callable[[_Pointer[_type.DOUBLE]],  # value
                          _type.HRESULT]
    put_AngleY: _Callable[[_type.DOUBLE],  # value
                          _type.HRESULT]


class ISkewTransformStatics(_inspectable.IInspectable, factory=True):
    get_CenterXProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_CenterYProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_AngleXProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_AngleYProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]


class ISolidColorBrush(_inspectable.IInspectable):
    get_Color: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                         _type.HRESULT]
    put_Color: _Callable[[_struct.Windows.UI.Color],  # value
                         _type.HRESULT]


class ISolidColorBrushFactory(_inspectable.IInspectable, factory=True):
    CreateInstanceWithColor: _Callable[[_struct.Windows.UI.Color,  # color
                                        _Pointer[ISolidColorBrush]],  # value
                                       _type.HRESULT]


class ISolidColorBrushStatics(_inspectable.IInspectable, factory=True):
    get_ColorProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]


class ISystemBackdrop(_inspectable.IInspectable):
    GetDefaultSystemBackdropConfiguration: _Callable[[_Microsoft_UI_Composition.ICompositionSupportsSystemBackdrop,  # target
                                                      _Microsoft_UI_Xaml.IXamlRoot,  # xamlRoot
                                                      _Pointer[_Microsoft_UI_Composition_SystemBackdrops.ISystemBackdropConfiguration]],  # result
                                                     _type.HRESULT]


class ISystemBackdropFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ISystemBackdrop]],  # value
                              _type.HRESULT]


class ISystemBackdropOverrides(_inspectable.IInspectable):
    OnTargetConnected: _Callable[[_Microsoft_UI_Composition.ICompositionSupportsSystemBackdrop,  # connectedTarget
                                  _Microsoft_UI_Xaml.IXamlRoot],  # xamlRoot
                                 _type.HRESULT]
    OnTargetDisconnected: _Callable[[_Microsoft_UI_Composition.ICompositionSupportsSystemBackdrop],  # disconnectedTarget
                                    _type.HRESULT]
    OnDefaultSystemBackdropConfigurationChanged: _Callable[[_Microsoft_UI_Composition.ICompositionSupportsSystemBackdrop,  # target
                                                            _Microsoft_UI_Xaml.IXamlRoot],  # xamlRoot
                                                           _type.HRESULT]


class IThemeShadow(_inspectable.IInspectable):
    get_Receivers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Microsoft_UI_Xaml.IUIElement]]],  # value
                             _type.HRESULT]


class IThemeShadowFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IThemeShadow]],  # value
                              _type.HRESULT]


class ITileBrush(_inspectable.IInspectable):
    get_AlignmentX: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Media.AlignmentX]],  # value
                              _type.HRESULT]
    put_AlignmentX: _Callable[[_enum.Microsoft.UI.Xaml.Media.AlignmentX],  # value
                              _type.HRESULT]
    get_AlignmentY: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Media.AlignmentY]],  # value
                              _type.HRESULT]
    put_AlignmentY: _Callable[[_enum.Microsoft.UI.Xaml.Media.AlignmentY],  # value
                              _type.HRESULT]
    get_Stretch: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Media.Stretch]],  # value
                           _type.HRESULT]
    put_Stretch: _Callable[[_enum.Microsoft.UI.Xaml.Media.Stretch],  # value
                           _type.HRESULT]


class ITileBrushFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ITileBrush]],  # value
                              _type.HRESULT]


class ITileBrushStatics(_inspectable.IInspectable, factory=True):
    get_AlignmentXProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_AlignmentYProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_StretchProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]


class ITransform(_inspectable.IInspectable):
    pass


class ITransformFactory(_inspectable.IInspectable):
    pass


class ITransformGroup(_inspectable.IInspectable):
    get_Children: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ITransform]]],  # value
                            _type.HRESULT]
    put_Children: _Callable[[_Windows_Foundation_Collections.IVector[ITransform]],  # value
                            _type.HRESULT]
    get_Value: _Callable[[_Pointer[_struct.Microsoft.UI.Xaml.Media.Matrix]],  # value
                         _type.HRESULT]


class ITransformGroupStatics(_inspectable.IInspectable, factory=True):
    get_ChildrenProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]


class ITranslateTransform(_inspectable.IInspectable):
    get_X: _Callable[[_Pointer[_type.DOUBLE]],  # value
                     _type.HRESULT]
    put_X: _Callable[[_type.DOUBLE],  # value
                     _type.HRESULT]
    get_Y: _Callable[[_Pointer[_type.DOUBLE]],  # value
                     _type.HRESULT]
    put_Y: _Callable[[_type.DOUBLE],  # value
                     _type.HRESULT]


class ITranslateTransformStatics(_inspectable.IInspectable, factory=True):
    get_XProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                             _type.HRESULT]
    get_YProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                             _type.HRESULT]


class IVisualTreeHelper(_inspectable.IInspectable):
    pass


class IVisualTreeHelperStatics(_inspectable.IInspectable, factory=True):
    FindElementsInHostCoordinatesPoint: _Callable[[_struct.Windows.Foundation.Point,  # intersectingPoint
                                                   _Microsoft_UI_Xaml.IUIElement,  # subtree
                                                   _Pointer[_Windows_Foundation_Collections.IIterable[_Microsoft_UI_Xaml.IUIElement]]],  # result
                                                  _type.HRESULT]
    FindElementsInHostCoordinatesRect: _Callable[[_struct.Windows.Foundation.Rect,  # intersectingRect
                                                  _Microsoft_UI_Xaml.IUIElement,  # subtree
                                                  _Pointer[_Windows_Foundation_Collections.IIterable[_Microsoft_UI_Xaml.IUIElement]]],  # result
                                                 _type.HRESULT]
    FindAllElementsInHostCoordinatesPoint: _Callable[[_struct.Windows.Foundation.Point,  # intersectingPoint
                                                      _Microsoft_UI_Xaml.IUIElement,  # subtree
                                                      _type.boolean,  # includeAllElements
                                                      _Pointer[_Windows_Foundation_Collections.IIterable[_Microsoft_UI_Xaml.IUIElement]]],  # result
                                                     _type.HRESULT]
    FindAllElementsInHostCoordinatesRect: _Callable[[_struct.Windows.Foundation.Rect,  # intersectingRect
                                                     _Microsoft_UI_Xaml.IUIElement,  # subtree
                                                     _type.boolean,  # includeAllElements
                                                     _Pointer[_Windows_Foundation_Collections.IIterable[_Microsoft_UI_Xaml.IUIElement]]],  # result
                                                    _type.HRESULT]
    GetChild: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # reference
                         _type.INT32,  # childIndex
                         _Pointer[_Microsoft_UI_Xaml.IDependencyObject]],  # result
                        _type.HRESULT]
    GetChildrenCount: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # reference
                                 _Pointer[_type.INT32]],  # result
                                _type.HRESULT]
    GetParent: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # reference
                          _Pointer[_Microsoft_UI_Xaml.IDependencyObject]],  # result
                         _type.HRESULT]
    DisconnectChildrenRecursive: _Callable[[_Microsoft_UI_Xaml.IUIElement],  # element
                                           _type.HRESULT]
    GetOpenPopups: _Callable[[_Microsoft_UI_Xaml.IWindow,  # window
                              _Pointer[_Windows_Foundation_Collections.IVectorView[_Microsoft_UI_Xaml_Controls_Primitives.IPopup]]],  # result
                             _type.HRESULT]
    GetOpenPopupsForXamlRoot: _Callable[[_Microsoft_UI_Xaml.IXamlRoot,  # xamlRoot
                                         _Pointer[_Windows_Foundation_Collections.IVectorView[_Microsoft_UI_Xaml_Controls_Primitives.IPopup]]],  # result
                                        _type.HRESULT]


class IXamlCompositionBrushBase(_inspectable.IInspectable):
    get_FallbackColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                 _type.HRESULT]
    put_FallbackColor: _Callable[[_struct.Windows.UI.Color],  # value
                                 _type.HRESULT]


class IXamlCompositionBrushBaseFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IXamlCompositionBrushBase]],  # value
                              _type.HRESULT]


class IXamlCompositionBrushBaseOverrides(_inspectable.IInspectable):
    OnConnected: _Callable[[],
                           _type.HRESULT]
    OnDisconnected: _Callable[[],
                              _type.HRESULT]


class IXamlCompositionBrushBaseProtected(_inspectable.IInspectable):
    get_CompositionBrush: _Callable[[_Pointer[_Microsoft_UI_Composition.ICompositionBrush]],  # value
                                    _type.HRESULT]
    put_CompositionBrush: _Callable[[_Microsoft_UI_Composition.ICompositionBrush],  # value
                                    _type.HRESULT]


class IXamlCompositionBrushBaseStatics(_inspectable.IInspectable, factory=True):
    get_FallbackColorProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]


class IXamlLight(_inspectable.IInspectable):
    pass


class IXamlLightFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IXamlLight]],  # value
                              _type.HRESULT]


class IXamlLightOverrides(_inspectable.IInspectable):
    GetId: _Callable[[_Pointer[_type.HSTRING]],  # result
                     _type.HRESULT]
    OnConnected: _Callable[[_Microsoft_UI_Xaml.IUIElement],  # newElement
                           _type.HRESULT]
    OnDisconnected: _Callable[[_Microsoft_UI_Xaml.IUIElement],  # oldElement
                              _type.HRESULT]


class IXamlLightProtected(_inspectable.IInspectable):
    get_CompositionLight: _Callable[[_Pointer[_Microsoft_UI_Composition.ICompositionLight]],  # value
                                    _type.HRESULT]
    put_CompositionLight: _Callable[[_Microsoft_UI_Composition.ICompositionLight],  # value
                                    _type.HRESULT]


class IXamlLightStatics(_inspectable.IInspectable, factory=True):
    AddTargetElement: _Callable[[_type.HSTRING,  # lightId
                                 _Microsoft_UI_Xaml.IUIElement],  # element
                                _type.HRESULT]
    RemoveTargetElement: _Callable[[_type.HSTRING,  # lightId
                                    _Microsoft_UI_Xaml.IUIElement],  # element
                                   _type.HRESULT]
    AddTargetBrush: _Callable[[_type.HSTRING,  # lightId
                               IBrush],  # brush
                              _type.HRESULT]
    RemoveTargetBrush: _Callable[[_type.HSTRING,  # lightId
                                  IBrush],  # brush
                                 _type.HRESULT]
