from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Composition as _Microsoft_UI_Composition
from ... import Input as _Microsoft_UI_Input
from ..... import inspectable as _inspectable
from .....Windows import Foundation as _Windows_Foundation
from .....Windows.Foundation import Collections as _Windows_Foundation_Collections
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class ICompositionConditionalValue(_inspectable.IInspectable):
    get_Condition: _Callable[[_Pointer[_Microsoft_UI_Composition.IExpressionAnimation]],  # value
                             _type.HRESULT]
    put_Condition: _Callable[[_Microsoft_UI_Composition.IExpressionAnimation],  # value
                             _type.HRESULT]
    get_Value: _Callable[[_Pointer[_Microsoft_UI_Composition.IExpressionAnimation]],  # value
                         _type.HRESULT]
    put_Value: _Callable[[_Microsoft_UI_Composition.IExpressionAnimation],  # value
                         _type.HRESULT]


class ICompositionConditionalValueStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Microsoft_UI_Composition.ICompositor,  # compositor
                       _Pointer[ICompositionConditionalValue]],  # result
                      _type.HRESULT]


class ICompositionInteractionSource(_inspectable.IInspectable):
    pass


class ICompositionInteractionSourceCollection(_inspectable.IInspectable):
    get_Count: _Callable[[_Pointer[_type.INT32]],  # value
                         _type.HRESULT]
    Add: _Callable[[ICompositionInteractionSource],  # value
                   _type.HRESULT]
    Remove: _Callable[[ICompositionInteractionSource],  # value
                      _type.HRESULT]
    RemoveAll: _Callable[[],
                         _type.HRESULT]


class IInteractionSourceConfiguration(_inspectable.IInspectable):
    get_PositionXSourceMode: _Callable[[_Pointer[_enum.Microsoft.UI.Composition.Interactions.InteractionSourceRedirectionMode]],  # value
                                       _type.HRESULT]
    put_PositionXSourceMode: _Callable[[_enum.Microsoft.UI.Composition.Interactions.InteractionSourceRedirectionMode],  # value
                                       _type.HRESULT]
    get_PositionYSourceMode: _Callable[[_Pointer[_enum.Microsoft.UI.Composition.Interactions.InteractionSourceRedirectionMode]],  # value
                                       _type.HRESULT]
    put_PositionYSourceMode: _Callable[[_enum.Microsoft.UI.Composition.Interactions.InteractionSourceRedirectionMode],  # value
                                       _type.HRESULT]
    get_ScaleSourceMode: _Callable[[_Pointer[_enum.Microsoft.UI.Composition.Interactions.InteractionSourceRedirectionMode]],  # value
                                   _type.HRESULT]
    put_ScaleSourceMode: _Callable[[_enum.Microsoft.UI.Composition.Interactions.InteractionSourceRedirectionMode],  # value
                                   _type.HRESULT]


