from __future__ import annotations as _

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import type as _type
from ......._utils import _Pointer


class IEnterpriseKeyCredentialRegistrationInfo(_inspectable.IInspectable):
    get_TenantId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_TenantName: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_Subject: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_KeyId: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_KeyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]


class IEnterpriseKeyCredentialRegistrationManager(_inspectable.IInspectable):
    GetRegistrationsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IEnterpriseKeyCredentialRegistrationInfo]]]],  # value
                                     _type.HRESULT]


class IEnterpriseKeyCredentialRegistrationManagerStatics(_inspectable.IInspectable, factory=True):
    get_Current: _Callable[[_Pointer[IEnterpriseKeyCredentialRegistrationManager]],  # value
                           _type.HRESULT]
