from __future__ import annotations

from typing import Callable as _Callable

from .. import Core as _Windows_UI_Core
from .. import WindowManagement as _Windows_UI_WindowManagement
from ... import Foundation as _Windows_Foundation
from ... import UI as _Windows_UI
from ...Devices import Enumeration as _Windows_Devices_Enumeration
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IAccessibilitySettings(_inspectable.IInspectable):
    get_HighContrast: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_HighContrastScheme: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    add_HighContrastChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAccessibilitySettings, _inspectable.IInspectable],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # cookie
                                       _type.HRESULT]
    remove_HighContrastChanged: _Callable[[_struct.EventRegistrationToken],  # cookie
                                          _type.HRESULT]


class IActivationViewSwitcher(_inspectable.IInspectable):
    ShowAsStandaloneAsync: _Callable[[_type.INT32,  # viewId
                                      _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                     _type.HRESULT]
    ShowAsStandaloneWithSizePreferenceAsync: _Callable[[_type.INT32,  # viewId
                                                        _enum.Windows.UI.ViewManagement.ViewSizePreference,  # sizePreference
                                                        _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                                       _type.HRESULT]
    IsViewPresentedOnActivationVirtualDesktop: _Callable[[_type.INT32,  # viewId
                                                          _Pointer[_type.boolean]],  # value
                                                         _type.HRESULT]


class IApplicationView(_inspectable.IInspectable):
    get_Orientation: _Callable[[_Pointer[_enum.Windows.UI.ViewManagement.ApplicationViewOrientation]],  # value
                               _type.HRESULT]
    get_AdjacentToLeftDisplayEdge: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    get_AdjacentToRightDisplayEdge: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]
    IsFullScreen: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_IsOnLockScreen: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    get_IsScreenCaptureEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_IsScreenCaptureEnabled: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    put_Title: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Id: _Callable[[_Pointer[_type.INT32]],  # value
                      _type.HRESULT]
    add_Consolidated: _Callable[[_Windows_Foundation.ITypedEventHandler[IApplicationView, IApplicationViewConsolidatedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_Consolidated: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]


class IApplicationView2(_inspectable.IInspectable):
    SuppressSystemOverlays: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    get_VisibleBounds: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                                 _type.HRESULT]
    add_VisibleBoundsChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IApplicationView, _inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_VisibleBoundsChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    SetDesiredBoundsMode: _Callable[[_enum.Windows.UI.ViewManagement.ApplicationViewBoundsMode,  # boundsMode
                                     _Pointer[_type.boolean]],  # success
                                    _type.HRESULT]
    get_DesiredBoundsMode: _Callable[[_Pointer[_enum.Windows.UI.ViewManagement.ApplicationViewBoundsMode]],  # value
                                     _type.HRESULT]


class IApplicationView3(_inspectable.IInspectable):
    get_TitleBar: _Callable[[_Pointer[IApplicationViewTitleBar]],  # value
                            _type.HRESULT]
    get_FullScreenSystemOverlayMode: _Callable[[_Pointer[_enum.Windows.UI.ViewManagement.FullScreenSystemOverlayMode]],  # value
                                               _type.HRESULT]
    put_FullScreenSystemOverlayMode: _Callable[[_enum.Windows.UI.ViewManagement.FullScreenSystemOverlayMode],  # value
                                               _type.HRESULT]
    get_IsFullScreenMode: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    TryEnterFullScreenMode: _Callable[[_Pointer[_type.boolean]],  # success
                                      _type.HRESULT]
    ExitFullScreenMode: _Callable[[],
                                  _type.HRESULT]
    ShowStandardSystemOverlays: _Callable[[],
                                          _type.HRESULT]
    TryResizeView: _Callable[[_struct.Windows.Foundation.Size,  # value
                              _Pointer[_type.boolean]],  # success
                             _type.HRESULT]
    SetPreferredMinSize: _Callable[[_struct.Windows.Foundation.Size],  # minSize
                                   _type.HRESULT]


class IApplicationView4(_inspectable.IInspectable):
    get_ViewMode: _Callable[[_Pointer[_enum.Windows.UI.ViewManagement.ApplicationViewMode]],  # value
                            _type.HRESULT]
    IsViewModeSupported: _Callable[[_enum.Windows.UI.ViewManagement.ApplicationViewMode,  # viewMode
                                    _Pointer[_type.boolean]],  # isViewModeSupported
                                   _type.HRESULT]
    TryEnterViewModeAsync: _Callable[[_enum.Windows.UI.ViewManagement.ApplicationViewMode,  # viewMode
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                     _type.HRESULT]
    TryEnterViewModeWithPreferencesAsync: _Callable[[_enum.Windows.UI.ViewManagement.ApplicationViewMode,  # viewMode
                                                     IViewModePreferences,  # viewModePreferences
                                                     _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                                    _type.HRESULT]
    TryConsolidateAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                   _type.HRESULT]


class IApplicationView7(_inspectable.IInspectable):
    get_PersistedStateId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    put_PersistedStateId: _Callable[[_type.HSTRING],  # value
                                    _type.HRESULT]


class IApplicationView9(_inspectable.IInspectable):
    get_WindowingEnvironment: _Callable[[_Pointer[_Windows_UI_WindowManagement.IWindowingEnvironment]],  # value
                                        _type.HRESULT]
    GetDisplayRegions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_UI_WindowManagement.IDisplayRegion]]],  # result
                                 _type.HRESULT]


