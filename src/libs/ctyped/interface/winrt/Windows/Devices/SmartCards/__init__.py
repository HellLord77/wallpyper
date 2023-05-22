from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from .....um import Unknwnbase as _Unknwnbase
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class _ISmartCardPinResetHandler:
    Invoke: _Callable[[ISmartCardProvisioning,  # sender
                       ISmartCardPinResetRequest],  # request
                      _type.HRESULT]


class ISmartCardPinResetHandler(_ISmartCardPinResetHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ISmartCardPinResetHandler_impl(_ISmartCardPinResetHandler, _Unknwnbase.IUnknown_impl):
    pass


class ICardAddedEventArgs(_inspectable.IInspectable):
    get_SmartCard: _Callable[[_Pointer[ISmartCard]],  # value
                             _type.HRESULT]


class ICardRemovedEventArgs(_inspectable.IInspectable):
    get_SmartCard: _Callable[[_Pointer[ISmartCard]],  # value
                             _type.HRESULT]


class IKnownSmartCardAppletIds(_inspectable.IInspectable, factory=True):
    get_PaymentSystemEnvironment: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                            _type.HRESULT]
    get_ProximityPaymentSystemEnvironment: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                                     _type.HRESULT]


class ISmartCard(_inspectable.IInspectable):
    get_Reader: _Callable[[_Pointer[ISmartCardReader]],  # value
                          _type.HRESULT]
    GetStatusAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Devices.SmartCards.SmartCardStatus]]],  # result
                              _type.HRESULT]
    GetAnswerToResetAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IBuffer]]],  # result
                                     _type.HRESULT]


class ISmartCardAppletIdGroup(_inspectable.IInspectable):
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_DisplayName: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_AppletIds: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_Storage_Streams.IBuffer]]],  # value
                             _type.HRESULT]
    get_SmartCardEmulationCategory: _Callable[[_Pointer[_enum.Windows.Devices.SmartCards.SmartCardEmulationCategory]],  # value
                                              _type.HRESULT]
    put_SmartCardEmulationCategory: _Callable[[_enum.Windows.Devices.SmartCards.SmartCardEmulationCategory],  # value
                                              _type.HRESULT]
    get_SmartCardEmulationType: _Callable[[_Pointer[_enum.Windows.Devices.SmartCards.SmartCardEmulationType]],  # value
                                          _type.HRESULT]
    put_SmartCardEmulationType: _Callable[[_enum.Windows.Devices.SmartCards.SmartCardEmulationType],  # value
                                          _type.HRESULT]
    get_AutomaticEnablement: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_AutomaticEnablement: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]


class ISmartCardAppletIdGroup2(_inspectable.IInspectable):
    get_Logo: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # value
                        _type.HRESULT]
    put_Logo: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference],  # value
                        _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                              _type.HRESULT]
    get_SecureUserAuthenticationRequired: _Callable[[_Pointer[_type.boolean]],  # value
                                                    _type.HRESULT]
    put_SecureUserAuthenticationRequired: _Callable[[_type.boolean],  # value
                                                    _type.HRESULT]


class ISmartCardAppletIdGroupFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.HSTRING,  # displayName
                       _Windows_Foundation_Collections.IVector[_Windows_Storage_Streams.IBuffer],  # appletIds
                       _enum.Windows.Devices.SmartCards.SmartCardEmulationCategory,  # emulationCategory
                       _enum.Windows.Devices.SmartCards.SmartCardEmulationType,  # emulationType
                       _Pointer[ISmartCardAppletIdGroup]],  # result
                      _type.HRESULT]


