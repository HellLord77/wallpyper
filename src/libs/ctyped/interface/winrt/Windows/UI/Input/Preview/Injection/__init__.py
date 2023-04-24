from __future__ import annotations

from typing import Callable as _Callable

from .....Foundation import Collections as _Windows_Foundation_Collections
from ...... import inspectable as _inspectable
from ........ import enum as _enum
from ........ import struct as _struct
from ........ import type as _type
from ........_utils import _Pointer


class IInjectedInputGamepadInfo(_inspectable.IInspectable):
    get_Buttons: _Callable[[_Pointer[_enum.Windows.Gaming.Input.GamepadButtons]],  # value
                           _type.HRESULT]
    put_Buttons: _Callable[[_enum.Windows.Gaming.Input.GamepadButtons],  # value
                           _type.HRESULT]
    get_LeftThumbstickX: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                   _type.HRESULT]
    put_LeftThumbstickX: _Callable[[_type.DOUBLE],  # value
                                   _type.HRESULT]
    get_LeftThumbstickY: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                   _type.HRESULT]
    put_LeftThumbstickY: _Callable[[_type.DOUBLE],  # value
                                   _type.HRESULT]
    get_LeftTrigger: _Callable[[_Pointer[_type.DOUBLE]],  # value
                               _type.HRESULT]
    put_LeftTrigger: _Callable[[_type.DOUBLE],  # value
                               _type.HRESULT]
    get_RightThumbstickX: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]
    put_RightThumbstickX: _Callable[[_type.DOUBLE],  # value
                                    _type.HRESULT]
    get_RightThumbstickY: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]
    put_RightThumbstickY: _Callable[[_type.DOUBLE],  # value
                                    _type.HRESULT]
    get_RightTrigger: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    put_RightTrigger: _Callable[[_type.DOUBLE],  # value
                                _type.HRESULT]


class IInjectedInputGamepadInfoFactory(_inspectable.IInspectable):
    CreateInstanceFromGamepadReading: _Callable[[_struct.Windows.Gaming.Input.GamepadReading,  # reading
                                                 _Pointer[IInjectedInputGamepadInfo]],  # value
                                                _type.HRESULT]

    _factory = True


class IInjectedInputKeyboardInfo(_inspectable.IInspectable):
    get_KeyOptions: _Callable[[_Pointer[_enum.Windows.UI.Input.Preview.Injection.InjectedInputKeyOptions]],  # value
                              _type.HRESULT]
    put_KeyOptions: _Callable[[_enum.Windows.UI.Input.Preview.Injection.InjectedInputKeyOptions],  # value
                              _type.HRESULT]
    get_ScanCode: _Callable[[_Pointer[_type.UINT16]],  # value
                            _type.HRESULT]
    put_ScanCode: _Callable[[_type.UINT16],  # value
                            _type.HRESULT]
    get_VirtualKey: _Callable[[_Pointer[_type.UINT16]],  # value
                              _type.HRESULT]
    put_VirtualKey: _Callable[[_type.UINT16],  # value
                              _type.HRESULT]


class IInjectedInputMouseInfo(_inspectable.IInspectable):
    get_MouseOptions: _Callable[[_Pointer[_enum.Windows.UI.Input.Preview.Injection.InjectedInputMouseOptions]],  # value
                                _type.HRESULT]
    put_MouseOptions: _Callable[[_enum.Windows.UI.Input.Preview.Injection.InjectedInputMouseOptions],  # value
                                _type.HRESULT]
    get_MouseData: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    put_MouseData: _Callable[[_type.UINT32],  # value
                             _type.HRESULT]
    get_DeltaY: _Callable[[_Pointer[_type.INT32]],  # value
                          _type.HRESULT]
    put_DeltaY: _Callable[[_type.INT32],  # value
                          _type.HRESULT]
    get_DeltaX: _Callable[[_Pointer[_type.INT32]],  # value
                          _type.HRESULT]
    put_DeltaX: _Callable[[_type.INT32],  # value
                          _type.HRESULT]
    get_TimeOffsetInMilliseconds: _Callable[[_Pointer[_type.UINT32]],  # value
                                            _type.HRESULT]
    put_TimeOffsetInMilliseconds: _Callable[[_type.UINT32],  # value
                                            _type.HRESULT]


