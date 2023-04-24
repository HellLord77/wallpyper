from __future__ import annotations

from typing import Callable as _Callable

from ... import Notifications as _Windows_UI_Notifications
from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IUserNotificationListener(_inspectable.IInspectable):
    RequestAccessAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.UI.Notifications.Management.UserNotificationListenerAccessStatus]]],  # operation
                                  _type.HRESULT]
    GetAccessStatus: _Callable[[_Pointer[_enum.Windows.UI.Notifications.Management.UserNotificationListenerAccessStatus]],  # result
                               _type.HRESULT]
    add_NotificationChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IUserNotificationListener, _Windows_UI_Notifications.IUserNotificationChangedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_NotificationChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    GetNotificationsAsync: _Callable[[_enum.Windows.UI.Notifications.NotificationKinds,  # kinds
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_UI_Notifications.IUserNotification]]]],  # operation
                                     _type.HRESULT]
    GetNotification: _Callable[[_type.UINT32,  # notificationId
                                _Pointer[_Windows_UI_Notifications.IUserNotification]],  # result
                               _type.HRESULT]
    ClearNotifications: _Callable[[],
                                  _type.HRESULT]
    RemoveNotification: _Callable[[_type.UINT32],  # notificationId
                                  _type.HRESULT]


class IUserNotificationListenerStatics(_inspectable.IInspectable):
    get_Current: _Callable[[_Pointer[IUserNotificationListener]],  # value
                           _type.HRESULT]

    _factory = True
