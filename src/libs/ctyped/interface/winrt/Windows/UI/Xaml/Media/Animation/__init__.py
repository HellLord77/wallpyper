from __future__ import annotations

from typing import Callable as _Callable

from ... import Controls as _Windows_UI_Xaml_Controls
from .... import Composition as _Windows_UI_Composition
from .... import Xaml as _Windows_UI_Xaml
from ..... import Foundation as _Windows_Foundation
from .....Foundation import Collections as _Windows_Foundation_Collections
from ...... import inspectable as _inspectable
from ........ import enum as _enum
from ........ import struct as _struct
from ........ import type as _type
from ........_utils import _Pointer


class IAddDeleteThemeTransition(_inspectable.IInspectable):
    pass


class IBackEase(_inspectable.IInspectable):
    get_Amplitude: _Callable[[_Pointer[_type.DOUBLE]],  # value
                             _type.HRESULT]
    put_Amplitude: _Callable[[_type.DOUBLE],  # value
                             _type.HRESULT]


class IBackEaseStatics(_inspectable.IInspectable):
    get_AmplitudeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]

    _factory = True


class IBasicConnectedAnimationConfiguration(_inspectable.IInspectable):
    pass


class IBasicConnectedAnimationConfigurationFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IBasicConnectedAnimationConfiguration]],  # value
                              _type.HRESULT]


class IBeginStoryboard(_inspectable.IInspectable):
    get_Storyboard: _Callable[[_Pointer[IStoryboard]],  # value
                              _type.HRESULT]
    put_Storyboard: _Callable[[IStoryboard],  # value
                              _type.HRESULT]


class IBeginStoryboardStatics(_inspectable.IInspectable):
    get_StoryboardProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]

    _factory = True


class IBounceEase(_inspectable.IInspectable):
    get_Bounces: _Callable[[_Pointer[_type.INT32]],  # value
                           _type.HRESULT]
    put_Bounces: _Callable[[_type.INT32],  # value
                           _type.HRESULT]
    get_Bounciness: _Callable[[_Pointer[_type.DOUBLE]],  # value
                              _type.HRESULT]
    put_Bounciness: _Callable[[_type.DOUBLE],  # value
                              _type.HRESULT]


class IBounceEaseStatics(_inspectable.IInspectable):
    get_BouncesProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_BouncinessProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]

    _factory = True


class ICircleEase(_inspectable.IInspectable):
    pass


class IColorAnimation(_inspectable.IInspectable):
    get_From: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                        _type.HRESULT]
    put_From: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                        _type.HRESULT]
    get_To: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                      _type.HRESULT]
    put_To: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                      _type.HRESULT]
    get_By: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                      _type.HRESULT]
    put_By: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                      _type.HRESULT]
    get_EasingFunction: _Callable[[_Pointer[IEasingFunctionBase]],  # value
                                  _type.HRESULT]
    put_EasingFunction: _Callable[[IEasingFunctionBase],  # value
                                  _type.HRESULT]
    get_EnableDependentAnimation: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_EnableDependentAnimation: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]


class IColorAnimationStatics(_inspectable.IInspectable):
    get_FromProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]
    get_ToProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                              _type.HRESULT]
    get_ByProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                              _type.HRESULT]
    get_EasingFunctionProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_EnableDependentAnimationProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]

    _factory = True


class IColorAnimationUsingKeyFrames(_inspectable.IInspectable):
    get_KeyFrames: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IColorKeyFrame]]],  # value
                             _type.HRESULT]
    get_EnableDependentAnimation: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_EnableDependentAnimation: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]


class IColorAnimationUsingKeyFramesStatics(_inspectable.IInspectable):
    get_EnableDependentAnimationProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]

    _factory = True


class IColorKeyFrame(_inspectable.IInspectable):
    get_Value: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                         _type.HRESULT]
    put_Value: _Callable[[_struct.Windows.UI.Color],  # value
                         _type.HRESULT]
    get_KeyTime: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Media.Animation.KeyTime]],  # value
                           _type.HRESULT]
    put_KeyTime: _Callable[[_struct.Windows.UI.Xaml.Media.Animation.KeyTime],  # value
                           _type.HRESULT]


class IColorKeyFrameFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IColorKeyFrame]],  # value
                              _type.HRESULT]


class IColorKeyFrameStatics(_inspectable.IInspectable):
    get_ValueProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_KeyTimeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]

    _factory = True


class ICommonNavigationTransitionInfo(_inspectable.IInspectable):
    get_IsStaggeringEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_IsStaggeringEnabled: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]


class ICommonNavigationTransitionInfoStatics(_inspectable.IInspectable):
    get_IsStaggeringEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_IsStaggerElementProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    GetIsStaggerElement: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                    _Pointer[_type.boolean]],  # result
                                   _type.HRESULT]
    SetIsStaggerElement: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                    _type.boolean],  # value
                                   _type.HRESULT]

    _factory = True


