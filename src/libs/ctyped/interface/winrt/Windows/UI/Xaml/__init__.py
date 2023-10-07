from __future__ import annotations as _

from typing import Callable as _Callable

from . import Controls as _Windows_UI_Xaml_Controls
from . import Data as _Windows_UI_Xaml_Data
from . import Input as _Windows_UI_Xaml_Input
from . import Media as _Windows_UI_Xaml_Media
from .Automation import Peers as _Windows_UI_Xaml_Automation_Peers
from .Controls import Primitives as _Windows_UI_Xaml_Controls_Primitives
from .Media import Animation as _Windows_UI_Xaml_Media_Animation
from .Media import Imaging as _Windows_UI_Xaml_Media_Imaging
from .Media import Media3D as _Windows_UI_Xaml_Media_Media3D
from .. import Composition as _Windows_UI_Composition
from .. import Core as _Windows_UI_Core
from .. import Input as _Windows_UI_Input
from ... import ApplicationModel as _Windows_ApplicationModel
from ... import Foundation as _Windows_Foundation
from ... import UI as _Windows_UI
from ...ApplicationModel import Activation as _Windows_ApplicationModel_Activation
from ...ApplicationModel import DataTransfer as _Windows_ApplicationModel_DataTransfer
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Graphics import Imaging as _Windows_Graphics_Imaging
from .... import inspectable as _inspectable
from .....um import Unknwnbase as _Unknwnbase
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class _IApplicationInitializationCallback:
    Invoke: _Callable[[IApplicationInitializationCallbackParams],  # p
                      _type.HRESULT]


class IApplicationInitializationCallback(_IApplicationInitializationCallback, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IApplicationInitializationCallback_impl(_IApplicationInitializationCallback, _Unknwnbase.IUnknown_impl):
    pass


class _IBindingFailedEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       IBindingFailedEventArgs],  # e
                      _type.HRESULT]


class IBindingFailedEventHandler(_IBindingFailedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IBindingFailedEventHandler_impl(_IBindingFailedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ICreateDefaultValueCallback:
    Invoke: _Callable[[_Pointer[_inspectable.IInspectable]],  # result
                      _type.HRESULT]


class ICreateDefaultValueCallback(_ICreateDefaultValueCallback, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICreateDefaultValueCallback_impl(_ICreateDefaultValueCallback, _Unknwnbase.IUnknown_impl):
    pass


class _IDependencyPropertyChangedCallback:
    Invoke: _Callable[[IDependencyObject,  # sender
                       IDependencyProperty],  # dp
                      _type.HRESULT]


class IDependencyPropertyChangedCallback(_IDependencyPropertyChangedCallback, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IDependencyPropertyChangedCallback_impl(_IDependencyPropertyChangedCallback, _Unknwnbase.IUnknown_impl):
    pass


class _IDependencyPropertyChangedEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       IDependencyPropertyChangedEventArgs],  # e
                      _type.HRESULT]


class IDependencyPropertyChangedEventHandler(_IDependencyPropertyChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IDependencyPropertyChangedEventHandler_impl(_IDependencyPropertyChangedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IDragEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       IDragEventArgs],  # e
                      _type.HRESULT]


class IDragEventHandler(_IDragEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IDragEventHandler_impl(_IDragEventHandler, _Unknwnbase.IUnknown_impl):
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


class _IExceptionRoutedEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       IExceptionRoutedEventArgs],  # e
                      _type.HRESULT]


class IExceptionRoutedEventHandler(_IExceptionRoutedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IExceptionRoutedEventHandler_impl(_IExceptionRoutedEventHandler, _Unknwnbase.IUnknown_impl):
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


class _IPropertyChangedCallback:
    Invoke: _Callable[[IDependencyObject,  # d
                       IDependencyPropertyChangedEventArgs],  # e
                      _type.HRESULT]


class IPropertyChangedCallback(_IPropertyChangedCallback, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IPropertyChangedCallback_impl(_IPropertyChangedCallback, _Unknwnbase.IUnknown_impl):
    pass


class _IRoutedEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       IRoutedEventArgs],  # e
                      _type.HRESULT]


class IRoutedEventHandler(_IRoutedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IRoutedEventHandler_impl(_IRoutedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ISizeChangedEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       ISizeChangedEventArgs],  # e
                      _type.HRESULT]


class ISizeChangedEventHandler(_ISizeChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ISizeChangedEventHandler_impl(_ISizeChangedEventHandler, _Unknwnbase.IUnknown_impl):
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


class _IUnhandledExceptionEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       IUnhandledExceptionEventArgs],  # e
                      _type.HRESULT]


class IUnhandledExceptionEventHandler(_IUnhandledExceptionEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IUnhandledExceptionEventHandler_impl(_IUnhandledExceptionEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IVisualStateChangedEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       IVisualStateChangedEventArgs],  # e
                      _type.HRESULT]


class IVisualStateChangedEventHandler(_IVisualStateChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IVisualStateChangedEventHandler_impl(_IVisualStateChangedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IWindowActivatedEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       _Windows_UI_Core.IWindowActivatedEventArgs],  # e
                      _type.HRESULT]


class IWindowActivatedEventHandler(_IWindowActivatedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IWindowActivatedEventHandler_impl(_IWindowActivatedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IWindowClosedEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       _Windows_UI_Core.ICoreWindowEventArgs],  # e
                      _type.HRESULT]


class IWindowClosedEventHandler(_IWindowClosedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IWindowClosedEventHandler_impl(_IWindowClosedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IWindowSizeChangedEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       _Windows_UI_Core.IWindowSizeChangedEventArgs],  # e
                      _type.HRESULT]


class IWindowSizeChangedEventHandler(_IWindowSizeChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IWindowSizeChangedEventHandler_impl(_IWindowSizeChangedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IWindowVisibilityChangedEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       _Windows_UI_Core.IVisibilityChangedEventArgs],  # e
                      _type.HRESULT]


class IWindowVisibilityChangedEventHandler(_IWindowVisibilityChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IWindowVisibilityChangedEventHandler_impl(_IWindowVisibilityChangedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class IAdaptiveTrigger(_inspectable.IInspectable):
    get_MinWindowWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    put_MinWindowWidth: _Callable[[_type.DOUBLE],  # value
                                  _type.HRESULT]
    get_MinWindowHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                   _type.HRESULT]
    put_MinWindowHeight: _Callable[[_type.DOUBLE],  # value
                                   _type.HRESULT]


class IAdaptiveTriggerFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IAdaptiveTrigger]],  # value
                              _type.HRESULT]


class IAdaptiveTriggerStatics(_inspectable.IInspectable, factory=True):
    get_MinWindowWidthProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_MinWindowHeightProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                           _type.HRESULT]


class IApplication(_inspectable.IInspectable):
    get_Resources: _Callable[[_Pointer[IResourceDictionary]],  # value
                             _type.HRESULT]
    put_Resources: _Callable[[IResourceDictionary],  # value
                             _type.HRESULT]
    get_DebugSettings: _Callable[[_Pointer[IDebugSettings]],  # value
                                 _type.HRESULT]
    get_RequestedTheme: _Callable[[_Pointer[_enum.Windows.UI.Xaml.ApplicationTheme]],  # value
                                  _type.HRESULT]
    put_RequestedTheme: _Callable[[_enum.Windows.UI.Xaml.ApplicationTheme],  # value
                                  _type.HRESULT]
    add_UnhandledException: _Callable[[IUnhandledExceptionEventHandler,  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_UnhandledException: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_Suspending: _Callable[[ISuspendingEventHandler,  # handler
                               _Pointer[_struct.EventRegistrationToken]],  # token
                              _type.HRESULT]
    remove_Suspending: _Callable[[_struct.EventRegistrationToken],  # token
                                 _type.HRESULT]
    add_Resuming: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                             _Pointer[_struct.EventRegistrationToken]],  # token
                            _type.HRESULT]
    remove_Resuming: _Callable[[_struct.EventRegistrationToken],  # token
                               _type.HRESULT]
    Exit: _Callable[[],
                    _type.HRESULT]


class IApplication2(_inspectable.IInspectable):
    get_FocusVisualKind: _Callable[[_Pointer[_enum.Windows.UI.Xaml.FocusVisualKind]],  # value
                                   _type.HRESULT]
    put_FocusVisualKind: _Callable[[_enum.Windows.UI.Xaml.FocusVisualKind],  # value
                                   _type.HRESULT]
    get_RequiresPointerMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.ApplicationRequiresPointerMode]],  # value
                                       _type.HRESULT]
    put_RequiresPointerMode: _Callable[[_enum.Windows.UI.Xaml.ApplicationRequiresPointerMode],  # value
                                       _type.HRESULT]
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


class IApplication3(_inspectable.IInspectable):
    get_HighContrastAdjustment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.ApplicationHighContrastAdjustment]],  # value
                                          _type.HRESULT]
    put_HighContrastAdjustment: _Callable[[_enum.Windows.UI.Xaml.ApplicationHighContrastAdjustment],  # value
                                          _type.HRESULT]


class IApplicationFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IApplication]],  # value
                              _type.HRESULT]


class IApplicationInitializationCallbackParams(_inspectable.IInspectable):
    pass


class IApplicationOverrides(_inspectable.IInspectable):
    OnActivated: _Callable[[_Windows_ApplicationModel_Activation.IActivatedEventArgs],  # args
                           _type.HRESULT]
    OnLaunched: _Callable[[_Windows_ApplicationModel_Activation.ILaunchActivatedEventArgs],  # args
                          _type.HRESULT]
    OnFileActivated: _Callable[[_Windows_ApplicationModel_Activation.IFileActivatedEventArgs],  # args
                               _type.HRESULT]
    OnSearchActivated: _Callable[[_Windows_ApplicationModel_Activation.ISearchActivatedEventArgs],  # args
                                 _type.HRESULT]
    OnShareTargetActivated: _Callable[[_Windows_ApplicationModel_Activation.IShareTargetActivatedEventArgs],  # args
                                      _type.HRESULT]
    OnFileOpenPickerActivated: _Callable[[_Windows_ApplicationModel_Activation.IFileOpenPickerActivatedEventArgs],  # args
                                         _type.HRESULT]
    OnFileSavePickerActivated: _Callable[[_Windows_ApplicationModel_Activation.IFileSavePickerActivatedEventArgs],  # args
                                         _type.HRESULT]
    OnCachedFileUpdaterActivated: _Callable[[_Windows_ApplicationModel_Activation.ICachedFileUpdaterActivatedEventArgs],  # args
                                            _type.HRESULT]
    OnWindowCreated: _Callable[[IWindowCreatedEventArgs],  # args
                               _type.HRESULT]


class IApplicationOverrides2(_inspectable.IInspectable):
    OnBackgroundActivated: _Callable[[_Windows_ApplicationModel_Activation.IBackgroundActivatedEventArgs],  # args
                                     _type.HRESULT]


class IApplicationStatics(_inspectable.IInspectable, factory=True):
    get_Current: _Callable[[_Pointer[IApplication]],  # value
                           _type.HRESULT]
    Start: _Callable[[IApplicationInitializationCallback],  # callback
                     _type.HRESULT]
    LoadComponent: _Callable[[_inspectable.IInspectable,  # component
                              _Windows_Foundation.IUriRuntimeClass],  # resourceLocator
                             _type.HRESULT]
    LoadComponentWithResourceLocation: _Callable[[_inspectable.IInspectable,  # component
                                                  _Windows_Foundation.IUriRuntimeClass,  # resourceLocator
                                                  _enum.Windows.UI.Xaml.Controls.Primitives.ComponentResourceLocation],  # componentResourceLocation
                                                 _type.HRESULT]


class IBindingFailedEventArgs(_inspectable.IInspectable):
    get_Message: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]


class IBringIntoViewOptions(_inspectable.IInspectable):
    get_AnimationDesired: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_AnimationDesired: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_TargetRect: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.Rect]]],  # value
                              _type.HRESULT]
    put_TargetRect: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.Rect]],  # value
                              _type.HRESULT]


