from __future__ import annotations

from typing import Callable as _Callable

from .. import Core as _Windows_Media_Core
from ... import Foundation as _Windows_Foundation
from ...ApplicationModel import Core as _Windows_ApplicationModel_Core
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IMiracastReceiver(_inspectable.IInspectable):
    GetDefaultSettings: _Callable[[_Pointer[IMiracastReceiverSettings]],  # result
                                  _type.HRESULT]
    GetCurrentSettings: _Callable[[_Pointer[IMiracastReceiverSettings]],  # result
                                  _type.HRESULT]
    GetCurrentSettingsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IMiracastReceiverSettings]]],  # operation
                                       _type.HRESULT]
    DisconnectAllAndApplySettings: _Callable[[IMiracastReceiverSettings,  # settings
                                              _Pointer[IMiracastReceiverApplySettingsResult]],  # result
                                             _type.HRESULT]
    DisconnectAllAndApplySettingsAsync: _Callable[[IMiracastReceiverSettings,  # settings
                                                   _Pointer[_Windows_Foundation.IAsyncOperation[IMiracastReceiverApplySettingsResult]]],  # operation
                                                  _type.HRESULT]
    GetStatus: _Callable[[_Pointer[IMiracastReceiverStatus]],  # result
                         _type.HRESULT]
    GetStatusAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IMiracastReceiverStatus]]],  # operation
                              _type.HRESULT]
    add_StatusChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMiracastReceiver, _inspectable.IInspectable],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_StatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    CreateSession: _Callable[[_Windows_ApplicationModel_Core.ICoreApplicationView,  # view
                              _Pointer[IMiracastReceiverSession]],  # result
                             _type.HRESULT]
    CreateSessionAsync: _Callable[[_Windows_ApplicationModel_Core.ICoreApplicationView,  # view
                                   _Pointer[_Windows_Foundation.IAsyncOperation[IMiracastReceiverSession]]],  # operation
                                  _type.HRESULT]
    ClearKnownTransmitters: _Callable[[],
                                      _type.HRESULT]
    RemoveKnownTransmitter: _Callable[[IMiracastTransmitter],  # transmitter
                                      _type.HRESULT]


class IMiracastReceiverApplySettingsResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Media.Miracast.MiracastReceiverApplySettingsStatus]],  # value
                          _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class IMiracastReceiverConnection(_inspectable.IInspectable):
    Disconnect: _Callable[[_enum.Windows.Media.Miracast.MiracastReceiverDisconnectReason],  # reason
                          _type.HRESULT]
    DisconnectWithMessage: _Callable[[_enum.Windows.Media.Miracast.MiracastReceiverDisconnectReason,  # reason
                                      _type.HSTRING],  # message
                                     _type.HRESULT]
    Pause: _Callable[[],
                     _type.HRESULT]
    PauseAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                          _type.HRESULT]
    Resume: _Callable[[],
                      _type.HRESULT]
    ResumeAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                           _type.HRESULT]
    get_Transmitter: _Callable[[_Pointer[IMiracastTransmitter]],  # value
                               _type.HRESULT]
    get_InputDevices: _Callable[[_Pointer[IMiracastReceiverInputDevices]],  # value
                                _type.HRESULT]
    get_CursorImageChannel: _Callable[[_Pointer[IMiracastReceiverCursorImageChannel]],  # value
                                      _type.HRESULT]
    get_StreamControl: _Callable[[_Pointer[IMiracastReceiverStreamControl]],  # value
                                 _type.HRESULT]


class IMiracastReceiverConnectionCreatedEventArgs(_inspectable.IInspectable):
    get_Connection: _Callable[[_Pointer[IMiracastReceiverConnection]],  # value
                              _type.HRESULT]
    get_Pin: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IMiracastReceiverCursorImageChannel(_inspectable.IInspectable):
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_MaxImageSize: _Callable[[_Pointer[_struct.Windows.Graphics.SizeInt32]],  # value
                                _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Graphics.PointInt32]],  # value
                            _type.HRESULT]
    get_ImageStream: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamWithContentType]],  # value
                               _type.HRESULT]
    add_ImageStreamChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMiracastReceiverCursorImageChannel, _inspectable.IInspectable],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_ImageStreamChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_PositionChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMiracastReceiverCursorImageChannel, _inspectable.IInspectable],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_PositionChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]