class IInjectedInputPenInfo(_inspectable.IInspectable):
    get_PointerInfo: _Callable[[_Pointer[_struct.Windows.UI.Input.Preview.Injection.InjectedInputPointerInfo]],  # value
                               _type.HRESULT]
    put_PointerInfo: _Callable[[_struct.Windows.UI.Input.Preview.Injection.InjectedInputPointerInfo],  # value
                               _type.HRESULT]
    get_PenButtons: _Callable[[_Pointer[_enum.Windows.UI.Input.Preview.Injection.InjectedInputPenButtons]],  # value
                              _type.HRESULT]
    put_PenButtons: _Callable[[_enum.Windows.UI.Input.Preview.Injection.InjectedInputPenButtons],  # value
                              _type.HRESULT]
    get_PenParameters: _Callable[[_Pointer[_enum.Windows.UI.Input.Preview.Injection.InjectedInputPenParameters]],  # value
                                 _type.HRESULT]
    put_PenParameters: _Callable[[_enum.Windows.UI.Input.Preview.Injection.InjectedInputPenParameters],  # value
                                 _type.HRESULT]
    get_Pressure: _Callable[[_Pointer[_type.DOUBLE]],  # value
                            _type.HRESULT]
    put_Pressure: _Callable[[_type.DOUBLE],  # value
                            _type.HRESULT]
    get_Rotation: _Callable[[_Pointer[_type.DOUBLE]],  # value
                            _type.HRESULT]
    put_Rotation: _Callable[[_type.DOUBLE],  # value
                            _type.HRESULT]
    get_TiltX: _Callable[[_Pointer[_type.INT32]],  # value
                         _type.HRESULT]
    put_TiltX: _Callable[[_type.INT32],  # value
                         _type.HRESULT]
    get_TiltY: _Callable[[_Pointer[_type.INT32]],  # value
                         _type.HRESULT]
    put_TiltY: _Callable[[_type.INT32],  # value
                         _type.HRESULT]


class IInjectedInputTouchInfo(_inspectable.IInspectable):
    get_Contact: _Callable[[_Pointer[_struct.Windows.UI.Input.Preview.Injection.InjectedInputRectangle]],  # value
                           _type.HRESULT]
    put_Contact: _Callable[[_struct.Windows.UI.Input.Preview.Injection.InjectedInputRectangle],  # value
                           _type.HRESULT]
    get_Orientation: _Callable[[_Pointer[_type.INT32]],  # value
                               _type.HRESULT]
    put_Orientation: _Callable[[_type.INT32],  # value
                               _type.HRESULT]
    get_PointerInfo: _Callable[[_Pointer[_struct.Windows.UI.Input.Preview.Injection.InjectedInputPointerInfo]],  # value
                               _type.HRESULT]
    put_PointerInfo: _Callable[[_struct.Windows.UI.Input.Preview.Injection.InjectedInputPointerInfo],  # value
                               _type.HRESULT]
    get_Pressure: _Callable[[_Pointer[_type.DOUBLE]],  # value
                            _type.HRESULT]
    put_Pressure: _Callable[[_type.DOUBLE],  # value
                            _type.HRESULT]
    get_TouchParameters: _Callable[[_Pointer[_enum.Windows.UI.Input.Preview.Injection.InjectedInputTouchParameters]],  # value
                                   _type.HRESULT]
    put_TouchParameters: _Callable[[_enum.Windows.UI.Input.Preview.Injection.InjectedInputTouchParameters],  # value
                                   _type.HRESULT]


class IInputInjector(_inspectable.IInspectable):
    InjectKeyboardInput: _Callable[[_Windows_Foundation_Collections.IIterable[IInjectedInputKeyboardInfo]],  # input
                                   _type.HRESULT]
    InjectMouseInput: _Callable[[_Windows_Foundation_Collections.IIterable[IInjectedInputMouseInfo]],  # input
                                _type.HRESULT]
    InitializeTouchInjection: _Callable[[_enum.Windows.UI.Input.Preview.Injection.InjectedInputVisualizationMode],  # visualMode
                                        _type.HRESULT]
    InjectTouchInput: _Callable[[_Windows_Foundation_Collections.IIterable[IInjectedInputTouchInfo]],  # input
                                _type.HRESULT]
    UninitializeTouchInjection: _Callable[[],
                                          _type.HRESULT]
    InitializePenInjection: _Callable[[_enum.Windows.UI.Input.Preview.Injection.InjectedInputVisualizationMode],  # visualMode
                                      _type.HRESULT]
    InjectPenInput: _Callable[[IInjectedInputPenInfo],  # input
                              _type.HRESULT]
    UninitializePenInjection: _Callable[[],
                                        _type.HRESULT]
    InjectShortcut: _Callable[[_enum.Windows.UI.Input.Preview.Injection.InjectedInputShortcut],  # shortcut
                              _type.HRESULT]


class IInputInjector2(_inspectable.IInspectable):
    InitializeGamepadInjection: _Callable[[],
                                          _type.HRESULT]
    InjectGamepadInput: _Callable[[IInjectedInputGamepadInfo],  # input
                                  _type.HRESULT]
    UninitializeGamepadInjection: _Callable[[],
                                            _type.HRESULT]


class IInputInjectorStatics(_inspectable.IInspectable):
    TryCreate: _Callable[[_Pointer[IInputInjector]],  # instance
                         _type.HRESULT]

    _factory = True


class IInputInjectorStatics2(_inspectable.IInspectable):
    TryCreateForAppBroadcastOnly: _Callable[[_Pointer[IInputInjector]],  # instance
                                            _type.HRESULT]

    _factory = True
