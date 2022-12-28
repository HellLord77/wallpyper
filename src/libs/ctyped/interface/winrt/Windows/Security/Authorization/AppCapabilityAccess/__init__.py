from __future__ import annotations as _

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from .... import System as _Windows_System
from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IAppCapability(_inspectable.IInspectable):
    get_CapabilityName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]
    RequestAccessAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Security.Authorization.AppCapabilityAccess.AppCapabilityAccessStatus]]],  # operation
                                  _type.HRESULT]
    CheckAccess: _Callable[[_Pointer[_enum.Windows.Security.Authorization.AppCapabilityAccess.AppCapabilityAccessStatus]],  # result
                           _type.HRESULT]
    add_AccessChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppCapability, IAppCapabilityAccessChangedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_AccessChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]


class IAppCapability2(_inspectable.IInspectable):
    get_DisplayMessage: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    put_DisplayMessage: _Callable[[_type.HSTRING],  # value
                                  _type.HRESULT]


class IAppCapabilityAccessChangedEventArgs(_inspectable.IInspectable):
    pass


class IAppCapabilityStatics(_inspectable.IInspectable):
    RequestAccessForCapabilitiesAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # capabilityNames
                                                  _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _enum.Windows.Security.Authorization.AppCapabilityAccess.AppCapabilityAccessStatus]]]],  # operation
                                                 _type.HRESULT]
    RequestAccessForCapabilitiesForUserAsync: _Callable[[_Windows_System.IUser,  # user
                                                         _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # capabilityNames
                                                         _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _enum.Windows.Security.Authorization.AppCapabilityAccess.AppCapabilityAccessStatus]]]],  # operation
                                                        _type.HRESULT]
    Create: _Callable[[_type.HSTRING,  # capabilityName
                       _Pointer[IAppCapability]],  # result
                      _type.HRESULT]
    CreateWithProcessIdForUser: _Callable[[_Windows_System.IUser,  # user
                                           _type.HSTRING,  # capabilityName
                                           _type.UINT32,  # pid
                                           _Pointer[IAppCapability]],  # result
                                          _type.HRESULT]

    _factory = True
