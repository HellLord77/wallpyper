from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...UI import Notifications as _Windows_UI_Notifications
from .... import inspectable as _inspectable
from ...... import type as _type
from ......_utils import _Pointer


class IDualSimTile(_inspectable.IInspectable):
    put_DisplayName: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_IsPinnedToStart: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    CreateAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                           _type.HRESULT]
    UpdateAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                           _type.HRESULT]
    DeleteAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                           _type.HRESULT]


class IDualSimTileStatics(_inspectable.IInspectable):
    GetTileForSim2: _Callable[[_Pointer[IDualSimTile]],  # result
                              _type.HRESULT]
    UpdateDisplayNameForSim1Async: _Callable[[_type.HSTRING,  # name
                                              _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                             _type.HRESULT]
    CreateTileUpdaterForSim1: _Callable[[_Pointer[_Windows_UI_Notifications.ITileUpdater]],  # updater
                                        _type.HRESULT]
    CreateTileUpdaterForSim2: _Callable[[_Pointer[_Windows_UI_Notifications.ITileUpdater]],  # updater
                                        _type.HRESULT]
    CreateBadgeUpdaterForSim1: _Callable[[_Pointer[_Windows_UI_Notifications.IBadgeUpdater]],  # updater
                                         _type.HRESULT]
    CreateBadgeUpdaterForSim2: _Callable[[_Pointer[_Windows_UI_Notifications.IBadgeUpdater]],  # updater
                                         _type.HRESULT]
    CreateToastNotifierForSim1: _Callable[[_Pointer[_Windows_UI_Notifications.IToastNotifier]],  # notifier
                                          _type.HRESULT]
    CreateToastNotifierForSim2: _Callable[[_Pointer[_Windows_UI_Notifications.IToastNotifier]],  # notifier
                                          _type.HRESULT]

    _factory = True


class IToastNotificationManagerStatics3(_inspectable.IInspectable):
    CreateToastNotifierForSecondaryTile: _Callable[[_type.HSTRING,  # tileId
                                                    _Pointer[_Windows_UI_Notifications.IToastNotifier]],  # notifier
                                                   _type.HRESULT]
