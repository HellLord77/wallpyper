from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Input as _Windows_Gaming_Input
from .... import Foundation as _Windows_Foundation
from ....Storage import Streams as _Windows_Storage_Streams
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class ICustomGameControllerFactory(_inspectable.IInspectable):
    CreateGameController: _Callable[[IGameControllerProvider,  # provider
                                     _Pointer[_inspectable.IInspectable]],  # value
                                    _type.HRESULT]
    OnGameControllerAdded: _Callable[[_Windows_Gaming_Input.IGameController],  # value
                                     _type.HRESULT]
    OnGameControllerRemoved: _Callable[[_Windows_Gaming_Input.IGameController],  # value
                                       _type.HRESULT]


class IGameControllerFactoryManagerStatics(_inspectable.IInspectable, factory=True):
    RegisterCustomFactoryForGipInterface: _Callable[[ICustomGameControllerFactory,  # factory
                                                     _struct.GUID],  # interfaceId
                                                    _type.HRESULT]
    RegisterCustomFactoryForHardwareId: _Callable[[ICustomGameControllerFactory,  # factory
                                                   _type.UINT16,  # hardwareVendorId
                                                   _type.UINT16],  # hardwareProductId
                                                  _type.HRESULT]
    RegisterCustomFactoryForXusbType: _Callable[[ICustomGameControllerFactory,  # factory
                                                 _enum.Windows.Gaming.Input.Custom.XusbDeviceType,  # xusbType
                                                 _enum.Windows.Gaming.Input.Custom.XusbDeviceSubtype],  # xusbSubtype
                                                _type.HRESULT]


class IGameControllerFactoryManagerStatics2(_inspectable.IInspectable, factory=True):
    TryGetFactoryControllerFromGameController: _Callable[[ICustomGameControllerFactory,  # factory
                                                          _Windows_Gaming_Input.IGameController,  # gameController
                                                          _Pointer[_Windows_Gaming_Input.IGameController]],  # factoryController
                                                         _type.HRESULT]


class IGameControllerInputSink(_inspectable.IInspectable):
    OnInputResumed: _Callable[[_type.UINT64],  # timestamp
                              _type.HRESULT]
    OnInputSuspended: _Callable[[_type.UINT64],  # timestamp
                                _type.HRESULT]


class IGameControllerProvider(_inspectable.IInspectable):
    get_FirmwareVersionInfo: _Callable[[_Pointer[_struct.Windows.Gaming.Input.Custom.GameControllerVersionInfo]],  # value
                                       _type.HRESULT]
    get_HardwareProductId: _Callable[[_Pointer[_type.UINT16]],  # value
                                     _type.HRESULT]
    get_HardwareVendorId: _Callable[[_Pointer[_type.UINT16]],  # value
                                    _type.HRESULT]
    get_HardwareVersionInfo: _Callable[[_Pointer[_struct.Windows.Gaming.Input.Custom.GameControllerVersionInfo]],  # value
                                       _type.HRESULT]
    get_IsConnected: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]


class IGipFirmwareUpdateResult(_inspectable.IInspectable):
    get_ExtendedErrorCode: _Callable[[_Pointer[_type.UINT32]],  # value
                                     _type.HRESULT]
    get_FinalComponentId: _Callable[[_Pointer[_type.UINT32]],  # value
                                    _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.Gaming.Input.Custom.GipFirmwareUpdateStatus]],  # value
                          _type.HRESULT]


class IGipGameControllerInputSink(_inspectable.IInspectable):
    OnKeyReceived: _Callable[[_type.UINT64,  # timestamp
                              _type.BYTE,  # keyCode
                              _type.boolean],  # isPressed
                             _type.HRESULT]
    OnMessageReceived: _Callable[[_type.UINT64,  # timestamp
                                  _enum.Windows.Gaming.Input.Custom.GipMessageClass,  # messageClass
                                  _type.BYTE,  # messageId
                                  _type.BYTE,  # sequenceId
                                  _type.UINT32,  # __messageBufferSize
                                  _Pointer[_type.BYTE]],  # messageBuffer
                                 _type.HRESULT]


class IGipGameControllerProvider(_inspectable.IInspectable):
    SendMessage: _Callable[[_enum.Windows.Gaming.Input.Custom.GipMessageClass,  # messageClass
                            _type.BYTE,  # messageId
                            _type.UINT32,  # __messageBufferSize
                            _Pointer[_type.BYTE]],  # messageBuffer
                           _type.HRESULT]
    SendReceiveMessage: _Callable[[_enum.Windows.Gaming.Input.Custom.GipMessageClass,  # messageClass
                                   _type.BYTE,  # messageId
                                   _type.UINT32,  # __requestMessageBufferSize
                                   _Pointer[_type.BYTE],  # requestMessageBuffer
                                   _type.UINT32,  # __responseMessageBufferSize
                                   _Pointer[_type.BYTE]],  # responseMessageBuffer
                                  _type.HRESULT]
    UpdateFirmwareAsync: _Callable[[_Windows_Storage_Streams.IInputStream,  # firmwareImage
                                    _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IGipFirmwareUpdateResult, _struct.Windows.Gaming.Input.Custom.GipFirmwareUpdateProgress]]],  # result
                                   _type.HRESULT]


class IHidGameControllerInputSink(_inspectable.IInspectable):
    OnInputReportReceived: _Callable[[_type.UINT64,  # timestamp
                                      _type.BYTE,  # reportId
                                      _type.UINT32,  # __reportBufferSize
                                      _Pointer[_type.BYTE]],  # reportBuffer
                                     _type.HRESULT]


class IHidGameControllerProvider(_inspectable.IInspectable):
    get_UsageId: _Callable[[_Pointer[_type.UINT16]],  # value
                           _type.HRESULT]
    get_UsagePage: _Callable[[_Pointer[_type.UINT16]],  # value
                             _type.HRESULT]
    GetFeatureReport: _Callable[[_type.BYTE,  # reportId
                                 _type.UINT32,  # __reportBufferSize
                                 _Pointer[_type.BYTE]],  # reportBuffer
                                _type.HRESULT]
    SendFeatureReport: _Callable[[_type.BYTE,  # reportId
                                  _type.UINT32,  # __reportBufferSize
                                  _Pointer[_type.BYTE]],  # reportBuffer
                                 _type.HRESULT]
    SendOutputReport: _Callable[[_type.BYTE,  # reportId
                                 _type.UINT32,  # __reportBufferSize
                                 _Pointer[_type.BYTE]],  # reportBuffer
                                _type.HRESULT]


class IXusbGameControllerInputSink(_inspectable.IInspectable):
    OnInputReceived: _Callable[[_type.UINT64,  # timestamp
                                _type.BYTE,  # reportId
                                _type.UINT32,  # __inputBufferSize
                                _Pointer[_type.BYTE]],  # inputBuffer
                               _type.HRESULT]


class IXusbGameControllerProvider(_inspectable.IInspectable):
    SetVibration: _Callable[[_type.DOUBLE,  # lowFrequencyMotorSpeed
                             _type.DOUBLE],  # highFrequencyMotorSpeed
                            _type.HRESULT]