class IConnectedAnimation(_inspectable.IInspectable):
    add_Completed: _Callable[[_Windows_Foundation.ITypedEventHandler[IConnectedAnimation, _inspectable.IInspectable],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_Completed: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    TryStart: _Callable[[_Windows_UI_Xaml.IUIElement,  # destination
                         _Pointer[_type.boolean]],  # result
                        _type.HRESULT]
    Cancel: _Callable[[],
                      _type.HRESULT]


class IConnectedAnimation2(_inspectable.IInspectable):
    get_IsScaleAnimationEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    put_IsScaleAnimationEnabled: _Callable[[_type.boolean],  # value
                                           _type.HRESULT]
    TryStartWithCoordinatedElements: _Callable[[_Windows_UI_Xaml.IUIElement,  # destination
                                                _Windows_Foundation_Collections.IIterable[_Windows_UI_Xaml.IUIElement],  # coordinatedElements
                                                _Pointer[_type.boolean]],  # result
                                               _type.HRESULT]
    SetAnimationComponent: _Callable[[_enum.Windows.UI.Xaml.Media.Animation.ConnectedAnimationComponent,  # component
                                      _Windows_UI_Composition.ICompositionAnimationBase],  # animation
                                     _type.HRESULT]


class IConnectedAnimation3(_inspectable.IInspectable):
    get_Configuration: _Callable[[_Pointer[IConnectedAnimationConfiguration]],  # value
                                 _type.HRESULT]
    put_Configuration: _Callable[[IConnectedAnimationConfiguration],  # value
                                 _type.HRESULT]


class IConnectedAnimationConfiguration(_inspectable.IInspectable):
    pass


class IConnectedAnimationConfigurationFactory(_inspectable.IInspectable):
    pass


class IConnectedAnimationService(_inspectable.IInspectable):
    get_DefaultDuration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                   _type.HRESULT]
    put_DefaultDuration: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                   _type.HRESULT]
    get_DefaultEasingFunction: _Callable[[_Pointer[_Windows_UI_Composition.ICompositionEasingFunction]],  # value
                                         _type.HRESULT]
    put_DefaultEasingFunction: _Callable[[_Windows_UI_Composition.ICompositionEasingFunction],  # value
                                         _type.HRESULT]
    PrepareToAnimate: _Callable[[_type.HSTRING,  # key
                                 _Windows_UI_Xaml.IUIElement,  # source
                                 _Pointer[IConnectedAnimation]],  # result
                                _type.HRESULT]
    GetAnimation: _Callable[[_type.HSTRING,  # key
                             _Pointer[IConnectedAnimation]],  # result
                            _type.HRESULT]


class IConnectedAnimationServiceStatics(_inspectable.IInspectable):
    GetForCurrentView: _Callable[[_Pointer[IConnectedAnimationService]],  # result
                                 _type.HRESULT]

    _factory = True


class IContentThemeTransition(_inspectable.IInspectable):
    get_HorizontalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]
    put_HorizontalOffset: _Callable[[_type.DOUBLE],  # value
                                    _type.HRESULT]
    get_VerticalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    put_VerticalOffset: _Callable[[_type.DOUBLE],  # value
                                  _type.HRESULT]


class IContentThemeTransitionStatics(_inspectable.IInspectable):
    get_HorizontalOffsetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_VerticalOffsetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]

    _factory = True


class IContinuumNavigationTransitionInfo(_inspectable.IInspectable):
    get_ExitElement: _Callable[[_Pointer[_Windows_UI_Xaml.IUIElement]],  # value
                               _type.HRESULT]
    put_ExitElement: _Callable[[_Windows_UI_Xaml.IUIElement],  # value
                               _type.HRESULT]


class IContinuumNavigationTransitionInfoStatics(_inspectable.IInspectable):
    get_ExitElementProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_IsEntranceElementProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    GetIsEntranceElement: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                     _Pointer[_type.boolean]],  # result
                                    _type.HRESULT]
    SetIsEntranceElement: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                     _type.boolean],  # value
                                    _type.HRESULT]
    get_IsExitElementProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    GetIsExitElement: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                 _Pointer[_type.boolean]],  # result
                                _type.HRESULT]
    SetIsExitElement: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                 _type.boolean],  # value
                                _type.HRESULT]
    get_ExitElementContainerProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    GetExitElementContainer: _Callable[[_Windows_UI_Xaml_Controls.IListViewBase,  # element
                                        _Pointer[_type.boolean]],  # result
                                       _type.HRESULT]
    SetExitElementContainer: _Callable[[_Windows_UI_Xaml_Controls.IListViewBase,  # element
                                        _type.boolean],  # value
                                       _type.HRESULT]

    _factory = True


class ICubicEase(_inspectable.IInspectable):
    pass


class IDirectConnectedAnimationConfiguration(_inspectable.IInspectable):
    pass


class IDirectConnectedAnimationConfigurationFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IDirectConnectedAnimationConfiguration]],  # value
                              _type.HRESULT]


class IDiscreteColorKeyFrame(_inspectable.IInspectable):
    pass


class IDiscreteDoubleKeyFrame(_inspectable.IInspectable):
    pass


class IDiscreteObjectKeyFrame(_inspectable.IInspectable):
    pass


class IDiscretePointKeyFrame(_inspectable.IInspectable):
    pass


class IDoubleAnimation(_inspectable.IInspectable):
    get_From: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                        _type.HRESULT]
    put_From: _Callable[[_Windows_Foundation.IReference[_type.DOUBLE]],  # value
                        _type.HRESULT]
    get_To: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                      _type.HRESULT]
    put_To: _Callable[[_Windows_Foundation.IReference[_type.DOUBLE]],  # value
                      _type.HRESULT]
    get_By: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                      _type.HRESULT]
    put_By: _Callable[[_Windows_Foundation.IReference[_type.DOUBLE]],  # value
                      _type.HRESULT]
    get_EasingFunction: _Callable[[_Pointer[IEasingFunctionBase]],  # value
                                  _type.HRESULT]
    put_EasingFunction: _Callable[[IEasingFunctionBase],  # value
                                  _type.HRESULT]
    get_EnableDependentAnimation: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_EnableDependentAnimation: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]


