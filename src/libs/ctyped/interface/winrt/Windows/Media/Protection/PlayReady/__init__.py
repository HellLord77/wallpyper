from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Core as _Windows_Media_Core
from ... import Protection as _Windows_Media_Protection
from .... import Foundation as _Windows_Foundation
from .... import Storage as _Windows_Storage
from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class INDClient(_inspectable.IInspectable):
    RegistrationCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    ProximityDetectionCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    LicenseFetchCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    ReRegistrationNeeded: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    ClosedCaptionDataReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    StartAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # contentUrl
                           _type.UINT32,  # startAsyncOptions
                           INDCustomData,  # registrationCustomData
                           INDLicenseFetchDescriptor,  # licenseFetchDescriptor
                           _Pointer[_Windows_Foundation.IAsyncOperation[INDStartResult]]],  # result
                          _type.HRESULT]
    LicenseFetchAsync: _Callable[[INDLicenseFetchDescriptor,  # licenseFetchDescriptor
                                  _Pointer[_Windows_Foundation.IAsyncOperation[INDLicenseFetchResult]]],  # result
                                 _type.HRESULT]
    ReRegistrationAsync: _Callable[[INDCustomData,  # registrationCustomData
                                    _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                   _type.HRESULT]
    Close: _Callable[[],
                     _type.HRESULT]


class INDClientFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[INDDownloadEngine,  # downloadEngine
                               INDStreamParser,  # streamParser
                               INDMessenger,  # pMessenger
                               _Pointer[INDClient]],  # instance
                              _type.HRESULT]

    _factory = True


class INDClosedCaptionDataReceivedEventArgs(_inspectable.IInspectable):
    ClosedCaptionDataFormat: _Callable[[_Pointer[_enum.Windows.Media.Protection.PlayReady.NDClosedCaptionFormat]],  # ccForamt
                                       _type.HRESULT]
    PresentationTimestamp: _Callable[[_Pointer[_type.INT64]],  # presentationTimestamp
                                     _type.HRESULT]
    ClosedCaptionData: _Callable[[_Pointer[_type.UINT32],  # __ccDataBytesSize
                                  _Pointer[_Pointer[_type.BYTE]]],  # ccDataBytes
                                 _type.HRESULT]


class INDCustomData(_inspectable.IInspectable):
    CustomDataTypeID: _Callable[[_Pointer[_type.UINT32],  # __customDataTypeIDBytesSize
                                 _Pointer[_Pointer[_type.BYTE]]],  # customDataTypeIDBytes
                                _type.HRESULT]
    CustomData: _Callable[[_Pointer[_type.UINT32],  # __customDataBytesSize
                           _Pointer[_Pointer[_type.BYTE]]],  # customDataBytes
                          _type.HRESULT]


class INDCustomDataFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_type.UINT32,  # __customDataTypeIDBytesSize
                               _Pointer[_type.BYTE],  # customDataTypeIDBytes
                               _type.UINT32,  # __customDataBytesSize
                               _Pointer[_type.BYTE],  # customDataBytes
                               _Pointer[INDCustomData]],  # instance
                              _type.HRESULT]

    _factory = True


class INDDownloadEngine(_inspectable.IInspectable):
    Open: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                     _type.UINT32,  # __sessionIDBytesSize
                     _Pointer[_type.BYTE]],  # sessionIDBytes
                    _type.HRESULT]
    Pause: _Callable[[],
                     _type.HRESULT]
    Resume: _Callable[[],
                      _type.HRESULT]
    Close: _Callable[[],
                     _type.HRESULT]
    Seek: _Callable[[_struct.Windows.Foundation.TimeSpan],  # startPosition
                    _type.HRESULT]
    CanSeek: _Callable[[_Pointer[_type.boolean]],  # canSeek
                       _type.HRESULT]
    BufferFullMinThresholdInSamples: _Callable[[_Pointer[_type.UINT32]],  # bufferFullMinThreshold
                                               _type.HRESULT]
    BufferFullMaxThresholdInSamples: _Callable[[_Pointer[_type.UINT32]],  # bufferFullMaxThreshold
                                               _type.HRESULT]
    Notifier: _Callable[[_Pointer[INDDownloadEngineNotifier]],  # instance
                        _type.HRESULT]


