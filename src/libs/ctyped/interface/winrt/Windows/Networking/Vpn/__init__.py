from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import Networking as _Windows_Networking
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Security import Credentials as _Windows_Security_Credentials
from ...Security.Cryptography import Certificates as _Windows_Security_Cryptography_Certificates
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IVpnAppId(_inspectable.IInspectable):
    get_Type: _Callable[[_Pointer[_enum.Windows.Networking.Vpn.VpnAppIdType]],  # value
                        _type.HRESULT]
    put_Type: _Callable[[_enum.Windows.Networking.Vpn.VpnAppIdType],  # value
                        _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Value: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]


class IVpnAppIdFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_enum.Windows.Networking.Vpn.VpnAppIdType,  # type
                       _type.HSTRING,  # value
                       _Pointer[IVpnAppId]],  # result
                      _type.HRESULT]


class IVpnChannel(_inspectable.IInspectable):
    AssociateTransport: _Callable[[_inspectable.IInspectable,  # mainOuterTunnelTransport
                                   _inspectable.IInspectable],  # optionalOuterTunnelTransport
                                  _type.HRESULT]
    Start: _Callable[[_Windows_Foundation_Collections.IVectorView[_Windows_Networking.IHostName],  # assignedClientIPv4list
                      _Windows_Foundation_Collections.IVectorView[_Windows_Networking.IHostName],  # assignedClientIPv6list
                      IVpnInterfaceId,  # vpnInterfaceId
                      IVpnRouteAssignment,  # routeScope
                      IVpnNamespaceAssignment,  # namespaceScope
                      _type.UINT32,  # mtuSize
                      _type.UINT32,  # maxFrameSize
                      _type.boolean,  # optimizeForLowCostNetwork
                      _inspectable.IInspectable,  # mainOuterTunnelTransport
                      _inspectable.IInspectable],  # optionalOuterTunnelTransport
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    RequestCredentials: _Callable[[_enum.Windows.Networking.Vpn.VpnCredentialType,  # credType
                                   _type.boolean,  # isRetry
                                   _type.boolean,  # isSingleSignOnCredential
                                   _Windows_Security_Cryptography_Certificates.ICertificate,  # certificate
                                   _Pointer[IVpnPickedCredential]],  # credential
                                  _type.HRESULT]
    RequestVpnPacketBuffer: _Callable[[_enum.Windows.Networking.Vpn.VpnDataPathType,  # type
                                       _Pointer[IVpnPacketBuffer]],  # vpnPacketBuffer
                                      _type.HRESULT]
    LogDiagnosticMessage: _Callable[[_type.HSTRING],  # message
                                    _type.HRESULT]
    get_Id: _Callable[[_Pointer[_type.UINT32]],  # value
                      _type.HRESULT]
    get_Configuration: _Callable[[_Pointer[IVpnChannelConfiguration]],  # value
                                 _type.HRESULT]
    add_ActivityChange: _Callable[[_Windows_Foundation.ITypedEventHandler[IVpnChannel, IVpnChannelActivityEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_ActivityChange: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    put_PlugInContext: _Callable[[_inspectable.IInspectable],  # value
                                 _type.HRESULT]
    get_PlugInContext: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                 _type.HRESULT]
    get_SystemHealth: _Callable[[_Pointer[IVpnSystemHealth]],  # value
                                _type.HRESULT]
    RequestCustomPrompt: _Callable[[_Windows_Foundation_Collections.IVectorView[IVpnCustomPrompt]],  # customPrompt
                                   _type.HRESULT]
    SetErrorMessage: _Callable[[_type.HSTRING],  # message
                               _type.HRESULT]
    SetAllowedSslTlsVersions: _Callable[[_inspectable.IInspectable,  # tunnelTransport
                                         _type.boolean],  # useTls12
                                        _type.HRESULT]


class IVpnChannel2(_inspectable.IInspectable):
    StartWithMainTransport: _Callable[[_Windows_Foundation_Collections.IVectorView[_Windows_Networking.IHostName],  # assignedClientIPv4list
                                       _Windows_Foundation_Collections.IVectorView[_Windows_Networking.IHostName],  # assignedClientIPv6list
                                       IVpnInterfaceId,  # vpnInterfaceId
                                       IVpnRouteAssignment,  # assignedRoutes
                                       IVpnDomainNameAssignment,  # assignedDomainName
                                       _type.UINT32,  # mtuSize
                                       _type.UINT32,  # maxFrameSize
                                       _type.boolean,  # Reserved
                                       _inspectable.IInspectable],  # mainOuterTunnelTransport
                                      _type.HRESULT]
    StartExistingTransports: _Callable[[_Windows_Foundation_Collections.IVectorView[_Windows_Networking.IHostName],  # assignedClientIPv4list
                                        _Windows_Foundation_Collections.IVectorView[_Windows_Networking.IHostName],  # assignedClientIPv6list
                                        IVpnInterfaceId,  # vpnInterfaceId
                                        IVpnRouteAssignment,  # assignedRoutes
                                        IVpnDomainNameAssignment,  # assignedDomainName
                                        _type.UINT32,  # mtuSize
                                        _type.UINT32,  # maxFrameSize
                                        _type.boolean],  # Reserved
                                       _type.HRESULT]
    add_ActivityStateChange: _Callable[[_Windows_Foundation.ITypedEventHandler[IVpnChannel, IVpnChannelActivityStateChangedArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_ActivityStateChange: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    GetVpnSendPacketBuffer: _Callable[[_Pointer[IVpnPacketBuffer]],  # vpnSendPacketBuffer
                                      _type.HRESULT]
    GetVpnReceivePacketBuffer: _Callable[[_Pointer[IVpnPacketBuffer]],  # vpnReceivePacketBuffer
                                         _type.HRESULT]
    RequestCustomPromptAsync: _Callable[[_Windows_Foundation_Collections.IVectorView[IVpnCustomPromptElement],  # customPromptElement
                                         _Pointer[_Windows_Foundation.IAsyncAction]],  # action
                                        _type.HRESULT]
    RequestCredentialsWithCertificateAsync: _Callable[[_enum.Windows.Networking.Vpn.VpnCredentialType,  # credType
                                                       _type.UINT32,  # credOptions
                                                       _Windows_Security_Cryptography_Certificates.ICertificate,  # certificate
                                                       _Pointer[_Windows_Foundation.IAsyncOperation[IVpnCredential]]],  # credential
                                                      _type.HRESULT]
    RequestCredentialsWithOptionsAsync: _Callable[[_enum.Windows.Networking.Vpn.VpnCredentialType,  # credType
                                                   _type.UINT32,  # credOptions
                                                   _Pointer[_Windows_Foundation.IAsyncOperation[IVpnCredential]]],  # credential
                                                  _type.HRESULT]
    RequestCredentialsSimpleAsync: _Callable[[_enum.Windows.Networking.Vpn.VpnCredentialType,  # credType
                                              _Pointer[_Windows_Foundation.IAsyncOperation[IVpnCredential]]],  # credential
                                             _type.HRESULT]
    TerminateConnection: _Callable[[_type.HSTRING],  # message
                                   _type.HRESULT]
    StartWithTrafficFilter: _Callable[[_Windows_Foundation_Collections.IVectorView[_Windows_Networking.IHostName],  # assignedClientIpv4List
                                       _Windows_Foundation_Collections.IVectorView[_Windows_Networking.IHostName],  # assignedClientIpv6List
                                       IVpnInterfaceId,  # vpnInterfaceId
                                       IVpnRouteAssignment,  # assignedRoutes
                                       IVpnDomainNameAssignment,  # assignedNamespace
                                       _type.UINT32,  # mtuSize
                                       _type.UINT32,  # maxFrameSize
                                       _type.boolean,  # reserved
                                       _inspectable.IInspectable,  # mainOuterTunnelTransport
                                       _inspectable.IInspectable,  # optionalOuterTunnelTransport
                                       IVpnTrafficFilterAssignment],  # assignedTrafficFilters
                                      _type.HRESULT]


class IVpnChannel4(_inspectable.IInspectable):
    AddAndAssociateTransport: _Callable[[_inspectable.IInspectable,  # transport
                                         _inspectable.IInspectable],  # context
                                        _type.HRESULT]
    StartWithMultipleTransports: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Networking.IHostName],  # assignedClientIpv4Addresses
                                            _Windows_Foundation_Collections.IIterable[_Windows_Networking.IHostName],  # assignedClientIpv6Addresses
                                            IVpnInterfaceId,  # vpninterfaceId
                                            IVpnRouteAssignment,  # assignedRoutes
                                            IVpnDomainNameAssignment,  # assignedNamespace
                                            _type.UINT32,  # mtuSize
                                            _type.UINT32,  # maxFrameSize
                                            _type.boolean,  # reserved
                                            _Windows_Foundation_Collections.IIterable[_inspectable.IInspectable],  # transports
                                            IVpnTrafficFilterAssignment],  # assignedTrafficFilters
                                           _type.HRESULT]
    ReplaceAndAssociateTransport: _Callable[[_inspectable.IInspectable,  # transport
                                             _inspectable.IInspectable],  # context
                                            _type.HRESULT]
    StartReconnectingTransport: _Callable[[_inspectable.IInspectable,  # transport
                                           _inspectable.IInspectable],  # context
                                          _type.HRESULT]
    GetSlotTypeForTransportContext: _Callable[[_inspectable.IInspectable,  # context
                                               _Pointer[_enum.Windows.Networking.Sockets.ControlChannelTriggerStatus]],  # slotType
                                              _type.HRESULT]
    get_CurrentRequestTransportContext: _Callable[[_Pointer[_inspectable.IInspectable]],  # context
                                                  _type.HRESULT]


class IVpnChannel5(_inspectable.IInspectable):
    AppendVpnReceivePacketBuffer: _Callable[[IVpnPacketBuffer],  # decapsulatedPacketBuffer
                                            _type.HRESULT]
    AppendVpnSendPacketBuffer: _Callable[[IVpnPacketBuffer],  # encapsulatedPacketBuffer
                                         _type.HRESULT]
    FlushVpnReceivePacketBuffers: _Callable[[],
                                            _type.HRESULT]
    FlushVpnSendPacketBuffers: _Callable[[],
                                         _type.HRESULT]


class IVpnChannel6(_inspectable.IInspectable):
    ActivateForeground: _Callable[[_type.HSTRING,  # packageRelativeAppId
                                   _Windows_Foundation_Collections.IPropertySet,  # sharedContext
                                   _Pointer[_Windows_Foundation_Collections.IPropertySet]],  # result
                                  _type.HRESULT]


class IVpnChannelActivityEventArgs(_inspectable.IInspectable):
    get_Type: _Callable[[_Pointer[_enum.Windows.Networking.Vpn.VpnChannelActivityEventType]],  # value
                        _type.HRESULT]


class IVpnChannelActivityStateChangedArgs(_inspectable.IInspectable):
    get_ActivityState: _Callable[[_Pointer[_enum.Windows.Networking.Vpn.VpnChannelActivityEventType]],  # value
                                 _type.HRESULT]


class IVpnChannelConfiguration(_inspectable.IInspectable):
    get_ServerServiceName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    get_ServerHostNameList: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Networking.IHostName]]],  # value
                                      _type.HRESULT]
    get_CustomField: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class IVpnChannelConfiguration2(_inspectable.IInspectable):
    get_ServerUris: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Foundation.IUriRuntimeClass]]],  # value
                              _type.HRESULT]


