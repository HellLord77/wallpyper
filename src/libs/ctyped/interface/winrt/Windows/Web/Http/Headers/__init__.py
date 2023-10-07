from __future__ import annotations as _

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from .... import Networking as _Windows_Networking
from ....Foundation import Collections as _Windows_Foundation_Collections
from ....Storage import Streams as _Windows_Storage_Streams
from ..... import inspectable as _inspectable
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IHttpCacheDirectiveHeaderValueCollection(_inspectable.IInspectable):
    get_MaxAge: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                          _type.HRESULT]
    put_MaxAge: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]],  # value
                          _type.HRESULT]
    get_MaxStale: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                            _type.HRESULT]
    put_MaxStale: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    get_MinFresh: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                            _type.HRESULT]
    put_MinFresh: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    get_SharedMaxAge: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                _type.HRESULT]
    put_SharedMaxAge: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]],  # value
                                _type.HRESULT]
    ParseAdd: _Callable[[_type.HSTRING],  # input
                        _type.HRESULT]
    TryParseAdd: _Callable[[_type.HSTRING,  # input
                            _Pointer[_type.boolean]],  # result
                           _type.HRESULT]


class IHttpChallengeHeaderValue(_inspectable.IInspectable):
    get_Parameters: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IHttpNameValueHeaderValue]]],  # value
                              _type.HRESULT]
    get_Scheme: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Token: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]


class IHttpChallengeHeaderValueCollection(_inspectable.IInspectable):
    ParseAdd: _Callable[[_type.HSTRING],  # input
                        _type.HRESULT]
    TryParseAdd: _Callable[[_type.HSTRING,  # input
                            _Pointer[_type.boolean]],  # result
                           _type.HRESULT]


class IHttpChallengeHeaderValueFactory(_inspectable.IInspectable, factory=True):
    CreateFromScheme: _Callable[[_type.HSTRING,  # scheme
                                 _Pointer[IHttpChallengeHeaderValue]],  # value
                                _type.HRESULT]
    CreateFromSchemeWithToken: _Callable[[_type.HSTRING,  # scheme
                                          _type.HSTRING,  # token
                                          _Pointer[IHttpChallengeHeaderValue]],  # value
                                         _type.HRESULT]


class IHttpChallengeHeaderValueStatics(_inspectable.IInspectable, factory=True):
    Parse: _Callable[[_type.HSTRING,  # input
                      _Pointer[IHttpChallengeHeaderValue]],  # result
                     _type.HRESULT]
    TryParse: _Callable[[_type.HSTRING,  # input
                         _Pointer[IHttpChallengeHeaderValue],  # challengeHeaderValue
                         _Pointer[_type.boolean]],  # succeeded
                        _type.HRESULT]


class IHttpConnectionOptionHeaderValue(_inspectable.IInspectable):
    get_Token: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]


class IHttpConnectionOptionHeaderValueCollection(_inspectable.IInspectable):
    ParseAdd: _Callable[[_type.HSTRING],  # input
                        _type.HRESULT]
    TryParseAdd: _Callable[[_type.HSTRING,  # input
                            _Pointer[_type.boolean]],  # result
                           _type.HRESULT]


class IHttpConnectionOptionHeaderValueFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.HSTRING,  # token
                       _Pointer[IHttpConnectionOptionHeaderValue]],  # value
                      _type.HRESULT]


class IHttpConnectionOptionHeaderValueStatics(_inspectable.IInspectable, factory=True):
    Parse: _Callable[[_type.HSTRING,  # input
                      _Pointer[IHttpConnectionOptionHeaderValue]],  # result
                     _type.HRESULT]
    TryParse: _Callable[[_type.HSTRING,  # input
                         _Pointer[IHttpConnectionOptionHeaderValue],  # connectionOptionHeaderValue
                         _Pointer[_type.boolean]],  # succeeded
                        _type.HRESULT]


class IHttpContentCodingHeaderValue(_inspectable.IInspectable):
    get_ContentCoding: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]


