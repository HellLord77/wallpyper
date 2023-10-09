from __future__ import annotations as _

from typing import Callable as _Callable

from .. import Controls as _Microsoft_UI_Xaml_Controls
from ... import Input as _Microsoft_UI_Input
from ... import Xaml as _Microsoft_UI_Xaml
from ..... import inspectable as _inspectable
from .....Windows import Foundation as _Windows_Foundation
from .....Windows.Foundation import Collections as _Windows_Foundation_Collections
from ......um import Unknwnbase as _Unknwnbase
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class _IDoubleTappedEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       IDoubleTappedRoutedEventArgs],  # e
                      _type.HRESULT]


class IDoubleTappedEventHandler(_IDoubleTappedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IDoubleTappedEventHandler_impl(_IDoubleTappedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IHoldingEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       IHoldingRoutedEventArgs],  # e
                      _type.HRESULT]


class IHoldingEventHandler(_IHoldingEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IHoldingEventHandler_impl(_IHoldingEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IKeyEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       IKeyRoutedEventArgs],  # e
                      _type.HRESULT]


class IKeyEventHandler(_IKeyEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IKeyEventHandler_impl(_IKeyEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IManipulationCompletedEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       IManipulationCompletedRoutedEventArgs],  # e
                      _type.HRESULT]


class IManipulationCompletedEventHandler(_IManipulationCompletedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IManipulationCompletedEventHandler_impl(_IManipulationCompletedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IManipulationDeltaEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       IManipulationDeltaRoutedEventArgs],  # e
                      _type.HRESULT]


class IManipulationDeltaEventHandler(_IManipulationDeltaEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IManipulationDeltaEventHandler_impl(_IManipulationDeltaEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IManipulationInertiaStartingEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       IManipulationInertiaStartingRoutedEventArgs],  # e
                      _type.HRESULT]


class IManipulationInertiaStartingEventHandler(_IManipulationInertiaStartingEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IManipulationInertiaStartingEventHandler_impl(_IManipulationInertiaStartingEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IManipulationStartedEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       IManipulationStartedRoutedEventArgs],  # e
                      _type.HRESULT]


class IManipulationStartedEventHandler(_IManipulationStartedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IManipulationStartedEventHandler_impl(_IManipulationStartedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IManipulationStartingEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       IManipulationStartingRoutedEventArgs],  # e
                      _type.HRESULT]


class IManipulationStartingEventHandler(_IManipulationStartingEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IManipulationStartingEventHandler_impl(_IManipulationStartingEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IPointerEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       IPointerRoutedEventArgs],  # e
                      _type.HRESULT]


class IPointerEventHandler(_IPointerEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IPointerEventHandler_impl(_IPointerEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IRightTappedEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       IRightTappedRoutedEventArgs],  # e
                      _type.HRESULT]


class IRightTappedEventHandler(_IRightTappedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IRightTappedEventHandler_impl(_IRightTappedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ITappedEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       ITappedRoutedEventArgs],  # e
                      _type.HRESULT]


class ITappedEventHandler(_ITappedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ITappedEventHandler_impl(_ITappedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class IAccessKeyDisplayDismissedEventArgs(_inspectable.IInspectable):
    pass


class IAccessKeyDisplayRequestedEventArgs(_inspectable.IInspectable):
    get_PressedKeys: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class IAccessKeyInvokedEventArgs(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class IAccessKeyManager(_inspectable.IInspectable):
    pass


class IAccessKeyManagerStatics(_inspectable.IInspectable, factory=True):
    get_IsDisplayModeEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_AreKeyTipsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    put_AreKeyTipsEnabled: _Callable[[_type.boolean],  # value
                                     _type.HRESULT]
    add_IsDisplayModeEnabledChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[_inspectable.IInspectable, _inspectable.IInspectable],  # handler
                                                _Pointer[_struct.EventRegistrationToken]],  # token
                                               _type.HRESULT]
    remove_IsDisplayModeEnabledChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                  _type.HRESULT]
    ExitDisplayMode: _Callable[[],
                               _type.HRESULT]


class IAccessKeyManagerStatics2(_inspectable.IInspectable, factory=True):
    EnterDisplayModeForXamlRoot: _Callable[[_Microsoft_UI_Xaml.IXamlRoot],  # XamlRoot
                                           _type.HRESULT]


