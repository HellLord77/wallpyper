from __future__ import annotations as _

from typing import Callable as _Callable

from .. import Composition as _Windows_UI_Composition
from .. import Input as _Windows_UI_Input
from .. import Popups as _Windows_UI_Popups
from ... import Foundation as _Windows_Foundation
from ... import System as _Windows_System
from ... import UI as _Windows_UI
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from .....um import Unknwnbase as _Unknwnbase
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class ICoreWindowFactory(_inspectable.IInspectable):
    CreateCoreWindow: _Callable[[_type.HSTRING,  # windowTitle
                                 _Pointer[ICoreWindow]],  # window
                                _type.HRESULT]
    get_WindowReuseAllowed: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]


class _IDispatchedHandler:
    Invoke: _Callable[[],
                      _type.HRESULT]


class IDispatchedHandler(_IDispatchedHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IDispatchedHandler_impl(_IDispatchedHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IIdleDispatchedHandler:
    Invoke: _Callable[[IIdleDispatchedHandlerArgs],  # e
                      _type.HRESULT]


class IIdleDispatchedHandler(_IIdleDispatchedHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IIdleDispatchedHandler_impl(_IIdleDispatchedHandler, _Unknwnbase.IUnknown_impl):
    pass


class IAcceleratorKeyEventArgs(_inspectable.IInspectable):
    get_EventType: _Callable[[_Pointer[_enum.Windows.UI.Core.CoreAcceleratorKeyEventType]],  # value
                             _type.HRESULT]
    get_VirtualKey: _Callable[[_Pointer[_enum.Windows.System.VirtualKey]],  # value
                              _type.HRESULT]
    get_KeyStatus: _Callable[[_Pointer[_struct.Windows.UI.Core.CorePhysicalKeyStatus]],  # value
                             _type.HRESULT]


class IAcceleratorKeyEventArgs2(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]


class IAutomationProviderRequestedEventArgs(_inspectable.IInspectable):
    get_AutomationProvider: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                      _type.HRESULT]
    put_AutomationProvider: _Callable[[_inspectable.IInspectable],  # value
                                      _type.HRESULT]


class IBackRequestedEventArgs(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class ICharacterReceivedEventArgs(_inspectable.IInspectable):
    get_KeyCode: _Callable[[_Pointer[_type.UINT32]],  # value
                           _type.HRESULT]
    get_KeyStatus: _Callable[[_Pointer[_struct.Windows.UI.Core.CorePhysicalKeyStatus]],  # value
                             _type.HRESULT]


class IClosestInteractiveBoundsRequestedEventArgs(_inspectable.IInspectable):
    get_PointerPosition: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                                   _type.HRESULT]
    get_SearchBounds: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                                _type.HRESULT]
    get_ClosestInteractiveBounds: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                                            _type.HRESULT]
    put_ClosestInteractiveBounds: _Callable[[_struct.Windows.Foundation.Rect],  # value
                                            _type.HRESULT]


class ICoreAcceleratorKeys(_inspectable.IInspectable):
    add_AcceleratorKeyActivated: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreDispatcher, IAcceleratorKeyEventArgs],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # pCookie
                                           _type.HRESULT]
    remove_AcceleratorKeyActivated: _Callable[[_struct.EventRegistrationToken],  # cookie
                                              _type.HRESULT]


class ICoreClosestInteractiveBoundsRequested(_inspectable.IInspectable):
    add_ClosestInteractiveBoundsRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreInputSourceBase, IClosestInteractiveBoundsRequestedEventArgs],  # handler
                                                      _Pointer[_struct.EventRegistrationToken]],  # pCookie
                                                     _type.HRESULT]
    remove_ClosestInteractiveBoundsRequested: _Callable[[_struct.EventRegistrationToken],  # cookie
                                                        _type.HRESULT]


