from __future__ import annotations

from typing import Callable as _Callable

from . import Filters as _Windows_Web_Http_Filters
from . import Headers as _Windows_Web_Http_Headers
from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Security.Cryptography import Certificates as _Windows_Security_Cryptography_Certificates
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IHttpBufferContentFactory(_inspectable.IInspectable):
    CreateFromBuffer: _Callable[[_Windows_Storage_Streams.IBuffer,  # content
                                 _Pointer[IHttpContent]],  # value
                                _type.HRESULT]
    CreateFromBufferWithOffset: _Callable[[_Windows_Storage_Streams.IBuffer,  # content
                                           _type.UINT32,  # offset
                                           _type.UINT32,  # count
                                           _Pointer[IHttpContent]],  # value
                                          _type.HRESULT]

    _factory = True


class IHttpClient(_inspectable.IInspectable):
    DeleteAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                            _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IHttpResponseMessage, _struct.Windows.Web.Http.HttpProgress]]],  # operation
                           _type.HRESULT]
    GetAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                         _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IHttpResponseMessage, _struct.Windows.Web.Http.HttpProgress]]],  # operation
                        _type.HRESULT]
    GetWithOptionAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                   _enum.Windows.Web.Http.HttpCompletionOption,  # completionOption
                                   _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IHttpResponseMessage, _struct.Windows.Web.Http.HttpProgress]]],  # operation
                                  _type.HRESULT]
    GetBufferAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                               _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[_Windows_Storage_Streams.IBuffer, _struct.Windows.Web.Http.HttpProgress]]],  # operation
                              _type.HRESULT]
    GetInputStreamAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                    _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[_Windows_Storage_Streams.IInputStream, _struct.Windows.Web.Http.HttpProgress]]],  # operation
                                   _type.HRESULT]
    GetStringAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                               _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[_type.HSTRING, _struct.Windows.Web.Http.HttpProgress]]],  # operation
                              _type.HRESULT]
    PostAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                          IHttpContent,  # content
                          _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IHttpResponseMessage, _struct.Windows.Web.Http.HttpProgress]]],  # operation
                         _type.HRESULT]
    PutAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                         IHttpContent,  # content
                         _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IHttpResponseMessage, _struct.Windows.Web.Http.HttpProgress]]],  # operation
                        _type.HRESULT]
    SendRequestAsync: _Callable[[IHttpRequestMessage,  # request
                                 _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IHttpResponseMessage, _struct.Windows.Web.Http.HttpProgress]]],  # operation
                                _type.HRESULT]
    SendRequestWithOptionAsync: _Callable[[IHttpRequestMessage,  # request
                                           _enum.Windows.Web.Http.HttpCompletionOption,  # completionOption
                                           _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IHttpResponseMessage, _struct.Windows.Web.Http.HttpProgress]]],  # operation
                                          _type.HRESULT]
    get_DefaultRequestHeaders: _Callable[[_Pointer[_Windows_Web_Http_Headers.IHttpRequestHeaderCollection]],  # value
                                         _type.HRESULT]


class IHttpClient2(_inspectable.IInspectable):
    TryDeleteAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                               _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IHttpRequestResult, _struct.Windows.Web.Http.HttpProgress]]],  # operation
                              _type.HRESULT]
    TryGetAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                            _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IHttpRequestResult, _struct.Windows.Web.Http.HttpProgress]]],  # operation
                           _type.HRESULT]
    TryGetAsync2: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                             _enum.Windows.Web.Http.HttpCompletionOption,  # completionOption
                             _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IHttpRequestResult, _struct.Windows.Web.Http.HttpProgress]]],  # operation
                            _type.HRESULT]
    TryGetBufferAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                  _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IHttpGetBufferResult, _struct.Windows.Web.Http.HttpProgress]]],  # operation
                                 _type.HRESULT]
    TryGetInputStreamAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                       _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IHttpGetInputStreamResult, _struct.Windows.Web.Http.HttpProgress]]],  # operation
                                      _type.HRESULT]
    TryGetStringAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                  _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IHttpGetStringResult, _struct.Windows.Web.Http.HttpProgress]]],  # operation
                                 _type.HRESULT]
    TryPostAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                             IHttpContent,  # content
                             _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IHttpRequestResult, _struct.Windows.Web.Http.HttpProgress]]],  # operation
                            _type.HRESULT]
    TryPutAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                            IHttpContent,  # content
                            _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IHttpRequestResult, _struct.Windows.Web.Http.HttpProgress]]],  # operation
                           _type.HRESULT]
    TrySendRequestAsync: _Callable[[IHttpRequestMessage,  # request
                                    _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IHttpRequestResult, _struct.Windows.Web.Http.HttpProgress]]],  # operation
                                   _type.HRESULT]
    TrySendRequestAsync2: _Callable[[IHttpRequestMessage,  # request
                                     _enum.Windows.Web.Http.HttpCompletionOption,  # completionOption
                                     _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IHttpRequestResult, _struct.Windows.Web.Http.HttpProgress]]],  # operation
                                    _type.HRESULT]