class IApplicationViewConsolidatedEventArgs(_inspectable.IInspectable):
    get_IsUserInitiated: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]


class IApplicationViewConsolidatedEventArgs2(_inspectable.IInspectable):
    get_IsAppInitiated: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]


class IApplicationViewFullscreenStatics(_inspectable.IInspectable):
    TryUnsnapToFullscreen: _Callable[[_Pointer[_type.boolean]],  # success
                                     _type.HRESULT]

    _factory = True


class IApplicationViewInteropStatics(_inspectable.IInspectable):
    GetApplicationViewIdForWindow: _Callable[[_Windows_UI_Core.ICoreWindow,  # window
                                              _Pointer[_type.INT32]],  # id
                                             _type.HRESULT]

    _factory = True


class IApplicationViewScaling(_inspectable.IInspectable):
    pass


class IApplicationViewScalingStatics(_inspectable.IInspectable):
    get_DisableLayoutScaling: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    TrySetDisableLayoutScaling: _Callable[[_type.boolean,  # disableLayoutScaling
                                           _Pointer[_type.boolean]],  # success
                                          _type.HRESULT]

    _factory = True


class IApplicationViewStatics(_inspectable.IInspectable):
    Value: _Callable[[_Pointer[_enum.Windows.UI.ViewManagement.ApplicationViewState]],  # value
                     _type.HRESULT]
    TryUnsnap: _Callable[[_Pointer[_type.boolean]],  # success
                         _type.HRESULT]

    _factory = True


class IApplicationViewStatics2(_inspectable.IInspectable):
    GetForCurrentView: _Callable[[_Pointer[IApplicationView]],  # current
                                 _type.HRESULT]
    get_TerminateAppOnFinalViewClose: _Callable[[_Pointer[_type.boolean]],  # value
                                                _type.HRESULT]
    put_TerminateAppOnFinalViewClose: _Callable[[_type.boolean],  # value
                                                _type.HRESULT]

    _factory = True


