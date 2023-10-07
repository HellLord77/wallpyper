from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Networking import Connectivity as _Windows_Networking_Connectivity
from ...Security import Credentials as _Windows_Security_Credentials
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IWiFiAdapter(_inspectable.IInspectable):
    get_NetworkAdapter: _Callable[[_Pointer[_Windows_Networking_Connectivity.INetworkAdapter]],  # value
                                  _type.HRESULT]
    ScanAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # value
                         _type.HRESULT]
    get_NetworkReport: _Callable[[_Pointer[IWiFiNetworkReport]],  # value
                                 _type.HRESULT]
    add_AvailableNetworksChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IWiFiAdapter, _inspectable.IInspectable],  # args
                                             _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                                            _type.HRESULT]
    remove_AvailableNetworksChanged: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                               _type.HRESULT]
    ConnectAsync: _Callable[[IWiFiAvailableNetwork,  # availableNetwork
                             _enum.Windows.Devices.WiFi.WiFiReconnectionKind,  # reconnectionKind
                             _Pointer[_Windows_Foundation.IAsyncOperation[IWiFiConnectionResult]]],  # value
                            _type.HRESULT]
    ConnectWithPasswordCredentialAsync: _Callable[[IWiFiAvailableNetwork,  # availableNetwork
                                                   _enum.Windows.Devices.WiFi.WiFiReconnectionKind,  # reconnectionKind
                                                   _Windows_Security_Credentials.IPasswordCredential,  # passwordCredential
                                                   _Pointer[_Windows_Foundation.IAsyncOperation[IWiFiConnectionResult]]],  # value
                                                  _type.HRESULT]
    ConnectWithPasswordCredentialAndSsidAsync: _Callable[[IWiFiAvailableNetwork,  # availableNetwork
                                                          _enum.Windows.Devices.WiFi.WiFiReconnectionKind,  # reconnectionKind
                                                          _Windows_Security_Credentials.IPasswordCredential,  # passwordCredential
                                                          _type.HSTRING,  # ssid
                                                          _Pointer[_Windows_Foundation.IAsyncOperation[IWiFiConnectionResult]]],  # value
                                                         _type.HRESULT]
    Disconnect: _Callable[[],
                          _type.HRESULT]


class IWiFiAdapter2(_inspectable.IInspectable):
    GetWpsConfigurationAsync: _Callable[[IWiFiAvailableNetwork,  # availableNetwork
                                         _Pointer[_Windows_Foundation.IAsyncOperation[IWiFiWpsConfigurationResult]]],  # operation
                                        _type.HRESULT]
    ConnectWithPasswordCredentialAndSsidAndConnectionMethodAsync: _Callable[[IWiFiAvailableNetwork,  # availableNetwork
                                                                             _enum.Windows.Devices.WiFi.WiFiReconnectionKind,  # reconnectionKind
                                                                             _Windows_Security_Credentials.IPasswordCredential,  # passwordCredential
                                                                             _type.HSTRING,  # ssid
                                                                             _enum.Windows.Devices.WiFi.WiFiConnectionMethod,  # connectionMethod
                                                                             _Pointer[_Windows_Foundation.IAsyncOperation[IWiFiConnectionResult]]],  # operation
                                                                            _type.HRESULT]


class IWiFiAdapterStatics(_inspectable.IInspectable, factory=True):
    FindAllAdaptersAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IWiFiAdapter]]]],  # value
                                    _type.HRESULT]
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # deviceSelector
                                 _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IWiFiAdapter]]],  # asyncOp
                           _type.HRESULT]
    RequestAccessAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Devices.WiFi.WiFiAccessStatus]]],  # value
                                  _type.HRESULT]


class IWiFiAvailableNetwork(_inspectable.IInspectable):
    get_Uptime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                          _type.HRESULT]
    get_Ssid: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Bssid: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_ChannelCenterFrequencyInKilohertz: _Callable[[_Pointer[_type.INT32]],  # value
                                                     _type.HRESULT]
    get_NetworkRssiInDecibelMilliwatts: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                  _type.HRESULT]
    get_SignalBars: _Callable[[_Pointer[_type.BYTE]],  # value
                              _type.HRESULT]
    get_NetworkKind: _Callable[[_Pointer[_enum.Windows.Devices.WiFi.WiFiNetworkKind]],  # value
                               _type.HRESULT]
    get_PhyKind: _Callable[[_Pointer[_enum.Windows.Devices.WiFi.WiFiPhyKind]],  # value
                           _type.HRESULT]
    get_SecuritySettings: _Callable[[_Pointer[_Windows_Networking_Connectivity.INetworkSecuritySettings]],  # value
                                    _type.HRESULT]
    get_BeaconInterval: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                  _type.HRESULT]
    get_IsWiFiDirect: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]


