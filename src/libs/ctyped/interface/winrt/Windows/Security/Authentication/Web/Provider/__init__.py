from __future__ import annotations as _

from typing import Callable as _Callable

from .. import Core as _Windows_Security_Authentication_Web_Core
from .... import Credentials as _Windows_Security_Credentials
from ....Cryptography import Core as _Windows_Security_Cryptography_Core
from ..... import Foundation as _Windows_Foundation
from ..... import System as _Windows_System
from .....Foundation import Collections as _Windows_Foundation_Collections
from .....Storage import Streams as _Windows_Storage_Streams
from .....Web import Http as _Windows_Web_Http
from ...... import inspectable as _inspectable
from ........ import enum as _enum
from ........ import struct as _struct
from ........ import type as _type
from ........_utils import _Pointer


class IWebAccountClientView(_inspectable.IInspectable):
    get_ApplicationCallbackUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                          _type.HRESULT]
    get_Type: _Callable[[_Pointer[_enum.Windows.Security.Authentication.Web.Provider.WebAccountClientViewType]],  # value
                        _type.HRESULT]
    get_AccountPairwiseId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]


class IWebAccountClientViewFactory(_inspectable.IInspectable):
    Create: _Callable[[_enum.Windows.Security.Authentication.Web.Provider.WebAccountClientViewType,  # viewType
                       _Windows_Foundation.IUriRuntimeClass,  # applicationCallbackUri
                       _Pointer[IWebAccountClientView]],  # view
                      _type.HRESULT]
    CreateWithPairwiseId: _Callable[[_enum.Windows.Security.Authentication.Web.Provider.WebAccountClientViewType,  # viewType
                                     _Windows_Foundation.IUriRuntimeClass,  # applicationCallbackUri
                                     _type.HSTRING,  # accountPairwiseId
                                     _Pointer[IWebAccountClientView]],  # view
                                    _type.HRESULT]

    _factory = True


class IWebAccountManagerStatics(_inspectable.IInspectable):
    UpdateWebAccountPropertiesAsync: _Callable[[_Windows_Security_Credentials.IWebAccount,  # webAccount
                                                _type.HSTRING,  # webAccountUserName
                                                _Windows_Foundation_Collections.IMapView[_type.HSTRING, _type.HSTRING],  # additionalProperties
                                                _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                               _type.HRESULT]
    AddWebAccountAsync: _Callable[[_type.HSTRING,  # webAccountId
                                   _type.HSTRING,  # webAccountUserName
                                   _Windows_Foundation_Collections.IMapView[_type.HSTRING, _type.HSTRING],  # props
                                   _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Security_Credentials.IWebAccount]]],  # asyncInfo
                                  _type.HRESULT]
    DeleteWebAccountAsync: _Callable[[_Windows_Security_Credentials.IWebAccount,  # webAccount
                                      _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                     _type.HRESULT]
    FindAllProviderWebAccountsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_Security_Credentials.IWebAccount]]]],  # asyncInfo
                                               _type.HRESULT]
    PushCookiesAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                 _Windows_Foundation_Collections.IVectorView[_Windows_Web_Http.IHttpCookie],  # cookies
                                 _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                _type.HRESULT]
    SetViewAsync: _Callable[[_Windows_Security_Credentials.IWebAccount,  # webAccount
                             IWebAccountClientView,  # view
                             _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                            _type.HRESULT]
    ClearViewAsync: _Callable[[_Windows_Security_Credentials.IWebAccount,  # webAccount
                               _Windows_Foundation.IUriRuntimeClass,  # applicationCallbackUri
                               _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                              _type.HRESULT]
    GetViewsAsync: _Callable[[_Windows_Security_Credentials.IWebAccount,  # webAccount
                              _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IWebAccountClientView]]]],  # asyncInfo
                             _type.HRESULT]
    SetWebAccountPictureAsync: _Callable[[_Windows_Security_Credentials.IWebAccount,  # webAccount
                                          _Windows_Storage_Streams.IRandomAccessStream,  # webAccountPicture
                                          _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                         _type.HRESULT]
    ClearWebAccountPictureAsync: _Callable[[_Windows_Security_Credentials.IWebAccount,  # webAccount
                                            _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                           _type.HRESULT]

    _factory = True


class IWebAccountManagerStatics2(_inspectable.IInspectable):
    PullCookiesAsync: _Callable[[_type.HSTRING,  # uriString
                                 _type.HSTRING,  # callerPFN
                                 _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                _type.HRESULT]

    _factory = True


class IWebAccountManagerStatics3(_inspectable.IInspectable):
    FindAllProviderWebAccountsForUserAsync: _Callable[[_Windows_System.IUser,  # user
                                                       _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_Security_Credentials.IWebAccount]]]],  # operation
                                                      _type.HRESULT]
    AddWebAccountForUserAsync: _Callable[[_Windows_System.IUser,  # user
                                          _type.HSTRING,  # webAccountId
                                          _type.HSTRING,  # webAccountUserName
                                          _Windows_Foundation_Collections.IMapView[_type.HSTRING, _type.HSTRING],  # props
                                          _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Security_Credentials.IWebAccount]]],  # operation
                                         _type.HRESULT]
    AddWebAccountWithScopeForUserAsync: _Callable[[_Windows_System.IUser,  # user
                                                   _type.HSTRING,  # webAccountId
                                                   _type.HSTRING,  # webAccountUserName
                                                   _Windows_Foundation_Collections.IMapView[_type.HSTRING, _type.HSTRING],  # props
                                                   _enum.Windows.Security.Authentication.Web.Provider.WebAccountScope,  # scope
                                                   _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Security_Credentials.IWebAccount]]],  # operation
                                                  _type.HRESULT]
    AddWebAccountWithScopeAndMapForUserAsync: _Callable[[_Windows_System.IUser,  # user
                                                         _type.HSTRING,  # webAccountId
                                                         _type.HSTRING,  # webAccountUserName
                                                         _Windows_Foundation_Collections.IMapView[_type.HSTRING, _type.HSTRING],  # props
                                                         _enum.Windows.Security.Authentication.Web.Provider.WebAccountScope,  # scope
                                                         _type.HSTRING,  # perUserWebAccountId
                                                         _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Security_Credentials.IWebAccount]]],  # operation
                                                        _type.HRESULT]

    _factory = True