class IInteractionTracker(_inspectable.IInspectable):
    get_InteractionSources: _Callable[[_Pointer[ICompositionInteractionSourceCollection]],  # value
                                      _type.HRESULT]
    get_IsPositionRoundingSuggested: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]
    get_MaxPosition: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                               _type.HRESULT]
    put_MaxPosition: _Callable[[_struct.Windows.Foundation.Numerics.Vector3],  # value
                               _type.HRESULT]
    get_MaxScale: _Callable[[_Pointer[_type.FLOAT]],  # value
                            _type.HRESULT]
    put_MaxScale: _Callable[[_type.FLOAT],  # value
                            _type.HRESULT]
    get_MinPosition: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                               _type.HRESULT]
    put_MinPosition: _Callable[[_struct.Windows.Foundation.Numerics.Vector3],  # value
                               _type.HRESULT]
    get_MinScale: _Callable[[_Pointer[_type.FLOAT]],  # value
                            _type.HRESULT]
    put_MinScale: _Callable[[_type.FLOAT],  # value
                            _type.HRESULT]
    get_NaturalRestingPosition: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                                          _type.HRESULT]
    get_NaturalRestingScale: _Callable[[_Pointer[_type.FLOAT]],  # value
                                       _type.HRESULT]
    get_Owner: _Callable[[_Pointer[IInteractionTrackerOwner]],  # value
                         _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                            _type.HRESULT]
    get_PositionInertiaDecayRate: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.Numerics.Vector3]]],  # value
                                            _type.HRESULT]
    put_PositionInertiaDecayRate: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                                            _type.HRESULT]
    get_PositionVelocityInPixelsPerSecond: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                                                     _type.HRESULT]
    get_Scale: _Callable[[_Pointer[_type.FLOAT]],  # value
                         _type.HRESULT]
    get_ScaleInertiaDecayRate: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.FLOAT]]],  # value
                                         _type.HRESULT]
    put_ScaleInertiaDecayRate: _Callable[[_Windows_Foundation.IReference[_type.FLOAT]],  # value
                                         _type.HRESULT]
    get_ScaleVelocityInPercentPerSecond: _Callable[[_Pointer[_type.FLOAT]],  # value
                                                   _type.HRESULT]
    AdjustPositionXIfGreaterThanThreshold: _Callable[[_type.FLOAT,  # adjustment
                                                      _type.FLOAT],  # positionThreshold
                                                     _type.HRESULT]
    AdjustPositionYIfGreaterThanThreshold: _Callable[[_type.FLOAT,  # adjustment
                                                      _type.FLOAT],  # positionThreshold
                                                     _type.HRESULT]
    ConfigurePositionXInertiaModifiers: _Callable[[_Windows_Foundation_Collections.IIterable[IInteractionTrackerInertiaModifier]],  # modifiers
                                                  _type.HRESULT]
    ConfigurePositionYInertiaModifiers: _Callable[[_Windows_Foundation_Collections.IIterable[IInteractionTrackerInertiaModifier]],  # modifiers
                                                  _type.HRESULT]
    ConfigureScaleInertiaModifiers: _Callable[[_Windows_Foundation_Collections.IIterable[IInteractionTrackerInertiaModifier]],  # modifiers
                                              _type.HRESULT]
    TryUpdatePosition: _Callable[[_struct.Windows.Foundation.Numerics.Vector3,  # value
                                  _Pointer[_type.INT32]],  # result
                                 _type.HRESULT]
    TryUpdatePositionBy: _Callable[[_struct.Windows.Foundation.Numerics.Vector3,  # amount
                                    _Pointer[_type.INT32]],  # result
                                   _type.HRESULT]
    TryUpdatePositionWithAnimation: _Callable[[_Microsoft_UI_Composition.ICompositionAnimation,  # animation
                                               _Pointer[_type.INT32]],  # result
                                              _type.HRESULT]
    TryUpdatePositionWithAdditionalVelocity: _Callable[[_struct.Windows.Foundation.Numerics.Vector3,  # velocityInPixelsPerSecond
                                                        _Pointer[_type.INT32]],  # result
                                                       _type.HRESULT]
    TryUpdateScale: _Callable[[_type.FLOAT,  # value
                               _struct.Windows.Foundation.Numerics.Vector3,  # centerPoint
                               _Pointer[_type.INT32]],  # result
                              _type.HRESULT]
    TryUpdateScaleWithAnimation: _Callable[[_Microsoft_UI_Composition.ICompositionAnimation,  # animation
                                            _struct.Windows.Foundation.Numerics.Vector3,  # centerPoint
                                            _Pointer[_type.INT32]],  # result
                                           _type.HRESULT]
    TryUpdateScaleWithAdditionalVelocity: _Callable[[_type.FLOAT,  # velocityInPercentPerSecond
                                                     _struct.Windows.Foundation.Numerics.Vector3,  # centerPoint
                                                     _Pointer[_type.INT32]],  # result
                                                    _type.HRESULT]