class INDDownloadEngineNotifier(_inspectable.IInspectable):
    OnStreamOpened: _Callable[[],
                              _type.HRESULT]
    OnPlayReadyObjectReceived: _Callable[[_type.UINT32,  # __dataBytesSize
                                          _Pointer[_type.BYTE]],  # dataBytes
                                         _type.HRESULT]
    OnContentIDReceived: _Callable[[INDLicenseFetchDescriptor],  # licenseFetchDescriptor
                                   _type.HRESULT]
    OnDataReceived: _Callable[[_type.UINT32,  # __dataBytesSize
                               _Pointer[_type.BYTE],  # dataBytes
                               _type.UINT32],  # bytesReceived
                              _type.HRESULT]
    OnEndOfStream: _Callable[[],
                             _type.HRESULT]
    OnNetworkError: _Callable[[],
                              _type.HRESULT]


class INDLicenseFetchCompletedEventArgs(_inspectable.IInspectable):
    ResponseCustomData: _Callable[[_Pointer[INDCustomData]],  # customData
                                  _type.HRESULT]


class INDLicenseFetchDescriptor(_inspectable.IInspectable):
    ContentIDType: _Callable[[_Pointer[_enum.Windows.Media.Protection.PlayReady.NDContentIDType]],  # contentIDType
                             _type.HRESULT]
    ContentID: _Callable[[_Pointer[_type.UINT32],  # __contentIDBytesSize
                          _Pointer[_Pointer[_type.BYTE]]],  # contentIDBytes
                         _type.HRESULT]
    LicenseFetchChallengeCustomData: _Callable[[INDCustomData],  # licenseFetchChallengeCustomData
                                               _type.HRESULT]


class INDLicenseFetchDescriptorFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_enum.Windows.Media.Protection.PlayReady.NDContentIDType,  # contentIDType
                               _type.UINT32,  # __contentIDBytesSize
                               _Pointer[_type.BYTE],  # contentIDBytes
                               INDCustomData,  # licenseFetchChallengeCustomData
                               _Pointer[INDLicenseFetchDescriptor]],  # instance
                              _type.HRESULT]

    _factory = True


class INDLicenseFetchResult(_inspectable.IInspectable):
    ResponseCustomData: _Callable[[_Pointer[INDCustomData]],  # customData
                                  _type.HRESULT]


class INDMessenger(_inspectable.IInspectable):
    SendRegistrationRequestAsync: _Callable[[_type.UINT32,  # __sessionIDBytesSize
                                             _Pointer[_type.BYTE],  # sessionIDBytes
                                             _type.UINT32,  # __challengeDataBytesSize
                                             _Pointer[_type.BYTE],  # challengeDataBytes
                                             _Pointer[_Windows_Foundation.IAsyncOperation[INDSendResult]]],  # result
                                            _type.HRESULT]
    SendProximityDetectionStartAsync: _Callable[[_enum.Windows.Media.Protection.PlayReady.NDProximityDetectionType,  # pdType
                                                 _type.UINT32,  # __transmitterChannelBytesSize
                                                 _Pointer[_type.BYTE],  # transmitterChannelBytes
                                                 _type.UINT32,  # __sessionIDBytesSize
                                                 _Pointer[_type.BYTE],  # sessionIDBytes
                                                 _type.UINT32,  # __challengeDataBytesSize
                                                 _Pointer[_type.BYTE],  # challengeDataBytes
                                                 _Pointer[_Windows_Foundation.IAsyncOperation[INDSendResult]]],  # result
                                                _type.HRESULT]
    SendProximityDetectionResponseAsync: _Callable[[_enum.Windows.Media.Protection.PlayReady.NDProximityDetectionType,  # pdType
                                                    _type.UINT32,  # __transmitterChannelBytesSize
                                                    _Pointer[_type.BYTE],  # transmitterChannelBytes
                                                    _type.UINT32,  # __sessionIDBytesSize
                                                    _Pointer[_type.BYTE],  # sessionIDBytes
                                                    _type.UINT32,  # __responseDataBytesSize
                                                    _Pointer[_type.BYTE],  # responseDataBytes
                                                    _Pointer[_Windows_Foundation.IAsyncOperation[INDSendResult]]],  # result
                                                   _type.HRESULT]
    SendLicenseFetchRequestAsync: _Callable[[_type.UINT32,  # __sessionIDBytesSize
                                             _Pointer[_type.BYTE],  # sessionIDBytes
                                             _type.UINT32,  # __challengeDataBytesSize
                                             _Pointer[_type.BYTE],  # challengeDataBytes
                                             _Pointer[_Windows_Foundation.IAsyncOperation[INDSendResult]]],  # result
                                            _type.HRESULT]


