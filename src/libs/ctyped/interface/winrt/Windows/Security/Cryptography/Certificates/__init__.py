from __future__ import annotations as _

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from .... import Networking as _Windows_Networking
from ....Foundation import Collections as _Windows_Foundation_Collections
from ....Storage import Streams as _Windows_Storage_Streams
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class ICertificate(_inspectable.IInspectable):
    BuildChainAsync: _Callable[[_Windows_Foundation_Collections.IIterable[ICertificate],  # certificates
                                _Pointer[_Windows_Foundation.IAsyncOperation[ICertificateChain]]],  # value
                               _type.HRESULT]
    BuildChainWithParametersAsync: _Callable[[_Windows_Foundation_Collections.IIterable[ICertificate],  # certificates
                                              IChainBuildingParameters,  # parameters
                                              _Pointer[_Windows_Foundation.IAsyncOperation[ICertificateChain]]],  # value
                                             _type.HRESULT]
    get_SerialNumber: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                                 _Pointer[_Pointer[_type.BYTE]]],  # value
                                _type.HRESULT]
    GetHashValue: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                             _Pointer[_Pointer[_type.BYTE]]],  # value
                            _type.HRESULT]
    GetHashValueWithAlgorithm: _Callable[[_type.HSTRING,  # hashAlgorithmName
                                          _Pointer[_type.UINT32],  # __valueSize
                                          _Pointer[_Pointer[_type.BYTE]]],  # value
                                         _type.HRESULT]
    GetCertificateBlob: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                  _type.HRESULT]
    get_Subject: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Issuer: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_HasPrivateKey: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_IsStronglyProtected: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    get_ValidFrom: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_ValidTo: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                           _type.HRESULT]
    get_EnhancedKeyUsages: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                     _type.HRESULT]
    put_FriendlyName: _Callable[[_type.HSTRING],  # value
                                _type.HRESULT]
    get_FriendlyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]


class ICertificate2(_inspectable.IInspectable):
    get_IsSecurityDeviceBound: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    get_KeyUsages: _Callable[[_Pointer[ICertificateKeyUsages]],  # value
                             _type.HRESULT]
    get_KeyAlgorithmName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_SignatureAlgorithmName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                          _type.HRESULT]
    get_SignatureHashAlgorithmName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                              _type.HRESULT]
    get_SubjectAlternativeName: _Callable[[_Pointer[ISubjectAlternativeNameInfo]],  # value
                                          _type.HRESULT]


class ICertificate3(_inspectable.IInspectable):
    get_IsPerUser: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_StoreName: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_KeyStorageProviderName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                          _type.HRESULT]


class ICertificateChain(_inspectable.IInspectable):
    Validate: _Callable[[_Pointer[_enum.Windows.Security.Cryptography.Certificates.ChainValidationResult]],  # status
                        _type.HRESULT]
    ValidateWithParameters: _Callable[[IChainValidationParameters,  # parameter
                                       _Pointer[_enum.Windows.Security.Cryptography.Certificates.ChainValidationResult]],  # status
                                      _type.HRESULT]
    GetCertificates: _Callable[[_type.boolean,  # includeRoot
                                _Pointer[_Windows_Foundation_Collections.IVectorView[ICertificate]]],  # certificates
                               _type.HRESULT]


