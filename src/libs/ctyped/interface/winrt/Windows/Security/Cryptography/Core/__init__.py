from __future__ import annotations

from typing import Callable as _Callable

from .. import Certificates as _Windows_Security_Cryptography_Certificates
from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ....Storage import Streams as _Windows_Storage_Streams
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import type as _type
from ......._utils import _Pointer


class IAsymmetricAlgorithmNamesStatics(_inspectable.IInspectable):
    get_RsaPkcs1: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_RsaOaepSha1: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_RsaOaepSha256: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_RsaOaepSha384: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_RsaOaepSha512: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_EcdsaP256Sha256: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_EcdsaP384Sha384: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_EcdsaP521Sha512: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_DsaSha1: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_DsaSha256: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_RsaSignPkcs1Sha1: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_RsaSignPkcs1Sha256: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_RsaSignPkcs1Sha384: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_RsaSignPkcs1Sha512: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_RsaSignPssSha1: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_RsaSignPssSha256: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_RsaSignPssSha384: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_RsaSignPssSha512: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]

    _factory = True


class IAsymmetricAlgorithmNamesStatics2(_inspectable.IInspectable):
    get_EcdsaSha256: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_EcdsaSha384: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_EcdsaSha512: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]

    _factory = True


class IAsymmetricKeyAlgorithmProvider(_inspectable.IInspectable):
    get_AlgorithmName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    CreateKeyPair: _Callable[[_type.UINT32,  # keySize
                              _Pointer[ICryptographicKey]],  # key
                             _type.HRESULT]
    ImportDefaultPrivateKeyBlob: _Callable[[_Windows_Storage_Streams.IBuffer,  # keyBlob
                                            _Pointer[ICryptographicKey]],  # key
                                           _type.HRESULT]
    ImportKeyPairWithBlobType: _Callable[[_Windows_Storage_Streams.IBuffer,  # keyBlob
                                          _enum.Windows.Security.Cryptography.Core.CryptographicPrivateKeyBlobType,  # BlobType
                                          _Pointer[ICryptographicKey]],  # key
                                         _type.HRESULT]
    ImportDefaultPublicKeyBlob: _Callable[[_Windows_Storage_Streams.IBuffer,  # keyBlob
                                           _Pointer[ICryptographicKey]],  # key
                                          _type.HRESULT]
    ImportPublicKeyWithBlobType: _Callable[[_Windows_Storage_Streams.IBuffer,  # keyBlob
                                            _enum.Windows.Security.Cryptography.Core.CryptographicPublicKeyBlobType,  # BlobType
                                            _Pointer[ICryptographicKey]],  # key
                                           _type.HRESULT]


class IAsymmetricKeyAlgorithmProvider2(_inspectable.IInspectable):
    CreateKeyPairWithCurveName: _Callable[[_type.HSTRING,  # curveName
                                           _Pointer[ICryptographicKey]],  # key
                                          _type.HRESULT]
    CreateKeyPairWithCurveParameters: _Callable[[_type.UINT32,  # __parametersSize
                                                 _Pointer[_type.BYTE],  # parameters
                                                 _Pointer[ICryptographicKey]],  # key
                                                _type.HRESULT]


class IAsymmetricKeyAlgorithmProviderStatics(_inspectable.IInspectable):
    OpenAlgorithm: _Callable[[_type.HSTRING,  # algorithm
                              _Pointer[IAsymmetricKeyAlgorithmProvider]],  # provider
                             _type.HRESULT]

    _factory = True