class ICoreComponentFocusable(_inspectable.IInspectable):
    get_HasFocus: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    add_GotFocus: _Callable[[_Windows_Foundation.ITypedEventHandler[_inspectable.IInspectable, ICoreWindowEventArgs],  # handler
                             _Pointer[_struct.EventRegistrationToken]],  # pCookie
                            _type.HRESULT]
    remove_GotFocus: _Callable[[_struct.EventRegistrationToken],  # cookie
                               _type.HRESULT]
    add_LostFocus: _Callable[[_Windows_Foundation.ITypedEventHandler[_inspectable.IInspectable, ICoreWindowEventArgs],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # pCookie
                             _type.HRESULT]
    remove_LostFocus: _Callable[[_struct.EventRegistrationToken],  # cookie
                                _type.HRESULT]


class ICoreCursor(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.UINT32]],  # value
                      _type.HRESULT]
    get_Type: _Callable[[_Pointer[_enum.Windows.UI.Core.CoreCursorType]],  # value
                        _type.HRESULT]


class ICoreCursorFactory(_inspectable.IInspectable):
    CreateCursor: _Callable[[_enum.Windows.UI.Core.CoreCursorType,  # type
                             _type.UINT32,  # id
                             _Pointer[ICoreCursor]],  # cursor
                            _type.HRESULT]

    _factory = True