class IHttpClient3(_inspectable.IInspectable):
    get_DefaultPrivacyAnnotation: _Callable[[_Pointer[_type.HSTRING]],  # value
                                            _type.HRESULT]
    put_DefaultPrivacyAnnotation: _Callable[[_type.HSTRING],  # value
                                            _type.HRESULT]


class IHttpClientFactory(_inspectable.IInspectable):
    Create: _Callable[[_Windows_Web_Http_Filters.IHttpFilter,  # filter
                       _Pointer[IHttpClient]],  # value
                      _type.HRESULT]

    _factory = True


class IHttpContent(_inspectable.IInspectable):
    get_Headers: _Callable[[_Pointer[_Windows_Web_Http_Headers.IHttpContentHeaderCollection]],  # value
                           _type.HRESULT]
    BufferAllAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperationWithProgress[_type.UINT64, _type.UINT64]]],  # operation
                              _type.HRESULT]
    ReadAsBufferAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperationWithProgress[_Windows_Storage_Streams.IBuffer, _type.UINT64]]],  # operation
                                 _type.HRESULT]
    ReadAsInputStreamAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperationWithProgress[_Windows_Storage_Streams.IInputStream, _type.UINT64]]],  # operation
                                      _type.HRESULT]
    ReadAsStringAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperationWithProgress[_type.HSTRING, _type.UINT64]]],  # operation
                                 _type.HRESULT]
    TryComputeLength: _Callable[[_Pointer[_type.UINT64],  # length
                                 _Pointer[_type.boolean]],  # succeeded
                                _type.HRESULT]
    WriteToStreamAsync: _Callable[[_Windows_Storage_Streams.IOutputStream,  # outputStream
                                   _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[_type.UINT64, _type.UINT64]]],  # operation
                                  _type.HRESULT]


class IHttpCookie(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Domain: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Path: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Expires: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                           _type.HRESULT]
    put_Expires: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                           _type.HRESULT]
    get_HttpOnly: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    put_HttpOnly: _Callable[[_type.boolean],  # value
                            _type.HRESULT]
    get_Secure: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_Secure: _Callable[[_type.boolean],  # value
                          _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Value: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]


class IHttpCookieFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.HSTRING,  # name
                       _type.HSTRING,  # domain
                       _type.HSTRING,  # path
                       _Pointer[IHttpCookie]],  # value
                      _type.HRESULT]

    _factory = True


class IHttpCookieManager(_inspectable.IInspectable):
    SetCookie: _Callable[[IHttpCookie,  # cookie
                          _Pointer[_type.boolean]],  # result
                         _type.HRESULT]
    SetCookieWithThirdParty: _Callable[[IHttpCookie,  # cookie
                                        _type.boolean,  # thirdParty
                                        _Pointer[_type.boolean]],  # result
                                       _type.HRESULT]
    DeleteCookie: _Callable[[IHttpCookie],  # cookie
                            _type.HRESULT]
    GetCookies: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                           _Pointer[_Windows_Foundation_Collections.IVectorView[IHttpCookie]]],  # result
                          _type.HRESULT]


class IHttpFormUrlEncodedContentFactory(_inspectable.IInspectable):
    Create: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Foundation_Collections.IKeyValuePair[_type.HSTRING, _type.HSTRING]],  # content
                       _Pointer[IHttpContent]],  # value
                      _type.HRESULT]

    _factory = True


class IHttpGetBufferResult(_inspectable.IInspectable):
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]
    get_RequestMessage: _Callable[[_Pointer[IHttpRequestMessage]],  # value
                                  _type.HRESULT]
    get_ResponseMessage: _Callable[[_Pointer[IHttpResponseMessage]],  # value
                                   _type.HRESULT]
    get_Succeeded: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_Value: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                         _type.HRESULT]