class IWiFiConnectionResult(_inspectable.IInspectable):
    get_ConnectionStatus: _Callable[[_Pointer[_enum.Windows.Devices.WiFi.WiFiConnectionStatus]],  # value
                                    _type.HRESULT]


class IWiFiNetworkReport(_inspectable.IInspectable):
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_AvailableNetworks: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IWiFiAvailableNetwork]]],  # value
                                     _type.HRESULT]


class IWiFiOnDemandHotspotConnectTriggerDetails(_inspectable.IInspectable):
    get_RequestedNetwork: _Callable[[_Pointer[IWiFiOnDemandHotspotNetwork]],  # value
                                    _type.HRESULT]
    ReportError: _Callable[[_enum.Windows.Devices.WiFi.WiFiOnDemandHotspotConnectStatus],  # status
                           _type.HRESULT]
    ConnectAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IWiFiOnDemandHotspotConnectionResult]]],  # operation
                            _type.HRESULT]
    Connect: _Callable[[_Pointer[IWiFiOnDemandHotspotConnectionResult]],  # result
                       _type.HRESULT]


class IWiFiOnDemandHotspotConnectionResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Devices.WiFi.WiFiOnDemandHotspotConnectStatus]],  # value
                          _type.HRESULT]


class IWiFiOnDemandHotspotNetwork(_inspectable.IInspectable):
    GetProperties: _Callable[[_Pointer[IWiFiOnDemandHotspotNetworkProperties]],  # result
                             _type.HRESULT]
    UpdateProperties: _Callable[[IWiFiOnDemandHotspotNetworkProperties],  # newProperties
                                _type.HRESULT]
    get_Id: _Callable[[_Pointer[_struct.GUID]],  # value
                      _type.HRESULT]


class IWiFiOnDemandHotspotNetworkProperties(_inspectable.IInspectable):
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_DisplayName: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_Availability: _Callable[[_Pointer[_enum.Windows.Devices.WiFi.WiFiOnDemandHotspotAvailability]],  # value
                                _type.HRESULT]
    put_Availability: _Callable[[_enum.Windows.Devices.WiFi.WiFiOnDemandHotspotAvailability],  # value
                                _type.HRESULT]
    get_RemainingBatteryPercent: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                                           _type.HRESULT]
    put_RemainingBatteryPercent: _Callable[[_Windows_Foundation.IReference[_type.UINT32]],  # value
                                           _type.HRESULT]
    get_CellularBars: _Callable[[_Pointer[_Windows_Foundation.IReference[_enum.Windows.Devices.WiFi.WiFiOnDemandHotspotCellularBars]]],  # value
                                _type.HRESULT]
    put_CellularBars: _Callable[[_Windows_Foundation.IReference[_enum.Windows.Devices.WiFi.WiFiOnDemandHotspotCellularBars]],  # value
                                _type.HRESULT]
    get_IsMetered: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsMetered: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    get_Ssid: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Ssid: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_Password: _Callable[[_Pointer[_Windows_Security_Credentials.IPasswordCredential]],  # value
                            _type.HRESULT]
    put_Password: _Callable[[_Windows_Security_Credentials.IPasswordCredential],  # value
                            _type.HRESULT]


class IWiFiOnDemandHotspotNetworkStatics(_inspectable.IInspectable, factory=True):
    GetOrCreateById: _Callable[[_struct.GUID,  # networkId
                                _Pointer[IWiFiOnDemandHotspotNetwork]],  # result
                               _type.HRESULT]


class IWiFiWpsConfigurationResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Devices.WiFi.WiFiWpsConfigurationStatus]],  # value
                          _type.HRESULT]
    get_SupportedWpsKinds: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Devices.WiFi.WiFiWpsKind]]],  # value
                                     _type.HRESULT]