class IBringIntoViewOptions2(_inspectable.IInspectable):
    get_HorizontalAlignmentRatio: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                            _type.HRESULT]
    put_HorizontalAlignmentRatio: _Callable[[_type.DOUBLE],  # value
                                            _type.HRESULT]
    get_VerticalAlignmentRatio: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                          _type.HRESULT]
    put_VerticalAlignmentRatio: _Callable[[_type.DOUBLE],  # value
                                          _type.HRESULT]
    get_HorizontalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]
    put_HorizontalOffset: _Callable[[_type.DOUBLE],  # value
                                    _type.HRESULT]
    get_VerticalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    put_VerticalOffset: _Callable[[_type.DOUBLE],  # value
                                  _type.HRESULT]


class IBringIntoViewRequestedEventArgs(_inspectable.IInspectable):
    get_TargetElement: _Callable[[_Pointer[IUIElement]],  # value
                                 _type.HRESULT]
    put_TargetElement: _Callable[[IUIElement],  # value
                                 _type.HRESULT]
    get_AnimationDesired: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_AnimationDesired: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_TargetRect: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                              _type.HRESULT]
    put_TargetRect: _Callable[[_struct.Windows.Foundation.Rect],  # value
                              _type.HRESULT]
    get_HorizontalAlignmentRatio: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                            _type.HRESULT]
    get_VerticalAlignmentRatio: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                          _type.HRESULT]
    get_HorizontalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]
    put_HorizontalOffset: _Callable[[_type.DOUBLE],  # value
                                    _type.HRESULT]
    get_VerticalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    put_VerticalOffset: _Callable[[_type.DOUBLE],  # value
                                  _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class IBrushTransition(_inspectable.IInspectable):
    get_Duration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    put_Duration: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                            _type.HRESULT]


class IBrushTransitionFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IBrushTransition]],  # value
                              _type.HRESULT]


class IColorPaletteResources(_inspectable.IInspectable):
    get_AltHigh: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                           _type.HRESULT]
    put_AltHigh: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                           _type.HRESULT]
    get_AltLow: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                          _type.HRESULT]
    put_AltLow: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                          _type.HRESULT]
    get_AltMedium: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                             _type.HRESULT]
    put_AltMedium: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    get_AltMediumHigh: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                 _type.HRESULT]
    put_AltMediumHigh: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                 _type.HRESULT]
    get_AltMediumLow: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                _type.HRESULT]
    put_AltMediumLow: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                _type.HRESULT]
    get_BaseHigh: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                            _type.HRESULT]
    put_BaseHigh: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                            _type.HRESULT]
    get_BaseLow: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                           _type.HRESULT]
    put_BaseLow: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                           _type.HRESULT]
    get_BaseMedium: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                              _type.HRESULT]
    put_BaseMedium: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                              _type.HRESULT]
    get_BaseMediumHigh: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                  _type.HRESULT]
    put_BaseMediumHigh: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                  _type.HRESULT]
    get_BaseMediumLow: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                 _type.HRESULT]
    put_BaseMediumLow: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                 _type.HRESULT]
    get_ChromeAltLow: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                _type.HRESULT]
    put_ChromeAltLow: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                _type.HRESULT]
    get_ChromeBlackHigh: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                   _type.HRESULT]
    put_ChromeBlackHigh: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                   _type.HRESULT]
    get_ChromeBlackLow: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                  _type.HRESULT]
    put_ChromeBlackLow: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                  _type.HRESULT]
    get_ChromeBlackMediumLow: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                        _type.HRESULT]
    put_ChromeBlackMediumLow: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                        _type.HRESULT]
    get_ChromeBlackMedium: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                     _type.HRESULT]
    put_ChromeBlackMedium: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                     _type.HRESULT]
    get_ChromeDisabledHigh: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                      _type.HRESULT]
    put_ChromeDisabledHigh: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                      _type.HRESULT]
    get_ChromeDisabledLow: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                     _type.HRESULT]
    put_ChromeDisabledLow: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                     _type.HRESULT]
    get_ChromeHigh: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                              _type.HRESULT]
    put_ChromeHigh: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                              _type.HRESULT]
    get_ChromeLow: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                             _type.HRESULT]
    put_ChromeLow: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    get_ChromeMedium: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                _type.HRESULT]
    put_ChromeMedium: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                _type.HRESULT]
    get_ChromeMediumLow: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                   _type.HRESULT]
    put_ChromeMediumLow: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                   _type.HRESULT]
    get_ChromeWhite: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                               _type.HRESULT]
    put_ChromeWhite: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                               _type.HRESULT]
    get_ChromeGray: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                              _type.HRESULT]
    put_ChromeGray: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                              _type.HRESULT]
    get_ListLow: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                           _type.HRESULT]
    put_ListLow: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                           _type.HRESULT]
    get_ListMedium: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                              _type.HRESULT]
    put_ListMedium: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                              _type.HRESULT]
    get_ErrorText: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                             _type.HRESULT]
    put_ErrorText: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    get_Accent: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                          _type.HRESULT]
    put_Accent: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                          _type.HRESULT]


class IColorPaletteResourcesFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IColorPaletteResources]],  # value
                              _type.HRESULT]


class ICornerRadiusHelper(_inspectable.IInspectable):
    pass


class ICornerRadiusHelperStatics(_inspectable.IInspectable, factory=True):
    FromRadii: _Callable[[_type.DOUBLE,  # topLeft
                          _type.DOUBLE,  # topRight
                          _type.DOUBLE,  # bottomRight
                          _type.DOUBLE,  # bottomLeft
                          _Pointer[_struct.Windows.UI.Xaml.CornerRadius]],  # result
                         _type.HRESULT]
    FromUniformRadius: _Callable[[_type.DOUBLE,  # uniformRadius
                                  _Pointer[_struct.Windows.UI.Xaml.CornerRadius]],  # result
                                 _type.HRESULT]


class IDataContextChangedEventArgs(_inspectable.IInspectable):
    get_NewValue: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                            _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class IDataTemplate(_inspectable.IInspectable):
    LoadContent: _Callable[[_Pointer[IDependencyObject]],  # result
                           _type.HRESULT]


class IDataTemplateExtension(_inspectable.IInspectable):
    ResetTemplate: _Callable[[],
                             _type.HRESULT]
    ProcessBinding: _Callable[[_type.UINT32,  # phase
                               _Pointer[_type.boolean]],  # result
                              _type.HRESULT]
    ProcessBindings: _Callable[[_Windows_UI_Xaml_Controls.IContainerContentChangingEventArgs,  # arg
                                _Pointer[_type.INT32]],  # result
                               _type.HRESULT]


class IDataTemplateFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IDataTemplate]],  # value
                              _type.HRESULT]


class IDataTemplateKey(_inspectable.IInspectable):
    get_DataType: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                            _type.HRESULT]
    put_DataType: _Callable[[_inspectable.IInspectable],  # value
                            _type.HRESULT]


class IDataTemplateKeyFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IDataTemplateKey]],  # value
                              _type.HRESULT]
    CreateInstanceWithType: _Callable[[_inspectable.IInspectable,  # dataType
                                       _inspectable.IInspectable,  # baseInterface
                                       _Pointer[_inspectable.IInspectable],  # innerInterface
                                       _Pointer[IDataTemplateKey]],  # value
                                      _type.HRESULT]


class IDataTemplateStatics2(_inspectable.IInspectable, factory=True):
    get_ExtensionInstanceProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                             _type.HRESULT]
    GetExtensionInstance: _Callable[[IFrameworkElement,  # element
                                     _Pointer[IDataTemplateExtension]],  # result
                                    _type.HRESULT]
    SetExtensionInstance: _Callable[[IFrameworkElement,  # element
                                     IDataTemplateExtension],  # value
                                    _type.HRESULT]


class IDebugSettings(_inspectable.IInspectable):
    get_EnableFrameRateCounter: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_EnableFrameRateCounter: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    get_IsBindingTracingEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    put_IsBindingTracingEnabled: _Callable[[_type.boolean],  # value
                                           _type.HRESULT]
    get_IsOverdrawHeatMapEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_IsOverdrawHeatMapEnabled: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]
    add_BindingFailed: _Callable[[IBindingFailedEventHandler,  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_BindingFailed: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]


class IDebugSettings2(_inspectable.IInspectable):
    get_EnableRedrawRegions: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_EnableRedrawRegions: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]


class IDebugSettings3(_inspectable.IInspectable):
    get_IsTextPerformanceVisualizationEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                         _type.HRESULT]
    put_IsTextPerformanceVisualizationEnabled: _Callable[[_type.boolean],  # value
                                                         _type.HRESULT]


class IDebugSettings4(_inspectable.IInspectable):
    get_FailFastOnErrors: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_FailFastOnErrors: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]


class IDependencyObject(_inspectable.IInspectable):
    GetValue: _Callable[[IDependencyProperty,  # dp
                         _Pointer[_inspectable.IInspectable]],  # result
                        _type.HRESULT]
    SetValue: _Callable[[IDependencyProperty,  # dp
                         _inspectable.IInspectable],  # value
                        _type.HRESULT]
    ClearValue: _Callable[[IDependencyProperty],  # dp
                          _type.HRESULT]
    ReadLocalValue: _Callable[[IDependencyProperty,  # dp
                               _Pointer[_inspectable.IInspectable]],  # result
                              _type.HRESULT]
    GetAnimationBaseValue: _Callable[[IDependencyProperty,  # dp
                                      _Pointer[_inspectable.IInspectable]],  # result
                                     _type.HRESULT]
    get_Dispatcher: _Callable[[_Pointer[_Windows_UI_Core.ICoreDispatcher]],  # value
                              _type.HRESULT]


class IDependencyObject2(_inspectable.IInspectable):
    RegisterPropertyChangedCallback: _Callable[[IDependencyProperty,  # dp
                                                IDependencyPropertyChangedCallback,  # callback
                                                _Pointer[_type.INT64]],  # result
                                               _type.HRESULT]
    UnregisterPropertyChangedCallback: _Callable[[IDependencyProperty,  # dp
                                                  _type.INT64],  # token
                                                 _type.HRESULT]


class IDependencyObjectCollectionFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[_Windows_Foundation_Collections.IObservableVector[IDependencyObject]]],  # value
                              _type.HRESULT]


class IDependencyObjectFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IDependencyObject]],  # value
                              _type.HRESULT]


class IDependencyProperty(_inspectable.IInspectable):
    GetMetadata: _Callable[[_struct.Windows.UI.Xaml.Interop.TypeName,  # forType
                            _Pointer[IPropertyMetadata]],  # result
                           _type.HRESULT]


class IDependencyPropertyChangedEventArgs(_inspectable.IInspectable):
    get_Property: _Callable[[_Pointer[IDependencyProperty]],  # value
                            _type.HRESULT]
    get_OldValue: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                            _type.HRESULT]
    get_NewValue: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                            _type.HRESULT]


class IDependencyPropertyStatics(_inspectable.IInspectable, factory=True):
    get_UnsetValue: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                              _type.HRESULT]
    Register: _Callable[[_type.HSTRING,  # name
                         _struct.Windows.UI.Xaml.Interop.TypeName,  # propertyType
                         _struct.Windows.UI.Xaml.Interop.TypeName,  # ownerType
                         IPropertyMetadata,  # typeMetadata
                         _Pointer[IDependencyProperty]],  # result
                        _type.HRESULT]
    RegisterAttached: _Callable[[_type.HSTRING,  # name
                                 _struct.Windows.UI.Xaml.Interop.TypeName,  # propertyType
                                 _struct.Windows.UI.Xaml.Interop.TypeName,  # ownerType
                                 IPropertyMetadata,  # defaultMetadata
                                 _Pointer[IDependencyProperty]],  # result
                                _type.HRESULT]


class IDispatcherTimer(_inspectable.IInspectable):
    get_Interval: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    put_Interval: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                            _type.HRESULT]
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    add_Tick: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                         _Pointer[_struct.EventRegistrationToken]],  # token
                        _type.HRESULT]
    remove_Tick: _Callable[[_struct.EventRegistrationToken],  # token
                           _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]


class IDispatcherTimerFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IDispatcherTimer]],  # value
                              _type.HRESULT]


class IDragEventArgs(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_Data: _Callable[[_Pointer[_Windows_ApplicationModel_DataTransfer.IDataPackage]],  # value
                        _type.HRESULT]
    put_Data: _Callable[[_Windows_ApplicationModel_DataTransfer.IDataPackage],  # value
                        _type.HRESULT]
    GetPosition: _Callable[[IUIElement,  # relativeTo
                            _Pointer[_struct.Windows.Foundation.Point]],  # result
                           _type.HRESULT]


class IDragEventArgs2(_inspectable.IInspectable):
    get_DataView: _Callable[[_Pointer[_Windows_ApplicationModel_DataTransfer.IDataPackageView]],  # value
                            _type.HRESULT]
    get_DragUIOverride: _Callable[[_Pointer[IDragUIOverride]],  # value
                                  _type.HRESULT]
    get_Modifiers: _Callable[[_Pointer[_enum.Windows.ApplicationModel.DataTransfer.DragDrop.DragDropModifiers]],  # value
                             _type.HRESULT]
    get_AcceptedOperation: _Callable[[_Pointer[_enum.Windows.ApplicationModel.DataTransfer.DataPackageOperation]],  # value
                                     _type.HRESULT]
    put_AcceptedOperation: _Callable[[_enum.Windows.ApplicationModel.DataTransfer.DataPackageOperation],  # value
                                     _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[IDragOperationDeferral]],  # result
                           _type.HRESULT]


class IDragEventArgs3(_inspectable.IInspectable):
    get_AllowedOperations: _Callable[[_Pointer[_enum.Windows.ApplicationModel.DataTransfer.DataPackageOperation]],  # value
                                     _type.HRESULT]


class IDragOperationDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class IDragStartingEventArgs(_inspectable.IInspectable):
    get_Cancel: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_Cancel: _Callable[[_type.boolean],  # value
                          _type.HRESULT]
    get_Data: _Callable[[_Pointer[_Windows_ApplicationModel_DataTransfer.IDataPackage]],  # value
                        _type.HRESULT]
    get_DragUI: _Callable[[_Pointer[IDragUI]],  # value
                          _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[IDragOperationDeferral]],  # result
                           _type.HRESULT]
    GetPosition: _Callable[[IUIElement,  # relativeTo
                            _Pointer[_struct.Windows.Foundation.Point]],  # result
                           _type.HRESULT]


class IDragStartingEventArgs2(_inspectable.IInspectable):
    get_AllowedOperations: _Callable[[_Pointer[_enum.Windows.ApplicationModel.DataTransfer.DataPackageOperation]],  # value
                                     _type.HRESULT]
    put_AllowedOperations: _Callable[[_enum.Windows.ApplicationModel.DataTransfer.DataPackageOperation],  # value
                                     _type.HRESULT]


class IDragUI(_inspectable.IInspectable):
    SetContentFromBitmapImage: _Callable[[_Windows_UI_Xaml_Media_Imaging.IBitmapImage],  # bitmapImage
                                         _type.HRESULT]
    SetContentFromBitmapImageWithAnchorPoint: _Callable[[_Windows_UI_Xaml_Media_Imaging.IBitmapImage,  # bitmapImage
                                                         _struct.Windows.Foundation.Point],  # anchorPoint
                                                        _type.HRESULT]
    SetContentFromSoftwareBitmap: _Callable[[_Windows_Graphics_Imaging.ISoftwareBitmap],  # softwareBitmap
                                            _type.HRESULT]
    SetContentFromSoftwareBitmapWithAnchorPoint: _Callable[[_Windows_Graphics_Imaging.ISoftwareBitmap,  # softwareBitmap
                                                            _struct.Windows.Foundation.Point],  # anchorPoint
                                                           _type.HRESULT]
    SetContentFromDataPackage: _Callable[[],
                                         _type.HRESULT]


class IDragUIOverride(_inspectable.IInspectable):
    get_Caption: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    put_Caption: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    get_IsContentVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_IsContentVisible: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_IsCaptionVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_IsCaptionVisible: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_IsGlyphVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    put_IsGlyphVisible: _Callable[[_type.boolean],  # value
                                  _type.HRESULT]
    Clear: _Callable[[],
                     _type.HRESULT]
    SetContentFromBitmapImage: _Callable[[_Windows_UI_Xaml_Media_Imaging.IBitmapImage],  # bitmapImage
                                         _type.HRESULT]
    SetContentFromBitmapImageWithAnchorPoint: _Callable[[_Windows_UI_Xaml_Media_Imaging.IBitmapImage,  # bitmapImage
                                                         _struct.Windows.Foundation.Point],  # anchorPoint
                                                        _type.HRESULT]
    SetContentFromSoftwareBitmap: _Callable[[_Windows_Graphics_Imaging.ISoftwareBitmap],  # softwareBitmap
                                            _type.HRESULT]
    SetContentFromSoftwareBitmapWithAnchorPoint: _Callable[[_Windows_Graphics_Imaging.ISoftwareBitmap,  # softwareBitmap
                                                            _struct.Windows.Foundation.Point],  # anchorPoint
                                                           _type.HRESULT]


class IDropCompletedEventArgs(_inspectable.IInspectable):
    get_DropResult: _Callable[[_Pointer[_enum.Windows.ApplicationModel.DataTransfer.DataPackageOperation]],  # value
                              _type.HRESULT]


class IDurationHelper(_inspectable.IInspectable):
    pass


class IDurationHelperStatics(_inspectable.IInspectable, factory=True):
    get_Automatic: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Duration]],  # value
                             _type.HRESULT]
    get_Forever: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Duration]],  # value
                           _type.HRESULT]
    Compare: _Callable[[_struct.Windows.UI.Xaml.Duration,  # duration1
                        _struct.Windows.UI.Xaml.Duration,  # duration2
                        _Pointer[_type.INT32]],  # result
                       _type.HRESULT]
    FromTimeSpan: _Callable[[_struct.Windows.Foundation.TimeSpan,  # timeSpan
                             _Pointer[_struct.Windows.UI.Xaml.Duration]],  # result
                            _type.HRESULT]
    GetHasTimeSpan: _Callable[[_struct.Windows.UI.Xaml.Duration,  # target
                               _Pointer[_type.boolean]],  # result
                              _type.HRESULT]
    Add: _Callable[[_struct.Windows.UI.Xaml.Duration,  # target
                    _struct.Windows.UI.Xaml.Duration,  # duration
                    _Pointer[_struct.Windows.UI.Xaml.Duration]],  # result
                   _type.HRESULT]
    Equals: _Callable[[_struct.Windows.UI.Xaml.Duration,  # target
                       _struct.Windows.UI.Xaml.Duration,  # value
                       _Pointer[_type.boolean]],  # result
                      _type.HRESULT]
    Subtract: _Callable[[_struct.Windows.UI.Xaml.Duration,  # target
                         _struct.Windows.UI.Xaml.Duration,  # duration
                         _Pointer[_struct.Windows.UI.Xaml.Duration]],  # result
                        _type.HRESULT]


class IEffectiveViewportChangedEventArgs(_inspectable.IInspectable):
    get_EffectiveViewport: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                                     _type.HRESULT]
    get_MaxViewport: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                               _type.HRESULT]
    get_BringIntoViewDistanceX: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                          _type.HRESULT]
    get_BringIntoViewDistanceY: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                          _type.HRESULT]


class IElementFactory(_inspectable.IInspectable):
    GetElement: _Callable[[IElementFactoryGetArgs,  # args
                           _Pointer[IUIElement]],  # result
                          _type.HRESULT]
    RecycleElement: _Callable[[IElementFactoryRecycleArgs],  # args
                              _type.HRESULT]


class IElementFactoryGetArgs(_inspectable.IInspectable):
    get_Data: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                        _type.HRESULT]
    put_Data: _Callable[[_inspectable.IInspectable],  # value
                        _type.HRESULT]
    get_Parent: _Callable[[_Pointer[IUIElement]],  # value
                          _type.HRESULT]
    put_Parent: _Callable[[IUIElement],  # value
                          _type.HRESULT]


class IElementFactoryGetArgsFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IElementFactoryGetArgs]],  # value
                              _type.HRESULT]


class IElementFactoryRecycleArgs(_inspectable.IInspectable):
    get_Element: _Callable[[_Pointer[IUIElement]],  # value
                           _type.HRESULT]
    put_Element: _Callable[[IUIElement],  # value
                           _type.HRESULT]
    get_Parent: _Callable[[_Pointer[IUIElement]],  # value
                          _type.HRESULT]
    put_Parent: _Callable[[IUIElement],  # value
                          _type.HRESULT]


class IElementFactoryRecycleArgsFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IElementFactoryRecycleArgs]],  # value
                              _type.HRESULT]


class IElementSoundPlayer(_inspectable.IInspectable):
    pass


class IElementSoundPlayerStatics(_inspectable.IInspectable, factory=True):
    get_Volume: _Callable[[_Pointer[_type.DOUBLE]],  # value
                          _type.HRESULT]
    put_Volume: _Callable[[_type.DOUBLE],  # value
                          _type.HRESULT]
    get_State: _Callable[[_Pointer[_enum.Windows.UI.Xaml.ElementSoundPlayerState]],  # value
                         _type.HRESULT]
    put_State: _Callable[[_enum.Windows.UI.Xaml.ElementSoundPlayerState],  # value
                         _type.HRESULT]
    Play: _Callable[[_enum.Windows.UI.Xaml.ElementSoundKind],  # sound
                    _type.HRESULT]


class IElementSoundPlayerStatics2(_inspectable.IInspectable, factory=True):
    get_SpatialAudioMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.ElementSpatialAudioMode]],  # value
                                    _type.HRESULT]
    put_SpatialAudioMode: _Callable[[_enum.Windows.UI.Xaml.ElementSpatialAudioMode],  # value
                                    _type.HRESULT]


class IEventTrigger(_inspectable.IInspectable):
    get_RoutedEvent: _Callable[[_Pointer[IRoutedEvent]],  # value
                               _type.HRESULT]
    put_RoutedEvent: _Callable[[IRoutedEvent],  # value
                               _type.HRESULT]
    get_Actions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ITriggerAction]]],  # value
                           _type.HRESULT]


class IExceptionRoutedEventArgs(_inspectable.IInspectable):
    get_ErrorMessage: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]


class IExceptionRoutedEventArgsFactory(_inspectable.IInspectable):
    pass