class ICoreDispatcher(_inspectable.IInspectable):
    get_HasThreadAccess: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    ProcessEvents: _Callable[[_enum.Windows.UI.Core.CoreProcessEventsOption],  # options
                             _type.HRESULT]
    RunAsync: _Callable[[_enum.Windows.UI.Core.CoreDispatcherPriority,  # priority
                         IDispatchedHandler,  # agileCallback
                         _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncAction
                        _type.HRESULT]
    RunIdleAsync: _Callable[[IIdleDispatchedHandler,  # agileCallback
                             _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncAction
                            _type.HRESULT]


class ICoreDispatcher2(_inspectable.IInspectable):
    TryRunAsync: _Callable[[_enum.Windows.UI.Core.CoreDispatcherPriority,  # priority
                            IDispatchedHandler,  # agileCallback
                            _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # asyncOperation
                           _type.HRESULT]
    TryRunIdleAsync: _Callable[[IIdleDispatchedHandler,  # agileCallback
                                _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # asyncOperation
                               _type.HRESULT]


class ICoreDispatcherWithTaskPriority(_inspectable.IInspectable):
    get_CurrentPriority: _Callable[[_Pointer[_enum.Windows.UI.Core.CoreDispatcherPriority]],  # value
                                   _type.HRESULT]
    put_CurrentPriority: _Callable[[_enum.Windows.UI.Core.CoreDispatcherPriority],  # value
                                   _type.HRESULT]
    ShouldYield: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    ShouldYieldToPriority: _Callable[[_enum.Windows.UI.Core.CoreDispatcherPriority,  # priority
                                      _Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    StopProcessEvents: _Callable[[],
                                 _type.HRESULT]


class ICoreIndependentInputSourceController(_inspectable.IInspectable):
    get_IsTransparentForUncontrolledInput: _Callable[[_Pointer[_type.boolean]],  # value
                                                     _type.HRESULT]
    put_IsTransparentForUncontrolledInput: _Callable[[_type.boolean],  # value
                                                     _type.HRESULT]
    get_IsPalmRejectionEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_IsPalmRejectionEnabled: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    get_Source: _Callable[[_Pointer[ICoreInputSourceBase]],  # value
                          _type.HRESULT]
    SetControlledInput: _Callable[[_enum.Windows.UI.Core.CoreInputDeviceTypes],  # inputTypes
                                  _type.HRESULT]
    SetControlledInputWithFilters: _Callable[[_enum.Windows.UI.Core.CoreInputDeviceTypes,  # inputTypes
                                              _enum.Windows.UI.Core.CoreIndependentInputFilters,  # required
                                              _enum.Windows.UI.Core.CoreIndependentInputFilters],  # excluded
                                             _type.HRESULT]


class ICoreIndependentInputSourceControllerStatics(_inspectable.IInspectable):
    CreateForVisual: _Callable[[_Windows_UI_Composition.IVisual,  # visual
                                _Pointer[ICoreIndependentInputSourceController]],  # result
                               _type.HRESULT]
    CreateForIVisualElement: _Callable[[_Windows_UI_Composition.IVisualElement,  # visualElement
                                        _Pointer[ICoreIndependentInputSourceController]],  # result
                                       _type.HRESULT]

    _factory = True


class ICoreInputSourceBase(_inspectable.IInspectable):
    get_Dispatcher: _Callable[[_Pointer[ICoreDispatcher]],  # value
                              _type.HRESULT]
    get_IsInputEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    put_IsInputEnabled: _Callable[[_type.boolean],  # value
                                  _type.HRESULT]
    add_InputEnabled: _Callable[[_Windows_Foundation.ITypedEventHandler[_inspectable.IInspectable, IInputEnabledEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # pCookie
                                _type.HRESULT]
    remove_InputEnabled: _Callable[[_struct.EventRegistrationToken],  # cookie
                                   _type.HRESULT]


class ICoreKeyboardInputSource(_inspectable.IInspectable):
    GetCurrentKeyState: _Callable[[_enum.Windows.System.VirtualKey,  # virtualKey
                                   _Pointer[_enum.Windows.UI.Core.CoreVirtualKeyStates]],  # KeyState
                                  _type.HRESULT]
    add_CharacterReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[_inspectable.IInspectable, ICharacterReceivedEventArgs],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # pCookie
                                     _type.HRESULT]
    remove_CharacterReceived: _Callable[[_struct.EventRegistrationToken],  # cookie
                                        _type.HRESULT]
    add_KeyDown: _Callable[[_Windows_Foundation.ITypedEventHandler[_inspectable.IInspectable, IKeyEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # pCookie
                           _type.HRESULT]
    remove_KeyDown: _Callable[[_struct.EventRegistrationToken],  # cookie
                              _type.HRESULT]
    add_KeyUp: _Callable[[_Windows_Foundation.ITypedEventHandler[_inspectable.IInspectable, IKeyEventArgs],  # handler
                          _Pointer[_struct.EventRegistrationToken]],  # pCookie
                         _type.HRESULT]
    remove_KeyUp: _Callable[[_struct.EventRegistrationToken],  # cookie
                            _type.HRESULT]


class ICoreKeyboardInputSource2(_inspectable.IInspectable):
    GetCurrentKeyEventDeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                          _type.HRESULT]


class ICorePointerInputSource(_inspectable.IInspectable):
    ReleasePointerCapture: _Callable[[],
                                     _type.HRESULT]
    SetPointerCapture: _Callable[[],
                                 _type.HRESULT]
    get_HasCapture: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_PointerPosition: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                                   _type.HRESULT]
    get_PointerCursor: _Callable[[_Pointer[ICoreCursor]],  # value
                                 _type.HRESULT]
    put_PointerCursor: _Callable[[ICoreCursor],  # value
                                 _type.HRESULT]
    add_PointerCaptureLost: _Callable[[_Windows_Foundation.ITypedEventHandler[_inspectable.IInspectable, IPointerEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # cookie
                                      _type.HRESULT]
    remove_PointerCaptureLost: _Callable[[_struct.EventRegistrationToken],  # cookie
                                         _type.HRESULT]
    add_PointerEntered: _Callable[[_Windows_Foundation.ITypedEventHandler[_inspectable.IInspectable, IPointerEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # cookie
                                  _type.HRESULT]
    remove_PointerEntered: _Callable[[_struct.EventRegistrationToken],  # cookie
                                     _type.HRESULT]
    add_PointerExited: _Callable[[_Windows_Foundation.ITypedEventHandler[_inspectable.IInspectable, IPointerEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # cookie
                                 _type.HRESULT]
    remove_PointerExited: _Callable[[_struct.EventRegistrationToken],  # cookie
                                    _type.HRESULT]
    add_PointerMoved: _Callable[[_Windows_Foundation.ITypedEventHandler[_inspectable.IInspectable, IPointerEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # cookie
                                _type.HRESULT]
    remove_PointerMoved: _Callable[[_struct.EventRegistrationToken],  # cookie
                                   _type.HRESULT]
    add_PointerPressed: _Callable[[_Windows_Foundation.ITypedEventHandler[_inspectable.IInspectable, IPointerEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # cookie
                                  _type.HRESULT]
    remove_PointerPressed: _Callable[[_struct.EventRegistrationToken],  # cookie
                                     _type.HRESULT]
    add_PointerReleased: _Callable[[_Windows_Foundation.ITypedEventHandler[_inspectable.IInspectable, IPointerEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # cookie
                                   _type.HRESULT]
    remove_PointerReleased: _Callable[[_struct.EventRegistrationToken],  # cookie
                                      _type.HRESULT]
    add_PointerWheelChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[_inspectable.IInspectable, IPointerEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # cookie
                                       _type.HRESULT]
    remove_PointerWheelChanged: _Callable[[_struct.EventRegistrationToken],  # cookie
                                          _type.HRESULT]


class ICorePointerInputSource2(_inspectable.IInspectable):
    get_DispatcherQueue: _Callable[[_Pointer[_Windows_System.IDispatcherQueue]],  # value
                                   _type.HRESULT]


class ICorePointerRedirector(_inspectable.IInspectable):
    add_PointerRoutedAway: _Callable[[_Windows_Foundation.ITypedEventHandler[ICorePointerRedirector, IPointerEventArgs],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # cookie
                                     _type.HRESULT]
    remove_PointerRoutedAway: _Callable[[_struct.EventRegistrationToken],  # cookie
                                        _type.HRESULT]
    add_PointerRoutedTo: _Callable[[_Windows_Foundation.ITypedEventHandler[ICorePointerRedirector, IPointerEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # cookie
                                   _type.HRESULT]
    remove_PointerRoutedTo: _Callable[[_struct.EventRegistrationToken],  # cookie
                                      _type.HRESULT]
    add_PointerRoutedReleased: _Callable[[_Windows_Foundation.ITypedEventHandler[ICorePointerRedirector, IPointerEventArgs],  # handler
                                          _Pointer[_struct.EventRegistrationToken]],  # cookie
                                         _type.HRESULT]
    remove_PointerRoutedReleased: _Callable[[_struct.EventRegistrationToken],  # cookie
                                            _type.HRESULT]


class ICoreTouchHitTesting(_inspectable.IInspectable):
    add_TouchHitTesting: _Callable[[_Windows_Foundation.ITypedEventHandler[_inspectable.IInspectable, ITouchHitTestingEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # pCookie
                                   _type.HRESULT]
    remove_TouchHitTesting: _Callable[[_struct.EventRegistrationToken],  # cookie
                                      _type.HRESULT]


class ICoreWindow(_inspectable.IInspectable):
    get_AutomationHostProvider: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                          _type.HRESULT]
    get_Bounds: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                          _type.HRESULT]
    get_CustomProperties: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                                    _type.HRESULT]
    get_Dispatcher: _Callable[[_Pointer[ICoreDispatcher]],  # value
                              _type.HRESULT]
    get_FlowDirection: _Callable[[_Pointer[_enum.Windows.UI.Core.CoreWindowFlowDirection]],  # value
                                 _type.HRESULT]
    put_FlowDirection: _Callable[[_enum.Windows.UI.Core.CoreWindowFlowDirection],  # value
                                 _type.HRESULT]
    get_IsInputEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    put_IsInputEnabled: _Callable[[_type.boolean],  # value
                                  _type.HRESULT]
    get_PointerCursor: _Callable[[_Pointer[ICoreCursor]],  # value
                                 _type.HRESULT]
    put_PointerCursor: _Callable[[ICoreCursor],  # value
                                 _type.HRESULT]
    get_PointerPosition: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                                   _type.HRESULT]
    get_Visible: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    Activate: _Callable[[],
                        _type.HRESULT]
    Close: _Callable[[],
                     _type.HRESULT]
    GetAsyncKeyState: _Callable[[_enum.Windows.System.VirtualKey,  # virtualKey
                                 _Pointer[_enum.Windows.UI.Core.CoreVirtualKeyStates]],  # KeyState
                                _type.HRESULT]
    GetKeyState: _Callable[[_enum.Windows.System.VirtualKey,  # virtualKey
                            _Pointer[_enum.Windows.UI.Core.CoreVirtualKeyStates]],  # KeyState
                           _type.HRESULT]
    ReleasePointerCapture: _Callable[[],
                                     _type.HRESULT]
    SetPointerCapture: _Callable[[],
                                 _type.HRESULT]
    add_Activated: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWindow, IWindowActivatedEventArgs],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # pCookie
                             _type.HRESULT]
    remove_Activated: _Callable[[_struct.EventRegistrationToken],  # cookie
                                _type.HRESULT]
    add_AutomationProviderRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWindow, IAutomationProviderRequestedEventArgs],  # handler
                                                _Pointer[_struct.EventRegistrationToken]],  # cookie
                                               _type.HRESULT]
    remove_AutomationProviderRequested: _Callable[[_struct.EventRegistrationToken],  # cookie
                                                  _type.HRESULT]
    add_CharacterReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWindow, ICharacterReceivedEventArgs],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # pCookie
                                     _type.HRESULT]
    remove_CharacterReceived: _Callable[[_struct.EventRegistrationToken],  # cookie
                                        _type.HRESULT]
    add_Closed: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWindow, ICoreWindowEventArgs],  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # pCookie
                          _type.HRESULT]
    remove_Closed: _Callable[[_struct.EventRegistrationToken],  # cookie
                             _type.HRESULT]
    add_InputEnabled: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWindow, IInputEnabledEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # pCookie
                                _type.HRESULT]
    remove_InputEnabled: _Callable[[_struct.EventRegistrationToken],  # cookie
                                   _type.HRESULT]
    add_KeyDown: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWindow, IKeyEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # pCookie
                           _type.HRESULT]
    remove_KeyDown: _Callable[[_struct.EventRegistrationToken],  # cookie
                              _type.HRESULT]
    add_KeyUp: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWindow, IKeyEventArgs],  # handler
                          _Pointer[_struct.EventRegistrationToken]],  # pCookie
                         _type.HRESULT]
    remove_KeyUp: _Callable[[_struct.EventRegistrationToken],  # cookie
                            _type.HRESULT]
    add_PointerCaptureLost: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWindow, IPointerEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # cookie
                                      _type.HRESULT]
    remove_PointerCaptureLost: _Callable[[_struct.EventRegistrationToken],  # cookie
                                         _type.HRESULT]
    add_PointerEntered: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWindow, IPointerEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # cookie
                                  _type.HRESULT]
    remove_PointerEntered: _Callable[[_struct.EventRegistrationToken],  # cookie
                                     _type.HRESULT]
    add_PointerExited: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWindow, IPointerEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # cookie
                                 _type.HRESULT]
    remove_PointerExited: _Callable[[_struct.EventRegistrationToken],  # cookie
                                    _type.HRESULT]
    add_PointerMoved: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWindow, IPointerEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # cookie
                                _type.HRESULT]
    remove_PointerMoved: _Callable[[_struct.EventRegistrationToken],  # cookie
                                   _type.HRESULT]
    add_PointerPressed: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWindow, IPointerEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # cookie
                                  _type.HRESULT]
    remove_PointerPressed: _Callable[[_struct.EventRegistrationToken],  # cookie
                                     _type.HRESULT]
    add_PointerReleased: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWindow, IPointerEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # cookie
                                   _type.HRESULT]
    remove_PointerReleased: _Callable[[_struct.EventRegistrationToken],  # cookie
                                      _type.HRESULT]
    add_TouchHitTesting: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWindow, ITouchHitTestingEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # pCookie
                                   _type.HRESULT]
    remove_TouchHitTesting: _Callable[[_struct.EventRegistrationToken],  # cookie
                                      _type.HRESULT]
    add_PointerWheelChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWindow, IPointerEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # cookie
                                       _type.HRESULT]
    remove_PointerWheelChanged: _Callable[[_struct.EventRegistrationToken],  # cookie
                                          _type.HRESULT]
    add_SizeChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWindow, IWindowSizeChangedEventArgs],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # pCookie
                               _type.HRESULT]
    remove_SizeChanged: _Callable[[_struct.EventRegistrationToken],  # cookie
                                  _type.HRESULT]
    add_VisibilityChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWindow, IVisibilityChangedEventArgs],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # pCookie
                                     _type.HRESULT]
    remove_VisibilityChanged: _Callable[[_struct.EventRegistrationToken],  # cookie
                                        _type.HRESULT]


