from __future__ import annotations as _

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ....Security import Credentials as _Windows_Security_Credentials
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import type as _type
from ......._utils import _Pointer


class IDeviceAccountConfiguration(_inspectable.IInspectable):
    get_AccountName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_AccountName: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_DeviceAccountTypeId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    put_DeviceAccountTypeId: _Callable[[_type.HSTRING],  # value
                                       _type.HRESULT]
    get_ServerType: _Callable[[_Pointer[_enum.Windows.ApplicationModel.UserDataAccounts.SystemAccess.DeviceAccountServerType]],  # value
                              _type.HRESULT]
    put_ServerType: _Callable[[_enum.Windows.ApplicationModel.UserDataAccounts.SystemAccess.DeviceAccountServerType],  # value
                              _type.HRESULT]
    get_EmailAddress: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    put_EmailAddress: _Callable[[_type.HSTRING],  # value
                                _type.HRESULT]
    get_Domain: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    put_Domain: _Callable[[_type.HSTRING],  # value
                          _type.HRESULT]
    get_EmailSyncEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_EmailSyncEnabled: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_ContactsSyncEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_ContactsSyncEnabled: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_CalendarSyncEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_CalendarSyncEnabled: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_IncomingServerAddress: _Callable[[_Pointer[_type.HSTRING]],  # value
                                         _type.HRESULT]
    put_IncomingServerAddress: _Callable[[_type.HSTRING],  # value
                                         _type.HRESULT]
    get_IncomingServerPort: _Callable[[_Pointer[_type.INT32]],  # value
                                      _type.HRESULT]
    put_IncomingServerPort: _Callable[[_type.INT32],  # value
                                      _type.HRESULT]
    get_IncomingServerRequiresSsl: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    put_IncomingServerRequiresSsl: _Callable[[_type.boolean],  # value
                                             _type.HRESULT]
    get_IncomingServerUsername: _Callable[[_Pointer[_type.HSTRING]],  # value
                                          _type.HRESULT]
    put_IncomingServerUsername: _Callable[[_type.HSTRING],  # value
                                          _type.HRESULT]
    get_OutgoingServerAddress: _Callable[[_Pointer[_type.HSTRING]],  # value
                                         _type.HRESULT]
    put_OutgoingServerAddress: _Callable[[_type.HSTRING],  # value
                                         _type.HRESULT]
    get_OutgoingServerPort: _Callable[[_Pointer[_type.INT32]],  # value
                                      _type.HRESULT]
    put_OutgoingServerPort: _Callable[[_type.INT32],  # value
                                      _type.HRESULT]
    get_OutgoingServerRequiresSsl: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    put_OutgoingServerRequiresSsl: _Callable[[_type.boolean],  # value
                                             _type.HRESULT]
    get_OutgoingServerUsername: _Callable[[_Pointer[_type.HSTRING]],  # value
                                          _type.HRESULT]
    put_OutgoingServerUsername: _Callable[[_type.HSTRING],  # value
                                          _type.HRESULT]


