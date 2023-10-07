from __future__ import annotations as _

from typing import Callable as _Callable

from . import Connectivity as _Windows_Networking_Connectivity
from ... import inspectable as _inspectable
from ..... import enum as _enum
from ..... import type as _type
from ....._utils import _Pointer


class IEndpointPair(_inspectable.IInspectable):
    get_LocalHostName: _Callable[[_Pointer[IHostName]],  # value
                                 _type.HRESULT]
    put_LocalHostName: _Callable[[IHostName],  # value
                                 _type.HRESULT]
    get_LocalServiceName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    put_LocalServiceName: _Callable[[_type.HSTRING],  # value
                                    _type.HRESULT]
    get_RemoteHostName: _Callable[[_Pointer[IHostName]],  # value
                                  _type.HRESULT]
    put_RemoteHostName: _Callable[[IHostName],  # value
                                  _type.HRESULT]
    get_RemoteServiceName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    put_RemoteServiceName: _Callable[[_type.HSTRING],  # value
                                     _type.HRESULT]


class IEndpointPairFactory(_inspectable.IInspectable, factory=True):
    CreateEndpointPair: _Callable[[IHostName,  # localHostName
                                   _type.HSTRING,  # localServiceName
                                   IHostName,  # remoteHostName
                                   _type.HSTRING,  # remoteServiceName
                                   _Pointer[IEndpointPair]],  # value
                                  _type.HRESULT]


class IHostName(_inspectable.IInspectable):
    get_IPInformation: _Callable[[_Pointer[_Windows_Networking_Connectivity.IIPInformation]],  # value
                                 _type.HRESULT]
    get_RawName: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_CanonicalName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_Type: _Callable[[_Pointer[_enum.Windows.Networking.HostNameType]],  # value
                        _type.HRESULT]
    IsEqual: _Callable[[IHostName,  # hostName
                        _Pointer[_type.boolean]],  # isEqual
                       _type.HRESULT]


class IHostNameFactory(_inspectable.IInspectable, factory=True):
    CreateHostName: _Callable[[_type.HSTRING,  # hostName
                               _Pointer[IHostName]],  # value
                              _type.HRESULT]


class IHostNameStatics(_inspectable.IInspectable, factory=True):
    Compare: _Callable[[_type.HSTRING,  # value1
                        _type.HSTRING,  # value2
                        _Pointer[_type.INT32]],  # result
                       _type.HRESULT]
