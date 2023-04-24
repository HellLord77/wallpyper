from __future__ import annotations

from typing import Callable as _Callable

from .. import Composition as _Windows_UI_Composition
from ... import Foundation as _Windows_Foundation
from ... import System as _Windows_System
from ... import UI as _Windows_UI
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IAppWindow(_inspectable.IInspectable):
    get_Content: _Callable[[_Pointer[_Windows_UI.IUIContentRoot]],  # value
                           _type.HRESULT]
    get_DispatcherQueue: _Callable[[_Pointer[_Windows_System.IDispatcherQueue]],  # value
                                   _type.HRESULT]
    get_Frame: _Callable[[_Pointer[IAppWindowFrame]],  # value
                         _type.HRESULT]
    get_IsVisible: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_PersistedStateId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    put_PersistedStateId: _Callable[[_type.HSTRING],  # value
                                    _type.HRESULT]
    get_Presenter: _Callable[[_Pointer[IAppWindowPresenter]],  # value
                             _type.HRESULT]
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Title: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_TitleBar: _Callable[[_Pointer[IAppWindowTitleBar]],  # value
                            _type.HRESULT]
    get_UIContext: _Callable[[_Pointer[_Windows_UI.IUIContext]],  # value
                             _type.HRESULT]
    get_WindowingEnvironment: _Callable[[_Pointer[IWindowingEnvironment]],  # value
                                        _type.HRESULT]
    CloseAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                          _type.HRESULT]
    GetPlacement: _Callable[[_Pointer[IAppWindowPlacement]],  # result
                            _type.HRESULT]
    GetDisplayRegions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IDisplayRegion]]],  # result
                                 _type.HRESULT]
    RequestMoveToDisplayRegion: _Callable[[IDisplayRegion],  # displayRegion
                                          _type.HRESULT]
    RequestMoveAdjacentToCurrentView: _Callable[[],
                                                _type.HRESULT]
    RequestMoveAdjacentToWindow: _Callable[[IAppWindow],  # anchorWindow
                                           _type.HRESULT]
    RequestMoveRelativeToWindowContent: _Callable[[IAppWindow,  # anchorWindow
                                                   _struct.Windows.Foundation.Point],  # contentOffset
                                                  _type.HRESULT]
    RequestMoveRelativeToCurrentViewContent: _Callable[[_struct.Windows.Foundation.Point],  # contentOffset
                                                       _type.HRESULT]
    RequestMoveRelativeToDisplayRegion: _Callable[[IDisplayRegion,  # displayRegion
                                                   _struct.Windows.Foundation.Point],  # displayRegionOffset
                                                  _type.HRESULT]
    RequestSize: _Callable[[_struct.Windows.Foundation.Size],  # frameSize
                           _type.HRESULT]
    TryShowAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                            _type.HRESULT]
    add_Changed: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppWindow, IAppWindowChangedEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Changed: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_Closed: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppWindow, IAppWindowClosedEventArgs],  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Closed: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    add_CloseRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppWindow, IAppWindowCloseRequestedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_CloseRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]


class IAppWindowChangedEventArgs(_inspectable.IInspectable):
    get_DidAvailableWindowPresentationsChange: _Callable[[_Pointer[_type.boolean]],  # value
                                                         _type.HRESULT]
    get_DidDisplayRegionsChange: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    get_DidFrameChange: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    get_DidSizeChange: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_DidTitleBarChange: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    get_DidVisibilityChange: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    get_DidWindowingEnvironmentChange: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]
    get_DidWindowPresentationChange: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]


class IAppWindowCloseRequestedEventArgs(_inspectable.IInspectable):
    get_Cancel: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_Cancel: _Callable[[_type.boolean],  # value
                          _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IAppWindowClosedEventArgs(_inspectable.IInspectable):
    get_Reason: _Callable[[_Pointer[_enum.Windows.UI.WindowManagement.AppWindowClosedReason]],  # value
                          _type.HRESULT]


class IAppWindowFrame(_inspectable.IInspectable):
    get_DragRegionVisuals: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Composition.IVisualElement]]],  # value
                                     _type.HRESULT]


class IAppWindowFrameStyle(_inspectable.IInspectable):
    GetFrameStyle: _Callable[[_Pointer[_enum.Windows.UI.WindowManagement.AppWindowFrameStyle]],  # result
                             _type.HRESULT]
    SetFrameStyle: _Callable[[_enum.Windows.UI.WindowManagement.AppWindowFrameStyle],  # frameStyle
                             _type.HRESULT]


class IAppWindowPlacement(_inspectable.IInspectable):
    get_DisplayRegion: _Callable[[_Pointer[IDisplayRegion]],  # value
                                 _type.HRESULT]
    get_Offset: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                          _type.HRESULT]
    get_Size: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                        _type.HRESULT]


class IAppWindowPresentationConfiguration(_inspectable.IInspectable):
    get_Kind: _Callable[[_Pointer[_enum.Windows.UI.WindowManagement.AppWindowPresentationKind]],  # value
                        _type.HRESULT]


class IAppWindowPresentationConfigurationFactory(_inspectable.IInspectable):
    pass


class IAppWindowPresenter(_inspectable.IInspectable):
    GetConfiguration: _Callable[[_Pointer[IAppWindowPresentationConfiguration]],  # result
                                _type.HRESULT]
    IsPresentationSupported: _Callable[[_enum.Windows.UI.WindowManagement.AppWindowPresentationKind,  # presentationKind
                                        _Pointer[_type.boolean]],  # result
                                       _type.HRESULT]
    RequestPresentation: _Callable[[IAppWindowPresentationConfiguration,  # configuration
                                    _Pointer[_type.boolean]],  # result
                                   _type.HRESULT]
    RequestPresentationByKind: _Callable[[_enum.Windows.UI.WindowManagement.AppWindowPresentationKind,  # presentationKind
                                          _Pointer[_type.boolean]],  # result
                                         _type.HRESULT]


