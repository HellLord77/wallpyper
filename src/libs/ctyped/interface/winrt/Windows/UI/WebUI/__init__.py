from __future__ import annotations as _

from typing import Callable as _Callable

from ... import ApplicationModel as _Windows_ApplicationModel
from ... import Foundation as _Windows_Foundation
from ... import System as _Windows_System
from ...ApplicationModel import Activation as _Windows_ApplicationModel_Activation
from .... import inspectable as _inspectable
from .....um import Unknwnbase as _Unknwnbase
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class _IActivatedEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       _Windows_ApplicationModel_Activation.IActivatedEventArgs],  # eventArgs
                      _type.HRESULT]


class IActivatedEventHandler(_IActivatedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IActivatedEventHandler_impl(_IActivatedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IBackgroundActivatedEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       _Windows_ApplicationModel_Activation.IBackgroundActivatedEventArgs],  # eventArgs
                      _type.HRESULT]


class IBackgroundActivatedEventHandler(_IBackgroundActivatedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IBackgroundActivatedEventHandler_impl(_IBackgroundActivatedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IEnteredBackgroundEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       _Windows_ApplicationModel.IEnteredBackgroundEventArgs],  # e
                      _type.HRESULT]


class IEnteredBackgroundEventHandler(_IEnteredBackgroundEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IEnteredBackgroundEventHandler_impl(_IEnteredBackgroundEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ILeavingBackgroundEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       _Windows_ApplicationModel.ILeavingBackgroundEventArgs],  # e
                      _type.HRESULT]


class ILeavingBackgroundEventHandler(_ILeavingBackgroundEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ILeavingBackgroundEventHandler_impl(_ILeavingBackgroundEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _INavigatedEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       IWebUINavigatedEventArgs],  # e
                      _type.HRESULT]


class INavigatedEventHandler(_INavigatedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class INavigatedEventHandler_impl(_INavigatedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IResumingEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable],  # sender
                      _type.HRESULT]


class IResumingEventHandler(_IResumingEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IResumingEventHandler_impl(_IResumingEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ISuspendingEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       _Windows_ApplicationModel.ISuspendingEventArgs],  # e
                      _type.HRESULT]


