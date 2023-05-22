from __future__ import annotations

from typing import Callable as _Callable

from .. import Appointments as _Windows_ApplicationModel_Appointments
from .. import Contacts as _Windows_ApplicationModel_Contacts
from .. import Email as _Windows_ApplicationModel_Email
from .. import UserDataTasks as _Windows_ApplicationModel_UserDataTasks
from ... import Foundation as _Windows_Foundation
from ... import System as _Windows_System
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IUserDataAccount(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_UserDisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    put_UserDisplayName: _Callable[[_type.HSTRING],  # value
                                   _type.HRESULT]
    get_OtherAppReadAccess: _Callable[[_Pointer[_enum.Windows.ApplicationModel.UserDataAccounts.UserDataAccountOtherAppReadAccess]],  # value
                                      _type.HRESULT]
    put_OtherAppReadAccess: _Callable[[_enum.Windows.ApplicationModel.UserDataAccounts.UserDataAccountOtherAppReadAccess],  # value
                                      _type.HRESULT]
    get_Icon: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # value
                        _type.HRESULT]
    get_DeviceAccountTypeId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    get_PackageFamilyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    SaveAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                         _type.HRESULT]
    DeleteAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                           _type.HRESULT]
    FindAppointmentCalendarsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_ApplicationModel_Appointments.IAppointmentCalendar]]]],  # result
                                             _type.HRESULT]
    FindEmailMailboxesAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_ApplicationModel_Email.IEmailMailbox]]]],  # result
                                       _type.HRESULT]
    FindContactListsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_ApplicationModel_Contacts.IContactList]]]],  # result
                                     _type.HRESULT]
    FindContactAnnotationListsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_ApplicationModel_Contacts.IContactAnnotationList]]]],  # result
                                               _type.HRESULT]


class IUserDataAccount2(_inspectable.IInspectable):
    get_EnterpriseId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_IsProtectedUnderLock: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]


class IUserDataAccount3(_inspectable.IInspectable):
    get_ExplictReadAccessPackageFamilyNames: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                                       _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_DisplayName: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]


class IUserDataAccount4(_inspectable.IInspectable):
    get_CanShowCreateContactGroup: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    put_CanShowCreateContactGroup: _Callable[[_type.boolean],  # value
                                             _type.HRESULT]
    get_ProviderProperties: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                                      _type.HRESULT]
    FindUserDataTaskListsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_ApplicationModel_UserDataTasks.IUserDataTaskList]]]],  # operation
                                          _type.HRESULT]
    FindContactGroupsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_ApplicationModel_Contacts.IContactGroup]]]],  # operation
                                      _type.HRESULT]
    TryShowCreateContactGroupAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                              _type.HRESULT]
    put_IsProtectedUnderLock: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]
    put_Icon: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference],  # value
                        _type.HRESULT]


class IUserDataAccountManagerForUser(_inspectable.IInspectable):
    RequestStoreAsync: _Callable[[_enum.Windows.ApplicationModel.UserDataAccounts.UserDataAccountStoreAccessType,  # storeAccessType
                                  _Pointer[_Windows_Foundation.IAsyncOperation[IUserDataAccountStore]]],  # result
                                 _type.HRESULT]
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]


class IUserDataAccountManagerStatics(_inspectable.IInspectable, factory=True):
    RequestStoreAsync: _Callable[[_enum.Windows.ApplicationModel.UserDataAccounts.UserDataAccountStoreAccessType,  # storeAccessType
                                  _Pointer[_Windows_Foundation.IAsyncOperation[IUserDataAccountStore]]],  # result
                                 _type.HRESULT]
    ShowAddAccountAsync: _Callable[[_enum.Windows.ApplicationModel.UserDataAccounts.UserDataAccountContentKinds,  # contentKinds
                                    _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # result
                                   _type.HRESULT]
    ShowAccountSettingsAsync: _Callable[[_type.HSTRING,  # id
                                         _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                        _type.HRESULT]
    ShowAccountErrorResolverAsync: _Callable[[_type.HSTRING,  # id
                                              _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                             _type.HRESULT]


class IUserDataAccountManagerStatics2(_inspectable.IInspectable, factory=True):
    GetForUser: _Callable[[_Windows_System.IUser,  # user
                           _Pointer[IUserDataAccountManagerForUser]],  # result
                          _type.HRESULT]


class IUserDataAccountStore(_inspectable.IInspectable):
    FindAccountsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IUserDataAccount]]]],  # result
                                 _type.HRESULT]
    GetAccountAsync: _Callable[[_type.HSTRING,  # id
                                _Pointer[_Windows_Foundation.IAsyncOperation[IUserDataAccount]]],  # result
                               _type.HRESULT]
    CreateAccountAsync: _Callable[[_type.HSTRING,  # userDisplayName
                                   _Pointer[_Windows_Foundation.IAsyncOperation[IUserDataAccount]]],  # result
                                  _type.HRESULT]


class IUserDataAccountStore2(_inspectable.IInspectable):
    CreateAccountWithPackageRelativeAppIdAsync: _Callable[[_type.HSTRING,  # userDisplayName
                                                           _type.HSTRING,  # packageRelativeAppId
                                                           _Pointer[_Windows_Foundation.IAsyncOperation[IUserDataAccount]]],  # result
                                                          _type.HRESULT]
    add_StoreChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IUserDataAccountStore, IUserDataAccountStoreChangedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_StoreChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]


class IUserDataAccountStore3(_inspectable.IInspectable):
    CreateAccountWithPackageRelativeAppIdAndEnterpriseIdAsync: _Callable[[_type.HSTRING,  # userDisplayName
                                                                          _type.HSTRING,  # packageRelativeAppId
                                                                          _type.HSTRING,  # enterpriseId
                                                                          _Pointer[_Windows_Foundation.IAsyncOperation[IUserDataAccount]]],  # result
                                                                         _type.HRESULT]


class IUserDataAccountStoreChangedEventArgs(_inspectable.IInspectable):
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]