class IAppWindowStatics(_inspectable.IInspectable):
    TryCreateAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IAppWindow]]],  # operation
                              _type.HRESULT]
    ClearAllPersistedState: _Callable[[],
                                      _type.HRESULT]
    ClearPersistedState: _Callable[[_type.HSTRING],  # key
                                   _type.HRESULT]

    _factory = True


class IAppWindowTitleBar(_inspectable.IInspectable):
    get_BackgroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                   _type.HRESULT]
    put_BackgroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                   _type.HRESULT]
    get_ButtonBackgroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                         _type.HRESULT]
    put_ButtonBackgroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                         _type.HRESULT]
    get_ButtonForegroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                         _type.HRESULT]
    put_ButtonForegroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                         _type.HRESULT]
    get_ButtonHoverBackgroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                              _type.HRESULT]
    put_ButtonHoverBackgroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                              _type.HRESULT]
    get_ButtonHoverForegroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                              _type.HRESULT]
    put_ButtonHoverForegroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                              _type.HRESULT]
    get_ButtonInactiveBackgroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                                 _type.HRESULT]
    put_ButtonInactiveBackgroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                                 _type.HRESULT]
    get_ButtonInactiveForegroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                                 _type.HRESULT]
    put_ButtonInactiveForegroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                                 _type.HRESULT]
    get_ButtonPressedBackgroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                                _type.HRESULT]
    put_ButtonPressedBackgroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                                _type.HRESULT]
    get_ButtonPressedForegroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                                _type.HRESULT]
    put_ButtonPressedForegroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                                _type.HRESULT]
    get_ExtendsContentIntoTitleBar: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]
    put_ExtendsContentIntoTitleBar: _Callable[[_type.boolean],  # value
                                              _type.HRESULT]
    get_ForegroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                   _type.HRESULT]
    put_ForegroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                   _type.HRESULT]
    get_InactiveBackgroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                           _type.HRESULT]
    put_InactiveBackgroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                           _type.HRESULT]
    get_InactiveForegroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                           _type.HRESULT]
    put_InactiveForegroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                           _type.HRESULT]
    get_IsVisible: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    GetTitleBarOcclusions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IAppWindowTitleBarOcclusion]]],  # result
                                     _type.HRESULT]


class IAppWindowTitleBarOcclusion(_inspectable.IInspectable):
    get_OccludingRect: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                                 _type.HRESULT]


class IAppWindowTitleBarVisibility(_inspectable.IInspectable):
    GetPreferredVisibility: _Callable[[_Pointer[_enum.Windows.UI.WindowManagement.AppWindowTitleBarVisibility]],  # result
                                      _type.HRESULT]
    SetPreferredVisibility: _Callable[[_enum.Windows.UI.WindowManagement.AppWindowTitleBarVisibility],  # visibilityMode
                                      _type.HRESULT]


class ICompactOverlayPresentationConfiguration(_inspectable.IInspectable):
    pass


class IDefaultPresentationConfiguration(_inspectable.IInspectable):
    pass


class IDisplayRegion(_inspectable.IInspectable):
    get_DisplayMonitorDeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                          _type.HRESULT]
    get_IsVisible: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_WorkAreaOffset: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                                  _type.HRESULT]
    get_WorkAreaSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                                _type.HRESULT]
    get_WindowingEnvironment: _Callable[[_Pointer[IWindowingEnvironment]],  # value
                                        _type.HRESULT]
    add_Changed: _Callable[[_Windows_Foundation.ITypedEventHandler[IDisplayRegion, _inspectable.IInspectable],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Changed: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]


class IFullScreenPresentationConfiguration(_inspectable.IInspectable):
    get_IsExclusive: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    put_IsExclusive: _Callable[[_type.boolean],  # value
                               _type.HRESULT]


class IWindowServicesStatics(_inspectable.IInspectable):
    FindAllTopLevelWindowIds: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_struct.Windows.UI.WindowId]]],  # result
                                        _type.HRESULT]

    _factory = True


class IWindowingEnvironment(_inspectable.IInspectable):
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_Kind: _Callable[[_Pointer[_enum.Windows.UI.WindowManagement.WindowingEnvironmentKind]],  # value
                        _type.HRESULT]
    GetDisplayRegions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IDisplayRegion]]],  # result
                                 _type.HRESULT]
    add_Changed: _Callable[[_Windows_Foundation.ITypedEventHandler[IWindowingEnvironment, IWindowingEnvironmentChangedEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Changed: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]


class IWindowingEnvironmentAddedEventArgs(_inspectable.IInspectable):
    get_WindowingEnvironment: _Callable[[_Pointer[IWindowingEnvironment]],  # value
                                        _type.HRESULT]


class IWindowingEnvironmentChangedEventArgs(_inspectable.IInspectable):
    pass


class IWindowingEnvironmentRemovedEventArgs(_inspectable.IInspectable):
    get_WindowingEnvironment: _Callable[[_Pointer[IWindowingEnvironment]],  # value
                                        _type.HRESULT]


class IWindowingEnvironmentStatics(_inspectable.IInspectable):
    FindAll: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IWindowingEnvironment]]],  # result
                       _type.HRESULT]
    FindAllWithKind: _Callable[[_enum.Windows.UI.WindowManagement.WindowingEnvironmentKind,  # kind
                                _Pointer[_Windows_Foundation_Collections.IVectorView[IWindowingEnvironment]]],  # result
                               _type.HRESULT]

    _factory = True