class IFrameworkElement(_inspectable.IInspectable):
    get_Triggers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ITriggerBase]]],  # value
                            _type.HRESULT]
    get_Resources: _Callable[[_Pointer[IResourceDictionary]],  # value
                             _type.HRESULT]
    put_Resources: _Callable[[IResourceDictionary],  # value
                             _type.HRESULT]
    get_Tag: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                       _type.HRESULT]
    put_Tag: _Callable[[_inspectable.IInspectable],  # value
                       _type.HRESULT]
    get_Language: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_Language: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_ActualWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                               _type.HRESULT]
    get_ActualHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    get_Width: _Callable[[_Pointer[_type.DOUBLE]],  # value
                         _type.HRESULT]
    put_Width: _Callable[[_type.DOUBLE],  # value
                         _type.HRESULT]
    get_Height: _Callable[[_Pointer[_type.DOUBLE]],  # value
                          _type.HRESULT]
    put_Height: _Callable[[_type.DOUBLE],  # value
                          _type.HRESULT]
    get_MinWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                            _type.HRESULT]
    put_MinWidth: _Callable[[_type.DOUBLE],  # value
                            _type.HRESULT]
    get_MaxWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                            _type.HRESULT]
    put_MaxWidth: _Callable[[_type.DOUBLE],  # value
                            _type.HRESULT]
    get_MinHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                             _type.HRESULT]
    put_MinHeight: _Callable[[_type.DOUBLE],  # value
                             _type.HRESULT]
    get_MaxHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                             _type.HRESULT]
    put_MaxHeight: _Callable[[_type.DOUBLE],  # value
                             _type.HRESULT]
    get_HorizontalAlignment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.HorizontalAlignment]],  # value
                                       _type.HRESULT]
    put_HorizontalAlignment: _Callable[[_enum.Windows.UI.Xaml.HorizontalAlignment],  # value
                                       _type.HRESULT]
    get_VerticalAlignment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.VerticalAlignment]],  # value
                                     _type.HRESULT]
    put_VerticalAlignment: _Callable[[_enum.Windows.UI.Xaml.VerticalAlignment],  # value
                                     _type.HRESULT]
    get_Margin: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                          _type.HRESULT]
    put_Margin: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                          _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Name: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_BaseUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                           _type.HRESULT]
    get_DataContext: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                               _type.HRESULT]
    put_DataContext: _Callable[[_inspectable.IInspectable],  # value
                               _type.HRESULT]
    get_Style: _Callable[[_Pointer[IStyle]],  # value
                         _type.HRESULT]
    put_Style: _Callable[[IStyle],  # value
                         _type.HRESULT]
    get_Parent: _Callable[[_Pointer[IDependencyObject]],  # value
                          _type.HRESULT]
    get_FlowDirection: _Callable[[_Pointer[_enum.Windows.UI.Xaml.FlowDirection]],  # value
                                 _type.HRESULT]
    put_FlowDirection: _Callable[[_enum.Windows.UI.Xaml.FlowDirection],  # value
                                 _type.HRESULT]
    add_Loaded: _Callable[[IRoutedEventHandler,  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Loaded: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    add_Unloaded: _Callable[[IRoutedEventHandler,  # handler
                             _Pointer[_struct.EventRegistrationToken]],  # token
                            _type.HRESULT]
    remove_Unloaded: _Callable[[_struct.EventRegistrationToken],  # token
                               _type.HRESULT]
    add_SizeChanged: _Callable[[ISizeChangedEventHandler,  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_SizeChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    add_LayoutUpdated: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_LayoutUpdated: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    FindName: _Callable[[_type.HSTRING,  # name
                         _Pointer[_inspectable.IInspectable]],  # result
                        _type.HRESULT]
    SetBinding: _Callable[[IDependencyProperty,  # dp
                           _Windows_UI_Xaml_Data.IBindingBase],  # binding
                          _type.HRESULT]


class IFrameworkElement2(_inspectable.IInspectable):
    get_RequestedTheme: _Callable[[_Pointer[_enum.Windows.UI.Xaml.ElementTheme]],  # value
                                  _type.HRESULT]
    put_RequestedTheme: _Callable[[_enum.Windows.UI.Xaml.ElementTheme],  # value
                                  _type.HRESULT]
    add_DataContextChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IFrameworkElement, IDataContextChangedEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_DataContextChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    GetBindingExpression: _Callable[[IDependencyProperty,  # dp
                                     _Pointer[_Windows_UI_Xaml_Data.IBindingExpression]],  # result
                                    _type.HRESULT]


class IFrameworkElement3(_inspectable.IInspectable):
    add_Loading: _Callable[[_Windows_Foundation.ITypedEventHandler[IFrameworkElement, _inspectable.IInspectable],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Loading: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]


class IFrameworkElement4(_inspectable.IInspectable):
    get_AllowFocusOnInteraction: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    put_AllowFocusOnInteraction: _Callable[[_type.boolean],  # value
                                           _type.HRESULT]
    get_FocusVisualMargin: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                                     _type.HRESULT]
    put_FocusVisualMargin: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                                     _type.HRESULT]
    get_FocusVisualSecondaryThickness: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                                                 _type.HRESULT]
    put_FocusVisualSecondaryThickness: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                                                 _type.HRESULT]
    get_FocusVisualPrimaryThickness: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                                               _type.HRESULT]
    put_FocusVisualPrimaryThickness: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                                               _type.HRESULT]
    get_FocusVisualSecondaryBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                             _type.HRESULT]
    put_FocusVisualSecondaryBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                             _type.HRESULT]
    get_FocusVisualPrimaryBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                           _type.HRESULT]
    put_FocusVisualPrimaryBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                           _type.HRESULT]
    get_AllowFocusWhenDisabled: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_AllowFocusWhenDisabled: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]


class IFrameworkElement6(_inspectable.IInspectable):
    get_ActualTheme: _Callable[[_Pointer[_enum.Windows.UI.Xaml.ElementTheme]],  # value
                               _type.HRESULT]
    add_ActualThemeChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IFrameworkElement, _inspectable.IInspectable],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_ActualThemeChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]


class IFrameworkElement7(_inspectable.IInspectable):
    get_IsLoaded: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    add_EffectiveViewportChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IFrameworkElement, IEffectiveViewportChangedEventArgs],  # handler
                                             _Pointer[_struct.EventRegistrationToken]],  # token
                                            _type.HRESULT]
    remove_EffectiveViewportChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                               _type.HRESULT]


class IFrameworkElementFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IFrameworkElement]],  # value
                              _type.HRESULT]


class IFrameworkElementOverrides(_inspectable.IInspectable):
    MeasureOverride: _Callable[[_struct.Windows.Foundation.Size,  # availableSize
                                _Pointer[_struct.Windows.Foundation.Size]],  # result
                               _type.HRESULT]
    ArrangeOverride: _Callable[[_struct.Windows.Foundation.Size,  # finalSize
                                _Pointer[_struct.Windows.Foundation.Size]],  # result
                               _type.HRESULT]
    OnApplyTemplate: _Callable[[],
                               _type.HRESULT]


class IFrameworkElementOverrides2(_inspectable.IInspectable):
    GoToElementStateCore: _Callable[[_type.HSTRING,  # stateName
                                     _type.boolean,  # useTransitions
                                     _Pointer[_type.boolean]],  # result
                                    _type.HRESULT]


class IFrameworkElementProtected7(_inspectable.IInspectable):
    InvalidateViewport: _Callable[[],
                                  _type.HRESULT]


class IFrameworkElementStatics(_inspectable.IInspectable, factory=True):
    get_TagProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                               _type.HRESULT]
    get_LanguageProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_ActualWidthProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_ActualHeightProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_WidthProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_HeightProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_MinWidthProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_MaxWidthProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_MinHeightProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_MaxHeightProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_HorizontalAlignmentProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_VerticalAlignmentProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_MarginProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_NameProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                _type.HRESULT]
    get_DataContextProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_StyleProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_FlowDirectionProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                         _type.HRESULT]


class IFrameworkElementStatics2(_inspectable.IInspectable, factory=True):
    get_RequestedThemeProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                          _type.HRESULT]


class IFrameworkElementStatics4(_inspectable.IInspectable, factory=True):
    get_AllowFocusOnInteractionProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_FocusVisualMarginProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_FocusVisualSecondaryThicknessProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                                         _type.HRESULT]
    get_FocusVisualPrimaryThicknessProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                                       _type.HRESULT]
    get_FocusVisualSecondaryBrushProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                                     _type.HRESULT]
    get_FocusVisualPrimaryBrushProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_AllowFocusWhenDisabledProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                                  _type.HRESULT]


class IFrameworkElementStatics5(_inspectable.IInspectable, factory=True):
    DeferTree: _Callable[[IDependencyObject],  # element
                         _type.HRESULT]


class IFrameworkElementStatics6(_inspectable.IInspectable, factory=True):
    get_ActualThemeProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                       _type.HRESULT]


class IFrameworkTemplate(_inspectable.IInspectable):
    pass


class IFrameworkTemplateFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IFrameworkTemplate]],  # value
                              _type.HRESULT]


class IFrameworkView(_inspectable.IInspectable):
    pass


class IFrameworkViewSource(_inspectable.IInspectable):
    pass


class IGridLengthHelper(_inspectable.IInspectable):
    pass


class IGridLengthHelperStatics(_inspectable.IInspectable, factory=True):
    get_Auto: _Callable[[_Pointer[_struct.Windows.UI.Xaml.GridLength]],  # value
                        _type.HRESULT]
    FromPixels: _Callable[[_type.DOUBLE,  # pixels
                           _Pointer[_struct.Windows.UI.Xaml.GridLength]],  # result
                          _type.HRESULT]
    FromValueAndType: _Callable[[_type.DOUBLE,  # value
                                 _enum.Windows.UI.Xaml.GridUnitType,  # type
                                 _Pointer[_struct.Windows.UI.Xaml.GridLength]],  # result
                                _type.HRESULT]
    GetIsAbsolute: _Callable[[_struct.Windows.UI.Xaml.GridLength,  # target
                              _Pointer[_type.boolean]],  # result
                             _type.HRESULT]
    GetIsAuto: _Callable[[_struct.Windows.UI.Xaml.GridLength,  # target
                          _Pointer[_type.boolean]],  # result
                         _type.HRESULT]
    GetIsStar: _Callable[[_struct.Windows.UI.Xaml.GridLength,  # target
                          _Pointer[_type.boolean]],  # result
                         _type.HRESULT]
    Equals: _Callable[[_struct.Windows.UI.Xaml.GridLength,  # target
                       _struct.Windows.UI.Xaml.GridLength,  # value
                       _Pointer[_type.boolean]],  # result
                      _type.HRESULT]


class IMediaFailedRoutedEventArgs(_inspectable.IInspectable):
    get_ErrorTrace: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]


class IPointHelper(_inspectable.IInspectable):
    pass


class IPointHelperStatics(_inspectable.IInspectable, factory=True):
    FromCoordinates: _Callable[[_type.FLOAT,  # x
                                _type.FLOAT,  # y
                                _Pointer[_struct.Windows.Foundation.Point]],  # result
                               _type.HRESULT]


class IPropertyMetadata(_inspectable.IInspectable):
    get_DefaultValue: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                _type.HRESULT]
    get_CreateDefaultValueCallback: _Callable[[_Pointer[ICreateDefaultValueCallback]],  # value
                                              _type.HRESULT]


class IPropertyMetadataFactory(_inspectable.IInspectable):
    CreateInstanceWithDefaultValue: _Callable[[_inspectable.IInspectable,  # defaultValue
                                               _inspectable.IInspectable,  # baseInterface
                                               _Pointer[_inspectable.IInspectable],  # innerInterface
                                               _Pointer[IPropertyMetadata]],  # value
                                              _type.HRESULT]
    CreateInstanceWithDefaultValueAndCallback: _Callable[[_inspectable.IInspectable,  # defaultValue
                                                          IPropertyChangedCallback,  # propertyChangedCallback
                                                          _inspectable.IInspectable,  # baseInterface
                                                          _Pointer[_inspectable.IInspectable],  # innerInterface
                                                          _Pointer[IPropertyMetadata]],  # value
                                                         _type.HRESULT]


class IPropertyMetadataStatics(_inspectable.IInspectable, factory=True):
    CreateWithDefaultValue: _Callable[[_inspectable.IInspectable,  # defaultValue
                                       _Pointer[IPropertyMetadata]],  # result
                                      _type.HRESULT]
    CreateWithDefaultValueAndCallback: _Callable[[_inspectable.IInspectable,  # defaultValue
                                                  IPropertyChangedCallback,  # propertyChangedCallback
                                                  _Pointer[IPropertyMetadata]],  # result
                                                 _type.HRESULT]
    CreateWithFactory: _Callable[[ICreateDefaultValueCallback,  # createDefaultValueCallback
                                  _Pointer[IPropertyMetadata]],  # result
                                 _type.HRESULT]
    CreateWithFactoryAndCallback: _Callable[[ICreateDefaultValueCallback,  # createDefaultValueCallback
                                             IPropertyChangedCallback,  # propertyChangedCallback
                                             _Pointer[IPropertyMetadata]],  # result
                                            _type.HRESULT]