class ISmartCardAppletIdGroupRegistration(_inspectable.IInspectable):
    get_ActivationPolicy: _Callable[[_Pointer[_enum.Windows.Devices.SmartCards.SmartCardAppletIdGroupActivationPolicy]],  # value
                                    _type.HRESULT]
    get_AppletIdGroup: _Callable[[_Pointer[ISmartCardAppletIdGroup]],  # value
                                 _type.HRESULT]
    RequestActivationPolicyChangeAsync: _Callable[[_enum.Windows.Devices.SmartCards.SmartCardAppletIdGroupActivationPolicy,  # policy
                                                   _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Devices.SmartCards.SmartCardActivationPolicyChangeResult]]],  # result
                                                  _type.HRESULT]
    get_Id: _Callable[[_Pointer[_struct.GUID]],  # value
                      _type.HRESULT]
    SetAutomaticResponseApdusAsync: _Callable[[_Windows_Foundation_Collections.IIterable[ISmartCardAutomaticResponseApdu],  # apdus
                                               _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                              _type.HRESULT]


class ISmartCardAppletIdGroupRegistration2(_inspectable.IInspectable):
    get_SmartCardReaderId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    SetPropertiesAsync: _Callable[[_Windows_Foundation_Collections.IPropertySet,  # props
                                   _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                  _type.HRESULT]


class ISmartCardAppletIdGroupStatics(_inspectable.IInspectable, factory=True):
    get_MaxAppletIds: _Callable[[_Pointer[_type.UINT16]],  # value
                                _type.HRESULT]


class ISmartCardAutomaticResponseApdu(_inspectable.IInspectable):
    get_CommandApdu: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                               _type.HRESULT]
    put_CommandApdu: _Callable[[_Windows_Storage_Streams.IBuffer],  # value
                               _type.HRESULT]
    get_CommandApduBitMask: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                      _type.HRESULT]
    put_CommandApduBitMask: _Callable[[_Windows_Storage_Streams.IBuffer],  # value
                                      _type.HRESULT]
    get_ShouldMatchLength: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    put_ShouldMatchLength: _Callable[[_type.boolean],  # value
                                     _type.HRESULT]
    get_AppletId: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                            _type.HRESULT]
    put_AppletId: _Callable[[_Windows_Storage_Streams.IBuffer],  # value
                            _type.HRESULT]
    get_ResponseApdu: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                _type.HRESULT]
    put_ResponseApdu: _Callable[[_Windows_Storage_Streams.IBuffer],  # value
                                _type.HRESULT]


class ISmartCardAutomaticResponseApdu2(_inspectable.IInspectable):
    get_InputState: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                              _type.HRESULT]
    put_InputState: _Callable[[_Windows_Foundation.IReference[_type.UINT32]],  # value
                              _type.HRESULT]
    get_OutputState: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                               _type.HRESULT]
    put_OutputState: _Callable[[_Windows_Foundation.IReference[_type.UINT32]],  # value
                               _type.HRESULT]


class ISmartCardAutomaticResponseApdu3(_inspectable.IInspectable):
    get_AllowWhenCryptogramGeneratorNotPrepared: _Callable[[_Pointer[_type.boolean]],  # value
                                                           _type.HRESULT]
    put_AllowWhenCryptogramGeneratorNotPrepared: _Callable[[_type.boolean],  # value
                                                           _type.HRESULT]


class ISmartCardAutomaticResponseApduFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Windows_Storage_Streams.IBuffer,  # commandApdu
                       _Windows_Storage_Streams.IBuffer,  # responseApdu
                       _Pointer[ISmartCardAutomaticResponseApdu]],  # result
                      _type.HRESULT]


class ISmartCardChallengeContext(_inspectable.IInspectable):
    get_Challenge: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                             _type.HRESULT]
    VerifyResponseAsync: _Callable[[_Windows_Storage_Streams.IBuffer,  # response
                                    _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                   _type.HRESULT]
    ProvisionAsync: _Callable[[_Windows_Storage_Streams.IBuffer,  # response
                               _type.boolean,  # formatCard
                               _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                              _type.HRESULT]
    ProvisionAsyncWithNewCardId: _Callable[[_Windows_Storage_Streams.IBuffer,  # response
                                            _type.boolean,  # formatCard
                                            _struct.GUID,  # newCardId
                                            _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                           _type.HRESULT]
    ChangeAdministrativeKeyAsync: _Callable[[_Windows_Storage_Streams.IBuffer,  # response
                                             _Windows_Storage_Streams.IBuffer,  # newAdministrativeKey
                                             _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                            _type.HRESULT]


class ISmartCardConnect(_inspectable.IInspectable):
    ConnectAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[ISmartCardConnection]]],  # result
                            _type.HRESULT]


class ISmartCardConnection(_inspectable.IInspectable):
    TransmitAsync: _Callable[[_Windows_Storage_Streams.IBuffer,  # command
                              _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IBuffer]]],  # result
                             _type.HRESULT]