class ICanExecuteRequestedEventArgs(_inspectable.IInspectable):
    get_Parameter: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                             _type.HRESULT]
    get_CanExecute: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    put_CanExecute: _Callable[[_type.boolean],  # value
                              _type.HRESULT]


class ICharacterReceivedRoutedEventArgs(_inspectable.IInspectable):
    get_Character: _Callable[[_Pointer[_type.WCHAR]],  # value
                             _type.HRESULT]
    get_KeyStatus: _Callable[[_Pointer[_struct.Windows.UI.Core.CorePhysicalKeyStatus]],  # value
                             _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class ICommand(_inspectable.IInspectable):
    add_CanExecuteChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_CanExecuteChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    CanExecute: _Callable[[_inspectable.IInspectable,  # parameter
                           _Pointer[_type.boolean]],  # result
                          _type.HRESULT]
    Execute: _Callable[[_inspectable.IInspectable],  # parameter
                       _type.HRESULT]


class IContextRequestedEventArgs(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    TryGetPosition: _Callable[[_Microsoft_UI_Xaml.IUIElement,  # relativeTo
                               _Pointer[_struct.Windows.Foundation.Point],  # point
                               _Pointer[_type.boolean]],  # returnValue
                              _type.HRESULT]


class IDoubleTappedRoutedEventArgs(_inspectable.IInspectable):
    get_PointerDeviceType: _Callable[[_Pointer[_enum.Microsoft.UI.Input.PointerDeviceType]],  # value
                                     _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    GetPosition: _Callable[[_Microsoft_UI_Xaml.IUIElement,  # relativeTo
                            _Pointer[_struct.Windows.Foundation.Point]],  # result
                           _type.HRESULT]


class IExecuteRequestedEventArgs(_inspectable.IInspectable):
    get_Parameter: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                             _type.HRESULT]


class IFindNextElementOptions(_inspectable.IInspectable):
    get_SearchRoot: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyObject]],  # value
                              _type.HRESULT]
    put_SearchRoot: _Callable[[_Microsoft_UI_Xaml.IDependencyObject],  # value
                              _type.HRESULT]
    get_ExclusionRect: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                                 _type.HRESULT]
    put_ExclusionRect: _Callable[[_struct.Windows.Foundation.Rect],  # value
                                 _type.HRESULT]
    get_HintRect: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                            _type.HRESULT]
    put_HintRect: _Callable[[_struct.Windows.Foundation.Rect],  # value
                            _type.HRESULT]
    get_XYFocusNavigationStrategyOverride: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Input.XYFocusNavigationStrategyOverride]],  # value
                                                     _type.HRESULT]
    put_XYFocusNavigationStrategyOverride: _Callable[[_enum.Microsoft.UI.Xaml.Input.XYFocusNavigationStrategyOverride],  # value
                                                     _type.HRESULT]


class IFocusManager(_inspectable.IInspectable):
    pass


class IFocusManagerGotFocusEventArgs(_inspectable.IInspectable):
    get_NewFocusedElement: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyObject]],  # value
                                     _type.HRESULT]
    get_CorrelationId: _Callable[[_Pointer[_struct.GUID]],  # value
                                 _type.HRESULT]


class IFocusManagerLostFocusEventArgs(_inspectable.IInspectable):
    get_OldFocusedElement: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyObject]],  # value
                                     _type.HRESULT]
    get_CorrelationId: _Callable[[_Pointer[_struct.GUID]],  # value
                                 _type.HRESULT]