class ICoreWindow2(_inspectable.IInspectable):
    put_PointerPosition: _Callable[[_struct.Windows.Foundation.Point],  # value
                                   _type.HRESULT]


class ICoreWindow3(_inspectable.IInspectable):
    add_ClosestInteractiveBoundsRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWindow, IClosestInteractiveBoundsRequestedEventArgs],  # handler
                                                      _Pointer[_struct.EventRegistrationToken]],  # pCookie
                                                     _type.HRESULT]
    remove_ClosestInteractiveBoundsRequested: _Callable[[_struct.EventRegistrationToken],  # cookie
                                                        _type.HRESULT]
    GetCurrentKeyEventDeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                          _type.HRESULT]


class ICoreWindow4(_inspectable.IInspectable):
    add_ResizeStarted: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWindow, _inspectable.IInspectable],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # pCookie
                                 _type.HRESULT]
    remove_ResizeStarted: _Callable[[_struct.EventRegistrationToken],  # cookie
                                    _type.HRESULT]
    add_ResizeCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWindow, _inspectable.IInspectable],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # pCookie
                                   _type.HRESULT]
    remove_ResizeCompleted: _Callable[[_struct.EventRegistrationToken],  # cookie
                                      _type.HRESULT]


class ICoreWindow5(_inspectable.IInspectable):
    get_DispatcherQueue: _Callable[[_Pointer[_Windows_System.IDispatcherQueue]],  # value
                                   _type.HRESULT]
    get_ActivationMode: _Callable[[_Pointer[_enum.Windows.UI.Core.CoreWindowActivationMode]],  # value
                                  _type.HRESULT]


