from __future__ import annotations

from typing import Callable as _Callable

from .... import Credentials as _Windows_Security_Credentials
from ..... import Foundation as _Windows_Foundation
from ..... import System as _Windows_System
from .....Foundation import Collections as _Windows_Foundation_Collections
from ...... import inspectable as _inspectable
from ........ import enum as _enum
from ........ import struct as _struct
from ........ import type as _type
from ........_utils import _Pointer


class IFindAllAccountsResult(_inspectable.IInspectable):
    get_Accounts: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Security_Credentials.IWebAccount]]],  # value
                            _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.Security.Authentication.Web.Core.FindAllWebAccountsStatus]],  # value
                          _type.HRESULT]
    get_ProviderError: _Callable[[_Pointer[IWebProviderError]],  # value
                                 _type.HRESULT]


class IWebAccountEventArgs(_inspectable.IInspectable):
    get_Account: _Callable[[_Pointer[_Windows_Security_Credentials.IWebAccount]],  # value
                           _type.HRESULT]


class IWebAccountMonitor(_inspectable.IInspectable):
    add_Updated: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebAccountMonitor, IWebAccountEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Updated: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_Removed: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebAccountMonitor, IWebAccountEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Removed: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_DefaultSignInAccountChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebAccountMonitor, _inspectable.IInspectable],  # handler
                                                _Pointer[_struct.EventRegistrationToken]],  # token
                                               _type.HRESULT]
    remove_DefaultSignInAccountChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                  _type.HRESULT]


class IWebAccountMonitor2(_inspectable.IInspectable):
    add_AccountPictureUpdated: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebAccountMonitor, IWebAccountEventArgs],  # handler
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_AccountPictureUpdated: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]


class IWebAuthenticationCoreManagerStatics(_inspectable.IInspectable):
    GetTokenSilentlyAsync: _Callable[[IWebTokenRequest,  # request
                                      _Pointer[_Windows_Foundation.IAsyncOperation[IWebTokenRequestResult]]],  # asyncInfo
                                     _type.HRESULT]
    GetTokenSilentlyWithWebAccountAsync: _Callable[[IWebTokenRequest,  # request
                                                    _Windows_Security_Credentials.IWebAccount,  # webAccount
                                                    _Pointer[_Windows_Foundation.IAsyncOperation[IWebTokenRequestResult]]],  # asyncInfo
                                                   _type.HRESULT]
    RequestTokenAsync: _Callable[[IWebTokenRequest,  # request
                                  _Pointer[_Windows_Foundation.IAsyncOperation[IWebTokenRequestResult]]],  # asyncInfo
                                 _type.HRESULT]
    RequestTokenWithWebAccountAsync: _Callable[[IWebTokenRequest,  # request
                                                _Windows_Security_Credentials.IWebAccount,  # webAccount
                                                _Pointer[_Windows_Foundation.IAsyncOperation[IWebTokenRequestResult]]],  # asyncInfo
                                               _type.HRESULT]
    FindAccountAsync: _Callable[[_Windows_Security_Credentials.IWebAccountProvider,  # provider
                                 _type.HSTRING,  # webAccountId
                                 _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Security_Credentials.IWebAccount]]],  # asyncInfo
                                _type.HRESULT]
    FindAccountProviderAsync: _Callable[[_type.HSTRING,  # webAccountProviderId
                                         _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Security_Credentials.IWebAccountProvider]]],  # asyncInfo
                                        _type.HRESULT]
    FindAccountProviderWithAuthorityAsync: _Callable[[_type.HSTRING,  # webAccountProviderId
                                                      _type.HSTRING,  # authority
                                                      _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Security_Credentials.IWebAccountProvider]]],  # asyncInfo
                                                     _type.HRESULT]

    _factory = True


class IWebAuthenticationCoreManagerStatics2(_inspectable.IInspectable):
    FindAccountProviderWithAuthorityForUserAsync: _Callable[[_type.HSTRING,  # webAccountProviderId
                                                             _type.HSTRING,  # authority
                                                             _Windows_System.IUser,  # user
                                                             _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Security_Credentials.IWebAccountProvider]]],  # asyncInfo
                                                            _type.HRESULT]

    _factory = True


class IWebAuthenticationCoreManagerStatics3(_inspectable.IInspectable):
    CreateWebAccountMonitor: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Security_Credentials.IWebAccount],  # webAccounts
                                        _Pointer[IWebAccountMonitor]],  # result
                                       _type.HRESULT]

    _factory = True