class ICryptographicEngineStatics(_inspectable.IInspectable):
    Encrypt: _Callable[[ICryptographicKey,  # key
                        _Windows_Storage_Streams.IBuffer,  # data
                        _Windows_Storage_Streams.IBuffer,  # iv
                        _Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                       _type.HRESULT]
    Decrypt: _Callable[[ICryptographicKey,  # key
                        _Windows_Storage_Streams.IBuffer,  # data
                        _Windows_Storage_Streams.IBuffer,  # iv
                        _Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                       _type.HRESULT]
    EncryptAndAuthenticate: _Callable[[ICryptographicKey,  # key
                                       _Windows_Storage_Streams.IBuffer,  # data
                                       _Windows_Storage_Streams.IBuffer,  # nonce
                                       _Windows_Storage_Streams.IBuffer,  # authenticatedData
                                       _Pointer[IEncryptedAndAuthenticatedData]],  # value
                                      _type.HRESULT]
    DecryptAndAuthenticate: _Callable[[ICryptographicKey,  # key
                                       _Windows_Storage_Streams.IBuffer,  # data
                                       _Windows_Storage_Streams.IBuffer,  # nonce
                                       _Windows_Storage_Streams.IBuffer,  # authenticationTag
                                       _Windows_Storage_Streams.IBuffer,  # authenticatedData
                                       _Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                      _type.HRESULT]
    Sign: _Callable[[ICryptographicKey,  # key
                     _Windows_Storage_Streams.IBuffer,  # data
                     _Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                    _type.HRESULT]
    VerifySignature: _Callable[[ICryptographicKey,  # key
                                _Windows_Storage_Streams.IBuffer,  # data
                                _Windows_Storage_Streams.IBuffer,  # signature
                                _Pointer[_type.boolean]],  # isAuthenticated
                               _type.HRESULT]
    DeriveKeyMaterial: _Callable[[ICryptographicKey,  # key
                                  IKeyDerivationParameters,  # parameters
                                  _type.UINT32,  # desiredKeySize
                                  _Pointer[_Windows_Storage_Streams.IBuffer]],  # keyMaterial
                                 _type.HRESULT]

    _factory = True


class ICryptographicEngineStatics2(_inspectable.IInspectable):
    SignHashedData: _Callable[[ICryptographicKey,  # key
                               _Windows_Storage_Streams.IBuffer,  # data
                               _Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                              _type.HRESULT]
    VerifySignatureWithHashInput: _Callable[[ICryptographicKey,  # key
                                             _Windows_Storage_Streams.IBuffer,  # data
                                             _Windows_Storage_Streams.IBuffer,  # signature
                                             _Pointer[_type.boolean]],  # isAuthenticated
                                            _type.HRESULT]
    DecryptAsync: _Callable[[ICryptographicKey,  # key
                             _Windows_Storage_Streams.IBuffer,  # data
                             _Windows_Storage_Streams.IBuffer,  # iv
                             _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IBuffer]]],  # value
                            _type.HRESULT]
    SignAsync: _Callable[[ICryptographicKey,  # key
                          _Windows_Storage_Streams.IBuffer,  # data
                          _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IBuffer]]],  # value
                         _type.HRESULT]
    SignHashedDataAsync: _Callable[[ICryptographicKey,  # key
                                    _Windows_Storage_Streams.IBuffer,  # data
                                    _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IBuffer]]],  # value
                                   _type.HRESULT]

    _factory = True


class ICryptographicKey(_inspectable.IInspectable):
    get_KeySize: _Callable[[_Pointer[_type.UINT32]],  # value
                           _type.HRESULT]
    ExportDefaultPrivateKeyBlobType: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                               _type.HRESULT]
    ExportPrivateKeyWithBlobType: _Callable[[_enum.Windows.Security.Cryptography.Core.CryptographicPrivateKeyBlobType,  # BlobType
                                             _Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                            _type.HRESULT]
    ExportDefaultPublicKeyBlobType: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                              _type.HRESULT]
    ExportPublicKeyWithBlobType: _Callable[[_enum.Windows.Security.Cryptography.Core.CryptographicPublicKeyBlobType,  # BlobType
                                            _Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                           _type.HRESULT]


class IEccCurveNamesStatics(_inspectable.IInspectable):
    get_BrainpoolP160r1: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_BrainpoolP160t1: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_BrainpoolP192r1: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_BrainpoolP192t1: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_BrainpoolP224r1: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_BrainpoolP224t1: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_BrainpoolP256r1: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_BrainpoolP256t1: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_BrainpoolP320r1: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_BrainpoolP320t1: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_BrainpoolP384r1: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_BrainpoolP384t1: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_BrainpoolP512r1: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_BrainpoolP512t1: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_Curve25519: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_Ec192wapi: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_NistP192: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_NistP224: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_NistP256: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_NistP384: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_NistP521: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_NumsP256t1: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_NumsP384t1: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_NumsP512t1: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_SecP160k1: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_SecP160r1: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_SecP160r2: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_SecP192k1: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_SecP192r1: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_SecP224k1: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_SecP224r1: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_SecP256k1: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_SecP256r1: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_SecP384r1: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_SecP521r1: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_Wtls7: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Wtls9: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Wtls12: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_X962P192v1: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_X962P192v2: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_X962P192v3: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_X962P239v1: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_X962P239v2: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_X962P239v3: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_X962P256v1: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_AllEccCurveNames: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                    _type.HRESULT]

    _factory = True