class IVpnChannelStatics(_inspectable.IInspectable, factory=True):
    ProcessEventAsync: _Callable[[_inspectable.IInspectable,  # thirdPartyPlugIn
                                  _inspectable.IInspectable],  # @event
                                 _type.HRESULT]


class IVpnCredential(_inspectable.IInspectable):
    get_PasskeyCredential: _Callable[[_Pointer[_Windows_Security_Credentials.IPasswordCredential]],  # value
                                     _type.HRESULT]
    get_CertificateCredential: _Callable[[_Pointer[_Windows_Security_Cryptography_Certificates.ICertificate]],  # value
                                         _type.HRESULT]
    get_AdditionalPin: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_OldPasswordCredential: _Callable[[_Pointer[_Windows_Security_Credentials.IPasswordCredential]],  # value
                                         _type.HRESULT]


class IVpnCustomCheckBox(_inspectable.IInspectable):
    put_InitialCheckState: _Callable[[_type.boolean],  # value
                                     _type.HRESULT]
    get_InitialCheckState: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    get_Checked: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]


class IVpnCustomComboBox(_inspectable.IInspectable):
    put_OptionsText: _Callable[[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_OptionsText: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                               _type.HRESULT]
    get_Selected: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]


class IVpnCustomEditBox(_inspectable.IInspectable):
    put_DefaultText: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_DefaultText: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_NoEcho: _Callable[[_type.boolean],  # value
                          _type.HRESULT]
    get_NoEcho: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class IVpnCustomErrorBox(_inspectable.IInspectable):
    pass