class ICertificateEnrollmentManagerStatics(_inspectable.IInspectable):
    CreateRequestAsync: _Callable[[ICertificateRequestProperties,  # request
                                   _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # value
                                  _type.HRESULT]
    InstallCertificateAsync: _Callable[[_type.HSTRING,  # certificate
                                        _enum.Windows.Security.Cryptography.Certificates.InstallOptions,  # installOption
                                        _Pointer[_Windows_Foundation.IAsyncAction]],  # value
                                       _type.HRESULT]
    ImportPfxDataAsync: _Callable[[_type.HSTRING,  # pfxData
                                   _type.HSTRING,  # password
                                   _enum.Windows.Security.Cryptography.Certificates.ExportOption,  # exportable
                                   _enum.Windows.Security.Cryptography.Certificates.KeyProtectionLevel,  # keyProtectionLevel
                                   _enum.Windows.Security.Cryptography.Certificates.InstallOptions,  # installOption
                                   _type.HSTRING,  # friendlyName
                                   _Pointer[_Windows_Foundation.IAsyncAction]],  # value
                                  _type.HRESULT]

    _factory = True


class ICertificateEnrollmentManagerStatics2(_inspectable.IInspectable):
    get_UserCertificateEnrollmentManager: _Callable[[_Pointer[IUserCertificateEnrollmentManager]],  # value
                                                    _type.HRESULT]
    ImportPfxDataToKspAsync: _Callable[[_type.HSTRING,  # pfxData
                                        _type.HSTRING,  # password
                                        _enum.Windows.Security.Cryptography.Certificates.ExportOption,  # exportable
                                        _enum.Windows.Security.Cryptography.Certificates.KeyProtectionLevel,  # keyProtectionLevel
                                        _enum.Windows.Security.Cryptography.Certificates.InstallOptions,  # installOption
                                        _type.HSTRING,  # friendlyName
                                        _type.HSTRING,  # keyStorageProvider
                                        _Pointer[_Windows_Foundation.IAsyncAction]],  # value
                                       _type.HRESULT]

    _factory = True


class ICertificateEnrollmentManagerStatics3(_inspectable.IInspectable):
    ImportPfxDataToKspWithParametersAsync: _Callable[[_type.HSTRING,  # pfxData
                                                      _type.HSTRING,  # password
                                                      IPfxImportParameters,  # pfxImportParameters
                                                      _Pointer[_Windows_Foundation.IAsyncAction]],  # value
                                                     _type.HRESULT]

    _factory = True


class ICertificateExtension(_inspectable.IInspectable):
    get_ObjectId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_ObjectId: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_IsCritical: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    put_IsCritical: _Callable[[_type.boolean],  # value
                              _type.HRESULT]
    EncodeValue: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                          _Pointer[_Pointer[_type.BYTE]]],  # value
                         _type.HRESULT]
    put_Value: _Callable[[_type.UINT32,  # __valueSize
                          _Pointer[_type.BYTE]],  # value
                         _type.HRESULT]


class ICertificateFactory(_inspectable.IInspectable):
    CreateCertificate: _Callable[[_Windows_Storage_Streams.IBuffer,  # certBlob
                                  _Pointer[ICertificate]],  # certificate
                                 _type.HRESULT]

    _factory = True


class ICertificateKeyUsages(_inspectable.IInspectable):
    get_EncipherOnly: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_EncipherOnly: _Callable[[_type.boolean],  # value
                                _type.HRESULT]
    get_CrlSign: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_CrlSign: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_KeyCertificateSign: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_KeyCertificateSign: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    get_KeyAgreement: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_KeyAgreement: _Callable[[_type.boolean],  # value
                                _type.HRESULT]
    get_DataEncipherment: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_DataEncipherment: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_KeyEncipherment: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    put_KeyEncipherment: _Callable[[_type.boolean],  # value
                                   _type.HRESULT]
    get_NonRepudiation: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    put_NonRepudiation: _Callable[[_type.boolean],  # value
                                  _type.HRESULT]
    get_DigitalSignature: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_DigitalSignature: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]


class ICertificateQuery(_inspectable.IInspectable):
    get_EnhancedKeyUsages: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                     _type.HRESULT]
    get_IssuerName: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_IssuerName: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]
    get_FriendlyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    put_FriendlyName: _Callable[[_type.HSTRING],  # value
                                _type.HRESULT]
    get_Thumbprint: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                               _Pointer[_Pointer[_type.BYTE]]],  # value
                              _type.HRESULT]
    put_Thumbprint: _Callable[[_type.UINT32,  # __valueSize
                               _Pointer[_type.BYTE]],  # value
                              _type.HRESULT]
    get_HardwareOnly: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_HardwareOnly: _Callable[[_type.boolean],  # value
                                _type.HRESULT]


class ICertificateQuery2(_inspectable.IInspectable):
    get_IncludeDuplicates: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    put_IncludeDuplicates: _Callable[[_type.boolean],  # value
                                     _type.HRESULT]
    get_IncludeExpiredCertificates: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]
    put_IncludeExpiredCertificates: _Callable[[_type.boolean],  # value
                                              _type.HRESULT]
    get_StoreName: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_StoreName: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]


