from __future__ import annotations as _

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IAnimationDescription(_inspectable.IInspectable):
    get_Animations: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IPropertyAnimation]]],  # value
                              _type.HRESULT]
    get_StaggerDelay: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                _type.HRESULT]
    get_StaggerDelayFactor: _Callable[[_Pointer[_type.FLOAT]],  # value
                                      _type.HRESULT]
    get_DelayLimit: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                              _type.HRESULT]
    get_ZOrder: _Callable[[_Pointer[_type.INT32]],  # value
                          _type.HRESULT]


class IAnimationDescriptionFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_enum.Windows.UI.Core.AnimationMetrics.AnimationEffect,  # effect
                               _enum.Windows.UI.Core.AnimationMetrics.AnimationEffectTarget,  # target
                               _Pointer[IAnimationDescription]],  # animation
                              _type.HRESULT]

    _factory = True


class IOpacityAnimation(_inspectable.IInspectable):
    get_InitialOpacity: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.FLOAT]]],  # value
                                  _type.HRESULT]
    get_FinalOpacity: _Callable[[_Pointer[_type.FLOAT]],  # value
                                _type.HRESULT]


class IPropertyAnimation(_inspectable.IInspectable):
    get_Type: _Callable[[_Pointer[_enum.Windows.UI.Core.AnimationMetrics.PropertyAnimationType]],  # value
                        _type.HRESULT]
    get_Delay: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                         _type.HRESULT]
    get_Duration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    get_Control1: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    get_Control2: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]


class IScaleAnimation(_inspectable.IInspectable):
    get_InitialScaleX: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.FLOAT]]],  # value
                                 _type.HRESULT]
    get_InitialScaleY: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.FLOAT]]],  # value
                                 _type.HRESULT]
    get_FinalScaleX: _Callable[[_Pointer[_type.FLOAT]],  # value
                               _type.HRESULT]
    get_FinalScaleY: _Callable[[_Pointer[_type.FLOAT]],  # value
                               _type.HRESULT]
    get_NormalizedOrigin: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                                    _type.HRESULT]
