from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import Networking as _Windows_Networking
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from .....um import Unknwnbase as _Unknwnbase
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class _INetworkStatusChangedEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable],  # sender
                      _type.HRESULT]


class INetworkStatusChangedEventHandler(_INetworkStatusChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class INetworkStatusChangedEventHandler_impl(_INetworkStatusChangedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class IAttributedNetworkUsage(_inspectable.IInspectable):
    get_BytesSent: _Callable[[_Pointer[_type.UINT64]],  # value
                             _type.HRESULT]
    get_BytesReceived: _Callable[[_Pointer[_type.UINT64]],  # value
                                 _type.HRESULT]
    get_AttributionId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_AttributionName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_AttributionThumbnail: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # value
                                        _type.HRESULT]


class ICellularApnContext(_inspectable.IInspectable):
    get_ProviderId: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_ProviderId: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]
    get_AccessPointName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    put_AccessPointName: _Callable[[_type.HSTRING],  # value
                                   _type.HRESULT]
    get_UserName: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_UserName: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_Password: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_Password: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_IsCompressionEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    put_IsCompressionEnabled: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]
    get_AuthenticationType: _Callable[[_Pointer[_enum.Windows.Networking.Connectivity.CellularApnAuthenticationType]],  # value
                                      _type.HRESULT]
    put_AuthenticationType: _Callable[[_enum.Windows.Networking.Connectivity.CellularApnAuthenticationType],  # value
                                      _type.HRESULT]


class ICellularApnContext2(_inspectable.IInspectable):
    get_ProfileName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_ProfileName: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]


class IConnectionCost(_inspectable.IInspectable):
    get_NetworkCostType: _Callable[[_Pointer[_enum.Windows.Networking.Connectivity.NetworkCostType]],  # value
                                   _type.HRESULT]
    get_Roaming: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_OverDataLimit: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_ApproachingDataLimit: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]


class IConnectionCost2(_inspectable.IInspectable):
    get_BackgroundDataUsageRestricted: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]


class IConnectionProfile(_inspectable.IInspectable):
    get_ProfileName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    GetNetworkConnectivityLevel: _Callable[[_Pointer[_enum.Windows.Networking.Connectivity.NetworkConnectivityLevel]],  # value
                                           _type.HRESULT]
    GetNetworkNames: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                               _type.HRESULT]
    GetConnectionCost: _Callable[[_Pointer[IConnectionCost]],  # value
                                 _type.HRESULT]
    GetDataPlanStatus: _Callable[[_Pointer[IDataPlanStatus]],  # value
                                 _type.HRESULT]
    get_NetworkAdapter: _Callable[[_Pointer[INetworkAdapter]],  # value
                                  _type.HRESULT]
    GetLocalUsage: _Callable[[_struct.Windows.Foundation.DateTime,  # StartTime
                              _struct.Windows.Foundation.DateTime,  # EndTime
                              _Pointer[IDataUsage]],  # value
                             _type.HRESULT]
    GetLocalUsagePerRoamingStates: _Callable[[_struct.Windows.Foundation.DateTime,  # StartTime
                                              _struct.Windows.Foundation.DateTime,  # EndTime
                                              _enum.Windows.Networking.Connectivity.RoamingStates,  # States
                                              _Pointer[IDataUsage]],  # value
                                             _type.HRESULT]
    get_NetworkSecuritySettings: _Callable[[_Pointer[INetworkSecuritySettings]],  # value
                                           _type.HRESULT]


class IConnectionProfile2(_inspectable.IInspectable):
    get_IsWwanConnectionProfile: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    get_IsWlanConnectionProfile: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    get_WwanConnectionProfileDetails: _Callable[[_Pointer[IWwanConnectionProfileDetails]],  # value
                                                _type.HRESULT]
    get_WlanConnectionProfileDetails: _Callable[[_Pointer[IWlanConnectionProfileDetails]],  # value
                                                _type.HRESULT]
    get_ServiceProviderGuid: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.GUID]]],  # value
                                       _type.HRESULT]
    GetSignalBars: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.BYTE]]],  # value
                             _type.HRESULT]
    GetDomainConnectivityLevel: _Callable[[_Pointer[_enum.Windows.Networking.Connectivity.DomainConnectivityLevel]],  # value
                                          _type.HRESULT]
    GetNetworkUsageAsync: _Callable[[_struct.Windows.Foundation.DateTime,  # startTime
                                     _struct.Windows.Foundation.DateTime,  # endTime
                                     _enum.Windows.Networking.Connectivity.DataUsageGranularity,  # granularity
                                     _struct.Windows.Networking.Connectivity.NetworkUsageStates,  # states
                                     _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[INetworkUsage]]]],  # value
                                    _type.HRESULT]
    GetConnectivityIntervalsAsync: _Callable[[_struct.Windows.Foundation.DateTime,  # startTime
                                              _struct.Windows.Foundation.DateTime,  # endTime
                                              _struct.Windows.Networking.Connectivity.NetworkUsageStates,  # states
                                              _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IConnectivityInterval]]]],  # value
                                             _type.HRESULT]


