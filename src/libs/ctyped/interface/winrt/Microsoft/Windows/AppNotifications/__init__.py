from __future__ import annotations as _

from typing import Callable as _Callable

from .... import inspectable as _inspectable
from ....Windows import Foundation as _Windows_Foundation
from ....Windows.Foundation import Collections as _Windows_Foundation_Collections
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IAppNotification(_inspectable.IInspectable):
    get_Tag: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    put_Tag: _Callable[[_type.HSTRING],  # value
                       _type.HRESULT]
    get_Group: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Group: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Id: _Callable[[_Pointer[_type.UINT32]],  # value
                      _type.HRESULT]
    get_Payload: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Progress: _Callable[[_Pointer[IAppNotificationProgressData]],  # value
                            _type.HRESULT]
    put_Progress: _Callable[[IAppNotificationProgressData],  # value
                            _type.HRESULT]
    get_Expiration: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                              _type.HRESULT]
    put_Expiration: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                              _type.HRESULT]
    get_ExpiresOnReboot: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    put_ExpiresOnReboot: _Callable[[_type.boolean],  # value
                                   _type.HRESULT]
    get_Priority: _Callable[[_Pointer[_enum.Microsoft.Windows.AppNotifications.AppNotificationPriority]],  # value
                            _type.HRESULT]
    put_Priority: _Callable[[_enum.Microsoft.Windows.AppNotifications.AppNotificationPriority],  # value
                            _type.HRESULT]
    get_SuppressDisplay: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    put_SuppressDisplay: _Callable[[_type.boolean],  # value
                                   _type.HRESULT]


class IAppNotificationActivatedEventArgs(_inspectable.IInspectable):
    get_Argument: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_UserInput: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, _type.HSTRING]]],  # value
                             _type.HRESULT]


class IAppNotificationActivatedEventArgs2(_inspectable.IInspectable):
    get_Arguments: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, _type.HSTRING]]],  # value
                             _type.HRESULT]


class IAppNotificationFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[_type.HSTRING,  # payload
                               _Pointer[IAppNotification]],  # value
                              _type.HRESULT]


class IAppNotificationManager(_inspectable.IInspectable):
    Register: _Callable[[],
                        _type.HRESULT]
    Unregister: _Callable[[],
                          _type.HRESULT]
    UnregisterAll: _Callable[[],
                             _type.HRESULT]
    add_NotificationInvoked: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppNotificationManager, IAppNotificationActivatedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_NotificationInvoked: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    Show: _Callable[[IAppNotification],  # notification
                    _type.HRESULT]
    UpdateAsync: _Callable[[IAppNotificationProgressData,  # data
                            _type.HSTRING,  # tag
                            _type.HSTRING,  # group
                            _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Microsoft.Windows.AppNotifications.AppNotificationProgressResult]]],  # operation
                           _type.HRESULT]
    UpdateAsync2: _Callable[[IAppNotificationProgressData,  # data
                             _type.HSTRING,  # tag
                             _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Microsoft.Windows.AppNotifications.AppNotificationProgressResult]]],  # operation
                            _type.HRESULT]
    get_Setting: _Callable[[_Pointer[_enum.Microsoft.Windows.AppNotifications.AppNotificationSetting]],  # value
                           _type.HRESULT]
    RemoveByIdAsync: _Callable[[_type.UINT32,  # notificationId
                                _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                               _type.HRESULT]
    RemoveByTagAsync: _Callable[[_type.HSTRING,  # tag
                                 _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                _type.HRESULT]
    RemoveByTagAndGroupAsync: _Callable[[_type.HSTRING,  # tag
                                         _type.HSTRING,  # group
                                         _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                        _type.HRESULT]
    RemoveByGroupAsync: _Callable[[_type.HSTRING,  # group
                                   _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                  _type.HRESULT]
    RemoveAllAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                              _type.HRESULT]
    GetAllAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVector[IAppNotification]]]],  # operation
                           _type.HRESULT]


class IAppNotificationManager2(_inspectable.IInspectable):
    Register: _Callable[[_type.HSTRING,  # displayName
                         _Windows_Foundation.IUriRuntimeClass],  # iconUri
                        _type.HRESULT]


class IAppNotificationManagerStatics(_inspectable.IInspectable, factory=True):
    get_Default: _Callable[[_Pointer[IAppNotificationManager]],  # value
                           _type.HRESULT]


class IAppNotificationManagerStatics2(_inspectable.IInspectable, factory=True):
    IsSupported: _Callable[[_Pointer[_type.boolean]],  # result
                           _type.HRESULT]


class IAppNotificationProgressData(_inspectable.IInspectable):
    get_SequenceNumber: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]
    put_SequenceNumber: _Callable[[_type.UINT32],  # value
                                  _type.HRESULT]
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Title: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.DOUBLE]],  # value
                         _type.HRESULT]
    put_Value: _Callable[[_type.DOUBLE],  # value
                         _type.HRESULT]
    get_ValueStringOverride: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    put_ValueStringOverride: _Callable[[_type.HSTRING],  # value
                                       _type.HRESULT]
    get_Status: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    put_Status: _Callable[[_type.HSTRING],  # value
                          _type.HRESULT]


class IAppNotificationProgressDataFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[_type.UINT32,  # sequenceNumber
                               _Pointer[IAppNotificationProgressData]],  # value
                              _type.HRESULT]
