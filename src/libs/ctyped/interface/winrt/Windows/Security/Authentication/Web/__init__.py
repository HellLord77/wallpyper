from __future__ import annotations as _

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import type as _type
from ......._utils import _Pointer


class IWebAuthenticationBrokerStatics(_inspectable.IInspectable, factory=True):
    AuthenticateWithCallbackUriAsync: _Callable[[_enum.Windows.Security.Authentication.Web.WebAuthenticationOptions,  # options
                                                 _Windows_Foundation.IUriRuntimeClass,  # requestUri
                                                 _Windows_Foundation.IUriRuntimeClass,  # callbackUri
                                                 _Pointer[_Windows_Foundation.IAsyncOperation[IWebAuthenticationResult]]],  # asyncInfo
                                                _type.HRESULT]
    AuthenticateWithoutCallbackUriAsync: _Callable[[_enum.Windows.Security.Authentication.Web.WebAuthenticationOptions,  # options
                                                    _Windows_Foundation.IUriRuntimeClass,  # requestUri
                                                    _Pointer[_Windows_Foundation.IAsyncOperation[IWebAuthenticationResult]]],  # asyncInfo
                                                   _type.HRESULT]
    GetCurrentApplicationCallbackUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # callbackUri
                                                _type.HRESULT]


class IWebAuthenticationBrokerStatics2(_inspectable.IInspectable, factory=True):
    AuthenticateAndContinue: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # requestUri
                                       _type.HRESULT]
    AuthenticateWithCallbackUriAndContinue: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # requestUri
                                                       _Windows_Foundation.IUriRuntimeClass],  # callbackUri
                                                      _type.HRESULT]
    AuthenticateWithCallbackUriContinuationDataAndOptionsAndContinue: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # requestUri
                                                                                 _Windows_Foundation.IUriRuntimeClass,  # callbackUri
                                                                                 _Windows_Foundation_Collections.IPropertySet,  # continuationData
                                                                                 _enum.Windows.Security.Authentication.Web.WebAuthenticationOptions],  # options
                                                                                _type.HRESULT]
    AuthenticateSilentlyAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # requestUri
                                          _Pointer[_Windows_Foundation.IAsyncOperation[IWebAuthenticationResult]]],  # asyncInfo
                                         _type.HRESULT]
    AuthenticateSilentlyWithOptionsAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # requestUri
                                                     _enum.Windows.Security.Authentication.Web.WebAuthenticationOptions,  # options
                                                     _Pointer[_Windows_Foundation.IAsyncOperation[IWebAuthenticationResult]]],  # asyncInfo
                                                    _type.HRESULT]


class IWebAuthenticationResult(_inspectable.IInspectable):
    get_ResponseData: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_ResponseStatus: _Callable[[_Pointer[_enum.Windows.Security.Authentication.Web.WebAuthenticationStatus]],  # value
                                  _type.HRESULT]
    get_ResponseErrorDetail: _Callable[[_Pointer[_type.UINT32]],  # value
                                       _type.HRESULT]