class IMiracastReceiverCursorImageChannelSettings(_inspectable.IInspectable):
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsEnabled: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    get_MaxImageSize: _Callable[[_Pointer[_struct.Windows.Graphics.SizeInt32]],  # value
                                _type.HRESULT]
    put_MaxImageSize: _Callable[[_struct.Windows.Graphics.SizeInt32],  # value
                                _type.HRESULT]


class IMiracastReceiverDisconnectedEventArgs(_inspectable.IInspectable):
    get_Connection: _Callable[[_Pointer[IMiracastReceiverConnection]],  # value
                              _type.HRESULT]


class IMiracastReceiverGameControllerDevice(_inspectable.IInspectable):
    get_TransmitInput: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_TransmitInput: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_IsRequestedByTransmitter: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    get_IsTransmittingInput: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    get_Mode: _Callable[[_Pointer[_enum.Windows.Media.Miracast.MiracastReceiverGameControllerDeviceUsageMode]],  # value
                        _type.HRESULT]
    put_Mode: _Callable[[_enum.Windows.Media.Miracast.MiracastReceiverGameControllerDeviceUsageMode],  # value
                        _type.HRESULT]
    add_Changed: _Callable[[_Windows_Foundation.ITypedEventHandler[IMiracastReceiverGameControllerDevice, _inspectable.IInspectable],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Changed: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]


class IMiracastReceiverInputDevices(_inspectable.IInspectable):
    get_Keyboard: _Callable[[_Pointer[IMiracastReceiverKeyboardDevice]],  # value
                            _type.HRESULT]
    get_GameController: _Callable[[_Pointer[IMiracastReceiverGameControllerDevice]],  # value
                                  _type.HRESULT]


class IMiracastReceiverKeyboardDevice(_inspectable.IInspectable):
    get_TransmitInput: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_TransmitInput: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_IsRequestedByTransmitter: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    get_IsTransmittingInput: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    add_Changed: _Callable[[_Windows_Foundation.ITypedEventHandler[IMiracastReceiverKeyboardDevice, _inspectable.IInspectable],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Changed: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]


class IMiracastReceiverMediaSourceCreatedEventArgs(_inspectable.IInspectable):
    get_Connection: _Callable[[_Pointer[IMiracastReceiverConnection]],  # value
                              _type.HRESULT]
    get_MediaSource: _Callable[[_Pointer[_Windows_Media_Core.IMediaSource2]],  # value
                               _type.HRESULT]
    get_CursorImageChannelSettings: _Callable[[_Pointer[IMiracastReceiverCursorImageChannelSettings]],  # value
                                              _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IMiracastReceiverSession(_inspectable.IInspectable):
    add_ConnectionCreated: _Callable[[_Windows_Foundation.ITypedEventHandler[IMiracastReceiverSession, IMiracastReceiverConnectionCreatedEventArgs],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_ConnectionCreated: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    add_MediaSourceCreated: _Callable[[_Windows_Foundation.ITypedEventHandler[IMiracastReceiverSession, IMiracastReceiverMediaSourceCreatedEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_MediaSourceCreated: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_Disconnected: _Callable[[_Windows_Foundation.ITypedEventHandler[IMiracastReceiverSession, IMiracastReceiverDisconnectedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_Disconnected: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    get_AllowConnectionTakeover: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    put_AllowConnectionTakeover: _Callable[[_type.boolean],  # value
                                           _type.HRESULT]
    get_MaxSimultaneousConnections: _Callable[[_Pointer[_type.INT32]],  # value
                                              _type.HRESULT]
    put_MaxSimultaneousConnections: _Callable[[_type.INT32],  # value
                                              _type.HRESULT]
    Start: _Callable[[_Pointer[IMiracastReceiverSessionStartResult]],  # result
                     _type.HRESULT]
    StartAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IMiracastReceiverSessionStartResult]]],  # operation
                          _type.HRESULT]


class IMiracastReceiverSessionStartResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Media.Miracast.MiracastReceiverSessionStartStatus]],  # value
                          _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class IMiracastReceiverSettings(_inspectable.IInspectable):
    get_FriendlyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    put_FriendlyName: _Callable[[_type.HSTRING],  # value
                                _type.HRESULT]
    get_ModelName: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_ModelName: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_ModelNumber: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_ModelNumber: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_AuthorizationMethod: _Callable[[_Pointer[_enum.Windows.Media.Miracast.MiracastReceiverAuthorizationMethod]],  # value
                                       _type.HRESULT]
    put_AuthorizationMethod: _Callable[[_enum.Windows.Media.Miracast.MiracastReceiverAuthorizationMethod],  # value
                                       _type.HRESULT]
    get_RequireAuthorizationFromKnownTransmitters: _Callable[[_Pointer[_type.boolean]],  # value
                                                             _type.HRESULT]
    put_RequireAuthorizationFromKnownTransmitters: _Callable[[_type.boolean],  # value
                                                             _type.HRESULT]


class IMiracastReceiverStatus(_inspectable.IInspectable):
    get_ListeningStatus: _Callable[[_Pointer[_enum.Windows.Media.Miracast.MiracastReceiverListeningStatus]],  # value
                                   _type.HRESULT]
    get_WiFiStatus: _Callable[[_Pointer[_enum.Windows.Media.Miracast.MiracastReceiverWiFiStatus]],  # value
                              _type.HRESULT]
    get_IsConnectionTakeoverSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]
    get_MaxSimultaneousConnections: _Callable[[_Pointer[_type.INT32]],  # value
                                              _type.HRESULT]
    get_KnownTransmitters: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMiracastTransmitter]]],  # value
                                     _type.HRESULT]


