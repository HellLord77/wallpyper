from __future__ import annotations as _

from typing import Callable as _Callable

from .. import StartScreen as _Windows_UI_StartScreen
from ... import Foundation as _Windows_Foundation
from ...ApplicationModel import Core as _Windows_ApplicationModel_Core
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IAdaptiveCard(_inspectable.IInspectable):
    ToJson: _Callable[[_Pointer[_type.HSTRING]],  # result
                      _type.HRESULT]


class IAdaptiveCardBuilderStatics(_inspectable.IInspectable, factory=True):
    CreateAdaptiveCardFromJson: _Callable[[_type.HSTRING,  # value
                                           _Pointer[IAdaptiveCard]],  # result
                                          _type.HRESULT]


class IFocusSession(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    End: _Callable[[],
                   _type.HRESULT]


class IFocusSessionManager(_inspectable.IInspectable):
    get_IsFocusActive: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    GetSession: _Callable[[_type.HSTRING,  # id
                           _Pointer[IFocusSession]],  # result
                          _type.HRESULT]
    TryStartFocusSession: _Callable[[_Pointer[IFocusSession]],  # result
                                    _type.HRESULT]
    TryStartFocusSession2: _Callable[[_struct.Windows.Foundation.DateTime,  # endTime
                                      _Pointer[IFocusSession]],  # result
                                     _type.HRESULT]
    DeactivateFocus: _Callable[[],
                               _type.HRESULT]
    add_IsFocusActiveChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IFocusSessionManager, _inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_IsFocusActiveChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]


class IFocusSessionManagerStatics(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[IFocusSessionManager]],  # result
                          _type.HRESULT]
    get_IsSupported: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]


class ISecurityAppManager(_inspectable.IInspectable):
    Register: _Callable[[_enum.Windows.UI.Shell.SecurityAppKind,  # kind
                         _type.HSTRING,  # displayName
                         _Windows_Foundation.IUriRuntimeClass,  # detailsUri
                         _type.boolean,  # registerPerUser
                         _Pointer[_struct.GUID]],  # result
                        _type.HRESULT]
    Unregister: _Callable[[_enum.Windows.UI.Shell.SecurityAppKind,  # kind
                           _struct.GUID],  # guidRegistration
                          _type.HRESULT]
    UpdateState: _Callable[[_enum.Windows.UI.Shell.SecurityAppKind,  # kind
                            _struct.GUID,  # guidRegistration
                            _enum.Windows.UI.Shell.SecurityAppState,  # state
                            _enum.Windows.UI.Shell.SecurityAppSubstatus,  # substatus
                            _Windows_Foundation.IUriRuntimeClass],  # detailsUri
                           _type.HRESULT]


class IShareWindowCommandEventArgs(_inspectable.IInspectable):
    get_WindowId: _Callable[[_Pointer[_struct.Windows.UI.WindowId]],  # value
                            _type.HRESULT]
    get_Command: _Callable[[_Pointer[_enum.Windows.UI.Shell.ShareWindowCommand]],  # value
                           _type.HRESULT]
    put_Command: _Callable[[_enum.Windows.UI.Shell.ShareWindowCommand],  # value
                           _type.HRESULT]


class IShareWindowCommandSource(_inspectable.IInspectable):
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    ReportCommandChanged: _Callable[[],
                                    _type.HRESULT]
    add_CommandRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IShareWindowCommandSource, IShareWindowCommandEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_CommandRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    add_CommandInvoked: _Callable[[_Windows_Foundation.ITypedEventHandler[IShareWindowCommandSource, IShareWindowCommandEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_CommandInvoked: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]


class IShareWindowCommandSourceStatics(_inspectable.IInspectable, factory=True):
    GetForCurrentView: _Callable[[_Pointer[IShareWindowCommandSource]],  # result
                                 _type.HRESULT]


class ITaskbarManager(_inspectable.IInspectable):
    get_IsSupported: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_IsPinningAllowed: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    IsCurrentAppPinnedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                       _type.HRESULT]
    IsAppListEntryPinnedAsync: _Callable[[_Windows_ApplicationModel_Core.IAppListEntry,  # appListEntry
                                          _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                         _type.HRESULT]
    RequestPinCurrentAppAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                         _type.HRESULT]
    RequestPinAppListEntryAsync: _Callable[[_Windows_ApplicationModel_Core.IAppListEntry,  # appListEntry
                                            _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                           _type.HRESULT]


class ITaskbarManager2(_inspectable.IInspectable):
    IsSecondaryTilePinnedAsync: _Callable[[_type.HSTRING,  # tileId
                                           _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                          _type.HRESULT]
    RequestPinSecondaryTileAsync: _Callable[[_Windows_UI_StartScreen.ISecondaryTile,  # secondaryTile
                                             _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                            _type.HRESULT]
    TryUnpinSecondaryTileAsync: _Callable[[_type.HSTRING,  # tileId
                                           _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                          _type.HRESULT]


class ITaskbarManagerStatics(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[ITaskbarManager]],  # result
                          _type.HRESULT]
