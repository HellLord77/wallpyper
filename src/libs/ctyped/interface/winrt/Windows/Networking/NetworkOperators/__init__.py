from __future__ import annotations

from typing import Callable as _Callable

from .. import Connectivity as _Windows_Networking_Connectivity
from ... import Foundation as _Windows_Foundation
from ... import Networking as _Windows_Networking
from ...Data.Xml import Dom as _Windows_Data_Xml_Dom
from ...Devices import Sms as _Windows_Devices_Sms
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IESim(_inspectable.IInspectable):
    get_AvailableMemoryInBytes: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                          _type.HRESULT]
    get_Eid: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_FirmwareVersion: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_MobileBroadbandModemDeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                                _type.HRESULT]
    get_Policy: _Callable[[_Pointer[IESimPolicy]],  # value
                          _type.HRESULT]
    get_State: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.ESimState]],  # value
                         _type.HRESULT]
    GetProfiles: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IESimProfile]]],  # result
                           _type.HRESULT]
    DeleteProfileAsync: _Callable[[_type.HSTRING,  # profileId
                                   _Pointer[_Windows_Foundation.IAsyncOperation[IESimOperationResult]]],  # operation
                                  _type.HRESULT]
    DownloadProfileMetadataAsync: _Callable[[_type.HSTRING,  # activationCode
                                             _Pointer[_Windows_Foundation.IAsyncOperation[IESimDownloadProfileMetadataResult]]],  # operation
                                            _type.HRESULT]
    ResetAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IESimOperationResult]]],  # operation
                          _type.HRESULT]
    add_ProfileChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IESim, _inspectable.IInspectable],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_ProfileChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]


class IESim2(_inspectable.IInspectable):
    Discover: _Callable[[_Pointer[IESimDiscoverResult]],  # result
                        _type.HRESULT]
    DiscoverWithServerAddressAndMatchingId: _Callable[[_type.HSTRING,  # serverAddress
                                                       _type.HSTRING,  # matchingId
                                                       _Pointer[IESimDiscoverResult]],  # result
                                                      _type.HRESULT]
    DiscoverAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IESimDiscoverResult]]],  # operation
                             _type.HRESULT]
    DiscoverWithServerAddressAndMatchingIdAsync: _Callable[[_type.HSTRING,  # serverAddress
                                                            _type.HSTRING,  # matchingId
                                                            _Pointer[_Windows_Foundation.IAsyncOperation[IESimDiscoverResult]]],  # operation
                                                           _type.HRESULT]


class IESim3(_inspectable.IInspectable):
    get_SlotIndex: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                             _type.HRESULT]


class IESimAddedEventArgs(_inspectable.IInspectable):
    get_ESim: _Callable[[_Pointer[IESim]],  # value
                        _type.HRESULT]


class IESimDiscoverEvent(_inspectable.IInspectable):
    get_MatchingId: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_RspServerAddress: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]


class IESimDiscoverResult(_inspectable.IInspectable):
    get_Events: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IESimDiscoverEvent]]],  # value
                          _type.HRESULT]
    get_Kind: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.ESimDiscoverResultKind]],  # value
                        _type.HRESULT]
    get_ProfileMetadata: _Callable[[_Pointer[IESimProfileMetadata]],  # value
                                   _type.HRESULT]
    get_Result: _Callable[[_Pointer[IESimOperationResult]],  # value
                          _type.HRESULT]


class IESimDownloadProfileMetadataResult(_inspectable.IInspectable):
    get_Result: _Callable[[_Pointer[IESimOperationResult]],  # value
                          _type.HRESULT]
    get_ProfileMetadata: _Callable[[_Pointer[IESimProfileMetadata]],  # value
                                   _type.HRESULT]


class IESimManagerStatics(_inspectable.IInspectable, factory=True):
    get_ServiceInfo: _Callable[[_Pointer[IESimServiceInfo]],  # value
                               _type.HRESULT]
    TryCreateESimWatcher: _Callable[[_Pointer[IESimWatcher]],  # result
                                    _type.HRESULT]
    add_ServiceInfoChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_ServiceInfoChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]


class IESimOperationResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.ESimOperationStatus]],  # value
                          _type.HRESULT]


class IESimPolicy(_inspectable.IInspectable):
    get_ShouldEnableManagingUi: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]


class IESimProfile(_inspectable.IInspectable):
    get_Class: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.ESimProfileClass]],  # value
                         _type.HRESULT]
    get_Nickname: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Policy: _Callable[[_Pointer[IESimProfilePolicy]],  # value
                          _type.HRESULT]
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_ProviderIcon: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # value
                                _type.HRESULT]
    get_ProviderId: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_ProviderName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_State: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.ESimProfileState]],  # value
                         _type.HRESULT]
    DisableAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IESimOperationResult]]],  # operation
                            _type.HRESULT]
    EnableAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IESimOperationResult]]],  # operation
                           _type.HRESULT]
    SetNicknameAsync: _Callable[[_type.HSTRING,  # newNickname
                                 _Pointer[_Windows_Foundation.IAsyncOperation[IESimOperationResult]]],  # operation
                                _type.HRESULT]


class IESimProfileMetadata(_inspectable.IInspectable):
    get_IsConfirmationCodeRequired: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]
    get_Policy: _Callable[[_Pointer[IESimProfilePolicy]],  # value
                          _type.HRESULT]
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_ProviderIcon: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # value
                                _type.HRESULT]
    get_ProviderId: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_ProviderName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_State: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.ESimProfileMetadataState]],  # value
                         _type.HRESULT]
    DenyInstallAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IESimOperationResult]]],  # operation
                                _type.HRESULT]
    ConfirmInstallAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IESimOperationResult, _struct.Windows.Networking.NetworkOperators.ESimProfileInstallProgress]]],  # operation
                                   _type.HRESULT]
    ConfirmInstallWithConfirmationCodeAsync: _Callable[[_type.HSTRING,  # confirmationCode
                                                        _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IESimOperationResult, _struct.Windows.Networking.NetworkOperators.ESimProfileInstallProgress]]],  # operation
                                                       _type.HRESULT]
    PostponeInstallAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IESimOperationResult]]],  # operation
                                    _type.HRESULT]
    add_StateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IESimProfileMetadata, _inspectable.IInspectable],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_StateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]


class IESimProfilePolicy(_inspectable.IInspectable):
    get_CanDelete: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_CanDisable: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_IsManagedByEnterprise: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]