class IConnectionProfile3(_inspectable.IInspectable):
    GetAttributedNetworkUsageAsync: _Callable[[_struct.Windows.Foundation.DateTime,  # startTime
                                               _struct.Windows.Foundation.DateTime,  # endTime
                                               _struct.Windows.Networking.Connectivity.NetworkUsageStates,  # states
                                               _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IAttributedNetworkUsage]]]],  # value
                                              _type.HRESULT]


class IConnectionProfile4(_inspectable.IInspectable):
    GetProviderNetworkUsageAsync: _Callable[[_struct.Windows.Foundation.DateTime,  # startTime
                                             _struct.Windows.Foundation.DateTime,  # endTime
                                             _struct.Windows.Networking.Connectivity.NetworkUsageStates,  # states
                                             _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IProviderNetworkUsage]]]],  # value
                                            _type.HRESULT]


class IConnectionProfile5(_inspectable.IInspectable):
    get_CanDelete: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    TryDeleteAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Networking.Connectivity.ConnectionProfileDeleteStatus]]],  # operation
                              _type.HRESULT]


class IConnectionProfile6(_inspectable.IInspectable):
    IsDomainAuthenticatedBy: _Callable[[_enum.Windows.Networking.Connectivity.DomainAuthenticationKind,  # kind
                                        _Pointer[_type.boolean]],  # result
                                       _type.HRESULT]


class IConnectionProfileFilter(_inspectable.IInspectable):
    put_IsConnected: _Callable[[_type.boolean],  # value
                               _type.HRESULT]
    get_IsConnected: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    put_IsWwanConnectionProfile: _Callable[[_type.boolean],  # value
                                           _type.HRESULT]
    get_IsWwanConnectionProfile: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    put_IsWlanConnectionProfile: _Callable[[_type.boolean],  # value
                                           _type.HRESULT]
    get_IsWlanConnectionProfile: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    put_NetworkCostType: _Callable[[_enum.Windows.Networking.Connectivity.NetworkCostType],  # value
                                   _type.HRESULT]
    get_NetworkCostType: _Callable[[_Pointer[_enum.Windows.Networking.Connectivity.NetworkCostType]],  # value
                                   _type.HRESULT]
    put_ServiceProviderGuid: _Callable[[_Windows_Foundation.IReference[_struct.GUID]],  # value
                                       _type.HRESULT]
    get_ServiceProviderGuid: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.GUID]]],  # value
                                       _type.HRESULT]


class IConnectionProfileFilter2(_inspectable.IInspectable):
    put_IsRoaming: _Callable[[_Windows_Foundation.IReference[_type.boolean]],  # value
                             _type.HRESULT]
    get_IsRoaming: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.boolean]]],  # value
                             _type.HRESULT]
    put_IsOverDataLimit: _Callable[[_Windows_Foundation.IReference[_type.boolean]],  # value
                                   _type.HRESULT]
    get_IsOverDataLimit: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.boolean]]],  # value
                                   _type.HRESULT]
    put_IsBackgroundDataUsageRestricted: _Callable[[_Windows_Foundation.IReference[_type.boolean]],  # value
                                                   _type.HRESULT]
    get_IsBackgroundDataUsageRestricted: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.boolean]]],  # value
                                                   _type.HRESULT]
    get_RawData: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                           _type.HRESULT]


class IConnectionProfileFilter3(_inspectable.IInspectable):
    put_PurposeGuid: _Callable[[_Windows_Foundation.IReference[_struct.GUID]],  # value
                               _type.HRESULT]
    get_PurposeGuid: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.GUID]]],  # value
                               _type.HRESULT]


class IConnectionSession(_inspectable.IInspectable):
    get_ConnectionProfile: _Callable[[_Pointer[IConnectionProfile]],  # value
                                     _type.HRESULT]


class IConnectivityInterval(_inspectable.IInspectable):
    get_StartTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # startTime
                             _type.HRESULT]
    get_ConnectionDuration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # duration
                                      _type.HRESULT]


