from __future__ import annotations

from typing import Callable as _Callable

from .. import Activation as _Windows_ApplicationModel_Activation
from ... import ApplicationModel as _Windows_ApplicationModel
from ... import Foundation as _Windows_Foundation
from ... import System as _Windows_System
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...UI import Core as _Windows_UI_Core
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IAppListEntry(_inspectable.IInspectable):
    get_DisplayInfo: _Callable[[_Pointer[_Windows_ApplicationModel.IAppDisplayInfo]],  # value
                               _type.HRESULT]
    LaunchAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                           _type.HRESULT]


class IAppListEntry2(_inspectable.IInspectable):
    get_AppUserModelId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]


class IAppListEntry3(_inspectable.IInspectable):
    LaunchForUserAsync: _Callable[[_Windows_System.IUser,  # user
                                   _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                  _type.HRESULT]


class IAppListEntry4(_inspectable.IInspectable):
    get_AppInfo: _Callable[[_Pointer[_Windows_ApplicationModel.IAppInfo]],  # value
                           _type.HRESULT]


class ICoreApplication(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    add_Suspending: _Callable[[_Windows_Foundation.IEventHandler[_Windows_ApplicationModel.ISuspendingEventArgs],  # handler
                               _Pointer[_struct.EventRegistrationToken]],  # token
                              _type.HRESULT]
    remove_Suspending: _Callable[[_struct.EventRegistrationToken],  # token
                                 _type.HRESULT]
    add_Resuming: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                             _Pointer[_struct.EventRegistrationToken]],  # token
                            _type.HRESULT]
    remove_Resuming: _Callable[[_struct.EventRegistrationToken],  # token
                               _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                              _type.HRESULT]
    GetCurrentView: _Callable[[_Pointer[ICoreApplicationView]],  # value
                              _type.HRESULT]
    Run: _Callable[[IFrameworkViewSource],  # viewSource
                   _type.HRESULT]
    RunWithActivationFactories: _Callable[[_Windows_Foundation.IGetActivationFactory],  # activationFactoryCallback
                                          _type.HRESULT]

    _factory = True


class ICoreApplication2(_inspectable.IInspectable):
    add_BackgroundActivated: _Callable[[_Windows_Foundation.IEventHandler[_Windows_ApplicationModel_Activation.IBackgroundActivatedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_BackgroundActivated: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_LeavingBackground: _Callable[[_Windows_Foundation.IEventHandler[_Windows_ApplicationModel.ILeavingBackgroundEventArgs],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_LeavingBackground: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    add_EnteredBackground: _Callable[[_Windows_Foundation.IEventHandler[_Windows_ApplicationModel.IEnteredBackgroundEventArgs],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_EnteredBackground: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    EnablePrelaunch: _Callable[[_type.boolean],  # value
                               _type.HRESULT]

    _factory = True


class ICoreApplication3(_inspectable.IInspectable):
    RequestRestartAsync: _Callable[[_type.HSTRING,  # launchArguments
                                    _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.Core.AppRestartFailureReason]]],  # operation
                                   _type.HRESULT]
    RequestRestartForUserAsync: _Callable[[_Windows_System.IUser,  # user
                                           _type.HSTRING,  # launchArguments
                                           _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.Core.AppRestartFailureReason]]],  # operation
                                          _type.HRESULT]

    _factory = True


class ICoreApplicationExit(_inspectable.IInspectable):
    Exit: _Callable[[],
                    _type.HRESULT]
    add_Exiting: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Exiting: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]

    _factory = True


class ICoreApplicationUnhandledError(_inspectable.IInspectable):
    add_UnhandledErrorDetected: _Callable[[_Windows_Foundation.IEventHandler[IUnhandledErrorDetectedEventArgs],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_UnhandledErrorDetected: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]

    _factory = True


class ICoreApplicationUseCount(_inspectable.IInspectable):
    IncrementApplicationUseCount: _Callable[[],
                                            _type.HRESULT]
    DecrementApplicationUseCount: _Callable[[],
                                            _type.HRESULT]

    _factory = True


class ICoreApplicationView(_inspectable.IInspectable):
    get_CoreWindow: _Callable[[_Pointer[_Windows_UI_Core.ICoreWindow]],  # value
                              _type.HRESULT]
    add_Activated: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreApplicationView, _Windows_ApplicationModel_Activation.IActivatedEventArgs],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_Activated: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    get_IsMain: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    get_IsHosted: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]


class ICoreApplicationView2(_inspectable.IInspectable):
    get_Dispatcher: _Callable[[_Pointer[_Windows_UI_Core.ICoreDispatcher]],  # value
                              _type.HRESULT]


class ICoreApplicationView3(_inspectable.IInspectable):
    get_IsComponent: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_TitleBar: _Callable[[_Pointer[ICoreApplicationViewTitleBar]],  # value
                            _type.HRESULT]
    add_HostedViewClosing: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreApplicationView, IHostedViewClosingEventArgs],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_HostedViewClosing: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]