class ICoreWindowDialog(_inspectable.IInspectable):
    add_Showing: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWindow, ICoreWindowPopupShowingEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # cookie
                           _type.HRESULT]
    remove_Showing: _Callable[[_struct.EventRegistrationToken],  # cookie
                              _type.HRESULT]
    get_MaxSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                           _type.HRESULT]
    get_MinSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                           _type.HRESULT]
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Title: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_IsInteractionDelayed: _Callable[[_Pointer[_type.INT32]],  # value
                                        _type.HRESULT]
    put_IsInteractionDelayed: _Callable[[_type.INT32],  # value
                                        _type.HRESULT]
    get_Commands: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Popups.IUICommand]]],  # value
                            _type.HRESULT]
    get_DefaultCommandIndex: _Callable[[_Pointer[_type.UINT32]],  # value
                                       _type.HRESULT]
    put_DefaultCommandIndex: _Callable[[_type.UINT32],  # value
                                       _type.HRESULT]
    get_CancelCommandIndex: _Callable[[_Pointer[_type.UINT32]],  # value
                                      _type.HRESULT]
    put_CancelCommandIndex: _Callable[[_type.UINT32],  # value
                                      _type.HRESULT]
    get_BackButtonCommand: _Callable[[_Pointer[_Windows_UI_Popups.IUICommandInvokedHandler]],  # value
                                     _type.HRESULT]
    put_BackButtonCommand: _Callable[[_Windows_UI_Popups.IUICommandInvokedHandler],  # value
                                     _type.HRESULT]
    ShowAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_UI_Popups.IUICommand]]],  # asyncInfo
                         _type.HRESULT]