class IDoubleAnimationStatics(_inspectable.IInspectable):
    get_FromProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]
    get_ToProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                              _type.HRESULT]
    get_ByProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                              _type.HRESULT]
    get_EasingFunctionProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_EnableDependentAnimationProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]

    _factory = True


class IDoubleAnimationUsingKeyFrames(_inspectable.IInspectable):
    get_KeyFrames: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IDoubleKeyFrame]]],  # value
                             _type.HRESULT]
    get_EnableDependentAnimation: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_EnableDependentAnimation: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]


class IDoubleAnimationUsingKeyFramesStatics(_inspectable.IInspectable):
    get_EnableDependentAnimationProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]

    _factory = True


class IDoubleKeyFrame(_inspectable.IInspectable):
    get_Value: _Callable[[_Pointer[_type.DOUBLE]],  # value
                         _type.HRESULT]
    put_Value: _Callable[[_type.DOUBLE],  # value
                         _type.HRESULT]
    get_KeyTime: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Media.Animation.KeyTime]],  # value
                           _type.HRESULT]
    put_KeyTime: _Callable[[_struct.Windows.UI.Xaml.Media.Animation.KeyTime],  # value
                           _type.HRESULT]


class IDoubleKeyFrameFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IDoubleKeyFrame]],  # value
                              _type.HRESULT]


class IDoubleKeyFrameStatics(_inspectable.IInspectable):
    get_ValueProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_KeyTimeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]

    _factory = True


class IDragItemThemeAnimation(_inspectable.IInspectable):
    get_TargetName: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_TargetName: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]


class IDragItemThemeAnimationStatics(_inspectable.IInspectable):
    get_TargetNameProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]

    _factory = True


class IDragOverThemeAnimation(_inspectable.IInspectable):
    get_TargetName: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_TargetName: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]
    get_ToOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                            _type.HRESULT]
    put_ToOffset: _Callable[[_type.DOUBLE],  # value
                            _type.HRESULT]
    get_Direction: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Primitives.AnimationDirection]],  # value
                             _type.HRESULT]
    put_Direction: _Callable[[_enum.Windows.UI.Xaml.Controls.Primitives.AnimationDirection],  # value
                             _type.HRESULT]


class IDragOverThemeAnimationStatics(_inspectable.IInspectable):
    get_TargetNameProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_ToOffsetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_DirectionProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]

    _factory = True


class IDrillInNavigationTransitionInfo(_inspectable.IInspectable):
    pass


class IDrillInThemeAnimation(_inspectable.IInspectable):
    get_EntranceTargetName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    put_EntranceTargetName: _Callable[[_type.HSTRING],  # value
                                      _type.HRESULT]
    get_EntranceTarget: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyObject]],  # value
                                  _type.HRESULT]
    put_EntranceTarget: _Callable[[_Windows_UI_Xaml.IDependencyObject],  # value
                                  _type.HRESULT]
    get_ExitTargetName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    put_ExitTargetName: _Callable[[_type.HSTRING],  # value
                                  _type.HRESULT]
    get_ExitTarget: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyObject]],  # value
                              _type.HRESULT]
    put_ExitTarget: _Callable[[_Windows_UI_Xaml.IDependencyObject],  # value
                              _type.HRESULT]


class IDrillInThemeAnimationStatics(_inspectable.IInspectable):
    get_EntranceTargetNameProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_EntranceTargetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_ExitTargetNameProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_ExitTargetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]

    _factory = True


class IDrillOutThemeAnimation(_inspectable.IInspectable):
    get_EntranceTargetName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    put_EntranceTargetName: _Callable[[_type.HSTRING],  # value
                                      _type.HRESULT]
    get_EntranceTarget: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyObject]],  # value
                                  _type.HRESULT]
    put_EntranceTarget: _Callable[[_Windows_UI_Xaml.IDependencyObject],  # value
                                  _type.HRESULT]
    get_ExitTargetName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    put_ExitTargetName: _Callable[[_type.HSTRING],  # value
                                  _type.HRESULT]
    get_ExitTarget: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyObject]],  # value
                              _type.HRESULT]
    put_ExitTarget: _Callable[[_Windows_UI_Xaml.IDependencyObject],  # value
                              _type.HRESULT]


class IDrillOutThemeAnimationStatics(_inspectable.IInspectable):
    get_EntranceTargetNameProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_EntranceTargetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_ExitTargetNameProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_ExitTargetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]

    _factory = True


class IDropTargetItemThemeAnimation(_inspectable.IInspectable):
    get_TargetName: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_TargetName: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]


class IDropTargetItemThemeAnimationStatics(_inspectable.IInspectable):
    get_TargetNameProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]

    _factory = True


class IEasingColorKeyFrame(_inspectable.IInspectable):
    get_EasingFunction: _Callable[[_Pointer[IEasingFunctionBase]],  # value
                                  _type.HRESULT]
    put_EasingFunction: _Callable[[IEasingFunctionBase],  # value
                                  _type.HRESULT]


class IEasingColorKeyFrameStatics(_inspectable.IInspectable):
    get_EasingFunctionProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]

    _factory = True


