from __future__ import annotations

from typing import Callable as _Callable

from ... import Capture as _Windows_Media_Capture
from .... import Foundation as _Windows_Foundation
from ..... import inspectable as _inspectable
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IVariablePhotoCapturedEventArgs(_inspectable.IInspectable):
    get_Frame: _Callable[[_Pointer[_Windows_Media_Capture.ICapturedFrame]],  # value
                         _type.HRESULT]
    get_CaptureTimeOffset: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                     _type.HRESULT]
    get_UsedFrameControllerIndex: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                                            _type.HRESULT]
    get_CapturedFrameControlValues: _Callable[[_Pointer[_Windows_Media_Capture.ICapturedFrameControlValues]],  # value
                                              _type.HRESULT]


class IVariablePhotoSequenceCapture(_inspectable.IInspectable):
    StartAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                          _type.HRESULT]
    StopAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                         _type.HRESULT]
    FinishAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                           _type.HRESULT]
    add_PhotoCaptured: _Callable[[_Windows_Foundation.ITypedEventHandler[IVariablePhotoSequenceCapture, IVariablePhotoCapturedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_PhotoCaptured: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_Stopped: _Callable[[_Windows_Foundation.ITypedEventHandler[IVariablePhotoSequenceCapture, _inspectable.IInspectable],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Stopped: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]


class IVariablePhotoSequenceCapture2(_inspectable.IInspectable):
    UpdateSettingsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                   _type.HRESULT]
