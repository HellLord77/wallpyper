from __future__ import annotations

from typing import Callable as _Callable

from .. import Enumeration as _Windows_Devices_Enumeration
from ... import Foundation as _Windows_Foundation
from ... import Globalization as _Windows_Globalization
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Security import Credentials as _Windows_Security_Credentials
from ...Security.Cryptography import Certificates as _Windows_Security_Cryptography_Certificates
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IAllJoynAboutData(_inspectable.IInspectable):
    IsEnabled: _Callable[[_type.boolean],  # value
                         _type.HRESULT]
    DefaultAppName: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]
    AppNames: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, _type.HSTRING]]],  # value
                        _type.HRESULT]
    DateOfManufacture: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                                 _type.HRESULT]
    DefaultDescription: _Callable[[_type.HSTRING],  # value
                                  _type.HRESULT]
    Descriptions: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, _type.HSTRING]]],  # value
                            _type.HRESULT]
    DefaultManufacturer: _Callable[[_type.HSTRING],  # value
                                   _type.HRESULT]
    Manufacturers: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, _type.HSTRING]]],  # value
                             _type.HRESULT]
    ModelNumber: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    SoftwareVersion: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    SupportUrl: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                          _type.HRESULT]
    AppId: _Callable[[_struct.GUID],  # value
                     _type.HRESULT]


class IAllJoynAboutDataView(_inspectable.IInspectable):
    Status: _Callable[[_Pointer[_type.INT32]],  # value
                      _type.HRESULT]
    Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _inspectable.IInspectable]]],  # value
                          _type.HRESULT]
    AJSoftwareVersion: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    AppId: _Callable[[_Pointer[_struct.GUID]],  # value
                     _type.HRESULT]
    DateOfManufacture: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                 _type.HRESULT]
    DefaultLanguage: _Callable[[_Pointer[_Windows_Globalization.ILanguage]],  # value
                               _type.HRESULT]
    DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    HardwareVersion: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    ModelNumber: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    SoftwareVersion: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    SupportedLanguages: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Globalization.ILanguage]]],  # value
                                  _type.HRESULT]
    SupportUrl: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                          _type.HRESULT]
    AppName: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    DeviceName: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    Manufacturer: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]


class IAllJoynAboutDataViewStatics(_inspectable.IInspectable, factory=True):
    GetDataBySessionPortAsync: _Callable[[_type.HSTRING,  # uniqueName
                                          IAllJoynBusAttachment,  # busAttachment
                                          _type.UINT16,  # sessionPort
                                          _Pointer[_Windows_Foundation.IAsyncOperation[IAllJoynAboutDataView]]],  # operation
                                         _type.HRESULT]
    GetDataBySessionPortWithLanguageAsync: _Callable[[_type.HSTRING,  # uniqueName
                                                      IAllJoynBusAttachment,  # busAttachment
                                                      _type.UINT16,  # sessionPort
                                                      _Windows_Globalization.ILanguage,  # language
                                                      _Pointer[_Windows_Foundation.IAsyncOperation[IAllJoynAboutDataView]]],  # operation
                                                     _type.HRESULT]


class IAllJoynAcceptSessionJoiner(_inspectable.IInspectable):
    Accept: _Callable[[],
                      _type.HRESULT]


class IAllJoynAcceptSessionJoinerEventArgs(_inspectable.IInspectable):
    UniqueName: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    SessionPort: _Callable[[_Pointer[_type.UINT16]],  # value
                           _type.HRESULT]
    TrafficType: _Callable[[_Pointer[_enum.Windows.Devices.AllJoyn.AllJoynTrafficType]],  # value
                           _type.HRESULT]
    SamePhysicalNode: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    SameNetwork: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    Accept: _Callable[[],
                      _type.HRESULT]


class IAllJoynAcceptSessionJoinerEventArgsFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.HSTRING,  # uniqueName
                       _type.UINT16,  # sessionPort
                       _enum.Windows.Devices.AllJoyn.AllJoynTrafficType,  # trafficType
                       _type.BYTE,  # proximity
                       IAllJoynAcceptSessionJoiner,  # acceptSessionJoiner
                       _Pointer[IAllJoynAcceptSessionJoinerEventArgs]],  # result
                      _type.HRESULT]


class IAllJoynAuthenticationCompleteEventArgs(_inspectable.IInspectable):
    AuthenticationMechanism: _Callable[[_Pointer[_enum.Windows.Devices.AllJoyn.AllJoynAuthenticationMechanism]],  # value
                                       _type.HRESULT]
    PeerUniqueName: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    Succeeded: _Callable[[_Pointer[_type.boolean]],  # value
                         _type.HRESULT]