class INDProximityDetectionCompletedEventArgs(_inspectable.IInspectable):
    ProximityDetectionRetryCount: _Callable[[_Pointer[_type.UINT32]],  # retryCount
                                            _type.HRESULT]


class INDRegistrationCompletedEventArgs(_inspectable.IInspectable):
    ResponseCustomData: _Callable[[_Pointer[INDCustomData]],  # customData
                                  _type.HRESULT]
    TransmitterProperties: _Callable[[_Pointer[INDTransmitterProperties]],  # transmitterProperties
                                     _type.HRESULT]
    TransmitterCertificateAccepted: _Callable[[_type.boolean],  # accept
                                              _type.HRESULT]


class INDSendResult(_inspectable.IInspectable):
    Response: _Callable[[_Pointer[_type.UINT32],  # __responseDataBytesSize
                         _Pointer[_Pointer[_type.BYTE]]],  # responseDataBytes
                        _type.HRESULT]


class INDStartResult(_inspectable.IInspectable):
    MediaStreamSource: _Callable[[_Pointer[_Windows_Media_Core.IMediaStreamSource]],  # mediaStreamSource
                                 _type.HRESULT]


class INDStorageFileHelper(_inspectable.IInspectable):
    GetFileURLs: _Callable[[_Windows_Storage.IStorageFile,  # file
                            _Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # fileURLs
                           _type.HRESULT]


class INDStreamParser(_inspectable.IInspectable):
    ParseData: _Callable[[_type.UINT32,  # __dataBytesSize
                          _Pointer[_type.BYTE]],  # dataBytes
                         _type.HRESULT]
    GetStreamInformation: _Callable[[_Windows_Media_Core.IMediaStreamDescriptor,  # descriptor
                                     _Pointer[_enum.Windows.Media.Protection.PlayReady.NDMediaStreamType],  # streamType
                                     _Pointer[_type.UINT32]],  # streamID
                                    _type.HRESULT]
    BeginOfStream: _Callable[[],
                             _type.HRESULT]
    EndOfStream: _Callable[[],
                           _type.HRESULT]
    Notifier: _Callable[[_Pointer[INDStreamParserNotifier]],  # instance
                        _type.HRESULT]


class INDStreamParserNotifier(_inspectable.IInspectable):
    OnContentIDReceived: _Callable[[INDLicenseFetchDescriptor],  # licenseFetchDescriptor
                                   _type.HRESULT]
    OnMediaStreamDescriptorCreated: _Callable[[_Windows_Foundation_Collections.IVector[_Windows_Media_Core.IAudioStreamDescriptor],  # audioStreamDescriptors
                                               _Windows_Foundation_Collections.IVector[_Windows_Media_Core.IVideoStreamDescriptor]],  # videoStreamDescriptors
                                              _type.HRESULT]
    OnSampleParsed: _Callable[[_type.UINT32,  # streamID
                               _enum.Windows.Media.Protection.PlayReady.NDMediaStreamType,  # streamType
                               _Windows_Media_Core.IMediaStreamSample,  # streamSample
                               _type.INT64,  # pts
                               _enum.Windows.Media.Protection.PlayReady.NDClosedCaptionFormat,  # ccFormat
                               _type.UINT32,  # __ccDataBytesSize
                               _Pointer[_type.BYTE]],  # ccDataBytes
                              _type.HRESULT]
    OnBeginSetupDecryptor: _Callable[[_Windows_Media_Core.IMediaStreamDescriptor,  # descriptor
                                      _struct.GUID,  # keyID
                                      _type.UINT32,  # __proBytesSize
                                      _Pointer[_type.BYTE]],  # proBytes
                                     _type.HRESULT]


class INDTCPMessengerFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_type.HSTRING,  # remoteHostName
                               _type.UINT32,  # remoteHostPort
                               _Pointer[INDMessenger]],  # instance
                              _type.HRESULT]

    _factory = True


