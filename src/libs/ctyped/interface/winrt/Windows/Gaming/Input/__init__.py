from __future__ import annotations

from typing import Callable as _Callable

from . import ForceFeedback as _Windows_Gaming_Input_ForceFeedback
from ... import Foundation as _Windows_Foundation
from ... import System as _Windows_System
from ...Devices import Haptics as _Windows_Devices_Haptics
from ...Devices import Power as _Windows_Devices_Power
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IArcadeStick(_inspectable.IInspectable):
    GetButtonLabel: _Callable[[_enum.Windows.Gaming.Input.ArcadeStickButtons,  # button
                               _Pointer[_enum.Windows.Gaming.Input.GameControllerButtonLabel]],  # value
                              _type.HRESULT]
    GetCurrentReading: _Callable[[_Pointer[_struct.Windows.Gaming.Input.ArcadeStickReading]],  # value
                                 _type.HRESULT]


class IArcadeStickStatics(_inspectable.IInspectable):
    add_ArcadeStickAdded: _Callable[[_Windows_Foundation.IEventHandler[IArcadeStick],  # value
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_ArcadeStickAdded: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    add_ArcadeStickRemoved: _Callable[[_Windows_Foundation.IEventHandler[IArcadeStick],  # value
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_ArcadeStickRemoved: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    get_ArcadeSticks: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IArcadeStick]]],  # value
                                _type.HRESULT]

    _factory = True


class IArcadeStickStatics2(_inspectable.IInspectable):
    FromGameController: _Callable[[IGameController,  # gameController
                                   _Pointer[IArcadeStick]],  # value
                                  _type.HRESULT]

    _factory = True


class IFlightStick(_inspectable.IInspectable):
    get_HatSwitchKind: _Callable[[_Pointer[_enum.Windows.Gaming.Input.GameControllerSwitchKind]],  # value
                                 _type.HRESULT]
    GetButtonLabel: _Callable[[_enum.Windows.Gaming.Input.FlightStickButtons,  # button
                               _Pointer[_enum.Windows.Gaming.Input.GameControllerButtonLabel]],  # value
                              _type.HRESULT]
    GetCurrentReading: _Callable[[_Pointer[_struct.Windows.Gaming.Input.FlightStickReading]],  # value
                                 _type.HRESULT]


class IFlightStickStatics(_inspectable.IInspectable):
    add_FlightStickAdded: _Callable[[_Windows_Foundation.IEventHandler[IFlightStick],  # value
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_FlightStickAdded: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    add_FlightStickRemoved: _Callable[[_Windows_Foundation.IEventHandler[IFlightStick],  # value
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_FlightStickRemoved: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    get_FlightSticks: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IFlightStick]]],  # value
                                _type.HRESULT]
    FromGameController: _Callable[[IGameController,  # gameController
                                   _Pointer[IFlightStick]],  # value
                                  _type.HRESULT]

    _factory = True


class IGameController(_inspectable.IInspectable):
    add_HeadsetConnected: _Callable[[_Windows_Foundation.ITypedEventHandler[IGameController, IHeadset],  # value
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_HeadsetConnected: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    add_HeadsetDisconnected: _Callable[[_Windows_Foundation.ITypedEventHandler[IGameController, IHeadset],  # value
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_HeadsetDisconnected: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_UserChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IGameController, _Windows_System.IUserChangedEventArgs],  # value
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_UserChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    get_Headset: _Callable[[_Pointer[IHeadset]],  # value
                           _type.HRESULT]
    get_IsWireless: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]


class IGameControllerBatteryInfo(_inspectable.IInspectable):
    TryGetBatteryReport: _Callable[[_Pointer[_Windows_Devices_Power.IBatteryReport]],  # value
                                   _type.HRESULT]


class IGamepad(_inspectable.IInspectable):
    get_Vibration: _Callable[[_Pointer[_struct.Windows.Gaming.Input.GamepadVibration]],  # value
                             _type.HRESULT]
    put_Vibration: _Callable[[_struct.Windows.Gaming.Input.GamepadVibration],  # value
                             _type.HRESULT]
    GetCurrentReading: _Callable[[_Pointer[_struct.Windows.Gaming.Input.GamepadReading]],  # value
                                 _type.HRESULT]


class IGamepad2(_inspectable.IInspectable):
    GetButtonLabel: _Callable[[_enum.Windows.Gaming.Input.GamepadButtons,  # button
                               _Pointer[_enum.Windows.Gaming.Input.GameControllerButtonLabel]],  # value
                              _type.HRESULT]


class IGamepadStatics(_inspectable.IInspectable):
    add_GamepadAdded: _Callable[[_Windows_Foundation.IEventHandler[IGamepad],  # value
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_GamepadAdded: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    add_GamepadRemoved: _Callable[[_Windows_Foundation.IEventHandler[IGamepad],  # value
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_GamepadRemoved: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    get_Gamepads: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IGamepad]]],  # value
                            _type.HRESULT]

    _factory = True


class IGamepadStatics2(_inspectable.IInspectable):
    FromGameController: _Callable[[IGameController,  # gameController
                                   _Pointer[IGamepad]],  # value
                                  _type.HRESULT]

    _factory = True


class IHeadset(_inspectable.IInspectable):
    get_CaptureDeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_RenderDeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]


class IRacingWheel(_inspectable.IInspectable):
    get_HasClutch: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_HasHandbrake: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_HasPatternShifter: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    get_MaxPatternShifterGear: _Callable[[_Pointer[_type.INT32]],  # value
                                         _type.HRESULT]
    get_MaxWheelAngle: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                 _type.HRESULT]
    get_WheelMotor: _Callable[[_Pointer[_Windows_Gaming_Input_ForceFeedback.IForceFeedbackMotor]],  # value
                              _type.HRESULT]
    GetButtonLabel: _Callable[[_enum.Windows.Gaming.Input.RacingWheelButtons,  # button
                               _Pointer[_enum.Windows.Gaming.Input.GameControllerButtonLabel]],  # value
                              _type.HRESULT]
    GetCurrentReading: _Callable[[_Pointer[_struct.Windows.Gaming.Input.RacingWheelReading]],  # value
                                 _type.HRESULT]