class IApplicationViewStatics3(_inspectable.IInspectable):
    get_PreferredLaunchWindowingMode: _Callable[[_Pointer[_enum.Windows.UI.ViewManagement.ApplicationViewWindowingMode]],  # value
                                                _type.HRESULT]
    put_PreferredLaunchWindowingMode: _Callable[[_enum.Windows.UI.ViewManagement.ApplicationViewWindowingMode],  # value
                                                _type.HRESULT]
    get_PreferredLaunchViewSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                                           _type.HRESULT]
    put_PreferredLaunchViewSize: _Callable[[_struct.Windows.Foundation.Size],  # value
                                           _type.HRESULT]

    _factory = True


class IApplicationViewStatics4(_inspectable.IInspectable):
    ClearAllPersistedState: _Callable[[],
                                      _type.HRESULT]
    ClearPersistedState: _Callable[[_type.HSTRING],  # key
                                   _type.HRESULT]

    _factory = True


class IApplicationViewSwitcherStatics(_inspectable.IInspectable):
    DisableShowingMainViewOnActivation: _Callable[[],
                                                  _type.HRESULT]
    TryShowAsStandaloneAsync: _Callable[[_type.INT32,  # viewId
                                         _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                        _type.HRESULT]
    TryShowAsStandaloneWithSizePreferenceAsync: _Callable[[_type.INT32,  # viewId
                                                           _enum.Windows.UI.ViewManagement.ViewSizePreference,  # sizePreference
                                                           _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                                          _type.HRESULT]
    TryShowAsStandaloneWithAnchorViewAndSizePreferenceAsync: _Callable[[_type.INT32,  # viewId
                                                                        _enum.Windows.UI.ViewManagement.ViewSizePreference,  # sizePreference
                                                                        _type.INT32,  # anchorViewId
                                                                        _enum.Windows.UI.ViewManagement.ViewSizePreference,  # anchorSizePreference
                                                                        _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                                                       _type.HRESULT]
    SwitchAsync: _Callable[[_type.INT32,  # viewId
                            _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                           _type.HRESULT]
    SwitchFromViewAsync: _Callable[[_type.INT32,  # toViewId
                                    _type.INT32,  # fromViewId
                                    _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                   _type.HRESULT]
    SwitchFromViewWithOptionsAsync: _Callable[[_type.INT32,  # toViewId
                                               _type.INT32,  # fromViewId
                                               _enum.Windows.UI.ViewManagement.ApplicationViewSwitchingOptions,  # options
                                               _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                              _type.HRESULT]
    PrepareForCustomAnimatedSwitchAsync: _Callable[[_type.INT32,  # toViewId
                                                    _type.INT32,  # fromViewId
                                                    _enum.Windows.UI.ViewManagement.ApplicationViewSwitchingOptions,  # options
                                                    _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                                   _type.HRESULT]

    _factory = True


class IApplicationViewSwitcherStatics2(_inspectable.IInspectable):
    DisableSystemViewActivationPolicy: _Callable[[],
                                                 _type.HRESULT]

    _factory = True


class IApplicationViewSwitcherStatics3(_inspectable.IInspectable):
    TryShowAsViewModeAsync: _Callable[[_type.INT32,  # viewId
                                       _enum.Windows.UI.ViewManagement.ApplicationViewMode,  # viewMode
                                       _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                      _type.HRESULT]
    TryShowAsViewModeWithPreferencesAsync: _Callable[[_type.INT32,  # viewId
                                                      _enum.Windows.UI.ViewManagement.ApplicationViewMode,  # viewMode
                                                      IViewModePreferences,  # viewModePreferences
                                                      _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                                     _type.HRESULT]

    _factory = True


class IApplicationViewTitleBar(_inspectable.IInspectable):
    put_ForegroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                   _type.HRESULT]
    get_ForegroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                   _type.HRESULT]
    put_BackgroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                   _type.HRESULT]
    get_BackgroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                   _type.HRESULT]
    put_ButtonForegroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                         _type.HRESULT]
    get_ButtonForegroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                         _type.HRESULT]
    put_ButtonBackgroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                         _type.HRESULT]
    get_ButtonBackgroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                         _type.HRESULT]
    put_ButtonHoverForegroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                              _type.HRESULT]
    get_ButtonHoverForegroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                              _type.HRESULT]
    put_ButtonHoverBackgroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                              _type.HRESULT]
    get_ButtonHoverBackgroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                              _type.HRESULT]
    put_ButtonPressedForegroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                                _type.HRESULT]
    get_ButtonPressedForegroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                                _type.HRESULT]
    put_ButtonPressedBackgroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                                _type.HRESULT]
    get_ButtonPressedBackgroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                                _type.HRESULT]
    put_InactiveForegroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                           _type.HRESULT]
    get_InactiveForegroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                           _type.HRESULT]
    put_InactiveBackgroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                           _type.HRESULT]
    get_InactiveBackgroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                           _type.HRESULT]
    put_ButtonInactiveForegroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                                 _type.HRESULT]
    get_ButtonInactiveForegroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                                 _type.HRESULT]
    put_ButtonInactiveBackgroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                                 _type.HRESULT]
    get_ButtonInactiveBackgroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                                 _type.HRESULT]


