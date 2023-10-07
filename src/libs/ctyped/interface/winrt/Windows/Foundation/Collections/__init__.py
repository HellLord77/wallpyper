from __future__ import annotations as _

from typing import Callable as _Callable
from typing import Generic as _Generic

from .... import inspectable as _inspectable
from ..... import _K
from ..... import _T
from ..... import _Template
from ..... import _V
from .....um import Unknwnbase as _Unknwnbase
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IIterator(_Template, _Generic[_T], _inspectable.IInspectable):
    get_Current: _Callable[[_Pointer[_T]],  # current
                           _type.HRESULT]
    get_HasCurrent: _Callable[[_Pointer[_type.boolean]],  # hasCurrent
                              _type.HRESULT]
    MoveNext: _Callable[[_Pointer[_type.boolean]],  # hasCurrent
                        _type.HRESULT]
    GetMany: _Callable[[_type.c_uint,  # capacity
                        _Pointer[_T],  # value
                        _Pointer[_type.c_uint]],  # actual
                       _type.HRESULT]


class IIterable(_Template, _Generic[_T], _inspectable.IInspectable):
    First: _Callable[[_Pointer[IIterator[_T]]],  # first
                     _type.HRESULT]


class IVectorView(_Template, _Generic[_T], _inspectable.IInspectable):
    GetAt: _Callable[[_type.c_uint,  # index
                      _Pointer[_T]],  # item
                     _type.HRESULT]
    get_Size: _Callable[[_Pointer[_type.c_uint]],  # size
                        _type.HRESULT]
    IndexOf: _Callable[[_T,  # value
                        _Pointer[_type.c_uint],  # index
                        _Pointer[_type.boolean]],  # found
                       _type.HRESULT]
    GetMany: _Callable[[_type.c_uint,  # startIndex
                        _type.c_uint,  # capacity
                        _Pointer[_T],  # value
                        _Pointer[_type.c_uint]],  # actual
                       _type.HRESULT]


class IVector(_Template, _Generic[_T], _inspectable.IInspectable):
    GetAt: _Callable[[_type.c_uint,  # index
                      _Pointer[_T]],  # item
                     _type.HRESULT]
    get_Size: _Callable[[_Pointer[_type.c_uint]],  # size
                        _type.HRESULT]
    GetView: _Callable[[_Pointer[IVectorView[_T]]],  # view
                       _type.HRESULT]
    IndexOf: _Callable[[_T,  # value
                        _Pointer[_type.c_uint],  # index
                        _Pointer[_type.boolean]],  # found
                       _type.HRESULT]
    SetAt: _Callable[[_type.c_uint,  # index
                      _T],  # item
                     _type.HRESULT]
    InsertAt: _Callable[[_type.c_uint,  # index
                         _T],  # item
                        _type.HRESULT]
    RemoveAt: _Callable[[_type.c_uint],  # index
                        _type.HRESULT]
    Append: _Callable[[_T],  # item
                      _type.HRESULT]
    RemoveAtEnd: _Callable[[],
                           _type.HRESULT]
    Clear: _Callable[[],
                     _type.HRESULT]
    GetMany: _Callable[[_type.c_uint,  # startIndex
                        _type.c_uint,  # capacity
                        _Pointer[_T],  # value
                        _Pointer[_type.c_uint]],  # actual
                       _type.HRESULT]
    ReplaceAll: _Callable[[_type.c_uint,  # count
                           _Pointer[_T]],  # value
                          _type.HRESULT]


class IKeyValuePair(_Template, _Generic[_K, _V], _inspectable.IInspectable):
    get_Key: _Callable[[_Pointer[_K]],  # key
                       _type.HRESULT]
    get_Value: _Callable[[_Pointer[_V]],  # value
                         _type.HRESULT]


class IMapView(_Template, _Generic[_K, _V], _inspectable.IInspectable):
    Lookup: _Callable[[_K,  # key
                       _Pointer[_V]],  # value
                      _type.HRESULT]
    get_Size: _Callable[[_Pointer[_type.c_uint]],  # size
                        _type.HRESULT]
    HasKey: _Callable[[_K,  # key
                       _Pointer[_type.boolean]],  # found
                      _type.HRESULT]
    Split: _Callable[[_Pointer[IMapView[_K, _V]],  # firstPartition
                      _Pointer[IMapView[_K, _V]]],  # secondPartition
                     _type.HRESULT]


class IMap(_Template, _Generic[_K, _V], _inspectable.IInspectable):
    Lookup: _Callable[[_K,  # key
                       _Pointer[_V]],  # value
                      _type.HRESULT]
    get_Size: _Callable[[_Pointer[_type.c_uint]],  # size
                        _type.HRESULT]
    HasKey: _Callable[[_K,  # key
                       _Pointer[_type.boolean]],  # found
                      _type.HRESULT]
    GetView: _Callable[[_Pointer[IMapView[_K, _V]]],  # view
                       _type.HRESULT]
    Insert: _Callable[[_K,  # key
                       _V,  # value
                       _Pointer[_type.boolean]],  # replaced
                      _type.HRESULT]
    Remove: _Callable[[_K],  # key
                      _type.HRESULT]
    Clear: _Callable[[],
                     _type.HRESULT]


class _IVectorChangedEventHandler(_Template):
    Invoke: _Callable[[IObservableVector[_T],  # sender
                       IVectorChangedEventArgs],  # e
                      _type.HRESULT]


class IVectorChangedEventHandler(_IVectorChangedEventHandler, _Generic[_T], _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IVectorChangedEventHandler_impl(_IVectorChangedEventHandler, _Generic[_T], _Unknwnbase.IUnknown_impl):
    pass


class IObservableVector(_Template, _Generic[_T], _inspectable.IInspectable):
    add_VectorChanged: _Callable[[IVectorChangedEventHandler[_T],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_VectorChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]


class IMapChangedEventArgs(_Template, _Generic[_K], _inspectable.IInspectable):
    get_CollectionChange: _Callable[[_Pointer[_enum.Windows.Foundation.Collections.CollectionChange]],  # value
                                    _type.HRESULT]
    get_Key: _Callable[[_Pointer[_K]],  # value
                       _type.HRESULT]


class _IMapChangedEventHandler(_Template):
    Invoke: _Callable[[IObservableMap[_K, _V],  # sender
                       IMapChangedEventArgs[_K]],  # e
                      _type.HRESULT]


class IMapChangedEventHandler(_IMapChangedEventHandler, _Generic[_K, _V], _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IMapChangedEventHandler_impl(_IMapChangedEventHandler, _Generic[_K, _V], _Unknwnbase.IUnknown_impl):
    pass


class IObservableMap(_Template, _Generic[_K, _V], _inspectable.IInspectable):
    add_MapChanged: _Callable[[IMapChangedEventHandler[_K, _V],  # handler
                               _Pointer[_struct.EventRegistrationToken]],  # token
                              _type.HRESULT]
    remove_MapChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                 _type.HRESULT]


class IVectorChangedEventArgs(_inspectable.IInspectable):
    get_CollectionChange: _Callable[[_Pointer[_enum.Windows.Foundation.Collections.CollectionChange]],
                                    _type.HRESULT]
    get_Index: _Callable[[_Pointer[_type.c_uint]],
                         _type.HRESULT]


class IPropertySet(_inspectable.IInspectable):
    pass