class IFocusManagerStatics(_inspectable.IInspectable, factory=True):
    add_GotFocus: _Callable[[_Windows_Foundation.IEventHandler[IFocusManagerGotFocusEventArgs],  # handler
                             _Pointer[_struct.EventRegistrationToken]],  # token
                            _type.HRESULT]
    remove_GotFocus: _Callable[[_struct.EventRegistrationToken],  # token
                               _type.HRESULT]
    add_LostFocus: _Callable[[_Windows_Foundation.IEventHandler[IFocusManagerLostFocusEventArgs],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_LostFocus: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    add_GettingFocus: _Callable[[_Windows_Foundation.IEventHandler[IGettingFocusEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_GettingFocus: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    add_LosingFocus: _Callable[[_Windows_Foundation.IEventHandler[ILosingFocusEventArgs],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_LosingFocus: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    TryFocusAsync: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                              _enum.Microsoft.UI.Xaml.FocusState,  # value
                              _Pointer[_Windows_Foundation.IAsyncOperation[IFocusMovementResult]]],  # operation
                             _type.HRESULT]
    TryMoveFocusAsync: _Callable[[_enum.Microsoft.UI.Xaml.Input.FocusNavigationDirection,  # focusNavigationDirection
                                  _Pointer[_Windows_Foundation.IAsyncOperation[IFocusMovementResult]]],  # operation
                                 _type.HRESULT]
    TryMoveFocusWithOptionsAsync: _Callable[[_enum.Microsoft.UI.Xaml.Input.FocusNavigationDirection,  # focusNavigationDirection
                                             IFindNextElementOptions,  # focusNavigationOptions
                                             _Pointer[_Windows_Foundation.IAsyncOperation[IFocusMovementResult]]],  # operation
                                            _type.HRESULT]
    TryMoveFocusWithOptions: _Callable[[_enum.Microsoft.UI.Xaml.Input.FocusNavigationDirection,  # focusNavigationDirection
                                        IFindNextElementOptions,  # focusNavigationOptions
                                        _Pointer[_type.boolean]],  # result
                                       _type.HRESULT]
    FindNextElement: _Callable[[_enum.Microsoft.UI.Xaml.Input.FocusNavigationDirection,  # focusNavigationDirection
                                _Pointer[_Microsoft_UI_Xaml.IDependencyObject]],  # result
                               _type.HRESULT]
    FindFirstFocusableElement: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # searchScope
                                          _Pointer[_Microsoft_UI_Xaml.IDependencyObject]],  # result
                                         _type.HRESULT]
    FindLastFocusableElement: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # searchScope
                                         _Pointer[_Microsoft_UI_Xaml.IDependencyObject]],  # result
                                        _type.HRESULT]
    FindNextElementWithOptions: _Callable[[_enum.Microsoft.UI.Xaml.Input.FocusNavigationDirection,  # focusNavigationDirection
                                           IFindNextElementOptions,  # focusNavigationOptions
                                           _Pointer[_Microsoft_UI_Xaml.IDependencyObject]],  # result
                                          _type.HRESULT]
    FindNextFocusableElement: _Callable[[_enum.Microsoft.UI.Xaml.Input.FocusNavigationDirection,  # focusNavigationDirection
                                         _Pointer[_Microsoft_UI_Xaml.IUIElement]],  # result
                                        _type.HRESULT]
    FindNextFocusableElementWithHint: _Callable[[_enum.Microsoft.UI.Xaml.Input.FocusNavigationDirection,  # focusNavigationDirection
                                                 _struct.Windows.Foundation.Rect,  # hintRect
                                                 _Pointer[_Microsoft_UI_Xaml.IUIElement]],  # result
                                                _type.HRESULT]
    TryMoveFocus: _Callable[[_enum.Microsoft.UI.Xaml.Input.FocusNavigationDirection,  # focusNavigationDirection
                             _Pointer[_type.boolean]],  # result
                            _type.HRESULT]
    GetFocusedElement: _Callable[[_Pointer[_inspectable.IInspectable]],  # result
                                 _type.HRESULT]
    GetFocusedElementWithRoot: _Callable[[_Microsoft_UI_Xaml.IXamlRoot,  # xamlRoot
                                          _Pointer[_inspectable.IInspectable]],  # result
                                         _type.HRESULT]


class IFocusMovementResult(_inspectable.IInspectable):
    get_Succeeded: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]