class IApplicationViewTransferContext(_inspectable.IInspectable):
    get_ViewId: _Callable[[_Pointer[_type.INT32]],  # value
                          _type.HRESULT]
    put_ViewId: _Callable[[_type.INT32],  # value
                          _type.HRESULT]


class IApplicationViewTransferContextStatics(_inspectable.IInspectable):
    get_DataPackageFormatId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]

    _factory = True


class IApplicationViewWithContext(_inspectable.IInspectable):
    get_UIContext: _Callable[[_Pointer[_Windows_UI.IUIContext]],  # value
                             _type.HRESULT]


class IInputPane(_inspectable.IInspectable):
    add_Showing: _Callable[[_Windows_Foundation.ITypedEventHandler[IInputPane, IInputPaneVisibilityEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Showing: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_Hiding: _Callable[[_Windows_Foundation.ITypedEventHandler[IInputPane, IInputPaneVisibilityEventArgs],  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Hiding: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    get_OccludedRect: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                                _type.HRESULT]


class IInputPane2(_inspectable.IInspectable):
    TryShow: _Callable[[_Pointer[_type.boolean]],  # result
                       _type.HRESULT]
    TryHide: _Callable[[_Pointer[_type.boolean]],  # result
                       _type.HRESULT]


class IInputPaneControl(_inspectable.IInspectable):
    get_Visible: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Visible: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class IInputPaneStatics(_inspectable.IInspectable):
    GetForCurrentView: _Callable[[_Pointer[IInputPane]],  # inputPane
                                 _type.HRESULT]

    _factory = True


class IInputPaneStatics2(_inspectable.IInspectable):
    GetForUIContext: _Callable[[_Windows_UI.IUIContext,  # context
                                _Pointer[IInputPane]],  # result
                               _type.HRESULT]

    _factory = True


class IInputPaneVisibilityEventArgs(_inspectable.IInspectable):
    get_OccludedRect: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                                _type.HRESULT]
    put_EnsuredFocusedElementInView: _Callable[[_type.boolean],  # value
                                               _type.HRESULT]
    get_EnsuredFocusedElementInView: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]


class IProjectionManagerStatics(_inspectable.IInspectable):
    StartProjectingAsync: _Callable[[_type.INT32,  # projectionViewId
                                     _type.INT32,  # anchorViewId
                                     _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                    _type.HRESULT]
    SwapDisplaysForViewsAsync: _Callable[[_type.INT32,  # projectionViewId
                                          _type.INT32,  # anchorViewId
                                          _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                         _type.HRESULT]
    StopProjectingAsync: _Callable[[_type.INT32,  # projectionViewId
                                    _type.INT32,  # anchorViewId
                                    _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                   _type.HRESULT]
    get_ProjectionDisplayAvailable: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]
    add_ProjectionDisplayAvailableChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                                     _type.HRESULT]
    remove_ProjectionDisplayAvailableChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                        _type.HRESULT]

    _factory = True


class IProjectionManagerStatics2(_inspectable.IInspectable):
    StartProjectingWithDeviceInfoAsync: _Callable[[_type.INT32,  # projectionViewId
                                                   _type.INT32,  # anchorViewId
                                                   _Windows_Devices_Enumeration.IDeviceInformation,  # displayDeviceInfo
                                                   _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                                  _type.HRESULT]
    RequestStartProjectingAsync: _Callable[[_type.INT32,  # projectionViewId
                                            _type.INT32,  # anchorViewId
                                            _struct.Windows.Foundation.Rect,  # selection
                                            _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                           _type.HRESULT]
    RequestStartProjectingWithPlacementAsync: _Callable[[_type.INT32,  # projectionViewId
                                                         _type.INT32,  # anchorViewId
                                                         _struct.Windows.Foundation.Rect,  # selection
                                                         _enum.Windows.UI.Popups.Placement,  # prefferedPlacement
                                                         _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                                        _type.HRESULT]
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # selector
                                 _type.HRESULT]

    _factory = True


class IStatusBar(_inspectable.IInspectable):
    ShowAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # returnValue
                         _type.HRESULT]
    HideAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # returnValue
                         _type.HRESULT]
    get_BackgroundOpacity: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                     _type.HRESULT]
    put_BackgroundOpacity: _Callable[[_type.DOUBLE],  # value
                                     _type.HRESULT]
    get_ForegroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                   _type.HRESULT]
    put_ForegroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                   _type.HRESULT]
    get_BackgroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                   _type.HRESULT]
    put_BackgroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                   _type.HRESULT]
    get_ProgressIndicator: _Callable[[_Pointer[IStatusBarProgressIndicator]],  # value
                                     _type.HRESULT]
    get_OccludedRect: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                                _type.HRESULT]
    add_Showing: _Callable[[_Windows_Foundation.ITypedEventHandler[IStatusBar, _inspectable.IInspectable],  # eventHandler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Showing: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_Hiding: _Callable[[_Windows_Foundation.ITypedEventHandler[IStatusBar, _inspectable.IInspectable],  # eventHandler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Hiding: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]


class IStatusBarProgressIndicator(_inspectable.IInspectable):
    ShowAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # returnValue
                         _type.HRESULT]
    HideAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # returnValue
                         _type.HRESULT]
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Text: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_ProgressValue: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                                 _type.HRESULT]
    put_ProgressValue: _Callable[[_Windows_Foundation.IReference[_type.DOUBLE]],  # value
                                 _type.HRESULT]


