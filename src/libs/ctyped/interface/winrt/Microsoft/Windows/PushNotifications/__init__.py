from __future__ import annotations as _

from typing import Callable as _Callable

from .... import inspectable as _inspectable
from ....Windows import Foundation as _Windows_Foundation
from ....Windows.ApplicationModel import Background as _Windows_ApplicationModel_Background
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IPushNotificationChannel(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]
    get_ExpirationTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                  _type.HRESULT]
    Close: _Callable[[],
                     _type.HRESULT]


class IPushNotificationCreateChannelResult(_inspectable.IInspectable):
    get_Channel: _Callable[[_Pointer[IPushNotificationChannel]],  # value
                           _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Microsoft.Windows.PushNotifications.PushNotificationChannelStatus]],  # value
                          _type.HRESULT]


class IPushNotificationManager(_inspectable.IInspectable):
    Register: _Callable[[],
                        _type.HRESULT]
    Unregister: _Callable[[],
                          _type.HRESULT]
    UnregisterAll: _Callable[[],
                             _type.HRESULT]
    CreateChannelAsync: _Callable[[_struct.GUID,  # remoteId
                                   _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IPushNotificationCreateChannelResult, _struct.Microsoft.Windows.PushNotifications.PushNotificationCreateChannelStatus]]],  # operation
                                  _type.HRESULT]
    add_PushReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[IPushNotificationManager, IPushNotificationReceivedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_PushReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]


class IPushNotificationManagerStatics(_inspectable.IInspectable, factory=True):
    IsSupported: _Callable[[_Pointer[_type.boolean]],  # result
                           _type.HRESULT]
    get_Default: _Callable[[_Pointer[IPushNotificationManager]],  # value
                           _type.HRESULT]


class IPushNotificationReceivedEventArgs(_inspectable.IInspectable):
    get_Payload: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                            _Pointer[_Pointer[_type.BYTE]]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_ApplicationModel_Background.IBackgroundTaskDeferral]],  # result
                           _type.HRESULT]
    add_Canceled: _Callable[[_Windows_ApplicationModel_Background.IBackgroundTaskCanceledEventHandler,  # handler
                             _Pointer[_struct.EventRegistrationToken]],  # token
                            _type.HRESULT]
    remove_Canceled: _Callable[[_struct.EventRegistrationToken],  # token
                               _type.HRESULT]
