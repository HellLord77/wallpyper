from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import System as _Windows_System
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Security import Credentials as _Windows_Security_Credentials
from ...UI import Shell as _Windows_UI_Shell
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IUserActivity(_inspectable.IInspectable):
    get_State: _Callable[[_Pointer[_enum.Windows.ApplicationModel.UserActivities.UserActivityState]],  # value
                         _type.HRESULT]
    get_ActivityId: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_VisualElements: _Callable[[_Pointer[IUserActivityVisualElements]],  # value
                                  _type.HRESULT]
    get_ContentUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                              _type.HRESULT]
    put_ContentUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                              _type.HRESULT]
    get_ContentType: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_ContentType: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_FallbackUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                               _type.HRESULT]
    put_FallbackUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                               _type.HRESULT]
    get_ActivationUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                 _type.HRESULT]
    put_ActivationUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                                 _type.HRESULT]
    get_ContentInfo: _Callable[[_Pointer[IUserActivityContentInfo]],  # value
                               _type.HRESULT]
    put_ContentInfo: _Callable[[IUserActivityContentInfo],  # value
                               _type.HRESULT]
    SaveAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                         _type.HRESULT]
    CreateSession: _Callable[[_Pointer[IUserActivitySession]],  # result
                             _type.HRESULT]


class IUserActivity2(_inspectable.IInspectable):
    ToJson: _Callable[[_Pointer[_type.HSTRING]],  # result
                      _type.HRESULT]


class IUserActivity3(_inspectable.IInspectable):
    get_IsRoamable: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    put_IsRoamable: _Callable[[_type.boolean],  # value
                              _type.HRESULT]


class IUserActivityAttribution(_inspectable.IInspectable):
    get_IconUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                           _type.HRESULT]
    put_IconUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                           _type.HRESULT]
    get_AlternateText: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    put_AlternateText: _Callable[[_type.HSTRING],  # value
                                 _type.HRESULT]
    get_AddImageQuery: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_AddImageQuery: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]


class IUserActivityAttributionFactory(_inspectable.IInspectable, factory=True):
    CreateWithUri: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # iconUri
                              _Pointer[IUserActivityAttribution]],  # value
                             _type.HRESULT]


class IUserActivityChannel(_inspectable.IInspectable):
    GetOrCreateUserActivityAsync: _Callable[[_type.HSTRING,  # activityId
                                             _Pointer[_Windows_Foundation.IAsyncOperation[IUserActivity]]],  # operation
                                            _type.HRESULT]
    DeleteActivityAsync: _Callable[[_type.HSTRING,  # activityId
                                    _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                   _type.HRESULT]
    DeleteAllActivitiesAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                        _type.HRESULT]


class IUserActivityChannel2(_inspectable.IInspectable):
    GetRecentUserActivitiesAsync: _Callable[[_type.INT32,  # maxUniqueActivities
                                             _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVector[IUserActivitySessionHistoryItem]]]],  # operation
                                            _type.HRESULT]
    GetSessionHistoryItemsForUserActivityAsync: _Callable[[_type.HSTRING,  # activityId
                                                           _struct.Windows.Foundation.DateTime,  # startTime
                                                           _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVector[IUserActivitySessionHistoryItem]]]],  # operation
                                                          _type.HRESULT]


class IUserActivityChannelStatics(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[IUserActivityChannel]],  # result
                          _type.HRESULT]


class IUserActivityChannelStatics2(_inspectable.IInspectable, factory=True):
    DisableAutoSessionCreation: _Callable[[],
                                          _type.HRESULT]
    TryGetForWebAccount: _Callable[[_Windows_Security_Credentials.IWebAccount,  # account
                                    _Pointer[IUserActivityChannel]],  # result
                                   _type.HRESULT]


class IUserActivityChannelStatics3(_inspectable.IInspectable, factory=True):
    GetForUser: _Callable[[_Windows_System.IUser,  # user
                           _Pointer[IUserActivityChannel]],  # result
                          _type.HRESULT]


class IUserActivityContentInfo(_inspectable.IInspectable):
    ToJson: _Callable[[_Pointer[_type.HSTRING]],  # result
                      _type.HRESULT]


class IUserActivityContentInfoStatics(_inspectable.IInspectable, factory=True):
    FromJson: _Callable[[_type.HSTRING,  # value
                         _Pointer[IUserActivityContentInfo]],  # result
                        _type.HRESULT]


class IUserActivityFactory(_inspectable.IInspectable, factory=True):
    CreateWithActivityId: _Callable[[_type.HSTRING,  # activityId
                                     _Pointer[IUserActivity]],  # value
                                    _type.HRESULT]


class IUserActivityRequest(_inspectable.IInspectable):
    SetUserActivity: _Callable[[IUserActivity],  # activity
                               _type.HRESULT]


class IUserActivityRequestManager(_inspectable.IInspectable):
    add_UserActivityRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IUserActivityRequestManager, IUserActivityRequestedEventArgs],  # handler
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_UserActivityRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]


class IUserActivityRequestManagerStatics(_inspectable.IInspectable, factory=True):
    GetForCurrentView: _Callable[[_Pointer[IUserActivityRequestManager]],  # result
                                 _type.HRESULT]


class IUserActivityRequestedEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IUserActivityRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IUserActivitySession(_inspectable.IInspectable):
    get_ActivityId: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]


class IUserActivitySessionHistoryItem(_inspectable.IInspectable):
    get_UserActivity: _Callable[[_Pointer[IUserActivity]],  # value
                                _type.HRESULT]
    get_StartTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_EndTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                           _type.HRESULT]


class IUserActivityStatics(_inspectable.IInspectable, factory=True):
    TryParseFromJson: _Callable[[_type.HSTRING,  # json
                                 _Pointer[IUserActivity]],  # result
                                _type.HRESULT]
    TryParseFromJsonArray: _Callable[[_type.HSTRING,  # json
                                      _Pointer[_Windows_Foundation_Collections.IVector[IUserActivity]]],  # result
                                     _type.HRESULT]
    ToJsonArray: _Callable[[_Windows_Foundation_Collections.IIterable[IUserActivity],  # activities
                            _Pointer[_type.HSTRING]],  # result
                           _type.HRESULT]


class IUserActivityVisualElements(_inspectable.IInspectable):
    get_DisplayText: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_DisplayText: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_BackgroundColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                   _type.HRESULT]
    put_BackgroundColor: _Callable[[_struct.Windows.UI.Color],  # value
                                   _type.HRESULT]
    get_Attribution: _Callable[[_Pointer[IUserActivityAttribution]],  # value
                               _type.HRESULT]
    put_Attribution: _Callable[[IUserActivityAttribution],  # value
                               _type.HRESULT]
    put_Content: _Callable[[_Windows_UI_Shell.IAdaptiveCard],  # value
                           _type.HRESULT]
    get_Content: _Callable[[_Pointer[_Windows_UI_Shell.IAdaptiveCard]],  # value
                           _type.HRESULT]


class IUserActivityVisualElements2(_inspectable.IInspectable):
    get_AttributionDisplayText: _Callable[[_Pointer[_type.HSTRING]],  # value
                                          _type.HRESULT]
    put_AttributionDisplayText: _Callable[[_type.HSTRING],  # value
                                          _type.HRESULT]