class ISmartCardCryptogramGenerator(_inspectable.IInspectable):
    get_SupportedCryptogramMaterialTypes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Devices.SmartCards.SmartCardCryptogramMaterialType]]],  # result
                                                    _type.HRESULT]
    get_SupportedCryptogramAlgorithms: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Devices.SmartCards.SmartCardCryptogramAlgorithm]]],  # result
                                                 _type.HRESULT]
    get_SupportedCryptogramMaterialPackageFormats: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageFormat]]],  # result
                                                             _type.HRESULT]
    get_SupportedCryptogramMaterialPackageConfirmationResponseFormats: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageConfirmationResponseFormat]]],  # result
                                                                                 _type.HRESULT]
    get_SupportedSmartCardCryptogramStorageKeyCapabilities: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyCapabilities]]],  # result
                                                                      _type.HRESULT]
    DeleteCryptogramMaterialStorageKeyAsync: _Callable[[_type.HSTRING,  # storageKeyName
                                                        _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]]],  # result
                                                       _type.HRESULT]
    CreateCryptogramMaterialStorageKeyAsync: _Callable[[_enum.Windows.Devices.SmartCards.SmartCardUnlockPromptingBehavior,  # promptingBehavior
                                                        _type.HSTRING,  # storageKeyName
                                                        _enum.Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyAlgorithm,  # algorithm
                                                        _enum.Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyCapabilities,  # capabilities
                                                        _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]]],  # result
                                                       _type.HRESULT]
    RequestCryptogramMaterialStorageKeyInfoAsync: _Callable[[_enum.Windows.Devices.SmartCards.SmartCardUnlockPromptingBehavior,  # promptingBehavior
                                                             _type.HSTRING,  # storageKeyName
                                                             _enum.Windows.Security.Cryptography.Core.CryptographicPublicKeyBlobType,  # format
                                                             _Pointer[_Windows_Foundation.IAsyncOperation[ISmartCardCryptogramStorageKeyInfo]]],  # result
                                                            _type.HRESULT]
    ImportCryptogramMaterialPackageAsync: _Callable[[_enum.Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageFormat,  # format
                                                     _type.HSTRING,  # storageKeyName
                                                     _type.HSTRING,  # materialPackageName
                                                     _Windows_Storage_Streams.IBuffer,  # cryptogramMaterialPackage
                                                     _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]]],  # result
                                                    _type.HRESULT]
    TryProvePossessionOfCryptogramMaterialPackageAsync: _Callable[[_enum.Windows.Devices.SmartCards.SmartCardUnlockPromptingBehavior,  # promptingBehavior
                                                                   _enum.Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageConfirmationResponseFormat,  # responseFormat
                                                                   _type.HSTRING,  # materialPackageName
                                                                   _type.HSTRING,  # materialName
                                                                   _Windows_Storage_Streams.IBuffer,  # challenge
                                                                   _Pointer[_Windows_Foundation.IAsyncOperation[ISmartCardCryptogramMaterialPossessionProof]]],  # result
                                                                  _type.HRESULT]
    RequestUnlockCryptogramMaterialForUseAsync: _Callable[[_enum.Windows.Devices.SmartCards.SmartCardUnlockPromptingBehavior,  # promptingBehavior
                                                           _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]]],  # result
                                                          _type.HRESULT]
    DeleteCryptogramMaterialPackageAsync: _Callable[[_type.HSTRING,  # materialPackageName
                                                     _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]]],  # result
                                                    _type.HRESULT]