class IEasingDoubleKeyFrame(_inspectable.IInspectable):
    get_EasingFunction: _Callable[[_Pointer[IEasingFunctionBase]],  # value
                                  _type.HRESULT]
    put_EasingFunction: _Callable[[IEasingFunctionBase],  # value
                                  _type.HRESULT]


class IEasingDoubleKeyFrameStatics(_inspectable.IInspectable):
    get_EasingFunctionProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]

    _factory = True


class IEasingFunctionBase(_inspectable.IInspectable):
    get_EasingMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Media.Animation.EasingMode]],  # value
                              _type.HRESULT]
    put_EasingMode: _Callable[[_enum.Windows.UI.Xaml.Media.Animation.EasingMode],  # value
                              _type.HRESULT]
    Ease: _Callable[[_type.DOUBLE,  # normalizedTime
                     _Pointer[_type.DOUBLE]],  # result
                    _type.HRESULT]


class IEasingFunctionBaseFactory(_inspectable.IInspectable):
    pass


class IEasingFunctionBaseStatics(_inspectable.IInspectable):
    get_EasingModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]

    _factory = True


class IEasingPointKeyFrame(_inspectable.IInspectable):
    get_EasingFunction: _Callable[[_Pointer[IEasingFunctionBase]],  # value
                                  _type.HRESULT]
    put_EasingFunction: _Callable[[IEasingFunctionBase],  # value
                                  _type.HRESULT]


class IEasingPointKeyFrameStatics(_inspectable.IInspectable):
    get_EasingFunctionProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]

    _factory = True


class IEdgeUIThemeTransition(_inspectable.IInspectable):
    get_Edge: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Primitives.EdgeTransitionLocation]],  # value
                        _type.HRESULT]
    put_Edge: _Callable[[_enum.Windows.UI.Xaml.Controls.Primitives.EdgeTransitionLocation],  # value
                        _type.HRESULT]


class IEdgeUIThemeTransitionStatics(_inspectable.IInspectable):
    get_EdgeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]

    _factory = True


class IElasticEase(_inspectable.IInspectable):
    get_Oscillations: _Callable[[_Pointer[_type.INT32]],  # value
                                _type.HRESULT]
    put_Oscillations: _Callable[[_type.INT32],  # value
                                _type.HRESULT]
    get_Springiness: _Callable[[_Pointer[_type.DOUBLE]],  # value
                               _type.HRESULT]
    put_Springiness: _Callable[[_type.DOUBLE],  # value
                               _type.HRESULT]


class IElasticEaseStatics(_inspectable.IInspectable):
    get_OscillationsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_SpringinessProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]

    _factory = True


class IEntranceNavigationTransitionInfo(_inspectable.IInspectable):
    pass


class IEntranceNavigationTransitionInfoStatics(_inspectable.IInspectable):
    get_IsTargetElementProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    GetIsTargetElement: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                   _Pointer[_type.boolean]],  # result
                                  _type.HRESULT]
    SetIsTargetElement: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                   _type.boolean],  # value
                                  _type.HRESULT]

    _factory = True


class IEntranceThemeTransition(_inspectable.IInspectable):
    get_FromHorizontalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                        _type.HRESULT]
    put_FromHorizontalOffset: _Callable[[_type.DOUBLE],  # value
                                        _type.HRESULT]
    get_FromVerticalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                      _type.HRESULT]
    put_FromVerticalOffset: _Callable[[_type.DOUBLE],  # value
                                      _type.HRESULT]
    get_IsStaggeringEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_IsStaggeringEnabled: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]


class IEntranceThemeTransitionStatics(_inspectable.IInspectable):
    get_FromHorizontalOffsetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_FromVerticalOffsetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_IsStaggeringEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]

    _factory = True


class IExponentialEase(_inspectable.IInspectable):
    get_Exponent: _Callable[[_Pointer[_type.DOUBLE]],  # value
                            _type.HRESULT]
    put_Exponent: _Callable[[_type.DOUBLE],  # value
                            _type.HRESULT]


class IExponentialEaseStatics(_inspectable.IInspectable):
    get_ExponentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]

    _factory = True


class IFadeInThemeAnimation(_inspectable.IInspectable):
    get_TargetName: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_TargetName: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]


class IFadeInThemeAnimationStatics(_inspectable.IInspectable):
    get_TargetNameProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]

    _factory = True


class IFadeOutThemeAnimation(_inspectable.IInspectable):
    get_TargetName: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_TargetName: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]


class IFadeOutThemeAnimationStatics(_inspectable.IInspectable):
    get_TargetNameProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]

    _factory = True


class IGravityConnectedAnimationConfiguration(_inspectable.IInspectable):
    pass


class IGravityConnectedAnimationConfiguration2(_inspectable.IInspectable):
    get_IsShadowEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    put_IsShadowEnabled: _Callable[[_type.boolean],  # value
                                   _type.HRESULT]


class IGravityConnectedAnimationConfigurationFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IGravityConnectedAnimationConfiguration]],  # value
                              _type.HRESULT]


class IKeySpline(_inspectable.IInspectable):
    get_ControlPoint1: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                                 _type.HRESULT]
    put_ControlPoint1: _Callable[[_struct.Windows.Foundation.Point],  # value
                                 _type.HRESULT]
    get_ControlPoint2: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                                 _type.HRESULT]
    put_ControlPoint2: _Callable[[_struct.Windows.Foundation.Point],  # value
                                 _type.HRESULT]


class IKeyTimeHelper(_inspectable.IInspectable):
    pass