class IVpnCustomPrompt(_inspectable.IInspectable):
    put_Label: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Label: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Compulsory: _Callable[[_type.boolean],  # value
                              _type.HRESULT]
    get_Compulsory: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    put_Bordered: _Callable[[_type.boolean],  # value
                            _type.HRESULT]
    get_Bordered: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]


class IVpnCustomPromptBooleanInput(_inspectable.IInspectable):
    put_InitialValue: _Callable[[_type.boolean],  # value
                                _type.HRESULT]
    get_InitialValue: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.boolean]],  # value
                         _type.HRESULT]


class IVpnCustomPromptElement(_inspectable.IInspectable):
    put_DisplayName: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_Compulsory: _Callable[[_type.boolean],  # value
                              _type.HRESULT]
    get_Compulsory: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    put_Emphasized: _Callable[[_type.boolean],  # value
                              _type.HRESULT]
    get_Emphasized: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]


class IVpnCustomPromptOptionSelector(_inspectable.IInspectable):
    get_Options: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                           _type.HRESULT]
    get_SelectedIndex: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]


class IVpnCustomPromptText(_inspectable.IInspectable):
    put_Text: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class IVpnCustomPromptTextInput(_inspectable.IInspectable):
    put_PlaceholderText: _Callable[[_type.HSTRING],  # value
                                   _type.HRESULT]
    get_PlaceholderText: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    put_IsTextHidden: _Callable[[_type.boolean],  # value
                                _type.HRESULT]
    get_IsTextHidden: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class IVpnCustomTextBox(_inspectable.IInspectable):
    put_DisplayText: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_DisplayText: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class IVpnDomainNameAssignment(_inspectable.IInspectable):
    get_DomainNameList: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IVpnDomainNameInfo]]],  # value
                                  _type.HRESULT]
    put_ProxyAutoConfigurationUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                                             _type.HRESULT]
    get_ProxyAutoConfigurationUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                             _type.HRESULT]