class ISmartCardCryptogramGenerator2(_inspectable.IInspectable):
    ValidateRequestApduAsync: _Callable[[_enum.Windows.Devices.SmartCards.SmartCardUnlockPromptingBehavior,  # promptingBehavior
                                         _Windows_Storage_Streams.IBuffer,  # apduToValidate
                                         _Windows_Foundation_Collections.IIterable[ISmartCardCryptogramPlacementStep],  # cryptogramPlacementSteps
                                         _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]]],  # result
                                        _type.HRESULT]
    GetAllCryptogramStorageKeyCharacteristicsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[ISmartCardCryptogramGetAllCryptogramStorageKeyCharacteristicsResult]]],  # result
                                                              _type.HRESULT]
    GetAllCryptogramMaterialPackageCharacteristicsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[ISmartCardCryptogramGetAllCryptogramMaterialPackageCharacteristicsResult]]],  # result
                                                                   _type.HRESULT]
    GetAllCryptogramMaterialPackageCharacteristicsWithStorageKeyAsync: _Callable[[_type.HSTRING,  # storageKeyName
                                                                                  _Pointer[_Windows_Foundation.IAsyncOperation[ISmartCardCryptogramGetAllCryptogramMaterialPackageCharacteristicsResult]]],  # result
                                                                                 _type.HRESULT]
    GetAllCryptogramMaterialCharacteristicsAsync: _Callable[[_enum.Windows.Devices.SmartCards.SmartCardUnlockPromptingBehavior,  # promptingBehavior
                                                             _type.HSTRING,  # materialPackageName
                                                             _Pointer[_Windows_Foundation.IAsyncOperation[ISmartCardCryptogramGetAllCryptogramMaterialCharacteristicsResult]]],  # result
                                                            _type.HRESULT]


class ISmartCardCryptogramGeneratorStatics(_inspectable.IInspectable, factory=True):
    GetSmartCardCryptogramGeneratorAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[ISmartCardCryptogramGenerator]]],  # result
                                                    _type.HRESULT]


class ISmartCardCryptogramGeneratorStatics2(_inspectable.IInspectable, factory=True):
    IsSupported: _Callable[[_Pointer[_type.boolean]],  # result
                           _type.HRESULT]


class ISmartCardCryptogramGetAllCryptogramMaterialCharacteristicsResult(_inspectable.IInspectable):
    get_OperationStatus: _Callable[[_Pointer[_enum.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]],  # value
                                   _type.HRESULT]
    get_Characteristics: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[ISmartCardCryptogramMaterialCharacteristics]]],  # value
                                   _type.HRESULT]


class ISmartCardCryptogramGetAllCryptogramMaterialPackageCharacteristicsResult(_inspectable.IInspectable):
    get_OperationStatus: _Callable[[_Pointer[_enum.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]],  # value
                                   _type.HRESULT]
    get_Characteristics: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[ISmartCardCryptogramMaterialPackageCharacteristics]]],  # value
                                   _type.HRESULT]


class ISmartCardCryptogramGetAllCryptogramStorageKeyCharacteristicsResult(_inspectable.IInspectable):
    get_OperationStatus: _Callable[[_Pointer[_enum.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]],  # value
                                   _type.HRESULT]
    get_Characteristics: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[ISmartCardCryptogramStorageKeyCharacteristics]]],  # value
                                   _type.HRESULT]


class ISmartCardCryptogramMaterialCharacteristics(_inspectable.IInspectable):
    get_MaterialName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_AllowedAlgorithms: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Devices.SmartCards.SmartCardCryptogramAlgorithm]]],  # value
                                     _type.HRESULT]
    get_AllowedProofOfPossessionAlgorithms: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageConfirmationResponseFormat]]],  # value
                                                      _type.HRESULT]
    get_AllowedValidations: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Devices.SmartCards.SmartCardCryptogramAlgorithm]]],  # value
                                      _type.HRESULT]
    get_MaterialType: _Callable[[_Pointer[_enum.Windows.Devices.SmartCards.SmartCardCryptogramMaterialType]],  # value
                                _type.HRESULT]
    get_ProtectionMethod: _Callable[[_Pointer[_enum.Windows.Devices.SmartCards.SmartCardCryptogramMaterialProtectionMethod]],  # value
                                    _type.HRESULT]
    get_ProtectionVersion: _Callable[[_Pointer[_type.INT32]],  # value
                                     _type.HRESULT]
    get_MaterialLength: _Callable[[_Pointer[_type.INT32]],  # value
                                  _type.HRESULT]