class IEncryptedAndAuthenticatedData(_inspectable.IInspectable):
    get_EncryptedData: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                 _type.HRESULT]
    get_AuthenticationTag: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                     _type.HRESULT]


class IHashAlgorithmNamesStatics(_inspectable.IInspectable):
    get_Md5: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_Sha1: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Sha256: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Sha384: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Sha512: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]

    _factory = True


class IHashAlgorithmProvider(_inspectable.IInspectable):
    get_AlgorithmName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_HashLength: _Callable[[_Pointer[_type.UINT32]],  # value
                              _type.HRESULT]
    HashData: _Callable[[_Windows_Storage_Streams.IBuffer,  # data
                         _Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                        _type.HRESULT]
    CreateHash: _Callable[[_Pointer[IHashComputation]],  # Value
                          _type.HRESULT]


class IHashAlgorithmProviderStatics(_inspectable.IInspectable):
    OpenAlgorithm: _Callable[[_type.HSTRING,  # algorithm
                              _Pointer[IHashAlgorithmProvider]],  # provider
                             _type.HRESULT]

    _factory = True


class IHashComputation(_inspectable.IInspectable):
    Append: _Callable[[_Windows_Storage_Streams.IBuffer],  # data
                      _type.HRESULT]
    GetValueAndReset: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                _type.HRESULT]


class IKeyDerivationAlgorithmNamesStatics(_inspectable.IInspectable):
    get_Pbkdf2Md5: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_Pbkdf2Sha1: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_Pbkdf2Sha256: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_Pbkdf2Sha384: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_Pbkdf2Sha512: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_Sp800108CtrHmacMd5: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_Sp800108CtrHmacSha1: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    get_Sp800108CtrHmacSha256: _Callable[[_Pointer[_type.HSTRING]],  # value
                                         _type.HRESULT]
    get_Sp800108CtrHmacSha384: _Callable[[_Pointer[_type.HSTRING]],  # value
                                         _type.HRESULT]
    get_Sp800108CtrHmacSha512: _Callable[[_Pointer[_type.HSTRING]],  # value
                                         _type.HRESULT]
    get_Sp80056aConcatMd5: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    get_Sp80056aConcatSha1: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_Sp80056aConcatSha256: _Callable[[_Pointer[_type.HSTRING]],  # value
                                        _type.HRESULT]
    get_Sp80056aConcatSha384: _Callable[[_Pointer[_type.HSTRING]],  # value
                                        _type.HRESULT]
    get_Sp80056aConcatSha512: _Callable[[_Pointer[_type.HSTRING]],  # value
                                        _type.HRESULT]

    _factory = True


class IKeyDerivationAlgorithmNamesStatics2(_inspectable.IInspectable):
    get_CapiKdfMd5: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_CapiKdfSha1: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_CapiKdfSha256: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_CapiKdfSha384: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_CapiKdfSha512: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]

    _factory = True


class IKeyDerivationAlgorithmProvider(_inspectable.IInspectable):
    get_AlgorithmName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    CreateKey: _Callable[[_Windows_Storage_Streams.IBuffer,  # keyMaterial
                          _Pointer[ICryptographicKey]],  # key
                         _type.HRESULT]


class IKeyDerivationAlgorithmProviderStatics(_inspectable.IInspectable):
    OpenAlgorithm: _Callable[[_type.HSTRING,  # algorithm
                              _Pointer[IKeyDerivationAlgorithmProvider]],  # provider
                             _type.HRESULT]

    _factory = True


class IKeyDerivationParameters(_inspectable.IInspectable):
    get_KdfGenericBinary: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                    _type.HRESULT]
    put_KdfGenericBinary: _Callable[[_Windows_Storage_Streams.IBuffer],  # value
                                    _type.HRESULT]
    get_IterationCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]


class IKeyDerivationParameters2(_inspectable.IInspectable):
    get_Capi1KdfTargetAlgorithm: _Callable[[_Pointer[_enum.Windows.Security.Cryptography.Core.Capi1KdfTargetAlgorithm]],  # value
                                           _type.HRESULT]
    put_Capi1KdfTargetAlgorithm: _Callable[[_enum.Windows.Security.Cryptography.Core.Capi1KdfTargetAlgorithm],  # value
                                           _type.HRESULT]