class IGettingFocusEventArgs(_inspectable.IInspectable):
    get_OldFocusedElement: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyObject]],  # value
                                     _type.HRESULT]
    get_NewFocusedElement: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyObject]],  # value
                                     _type.HRESULT]
    put_NewFocusedElement: _Callable[[_Microsoft_UI_Xaml.IDependencyObject],  # value
                                     _type.HRESULT]
    get_FocusState: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.FocusState]],  # value
                              _type.HRESULT]
    get_Direction: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Input.FocusNavigationDirection]],  # value
                             _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_InputDevice: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Input.FocusInputDeviceKind]],  # value
                               _type.HRESULT]
    get_Cancel: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_Cancel: _Callable[[_type.boolean],  # value
                          _type.HRESULT]
    get_CorrelationId: _Callable[[_Pointer[_struct.GUID]],  # value
                                 _type.HRESULT]
    TryCancel: _Callable[[_Pointer[_type.boolean]],  # result
                         _type.HRESULT]
    TrySetNewFocusedElement: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                        _Pointer[_type.boolean]],  # result
                                       _type.HRESULT]


class IHoldingRoutedEventArgs(_inspectable.IInspectable):
    get_PointerDeviceType: _Callable[[_Pointer[_enum.Microsoft.UI.Input.PointerDeviceType]],  # value
                                     _type.HRESULT]
    get_HoldingState: _Callable[[_Pointer[_enum.Microsoft.UI.Input.HoldingState]],  # value
                                _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    GetPosition: _Callable[[_Microsoft_UI_Xaml.IUIElement,  # relativeTo
                            _Pointer[_struct.Windows.Foundation.Point]],  # result
                           _type.HRESULT]


class IInertiaExpansionBehavior(_inspectable.IInspectable):
    get_DesiredDeceleration: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                       _type.HRESULT]
    put_DesiredDeceleration: _Callable[[_type.DOUBLE],  # value
                                       _type.HRESULT]
    get_DesiredExpansion: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]
    put_DesiredExpansion: _Callable[[_type.DOUBLE],  # value
                                    _type.HRESULT]


class IInertiaRotationBehavior(_inspectable.IInspectable):
    get_DesiredDeceleration: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                       _type.HRESULT]
    put_DesiredDeceleration: _Callable[[_type.DOUBLE],  # value
                                       _type.HRESULT]
    get_DesiredRotation: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                   _type.HRESULT]
    put_DesiredRotation: _Callable[[_type.DOUBLE],  # value
                                   _type.HRESULT]


class IInertiaTranslationBehavior(_inspectable.IInspectable):
    get_DesiredDeceleration: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                       _type.HRESULT]
    put_DesiredDeceleration: _Callable[[_type.DOUBLE],  # value
                                       _type.HRESULT]
    get_DesiredDisplacement: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                       _type.HRESULT]
    put_DesiredDisplacement: _Callable[[_type.DOUBLE],  # value
                                       _type.HRESULT]


class IInputScope(_inspectable.IInspectable):
    get_Names: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IInputScopeName]]],  # value
                         _type.HRESULT]


class IInputScopeName(_inspectable.IInspectable):
    get_NameValue: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Input.InputScopeNameValue]],  # value
                             _type.HRESULT]
    put_NameValue: _Callable[[_enum.Microsoft.UI.Xaml.Input.InputScopeNameValue],  # value
                             _type.HRESULT]


class IInputScopeNameFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[_enum.Microsoft.UI.Xaml.Input.InputScopeNameValue,  # nameValue
                               _Pointer[IInputScopeName]],  # value
                              _type.HRESULT]


class IKeyRoutedEventArgs(_inspectable.IInspectable):
    get_Key: _Callable[[_Pointer[_enum.Windows.System.VirtualKey]],  # value
                       _type.HRESULT]
    get_KeyStatus: _Callable[[_Pointer[_struct.Windows.UI.Core.CorePhysicalKeyStatus]],  # value
                             _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_OriginalKey: _Callable[[_Pointer[_enum.Windows.System.VirtualKey]],  # value
                               _type.HRESULT]
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]


