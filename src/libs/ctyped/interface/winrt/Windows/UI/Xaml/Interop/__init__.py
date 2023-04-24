from __future__ import annotations

from typing import Callable as _Callable

from ..... import inspectable as _inspectable
from ......um import Unknwnbase as _Unknwnbase
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class _IBindableVectorChangedEventHandler:
    Invoke: _Callable[[IBindableObservableVector,  # vector
                       _inspectable.IInspectable],  # e
                      _type.HRESULT]


class IBindableVectorChangedEventHandler(_IBindableVectorChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IBindableVectorChangedEventHandler_impl(_IBindableVectorChangedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _INotifyCollectionChangedEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       INotifyCollectionChangedEventArgs],  # e
                      _type.HRESULT]


class INotifyCollectionChangedEventHandler(_INotifyCollectionChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class INotifyCollectionChangedEventHandler_impl(_INotifyCollectionChangedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class IBindableIterable(_inspectable.IInspectable):
    First: _Callable[[_Pointer[IBindableIterator]],  # result
                     _type.HRESULT]


class IBindableIterator(_inspectable.IInspectable):
    get_Current: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                           _type.HRESULT]
    get_HasCurrent: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    MoveNext: _Callable[[_Pointer[_type.boolean]],  # result
                        _type.HRESULT]


class IBindableObservableVector(_inspectable.IInspectable):
    add_VectorChanged: _Callable[[IBindableVectorChangedEventHandler,  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_VectorChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]


class IBindableVector(_inspectable.IInspectable):
    GetAt: _Callable[[_type.UINT32,  # index
                      _Pointer[_inspectable.IInspectable]],  # result
                     _type.HRESULT]
    get_Size: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]
    GetView: _Callable[[_Pointer[IBindableVectorView]],  # result
                       _type.HRESULT]
    IndexOf: _Callable[[_inspectable.IInspectable,  # value
                        _Pointer[_type.UINT32],  # index
                        _Pointer[_type.boolean]],  # returnValue
                       _type.HRESULT]
    SetAt: _Callable[[_type.UINT32,  # index
                      _inspectable.IInspectable],  # value
                     _type.HRESULT]
    InsertAt: _Callable[[_type.UINT32,  # index
                         _inspectable.IInspectable],  # value
                        _type.HRESULT]
    RemoveAt: _Callable[[_type.UINT32],  # index
                        _type.HRESULT]
    Append: _Callable[[_inspectable.IInspectable],  # value
                      _type.HRESULT]
    RemoveAtEnd: _Callable[[],
                           _type.HRESULT]
    Clear: _Callable[[],
                     _type.HRESULT]


class IBindableVectorView(_inspectable.IInspectable):
    GetAt: _Callable[[_type.UINT32,  # index
                      _Pointer[_inspectable.IInspectable]],  # result
                     _type.HRESULT]
    get_Size: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]
    IndexOf: _Callable[[_inspectable.IInspectable,  # value
                        _Pointer[_type.UINT32],  # index
                        _Pointer[_type.boolean]],  # returnValue
                       _type.HRESULT]


class INotifyCollectionChanged(_inspectable.IInspectable):
    add_CollectionChanged: _Callable[[INotifyCollectionChangedEventHandler,  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_CollectionChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]


class INotifyCollectionChangedEventArgs(_inspectable.IInspectable):
    get_Action: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Interop.NotifyCollectionChangedAction]],  # value
                          _type.HRESULT]
    get_NewItems: _Callable[[_Pointer[IBindableVector]],  # value
                            _type.HRESULT]
    get_OldItems: _Callable[[_Pointer[IBindableVector]],  # value
                            _type.HRESULT]
    get_NewStartingIndex: _Callable[[_Pointer[_type.INT32]],  # value
                                    _type.HRESULT]
    get_OldStartingIndex: _Callable[[_Pointer[_type.INT32]],  # value
                                    _type.HRESULT]


class INotifyCollectionChangedEventArgsFactory(_inspectable.IInspectable):
    CreateInstanceWithAllParameters: _Callable[[_enum.Windows.UI.Xaml.Interop.NotifyCollectionChangedAction,  # action
                                                IBindableVector,  # newItems
                                                IBindableVector,  # oldItems
                                                _type.INT32,  # newIndex
                                                _type.INT32,  # oldIndex
                                                _inspectable.IInspectable,  # baseInterface
                                                _Pointer[_inspectable.IInspectable],  # innerInterface
                                                _Pointer[INotifyCollectionChangedEventArgs]],  # value
                                               _type.HRESULT]