class IVpnDomainNameInfo(_inspectable.IInspectable):
    put_DomainName: _Callable[[_Windows_Networking.IHostName],  # value
                              _type.HRESULT]
    get_DomainName: _Callable[[_Pointer[_Windows_Networking.IHostName]],  # value
                              _type.HRESULT]
    put_DomainNameType: _Callable[[_enum.Windows.Networking.Vpn.VpnDomainNameType],  # value
                                  _type.HRESULT]
    get_DomainNameType: _Callable[[_Pointer[_enum.Windows.Networking.Vpn.VpnDomainNameType]],  # value
                                  _type.HRESULT]
    get_DnsServers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_Networking.IHostName]]],  # value
                              _type.HRESULT]
    get_WebProxyServers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_Networking.IHostName]]],  # value
                                   _type.HRESULT]


class IVpnDomainNameInfo2(_inspectable.IInspectable):
    get_WebProxyUris: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_Foundation.IUriRuntimeClass]]],  # value
                                _type.HRESULT]


class IVpnDomainNameInfoFactory(_inspectable.IInspectable, factory=True):
    CreateVpnDomainNameInfo: _Callable[[_type.HSTRING,  # name
                                        _enum.Windows.Networking.Vpn.VpnDomainNameType,  # nameType
                                        _Windows_Foundation_Collections.IIterable[_Windows_Networking.IHostName],  # dnsServerList
                                        _Windows_Foundation_Collections.IIterable[_Windows_Networking.IHostName],  # proxyServerList
                                        _Pointer[IVpnDomainNameInfo]],  # domainNameInfo
                                       _type.HRESULT]