class IESimRemovedEventArgs(_inspectable.IInspectable):
    get_ESim: _Callable[[_Pointer[IESim]],  # value
                        _type.HRESULT]


class IESimServiceInfo(_inspectable.IInspectable):
    get_AuthenticationPreference: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.ESimAuthenticationPreference]],  # value
                                            _type.HRESULT]
    get_IsESimUiEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]


class IESimUpdatedEventArgs(_inspectable.IInspectable):
    get_ESim: _Callable[[_Pointer[IESim]],  # value
                        _type.HRESULT]


class IESimWatcher(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.ESimWatcherStatus]],  # value
                          _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    add_Added: _Callable[[_Windows_Foundation.ITypedEventHandler[IESimWatcher, IESimAddedEventArgs],  # handler
                          _Pointer[_struct.EventRegistrationToken]],  # token
                         _type.HRESULT]
    remove_Added: _Callable[[_struct.EventRegistrationToken],  # token
                            _type.HRESULT]
    add_EnumerationCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IESimWatcher, _inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_EnumerationCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    add_Removed: _Callable[[_Windows_Foundation.ITypedEventHandler[IESimWatcher, IESimRemovedEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Removed: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_Stopped: _Callable[[_Windows_Foundation.ITypedEventHandler[IESimWatcher, _inspectable.IInspectable],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Stopped: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_Updated: _Callable[[_Windows_Foundation.ITypedEventHandler[IESimWatcher, IESimUpdatedEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Updated: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]


class IFdnAccessManagerStatics(_inspectable.IInspectable, factory=True):
    RequestUnlockAsync: _Callable[[_type.HSTRING,  # contactListId
                                   _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # returnValue
                                  _type.HRESULT]


class IHotspotAuthenticationContext(_inspectable.IInspectable):
    get_WirelessNetworkId: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                                      _Pointer[_Pointer[_type.BYTE]]],  # value
                                     _type.HRESULT]
    get_NetworkAdapter: _Callable[[_Pointer[_Windows_Networking_Connectivity.INetworkAdapter]],  # value
                                  _type.HRESULT]
    get_RedirectMessageUrl: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                      _type.HRESULT]
    get_RedirectMessageXml: _Callable[[_Pointer[_Windows_Data_Xml_Dom.IXmlDocument]],  # value
                                      _type.HRESULT]
    get_AuthenticationUrl: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                     _type.HRESULT]
    IssueCredentials: _Callable[[_type.HSTRING,  # userName
                                 _type.HSTRING,  # password
                                 _type.HSTRING,  # extraParameters
                                 _type.boolean],  # markAsManualConnectOnFailure
                                _type.HRESULT]
    AbortAuthentication: _Callable[[_type.boolean],  # markAsManual
                                   _type.HRESULT]
    SkipAuthentication: _Callable[[],
                                  _type.HRESULT]
    TriggerAttentionRequired: _Callable[[_type.HSTRING,  # packageRelativeApplicationId
                                         _type.HSTRING],  # applicationParameters
                                        _type.HRESULT]


class IHotspotAuthenticationContext2(_inspectable.IInspectable):
    IssueCredentialsAsync: _Callable[[_type.HSTRING,  # userName
                                      _type.HSTRING,  # password
                                      _type.HSTRING,  # extraParameters
                                      _type.boolean,  # markAsManualConnectOnFailure
                                      _Pointer[_Windows_Foundation.IAsyncOperation[IHotspotCredentialsAuthenticationResult]]],  # asyncInfo
                                     _type.HRESULT]


class IHotspotAuthenticationContextStatics(_inspectable.IInspectable, factory=True):
    TryGetAuthenticationContext: _Callable[[_type.HSTRING,  # evenToken
                                            _Pointer[IHotspotAuthenticationContext],  # context
                                            _Pointer[_type.boolean]],  # isValid
                                           _type.HRESULT]


class IHotspotAuthenticationEventDetails(_inspectable.IInspectable):
    get_EventToken: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]


class IHotspotCredentialsAuthenticationResult(_inspectable.IInspectable):
    get_HasNetworkErrorOccurred: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    get_ResponseCode: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.HotspotAuthenticationResponseCode]],  # value
                                _type.HRESULT]
    get_LogoffUrl: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                             _type.HRESULT]
    get_AuthenticationReplyXml: _Callable[[_Pointer[_Windows_Data_Xml_Dom.IXmlDocument]],  # value
                                          _type.HRESULT]


class IKnownCSimFilePathsStatics(_inspectable.IInspectable, factory=True):
    get_EFSpn: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.UINT32]]],  # value
                         _type.HRESULT]
    get_Gid1: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.UINT32]]],  # value
                        _type.HRESULT]
    get_Gid2: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.UINT32]]],  # value
                        _type.HRESULT]


class IKnownRuimFilePathsStatics(_inspectable.IInspectable, factory=True):
    get_EFSpn: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.UINT32]]],  # value
                         _type.HRESULT]
    get_Gid1: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.UINT32]]],  # value
                        _type.HRESULT]
    get_Gid2: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.UINT32]]],  # value
                        _type.HRESULT]


class IKnownSimFilePathsStatics(_inspectable.IInspectable, factory=True):
    get_EFOns: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.UINT32]]],  # value
                         _type.HRESULT]
    get_EFSpn: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.UINT32]]],  # value
                         _type.HRESULT]
    get_Gid1: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.UINT32]]],  # value
                        _type.HRESULT]
    get_Gid2: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.UINT32]]],  # value
                        _type.HRESULT]


class IKnownUSimFilePathsStatics(_inspectable.IInspectable, factory=True):
    get_EFSpn: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.UINT32]]],  # value
                         _type.HRESULT]
    get_EFOpl: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.UINT32]]],  # value
                         _type.HRESULT]
    get_EFPnn: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.UINT32]]],  # value
                         _type.HRESULT]
    get_Gid1: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.UINT32]]],  # value
                        _type.HRESULT]
    get_Gid2: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.UINT32]]],  # value
                        _type.HRESULT]


class IMobileBroadbandAccount(_inspectable.IInspectable):
    get_NetworkAccountId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_ServiceProviderGuid: _Callable[[_Pointer[_struct.GUID]],  # value
                                       _type.HRESULT]
    get_ServiceProviderName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    get_CurrentNetwork: _Callable[[_Pointer[IMobileBroadbandNetwork]],  # network
                                  _type.HRESULT]
    get_CurrentDeviceInformation: _Callable[[_Pointer[IMobileBroadbandDeviceInformation]],  # deviceInformation
                                            _type.HRESULT]


