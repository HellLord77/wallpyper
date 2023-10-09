from __future__ import annotations as _

from typing import Callable as _Callable

from .. import Controls as _Microsoft_UI_Xaml_Controls
from .. import Media as _Microsoft_UI_Xaml_Media
from ... import Composition as _Microsoft_UI_Composition
from ... import Content as _Microsoft_UI_Content
from ... import Xaml as _Microsoft_UI_Xaml
from ..... import inspectable as _inspectable
from .....Windows import Foundation as _Windows_Foundation
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IDesktopWindowXamlSource(_inspectable.IInspectable):
    get_Content: _Callable[[_Pointer[_Microsoft_UI_Xaml.IUIElement]],  # value
                           _type.HRESULT]
    put_Content: _Callable[[_Microsoft_UI_Xaml.IUIElement],  # value
                           _type.HRESULT]
    get_HasFocus: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_SystemBackdrop: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.ISystemBackdrop]],  # value
                                  _type.HRESULT]
    put_SystemBackdrop: _Callable[[_Microsoft_UI_Xaml_Media.ISystemBackdrop],  # value
                                  _type.HRESULT]
    get_SiteBridge: _Callable[[_Pointer[_Microsoft_UI_Content.IDesktopChildSiteBridge]],  # value
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
    Initialize: _Callable[[_struct.Microsoft.UI.WindowId],  # parentWindowId
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


class IElementCompositionPreviewStatics(_inspectable.IInspectable, factory=True):
    GetElementVisual: _Callable[[_Microsoft_UI_Xaml.IUIElement,  # element
                                 _Pointer[_Microsoft_UI_Composition.IVisual]],  # result
                                _type.HRESULT]
    GetElementChildVisual: _Callable[[_Microsoft_UI_Xaml.IUIElement,  # element
                                      _Pointer[_Microsoft_UI_Composition.IVisual]],  # result
                                     _type.HRESULT]
    SetElementChildVisual: _Callable[[_Microsoft_UI_Xaml.IUIElement,  # element
                                      _Microsoft_UI_Composition.IVisual],  # visual
                                     _type.HRESULT]
    GetScrollViewerManipulationPropertySet: _Callable[[_Microsoft_UI_Xaml_Controls.IScrollViewer,  # scrollViewer
                                                       _Pointer[_Microsoft_UI_Composition.ICompositionPropertySet]],  # result
                                                      _type.HRESULT]
    SetImplicitShowAnimation: _Callable[[_Microsoft_UI_Xaml.IUIElement,  # element
                                         _Microsoft_UI_Composition.ICompositionAnimationBase],  # animation
                                        _type.HRESULT]
    SetImplicitHideAnimation: _Callable[[_Microsoft_UI_Xaml.IUIElement,  # element
                                         _Microsoft_UI_Composition.ICompositionAnimationBase],  # animation
                                        _type.HRESULT]
    SetIsTranslationEnabled: _Callable[[_Microsoft_UI_Xaml.IUIElement,  # element
                                        _type.boolean],  # value
                                       _type.HRESULT]
    GetPointerPositionPropertySet: _Callable[[_Microsoft_UI_Xaml.IUIElement,  # targetElement
                                              _Pointer[_Microsoft_UI_Composition.ICompositionPropertySet]],  # result
                                             _type.HRESULT]


class IWindowsXamlManager(_inspectable.IInspectable):
    pass


class IWindowsXamlManagerStatics(_inspectable.IInspectable, factory=True):
    InitializeForCurrentThread: _Callable[[_Pointer[IWindowsXamlManager]],  # result
                                          _type.HRESULT]


class IXamlSourceFocusNavigationRequest(_inspectable.IInspectable):
    get_Reason: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Hosting.XamlSourceFocusNavigationReason]],  # value
                          _type.HRESULT]
    get_HintRect: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                            _type.HRESULT]
    get_CorrelationId: _Callable[[_Pointer[_struct.GUID]],  # value
                                 _type.HRESULT]


class IXamlSourceFocusNavigationRequestFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[_enum.Microsoft.UI.Xaml.Hosting.XamlSourceFocusNavigationReason,  # reason
                               _Pointer[IXamlSourceFocusNavigationRequest]],  # value
                              _type.HRESULT]
    CreateInstanceWithHintRect: _Callable[[_enum.Microsoft.UI.Xaml.Hosting.XamlSourceFocusNavigationReason,  # reason
                                           _struct.Windows.Foundation.Rect,  # hintRect
                                           _Pointer[IXamlSourceFocusNavigationRequest]],  # value
                                          _type.HRESULT]
    CreateInstanceWithHintRectAndCorrelationId: _Callable[[_enum.Microsoft.UI.Xaml.Hosting.XamlSourceFocusNavigationReason,  # reason
                                                           _struct.Windows.Foundation.Rect,  # hintRect
                                                           _struct.GUID,  # correlationId
                                                           _Pointer[IXamlSourceFocusNavigationRequest]],  # value
                                                          _type.HRESULT]


class IXamlSourceFocusNavigationResult(_inspectable.IInspectable):
    get_WasFocusMoved: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]


class IXamlSourceFocusNavigationResultFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[_type.boolean,  # focusMoved
                               _Pointer[IXamlSourceFocusNavigationResult]],  # value
                              _type.HRESULT]