class ICertificateRequestProperties(_inspectable.IInspectable):
    get_Subject: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    put_Subject: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    get_KeyAlgorithmName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    put_KeyAlgorithmName: _Callable[[_type.HSTRING],  # value
                                    _type.HRESULT]
    get_KeySize: _Callable[[_Pointer[_type.UINT32]],  # value
                           _type.HRESULT]
    put_KeySize: _Callable[[_type.UINT32],  # value
                           _type.HRESULT]
    get_FriendlyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    put_FriendlyName: _Callable[[_type.HSTRING],  # value
                                _type.HRESULT]
    get_HashAlgorithmName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    put_HashAlgorithmName: _Callable[[_type.HSTRING],  # value
                                     _type.HRESULT]
    get_Exportable: _Callable[[_Pointer[_enum.Windows.Security.Cryptography.Certificates.ExportOption]],  # value
                              _type.HRESULT]
    put_Exportable: _Callable[[_enum.Windows.Security.Cryptography.Certificates.ExportOption],  # value
                              _type.HRESULT]
    get_KeyUsages: _Callable[[_Pointer[_enum.Windows.Security.Cryptography.Certificates.EnrollKeyUsages]],  # value
                             _type.HRESULT]
    put_KeyUsages: _Callable[[_enum.Windows.Security.Cryptography.Certificates.EnrollKeyUsages],  # value
                             _type.HRESULT]
    get_KeyProtectionLevel: _Callable[[_Pointer[_enum.Windows.Security.Cryptography.Certificates.KeyProtectionLevel]],  # value
                                      _type.HRESULT]
    put_KeyProtectionLevel: _Callable[[_enum.Windows.Security.Cryptography.Certificates.KeyProtectionLevel],  # value
                                      _type.HRESULT]
    get_KeyStorageProviderName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                          _type.HRESULT]
    put_KeyStorageProviderName: _Callable[[_type.HSTRING],  # value
                                          _type.HRESULT]


class ICertificateRequestProperties2(_inspectable.IInspectable):
    get_SmartcardReaderName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    put_SmartcardReaderName: _Callable[[_type.HSTRING],  # value
                                       _type.HRESULT]
    get_SigningCertificate: _Callable[[_Pointer[ICertificate]],  # value
                                      _type.HRESULT]
    put_SigningCertificate: _Callable[[ICertificate],  # value
                                      _type.HRESULT]
    get_AttestationCredentialCertificate: _Callable[[_Pointer[ICertificate]],  # value
                                                    _type.HRESULT]
    put_AttestationCredentialCertificate: _Callable[[ICertificate],  # value
                                                    _type.HRESULT]


class ICertificateRequestProperties3(_inspectable.IInspectable):
    get_CurveName: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_CurveName: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_CurveParameters: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                                    _Pointer[_Pointer[_type.BYTE]]],  # value
                                   _type.HRESULT]
    put_CurveParameters: _Callable[[_type.UINT32,  # __valueSize
                                    _Pointer[_type.BYTE]],  # value
                                   _type.HRESULT]
    get_ContainerNamePrefix: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    put_ContainerNamePrefix: _Callable[[_type.HSTRING],  # value
                                       _type.HRESULT]
    get_ContainerName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    put_ContainerName: _Callable[[_type.HSTRING],  # value
                                 _type.HRESULT]
    get_UseExistingKey: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    put_UseExistingKey: _Callable[[_type.boolean],  # value
                                  _type.HRESULT]


class ICertificateRequestProperties4(_inspectable.IInspectable):
    get_SuppressedDefaults: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                      _type.HRESULT]
    get_SubjectAlternativeName: _Callable[[_Pointer[ISubjectAlternativeNameInfo]],  # value
                                          _type.HRESULT]
    get_Extensions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ICertificateExtension]]],  # value
                              _type.HRESULT]


class ICertificateStore(_inspectable.IInspectable):
    Add: _Callable[[ICertificate],  # certificate
                   _type.HRESULT]
    Delete: _Callable[[ICertificate],  # certificate
                      _type.HRESULT]


class ICertificateStore2(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class ICertificateStoresStatics(_inspectable.IInspectable):
    FindAllAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[ICertificate]]]],  # value
                            _type.HRESULT]
    FindAllWithQueryAsync: _Callable[[ICertificateQuery,  # query
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[ICertificate]]]],  # value
                                     _type.HRESULT]
    get_TrustedRootCertificationAuthorities: _Callable[[_Pointer[ICertificateStore]],  # value
                                                       _type.HRESULT]
    get_IntermediateCertificationAuthorities: _Callable[[_Pointer[ICertificateStore]],  # value
                                                        _type.HRESULT]
    GetStoreByName: _Callable[[_type.HSTRING,  # storeName
                               _Pointer[ICertificateStore]],  # value
                              _type.HRESULT]

    _factory = True