class IHttpGetInputStreamResult(_inspectable.IInspectable):
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]
    get_RequestMessage: _Callable[[_Pointer[IHttpRequestMessage]],  # value
                                  _type.HRESULT]
    get_ResponseMessage: _Callable[[_Pointer[IHttpResponseMessage]],  # value
                                   _type.HRESULT]
    get_Succeeded: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_Value: _Callable[[_Pointer[_Windows_Storage_Streams.IInputStream]],  # value
                         _type.HRESULT]


class IHttpGetStringResult(_inspectable.IInspectable):
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]
    get_RequestMessage: _Callable[[_Pointer[IHttpRequestMessage]],  # value
                                  _type.HRESULT]
    get_ResponseMessage: _Callable[[_Pointer[IHttpResponseMessage]],  # value
                                   _type.HRESULT]
    get_Succeeded: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]


class IHttpMethod(_inspectable.IInspectable):
    get_Method: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]


class IHttpMethodFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.HSTRING,  # method
                       _Pointer[IHttpMethod]],  # value
                      _type.HRESULT]

    _factory = True


class IHttpMethodStatics(_inspectable.IInspectable):
    get_Delete: _Callable[[_Pointer[IHttpMethod]],  # value
                          _type.HRESULT]
    get_Get: _Callable[[_Pointer[IHttpMethod]],  # value
                       _type.HRESULT]
    get_Head: _Callable[[_Pointer[IHttpMethod]],  # value
                        _type.HRESULT]
    get_Options: _Callable[[_Pointer[IHttpMethod]],  # value
                           _type.HRESULT]
    get_Patch: _Callable[[_Pointer[IHttpMethod]],  # value
                         _type.HRESULT]
    get_Post: _Callable[[_Pointer[IHttpMethod]],  # value
                        _type.HRESULT]
    get_Put: _Callable[[_Pointer[IHttpMethod]],  # value
                       _type.HRESULT]

    _factory = True


class IHttpMultipartContent(_inspectable.IInspectable):
    Add: _Callable[[IHttpContent],  # content
                   _type.HRESULT]


class IHttpMultipartContentFactory(_inspectable.IInspectable):
    CreateWithSubtype: _Callable[[_type.HSTRING,  # subtype
                                  _Pointer[IHttpContent]],  # value
                                 _type.HRESULT]
    CreateWithSubtypeAndBoundary: _Callable[[_type.HSTRING,  # subtype
                                             _type.HSTRING,  # boundary
                                             _Pointer[IHttpContent]],  # value
                                            _type.HRESULT]

    _factory = True


class IHttpMultipartFormDataContent(_inspectable.IInspectable):
    Add: _Callable[[IHttpContent],  # content
                   _type.HRESULT]
    AddWithName: _Callable[[IHttpContent,  # content
                            _type.HSTRING],  # name
                           _type.HRESULT]
    AddWithNameAndFileName: _Callable[[IHttpContent,  # content
                                       _type.HSTRING,  # name
                                       _type.HSTRING],  # fileName
                                      _type.HRESULT]


class IHttpMultipartFormDataContentFactory(_inspectable.IInspectable):
    CreateWithBoundary: _Callable[[_type.HSTRING,  # boundary
                                   _Pointer[IHttpContent]],  # value
                                  _type.HRESULT]

    _factory = True


class IHttpRequestMessage(_inspectable.IInspectable):
    get_Content: _Callable[[_Pointer[IHttpContent]],  # value
                           _type.HRESULT]
    put_Content: _Callable[[IHttpContent],  # value
                           _type.HRESULT]
    get_Headers: _Callable[[_Pointer[_Windows_Web_Http_Headers.IHttpRequestHeaderCollection]],  # value
                           _type.HRESULT]
    get_Method: _Callable[[_Pointer[IHttpMethod]],  # value
                          _type.HRESULT]
    put_Method: _Callable[[IHttpMethod],  # value
                          _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, _inspectable.IInspectable]]],  # value
                              _type.HRESULT]
    get_RequestUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                              _type.HRESULT]
    put_RequestUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                              _type.HRESULT]
    get_TransportInformation: _Callable[[_Pointer[IHttpTransportInformation]],  # value
                                        _type.HRESULT]


class IHttpRequestMessage2(_inspectable.IInspectable):
    get_PrivacyAnnotation: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    put_PrivacyAnnotation: _Callable[[_type.HSTRING],  # value
                                     _type.HRESULT]


