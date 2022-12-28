from __future__ import annotations as _

from typing import Callable as _Callable

from .. import Core as _Windows_UI_Core
from ... import Foundation as _Windows_Foundation
from ... import System as _Windows_System
from ...Devices import Haptics as _Windows_Devices_Haptics
from ...Devices import Input as _Windows_Devices_Input
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IAttachableInputObject(_inspectable.IInspectable):
    pass


class IAttachableInputObjectFactory(_inspectable.IInspectable):
    pass


class ICrossSlidingEventArgs(_inspectable.IInspectable):
    get_PointerDeviceType: _Callable[[_Pointer[_enum.Windows.Devices.Input.PointerDeviceType]],  # value
                                     _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    get_CrossSlidingState: _Callable[[_Pointer[_enum.Windows.UI.Input.CrossSlidingState]],  # value
                                     _type.HRESULT]


class ICrossSlidingEventArgs2(_inspectable.IInspectable):
    get_ContactCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]


class IDraggingEventArgs(_inspectable.IInspectable):
    get_PointerDeviceType: _Callable[[_Pointer[_enum.Windows.Devices.Input.PointerDeviceType]],  # value
                                     _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    get_DraggingState: _Callable[[_Pointer[_enum.Windows.UI.Input.DraggingState]],  # value
                                 _type.HRESULT]


class IDraggingEventArgs2(_inspectable.IInspectable):
    get_ContactCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]


