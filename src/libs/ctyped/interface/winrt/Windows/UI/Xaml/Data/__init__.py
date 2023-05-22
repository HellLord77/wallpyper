from __future__ import annotations

from typing import Callable as _Callable

from ... import Xaml as _Windows_UI_Xaml
from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ......um import Unknwnbase as _Unknwnbase
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class _ICurrentChangingEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       ICurrentChangingEventArgs],  # e
                      _type.HRESULT]


class ICurrentChangingEventHandler(_ICurrentChangingEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICurrentChangingEventHandler_impl(_ICurrentChangingEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IPropertyChangedEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       IPropertyChangedEventArgs],  # e
                      _type.HRESULT]


class IPropertyChangedEventHandler(_IPropertyChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IPropertyChangedEventHandler_impl(_IPropertyChangedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class IBinding(_inspectable.IInspectable):
    get_Path: _Callable[[_Pointer[_Windows_UI_Xaml.IPropertyPath]],  # value
                        _type.HRESULT]
    put_Path: _Callable[[_Windows_UI_Xaml.IPropertyPath],  # value
                        _type.HRESULT]
    get_Mode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Data.BindingMode]],  # value
                        _type.HRESULT]
    put_Mode: _Callable[[_enum.Windows.UI.Xaml.Data.BindingMode],  # value
                        _type.HRESULT]
    get_Source: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                          _type.HRESULT]
    put_Source: _Callable[[_inspectable.IInspectable],  # value
                          _type.HRESULT]
    get_RelativeSource: _Callable[[_Pointer[IRelativeSource]],  # value
                                  _type.HRESULT]
    put_RelativeSource: _Callable[[IRelativeSource],  # value
                                  _type.HRESULT]
    get_ElementName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_ElementName: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_Converter: _Callable[[_Pointer[IValueConverter]],  # value
                             _type.HRESULT]
    put_Converter: _Callable[[IValueConverter],  # value
                             _type.HRESULT]
    get_ConverterParameter: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                      _type.HRESULT]
    put_ConverterParameter: _Callable[[_inspectable.IInspectable],  # value
                                      _type.HRESULT]
    get_ConverterLanguage: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    put_ConverterLanguage: _Callable[[_type.HSTRING],  # value
                                     _type.HRESULT]


class IBinding2(_inspectable.IInspectable):
    get_FallbackValue: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                 _type.HRESULT]
    put_FallbackValue: _Callable[[_inspectable.IInspectable],  # value
                                 _type.HRESULT]
    get_TargetNullValue: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                   _type.HRESULT]
    put_TargetNullValue: _Callable[[_inspectable.IInspectable],  # value
                                   _type.HRESULT]
    get_UpdateSourceTrigger: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Data.UpdateSourceTrigger]],  # value
                                       _type.HRESULT]
    put_UpdateSourceTrigger: _Callable[[_enum.Windows.UI.Xaml.Data.UpdateSourceTrigger],  # value
                                       _type.HRESULT]


class IBindingBase(_inspectable.IInspectable):
    pass


class IBindingBaseFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IBindingBase]],  # value
                              _type.HRESULT]


class IBindingExpression(_inspectable.IInspectable):
    get_DataItem: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                            _type.HRESULT]
    get_ParentBinding: _Callable[[_Pointer[IBinding]],  # value
                                 _type.HRESULT]
    UpdateSource: _Callable[[],
                            _type.HRESULT]


class IBindingExpressionBase(_inspectable.IInspectable):
    pass


class IBindingExpressionBaseFactory(_inspectable.IInspectable):
    pass


class IBindingExpressionFactory(_inspectable.IInspectable):
    pass


class IBindingFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IBinding]],  # value
                              _type.HRESULT]


class IBindingOperations(_inspectable.IInspectable):
    pass


class IBindingOperationsStatics(_inspectable.IInspectable, factory=True):
    SetBinding: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # target
                           _Windows_UI_Xaml.IDependencyProperty,  # dp
                           IBindingBase],  # binding
                          _type.HRESULT]