class ISmartCardCryptogramMaterialPackageCharacteristics(_inspectable.IInspectable):
    get_PackageName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_StorageKeyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_DateImported: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                _type.HRESULT]
    get_PackageFormat: _Callable[[_Pointer[_enum.Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageFormat]],  # value
                                 _type.HRESULT]


class ISmartCardCryptogramMaterialPossessionProof(_inspectable.IInspectable):
    get_OperationStatus: _Callable[[_Pointer[_enum.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]],  # value
                                   _type.HRESULT]
    get_Proof: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                         _type.HRESULT]


class ISmartCardCryptogramPlacementStep(_inspectable.IInspectable):
    get_Algorithm: _Callable[[_Pointer[_enum.Windows.Devices.SmartCards.SmartCardCryptogramAlgorithm]],  # value
                             _type.HRESULT]
    put_Algorithm: _Callable[[_enum.Windows.Devices.SmartCards.SmartCardCryptogramAlgorithm],  # value
                             _type.HRESULT]
    get_SourceData: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                              _type.HRESULT]
    put_SourceData: _Callable[[_Windows_Storage_Streams.IBuffer],  # value
                              _type.HRESULT]
    get_CryptogramMaterialPackageName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                                 _type.HRESULT]
    put_CryptogramMaterialPackageName: _Callable[[_type.HSTRING],  # value
                                                 _type.HRESULT]
    get_CryptogramMaterialName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                          _type.HRESULT]
    put_CryptogramMaterialName: _Callable[[_type.HSTRING],  # value
                                          _type.HRESULT]
    get_TemplateOffset: _Callable[[_Pointer[_type.INT32]],  # value
                                  _type.HRESULT]
    put_TemplateOffset: _Callable[[_type.INT32],  # value
                                  _type.HRESULT]
    get_CryptogramOffset: _Callable[[_Pointer[_type.INT32]],  # value
                                    _type.HRESULT]
    put_CryptogramOffset: _Callable[[_type.INT32],  # value
                                    _type.HRESULT]
    get_CryptogramLength: _Callable[[_Pointer[_type.INT32]],  # value
                                    _type.HRESULT]
    put_CryptogramLength: _Callable[[_type.INT32],  # value
                                    _type.HRESULT]
    get_CryptogramPlacementOptions: _Callable[[_Pointer[_enum.Windows.Devices.SmartCards.SmartCardCryptogramPlacementOptions]],  # value
                                              _type.HRESULT]
    put_CryptogramPlacementOptions: _Callable[[_enum.Windows.Devices.SmartCards.SmartCardCryptogramPlacementOptions],  # value
                                              _type.HRESULT]
    get_ChainedOutputStep: _Callable[[_Pointer[ISmartCardCryptogramPlacementStep]],  # value
                                     _type.HRESULT]
    put_ChainedOutputStep: _Callable[[ISmartCardCryptogramPlacementStep],  # value
                                     _type.HRESULT]


class ISmartCardCryptogramStorageKeyCharacteristics(_inspectable.IInspectable):
    get_StorageKeyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_DateCreated: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                               _type.HRESULT]
    get_Algorithm: _Callable[[_Pointer[_enum.Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyAlgorithm]],  # value
                             _type.HRESULT]
    get_Capabilities: _Callable[[_Pointer[_enum.Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyCapabilities]],  # value
                                _type.HRESULT]


class ISmartCardCryptogramStorageKeyInfo(_inspectable.IInspectable):
    get_OperationStatus: _Callable[[_Pointer[_enum.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]],  # value
                                   _type.HRESULT]
    get_PublicKeyBlobType: _Callable[[_Pointer[_enum.Windows.Security.Cryptography.Core.CryptographicPublicKeyBlobType]],  # value
                                     _type.HRESULT]
    get_PublicKey: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                             _type.HRESULT]
    get_AttestationStatus: _Callable[[_Pointer[_enum.Windows.Devices.SmartCards.SmartCardCryptographicKeyAttestationStatus]],  # value
                                     _type.HRESULT]
    get_Attestation: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                               _type.HRESULT]
    get_AttestationCertificateChain: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                               _type.HRESULT]
    get_Capabilities: _Callable[[_Pointer[_enum.Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyCapabilities]],  # value
                                _type.HRESULT]


