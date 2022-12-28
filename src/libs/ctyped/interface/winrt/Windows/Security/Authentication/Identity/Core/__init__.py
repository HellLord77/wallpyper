from __future__ import annotations as _

from typing import Callable as _Callable

from ..... import Foundation as _Windows_Foundation
from .....Foundation import Collections as _Windows_Foundation_Collections
from ...... import inspectable as _inspectable
from ........ import enum as _enum
from ........ import struct as _struct
from ........ import type as _type
from ........_utils import _Pointer


class IMicrosoftAccountMultiFactorAuthenticationManager(_inspectable.IInspectable):
    GetOneTimePassCodeAsync: _Callable[[_type.HSTRING,  # userAccountId
                                        _type.UINT32,  # codeLength
                                        _Pointer[_Windows_Foundation.IAsyncOperation[IMicrosoftAccountMultiFactorOneTimeCodedInfo]]],  # asyncOperation
                                       _type.HRESULT]
    AddDeviceAsync: _Callable[[_type.HSTRING,  # userAccountId
                               _type.HSTRING,  # authenticationToken
                               _type.HSTRING,  # wnsChannelId
                               _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorServiceResponse]]],  # asyncOperation
                              _type.HRESULT]
    RemoveDeviceAsync: _Callable[[_type.HSTRING,  # userAccountId
                                  _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorServiceResponse]]],  # asyncOperation
                                 _type.HRESULT]
    UpdateWnsChannelAsync: _Callable[[_type.HSTRING,  # userAccountId
                                      _type.HSTRING,  # channelUri
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorServiceResponse]]],  # asyncOperation
                                     _type.HRESULT]
    GetSessionsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # userAccountIdList
                                 _Pointer[_Windows_Foundation.IAsyncOperation[IMicrosoftAccountMultiFactorGetSessionsResult]]],  # asyncOperation
                                _type.HRESULT]
    GetSessionsAndUnregisteredAccountsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # userAccountIdList
                                                        _Pointer[_Windows_Foundation.IAsyncOperation[IMicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo]]],  # asyncOperation
                                                       _type.HRESULT]
    ApproveSessionUsingAuthSessionInfoAsync: _Callable[[_enum.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorSessionAuthenticationStatus,  # sessionAuthentictionStatus
                                                        IMicrosoftAccountMultiFactorSessionInfo,  # authenticationSessionInfo
                                                        _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorServiceResponse]]],  # asyncOperation
                                                       _type.HRESULT]
    ApproveSessionAsync: _Callable[[_enum.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorSessionAuthenticationStatus,  # sessionAuthentictionStatus
                                    _type.HSTRING,  # userAccountId
                                    _type.HSTRING,  # sessionId
                                    _enum.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorAuthenticationType,  # sessionAuthenticationType
                                    _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorServiceResponse]]],  # asyncOperation
                                   _type.HRESULT]
    DenySessionUsingAuthSessionInfoAsync: _Callable[[IMicrosoftAccountMultiFactorSessionInfo,  # authenticationSessionInfo
                                                     _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorServiceResponse]]],  # asyncOperation
                                                    _type.HRESULT]
    DenySessionAsync: _Callable[[_type.HSTRING,  # userAccountId
                                 _type.HSTRING,  # sessionId
                                 _enum.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorAuthenticationType,  # sessionAuthenticationType
                                 _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorServiceResponse]]],  # asyncOperation
                                _type.HRESULT]


class IMicrosoftAccountMultiFactorAuthenticatorStatics(_inspectable.IInspectable):
    get_Current: _Callable[[_Pointer[IMicrosoftAccountMultiFactorAuthenticationManager]],  # value
                           _type.HRESULT]

    _factory = True


class IMicrosoftAccountMultiFactorGetSessionsResult(_inspectable.IInspectable):
    get_Sessions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMicrosoftAccountMultiFactorSessionInfo]]],  # value
                            _type.HRESULT]
    get_ServiceResponse: _Callable[[_Pointer[_enum.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorServiceResponse]],  # value
                                   _type.HRESULT]


class IMicrosoftAccountMultiFactorOneTimeCodedInfo(_inspectable.IInspectable):
    get_Code: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_TimeInterval: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                _type.HRESULT]
    get_TimeToLive: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                              _type.HRESULT]
    get_ServiceResponse: _Callable[[_Pointer[_enum.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorServiceResponse]],  # value
                                   _type.HRESULT]


class IMicrosoftAccountMultiFactorSessionInfo(_inspectable.IInspectable):
    get_UserAccountId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_SessionId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_DisplaySessionId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_ApprovalStatus: _Callable[[_Pointer[_enum.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorSessionApprovalStatus]],  # value
                                  _type.HRESULT]
    get_AuthenticationType: _Callable[[_Pointer[_enum.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorAuthenticationType]],  # value
                                      _type.HRESULT]
    get_RequestTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                               _type.HRESULT]
    get_ExpirationTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                  _type.HRESULT]


class IMicrosoftAccountMultiFactorUnregisteredAccountsAndSessionInfo(_inspectable.IInspectable):
    get_Sessions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMicrosoftAccountMultiFactorSessionInfo]]],  # value
                            _type.HRESULT]
    get_UnregisteredAccounts: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                        _type.HRESULT]
    get_ServiceResponse: _Callable[[_Pointer[_enum.Windows.Security.Authentication.Identity.Core.MicrosoftAccountMultiFactorServiceResponse]],  # value
                                   _type.HRESULT]