class IKeyTimeHelperStatics(_inspectable.IInspectable):
    FromTimeSpan: _Callable[[_struct.Windows.Foundation.TimeSpan,  # timeSpan
                             _Pointer[_struct.Windows.UI.Xaml.Media.Animation.KeyTime]],  # result
                            _type.HRESULT]

    _factory = True


class ILinearColorKeyFrame(_inspectable.IInspectable):
    pass


class ILinearDoubleKeyFrame(_inspectable.IInspectable):
    pass


class ILinearPointKeyFrame(_inspectable.IInspectable):
    pass


class INavigationThemeTransition(_inspectable.IInspectable):
    get_DefaultNavigationTransitionInfo: _Callable[[_Pointer[INavigationTransitionInfo]],  # value
                                                   _type.HRESULT]
    put_DefaultNavigationTransitionInfo: _Callable[[INavigationTransitionInfo],  # value
                                                   _type.HRESULT]


class INavigationThemeTransitionStatics(_inspectable.IInspectable):
    get_DefaultNavigationTransitionInfoProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                           _type.HRESULT]

    _factory = True


class INavigationTransitionInfo(_inspectable.IInspectable):
    pass


class INavigationTransitionInfoFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[INavigationTransitionInfo]],  # value
                              _type.HRESULT]


class INavigationTransitionInfoOverrides(_inspectable.IInspectable):
    GetNavigationStateCore: _Callable[[_Pointer[_type.HSTRING]],  # result
                                      _type.HRESULT]
    SetNavigationStateCore: _Callable[[_type.HSTRING],  # navigationState
                                      _type.HRESULT]


class IObjectAnimationUsingKeyFrames(_inspectable.IInspectable):
    get_KeyFrames: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IObjectKeyFrame]]],  # value
                             _type.HRESULT]
    get_EnableDependentAnimation: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_EnableDependentAnimation: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]


class IObjectAnimationUsingKeyFramesStatics(_inspectable.IInspectable):
    get_EnableDependentAnimationProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]

    _factory = True


class IObjectKeyFrame(_inspectable.IInspectable):
    get_Value: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                         _type.HRESULT]
    put_Value: _Callable[[_inspectable.IInspectable],  # value
                         _type.HRESULT]
    get_KeyTime: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Media.Animation.KeyTime]],  # value
                           _type.HRESULT]
    put_KeyTime: _Callable[[_struct.Windows.UI.Xaml.Media.Animation.KeyTime],  # value
                           _type.HRESULT]


class IObjectKeyFrameFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IObjectKeyFrame]],  # value
                              _type.HRESULT]


class IObjectKeyFrameStatics(_inspectable.IInspectable):
    get_ValueProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_KeyTimeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]

    _factory = True


class IPaneThemeTransition(_inspectable.IInspectable):
    get_Edge: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Primitives.EdgeTransitionLocation]],  # value
                        _type.HRESULT]
    put_Edge: _Callable[[_enum.Windows.UI.Xaml.Controls.Primitives.EdgeTransitionLocation],  # value
                        _type.HRESULT]


class IPaneThemeTransitionStatics(_inspectable.IInspectable):
    get_EdgeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]

    _factory = True


class IPointAnimation(_inspectable.IInspectable):
    get_From: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.Point]]],  # value
                        _type.HRESULT]
    put_From: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.Point]],  # value
                        _type.HRESULT]
    get_To: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.Point]]],  # value
                      _type.HRESULT]
    put_To: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.Point]],  # value
                      _type.HRESULT]
    get_By: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.Point]]],  # value
                      _type.HRESULT]
    put_By: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.Point]],  # value
                      _type.HRESULT]
    get_EasingFunction: _Callable[[_Pointer[IEasingFunctionBase]],  # value
                                  _type.HRESULT]
    put_EasingFunction: _Callable[[IEasingFunctionBase],  # value
                                  _type.HRESULT]
    get_EnableDependentAnimation: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_EnableDependentAnimation: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]


class IPointAnimationStatics(_inspectable.IInspectable):
    get_FromProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]
    get_ToProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                              _type.HRESULT]
    get_ByProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                              _type.HRESULT]
    get_EasingFunctionProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_EnableDependentAnimationProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]

    _factory = True


class IPointAnimationUsingKeyFrames(_inspectable.IInspectable):
    get_KeyFrames: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IPointKeyFrame]]],  # value
                             _type.HRESULT]
    get_EnableDependentAnimation: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_EnableDependentAnimation: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]


class IPointAnimationUsingKeyFramesStatics(_inspectable.IInspectable):
    get_EnableDependentAnimationProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]

    _factory = True


class IPointKeyFrame(_inspectable.IInspectable):
    get_Value: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                         _type.HRESULT]
    put_Value: _Callable[[_struct.Windows.Foundation.Point],  # value
                         _type.HRESULT]
    get_KeyTime: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Media.Animation.KeyTime]],  # value
                           _type.HRESULT]
    put_KeyTime: _Callable[[_struct.Windows.UI.Xaml.Media.Animation.KeyTime],  # value
                           _type.HRESULT]


class IPointKeyFrameFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IPointKeyFrame]],  # value
                              _type.HRESULT]


class IPointKeyFrameStatics(_inspectable.IInspectable):
    get_ValueProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_KeyTimeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]

    _factory = True


class IPointerDownThemeAnimation(_inspectable.IInspectable):
    get_TargetName: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_TargetName: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]