class IAllJoynBusAttachment(_inspectable.IInspectable):
    AboutData: _Callable[[_Pointer[IAllJoynAboutData]],  # value
                         _type.HRESULT]
    ConnectionSpecification: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    State: _Callable[[_Pointer[_enum.Windows.Devices.AllJoyn.AllJoynBusAttachmentState]],  # value
                     _type.HRESULT]
    UniqueName: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    PingAsync: _Callable[[_type.HSTRING,  # uniqueName
                          _Pointer[_Windows_Foundation.IAsyncOperation[_type.INT32]]],  # operation
                         _type.HRESULT]
    Connect: _Callable[[],
                       _type.HRESULT]
    Disconnect: _Callable[[],
                          _type.HRESULT]
    StateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                            _type.HRESULT]
    AuthenticationMechanisms: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_enum.Windows.Devices.AllJoyn.AllJoynAuthenticationMechanism]]],  # value
                                        _type.HRESULT]
    CredentialsRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    CredentialsVerificationRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                _type.HRESULT]
    AuthenticationComplete: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]


class IAllJoynBusAttachment2(_inspectable.IInspectable):
    GetAboutDataAsync: _Callable[[IAllJoynServiceInfo,  # serviceInfo
                                  _Pointer[_Windows_Foundation.IAsyncOperation[IAllJoynAboutDataView]]],  # operation
                                 _type.HRESULT]
    GetAboutDataWithLanguageAsync: _Callable[[IAllJoynServiceInfo,  # serviceInfo
                                              _Windows_Globalization.ILanguage,  # language
                                              _Pointer[_Windows_Foundation.IAsyncOperation[IAllJoynAboutDataView]]],  # operation
                                             _type.HRESULT]
    AcceptSessionJoinerRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]
    SessionJoined: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]


class IAllJoynBusAttachmentFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.HSTRING,  # connectionSpecification
                       _Pointer[IAllJoynBusAttachment]],  # result
                      _type.HRESULT]


class IAllJoynBusAttachmentStateChangedEventArgs(_inspectable.IInspectable):
    State: _Callable[[_Pointer[_enum.Windows.Devices.AllJoyn.AllJoynBusAttachmentState]],  # value
                     _type.HRESULT]
    Status: _Callable[[_Pointer[_type.INT32]],  # value
                      _type.HRESULT]


class IAllJoynBusAttachmentStatics(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[IAllJoynBusAttachment]],  # defaultBusAttachment
                          _type.HRESULT]
    GetWatcher: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # requiredInterfaces
                           _Pointer[_Windows_Devices_Enumeration.IDeviceWatcher]],  # deviceWatcher
                          _type.HRESULT]


class IAllJoynBusObject(_inspectable.IInspectable):
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    AddProducer: _Callable[[IAllJoynProducer],  # producer
                           _type.HRESULT]
    BusAttachment: _Callable[[_Pointer[IAllJoynBusAttachment]],  # value
                             _type.HRESULT]
    Session: _Callable[[_Pointer[IAllJoynSession]],  # value
                       _type.HRESULT]
    Stopped: _Callable[[_struct.EventRegistrationToken],  # token
                       _type.HRESULT]


class IAllJoynBusObjectFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.HSTRING,  # objectPath
                       _Pointer[IAllJoynBusObject]],  # result
                      _type.HRESULT]
    CreateWithBusAttachment: _Callable[[_type.HSTRING,  # objectPath
                                        IAllJoynBusAttachment,  # busAttachment
                                        _Pointer[IAllJoynBusObject]],  # result
                                       _type.HRESULT]


class IAllJoynBusObjectStoppedEventArgs(_inspectable.IInspectable):
    Status: _Callable[[_Pointer[_type.INT32]],  # value
                      _type.HRESULT]


class IAllJoynBusObjectStoppedEventArgsFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.INT32,  # status
                       _Pointer[IAllJoynBusObjectStoppedEventArgs]],  # result
                      _type.HRESULT]


class IAllJoynCredentials(_inspectable.IInspectable):
    AuthenticationMechanism: _Callable[[_Pointer[_enum.Windows.Devices.AllJoyn.AllJoynAuthenticationMechanism]],  # value
                                       _type.HRESULT]
    Certificate: _Callable[[_Windows_Security_Cryptography_Certificates.ICertificate],  # value
                           _type.HRESULT]
    PasswordCredential: _Callable[[_Windows_Security_Credentials.IPasswordCredential],  # value
                                  _type.HRESULT]
    Timeout: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                       _type.HRESULT]


