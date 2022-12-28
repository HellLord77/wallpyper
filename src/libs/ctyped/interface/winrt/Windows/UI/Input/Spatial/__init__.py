from __future__ import annotations as _

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from .... import Perception as _Windows_Perception
from ....Devices import Haptics as _Windows_Devices_Haptics
from ....Devices import Power as _Windows_Devices_Power
from ....Foundation import Collections as _Windows_Foundation_Collections
from ....Perception import People as _Windows_Perception_People
from ....Perception import Spatial as _Windows_Perception_Spatial
from ....Storage import Streams as _Windows_Storage_Streams
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class ISpatialGestureRecognizer(_inspectable.IInspectable):
    add_RecognitionStarted: _Callable[[_Windows_Foundation.ITypedEventHandler[ISpatialGestureRecognizer, ISpatialRecognitionStartedEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_RecognitionStarted: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_RecognitionEnded: _Callable[[_Windows_Foundation.ITypedEventHandler[ISpatialGestureRecognizer, ISpatialRecognitionEndedEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_RecognitionEnded: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    add_Tapped: _Callable[[_Windows_Foundation.ITypedEventHandler[ISpatialGestureRecognizer, ISpatialTappedEventArgs],  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Tapped: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    add_HoldStarted: _Callable[[_Windows_Foundation.ITypedEventHandler[ISpatialGestureRecognizer, ISpatialHoldStartedEventArgs],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_HoldStarted: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    add_HoldCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[ISpatialGestureRecognizer, ISpatialHoldCompletedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_HoldCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_HoldCanceled: _Callable[[_Windows_Foundation.ITypedEventHandler[ISpatialGestureRecognizer, ISpatialHoldCanceledEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_HoldCanceled: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    add_ManipulationStarted: _Callable[[_Windows_Foundation.ITypedEventHandler[ISpatialGestureRecognizer, ISpatialManipulationStartedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_ManipulationStarted: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_ManipulationUpdated: _Callable[[_Windows_Foundation.ITypedEventHandler[ISpatialGestureRecognizer, ISpatialManipulationUpdatedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_ManipulationUpdated: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_ManipulationCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[ISpatialGestureRecognizer, ISpatialManipulationCompletedEventArgs],  # handler
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_ManipulationCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]
    add_ManipulationCanceled: _Callable[[_Windows_Foundation.ITypedEventHandler[ISpatialGestureRecognizer, ISpatialManipulationCanceledEventArgs],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_ManipulationCanceled: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    add_NavigationStarted: _Callable[[_Windows_Foundation.ITypedEventHandler[ISpatialGestureRecognizer, ISpatialNavigationStartedEventArgs],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_NavigationStarted: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    add_NavigationUpdated: _Callable[[_Windows_Foundation.ITypedEventHandler[ISpatialGestureRecognizer, ISpatialNavigationUpdatedEventArgs],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_NavigationUpdated: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    add_NavigationCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[ISpatialGestureRecognizer, ISpatialNavigationCompletedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_NavigationCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_NavigationCanceled: _Callable[[_Windows_Foundation.ITypedEventHandler[ISpatialGestureRecognizer, ISpatialNavigationCanceledEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_NavigationCanceled: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    CaptureInteraction: _Callable[[ISpatialInteraction],  # interaction
                                  _type.HRESULT]
    CancelPendingGestures: _Callable[[],
                                     _type.HRESULT]
    TrySetGestureSettings: _Callable[[_enum.Windows.UI.Input.Spatial.SpatialGestureSettings,  # settings
                                      _Pointer[_type.boolean]],  # succeeded
                                     _type.HRESULT]
    get_GestureSettings: _Callable[[_Pointer[_enum.Windows.UI.Input.Spatial.SpatialGestureSettings]],  # value
                                   _type.HRESULT]


class ISpatialGestureRecognizerFactory(_inspectable.IInspectable):
    Create: _Callable[[_enum.Windows.UI.Input.Spatial.SpatialGestureSettings,  # settings
                       _Pointer[ISpatialGestureRecognizer]],  # value
                      _type.HRESULT]

    _factory = True


class ISpatialHoldCanceledEventArgs(_inspectable.IInspectable):
    get_InteractionSourceKind: _Callable[[_Pointer[_enum.Windows.UI.Input.Spatial.SpatialInteractionSourceKind]],  # value
                                         _type.HRESULT]


class ISpatialHoldCompletedEventArgs(_inspectable.IInspectable):
    get_InteractionSourceKind: _Callable[[_Pointer[_enum.Windows.UI.Input.Spatial.SpatialInteractionSourceKind]],  # value
                                         _type.HRESULT]


class ISpatialHoldStartedEventArgs(_inspectable.IInspectable):
    get_InteractionSourceKind: _Callable[[_Pointer[_enum.Windows.UI.Input.Spatial.SpatialInteractionSourceKind]],  # value
                                         _type.HRESULT]
    TryGetPointerPose: _Callable[[_Windows_Perception_Spatial.ISpatialCoordinateSystem,  # coordinateSystem
                                  _Pointer[ISpatialPointerPose]],  # value
                                 _type.HRESULT]


class ISpatialInteraction(_inspectable.IInspectable):
    get_SourceState: _Callable[[_Pointer[ISpatialInteractionSourceState]],  # value
                               _type.HRESULT]


class ISpatialInteractionController(_inspectable.IInspectable):
    get_HasTouchpad: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_HasThumbstick: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_SimpleHapticsController: _Callable[[_Pointer[_Windows_Devices_Haptics.ISimpleHapticsController]],  # value
                                           _type.HRESULT]
    get_VendorId: _Callable[[_Pointer[_type.UINT16]],  # value
                            _type.HRESULT]
    get_ProductId: _Callable[[_Pointer[_type.UINT16]],  # value
                             _type.HRESULT]
    get_Version: _Callable[[_Pointer[_type.UINT16]],  # value
                           _type.HRESULT]


class ISpatialInteractionController2(_inspectable.IInspectable):
    TryGetRenderableModelAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStreamWithContentType]]],  # value
                                          _type.HRESULT]


class ISpatialInteractionController3(_inspectable.IInspectable):
    TryGetBatteryReport: _Callable[[_Pointer[_Windows_Devices_Power.IBatteryReport]],  # value
                                   _type.HRESULT]


class ISpatialInteractionControllerProperties(_inspectable.IInspectable):
    get_IsTouchpadTouched: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    get_IsTouchpadPressed: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    get_IsThumbstickPressed: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    get_ThumbstickX: _Callable[[_Pointer[_type.DOUBLE]],  # value
                               _type.HRESULT]
    get_ThumbstickY: _Callable[[_Pointer[_type.DOUBLE]],  # value
                               _type.HRESULT]
    get_TouchpadX: _Callable[[_Pointer[_type.DOUBLE]],  # value
                             _type.HRESULT]
    get_TouchpadY: _Callable[[_Pointer[_type.DOUBLE]],  # value
                             _type.HRESULT]


class ISpatialInteractionDetectedEventArgs(_inspectable.IInspectable):
    get_InteractionSourceKind: _Callable[[_Pointer[_enum.Windows.UI.Input.Spatial.SpatialInteractionSourceKind]],  # value
                                         _type.HRESULT]
    TryGetPointerPose: _Callable[[_Windows_Perception_Spatial.ISpatialCoordinateSystem,  # coordinateSystem
                                  _Pointer[ISpatialPointerPose]],  # value
                                 _type.HRESULT]
    get_Interaction: _Callable[[_Pointer[ISpatialInteraction]],  # value
                               _type.HRESULT]


class ISpatialInteractionDetectedEventArgs2(_inspectable.IInspectable):
    get_InteractionSource: _Callable[[_Pointer[ISpatialInteractionSource]],  # value
                                     _type.HRESULT]


class ISpatialInteractionManager(_inspectable.IInspectable):
    add_SourceDetected: _Callable[[_Windows_Foundation.ITypedEventHandler[ISpatialInteractionManager, ISpatialInteractionSourceEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_SourceDetected: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_SourceLost: _Callable[[_Windows_Foundation.ITypedEventHandler[ISpatialInteractionManager, ISpatialInteractionSourceEventArgs],  # handler
                               _Pointer[_struct.EventRegistrationToken]],  # token
                              _type.HRESULT]
    remove_SourceLost: _Callable[[_struct.EventRegistrationToken],  # token
                                 _type.HRESULT]
    add_SourceUpdated: _Callable[[_Windows_Foundation.ITypedEventHandler[ISpatialInteractionManager, ISpatialInteractionSourceEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_SourceUpdated: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_SourcePressed: _Callable[[_Windows_Foundation.ITypedEventHandler[ISpatialInteractionManager, ISpatialInteractionSourceEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_SourcePressed: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_SourceReleased: _Callable[[_Windows_Foundation.ITypedEventHandler[ISpatialInteractionManager, ISpatialInteractionSourceEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_SourceReleased: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_InteractionDetected: _Callable[[_Windows_Foundation.ITypedEventHandler[ISpatialInteractionManager, ISpatialInteractionDetectedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_InteractionDetected: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    GetDetectedSourcesAtTimestamp: _Callable[[_Windows_Perception.IPerceptionTimestamp,  # timeStamp
                                              _Pointer[_Windows_Foundation_Collections.IVectorView[ISpatialInteractionSourceState]]],  # value
                                             _type.HRESULT]


class ISpatialInteractionManagerStatics(_inspectable.IInspectable):
    GetForCurrentView: _Callable[[_Pointer[ISpatialInteractionManager]],  # value
                                 _type.HRESULT]

    _factory = True


class ISpatialInteractionManagerStatics2(_inspectable.IInspectable):
    IsSourceKindSupported: _Callable[[_enum.Windows.UI.Input.Spatial.SpatialInteractionSourceKind,  # kind
                                      _Pointer[_type.boolean]],  # result
                                     _type.HRESULT]

    _factory = True


class ISpatialInteractionSource(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.UINT32]],  # value
                      _type.HRESULT]
    get_Kind: _Callable[[_Pointer[_enum.Windows.UI.Input.Spatial.SpatialInteractionSourceKind]],  # value
                        _type.HRESULT]


class ISpatialInteractionSource2(_inspectable.IInspectable):
    get_IsPointingSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    get_IsMenuSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_IsGraspSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_Controller: _Callable[[_Pointer[ISpatialInteractionController]],  # value
                              _type.HRESULT]
    TryGetStateAtTimestamp: _Callable[[_Windows_Perception.IPerceptionTimestamp,  # timestamp
                                       _Pointer[ISpatialInteractionSourceState]],  # value
                                      _type.HRESULT]


class ISpatialInteractionSource3(_inspectable.IInspectable):
    get_Handedness: _Callable[[_Pointer[_enum.Windows.UI.Input.Spatial.SpatialInteractionSourceHandedness]],  # value
                              _type.HRESULT]


class ISpatialInteractionSource4(_inspectable.IInspectable):
    TryCreateHandMeshObserver: _Callable[[_Pointer[_Windows_Perception_People.IHandMeshObserver]],  # result
                                         _type.HRESULT]
    TryCreateHandMeshObserverAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Perception_People.IHandMeshObserver]]],  # operation
                                              _type.HRESULT]


class ISpatialInteractionSourceEventArgs(_inspectable.IInspectable):
    get_State: _Callable[[_Pointer[ISpatialInteractionSourceState]],  # value
                         _type.HRESULT]


class ISpatialInteractionSourceEventArgs2(_inspectable.IInspectable):
    get_PressKind: _Callable[[_Pointer[_enum.Windows.UI.Input.Spatial.SpatialInteractionPressKind]],  # value
                             _type.HRESULT]


class ISpatialInteractionSourceLocation(_inspectable.IInspectable):
    get_Position: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.Numerics.Vector3]]],  # value
                            _type.HRESULT]
    get_Velocity: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.Numerics.Vector3]]],  # value
                            _type.HRESULT]


class ISpatialInteractionSourceLocation2(_inspectable.IInspectable):
    get_Orientation: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.Numerics.Quaternion]]],  # value
                               _type.HRESULT]


class ISpatialInteractionSourceLocation3(_inspectable.IInspectable):
    get_PositionAccuracy: _Callable[[_Pointer[_enum.Windows.UI.Input.Spatial.SpatialInteractionSourcePositionAccuracy]],  # value
                                    _type.HRESULT]
    get_AngularVelocity: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.Numerics.Vector3]]],  # value
                                   _type.HRESULT]
    get_SourcePointerPose: _Callable[[_Pointer[ISpatialPointerInteractionSourcePose]],  # value
                                     _type.HRESULT]


class ISpatialInteractionSourceProperties(_inspectable.IInspectable):
    TryGetSourceLossMitigationDirection: _Callable[[_Windows_Perception_Spatial.ISpatialCoordinateSystem,  # coordinateSystem
                                                    _Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.Numerics.Vector3]]],  # value
                                                   _type.HRESULT]
    get_SourceLossRisk: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    TryGetLocation: _Callable[[_Windows_Perception_Spatial.ISpatialCoordinateSystem,  # coordinateSystem
                               _Pointer[ISpatialInteractionSourceLocation]],  # value
                              _type.HRESULT]


class ISpatialInteractionSourceState(_inspectable.IInspectable):
    get_Source: _Callable[[_Pointer[ISpatialInteractionSource]],  # value
                          _type.HRESULT]
    get_Properties: _Callable[[_Pointer[ISpatialInteractionSourceProperties]],  # value
                              _type.HRESULT]
    get_IsPressed: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_Timestamp: _Callable[[_Pointer[_Windows_Perception.IPerceptionTimestamp]],  # value
                             _type.HRESULT]
    TryGetPointerPose: _Callable[[_Windows_Perception_Spatial.ISpatialCoordinateSystem,  # coordinateSystem
                                  _Pointer[ISpatialPointerPose]],  # value
                                 _type.HRESULT]


class ISpatialInteractionSourceState2(_inspectable.IInspectable):
    get_IsSelectPressed: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_IsMenuPressed: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_IsGrasped: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_SelectPressedValue: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                      _type.HRESULT]
    get_ControllerProperties: _Callable[[_Pointer[ISpatialInteractionControllerProperties]],  # value
                                        _type.HRESULT]


class ISpatialInteractionSourceState3(_inspectable.IInspectable):
    TryGetHandPose: _Callable[[_Pointer[_Windows_Perception_People.IHandPose]],  # value
                              _type.HRESULT]


class ISpatialManipulationCanceledEventArgs(_inspectable.IInspectable):
    get_InteractionSourceKind: _Callable[[_Pointer[_enum.Windows.UI.Input.Spatial.SpatialInteractionSourceKind]],  # value
                                         _type.HRESULT]


class ISpatialManipulationCompletedEventArgs(_inspectable.IInspectable):
    get_InteractionSourceKind: _Callable[[_Pointer[_enum.Windows.UI.Input.Spatial.SpatialInteractionSourceKind]],  # value
                                         _type.HRESULT]
    TryGetCumulativeDelta: _Callable[[_Windows_Perception_Spatial.ISpatialCoordinateSystem,  # coordinateSystem
                                      _Pointer[ISpatialManipulationDelta]],  # value
                                     _type.HRESULT]


class ISpatialManipulationDelta(_inspectable.IInspectable):
    get_Translation: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                               _type.HRESULT]


class ISpatialManipulationStartedEventArgs(_inspectable.IInspectable):
    get_InteractionSourceKind: _Callable[[_Pointer[_enum.Windows.UI.Input.Spatial.SpatialInteractionSourceKind]],  # value
                                         _type.HRESULT]
    TryGetPointerPose: _Callable[[_Windows_Perception_Spatial.ISpatialCoordinateSystem,  # coordinateSystem
                                  _Pointer[ISpatialPointerPose]],  # value
                                 _type.HRESULT]


class ISpatialManipulationUpdatedEventArgs(_inspectable.IInspectable):
    get_InteractionSourceKind: _Callable[[_Pointer[_enum.Windows.UI.Input.Spatial.SpatialInteractionSourceKind]],  # value
                                         _type.HRESULT]
    TryGetCumulativeDelta: _Callable[[_Windows_Perception_Spatial.ISpatialCoordinateSystem,  # coordinateSystem
                                      _Pointer[ISpatialManipulationDelta]],  # value
                                     _type.HRESULT]


class ISpatialNavigationCanceledEventArgs(_inspectable.IInspectable):
    get_InteractionSourceKind: _Callable[[_Pointer[_enum.Windows.UI.Input.Spatial.SpatialInteractionSourceKind]],  # value
                                         _type.HRESULT]


class ISpatialNavigationCompletedEventArgs(_inspectable.IInspectable):
    get_InteractionSourceKind: _Callable[[_Pointer[_enum.Windows.UI.Input.Spatial.SpatialInteractionSourceKind]],  # value
                                         _type.HRESULT]
    get_NormalizedOffset: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                                    _type.HRESULT]


class ISpatialNavigationStartedEventArgs(_inspectable.IInspectable):
    get_InteractionSourceKind: _Callable[[_Pointer[_enum.Windows.UI.Input.Spatial.SpatialInteractionSourceKind]],  # value
                                         _type.HRESULT]
    TryGetPointerPose: _Callable[[_Windows_Perception_Spatial.ISpatialCoordinateSystem,  # coordinateSystem
                                  _Pointer[ISpatialPointerPose]],  # value
                                 _type.HRESULT]
    get_IsNavigatingX: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_IsNavigatingY: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_IsNavigatingZ: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]


class ISpatialNavigationUpdatedEventArgs(_inspectable.IInspectable):
    get_InteractionSourceKind: _Callable[[_Pointer[_enum.Windows.UI.Input.Spatial.SpatialInteractionSourceKind]],  # value
                                         _type.HRESULT]
    get_NormalizedOffset: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                                    _type.HRESULT]


class ISpatialPointerInteractionSourcePose(_inspectable.IInspectable):
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                            _type.HRESULT]
    get_ForwardDirection: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                                    _type.HRESULT]
    get_UpDirection: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                               _type.HRESULT]


class ISpatialPointerInteractionSourcePose2(_inspectable.IInspectable):
    get_Orientation: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Quaternion]],  # value
                               _type.HRESULT]
    get_PositionAccuracy: _Callable[[_Pointer[_enum.Windows.UI.Input.Spatial.SpatialInteractionSourcePositionAccuracy]],  # value
                                    _type.HRESULT]


class ISpatialPointerPose(_inspectable.IInspectable):
    get_Timestamp: _Callable[[_Pointer[_Windows_Perception.IPerceptionTimestamp]],  # value
                             _type.HRESULT]
    get_Head: _Callable[[_Pointer[_Windows_Perception_People.IHeadPose]],  # value
                        _type.HRESULT]


class ISpatialPointerPose2(_inspectable.IInspectable):
    TryGetInteractionSourcePose: _Callable[[ISpatialInteractionSource,  # source
                                            _Pointer[ISpatialPointerInteractionSourcePose]],  # value
                                           _type.HRESULT]


class ISpatialPointerPose3(_inspectable.IInspectable):
    get_Eyes: _Callable[[_Pointer[_Windows_Perception_People.IEyesPose]],  # value
                        _type.HRESULT]
    get_IsHeadCapturedBySystem: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]


class ISpatialPointerPoseStatics(_inspectable.IInspectable):
    TryGetAtTimestamp: _Callable[[_Windows_Perception_Spatial.ISpatialCoordinateSystem,  # coordinateSystem
                                  _Windows_Perception.IPerceptionTimestamp,  # timestamp
                                  _Pointer[ISpatialPointerPose]],  # value
                                 _type.HRESULT]

    _factory = True


class ISpatialRecognitionEndedEventArgs(_inspectable.IInspectable):
    get_InteractionSourceKind: _Callable[[_Pointer[_enum.Windows.UI.Input.Spatial.SpatialInteractionSourceKind]],  # value
                                         _type.HRESULT]


class ISpatialRecognitionStartedEventArgs(_inspectable.IInspectable):
    get_InteractionSourceKind: _Callable[[_Pointer[_enum.Windows.UI.Input.Spatial.SpatialInteractionSourceKind]],  # value
                                         _type.HRESULT]
    TryGetPointerPose: _Callable[[_Windows_Perception_Spatial.ISpatialCoordinateSystem,  # coordinateSystem
                                  _Pointer[ISpatialPointerPose]],  # value
                                 _type.HRESULT]
    IsGesturePossible: _Callable[[_enum.Windows.UI.Input.Spatial.SpatialGestureSettings,  # gesture
                                  _Pointer[_type.boolean]],  # value
                                 _type.HRESULT]


class ISpatialTappedEventArgs(_inspectable.IInspectable):
    get_InteractionSourceKind: _Callable[[_Pointer[_enum.Windows.UI.Input.Spatial.SpatialInteractionSourceKind]],  # value
                                         _type.HRESULT]
    TryGetPointerPose: _Callable[[_Windows_Perception_Spatial.ISpatialCoordinateSystem,  # coordinateSystem
                                  _Pointer[ISpatialPointerPose]],  # value
                                 _type.HRESULT]
    get_TapCount: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