class IPointerDownThemeAnimationStatics(_inspectable.IInspectable):
    get_TargetNameProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]

    _factory = True


class IPointerUpThemeAnimation(_inspectable.IInspectable):
    get_TargetName: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_TargetName: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]


class IPointerUpThemeAnimationStatics(_inspectable.IInspectable):
    get_TargetNameProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]

    _factory = True


class IPopInThemeAnimation(_inspectable.IInspectable):
    get_TargetName: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_TargetName: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]
    get_FromHorizontalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                        _type.HRESULT]
    put_FromHorizontalOffset: _Callable[[_type.DOUBLE],  # value
                                        _type.HRESULT]
    get_FromVerticalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                      _type.HRESULT]
    put_FromVerticalOffset: _Callable[[_type.DOUBLE],  # value
                                      _type.HRESULT]


class IPopInThemeAnimationStatics(_inspectable.IInspectable):
    get_TargetNameProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_FromHorizontalOffsetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_FromVerticalOffsetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]

    _factory = True


class IPopOutThemeAnimation(_inspectable.IInspectable):
    get_TargetName: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_TargetName: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]


class IPopOutThemeAnimationStatics(_inspectable.IInspectable):
    get_TargetNameProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]

    _factory = True


class IPopupThemeTransition(_inspectable.IInspectable):
    get_FromHorizontalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                        _type.HRESULT]
    put_FromHorizontalOffset: _Callable[[_type.DOUBLE],  # value
                                        _type.HRESULT]
    get_FromVerticalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                      _type.HRESULT]
    put_FromVerticalOffset: _Callable[[_type.DOUBLE],  # value
                                      _type.HRESULT]


class IPopupThemeTransitionStatics(_inspectable.IInspectable):
    get_FromHorizontalOffsetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_FromVerticalOffsetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]

    _factory = True


class IPowerEase(_inspectable.IInspectable):
    get_Power: _Callable[[_Pointer[_type.DOUBLE]],  # value
                         _type.HRESULT]
    put_Power: _Callable[[_type.DOUBLE],  # value
                         _type.HRESULT]


class IPowerEaseStatics(_inspectable.IInspectable):
    get_PowerProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]

    _factory = True


class IQuadraticEase(_inspectable.IInspectable):
    pass


class IQuarticEase(_inspectable.IInspectable):
    pass


class IQuinticEase(_inspectable.IInspectable):
    pass


class IReorderThemeTransition(_inspectable.IInspectable):
    pass


class IRepeatBehaviorHelper(_inspectable.IInspectable):
    pass


class IRepeatBehaviorHelperStatics(_inspectable.IInspectable):
    get_Forever: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Media.Animation.RepeatBehavior]],  # value
                           _type.HRESULT]
    FromCount: _Callable[[_type.DOUBLE,  # count
                          _Pointer[_struct.Windows.UI.Xaml.Media.Animation.RepeatBehavior]],  # result
                         _type.HRESULT]
    FromDuration: _Callable[[_struct.Windows.Foundation.TimeSpan,  # duration
                             _Pointer[_struct.Windows.UI.Xaml.Media.Animation.RepeatBehavior]],  # result
                            _type.HRESULT]
    GetHasCount: _Callable[[_struct.Windows.UI.Xaml.Media.Animation.RepeatBehavior,  # target
                            _Pointer[_type.boolean]],  # result
                           _type.HRESULT]
    GetHasDuration: _Callable[[_struct.Windows.UI.Xaml.Media.Animation.RepeatBehavior,  # target
                               _Pointer[_type.boolean]],  # result
                              _type.HRESULT]
    Equals: _Callable[[_struct.Windows.UI.Xaml.Media.Animation.RepeatBehavior,  # target
                       _struct.Windows.UI.Xaml.Media.Animation.RepeatBehavior,  # value
                       _Pointer[_type.boolean]],  # result
                      _type.HRESULT]

    _factory = True


class IRepositionThemeAnimation(_inspectable.IInspectable):
    get_TargetName: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_TargetName: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]
    get_FromHorizontalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                        _type.HRESULT]
    put_FromHorizontalOffset: _Callable[[_type.DOUBLE],  # value
                                        _type.HRESULT]
    get_FromVerticalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                      _type.HRESULT]
    put_FromVerticalOffset: _Callable[[_type.DOUBLE],  # value
                                      _type.HRESULT]


class IRepositionThemeAnimationStatics(_inspectable.IInspectable):
    get_TargetNameProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_FromHorizontalOffsetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_FromVerticalOffsetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]

    _factory = True


class IRepositionThemeTransition(_inspectable.IInspectable):
    pass


class IRepositionThemeTransition2(_inspectable.IInspectable):
    get_IsStaggeringEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_IsStaggeringEnabled: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]


class IRepositionThemeTransitionStatics2(_inspectable.IInspectable):
    get_IsStaggeringEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]

    _factory = True


class ISineEase(_inspectable.IInspectable):
    pass


class ISlideNavigationTransitionInfo(_inspectable.IInspectable):
    pass


class ISlideNavigationTransitionInfo2(_inspectable.IInspectable):
    get_Effect: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Media.Animation.SlideNavigationTransitionEffect]],  # value
                          _type.HRESULT]
    put_Effect: _Callable[[_enum.Windows.UI.Xaml.Media.Animation.SlideNavigationTransitionEffect],  # value
                          _type.HRESULT]


class ISlideNavigationTransitionInfoStatics2(_inspectable.IInspectable):
    get_EffectProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]

    _factory = True