class IRacingWheelStatics(_inspectable.IInspectable):
    add_RacingWheelAdded: _Callable[[_Windows_Foundation.IEventHandler[IRacingWheel],  # value
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_RacingWheelAdded: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    add_RacingWheelRemoved: _Callable[[_Windows_Foundation.IEventHandler[IRacingWheel],  # value
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_RacingWheelRemoved: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    get_RacingWheels: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IRacingWheel]]],  # value
                                _type.HRESULT]

    _factory = True


class IRacingWheelStatics2(_inspectable.IInspectable):
    FromGameController: _Callable[[IGameController,  # gameController
                                   _Pointer[IRacingWheel]],  # value
                                  _type.HRESULT]

    _factory = True


class IRawGameController(_inspectable.IInspectable):
    get_AxisCount: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]
    get_ButtonCount: _Callable[[_Pointer[_type.INT32]],  # value
                               _type.HRESULT]
    get_ForceFeedbackMotors: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Gaming_Input_ForceFeedback.IForceFeedbackMotor]]],  # value
                                       _type.HRESULT]
    get_HardwareProductId: _Callable[[_Pointer[_type.UINT16]],  # value
                                     _type.HRESULT]
    get_HardwareVendorId: _Callable[[_Pointer[_type.UINT16]],  # value
                                    _type.HRESULT]
    get_SwitchCount: _Callable[[_Pointer[_type.INT32]],  # value
                               _type.HRESULT]
    GetButtonLabel: _Callable[[_type.INT32,  # buttonIndex
                               _Pointer[_enum.Windows.Gaming.Input.GameControllerButtonLabel]],  # value
                              _type.HRESULT]
    GetCurrentReading: _Callable[[_type.UINT32,  # __buttonArraySize
                                  _Pointer[_type.boolean],  # buttonArray
                                  _type.UINT32,  # __switchArraySize
                                  _Pointer[_enum.Windows.Gaming.Input.GameControllerSwitchPosition],  # switchArray
                                  _type.UINT32,  # __axisArraySize
                                  _Pointer[_type.DOUBLE],  # axisArray
                                  _Pointer[_type.UINT64]],  # timestamp
                                 _type.HRESULT]
    GetSwitchKind: _Callable[[_type.INT32,  # switchIndex
                              _Pointer[_enum.Windows.Gaming.Input.GameControllerSwitchKind]],  # value
                             _type.HRESULT]


class IRawGameController2(_inspectable.IInspectable):
    get_SimpleHapticsControllers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Devices_Haptics.ISimpleHapticsController]]],  # value
                                            _type.HRESULT]
    get_NonRoamableId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class IRawGameControllerStatics(_inspectable.IInspectable):
    add_RawGameControllerAdded: _Callable[[_Windows_Foundation.IEventHandler[IRawGameController],  # value
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_RawGameControllerAdded: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]
    add_RawGameControllerRemoved: _Callable[[_Windows_Foundation.IEventHandler[IRawGameController],  # value
                                             _Pointer[_struct.EventRegistrationToken]],  # token
                                            _type.HRESULT]
    remove_RawGameControllerRemoved: _Callable[[_struct.EventRegistrationToken],  # token
                                               _type.HRESULT]
    get_RawGameControllers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IRawGameController]]],  # value
                                      _type.HRESULT]
    FromGameController: _Callable[[IGameController,  # gameController
                                   _Pointer[IRawGameController]],  # value
                                  _type.HRESULT]

    _factory = True


class IUINavigationController(_inspectable.IInspectable):
    GetCurrentReading: _Callable[[_Pointer[_struct.Windows.Gaming.Input.UINavigationReading]],  # value
                                 _type.HRESULT]
    GetOptionalButtonLabel: _Callable[[_enum.Windows.Gaming.Input.OptionalUINavigationButtons,  # button
                                       _Pointer[_enum.Windows.Gaming.Input.GameControllerButtonLabel]],  # value
                                      _type.HRESULT]
    GetRequiredButtonLabel: _Callable[[_enum.Windows.Gaming.Input.RequiredUINavigationButtons,  # button
                                       _Pointer[_enum.Windows.Gaming.Input.GameControllerButtonLabel]],  # value
                                      _type.HRESULT]


class IUINavigationControllerStatics(_inspectable.IInspectable):
    add_UINavigationControllerAdded: _Callable[[_Windows_Foundation.IEventHandler[IUINavigationController],  # value
                                                _Pointer[_struct.EventRegistrationToken]],  # token
                                               _type.HRESULT]
    remove_UINavigationControllerAdded: _Callable[[_struct.EventRegistrationToken],  # token
                                                  _type.HRESULT]
    add_UINavigationControllerRemoved: _Callable[[_Windows_Foundation.IEventHandler[IUINavigationController],  # value
                                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                                 _type.HRESULT]
    remove_UINavigationControllerRemoved: _Callable[[_struct.EventRegistrationToken],  # token
                                                    _type.HRESULT]
    get_UINavigationControllers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IUINavigationController]]],  # value
                                           _type.HRESULT]

    _factory = True


class IUINavigationControllerStatics2(_inspectable.IInspectable):
    FromGameController: _Callable[[IGameController,  # gameController
                                   _Pointer[IUINavigationController]],  # value
                                  _type.HRESULT]

    _factory = True