class IMobileBroadbandAccount2(_inspectable.IInspectable):
    GetConnectionProfiles: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Networking_Connectivity.IConnectionProfile]]],  # value
                                     _type.HRESULT]


class IMobileBroadbandAccount3(_inspectable.IInspectable):
    get_AccountExperienceUrl: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                        _type.HRESULT]


class IMobileBroadbandAccountEventArgs(_inspectable.IInspectable):
    get_NetworkAccountId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]


class IMobileBroadbandAccountStatics(_inspectable.IInspectable, factory=True):
    get_AvailableNetworkAccountIds: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # ppAccountIds
                                              _type.HRESULT]
    CreateFromNetworkAccountId: _Callable[[_type.HSTRING,  # networkAccountId
                                           _Pointer[IMobileBroadbandAccount]],  # ppAccount
                                          _type.HRESULT]


class IMobileBroadbandAccountUpdatedEventArgs(_inspectable.IInspectable):
    get_NetworkAccountId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_HasDeviceInformationChanged: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]
    get_HasNetworkChanged: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]


class IMobileBroadbandAccountWatcher(_inspectable.IInspectable):
    add_AccountAdded: _Callable[[_Windows_Foundation.ITypedEventHandler[IMobileBroadbandAccountWatcher, IMobileBroadbandAccountEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # cookie
                                _type.HRESULT]
    remove_AccountAdded: _Callable[[_struct.EventRegistrationToken],  # cookie
                                   _type.HRESULT]
    add_AccountUpdated: _Callable[[_Windows_Foundation.ITypedEventHandler[IMobileBroadbandAccountWatcher, IMobileBroadbandAccountUpdatedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # cookie
                                  _type.HRESULT]
    remove_AccountUpdated: _Callable[[_struct.EventRegistrationToken],  # cookie
                                     _type.HRESULT]
    add_AccountRemoved: _Callable[[_Windows_Foundation.ITypedEventHandler[IMobileBroadbandAccountWatcher, IMobileBroadbandAccountEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # cookie
                                  _type.HRESULT]
    remove_AccountRemoved: _Callable[[_struct.EventRegistrationToken],  # cookie
                                     _type.HRESULT]
    add_EnumerationCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IMobileBroadbandAccountWatcher, _inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # cookie
                                        _type.HRESULT]
    remove_EnumerationCompleted: _Callable[[_struct.EventRegistrationToken],  # cookie
                                           _type.HRESULT]
    add_Stopped: _Callable[[_Windows_Foundation.ITypedEventHandler[IMobileBroadbandAccountWatcher, _inspectable.IInspectable],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # cookie
                           _type.HRESULT]
    remove_Stopped: _Callable[[_struct.EventRegistrationToken],  # cookie
                              _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.MobileBroadbandAccountWatcherStatus]],  # status
                          _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]


class IMobileBroadbandAntennaSar(_inspectable.IInspectable):
    get_AntennaIndex: _Callable[[_Pointer[_type.INT32]],  # value
                                _type.HRESULT]
    get_SarBackoffIndex: _Callable[[_Pointer[_type.INT32]],  # value
                                   _type.HRESULT]


class IMobileBroadbandAntennaSarFactory(_inspectable.IInspectable, factory=True):
    CreateWithIndex: _Callable[[_type.INT32,  # antennaIndex
                                _type.INT32,  # sarBackoffIndex
                                _Pointer[IMobileBroadbandAntennaSar]],  # antennaSar
                               _type.HRESULT]


class IMobileBroadbandCellCdma(_inspectable.IInspectable):
    get_BaseStationId: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                 _type.HRESULT]
    get_BaseStationPNCode: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                     _type.HRESULT]
    get_BaseStationLatitude: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                                       _type.HRESULT]
    get_BaseStationLongitude: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                                        _type.HRESULT]
    get_BaseStationLastBroadcastGpsTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                                   _type.HRESULT]
    get_NetworkId: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                             _type.HRESULT]
    get_PilotSignalStrengthInDB: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                                           _type.HRESULT]
    get_SystemId: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                            _type.HRESULT]


class IMobileBroadbandCellGsm(_inspectable.IInspectable):
    get_BaseStationId: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                 _type.HRESULT]
    get_CellId: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                          _type.HRESULT]
    get_ChannelNumber: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                 _type.HRESULT]
    get_LocationAreaCode: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                    _type.HRESULT]
    get_ProviderId: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_ReceivedSignalStrengthInDBm: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                                               _type.HRESULT]
    get_TimingAdvanceInBitPeriods: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                             _type.HRESULT]


class IMobileBroadbandCellLte(_inspectable.IInspectable):
    get_CellId: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                          _type.HRESULT]
    get_ChannelNumber: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                 _type.HRESULT]
    get_PhysicalCellId: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                  _type.HRESULT]
    get_ProviderId: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_ReferenceSignalReceivedPowerInDBm: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                                                     _type.HRESULT]
    get_ReferenceSignalReceivedQualityInDBm: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                                                       _type.HRESULT]
    get_TimingAdvanceInBitPeriods: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                             _type.HRESULT]
    get_TrackingAreaCode: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                    _type.HRESULT]


class IMobileBroadbandCellNR(_inspectable.IInspectable):
    get_CellId: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT64]]],  # value
                          _type.HRESULT]
    get_ChannelNumber: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                 _type.HRESULT]
    get_PhysicalCellId: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                  _type.HRESULT]
    get_ProviderId: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_ReferenceSignalReceivedPowerInDBm: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                                                     _type.HRESULT]
    get_ReferenceSignalReceivedQualityInDBm: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                                                       _type.HRESULT]
    get_TimingAdvanceInNanoseconds: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                              _type.HRESULT]
    get_TrackingAreaCode: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                    _type.HRESULT]
    get_SignalToNoiseRatioInDB: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                                          _type.HRESULT]


class IMobileBroadbandCellTdscdma(_inspectable.IInspectable):
    get_CellId: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                          _type.HRESULT]
    get_CellParameterId: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                   _type.HRESULT]
    get_ChannelNumber: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                 _type.HRESULT]
    get_LocationAreaCode: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                    _type.HRESULT]
    get_PathLossInDB: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                                _type.HRESULT]
    get_ProviderId: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_ReceivedSignalCodePowerInDBm: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                                                _type.HRESULT]
    get_TimingAdvanceInBitPeriods: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                             _type.HRESULT]