class IPropertyPath(_inspectable.IInspectable):
    get_Path: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class IPropertyPathFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[_type.HSTRING,  # path
                               _Pointer[IPropertyPath]],  # value
                              _type.HRESULT]


class IRectHelper(_inspectable.IInspectable):
    pass


class IRectHelperStatics(_inspectable.IInspectable, factory=True):
    get_Empty: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                         _type.HRESULT]
    FromCoordinatesAndDimensions: _Callable[[_type.FLOAT,  # x
                                             _type.FLOAT,  # y
                                             _type.FLOAT,  # width
                                             _type.FLOAT,  # height
                                             _Pointer[_struct.Windows.Foundation.Rect]],  # result
                                            _type.HRESULT]
    FromPoints: _Callable[[_struct.Windows.Foundation.Point,  # point1
                           _struct.Windows.Foundation.Point,  # point2
                           _Pointer[_struct.Windows.Foundation.Rect]],  # result
                          _type.HRESULT]
    FromLocationAndSize: _Callable[[_struct.Windows.Foundation.Point,  # location
                                    _struct.Windows.Foundation.Size,  # size
                                    _Pointer[_struct.Windows.Foundation.Rect]],  # result
                                   _type.HRESULT]
    GetIsEmpty: _Callable[[_struct.Windows.Foundation.Rect,  # target
                           _Pointer[_type.boolean]],  # result
                          _type.HRESULT]
    GetBottom: _Callable[[_struct.Windows.Foundation.Rect,  # target
                          _Pointer[_type.FLOAT]],  # result
                         _type.HRESULT]
    GetLeft: _Callable[[_struct.Windows.Foundation.Rect,  # target
                        _Pointer[_type.FLOAT]],  # result
                       _type.HRESULT]
    GetRight: _Callable[[_struct.Windows.Foundation.Rect,  # target
                         _Pointer[_type.FLOAT]],  # result
                        _type.HRESULT]
    GetTop: _Callable[[_struct.Windows.Foundation.Rect,  # target
                       _Pointer[_type.FLOAT]],  # result
                      _type.HRESULT]
    Contains: _Callable[[_struct.Windows.Foundation.Rect,  # target
                         _struct.Windows.Foundation.Point,  # point
                         _Pointer[_type.boolean]],  # result
                        _type.HRESULT]
    Equals: _Callable[[_struct.Windows.Foundation.Rect,  # target
                       _struct.Windows.Foundation.Rect,  # value
                       _Pointer[_type.boolean]],  # result
                      _type.HRESULT]
    Intersect: _Callable[[_struct.Windows.Foundation.Rect,  # target
                          _struct.Windows.Foundation.Rect,  # rect
                          _Pointer[_struct.Windows.Foundation.Rect]],  # result
                         _type.HRESULT]
    UnionWithPoint: _Callable[[_struct.Windows.Foundation.Rect,  # target
                               _struct.Windows.Foundation.Point,  # point
                               _Pointer[_struct.Windows.Foundation.Rect]],  # result
                              _type.HRESULT]
    UnionWithRect: _Callable[[_struct.Windows.Foundation.Rect,  # target
                              _struct.Windows.Foundation.Rect,  # rect
                              _Pointer[_struct.Windows.Foundation.Rect]],  # result
                             _type.HRESULT]


class IResourceDictionary(_inspectable.IInspectable):
    get_Source: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                          _type.HRESULT]
    put_Source: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                          _type.HRESULT]
    get_MergedDictionaries: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IResourceDictionary]]],  # value
                                      _type.HRESULT]
    get_ThemeDictionaries: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_inspectable.IInspectable, _inspectable.IInspectable]]],  # value
                                     _type.HRESULT]


class IResourceDictionaryFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IResourceDictionary]],  # value
                              _type.HRESULT]


class IRoutedEvent(_inspectable.IInspectable):
    pass


class IRoutedEventArgs(_inspectable.IInspectable):
    get_OriginalSource: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                  _type.HRESULT]


class IRoutedEventArgsFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IRoutedEventArgs]],  # value
                              _type.HRESULT]


class IScalarTransition(_inspectable.IInspectable):
    get_Duration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    put_Duration: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                            _type.HRESULT]


class IScalarTransitionFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IScalarTransition]],  # value
                              _type.HRESULT]


class ISetter(_inspectable.IInspectable):
    get_Property: _Callable[[_Pointer[IDependencyProperty]],  # value
                            _type.HRESULT]
    put_Property: _Callable[[IDependencyProperty],  # value
                            _type.HRESULT]
    get_Value: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                         _type.HRESULT]
    put_Value: _Callable[[_inspectable.IInspectable],  # value
                         _type.HRESULT]


class ISetter2(_inspectable.IInspectable):
    get_Target: _Callable[[_Pointer[ITargetPropertyPath]],  # value
                          _type.HRESULT]
    put_Target: _Callable[[ITargetPropertyPath],  # value
                          _type.HRESULT]


class ISetterBase(_inspectable.IInspectable):
    get_IsSealed: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]


class ISetterBaseCollection(_inspectable.IInspectable):
    get_IsSealed: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]


class ISetterBaseFactory(_inspectable.IInspectable):
    pass


class ISetterFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[IDependencyProperty,  # targetProperty
                               _inspectable.IInspectable,  # value
                               _Pointer[ISetter]],  # instance
                              _type.HRESULT]


class ISizeChangedEventArgs(_inspectable.IInspectable):
    get_PreviousSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                                _type.HRESULT]
    get_NewSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                           _type.HRESULT]


class ISizeHelper(_inspectable.IInspectable):
    pass


class ISizeHelperStatics(_inspectable.IInspectable, factory=True):
    get_Empty: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                         _type.HRESULT]
    FromDimensions: _Callable[[_type.FLOAT,  # width
                               _type.FLOAT,  # height
                               _Pointer[_struct.Windows.Foundation.Size]],  # result
                              _type.HRESULT]
    GetIsEmpty: _Callable[[_struct.Windows.Foundation.Size,  # target
                           _Pointer[_type.boolean]],  # result
                          _type.HRESULT]
    Equals: _Callable[[_struct.Windows.Foundation.Size,  # target
                       _struct.Windows.Foundation.Size,  # value
                       _Pointer[_type.boolean]],  # result
                      _type.HRESULT]


class IStateTrigger(_inspectable.IInspectable):
    get_IsActive: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    put_IsActive: _Callable[[_type.boolean],  # value
                            _type.HRESULT]


class IStateTriggerBase(_inspectable.IInspectable):
    pass


class IStateTriggerBaseFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IStateTriggerBase]],  # value
                              _type.HRESULT]


class IStateTriggerBaseProtected(_inspectable.IInspectable):
    SetActive: _Callable[[_type.boolean],  # IsActive
                         _type.HRESULT]


class IStateTriggerStatics(_inspectable.IInspectable, factory=True):
    get_IsActiveProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                    _type.HRESULT]


class IStyle(_inspectable.IInspectable):
    get_IsSealed: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_Setters: _Callable[[_Pointer[ISetterBaseCollection]],  # value
                           _type.HRESULT]
    get_TargetType: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Interop.TypeName]],  # value
                              _type.HRESULT]
    put_TargetType: _Callable[[_struct.Windows.UI.Xaml.Interop.TypeName],  # value
                              _type.HRESULT]
    get_BasedOn: _Callable[[_Pointer[IStyle]],  # value
                           _type.HRESULT]
    put_BasedOn: _Callable[[IStyle],  # value
                           _type.HRESULT]
    Seal: _Callable[[],
                    _type.HRESULT]


class IStyleFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[_struct.Windows.UI.Xaml.Interop.TypeName,  # targetType
                               _Pointer[IStyle]],  # value
                              _type.HRESULT]


class ITargetPropertyPath(_inspectable.IInspectable):
    get_Path: _Callable[[_Pointer[IPropertyPath]],  # value
                        _type.HRESULT]
    put_Path: _Callable[[IPropertyPath],  # value
                        _type.HRESULT]
    get_Target: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                          _type.HRESULT]
    put_Target: _Callable[[_inspectable.IInspectable],  # value
                          _type.HRESULT]


class ITargetPropertyPathFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[IDependencyProperty,  # targetProperty
                               _Pointer[ITargetPropertyPath]],  # value
                              _type.HRESULT]


class IThicknessHelper(_inspectable.IInspectable):
    pass


class IThicknessHelperStatics(_inspectable.IInspectable, factory=True):
    FromLengths: _Callable[[_type.DOUBLE,  # left
                            _type.DOUBLE,  # top
                            _type.DOUBLE,  # right
                            _type.DOUBLE,  # bottom
                            _Pointer[_struct.Windows.UI.Xaml.Thickness]],  # result
                           _type.HRESULT]
    FromUniformLength: _Callable[[_type.DOUBLE,  # uniformLength
                                  _Pointer[_struct.Windows.UI.Xaml.Thickness]],  # result
                                 _type.HRESULT]


class ITriggerAction(_inspectable.IInspectable):
    pass


class ITriggerActionFactory(_inspectable.IInspectable):
    pass


class ITriggerBase(_inspectable.IInspectable):
    pass


class ITriggerBaseFactory(_inspectable.IInspectable):
    pass