class ICoreWindowDialogFactory(_inspectable.IInspectable):
    CreateWithTitle: _Callable[[_type.HSTRING,  # title
                                _Pointer[ICoreWindowDialog]],  # coreWindowDialog
                               _type.HRESULT]

    _factory = True


class ICoreWindowEventArgs(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class ICoreWindowFlyout(_inspectable.IInspectable):
    add_Showing: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWindow, ICoreWindowPopupShowingEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # cookie
                           _type.HRESULT]
    remove_Showing: _Callable[[_struct.EventRegistrationToken],  # cookie
                              _type.HRESULT]
    get_MaxSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                           _type.HRESULT]
    get_MinSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                           _type.HRESULT]
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Title: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_IsInteractionDelayed: _Callable[[_Pointer[_type.INT32]],  # value
                                        _type.HRESULT]
    put_IsInteractionDelayed: _Callable[[_type.INT32],  # value
                                        _type.HRESULT]
    get_Commands: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Popups.IUICommand]]],  # value
                            _type.HRESULT]
    get_DefaultCommandIndex: _Callable[[_Pointer[_type.UINT32]],  # value
                                       _type.HRESULT]
    put_DefaultCommandIndex: _Callable[[_type.UINT32],  # value
                                       _type.HRESULT]
    get_BackButtonCommand: _Callable[[_Pointer[_Windows_UI_Popups.IUICommandInvokedHandler]],  # value
                                     _type.HRESULT]
    put_BackButtonCommand: _Callable[[_Windows_UI_Popups.IUICommandInvokedHandler],  # value
                                     _type.HRESULT]
    ShowAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_UI_Popups.IUICommand]]],  # asyncInfo
                         _type.HRESULT]