class ISmartCardCryptogramStorageKeyInfo2(_inspectable.IInspectable):
    get_OperationalRequirements: _Callable[[_Pointer[_type.HSTRING]],  # value
                                           _type.HRESULT]


class ISmartCardEmulator(_inspectable.IInspectable):
    get_EnablementPolicy: _Callable[[_Pointer[_enum.Windows.Devices.SmartCards.SmartCardEmulatorEnablementPolicy]],  # value
                                    _type.HRESULT]


class ISmartCardEmulator2(_inspectable.IInspectable):
    add_ApduReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[ISmartCardEmulator, ISmartCardEmulatorApduReceivedEventArgs],  # value
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_ApduReceived: _Callable[[_struct.EventRegistrationToken],  # value
                                   _type.HRESULT]
    add_ConnectionDeactivated: _Callable[[_Windows_Foundation.ITypedEventHandler[ISmartCardEmulator, ISmartCardEmulatorConnectionDeactivatedEventArgs],  # value
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_ConnectionDeactivated: _Callable[[_struct.EventRegistrationToken],  # value
                                            _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    IsHostCardEmulationSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]


class ISmartCardEmulatorApduReceivedEventArgs(_inspectable.IInspectable):
    get_CommandApdu: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                               _type.HRESULT]
    get_ConnectionProperties: _Callable[[_Pointer[ISmartCardEmulatorConnectionProperties]],  # value
                                        _type.HRESULT]
    TryRespondAsync: _Callable[[_Windows_Storage_Streams.IBuffer,  # responseApdu
                                _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                               _type.HRESULT]
    get_AutomaticResponseStatus: _Callable[[_Pointer[_enum.Windows.Devices.SmartCards.SmartCardAutomaticResponseStatus]],  # value
                                           _type.HRESULT]


class ISmartCardEmulatorApduReceivedEventArgs2(_inspectable.IInspectable):
    get_State: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    TryRespondWithStateAsync: _Callable[[_Windows_Storage_Streams.IBuffer,  # responseApdu
                                         _Windows_Foundation.IReference[_type.UINT32],  # nextState
                                         _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                        _type.HRESULT]


class ISmartCardEmulatorApduReceivedEventArgsWithCryptograms(_inspectable.IInspectable):
    TryRespondWithCryptogramsAsync: _Callable[[_Windows_Storage_Streams.IBuffer,  # responseTemplate
                                               _Windows_Foundation_Collections.IIterable[ISmartCardCryptogramPlacementStep],  # cryptogramPlacementSteps
                                               _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]]],  # result
                                              _type.HRESULT]
    TryRespondWithCryptogramsAndStateAsync: _Callable[[_Windows_Storage_Streams.IBuffer,  # responseTemplate
                                                       _Windows_Foundation_Collections.IIterable[ISmartCardCryptogramPlacementStep],  # cryptogramPlacementSteps
                                                       _Windows_Foundation.IReference[_type.UINT32],  # nextState
                                                       _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]]],  # result
                                                      _type.HRESULT]


class ISmartCardEmulatorConnectionDeactivatedEventArgs(_inspectable.IInspectable):
    get_ConnectionProperties: _Callable[[_Pointer[ISmartCardEmulatorConnectionProperties]],  # value
                                        _type.HRESULT]
    get_Reason: _Callable[[_Pointer[_enum.Windows.Devices.SmartCards.SmartCardEmulatorConnectionDeactivatedReason]],  # value
                          _type.HRESULT]


class ISmartCardEmulatorConnectionProperties(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_struct.GUID]],  # value
                      _type.HRESULT]
    get_Source: _Callable[[_Pointer[_enum.Windows.Devices.SmartCards.SmartCardEmulatorConnectionSource]],  # value
                          _type.HRESULT]


