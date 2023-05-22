from __future__ import annotations

from typing import Callable as _Callable

from .. import Enumeration as _Windows_Devices_Enumeration
from ... import Foundation as _Windows_Foundation
from ... import Networking as _Windows_Networking
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Security import Credentials as _Windows_Security_Credentials
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IWiFiDirectAdvertisement(_inspectable.IInspectable):
    get_InformationElements: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IWiFiDirectInformationElement]]],  # value
                                       _type.HRESULT]
    put_InformationElements: _Callable[[_Windows_Foundation_Collections.IVector[IWiFiDirectInformationElement]],  # value
                                       _type.HRESULT]
    get_ListenStateDiscoverability: _Callable[[_Pointer[_enum.Windows.Devices.WiFiDirect.WiFiDirectAdvertisementListenStateDiscoverability]],  # value
                                              _type.HRESULT]
    put_ListenStateDiscoverability: _Callable[[_enum.Windows.Devices.WiFiDirect.WiFiDirectAdvertisementListenStateDiscoverability],  # value
                                              _type.HRESULT]
    get_IsAutonomousGroupOwnerEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]
    put_IsAutonomousGroupOwnerEnabled: _Callable[[_type.boolean],  # value
                                                 _type.HRESULT]
    get_LegacySettings: _Callable[[_Pointer[IWiFiDirectLegacySettings]],  # value
                                  _type.HRESULT]


class IWiFiDirectAdvertisement2(_inspectable.IInspectable):
    get_SupportedConfigurationMethods: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_enum.Windows.Devices.WiFiDirect.WiFiDirectConfigurationMethod]]],  # value
                                                 _type.HRESULT]


class IWiFiDirectAdvertisementPublisher(_inspectable.IInspectable):
    get_Advertisement: _Callable[[_Pointer[IWiFiDirectAdvertisement]],  # value
                                 _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.Devices.WiFiDirect.WiFiDirectAdvertisementPublisherStatus]],  # value
                          _type.HRESULT]
    add_StatusChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IWiFiDirectAdvertisementPublisher, IWiFiDirectAdvertisementPublisherStatusChangedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_StatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]


class IWiFiDirectAdvertisementPublisherStatusChangedEventArgs(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Devices.WiFiDirect.WiFiDirectAdvertisementPublisherStatus]],  # value
                          _type.HRESULT]
    get_Error: _Callable[[_Pointer[_enum.Windows.Devices.WiFiDirect.WiFiDirectError]],  # value
                         _type.HRESULT]


class IWiFiDirectConnectionListener(_inspectable.IInspectable):
    add_ConnectionRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IWiFiDirectConnectionListener, IWiFiDirectConnectionRequestedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_ConnectionRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]


class IWiFiDirectConnectionParameters(_inspectable.IInspectable):
    get_GroupOwnerIntent: _Callable[[_Pointer[_type.INT16]],  # value
                                    _type.HRESULT]
    put_GroupOwnerIntent: _Callable[[_type.INT16],  # value
                                    _type.HRESULT]


class IWiFiDirectConnectionParameters2(_inspectable.IInspectable):
    get_PreferenceOrderedConfigurationMethods: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_enum.Windows.Devices.WiFiDirect.WiFiDirectConfigurationMethod]]],  # value
                                                         _type.HRESULT]
    get_PreferredPairingProcedure: _Callable[[_Pointer[_enum.Windows.Devices.WiFiDirect.WiFiDirectPairingProcedure]],  # value
                                             _type.HRESULT]
    put_PreferredPairingProcedure: _Callable[[_enum.Windows.Devices.WiFiDirect.WiFiDirectPairingProcedure],  # value
                                             _type.HRESULT]


class IWiFiDirectConnectionParametersStatics(_inspectable.IInspectable, factory=True):
    GetDevicePairingKinds: _Callable[[_enum.Windows.Devices.WiFiDirect.WiFiDirectConfigurationMethod,  # configurationMethod
                                      _Pointer[_enum.Windows.Devices.Enumeration.DevicePairingKinds]],  # result
                                     _type.HRESULT]


class IWiFiDirectConnectionRequest(_inspectable.IInspectable):
    get_DeviceInformation: _Callable[[_Pointer[_Windows_Devices_Enumeration.IDeviceInformation]],  # value
                                     _type.HRESULT]


class IWiFiDirectConnectionRequestedEventArgs(_inspectable.IInspectable):
    GetConnectionRequest: _Callable[[_Pointer[IWiFiDirectConnectionRequest]],  # result
                                    _type.HRESULT]


class IWiFiDirectDevice(_inspectable.IInspectable):
    get_ConnectionStatus: _Callable[[_Pointer[_enum.Windows.Devices.WiFiDirect.WiFiDirectConnectionStatus]],  # value
                                    _type.HRESULT]
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    add_ConnectionStatusChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IWiFiDirectDevice, _inspectable.IInspectable],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_ConnectionStatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]
    GetConnectionEndpointPairs: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Networking.IEndpointPair]]],  # value
                                          _type.HRESULT]


class IWiFiDirectDeviceStatics(_inspectable.IInspectable, factory=True):
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # deviceSelector
                                 _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IWiFiDirectDevice]]],  # asyncOp
                           _type.HRESULT]


class IWiFiDirectDeviceStatics2(_inspectable.IInspectable, factory=True):
    GetDeviceSelector: _Callable[[_enum.Windows.Devices.WiFiDirect.WiFiDirectDeviceSelectorType,  # type
                                  _Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            IWiFiDirectConnectionParameters,  # connectionParameters
                            _Pointer[_Windows_Foundation.IAsyncOperation[IWiFiDirectDevice]]],  # result
                           _type.HRESULT]


class IWiFiDirectInformationElement(_inspectable.IInspectable):
    get_Oui: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                       _type.HRESULT]
    put_Oui: _Callable[[_Windows_Storage_Streams.IBuffer],  # value
                       _type.HRESULT]
    get_OuiType: _Callable[[_Pointer[_type.BYTE]],  # value
                           _type.HRESULT]
    put_OuiType: _Callable[[_type.BYTE],  # value
                           _type.HRESULT]
    get_Value: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                         _type.HRESULT]
    put_Value: _Callable[[_Windows_Storage_Streams.IBuffer],  # value
                         _type.HRESULT]


class IWiFiDirectInformationElementStatics(_inspectable.IInspectable, factory=True):
    CreateFromBuffer: _Callable[[_Windows_Storage_Streams.IBuffer,  # buffer
                                 _Pointer[_Windows_Foundation_Collections.IVector[IWiFiDirectInformationElement]]],  # result
                                _type.HRESULT]
    CreateFromDeviceInformation: _Callable[[_Windows_Devices_Enumeration.IDeviceInformation,  # deviceInformation
                                            _Pointer[_Windows_Foundation_Collections.IVector[IWiFiDirectInformationElement]]],  # result
                                           _type.HRESULT]


class IWiFiDirectLegacySettings(_inspectable.IInspectable):
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsEnabled: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    get_Ssid: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Ssid: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_Passphrase: _Callable[[_Pointer[_Windows_Security_Credentials.IPasswordCredential]],  # value
                              _type.HRESULT]
    put_Passphrase: _Callable[[_Windows_Security_Credentials.IPasswordCredential],  # value
                              _type.HRESULT]
