from __future__ import annotations

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IConditionForceEffect(_inspectable.IInspectable):
    get_Kind: _Callable[[_Pointer[_enum.Windows.Gaming.Input.ForceFeedback.ConditionForceEffectKind]],  # value
                        _type.HRESULT]
    SetParameters: _Callable[[_struct.Windows.Foundation.Numerics.Vector3,  # direction
                              _type.FLOAT,  # positiveCoefficient
                              _type.FLOAT,  # negativeCoefficient
                              _type.FLOAT,  # maxPositiveMagnitude
                              _type.FLOAT,  # maxNegativeMagnitude
                              _type.FLOAT,  # deadZone
                              _type.FLOAT],  # bias
                             _type.HRESULT]


class IConditionForceEffectFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[_enum.Windows.Gaming.Input.ForceFeedback.ConditionForceEffectKind,  # effectKind
                               _Pointer[IForceFeedbackEffect]],  # value
                              _type.HRESULT]


class IConstantForceEffect(_inspectable.IInspectable):
    SetParameters: _Callable[[_struct.Windows.Foundation.Numerics.Vector3,  # vector
                              _struct.Windows.Foundation.TimeSpan],  # duration
                             _type.HRESULT]
    SetParametersWithEnvelope: _Callable[[_struct.Windows.Foundation.Numerics.Vector3,  # vector
                                          _type.FLOAT,  # attackGain
                                          _type.FLOAT,  # sustainGain
                                          _type.FLOAT,  # releaseGain
                                          _struct.Windows.Foundation.TimeSpan,  # startDelay
                                          _struct.Windows.Foundation.TimeSpan,  # attackDuration
                                          _struct.Windows.Foundation.TimeSpan,  # sustainDuration
                                          _struct.Windows.Foundation.TimeSpan,  # releaseDuration
                                          _type.UINT32],  # repeatCount
                                         _type.HRESULT]


class IForceFeedbackEffect(_inspectable.IInspectable):
    get_Gain: _Callable[[_Pointer[_type.DOUBLE]],  # value
                        _type.HRESULT]
    put_Gain: _Callable[[_type.DOUBLE],  # value
                        _type.HRESULT]
    get_State: _Callable[[_Pointer[_enum.Windows.Gaming.Input.ForceFeedback.ForceFeedbackEffectState]],  # value
                         _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]


class IForceFeedbackMotor(_inspectable.IInspectable):
    get_AreEffectsPaused: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_MasterGain: _Callable[[_Pointer[_type.DOUBLE]],  # value
                              _type.HRESULT]
    put_MasterGain: _Callable[[_type.DOUBLE],  # value
                              _type.HRESULT]
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_SupportedAxes: _Callable[[_Pointer[_enum.Windows.Gaming.Input.ForceFeedback.ForceFeedbackEffectAxes]],  # value
                                 _type.HRESULT]
    LoadEffectAsync: _Callable[[IForceFeedbackEffect,  # effect
                                _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Gaming.Input.ForceFeedback.ForceFeedbackLoadEffectResult]]],  # asyncOperation
                               _type.HRESULT]
    PauseAllEffects: _Callable[[],
                               _type.HRESULT]
    ResumeAllEffects: _Callable[[],
                                _type.HRESULT]
    StopAllEffects: _Callable[[],
                              _type.HRESULT]
    TryDisableAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # asyncOperation
                               _type.HRESULT]
    TryEnableAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # asyncOperation
                              _type.HRESULT]
    TryResetAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # asyncOperation
                             _type.HRESULT]
    TryUnloadEffectAsync: _Callable[[IForceFeedbackEffect,  # effect
                                     _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # asyncOperation
                                    _type.HRESULT]


class IPeriodicForceEffect(_inspectable.IInspectable):
    get_Kind: _Callable[[_Pointer[_enum.Windows.Gaming.Input.ForceFeedback.PeriodicForceEffectKind]],  # value
                        _type.HRESULT]
    SetParameters: _Callable[[_struct.Windows.Foundation.Numerics.Vector3,  # vector
                              _type.FLOAT,  # frequency
                              _type.FLOAT,  # phase
                              _type.FLOAT,  # bias
                              _struct.Windows.Foundation.TimeSpan],  # duration
                             _type.HRESULT]
    SetParametersWithEnvelope: _Callable[[_struct.Windows.Foundation.Numerics.Vector3,  # vector
                                          _type.FLOAT,  # frequency
                                          _type.FLOAT,  # phase
                                          _type.FLOAT,  # bias
                                          _type.FLOAT,  # attackGain
                                          _type.FLOAT,  # sustainGain
                                          _type.FLOAT,  # releaseGain
                                          _struct.Windows.Foundation.TimeSpan,  # startDelay
                                          _struct.Windows.Foundation.TimeSpan,  # attackDuration
                                          _struct.Windows.Foundation.TimeSpan,  # sustainDuration
                                          _struct.Windows.Foundation.TimeSpan,  # releaseDuration
                                          _type.UINT32],  # repeatCount
                                         _type.HRESULT]


class IPeriodicForceEffectFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[_enum.Windows.Gaming.Input.ForceFeedback.PeriodicForceEffectKind,  # effectKind
                               _Pointer[IForceFeedbackEffect]],  # value
                              _type.HRESULT]


class IRampForceEffect(_inspectable.IInspectable):
    SetParameters: _Callable[[_struct.Windows.Foundation.Numerics.Vector3,  # startVector
                              _struct.Windows.Foundation.Numerics.Vector3,  # endVector
                              _struct.Windows.Foundation.TimeSpan],  # duration
                             _type.HRESULT]
    SetParametersWithEnvelope: _Callable[[_struct.Windows.Foundation.Numerics.Vector3,  # startVector
                                          _struct.Windows.Foundation.Numerics.Vector3,  # endVector
                                          _type.FLOAT,  # attackGain
                                          _type.FLOAT,  # sustainGain
                                          _type.FLOAT,  # releaseGain
                                          _struct.Windows.Foundation.TimeSpan,  # startDelay
                                          _struct.Windows.Foundation.TimeSpan,  # attackDuration
                                          _struct.Windows.Foundation.TimeSpan,  # sustainDuration
                                          _struct.Windows.Foundation.TimeSpan,  # releaseDuration
                                          _type.UINT32],  # repeatCount
                                         _type.HRESULT]