class ICoreWindowFlyoutFactory(_inspectable.IInspectable):
    Create: _Callable[[_struct.Windows.Foundation.Point,  # position
                       _Pointer[ICoreWindowFlyout]],  # coreWindowFlyout
                      _type.HRESULT]
    CreateWithTitle: _Callable[[_struct.Windows.Foundation.Point,  # position
                                _type.HSTRING,  # title
                                _Pointer[ICoreWindowFlyout]],  # coreWindowFlyout
                               _type.HRESULT]

    _factory = True


class ICoreWindowPopupShowingEventArgs(_inspectable.IInspectable):
    SetDesiredSize: _Callable[[_struct.Windows.Foundation.Size],  # value
                              _type.HRESULT]


class ICoreWindowResizeManager(_inspectable.IInspectable):
    NotifyLayoutCompleted: _Callable[[],
                                     _type.HRESULT]


class ICoreWindowResizeManagerLayoutCapability(_inspectable.IInspectable):
    put_ShouldWaitForLayoutCompletion: _Callable[[_type.boolean],  # value
                                                 _type.HRESULT]
    get_ShouldWaitForLayoutCompletion: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]


class ICoreWindowResizeManagerStatics(_inspectable.IInspectable):
    GetForCurrentView: _Callable[[_Pointer[ICoreWindowResizeManager]],  # CoreWindowResizeManager
                                 _type.HRESULT]

    _factory = True


class ICoreWindowStatic(_inspectable.IInspectable):
    GetForCurrentThread: _Callable[[_Pointer[ICoreWindow]],  # ppWindow
                                   _type.HRESULT]

    _factory = True