class IKeyboardAccelerator(_inspectable.IInspectable):
    get_Key: _Callable[[_Pointer[_enum.Windows.System.VirtualKey]],  # value
                       _type.HRESULT]
    put_Key: _Callable[[_enum.Windows.System.VirtualKey],  # value
                       _type.HRESULT]
    get_Modifiers: _Callable[[_Pointer[_enum.Windows.System.VirtualKeyModifiers]],  # value
                             _type.HRESULT]
    put_Modifiers: _Callable[[_enum.Windows.System.VirtualKeyModifiers],  # value
                             _type.HRESULT]
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsEnabled: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    get_ScopeOwner: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyObject]],  # value
                              _type.HRESULT]
    put_ScopeOwner: _Callable[[_Microsoft_UI_Xaml.IDependencyObject],  # value
                              _type.HRESULT]
    add_Invoked: _Callable[[_Windows_Foundation.ITypedEventHandler[IKeyboardAccelerator, IKeyboardAcceleratorInvokedEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Invoked: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]


class IKeyboardAcceleratorFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IKeyboardAccelerator]],  # value
                              _type.HRESULT]


class IKeyboardAcceleratorInvokedEventArgs(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_Element: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyObject]],  # value
                           _type.HRESULT]
    get_KeyboardAccelerator: _Callable[[_Pointer[IKeyboardAccelerator]],  # value
                                       _type.HRESULT]


class IKeyboardAcceleratorStatics(_inspectable.IInspectable, factory=True):
    get_KeyProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                               _type.HRESULT]
    get_ModifiersProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_IsEnabledProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_ScopeOwnerProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]


class ILosingFocusEventArgs(_inspectable.IInspectable):
    get_OldFocusedElement: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyObject]],  # value
                                     _type.HRESULT]
    get_NewFocusedElement: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyObject]],  # value
                                     _type.HRESULT]
    put_NewFocusedElement: _Callable[[_Microsoft_UI_Xaml.IDependencyObject],  # value
                                     _type.HRESULT]
    get_FocusState: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.FocusState]],  # value
                              _type.HRESULT]
    get_Direction: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Input.FocusNavigationDirection]],  # value
                             _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_InputDevice: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Input.FocusInputDeviceKind]],  # value
                               _type.HRESULT]
    get_Cancel: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_Cancel: _Callable[[_type.boolean],  # value
                          _type.HRESULT]
    get_CorrelationId: _Callable[[_Pointer[_struct.GUID]],  # value
                                 _type.HRESULT]
    TryCancel: _Callable[[_Pointer[_type.boolean]],  # result
                         _type.HRESULT]
    TrySetNewFocusedElement: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                        _Pointer[_type.boolean]],  # result
                                       _type.HRESULT]


