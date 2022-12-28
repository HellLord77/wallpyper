from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IEasClientDeviceInformation(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_struct.GUID]],  # value
                      _type.HRESULT]
    get_OperatingSystem: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_FriendlyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_SystemManufacturer: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_SystemProductName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    get_SystemSku: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]


class IEasClientDeviceInformation2(_inspectable.IInspectable):
    get_SystemHardwareVersion: _Callable[[_Pointer[_type.HSTRING]],  # value
                                         _type.HRESULT]
    get_SystemFirmwareVersion: _Callable[[_Pointer[_type.HSTRING]],  # value
                                         _type.HRESULT]


class IEasClientSecurityPolicy(_inspectable.IInspectable):
    get_RequireEncryption: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    put_RequireEncryption: _Callable[[_type.boolean],  # value
                                     _type.HRESULT]
    get_MinPasswordLength: _Callable[[_Pointer[_type.BYTE]],  # value
                                     _type.HRESULT]
    put_MinPasswordLength: _Callable[[_type.BYTE],  # value
                                     _type.HRESULT]
    get_DisallowConvenienceLogon: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_DisallowConvenienceLogon: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]
    get_MinPasswordComplexCharacters: _Callable[[_Pointer[_type.BYTE]],  # value
                                                _type.HRESULT]
    put_MinPasswordComplexCharacters: _Callable[[_type.BYTE],  # value
                                                _type.HRESULT]
    get_PasswordExpiration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                      _type.HRESULT]
    put_PasswordExpiration: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                      _type.HRESULT]
    get_PasswordHistory: _Callable[[_Pointer[_type.UINT32]],  # value
                                   _type.HRESULT]
    put_PasswordHistory: _Callable[[_type.UINT32],  # value
                                   _type.HRESULT]
    get_MaxPasswordFailedAttempts: _Callable[[_Pointer[_type.BYTE]],  # value
                                             _type.HRESULT]
    put_MaxPasswordFailedAttempts: _Callable[[_type.BYTE],  # value
                                             _type.HRESULT]
    get_MaxInactivityTimeLock: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                         _type.HRESULT]
    put_MaxInactivityTimeLock: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                         _type.HRESULT]
    CheckCompliance: _Callable[[_Pointer[IEasComplianceResults]],  # result
                               _type.HRESULT]
    ApplyAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IEasComplianceResults]]],  # operation
                          _type.HRESULT]


class IEasComplianceResults(_inspectable.IInspectable):
    get_Compliant: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_RequireEncryptionResult: _Callable[[_Pointer[_enum.Windows.Security.ExchangeActiveSyncProvisioning.EasRequireEncryptionResult]],  # value
                                           _type.HRESULT]
    get_MinPasswordLengthResult: _Callable[[_Pointer[_enum.Windows.Security.ExchangeActiveSyncProvisioning.EasMinPasswordLengthResult]],  # value
                                           _type.HRESULT]
    get_DisallowConvenienceLogonResult: _Callable[[_Pointer[_enum.Windows.Security.ExchangeActiveSyncProvisioning.EasDisallowConvenienceLogonResult]],  # value
                                                  _type.HRESULT]
    get_MinPasswordComplexCharactersResult: _Callable[[_Pointer[_enum.Windows.Security.ExchangeActiveSyncProvisioning.EasMinPasswordComplexCharactersResult]],  # value
                                                      _type.HRESULT]
    get_PasswordExpirationResult: _Callable[[_Pointer[_enum.Windows.Security.ExchangeActiveSyncProvisioning.EasPasswordExpirationResult]],  # value
                                            _type.HRESULT]
    get_PasswordHistoryResult: _Callable[[_Pointer[_enum.Windows.Security.ExchangeActiveSyncProvisioning.EasPasswordHistoryResult]],  # value
                                         _type.HRESULT]
    get_MaxPasswordFailedAttemptsResult: _Callable[[_Pointer[_enum.Windows.Security.ExchangeActiveSyncProvisioning.EasMaxPasswordFailedAttemptsResult]],  # value
                                                   _type.HRESULT]
    get_MaxInactivityTimeLockResult: _Callable[[_Pointer[_enum.Windows.Security.ExchangeActiveSyncProvisioning.EasMaxInactivityTimeLockResult]],  # value
                                               _type.HRESULT]


class IEasComplianceResults2(_inspectable.IInspectable):
    get_EncryptionProviderType: _Callable[[_Pointer[_enum.Windows.Security.ExchangeActiveSyncProvisioning.EasEncryptionProviderType]],  # value
                                          _type.HRESULT]