class IVpnForegroundActivatedEventArgs(_inspectable.IInspectable):
    get_ProfileName: _Callable[[_Pointer[_type.HSTRING]],  # name
                               _type.HRESULT]
    get_SharedContext: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # sharedContext
                                 _type.HRESULT]
    get_ActivationOperation: _Callable[[_Pointer[IVpnForegroundActivationOperation]],  # activationOperation
                                       _type.HRESULT]


class IVpnForegroundActivationOperation(_inspectable.IInspectable):
    Complete: _Callable[[_Windows_Foundation_Collections.IPropertySet],  # result
                        _type.HRESULT]


class IVpnInterfaceId(_inspectable.IInspectable):
    GetAddressInfo: _Callable[[_Pointer[_type.UINT32],  # __idSize
                               _Pointer[_Pointer[_type.BYTE]]],  # id
                              _type.HRESULT]


class IVpnInterfaceIdFactory(_inspectable.IInspectable, factory=True):
    CreateVpnInterfaceId: _Callable[[_type.UINT32,  # __addressSize
                                     _Pointer[_type.BYTE],  # address
                                     _Pointer[IVpnInterfaceId]],  # vpnInterfaceId
                                    _type.HRESULT]


class IVpnManagementAgent(_inspectable.IInspectable):
    AddProfileFromXmlAsync: _Callable[[_type.HSTRING,  # xml
                                       _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Networking.Vpn.VpnManagementErrorStatus]]],  # operation
                                      _type.HRESULT]
    AddProfileFromObjectAsync: _Callable[[IVpnProfile,  # profile
                                          _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Networking.Vpn.VpnManagementErrorStatus]]],  # operation
                                         _type.HRESULT]
    UpdateProfileFromXmlAsync: _Callable[[_type.HSTRING,  # xml
                                          _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Networking.Vpn.VpnManagementErrorStatus]]],  # operation
                                         _type.HRESULT]
    UpdateProfileFromObjectAsync: _Callable[[IVpnProfile,  # profile
                                             _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Networking.Vpn.VpnManagementErrorStatus]]],  # operation
                                            _type.HRESULT]
    GetProfilesAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IVpnProfile]]]],  # operation
                                _type.HRESULT]
    DeleteProfileAsync: _Callable[[IVpnProfile,  # profile
                                   _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Networking.Vpn.VpnManagementErrorStatus]]],  # operation
                                  _type.HRESULT]
    ConnectProfileAsync: _Callable[[IVpnProfile,  # profile
                                    _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Networking.Vpn.VpnManagementErrorStatus]]],  # operation
                                   _type.HRESULT]
    ConnectProfileWithPasswordCredentialAsync: _Callable[[IVpnProfile,  # profile
                                                          _Windows_Security_Credentials.IPasswordCredential,  # passwordCredential
                                                          _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Networking.Vpn.VpnManagementErrorStatus]]],  # operation
                                                         _type.HRESULT]
    DisconnectProfileAsync: _Callable[[IVpnProfile,  # profile
                                       _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Networking.Vpn.VpnManagementErrorStatus]]],  # operation
                                      _type.HRESULT]


class IVpnNamespaceAssignment(_inspectable.IInspectable):
    put_NamespaceList: _Callable[[_Windows_Foundation_Collections.IVector[IVpnNamespaceInfo]],  # value
                                 _type.HRESULT]
    get_NamespaceList: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IVpnNamespaceInfo]]],  # value
                                 _type.HRESULT]
    put_ProxyAutoConfigUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                                      _type.HRESULT]
    get_ProxyAutoConfigUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                      _type.HRESULT]


class IVpnNamespaceInfo(_inspectable.IInspectable):
    put_Namespace: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_Namespace: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_DnsServers: _Callable[[_Windows_Foundation_Collections.IVector[_Windows_Networking.IHostName]],  # value
                              _type.HRESULT]
    get_DnsServers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_Networking.IHostName]]],  # value
                              _type.HRESULT]
    put_WebProxyServers: _Callable[[_Windows_Foundation_Collections.IVector[_Windows_Networking.IHostName]],  # value
                                   _type.HRESULT]
    get_WebProxyServers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_Networking.IHostName]]],  # value
                                   _type.HRESULT]