class IWebAccountManagerStatics4(_inspectable.IInspectable):
    InvalidateAppCacheForAllAccountsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                                     _type.HRESULT]
    InvalidateAppCacheForAccountAsync: _Callable[[_Windows_Security_Credentials.IWebAccount,  # webAccount
                                                  _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                                 _type.HRESULT]

    _factory = True


class IWebAccountMapManagerStatics(_inspectable.IInspectable):
    AddWebAccountWithScopeAndMapAsync: _Callable[[_type.HSTRING,  # webAccountId
                                                  _type.HSTRING,  # webAccountUserName
                                                  _Windows_Foundation_Collections.IMapView[_type.HSTRING, _type.HSTRING],  # props
                                                  _enum.Windows.Security.Authentication.Web.Provider.WebAccountScope,  # scope
                                                  _type.HSTRING,  # perUserWebAccountId
                                                  _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Security_Credentials.IWebAccount]]],  # asyncInfo
                                                 _type.HRESULT]
    SetPerAppToPerUserAccountAsync: _Callable[[_Windows_Security_Credentials.IWebAccount,  # perAppAccount
                                               _type.HSTRING,  # perUserWebAccountId
                                               _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                              _type.HRESULT]
    GetPerUserFromPerAppAccountAsync: _Callable[[_Windows_Security_Credentials.IWebAccount,  # perAppAccount
                                                 _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Security_Credentials.IWebAccount]]],  # asyncInfo
                                                _type.HRESULT]
    ClearPerUserFromPerAppAccountAsync: _Callable[[_Windows_Security_Credentials.IWebAccount,  # perAppAccount
                                                   _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                                  _type.HRESULT]

    _factory = True


class IWebAccountProviderAddAccountOperation(_inspectable.IInspectable):
    ReportCompleted: _Callable[[],
                               _type.HRESULT]


class IWebAccountProviderBaseReportOperation(_inspectable.IInspectable):
    ReportCompleted: _Callable[[],
                               _type.HRESULT]
    ReportError: _Callable[[_Windows_Security_Authentication_Web_Core.IWebProviderError],  # value
                           _type.HRESULT]


class IWebAccountProviderDeleteAccountOperation(_inspectable.IInspectable):
    get_WebAccount: _Callable[[_Pointer[_Windows_Security_Credentials.IWebAccount]],  # value
                              _type.HRESULT]


class IWebAccountProviderManageAccountOperation(_inspectable.IInspectable):
    get_WebAccount: _Callable[[_Pointer[_Windows_Security_Credentials.IWebAccount]],  # value
                              _type.HRESULT]
    ReportCompleted: _Callable[[],
                               _type.HRESULT]


class IWebAccountProviderOperation(_inspectable.IInspectable):
    get_Kind: _Callable[[_Pointer[_enum.Windows.Security.Authentication.Web.Provider.WebAccountProviderOperationKind]],  # value
                        _type.HRESULT]


class IWebAccountProviderRetrieveCookiesOperation(_inspectable.IInspectable):
    get_Context: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # webCookieRequestContext
                           _type.HRESULT]
    get_Cookies: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_Web_Http.IHttpCookie]]],  # cookies
                           _type.HRESULT]
    put_Uri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # uri
                       _type.HRESULT]
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # uri
                       _type.HRESULT]
    get_ApplicationCallbackUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                          _type.HRESULT]