class IStatusBarStatics(_inspectable.IInspectable):
    GetForCurrentView: _Callable[[_Pointer[IStatusBar]],  # value
                                 _type.HRESULT]

    _factory = True


class IUISettings(_inspectable.IInspectable):
    get_HandPreference: _Callable[[_Pointer[_enum.Windows.UI.ViewManagement.HandPreference]],  # value
                                  _type.HRESULT]
    get_CursorSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                              _type.HRESULT]
    get_ScrollBarSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                                 _type.HRESULT]
    get_ScrollBarArrowSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                                      _type.HRESULT]
    get_ScrollBarThumbBoxSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                                         _type.HRESULT]
    get_MessageDuration: _Callable[[_Pointer[_type.UINT32]],  # value
                                   _type.HRESULT]
    get_AnimationsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    get_CaretBrowsingEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_CaretBlinkRate: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]
    get_CaretWidth: _Callable[[_Pointer[_type.UINT32]],  # value
                              _type.HRESULT]
    get_DoubleClickTime: _Callable[[_Pointer[_type.UINT32]],  # value
                                   _type.HRESULT]
    get_MouseHoverTime: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]
    UIElementColor: _Callable[[_enum.Windows.UI.ViewManagement.UIElementType,  # desiredElement
                               _Pointer[_struct.Windows.UI.Color]],  # value
                              _type.HRESULT]