class IAllJoynCredentialsRequestedEventArgs(_inspectable.IInspectable):
    AttemptCount: _Callable[[_Pointer[_type.UINT16]],  # value
                            _type.HRESULT]
    Credentials: _Callable[[_Pointer[IAllJoynCredentials]],  # value
                           _type.HRESULT]
    PeerUniqueName: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    RequestedUserName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IAllJoynCredentialsVerificationRequestedEventArgs(_inspectable.IInspectable):
    AuthenticationMechanism: _Callable[[_Pointer[_enum.Windows.Devices.AllJoyn.AllJoynAuthenticationMechanism]],  # value
                                       _type.HRESULT]
    PeerUniqueName: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    PeerCertificate: _Callable[[_Pointer[_Windows_Security_Cryptography_Certificates.ICertificate]],  # value
                               _type.HRESULT]
    PeerCertificateErrorSeverity: _Callable[[_Pointer[_enum.Windows.Networking.Sockets.SocketSslErrorSeverity]],  # value
                                            _type.HRESULT]
    PeerCertificateErrors: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Security.Cryptography.Certificates.ChainValidationResult]]],  # value
                                     _type.HRESULT]
    PeerIntermediateCertificates: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Security_Cryptography_Certificates.ICertificate]]],  # value
                                            _type.HRESULT]
    Accept: _Callable[[],
                      _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IAllJoynMessageInfo(_inspectable.IInspectable):
    SenderUniqueName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]


class IAllJoynMessageInfoFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.HSTRING,  # senderUniqueName
                       _Pointer[IAllJoynMessageInfo]],  # result
                      _type.HRESULT]


class IAllJoynProducer(_inspectable.IInspectable):
    SetBusObject: _Callable[[IAllJoynBusObject],  # busObject
                            _type.HRESULT]


class IAllJoynProducerStoppedEventArgs(_inspectable.IInspectable):
    Status: _Callable[[_Pointer[_type.INT32]],  # value
                      _type.HRESULT]


class IAllJoynProducerStoppedEventArgsFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.INT32,  # status
                       _Pointer[IAllJoynProducerStoppedEventArgs]],  # result
                      _type.HRESULT]


class IAllJoynServiceInfo(_inspectable.IInspectable):
    UniqueName: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    ObjectPath: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    SessionPort: _Callable[[_Pointer[_type.UINT16]],  # value
                           _type.HRESULT]


class IAllJoynServiceInfoFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.HSTRING,  # uniqueName
                       _type.HSTRING,  # objectPath
                       _type.UINT16,  # sessionPort
                       _Pointer[IAllJoynServiceInfo]],  # result
                      _type.HRESULT]


class IAllJoynServiceInfoRemovedEventArgs(_inspectable.IInspectable):
    UniqueName: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]


class IAllJoynServiceInfoRemovedEventArgsFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.HSTRING,  # uniqueName
                       _Pointer[IAllJoynServiceInfoRemovedEventArgs]],  # result
                      _type.HRESULT]


class IAllJoynServiceInfoStatics(_inspectable.IInspectable, factory=True):
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IAllJoynServiceInfo]]],  # operation
                           _type.HRESULT]


class IAllJoynSession(_inspectable.IInspectable):
    Id: _Callable[[_Pointer[_type.INT32]],  # value
                  _type.HRESULT]
    Status: _Callable[[_Pointer[_type.INT32]],  # value
                      _type.HRESULT]
    RemoveMemberAsync: _Callable[[_type.HSTRING,  # uniqueName
                                  _Pointer[_Windows_Foundation.IAsyncOperation[_type.INT32]]],  # operation
                                 _type.HRESULT]
    MemberAdded: _Callable[[_struct.EventRegistrationToken],  # token
                           _type.HRESULT]
    MemberRemoved: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    Lost: _Callable[[_struct.EventRegistrationToken],  # token
                    _type.HRESULT]


class IAllJoynSessionJoinedEventArgs(_inspectable.IInspectable):
    Session: _Callable[[_Pointer[IAllJoynSession]],  # value
                       _type.HRESULT]


class IAllJoynSessionJoinedEventArgsFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[IAllJoynSession,  # session
                       _Pointer[IAllJoynSessionJoinedEventArgs]],  # result
                      _type.HRESULT]