class IHttpRequestMessageFactory(_inspectable.IInspectable):
    Create: _Callable[[IHttpMethod,  # method
                       _Windows_Foundation.IUriRuntimeClass,  # uri
                       _Pointer[IHttpRequestMessage]],  # value
                      _type.HRESULT]

    _factory = True


class IHttpRequestResult(_inspectable.IInspectable):
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]
    get_RequestMessage: _Callable[[_Pointer[IHttpRequestMessage]],  # value
                                  _type.HRESULT]
    get_ResponseMessage: _Callable[[_Pointer[IHttpResponseMessage]],  # value
                                   _type.HRESULT]
    get_Succeeded: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]


class IHttpResponseMessage(_inspectable.IInspectable):
    get_Content: _Callable[[_Pointer[IHttpContent]],  # value
                           _type.HRESULT]
    put_Content: _Callable[[IHttpContent],  # value
                           _type.HRESULT]
    get_Headers: _Callable[[_Pointer[_Windows_Web_Http_Headers.IHttpResponseHeaderCollection]],  # value
                           _type.HRESULT]
    get_IsSuccessStatusCode: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    get_ReasonPhrase: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    put_ReasonPhrase: _Callable[[_type.HSTRING],  # value
                                _type.HRESULT]
    get_RequestMessage: _Callable[[_Pointer[IHttpRequestMessage]],  # value
                                  _type.HRESULT]
    put_RequestMessage: _Callable[[IHttpRequestMessage],  # value
                                  _type.HRESULT]
    get_Source: _Callable[[_Pointer[_enum.Windows.Web.Http.HttpResponseMessageSource]],  # value
                          _type.HRESULT]
    put_Source: _Callable[[_enum.Windows.Web.Http.HttpResponseMessageSource],  # value
                          _type.HRESULT]
    get_StatusCode: _Callable[[_Pointer[_enum.Windows.Web.Http.HttpStatusCode]],  # value
                              _type.HRESULT]
    put_StatusCode: _Callable[[_enum.Windows.Web.Http.HttpStatusCode],  # value
                              _type.HRESULT]
    get_Version: _Callable[[_Pointer[_enum.Windows.Web.Http.HttpVersion]],  # value
                           _type.HRESULT]
    put_Version: _Callable[[_enum.Windows.Web.Http.HttpVersion],  # value
                           _type.HRESULT]
    EnsureSuccessStatusCode: _Callable[[_Pointer[IHttpResponseMessage]],  # result
                                       _type.HRESULT]


class IHttpResponseMessageFactory(_inspectable.IInspectable):
    Create: _Callable[[_enum.Windows.Web.Http.HttpStatusCode,  # statusCode
                       _Pointer[IHttpResponseMessage]],  # value
                      _type.HRESULT]

    _factory = True


class IHttpStreamContentFactory(_inspectable.IInspectable):
    CreateFromInputStream: _Callable[[_Windows_Storage_Streams.IInputStream,  # content
                                      _Pointer[IHttpContent]],  # value
                                     _type.HRESULT]

    _factory = True


class IHttpStringContentFactory(_inspectable.IInspectable):
    CreateFromString: _Callable[[_type.HSTRING,  # content
                                 _Pointer[IHttpContent]],  # value
                                _type.HRESULT]
    CreateFromStringWithEncoding: _Callable[[_type.HSTRING,  # content
                                             _enum.Windows.Storage.Streams.UnicodeEncoding,  # encoding
                                             _Pointer[IHttpContent]],  # value
                                            _type.HRESULT]
    CreateFromStringWithEncodingAndMediaType: _Callable[[_type.HSTRING,  # content
                                                         _enum.Windows.Storage.Streams.UnicodeEncoding,  # encoding
                                                         _type.HSTRING,  # mediaType
                                                         _Pointer[IHttpContent]],  # value
                                                        _type.HRESULT]

    _factory = True


class IHttpTransportInformation(_inspectable.IInspectable):
    get_ServerCertificate: _Callable[[_Pointer[_Windows_Security_Cryptography_Certificates.ICertificate]],  # value
                                     _type.HRESULT]
    get_ServerCertificateErrorSeverity: _Callable[[_Pointer[_enum.Windows.Networking.Sockets.SocketSslErrorSeverity]],  # value
                                                  _type.HRESULT]
    get_ServerCertificateErrors: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Security.Cryptography.Certificates.ChainValidationResult]]],  # value
                                           _type.HRESULT]
    get_ServerIntermediateCertificates: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Security_Cryptography_Certificates.ICertificate]]],  # value
                                                  _type.HRESULT]
