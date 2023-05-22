from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import System as _Windows_System
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from ...UI import Notifications as _Windows_UI_Notifications
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IPushNotificationChannel(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_ExpirationTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                  _type.HRESULT]
    Close: _Callable[[],
                     _type.HRESULT]
    add_PushNotificationReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[IPushNotificationChannel, IPushNotificationReceivedEventArgs],  # handler
                                             _Pointer[_struct.EventRegistrationToken]],  # token
                                            _type.HRESULT]
    remove_PushNotificationReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                               _type.HRESULT]


class IPushNotificationChannelManagerForUser(_inspectable.IInspectable):
    CreatePushNotificationChannelForApplicationAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IPushNotificationChannel]]],  # operation
                                                                _type.HRESULT]
    CreatePushNotificationChannelForApplicationAsyncWithId: _Callable[[_type.HSTRING,  # applicationId
                                                                       _Pointer[_Windows_Foundation.IAsyncOperation[IPushNotificationChannel]]],  # operation
                                                                      _type.HRESULT]
    CreatePushNotificationChannelForSecondaryTileAsync: _Callable[[_type.HSTRING,  # tileId
                                                                   _Pointer[_Windows_Foundation.IAsyncOperation[IPushNotificationChannel]]],  # operation
                                                                  _type.HRESULT]
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]


class IPushNotificationChannelManagerForUser2(_inspectable.IInspectable):
    CreateRawPushNotificationChannelWithAlternateKeyForApplicationAsync: _Callable[[_Windows_Storage_Streams.IBuffer,  # appServerKey
                                                                                    _type.HSTRING,  # channelId
                                                                                    _Pointer[_Windows_Foundation.IAsyncOperation[IPushNotificationChannel]]],  # operation
                                                                                   _type.HRESULT]
    CreateRawPushNotificationChannelWithAlternateKeyForApplicationAsyncWithId: _Callable[[_Windows_Storage_Streams.IBuffer,  # appServerKey
                                                                                          _type.HSTRING,  # channelId
                                                                                          _type.HSTRING,  # appId
                                                                                          _Pointer[_Windows_Foundation.IAsyncOperation[IPushNotificationChannel]]],  # operation
                                                                                         _type.HRESULT]


class IPushNotificationChannelManagerStatics(_inspectable.IInspectable, factory=True):
    CreatePushNotificationChannelForApplicationAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IPushNotificationChannel]]],  # operation
                                                                _type.HRESULT]
    CreatePushNotificationChannelForApplicationAsyncWithId: _Callable[[_type.HSTRING,  # applicationId
                                                                       _Pointer[_Windows_Foundation.IAsyncOperation[IPushNotificationChannel]]],  # operation
                                                                      _type.HRESULT]
    CreatePushNotificationChannelForSecondaryTileAsync: _Callable[[_type.HSTRING,  # tileId
                                                                   _Pointer[_Windows_Foundation.IAsyncOperation[IPushNotificationChannel]]],  # operation
                                                                  _type.HRESULT]


class IPushNotificationChannelManagerStatics2(_inspectable.IInspectable, factory=True):
    GetForUser: _Callable[[_Windows_System.IUser,  # user
                           _Pointer[IPushNotificationChannelManagerForUser]],  # result
                          _type.HRESULT]


class IPushNotificationChannelManagerStatics3(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[IPushNotificationChannelManagerForUser]],  # result
                          _type.HRESULT]


class IPushNotificationChannelManagerStatics4(_inspectable.IInspectable, factory=True):
    add_ChannelsRevoked: _Callable[[_Windows_Foundation.IEventHandler[IPushNotificationChannelsRevokedEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_ChannelsRevoked: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]


class IPushNotificationChannelsRevokedEventArgs(_inspectable.IInspectable):
    pass


class IPushNotificationReceivedEventArgs(_inspectable.IInspectable):
    put_Cancel: _Callable[[_type.boolean],  # value
                          _type.HRESULT]
    get_Cancel: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    get_NotificationType: _Callable[[_Pointer[_enum.Windows.Networking.PushNotifications.PushNotificationType]],  # value
                                    _type.HRESULT]
    get_ToastNotification: _Callable[[_Pointer[_Windows_UI_Notifications.IToastNotification]],  # value
                                     _type.HRESULT]
    get_TileNotification: _Callable[[_Pointer[_Windows_UI_Notifications.ITileNotification]],  # value
                                    _type.HRESULT]
    get_BadgeNotification: _Callable[[_Pointer[_Windows_UI_Notifications.IBadgeNotification]],  # value
                                     _type.HRESULT]
    get_RawNotification: _Callable[[_Pointer[IRawNotification]],  # value
                                   _type.HRESULT]


class IRawNotification(_inspectable.IInspectable):
    get_Content: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]


class IRawNotification2(_inspectable.IInspectable):
    get_Headers: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _type.HSTRING]]],  # value
                           _type.HRESULT]
    get_ChannelId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]


class IRawNotification3(_inspectable.IInspectable):
    get_ContentBytes: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                _type.HRESULT]