class IMobileBroadbandCellUmts(_inspectable.IInspectable):
    get_CellId: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                          _type.HRESULT]
    get_ChannelNumber: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                 _type.HRESULT]
    get_LocationAreaCode: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                    _type.HRESULT]
    get_PathLossInDB: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                                _type.HRESULT]
    get_PrimaryScramblingCode: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                         _type.HRESULT]
    get_ProviderId: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_ReceivedSignalCodePowerInDBm: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                                                _type.HRESULT]
    get_SignalToNoiseRatioInDB: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                                          _type.HRESULT]


class IMobileBroadbandCellsInfo(_inspectable.IInspectable):
    get_NeighboringCellsCdma: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMobileBroadbandCellCdma]]],  # value
                                        _type.HRESULT]
    get_NeighboringCellsGsm: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMobileBroadbandCellGsm]]],  # value
                                       _type.HRESULT]
    get_NeighboringCellsLte: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMobileBroadbandCellLte]]],  # value
                                       _type.HRESULT]
    get_NeighboringCellsTdscdma: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMobileBroadbandCellTdscdma]]],  # value
                                           _type.HRESULT]
    get_NeighboringCellsUmts: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMobileBroadbandCellUmts]]],  # value
                                        _type.HRESULT]
    get_ServingCellsCdma: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMobileBroadbandCellCdma]]],  # value
                                    _type.HRESULT]
    get_ServingCellsGsm: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMobileBroadbandCellGsm]]],  # value
                                   _type.HRESULT]
    get_ServingCellsLte: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMobileBroadbandCellLte]]],  # value
                                   _type.HRESULT]
    get_ServingCellsTdscdma: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMobileBroadbandCellTdscdma]]],  # value
                                       _type.HRESULT]
    get_ServingCellsUmts: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMobileBroadbandCellUmts]]],  # value
                                    _type.HRESULT]


class IMobileBroadbandCellsInfo2(_inspectable.IInspectable):
    get_NeighboringCellsNR: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMobileBroadbandCellNR]]],  # value
                                      _type.HRESULT]
    get_ServingCellsNR: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMobileBroadbandCellNR]]],  # value
                                  _type.HRESULT]


class IMobileBroadbandCurrentSlotIndexChangedEventArgs(_inspectable.IInspectable):
    get_CurrentSlotIndex: _Callable[[_Pointer[_type.INT32]],  # value
                                    _type.HRESULT]


class IMobileBroadbandDeviceInformation(_inspectable.IInspectable):
    get_NetworkDeviceStatus: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.NetworkDeviceStatus]],  # value
                                       _type.HRESULT]
    get_Manufacturer: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_Model: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_FirmwareInformation: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    get_CellularClass: _Callable[[_Pointer[_enum.Windows.Devices.Sms.CellularClass]],  # value
                                 _type.HRESULT]
    get_DataClasses: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.DataClasses]],  # value
                               _type.HRESULT]
    get_CustomDataClass: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_MobileEquipmentId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    get_TelephoneNumbers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                    _type.HRESULT]
    get_SubscriberId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_SimIccId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_DeviceType: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.MobileBroadbandDeviceType]],  # pDeviceType
                              _type.HRESULT]
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_CurrentRadioState: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.MobileBroadbandRadioState]],  # pCurrentState
                                     _type.HRESULT]


class IMobileBroadbandDeviceInformation2(_inspectable.IInspectable):
    get_PinManager: _Callable[[_Pointer[IMobileBroadbandPinManager]],  # value
                              _type.HRESULT]
    get_Revision: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_SerialNumber: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]


class IMobileBroadbandDeviceInformation3(_inspectable.IInspectable):
    get_SimSpn: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_SimPnn: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_SimGid1: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]


class IMobileBroadbandDeviceInformation4(_inspectable.IInspectable):
    get_SlotManager: _Callable[[_Pointer[IMobileBroadbandSlotManager]],  # value
                               _type.HRESULT]


class IMobileBroadbandDeviceService(_inspectable.IInspectable):
    get_DeviceServiceId: _Callable[[_Pointer[_struct.GUID]],  # value
                                   _type.HRESULT]
    get_SupportedCommands: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.UINT32]]],  # value
                                     _type.HRESULT]
    OpenDataSession: _Callable[[_Pointer[IMobileBroadbandDeviceServiceDataSession]],  # value
                               _type.HRESULT]
    OpenCommandSession: _Callable[[_Pointer[IMobileBroadbandDeviceServiceCommandSession]],  # value
                                  _type.HRESULT]


class IMobileBroadbandDeviceServiceCommandResult(_inspectable.IInspectable):
    get_StatusCode: _Callable[[_Pointer[_type.UINT32]],  # value
                              _type.HRESULT]
    get_ResponseData: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                _type.HRESULT]


class IMobileBroadbandDeviceServiceCommandSession(_inspectable.IInspectable):
    SendQueryCommandAsync: _Callable[[_type.UINT32,  # commandId
                                      _Windows_Storage_Streams.IBuffer,  # data
                                      _Pointer[_Windows_Foundation.IAsyncOperation[IMobileBroadbandDeviceServiceCommandResult]]],  # asyncInfo
                                     _type.HRESULT]
    SendSetCommandAsync: _Callable[[_type.UINT32,  # commandId
                                    _Windows_Storage_Streams.IBuffer,  # data
                                    _Pointer[_Windows_Foundation.IAsyncOperation[IMobileBroadbandDeviceServiceCommandResult]]],  # asyncInfo
                                   _type.HRESULT]
    CloseSession: _Callable[[],
                            _type.HRESULT]


class IMobileBroadbandDeviceServiceDataReceivedEventArgs(_inspectable.IInspectable):
    get_ReceivedData: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                _type.HRESULT]


class IMobileBroadbandDeviceServiceDataSession(_inspectable.IInspectable):
    WriteDataAsync: _Callable[[_Windows_Storage_Streams.IBuffer,  # value
                               _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                              _type.HRESULT]
    CloseSession: _Callable[[],
                            _type.HRESULT]
    add_DataReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[IMobileBroadbandDeviceServiceDataSession, IMobileBroadbandDeviceServiceDataReceivedEventArgs],  # eventHandler
                                 _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                                _type.HRESULT]
    remove_DataReceived: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                   _type.HRESULT]


class IMobileBroadbandDeviceServiceInformation(_inspectable.IInspectable):
    get_DeviceServiceId: _Callable[[_Pointer[_struct.GUID]],  # value
                                   _type.HRESULT]
    get_IsDataReadSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    get_IsDataWriteSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]