class ISmartCardEmulatorStatics(_inspectable.IInspectable, factory=True):
    GetDefaultAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[ISmartCardEmulator]]],  # result
                               _type.HRESULT]


class ISmartCardEmulatorStatics2(_inspectable.IInspectable, factory=True):
    GetAppletIdGroupRegistrationsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[ISmartCardAppletIdGroupRegistration]]]],  # result
                                                  _type.HRESULT]
    RegisterAppletIdGroupAsync: _Callable[[ISmartCardAppletIdGroup,  # appletIdGroup
                                           _Pointer[_Windows_Foundation.IAsyncOperation[ISmartCardAppletIdGroupRegistration]]],  # result
                                          _type.HRESULT]
    UnregisterAppletIdGroupAsync: _Callable[[ISmartCardAppletIdGroupRegistration,  # registration
                                             _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                            _type.HRESULT]
    get_MaxAppletIdGroupRegistrations: _Callable[[_Pointer[_type.UINT16]],  # value
                                                 _type.HRESULT]


class ISmartCardEmulatorStatics3(_inspectable.IInspectable, factory=True):
    IsSupported: _Callable[[_Pointer[_type.boolean]],  # result
                           _type.HRESULT]


class ISmartCardPinPolicy(_inspectable.IInspectable):
    get_MinLength: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    put_MinLength: _Callable[[_type.UINT32],  # value
                             _type.HRESULT]
    get_MaxLength: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    put_MaxLength: _Callable[[_type.UINT32],  # value
                             _type.HRESULT]
    get_UppercaseLetters: _Callable[[_Pointer[_enum.Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption]],  # value
                                    _type.HRESULT]
    put_UppercaseLetters: _Callable[[_enum.Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption],  # value
                                    _type.HRESULT]
    get_LowercaseLetters: _Callable[[_Pointer[_enum.Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption]],  # value
                                    _type.HRESULT]
    put_LowercaseLetters: _Callable[[_enum.Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption],  # value
                                    _type.HRESULT]
    get_Digits: _Callable[[_Pointer[_enum.Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption]],  # value
                          _type.HRESULT]
    put_Digits: _Callable[[_enum.Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption],  # value
                          _type.HRESULT]
    get_SpecialCharacters: _Callable[[_Pointer[_enum.Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption]],  # value
                                     _type.HRESULT]
    put_SpecialCharacters: _Callable[[_enum.Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption],  # value
                                     _type.HRESULT]


class ISmartCardPinResetDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class ISmartCardPinResetRequest(_inspectable.IInspectable):
    get_Challenge: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                             _type.HRESULT]
    get_Deadline: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                            _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[ISmartCardPinResetDeferral]],  # result
                           _type.HRESULT]
    SetResponse: _Callable[[_Windows_Storage_Streams.IBuffer],  # response
                           _type.HRESULT]


class ISmartCardProvisioning(_inspectable.IInspectable):
    get_SmartCard: _Callable[[_Pointer[ISmartCard]],  # value
                             _type.HRESULT]
    GetIdAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_struct.GUID]]],  # result
                          _type.HRESULT]
    GetNameAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # result
                            _type.HRESULT]
    GetChallengeContextAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[ISmartCardChallengeContext]]],  # result
                                        _type.HRESULT]
    RequestPinChangeAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                     _type.HRESULT]
    RequestPinResetAsync: _Callable[[ISmartCardPinResetHandler,  # handler
                                     _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                    _type.HRESULT]


class ISmartCardProvisioning2(_inspectable.IInspectable):
    GetAuthorityKeyContainerNameAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # result
                                                 _type.HRESULT]