class ICertificateStoresStatics2(_inspectable.IInspectable):
    GetUserStoreByName: _Callable[[_type.HSTRING,  # storeName
                                   _Pointer[IUserCertificateStore]],  # result
                                  _type.HRESULT]

    _factory = True


class IChainBuildingParameters(_inspectable.IInspectable):
    get_EnhancedKeyUsages: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                     _type.HRESULT]
    get_ValidationTimestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                       _type.HRESULT]
    put_ValidationTimestamp: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                                       _type.HRESULT]
    get_RevocationCheckEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_RevocationCheckEnabled: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    get_NetworkRetrievalEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    put_NetworkRetrievalEnabled: _Callable[[_type.boolean],  # value
                                           _type.HRESULT]
    get_AuthorityInformationAccessEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                     _type.HRESULT]
    put_AuthorityInformationAccessEnabled: _Callable[[_type.boolean],  # value
                                                     _type.HRESULT]
    get_CurrentTimeValidationEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                _type.HRESULT]
    put_CurrentTimeValidationEnabled: _Callable[[_type.boolean],  # value
                                                _type.HRESULT]
    get_ExclusiveTrustRoots: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ICertificate]]],  # certificates
                                       _type.HRESULT]


class IChainValidationParameters(_inspectable.IInspectable):
    get_CertificateChainPolicy: _Callable[[_Pointer[_enum.Windows.Security.Cryptography.Certificates.CertificateChainPolicy]],  # value
                                          _type.HRESULT]
    put_CertificateChainPolicy: _Callable[[_enum.Windows.Security.Cryptography.Certificates.CertificateChainPolicy],  # value
                                          _type.HRESULT]
    get_ServerDnsName: _Callable[[_Pointer[_Windows_Networking.IHostName]],  # value
                                 _type.HRESULT]
    put_ServerDnsName: _Callable[[_Windows_Networking.IHostName],  # value
                                 _type.HRESULT]


class ICmsAttachedSignature(_inspectable.IInspectable):
    get_Certificates: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[ICertificate]]],  # value
                                _type.HRESULT]
    get_Content: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                            _Pointer[_Pointer[_type.BYTE]]],  # value
                           _type.HRESULT]
    get_Signers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[ICmsSignerInfo]]],  # value
                           _type.HRESULT]
    VerifySignature: _Callable[[_Pointer[_enum.Windows.Security.Cryptography.Certificates.SignatureValidationResult]],  # value
                               _type.HRESULT]


class ICmsAttachedSignatureFactory(_inspectable.IInspectable):
    CreateCmsAttachedSignature: _Callable[[_Windows_Storage_Streams.IBuffer,  # inputBlob
                                           _Pointer[ICmsAttachedSignature]],  # cmsSignedData
                                          _type.HRESULT]

    _factory = True


class ICmsAttachedSignatureStatics(_inspectable.IInspectable):
    GenerateSignatureAsync: _Callable[[_Windows_Storage_Streams.IBuffer,  # data
                                       _Windows_Foundation_Collections.IIterable[ICmsSignerInfo],  # signers
                                       _Windows_Foundation_Collections.IIterable[ICertificate],  # certificates
                                       _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IBuffer]]],  # outputBlob
                                      _type.HRESULT]

    _factory = True


class ICmsDetachedSignature(_inspectable.IInspectable):
    get_Certificates: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[ICertificate]]],  # value
                                _type.HRESULT]
    get_Signers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[ICmsSignerInfo]]],  # value
                           _type.HRESULT]
    VerifySignatureAsync: _Callable[[_Windows_Storage_Streams.IInputStream,  # data
                                     _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Security.Cryptography.Certificates.SignatureValidationResult]]],  # value
                                    _type.HRESULT]


class ICmsDetachedSignatureFactory(_inspectable.IInspectable):
    CreateCmsDetachedSignature: _Callable[[_Windows_Storage_Streams.IBuffer,  # inputBlob
                                           _Pointer[ICmsDetachedSignature]],  # cmsSignedData
                                          _type.HRESULT]

    _factory = True