class INDTransmitterProperties(_inspectable.IInspectable):
    CertificateType: _Callable[[_Pointer[_enum.Windows.Media.Protection.PlayReady.NDCertificateType]],  # type
                               _type.HRESULT]
    PlatformIdentifier: _Callable[[_Pointer[_enum.Windows.Media.Protection.PlayReady.NDCertificatePlatformID]],  # identifier
                                  _type.HRESULT]
    SupportedFeatures: _Callable[[_Pointer[_type.UINT32],  # __featureSetsSize
                                  _Pointer[_Pointer[_enum.Windows.Media.Protection.PlayReady.NDCertificateFeature]]],  # featureSets
                                 _type.HRESULT]
    SecurityLevel: _Callable[[_Pointer[_type.UINT32]],  # level
                             _type.HRESULT]
    SecurityVersion: _Callable[[_Pointer[_type.UINT32]],  # securityVersion
                               _type.HRESULT]
    ExpirationDate: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # expirationDate
                              _type.HRESULT]
    ClientID: _Callable[[_Pointer[_type.UINT32],  # __clientIDBytesSize
                         _Pointer[_Pointer[_type.BYTE]]],  # clientIDBytes
                        _type.HRESULT]
    ModelDigest: _Callable[[_Pointer[_type.UINT32],  # __modelDigestBytesSize
                            _Pointer[_Pointer[_type.BYTE]]],  # modelDigestBytes
                           _type.HRESULT]
    ModelManufacturerName: _Callable[[_Pointer[_type.HSTRING]],  # modelManufacturerName
                                     _type.HRESULT]
    ModelName: _Callable[[_Pointer[_type.HSTRING]],  # modelName
                         _type.HRESULT]
    ModelNumber: _Callable[[_Pointer[_type.HSTRING]],  # modelNumber
                           _type.HRESULT]


class IPlayReadyContentHeader(_inspectable.IInspectable):
    get_KeyId: _Callable[[_Pointer[_struct.GUID]],  # value
                         _type.HRESULT]
    get_KeyIdString: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_LicenseAcquisitionUrl: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                         _type.HRESULT]
    get_LicenseAcquisitionUserInterfaceUrl: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                                      _type.HRESULT]
    get_DomainServiceId: _Callable[[_Pointer[_struct.GUID]],  # value
                                   _type.HRESULT]
    get_EncryptionType: _Callable[[_Pointer[_enum.Windows.Media.Protection.PlayReady.PlayReadyEncryptionAlgorithm]],  # value
                                  _type.HRESULT]
    get_CustomAttributes: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_DecryptorSetup: _Callable[[_Pointer[_enum.Windows.Media.Protection.PlayReady.PlayReadyDecryptorSetup]],  # value
                                  _type.HRESULT]
    GetSerializedHeader: _Callable[[_Pointer[_type.UINT32],  # __headerBytesSize
                                    _Pointer[_Pointer[_type.BYTE]]],  # headerBytes
                                   _type.HRESULT]
    get_HeaderWithEmbeddedUpdates: _Callable[[_Pointer[IPlayReadyContentHeader]],  # value
                                             _type.HRESULT]