class ISplineColorKeyFrame(_inspectable.IInspectable):
    get_KeySpline: _Callable[[_Pointer[IKeySpline]],  # value
                             _type.HRESULT]
    put_KeySpline: _Callable[[IKeySpline],  # value
                             _type.HRESULT]


class ISplineColorKeyFrameStatics(_inspectable.IInspectable):
    get_KeySplineProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]

    _factory = True


class ISplineDoubleKeyFrame(_inspectable.IInspectable):
    get_KeySpline: _Callable[[_Pointer[IKeySpline]],  # value
                             _type.HRESULT]
    put_KeySpline: _Callable[[IKeySpline],  # value
                             _type.HRESULT]


class ISplineDoubleKeyFrameStatics(_inspectable.IInspectable):
    get_KeySplineProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]

    _factory = True


class ISplinePointKeyFrame(_inspectable.IInspectable):
    get_KeySpline: _Callable[[_Pointer[IKeySpline]],  # value
                             _type.HRESULT]
    put_KeySpline: _Callable[[IKeySpline],  # value
                             _type.HRESULT]


class ISplinePointKeyFrameStatics(_inspectable.IInspectable):
    get_KeySplineProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]

    _factory = True


class ISplitCloseThemeAnimation(_inspectable.IInspectable):
    get_OpenedTargetName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    put_OpenedTargetName: _Callable[[_type.HSTRING],  # value
                                    _type.HRESULT]
    get_OpenedTarget: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyObject]],  # value
                                _type.HRESULT]
    put_OpenedTarget: _Callable[[_Windows_UI_Xaml.IDependencyObject],  # value
                                _type.HRESULT]
    get_ClosedTargetName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    put_ClosedTargetName: _Callable[[_type.HSTRING],  # value
                                    _type.HRESULT]
    get_ClosedTarget: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyObject]],  # value
                                _type.HRESULT]
    put_ClosedTarget: _Callable[[_Windows_UI_Xaml.IDependencyObject],  # value
                                _type.HRESULT]
    get_ContentTargetName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    put_ContentTargetName: _Callable[[_type.HSTRING],  # value
                                     _type.HRESULT]
    get_ContentTarget: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyObject]],  # value
                                 _type.HRESULT]
    put_ContentTarget: _Callable[[_Windows_UI_Xaml.IDependencyObject],  # value
                                 _type.HRESULT]
    get_OpenedLength: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    put_OpenedLength: _Callable[[_type.DOUBLE],  # value
                                _type.HRESULT]
    get_ClosedLength: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    put_ClosedLength: _Callable[[_type.DOUBLE],  # value
                                _type.HRESULT]
    get_OffsetFromCenter: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]
    put_OffsetFromCenter: _Callable[[_type.DOUBLE],  # value
                                    _type.HRESULT]
    get_ContentTranslationDirection: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Primitives.AnimationDirection]],  # value
                                               _type.HRESULT]
    put_ContentTranslationDirection: _Callable[[_enum.Windows.UI.Xaml.Controls.Primitives.AnimationDirection],  # value
                                               _type.HRESULT]
    get_ContentTranslationOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                            _type.HRESULT]
    put_ContentTranslationOffset: _Callable[[_type.DOUBLE],  # value
                                            _type.HRESULT]


class ISplitCloseThemeAnimationStatics(_inspectable.IInspectable):
    get_OpenedTargetNameProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_OpenedTargetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_ClosedTargetNameProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_ClosedTargetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_ContentTargetNameProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_ContentTargetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_OpenedLengthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_ClosedLengthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_OffsetFromCenterProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_ContentTranslationDirectionProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]
    get_ContentTranslationOffsetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]

    _factory = True


class ISplitOpenThemeAnimation(_inspectable.IInspectable):
    get_OpenedTargetName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    put_OpenedTargetName: _Callable[[_type.HSTRING],  # value
                                    _type.HRESULT]
    get_OpenedTarget: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyObject]],  # value
                                _type.HRESULT]
    put_OpenedTarget: _Callable[[_Windows_UI_Xaml.IDependencyObject],  # value
                                _type.HRESULT]
    get_ClosedTargetName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    put_ClosedTargetName: _Callable[[_type.HSTRING],  # value
                                    _type.HRESULT]
    get_ClosedTarget: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyObject]],  # value
                                _type.HRESULT]
    put_ClosedTarget: _Callable[[_Windows_UI_Xaml.IDependencyObject],  # value
                                _type.HRESULT]
    get_ContentTargetName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    put_ContentTargetName: _Callable[[_type.HSTRING],  # value
                                     _type.HRESULT]
    get_ContentTarget: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyObject]],  # value
                                 _type.HRESULT]
    put_ContentTarget: _Callable[[_Windows_UI_Xaml.IDependencyObject],  # value
                                 _type.HRESULT]
    get_OpenedLength: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    put_OpenedLength: _Callable[[_type.DOUBLE],  # value
                                _type.HRESULT]
    get_ClosedLength: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    put_ClosedLength: _Callable[[_type.DOUBLE],  # value
                                _type.HRESULT]
    get_OffsetFromCenter: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]
    put_OffsetFromCenter: _Callable[[_type.DOUBLE],  # value
                                    _type.HRESULT]
    get_ContentTranslationDirection: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Primitives.AnimationDirection]],  # value
                                               _type.HRESULT]
    put_ContentTranslationDirection: _Callable[[_enum.Windows.UI.Xaml.Controls.Primitives.AnimationDirection],  # value
                                               _type.HRESULT]
    get_ContentTranslationOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                            _type.HRESULT]
    put_ContentTranslationOffset: _Callable[[_type.DOUBLE],  # value
                                            _type.HRESULT]


