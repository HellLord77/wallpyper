from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IKnownSimpleHapticsControllerWaveformsStatics(_inspectable.IInspectable, factory=True):
    get_Click: _Callable[[_Pointer[_type.UINT16]],  # value
                         _type.HRESULT]
    get_BuzzContinuous: _Callable[[_Pointer[_type.UINT16]],  # value
                                  _type.HRESULT]
    get_RumbleContinuous: _Callable[[_Pointer[_type.UINT16]],  # value
                                    _type.HRESULT]
    get_Press: _Callable[[_Pointer[_type.UINT16]],  # value
                         _type.HRESULT]
    get_Release: _Callable[[_Pointer[_type.UINT16]],  # value
                           _type.HRESULT]


class IKnownSimpleHapticsControllerWaveformsStatics2(_inspectable.IInspectable, factory=True):
    get_BrushContinuous: _Callable[[_Pointer[_type.UINT16]],  # value
                                   _type.HRESULT]
    get_ChiselMarkerContinuous: _Callable[[_Pointer[_type.UINT16]],  # value
                                          _type.HRESULT]
    get_EraserContinuous: _Callable[[_Pointer[_type.UINT16]],  # value
                                    _type.HRESULT]
    get_Error: _Callable[[_Pointer[_type.UINT16]],  # value
                         _type.HRESULT]
    get_GalaxyPenContinuous: _Callable[[_Pointer[_type.UINT16]],  # value
                                       _type.HRESULT]
    get_Hover: _Callable[[_Pointer[_type.UINT16]],  # value
                         _type.HRESULT]
    get_InkContinuous: _Callable[[_Pointer[_type.UINT16]],  # value
                                 _type.HRESULT]
    get_MarkerContinuous: _Callable[[_Pointer[_type.UINT16]],  # value
                                    _type.HRESULT]
    get_PencilContinuous: _Callable[[_Pointer[_type.UINT16]],  # value
                                    _type.HRESULT]
    get_Success: _Callable[[_Pointer[_type.UINT16]],  # value
                           _type.HRESULT]


class ISimpleHapticsController(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_SupportedFeedback: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[ISimpleHapticsControllerFeedback]]],  # value
                                     _type.HRESULT]
    get_IsIntensitySupported: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_IsPlayCountSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_IsPlayDurationSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    get_IsReplayPauseIntervalSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                  _type.HRESULT]
    StopFeedback: _Callable[[],
                            _type.HRESULT]
    SendHapticFeedback: _Callable[[ISimpleHapticsControllerFeedback],  # feedback
                                  _type.HRESULT]
    SendHapticFeedbackWithIntensity: _Callable[[ISimpleHapticsControllerFeedback,  # feedback
                                                _type.DOUBLE],  # intensity
                                               _type.HRESULT]
    SendHapticFeedbackForDuration: _Callable[[ISimpleHapticsControllerFeedback,  # feedback
                                              _type.DOUBLE,  # intensity
                                              _struct.Windows.Foundation.TimeSpan],  # playDuration
                                             _type.HRESULT]
    SendHapticFeedbackForPlayCount: _Callable[[ISimpleHapticsControllerFeedback,  # feedback
                                               _type.DOUBLE,  # intensity
                                               _type.INT32,  # playCount
                                               _struct.Windows.Foundation.TimeSpan],  # replayPauseInterval
                                              _type.HRESULT]


class ISimpleHapticsControllerFeedback(_inspectable.IInspectable):
    get_Waveform: _Callable[[_Pointer[_type.UINT16]],  # value
                            _type.HRESULT]
    get_Duration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]


class IVibrationDevice(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_SimpleHapticsController: _Callable[[_Pointer[ISimpleHapticsController]],  # value
                                           _type.HRESULT]


class IVibrationDeviceStatics(_inspectable.IInspectable, factory=True):
    RequestAccessAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Devices.Haptics.VibrationAccessStatus]]],  # operation
                                  _type.HRESULT]
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IVibrationDevice]]],  # operation
                           _type.HRESULT]
    GetDefaultAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IVibrationDevice]]],  # operation
                               _type.HRESULT]
    FindAllAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IVibrationDevice]]]],  # operation
                            _type.HRESULT]
