from __future__ import annotations as _

from typing import Callable as _Callable

from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import type as _type
from ......._utils import _Pointer


class IUserDataAccountPartnerAccountInfo(_inspectable.IInspectable):
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Priority: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    get_AccountKind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.UserDataAccounts.Provider.UserDataAccountProviderPartnerAccountKind]],  # value
                               _type.HRESULT]


class IUserDataAccountProviderAddAccountOperation(_inspectable.IInspectable):
    get_ContentKinds: _Callable[[_Pointer[_enum.Windows.ApplicationModel.UserDataAccounts.UserDataAccountContentKinds]],  # value
                                _type.HRESULT]
    get_PartnerAccountInfos: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IUserDataAccountPartnerAccountInfo]]],  # value
                                       _type.HRESULT]
    ReportCompleted: _Callable[[_type.HSTRING],  # userDataAccountId
                               _type.HRESULT]


class IUserDataAccountProviderOperation(_inspectable.IInspectable):
    get_Kind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.UserDataAccounts.Provider.UserDataAccountProviderOperationKind]],  # value
                        _type.HRESULT]


class IUserDataAccountProviderResolveErrorsOperation(_inspectable.IInspectable):
    get_UserDataAccountId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    ReportCompleted: _Callable[[],
                               _type.HRESULT]


class IUserDataAccountProviderSettingsOperation(_inspectable.IInspectable):
    get_UserDataAccountId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    ReportCompleted: _Callable[[],
                               _type.HRESULT]