class IWebAuthenticationCoreManagerStatics4(_inspectable.IInspectable):
    FindAllAccountsAsync: _Callable[[_Windows_Security_Credentials.IWebAccountProvider,  # provider
                                     _Pointer[_Windows_Foundation.IAsyncOperation[IFindAllAccountsResult]]],  # operation
                                    _type.HRESULT]
    FindAllAccountsWithClientIdAsync: _Callable[[_Windows_Security_Credentials.IWebAccountProvider,  # provider
                                                 _type.HSTRING,  # clientId
                                                 _Pointer[_Windows_Foundation.IAsyncOperation[IFindAllAccountsResult]]],  # operation
                                                _type.HRESULT]
    FindSystemAccountProviderAsync: _Callable[[_type.HSTRING,  # webAccountProviderId
                                               _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Security_Credentials.IWebAccountProvider]]],  # operation
                                              _type.HRESULT]
    FindSystemAccountProviderWithAuthorityAsync: _Callable[[_type.HSTRING,  # webAccountProviderId
                                                            _type.HSTRING,  # authority
                                                            _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Security_Credentials.IWebAccountProvider]]],  # operation
                                                           _type.HRESULT]
    FindSystemAccountProviderWithAuthorityForUserAsync: _Callable[[_type.HSTRING,  # webAccountProviderId
                                                                   _type.HSTRING,  # authority
                                                                   _Windows_System.IUser,  # user
                                                                   _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Security_Credentials.IWebAccountProvider]]],  # operation
                                                                  _type.HRESULT]

    _factory = True


class IWebProviderError(_inspectable.IInspectable):
    get_ErrorCode: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    get_ErrorMessage: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, _type.HSTRING]]],  # value
                              _type.HRESULT]


class IWebProviderErrorFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.UINT32,  # errorCode
                       _type.HSTRING,  # errorMessage
                       _Pointer[IWebProviderError]],  # webProviderError
                      _type.HRESULT]

    _factory = True


class IWebTokenRequest(_inspectable.IInspectable):
    get_WebAccountProvider: _Callable[[_Pointer[_Windows_Security_Credentials.IWebAccountProvider]],  # value
                                      _type.HRESULT]
    get_Scope: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_ClientId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_PromptType: _Callable[[_Pointer[_enum.Windows.Security.Authentication.Web.Core.WebTokenRequestPromptType]],  # value
                              _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, _type.HSTRING]]],  # requestProperties
                              _type.HRESULT]


class IWebTokenRequest2(_inspectable.IInspectable):
    get_AppProperties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, _type.HSTRING]]],  # requestProperties
                                 _type.HRESULT]


class IWebTokenRequest3(_inspectable.IInspectable):
    get_CorrelationId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    put_CorrelationId: _Callable[[_type.HSTRING],  # value
                                 _type.HRESULT]


class IWebTokenRequestFactory(_inspectable.IInspectable):
    Create: _Callable[[_Windows_Security_Credentials.IWebAccountProvider,  # provider
                       _type.HSTRING,  # scope
                       _type.HSTRING,  # clientId
                       _Pointer[IWebTokenRequest]],  # webTokenRequest
                      _type.HRESULT]
    CreateWithPromptType: _Callable[[_Windows_Security_Credentials.IWebAccountProvider,  # provider
                                     _type.HSTRING,  # scope
                                     _type.HSTRING,  # clientId
                                     _enum.Windows.Security.Authentication.Web.Core.WebTokenRequestPromptType,  # promptType
                                     _Pointer[IWebTokenRequest]],  # webTokenRequest
                                    _type.HRESULT]
    CreateWithProvider: _Callable[[_Windows_Security_Credentials.IWebAccountProvider,  # provider
                                   _Pointer[IWebTokenRequest]],  # webTokenRequest
                                  _type.HRESULT]
    CreateWithScope: _Callable[[_Windows_Security_Credentials.IWebAccountProvider,  # provider
                                _type.HSTRING,  # scope
                                _Pointer[IWebTokenRequest]],  # webTokenRequest
                               _type.HRESULT]

    _factory = True


class IWebTokenRequestResult(_inspectable.IInspectable):
    get_ResponseData: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IWebTokenResponse]]],  # value
                                _type.HRESULT]
    get_ResponseStatus: _Callable[[_Pointer[_enum.Windows.Security.Authentication.Web.Core.WebTokenRequestStatus]],  # value
                                  _type.HRESULT]
    get_ResponseError: _Callable[[_Pointer[IWebProviderError]],  # value
                                 _type.HRESULT]
    InvalidateCacheAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                    _type.HRESULT]


class IWebTokenResponse(_inspectable.IInspectable):
    get_Token: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_ProviderError: _Callable[[_Pointer[IWebProviderError]],  # value
                                 _type.HRESULT]
    get_WebAccount: _Callable[[_Pointer[_Windows_Security_Credentials.IWebAccount]],  # value
                              _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, _type.HSTRING]]],  # value
                              _type.HRESULT]


class IWebTokenResponseFactory(_inspectable.IInspectable):
    CreateWithToken: _Callable[[_type.HSTRING,  # token
                                _Pointer[IWebTokenResponse]],  # webTokenResponse
                               _type.HRESULT]
    CreateWithTokenAndAccount: _Callable[[_type.HSTRING,  # token
                                          _Windows_Security_Credentials.IWebAccount,  # webAccount
                                          _Pointer[IWebTokenResponse]],  # webTokenResponse
                                         _type.HRESULT]
    CreateWithTokenAccountAndError: _Callable[[_type.HSTRING,  # token
                                               _Windows_Security_Credentials.IWebAccount,  # webAccount
                                               IWebProviderError,  # error
                                               _Pointer[IWebTokenResponse]],  # webTokenResponse
                                              _type.HRESULT]

    _factory = True
