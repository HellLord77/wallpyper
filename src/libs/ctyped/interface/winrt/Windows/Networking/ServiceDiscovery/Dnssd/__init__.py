from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Connectivity as _Windows_Networking_Connectivity
from ... import Sockets as _Windows_Networking_Sockets
from .... import Foundation as _Windows_Foundation
from .... import Networking as _Windows_Networking
from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IDnssdRegistrationResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Networking.ServiceDiscovery.Dnssd.DnssdRegistrationStatus]],  # value
                          _type.HRESULT]
    get_IPAddress: _Callable[[_Pointer[_Windows_Networking.IHostName]],  # value
                             _type.HRESULT]
    get_HasInstanceNameChanged: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]


class IDnssdServiceInstance(_inspectable.IInspectable):
    get_DnssdServiceInstanceName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                            _type.HRESULT]
    put_DnssdServiceInstanceName: _Callable[[_type.HSTRING],  # value
                                            _type.HRESULT]
    get_HostName: _Callable[[_Pointer[_Windows_Networking.IHostName]],  # value
                            _type.HRESULT]
    put_HostName: _Callable[[_Windows_Networking.IHostName],  # value
                            _type.HRESULT]
    get_Port: _Callable[[_Pointer[_type.UINT16]],  # value
                        _type.HRESULT]
    put_Port: _Callable[[_type.UINT16],  # value
                        _type.HRESULT]
    get_Priority: _Callable[[_Pointer[_type.UINT16]],  # value
                            _type.HRESULT]
    put_Priority: _Callable[[_type.UINT16],  # value
                            _type.HRESULT]
    get_Weight: _Callable[[_Pointer[_type.UINT16]],  # value
                          _type.HRESULT]
    put_Weight: _Callable[[_type.UINT16],  # value
                          _type.HRESULT]
    get_TextAttributes: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, _type.HSTRING]]],  # value
                                  _type.HRESULT]
    RegisterStreamSocketListenerAsync1: _Callable[[_Windows_Networking_Sockets.IStreamSocketListener,  # socket
                                                   _Pointer[_Windows_Foundation.IAsyncOperation[IDnssdRegistrationResult]]],  # result
                                                  _type.HRESULT]
    RegisterStreamSocketListenerAsync2: _Callable[[_Windows_Networking_Sockets.IStreamSocketListener,  # socket
                                                   _Windows_Networking_Connectivity.INetworkAdapter,  # adapter
                                                   _Pointer[_Windows_Foundation.IAsyncOperation[IDnssdRegistrationResult]]],  # result
                                                  _type.HRESULT]
    RegisterDatagramSocketAsync1: _Callable[[_Windows_Networking_Sockets.IDatagramSocket,  # socket
                                             _Pointer[_Windows_Foundation.IAsyncOperation[IDnssdRegistrationResult]]],  # result
                                            _type.HRESULT]
    RegisterDatagramSocketAsync2: _Callable[[_Windows_Networking_Sockets.IDatagramSocket,  # socket
                                             _Windows_Networking_Connectivity.INetworkAdapter,  # adapter
                                             _Pointer[_Windows_Foundation.IAsyncOperation[IDnssdRegistrationResult]]],  # result
                                            _type.HRESULT]


class IDnssdServiceInstanceFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.HSTRING,  # dnssdServiceInstanceName
                       _Windows_Networking.IHostName,  # hostName
                       _type.UINT16,  # port
                       _Pointer[IDnssdServiceInstance]],  # result
                      _type.HRESULT]

    _factory = True


class IDnssdServiceWatcher(_inspectable.IInspectable):
    add_Added: _Callable[[_Windows_Foundation.ITypedEventHandler[IDnssdServiceWatcher, IDnssdServiceInstance],  # handler
                          _Pointer[_struct.EventRegistrationToken]],  # token
                         _type.HRESULT]
    remove_Added: _Callable[[_struct.EventRegistrationToken],  # token
                            _type.HRESULT]
    add_EnumerationCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IDnssdServiceWatcher, _inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_EnumerationCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    add_Stopped: _Callable[[_Windows_Foundation.ITypedEventHandler[IDnssdServiceWatcher, _inspectable.IInspectable],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Stopped: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.Networking.ServiceDiscovery.Dnssd.DnssdServiceWatcherStatus]],  # status
                          _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
