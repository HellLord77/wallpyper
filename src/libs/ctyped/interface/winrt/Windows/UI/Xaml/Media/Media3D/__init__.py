from __future__ import annotations as _

from typing import Callable as _Callable

from .... import Xaml as _Windows_UI_Xaml
from ...... import inspectable as _inspectable
from ........ import struct as _struct
from ........ import type as _type
from ........_utils import _Pointer


class ICompositeTransform3D(_inspectable.IInspectable):
    get_CenterX: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    put_CenterX: _Callable[[_type.DOUBLE],  # value
                           _type.HRESULT]
    get_CenterY: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    put_CenterY: _Callable[[_type.DOUBLE],  # value
                           _type.HRESULT]
    get_CenterZ: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    put_CenterZ: _Callable[[_type.DOUBLE],  # value
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
    get_ScaleX: _Callable[[_Pointer[_type.DOUBLE]],  # value
                          _type.HRESULT]
    put_ScaleX: _Callable[[_type.DOUBLE],  # value
                          _type.HRESULT]
    get_ScaleY: _Callable[[_Pointer[_type.DOUBLE]],  # value
                          _type.HRESULT]
    put_ScaleY: _Callable[[_type.DOUBLE],  # value
                          _type.HRESULT]
    get_ScaleZ: _Callable[[_Pointer[_type.DOUBLE]],  # value
                          _type.HRESULT]
    put_ScaleZ: _Callable[[_type.DOUBLE],  # value
                          _type.HRESULT]
    get_TranslateX: _Callable[[_Pointer[_type.DOUBLE]],  # value
                              _type.HRESULT]
    put_TranslateX: _Callable[[_type.DOUBLE],  # value
                              _type.HRESULT]
    get_TranslateY: _Callable[[_Pointer[_type.DOUBLE]],  # value
                              _type.HRESULT]
    put_TranslateY: _Callable[[_type.DOUBLE],  # value
                              _type.HRESULT]
    get_TranslateZ: _Callable[[_Pointer[_type.DOUBLE]],  # value
                              _type.HRESULT]
    put_TranslateZ: _Callable[[_type.DOUBLE],  # value
                              _type.HRESULT]


class ICompositeTransform3DStatics(_inspectable.IInspectable):
    get_CenterXProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_CenterYProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_CenterZProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_RotationXProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_RotationYProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_RotationZProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_ScaleXProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_ScaleYProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_ScaleZProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_TranslateXProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_TranslateYProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_TranslateZProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]

    _factory = True


class IMatrix3DHelper(_inspectable.IInspectable):
    pass


class IMatrix3DHelperStatics(_inspectable.IInspectable):
    get_Identity: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Media.Media3D.Matrix3D]],  # value
                            _type.HRESULT]
    Multiply: _Callable[[_struct.Windows.UI.Xaml.Media.Media3D.Matrix3D,  # matrix1
                         _struct.Windows.UI.Xaml.Media.Media3D.Matrix3D,  # matrix2
                         _Pointer[_struct.Windows.UI.Xaml.Media.Media3D.Matrix3D]],  # result
                        _type.HRESULT]
    FromElements: _Callable[[_type.DOUBLE,  # m11
                             _type.DOUBLE,  # m12
                             _type.DOUBLE,  # m13
                             _type.DOUBLE,  # m14
                             _type.DOUBLE,  # m21
                             _type.DOUBLE,  # m22
                             _type.DOUBLE,  # m23
                             _type.DOUBLE,  # m24
                             _type.DOUBLE,  # m31
                             _type.DOUBLE,  # m32
                             _type.DOUBLE,  # m33
                             _type.DOUBLE,  # m34
                             _type.DOUBLE,  # offsetX
                             _type.DOUBLE,  # offsetY
                             _type.DOUBLE,  # offsetZ
                             _type.DOUBLE,  # m44
                             _Pointer[_struct.Windows.UI.Xaml.Media.Media3D.Matrix3D]],  # result
                            _type.HRESULT]
    GetHasInverse: _Callable[[_struct.Windows.UI.Xaml.Media.Media3D.Matrix3D,  # target
                              _Pointer[_type.boolean]],  # result
                             _type.HRESULT]
    GetIsIdentity: _Callable[[_struct.Windows.UI.Xaml.Media.Media3D.Matrix3D,  # target
                              _Pointer[_type.boolean]],  # result
                             _type.HRESULT]
    Invert: _Callable[[_struct.Windows.UI.Xaml.Media.Media3D.Matrix3D,  # target
                       _Pointer[_struct.Windows.UI.Xaml.Media.Media3D.Matrix3D]],  # result
                      _type.HRESULT]

    _factory = True


class IPerspectiveTransform3D(_inspectable.IInspectable):
    get_Depth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                         _type.HRESULT]
    put_Depth: _Callable[[_type.DOUBLE],  # value
                         _type.HRESULT]
    get_OffsetX: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    put_OffsetX: _Callable[[_type.DOUBLE],  # value
                           _type.HRESULT]
    get_OffsetY: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    put_OffsetY: _Callable[[_type.DOUBLE],  # value
                           _type.HRESULT]


class IPerspectiveTransform3DStatics(_inspectable.IInspectable):
    get_DepthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_OffsetXProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_OffsetYProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]

    _factory = True


class ITransform3D(_inspectable.IInspectable):
    pass


class ITransform3DFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ITransform3D]],  # value
                              _type.HRESULT]
