from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import System as _Windows_System
from .... import inspectable as _inspectable
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IAppBroadcastingMonitor(_inspectable.IInspectable):
    get_IsCurrentAppBroadcasting: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    add_IsCurrentAppBroadcastingChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppBroadcastingMonitor, _inspectable.IInspectable],  # handler
                                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                                   _type.HRESULT]
    remove_IsCurrentAppBroadcastingChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                      _type.HRESULT]


class IAppBroadcastingStatus(_inspectable.IInspectable):
    get_CanStartBroadcast: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    get_Details: _Callable[[_Pointer[IAppBroadcastingStatusDetails]],  # value
                           _type.HRESULT]


class IAppBroadcastingStatusDetails(_inspectable.IInspectable):
    get_IsAnyAppBroadcasting: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_IsCaptureResourceUnavailable: _Callable[[_Pointer[_type.boolean]],  # value
                                                _type.HRESULT]
    get_IsGameStreamInProgress: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    get_IsGpuConstrained: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_IsAppInactive: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_IsBlockedForApp: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_IsDisabledByUser: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_IsDisabledBySystem: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]


class IAppBroadcastingUI(_inspectable.IInspectable):
    GetStatus: _Callable[[_Pointer[IAppBroadcastingStatus]],  # result
                         _type.HRESULT]
    ShowBroadcastUI: _Callable[[],
                               _type.HRESULT]


class IAppBroadcastingUIStatics(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[IAppBroadcastingUI]],  # result
                          _type.HRESULT]
    GetForUser: _Callable[[_Windows_System.IUser,  # user
                           _Pointer[IAppBroadcastingUI]],  # result
                          _type.HRESULT]