class IConnectivityManagerStatics(_inspectable.IInspectable):
    AcquireConnectionAsync: _Callable[[ICellularApnContext,  # cellularApnContext
                                       _Pointer[_Windows_Foundation.IAsyncOperation[IConnectionSession]]],  # operation
                                      _type.HRESULT]
    AddHttpRoutePolicy: _Callable[[IRoutePolicy],  # routePolicy
                                  _type.HRESULT]
    RemoveHttpRoutePolicy: _Callable[[IRoutePolicy],  # routePolicy
                                     _type.HRESULT]

    _factory = True


class IDataPlanStatus(_inspectable.IInspectable):
    get_DataPlanUsage: _Callable[[_Pointer[IDataPlanUsage]],  # value
                                 _type.HRESULT]
    get_DataLimitInMegabytes: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                                        _type.HRESULT]
    get_InboundBitsPerSecond: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT64]]],  # value
                                        _type.HRESULT]
    get_OutboundBitsPerSecond: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT64]]],  # value
                                         _type.HRESULT]
    get_NextBillingCycle: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                    _type.HRESULT]
    get_MaxTransferSizeInMegabytes: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                                              _type.HRESULT]


class IDataPlanUsage(_inspectable.IInspectable):
    get_MegabytesUsed: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    get_LastSyncTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                _type.HRESULT]


class IDataUsage(_inspectable.IInspectable):
    BytesSent: _Callable[[_Pointer[_type.UINT64]],  # value
                         _type.HRESULT]
    BytesReceived: _Callable[[_Pointer[_type.UINT64]],  # value
                             _type.HRESULT]


class IIPInformation(_inspectable.IInspectable):
    get_NetworkAdapter: _Callable[[_Pointer[INetworkAdapter]],  # value
                                  _type.HRESULT]
    get_PrefixLength: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.BYTE]]],  # value
                                _type.HRESULT]


class ILanIdentifier(_inspectable.IInspectable):
    get_InfrastructureId: _Callable[[_Pointer[ILanIdentifierData]],  # value
                                    _type.HRESULT]
    get_PortId: _Callable[[_Pointer[ILanIdentifierData]],  # value
                          _type.HRESULT]
    get_NetworkAdapterId: _Callable[[_Pointer[_struct.GUID]],  # value
                                    _type.HRESULT]


class ILanIdentifierData(_inspectable.IInspectable):
    get_Type: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]
    get_Value: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.BYTE]]],  # value
                         _type.HRESULT]


class INetworkAdapter(_inspectable.IInspectable):
    get_OutboundMaxBitsPerSecond: _Callable[[_Pointer[_type.UINT64]],  # value
                                            _type.HRESULT]
    get_InboundMaxBitsPerSecond: _Callable[[_Pointer[_type.UINT64]],  # value
                                           _type.HRESULT]
    get_IanaInterfaceType: _Callable[[_Pointer[_type.UINT32]],  # value
                                     _type.HRESULT]
    get_NetworkItem: _Callable[[_Pointer[INetworkItem]],  # value
                               _type.HRESULT]
    get_NetworkAdapterId: _Callable[[_Pointer[_struct.GUID]],  # value
                                    _type.HRESULT]
    GetConnectedProfileAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IConnectionProfile]]],  # value
                                        _type.HRESULT]


class INetworkInformationStatics(_inspectable.IInspectable):
    GetConnectionProfiles: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IConnectionProfile]]],  # value
                                     _type.HRESULT]
    GetInternetConnectionProfile: _Callable[[_Pointer[IConnectionProfile]],  # value
                                            _type.HRESULT]
    GetLanIdentifiers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[ILanIdentifier]]],  # value
                                 _type.HRESULT]
    GetHostNames: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Networking.IHostName]]],  # value
                            _type.HRESULT]
    GetProxyConfigurationAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                           _Pointer[_Windows_Foundation.IAsyncOperation[IProxyConfiguration]]],  # value
                                          _type.HRESULT]
    GetSortedEndpointPairs: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Networking.IEndpointPair],  # destinationList
                                       _enum.Windows.Networking.HostNameSortOptions,  # sortOptions
                                       _Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Networking.IEndpointPair]]],  # value
                                      _type.HRESULT]
    add_NetworkStatusChanged: _Callable[[INetworkStatusChangedEventHandler,  # networkStatusHandler
                                         _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                                        _type.HRESULT]
    remove_NetworkStatusChanged: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                           _type.HRESULT]

    _factory = True


