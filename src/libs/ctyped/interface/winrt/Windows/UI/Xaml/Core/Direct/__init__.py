from __future__ import annotations

from typing import Callable as _Callable

from ...... import inspectable as _inspectable
from ........ import enum as _enum
from ........ import struct as _struct
from ........ import type as _type
from ........_utils import _Pointer


class IXamlDirect(_inspectable.IInspectable):
    GetObject: _Callable[[IXamlDirectObject,  # xamlDirectObject
                          _Pointer[_inspectable.IInspectable]],  # result
                         _type.HRESULT]
    GetXamlDirectObject: _Callable[[_inspectable.IInspectable,  # object
                                    _Pointer[IXamlDirectObject]],  # result
                                   _type.HRESULT]
    CreateInstance: _Callable[[_enum.Windows.UI.Xaml.Core.Direct.XamlTypeIndex,  # typeIndex
                               _Pointer[IXamlDirectObject]],  # result
                              _type.HRESULT]
    SetObjectProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                  _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                  _inspectable.IInspectable],  # value
                                 _type.HRESULT]
    SetXamlDirectObjectProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                            _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                            IXamlDirectObject],  # value
                                           _type.HRESULT]
    SetBooleanProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                   _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                   _type.boolean],  # value
                                  _type.HRESULT]
    SetDoubleProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                  _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                  _type.DOUBLE],  # value
                                 _type.HRESULT]
    SetInt32Property: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                 _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                 _type.INT32],  # value
                                _type.HRESULT]
    SetStringProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                  _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                  _type.HSTRING],  # value
                                 _type.HRESULT]
    SetDateTimeProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                    _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                    _struct.Windows.Foundation.DateTime],  # value
                                   _type.HRESULT]
    SetPointProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                 _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                 _struct.Windows.Foundation.Point],  # value
                                _type.HRESULT]
    SetRectProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                _struct.Windows.Foundation.Rect],  # value
                               _type.HRESULT]
    SetSizeProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                _struct.Windows.Foundation.Size],  # value
                               _type.HRESULT]
    SetTimeSpanProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                    _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                    _struct.Windows.Foundation.TimeSpan],  # value
                                   _type.HRESULT]
    SetColorProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                 _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                 _struct.Windows.UI.Color],  # value
                                _type.HRESULT]
    SetCornerRadiusProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                        _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                        _struct.Windows.UI.Xaml.CornerRadius],  # value
                                       _type.HRESULT]
    SetDurationProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                    _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                    _struct.Windows.UI.Xaml.Duration],  # value
                                   _type.HRESULT]
    SetGridLengthProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                      _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                      _struct.Windows.UI.Xaml.GridLength],  # value
                                     _type.HRESULT]
    SetThicknessProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                     _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                     _struct.Windows.UI.Xaml.Thickness],  # value
                                    _type.HRESULT]
    SetMatrixProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                  _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                  _struct.Windows.UI.Xaml.Media.Matrix],  # value
                                 _type.HRESULT]
    SetMatrix3DProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                    _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                    _struct.Windows.UI.Xaml.Media.Media3D.Matrix3D],  # value
                                   _type.HRESULT]
    SetEnumProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                _type.UINT32],  # value
                               _type.HRESULT]
    GetObjectProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                  _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                  _Pointer[_inspectable.IInspectable]],  # result
                                 _type.HRESULT]
    GetXamlDirectObjectProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                            _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                            _Pointer[IXamlDirectObject]],  # result
                                           _type.HRESULT]
    GetBooleanProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                   _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                   _Pointer[_type.boolean]],  # result
                                  _type.HRESULT]
    GetDoubleProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                  _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                  _Pointer[_type.DOUBLE]],  # result
                                 _type.HRESULT]
    GetInt32Property: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                 _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                 _Pointer[_type.INT32]],  # result
                                _type.HRESULT]
    GetStringProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                  _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                  _Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]
    GetDateTimeProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                    _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                    _Pointer[_struct.Windows.Foundation.DateTime]],  # result
                                   _type.HRESULT]
    GetPointProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                 _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                 _Pointer[_struct.Windows.Foundation.Point]],  # result
                                _type.HRESULT]
    GetRectProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                _Pointer[_struct.Windows.Foundation.Rect]],  # result
                               _type.HRESULT]
    GetSizeProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                _Pointer[_struct.Windows.Foundation.Size]],  # result
                               _type.HRESULT]
    GetTimeSpanProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                    _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                    _Pointer[_struct.Windows.Foundation.TimeSpan]],  # result
                                   _type.HRESULT]
    GetColorProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                 _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                 _Pointer[_struct.Windows.UI.Color]],  # result
                                _type.HRESULT]
    GetCornerRadiusProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                        _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                        _Pointer[_struct.Windows.UI.Xaml.CornerRadius]],  # result
                                       _type.HRESULT]
    GetDurationProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                    _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                    _Pointer[_struct.Windows.UI.Xaml.Duration]],  # result
                                   _type.HRESULT]
    GetGridLengthProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                      _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                      _Pointer[_struct.Windows.UI.Xaml.GridLength]],  # result
                                     _type.HRESULT]
    GetThicknessProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                     _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                     _Pointer[_struct.Windows.UI.Xaml.Thickness]],  # result
                                    _type.HRESULT]
    GetMatrixProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                  _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                  _Pointer[_struct.Windows.UI.Xaml.Media.Matrix]],  # result
                                 _type.HRESULT]
    GetMatrix3DProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                    _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                    _Pointer[_struct.Windows.UI.Xaml.Media.Media3D.Matrix3D]],  # result
                                   _type.HRESULT]
    GetEnumProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex,  # propertyIndex
                                _Pointer[_type.UINT32]],  # result
                               _type.HRESULT]
    ClearProperty: _Callable[[IXamlDirectObject,  # xamlDirectObject
                              _enum.Windows.UI.Xaml.Core.Direct.XamlPropertyIndex],  # propertyIndex
                             _type.HRESULT]
    GetCollectionCount: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                   _Pointer[_type.UINT32]],  # result
                                  _type.HRESULT]
    GetXamlDirectObjectFromCollectionAt: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                                    _type.UINT32,  # index
                                                    _Pointer[IXamlDirectObject]],  # result
                                                   _type.HRESULT]
    AddToCollection: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                IXamlDirectObject],  # value
                               _type.HRESULT]
    InsertIntoCollectionAt: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                       _type.UINT32,  # index
                                       IXamlDirectObject],  # value
                                      _type.HRESULT]
    RemoveFromCollection: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                     IXamlDirectObject,  # value
                                     _Pointer[_type.boolean]],  # result
                                    _type.HRESULT]
    RemoveFromCollectionAt: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                       _type.UINT32],  # index
                                      _type.HRESULT]
    ClearCollection: _Callable[[IXamlDirectObject],  # xamlDirectObject
                               _type.HRESULT]
    AddEventHandler: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                _enum.Windows.UI.Xaml.Core.Direct.XamlEventIndex,  # eventIndex
                                _inspectable.IInspectable],  # handler
                               _type.HRESULT]
    AddEventHandler_HandledEventsToo: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                                 _enum.Windows.UI.Xaml.Core.Direct.XamlEventIndex,  # eventIndex
                                                 _inspectable.IInspectable,  # handler
                                                 _type.boolean],  # handledEventsToo
                                                _type.HRESULT]
    RemoveEventHandler: _Callable[[IXamlDirectObject,  # xamlDirectObject
                                   _enum.Windows.UI.Xaml.Core.Direct.XamlEventIndex,  # eventIndex
                                   _inspectable.IInspectable],  # handler
                                  _type.HRESULT]


class IXamlDirectObject(_inspectable.IInspectable):
    pass


class IXamlDirectStatics(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[IXamlDirect]],  # result
                          _type.HRESULT]