class IInteractionTracker2(_inspectable.IInspectable):
    ConfigureCenterPointXInertiaModifiers: _Callable[[_Windows_Foundation_Collections.IIterable[ICompositionConditionalValue]],  # conditionalValues
                                                     _type.HRESULT]
    ConfigureCenterPointYInertiaModifiers: _Callable[[_Windows_Foundation_Collections.IIterable[ICompositionConditionalValue]],  # conditionalValues
                                                     _type.HRESULT]


class IInteractionTracker3(_inspectable.IInspectable):
    ConfigureVector2PositionInertiaModifiers: _Callable[[_Windows_Foundation_Collections.IIterable[IInteractionTrackerVector2InertiaModifier]],  # modifiers
                                                        _type.HRESULT]


class IInteractionTracker4(_inspectable.IInspectable):
    TryUpdatePositionWithOption: _Callable[[_struct.Windows.Foundation.Numerics.Vector3,  # value
                                            _enum.Microsoft.UI.Composition.Interactions.InteractionTrackerClampingOption,  # option
                                            _Pointer[_type.INT32]],  # result
                                           _type.HRESULT]
    TryUpdatePositionByWithOption: _Callable[[_struct.Windows.Foundation.Numerics.Vector3,  # amount
                                              _enum.Microsoft.UI.Composition.Interactions.InteractionTrackerClampingOption,  # option
                                              _Pointer[_type.INT32]],  # result
                                             _type.HRESULT]
    get_IsInertiaFromImpulse: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]


class IInteractionTracker5(_inspectable.IInspectable):
    TryUpdatePositionWithOption: _Callable[[_struct.Windows.Foundation.Numerics.Vector3,  # value
                                            _enum.Microsoft.UI.Composition.Interactions.InteractionTrackerClampingOption,  # option
                                            _enum.Microsoft.UI.Composition.Interactions.InteractionTrackerPositionUpdateOption,  # posUpdateOption
                                            _Pointer[_type.INT32]],  # result
                                           _type.HRESULT]


class IInteractionTrackerCustomAnimationStateEnteredArgs(_inspectable.IInspectable):
    get_RequestId: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]


class IInteractionTrackerCustomAnimationStateEnteredArgs2(_inspectable.IInspectable):
    get_IsFromBinding: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]


class IInteractionTrackerIdleStateEnteredArgs(_inspectable.IInspectable):
    get_RequestId: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]


class IInteractionTrackerIdleStateEnteredArgs2(_inspectable.IInspectable):
    get_IsFromBinding: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]


class IInteractionTrackerInertiaModifier(_inspectable.IInspectable):
    pass


class IInteractionTrackerInertiaModifierFactory(_inspectable.IInspectable):
    pass


class IInteractionTrackerInertiaMotion(_inspectable.IInspectable):
    get_Condition: _Callable[[_Pointer[_Microsoft_UI_Composition.IExpressionAnimation]],  # value
                             _type.HRESULT]
    put_Condition: _Callable[[_Microsoft_UI_Composition.IExpressionAnimation],  # value
                             _type.HRESULT]
    get_Motion: _Callable[[_Pointer[_Microsoft_UI_Composition.IExpressionAnimation]],  # value
                          _type.HRESULT]
    put_Motion: _Callable[[_Microsoft_UI_Composition.IExpressionAnimation],  # value
                          _type.HRESULT]


class IInteractionTrackerInertiaMotionStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Microsoft_UI_Composition.ICompositor,  # compositor
                       _Pointer[IInteractionTrackerInertiaMotion]],  # result
                      _type.HRESULT]


class IInteractionTrackerInertiaNaturalMotion(_inspectable.IInspectable):
    get_Condition: _Callable[[_Pointer[_Microsoft_UI_Composition.IExpressionAnimation]],  # value
                             _type.HRESULT]
    put_Condition: _Callable[[_Microsoft_UI_Composition.IExpressionAnimation],  # value
                             _type.HRESULT]
    get_NaturalMotion: _Callable[[_Pointer[_Microsoft_UI_Composition.IScalarNaturalMotionAnimation]],  # value
                                 _type.HRESULT]
    put_NaturalMotion: _Callable[[_Microsoft_UI_Composition.IScalarNaturalMotionAnimation],  # value
                                 _type.HRESULT]


class IInteractionTrackerInertiaNaturalMotionStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Microsoft_UI_Composition.ICompositor,  # compositor
                       _Pointer[IInteractionTrackerInertiaNaturalMotion]],  # result
                      _type.HRESULT]


class IInteractionTrackerInertiaRestingValue(_inspectable.IInspectable):
    get_Condition: _Callable[[_Pointer[_Microsoft_UI_Composition.IExpressionAnimation]],  # value
                             _type.HRESULT]
    put_Condition: _Callable[[_Microsoft_UI_Composition.IExpressionAnimation],  # value
                             _type.HRESULT]
    get_RestingValue: _Callable[[_Pointer[_Microsoft_UI_Composition.IExpressionAnimation]],  # value
                                _type.HRESULT]
    put_RestingValue: _Callable[[_Microsoft_UI_Composition.IExpressionAnimation],  # value
                                _type.HRESULT]


class IInteractionTrackerInertiaRestingValueStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Microsoft_UI_Composition.ICompositor,  # compositor
                       _Pointer[IInteractionTrackerInertiaRestingValue]],  # result
                      _type.HRESULT]


class IInteractionTrackerInertiaStateEnteredArgs(_inspectable.IInspectable):
    get_ModifiedRestingPosition: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.Numerics.Vector3]]],  # value
                                           _type.HRESULT]
    get_ModifiedRestingScale: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.FLOAT]]],  # value
                                        _type.HRESULT]
    get_NaturalRestingPosition: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                                          _type.HRESULT]
    get_NaturalRestingScale: _Callable[[_Pointer[_type.FLOAT]],  # value
                                       _type.HRESULT]
    get_PositionVelocityInPixelsPerSecond: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                                                     _type.HRESULT]
    get_RequestId: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]
    get_ScaleVelocityInPercentPerSecond: _Callable[[_Pointer[_type.FLOAT]],  # value
                                                   _type.HRESULT]


class IInteractionTrackerInertiaStateEnteredArgs2(_inspectable.IInspectable):
    get_IsInertiaFromImpulse: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]


class IInteractionTrackerInertiaStateEnteredArgs3(_inspectable.IInspectable):
    get_IsFromBinding: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]


class IInteractionTrackerInteractingStateEnteredArgs(_inspectable.IInspectable):
    get_RequestId: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]


class IInteractionTrackerInteractingStateEnteredArgs2(_inspectable.IInspectable):
    get_IsFromBinding: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]


class IInteractionTrackerOwner(_inspectable.IInspectable):
    CustomAnimationStateEntered: _Callable[[IInteractionTracker,  # sender
                                            IInteractionTrackerCustomAnimationStateEnteredArgs],  # args
                                           _type.HRESULT]
    IdleStateEntered: _Callable[[IInteractionTracker,  # sender
                                 IInteractionTrackerIdleStateEnteredArgs],  # args
                                _type.HRESULT]
    InertiaStateEntered: _Callable[[IInteractionTracker,  # sender
                                    IInteractionTrackerInertiaStateEnteredArgs],  # args
                                   _type.HRESULT]
    InteractingStateEntered: _Callable[[IInteractionTracker,  # sender
                                        IInteractionTrackerInteractingStateEnteredArgs],  # args
                                       _type.HRESULT]
    RequestIgnored: _Callable[[IInteractionTracker,  # sender
                               IInteractionTrackerRequestIgnoredArgs],  # args
                              _type.HRESULT]
    ValuesChanged: _Callable[[IInteractionTracker,  # sender
                              IInteractionTrackerValuesChangedArgs],  # args
                             _type.HRESULT]


class IInteractionTrackerRequestIgnoredArgs(_inspectable.IInspectable):
    get_RequestId: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]


class IInteractionTrackerStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Microsoft_UI_Composition.ICompositor,  # compositor
                       _Pointer[IInteractionTracker]],  # result
                      _type.HRESULT]
    CreateWithOwner: _Callable[[_Microsoft_UI_Composition.ICompositor,  # compositor
                                IInteractionTrackerOwner,  # owner
                                _Pointer[IInteractionTracker]],  # result
                               _type.HRESULT]


class IInteractionTrackerStatics2(_inspectable.IInspectable, factory=True):
    SetBindingMode: _Callable[[IInteractionTracker,  # boundTracker1
                               IInteractionTracker,  # boundTracker2
                               _enum.Microsoft.UI.Composition.Interactions.InteractionBindingAxisModes],  # axisMode
                              _type.HRESULT]
    GetBindingMode: _Callable[[IInteractionTracker,  # boundTracker1
                               IInteractionTracker,  # boundTracker2
                               _Pointer[_enum.Microsoft.UI.Composition.Interactions.InteractionBindingAxisModes]],  # result
                              _type.HRESULT]


class IInteractionTrackerValuesChangedArgs(_inspectable.IInspectable):
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                            _type.HRESULT]
    get_RequestId: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]
    get_Scale: _Callable[[_Pointer[_type.FLOAT]],  # value
                         _type.HRESULT]


class IInteractionTrackerVector2InertiaModifier(_inspectable.IInspectable):
    pass


class IInteractionTrackerVector2InertiaModifierFactory(_inspectable.IInspectable):
    pass


class IInteractionTrackerVector2InertiaNaturalMotion(_inspectable.IInspectable):
    get_Condition: _Callable[[_Pointer[_Microsoft_UI_Composition.IExpressionAnimation]],  # value
                             _type.HRESULT]
    put_Condition: _Callable[[_Microsoft_UI_Composition.IExpressionAnimation],  # value
                             _type.HRESULT]
    get_NaturalMotion: _Callable[[_Pointer[_Microsoft_UI_Composition.IVector2NaturalMotionAnimation]],  # value
                                 _type.HRESULT]
    put_NaturalMotion: _Callable[[_Microsoft_UI_Composition.IVector2NaturalMotionAnimation],  # value
                                 _type.HRESULT]


class IInteractionTrackerVector2InertiaNaturalMotionStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Microsoft_UI_Composition.ICompositor,  # compositor
                       _Pointer[IInteractionTrackerVector2InertiaNaturalMotion]],  # result
                      _type.HRESULT]


