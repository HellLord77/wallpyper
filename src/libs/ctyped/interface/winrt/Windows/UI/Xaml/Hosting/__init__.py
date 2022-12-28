from __future__ import annotations as _

from typing import Callable as _Callable

from .. import Controls as _Windows_UI_Xaml_Controls
from ... import Composition as _Windows_UI_Composition
from ... import WindowManagement as _Windows_UI_WindowManagement
from ... import Xaml as _Windows_UI_Xaml
from .... import Foundation as _Windows_Foundation
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IDesignerAppExitedEventArgs(_inspectable.IInspectable):
    get_ExitCode: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]


class IDesignerAppManager(_inspectable.IInspectable):
    get_AppUserModelId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    add_DesignerAppExited: _Callable[[_Windows_Foundation.ITypedEventHandler[IDesignerAppManager, IDesignerAppExitedEventArgs],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_DesignerAppExited: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    CreateNewViewAsync: _Callable[[_enum.Windows.UI.Xaml.Hosting.DesignerAppViewState,  # initialViewState
                                   _struct.Windows.Foundation.Size,  # initialViewSize
                                   _Pointer[_Windows_Foundation.IAsyncOperation[IDesignerAppView]]],  # operation
                                  _type.HRESULT]
    LoadObjectIntoAppAsync: _Callable[[_type.HSTRING,  # dllName
                                       _struct.GUID,  # classId
                                       _type.HSTRING,  # initializationData
                                       _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                      _type.HRESULT]


class IDesignerAppManagerFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.HSTRING,  # appUserModelId
                       _Pointer[IDesignerAppManager]],  # value
                      _type.HRESULT]

    _factory = True


class IDesignerAppView(_inspectable.IInspectable):
    get_ApplicationViewId: _Callable[[_Pointer[_type.INT32]],  # value
                                     _type.HRESULT]
    get_AppUserModelId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_ViewState: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Hosting.DesignerAppViewState]],  # value
                             _type.HRESULT]
    get_ViewSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                            _type.HRESULT]
    UpdateViewAsync: _Callable[[_enum.Windows.UI.Xaml.Hosting.DesignerAppViewState,  # viewState
                                _struct.Windows.Foundation.Size,  # viewSize
                                _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                               _type.HRESULT]


class IDesktopWindowXamlSource(_inspectable.IInspectable):
    get_Content: _Callable[[_Pointer[_Windows_UI_Xaml.IUIElement]],  # value
                           _type.HRESULT]
    put_Content: _Callable[[_Windows_UI_Xaml.IUIElement],  # value
                           _type.HRESULT]
    get_HasFocus: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    add_TakeFocusRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IDesktopWindowXamlSource, IDesktopWindowXamlSourceTakeFocusRequestedEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_TakeFocusRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_GotFocus: _Callable[[_Windows_Foundation.ITypedEventHandler[IDesktopWindowXamlSource, IDesktopWindowXamlSourceGotFocusEventArgs],  # handler
                             _Pointer[_struct.EventRegistrationToken]],  # token
                            _type.HRESULT]
    remove_GotFocus: _Callable[[_struct.EventRegistrationToken],  # token
                               _type.HRESULT]
    NavigateFocus: _Callable[[IXamlSourceFocusNavigationRequest,  # request
                              _Pointer[IXamlSourceFocusNavigationResult]],  # result
                             _type.HRESULT]


class IDesktopWindowXamlSourceFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IDesktopWindowXamlSource]],  # value
                              _type.HRESULT]


class IDesktopWindowXamlSourceGotFocusEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IXamlSourceFocusNavigationRequest]],  # value
                           _type.HRESULT]


class IDesktopWindowXamlSourceTakeFocusRequestedEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IXamlSourceFocusNavigationRequest]],  # value
                           _type.HRESULT]


class IElementCompositionPreview(_inspectable.IInspectable):
    pass


class IElementCompositionPreviewStatics(_inspectable.IInspectable):
    GetElementVisual: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                 _Pointer[_Windows_UI_Composition.IVisual]],  # result
                                _type.HRESULT]
    GetElementChildVisual: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                      _Pointer[_Windows_UI_Composition.IVisual]],  # result
                                     _type.HRESULT]
    SetElementChildVisual: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                      _Windows_UI_Composition.IVisual],  # visual
                                     _type.HRESULT]
    GetScrollViewerManipulationPropertySet: _Callable[[_Windows_UI_Xaml_Controls.IScrollViewer,  # scrollViewer
                                                       _Pointer[_Windows_UI_Composition.ICompositionPropertySet]],  # result
                                                      _type.HRESULT]

    _factory = True


class IElementCompositionPreviewStatics2(_inspectable.IInspectable):
    SetImplicitShowAnimation: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                         _Windows_UI_Composition.ICompositionAnimationBase],  # animation
                                        _type.HRESULT]
    SetImplicitHideAnimation: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                         _Windows_UI_Composition.ICompositionAnimationBase],  # animation
                                        _type.HRESULT]
    SetIsTranslationEnabled: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                        _type.boolean],  # value
                                       _type.HRESULT]
    GetPointerPositionPropertySet: _Callable[[_Windows_UI_Xaml.IUIElement,  # targetElement
                                              _Pointer[_Windows_UI_Composition.ICompositionPropertySet]],  # result
                                             _type.HRESULT]

    _factory = True