class IMobileBroadbandDeviceServiceTriggerDetails(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_DeviceServiceId: _Callable[[_Pointer[_struct.GUID]],  # value
                                   _type.HRESULT]
    get_ReceivedData: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                _type.HRESULT]


class IMobileBroadbandDeviceServiceTriggerDetails2(_inspectable.IInspectable):
    get_EventId: _Callable[[_Pointer[_type.UINT32]],  # value
                           _type.HRESULT]


class IMobileBroadbandModem(_inspectable.IInspectable):
    get_CurrentAccount: _Callable[[_Pointer[IMobileBroadbandAccount]],  # value
                                  _type.HRESULT]
    get_DeviceInformation: _Callable[[_Pointer[IMobileBroadbandDeviceInformation]],  # value
                                     _type.HRESULT]
    get_MaxDeviceServiceCommandSizeInBytes: _Callable[[_Pointer[_type.UINT32]],  # value
                                                      _type.HRESULT]
    get_MaxDeviceServiceDataSizeInBytes: _Callable[[_Pointer[_type.UINT32]],  # value
                                                   _type.HRESULT]
    get_DeviceServices: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMobileBroadbandDeviceServiceInformation]]],  # value
                                  _type.HRESULT]
    GetDeviceService: _Callable[[_struct.GUID,  # deviceServiceId
                                 _Pointer[IMobileBroadbandDeviceService]],  # value
                                _type.HRESULT]
    get_IsResetSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    ResetAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                          _type.HRESULT]
    GetCurrentConfigurationAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IMobileBroadbandModemConfiguration]]],  # asyncInfo
                                            _type.HRESULT]
    get_CurrentNetwork: _Callable[[_Pointer[IMobileBroadbandNetwork]],  # value
                                  _type.HRESULT]


class IMobileBroadbandModem2(_inspectable.IInspectable):
    GetIsPassthroughEnabledAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # asyncInfo
                                            _type.HRESULT]
    SetIsPassthroughEnabledAsync: _Callable[[_type.boolean,  # value
                                             _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Networking.NetworkOperators.MobileBroadbandModemStatus]]],  # asyncInfo
                                            _type.HRESULT]


class IMobileBroadbandModem3(_inspectable.IInspectable):
    TryGetPcoAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IMobileBroadbandPco]]],  # operation
                              _type.HRESULT]
    get_IsInEmergencyCallMode: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    add_IsInEmergencyCallModeChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMobileBroadbandModem, _inspectable.IInspectable],  # handler
                                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                                _type.HRESULT]
    remove_IsInEmergencyCallModeChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                   _type.HRESULT]


class IMobileBroadbandModem4(_inspectable.IInspectable):
    SetIsPassthroughEnabledWithSlotIndexAsync: _Callable[[_type.boolean,  # value
                                                          _type.INT32,  # slotindex
                                                          _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Networking.NetworkOperators.MobileBroadbandModemStatus]]],  # operation
                                                         _type.HRESULT]
    GetIsPassthroughEnabledWithSlotIndexAsync: _Callable[[_type.INT32,  # slotindex
                                                          _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                                         _type.HRESULT]
    SetIsPassthroughEnabledWithSlotIndex: _Callable[[_type.boolean,  # value
                                                     _type.INT32,  # slotindex
                                                     _Pointer[_enum.Windows.Networking.NetworkOperators.MobileBroadbandModemStatus]],  # result
                                                    _type.HRESULT]
    GetIsPassthroughEnabledWithSlotIndex: _Callable[[_type.INT32,  # slotindex
                                                     _Pointer[_type.boolean]],  # result
                                                    _type.HRESULT]


class IMobileBroadbandModemConfiguration(_inspectable.IInspectable):
    get_Uicc: _Callable[[_Pointer[IMobileBroadbandUicc]],  # value
                        _type.HRESULT]
    get_HomeProviderId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_HomeProviderName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]


class IMobileBroadbandModemConfiguration2(_inspectable.IInspectable):
    get_SarManager: _Callable[[_Pointer[IMobileBroadbandSarManager]],  # value
                              _type.HRESULT]


class IMobileBroadbandModemIsolation(_inspectable.IInspectable):
    AddAllowedHost: _Callable[[_Windows_Networking.IHostName],  # host
                              _type.HRESULT]
    AddAllowedHostRange: _Callable[[_Windows_Networking.IHostName,  # first
                                    _Windows_Networking.IHostName],  # last
                                   _type.HRESULT]
    ApplyConfigurationAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                       _type.HRESULT]
    ClearConfigurationAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                       _type.HRESULT]


class IMobileBroadbandModemIsolationFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.HSTRING,  # modemDeviceId
                       _type.HSTRING,  # ruleGroupId
                       _Pointer[IMobileBroadbandModemIsolation]],  # result
                      _type.HRESULT]


class IMobileBroadbandModemStatics(_inspectable.IInspectable, factory=True):
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    FromId: _Callable[[_type.HSTRING,  # deviceId
                       _Pointer[IMobileBroadbandModem]],  # value
                      _type.HRESULT]
    GetDefault: _Callable[[_Pointer[IMobileBroadbandModem]],  # value
                          _type.HRESULT]


class IMobileBroadbandNetwork(_inspectable.IInspectable):
    get_NetworkAdapter: _Callable[[_Pointer[_Windows_Networking_Connectivity.INetworkAdapter]],  # value
                                  _type.HRESULT]
    get_NetworkRegistrationState: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.NetworkRegistrationState]],  # registrationState
                                            _type.HRESULT]
    get_RegistrationNetworkError: _Callable[[_Pointer[_type.UINT32]],  # networkError
                                            _type.HRESULT]
    get_PacketAttachNetworkError: _Callable[[_Pointer[_type.UINT32]],  # networkError
                                            _type.HRESULT]
    get_ActivationNetworkError: _Callable[[_Pointer[_type.UINT32]],  # networkError
                                          _type.HRESULT]
    get_AccessPointName: _Callable[[_Pointer[_type.HSTRING]],  # apn
                                   _type.HRESULT]
    get_RegisteredDataClass: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.DataClasses]],  # value
                                       _type.HRESULT]
    get_RegisteredProviderId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                        _type.HRESULT]
    get_RegisteredProviderName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                          _type.HRESULT]
    ShowConnectionUI: _Callable[[],
                                _type.HRESULT]