class IVisualInteractionSource(_inspectable.IInspectable):
    get_IsPositionXRailsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    put_IsPositionXRailsEnabled: _Callable[[_type.boolean],  # value
                                           _type.HRESULT]
    get_IsPositionYRailsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    put_IsPositionYRailsEnabled: _Callable[[_type.boolean],  # value
                                           _type.HRESULT]
    get_ManipulationRedirectionMode: _Callable[[_Pointer[_enum.Microsoft.UI.Composition.Interactions.VisualInteractionSourceRedirectionMode]],  # value
                                               _type.HRESULT]
    put_ManipulationRedirectionMode: _Callable[[_enum.Microsoft.UI.Composition.Interactions.VisualInteractionSourceRedirectionMode],  # value
                                               _type.HRESULT]
    get_PositionXChainingMode: _Callable[[_Pointer[_enum.Microsoft.UI.Composition.Interactions.InteractionChainingMode]],  # value
                                         _type.HRESULT]
    put_PositionXChainingMode: _Callable[[_enum.Microsoft.UI.Composition.Interactions.InteractionChainingMode],  # value
                                         _type.HRESULT]
    get_PositionXSourceMode: _Callable[[_Pointer[_enum.Microsoft.UI.Composition.Interactions.InteractionSourceMode]],  # value
                                       _type.HRESULT]
    put_PositionXSourceMode: _Callable[[_enum.Microsoft.UI.Composition.Interactions.InteractionSourceMode],  # value
                                       _type.HRESULT]
    get_PositionYChainingMode: _Callable[[_Pointer[_enum.Microsoft.UI.Composition.Interactions.InteractionChainingMode]],  # value
                                         _type.HRESULT]
    put_PositionYChainingMode: _Callable[[_enum.Microsoft.UI.Composition.Interactions.InteractionChainingMode],  # value
                                         _type.HRESULT]
    get_PositionYSourceMode: _Callable[[_Pointer[_enum.Microsoft.UI.Composition.Interactions.InteractionSourceMode]],  # value
                                       _type.HRESULT]
    put_PositionYSourceMode: _Callable[[_enum.Microsoft.UI.Composition.Interactions.InteractionSourceMode],  # value
                                       _type.HRESULT]
    get_ScaleChainingMode: _Callable[[_Pointer[_enum.Microsoft.UI.Composition.Interactions.InteractionChainingMode]],  # value
                                     _type.HRESULT]
    put_ScaleChainingMode: _Callable[[_enum.Microsoft.UI.Composition.Interactions.InteractionChainingMode],  # value
                                     _type.HRESULT]
    get_ScaleSourceMode: _Callable[[_Pointer[_enum.Microsoft.UI.Composition.Interactions.InteractionSourceMode]],  # value
                                   _type.HRESULT]
    put_ScaleSourceMode: _Callable[[_enum.Microsoft.UI.Composition.Interactions.InteractionSourceMode],  # value
                                   _type.HRESULT]
    get_Source: _Callable[[_Pointer[_Microsoft_UI_Composition.IVisual]],  # value
                          _type.HRESULT]
    TryRedirectForManipulation: _Callable[[_Microsoft_UI_Input.IPointerPoint],  # pointerPoint
                                          _type.HRESULT]


class IVisualInteractionSource2(_inspectable.IInspectable):
    get_DeltaPosition: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                                 _type.HRESULT]
    get_DeltaScale: _Callable[[_Pointer[_type.FLOAT]],  # value
                              _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                            _type.HRESULT]
    get_PositionVelocity: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                                    _type.HRESULT]
    get_Scale: _Callable[[_Pointer[_type.FLOAT]],  # value
                         _type.HRESULT]
    get_ScaleVelocity: _Callable[[_Pointer[_type.FLOAT]],  # value
                                 _type.HRESULT]
    ConfigureCenterPointXModifiers: _Callable[[_Windows_Foundation_Collections.IIterable[ICompositionConditionalValue]],  # conditionalValues
                                              _type.HRESULT]
    ConfigureCenterPointYModifiers: _Callable[[_Windows_Foundation_Collections.IIterable[ICompositionConditionalValue]],  # conditionalValues
                                              _type.HRESULT]
    ConfigureDeltaPositionXModifiers: _Callable[[_Windows_Foundation_Collections.IIterable[ICompositionConditionalValue]],  # conditionalValues
                                                _type.HRESULT]
    ConfigureDeltaPositionYModifiers: _Callable[[_Windows_Foundation_Collections.IIterable[ICompositionConditionalValue]],  # conditionalValues
                                                _type.HRESULT]
    ConfigureDeltaScaleModifiers: _Callable[[_Windows_Foundation_Collections.IIterable[ICompositionConditionalValue]],  # conditionalValues
                                            _type.HRESULT]


class IVisualInteractionSource3(_inspectable.IInspectable):
    get_PointerWheelConfig: _Callable[[_Pointer[IInteractionSourceConfiguration]],  # value
                                      _type.HRESULT]


class IVisualInteractionSourceObjectFactory(_inspectable.IInspectable):
    pass


class IVisualInteractionSourceStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Microsoft_UI_Composition.IVisual,  # source
                       _Pointer[IVisualInteractionSource]],  # result
                      _type.HRESULT]


class IVisualInteractionSourceStatics2(_inspectable.IInspectable, factory=True):
    CreateFromIVisualElement: _Callable[[_Microsoft_UI_Composition.IVisualElement,  # source
                                         _Pointer[IVisualInteractionSource]],  # result
                                        _type.HRESULT]
