from __future__ import annotations as _

from typing import Callable as _Callable

from .. import Content as _Microsoft_UI_Content
from .. import Dispatching as _Microsoft_UI_Dispatching
from .... import inspectable as _inspectable
from ....Windows import Foundation as _Windows_Foundation
from ....Windows.Foundation import Collections as _Windows_Foundation_Collections
from ....Windows.UI import Core as _Windows_UI_Core
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class ICharacterReceivedEventArgs(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_KeyCode: _Callable[[_Pointer[_type.UINT32]],  # value
                           _type.HRESULT]
    get_KeyStatus: _Callable[[_Pointer[_struct.Microsoft.UI.Input.PhysicalKeyStatus]],  # value
                             _type.HRESULT]


class IContextMenuKeyEventArgs(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class ICrossSlidingEventArgs(_inspectable.IInspectable):
    get_CrossSlidingState: _Callable[[_Pointer[_enum.Microsoft.UI.Input.CrossSlidingState]],  # value
                                     _type.HRESULT]
    get_PointerDeviceType: _Callable[[_Pointer[_enum.Microsoft.UI.Input.PointerDeviceType]],  # value
                                     _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]


class IDraggingEventArgs(_inspectable.IInspectable):
    get_DraggingState: _Callable[[_Pointer[_enum.Microsoft.UI.Input.DraggingState]],  # value
                                 _type.HRESULT]
    get_PointerDeviceType: _Callable[[_Pointer[_enum.Microsoft.UI.Input.PointerDeviceType]],  # value
                                     _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]


class IFocusChangedEventArgs(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class IGestureRecognizer(_inspectable.IInspectable):
    get_AutoProcessInertia: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_AutoProcessInertia: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    get_CrossSlideExact: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    put_CrossSlideExact: _Callable[[_type.boolean],  # value
                                   _type.HRESULT]
    get_CrossSlideHorizontally: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_CrossSlideHorizontally: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    get_CrossSlideThresholds: _Callable[[_Pointer[_struct.Microsoft.UI.Input.CrossSlideThresholds]],  # value
                                        _type.HRESULT]
    put_CrossSlideThresholds: _Callable[[_struct.Microsoft.UI.Input.CrossSlideThresholds],  # value
                                        _type.HRESULT]
    get_GestureSettings: _Callable[[_Pointer[_enum.Microsoft.UI.Input.GestureSettings]],  # value
                                   _type.HRESULT]
    put_GestureSettings: _Callable[[_enum.Microsoft.UI.Input.GestureSettings],  # value
                                   _type.HRESULT]
    get_IsActive: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_IsInertial: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_PivotCenter: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                               _type.HRESULT]
    put_PivotCenter: _Callable[[_struct.Windows.Foundation.Point],  # value
                               _type.HRESULT]
    get_PivotRadius: _Callable[[_Pointer[_type.FLOAT]],  # value
                               _type.HRESULT]
    put_PivotRadius: _Callable[[_type.FLOAT],  # value
                               _type.HRESULT]
    get_InertiaExpansionDeceleration: _Callable[[_Pointer[_type.FLOAT]],  # value
                                                _type.HRESULT]
    put_InertiaExpansionDeceleration: _Callable[[_type.FLOAT],  # value
                                                _type.HRESULT]
    get_InertiaExpansion: _Callable[[_Pointer[_type.FLOAT]],  # value
                                    _type.HRESULT]
    put_InertiaExpansion: _Callable[[_type.FLOAT],  # value
                                    _type.HRESULT]
    get_InertiaRotationAngle: _Callable[[_Pointer[_type.FLOAT]],  # value
                                        _type.HRESULT]
    put_InertiaRotationAngle: _Callable[[_type.FLOAT],  # value
                                        _type.HRESULT]
    get_InertiaRotationDeceleration: _Callable[[_Pointer[_type.FLOAT]],  # value
                                               _type.HRESULT]
    put_InertiaRotationDeceleration: _Callable[[_type.FLOAT],  # value
                                               _type.HRESULT]
    get_InertiaTranslationDeceleration: _Callable[[_Pointer[_type.FLOAT]],  # value
                                                  _type.HRESULT]
    put_InertiaTranslationDeceleration: _Callable[[_type.FLOAT],  # value
                                                  _type.HRESULT]
    get_InertiaTranslationDisplacement: _Callable[[_Pointer[_type.FLOAT]],  # value
                                                  _type.HRESULT]
    put_InertiaTranslationDisplacement: _Callable[[_type.FLOAT],  # value
                                                  _type.HRESULT]
    get_ManipulationExact: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    put_ManipulationExact: _Callable[[_type.boolean],  # value
                                     _type.HRESULT]
    get_MouseWheelParameters: _Callable[[_Pointer[IMouseWheelParameters]],  # value
                                        _type.HRESULT]
    get_ShowGestureFeedback: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_ShowGestureFeedback: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    CanBeDoubleTap: _Callable[[IPointerPoint,  # value
                               _Pointer[_type.boolean]],  # result
                              _type.HRESULT]
    CompleteGesture: _Callable[[],
                               _type.HRESULT]
    ProcessDownEvent: _Callable[[IPointerPoint],  # value
                                _type.HRESULT]
    ProcessMoveEvents: _Callable[[_Windows_Foundation_Collections.IVector[IPointerPoint]],  # value
                                 _type.HRESULT]
    ProcessMouseWheelEvent: _Callable[[IPointerPoint,  # value
                                       _type.boolean,  # isShiftKeyDown
                                       _type.boolean],  # isControlKeyDown
                                      _type.HRESULT]
    ProcessInertia: _Callable[[],
                              _type.HRESULT]
    ProcessUpEvent: _Callable[[IPointerPoint],  # value
                              _type.HRESULT]
    add_Tapped: _Callable[[_Windows_Foundation.ITypedEventHandler[IGestureRecognizer, ITappedEventArgs],  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Tapped: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    add_RightTapped: _Callable[[_Windows_Foundation.ITypedEventHandler[IGestureRecognizer, IRightTappedEventArgs],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_RightTapped: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    add_Holding: _Callable[[_Windows_Foundation.ITypedEventHandler[IGestureRecognizer, IHoldingEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Holding: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_Dragging: _Callable[[_Windows_Foundation.ITypedEventHandler[IGestureRecognizer, IDraggingEventArgs],  # handler
                             _Pointer[_struct.EventRegistrationToken]],  # token
                            _type.HRESULT]
    remove_Dragging: _Callable[[_struct.EventRegistrationToken],  # token
                               _type.HRESULT]
    add_ManipulationStarted: _Callable[[_Windows_Foundation.ITypedEventHandler[IGestureRecognizer, IManipulationStartedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_ManipulationStarted: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_ManipulationUpdated: _Callable[[_Windows_Foundation.ITypedEventHandler[IGestureRecognizer, IManipulationUpdatedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_ManipulationUpdated: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_ManipulationInertiaStarting: _Callable[[_Windows_Foundation.ITypedEventHandler[IGestureRecognizer, IManipulationInertiaStartingEventArgs],  # handler
                                                _Pointer[_struct.EventRegistrationToken]],  # token
                                               _type.HRESULT]
    remove_ManipulationInertiaStarting: _Callable[[_struct.EventRegistrationToken],  # token
                                                  _type.HRESULT]
    add_ManipulationCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IGestureRecognizer, IManipulationCompletedEventArgs],  # handler
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_ManipulationCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]
    add_CrossSliding: _Callable[[_Windows_Foundation.ITypedEventHandler[IGestureRecognizer, ICrossSlidingEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_CrossSliding: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]


class IHoldingEventArgs(_inspectable.IInspectable):
    get_HoldingState: _Callable[[_Pointer[_enum.Microsoft.UI.Input.HoldingState]],  # value
                                _type.HRESULT]
    get_PointerDeviceType: _Callable[[_Pointer[_enum.Microsoft.UI.Input.PointerDeviceType]],  # value
                                     _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]


class IInputActivationListener(_inspectable.IInspectable):
    get_State: _Callable[[_Pointer[_enum.Microsoft.UI.Input.InputActivationState]],  # value
                         _type.HRESULT]
    add_InputActivationChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IInputActivationListener, IInputActivationListenerActivationChangedEventArgs],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_InputActivationChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]


class IInputActivationListenerActivationChangedEventArgs(_inspectable.IInspectable):
    pass


class IInputActivationListenerStatics(_inspectable.IInspectable, factory=True):
    GetForWindowId: _Callable[[_struct.Microsoft.UI.WindowId,  # windowId
                               _Pointer[IInputActivationListener]],  # result
                              _type.HRESULT]


class IInputActivationListenerStatics2(_inspectable.IInspectable, factory=True):
    GetForIsland: _Callable[[_Microsoft_UI_Content.IContentIsland,  # island
                             _Pointer[IInputActivationListener]],  # result
                            _type.HRESULT]


class IInputCursor(_inspectable.IInspectable):
    pass


class IInputCursorFactory(_inspectable.IInspectable):
    pass


class IInputCursorStatics(_inspectable.IInspectable, factory=True):
    CreateFromCoreCursor: _Callable[[_Windows_UI_Core.ICoreCursor,  # cursor
                                     _Pointer[IInputCursor]],  # result
                                    _type.HRESULT]


class IInputCustomCursor(_inspectable.IInspectable):
    pass


class IInputCustomCursorFactory(_inspectable.IInspectable):
    pass


class IInputDesktopNamedResourceCursor(_inspectable.IInspectable):
    get_ModuleName: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_ResourceName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]


class IInputDesktopNamedResourceCursorStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.HSTRING,  # resourceName
                       _Pointer[IInputDesktopNamedResourceCursor]],  # result
                      _type.HRESULT]
    CreateFromModule: _Callable[[_type.HSTRING,  # moduleName
                                 _type.HSTRING,  # resourceName
                                 _Pointer[IInputDesktopNamedResourceCursor]],  # result
                                _type.HRESULT]


class IInputDesktopResourceCursor(_inspectable.IInspectable):
    get_ModuleName: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_ResourceId: _Callable[[_Pointer[_type.UINT32]],  # value
                              _type.HRESULT]


class IInputDesktopResourceCursorStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.UINT32,  # resourceId
                       _Pointer[IInputDesktopResourceCursor]],  # result
                      _type.HRESULT]
    CreateFromModule: _Callable[[_type.HSTRING,  # moduleName
                                 _type.UINT32,  # resourceId
                                 _Pointer[IInputDesktopResourceCursor]],  # result
                                _type.HRESULT]


class IInputFocusChangedEventArgs(_inspectable.IInspectable):
    pass


class IInputFocusController(_inspectable.IInspectable):
    get_HasFocus: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    TrySetFocus: _Callable[[_Pointer[_type.boolean]],  # result
                           _type.HRESULT]
    add_GotFocus: _Callable[[_Windows_Foundation.ITypedEventHandler[IInputFocusController, IFocusChangedEventArgs],  # handler
                             _Pointer[_struct.EventRegistrationToken]],  # token
                            _type.HRESULT]
    remove_GotFocus: _Callable[[_struct.EventRegistrationToken],  # token
                               _type.HRESULT]
    add_LostFocus: _Callable[[_Windows_Foundation.ITypedEventHandler[IInputFocusController, IFocusChangedEventArgs],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_LostFocus: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]


class IInputFocusControllerStatics(_inspectable.IInspectable, factory=True):
    GetForIsland: _Callable[[_Microsoft_UI_Content.IContentIsland,  # island
                             _Pointer[IInputFocusController]],  # result
                            _type.HRESULT]


class IInputKeyboardSource(_inspectable.IInspectable):
    pass


class IInputKeyboardSource2(_inspectable.IInspectable):
    GetCurrentKeyState: _Callable[[_enum.Windows.System.VirtualKey,  # virtualKey
                                   _Pointer[_enum.Microsoft.UI.Input.VirtualKeyStates]],  # result
                                  _type.HRESULT]
    GetKeyState: _Callable[[_enum.Windows.System.VirtualKey,  # virtualKey
                            _Pointer[_enum.Microsoft.UI.Input.VirtualKeyStates]],  # result
                           _type.HRESULT]
    add_CharacterReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[IInputKeyboardSource, ICharacterReceivedEventArgs],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_CharacterReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    add_ContextMenuKey: _Callable[[_Windows_Foundation.ITypedEventHandler[IInputKeyboardSource, IContextMenuKeyEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_ContextMenuKey: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_KeyDown: _Callable[[_Windows_Foundation.ITypedEventHandler[IInputKeyboardSource, IKeyEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_KeyDown: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_KeyUp: _Callable[[_Windows_Foundation.ITypedEventHandler[IInputKeyboardSource, IKeyEventArgs],  # handler
                          _Pointer[_struct.EventRegistrationToken]],  # token
                         _type.HRESULT]
    remove_KeyUp: _Callable[[_struct.EventRegistrationToken],  # token
                            _type.HRESULT]
    add_SystemKeyDown: _Callable[[_Windows_Foundation.ITypedEventHandler[IInputKeyboardSource, IKeyEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_SystemKeyDown: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_SystemKeyUp: _Callable[[_Windows_Foundation.ITypedEventHandler[IInputKeyboardSource, IKeyEventArgs],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_SystemKeyUp: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]


class IInputKeyboardSourceStatics(_inspectable.IInspectable, factory=True):
    GetKeyStateForCurrentThread: _Callable[[_enum.Windows.System.VirtualKey,  # virtualKey
                                            _Pointer[_enum.Windows.UI.Core.CoreVirtualKeyStates]],  # result
                                           _type.HRESULT]


class IInputKeyboardSourceStatics2(_inspectable.IInspectable, factory=True):
    GetForIsland: _Callable[[_Microsoft_UI_Content.IContentIsland,  # island
                             _Pointer[IInputKeyboardSource]],  # result
                            _type.HRESULT]


class IInputLightDismissAction(_inspectable.IInspectable):
    add_Dismissed: _Callable[[_Windows_Foundation.ITypedEventHandler[IInputLightDismissAction, IInputLightDismissEventArgs],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_Dismissed: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]


class IInputLightDismissActionStatics(_inspectable.IInspectable, factory=True):
    GetForWindowId: _Callable[[_struct.Microsoft.UI.WindowId,  # windowId
                               _Pointer[IInputLightDismissAction]],  # result
                              _type.HRESULT]


class IInputLightDismissEventArgs(_inspectable.IInspectable):
    pass


class IInputNonClientPointerSource(_inspectable.IInspectable):
    get_DispatcherQueue: _Callable[[_Pointer[_Microsoft_UI_Dispatching.IDispatcherQueue]],  # value
                                   _type.HRESULT]
    ClearAllRegionRects: _Callable[[],
                                   _type.HRESULT]
    ClearRegionRects: _Callable[[_enum.Microsoft.UI.Input.NonClientRegionKind],  # region
                                _type.HRESULT]
    GetRegionRects: _Callable[[_enum.Microsoft.UI.Input.NonClientRegionKind,  # region
                               _Pointer[_type.UINT32],  # __resultSize
                               _Pointer[_Pointer[_struct.Windows.Graphics.RectInt32]]],  # result
                              _type.HRESULT]
    SetRegionRects: _Callable[[_enum.Microsoft.UI.Input.NonClientRegionKind,  # region
                               _type.UINT32,  # __rectsSize
                               _Pointer[_struct.Windows.Graphics.RectInt32]],  # rects
                              _type.HRESULT]
    add_CaptionTapped: _Callable[[_Windows_Foundation.ITypedEventHandler[IInputNonClientPointerSource, INonClientCaptionTappedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_CaptionTapped: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_PointerEntered: _Callable[[_Windows_Foundation.ITypedEventHandler[IInputNonClientPointerSource, INonClientPointerEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_PointerEntered: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_PointerExited: _Callable[[_Windows_Foundation.ITypedEventHandler[IInputNonClientPointerSource, INonClientPointerEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_PointerExited: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_PointerMoved: _Callable[[_Windows_Foundation.ITypedEventHandler[IInputNonClientPointerSource, INonClientPointerEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_PointerMoved: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    add_PointerPressed: _Callable[[_Windows_Foundation.ITypedEventHandler[IInputNonClientPointerSource, INonClientPointerEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_PointerPressed: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_PointerReleased: _Callable[[_Windows_Foundation.ITypedEventHandler[IInputNonClientPointerSource, INonClientPointerEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_PointerReleased: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    add_RegionsChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IInputNonClientPointerSource, INonClientRegionsChangedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_RegionsChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]


class IInputNonClientPointerSourceStatics(_inspectable.IInspectable, factory=True):
    GetForWindowId: _Callable[[_struct.Microsoft.UI.WindowId,  # windowId
                               _Pointer[IInputNonClientPointerSource]],  # result
                              _type.HRESULT]


class IInputObject(_inspectable.IInspectable):
    get_DispatcherQueue: _Callable[[_Pointer[_Microsoft_UI_Dispatching.IDispatcherQueue]],  # value
                                   _type.HRESULT]


class IInputObjectFactory(_inspectable.IInspectable):
    pass


class IInputPointerSource(_inspectable.IInspectable):
    get_Cursor: _Callable[[_Pointer[IInputCursor]],  # value
                          _type.HRESULT]
    put_Cursor: _Callable[[IInputCursor],  # value
                          _type.HRESULT]
    get_DeviceKinds: _Callable[[_Pointer[_enum.Microsoft.UI.Input.InputPointerSourceDeviceKinds]],  # value
                               _type.HRESULT]
    add_PointerCaptureLost: _Callable[[_Windows_Foundation.ITypedEventHandler[IInputPointerSource, IPointerEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_PointerCaptureLost: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_PointerEntered: _Callable[[_Windows_Foundation.ITypedEventHandler[IInputPointerSource, IPointerEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_PointerEntered: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_PointerExited: _Callable[[_Windows_Foundation.ITypedEventHandler[IInputPointerSource, IPointerEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_PointerExited: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_PointerMoved: _Callable[[_Windows_Foundation.ITypedEventHandler[IInputPointerSource, IPointerEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_PointerMoved: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    add_PointerPressed: _Callable[[_Windows_Foundation.ITypedEventHandler[IInputPointerSource, IPointerEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_PointerPressed: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_PointerReleased: _Callable[[_Windows_Foundation.ITypedEventHandler[IInputPointerSource, IPointerEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_PointerReleased: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    add_PointerRoutedAway: _Callable[[_Windows_Foundation.ITypedEventHandler[IInputPointerSource, IPointerEventArgs],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_PointerRoutedAway: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    add_PointerRoutedReleased: _Callable[[_Windows_Foundation.ITypedEventHandler[IInputPointerSource, IPointerEventArgs],  # handler
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_PointerRoutedReleased: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]
    add_PointerRoutedTo: _Callable[[_Windows_Foundation.ITypedEventHandler[IInputPointerSource, IPointerEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_PointerRoutedTo: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    add_PointerWheelChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IInputPointerSource, IPointerEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_PointerWheelChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]


class IInputPointerSourceStatics(_inspectable.IInspectable, factory=True):
    GetForIsland: _Callable[[_Microsoft_UI_Content.IContentIsland,  # island
                             _Pointer[IInputPointerSource]],  # result
                            _type.HRESULT]


class IInputPreTranslateKeyboardSource(_inspectable.IInspectable):
    pass


class IInputPreTranslateKeyboardSourceStatics(_inspectable.IInspectable, factory=True):
    GetForIsland: _Callable[[_Microsoft_UI_Content.IContentIsland,  # island
                             _Pointer[IInputPreTranslateKeyboardSource]],  # result
                            _type.HRESULT]


class IInputSystemCursor(_inspectable.IInspectable):
    get_CursorShape: _Callable[[_Pointer[_enum.Microsoft.UI.Input.InputSystemCursorShape]],  # value
                               _type.HRESULT]


class IInputSystemCursorStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_enum.Microsoft.UI.Input.InputSystemCursorShape,  # type
                       _Pointer[IInputSystemCursor]],  # result
                      _type.HRESULT]


class IKeyEventArgs(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_KeyStatus: _Callable[[_Pointer[_struct.Microsoft.UI.Input.PhysicalKeyStatus]],  # value
                             _type.HRESULT]
    get_Timestamp: _Callable[[_Pointer[_type.UINT64]],  # value
                             _type.HRESULT]
    get_VirtualKey: _Callable[[_Pointer[_enum.Windows.System.VirtualKey]],  # value
                              _type.HRESULT]


class IManipulationCompletedEventArgs(_inspectable.IInspectable):
    get_Cumulative: _Callable[[_Pointer[_struct.Microsoft.UI.Input.ManipulationDelta]],  # value
                              _type.HRESULT]
    get_PointerDeviceType: _Callable[[_Pointer[_enum.Microsoft.UI.Input.PointerDeviceType]],  # value
                                     _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    get_Velocities: _Callable[[_Pointer[_struct.Microsoft.UI.Input.ManipulationVelocities]],  # value
                              _type.HRESULT]


class IManipulationInertiaStartingEventArgs(_inspectable.IInspectable):
    get_Cumulative: _Callable[[_Pointer[_struct.Microsoft.UI.Input.ManipulationDelta]],  # value
                              _type.HRESULT]
    get_Delta: _Callable[[_Pointer[_struct.Microsoft.UI.Input.ManipulationDelta]],  # value
                         _type.HRESULT]
    get_PointerDeviceType: _Callable[[_Pointer[_enum.Microsoft.UI.Input.PointerDeviceType]],  # value
                                     _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    get_Velocities: _Callable[[_Pointer[_struct.Microsoft.UI.Input.ManipulationVelocities]],  # value
                              _type.HRESULT]


class IManipulationStartedEventArgs(_inspectable.IInspectable):
    get_Cumulative: _Callable[[_Pointer[_struct.Microsoft.UI.Input.ManipulationDelta]],  # value
                              _type.HRESULT]
    get_PointerDeviceType: _Callable[[_Pointer[_enum.Microsoft.UI.Input.PointerDeviceType]],  # value
                                     _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]


class IManipulationUpdatedEventArgs(_inspectable.IInspectable):
    get_Cumulative: _Callable[[_Pointer[_struct.Microsoft.UI.Input.ManipulationDelta]],  # value
                              _type.HRESULT]
    get_Delta: _Callable[[_Pointer[_struct.Microsoft.UI.Input.ManipulationDelta]],  # value
                         _type.HRESULT]
    get_PointerDeviceType: _Callable[[_Pointer[_enum.Microsoft.UI.Input.PointerDeviceType]],  # value
                                     _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    get_Velocities: _Callable[[_Pointer[_struct.Microsoft.UI.Input.ManipulationVelocities]],  # value
                              _type.HRESULT]


class IMouseWheelParameters(_inspectable.IInspectable):
    get_CharTranslation: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                                   _type.HRESULT]
    put_CharTranslation: _Callable[[_struct.Windows.Foundation.Point],  # value
                                   _type.HRESULT]
    get_DeltaScale: _Callable[[_Pointer[_type.FLOAT]],  # value
                              _type.HRESULT]
    put_DeltaScale: _Callable[[_type.FLOAT],  # value
                              _type.HRESULT]
    get_DeltaRotationAngle: _Callable[[_Pointer[_type.FLOAT]],  # value
                                      _type.HRESULT]
    put_DeltaRotationAngle: _Callable[[_type.FLOAT],  # value
                                      _type.HRESULT]
    get_PageTranslation: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                                   _type.HRESULT]
    put_PageTranslation: _Callable[[_struct.Windows.Foundation.Point],  # value
                                   _type.HRESULT]


class INonClientCaptionTappedEventArgs(_inspectable.IInspectable):
    get_Point: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                         _type.HRESULT]
    get_PointerDeviceType: _Callable[[_Pointer[_enum.Microsoft.UI.Input.PointerDeviceType]],  # value
                                     _type.HRESULT]


class INonClientPointerEventArgs(_inspectable.IInspectable):
    get_Point: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                         _type.HRESULT]
    get_PointerDeviceType: _Callable[[_Pointer[_enum.Microsoft.UI.Input.PointerDeviceType]],  # value
                                     _type.HRESULT]
    get_RegionKind: _Callable[[_Pointer[_enum.Microsoft.UI.Input.NonClientRegionKind]],  # value
                              _type.HRESULT]
    get_IsPointInRegion: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]


class INonClientRegionsChangedEventArgs(_inspectable.IInspectable):
    get_ChangedRegions: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                                   _Pointer[_Pointer[_enum.Microsoft.UI.Input.NonClientRegionKind]]],  # value
                                  _type.HRESULT]


class IPointerEventArgs(_inspectable.IInspectable):
    get_CurrentPoint: _Callable[[_Pointer[IPointerPoint]],  # value
                                _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_KeyModifiers: _Callable[[_Pointer[_enum.Windows.System.VirtualKeyModifiers]],  # value
                                _type.HRESULT]
    GetIntermediatePoints: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IPointerPoint]]],  # result
                                     _type.HRESULT]
    GetIntermediateTransformedPoints: _Callable[[IPointerPointTransform,  # transform
                                                 _Pointer[_Windows_Foundation_Collections.IVector[IPointerPoint]]],  # result
                                                _type.HRESULT]


class IPointerPoint(_inspectable.IInspectable):
    get_FrameId: _Callable[[_Pointer[_type.UINT32]],  # value
                           _type.HRESULT]
    get_IsInContact: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_PointerDeviceType: _Callable[[_Pointer[_enum.Microsoft.UI.Input.PointerDeviceType]],  # value
                                     _type.HRESULT]
    get_PointerId: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    get_Properties: _Callable[[_Pointer[IPointerPointProperties]],  # value
                              _type.HRESULT]
    get_Timestamp: _Callable[[_Pointer[_type.UINT64]],  # value
                             _type.HRESULT]
    GetTransformedPoint: _Callable[[IPointerPointTransform,  # transform
                                    _Pointer[IPointerPoint]],  # result
                                   _type.HRESULT]


class IPointerPointProperties(_inspectable.IInspectable):
    get_ContactRect: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                               _type.HRESULT]
    get_IsBarrelButtonPressed: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    get_IsCanceled: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_IsEraser: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_IsHorizontalMouseWheel: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    get_IsInRange: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_IsInverted: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_IsLeftButtonPressed: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    get_IsMiddleButtonPressed: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    get_IsPrimary: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_IsRightButtonPressed: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_IsXButton1Pressed: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    get_IsXButton2Pressed: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    get_MouseWheelDelta: _Callable[[_Pointer[_type.INT32]],  # value
                                   _type.HRESULT]
    get_Orientation: _Callable[[_Pointer[_type.FLOAT]],  # value
                               _type.HRESULT]
    get_PointerUpdateKind: _Callable[[_Pointer[_enum.Microsoft.UI.Input.PointerUpdateKind]],  # value
                                     _type.HRESULT]
    get_Pressure: _Callable[[_Pointer[_type.FLOAT]],  # value
                            _type.HRESULT]
    get_TouchConfidence: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_Twist: _Callable[[_Pointer[_type.FLOAT]],  # value
                         _type.HRESULT]
    get_XTilt: _Callable[[_Pointer[_type.FLOAT]],  # value
                         _type.HRESULT]
    get_YTilt: _Callable[[_Pointer[_type.FLOAT]],  # value
                         _type.HRESULT]


class IPointerPointTransform(_inspectable.IInspectable):
    get_Inverse: _Callable[[_Pointer[IPointerPointTransform]],  # value
                           _type.HRESULT]
    TryTransform: _Callable[[_struct.Windows.Foundation.Point,  # inPoint
                             _Pointer[_struct.Windows.Foundation.Point],  # outPoint
                             _Pointer[_type.boolean]],  # result
                            _type.HRESULT]
    TryTransformBounds: _Callable[[_struct.Windows.Foundation.Rect,  # inRect
                                   _Pointer[_struct.Windows.Foundation.Rect],  # outRect
                                   _Pointer[_type.boolean]],  # result
                                  _type.HRESULT]


class IPointerPredictor(_inspectable.IInspectable):
    get_PredictionTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                  _type.HRESULT]
    put_PredictionTime: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                  _type.HRESULT]
    GetPredictedPoints: _Callable[[IPointerPoint,  # point
                                   _Pointer[_type.UINT32],  # __resultSize
                                   _Pointer[_Pointer[IPointerPoint]]],  # result
                                  _type.HRESULT]


class IPointerPredictorStatics(_inspectable.IInspectable, factory=True):
    CreateForInputPointerSource: _Callable[[IInputPointerSource,  # inputPointerSource
                                            _Pointer[IPointerPredictor]],  # result
                                           _type.HRESULT]


class IRightTappedEventArgs(_inspectable.IInspectable):
    get_PointerDeviceType: _Callable[[_Pointer[_enum.Microsoft.UI.Input.PointerDeviceType]],  # value
                                     _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]


class ITappedEventArgs(_inspectable.IInspectable):
    get_PointerDeviceType: _Callable[[_Pointer[_enum.Microsoft.UI.Input.PointerDeviceType]],  # value
                                     _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    get_TapCount: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