class ICoreWindowWithContext(_inspectable.IInspectable):
    get_UIContext: _Callable[[_Pointer[_Windows_UI.IUIContext]],  # value
                             _type.HRESULT]


class IIdleDispatchedHandlerArgs(_inspectable.IInspectable):
    get_IsDispatcherIdle: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]


class IInitializeWithCoreWindow(_inspectable.IInspectable):
    Initialize: _Callable[[ICoreWindow],  # window
                          _type.HRESULT]


class IInputEnabledEventArgs(_inspectable.IInspectable):
    get_InputEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]


class IKeyEventArgs(_inspectable.IInspectable):
    get_VirtualKey: _Callable[[_Pointer[_enum.Windows.System.VirtualKey]],  # value
                              _type.HRESULT]
    get_KeyStatus: _Callable[[_Pointer[_struct.Windows.UI.Core.CorePhysicalKeyStatus]],  # value
                             _type.HRESULT]


class IKeyEventArgs2(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]


class IPointerEventArgs(_inspectable.IInspectable):
    get_CurrentPoint: _Callable[[_Pointer[_Windows_UI_Input.IPointerPoint]],  # value
                                _type.HRESULT]
    get_KeyModifiers: _Callable[[_Pointer[_enum.Windows.System.VirtualKeyModifiers]],  # value
                                _type.HRESULT]
    GetIntermediatePoints: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Input.IPointerPoint]]],  # value
                                     _type.HRESULT]


class ISystemNavigationManager(_inspectable.IInspectable):
    add_BackRequested: _Callable[[_Windows_Foundation.IEventHandler[IBackRequestedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_BackRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]


class ISystemNavigationManager2(_inspectable.IInspectable):
    get_AppViewBackButtonVisibility: _Callable[[_Pointer[_enum.Windows.UI.Core.AppViewBackButtonVisibility]],  # value
                                               _type.HRESULT]
    put_AppViewBackButtonVisibility: _Callable[[_enum.Windows.UI.Core.AppViewBackButtonVisibility],  # value
                                               _type.HRESULT]


class ISystemNavigationManagerStatics(_inspectable.IInspectable):
    GetForCurrentView: _Callable[[_Pointer[ISystemNavigationManager]],  # loader
                                 _type.HRESULT]

    _factory = True


class ITouchHitTestingEventArgs(_inspectable.IInspectable):
    get_ProximityEvaluation: _Callable[[_Pointer[_struct.Windows.UI.Core.CoreProximityEvaluation]],  # value
                                       _type.HRESULT]
    put_ProximityEvaluation: _Callable[[_struct.Windows.UI.Core.CoreProximityEvaluation],  # value
                                       _type.HRESULT]
    get_Point: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                         _type.HRESULT]
    get_BoundingBox: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                               _type.HRESULT]
    EvaluateProximityToRect: _Callable[[_struct.Windows.Foundation.Rect,  # controlBoundingBox
                                        _Pointer[_struct.Windows.UI.Core.CoreProximityEvaluation]],  # proximityEvaluation
                                       _type.HRESULT]
    EvaluateProximityToPolygon: _Callable[[_type.UINT32,  # __controlVerticesSize
                                           _Pointer[_struct.Windows.Foundation.Point],  # controlVertices
                                           _Pointer[_struct.Windows.UI.Core.CoreProximityEvaluation]],  # proximityEvaluation
                                          _type.HRESULT]


class IVisibilityChangedEventArgs(_inspectable.IInspectable):
    get_Visible: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]


class IWindowActivatedEventArgs(_inspectable.IInspectable):
    get_WindowActivationState: _Callable[[_Pointer[_enum.Windows.UI.Core.CoreWindowActivationState]],  # value
                                         _type.HRESULT]


class IWindowSizeChangedEventArgs(_inspectable.IInspectable):
    get_Size: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                        _type.HRESULT]