class INetworkInformationStatics2(_inspectable.IInspectable):
    FindConnectionProfilesAsync: _Callable[[IConnectionProfileFilter,  # pProfileFilter
                                            _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IConnectionProfile]]]],  # value
                                           _type.HRESULT]

    _factory = True


class INetworkItem(_inspectable.IInspectable):
    get_NetworkId: _Callable[[_Pointer[_struct.GUID]],  # value
                             _type.HRESULT]
    GetNetworkTypes: _Callable[[_Pointer[_enum.Windows.Networking.Connectivity.NetworkTypes]],  # value
                               _type.HRESULT]


class INetworkSecuritySettings(_inspectable.IInspectable):
    get_NetworkAuthenticationType: _Callable[[_Pointer[_enum.Windows.Networking.Connectivity.NetworkAuthenticationType]],  # value
                                             _type.HRESULT]
    get_NetworkEncryptionType: _Callable[[_Pointer[_enum.Windows.Networking.Connectivity.NetworkEncryptionType]],  # value
                                         _type.HRESULT]


class INetworkStateChangeEventDetails(_inspectable.IInspectable):
    get_HasNewInternetConnectionProfile: _Callable[[_Pointer[_type.boolean]],  # value
                                                   _type.HRESULT]
    get_HasNewConnectionCost: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_HasNewNetworkConnectivityLevel: _Callable[[_Pointer[_type.boolean]],  # value
                                                  _type.HRESULT]
    get_HasNewDomainConnectivityLevel: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]
    get_HasNewHostNameList: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    get_HasNewWwanRegistrationState: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]


class INetworkStateChangeEventDetails2(_inspectable.IInspectable):
    get_HasNewTetheringOperationalState: _Callable[[_Pointer[_type.boolean]],  # value
                                                   _type.HRESULT]
    get_HasNewTetheringClientCount: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]


class INetworkUsage(_inspectable.IInspectable):
    get_BytesSent: _Callable[[_Pointer[_type.UINT64]],  # value
                             _type.HRESULT]
    get_BytesReceived: _Callable[[_Pointer[_type.UINT64]],  # value
                                 _type.HRESULT]
    get_ConnectionDuration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # duration
                                      _type.HRESULT]


class IProviderNetworkUsage(_inspectable.IInspectable):
    get_BytesSent: _Callable[[_Pointer[_type.UINT64]],  # value
                             _type.HRESULT]
    get_BytesReceived: _Callable[[_Pointer[_type.UINT64]],  # value
                                 _type.HRESULT]
    get_ProviderId: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]


class IProxyConfiguration(_inspectable.IInspectable):
    get_ProxyUris: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Foundation.IUriRuntimeClass]]],  # value
                             _type.HRESULT]
    get_CanConnectDirectly: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]


class IRoutePolicy(_inspectable.IInspectable):
    get_ConnectionProfile: _Callable[[_Pointer[IConnectionProfile]],  # value
                                     _type.HRESULT]
    get_HostName: _Callable[[_Pointer[_Windows_Networking.IHostName]],  # value
                            _type.HRESULT]
    get_HostNameType: _Callable[[_Pointer[_enum.Windows.Networking.DomainNameType]],  # value
                                _type.HRESULT]


class IRoutePolicyFactory(_inspectable.IInspectable):
    CreateRoutePolicy: _Callable[[IConnectionProfile,  # connectionProfile
                                  _Windows_Networking.IHostName,  # hostName
                                  _enum.Windows.Networking.DomainNameType,  # type
                                  _Pointer[IRoutePolicy]],  # routePolicy
                                 _type.HRESULT]

    _factory = True


class IWlanConnectionProfileDetails(_inspectable.IInspectable):
    GetConnectedSsid: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]


class IWwanConnectionProfileDetails(_inspectable.IInspectable):
    get_HomeProviderId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_AccessPointName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    GetNetworkRegistrationState: _Callable[[_Pointer[_enum.Windows.Networking.Connectivity.WwanNetworkRegistrationState]],  # value
                                           _type.HRESULT]
    GetCurrentDataClass: _Callable[[_Pointer[_enum.Windows.Networking.Connectivity.WwanDataClass]],  # value
                                   _type.HRESULT]


class IWwanConnectionProfileDetails2(_inspectable.IInspectable):
    get_IPKind: _Callable[[_Pointer[_enum.Windows.Networking.Connectivity.WwanNetworkIPKind]],  # value
                          _type.HRESULT]
    get_PurposeGuids: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_struct.GUID]]],  # value
                                _type.HRESULT]