class IPlayReadyContentHeader2(_inspectable.IInspectable):
    get_KeyIds: _Callable[[_Pointer[_type.UINT32],  # __contentKeyIdsSize
                           _Pointer[_Pointer[_struct.GUID]]],  # contentKeyIds
                          _type.HRESULT]
    get_KeyIdStrings: _Callable[[_Pointer[_type.UINT32],  # __contentKeyIdStringsSize
                                 _Pointer[_Pointer[_type.HSTRING]]],  # contentKeyIdStrings
                                _type.HRESULT]


class IPlayReadyContentHeaderFactory(_inspectable.IInspectable):
    CreateInstanceFromWindowsMediaDrmHeader: _Callable[[_type.UINT32,  # __headerBytesSize
                                                        _Pointer[_type.BYTE],  # headerBytes
                                                        _Windows_Foundation.IUriRuntimeClass,  # licenseAcquisitionUrl
                                                        _Windows_Foundation.IUriRuntimeClass,  # licenseAcquisitionUserInterfaceUrl
                                                        _type.HSTRING,  # customAttributes
                                                        _struct.GUID,  # domainServiceId
                                                        _Pointer[IPlayReadyContentHeader]],  # instance
                                                       _type.HRESULT]
    CreateInstanceFromComponents: _Callable[[_struct.GUID,  # contentKeyId
                                             _type.HSTRING,  # contentKeyIdString
                                             _enum.Windows.Media.Protection.PlayReady.PlayReadyEncryptionAlgorithm,  # contentEncryptionAlgorithm
                                             _Windows_Foundation.IUriRuntimeClass,  # licenseAcquisitionUrl
                                             _Windows_Foundation.IUriRuntimeClass,  # licenseAcquisitionUserInterfaceUrl
                                             _type.HSTRING,  # customAttributes
                                             _struct.GUID,  # domainServiceId
                                             _Pointer[IPlayReadyContentHeader]],  # instance
                                            _type.HRESULT]
    CreateInstanceFromPlayReadyHeader: _Callable[[_type.UINT32,  # __headerBytesSize
                                                  _Pointer[_type.BYTE],  # headerBytes
                                                  _Pointer[IPlayReadyContentHeader]],  # instance
                                                 _type.HRESULT]


class IPlayReadyContentHeaderFactory2(_inspectable.IInspectable):
    CreateInstanceFromComponents2: _Callable[[_type.UINT32,  # dwFlags
                                              _type.UINT32,  # __contentKeyIdsSize
                                              _Pointer[_struct.GUID],  # contentKeyIds
                                              _type.UINT32,  # __contentKeyIdStringsSize
                                              _Pointer[_type.HSTRING],  # contentKeyIdStrings
                                              _enum.Windows.Media.Protection.PlayReady.PlayReadyEncryptionAlgorithm,  # contentEncryptionAlgorithm
                                              _Windows_Foundation.IUriRuntimeClass,  # licenseAcquisitionUrl
                                              _Windows_Foundation.IUriRuntimeClass,  # licenseAcquisitionUserInterfaceUrl
                                              _type.HSTRING,  # customAttributes
                                              _struct.GUID,  # domainServiceId
                                              _Pointer[IPlayReadyContentHeader]],  # instance
                                             _type.HRESULT]

    _factory = True


class IPlayReadyContentResolver(_inspectable.IInspectable):
    ServiceRequest: _Callable[[IPlayReadyContentHeader,  # contentHeader
                               _Pointer[IPlayReadyServiceRequest]],  # serviceRequest
                              _type.HRESULT]

    _factory = True


class IPlayReadyDomain(_inspectable.IInspectable):
    get_AccountId: _Callable[[_Pointer[_struct.GUID]],  # value
                             _type.HRESULT]
    get_ServiceId: _Callable[[_Pointer[_struct.GUID]],  # value
                             _type.HRESULT]
    get_Revision: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    get_FriendlyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_DomainJoinUrl: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                 _type.HRESULT]


class IPlayReadyDomainIterableFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_struct.GUID,  # domainAccountId
                               _Pointer[_Windows_Foundation_Collections.IIterable[IPlayReadyDomain]]],  # domainIterable
                              _type.HRESULT]

    _factory = True


class IPlayReadyDomainJoinServiceRequest(_inspectable.IInspectable):
    get_DomainAccountId: _Callable[[_Pointer[_struct.GUID]],  # value
                                   _type.HRESULT]
    put_DomainAccountId: _Callable[[_struct.GUID],  # value
                                   _type.HRESULT]
    get_DomainFriendlyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    put_DomainFriendlyName: _Callable[[_type.HSTRING],  # value
                                      _type.HRESULT]
    get_DomainServiceId: _Callable[[_Pointer[_struct.GUID]],  # value
                                   _type.HRESULT]
    put_DomainServiceId: _Callable[[_struct.GUID],  # value
                                   _type.HRESULT]


class IPlayReadyDomainLeaveServiceRequest(_inspectable.IInspectable):
    get_DomainAccountId: _Callable[[_Pointer[_struct.GUID]],  # value
                                   _type.HRESULT]
    put_DomainAccountId: _Callable[[_struct.GUID],  # value
                                   _type.HRESULT]
    get_DomainServiceId: _Callable[[_Pointer[_struct.GUID]],  # value
                                   _type.HRESULT]
    put_DomainServiceId: _Callable[[_struct.GUID],  # value
                                   _type.HRESULT]


class IPlayReadyITADataGenerator(_inspectable.IInspectable):
    GenerateData: _Callable[[_struct.GUID,  # guidCPSystemId
                             _type.UINT32,  # countOfStreams
                             _Windows_Foundation_Collections.IPropertySet,  # configuration
                             _enum.Windows.Media.Protection.PlayReady.PlayReadyITADataFormat,  # format
                             _Pointer[_type.UINT32],  # __dataBytesSize
                             _Pointer[_Pointer[_type.BYTE]]],  # dataBytes
                            _type.HRESULT]


class IPlayReadyIndividualizationServiceRequest(_inspectable.IInspectable):
    pass


class IPlayReadyLicense(_inspectable.IInspectable):
    get_FullyEvaluated: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    get_UsableForPlay: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_ExpirationDate: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                  _type.HRESULT]
    get_ExpireAfterFirstPlay: _Callable[[_Pointer[_type.UINT32]],  # value
                                        _type.HRESULT]
    get_DomainAccountID: _Callable[[_Pointer[_struct.GUID]],  # value
                                   _type.HRESULT]
    get_ChainDepth: _Callable[[_Pointer[_type.UINT32]],  # value
                              _type.HRESULT]
    GetKIDAtChainDepth: _Callable[[_type.UINT32,  # chainDepth
                                   _Pointer[_struct.GUID]],  # kid
                                  _type.HRESULT]


class IPlayReadyLicense2(_inspectable.IInspectable):
    get_SecureStopId: _Callable[[_Pointer[_struct.GUID]],  # value
                                _type.HRESULT]
    get_SecurityLevel: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    get_InMemoryOnly: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_ExpiresInRealTime: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]


class IPlayReadyLicenseAcquisitionServiceRequest(_inspectable.IInspectable):
    get_ContentHeader: _Callable[[_Pointer[IPlayReadyContentHeader]],  # value
                                 _type.HRESULT]
    put_ContentHeader: _Callable[[IPlayReadyContentHeader],  # value
                                 _type.HRESULT]
    get_DomainServiceId: _Callable[[_Pointer[_struct.GUID]],  # value
                                   _type.HRESULT]
    put_DomainServiceId: _Callable[[_struct.GUID],  # value
                                   _type.HRESULT]


class IPlayReadyLicenseAcquisitionServiceRequest2(_inspectable.IInspectable):
    get_SessionId: _Callable[[_Pointer[_struct.GUID]],  # value
                             _type.HRESULT]