class ISmartCardProvisioningStatics(_inspectable.IInspectable, factory=True):
    FromSmartCardAsync: _Callable[[ISmartCard,  # card
                                   _Pointer[_Windows_Foundation.IAsyncOperation[ISmartCardProvisioning]]],  # result
                                  _type.HRESULT]
    RequestVirtualSmartCardCreationAsync: _Callable[[_type.HSTRING,  # friendlyName
                                                     _Windows_Storage_Streams.IBuffer,  # administrativeKey
                                                     ISmartCardPinPolicy,  # pinPolicy
                                                     _Pointer[_Windows_Foundation.IAsyncOperation[ISmartCardProvisioning]]],  # result
                                                    _type.HRESULT]
    RequestVirtualSmartCardCreationAsyncWithCardId: _Callable[[_type.HSTRING,  # friendlyName
                                                               _Windows_Storage_Streams.IBuffer,  # administrativeKey
                                                               ISmartCardPinPolicy,  # pinPolicy
                                                               _struct.GUID,  # cardId
                                                               _Pointer[_Windows_Foundation.IAsyncOperation[ISmartCardProvisioning]]],  # result
                                                              _type.HRESULT]
    RequestVirtualSmartCardDeletionAsync: _Callable[[ISmartCard,  # card
                                                     _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                                    _type.HRESULT]


class ISmartCardProvisioningStatics2(_inspectable.IInspectable, factory=True):
    RequestAttestedVirtualSmartCardCreationAsync: _Callable[[_type.HSTRING,  # friendlyName
                                                             _Windows_Storage_Streams.IBuffer,  # administrativeKey
                                                             ISmartCardPinPolicy,  # pinPolicy
                                                             _Pointer[_Windows_Foundation.IAsyncOperation[ISmartCardProvisioning]]],  # result
                                                            _type.HRESULT]
    RequestAttestedVirtualSmartCardCreationAsyncWithCardId: _Callable[[_type.HSTRING,  # friendlyName
                                                                       _Windows_Storage_Streams.IBuffer,  # administrativeKey
                                                                       ISmartCardPinPolicy,  # pinPolicy
                                                                       _struct.GUID,  # cardId
                                                                       _Pointer[_Windows_Foundation.IAsyncOperation[ISmartCardProvisioning]]],  # result
                                                                      _type.HRESULT]


class ISmartCardReader(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Kind: _Callable[[_Pointer[_enum.Windows.Devices.SmartCards.SmartCardReaderKind]],  # value
                        _type.HRESULT]
    GetStatusAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Devices.SmartCards.SmartCardReaderStatus]]],  # result
                              _type.HRESULT]
    FindAllCardsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[ISmartCard]]]],  # result
                                 _type.HRESULT]
    add_CardAdded: _Callable[[_Windows_Foundation.ITypedEventHandler[ISmartCardReader, ICardAddedEventArgs],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_CardAdded: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    add_CardRemoved: _Callable[[_Windows_Foundation.ITypedEventHandler[ISmartCardReader, ICardRemovedEventArgs],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_CardRemoved: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]


class ISmartCardReaderStatics(_inspectable.IInspectable, factory=True):
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # selector
                                 _type.HRESULT]
    GetDeviceSelectorWithKind: _Callable[[_enum.Windows.Devices.SmartCards.SmartCardReaderKind,  # kind
                                          _Pointer[_type.HSTRING]],  # selector
                                         _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[ISmartCardReader]]],  # result
                           _type.HRESULT]


class ISmartCardTriggerDetails(_inspectable.IInspectable):
    get_TriggerType: _Callable[[_Pointer[_enum.Windows.Devices.SmartCards.SmartCardTriggerType]],  # value
                               _type.HRESULT]
    get_SourceAppletId: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                  _type.HRESULT]
    get_TriggerData: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                               _type.HRESULT]


class ISmartCardTriggerDetails2(_inspectable.IInspectable):
    get_Emulator: _Callable[[_Pointer[ISmartCardEmulator]],  # value
                            _type.HRESULT]
    TryLaunchCurrentAppAsync: _Callable[[_type.HSTRING,  # arguments
                                         _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                        _type.HRESULT]
    TryLaunchCurrentAppWithBehaviorAsync: _Callable[[_type.HSTRING,  # arguments
                                                     _enum.Windows.Devices.SmartCards.SmartCardLaunchBehavior,  # behavior
                                                     _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                                    _type.HRESULT]


class ISmartCardTriggerDetails3(_inspectable.IInspectable):
    get_SmartCard: _Callable[[_Pointer[ISmartCard]],  # value
                             _type.HRESULT]
