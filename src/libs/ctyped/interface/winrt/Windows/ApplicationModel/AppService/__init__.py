from __future__ import annotations as _

from typing import Callable as _Callable

from ... import ApplicationModel as _Windows_ApplicationModel
from ... import Foundation as _Windows_Foundation
from ... import System as _Windows_System
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...System import RemoteSystems as _Windows_System_RemoteSystems
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IAppServiceCatalogStatics(_inspectable.IInspectable, factory=True):
    FindAppServiceProvidersAsync: _Callable[[_type.HSTRING,  # appServiceName
                                             _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_ApplicationModel.IAppInfo]]]],  # operation
                                            _type.HRESULT]


class IAppServiceClosedEventArgs(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.ApplicationModel.AppService.AppServiceClosedStatus]],  # value
                          _type.HRESULT]


class IAppServiceConnection(_inspectable.IInspectable):
    get_AppServiceName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    put_AppServiceName: _Callable[[_type.HSTRING],  # value
                                  _type.HRESULT]
    get_PackageFamilyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    put_PackageFamilyName: _Callable[[_type.HSTRING],  # value
                                     _type.HRESULT]
    OpenAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.AppService.AppServiceConnectionStatus]]],  # operation
                         _type.HRESULT]
    SendMessageAsync: _Callable[[_Windows_Foundation_Collections.IPropertySet,  # message
                                 _Pointer[_Windows_Foundation.IAsyncOperation[IAppServiceResponse]]],  # operation
                                _type.HRESULT]
    add_RequestReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppServiceConnection, IAppServiceRequestReceivedEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_RequestReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    add_ServiceClosed: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppServiceConnection, IAppServiceClosedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_ServiceClosed: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]


class IAppServiceConnection2(_inspectable.IInspectable):
    OpenRemoteAsync: _Callable[[_Windows_System_RemoteSystems.IRemoteSystemConnectionRequest,  # remoteSystemConnectionRequest
                                _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.AppService.AppServiceConnectionStatus]]],  # operation
                               _type.HRESULT]
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]
    put_User: _Callable[[_Windows_System.IUser],  # value
                        _type.HRESULT]


class IAppServiceConnectionStatics(_inspectable.IInspectable, factory=True):
    SendStatelessMessageAsync: _Callable[[IAppServiceConnection,  # connection
                                          _Windows_System_RemoteSystems.IRemoteSystemConnectionRequest,  # connectionRequest
                                          _Windows_Foundation_Collections.IPropertySet,  # message
                                          _Pointer[_Windows_Foundation.IAsyncOperation[IStatelessAppServiceResponse]]],  # operation
                                         _type.HRESULT]


class IAppServiceDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class IAppServiceRequest(_inspectable.IInspectable):
    get_Message: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                           _type.HRESULT]
    SendResponseAsync: _Callable[[_Windows_Foundation_Collections.IPropertySet,  # message
                                  _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.AppService.AppServiceResponseStatus]]],  # operation
                                 _type.HRESULT]


class IAppServiceRequestReceivedEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IAppServiceRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[IAppServiceDeferral]],  # result
                           _type.HRESULT]


class IAppServiceResponse(_inspectable.IInspectable):
    get_Message: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                           _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.ApplicationModel.AppService.AppServiceResponseStatus]],  # value
                          _type.HRESULT]


class IAppServiceTriggerDetails(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_CallerPackageFamilyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                           _type.HRESULT]
    get_AppServiceConnection: _Callable[[_Pointer[IAppServiceConnection]],  # value
                                        _type.HRESULT]


class IAppServiceTriggerDetails2(_inspectable.IInspectable):
    get_IsRemoteSystemConnection: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]


class IAppServiceTriggerDetails3(_inspectable.IInspectable):
    CheckCallerForCapabilityAsync: _Callable[[_type.HSTRING,  # capabilityName
                                              _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                             _type.HRESULT]


class IAppServiceTriggerDetails4(_inspectable.IInspectable):
    get_CallerRemoteConnectionToken: _Callable[[_Pointer[_type.HSTRING]],  # value
                                               _type.HRESULT]


class IStatelessAppServiceResponse(_inspectable.IInspectable):
    get_Message: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                           _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.ApplicationModel.AppService.StatelessAppServiceResponseStatus]],  # value
                          _type.HRESULT]