class IMiracastReceiverStreamControl(_inspectable.IInspectable):
    GetVideoStreamSettings: _Callable[[_Pointer[IMiracastReceiverVideoStreamSettings]],  # result
                                      _type.HRESULT]
    GetVideoStreamSettingsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IMiracastReceiverVideoStreamSettings]]],  # operation
                                           _type.HRESULT]
    SuggestVideoStreamSettings: _Callable[[IMiracastReceiverVideoStreamSettings],  # settings
                                          _type.HRESULT]
    SuggestVideoStreamSettingsAsync: _Callable[[IMiracastReceiverVideoStreamSettings,  # settings
                                                _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                               _type.HRESULT]
    get_MuteAudio: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_MuteAudio: _Callable[[_type.boolean],  # value
                             _type.HRESULT]


class IMiracastReceiverVideoStreamSettings(_inspectable.IInspectable):
    get_Size: _Callable[[_Pointer[_struct.Windows.Graphics.SizeInt32]],  # value
                        _type.HRESULT]
    put_Size: _Callable[[_struct.Windows.Graphics.SizeInt32],  # value
                        _type.HRESULT]
    get_Bitrate: _Callable[[_Pointer[_type.INT32]],  # value
                           _type.HRESULT]
    put_Bitrate: _Callable[[_type.INT32],  # value
                           _type.HRESULT]


class IMiracastTransmitter(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Name: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_AuthorizationStatus: _Callable[[_Pointer[_enum.Windows.Media.Miracast.MiracastTransmitterAuthorizationStatus]],  # value
                                       _type.HRESULT]
    put_AuthorizationStatus: _Callable[[_enum.Windows.Media.Miracast.MiracastTransmitterAuthorizationStatus],  # value
                                       _type.HRESULT]
    GetConnections: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMiracastReceiverConnection]]],  # result
                              _type.HRESULT]
    get_MacAddress: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_LastConnectionTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                      _type.HRESULT]