class IUIElement(_inspectable.IInspectable):
    get_DesiredSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                               _type.HRESULT]
    get_AllowDrop: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_AllowDrop: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    get_Opacity: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    put_Opacity: _Callable[[_type.DOUBLE],  # value
                           _type.HRESULT]
    get_Clip: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IRectangleGeometry]],  # value
                        _type.HRESULT]
    put_Clip: _Callable[[_Windows_UI_Xaml_Media.IRectangleGeometry],  # value
                        _type.HRESULT]
    get_RenderTransform: _Callable[[_Pointer[_Windows_UI_Xaml_Media.ITransform]],  # value
                                   _type.HRESULT]
    put_RenderTransform: _Callable[[_Windows_UI_Xaml_Media.ITransform],  # value
                                   _type.HRESULT]
    get_Projection: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IProjection]],  # value
                              _type.HRESULT]
    put_Projection: _Callable[[_Windows_UI_Xaml_Media.IProjection],  # value
                              _type.HRESULT]
    get_RenderTransformOrigin: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                                         _type.HRESULT]
    put_RenderTransformOrigin: _Callable[[_struct.Windows.Foundation.Point],  # value
                                         _type.HRESULT]
    get_IsHitTestVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_IsHitTestVisible: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_Visibility: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Visibility]],  # value
                              _type.HRESULT]
    put_Visibility: _Callable[[_enum.Windows.UI.Xaml.Visibility],  # value
                              _type.HRESULT]
    get_RenderSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                              _type.HRESULT]
    get_UseLayoutRounding: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    put_UseLayoutRounding: _Callable[[_type.boolean],  # value
                                     _type.HRESULT]
    get_Transitions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Media_Animation.ITransition]]],  # value
                               _type.HRESULT]
    put_Transitions: _Callable[[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Media_Animation.ITransition]],  # value
                               _type.HRESULT]
    get_CacheMode: _Callable[[_Pointer[_Windows_UI_Xaml_Media.ICacheMode]],  # value
                             _type.HRESULT]
    put_CacheMode: _Callable[[_Windows_UI_Xaml_Media.ICacheMode],  # value
                             _type.HRESULT]
    get_IsTapEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_IsTapEnabled: _Callable[[_type.boolean],  # value
                                _type.HRESULT]
    get_IsDoubleTapEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_IsDoubleTapEnabled: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    get_IsRightTapEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    put_IsRightTapEnabled: _Callable[[_type.boolean],  # value
                                     _type.HRESULT]
    get_IsHoldingEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_IsHoldingEnabled: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_ManipulationMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Input.ManipulationModes]],  # value
                                    _type.HRESULT]
    put_ManipulationMode: _Callable[[_enum.Windows.UI.Xaml.Input.ManipulationModes],  # value
                                    _type.HRESULT]
    get_PointerCaptures: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_UI_Xaml_Input.IPointer]]],  # value
                                   _type.HRESULT]
    add_KeyUp: _Callable[[_Windows_UI_Xaml_Input.IKeyEventHandler,  # handler
                          _Pointer[_struct.EventRegistrationToken]],  # token
                         _type.HRESULT]
    remove_KeyUp: _Callable[[_struct.EventRegistrationToken],  # token
                            _type.HRESULT]
    add_KeyDown: _Callable[[_Windows_UI_Xaml_Input.IKeyEventHandler,  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_KeyDown: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_GotFocus: _Callable[[IRoutedEventHandler,  # handler
                             _Pointer[_struct.EventRegistrationToken]],  # token
                            _type.HRESULT]
    remove_GotFocus: _Callable[[_struct.EventRegistrationToken],  # token
                               _type.HRESULT]
    add_LostFocus: _Callable[[IRoutedEventHandler,  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_LostFocus: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    add_DragEnter: _Callable[[IDragEventHandler,  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_DragEnter: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    add_DragLeave: _Callable[[IDragEventHandler,  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_DragLeave: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    add_DragOver: _Callable[[IDragEventHandler,  # handler
                             _Pointer[_struct.EventRegistrationToken]],  # token
                            _type.HRESULT]
    remove_DragOver: _Callable[[_struct.EventRegistrationToken],  # token
                               _type.HRESULT]
    add_Drop: _Callable[[IDragEventHandler,  # handler
                         _Pointer[_struct.EventRegistrationToken]],  # token
                        _type.HRESULT]
    remove_Drop: _Callable[[_struct.EventRegistrationToken],  # token
                           _type.HRESULT]
    add_PointerPressed: _Callable[[_Windows_UI_Xaml_Input.IPointerEventHandler,  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_PointerPressed: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_PointerMoved: _Callable[[_Windows_UI_Xaml_Input.IPointerEventHandler,  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_PointerMoved: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    add_PointerReleased: _Callable[[_Windows_UI_Xaml_Input.IPointerEventHandler,  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_PointerReleased: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    add_PointerEntered: _Callable[[_Windows_UI_Xaml_Input.IPointerEventHandler,  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_PointerEntered: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_PointerExited: _Callable[[_Windows_UI_Xaml_Input.IPointerEventHandler,  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_PointerExited: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_PointerCaptureLost: _Callable[[_Windows_UI_Xaml_Input.IPointerEventHandler,  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_PointerCaptureLost: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_PointerCanceled: _Callable[[_Windows_UI_Xaml_Input.IPointerEventHandler,  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_PointerCanceled: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    add_PointerWheelChanged: _Callable[[_Windows_UI_Xaml_Input.IPointerEventHandler,  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_PointerWheelChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_Tapped: _Callable[[_Windows_UI_Xaml_Input.ITappedEventHandler,  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Tapped: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    add_DoubleTapped: _Callable[[_Windows_UI_Xaml_Input.IDoubleTappedEventHandler,  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_DoubleTapped: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    add_Holding: _Callable[[_Windows_UI_Xaml_Input.IHoldingEventHandler,  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Holding: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_RightTapped: _Callable[[_Windows_UI_Xaml_Input.IRightTappedEventHandler,  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_RightTapped: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    add_ManipulationStarting: _Callable[[_Windows_UI_Xaml_Input.IManipulationStartingEventHandler,  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_ManipulationStarting: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    add_ManipulationInertiaStarting: _Callable[[_Windows_UI_Xaml_Input.IManipulationInertiaStartingEventHandler,  # handler
                                                _Pointer[_struct.EventRegistrationToken]],  # token
                                               _type.HRESULT]
    remove_ManipulationInertiaStarting: _Callable[[_struct.EventRegistrationToken],  # token
                                                  _type.HRESULT]
    add_ManipulationStarted: _Callable[[_Windows_UI_Xaml_Input.IManipulationStartedEventHandler,  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_ManipulationStarted: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_ManipulationDelta: _Callable[[_Windows_UI_Xaml_Input.IManipulationDeltaEventHandler,  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_ManipulationDelta: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    add_ManipulationCompleted: _Callable[[_Windows_UI_Xaml_Input.IManipulationCompletedEventHandler,  # handler
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_ManipulationCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]
    Measure: _Callable[[_struct.Windows.Foundation.Size],  # availableSize
                       _type.HRESULT]
    Arrange: _Callable[[_struct.Windows.Foundation.Rect],  # finalRect
                       _type.HRESULT]
    CapturePointer: _Callable[[_Windows_UI_Xaml_Input.IPointer,  # value
                               _Pointer[_type.boolean]],  # result
                              _type.HRESULT]
    ReleasePointerCapture: _Callable[[_Windows_UI_Xaml_Input.IPointer],  # value
                                     _type.HRESULT]
    ReleasePointerCaptures: _Callable[[],
                                      _type.HRESULT]
    AddHandler: _Callable[[IRoutedEvent,  # routedEvent
                           _inspectable.IInspectable,  # handler
                           _type.boolean],  # handledEventsToo
                          _type.HRESULT]
    RemoveHandler: _Callable[[IRoutedEvent,  # routedEvent
                              _inspectable.IInspectable],  # handler
                             _type.HRESULT]
    TransformToVisual: _Callable[[IUIElement,  # visual
                                  _Pointer[_Windows_UI_Xaml_Media.IGeneralTransform]],  # result
                                 _type.HRESULT]
    InvalidateMeasure: _Callable[[],
                                 _type.HRESULT]
    InvalidateArrange: _Callable[[],
                                 _type.HRESULT]
    UpdateLayout: _Callable[[],
                            _type.HRESULT]


class IUIElement10(_inspectable.IInspectable):
    get_ActualOffset: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                                _type.HRESULT]
    get_ActualSize: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                              _type.HRESULT]
    get_XamlRoot: _Callable[[_Pointer[IXamlRoot]],  # value
                            _type.HRESULT]
    put_XamlRoot: _Callable[[IXamlRoot],  # value
                            _type.HRESULT]
    get_UIContext: _Callable[[_Pointer[_Windows_UI.IUIContext]],  # value
                             _type.HRESULT]
    get_Shadow: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IShadow]],  # value
                          _type.HRESULT]
    put_Shadow: _Callable[[_Windows_UI_Xaml_Media.IShadow],  # value
                          _type.HRESULT]


class IUIElement2(_inspectable.IInspectable):
    get_CompositeMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Media.ElementCompositeMode]],  # value
                                 _type.HRESULT]
    put_CompositeMode: _Callable[[_enum.Windows.UI.Xaml.Media.ElementCompositeMode],  # value
                                 _type.HRESULT]
    CancelDirectManipulations: _Callable[[_Pointer[_type.boolean]],  # result
                                         _type.HRESULT]


class IUIElement3(_inspectable.IInspectable):
    get_Transform3D: _Callable[[_Pointer[_Windows_UI_Xaml_Media_Media3D.ITransform3D]],  # value
                               _type.HRESULT]
    put_Transform3D: _Callable[[_Windows_UI_Xaml_Media_Media3D.ITransform3D],  # value
                               _type.HRESULT]
    get_CanDrag: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_CanDrag: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    add_DragStarting: _Callable[[_Windows_Foundation.ITypedEventHandler[IUIElement, IDragStartingEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_DragStarting: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    add_DropCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IUIElement, IDropCompletedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_DropCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    StartDragAsync: _Callable[[_Windows_UI_Input.IPointerPoint,  # pointerPoint
                               _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.DataTransfer.DataPackageOperation]]],  # operation
                              _type.HRESULT]


class IUIElement4(_inspectable.IInspectable):
    get_ContextFlyout: _Callable[[_Pointer[_Windows_UI_Xaml_Controls_Primitives.IFlyoutBase]],  # value
                                 _type.HRESULT]
    put_ContextFlyout: _Callable[[_Windows_UI_Xaml_Controls_Primitives.IFlyoutBase],  # value
                                 _type.HRESULT]
    get_ExitDisplayModeOnAccessKeyInvoked: _Callable[[_Pointer[_type.boolean]],  # value
                                                     _type.HRESULT]
    put_ExitDisplayModeOnAccessKeyInvoked: _Callable[[_type.boolean],  # value
                                                     _type.HRESULT]
    get_IsAccessKeyScope: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_IsAccessKeyScope: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_AccessKeyScopeOwner: _Callable[[_Pointer[IDependencyObject]],  # value
                                       _type.HRESULT]
    put_AccessKeyScopeOwner: _Callable[[IDependencyObject],  # value
                                       _type.HRESULT]
    get_AccessKey: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_AccessKey: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    add_ContextRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IUIElement, _Windows_UI_Xaml_Input.IContextRequestedEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_ContextRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    add_ContextCanceled: _Callable[[_Windows_Foundation.ITypedEventHandler[IUIElement, IRoutedEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_ContextCanceled: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    add_AccessKeyDisplayRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IUIElement, _Windows_UI_Xaml_Input.IAccessKeyDisplayRequestedEventArgs],  # handler
                                              _Pointer[_struct.EventRegistrationToken]],  # token
                                             _type.HRESULT]
    remove_AccessKeyDisplayRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                _type.HRESULT]
    add_AccessKeyDisplayDismissed: _Callable[[_Windows_Foundation.ITypedEventHandler[IUIElement, _Windows_UI_Xaml_Input.IAccessKeyDisplayDismissedEventArgs],  # handler
                                              _Pointer[_struct.EventRegistrationToken]],  # token
                                             _type.HRESULT]
    remove_AccessKeyDisplayDismissed: _Callable[[_struct.EventRegistrationToken],  # token
                                                _type.HRESULT]
    add_AccessKeyInvoked: _Callable[[_Windows_Foundation.ITypedEventHandler[IUIElement, _Windows_UI_Xaml_Input.IAccessKeyInvokedEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_AccessKeyInvoked: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]


class IUIElement5(_inspectable.IInspectable):
    get_Lights: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Media.IXamlLight]]],  # value
                          _type.HRESULT]
    get_KeyTipPlacementMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Input.KeyTipPlacementMode]],  # value
                                       _type.HRESULT]
    put_KeyTipPlacementMode: _Callable[[_enum.Windows.UI.Xaml.Input.KeyTipPlacementMode],  # value
                                       _type.HRESULT]
    get_KeyTipHorizontalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                          _type.HRESULT]
    put_KeyTipHorizontalOffset: _Callable[[_type.DOUBLE],  # value
                                          _type.HRESULT]
    get_KeyTipVerticalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                        _type.HRESULT]
    put_KeyTipVerticalOffset: _Callable[[_type.DOUBLE],  # value
                                        _type.HRESULT]
    get_XYFocusKeyboardNavigation: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Input.XYFocusKeyboardNavigationMode]],  # value
                                             _type.HRESULT]
    put_XYFocusKeyboardNavigation: _Callable[[_enum.Windows.UI.Xaml.Input.XYFocusKeyboardNavigationMode],  # value
                                             _type.HRESULT]
    get_XYFocusUpNavigationStrategy: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Input.XYFocusNavigationStrategy]],  # value
                                               _type.HRESULT]
    put_XYFocusUpNavigationStrategy: _Callable[[_enum.Windows.UI.Xaml.Input.XYFocusNavigationStrategy],  # value
                                               _type.HRESULT]
    get_XYFocusDownNavigationStrategy: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Input.XYFocusNavigationStrategy]],  # value
                                                 _type.HRESULT]
    put_XYFocusDownNavigationStrategy: _Callable[[_enum.Windows.UI.Xaml.Input.XYFocusNavigationStrategy],  # value
                                                 _type.HRESULT]
    get_XYFocusLeftNavigationStrategy: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Input.XYFocusNavigationStrategy]],  # value
                                                 _type.HRESULT]
    put_XYFocusLeftNavigationStrategy: _Callable[[_enum.Windows.UI.Xaml.Input.XYFocusNavigationStrategy],  # value
                                                 _type.HRESULT]
    get_XYFocusRightNavigationStrategy: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Input.XYFocusNavigationStrategy]],  # value
                                                  _type.HRESULT]
    put_XYFocusRightNavigationStrategy: _Callable[[_enum.Windows.UI.Xaml.Input.XYFocusNavigationStrategy],  # value
                                                  _type.HRESULT]
    get_HighContrastAdjustment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.ElementHighContrastAdjustment]],  # value
                                          _type.HRESULT]
    put_HighContrastAdjustment: _Callable[[_enum.Windows.UI.Xaml.ElementHighContrastAdjustment],  # value
                                          _type.HRESULT]
    get_TabFocusNavigation: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Input.KeyboardNavigationMode]],  # value
                                      _type.HRESULT]
    put_TabFocusNavigation: _Callable[[_enum.Windows.UI.Xaml.Input.KeyboardNavigationMode],  # value
                                      _type.HRESULT]
    add_GettingFocus: _Callable[[_Windows_Foundation.ITypedEventHandler[IUIElement, _Windows_UI_Xaml_Input.IGettingFocusEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_GettingFocus: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    add_LosingFocus: _Callable[[_Windows_Foundation.ITypedEventHandler[IUIElement, _Windows_UI_Xaml_Input.ILosingFocusEventArgs],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_LosingFocus: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    add_NoFocusCandidateFound: _Callable[[_Windows_Foundation.ITypedEventHandler[IUIElement, _Windows_UI_Xaml_Input.INoFocusCandidateFoundEventArgs],  # handler
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_NoFocusCandidateFound: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]
    StartBringIntoView: _Callable[[],
                                  _type.HRESULT]
    StartBringIntoViewWithOptions: _Callable[[IBringIntoViewOptions],  # options
                                             _type.HRESULT]


class IUIElement7(_inspectable.IInspectable):
    get_KeyboardAccelerators: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Input.IKeyboardAccelerator]]],  # value
                                        _type.HRESULT]
    add_CharacterReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[IUIElement, _Windows_UI_Xaml_Input.ICharacterReceivedRoutedEventArgs],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_CharacterReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    add_ProcessKeyboardAccelerators: _Callable[[_Windows_Foundation.ITypedEventHandler[IUIElement, _Windows_UI_Xaml_Input.IProcessKeyboardAcceleratorEventArgs],  # handler
                                                _Pointer[_struct.EventRegistrationToken]],  # token
                                               _type.HRESULT]
    remove_ProcessKeyboardAccelerators: _Callable[[_struct.EventRegistrationToken],  # token
                                                  _type.HRESULT]
    add_PreviewKeyDown: _Callable[[_Windows_UI_Xaml_Input.IKeyEventHandler,  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_PreviewKeyDown: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_PreviewKeyUp: _Callable[[_Windows_UI_Xaml_Input.IKeyEventHandler,  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_PreviewKeyUp: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    TryInvokeKeyboardAccelerator: _Callable[[_Windows_UI_Xaml_Input.IProcessKeyboardAcceleratorEventArgs],  # args
                                            _type.HRESULT]


class IUIElement8(_inspectable.IInspectable):
    get_KeyTipTarget: _Callable[[_Pointer[IDependencyObject]],  # value
                                _type.HRESULT]
    put_KeyTipTarget: _Callable[[IDependencyObject],  # value
                                _type.HRESULT]
    get_KeyboardAcceleratorPlacementTarget: _Callable[[_Pointer[IDependencyObject]],  # value
                                                      _type.HRESULT]
    put_KeyboardAcceleratorPlacementTarget: _Callable[[IDependencyObject],  # value
                                                      _type.HRESULT]
    get_KeyboardAcceleratorPlacementMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Input.KeyboardAcceleratorPlacementMode]],  # value
                                                    _type.HRESULT]
    put_KeyboardAcceleratorPlacementMode: _Callable[[_enum.Windows.UI.Xaml.Input.KeyboardAcceleratorPlacementMode],  # value
                                                    _type.HRESULT]
    add_BringIntoViewRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IUIElement, IBringIntoViewRequestedEventArgs],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_BringIntoViewRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]


class IUIElement9(_inspectable.IInspectable):
    get_CanBeScrollAnchor: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    put_CanBeScrollAnchor: _Callable[[_type.boolean],  # value
                                     _type.HRESULT]
    get_OpacityTransition: _Callable[[_Pointer[IScalarTransition]],  # value
                                     _type.HRESULT]
    put_OpacityTransition: _Callable[[IScalarTransition],  # value
                                     _type.HRESULT]
    get_Translation: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                               _type.HRESULT]
    put_Translation: _Callable[[_struct.Windows.Foundation.Numerics.Vector3],  # value
                               _type.HRESULT]
    get_TranslationTransition: _Callable[[_Pointer[IVector3Transition]],  # value
                                         _type.HRESULT]
    put_TranslationTransition: _Callable[[IVector3Transition],  # value
                                         _type.HRESULT]
    get_Rotation: _Callable[[_Pointer[_type.FLOAT]],  # value
                            _type.HRESULT]
    put_Rotation: _Callable[[_type.FLOAT],  # value
                            _type.HRESULT]
    get_RotationTransition: _Callable[[_Pointer[IScalarTransition]],  # value
                                      _type.HRESULT]
    put_RotationTransition: _Callable[[IScalarTransition],  # value
                                      _type.HRESULT]
    get_Scale: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                         _type.HRESULT]
    put_Scale: _Callable[[_struct.Windows.Foundation.Numerics.Vector3],  # value
                         _type.HRESULT]
    get_ScaleTransition: _Callable[[_Pointer[IVector3Transition]],  # value
                                   _type.HRESULT]
    put_ScaleTransition: _Callable[[IVector3Transition],  # value
                                   _type.HRESULT]
    get_TransformMatrix: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Matrix4x4]],  # value
                                   _type.HRESULT]
    put_TransformMatrix: _Callable[[_struct.Windows.Foundation.Numerics.Matrix4x4],  # value
                                   _type.HRESULT]
    get_CenterPoint: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                               _type.HRESULT]
    put_CenterPoint: _Callable[[_struct.Windows.Foundation.Numerics.Vector3],  # value
                               _type.HRESULT]
    get_RotationAxis: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                                _type.HRESULT]
    put_RotationAxis: _Callable[[_struct.Windows.Foundation.Numerics.Vector3],  # value
                                _type.HRESULT]
    StartAnimation: _Callable[[_Windows_UI_Composition.ICompositionAnimationBase],  # animation
                              _type.HRESULT]
    StopAnimation: _Callable[[_Windows_UI_Composition.ICompositionAnimationBase],  # animation
                             _type.HRESULT]