class IHttpContentCodingHeaderValueCollection(_inspectable.IInspectable):
    ParseAdd: _Callable[[_type.HSTRING],  # input
                        _type.HRESULT]
    TryParseAdd: _Callable[[_type.HSTRING,  # input
                            _Pointer[_type.boolean]],  # result
                           _type.HRESULT]


class IHttpContentCodingHeaderValueFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.HSTRING,  # contentCoding
                       _Pointer[IHttpContentCodingHeaderValue]],  # value
                      _type.HRESULT]


class IHttpContentCodingHeaderValueStatics(_inspectable.IInspectable, factory=True):
    Parse: _Callable[[_type.HSTRING,  # input
                      _Pointer[IHttpContentCodingHeaderValue]],  # result
                     _type.HRESULT]
    TryParse: _Callable[[_type.HSTRING,  # input
                         _Pointer[IHttpContentCodingHeaderValue],  # contentCodingHeaderValue
                         _Pointer[_type.boolean]],  # succeeded
                        _type.HRESULT]


class IHttpContentCodingWithQualityHeaderValue(_inspectable.IInspectable):
    get_ContentCoding: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_Quality: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                           _type.HRESULT]


class IHttpContentCodingWithQualityHeaderValueCollection(_inspectable.IInspectable):
    ParseAdd: _Callable[[_type.HSTRING],  # input
                        _type.HRESULT]
    TryParseAdd: _Callable[[_type.HSTRING,  # input
                            _Pointer[_type.boolean]],  # result
                           _type.HRESULT]


class IHttpContentCodingWithQualityHeaderValueFactory(_inspectable.IInspectable, factory=True):
    CreateFromValue: _Callable[[_type.HSTRING,  # contentCoding
                                _Pointer[IHttpContentCodingWithQualityHeaderValue]],  # value
                               _type.HRESULT]
    CreateFromValueWithQuality: _Callable[[_type.HSTRING,  # contentCoding
                                           _type.DOUBLE,  # quality
                                           _Pointer[IHttpContentCodingWithQualityHeaderValue]],  # value
                                          _type.HRESULT]


class IHttpContentCodingWithQualityHeaderValueStatics(_inspectable.IInspectable, factory=True):
    Parse: _Callable[[_type.HSTRING,  # input
                      _Pointer[IHttpContentCodingWithQualityHeaderValue]],  # result
                     _type.HRESULT]
    TryParse: _Callable[[_type.HSTRING,  # input
                         _Pointer[IHttpContentCodingWithQualityHeaderValue],  # contentCodingWithQualityHeaderValue
                         _Pointer[_type.boolean]],  # succeeded
                        _type.HRESULT]


class IHttpContentDispositionHeaderValue(_inspectable.IInspectable):
    get_DispositionType: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    put_DispositionType: _Callable[[_type.HSTRING],  # value
                                   _type.HRESULT]
    get_FileName: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_FileName: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_FileNameStar: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    put_FileNameStar: _Callable[[_type.HSTRING],  # value
                                _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Name: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_Parameters: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IHttpNameValueHeaderValue]]],  # value
                              _type.HRESULT]
    get_Size: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT64]]],  # value
                        _type.HRESULT]
    put_Size: _Callable[[_Windows_Foundation.IReference[_type.UINT64]],  # value
                        _type.HRESULT]


class IHttpContentDispositionHeaderValueFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.HSTRING,  # dispositionType
                       _Pointer[IHttpContentDispositionHeaderValue]],  # value
                      _type.HRESULT]


class IHttpContentDispositionHeaderValueStatics(_inspectable.IInspectable, factory=True):
    Parse: _Callable[[_type.HSTRING,  # input
                      _Pointer[IHttpContentDispositionHeaderValue]],  # result
                     _type.HRESULT]
    TryParse: _Callable[[_type.HSTRING,  # input
                         _Pointer[IHttpContentDispositionHeaderValue],  # contentDispositionHeaderValue
                         _Pointer[_type.boolean]],  # succeeded
                        _type.HRESULT]