class IEdgeGesture(_inspectable.IInspectable):
    add_Starting: _Callable[[_Windows_Foundation.ITypedEventHandler[IEdgeGesture, IEdgeGestureEventArgs],  # handler
                             _Pointer[_struct.EventRegistrationToken]],  # token
                            _type.HRESULT]
    remove_Starting: _Callable[[_struct.EventRegistrationToken],  # token
                               _type.HRESULT]
    add_Completed: _Callable[[_Windows_Foundation.ITypedEventHandler[IEdgeGesture, IEdgeGestureEventArgs],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_Completed: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    add_Canceled: _Callable[[_Windows_Foundation.ITypedEventHandler[IEdgeGesture, IEdgeGestureEventArgs],  # handler
                             _Pointer[_struct.EventRegistrationToken]],  # token
                            _type.HRESULT]
    remove_Canceled: _Callable[[_struct.EventRegistrationToken],  # token
                               _type.HRESULT]


class IEdgeGestureEventArgs(_inspectable.IInspectable):
    get_Kind: _Callable[[_Pointer[_enum.Windows.UI.Input.EdgeGestureKind]],  # value
                        _type.HRESULT]


class IEdgeGestureStatics(_inspectable.IInspectable):
    GetForCurrentView: _Callable[[_Pointer[IEdgeGesture]],  # current
                                 _type.HRESULT]

    _factory = True


class IGestureRecognizer(_inspectable.IInspectable):
    get_GestureSettings: _Callable[[_Pointer[_enum.Windows.UI.Input.GestureSettings]],  # value
                                   _type.HRESULT]
    put_GestureSettings: _Callable[[_enum.Windows.UI.Input.GestureSettings],  # value
                                   _type.HRESULT]
    get_IsInertial: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_IsActive: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_ShowGestureFeedback: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_ShowGestureFeedback: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_PivotCenter: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                               _type.HRESULT]
    put_PivotCenter: _Callable[[_struct.Windows.Foundation.Point],  # value
                               _type.HRESULT]
    get_PivotRadius: _Callable[[_Pointer[_type.FLOAT]],  # value
                               _type.HRESULT]
    put_PivotRadius: _Callable[[_type.FLOAT],  # value
                               _type.HRESULT]
    get_InertiaTranslationDeceleration: _Callable[[_Pointer[_type.FLOAT]],  # value
                                                  _type.HRESULT]
    put_InertiaTranslationDeceleration: _Callable[[_type.FLOAT],  # value
                                                  _type.HRESULT]
    get_InertiaRotationDeceleration: _Callable[[_Pointer[_type.FLOAT]],  # value
                                               _type.HRESULT]
    put_InertiaRotationDeceleration: _Callable[[_type.FLOAT],  # value
                                               _type.HRESULT]
    get_InertiaExpansionDeceleration: _Callable[[_Pointer[_type.FLOAT]],  # value
                                                _type.HRESULT]
    put_InertiaExpansionDeceleration: _Callable[[_type.FLOAT],  # value
                                                _type.HRESULT]
    get_InertiaTranslationDisplacement: _Callable[[_Pointer[_type.FLOAT]],  # value
                                                  _type.HRESULT]
    put_InertiaTranslationDisplacement: _Callable[[_type.FLOAT],  # value
                                                  _type.HRESULT]
    get_InertiaRotationAngle: _Callable[[_Pointer[_type.FLOAT]],  # value
                                        _type.HRESULT]
    put_InertiaRotationAngle: _Callable[[_type.FLOAT],  # value
                                        _type.HRESULT]
    get_InertiaExpansion: _Callable[[_Pointer[_type.FLOAT]],  # value
                                    _type.HRESULT]
    put_InertiaExpansion: _Callable[[_type.FLOAT],  # value
                                    _type.HRESULT]
    get_ManipulationExact: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    put_ManipulationExact: _Callable[[_type.boolean],  # value
                                     _type.HRESULT]
    get_CrossSlideThresholds: _Callable[[_Pointer[_struct.Windows.UI.Input.CrossSlideThresholds]],  # value
                                        _type.HRESULT]
    put_CrossSlideThresholds: _Callable[[_struct.Windows.UI.Input.CrossSlideThresholds],  # value
                                        _type.HRESULT]
    get_CrossSlideHorizontally: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_CrossSlideHorizontally: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    get_CrossSlideExact: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    put_CrossSlideExact: _Callable[[_type.boolean],  # value
                                   _type.HRESULT]
    get_AutoProcessInertia: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_AutoProcessInertia: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    get_MouseWheelParameters: _Callable[[_Pointer[IMouseWheelParameters]],  # value
                                        _type.HRESULT]
    CanBeDoubleTap: _Callable[[IPointerPoint,  # value
                               _Pointer[_type.boolean]],  # result
                              _type.HRESULT]
    ProcessDownEvent: _Callable[[IPointerPoint],  # value
                                _type.HRESULT]
    ProcessMoveEvents: _Callable[[_Windows_Foundation_Collections.IVector[IPointerPoint]],  # value
                                 _type.HRESULT]
    ProcessUpEvent: _Callable[[IPointerPoint],  # value
                              _type.HRESULT]
    ProcessMouseWheelEvent: _Callable[[IPointerPoint,  # value
                                       _type.boolean,  # isShiftKeyDown
                                       _type.boolean],  # isControlKeyDown
                                      _type.HRESULT]
    ProcessInertia: _Callable[[],
                              _type.HRESULT]
    CompleteGesture: _Callable[[],
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


class IGestureRecognizer2(_inspectable.IInspectable):
    get_TapMinContactCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                      _type.HRESULT]
    put_TapMinContactCount: _Callable[[_type.UINT32],  # value
                                      _type.HRESULT]
    get_TapMaxContactCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                      _type.HRESULT]
    put_TapMaxContactCount: _Callable[[_type.UINT32],  # value
                                      _type.HRESULT]
    get_HoldMinContactCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                       _type.HRESULT]
    put_HoldMinContactCount: _Callable[[_type.UINT32],  # value
                                       _type.HRESULT]
    get_HoldMaxContactCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                       _type.HRESULT]
    put_HoldMaxContactCount: _Callable[[_type.UINT32],  # value
                                       _type.HRESULT]
    get_HoldRadius: _Callable[[_Pointer[_type.FLOAT]],  # value
                              _type.HRESULT]
    put_HoldRadius: _Callable[[_type.FLOAT],  # value
                              _type.HRESULT]
    get_HoldStartDelay: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                  _type.HRESULT]
    put_HoldStartDelay: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                  _type.HRESULT]
    get_TranslationMinContactCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                              _type.HRESULT]
    put_TranslationMinContactCount: _Callable[[_type.UINT32],  # value
                                              _type.HRESULT]
    get_TranslationMaxContactCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                              _type.HRESULT]
    put_TranslationMaxContactCount: _Callable[[_type.UINT32],  # value
                                              _type.HRESULT]