class IElementCompositionPreviewStatics3(_inspectable.IInspectable):
    SetAppWindowContent: _Callable[[_Windows_UI_WindowManagement.IAppWindow,  # appWindow
                                    _Windows_UI_Xaml.IUIElement],  # xamlContent
                                   _type.HRESULT]
    GetAppWindowContent: _Callable[[_Windows_UI_WindowManagement.IAppWindow,  # appWindow
                                    _Pointer[_Windows_UI_Xaml.IUIElement]],  # result
                                   _type.HRESULT]

    _factory = True


class IWindowsXamlManager(_inspectable.IInspectable):
    pass


class IWindowsXamlManagerStatics(_inspectable.IInspectable):
    InitializeForCurrentThread: _Callable[[_Pointer[IWindowsXamlManager]],  # result
                                          _type.HRESULT]

    _factory = True


class IXamlSourceFocusNavigationRequest(_inspectable.IInspectable):
    get_Reason: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationReason]],  # value
                          _type.HRESULT]
    get_HintRect: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                            _type.HRESULT]
    get_CorrelationId: _Callable[[_Pointer[_struct.GUID]],  # value
                                 _type.HRESULT]


class IXamlSourceFocusNavigationRequestFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_enum.Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationReason,  # reason
                               _Pointer[IXamlSourceFocusNavigationRequest]],  # value
                              _type.HRESULT]
    CreateInstanceWithHintRect: _Callable[[_enum.Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationReason,  # reason
                                           _struct.Windows.Foundation.Rect,  # hintRect
                                           _Pointer[IXamlSourceFocusNavigationRequest]],  # value
                                          _type.HRESULT]
    CreateInstanceWithHintRectAndCorrelationId: _Callable[[_enum.Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationReason,  # reason
                                                           _struct.Windows.Foundation.Rect,  # hintRect
                                                           _struct.GUID,  # correlationId
                                                           _Pointer[IXamlSourceFocusNavigationRequest]],  # value
                                                          _type.HRESULT]

    _factory = True


class IXamlSourceFocusNavigationResult(_inspectable.IInspectable):
    get_WasFocusMoved: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]


class IXamlSourceFocusNavigationResultFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_type.boolean,  # focusMoved
                               _Pointer[IXamlSourceFocusNavigationResult]],  # value
                              _type.HRESULT]

    _factory = True


class IXamlUIPresenter(_inspectable.IInspectable):
    get_RootElement: _Callable[[_Pointer[_Windows_UI_Xaml.IUIElement]],  # value
                               _type.HRESULT]
    put_RootElement: _Callable[[_Windows_UI_Xaml.IUIElement],  # value
                               _type.HRESULT]
    get_ThemeKey: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_ThemeKey: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_ThemeResourcesXaml: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    put_ThemeResourcesXaml: _Callable[[_type.HSTRING],  # value
                                      _type.HRESULT]
    SetSize: _Callable[[_type.INT32,  # width
                        _type.INT32],  # height
                       _type.HRESULT]
    Render: _Callable[[],
                      _type.HRESULT]
    Present: _Callable[[],
                       _type.HRESULT]


class IXamlUIPresenterHost(_inspectable.IInspectable):
    ResolveFileResource: _Callable[[_type.HSTRING,  # path
                                    _Pointer[_type.HSTRING]],  # result
                                   _type.HRESULT]


class IXamlUIPresenterHost2(_inspectable.IInspectable):
    GetGenericXamlFilePath: _Callable[[_Pointer[_type.HSTRING]],  # result
                                      _type.HRESULT]


class IXamlUIPresenterHost3(_inspectable.IInspectable):
    ResolveDictionaryResource: _Callable[[_Windows_UI_Xaml.IResourceDictionary,  # dictionary
                                          _inspectable.IInspectable,  # dictionaryKey
                                          _inspectable.IInspectable,  # suggestedValue
                                          _Pointer[_inspectable.IInspectable]],  # result
                                         _type.HRESULT]


class IXamlUIPresenterStatics(_inspectable.IInspectable):
    get_CompleteTimelinesAutomatically: _Callable[[_Pointer[_type.boolean]],  # value
                                                  _type.HRESULT]
    put_CompleteTimelinesAutomatically: _Callable[[_type.boolean],  # value
                                                  _type.HRESULT]
    SetHost: _Callable[[IXamlUIPresenterHost],  # host
                       _type.HRESULT]
    NotifyWindowSizeChanged: _Callable[[],
                                       _type.HRESULT]

    _factory = True


class IXamlUIPresenterStatics2(_inspectable.IInspectable):
    GetFlyoutPlacementTargetInfo: _Callable[[_Windows_UI_Xaml.IFrameworkElement,  # placementTarget
                                             _enum.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode,  # preferredPlacement
                                             _Pointer[_enum.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode],  # targetPreferredPlacement
                                             _Pointer[_type.boolean],  # allowFallbacks
                                             _Pointer[_struct.Windows.Foundation.Rect]],  # returnValue
                                            _type.HRESULT]
    GetFlyoutPlacement: _Callable[[_struct.Windows.Foundation.Rect,  # placementTargetBounds
                                   _struct.Windows.Foundation.Size,  # controlSize
                                   _struct.Windows.Foundation.Size,  # minControlSize
                                   _struct.Windows.Foundation.Rect,  # containerRect
                                   _enum.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode,  # targetPreferredPlacement
                                   _type.boolean,  # allowFallbacks
                                   _Pointer[_enum.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode],  # chosenPlacement
                                   _Pointer[_struct.Windows.Foundation.Rect]],  # returnValue
                                  _type.HRESULT]

    _factory = True
