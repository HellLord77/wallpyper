from __future__ import annotations as _

from typing import Callable as _Callable

from .... import inspectable as _inspectable
from ....Windows import Foundation as _Windows_Foundation
from ....Windows.Foundation import Collections as _Windows_Foundation_Collections
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IActivationRegistrationManagerStatics(_inspectable.IInspectable, factory=True):
    RegisterForFileTypeActivation: _Callable[[_type.UINT32,  # __supportedFileTypesSize
                                              _Pointer[_type.HSTRING],  # supportedFileTypes
                                              _type.HSTRING,  # logo
                                              _type.HSTRING,  # displayName
                                              _type.UINT32,  # __supportedVerbsSize
                                              _Pointer[_type.HSTRING],  # supportedVerbs
                                              _type.HSTRING],  # exePath
                                             _type.HRESULT]
    RegisterForProtocolActivation: _Callable[[_type.HSTRING,  # scheme
                                              _type.HSTRING,  # logo
                                              _type.HSTRING,  # displayName
                                              _type.HSTRING],  # exePath
                                             _type.HRESULT]
    RegisterForStartupActivation: _Callable[[_type.HSTRING,  # taskId
                                             _type.HSTRING],  # exePath
                                            _type.HRESULT]
    UnregisterForFileTypeActivation: _Callable[[_type.UINT32,  # __fileTypesSize
                                                _Pointer[_type.HSTRING],  # fileTypes
                                                _type.HSTRING],  # exePath
                                               _type.HRESULT]
    UnregisterForProtocolActivation: _Callable[[_type.HSTRING,  # scheme
                                                _type.HSTRING],  # exePath
                                               _type.HRESULT]
    UnregisterForStartupActivation: _Callable[[_type.HSTRING],  # taskId
                                              _type.HRESULT]


class IAppActivationArguments(_inspectable.IInspectable):
    get_Kind: _Callable[[_Pointer[_enum.Microsoft.Windows.AppLifecycle.ExtendedActivationKind]],  # value
                        _type.HRESULT]
    get_Data: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                        _type.HRESULT]


class IAppInstance(_inspectable.IInspectable):
    UnregisterKey: _Callable[[],
                             _type.HRESULT]
    RedirectActivationToAsync: _Callable[[IAppActivationArguments,  # args
                                          _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                         _type.HRESULT]
    GetActivatedEventArgs: _Callable[[_Pointer[IAppActivationArguments]],  # result
                                     _type.HRESULT]
    add_Activated: _Callable[[_Windows_Foundation.IEventHandler[IAppActivationArguments],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_Activated: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    get_Key: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_IsCurrent: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_ProcessId: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]


class IAppInstanceStatics(_inspectable.IInspectable, factory=True):
    GetCurrent: _Callable[[_Pointer[IAppInstance]],  # result
                          _type.HRESULT]
    GetInstances: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IAppInstance]]],  # result
                            _type.HRESULT]
    FindOrRegisterForKey: _Callable[[_type.HSTRING,  # key
                                     _Pointer[IAppInstance]],  # result
                                    _type.HRESULT]


class IAppInstanceStatics2(_inspectable.IInspectable, factory=True):
    Restart: _Callable[[_type.HSTRING,  # arguments
                        _Pointer[_enum.Windows.ApplicationModel.Core.AppRestartFailureReason]],  # result
                       _type.HRESULT]