class IManipulationCompletedRoutedEventArgs(_inspectable.IInspectable):
    get_Container: _Callable[[_Pointer[_Microsoft_UI_Xaml.IUIElement]],  # value
                             _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    get_IsInertial: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_Cumulative: _Callable[[_Pointer[_struct.Microsoft.UI.Input.ManipulationDelta]],  # value
                              _type.HRESULT]
    get_Velocities: _Callable[[_Pointer[_struct.Microsoft.UI.Input.ManipulationVelocities]],  # value
                              _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_PointerDeviceType: _Callable[[_Pointer[_enum.Microsoft.UI.Input.PointerDeviceType]],  # value
                                     _type.HRESULT]


class IManipulationDeltaRoutedEventArgs(_inspectable.IInspectable):
    get_Container: _Callable[[_Pointer[_Microsoft_UI_Xaml.IUIElement]],  # value
                             _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    get_IsInertial: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_Delta: _Callable[[_Pointer[_struct.Microsoft.UI.Input.ManipulationDelta]],  # value
                         _type.HRESULT]
    get_Cumulative: _Callable[[_Pointer[_struct.Microsoft.UI.Input.ManipulationDelta]],  # value
                              _type.HRESULT]
    get_Velocities: _Callable[[_Pointer[_struct.Microsoft.UI.Input.ManipulationVelocities]],  # value
                              _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_PointerDeviceType: _Callable[[_Pointer[_enum.Microsoft.UI.Input.PointerDeviceType]],  # value
                                     _type.HRESULT]
    Complete: _Callable[[],
                        _type.HRESULT]


class IManipulationInertiaStartingRoutedEventArgs(_inspectable.IInspectable):
    get_Container: _Callable[[_Pointer[_Microsoft_UI_Xaml.IUIElement]],  # value
                             _type.HRESULT]
    get_ExpansionBehavior: _Callable[[_Pointer[IInertiaExpansionBehavior]],  # value
                                     _type.HRESULT]
    put_ExpansionBehavior: _Callable[[IInertiaExpansionBehavior],  # value
                                     _type.HRESULT]
    get_RotationBehavior: _Callable[[_Pointer[IInertiaRotationBehavior]],  # value
                                    _type.HRESULT]
    put_RotationBehavior: _Callable[[IInertiaRotationBehavior],  # value
                                    _type.HRESULT]
    get_TranslationBehavior: _Callable[[_Pointer[IInertiaTranslationBehavior]],  # value
                                       _type.HRESULT]
    put_TranslationBehavior: _Callable[[IInertiaTranslationBehavior],  # value
                                       _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_PointerDeviceType: _Callable[[_Pointer[_enum.Microsoft.UI.Input.PointerDeviceType]],  # value
                                     _type.HRESULT]
    get_Delta: _Callable[[_Pointer[_struct.Microsoft.UI.Input.ManipulationDelta]],  # value
                         _type.HRESULT]
    get_Cumulative: _Callable[[_Pointer[_struct.Microsoft.UI.Input.ManipulationDelta]],  # value
                              _type.HRESULT]
    get_Velocities: _Callable[[_Pointer[_struct.Microsoft.UI.Input.ManipulationVelocities]],  # value
                              _type.HRESULT]


class IManipulationPivot(_inspectable.IInspectable):
    get_Center: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                          _type.HRESULT]
    put_Center: _Callable[[_struct.Windows.Foundation.Point],  # value
                          _type.HRESULT]
    get_Radius: _Callable[[_Pointer[_type.DOUBLE]],  # value
                          _type.HRESULT]
    put_Radius: _Callable[[_type.DOUBLE],  # value
                          _type.HRESULT]


class IManipulationPivotFactory(_inspectable.IInspectable, factory=True):
    CreateInstanceWithCenterAndRadius: _Callable[[_struct.Windows.Foundation.Point,  # center
                                                  _type.DOUBLE,  # radius
                                                  _Pointer[IManipulationPivot]],  # value
                                                 _type.HRESULT]


class IManipulationStartedRoutedEventArgs(_inspectable.IInspectable):
    get_Container: _Callable[[_Pointer[_Microsoft_UI_Xaml.IUIElement]],  # value
                             _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_PointerDeviceType: _Callable[[_Pointer[_enum.Microsoft.UI.Input.PointerDeviceType]],  # value
                                     _type.HRESULT]
    get_Cumulative: _Callable[[_Pointer[_struct.Microsoft.UI.Input.ManipulationDelta]],  # value
                              _type.HRESULT]
    Complete: _Callable[[],
                        _type.HRESULT]


class IManipulationStartedRoutedEventArgsFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IManipulationStartedRoutedEventArgs]],  # value
                              _type.HRESULT]


class IManipulationStartingRoutedEventArgs(_inspectable.IInspectable):
    get_Mode: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Input.ManipulationModes]],  # value
                        _type.HRESULT]
    put_Mode: _Callable[[_enum.Microsoft.UI.Xaml.Input.ManipulationModes],  # value
                        _type.HRESULT]
    get_Container: _Callable[[_Pointer[_Microsoft_UI_Xaml.IUIElement]],  # value
                             _type.HRESULT]
    put_Container: _Callable[[_Microsoft_UI_Xaml.IUIElement],  # value
                             _type.HRESULT]
    get_Pivot: _Callable[[_Pointer[IManipulationPivot]],  # value
                         _type.HRESULT]
    put_Pivot: _Callable[[IManipulationPivot],  # value
                         _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class INoFocusCandidateFoundEventArgs(_inspectable.IInspectable):
    get_Direction: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Input.FocusNavigationDirection]],  # value
                             _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_InputDevice: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Input.FocusInputDeviceKind]],  # value
                               _type.HRESULT]


class IPointer(_inspectable.IInspectable):
    get_PointerId: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    get_PointerDeviceType: _Callable[[_Pointer[_enum.Microsoft.UI.Input.PointerDeviceType]],  # value
                                     _type.HRESULT]
    get_IsInContact: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_IsInRange: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]