class IHttpContentHeaderCollection(_inspectable.IInspectable):
    get_ContentDisposition: _Callable[[_Pointer[IHttpContentDispositionHeaderValue]],  # value
                                      _type.HRESULT]
    put_ContentDisposition: _Callable[[IHttpContentDispositionHeaderValue],  # value
                                      _type.HRESULT]
    get_ContentEncoding: _Callable[[_Pointer[IHttpContentCodingHeaderValueCollection]],  # value
                                   _type.HRESULT]
    get_ContentLanguage: _Callable[[_Pointer[IHttpLanguageHeaderValueCollection]],  # value
                                   _type.HRESULT]
    get_ContentLength: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT64]]],  # value
                                 _type.HRESULT]
    put_ContentLength: _Callable[[_Windows_Foundation.IReference[_type.UINT64]],  # value
                                 _type.HRESULT]
    get_ContentLocation: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                   _type.HRESULT]
    put_ContentLocation: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                                   _type.HRESULT]
    get_ContentMD5: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                              _type.HRESULT]
    put_ContentMD5: _Callable[[_Windows_Storage_Streams.IBuffer],  # value
                              _type.HRESULT]
    get_ContentRange: _Callable[[_Pointer[IHttpContentRangeHeaderValue]],  # value
                                _type.HRESULT]
    put_ContentRange: _Callable[[IHttpContentRangeHeaderValue],  # value
                                _type.HRESULT]
    get_ContentType: _Callable[[_Pointer[IHttpMediaTypeHeaderValue]],  # value
                               _type.HRESULT]
    put_ContentType: _Callable[[IHttpMediaTypeHeaderValue],  # value
                               _type.HRESULT]
    get_Expires: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                           _type.HRESULT]
    put_Expires: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                           _type.HRESULT]
    get_LastModified: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                _type.HRESULT]
    put_LastModified: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                                _type.HRESULT]
    Append: _Callable[[_type.HSTRING,  # name
                       _type.HSTRING],  # value
                      _type.HRESULT]
    TryAppendWithoutValidation: _Callable[[_type.HSTRING,  # name
                                           _type.HSTRING,  # value
                                           _Pointer[_type.boolean]],  # result
                                          _type.HRESULT]


class IHttpContentRangeHeaderValue(_inspectable.IInspectable):
    get_FirstBytePosition: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT64]]],  # value
                                     _type.HRESULT]
    get_LastBytePosition: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT64]]],  # value
                                    _type.HRESULT]
    get_Length: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT64]]],  # value
                          _type.HRESULT]
    get_Unit: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Unit: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]


class IHttpContentRangeHeaderValueFactory(_inspectable.IInspectable, factory=True):
    CreateFromLength: _Callable[[_type.UINT64,  # length
                                 _Pointer[IHttpContentRangeHeaderValue]],  # value
                                _type.HRESULT]
    CreateFromRange: _Callable[[_type.UINT64,  # from
                                _type.UINT64,  # to
                                _Pointer[IHttpContentRangeHeaderValue]],  # value
                               _type.HRESULT]
    CreateFromRangeWithLength: _Callable[[_type.UINT64,  # from
                                          _type.UINT64,  # to
                                          _type.UINT64,  # length
                                          _Pointer[IHttpContentRangeHeaderValue]],  # value
                                         _type.HRESULT]


class IHttpContentRangeHeaderValueStatics(_inspectable.IInspectable, factory=True):
    Parse: _Callable[[_type.HSTRING,  # input
                      _Pointer[IHttpContentRangeHeaderValue]],  # result
                     _type.HRESULT]
    TryParse: _Callable[[_type.HSTRING,  # input
                         _Pointer[IHttpContentRangeHeaderValue],  # contentRangeHeaderValue
                         _Pointer[_type.boolean]],  # succeeded
                        _type.HRESULT]


class IHttpCookiePairHeaderValue(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Value: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]