class IVpnNamespaceInfoFactory(_inspectable.IInspectable, factory=True):
    CreateVpnNamespaceInfo: _Callable[[_type.HSTRING,  # name
                                       _Windows_Foundation_Collections.IVector[_Windows_Networking.IHostName],  # dnsServerList
                                       _Windows_Foundation_Collections.IVector[_Windows_Networking.IHostName],  # proxyServerList
                                       _Pointer[IVpnNamespaceInfo]],  # namespaceInfo
                                      _type.HRESULT]


class IVpnNativeProfile(_inspectable.IInspectable):
    get_Servers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                           _type.HRESULT]
    get_RoutingPolicyType: _Callable[[_Pointer[_enum.Windows.Networking.Vpn.VpnRoutingPolicyType]],  # value
                                     _type.HRESULT]
    put_RoutingPolicyType: _Callable[[_enum.Windows.Networking.Vpn.VpnRoutingPolicyType],  # value
                                     _type.HRESULT]
    get_NativeProtocolType: _Callable[[_Pointer[_enum.Windows.Networking.Vpn.VpnNativeProtocolType]],  # value
                                      _type.HRESULT]
    put_NativeProtocolType: _Callable[[_enum.Windows.Networking.Vpn.VpnNativeProtocolType],  # value
                                      _type.HRESULT]
    get_UserAuthenticationMethod: _Callable[[_Pointer[_enum.Windows.Networking.Vpn.VpnAuthenticationMethod]],  # value
                                            _type.HRESULT]
    put_UserAuthenticationMethod: _Callable[[_enum.Windows.Networking.Vpn.VpnAuthenticationMethod],  # value
                                            _type.HRESULT]
    get_TunnelAuthenticationMethod: _Callable[[_Pointer[_enum.Windows.Networking.Vpn.VpnAuthenticationMethod]],  # value
                                              _type.HRESULT]
    put_TunnelAuthenticationMethod: _Callable[[_enum.Windows.Networking.Vpn.VpnAuthenticationMethod],  # value
                                              _type.HRESULT]
    get_EapConfiguration: _Callable[[_Pointer[_type.HSTRING]],  # Value
                                    _type.HRESULT]
    put_EapConfiguration: _Callable[[_type.HSTRING],  # value
                                    _type.HRESULT]


class IVpnNativeProfile2(_inspectable.IInspectable):
    get_RequireVpnClientAppUI: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_RequireVpnClientAppUI: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]
    get_ConnectionStatus: _Callable[[_Pointer[_enum.Windows.Networking.Vpn.VpnManagementConnectionStatus]],  # value
                                    _type.HRESULT]


class IVpnPacketBuffer(_inspectable.IInspectable):
    get_Buffer: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                          _type.HRESULT]
    put_Status: _Callable[[_enum.Windows.Networking.Vpn.VpnPacketBufferStatus],  # value
                          _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.Networking.Vpn.VpnPacketBufferStatus]],  # value
                          _type.HRESULT]
    put_TransportAffinity: _Callable[[_type.UINT32],  # value
                                     _type.HRESULT]
    get_TransportAffinity: _Callable[[_Pointer[_type.UINT32]],  # value
                                     _type.HRESULT]


class IVpnPacketBuffer2(_inspectable.IInspectable):
    get_AppId: _Callable[[_Pointer[IVpnAppId]],  # value
                         _type.HRESULT]


class IVpnPacketBuffer3(_inspectable.IInspectable):
    put_TransportContext: _Callable[[_inspectable.IInspectable],  # value
                                    _type.HRESULT]
    get_TransportContext: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                    _type.HRESULT]


class IVpnPacketBufferFactory(_inspectable.IInspectable, factory=True):
    CreateVpnPacketBuffer: _Callable[[IVpnPacketBuffer,  # parentBuffer
                                      _type.UINT32,  # offset
                                      _type.UINT32,  # length
                                      _Pointer[IVpnPacketBuffer]],  # vpnPacketBuffer
                                     _type.HRESULT]