class ISuspendingEventHandler(_ISuspendingEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ISuspendingEventHandler_impl(_ISuspendingEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class IActivatedDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class IActivatedEventArgsDeferral(_inspectable.IInspectable):
    get_ActivatedOperation: _Callable[[_Pointer[IActivatedOperation]],  # value
                                      _type.HRESULT]


class IActivatedOperation(_inspectable.IInspectable):
    GetDeferral: _Callable[[_Pointer[IActivatedDeferral]],  # deferral
                           _type.HRESULT]


class IHtmlPrintDocumentSource(_inspectable.IInspectable):
    get_Content: _Callable[[_Pointer[_enum.Windows.UI.WebUI.PrintContent]],  # value
                           _type.HRESULT]
    put_Content: _Callable[[_enum.Windows.UI.WebUI.PrintContent],  # value
                           _type.HRESULT]
    get_LeftMargin: _Callable[[_Pointer[_type.FLOAT]],  # value
                              _type.HRESULT]
    put_LeftMargin: _Callable[[_type.FLOAT],  # value
                              _type.HRESULT]
    get_TopMargin: _Callable[[_Pointer[_type.FLOAT]],  # value
                             _type.HRESULT]
    put_TopMargin: _Callable[[_type.FLOAT],  # value
                             _type.HRESULT]
    get_RightMargin: _Callable[[_Pointer[_type.FLOAT]],  # value
                               _type.HRESULT]
    put_RightMargin: _Callable[[_type.FLOAT],  # value
                               _type.HRESULT]
    get_BottomMargin: _Callable[[_Pointer[_type.FLOAT]],  # value
                                _type.HRESULT]
    put_BottomMargin: _Callable[[_type.FLOAT],  # value
                                _type.HRESULT]
    get_EnableHeaderFooter: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_EnableHeaderFooter: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    get_ShrinkToFit: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    put_ShrinkToFit: _Callable[[_type.boolean],  # value
                               _type.HRESULT]
    get_PercentScale: _Callable[[_Pointer[_type.FLOAT]],  # pScalePercent
                                _type.HRESULT]
    put_PercentScale: _Callable[[_type.FLOAT],  # scalePercent
                                _type.HRESULT]
    get_PageRange: _Callable[[_Pointer[_type.HSTRING]],  # pstrPageRange
                             _type.HRESULT]
    TrySetPageRange: _Callable[[_type.HSTRING,  # strPageRange
                                _Pointer[_type.boolean]],  # pfSuccess
                               _type.HRESULT]


class INewWebUIViewCreatedEventArgs(_inspectable.IInspectable):
    get_WebUIView: _Callable[[_Pointer[IWebUIView]],  # value
                             _type.HRESULT]
    get_ActivatedEventArgs: _Callable[[_Pointer[_Windows_ApplicationModel_Activation.IActivatedEventArgs]],  # value
                                      _type.HRESULT]
    get_HasPendingNavigate: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IWebUIActivationStatics(_inspectable.IInspectable, factory=True):
    add_Activated: _Callable[[IActivatedEventHandler,  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_Activated: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    add_Suspending: _Callable[[ISuspendingEventHandler,  # handler
                               _Pointer[_struct.EventRegistrationToken]],  # token
                              _type.HRESULT]
    remove_Suspending: _Callable[[_struct.EventRegistrationToken],  # token
                                 _type.HRESULT]
    add_Resuming: _Callable[[IResumingEventHandler,  # handler
                             _Pointer[_struct.EventRegistrationToken]],  # token
                            _type.HRESULT]
    remove_Resuming: _Callable[[_struct.EventRegistrationToken],  # token
                               _type.HRESULT]
    add_Navigated: _Callable[[INavigatedEventHandler,  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_Navigated: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]


class IWebUIActivationStatics2(_inspectable.IInspectable, factory=True):
    add_LeavingBackground: _Callable[[ILeavingBackgroundEventHandler,  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_LeavingBackground: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    add_EnteredBackground: _Callable[[IEnteredBackgroundEventHandler,  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_EnteredBackground: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    EnablePrelaunch: _Callable[[_type.boolean],  # value
                               _type.HRESULT]


class IWebUIActivationStatics3(_inspectable.IInspectable, factory=True):
    RequestRestartAsync: _Callable[[_type.HSTRING,  # launchArguments
                                    _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.Core.AppRestartFailureReason]]],  # operation
                                   _type.HRESULT]
    RequestRestartForUserAsync: _Callable[[_Windows_System.IUser,  # user
                                           _type.HSTRING,  # launchArguments
                                           _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.Core.AppRestartFailureReason]]],  # operation
                                          _type.HRESULT]


class IWebUIActivationStatics4(_inspectable.IInspectable, factory=True):
    add_NewWebUIViewCreated: _Callable[[_Windows_Foundation.IEventHandler[INewWebUIViewCreatedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_NewWebUIViewCreated: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_BackgroundActivated: _Callable[[IBackgroundActivatedEventHandler,  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_BackgroundActivated: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]


class IWebUIBackgroundTaskInstance(_inspectable.IInspectable):
    get_Succeeded: _Callable[[_Pointer[_type.boolean]],  # succeeded
                             _type.HRESULT]
    put_Succeeded: _Callable[[_type.boolean],  # succeeded
                             _type.HRESULT]


class IWebUIBackgroundTaskInstanceStatics(_inspectable.IInspectable, factory=True):
    get_Current: _Callable[[_Pointer[IWebUIBackgroundTaskInstance]],  # backgroundTaskInstance
                           _type.HRESULT]


class IWebUINavigatedDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class IWebUINavigatedEventArgs(_inspectable.IInspectable):
    get_NavigatedOperation: _Callable[[_Pointer[IWebUINavigatedOperation]],  # value
                                      _type.HRESULT]


class IWebUINavigatedOperation(_inspectable.IInspectable):
    GetDeferral: _Callable[[_Pointer[IWebUINavigatedDeferral]],  # deferral
                           _type.HRESULT]


class IWebUIView(_inspectable.IInspectable):
    get_ApplicationViewId: _Callable[[_Pointer[_type.INT32]],  # value
                                     _type.HRESULT]
    add_Closed: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebUIView, _inspectable.IInspectable],  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Closed: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    add_Activated: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebUIView, _Windows_ApplicationModel_Activation.IActivatedEventArgs],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_Activated: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    get_IgnoreApplicationContentUriRulesNavigationRestrictions: _Callable[[_Pointer[_type.boolean]],  # value
                                                                          _type.HRESULT]
    put_IgnoreApplicationContentUriRulesNavigationRestrictions: _Callable[[_type.boolean],  # value
                                                                          _type.HRESULT]


class IWebUIViewStatics(_inspectable.IInspectable, factory=True):
    CreateAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IWebUIView]]],  # operation
                           _type.HRESULT]
    CreateWithUriAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                   _Pointer[_Windows_Foundation.IAsyncOperation[IWebUIView]]],  # operation
                                  _type.HRESULT]