class IMobileBroadbandNetwork2(_inspectable.IInspectable):
    GetVoiceCallSupportAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # asyncInfo
                                        _type.HRESULT]
    get_RegistrationUiccApps: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMobileBroadbandUiccApp]]],  # value
                                        _type.HRESULT]


class IMobileBroadbandNetwork3(_inspectable.IInspectable):
    GetCellsInfoAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IMobileBroadbandCellsInfo]]],  # asyncOperation
                                 _type.HRESULT]


class IMobileBroadbandNetworkRegistrationStateChange(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Network: _Callable[[_Pointer[IMobileBroadbandNetwork]],  # value
                           _type.HRESULT]


class IMobileBroadbandNetworkRegistrationStateChangeTriggerDetails(_inspectable.IInspectable):
    get_NetworkRegistrationStateChanges: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMobileBroadbandNetworkRegistrationStateChange]]],  # value
                                                   _type.HRESULT]


class IMobileBroadbandPco(_inspectable.IInspectable):
    get_Data: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # result
                        _type.HRESULT]
    get_IsComplete: _Callable[[_Pointer[_type.boolean]],  # result
                              _type.HRESULT]
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # result
                            _type.HRESULT]


class IMobileBroadbandPcoDataChangeTriggerDetails(_inspectable.IInspectable):
    get_UpdatedData: _Callable[[_Pointer[IMobileBroadbandPco]],  # result
                               _type.HRESULT]


class IMobileBroadbandPin(_inspectable.IInspectable):
    get_Type: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.MobileBroadbandPinType]],  # value
                        _type.HRESULT]
    get_LockState: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.MobileBroadbandPinLockState]],  # value
                             _type.HRESULT]
    get_Format: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.MobileBroadbandPinFormat]],  # value
                          _type.HRESULT]
    get_Enabled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_MaxLength: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    get_MinLength: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    get_AttemptsRemaining: _Callable[[_Pointer[_type.UINT32]],  # value
                                     _type.HRESULT]
    EnableAsync: _Callable[[_type.HSTRING,  # currentPin
                            _Pointer[_Windows_Foundation.IAsyncOperation[IMobileBroadbandPinOperationResult]]],  # asyncInfo
                           _type.HRESULT]
    DisableAsync: _Callable[[_type.HSTRING,  # currentPin
                             _Pointer[_Windows_Foundation.IAsyncOperation[IMobileBroadbandPinOperationResult]]],  # asyncInfo
                            _type.HRESULT]
    EnterAsync: _Callable[[_type.HSTRING,  # currentPin
                           _Pointer[_Windows_Foundation.IAsyncOperation[IMobileBroadbandPinOperationResult]]],  # asyncInfo
                          _type.HRESULT]
    ChangeAsync: _Callable[[_type.HSTRING,  # currentPin
                            _type.HSTRING,  # newPin
                            _Pointer[_Windows_Foundation.IAsyncOperation[IMobileBroadbandPinOperationResult]]],  # asyncInfo
                           _type.HRESULT]
    UnblockAsync: _Callable[[_type.HSTRING,  # pinUnblockKey
                             _type.HSTRING,  # newPin
                             _Pointer[_Windows_Foundation.IAsyncOperation[IMobileBroadbandPinOperationResult]]],  # asyncInfo
                            _type.HRESULT]


class IMobileBroadbandPinLockStateChange(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_PinType: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.MobileBroadbandPinType]],  # value
                           _type.HRESULT]
    get_PinLockState: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.MobileBroadbandPinLockState]],  # value
                                _type.HRESULT]


class IMobileBroadbandPinLockStateChangeTriggerDetails(_inspectable.IInspectable):
    get_PinLockStateChanges: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMobileBroadbandPinLockStateChange]]],  # value
                                       _type.HRESULT]


class IMobileBroadbandPinManager(_inspectable.IInspectable):
    get_SupportedPins: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Networking.NetworkOperators.MobileBroadbandPinType]]],  # value
                                 _type.HRESULT]
    GetPin: _Callable[[_enum.Windows.Networking.NetworkOperators.MobileBroadbandPinType,  # pinType
                       _Pointer[IMobileBroadbandPin]],  # value
                      _type.HRESULT]


class IMobileBroadbandPinOperationResult(_inspectable.IInspectable):
    get_IsSuccessful: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_AttemptsRemaining: _Callable[[_Pointer[_type.UINT32]],  # value
                                     _type.HRESULT]


class IMobileBroadbandRadioStateChange(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_RadioState: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.MobileBroadbandRadioState]],  # value
                              _type.HRESULT]


class IMobileBroadbandRadioStateChangeTriggerDetails(_inspectable.IInspectable):
    get_RadioStateChanges: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMobileBroadbandRadioStateChange]]],  # value
                                     _type.HRESULT]


class IMobileBroadbandSarManager(_inspectable.IInspectable):
    get_IsBackoffEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_IsWiFiHardwareIntegrated: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    get_IsSarControlledByHardware: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    get_Antennas: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMobileBroadbandAntennaSar]]],  # value
                            _type.HRESULT]
    get_HysteresisTimerPeriod: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                         _type.HRESULT]
    add_TransmissionStateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMobileBroadbandSarManager, IMobileBroadbandTransmissionStateChangedEventArgs],  # handler
                                             _Pointer[_struct.EventRegistrationToken]],  # token
                                            _type.HRESULT]
    remove_TransmissionStateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                               _type.HRESULT]
    EnableBackoffAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                  _type.HRESULT]
    DisableBackoffAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                   _type.HRESULT]
    SetConfigurationAsync: _Callable[[_Windows_Foundation_Collections.IIterable[IMobileBroadbandAntennaSar],  # antennas
                                      _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                     _type.HRESULT]
    RevertSarToHardwareControlAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                               _type.HRESULT]
    SetTransmissionStateChangedHysteresisAsync: _Callable[[_struct.Windows.Foundation.TimeSpan,  # timerPeriod
                                                           _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                                          _type.HRESULT]
    GetIsTransmittingAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                      _type.HRESULT]
    StartTransmissionStateMonitoring: _Callable[[],
                                                _type.HRESULT]
    StopTransmissionStateMonitoring: _Callable[[],
                                               _type.HRESULT]


class IMobileBroadbandSlotInfo(_inspectable.IInspectable):
    get_Index: _Callable[[_Pointer[_type.INT32]],  # value
                         _type.HRESULT]
    get_State: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.MobileBroadbandSlotState]],  # value
                         _type.HRESULT]


