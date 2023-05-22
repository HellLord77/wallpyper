from __future__ import annotations

from typing import Callable as _Callable

from ... import Http as _Windows_Web_Http
from .... import Foundation as _Windows_Foundation
from .... import System as _Windows_System
from ....Foundation import Collections as _Windows_Foundation_Collections
from ....Security import Credentials as _Windows_Security_Credentials
from ....Security.Cryptography import Certificates as _Windows_Security_Cryptography_Certificates
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IHttpBaseProtocolFilter(_inspectable.IInspectable):
    get_AllowAutoRedirect: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    put_AllowAutoRedirect: _Callable[[_type.boolean],  # value
                                     _type.HRESULT]
    get_AllowUI: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_AllowUI: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_AutomaticDecompression: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_AutomaticDecompression: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    get_CacheControl: _Callable[[_Pointer[IHttpCacheControl]],  # value
                                _type.HRESULT]
    get_CookieManager: _Callable[[_Pointer[_Windows_Web_Http.IHttpCookieManager]],  # value
                                 _type.HRESULT]
    get_ClientCertificate: _Callable[[_Pointer[_Windows_Security_Cryptography_Certificates.ICertificate]],  # value
                                     _type.HRESULT]
    put_ClientCertificate: _Callable[[_Windows_Security_Cryptography_Certificates.ICertificate],  # value
                                     _type.HRESULT]
    get_IgnorableServerCertificateErrors: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_enum.Windows.Security.Cryptography.Certificates.ChainValidationResult]]],  # value
                                                    _type.HRESULT]
    get_MaxConnectionsPerServer: _Callable[[_Pointer[_type.UINT32]],  # value
                                           _type.HRESULT]
    put_MaxConnectionsPerServer: _Callable[[_type.UINT32],  # value
                                           _type.HRESULT]
    get_ProxyCredential: _Callable[[_Pointer[_Windows_Security_Credentials.IPasswordCredential]],  # value
                                   _type.HRESULT]
    put_ProxyCredential: _Callable[[_Windows_Security_Credentials.IPasswordCredential],  # value
                                   _type.HRESULT]
    get_ServerCredential: _Callable[[_Pointer[_Windows_Security_Credentials.IPasswordCredential]],  # value
                                    _type.HRESULT]
    put_ServerCredential: _Callable[[_Windows_Security_Credentials.IPasswordCredential],  # value
                                    _type.HRESULT]
    get_UseProxy: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    put_UseProxy: _Callable[[_type.boolean],  # value
                            _type.HRESULT]


class IHttpBaseProtocolFilter2(_inspectable.IInspectable):
    get_MaxVersion: _Callable[[_Pointer[_enum.Windows.Web.Http.HttpVersion]],  # value
                              _type.HRESULT]
    put_MaxVersion: _Callable[[_enum.Windows.Web.Http.HttpVersion],  # value
                              _type.HRESULT]


class IHttpBaseProtocolFilter3(_inspectable.IInspectable):
    get_CookieUsageBehavior: _Callable[[_Pointer[_enum.Windows.Web.Http.Filters.HttpCookieUsageBehavior]],  # value
                                       _type.HRESULT]
    put_CookieUsageBehavior: _Callable[[_enum.Windows.Web.Http.Filters.HttpCookieUsageBehavior],  # value
                                       _type.HRESULT]


class IHttpBaseProtocolFilter4(_inspectable.IInspectable):
    add_ServerCustomValidationRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IHttpBaseProtocolFilter, IHttpServerCustomValidationRequestedEventArgs],  # handler
                                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                                   _type.HRESULT]
    remove_ServerCustomValidationRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                      _type.HRESULT]
    ClearAuthenticationCache: _Callable[[],
                                        _type.HRESULT]


class IHttpBaseProtocolFilter5(_inspectable.IInspectable):
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]


class IHttpBaseProtocolFilterStatics(_inspectable.IInspectable, factory=True):
    CreateForUser: _Callable[[_Windows_System.IUser,  # user
                              _Pointer[IHttpBaseProtocolFilter]],  # result
                             _type.HRESULT]


class IHttpCacheControl(_inspectable.IInspectable):
    get_ReadBehavior: _Callable[[_Pointer[_enum.Windows.Web.Http.Filters.HttpCacheReadBehavior]],  # value
                                _type.HRESULT]
    put_ReadBehavior: _Callable[[_enum.Windows.Web.Http.Filters.HttpCacheReadBehavior],  # value
                                _type.HRESULT]
    get_WriteBehavior: _Callable[[_Pointer[_enum.Windows.Web.Http.Filters.HttpCacheWriteBehavior]],  # value
                                 _type.HRESULT]
    put_WriteBehavior: _Callable[[_enum.Windows.Web.Http.Filters.HttpCacheWriteBehavior],  # value
                                 _type.HRESULT]


class IHttpFilter(_inspectable.IInspectable):
    SendRequestAsync: _Callable[[_Windows_Web_Http.IHttpRequestMessage,  # request
                                 _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[_Windows_Web_Http.IHttpResponseMessage, _struct.Windows.Web.Http.HttpProgress]]],  # operation
                                _type.HRESULT]


class IHttpServerCustomValidationRequestedEventArgs(_inspectable.IInspectable):
    get_RequestMessage: _Callable[[_Pointer[_Windows_Web_Http.IHttpRequestMessage]],  # value
                                  _type.HRESULT]
    get_ServerCertificate: _Callable[[_Pointer[_Windows_Security_Cryptography_Certificates.ICertificate]],  # value
                                     _type.HRESULT]
    get_ServerCertificateErrorSeverity: _Callable[[_Pointer[_enum.Windows.Networking.Sockets.SocketSslErrorSeverity]],  # value
                                                  _type.HRESULT]
    get_ServerCertificateErrors: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Security.Cryptography.Certificates.ChainValidationResult]]],  # value
                                           _type.HRESULT]
    get_ServerIntermediateCertificates: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Security_Cryptography_Certificates.ICertificate]]],  # value
                                                  _type.HRESULT]
    Reject: _Callable[[],
                      _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]