class ICoreApplicationView5(_inspectable.IInspectable):
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                              _type.HRESULT]


class ICoreApplicationView6(_inspectable.IInspectable):
    get_DispatcherQueue: _Callable[[_Pointer[_Windows_System.IDispatcherQueue]],  # value
                                   _type.HRESULT]


class ICoreApplicationViewTitleBar(_inspectable.IInspectable):
    put_ExtendViewIntoTitleBar: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    get_ExtendViewIntoTitleBar: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    get_SystemOverlayLeftInset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                          _type.HRESULT]
    get_SystemOverlayRightInset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                           _type.HRESULT]
    get_Height: _Callable[[_Pointer[_type.DOUBLE]],  # value
                          _type.HRESULT]
    add_LayoutMetricsChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreApplicationViewTitleBar, _inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_LayoutMetricsChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    get_IsVisible: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    add_IsVisibleChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreApplicationViewTitleBar, _inspectable.IInspectable],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_IsVisibleChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]


class ICoreImmersiveApplication(_inspectable.IInspectable):
    get_Views: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[ICoreApplicationView]]],  # value
                         _type.HRESULT]
    CreateNewView: _Callable[[_type.HSTRING,  # runtimeType
                              _type.HSTRING,  # entryPoint
                              _Pointer[ICoreApplicationView]],  # view
                             _type.HRESULT]
    get_MainView: _Callable[[_Pointer[ICoreApplicationView]],  # value
                            _type.HRESULT]

    _factory = True


class ICoreImmersiveApplication2(_inspectable.IInspectable):
    CreateNewViewFromMainView: _Callable[[_Pointer[ICoreApplicationView]],  # view
                                         _type.HRESULT]

    _factory = True


class ICoreImmersiveApplication3(_inspectable.IInspectable):
    CreateNewViewWithViewSource: _Callable[[IFrameworkViewSource,  # viewSource
                                            _Pointer[ICoreApplicationView]],  # view
                                           _type.HRESULT]

    _factory = True


class IFrameworkView(_inspectable.IInspectable):
    Initialize: _Callable[[ICoreApplicationView],  # applicationView
                          _type.HRESULT]
    SetWindow: _Callable[[_Windows_UI_Core.ICoreWindow],  # window
                         _type.HRESULT]
    Load: _Callable[[_type.HSTRING],  # entryPoint
                    _type.HRESULT]
    Run: _Callable[[],
                   _type.HRESULT]
    Uninitialize: _Callable[[],
                            _type.HRESULT]


class IFrameworkViewSource(_inspectable.IInspectable):
    CreateView: _Callable[[_Pointer[IFrameworkView]],  # viewProvider
                          _type.HRESULT]


class IHostedViewClosingEventArgs(_inspectable.IInspectable):
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IUnhandledError(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    Propagate: _Callable[[],
                         _type.HRESULT]


class IUnhandledErrorDetectedEventArgs(_inspectable.IInspectable):
    get_UnhandledError: _Callable[[_Pointer[IUnhandledError]],  # value
                                  _type.HRESULT]