class IPointerRoutedEventArgs(_inspectable.IInspectable):
    get_Pointer: _Callable[[_Pointer[IPointer]],  # value
                           _type.HRESULT]
    get_KeyModifiers: _Callable[[_Pointer[_enum.Windows.System.VirtualKeyModifiers]],  # value
                                _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_IsGenerated: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    GetCurrentPoint: _Callable[[_Microsoft_UI_Xaml.IUIElement,  # relativeTo
                                _Pointer[_Microsoft_UI_Input.IPointerPoint]],  # result
                               _type.HRESULT]
    GetIntermediatePoints: _Callable[[_Microsoft_UI_Xaml.IUIElement,  # relativeTo
                                      _Pointer[_Windows_Foundation_Collections.IVector[_Microsoft_UI_Input.IPointerPoint]]],  # result
                                     _type.HRESULT]


class IProcessKeyboardAcceleratorEventArgs(_inspectable.IInspectable):
    get_Key: _Callable[[_Pointer[_enum.Windows.System.VirtualKey]],  # value
                       _type.HRESULT]
    get_Modifiers: _Callable[[_Pointer[_enum.Windows.System.VirtualKeyModifiers]],  # value
                             _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class IRightTappedRoutedEventArgs(_inspectable.IInspectable):
    get_PointerDeviceType: _Callable[[_Pointer[_enum.Microsoft.UI.Input.PointerDeviceType]],  # value
                                     _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    GetPosition: _Callable[[_Microsoft_UI_Xaml.IUIElement,  # relativeTo
                            _Pointer[_struct.Windows.Foundation.Point]],  # result
                           _type.HRESULT]


class IStandardUICommand(_inspectable.IInspectable):
    get_Kind: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Input.StandardUICommandKind]],  # value
                        _type.HRESULT]
    put_Kind: _Callable[[_enum.Microsoft.UI.Xaml.Input.StandardUICommandKind],  # value
                        _type.HRESULT]


class IStandardUICommandFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IStandardUICommand]],  # value
                              _type.HRESULT]
    CreateInstanceWithKind: _Callable[[_enum.Microsoft.UI.Xaml.Input.StandardUICommandKind,  # kind
                                       _inspectable.IInspectable,  # baseInterface
                                       _Pointer[_inspectable.IInspectable],  # innerInterface
                                       _Pointer[IStandardUICommand]],  # value
                                      _type.HRESULT]


class IStandardUICommandStatics(_inspectable.IInspectable, factory=True):
    get_KindProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]


class ITappedRoutedEventArgs(_inspectable.IInspectable):
    get_PointerDeviceType: _Callable[[_Pointer[_enum.Microsoft.UI.Input.PointerDeviceType]],  # value
                                     _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    GetPosition: _Callable[[_Microsoft_UI_Xaml.IUIElement,  # relativeTo
                            _Pointer[_struct.Windows.Foundation.Point]],  # result
                           _type.HRESULT]


class IXamlUICommand(_inspectable.IInspectable):
    get_Label: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Label: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_IconSource: _Callable[[_Pointer[_Microsoft_UI_Xaml_Controls.IIconSource]],  # value
                              _type.HRESULT]
    put_IconSource: _Callable[[_Microsoft_UI_Xaml_Controls.IIconSource],  # value
                              _type.HRESULT]
    get_KeyboardAccelerators: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IKeyboardAccelerator]]],  # value
                                        _type.HRESULT]
    get_AccessKey: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_AccessKey: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_Command: _Callable[[_Pointer[ICommand]],  # value
                           _type.HRESULT]
    put_Command: _Callable[[ICommand],  # value
                           _type.HRESULT]
    add_ExecuteRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IXamlUICommand, IExecuteRequestedEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_ExecuteRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    add_CanExecuteRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IXamlUICommand, ICanExecuteRequestedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_CanExecuteRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    NotifyCanExecuteChanged: _Callable[[],
                                       _type.HRESULT]


class IXamlUICommandFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IXamlUICommand]],  # value
                              _type.HRESULT]


class IXamlUICommandStatics(_inspectable.IInspectable, factory=True):
    get_LabelProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_IconSourceProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_KeyboardAcceleratorsProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_AccessKeyProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_DescriptionProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_CommandProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