class IMobileBroadbandSlotInfo2(_inspectable.IInspectable):
    get_IccId: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]


class IMobileBroadbandSlotInfoChangedEventArgs(_inspectable.IInspectable):
    get_SlotInfo: _Callable[[_Pointer[IMobileBroadbandSlotInfo]],  # value
                            _type.HRESULT]


class IMobileBroadbandSlotManager(_inspectable.IInspectable):
    get_SlotInfos: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMobileBroadbandSlotInfo]]],  # value
                             _type.HRESULT]
    get_CurrentSlotIndex: _Callable[[_Pointer[_type.INT32]],  # value
                                    _type.HRESULT]
    SetCurrentSlot: _Callable[[_type.INT32,  # slotIndex
                               _Pointer[_enum.Windows.Networking.NetworkOperators.MobileBroadbandModemStatus]],  # result
                              _type.HRESULT]
    SetCurrentSlotAsync: _Callable[[_type.INT32,  # slotIndex
                                    _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Networking.NetworkOperators.MobileBroadbandModemStatus]]],  # operation
                                   _type.HRESULT]
    add_SlotInfoChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMobileBroadbandSlotManager, IMobileBroadbandSlotInfoChangedEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_SlotInfoChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    add_CurrentSlotIndexChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMobileBroadbandSlotManager, IMobileBroadbandCurrentSlotIndexChangedEventArgs],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_CurrentSlotIndexChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]


class IMobileBroadbandTransmissionStateChangedEventArgs(_inspectable.IInspectable):
    get_IsTransmitting: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]


class IMobileBroadbandUicc(_inspectable.IInspectable):
    get_SimIccId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    GetUiccAppsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IMobileBroadbandUiccAppsResult]]],  # asyncInfo
                                _type.HRESULT]


class IMobileBroadbandUiccApp(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                      _type.HRESULT]
    get_Kind: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.UiccAppKind]],  # value
                        _type.HRESULT]
    GetRecordDetailsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.UINT32],  # uiccFilePath
                                      _Pointer[_Windows_Foundation.IAsyncOperation[IMobileBroadbandUiccAppRecordDetailsResult]]],  # asyncInfo
                                     _type.HRESULT]
    ReadRecordAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.UINT32],  # uiccFilePath
                                _type.INT32,  # recordIndex
                                _Pointer[_Windows_Foundation.IAsyncOperation[IMobileBroadbandUiccAppReadRecordResult]]],  # asyncInfo
                               _type.HRESULT]


class IMobileBroadbandUiccAppReadRecordResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.MobileBroadbandUiccAppOperationStatus]],  # value
                          _type.HRESULT]
    get_Data: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                        _type.HRESULT]


class IMobileBroadbandUiccAppRecordDetailsResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.MobileBroadbandUiccAppOperationStatus]],  # value
                          _type.HRESULT]
    get_Kind: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.UiccAppRecordKind]],  # value
                        _type.HRESULT]
    get_RecordCount: _Callable[[_Pointer[_type.INT32]],  # value
                               _type.HRESULT]
    get_RecordSize: _Callable[[_Pointer[_type.INT32]],  # value
                              _type.HRESULT]
    get_ReadAccessCondition: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.UiccAccessCondition]],  # value
                                       _type.HRESULT]
    get_WriteAccessCondition: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.UiccAccessCondition]],  # value
                                        _type.HRESULT]


class IMobileBroadbandUiccAppsResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.MobileBroadbandUiccAppOperationStatus]],  # value
                          _type.HRESULT]
    get_UiccApps: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMobileBroadbandUiccApp]]],  # value
                            _type.HRESULT]


class INetworkOperatorDataUsageTriggerDetails(_inspectable.IInspectable):
    get_NotificationKind: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.NetworkOperatorDataUsageNotificationKind]],  # value
                                    _type.HRESULT]


class INetworkOperatorNotificationEventDetails(_inspectable.IInspectable):
    get_NotificationType: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.NetworkOperatorEventMessageType]],  # value
                                    _type.HRESULT]
    get_NetworkAccountId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_EncodingType: _Callable[[_Pointer[_type.BYTE]],  # value
                                _type.HRESULT]
    get_Message: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_RuleId: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_SmsMessage: _Callable[[_Pointer[_Windows_Devices_Sms.ISmsMessage]],  # value
                              _type.HRESULT]


class INetworkOperatorTetheringAccessPointConfiguration(_inspectable.IInspectable):
    get_Ssid: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Ssid: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_Passphrase: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_Passphrase: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]


class INetworkOperatorTetheringAccessPointConfiguration2(_inspectable.IInspectable):
    IsBandSupported: _Callable[[_enum.Windows.Networking.NetworkOperators.TetheringWiFiBand,  # band
                                _Pointer[_type.boolean]],  # result
                               _type.HRESULT]
    IsBandSupportedAsync: _Callable[[_enum.Windows.Networking.NetworkOperators.TetheringWiFiBand,  # band
                                     _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                    _type.HRESULT]
    get_Band: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.TetheringWiFiBand]],  # value
                        _type.HRESULT]
    put_Band: _Callable[[_enum.Windows.Networking.NetworkOperators.TetheringWiFiBand],  # value
                        _type.HRESULT]


class INetworkOperatorTetheringClient(_inspectable.IInspectable):
    get_MacAddress: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_HostNames: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Networking.IHostName]]],  # value
                             _type.HRESULT]


class INetworkOperatorTetheringClientManager(_inspectable.IInspectable):
    GetTetheringClients: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[INetworkOperatorTetheringClient]]],  # value
                                   _type.HRESULT]


class INetworkOperatorTetheringEntitlementCheck(_inspectable.IInspectable):
    AuthorizeTethering: _Callable[[_type.boolean,  # allow
                                   _type.HSTRING],  # entitlementFailureReason
                                  _type.HRESULT]


class INetworkOperatorTetheringManager(_inspectable.IInspectable):
    get_MaxClientCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]
    get_ClientCount: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]
    get_TetheringOperationalState: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.TetheringOperationalState]],  # value
                                             _type.HRESULT]
    GetCurrentAccessPointConfiguration: _Callable[[_Pointer[INetworkOperatorTetheringAccessPointConfiguration]],  # configuration
                                                  _type.HRESULT]
    ConfigureAccessPointAsync: _Callable[[INetworkOperatorTetheringAccessPointConfiguration,  # configuration
                                          _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                         _type.HRESULT]
    StartTetheringAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[INetworkOperatorTetheringOperationResult]]],  # asyncInfo
                                   _type.HRESULT]
    StopTetheringAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[INetworkOperatorTetheringOperationResult]]],  # asyncInfo
                                  _type.HRESULT]