class IHttpCookiePairHeaderValueCollection(_inspectable.IInspectable):
    ParseAdd: _Callable[[_type.HSTRING],  # input
                        _type.HRESULT]
    TryParseAdd: _Callable[[_type.HSTRING,  # input
                            _Pointer[_type.boolean]],  # result
                           _type.HRESULT]


class IHttpCookiePairHeaderValueFactory(_inspectable.IInspectable, factory=True):
    CreateFromName: _Callable[[_type.HSTRING,  # name
                               _Pointer[IHttpCookiePairHeaderValue]],  # value
                              _type.HRESULT]
    CreateFromNameWithValue: _Callable[[_type.HSTRING,  # name
                                        _type.HSTRING,  # value
                                        _Pointer[IHttpCookiePairHeaderValue]],  # cookiePairHeaderValue
                                       _type.HRESULT]


class IHttpCookiePairHeaderValueStatics(_inspectable.IInspectable, factory=True):
    Parse: _Callable[[_type.HSTRING,  # input
                      _Pointer[IHttpCookiePairHeaderValue]],  # result
                     _type.HRESULT]
    TryParse: _Callable[[_type.HSTRING,  # input
                         _Pointer[IHttpCookiePairHeaderValue],  # cookiePairHeaderValue
                         _Pointer[_type.boolean]],  # succeeded
                        _type.HRESULT]


class IHttpCredentialsHeaderValue(_inspectable.IInspectable):
    get_Parameters: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IHttpNameValueHeaderValue]]],  # value
                              _type.HRESULT]
    get_Scheme: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Token: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]


class IHttpCredentialsHeaderValueFactory(_inspectable.IInspectable, factory=True):
    CreateFromScheme: _Callable[[_type.HSTRING,  # scheme
                                 _Pointer[IHttpCredentialsHeaderValue]],  # value
                                _type.HRESULT]
    CreateFromSchemeWithToken: _Callable[[_type.HSTRING,  # scheme
                                          _type.HSTRING,  # token
                                          _Pointer[IHttpCredentialsHeaderValue]],  # value
                                         _type.HRESULT]


class IHttpCredentialsHeaderValueStatics(_inspectable.IInspectable, factory=True):
    Parse: _Callable[[_type.HSTRING,  # input
                      _Pointer[IHttpCredentialsHeaderValue]],  # result
                     _type.HRESULT]
    TryParse: _Callable[[_type.HSTRING,  # input
                         _Pointer[IHttpCredentialsHeaderValue],  # credentialsHeaderValue
                         _Pointer[_type.boolean]],  # succeeded
                        _type.HRESULT]


class IHttpDateOrDeltaHeaderValue(_inspectable.IInspectable):
    get_Date: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                        _type.HRESULT]
    get_Delta: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                         _type.HRESULT]


class IHttpDateOrDeltaHeaderValueStatics(_inspectable.IInspectable, factory=True):
    Parse: _Callable[[_type.HSTRING,  # input
                      _Pointer[IHttpDateOrDeltaHeaderValue]],  # result
                     _type.HRESULT]
    TryParse: _Callable[[_type.HSTRING,  # input
                         _Pointer[IHttpDateOrDeltaHeaderValue],  # dateOrDeltaHeaderValue
                         _Pointer[_type.boolean]],  # succeeded
                        _type.HRESULT]


class IHttpExpectationHeaderValue(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Value: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Parameters: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IHttpNameValueHeaderValue]]],  # value
                              _type.HRESULT]


class IHttpExpectationHeaderValueCollection(_inspectable.IInspectable):
    ParseAdd: _Callable[[_type.HSTRING],  # input
                        _type.HRESULT]
    TryParseAdd: _Callable[[_type.HSTRING,  # input
                            _Pointer[_type.boolean]],  # result
                           _type.HRESULT]


class IHttpExpectationHeaderValueFactory(_inspectable.IInspectable, factory=True):
    CreateFromName: _Callable[[_type.HSTRING,  # name
                               _Pointer[IHttpExpectationHeaderValue]],  # value
                              _type.HRESULT]
    CreateFromNameWithValue: _Callable[[_type.HSTRING,  # name
                                        _type.HSTRING,  # value
                                        _Pointer[IHttpExpectationHeaderValue]],  # expectationHeaderValue
                                       _type.HRESULT]