class IAllJoynSessionLostEventArgs(_inspectable.IInspectable):
    Reason: _Callable[[_Pointer[_enum.Windows.Devices.AllJoyn.AllJoynSessionLostReason]],  # value
                      _type.HRESULT]


class IAllJoynSessionLostEventArgsFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_enum.Windows.Devices.AllJoyn.AllJoynSessionLostReason,  # reason
                       _Pointer[IAllJoynSessionLostEventArgs]],  # result
                      _type.HRESULT]


class IAllJoynSessionMemberAddedEventArgs(_inspectable.IInspectable):
    UniqueName: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]


class IAllJoynSessionMemberAddedEventArgsFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.HSTRING,  # uniqueName
                       _Pointer[IAllJoynSessionMemberAddedEventArgs]],  # result
                      _type.HRESULT]


class IAllJoynSessionMemberRemovedEventArgs(_inspectable.IInspectable):
    UniqueName: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]


class IAllJoynSessionMemberRemovedEventArgsFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.HSTRING,  # uniqueName
                       _Pointer[IAllJoynSessionMemberRemovedEventArgs]],  # result
                      _type.HRESULT]


class IAllJoynSessionStatics(_inspectable.IInspectable, factory=True):
    GetFromServiceInfoAsync: _Callable[[IAllJoynServiceInfo,  # serviceInfo
                                        _Pointer[_Windows_Foundation.IAsyncOperation[IAllJoynSession]]],  # operation
                                       _type.HRESULT]
    GetFromServiceInfoAndBusAttachmentAsync: _Callable[[IAllJoynServiceInfo,  # serviceInfo
                                                        IAllJoynBusAttachment,  # busAttachment
                                                        _Pointer[_Windows_Foundation.IAsyncOperation[IAllJoynSession]]],  # operation
                                                       _type.HRESULT]


class IAllJoynStatusStatics(_inspectable.IInspectable, factory=True):
    Ok: _Callable[[_Pointer[_type.INT32]],  # value
                  _type.HRESULT]
    Fail: _Callable[[_Pointer[_type.INT32]],  # value
                    _type.HRESULT]
    OperationTimedOut: _Callable[[_Pointer[_type.INT32]],  # value
                                 _type.HRESULT]
    OtherEndClosed: _Callable[[_Pointer[_type.INT32]],  # value
                              _type.HRESULT]
    ConnectionRefused: _Callable[[_Pointer[_type.INT32]],  # value
                                 _type.HRESULT]
    AuthenticationFailed: _Callable[[_Pointer[_type.INT32]],  # value
                                    _type.HRESULT]
    AuthenticationRejectedByUser: _Callable[[_Pointer[_type.INT32]],  # value
                                            _type.HRESULT]
    SslConnectFailed: _Callable[[_Pointer[_type.INT32]],  # value
                                _type.HRESULT]
    SslIdentityVerificationFailed: _Callable[[_Pointer[_type.INT32]],  # value
                                             _type.HRESULT]
    InsufficientSecurity: _Callable[[_Pointer[_type.INT32]],  # value
                                    _type.HRESULT]
    InvalidArgument1: _Callable[[_Pointer[_type.INT32]],  # value
                                _type.HRESULT]
    InvalidArgument2: _Callable[[_Pointer[_type.INT32]],  # value
                                _type.HRESULT]
    InvalidArgument3: _Callable[[_Pointer[_type.INT32]],  # value
                                _type.HRESULT]
    InvalidArgument4: _Callable[[_Pointer[_type.INT32]],  # value
                                _type.HRESULT]
    InvalidArgument5: _Callable[[_Pointer[_type.INT32]],  # value
                                _type.HRESULT]
    InvalidArgument6: _Callable[[_Pointer[_type.INT32]],  # value
                                _type.HRESULT]
    InvalidArgument7: _Callable[[_Pointer[_type.INT32]],  # value
                                _type.HRESULT]
    InvalidArgument8: _Callable[[_Pointer[_type.INT32]],  # value
                                _type.HRESULT]


class IAllJoynWatcherStoppedEventArgs(_inspectable.IInspectable):
    Status: _Callable[[_Pointer[_type.INT32]],  # value
                      _type.HRESULT]


class IAllJoynWatcherStoppedEventArgsFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.INT32,  # status
                       _Pointer[IAllJoynWatcherStoppedEventArgs]],  # result
                      _type.HRESULT]