class IDeviceAccountConfiguration2(_inspectable.IInspectable):
    get_IncomingServerCredential: _Callable[[_Pointer[_Windows_Security_Credentials.IPasswordCredential]],  # value
                                            _type.HRESULT]
    put_IncomingServerCredential: _Callable[[_Windows_Security_Credentials.IPasswordCredential],  # value
                                            _type.HRESULT]
    get_OutgoingServerCredential: _Callable[[_Pointer[_Windows_Security_Credentials.IPasswordCredential]],  # value
                                            _type.HRESULT]
    put_OutgoingServerCredential: _Callable[[_Windows_Security_Credentials.IPasswordCredential],  # value
                                            _type.HRESULT]
    get_OAuthRefreshToken: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    put_OAuthRefreshToken: _Callable[[_type.HSTRING],  # value
                                     _type.HRESULT]
    get_IsExternallyManaged: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_IsExternallyManaged: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_AccountIconId: _Callable[[_Pointer[_enum.Windows.ApplicationModel.UserDataAccounts.SystemAccess.DeviceAccountIconId]],  # value
                                 _type.HRESULT]
    put_AccountIconId: _Callable[[_enum.Windows.ApplicationModel.UserDataAccounts.SystemAccess.DeviceAccountIconId],  # value
                                 _type.HRESULT]
    get_AuthenticationType: _Callable[[_Pointer[_enum.Windows.ApplicationModel.UserDataAccounts.SystemAccess.DeviceAccountAuthenticationType]],  # value
                                      _type.HRESULT]
    put_AuthenticationType: _Callable[[_enum.Windows.ApplicationModel.UserDataAccounts.SystemAccess.DeviceAccountAuthenticationType],  # value
                                      _type.HRESULT]
    get_IsSsoAuthenticationSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                _type.HRESULT]
    get_SsoAccountId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    put_SsoAccountId: _Callable[[_type.HSTRING],  # value
                                _type.HRESULT]
    get_AlwaysDownloadFullMessage: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    put_AlwaysDownloadFullMessage: _Callable[[_type.boolean],  # value
                                             _type.HRESULT]
    get_DoesPolicyAllowMailSync: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    get_SyncScheduleKind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.UserDataAccounts.SystemAccess.DeviceAccountSyncScheduleKind]],  # value
                                    _type.HRESULT]
    put_SyncScheduleKind: _Callable[[_enum.Windows.ApplicationModel.UserDataAccounts.SystemAccess.DeviceAccountSyncScheduleKind],  # value
                                    _type.HRESULT]
    get_MailAgeFilter: _Callable[[_Pointer[_enum.Windows.ApplicationModel.UserDataAccounts.SystemAccess.DeviceAccountMailAgeFilter]],  # value
                                 _type.HRESULT]
    put_MailAgeFilter: _Callable[[_enum.Windows.ApplicationModel.UserDataAccounts.SystemAccess.DeviceAccountMailAgeFilter],  # value
                                 _type.HRESULT]
    get_IsClientAuthenticationCertificateRequired: _Callable[[_Pointer[_type.boolean]],  # value
                                                             _type.HRESULT]
    put_IsClientAuthenticationCertificateRequired: _Callable[[_type.boolean],  # value
                                                             _type.HRESULT]
    get_AutoSelectAuthenticationCertificate: _Callable[[_Pointer[_type.boolean]],  # value
                                                       _type.HRESULT]
    put_AutoSelectAuthenticationCertificate: _Callable[[_type.boolean],  # value
                                                       _type.HRESULT]
    get_AuthenticationCertificateId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                               _type.HRESULT]
    put_AuthenticationCertificateId: _Callable[[_type.HSTRING],  # value
                                               _type.HRESULT]
    get_CardDavSyncScheduleKind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.UserDataAccounts.SystemAccess.DeviceAccountSyncScheduleKind]],  # value
                                           _type.HRESULT]
    put_CardDavSyncScheduleKind: _Callable[[_enum.Windows.ApplicationModel.UserDataAccounts.SystemAccess.DeviceAccountSyncScheduleKind],  # value
                                           _type.HRESULT]
    get_CalDavSyncScheduleKind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.UserDataAccounts.SystemAccess.DeviceAccountSyncScheduleKind]],  # value
                                          _type.HRESULT]
    put_CalDavSyncScheduleKind: _Callable[[_enum.Windows.ApplicationModel.UserDataAccounts.SystemAccess.DeviceAccountSyncScheduleKind],  # value
                                          _type.HRESULT]
    get_CardDavServerUrl: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                    _type.HRESULT]
    put_CardDavServerUrl: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                                    _type.HRESULT]
    get_CardDavRequiresSsl: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_CardDavRequiresSsl: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    get_CalDavServerUrl: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                   _type.HRESULT]
    put_CalDavServerUrl: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                                   _type.HRESULT]
    get_CalDavRequiresSsl: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    put_CalDavRequiresSsl: _Callable[[_type.boolean],  # value
                                     _type.HRESULT]
    get_WasModifiedByUser: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    put_WasModifiedByUser: _Callable[[_type.boolean],  # value
                                     _type.HRESULT]
    get_WasIncomingServerCertificateHashConfirmed: _Callable[[_Pointer[_type.boolean]],  # value
                                                             _type.HRESULT]
    put_WasIncomingServerCertificateHashConfirmed: _Callable[[_type.boolean],  # value
                                                             _type.HRESULT]
    get_IncomingServerCertificateHash: _Callable[[_Pointer[_type.HSTRING]],  # value
                                                 _type.HRESULT]
    put_IncomingServerCertificateHash: _Callable[[_type.HSTRING],  # value
                                                 _type.HRESULT]
    get_IsOutgoingServerAuthenticationRequired: _Callable[[_Pointer[_type.boolean]],  # value
                                                          _type.HRESULT]
    put_IsOutgoingServerAuthenticationRequired: _Callable[[_type.boolean],  # value
                                                          _type.HRESULT]
    get_IsOutgoingServerAuthenticationEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                         _type.HRESULT]
    put_IsOutgoingServerAuthenticationEnabled: _Callable[[_type.boolean],  # value
                                                         _type.HRESULT]
    get_WasOutgoingServerCertificateHashConfirmed: _Callable[[_Pointer[_type.boolean]],  # value
                                                             _type.HRESULT]
    put_WasOutgoingServerCertificateHashConfirmed: _Callable[[_type.boolean],  # value
                                                             _type.HRESULT]
    get_OutgoingServerCertificateHash: _Callable[[_Pointer[_type.HSTRING]],  # value
                                                 _type.HRESULT]
    put_OutgoingServerCertificateHash: _Callable[[_type.HSTRING],  # value
                                                 _type.HRESULT]
    get_IsSyncScheduleManagedBySystem: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]
    put_IsSyncScheduleManagedBySystem: _Callable[[_type.boolean],  # value
                                                 _type.HRESULT]


class IUserDataAccountSystemAccessManagerStatics(_inspectable.IInspectable, factory=True):
    AddAndShowDeviceAccountsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[IDeviceAccountConfiguration],  # accounts
                                              _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]]],  # result
                                             _type.HRESULT]


class IUserDataAccountSystemAccessManagerStatics2(_inspectable.IInspectable, factory=True):
    SuppressLocalAccountWithAccountAsync: _Callable[[_type.HSTRING,  # userDataAccountId
                                                     _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                                    _type.HRESULT]
    CreateDeviceAccountAsync: _Callable[[IDeviceAccountConfiguration,  # account
                                         _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # result
                                        _type.HRESULT]
    DeleteDeviceAccountAsync: _Callable[[_type.HSTRING,  # accountId
                                         _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                        _type.HRESULT]
    GetDeviceAccountConfigurationAsync: _Callable[[_type.HSTRING,  # accountId
                                                   _Pointer[_Windows_Foundation.IAsyncOperation[IDeviceAccountConfiguration]]],  # result
                                                  _type.HRESULT]