class IHttpExpectationHeaderValueStatics(_inspectable.IInspectable, factory=True):
    Parse: _Callable[[_type.HSTRING,  # input
                      _Pointer[IHttpExpectationHeaderValue]],  # result
                     _type.HRESULT]
    TryParse: _Callable[[_type.HSTRING,  # input
                         _Pointer[IHttpExpectationHeaderValue],  # expectationHeaderValue
                         _Pointer[_type.boolean]],  # succeeded
                        _type.HRESULT]


class IHttpLanguageHeaderValueCollection(_inspectable.IInspectable):
    ParseAdd: _Callable[[_type.HSTRING],  # input
                        _type.HRESULT]
    TryParseAdd: _Callable[[_type.HSTRING,  # input
                            _Pointer[_type.boolean]],  # result
                           _type.HRESULT]


class IHttpLanguageRangeWithQualityHeaderValue(_inspectable.IInspectable):
    get_LanguageRange: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_Quality: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                           _type.HRESULT]


class IHttpLanguageRangeWithQualityHeaderValueCollection(_inspectable.IInspectable):
    ParseAdd: _Callable[[_type.HSTRING],  # input
                        _type.HRESULT]
    TryParseAdd: _Callable[[_type.HSTRING,  # input
                            _Pointer[_type.boolean]],  # result
                           _type.HRESULT]


class IHttpLanguageRangeWithQualityHeaderValueFactory(_inspectable.IInspectable, factory=True):
    CreateFromLanguageRange: _Callable[[_type.HSTRING,  # languageRange
                                        _Pointer[IHttpLanguageRangeWithQualityHeaderValue]],  # value
                                       _type.HRESULT]
    CreateFromLanguageRangeWithQuality: _Callable[[_type.HSTRING,  # languageRange
                                                   _type.DOUBLE,  # quality
                                                   _Pointer[IHttpLanguageRangeWithQualityHeaderValue]],  # value
                                                  _type.HRESULT]


class IHttpLanguageRangeWithQualityHeaderValueStatics(_inspectable.IInspectable, factory=True):
    Parse: _Callable[[_type.HSTRING,  # input
                      _Pointer[IHttpLanguageRangeWithQualityHeaderValue]],  # result
                     _type.HRESULT]
    TryParse: _Callable[[_type.HSTRING,  # input
                         _Pointer[IHttpLanguageRangeWithQualityHeaderValue],  # languageRangeWithQualityHeaderValue
                         _Pointer[_type.boolean]],  # succeeded
                        _type.HRESULT]


class IHttpMediaTypeHeaderValue(_inspectable.IInspectable):
    get_CharSet: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    put_CharSet: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    get_MediaType: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_MediaType: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_Parameters: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IHttpNameValueHeaderValue]]],  # value
                              _type.HRESULT]


class IHttpMediaTypeHeaderValueFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.HSTRING,  # mediaType
                       _Pointer[IHttpMediaTypeHeaderValue]],  # value
                      _type.HRESULT]


class IHttpMediaTypeHeaderValueStatics(_inspectable.IInspectable, factory=True):
    Parse: _Callable[[_type.HSTRING,  # input
                      _Pointer[IHttpMediaTypeHeaderValue]],  # result
                     _type.HRESULT]
    TryParse: _Callable[[_type.HSTRING,  # input
                         _Pointer[IHttpMediaTypeHeaderValue],  # mediaTypeHeaderValue
                         _Pointer[_type.boolean]],  # succeeded
                        _type.HRESULT]


class IHttpMediaTypeWithQualityHeaderValue(_inspectable.IInspectable):
    get_CharSet: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    put_CharSet: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    get_MediaType: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_MediaType: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_Parameters: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IHttpNameValueHeaderValue]]],  # value
                              _type.HRESULT]
    get_Quality: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                           _type.HRESULT]
    put_Quality: _Callable[[_Windows_Foundation.IReference[_type.DOUBLE]],  # value
                           _type.HRESULT]