class ICollectionView(_inspectable.IInspectable):
    get_CurrentItem: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                               _type.HRESULT]
    get_CurrentPosition: _Callable[[_Pointer[_type.INT32]],  # value
                                   _type.HRESULT]
    get_IsCurrentAfterLast: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    get_IsCurrentBeforeFirst: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_CollectionGroups: _Callable[[_Pointer[_Windows_Foundation_Collections.IObservableVector[_inspectable.IInspectable]]],  # value
                                    _type.HRESULT]
    get_HasMoreItems: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    add_CurrentChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_CurrentChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_CurrentChanging: _Callable[[ICurrentChangingEventHandler,  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_CurrentChanging: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    MoveCurrentTo: _Callable[[_inspectable.IInspectable,  # item
                              _Pointer[_type.boolean]],  # result
                             _type.HRESULT]
    MoveCurrentToPosition: _Callable[[_type.INT32,  # index
                                      _Pointer[_type.boolean]],  # result
                                     _type.HRESULT]
    MoveCurrentToFirst: _Callable[[_Pointer[_type.boolean]],  # result
                                  _type.HRESULT]
    MoveCurrentToLast: _Callable[[_Pointer[_type.boolean]],  # result
                                 _type.HRESULT]
    MoveCurrentToNext: _Callable[[_Pointer[_type.boolean]],  # result
                                 _type.HRESULT]
    MoveCurrentToPrevious: _Callable[[_Pointer[_type.boolean]],  # result
                                     _type.HRESULT]
    LoadMoreItemsAsync: _Callable[[_type.UINT32,  # count
                                   _Pointer[_Windows_Foundation.IAsyncOperation[_struct.Windows.UI.Xaml.Data.LoadMoreItemsResult]]],  # operation
                                  _type.HRESULT]


class ICollectionViewFactory(_inspectable.IInspectable):
    CreateView: _Callable[[_Pointer[ICollectionView]],  # result
                          _type.HRESULT]


class ICollectionViewGroup(_inspectable.IInspectable):
    get_Group: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                         _type.HRESULT]
    get_GroupItems: _Callable[[_Pointer[_Windows_Foundation_Collections.IObservableVector[_inspectable.IInspectable]]],  # value
                              _type.HRESULT]


class ICollectionViewSource(_inspectable.IInspectable):
    get_Source: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                          _type.HRESULT]
    put_Source: _Callable[[_inspectable.IInspectable],  # value
                          _type.HRESULT]
    get_View: _Callable[[_Pointer[ICollectionView]],  # value
                        _type.HRESULT]
    get_IsSourceGrouped: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    put_IsSourceGrouped: _Callable[[_type.boolean],  # value
                                   _type.HRESULT]
    get_ItemsPath: _Callable[[_Pointer[_Windows_UI_Xaml.IPropertyPath]],  # value
                             _type.HRESULT]
    put_ItemsPath: _Callable[[_Windows_UI_Xaml.IPropertyPath],  # value
                             _type.HRESULT]


class ICollectionViewSourceStatics(_inspectable.IInspectable, factory=True):
    get_SourceProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_ViewProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]
    get_IsSourceGroupedProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_ItemsPathProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]


class ICurrentChangingEventArgs(_inspectable.IInspectable):
    get_Cancel: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_Cancel: _Callable[[_type.boolean],  # value
                          _type.HRESULT]
    get_IsCancelable: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]


class ICurrentChangingEventArgsFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ICurrentChangingEventArgs]],  # value
                              _type.HRESULT]
    CreateWithCancelableParameter: _Callable[[_type.boolean,  # isCancelable
                                              _inspectable.IInspectable,  # baseInterface
                                              _Pointer[_inspectable.IInspectable],  # innerInterface
                                              _Pointer[ICurrentChangingEventArgs]],  # value
                                             _type.HRESULT]


class ICustomProperty(_inspectable.IInspectable):
    get_Type: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Interop.TypeName]],  # value
                        _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    GetValue: _Callable[[_inspectable.IInspectable,  # target
                         _Pointer[_inspectable.IInspectable]],  # result
                        _type.HRESULT]
    SetValue: _Callable[[_inspectable.IInspectable,  # target
                         _inspectable.IInspectable],  # value
                        _type.HRESULT]
    GetIndexedValue: _Callable[[_inspectable.IInspectable,  # target
                                _inspectable.IInspectable,  # index
                                _Pointer[_inspectable.IInspectable]],  # result
                               _type.HRESULT]
    SetIndexedValue: _Callable[[_inspectable.IInspectable,  # target
                                _inspectable.IInspectable,  # value
                                _inspectable.IInspectable],  # index
                               _type.HRESULT]
    get_CanWrite: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_CanRead: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]