class IHoldingEventArgs(_inspectable.IInspectable):
    get_PointerDeviceType: _Callable[[_Pointer[_enum.Windows.Devices.Input.PointerDeviceType]],  # value
                                     _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    get_HoldingState: _Callable[[_Pointer[_enum.Windows.UI.Input.HoldingState]],  # value
                                _type.HRESULT]


class IHoldingEventArgs2(_inspectable.IInspectable):
    get_ContactCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]
    get_CurrentContactCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                       _type.HRESULT]


class IInputActivationListener(_inspectable.IInspectable):
    get_State: _Callable[[_Pointer[_enum.Windows.UI.Input.InputActivationState]],  # value
                         _type.HRESULT]
    add_InputActivationChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IInputActivationListener, IInputActivationListenerActivationChangedEventArgs],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_InputActivationChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]


class IInputActivationListenerActivationChangedEventArgs(_inspectable.IInspectable):
    get_State: _Callable[[_Pointer[_enum.Windows.UI.Input.InputActivationState]],  # value
                         _type.HRESULT]


class IKeyboardDeliveryInterceptor(_inspectable.IInspectable):
    get_IsInterceptionEnabledWhenInForeground: _Callable[[_Pointer[_type.boolean]],  # value
                                                         _type.HRESULT]
    put_IsInterceptionEnabledWhenInForeground: _Callable[[_type.boolean],  # value
                                                         _type.HRESULT]
    add_KeyDown: _Callable[[_Windows_Foundation.ITypedEventHandler[IKeyboardDeliveryInterceptor, _Windows_UI_Core.IKeyEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_KeyDown: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_KeyUp: _Callable[[_Windows_Foundation.ITypedEventHandler[IKeyboardDeliveryInterceptor, _Windows_UI_Core.IKeyEventArgs],  # handler
                          _Pointer[_struct.EventRegistrationToken]],  # token
                         _type.HRESULT]
    remove_KeyUp: _Callable[[_struct.EventRegistrationToken],  # token
                            _type.HRESULT]


class IKeyboardDeliveryInterceptorStatics(_inspectable.IInspectable):
    GetForCurrentView: _Callable[[_Pointer[IKeyboardDeliveryInterceptor]],  # keyboardDeliverySettings
                                 _type.HRESULT]

    _factory = True


class IManipulationCompletedEventArgs(_inspectable.IInspectable):
    get_PointerDeviceType: _Callable[[_Pointer[_enum.Windows.Devices.Input.PointerDeviceType]],  # value
                                     _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    get_Cumulative: _Callable[[_Pointer[_struct.Windows.UI.Input.ManipulationDelta]],  # value
                              _type.HRESULT]
    get_Velocities: _Callable[[_Pointer[_struct.Windows.UI.Input.ManipulationVelocities]],  # value
                              _type.HRESULT]


class IManipulationCompletedEventArgs2(_inspectable.IInspectable):
    get_ContactCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]
    get_CurrentContactCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                       _type.HRESULT]


class IManipulationInertiaStartingEventArgs(_inspectable.IInspectable):
    get_PointerDeviceType: _Callable[[_Pointer[_enum.Windows.Devices.Input.PointerDeviceType]],  # value
                                     _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    get_Delta: _Callable[[_Pointer[_struct.Windows.UI.Input.ManipulationDelta]],  # value
                         _type.HRESULT]
    get_Cumulative: _Callable[[_Pointer[_struct.Windows.UI.Input.ManipulationDelta]],  # value
                              _type.HRESULT]
    get_Velocities: _Callable[[_Pointer[_struct.Windows.UI.Input.ManipulationVelocities]],  # value
                              _type.HRESULT]


class IManipulationInertiaStartingEventArgs2(_inspectable.IInspectable):
    get_ContactCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]


class IManipulationStartedEventArgs(_inspectable.IInspectable):
    get_PointerDeviceType: _Callable[[_Pointer[_enum.Windows.Devices.Input.PointerDeviceType]],  # value
                                     _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    get_Cumulative: _Callable[[_Pointer[_struct.Windows.UI.Input.ManipulationDelta]],  # value
                              _type.HRESULT]


class IManipulationStartedEventArgs2(_inspectable.IInspectable):
    get_ContactCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]


class IManipulationUpdatedEventArgs(_inspectable.IInspectable):
    get_PointerDeviceType: _Callable[[_Pointer[_enum.Windows.Devices.Input.PointerDeviceType]],  # value
                                     _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    get_Delta: _Callable[[_Pointer[_struct.Windows.UI.Input.ManipulationDelta]],  # value
                         _type.HRESULT]
    get_Cumulative: _Callable[[_Pointer[_struct.Windows.UI.Input.ManipulationDelta]],  # value
                              _type.HRESULT]
    get_Velocities: _Callable[[_Pointer[_struct.Windows.UI.Input.ManipulationVelocities]],  # value
                              _type.HRESULT]


class IManipulationUpdatedEventArgs2(_inspectable.IInspectable):
    get_ContactCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]
    get_CurrentContactCount: _Callable[[_Pointer[_type.UINT32]],  # value
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


class IPointerPoint(_inspectable.IInspectable):
    get_PointerDevice: _Callable[[_Pointer[_Windows_Devices_Input.IPointerDevice]],  # value
                                 _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    get_RawPosition: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                               _type.HRESULT]
    get_PointerId: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    get_FrameId: _Callable[[_Pointer[_type.UINT32]],  # value
                           _type.HRESULT]
    get_Timestamp: _Callable[[_Pointer[_type.UINT64]],  # value
                             _type.HRESULT]
    get_IsInContact: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_Properties: _Callable[[_Pointer[IPointerPointProperties]],  # value
                              _type.HRESULT]


class IPointerPointProperties(_inspectable.IInspectable):
    get_Pressure: _Callable[[_Pointer[_type.FLOAT]],  # value
                            _type.HRESULT]
    get_IsInverted: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_IsEraser: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_Orientation: _Callable[[_Pointer[_type.FLOAT]],  # value
                               _type.HRESULT]
    get_XTilt: _Callable[[_Pointer[_type.FLOAT]],  # value
                         _type.HRESULT]
    get_YTilt: _Callable[[_Pointer[_type.FLOAT]],  # value
                         _type.HRESULT]
    get_Twist: _Callable[[_Pointer[_type.FLOAT]],  # value
                         _type.HRESULT]
    get_ContactRect: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                               _type.HRESULT]
    get_ContactRectRaw: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                                  _type.HRESULT]
    get_TouchConfidence: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_IsLeftButtonPressed: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    get_IsRightButtonPressed: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_IsMiddleButtonPressed: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    get_MouseWheelDelta: _Callable[[_Pointer[_type.INT32]],  # value
                                   _type.HRESULT]
    get_IsHorizontalMouseWheel: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    get_IsPrimary: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_IsInRange: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_IsCanceled: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_IsBarrelButtonPressed: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    get_IsXButton1Pressed: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    get_IsXButton2Pressed: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    get_PointerUpdateKind: _Callable[[_Pointer[_enum.Windows.UI.Input.PointerUpdateKind]],  # value
                                     _type.HRESULT]
    HasUsage: _Callable[[_type.UINT32,  # usagePage
                         _type.UINT32,  # usageId
                         _Pointer[_type.boolean]],  # value
                        _type.HRESULT]
    GetUsageValue: _Callable[[_type.UINT32,  # usagePage
                              _type.UINT32,  # usageId
                              _Pointer[_type.INT32]],  # value
                             _type.HRESULT]


class IPointerPointProperties2(_inspectable.IInspectable):
    get_ZDistance: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.FLOAT]]],  # value
                             _type.HRESULT]