class IUIElementFactory(_inspectable.IInspectable):
    pass


class IUIElementOverrides(_inspectable.IInspectable):
    OnCreateAutomationPeer: _Callable[[_Pointer[_Windows_UI_Xaml_Automation_Peers.IAutomationPeer]],  # result
                                      _type.HRESULT]
    OnDisconnectVisualChildren: _Callable[[],
                                          _type.HRESULT]
    FindSubElementsForTouchTargeting: _Callable[[_struct.Windows.Foundation.Point,  # point
                                                 _struct.Windows.Foundation.Rect,  # boundingRect
                                                 _Pointer[_Windows_Foundation_Collections.IIterable[_Windows_Foundation_Collections.IIterable[_struct.Windows.Foundation.Point]]]],  # result
                                                _type.HRESULT]


class IUIElementOverrides7(_inspectable.IInspectable):
    GetChildrenInTabFocusOrder: _Callable[[_Pointer[_Windows_Foundation_Collections.IIterable[IDependencyObject]]],  # result
                                          _type.HRESULT]
    OnProcessKeyboardAccelerators: _Callable[[_Windows_UI_Xaml_Input.IProcessKeyboardAcceleratorEventArgs],  # args
                                             _type.HRESULT]


class IUIElementOverrides8(_inspectable.IInspectable):
    OnKeyboardAcceleratorInvoked: _Callable[[_Windows_UI_Xaml_Input.IKeyboardAcceleratorInvokedEventArgs],  # args
                                            _type.HRESULT]
    OnBringIntoViewRequested: _Callable[[IBringIntoViewRequestedEventArgs],  # e
                                        _type.HRESULT]


class IUIElementOverrides9(_inspectable.IInspectable):
    PopulatePropertyInfoOverride: _Callable[[_type.HSTRING,  # propertyName
                                             _Windows_UI_Composition.IAnimationPropertyInfo],  # animationPropertyInfo
                                            _type.HRESULT]


class IUIElementStatics(_inspectable.IInspectable, factory=True):
    get_KeyDownEvent: _Callable[[_Pointer[IRoutedEvent]],  # value
                                _type.HRESULT]
    get_KeyUpEvent: _Callable[[_Pointer[IRoutedEvent]],  # value
                              _type.HRESULT]
    get_PointerEnteredEvent: _Callable[[_Pointer[IRoutedEvent]],  # value
                                       _type.HRESULT]
    get_PointerPressedEvent: _Callable[[_Pointer[IRoutedEvent]],  # value
                                       _type.HRESULT]
    get_PointerMovedEvent: _Callable[[_Pointer[IRoutedEvent]],  # value
                                     _type.HRESULT]
    get_PointerReleasedEvent: _Callable[[_Pointer[IRoutedEvent]],  # value
                                        _type.HRESULT]
    get_PointerExitedEvent: _Callable[[_Pointer[IRoutedEvent]],  # value
                                      _type.HRESULT]
    get_PointerCaptureLostEvent: _Callable[[_Pointer[IRoutedEvent]],  # value
                                           _type.HRESULT]
    get_PointerCanceledEvent: _Callable[[_Pointer[IRoutedEvent]],  # value
                                        _type.HRESULT]
    get_PointerWheelChangedEvent: _Callable[[_Pointer[IRoutedEvent]],  # value
                                            _type.HRESULT]
    get_TappedEvent: _Callable[[_Pointer[IRoutedEvent]],  # value
                               _type.HRESULT]
    get_DoubleTappedEvent: _Callable[[_Pointer[IRoutedEvent]],  # value
                                     _type.HRESULT]
    get_HoldingEvent: _Callable[[_Pointer[IRoutedEvent]],  # value
                                _type.HRESULT]
    get_RightTappedEvent: _Callable[[_Pointer[IRoutedEvent]],  # value
                                    _type.HRESULT]
    get_ManipulationStartingEvent: _Callable[[_Pointer[IRoutedEvent]],  # value
                                             _type.HRESULT]
    get_ManipulationInertiaStartingEvent: _Callable[[_Pointer[IRoutedEvent]],  # value
                                                    _type.HRESULT]
    get_ManipulationStartedEvent: _Callable[[_Pointer[IRoutedEvent]],  # value
                                            _type.HRESULT]
    get_ManipulationDeltaEvent: _Callable[[_Pointer[IRoutedEvent]],  # value
                                          _type.HRESULT]
    get_ManipulationCompletedEvent: _Callable[[_Pointer[IRoutedEvent]],  # value
                                              _type.HRESULT]
    get_DragEnterEvent: _Callable[[_Pointer[IRoutedEvent]],  # value
                                  _type.HRESULT]
    get_DragLeaveEvent: _Callable[[_Pointer[IRoutedEvent]],  # value
                                  _type.HRESULT]
    get_DragOverEvent: _Callable[[_Pointer[IRoutedEvent]],  # value
                                 _type.HRESULT]
    get_DropEvent: _Callable[[_Pointer[IRoutedEvent]],  # value
                             _type.HRESULT]
    get_AllowDropProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_OpacityProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_ClipProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                _type.HRESULT]
    get_RenderTransformProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_ProjectionProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_RenderTransformOriginProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_IsHitTestVisibleProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_VisibilityProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_UseLayoutRoundingProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_TransitionsProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_CacheModeProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_IsTapEnabledProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_IsDoubleTapEnabledProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_IsRightTapEnabledProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_IsHoldingEnabledProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_ManipulationModeProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_PointerCapturesProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                           _type.HRESULT]


class IUIElementStatics10(_inspectable.IInspectable, factory=True):
    get_ShadowProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                  _type.HRESULT]


