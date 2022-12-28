from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class ILockApplicationHost(_inspectable.IInspectable):
    RequestUnlock: _Callable[[],
                             _type.HRESULT]
    add_Unlocking: _Callable[[_Windows_Foundation.ITypedEventHandler[ILockApplicationHost, ILockScreenUnlockingEventArgs],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_Unlocking: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]


class ILockApplicationHostStatics(_inspectable.IInspectable):
    GetForCurrentView: _Callable[[_Pointer[ILockApplicationHost]],  # result
                                 _type.HRESULT]

    _factory = True


class ILockScreenBadge(_inspectable.IInspectable):
    get_Logo: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStream]],  # value
                        _type.HRESULT]
    get_Glyph: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStream]],  # value
                         _type.HRESULT]
    get_Number: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                          _type.HRESULT]
    get_AutomationName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    LaunchApp: _Callable[[],
                         _type.HRESULT]


class ILockScreenInfo(_inspectable.IInspectable):
    add_LockScreenImageChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ILockScreenInfo, _inspectable.IInspectable],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_LockScreenImageChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]
    get_LockScreenImage: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStream]],  # value
                                   _type.HRESULT]
    add_BadgesChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ILockScreenInfo, _inspectable.IInspectable],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_BadgesChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    get_Badges: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[ILockScreenBadge]]],  # value
                          _type.HRESULT]
    add_DetailTextChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ILockScreenInfo, _inspectable.IInspectable],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_DetailTextChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    get_DetailText: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                              _type.HRESULT]
    add_AlarmIconChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ILockScreenInfo, _inspectable.IInspectable],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_AlarmIconChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    get_AlarmIcon: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStream]],  # value
                             _type.HRESULT]


class ILockScreenUnlockingDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class ILockScreenUnlockingEventArgs(_inspectable.IInspectable):
    GetDeferral: _Callable[[_Pointer[ILockScreenUnlockingDeferral]],  # deferral
                           _type.HRESULT]
    get_Deadline: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                            _type.HRESULT]