class IUISettings2(_inspectable.IInspectable):
    get_TextScaleFactor: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                   _type.HRESULT]
    add_TextScaleFactorChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IUISettings, _inspectable.IInspectable],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # cookie
                                          _type.HRESULT]
    remove_TextScaleFactorChanged: _Callable[[_struct.EventRegistrationToken],  # cookie
                                             _type.HRESULT]


class IUISettings3(_inspectable.IInspectable):
    GetColorValue: _Callable[[_enum.Windows.UI.ViewManagement.UIColorType,  # desiredColor
                              _Pointer[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    add_ColorValuesChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IUISettings, _inspectable.IInspectable],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # cookie
                                      _type.HRESULT]
    remove_ColorValuesChanged: _Callable[[_struct.EventRegistrationToken],  # cookie
                                         _type.HRESULT]


class IUISettings4(_inspectable.IInspectable):
    get_AdvancedEffectsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    add_AdvancedEffectsEnabledChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IUISettings, _inspectable.IInspectable],  # handler
                                                  _Pointer[_struct.EventRegistrationToken]],  # cookie
                                                 _type.HRESULT]
    remove_AdvancedEffectsEnabledChanged: _Callable[[_struct.EventRegistrationToken],  # cookie
                                                    _type.HRESULT]


class IUISettings5(_inspectable.IInspectable):
    get_AutoHideScrollBars: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    add_AutoHideScrollBarsChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IUISettings, IUISettingsAutoHideScrollBarsChangedEventArgs],  # handler
                                              _Pointer[_struct.EventRegistrationToken]],  # token
                                             _type.HRESULT]
    remove_AutoHideScrollBarsChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                _type.HRESULT]


class IUISettings6(_inspectable.IInspectable):
    add_AnimationsEnabledChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IUISettings, IUISettingsAnimationsEnabledChangedEventArgs],  # handler
                                             _Pointer[_struct.EventRegistrationToken]],  # token
                                            _type.HRESULT]
    remove_AnimationsEnabledChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                               _type.HRESULT]
    add_MessageDurationChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IUISettings, IUISettingsMessageDurationChangedEventArgs],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_MessageDurationChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]


class IUISettingsAnimationsEnabledChangedEventArgs(_inspectable.IInspectable):
    pass


class IUISettingsAutoHideScrollBarsChangedEventArgs(_inspectable.IInspectable):
    pass


class IUISettingsMessageDurationChangedEventArgs(_inspectable.IInspectable):
    pass


class IUIViewSettings(_inspectable.IInspectable):
    get_UserInteractionMode: _Callable[[_Pointer[_enum.Windows.UI.ViewManagement.UserInteractionMode]],  # value
                                       _type.HRESULT]


class IUIViewSettingsStatics(_inspectable.IInspectable):
    GetForCurrentView: _Callable[[_Pointer[IUIViewSettings]],  # current
                                 _type.HRESULT]

    _factory = True


class IViewModePreferences(_inspectable.IInspectable):
    get_ViewSizePreference: _Callable[[_Pointer[_enum.Windows.UI.ViewManagement.ViewSizePreference]],  # value
                                      _type.HRESULT]
    put_ViewSizePreference: _Callable[[_enum.Windows.UI.ViewManagement.ViewSizePreference],  # value
                                      _type.HRESULT]
    get_CustomSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                              _type.HRESULT]
    put_CustomSize: _Callable[[_struct.Windows.Foundation.Size],  # value
                              _type.HRESULT]


class IViewModePreferencesStatics(_inspectable.IInspectable):
    CreateDefault: _Callable[[_enum.Windows.UI.ViewManagement.ApplicationViewMode,  # mode
                              _Pointer[IViewModePreferences]],  # result
                             _type.HRESULT]

    _factory = True
