from __future__ import annotations as _

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IPnpObject(_inspectable.IInspectable):
    get_Type: _Callable[[_Pointer[_enum.Windows.Devices.Enumeration.Pnp.PnpObjectType]],  # value
                        _type.HRESULT]
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _inspectable.IInspectable]]],  # value
                              _type.HRESULT]
    Update: _Callable[[IPnpObjectUpdate],  # updateInfo
                      _type.HRESULT]


class IPnpObjectStatics(_inspectable.IInspectable):
    CreateFromIdAsync: _Callable[[_enum.Windows.Devices.Enumeration.Pnp.PnpObjectType,  # type
                                  _type.HSTRING,  # id
                                  _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # requestedProperties
                                  _Pointer[_Windows_Foundation.IAsyncOperation[IPnpObject]]],  # asyncOp
                                 _type.HRESULT]
    FindAllAsync: _Callable[[_enum.Windows.Devices.Enumeration.Pnp.PnpObjectType,  # type
                             _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # requestedProperties
                             _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IPnpObject]]]],  # asyncOp
                            _type.HRESULT]
    FindAllAsyncAqsFilter: _Callable[[_enum.Windows.Devices.Enumeration.Pnp.PnpObjectType,  # type
                                      _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # requestedProperties
                                      _type.HSTRING,  # aqsFilter
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IPnpObject]]]],  # asyncOp
                                     _type.HRESULT]
    CreateWatcher: _Callable[[_enum.Windows.Devices.Enumeration.Pnp.PnpObjectType,  # type
                              _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # requestedProperties
                              _Pointer[IPnpObjectWatcher]],  # watcher
                             _type.HRESULT]
    CreateWatcherAqsFilter: _Callable[[_enum.Windows.Devices.Enumeration.Pnp.PnpObjectType,  # type
                                       _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # requestedProperties
                                       _type.HSTRING,  # aqsFilter
                                       _Pointer[IPnpObjectWatcher]],  # watcher
                                      _type.HRESULT]

    _factory = True


class IPnpObjectUpdate(_inspectable.IInspectable):
    get_Type: _Callable[[_Pointer[_enum.Windows.Devices.Enumeration.Pnp.PnpObjectType]],  # value
                        _type.HRESULT]
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _inspectable.IInspectable]]],  # value
                              _type.HRESULT]


class IPnpObjectWatcher(_inspectable.IInspectable):
    add_Added: _Callable[[_Windows_Foundation.ITypedEventHandler[IPnpObjectWatcher, IPnpObject],  # handler
                          _Pointer[_struct.EventRegistrationToken]],  # token
                         _type.HRESULT]
    remove_Added: _Callable[[_struct.EventRegistrationToken],  # token
                            _type.HRESULT]
    add_Updated: _Callable[[_Windows_Foundation.ITypedEventHandler[IPnpObjectWatcher, IPnpObjectUpdate],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Updated: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_Removed: _Callable[[_Windows_Foundation.ITypedEventHandler[IPnpObjectWatcher, IPnpObjectUpdate],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Removed: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_EnumerationCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IPnpObjectWatcher, _inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_EnumerationCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    add_Stopped: _Callable[[_Windows_Foundation.ITypedEventHandler[IPnpObjectWatcher, _inspectable.IInspectable],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Stopped: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.Devices.Enumeration.DeviceWatcherStatus]],  # status
                          _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