class IPointerPointStatics(_inspectable.IInspectable):
    GetCurrentPoint: _Callable[[_type.UINT32,  # pointerId
                                _Pointer[IPointerPoint]],  # pointerPoint
                               _type.HRESULT]
    GetIntermediatePoints: _Callable[[_type.UINT32,  # pointerId
                                      _Pointer[_Windows_Foundation_Collections.IVector[IPointerPoint]]],  # pointerPoints
                                     _type.HRESULT]
    GetCurrentPointTransformed: _Callable[[_type.UINT32,  # pointerId
                                           IPointerPointTransform,  # transform
                                           _Pointer[IPointerPoint]],  # pointerPoint
                                          _type.HRESULT]
    GetIntermediatePointsTransformed: _Callable[[_type.UINT32,  # pointerId
                                                 IPointerPointTransform,  # transform
                                                 _Pointer[_Windows_Foundation_Collections.IVector[IPointerPoint]]],  # pointerPoints
                                                _type.HRESULT]

    _factory = True


class IPointerPointTransform(_inspectable.IInspectable):
    get_Inverse: _Callable[[_Pointer[IPointerPointTransform]],  # value
                           _type.HRESULT]
    TryTransform: _Callable[[_struct.Windows.Foundation.Point,  # inPoint
                             _Pointer[_struct.Windows.Foundation.Point],  # outPoint
                             _Pointer[_type.boolean]],  # returnValue
                            _type.HRESULT]
    TransformBounds: _Callable[[_struct.Windows.Foundation.Rect,  # rect
                                _Pointer[_struct.Windows.Foundation.Rect]],  # returnValue
                               _type.HRESULT]