class IVpnPacketBufferList(_inspectable.IInspectable):
    Append: _Callable[[IVpnPacketBuffer],  # nextVpnPacketBuffer
                      _type.HRESULT]
    AddAtBegin: _Callable[[IVpnPacketBuffer],  # nextVpnPacketBuffer
                          _type.HRESULT]
    RemoveAtEnd: _Callable[[_Pointer[IVpnPacketBuffer]],  # nextVpnPacketBuffer
                           _type.HRESULT]
    RemoveAtBegin: _Callable[[_Pointer[IVpnPacketBuffer]],  # nextVpnPacketBuffer
                             _type.HRESULT]
    Clear: _Callable[[],
                     _type.HRESULT]
    put_Status: _Callable[[_enum.Windows.Networking.Vpn.VpnPacketBufferStatus],  # value
                          _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.Networking.Vpn.VpnPacketBufferStatus]],  # value
                          _type.HRESULT]
    get_Size: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]


class IVpnPacketBufferList2(_inspectable.IInspectable):
    AddLeadingPacket: _Callable[[IVpnPacketBuffer],  # nextVpnPacketBuffer
                                _type.HRESULT]
    RemoveLeadingPacket: _Callable[[_Pointer[IVpnPacketBuffer]],  # nextVpnPacketBuffer
                                   _type.HRESULT]
    AddTrailingPacket: _Callable[[IVpnPacketBuffer],  # nextVpnPacketBuffer
                                 _type.HRESULT]
    RemoveTrailingPacket: _Callable[[_Pointer[IVpnPacketBuffer]],  # nextVpnPacketBuffer
                                    _type.HRESULT]


class IVpnPickedCredential(_inspectable.IInspectable):
    get_PasskeyCredential: _Callable[[_Pointer[_Windows_Security_Credentials.IPasswordCredential]],  # value
                                     _type.HRESULT]
    get_AdditionalPin: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_OldPasswordCredential: _Callable[[_Pointer[_Windows_Security_Credentials.IPasswordCredential]],  # value
                                         _type.HRESULT]


class IVpnPlugIn(_inspectable.IInspectable):
    Connect: _Callable[[IVpnChannel],  # channel
                       _type.HRESULT]
    Disconnect: _Callable[[IVpnChannel],  # channel
                          _type.HRESULT]
    GetKeepAlivePayload: _Callable[[IVpnChannel,  # channel
                                    _Pointer[IVpnPacketBuffer]],  # keepAlivePacket
                                   _type.HRESULT]
    Encapsulate: _Callable[[IVpnChannel,  # channel
                            IVpnPacketBufferList,  # packets
                            IVpnPacketBufferList],  # encapulatedPackets
                           _type.HRESULT]
    Decapsulate: _Callable[[IVpnChannel,  # channel
                            IVpnPacketBuffer,  # encapBuffer
                            IVpnPacketBufferList,  # decapsulatedPackets
                            IVpnPacketBufferList],  # controlPacketsToSend
                           _type.HRESULT]


class IVpnPlugInProfile(_inspectable.IInspectable):
    get_ServerUris: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_Foundation.IUriRuntimeClass]]],  # value
                              _type.HRESULT]
    get_CustomConfiguration: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    put_CustomConfiguration: _Callable[[_type.HSTRING],  # value
                                       _type.HRESULT]
    get_VpnPluginPackageFamilyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                              _type.HRESULT]
    put_VpnPluginPackageFamilyName: _Callable[[_type.HSTRING],  # value
                                              _type.HRESULT]


class IVpnPlugInProfile2(_inspectable.IInspectable):
    get_RequireVpnClientAppUI: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_RequireVpnClientAppUI: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]
    get_ConnectionStatus: _Callable[[_Pointer[_enum.Windows.Networking.Vpn.VpnManagementConnectionStatus]],  # value
                                    _type.HRESULT]


class IVpnProfile(_inspectable.IInspectable):
    get_ProfileName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_ProfileName: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_AppTriggers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IVpnAppId]]],  # value
                               _type.HRESULT]
    get_Routes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IVpnRoute]]],  # value
                          _type.HRESULT]
    get_DomainNameInfoList: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IVpnDomainNameInfo]]],  # value
                                      _type.HRESULT]
    get_TrafficFilters: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IVpnTrafficFilter]]],  # value
                                  _type.HRESULT]
    get_RememberCredentials: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_RememberCredentials: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_AlwaysOn: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    put_AlwaysOn: _Callable[[_type.boolean],  # value
                            _type.HRESULT]