class ISplitOpenThemeAnimationStatics(_inspectable.IInspectable):
    get_OpenedTargetNameProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_OpenedTargetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_ClosedTargetNameProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_ClosedTargetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_ContentTargetNameProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_ContentTargetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_OpenedLengthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_ClosedLengthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_OffsetFromCenterProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_ContentTranslationDirectionProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]
    get_ContentTranslationOffsetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]

    _factory = True


class IStoryboard(_inspectable.IInspectable):
    get_Children: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ITimeline]]],  # value
                            _type.HRESULT]
    Seek: _Callable[[_struct.Windows.Foundation.TimeSpan],  # offset
                    _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    Begin: _Callable[[],
                     _type.HRESULT]
    Pause: _Callable[[],
                     _type.HRESULT]
    Resume: _Callable[[],
                      _type.HRESULT]
    GetCurrentState: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Media.Animation.ClockState]],  # result
                               _type.HRESULT]
    GetCurrentTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # result
                              _type.HRESULT]
    SeekAlignedToLastTick: _Callable[[_struct.Windows.Foundation.TimeSpan],  # offset
                                     _type.HRESULT]
    SkipToFill: _Callable[[],
                          _type.HRESULT]


class IStoryboardStatics(_inspectable.IInspectable):
    get_TargetPropertyProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    GetTargetProperty: _Callable[[ITimeline,  # element
                                  _Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]
    SetTargetProperty: _Callable[[ITimeline,  # element
                                  _type.HSTRING],  # path
                                 _type.HRESULT]
    get_TargetNameProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    GetTargetName: _Callable[[ITimeline,  # element
                              _Pointer[_type.HSTRING]],  # result
                             _type.HRESULT]
    SetTargetName: _Callable[[ITimeline,  # element
                              _type.HSTRING],  # name
                             _type.HRESULT]
    SetTarget: _Callable[[ITimeline,  # timeline
                          _Windows_UI_Xaml.IDependencyObject],  # target
                         _type.HRESULT]

    _factory = True


class ISuppressNavigationTransitionInfo(_inspectable.IInspectable):
    pass


class ISwipeBackThemeAnimation(_inspectable.IInspectable):
    get_TargetName: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_TargetName: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]
    get_FromHorizontalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                        _type.HRESULT]
    put_FromHorizontalOffset: _Callable[[_type.DOUBLE],  # value
                                        _type.HRESULT]
    get_FromVerticalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                      _type.HRESULT]
    put_FromVerticalOffset: _Callable[[_type.DOUBLE],  # value
                                      _type.HRESULT]


class ISwipeBackThemeAnimationStatics(_inspectable.IInspectable):
    get_TargetNameProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_FromHorizontalOffsetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_FromVerticalOffsetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]

    _factory = True


class ISwipeHintThemeAnimation(_inspectable.IInspectable):
    get_TargetName: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_TargetName: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]
    get_ToHorizontalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                      _type.HRESULT]
    put_ToHorizontalOffset: _Callable[[_type.DOUBLE],  # value
                                      _type.HRESULT]
    get_ToVerticalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]
    put_ToVerticalOffset: _Callable[[_type.DOUBLE],  # value
                                    _type.HRESULT]


class ISwipeHintThemeAnimationStatics(_inspectable.IInspectable):
    get_TargetNameProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_ToHorizontalOffsetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_ToVerticalOffsetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]

    _factory = True


class ITimeline(_inspectable.IInspectable):
    get_AutoReverse: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    put_AutoReverse: _Callable[[_type.boolean],  # value
                               _type.HRESULT]
    get_BeginTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                             _type.HRESULT]
    put_BeginTime: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]],  # value
                             _type.HRESULT]
    get_Duration: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Duration]],  # value
                            _type.HRESULT]
    put_Duration: _Callable[[_struct.Windows.UI.Xaml.Duration],  # value
                            _type.HRESULT]
    get_SpeedRatio: _Callable[[_Pointer[_type.DOUBLE]],  # value
                              _type.HRESULT]
    put_SpeedRatio: _Callable[[_type.DOUBLE],  # value
                              _type.HRESULT]
    get_FillBehavior: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Media.Animation.FillBehavior]],  # value
                                _type.HRESULT]
    put_FillBehavior: _Callable[[_enum.Windows.UI.Xaml.Media.Animation.FillBehavior],  # value
                                _type.HRESULT]
    get_RepeatBehavior: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Media.Animation.RepeatBehavior]],  # value
                                  _type.HRESULT]
    put_RepeatBehavior: _Callable[[_struct.Windows.UI.Xaml.Media.Animation.RepeatBehavior],  # value
                                  _type.HRESULT]
    add_Completed: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_Completed: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]


class ITimelineFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ITimeline]],  # value
                              _type.HRESULT]


class ITimelineStatics(_inspectable.IInspectable):
    get_AllowDependentAnimations: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_AllowDependentAnimations: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]
    get_AutoReverseProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_BeginTimeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_DurationProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_SpeedRatioProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_FillBehaviorProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_RepeatBehaviorProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]

    _factory = True


class ITransition(_inspectable.IInspectable):
    pass


class ITransitionFactory(_inspectable.IInspectable):
    pass