class IWebAccountProviderSignOutAccountOperation(_inspectable.IInspectable):
    get_WebAccount: _Callable[[_Pointer[_Windows_Security_Credentials.IWebAccount]],  # value
                              _type.HRESULT]
    get_ApplicationCallbackUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                          _type.HRESULT]
    get_ClientId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]


class IWebAccountProviderSilentReportOperation(_inspectable.IInspectable):
    ReportUserInteractionRequired: _Callable[[],
                                             _type.HRESULT]
    ReportUserInteractionRequiredWithError: _Callable[[_Windows_Security_Authentication_Web_Core.IWebProviderError],  # value
                                                      _type.HRESULT]


class IWebAccountProviderTokenObjects(_inspectable.IInspectable):
    get_Operation: _Callable[[_Pointer[IWebAccountProviderOperation]],  # value
                             _type.HRESULT]


class IWebAccountProviderTokenObjects2(_inspectable.IInspectable):
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]


class IWebAccountProviderTokenOperation(_inspectable.IInspectable):
    get_ProviderRequest: _Callable[[_Pointer[IWebProviderTokenRequest]],  # webTokenRequest
                                   _type.HRESULT]
    get_ProviderResponses: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IWebProviderTokenResponse]]],  # value
                                     _type.HRESULT]
    put_CacheExpirationTime: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                                       _type.HRESULT]
    get_CacheExpirationTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                       _type.HRESULT]


class IWebAccountProviderUIReportOperation(_inspectable.IInspectable):
    ReportUserCanceled: _Callable[[],
                                  _type.HRESULT]


class IWebAccountScopeManagerStatics(_inspectable.IInspectable):
    AddWebAccountWithScopeAsync: _Callable[[_type.HSTRING,  # webAccountId
                                            _type.HSTRING,  # webAccountUserName
                                            _Windows_Foundation_Collections.IMapView[_type.HSTRING, _type.HSTRING],  # props
                                            _enum.Windows.Security.Authentication.Web.Provider.WebAccountScope,  # scope
                                            _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Security_Credentials.IWebAccount]]],  # asyncInfo
                                           _type.HRESULT]
    SetScopeAsync: _Callable[[_Windows_Security_Credentials.IWebAccount,  # webAccount
                              _enum.Windows.Security.Authentication.Web.Provider.WebAccountScope,  # scope
                              _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                             _type.HRESULT]
    GetScope: _Callable[[_Windows_Security_Credentials.IWebAccount,  # webAccount
                         _Pointer[_enum.Windows.Security.Authentication.Web.Provider.WebAccountScope]],  # scope
                        _type.HRESULT]

    _factory = True


class IWebProviderTokenRequest(_inspectable.IInspectable):
    get_ClientRequest: _Callable[[_Pointer[_Windows_Security_Authentication_Web_Core.IWebTokenRequest]],  # value
                                 _type.HRESULT]
    get_WebAccounts: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Security_Credentials.IWebAccount]]],  # value
                               _type.HRESULT]
    get_WebAccountSelectionOptions: _Callable[[_Pointer[_enum.Windows.Security.Authentication.Web.Provider.WebAccountSelectionOptions]],  # value
                                              _type.HRESULT]
    get_ApplicationCallbackUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                          _type.HRESULT]
    GetApplicationTokenBindingKeyAsync: _Callable[[_enum.Windows.Security.Authentication.Web.TokenBindingKeyType,  # keyType
                                                   _Windows_Foundation.IUriRuntimeClass,  # target
                                                   _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Security_Cryptography_Core.ICryptographicKey]]],  # asyncInfo
                                                  _type.HRESULT]


class IWebProviderTokenRequest2(_inspectable.IInspectable):
    GetApplicationTokenBindingKeyIdAsync: _Callable[[_enum.Windows.Security.Authentication.Web.TokenBindingKeyType,  # keyType
                                                     _Windows_Foundation.IUriRuntimeClass,  # target
                                                     _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IBuffer]]],  # asyncInfo
                                                    _type.HRESULT]


class IWebProviderTokenRequest3(_inspectable.IInspectable):
    get_ApplicationPackageFamilyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                                _type.HRESULT]
    get_ApplicationProcessName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                          _type.HRESULT]
    CheckApplicationForCapabilityAsync: _Callable[[_type.HSTRING,  # capabilityName
                                                   _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                                  _type.HRESULT]


class IWebProviderTokenResponse(_inspectable.IInspectable):
    get_ClientResponse: _Callable[[_Pointer[_Windows_Security_Authentication_Web_Core.IWebTokenResponse]],  # value
                                  _type.HRESULT]


class IWebProviderTokenResponseFactory(_inspectable.IInspectable):
    Create: _Callable[[_Windows_Security_Authentication_Web_Core.IWebTokenResponse,  # webTokenResponse
                       _Pointer[IWebProviderTokenResponse]],  # webProviderTokenResponse
                      _type.HRESULT]

    _factory = True