class IUIElementStatics2(_inspectable.IInspectable, factory=True):
    get_CompositeModeProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                         _type.HRESULT]


class IUIElementStatics3(_inspectable.IInspectable, factory=True):
    get_Transform3DProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_CanDragProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                   _type.HRESULT]
    TryStartDirectManipulation: _Callable[[_Windows_UI_Xaml_Input.IPointer,  # value
                                           _Pointer[_type.boolean]],  # result
                                          _type.HRESULT]


class IUIElementStatics4(_inspectable.IInspectable, factory=True):
    get_ContextFlyoutProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_ExitDisplayModeOnAccessKeyInvokedProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                                             _type.HRESULT]
    get_IsAccessKeyScopeProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_AccessKeyScopeOwnerProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_AccessKeyProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                     _type.HRESULT]


class IUIElementStatics5(_inspectable.IInspectable, factory=True):
    get_LightsProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_KeyTipPlacementModeProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_KeyTipHorizontalOffsetProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                                  _type.HRESULT]
    get_KeyTipVerticalOffsetProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_XYFocusKeyboardNavigationProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                                     _type.HRESULT]
    get_XYFocusUpNavigationStrategyProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                                       _type.HRESULT]
    get_XYFocusDownNavigationStrategyProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                                         _type.HRESULT]
    get_XYFocusLeftNavigationStrategyProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                                         _type.HRESULT]
    get_XYFocusRightNavigationStrategyProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                                          _type.HRESULT]
    get_HighContrastAdjustmentProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                                  _type.HRESULT]
    get_TabFocusNavigationProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                              _type.HRESULT]


class IUIElementStatics6(_inspectable.IInspectable, factory=True):
    get_GettingFocusEvent: _Callable[[_Pointer[IRoutedEvent]],  # value
                                     _type.HRESULT]
    get_LosingFocusEvent: _Callable[[_Pointer[IRoutedEvent]],  # value
                                    _type.HRESULT]
    get_NoFocusCandidateFoundEvent: _Callable[[_Pointer[IRoutedEvent]],  # value
                                              _type.HRESULT]


class IUIElementStatics7(_inspectable.IInspectable, factory=True):
    get_PreviewKeyDownEvent: _Callable[[_Pointer[IRoutedEvent]],  # value
                                       _type.HRESULT]
    get_CharacterReceivedEvent: _Callable[[_Pointer[IRoutedEvent]],  # value
                                          _type.HRESULT]
    get_PreviewKeyUpEvent: _Callable[[_Pointer[IRoutedEvent]],  # value
                                     _type.HRESULT]


class IUIElementStatics8(_inspectable.IInspectable, factory=True):
    get_BringIntoViewRequestedEvent: _Callable[[_Pointer[IRoutedEvent]],  # value
                                               _type.HRESULT]
    get_ContextRequestedEvent: _Callable[[_Pointer[IRoutedEvent]],  # value
                                         _type.HRESULT]
    get_KeyTipTargetProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_KeyboardAcceleratorPlacementTargetProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                                              _type.HRESULT]
    get_KeyboardAcceleratorPlacementModeProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                                            _type.HRESULT]
    RegisterAsScrollPort: _Callable[[IUIElement],  # element
                                    _type.HRESULT]


class IUIElementStatics9(_inspectable.IInspectable, factory=True):
    get_CanBeScrollAnchorProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                             _type.HRESULT]


class IUIElementWeakCollection(_inspectable.IInspectable):
    pass


class IUIElementWeakCollectionFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IUIElementWeakCollection]],  # value
                              _type.HRESULT]


class IUnhandledExceptionEventArgs(_inspectable.IInspectable):
    get_Exception: _Callable[[_Pointer[_type.HRESULT]],  # value
                             _type.HRESULT]
    get_Message: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class IVector3Transition(_inspectable.IInspectable):
    get_Duration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    put_Duration: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                            _type.HRESULT]
    get_Components: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Vector3TransitionComponents]],  # value
                              _type.HRESULT]
    put_Components: _Callable[[_enum.Windows.UI.Xaml.Vector3TransitionComponents],  # value
                              _type.HRESULT]


class IVector3TransitionFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IVector3Transition]],  # value
                              _type.HRESULT]


class IVisualState(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Storyboard: _Callable[[_Pointer[_Windows_UI_Xaml_Media_Animation.IStoryboard]],  # value
                              _type.HRESULT]
    put_Storyboard: _Callable[[_Windows_UI_Xaml_Media_Animation.IStoryboard],  # value
                              _type.HRESULT]


class IVisualState2(_inspectable.IInspectable):
    get_Setters: _Callable[[_Pointer[ISetterBaseCollection]],  # value
                           _type.HRESULT]
    get_StateTriggers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IStateTriggerBase]]],  # value
                                 _type.HRESULT]


class IVisualStateChangedEventArgs(_inspectable.IInspectable):
    get_OldState: _Callable[[_Pointer[IVisualState]],  # value
                            _type.HRESULT]
    put_OldState: _Callable[[IVisualState],  # value
                            _type.HRESULT]
    get_NewState: _Callable[[_Pointer[IVisualState]],  # value
                            _type.HRESULT]
    put_NewState: _Callable[[IVisualState],  # value
                            _type.HRESULT]
    get_Control: _Callable[[_Pointer[_Windows_UI_Xaml_Controls.IControl]],  # value
                           _type.HRESULT]
    put_Control: _Callable[[_Windows_UI_Xaml_Controls.IControl],  # value
                           _type.HRESULT]


class IVisualStateGroup(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Transitions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IVisualTransition]]],  # value
                               _type.HRESULT]
    get_States: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IVisualState]]],  # value
                          _type.HRESULT]
    get_CurrentState: _Callable[[_Pointer[IVisualState]],  # value
                                _type.HRESULT]
    add_CurrentStateChanged: _Callable[[IVisualStateChangedEventHandler,  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_CurrentStateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_CurrentStateChanging: _Callable[[IVisualStateChangedEventHandler,  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_CurrentStateChanging: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]


class IVisualStateManager(_inspectable.IInspectable):
    pass


class IVisualStateManagerFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IVisualStateManager]],  # value
                              _type.HRESULT]


class IVisualStateManagerOverrides(_inspectable.IInspectable):
    GoToStateCore: _Callable[[_Windows_UI_Xaml_Controls.IControl,  # control
                              IFrameworkElement,  # templateRoot
                              _type.HSTRING,  # stateName
                              IVisualStateGroup,  # group
                              IVisualState,  # state
                              _type.boolean,  # useTransitions
                              _Pointer[_type.boolean]],  # result
                             _type.HRESULT]


class IVisualStateManagerProtected(_inspectable.IInspectable):
    RaiseCurrentStateChanging: _Callable[[IVisualStateGroup,  # stateGroup
                                          IVisualState,  # oldState
                                          IVisualState,  # newState
                                          _Windows_UI_Xaml_Controls.IControl],  # control
                                         _type.HRESULT]
    RaiseCurrentStateChanged: _Callable[[IVisualStateGroup,  # stateGroup
                                         IVisualState,  # oldState
                                         IVisualState,  # newState
                                         _Windows_UI_Xaml_Controls.IControl],  # control
                                        _type.HRESULT]


class IVisualStateManagerStatics(_inspectable.IInspectable, factory=True):
    GetVisualStateGroups: _Callable[[IFrameworkElement,  # obj
                                     _Pointer[_Windows_Foundation_Collections.IVector[IVisualStateGroup]]],  # result
                                    _type.HRESULT]
    get_CustomVisualStateManagerProperty: _Callable[[_Pointer[IDependencyProperty]],  # value
                                                    _type.HRESULT]
    GetCustomVisualStateManager: _Callable[[IFrameworkElement,  # obj
                                            _Pointer[IVisualStateManager]],  # result
                                           _type.HRESULT]
    SetCustomVisualStateManager: _Callable[[IFrameworkElement,  # obj
                                            IVisualStateManager],  # value
                                           _type.HRESULT]
    GoToState: _Callable[[_Windows_UI_Xaml_Controls.IControl,  # control
                          _type.HSTRING,  # stateName
                          _type.boolean,  # useTransitions
                          _Pointer[_type.boolean]],  # result
                         _type.HRESULT]


class IVisualTransition(_inspectable.IInspectable):
    get_GeneratedDuration: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Duration]],  # value
                                     _type.HRESULT]
    put_GeneratedDuration: _Callable[[_struct.Windows.UI.Xaml.Duration],  # value
                                     _type.HRESULT]
    get_GeneratedEasingFunction: _Callable[[_Pointer[_Windows_UI_Xaml_Media_Animation.IEasingFunctionBase]],  # value
                                           _type.HRESULT]
    put_GeneratedEasingFunction: _Callable[[_Windows_UI_Xaml_Media_Animation.IEasingFunctionBase],  # value
                                           _type.HRESULT]
    get_To: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    put_To: _Callable[[_type.HSTRING],  # value
                      _type.HRESULT]
    get_From: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_From: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_Storyboard: _Callable[[_Pointer[_Windows_UI_Xaml_Media_Animation.IStoryboard]],  # value
                              _type.HRESULT]
    put_Storyboard: _Callable[[_Windows_UI_Xaml_Media_Animation.IStoryboard],  # value
                              _type.HRESULT]


class IVisualTransitionFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IVisualTransition]],  # value
                              _type.HRESULT]


class IWindow(_inspectable.IInspectable):
    get_Bounds: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                          _type.HRESULT]
    get_Visible: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_Content: _Callable[[_Pointer[IUIElement]],  # value
                           _type.HRESULT]
    put_Content: _Callable[[IUIElement],  # value
                           _type.HRESULT]
    get_CoreWindow: _Callable[[_Pointer[_Windows_UI_Core.ICoreWindow]],  # value
                              _type.HRESULT]
    get_Dispatcher: _Callable[[_Pointer[_Windows_UI_Core.ICoreDispatcher]],  # value
                              _type.HRESULT]
    add_Activated: _Callable[[IWindowActivatedEventHandler,  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_Activated: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    add_Closed: _Callable[[IWindowClosedEventHandler,  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Closed: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    add_SizeChanged: _Callable[[IWindowSizeChangedEventHandler,  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_SizeChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    add_VisibilityChanged: _Callable[[IWindowVisibilityChangedEventHandler,  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_VisibilityChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    Activate: _Callable[[],
                        _type.HRESULT]
    Close: _Callable[[],
                     _type.HRESULT]


class IWindow2(_inspectable.IInspectable):
    SetTitleBar: _Callable[[IUIElement],  # value
                           _type.HRESULT]


class IWindow3(_inspectable.IInspectable):
    get_Compositor: _Callable[[_Pointer[_Windows_UI_Composition.ICompositor]],  # value
                              _type.HRESULT]


class IWindow4(_inspectable.IInspectable):
    get_UIContext: _Callable[[_Pointer[_Windows_UI.IUIContext]],  # value
                             _type.HRESULT]


class IWindowCreatedEventArgs(_inspectable.IInspectable):
    get_Window: _Callable[[_Pointer[IWindow]],  # value
                          _type.HRESULT]


class IWindowStatics(_inspectable.IInspectable, factory=True):
    get_Current: _Callable[[_Pointer[IWindow]],  # value
                           _type.HRESULT]


class IXamlRoot(_inspectable.IInspectable):
    get_Content: _Callable[[_Pointer[IUIElement]],  # value
                           _type.HRESULT]
    get_Size: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                        _type.HRESULT]
    get_RasterizationScale: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                      _type.HRESULT]
    get_IsHostVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_UIContext: _Callable[[_Pointer[_Windows_UI.IUIContext]],  # value
                             _type.HRESULT]
    add_Changed: _Callable[[_Windows_Foundation.ITypedEventHandler[IXamlRoot, IXamlRootChangedEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Changed: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]


class IXamlRootChangedEventArgs(_inspectable.IInspectable):
    pass