class IVpnRoute(_inspectable.IInspectable):
    put_Address: _Callable[[_Windows_Networking.IHostName],  # value
                           _type.HRESULT]
    get_Address: _Callable[[_Pointer[_Windows_Networking.IHostName]],  # value
                           _type.HRESULT]
    put_PrefixSize: _Callable[[_type.BYTE],  # value
                              _type.HRESULT]
    get_PrefixSize: _Callable[[_Pointer[_type.BYTE]],  # value
                              _type.HRESULT]


class IVpnRouteAssignment(_inspectable.IInspectable):
    put_Ipv4InclusionRoutes: _Callable[[_Windows_Foundation_Collections.IVector[IVpnRoute]],  # value
                                       _type.HRESULT]
    put_Ipv6InclusionRoutes: _Callable[[_Windows_Foundation_Collections.IVector[IVpnRoute]],  # value
                                       _type.HRESULT]
    get_Ipv4InclusionRoutes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IVpnRoute]]],  # value
                                       _type.HRESULT]
    get_Ipv6InclusionRoutes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IVpnRoute]]],  # value
                                       _type.HRESULT]
    put_Ipv4ExclusionRoutes: _Callable[[_Windows_Foundation_Collections.IVector[IVpnRoute]],  # value
                                       _type.HRESULT]
    put_Ipv6ExclusionRoutes: _Callable[[_Windows_Foundation_Collections.IVector[IVpnRoute]],  # value
                                       _type.HRESULT]
    get_Ipv4ExclusionRoutes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IVpnRoute]]],  # value
                                       _type.HRESULT]
    get_Ipv6ExclusionRoutes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IVpnRoute]]],  # value
                                       _type.HRESULT]
    put_ExcludeLocalSubnets: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_ExcludeLocalSubnets: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]


class IVpnRouteFactory(_inspectable.IInspectable, factory=True):
    CreateVpnRoute: _Callable[[_Windows_Networking.IHostName,  # address
                               _type.BYTE,  # prefixSize
                               _Pointer[IVpnRoute]],  # route
                              _type.HRESULT]


class IVpnSystemHealth(_inspectable.IInspectable):
    get_StatementOfHealth: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                     _type.HRESULT]


class IVpnTrafficFilter(_inspectable.IInspectable):
    get_AppId: _Callable[[_Pointer[IVpnAppId]],  # value
                         _type.HRESULT]
    put_AppId: _Callable[[IVpnAppId],  # value
                         _type.HRESULT]
    get_AppClaims: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                             _type.HRESULT]
    get_Protocol: _Callable[[_Pointer[_enum.Windows.Networking.Vpn.VpnIPProtocol]],  # value
                            _type.HRESULT]
    put_Protocol: _Callable[[_enum.Windows.Networking.Vpn.VpnIPProtocol],  # value
                            _type.HRESULT]
    get_LocalPortRanges: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                   _type.HRESULT]
    get_RemotePortRanges: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                    _type.HRESULT]
    get_LocalAddressRanges: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                      _type.HRESULT]
    get_RemoteAddressRanges: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                       _type.HRESULT]
    get_RoutingPolicyType: _Callable[[_Pointer[_enum.Windows.Networking.Vpn.VpnRoutingPolicyType]],  # value
                                     _type.HRESULT]
    put_RoutingPolicyType: _Callable[[_enum.Windows.Networking.Vpn.VpnRoutingPolicyType],  # value
                                     _type.HRESULT]


class IVpnTrafficFilterAssignment(_inspectable.IInspectable):
    get_TrafficFilterList: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IVpnTrafficFilter]]],  # value
                                     _type.HRESULT]
    get_AllowOutbound: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_AllowOutbound: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_AllowInbound: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_AllowInbound: _Callable[[_type.boolean],  # value
                                _type.HRESULT]


class IVpnTrafficFilterFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[IVpnAppId,  # appId
                       _Pointer[IVpnTrafficFilter]],  # result
                      _type.HRESULT]