class IHttpMediaTypeWithQualityHeaderValueCollection(_inspectable.IInspectable):
    ParseAdd: _Callable[[_type.HSTRING],  # input
                        _type.HRESULT]
    TryParseAdd: _Callable[[_type.HSTRING,  # input
                            _Pointer[_type.boolean]],  # result
                           _type.HRESULT]


class IHttpMediaTypeWithQualityHeaderValueFactory(_inspectable.IInspectable, factory=True):
    CreateFromMediaType: _Callable[[_type.HSTRING,  # mediaType
                                    _Pointer[IHttpMediaTypeWithQualityHeaderValue]],  # value
                                   _type.HRESULT]
    CreateFromMediaTypeWithQuality: _Callable[[_type.HSTRING,  # mediaType
                                               _type.DOUBLE,  # quality
                                               _Pointer[IHttpMediaTypeWithQualityHeaderValue]],  # value
                                              _type.HRESULT]


class IHttpMediaTypeWithQualityHeaderValueStatics(_inspectable.IInspectable, factory=True):
    Parse: _Callable[[_type.HSTRING,  # input
                      _Pointer[IHttpMediaTypeWithQualityHeaderValue]],  # result
                     _type.HRESULT]
    TryParse: _Callable[[_type.HSTRING,  # input
                         _Pointer[IHttpMediaTypeWithQualityHeaderValue],  # mediaTypeWithQualityHeaderValue
                         _Pointer[_type.boolean]],  # succeeded
                        _type.HRESULT]


class IHttpMethodHeaderValueCollection(_inspectable.IInspectable):
    ParseAdd: _Callable[[_type.HSTRING],  # input
                        _type.HRESULT]
    TryParseAdd: _Callable[[_type.HSTRING,  # input
                            _Pointer[_type.boolean]],  # result
                           _type.HRESULT]


class IHttpNameValueHeaderValue(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Value: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]


class IHttpNameValueHeaderValueFactory(_inspectable.IInspectable, factory=True):
    CreateFromName: _Callable[[_type.HSTRING,  # name
                               _Pointer[IHttpNameValueHeaderValue]],  # value
                              _type.HRESULT]
    CreateFromNameWithValue: _Callable[[_type.HSTRING,  # name
                                        _type.HSTRING,  # value
                                        _Pointer[IHttpNameValueHeaderValue]],  # nameValueHeaderValue
                                       _type.HRESULT]


class IHttpNameValueHeaderValueStatics(_inspectable.IInspectable, factory=True):
    Parse: _Callable[[_type.HSTRING,  # input
                      _Pointer[IHttpNameValueHeaderValue]],  # result
                     _type.HRESULT]
    TryParse: _Callable[[_type.HSTRING,  # input
                         _Pointer[IHttpNameValueHeaderValue],  # nameValueHeaderValue
                         _Pointer[_type.boolean]],  # succeeded
                        _type.HRESULT]


class IHttpProductHeaderValue(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Version: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]


class IHttpProductHeaderValueFactory(_inspectable.IInspectable, factory=True):
    CreateFromName: _Callable[[_type.HSTRING,  # productName
                               _Pointer[IHttpProductHeaderValue]],  # value
                              _type.HRESULT]
    CreateFromNameWithVersion: _Callable[[_type.HSTRING,  # productName
                                          _type.HSTRING,  # productVersion
                                          _Pointer[IHttpProductHeaderValue]],  # value
                                         _type.HRESULT]


class IHttpProductHeaderValueStatics(_inspectable.IInspectable, factory=True):
    Parse: _Callable[[_type.HSTRING,  # input
                      _Pointer[IHttpProductHeaderValue]],  # result
                     _type.HRESULT]
    TryParse: _Callable[[_type.HSTRING,  # input
                         _Pointer[IHttpProductHeaderValue],  # productHeaderValue
                         _Pointer[_type.boolean]],  # succeeded
                        _type.HRESULT]