class INetworkOperatorTetheringManagerStatics(_inspectable.IInspectable, factory=True):
    GetTetheringCapability: _Callable[[_type.HSTRING,  # networkAccountId
                                       _Pointer[_enum.Windows.Networking.NetworkOperators.TetheringCapability]],  # value
                                      _type.HRESULT]
    CreateFromNetworkAccountId: _Callable[[_type.HSTRING,  # networkAccountId
                                           _Pointer[INetworkOperatorTetheringManager]],  # ppManager
                                          _type.HRESULT]


class INetworkOperatorTetheringManagerStatics2(_inspectable.IInspectable, factory=True):
    GetTetheringCapabilityFromConnectionProfile: _Callable[[_Windows_Networking_Connectivity.IConnectionProfile,  # profile
                                                            _Pointer[_enum.Windows.Networking.NetworkOperators.TetheringCapability]],  # result
                                                           _type.HRESULT]
    CreateFromConnectionProfile: _Callable[[_Windows_Networking_Connectivity.IConnectionProfile,  # profile
                                            _Pointer[INetworkOperatorTetheringManager]],  # ppManager
                                           _type.HRESULT]


class INetworkOperatorTetheringManagerStatics3(_inspectable.IInspectable, factory=True):
    CreateFromConnectionProfileWithTargetAdapter: _Callable[[_Windows_Networking_Connectivity.IConnectionProfile,  # profile
                                                             _Windows_Networking_Connectivity.INetworkAdapter,  # adapter
                                                             _Pointer[INetworkOperatorTetheringManager]],  # ppManager
                                                            _type.HRESULT]


class INetworkOperatorTetheringManagerStatics4(_inspectable.IInspectable, factory=True):
    IsNoConnectionsTimeoutEnabled: _Callable[[_Pointer[_type.boolean]],  # result
                                             _type.HRESULT]
    EnableNoConnectionsTimeout: _Callable[[],
                                          _type.HRESULT]
    EnableNoConnectionsTimeoutAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                               _type.HRESULT]
    DisableNoConnectionsTimeout: _Callable[[],
                                           _type.HRESULT]
    DisableNoConnectionsTimeoutAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                                _type.HRESULT]


class INetworkOperatorTetheringOperationResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.TetheringOperationStatus]],  # value
                          _type.HRESULT]
    get_AdditionalErrorMessage: _Callable[[_Pointer[_type.HSTRING]],  # value
                                          _type.HRESULT]


class IProvisionFromXmlDocumentResults(_inspectable.IInspectable):
    get_AllElementsProvisioned: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    get_ProvisionResultsXml: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]


class IProvisionedProfile(_inspectable.IInspectable):
    UpdateCost: _Callable[[_enum.Windows.Networking.Connectivity.NetworkCostType],  # value
                          _type.HRESULT]
    UpdateUsage: _Callable[[_struct.Windows.Networking.NetworkOperators.ProfileUsage],  # value
                           _type.HRESULT]


class IProvisioningAgent(_inspectable.IInspectable):
    ProvisionFromXmlDocumentAsync: _Callable[[_type.HSTRING,  # provisioningXmlDocument
                                              _Pointer[_Windows_Foundation.IAsyncOperation[IProvisionFromXmlDocumentResults]]],  # asyncInfo
                                             _type.HRESULT]
    GetProvisionedProfile: _Callable[[_enum.Windows.Networking.NetworkOperators.ProfileMediaType,  # mediaType
                                      _type.HSTRING,  # profileName
                                      _Pointer[IProvisionedProfile]],  # provisionedProfile
                                     _type.HRESULT]


class IProvisioningAgentStaticMethods(_inspectable.IInspectable, factory=True):
    CreateFromNetworkAccountId: _Callable[[_type.HSTRING,  # networkAccountId
                                           _Pointer[IProvisioningAgent]],  # provisioningAgent
                                          _type.HRESULT]


class ITetheringEntitlementCheckTriggerDetails(_inspectable.IInspectable):
    get_NetworkAccountId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    AllowTethering: _Callable[[],
                              _type.HRESULT]
    DenyTethering: _Callable[[_type.HSTRING],  # entitlementFailureReason
                             _type.HRESULT]


class IUssdMessage(_inspectable.IInspectable):
    get_DataCodingScheme: _Callable[[_Pointer[_type.BYTE]],  # value
                                    _type.HRESULT]
    put_DataCodingScheme: _Callable[[_type.BYTE],  # value
                                    _type.HRESULT]
    GetPayload: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                           _Pointer[_Pointer[_type.BYTE]]],  # value
                          _type.HRESULT]
    SetPayload: _Callable[[_type.UINT32,  # __valueSize
                           _Pointer[_type.BYTE]],  # value
                          _type.HRESULT]
    get_PayloadAsText: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    put_PayloadAsText: _Callable[[_type.HSTRING],  # value
                                 _type.HRESULT]


class IUssdMessageFactory(_inspectable.IInspectable, factory=True):
    CreateMessage: _Callable[[_type.HSTRING,  # messageText
                              _Pointer[IUssdMessage]],  # ussdMessage
                             _type.HRESULT]


class IUssdReply(_inspectable.IInspectable):
    get_ResultCode: _Callable[[_Pointer[_enum.Windows.Networking.NetworkOperators.UssdResultCode]],  # value
                              _type.HRESULT]
    get_Message: _Callable[[_Pointer[IUssdMessage]],  # value
                           _type.HRESULT]


class IUssdSession(_inspectable.IInspectable):
    SendMessageAndGetReplyAsync: _Callable[[IUssdMessage,  # message
                                            _Pointer[_Windows_Foundation.IAsyncOperation[IUssdReply]]],  # asyncInfo
                                           _type.HRESULT]
    Close: _Callable[[],
                     _type.HRESULT]


class IUssdSessionStatics(_inspectable.IInspectable, factory=True):
    CreateFromNetworkAccountId: _Callable[[_type.HSTRING,  # networkAccountId
                                           _Pointer[IUssdSession]],  # ussdSession
                                          _type.HRESULT]
    CreateFromNetworkInterfaceId: _Callable[[_type.HSTRING,  # networkInterfaceId
                                             _Pointer[IUssdSession]],  # ussdSession
                                            _type.HRESULT]