class IPointerVisualizationSettings(_inspectable.IInspectable):
    put_IsContactFeedbackEnabled: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]
    get_IsContactFeedbackEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_IsBarrelButtonFeedbackEnabled: _Callable[[_type.boolean],  # value
                                                 _type.HRESULT]
    get_IsBarrelButtonFeedbackEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]


class IPointerVisualizationSettingsStatics(_inspectable.IInspectable):
    GetForCurrentView: _Callable[[_Pointer[IPointerVisualizationSettings]],  # visualizationSettings
                                 _type.HRESULT]

    _factory = True


class IRadialController(_inspectable.IInspectable):
    get_Menu: _Callable[[_Pointer[IRadialControllerMenu]],  # value
                        _type.HRESULT]
    get_RotationResolutionInDegrees: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                               _type.HRESULT]
    put_RotationResolutionInDegrees: _Callable[[_type.DOUBLE],  # value
                                               _type.HRESULT]
    get_UseAutomaticHapticFeedback: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]
    put_UseAutomaticHapticFeedback: _Callable[[_type.boolean],  # value
                                              _type.HRESULT]
    add_ScreenContactStarted: _Callable[[_Windows_Foundation.ITypedEventHandler[IRadialController, IRadialControllerScreenContactStartedEventArgs],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # cookie
                                        _type.HRESULT]
    remove_ScreenContactStarted: _Callable[[_struct.EventRegistrationToken],  # cookie
                                           _type.HRESULT]
    add_ScreenContactEnded: _Callable[[_Windows_Foundation.ITypedEventHandler[IRadialController, _inspectable.IInspectable],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # cookie
                                      _type.HRESULT]
    remove_ScreenContactEnded: _Callable[[_struct.EventRegistrationToken],  # cookie
                                         _type.HRESULT]
    add_ScreenContactContinued: _Callable[[_Windows_Foundation.ITypedEventHandler[IRadialController, IRadialControllerScreenContactContinuedEventArgs],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # cookie
                                          _type.HRESULT]
    remove_ScreenContactContinued: _Callable[[_struct.EventRegistrationToken],  # cookie
                                             _type.HRESULT]
    add_ControlLost: _Callable[[_Windows_Foundation.ITypedEventHandler[IRadialController, _inspectable.IInspectable],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # cookie
                               _type.HRESULT]
    remove_ControlLost: _Callable[[_struct.EventRegistrationToken],  # cookie
                                  _type.HRESULT]
    add_RotationChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IRadialController, IRadialControllerRotationChangedEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_RotationChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    add_ButtonClicked: _Callable[[_Windows_Foundation.ITypedEventHandler[IRadialController, IRadialControllerButtonClickedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_ButtonClicked: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_ControlAcquired: _Callable[[_Windows_Foundation.ITypedEventHandler[IRadialController, IRadialControllerControlAcquiredEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # cookie
                                   _type.HRESULT]
    remove_ControlAcquired: _Callable[[_struct.EventRegistrationToken],  # cookie
                                      _type.HRESULT]


class IRadialController2(_inspectable.IInspectable):
    add_ButtonPressed: _Callable[[_Windows_Foundation.ITypedEventHandler[IRadialController, IRadialControllerButtonPressedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_ButtonPressed: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_ButtonHolding: _Callable[[_Windows_Foundation.ITypedEventHandler[IRadialController, IRadialControllerButtonHoldingEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_ButtonHolding: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_ButtonReleased: _Callable[[_Windows_Foundation.ITypedEventHandler[IRadialController, IRadialControllerButtonReleasedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_ButtonReleased: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]


class IRadialControllerButtonClickedEventArgs(_inspectable.IInspectable):
    get_Contact: _Callable[[_Pointer[IRadialControllerScreenContact]],  # value
                           _type.HRESULT]


class IRadialControllerButtonClickedEventArgs2(_inspectable.IInspectable):
    get_SimpleHapticsController: _Callable[[_Pointer[_Windows_Devices_Haptics.ISimpleHapticsController]],  # value
                                           _type.HRESULT]


class IRadialControllerButtonHoldingEventArgs(_inspectable.IInspectable):
    get_Contact: _Callable[[_Pointer[IRadialControllerScreenContact]],  # value
                           _type.HRESULT]
    get_SimpleHapticsController: _Callable[[_Pointer[_Windows_Devices_Haptics.ISimpleHapticsController]],  # value
                                           _type.HRESULT]


class IRadialControllerButtonPressedEventArgs(_inspectable.IInspectable):
    get_Contact: _Callable[[_Pointer[IRadialControllerScreenContact]],  # value
                           _type.HRESULT]
    get_SimpleHapticsController: _Callable[[_Pointer[_Windows_Devices_Haptics.ISimpleHapticsController]],  # value
                                           _type.HRESULT]


class IRadialControllerButtonReleasedEventArgs(_inspectable.IInspectable):
    get_Contact: _Callable[[_Pointer[IRadialControllerScreenContact]],  # value
                           _type.HRESULT]
    get_SimpleHapticsController: _Callable[[_Pointer[_Windows_Devices_Haptics.ISimpleHapticsController]],  # value
                                           _type.HRESULT]


class IRadialControllerConfiguration(_inspectable.IInspectable):
    SetDefaultMenuItems: _Callable[[_Windows_Foundation_Collections.IIterable[_enum.Windows.UI.Input.RadialControllerSystemMenuItemKind]],  # buttons
                                   _type.HRESULT]
    ResetToDefaultMenuItems: _Callable[[],
                                       _type.HRESULT]
    TrySelectDefaultMenuItem: _Callable[[_enum.Windows.UI.Input.RadialControllerSystemMenuItemKind,  # type
                                         _Pointer[_type.boolean]],  # result
                                        _type.HRESULT]


class IRadialControllerConfiguration2(_inspectable.IInspectable):
    put_ActiveControllerWhenMenuIsSuppressed: _Callable[[IRadialController],  # value
                                                        _type.HRESULT]
    get_ActiveControllerWhenMenuIsSuppressed: _Callable[[_Pointer[IRadialController]],  # value
                                                        _type.HRESULT]
    put_IsMenuSuppressed: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_IsMenuSuppressed: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]


class IRadialControllerConfigurationStatics(_inspectable.IInspectable):
    GetForCurrentView: _Callable[[_Pointer[IRadialControllerConfiguration]],  # configuration
                                 _type.HRESULT]

    _factory = True


class IRadialControllerConfigurationStatics2(_inspectable.IInspectable):
    put_AppController: _Callable[[IRadialController],  # value
                                 _type.HRESULT]
    get_AppController: _Callable[[_Pointer[IRadialController]],  # value
                                 _type.HRESULT]
    put_IsAppControllerEnabled: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    get_IsAppControllerEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]

    _factory = True


class IRadialControllerControlAcquiredEventArgs(_inspectable.IInspectable):
    get_Contact: _Callable[[_Pointer[IRadialControllerScreenContact]],  # value
                           _type.HRESULT]


class IRadialControllerControlAcquiredEventArgs2(_inspectable.IInspectable):
    get_IsButtonPressed: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_SimpleHapticsController: _Callable[[_Pointer[_Windows_Devices_Haptics.ISimpleHapticsController]],  # value
                                           _type.HRESULT]


class IRadialControllerMenu(_inspectable.IInspectable):
    get_Items: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IRadialControllerMenuItem]]],  # value
                         _type.HRESULT]
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsEnabled: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    GetSelectedMenuItem: _Callable[[_Pointer[IRadialControllerMenuItem]],  # result
                                   _type.HRESULT]
    SelectMenuItem: _Callable[[IRadialControllerMenuItem],  # menuItem
                              _type.HRESULT]
    TrySelectPreviouslySelectedMenuItem: _Callable[[_Pointer[_type.boolean]],  # result
                                                   _type.HRESULT]


class IRadialControllerMenuItem(_inspectable.IInspectable):
    get_DisplayText: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Tag: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                       _type.HRESULT]
    put_Tag: _Callable[[_inspectable.IInspectable],  # value
                       _type.HRESULT]
    add_Invoked: _Callable[[_Windows_Foundation.ITypedEventHandler[IRadialControllerMenuItem, _inspectable.IInspectable],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Invoked: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]


class IRadialControllerMenuItemStatics(_inspectable.IInspectable):
    CreateFromIcon: _Callable[[_type.HSTRING,  # displayText
                               _Windows_Storage_Streams.IRandomAccessStreamReference,  # icon
                               _Pointer[IRadialControllerMenuItem]],  # result
                              _type.HRESULT]
    CreateFromKnownIcon: _Callable[[_type.HSTRING,  # displayText
                                    _enum.Windows.UI.Input.RadialControllerMenuKnownIcon,  # value
                                    _Pointer[IRadialControllerMenuItem]],  # result
                                   _type.HRESULT]

    _factory = True


class IRadialControllerMenuItemStatics2(_inspectable.IInspectable):
    CreateFromFontGlyph: _Callable[[_type.HSTRING,  # displayText
                                    _type.HSTRING,  # glyph
                                    _type.HSTRING,  # fontFamily
                                    _Pointer[IRadialControllerMenuItem]],  # result
                                   _type.HRESULT]
    CreateFromFontGlyphWithUri: _Callable[[_type.HSTRING,  # displayText
                                           _type.HSTRING,  # glyph
                                           _type.HSTRING,  # fontFamily
                                           _Windows_Foundation.IUriRuntimeClass,  # fontUri
                                           _Pointer[IRadialControllerMenuItem]],  # result
                                          _type.HRESULT]

    _factory = True


class IRadialControllerRotationChangedEventArgs(_inspectable.IInspectable):
    get_RotationDeltaInDegrees: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                          _type.HRESULT]
    get_Contact: _Callable[[_Pointer[IRadialControllerScreenContact]],  # value
                           _type.HRESULT]


class IRadialControllerRotationChangedEventArgs2(_inspectable.IInspectable):
    get_IsButtonPressed: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_SimpleHapticsController: _Callable[[_Pointer[_Windows_Devices_Haptics.ISimpleHapticsController]],  # value
                                           _type.HRESULT]


class IRadialControllerScreenContact(_inspectable.IInspectable):
    get_Bounds: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                          _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]


class IRadialControllerScreenContactContinuedEventArgs(_inspectable.IInspectable):
    get_Contact: _Callable[[_Pointer[IRadialControllerScreenContact]],  # value
                           _type.HRESULT]


class IRadialControllerScreenContactContinuedEventArgs2(_inspectable.IInspectable):
    get_IsButtonPressed: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_SimpleHapticsController: _Callable[[_Pointer[_Windows_Devices_Haptics.ISimpleHapticsController]],  # value
                                           _type.HRESULT]


class IRadialControllerScreenContactEndedEventArgs(_inspectable.IInspectable):
    get_IsButtonPressed: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_SimpleHapticsController: _Callable[[_Pointer[_Windows_Devices_Haptics.ISimpleHapticsController]],  # value
                                           _type.HRESULT]


class IRadialControllerScreenContactStartedEventArgs(_inspectable.IInspectable):
    get_Contact: _Callable[[_Pointer[IRadialControllerScreenContact]],  # value
                           _type.HRESULT]


class IRadialControllerScreenContactStartedEventArgs2(_inspectable.IInspectable):
    get_IsButtonPressed: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_SimpleHapticsController: _Callable[[_Pointer[_Windows_Devices_Haptics.ISimpleHapticsController]],  # value
                                           _type.HRESULT]


class IRadialControllerStatics(_inspectable.IInspectable):
    IsSupported: _Callable[[_Pointer[_type.boolean]],  # result
                           _type.HRESULT]
    CreateForCurrentView: _Callable[[_Pointer[IRadialController]],  # result
                                    _type.HRESULT]

    _factory = True


class IRightTappedEventArgs(_inspectable.IInspectable):
    get_PointerDeviceType: _Callable[[_Pointer[_enum.Windows.Devices.Input.PointerDeviceType]],  # value
                                     _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]


class IRightTappedEventArgs2(_inspectable.IInspectable):
    get_ContactCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]


class ISystemButtonEventController(_inspectable.IInspectable):
    add_SystemFunctionButtonPressed: _Callable[[_Windows_Foundation.ITypedEventHandler[ISystemButtonEventController, ISystemFunctionButtonEventArgs],  # handler
                                                _Pointer[_struct.EventRegistrationToken]],  # token
                                               _type.HRESULT]
    remove_SystemFunctionButtonPressed: _Callable[[_struct.EventRegistrationToken],  # token
                                                  _type.HRESULT]
    add_SystemFunctionButtonReleased: _Callable[[_Windows_Foundation.ITypedEventHandler[ISystemButtonEventController, ISystemFunctionButtonEventArgs],  # handler
                                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                                _type.HRESULT]
    remove_SystemFunctionButtonReleased: _Callable[[_struct.EventRegistrationToken],  # token
                                                   _type.HRESULT]
    add_SystemFunctionLockChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ISystemButtonEventController, ISystemFunctionLockChangedEventArgs],  # handler
                                              _Pointer[_struct.EventRegistrationToken]],  # token
                                             _type.HRESULT]
    remove_SystemFunctionLockChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                _type.HRESULT]
    add_SystemFunctionLockIndicatorChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ISystemButtonEventController, ISystemFunctionLockIndicatorChangedEventArgs],  # handler
                                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                                      _type.HRESULT]
    remove_SystemFunctionLockIndicatorChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                         _type.HRESULT]


class ISystemButtonEventControllerStatics(_inspectable.IInspectable):
    CreateForDispatcherQueue: _Callable[[_Windows_System.IDispatcherQueue,  # queue
                                         _Pointer[ISystemButtonEventController]],  # result
                                        _type.HRESULT]

    _factory = True


class ISystemFunctionButtonEventArgs(_inspectable.IInspectable):
    get_Timestamp: _Callable[[_Pointer[_type.UINT64]],  # value
                             _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class ISystemFunctionLockChangedEventArgs(_inspectable.IInspectable):
    get_Timestamp: _Callable[[_Pointer[_type.UINT64]],  # value
                             _type.HRESULT]
    get_IsLocked: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class ISystemFunctionLockIndicatorChangedEventArgs(_inspectable.IInspectable):
    get_Timestamp: _Callable[[_Pointer[_type.UINT64]],  # value
                             _type.HRESULT]
    get_IsIndicatorOn: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class ITappedEventArgs(_inspectable.IInspectable):
    get_PointerDeviceType: _Callable[[_Pointer[_enum.Windows.Devices.Input.PointerDeviceType]],  # value
                                     _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    get_TapCount: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]


class ITappedEventArgs2(_inspectable.IInspectable):
    get_ContactCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]