class IHttpProductInfoHeaderValue(_inspectable.IInspectable):
    get_Product: _Callable[[_Pointer[IHttpProductHeaderValue]],  # value
                           _type.HRESULT]
    get_Comment: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]


class IHttpProductInfoHeaderValueCollection(_inspectable.IInspectable):
    ParseAdd: _Callable[[_type.HSTRING],  # input
                        _type.HRESULT]
    TryParseAdd: _Callable[[_type.HSTRING,  # input
                            _Pointer[_type.boolean]],  # result
                           _type.HRESULT]


class IHttpProductInfoHeaderValueFactory(_inspectable.IInspectable, factory=True):
    CreateFromComment: _Callable[[_type.HSTRING,  # productComment
                                  _Pointer[IHttpProductInfoHeaderValue]],  # value
                                 _type.HRESULT]
    CreateFromNameWithVersion: _Callable[[_type.HSTRING,  # productName
                                          _type.HSTRING,  # productVersion
                                          _Pointer[IHttpProductInfoHeaderValue]],  # value
                                         _type.HRESULT]


class IHttpProductInfoHeaderValueStatics(_inspectable.IInspectable, factory=True):
    Parse: _Callable[[_type.HSTRING,  # input
                      _Pointer[IHttpProductInfoHeaderValue]],  # result
                     _type.HRESULT]
    TryParse: _Callable[[_type.HSTRING,  # input
                         _Pointer[IHttpProductInfoHeaderValue],  # productInfoHeaderValue
                         _Pointer[_type.boolean]],  # succeeded
                        _type.HRESULT]


class IHttpRequestHeaderCollection(_inspectable.IInspectable):
    get_Accept: _Callable[[_Pointer[IHttpMediaTypeWithQualityHeaderValueCollection]],  # value
                          _type.HRESULT]
    get_AcceptEncoding: _Callable[[_Pointer[IHttpContentCodingWithQualityHeaderValueCollection]],  # value
                                  _type.HRESULT]
    get_AcceptLanguage: _Callable[[_Pointer[IHttpLanguageRangeWithQualityHeaderValueCollection]],  # value
                                  _type.HRESULT]
    get_Authorization: _Callable[[_Pointer[IHttpCredentialsHeaderValue]],  # value
                                 _type.HRESULT]
    put_Authorization: _Callable[[IHttpCredentialsHeaderValue],  # value
                                 _type.HRESULT]
    get_CacheControl: _Callable[[_Pointer[IHttpCacheDirectiveHeaderValueCollection]],  # value
                                _type.HRESULT]
    get_Connection: _Callable[[_Pointer[IHttpConnectionOptionHeaderValueCollection]],  # value
                              _type.HRESULT]
    get_Cookie: _Callable[[_Pointer[IHttpCookiePairHeaderValueCollection]],  # value
                          _type.HRESULT]
    get_Date: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                        _type.HRESULT]
    put_Date: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                        _type.HRESULT]
    get_Expect: _Callable[[_Pointer[IHttpExpectationHeaderValueCollection]],  # value
                          _type.HRESULT]
    get_From: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_From: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_Host: _Callable[[_Pointer[_Windows_Networking.IHostName]],  # value
                        _type.HRESULT]
    put_Host: _Callable[[_Windows_Networking.IHostName],  # value
                        _type.HRESULT]
    get_IfModifiedSince: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                   _type.HRESULT]
    put_IfModifiedSince: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                                   _type.HRESULT]
    get_IfUnmodifiedSince: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                     _type.HRESULT]
    put_IfUnmodifiedSince: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                                     _type.HRESULT]
    get_MaxForwards: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                               _type.HRESULT]
    put_MaxForwards: _Callable[[_Windows_Foundation.IReference[_type.UINT32]],  # value
                               _type.HRESULT]
    get_ProxyAuthorization: _Callable[[_Pointer[IHttpCredentialsHeaderValue]],  # value
                                      _type.HRESULT]
    put_ProxyAuthorization: _Callable[[IHttpCredentialsHeaderValue],  # value
                                      _type.HRESULT]
    get_Referer: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                           _type.HRESULT]
    put_Referer: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                           _type.HRESULT]
    get_TransferEncoding: _Callable[[_Pointer[IHttpTransferCodingHeaderValueCollection]],  # value
                                    _type.HRESULT]
    get_UserAgent: _Callable[[_Pointer[IHttpProductInfoHeaderValueCollection]],  # value
                             _type.HRESULT]
    Append: _Callable[[_type.HSTRING,  # name
                       _type.HSTRING],  # value
                      _type.HRESULT]
    TryAppendWithoutValidation: _Callable[[_type.HSTRING,  # name
                                           _type.HSTRING,  # value
                                           _Pointer[_type.boolean]],  # result
                                          _type.HRESULT]