class ICustomPropertyProvider(_inspectable.IInspectable):
    GetCustomProperty: _Callable[[_type.HSTRING,  # name
                                  _Pointer[ICustomProperty]],  # result
                                 _type.HRESULT]
    GetIndexedProperty: _Callable[[_type.HSTRING,  # name
                                   _struct.Windows.UI.Xaml.Interop.TypeName,  # type
                                   _Pointer[ICustomProperty]],  # result
                                  _type.HRESULT]
    GetStringRepresentation: _Callable[[_Pointer[_type.HSTRING]],  # result
                                       _type.HRESULT]
    get_Type: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Interop.TypeName]],  # value
                        _type.HRESULT]


class IItemIndexRange(_inspectable.IInspectable):
    get_FirstIndex: _Callable[[_Pointer[_type.INT32]],  # value
                              _type.HRESULT]
    get_Length: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    get_LastIndex: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]


class IItemIndexRangeFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_type.INT32,  # firstIndex
                               _type.UINT32,  # length
                               _inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IItemIndexRange]],  # value
                              _type.HRESULT]


class IItemsRangeInfo(_inspectable.IInspectable):
    RangesChanged: _Callable[[IItemIndexRange,  # visibleRange
                              _Windows_Foundation_Collections.IVectorView[IItemIndexRange]],  # trackedItems
                             _type.HRESULT]


class INotifyPropertyChanged(_inspectable.IInspectable):
    add_PropertyChanged: _Callable[[IPropertyChangedEventHandler,  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_PropertyChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]


class IPropertyChangedEventArgs(_inspectable.IInspectable):
    get_PropertyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]


class IPropertyChangedEventArgsFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_type.HSTRING,  # name
                               _inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IPropertyChangedEventArgs]],  # value
                              _type.HRESULT]


class IRelativeSource(_inspectable.IInspectable):
    get_Mode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Data.RelativeSourceMode]],  # value
                        _type.HRESULT]
    put_Mode: _Callable[[_enum.Windows.UI.Xaml.Data.RelativeSourceMode],  # value
                        _type.HRESULT]


class IRelativeSourceFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IRelativeSource]],  # value
                              _type.HRESULT]


class ISelectionInfo(_inspectable.IInspectable):
    SelectRange: _Callable[[IItemIndexRange],  # itemIndexRange
                           _type.HRESULT]
    DeselectRange: _Callable[[IItemIndexRange],  # itemIndexRange
                             _type.HRESULT]
    IsSelected: _Callable[[_type.INT32,  # index
                           _Pointer[_type.boolean]],  # result
                          _type.HRESULT]
    GetSelectedRanges: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IItemIndexRange]]],  # result
                                 _type.HRESULT]


class ISupportIncrementalLoading(_inspectable.IInspectable):
    LoadMoreItemsAsync: _Callable[[_type.UINT32,  # count
                                   _Pointer[_Windows_Foundation.IAsyncOperation[_struct.Windows.UI.Xaml.Data.LoadMoreItemsResult]]],  # operation
                                  _type.HRESULT]
    get_HasMoreItems: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]


class IValueConverter(_inspectable.IInspectable):
    Convert: _Callable[[_inspectable.IInspectable,  # value
                        _struct.Windows.UI.Xaml.Interop.TypeName,  # targetType
                        _inspectable.IInspectable,  # parameter
                        _type.HSTRING,  # language
                        _Pointer[_inspectable.IInspectable]],  # result
                       _type.HRESULT]
    ConvertBack: _Callable[[_inspectable.IInspectable,  # value
                            _struct.Windows.UI.Xaml.Interop.TypeName,  # targetType
                            _inspectable.IInspectable,  # parameter
                            _type.HSTRING,  # language
                            _Pointer[_inspectable.IInspectable]],  # result
                           _type.HRESULT]