class IPlayReadyLicenseAcquisitionServiceRequest3(_inspectable.IInspectable):
    CreateLicenseIterable: _Callable[[IPlayReadyContentHeader,  # contentHeader
                                      _type.boolean,  # fullyEvaluated
                                      _Pointer[_Windows_Foundation_Collections.IIterable[IPlayReadyLicense]]],  # result
                                     _type.HRESULT]


class IPlayReadyLicenseIterableFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[IPlayReadyContentHeader,  # contentHeader
                               _type.boolean,  # fullyEvaluated
                               _Pointer[_Windows_Foundation_Collections.IIterable[IPlayReadyLicense]]],  # instance
                              _type.HRESULT]

    _factory = True


class IPlayReadyLicenseManagement(_inspectable.IInspectable):
    DeleteLicenses: _Callable[[IPlayReadyContentHeader,  # contentHeader
                               _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                              _type.HRESULT]

    _factory = True


class IPlayReadyLicenseSession(_inspectable.IInspectable):
    CreateLAServiceRequest: _Callable[[_Pointer[IPlayReadyLicenseAcquisitionServiceRequest]],  # serviceRequest
                                      _type.HRESULT]
    ConfigureMediaProtectionManager: _Callable[[_Windows_Media_Protection.IMediaProtectionManager],  # mpm
                                               _type.HRESULT]


class IPlayReadyLicenseSession2(_inspectable.IInspectable):
    CreateLicenseIterable: _Callable[[IPlayReadyContentHeader,  # contentHeader
                                      _type.boolean,  # fullyEvaluated
                                      _Pointer[_Windows_Foundation_Collections.IIterable[IPlayReadyLicense]]],  # licenseIterable
                                     _type.HRESULT]


class IPlayReadyLicenseSessionFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_Windows_Foundation_Collections.IPropertySet,  # configuration
                               _Pointer[IPlayReadyLicenseSession]],  # instance
                              _type.HRESULT]

    _factory = True


class IPlayReadyMeteringReportServiceRequest(_inspectable.IInspectable):
    get_MeteringCertificate: _Callable[[_Pointer[_type.UINT32],  # __meteringCertBytesSize
                                        _Pointer[_Pointer[_type.BYTE]]],  # meteringCertBytes
                                       _type.HRESULT]
    put_MeteringCertificate: _Callable[[_type.UINT32,  # __meteringCertBytesSize
                                        _Pointer[_type.BYTE]],  # meteringCertBytes
                                       _type.HRESULT]


class IPlayReadyRevocationServiceRequest(_inspectable.IInspectable):
    pass


class IPlayReadySecureStopIterableFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_type.UINT32,  # __publisherCertBytesSize
                               _Pointer[_type.BYTE],  # publisherCertBytes
                               _Pointer[_Windows_Foundation_Collections.IIterable[IPlayReadySecureStopServiceRequest]]],  # instance
                              _type.HRESULT]

    _factory = True


class IPlayReadySecureStopServiceRequest(_inspectable.IInspectable):
    get_SessionID: _Callable[[_Pointer[_struct.GUID]],  # value
                             _type.HRESULT]
    get_StartTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_UpdateTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                              _type.HRESULT]
    get_Stopped: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_PublisherCertificate: _Callable[[_Pointer[_type.UINT32],  # __publisherCertBytesSize
                                         _Pointer[_Pointer[_type.BYTE]]],  # publisherCertBytes
                                        _type.HRESULT]


class IPlayReadySecureStopServiceRequestFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_type.UINT32,  # __publisherCertBytesSize
                               _Pointer[_type.BYTE],  # publisherCertBytes
                               _Pointer[IPlayReadySecureStopServiceRequest]],  # instance
                              _type.HRESULT]
    CreateInstanceFromSessionID: _Callable[[_struct.GUID,  # sessionID
                                            _type.UINT32,  # __publisherCertBytesSize
                                            _Pointer[_type.BYTE],  # publisherCertBytes
                                            _Pointer[IPlayReadySecureStopServiceRequest]],  # instance
                                           _type.HRESULT]

    _factory = True