class IHttpResponseHeaderCollection(_inspectable.IInspectable):
    get_Age: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                       _type.HRESULT]
    put_Age: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]],  # value
                       _type.HRESULT]
    get_Allow: _Callable[[_Pointer[IHttpMethodHeaderValueCollection]],  # value
                         _type.HRESULT]
    get_CacheControl: _Callable[[_Pointer[IHttpCacheDirectiveHeaderValueCollection]],  # value
                                _type.HRESULT]
    get_Connection: _Callable[[_Pointer[IHttpConnectionOptionHeaderValueCollection]],  # value
                              _type.HRESULT]
    get_Date: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                        _type.HRESULT]
    put_Date: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                        _type.HRESULT]
    get_Location: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                            _type.HRESULT]
    put_Location: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                            _type.HRESULT]
    get_ProxyAuthenticate: _Callable[[_Pointer[IHttpChallengeHeaderValueCollection]],  # value
                                     _type.HRESULT]
    get_RetryAfter: _Callable[[_Pointer[IHttpDateOrDeltaHeaderValue]],  # value
                              _type.HRESULT]
    put_RetryAfter: _Callable[[IHttpDateOrDeltaHeaderValue],  # value
                              _type.HRESULT]
    get_TransferEncoding: _Callable[[_Pointer[IHttpTransferCodingHeaderValueCollection]],  # value
                                    _type.HRESULT]
    get_WwwAuthenticate: _Callable[[_Pointer[IHttpChallengeHeaderValueCollection]],  # value
                                   _type.HRESULT]
    Append: _Callable[[_type.HSTRING,  # name
                       _type.HSTRING],  # value
                      _type.HRESULT]
    TryAppendWithoutValidation: _Callable[[_type.HSTRING,  # name
                                           _type.HSTRING,  # value
                                           _Pointer[_type.boolean]],  # result
                                          _type.HRESULT]


class IHttpTransferCodingHeaderValue(_inspectable.IInspectable):
    get_Parameters: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IHttpNameValueHeaderValue]]],  # value
                              _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]


class IHttpTransferCodingHeaderValueCollection(_inspectable.IInspectable):
    ParseAdd: _Callable[[_type.HSTRING],  # input
                        _type.HRESULT]
    TryParseAdd: _Callable[[_type.HSTRING,  # input
                            _Pointer[_type.boolean]],  # result
                           _type.HRESULT]


class IHttpTransferCodingHeaderValueFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.HSTRING,  # input
                       _Pointer[IHttpTransferCodingHeaderValue]],  # value
                      _type.HRESULT]


class IHttpTransferCodingHeaderValueStatics(_inspectable.IInspectable, factory=True):
    Parse: _Callable[[_type.HSTRING,  # input
                      _Pointer[IHttpTransferCodingHeaderValue]],  # result
                     _type.HRESULT]
    TryParse: _Callable[[_type.HSTRING,  # input
                         _Pointer[IHttpTransferCodingHeaderValue],  # transferCodingHeaderValue
                         _Pointer[_type.boolean]],  # succeeded
                        _type.HRESULT]