class IKeyDerivationParametersStatics(_inspectable.IInspectable):
    BuildForPbkdf2: _Callable[[_Windows_Storage_Streams.IBuffer,  # pbkdf2Salt
                               _type.UINT32,  # iterationCount
                               _Pointer[IKeyDerivationParameters]],  # value
                              _type.HRESULT]
    BuildForSP800108: _Callable[[_Windows_Storage_Streams.IBuffer,  # label
                                 _Windows_Storage_Streams.IBuffer,  # context
                                 _Pointer[IKeyDerivationParameters]],  # value
                                _type.HRESULT]
    BuildForSP80056a: _Callable[[_Windows_Storage_Streams.IBuffer,  # algorithmId
                                 _Windows_Storage_Streams.IBuffer,  # partyUInfo
                                 _Windows_Storage_Streams.IBuffer,  # partyVInfo
                                 _Windows_Storage_Streams.IBuffer,  # suppPubInfo
                                 _Windows_Storage_Streams.IBuffer,  # suppPrivInfo
                                 _Pointer[IKeyDerivationParameters]],  # value
                                _type.HRESULT]

    _factory = True


class IKeyDerivationParametersStatics2(_inspectable.IInspectable):
    BuildForCapi1Kdf: _Callable[[_enum.Windows.Security.Cryptography.Core.Capi1KdfTargetAlgorithm,  # capi1KdfTargetAlgorithm
                                 _Pointer[IKeyDerivationParameters]],  # value
                                _type.HRESULT]

    _factory = True


class IMacAlgorithmNamesStatics(_inspectable.IInspectable):
    get_HmacMd5: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_HmacSha1: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_HmacSha256: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_HmacSha384: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_HmacSha512: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_AesCmac: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]

    _factory = True


class IMacAlgorithmProvider(_inspectable.IInspectable):
    get_AlgorithmName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_MacLength: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    CreateKey: _Callable[[_Windows_Storage_Streams.IBuffer,  # keyMaterial
                          _Pointer[ICryptographicKey]],  # macKey
                         _type.HRESULT]


class IMacAlgorithmProvider2(_inspectable.IInspectable):
    CreateHash: _Callable[[_Windows_Storage_Streams.IBuffer,  # keyMaterial
                           _Pointer[IHashComputation]],  # value
                          _type.HRESULT]


class IMacAlgorithmProviderStatics(_inspectable.IInspectable):
    OpenAlgorithm: _Callable[[_type.HSTRING,  # algorithm
                              _Pointer[IMacAlgorithmProvider]],  # provider
                             _type.HRESULT]

    _factory = True


class IPersistedKeyProviderStatics(_inspectable.IInspectable):
    OpenKeyPairFromCertificateAsync: _Callable[[_Windows_Security_Cryptography_Certificates.ICertificate,  # certificate
                                                _type.HSTRING,  # hashAlgorithmName
                                                _enum.Windows.Security.Cryptography.Core.CryptographicPadding,  # padding
                                                _Pointer[_Windows_Foundation.IAsyncOperation[ICryptographicKey]]],  # operation
                                               _type.HRESULT]
    OpenPublicKeyFromCertificate: _Callable[[_Windows_Security_Cryptography_Certificates.ICertificate,  # certificate
                                             _type.HSTRING,  # hashAlgorithmName
                                             _enum.Windows.Security.Cryptography.Core.CryptographicPadding,  # padding
                                             _Pointer[ICryptographicKey]],  # key
                                            _type.HRESULT]

    _factory = True


class ISymmetricAlgorithmNamesStatics(_inspectable.IInspectable):
    get_DesCbc: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_DesEcb: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_TripleDesCbc: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_TripleDesEcb: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_Rc2Cbc: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Rc2Ecb: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_AesCbc: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_AesEcb: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_AesGcm: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_AesCcm: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_AesCbcPkcs7: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_AesEcbPkcs7: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_DesCbcPkcs7: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_DesEcbPkcs7: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_TripleDesCbcPkcs7: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    get_TripleDesEcbPkcs7: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    get_Rc2CbcPkcs7: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Rc2EcbPkcs7: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Rc4: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]

    _factory = True


class ISymmetricKeyAlgorithmProvider(_inspectable.IInspectable):
    get_AlgorithmName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_BlockLength: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]
    CreateSymmetricKey: _Callable[[_Windows_Storage_Streams.IBuffer,  # keyMaterial
                                   _Pointer[ICryptographicKey]],  # key
                                  _type.HRESULT]


class ISymmetricKeyAlgorithmProviderStatics(_inspectable.IInspectable):
    OpenAlgorithm: _Callable[[_type.HSTRING,  # algorithm
                              _Pointer[ISymmetricKeyAlgorithmProvider]],  # provider
                             _type.HRESULT]

    _factory = True
