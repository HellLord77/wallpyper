from __future__ import annotations as _

from typing import Callable as _Callable

from ..... import Foundation as _Windows_Foundation
from .....Foundation import Collections as _Windows_Foundation_Collections
from .....Storage import Streams as _Windows_Storage_Streams
from ...... import inspectable as _inspectable
from ........ import enum as _enum
from ........ import struct as _struct
from ........ import type as _type
from ........_utils import _Pointer


class ISecondaryAuthenticationFactorAuthentication(_inspectable.IInspectable):
    ServiceAuthenticationHmac: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                         _type.HRESULT]
    SessionNonce: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                            _type.HRESULT]
    DeviceNonce: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                           _type.HRESULT]
    DeviceConfigurationData: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                       _type.HRESULT]
    FinishAuthenticationAsync: _Callable[[_Windows_Storage_Streams.IBuffer,  # deviceHmac
                                          _Windows_Storage_Streams.IBuffer,  # sessionHmac
                                          _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorFinishAuthenticationStatus]]],  # result
                                         _type.HRESULT]
    AbortAuthenticationAsync: _Callable[[_type.HSTRING,  # errorLogMessage
                                         _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                        _type.HRESULT]


class ISecondaryAuthenticationFactorAuthenticationResult(_inspectable.IInspectable):
    Status: _Callable[[_Pointer[_enum.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationStatus]],  # value
                      _type.HRESULT]
    Authentication: _Callable[[_Pointer[ISecondaryAuthenticationFactorAuthentication]],  # value
                              _type.HRESULT]


class ISecondaryAuthenticationFactorAuthenticationStageChangedEventArgs(_inspectable.IInspectable):
    StageInfo: _Callable[[_Pointer[ISecondaryAuthenticationFactorAuthenticationStageInfo]],  # value
                         _type.HRESULT]


class ISecondaryAuthenticationFactorAuthenticationStageInfo(_inspectable.IInspectable):
    Stage: _Callable[[_Pointer[_enum.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationStage]],  # value
                     _type.HRESULT]
    Scenario: _Callable[[_Pointer[_enum.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationScenario]],  # value
                        _type.HRESULT]
    DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class ISecondaryAuthenticationFactorAuthenticationStatics(_inspectable.IInspectable, factory=True):
    ShowNotificationMessageAsync: _Callable[[_type.HSTRING,  # deviceName
                                             _enum.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorAuthenticationMessage,  # message
                                             _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                            _type.HRESULT]
    StartAuthenticationAsync: _Callable[[_type.HSTRING,  # deviceId
                                         _Windows_Storage_Streams.IBuffer,  # serviceAuthenticationNonce
                                         _Pointer[_Windows_Foundation.IAsyncOperation[ISecondaryAuthenticationFactorAuthenticationResult]]],  # operation
                                        _type.HRESULT]
    AuthenticationStageChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    GetAuthenticationStageInfoAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[ISecondaryAuthenticationFactorAuthenticationStageInfo]]],  # result
                                               _type.HRESULT]


class ISecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatics(_inspectable.IInspectable, factory=True):
    RegisterDevicePresenceMonitoringAsync: _Callable[[_type.HSTRING,  # deviceId
                                                      _type.HSTRING,  # deviceInstancePath
                                                      _enum.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDevicePresenceMonitoringMode,  # monitoringMode
                                                      _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatus]]],  # operation
                                                     _type.HRESULT]
    RegisterDevicePresenceMonitoringWithNewDeviceAsync: _Callable[[_type.HSTRING,  # deviceId
                                                                   _type.HSTRING,  # deviceInstancePath
                                                                   _enum.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDevicePresenceMonitoringMode,  # monitoringMode
                                                                   _type.HSTRING,  # deviceFriendlyName
                                                                   _type.HSTRING,  # deviceModelNumber
                                                                   _Windows_Storage_Streams.IBuffer,  # deviceConfigurationData
                                                                   _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDevicePresenceMonitoringRegistrationStatus]]],  # operation
                                                                  _type.HRESULT]
    UnregisterDevicePresenceMonitoringAsync: _Callable[[_type.HSTRING,  # deviceId
                                                        _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                                       _type.HRESULT]
    IsDevicePresenceMonitoringSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                   _type.HRESULT]


class ISecondaryAuthenticationFactorInfo(_inspectable.IInspectable):
    DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # deviceId
                        _type.HRESULT]
    DeviceFriendlyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    DeviceModelNumber: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    DeviceConfigurationData: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                       _type.HRESULT]


class ISecondaryAuthenticationFactorInfo2(_inspectable.IInspectable):
    PresenceMonitoringMode: _Callable[[_Pointer[_enum.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDevicePresenceMonitoringMode]],  # value
                                      _type.HRESULT]
    UpdateDevicePresenceAsync: _Callable[[_enum.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDevicePresence,  # presenceState
                                          _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                         _type.HRESULT]
    IsAuthenticationSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]


class ISecondaryAuthenticationFactorRegistration(_inspectable.IInspectable):
    FinishRegisteringDeviceAsync: _Callable[[_Windows_Storage_Streams.IBuffer,  # deviceConfigurationData
                                             _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                            _type.HRESULT]
    AbortRegisteringDeviceAsync: _Callable[[_type.HSTRING,  # errorLogMessage
                                            _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                           _type.HRESULT]


class ISecondaryAuthenticationFactorRegistrationResult(_inspectable.IInspectable):
    Status: _Callable[[_Pointer[_enum.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorRegistrationStatus]],  # value
                      _type.HRESULT]
    Registration: _Callable[[_Pointer[ISecondaryAuthenticationFactorRegistration]],  # value
                            _type.HRESULT]


class ISecondaryAuthenticationFactorRegistrationStatics(_inspectable.IInspectable, factory=True):
    RequestStartRegisteringDeviceAsync: _Callable[[_type.HSTRING,  # deviceId
                                                   _enum.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDeviceCapabilities,  # capabilities
                                                   _type.HSTRING,  # deviceFriendlyName
                                                   _type.HSTRING,  # deviceModelNumber
                                                   _Windows_Storage_Streams.IBuffer,  # deviceKey
                                                   _Windows_Storage_Streams.IBuffer,  # mutualAuthenticationKey
                                                   _Pointer[_Windows_Foundation.IAsyncOperation[ISecondaryAuthenticationFactorRegistrationResult]]],  # operation
                                                  _type.HRESULT]
    FindAllRegisteredDeviceInfoAsync: _Callable[[_enum.Windows.Security.Authentication.Identity.Provider.SecondaryAuthenticationFactorDeviceFindScope,  # queryType
                                                 _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[ISecondaryAuthenticationFactorInfo]]]],  # deviceInfoList
                                                _type.HRESULT]
    UnregisterDeviceAsync: _Callable[[_type.HSTRING,  # deviceId
                                      _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                     _type.HRESULT]
    UpdateDeviceConfigurationDataAsync: _Callable[[_type.HSTRING,  # deviceId
                                                   _Windows_Storage_Streams.IBuffer,  # deviceConfigurationData
                                                   _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                                  _type.HRESULT]
