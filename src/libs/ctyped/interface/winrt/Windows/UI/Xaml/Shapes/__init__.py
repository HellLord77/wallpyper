from __future__ import annotations

from typing import Callable as _Callable

from .. import Media as _Windows_UI_Xaml_Media
from ... import Composition as _Windows_UI_Composition
from ... import Xaml as _Windows_UI_Xaml
from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IEllipse(_inspectable.IInspectable):
    pass


class ILine(_inspectable.IInspectable):
    get_X1: _Callable[[_Pointer[_type.DOUBLE]],  # value
                      _type.HRESULT]
    put_X1: _Callable[[_type.DOUBLE],  # value
                      _type.HRESULT]
    get_Y1: _Callable[[_Pointer[_type.DOUBLE]],  # value
                      _type.HRESULT]
    put_Y1: _Callable[[_type.DOUBLE],  # value
                      _type.HRESULT]
    get_X2: _Callable[[_Pointer[_type.DOUBLE]],  # value
                      _type.HRESULT]
    put_X2: _Callable[[_type.DOUBLE],  # value
                      _type.HRESULT]
    get_Y2: _Callable[[_Pointer[_type.DOUBLE]],  # value
                      _type.HRESULT]
    put_Y2: _Callable[[_type.DOUBLE],  # value
                      _type.HRESULT]


class ILineStatics(_inspectable.IInspectable):
    get_X1Property: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                              _type.HRESULT]
    get_Y1Property: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                              _type.HRESULT]
    get_X2Property: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                              _type.HRESULT]
    get_Y2Property: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                              _type.HRESULT]

    _factory = True


class IPath(_inspectable.IInspectable):
    get_Data: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IGeometry]],  # value
                        _type.HRESULT]
    put_Data: _Callable[[_Windows_UI_Xaml_Media.IGeometry],  # value
                        _type.HRESULT]


class IPathFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IPath]],  # value
                              _type.HRESULT]


class IPathStatics(_inspectable.IInspectable):
    get_DataProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]

    _factory = True


class IPolygon(_inspectable.IInspectable):
    get_FillRule: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Media.FillRule]],  # value
                            _type.HRESULT]
    put_FillRule: _Callable[[_enum.Windows.UI.Xaml.Media.FillRule],  # value
                            _type.HRESULT]
    get_Points: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_struct.Windows.Foundation.Point]]],  # value
                          _type.HRESULT]
    put_Points: _Callable[[_Windows_Foundation_Collections.IVector[_struct.Windows.Foundation.Point]],  # value
                          _type.HRESULT]


class IPolygonStatics(_inspectable.IInspectable):
    get_FillRuleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_PointsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]

    _factory = True


class IPolyline(_inspectable.IInspectable):
    get_FillRule: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Media.FillRule]],  # value
                            _type.HRESULT]
    put_FillRule: _Callable[[_enum.Windows.UI.Xaml.Media.FillRule],  # value
                            _type.HRESULT]
    get_Points: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_struct.Windows.Foundation.Point]]],  # value
                          _type.HRESULT]
    put_Points: _Callable[[_Windows_Foundation_Collections.IVector[_struct.Windows.Foundation.Point]],  # value
                          _type.HRESULT]


class IPolylineStatics(_inspectable.IInspectable):
    get_FillRuleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_PointsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]

    _factory = True


class IRectangle(_inspectable.IInspectable):
    get_RadiusX: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    put_RadiusX: _Callable[[_type.DOUBLE],  # value
                           _type.HRESULT]
    get_RadiusY: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    put_RadiusY: _Callable[[_type.DOUBLE],  # value
                           _type.HRESULT]


class IRectangleStatics(_inspectable.IInspectable):
    get_RadiusXProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_RadiusYProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]

    _factory = True


class IShape(_inspectable.IInspectable):
    get_Fill: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                        _type.HRESULT]
    put_Fill: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                        _type.HRESULT]
    get_Stroke: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                          _type.HRESULT]
    put_Stroke: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                          _type.HRESULT]
    get_StrokeMiterLimit: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]
    put_StrokeMiterLimit: _Callable[[_type.DOUBLE],  # value
                                    _type.HRESULT]
    get_StrokeThickness: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                   _type.HRESULT]
    put_StrokeThickness: _Callable[[_type.DOUBLE],  # value
                                   _type.HRESULT]
    get_StrokeStartLineCap: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Media.PenLineCap]],  # value
                                      _type.HRESULT]
    put_StrokeStartLineCap: _Callable[[_enum.Windows.UI.Xaml.Media.PenLineCap],  # value
                                      _type.HRESULT]
    get_StrokeEndLineCap: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Media.PenLineCap]],  # value
                                    _type.HRESULT]
    put_StrokeEndLineCap: _Callable[[_enum.Windows.UI.Xaml.Media.PenLineCap],  # value
                                    _type.HRESULT]
    get_StrokeLineJoin: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Media.PenLineJoin]],  # value
                                  _type.HRESULT]
    put_StrokeLineJoin: _Callable[[_enum.Windows.UI.Xaml.Media.PenLineJoin],  # value
                                  _type.HRESULT]
    get_StrokeDashOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]
    put_StrokeDashOffset: _Callable[[_type.DOUBLE],  # value
                                    _type.HRESULT]
    get_StrokeDashCap: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Media.PenLineCap]],  # value
                                 _type.HRESULT]
    put_StrokeDashCap: _Callable[[_enum.Windows.UI.Xaml.Media.PenLineCap],  # value
                                 _type.HRESULT]
    get_StrokeDashArray: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.DOUBLE]]],  # value
                                   _type.HRESULT]
    put_StrokeDashArray: _Callable[[_Windows_Foundation_Collections.IVector[_type.DOUBLE]],  # value
                                   _type.HRESULT]
    get_Stretch: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Media.Stretch]],  # value
                           _type.HRESULT]
    put_Stretch: _Callable[[_enum.Windows.UI.Xaml.Media.Stretch],  # value
                           _type.HRESULT]
    get_GeometryTransform: _Callable[[_Pointer[_Windows_UI_Xaml_Media.ITransform]],  # value
                                     _type.HRESULT]


class IShape2(_inspectable.IInspectable):
    GetAlphaMask: _Callable[[_Pointer[_Windows_UI_Composition.ICompositionBrush]],  # result
                            _type.HRESULT]


class IShapeFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IShape]],  # value
                              _type.HRESULT]


class IShapeStatics(_inspectable.IInspectable):
    get_FillProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]
    get_StrokeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_StrokeMiterLimitProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_StrokeThicknessProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_StrokeStartLineCapProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_StrokeEndLineCapProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_StrokeLineJoinProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_StrokeDashOffsetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_StrokeDashCapProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_StrokeDashArrayProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_StretchProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]

    _factory = True