class ICmsDetachedSignatureStatics(_inspectable.IInspectable):
    GenerateSignatureAsync: _Callable[[_Windows_Storage_Streams.IInputStream,  # data
                                       _Windows_Foundation_Collections.IIterable[ICmsSignerInfo],  # signers
                                       _Windows_Foundation_Collections.IIterable[ICertificate],  # certificates
                                       _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IBuffer]]],  # outputBlob
                                      _type.HRESULT]

    _factory = True


class ICmsSignerInfo(_inspectable.IInspectable):
    get_Certificate: _Callable[[_Pointer[ICertificate]],  # value
                               _type.HRESULT]
    put_Certificate: _Callable[[ICertificate],  # value
                               _type.HRESULT]
    get_HashAlgorithmName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    put_HashAlgorithmName: _Callable[[_type.HSTRING],  # value
                                     _type.HRESULT]
    get_TimestampInfo: _Callable[[_Pointer[ICmsTimestampInfo]],  # value
                                 _type.HRESULT]


class ICmsTimestampInfo(_inspectable.IInspectable):
    get_SigningCertificate: _Callable[[_Pointer[ICertificate]],  # value
                                      _type.HRESULT]
    get_Certificates: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[ICertificate]]],  # value
                                _type.HRESULT]
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]


class IKeyAlgorithmNamesStatics(_inspectable.IInspectable):
    get_Rsa: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_Dsa: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_Ecdh256: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Ecdh384: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Ecdh521: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Ecdsa256: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Ecdsa384: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Ecdsa521: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]

    _factory = True


class IKeyAlgorithmNamesStatics2(_inspectable.IInspectable):
    get_Ecdsa: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Ecdh: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]

    _factory = True


class IKeyAttestationHelperStatics(_inspectable.IInspectable):
    DecryptTpmAttestationCredentialAsync: _Callable[[_type.HSTRING,  # credential
                                                     _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # value
                                                    _type.HRESULT]
    GetTpmAttestationCredentialId: _Callable[[_type.HSTRING,  # credential
                                              _Pointer[_type.HSTRING]],  # value
                                             _type.HRESULT]

    _factory = True


class IKeyAttestationHelperStatics2(_inspectable.IInspectable):
    DecryptTpmAttestationCredentialWithContainerNameAsync: _Callable[[_type.HSTRING,  # credential
                                                                      _type.HSTRING,  # containerName
                                                                      _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # value
                                                                     _type.HRESULT]

    _factory = True


class IKeyStorageProviderNamesStatics(_inspectable.IInspectable):
    get_SoftwareKeyStorageProvider: _Callable[[_Pointer[_type.HSTRING]],  # value
                                              _type.HRESULT]
    get_SmartcardKeyStorageProvider: _Callable[[_Pointer[_type.HSTRING]],  # value
                                               _type.HRESULT]
    get_PlatformKeyStorageProvider: _Callable[[_Pointer[_type.HSTRING]],  # value
                                              _type.HRESULT]

    _factory = True


class IKeyStorageProviderNamesStatics2(_inspectable.IInspectable):
    get_PassportKeyStorageProvider: _Callable[[_Pointer[_type.HSTRING]],  # value
                                              _type.HRESULT]

    _factory = True


class IPfxImportParameters(_inspectable.IInspectable):
    get_Exportable: _Callable[[_Pointer[_enum.Windows.Security.Cryptography.Certificates.ExportOption]],  # value
                              _type.HRESULT]
    put_Exportable: _Callable[[_enum.Windows.Security.Cryptography.Certificates.ExportOption],  # value
                              _type.HRESULT]
    get_KeyProtectionLevel: _Callable[[_Pointer[_enum.Windows.Security.Cryptography.Certificates.KeyProtectionLevel]],  # value
                                      _type.HRESULT]
    put_KeyProtectionLevel: _Callable[[_enum.Windows.Security.Cryptography.Certificates.KeyProtectionLevel],  # value
                                      _type.HRESULT]
    get_InstallOptions: _Callable[[_Pointer[_enum.Windows.Security.Cryptography.Certificates.InstallOptions]],  # value
                                  _type.HRESULT]
    put_InstallOptions: _Callable[[_enum.Windows.Security.Cryptography.Certificates.InstallOptions],  # value
                                  _type.HRESULT]
    get_FriendlyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    put_FriendlyName: _Callable[[_type.HSTRING],  # value
                                _type.HRESULT]
    get_KeyStorageProviderName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                          _type.HRESULT]
    put_KeyStorageProviderName: _Callable[[_type.HSTRING],  # value
                                          _type.HRESULT]
    get_ContainerNamePrefix: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    put_ContainerNamePrefix: _Callable[[_type.HSTRING],  # value
                                       _type.HRESULT]
    get_ReaderName: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_ReaderName: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]