class IPlayReadyServiceRequest(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]
    put_Uri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                       _type.HRESULT]
    get_ResponseCustomData: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_ChallengeCustomData: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    put_ChallengeCustomData: _Callable[[_type.HSTRING],  # value
                                       _type.HRESULT]
    BeginServiceRequest: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # action
                                   _type.HRESULT]
    NextServiceRequest: _Callable[[_Pointer[IPlayReadyServiceRequest]],  # serviceRequest
                                  _type.HRESULT]
    GenerateManualEnablingChallenge: _Callable[[_Pointer[IPlayReadySoapMessage]],  # challengeMessage
                                               _type.HRESULT]
    ProcessManualEnablingResponse: _Callable[[_type.UINT32,  # __responseBytesSize
                                              _Pointer[_type.BYTE],  # responseBytes
                                              _Pointer[_type.HRESULT]],  # result
                                             _type.HRESULT]


class IPlayReadySoapMessage(_inspectable.IInspectable):
    GetMessageBody: _Callable[[_Pointer[_type.UINT32],  # __messageBodyBytesSize
                               _Pointer[_Pointer[_type.BYTE]]],  # messageBodyBytes
                              _type.HRESULT]
    get_MessageHeaders: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                                  _type.HRESULT]
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # messageUri
                       _type.HRESULT]


class IPlayReadyStatics(_inspectable.IInspectable):
    get_DomainJoinServiceRequestType: _Callable[[_Pointer[_struct.GUID]],  # value
                                                _type.HRESULT]
    get_DomainLeaveServiceRequestType: _Callable[[_Pointer[_struct.GUID]],  # value
                                                 _type.HRESULT]
    get_IndividualizationServiceRequestType: _Callable[[_Pointer[_struct.GUID]],  # value
                                                       _type.HRESULT]
    get_LicenseAcquirerServiceRequestType: _Callable[[_Pointer[_struct.GUID]],  # value
                                                     _type.HRESULT]
    get_MeteringReportServiceRequestType: _Callable[[_Pointer[_struct.GUID]],  # value
                                                    _type.HRESULT]
    get_RevocationServiceRequestType: _Callable[[_Pointer[_struct.GUID]],  # value
                                                _type.HRESULT]
    get_MediaProtectionSystemId: _Callable[[_Pointer[_struct.GUID]],  # value
                                           _type.HRESULT]
    get_PlayReadySecurityVersion: _Callable[[_Pointer[_type.UINT32]],  # value
                                            _type.HRESULT]

    _factory = True


class IPlayReadyStatics2(_inspectable.IInspectable):
    get_PlayReadyCertificateSecurityLevel: _Callable[[_Pointer[_type.UINT32]],  # value
                                                     _type.HRESULT]

    _factory = True


class IPlayReadyStatics3(_inspectable.IInspectable):
    get_SecureStopServiceRequestType: _Callable[[_Pointer[_struct.GUID]],  # value
                                                _type.HRESULT]
    CheckSupportedHardware: _Callable[[_enum.Windows.Media.Protection.PlayReady.PlayReadyHardwareDRMFeatures,  # hwdrmFeature
                                       _Pointer[_type.boolean]],  # value
                                      _type.HRESULT]

    _factory = True


class IPlayReadyStatics4(_inspectable.IInspectable):
    get_InputTrustAuthorityToCreate: _Callable[[_Pointer[_type.HSTRING]],  # value
                                               _type.HRESULT]
    get_ProtectionSystemId: _Callable[[_Pointer[_struct.GUID]],  # value
                                      _type.HRESULT]

    _factory = True


class IPlayReadyStatics5(_inspectable.IInspectable):
    get_HardwareDRMDisabledAtTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                             _type.HRESULT]
    get_HardwareDRMDisabledUntilTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                                _type.HRESULT]
    ResetHardwareDRMDisabled: _Callable[[],
                                        _type.HRESULT]

    _factory = True