class IStandardCertificateStoreNamesStatics(_inspectable.IInspectable):
    get_Personal: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_TrustedRootCertificationAuthorities: _Callable[[_Pointer[_type.HSTRING]],  # value
                                                       _type.HRESULT]
    get_IntermediateCertificationAuthorities: _Callable[[_Pointer[_type.HSTRING]],  # value
                                                        _type.HRESULT]

    _factory = True


class ISubjectAlternativeNameInfo(_inspectable.IInspectable):
    get_EmailName: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                             _type.HRESULT]
    get_IPAddress: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                             _type.HRESULT]
    get_Url: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                       _type.HRESULT]
    get_DnsName: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                           _type.HRESULT]
    get_DistinguishedName: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                     _type.HRESULT]
    get_PrincipalName: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                 _type.HRESULT]


class ISubjectAlternativeNameInfo2(_inspectable.IInspectable):
    get_EmailNames: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                              _type.HRESULT]
    get_IPAddresses: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                               _type.HRESULT]
    get_Urls: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                        _type.HRESULT]
    get_DnsNames: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                            _type.HRESULT]
    get_DistinguishedNames: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                      _type.HRESULT]
    get_PrincipalNames: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                  _type.HRESULT]
    get_Extension: _Callable[[_Pointer[ICertificateExtension]],  # value
                             _type.HRESULT]


class IUserCertificateEnrollmentManager(_inspectable.IInspectable):
    CreateRequestAsync: _Callable[[ICertificateRequestProperties,  # request
                                   _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # value
                                  _type.HRESULT]
    InstallCertificateAsync: _Callable[[_type.HSTRING,  # certificate
                                        _enum.Windows.Security.Cryptography.Certificates.InstallOptions,  # installOption
                                        _Pointer[_Windows_Foundation.IAsyncAction]],  # value
                                       _type.HRESULT]
    ImportPfxDataAsync: _Callable[[_type.HSTRING,  # pfxData
                                   _type.HSTRING,  # password
                                   _enum.Windows.Security.Cryptography.Certificates.ExportOption,  # exportable
                                   _enum.Windows.Security.Cryptography.Certificates.KeyProtectionLevel,  # keyProtectionLevel
                                   _enum.Windows.Security.Cryptography.Certificates.InstallOptions,  # installOption
                                   _type.HSTRING,  # friendlyName
                                   _Pointer[_Windows_Foundation.IAsyncAction]],  # value
                                  _type.HRESULT]
    ImportPfxDataToKspAsync: _Callable[[_type.HSTRING,  # pfxData
                                        _type.HSTRING,  # password
                                        _enum.Windows.Security.Cryptography.Certificates.ExportOption,  # exportable
                                        _enum.Windows.Security.Cryptography.Certificates.KeyProtectionLevel,  # keyProtectionLevel
                                        _enum.Windows.Security.Cryptography.Certificates.InstallOptions,  # installOption
                                        _type.HSTRING,  # friendlyName
                                        _type.HSTRING,  # keyStorageProvider
                                        _Pointer[_Windows_Foundation.IAsyncAction]],  # value
                                       _type.HRESULT]


class IUserCertificateEnrollmentManager2(_inspectable.IInspectable):
    ImportPfxDataToKspWithParametersAsync: _Callable[[_type.HSTRING,  # pfxData
                                                      _type.HSTRING,  # password
                                                      IPfxImportParameters,  # pfxImportParameters
                                                      _Pointer[_Windows_Foundation.IAsyncAction]],  # value
                                                     _type.HRESULT]


class IUserCertificateStore(_inspectable.IInspectable):
    RequestAddAsync: _Callable[[ICertificate,  # certificate
                                _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                               _type.HRESULT]
    RequestDeleteAsync: _Callable[[ICertificate,  # certificate
                                   _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                  _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
