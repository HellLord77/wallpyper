from __future__ import annotations as _

__version__ = '0.2.1'

import base64
import calendar
import contextlib
import dataclasses
import datetime
import functools
import http.client
import http.cookiejar
import http.cookies
import io
import json as json_
import os
import re
import ssl
import sys
import time
import typing
import urllib.error
import urllib.parse
import urllib.request
import urllib.response
import uuid
from typing import Any, AnyStr, BinaryIO, Callable, IO, Iterator, Iterable, Literal, Mapping, Optional

CONTENT_CHUNK_SIZE = 10 * 1024


class Header:
    # Authentication
    WWW_AUTHENTICATE = 'WWW-Authenticate'
    AUTHORIZATION = 'Authorization'
    PROXY_AUTHENTICATE = 'Proxy-Authenticate'
    PROXY_AUTHORIZATION = 'Proxy-Authorization'
    # Caching
    AGE = 'Age'
    CACHE_CONTROL = 'Cache-Control'
    CLEAR_SITE_DATA = 'Clear-Site-Data'
    EXPIRES = 'Expires'
    PRAGMA = 'Pragma'
    WARNING = 'Warning'
    # Client hints
    ACCEPT_CH = 'Accept-CH'
    ACCEPT_CH_LIFETIME = 'Accept-CH-Lifetime'
    CRITICAL_CH = 'Critical-CH'
    # User agent client hints
    SEC_CH_PREFERS_REDUCED_MOTION = 'Sec-CH-Prefers-Reduced-Motion'
    SEC_CH_UA = 'Sec-CH-UA'
    SEC_CH_UA_ARCH = 'Sec-CH-UA-Arch'
    SEC_CH_UA_BITNESS = 'Sec-CH-UA-Bitness'
    SEC_CH_UA_FULL_VERSION = 'Sec-CH-UA-Full-Version'
    SEC_CH_UA_MOBILE = 'Sec-CH-UA-Mobile'
    SEC_CH_UA_MODEL = 'Sec-CH-UA-Model'
    SEC_CH_UA_PLATFORM = 'Sec-CH-UA-Platform'
    SEC_CH_UA_PLATFORM_VERSION = 'Sec-CH-UA-Platform-Version'
    # Device client hints
    CONTENT_DPR = 'Content-DPR'
    DEVICE_MEMORY = 'Device-Memory'
    DPR = 'DPR'
    VIEWPORT_WIDTH = 'Viewport-Width'
    WIDTH = 'Width'
    # Network client hints
    DOWNLINK = 'Downlink'
    ECT = 'ECT'
    RTT = 'RTT'
    SAVE_DATA = 'Save-Data'
    # Conditionals
    LAST_MODIFIED = 'Last-Modified'
    ETAG = 'ETag'
    IF_MATCH = 'If-Match'
    IF_NONE_MATCH = 'If-None-Match'
    IF_MODIFIED_SINCE = 'If-Modified-Since'
    IF_UNMODIFIED_SINCE = 'If-Unmodified-Since'
    VARY = 'Vary'
    # Connection management
    CONNECTION = 'Connection'
    KEEP_ALIVE = 'Keep-Alive'
    # Content negotiation
    ACCEPT = 'Accept'
    ACCEPT_ENCODING = 'Accept-Encoding'
    ACCEPT_LANGUAGE = 'Accept-Language'
    # Controls
    EXCEPT = 'Except'
    MAX_FORWARDS = 'Max-Forwards'
    # Cookie
    COOKIE = 'Cookie'
    SET_COOKIE = 'Set-Cookie'
    # CORS
    ACCESS_CONTROL_ALLOW_ORIGIN = 'Access-Control-Allow-Origin'
    ACCESS_CONTROL_ALLOW_CREDENTIALS = 'Access-Control-Allow-Credentials'
    ACCESS_CONTROL_ALLOW_HEADERS = 'Access-Control-Allow-Headers'
    ACCESS_CONTROL_ALLOW_METHODS = 'Access-Control-Allow-Methods'
    ACCESS_CONTROL_EXPOSE_METHODS = 'Access-Control-Expose-Methods'
    ACCESS_CONTROL_EXPOSE_HEADERS = 'Access-Control-Expose-Headers'
    ACCESS_CONTROL_MAX_AGE = 'Access-Control-Max-Age'
    ACCESS_CONTROL_REQUEST_HEADERS = 'Access-Control-Request-Headers'
    ACCESS_CONTROL_REQUEST_METHOD = 'Access-Control-Request-Method'
    ORIGIN = 'Origin'
    TIMING_ALLOW_ORIGIN = 'Timing-Allow-Origin'
    # Downloads
    CONTENT_DISPOSITION = 'Content-Disposition'
    # Message body information
    CONTENT_LENGTH = 'Content-Length'
    CONTENT_TYPE = 'Content-Type'
    CONTENT_ENCODING = 'Content-Encoding'
    CONTENT_LANGUAGE = 'Content-Language'
    CONTENT_LOCATION = 'Content-Location'
    # Proxies
    FORWARDED = 'Forwarded'
    X_FORWARDED_FOR = 'X-Forwarded-For'
    X_FORWARDED_HOST = 'X-Forwarded-Host'
    X_FORWARDED_PROTO = 'X-Forwarded-Proto'
    VIA = 'Via'
    # Redirects
    LOCATION = 'Location'
    REFRESH = 'Refresh'
    # Request context
    FROM = 'From'
    HOST = 'Host'
    REFERER = 'Referer'
    REFERER_POLICY = 'Referrer-Policy'
    USER_AGENT = 'User-Agent'
    # Response context
    ALLOW = 'Allow'
    SERVER = 'Server'
    # Range requests
    ACCEPT_RANGES = 'Accept-Ranges'
    RANGE = 'Range'
    IF_RANGE = 'If-Range'
    CONTENT_RANGE = 'Content-Range'
    # Security
    CROSS_ORIGIN_EMBEDER_POLICY = 'Cross-Origin-Embedder-Policy'
    CROSS_ORIGIN_OPENER_POLICY = 'Cross-Origin-Opener-Policy'
    CROSS_ORIGIN_RESOURCE_POLICY = 'Cross-Origin-Resource-Policy'
    CONTENT_SECURITY_POLICY = 'Content-Security-Policy'
    CONTENT_SECURITY_POLICY_REPORT_ONLY = 'Content-Security-Policy-Report-Only'
    EXPECT_CT = 'Expect-CT'
    ORIGIN_LOCATION = 'Origin-Location'
    PERMISSION_POLICY = 'Permission-Policy'
    STRICT_TRANSPORT_SECURITY = 'Strict-Transport-Security'
    UPGRADE_INSECURE_REQUESTS = 'Upgrade-Insecure-Requests'
    X_CONTENT_TYPE_OPTIONS = 'X-Content-Type-Options'
    X_FRAME_OPTIONS = 'X-Frame-Options'
    X_PERMITTED_CROSS_DOMAIN_POLICIES = 'X-Permitted-Cross-Domain-Policies'
    X_POWERED_BY = 'X-Powered-By'
    X_XSS_PROTECTION = 'X-XSS-Protection'
    # Fetch metadata request headers
    SET_FETCH_SITE = 'Sec-Fetch-Site'
    SET_FETCH_MODE = 'Sec-Fetch-Mode'
    SET_FETCH_USER = 'Sec-Fetch-User'
    SET_FETCH_DEST = 'Sec-Fetch-Dest'
    SERVICE_WORKER_NAVIGATION_PRELOAD = 'Service-Worker-Navigation-Preload'
    # Server-sent events
    LAST_EVENT_ID = 'Last-Event-ID'
    NEL = 'NEL'
    PING_FROM = 'Ping-From'
    PING_TO = 'Ping-To'
    REPORT_TO = 'Report-To'
    # Transfer coding
    TRANSFER_ENCODING = 'Transfer-Encoding'
    TE = 'TE'
    TRAILER = 'Trailer'
    # WebSockets
    SEC_WEBSOCKET_KEY = 'Sec-WebSocket-Key'
    SET_WEBSOCKET_EXTENSIONS = 'Sec-WebSocket-Extensions'
    SET_WEBSOCKET_ACCEPT = 'Sec-WebSocket-Accept'
    SET_WEBSOCKET_PROTOCOL = 'Sec-WebSocket-Protocol'
    SET_WEBSOCKET_VERSION = 'Sec-WebSocket-Version'
    # Other
    ACCEPT_PUSH_POLICY = 'Accept-Push-Policy'
    ACCEPT_SIGNATURE = 'Accept-Signature'
    ALT_SVC = 'Alt-Svc'
    DATE = 'Date'
    EARLY_DATA = 'Early-Data'
    LARGE_ALLOCATION = 'Large-Allocation'
    LINK = 'Link'
    PUSH_POLICY = 'Push-Policy'
    RETRY_AFTER = 'Retry-After'
    SIGNATURE = 'Signature'
    SIGNED_HEADERS = 'Signed-Headers'
    SERVER_TIMING = 'Server-Timing'
    SERVICE_WORKER_ALLOWED = 'Service-Worker-Allowed'
    SOURCEMAP = 'SourceMap'
    UPGRADE = 'Upgrade'
    X_DNS_PREFETCH_CONTROL = 'X-DNS-Prefetch-Control'
    X_FIREFOX_SPDY = 'X-Firefox-Spdy'
    X_PINGBACK = 'X-Pingback'
    X_REQUESTED_WITH = 'X-Requested-With'
    X_ROBOTS_TAG = 'X-Robots-Tag'


_TMethod = str | http.HTTPMethod
_TParams = tuple[AnyStr, Optional[AnyStr | Iterable[
    AnyStr]]] | Mapping[AnyStr, Optional[AnyStr | Iterable[AnyStr]]]
_TData = Mapping[AnyStr, Optional[AnyStr | Iterable[AnyStr]]]
_THeaders = AnyStr | Iterable[tuple[str, Optional[
    str]]] | Mapping[str, Optional[str]] | io.BufferedIOBase
_TCookie = tuple[str, str] | http.cookies.Morsel | http.cookiejar.Cookie | http.cookiejar.CookieJar
_TCookies = Iterable[_TCookie] | Mapping[
    str | http.cookies.Morsel, Optional[str]] | http.cookiejar.CookieJar
_TFiles = Mapping[str, AnyStr | BinaryIO | tuple[
    AnyStr | BinaryIO] | tuple[AnyStr | BinaryIO, AnyStr] | tuple[
                      AnyStr | BinaryIO, AnyStr, Mapping[str, Optional[str]]]]
_TAuth = str | tuple[str, str]
_TJSON = bool | int | float | str | tuple | list | dict
_TProxies = str | Iterable[tuple[str, str]] | Mapping[str, Optional[str]]
_TVerify = bool | AnyStr | tuple[Optional[AnyStr], Optional[AnyStr]] | tuple[
    Optional[AnyStr], Optional[AnyStr], Optional[bytes]] | ssl.SSLContext

_UNK_SIZE = -1
_MIN_CHUNK = 32 * 1024
_BYTES_PATH = b"!$&'()*+,;=:@/"
_BYTES_QUERY = _BYTES_PATH + b'?'
_BYTES_FRAGMENT = _BYTES_QUERY
_FILE_SCHEME = 'file'
_STATUS_CODES_REDIRECT = (
    http.HTTPStatus.MOVED_PERMANENTLY, http.HTTPStatus.FOUND, http.HTTPStatus.SEE_OTHER,
    http.HTTPStatus.TEMPORARY_REDIRECT, http.HTTPStatus.PERMANENT_REDIRECT)
_RE_ENCODED = re.compile(r'%[a-fA-F0-9]{2}')


def default_user_agent(name: str = __name__) -> str:
    return f'{name}/{__version__}'


def default_headers() -> dict[str, str]:
    return {
        Header.USER_AGENT: default_user_agent(),
        Header.ACCEPT: '*/*',
        Header.CONNECTION: 'keep-alive'}


class _HTTPErrorProcessor(urllib.request.HTTPErrorProcessor):
    # noinspection PyShadowingNames
    def http_response(self, request: urllib.request.Request,
                      response: http.client.HTTPResponse) -> Any:
        response_ = super().http_response(request, response)
        if response is not response_:
            try:
                histories = response_.history
            except AttributeError:
                histories = response_.history = []
            for index, history in enumerate(reversed(histories)):
                history.history = histories[index:]
            histories.insert(0, Response(request, response))
        return response_

    https_response = http_response


class _HTTPRedirectHandler(urllib.request.HTTPRedirectHandler):
    # noinspection PyShadowingNames
    def redirect_request(self, request: urllib.request.Request, fp: IO[bytes],
                         code: int, msg: str, headers: http.client.HTTPMessage,
                         newurl: str) -> Optional[urllib.request.Request]:
        request_ = request.next = super().redirect_request(request, fp, code, msg, headers, newurl)
        request_.cookies = getattr(request, 'cookies', None)
        request_.proxies = getattr(request, 'proxies', None)
        allow_redirects = request_.allow_redirects = getattr(request, 'allow_redirects', True)
        if allow_redirects:
            return request_


class _ProxyHandler(urllib.request.ProxyHandler):
    def __init__(self):
        super().__init__({})

    # noinspection PyShadowingNames
    def default_open(self, request: urllib.request.Request) -> Optional[urllib.request.Request]:
        if (proxies := getattr(request, 'proxies', None)) is not None:
            if (proxy := proxies.get(request.type)) is not None:
                return self.proxy_open(request, proxy, request.type)


class _HTTPCookieProcessor(urllib.request.HTTPCookieProcessor):
    # noinspection PyShadowingNames
    def http_request(self, request: urllib.request.Request) -> urllib.request.Request:
        if (cookies := getattr(request, 'cookies', None)) is not None:
            cookies.add_cookie_header(request)
        return request

    # noinspection PyShadowingNames
    def http_response(self, request: urllib.request.Request,
                      response: http.client.HTTPResponse) -> http.client.HTTPResponse:
        if self.cookiejar is not None:
            return super().http_response(request, response)
        return response

    https_request = http_request
    https_response = http_response


class _HTTPHandler(urllib.request.HTTPHandler):
    # noinspection PyShadowingNames
    def http_open(self, request: urllib.request.Request) -> http.client.HTTPResponse:
        start = time.perf_counter()
        response = super().http_open(request)
        response.elapsed = time.perf_counter() - start
        return response


class _HTTPSHandler(urllib.request.HTTPSHandler):
    # noinspection PyShadowingNames
    def https_open(self, request: urllib.request.Request) -> http.client.HTTPResponse:
        start = time.perf_counter()
        response = self.do_open(http.client.HTTPSConnection, request,
                                context=getattr(request, 'verify', None))
        response.elapsed = datetime.timedelta(
            seconds=time.perf_counter() - start)
        return response


@dataclasses.dataclass
class Request:
    method: Optional[_TMethod] = None
    url: Optional[AnyStr] = None
    headers: Optional[_THeaders] = None
    files: Optional[_TFiles] = None
    data: Optional[_TData] = None
    params: Optional[_TParams] = None
    auth: Optional[_TAuth] = None
    cookies: Optional[_TCookies] = None
    json: Optional[_TJSON] = None
    unredirected_hdrs: Optional[_THeaders] = None

    def __post_init__(self):
        self._request = urllib.request.Request(self.url)

    def prepare(self) -> urllib.request.Request:
        self.prepare_method(self.method)
        self.prepare_url(self.url, self.params)
        self.prepare_headers(self.headers, self.unredirected_hdrs)
        self.prepare_cookies(self.cookies)
        self.prepare_body(self.data, self.files, self.json)
        self.prepare_auth(self.auth)
        return self._request

    def prepare_method(self, method: Optional[_TMethod] = None):
        encode_method(method, self._request)

    def prepare_url(self, url: Optional[AnyStr] = None, params: Optional[_TParams] = None):
        if url is None:
            url = self.url
        encode_params(url, params, self._request)

    def prepare_headers(self, headers: Optional[_THeaders] = None,
                        unredirected_hdrs: Optional[_THeaders] = None):
        if headers is not None:
            encode_headers(headers, request=self._request)
        if unredirected_hdrs is not None:
            encode_headers(unredirected_hdrs, True, self._request)

    def prepare_body(self, data: Optional[_TData] = None,
                     files: Optional[_TFiles] = None, json: Optional[_TJSON] = None):
        if data is not None or files is not None or json is not None:
            encode_body(data, files, json, self._request)

    def prepare_auth(self, auth: Optional[_TAuth] = None):
        if auth is None and any(auth_ := get_auth(self.url)):
            auth = auth_
        if auth is not None:
            encode_auth(auth, self._request)

    def prepare_cookies(self, cookies: Optional[_TCookies] = None):
        if cookies is not None:
            encode_cookies(cookies, self._request)


class Response:
    status_code: http.HTTPStatus
    headers: http.client.HTTPMessage
    url: str
    raw: urllib.response.addinfourl | http.client.HTTPResponse | urllib.error.URLError
    encoding: Optional[str]
    history: list[Response]
    reason: str
    cookies: http.cookiejar.CookieJar
    elapsed: datetime.timedelta
    request: urllib.request.Request

    # noinspection PyShadowingNames
    def __init__(self, request: urllib.request.Request,
                 raw: urllib.response.addinfourl | http.client.HTTPResponse | urllib.error.URLError):
        self._next = getattr(request, 'next', None)
        if isinstance(raw, urllib.error.URLError):
            self.status_code = http.HTTPStatus(getattr(
                raw, 'status', http.HTTPStatus.IM_A_TEAPOT))
        elif isinstance(raw, urllib.response.addinfourl):
            # noinspection PyTypeChecker
            self.status_code = http.HTTPStatus.OK
        else:
            self.status_code = http.HTTPStatus(raw.status)
        self.headers = getattr(raw, 'headers', http.client.HTTPMessage())
        self.raw = raw
        self.url = getattr(raw, 'url', '')
        self.encoding = None
        self.history = getattr(raw, 'history', [])
        self.reason = getattr(raw, 'reason', '')
        self.cookies = http.cookiejar.CookieJar()
        if isinstance(raw, http.client.HTTPResponse):
            self.cookies.extract_cookies(raw, request)
        self.elapsed = getattr(raw, 'elapsed', datetime.timedelta())
        self.request = request

    def __bool__(self) -> bool:
        return self.status_code is http.HTTPStatus.OK

    def __repr__(self) -> str:
        return f'<{type(self).__name__}: {self.status_code!r}>'

    def __iter__(self) -> Iterator[bytes]:
        return self.iter_content(128)

    def __enter__(self) -> Response:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def ok(self) -> bool:
        return not 400 <= self.status_code < 600

    @property
    def is_redirect(self) -> bool:
        return Header.LOCATION in self.headers and self.status_code in _STATUS_CODES_REDIRECT

    @property
    def is_permanent_redirect(self) -> bool:
        return Header.LOCATION in self.headers and self.status_code in (
            http.HTTPStatus.MOVED_PERMANENTLY, http.HTTPStatus.PERMANENT_REDIRECT)

    @property
    def next(self) -> Optional[urllib.request.Request]:
        if self.is_redirect:
            return self._next

    @property
    def apparent_encoding(self) -> str:
        return 'utf-8'

    def iter_content(self, chunk_size: int = 1) -> Iterator[bytes]:
        while chunk := self.raw.read(chunk_size):
            yield chunk

    @functools.cached_property
    def content(self) -> bytes:
        return b''.join(self.iter_content(CONTENT_CHUNK_SIZE))

    @property
    def text(self) -> str:
        try:
            return self.content.decode(
                self.encoding or self.apparent_encoding, 'replace')
        except LookupError:
            return self.content.decode(errors='replace')

    def json(self) -> Any:
        with contextlib.suppress(json_.decoder.JSONDecodeError):
            return json_.loads(self.text)

    @property
    def links(self):
        links = {}
        if Header.LINK in self.headers:
            for url, params in get_links(self.headers[Header.LINK]).items():
                links[params.get('rel', url)] = {'url': url, **params}
        return links

    def close(self):
        self.raw.close()


class Session:
    __attrs__ = ('headers', 'auth', 'proxies', 'params', 'stream', 'verify', 'trust_env', 'cookies',
                 'timeout', 'allow_redirects', 'max_repeats', 'max_redirections', 'unredirected_hdrs')
    _error_processor = _HTTPErrorProcessor()
    _proxy_handler = _ProxyHandler()
    _http_handler = _HTTPHandler()
    _https_handler = _HTTPSHandler()

    def __init__(self, headers: Optional[_THeaders] = None, auth: Optional[_TAuth] = None,
                 proxies: Optional[_TProxies] = None, params: Optional[_TParams] = None,
                 stream: Optional[bool] = None, verify: Optional[_TVerify] = None, trust_env: bool = True,
                 cookies: Optional[_TCookies] = None, timeout: Optional[float] = None,
                 allow_redirects: Optional[bool] = None, max_repeats: Optional[int] = None,
                 max_redirections: Optional[int] = None, unredirected_hdrs: Optional[_THeaders] = None):
        self._redirect_handler = _HTTPRedirectHandler()
        self._cookie_processor = _HTTPCookieProcessor()
        if headers is None:
            headers = default_headers()
        self.headers = headers
        self.auth = auth
        self.proxies = proxies
        self.params = params
        self.stream = stream
        self.verify = verify
        self.trust_env = trust_env  # TODO extend
        if cookies is None:
            cookies = http.cookiejar.CookieJar()
        self.cookies = cookies
        self.timeout = timeout
        self.allow_redirects = allow_redirects
        self.max_redirections = max_redirections
        self.max_repeats = max_repeats
        self.unredirected_hdrs = unredirected_hdrs
        self._opener = urllib.request.build_opener(
            self._error_processor, self._redirect_handler, self._proxy_handler,
            self._cookie_processor, self._http_handler, self._https_handler)

    def __repr__(self):
        attrs = (f'{name}={val}' for name in self.__attrs__
                 if (val := getattr(self, name)) is not None)
        return f'<{type(self).__name__}: <{", ".join(attrs)}>>'

    @property
    def headers(self) -> Optional[dict[str, str]]:
        return self._headers

    @headers.setter
    def headers(self, headers: Optional[_THeaders]):
        if headers is not None:
            headers = encode_headers(headers)
        self._headers = encode_headers(headers)

    @property
    def proxies(self) -> Optional[dict[str, str]]:
        return self._proxies

    @proxies.setter
    def proxies(self, proxies: Optional[_TProxies]):
        if proxies is not None:
            proxies = encode_proxies(proxies)
        self._proxies = proxies

    @property
    def params(self) -> Optional[dict[str, list[str]]]:
        return self._params

    @params.setter
    def params(self, params: Optional[_TParams]):
        if params is not None:
            params = get_params(params)
        self._params = params

    @property
    def verify(self) -> Optional[ssl.SSLContext]:
        return self._verify

    @verify.setter
    def verify(self, verify: Optional[_TVerify]):
        if verify is not None:
            verify = encode_verify(verify)
        self._verify = verify

    @property
    def cookies(self) -> Optional[http.cookiejar.CookieJar]:
        return self._cookie_processor.cookiejar

    @cookies.setter
    def cookies(self, cookies: Optional[_TCookies]):
        if cookies is not None:
            cookies = encode_cookies(cookies)
        self._cookie_processor.cookiejar = cookies

    @property
    def max_repeats(self) -> int:
        return self._redirect_handler.max_repeats

    @max_repeats.setter
    def max_repeats(self, max_repeats: Optional[int]):
        if max_repeats is None:
            try:
                del self._redirect_handler.max_repeats
            except AttributeError:
                pass
        else:
            # noinspection PyClassVar
            self._redirect_handler.max_repeats = max_repeats

    @property
    def max_redirections(self) -> int:
        return self._redirect_handler.max_redirections

    @max_redirections.setter
    def max_redirections(self, max_redirections: Optional[int]):
        if max_redirections is None:
            try:
                del self._redirect_handler.max_redirections
            except AttributeError:
                pass
        else:
            # noinspection PyClassVar
            self._redirect_handler.max_redirections = max_redirections

    @property
    def unredirected_hdrs(self) -> Optional[dict[str, str]]:
        return self._unredirected_hdrs

    @unredirected_hdrs.setter
    def unredirected_hdrs(self, unredirected_hdrs: Optional[_THeaders]):
        if unredirected_hdrs is not None:
            unredirected_hdrs = encode_headers(unredirected_hdrs)
        self._unredirected_hdrs = unredirected_hdrs

    # noinspection PyShadowingNames
    def prepare_request(self, request: Request) -> urllib.request.Request:
        headers = request.headers
        if headers is not None:
            headers = encode_headers(headers)
        request.headers = _merge_setting(headers, self.headers)
        request.auth = _merge_setting(request.auth, self.auth)
        params = request.params
        if params is not None:
            params = get_params(params)
        request.params = _merge_setting(params, self.params)
        cookies = []
        if self.cookies is not None:
            cookies.append(self.cookies)
        if request.cookies is not None:
            cookies.append(encode_cookies(request.cookies))
        request.cookies = merge_cookies(*cookies) if cookies else None
        unredirected_hdrs = request.unredirected_hdrs
        if unredirected_hdrs is not None:
            unredirected_hdrs = encode_headers(unredirected_hdrs)
        request.unredirected_hdrs = _merge_setting(unredirected_hdrs, self.unredirected_hdrs)
        return request.prepare()

    def request(self, method: Optional[_TMethod], url: AnyStr,
                params: Optional[_TParams] = None, data: Optional[_TData] = None, headers: Optional[_THeaders] = None,
                cookies: Optional[_TCookies] = None, files: Optional[_TFiles] = None, auth: Optional[_TAuth] = None,
                timeout: Optional[float] = None, allow_redirects: Optional[bool] = None, proxies: Optional[_TProxies] = None,
                stream: Optional[bool] = None, verify: Optional[_TVerify] = None, json: Optional[_TJSON] = None,
                unredirected_hdrs: Optional[_THeaders] = None) -> Response:
        request_ = self.prepare_request(Request(method, url, headers, files, data, params,
                                                auth, cookies, json, unredirected_hdrs))
        return self.send(request_, **self.merge_environment_settings(
            proxies, stream, verify, timeout, allow_redirects))

    def get(self, url: AnyStr, params: Optional[_TParams] = None, data: Optional[_TData] = None,
            headers: Optional[_THeaders] = None, cookies: Optional[_TCookies] = None, files: Optional[_TFiles] = None,
            auth: Optional[_TAuth] = None, timeout: Optional[float] = None, allow_redirects: Optional[bool] = None,
            proxies: Optional[_TProxies] = None, stream: Optional[bool] = None, verify: Optional[_TVerify] = None,
            json: Optional[_TJSON] = None, unredirected_hdrs: Optional[_THeaders] = None) -> Response:
        return self.request(http.HTTPMethod.GET, url, params, data, headers, cookies, files,
                            auth, timeout, allow_redirects, proxies, stream, verify, json, unredirected_hdrs)

    def options(self, url: AnyStr, params: Optional[_TParams] = None, data: Optional[_TData] = None,
                headers: Optional[_THeaders] = None, cookies: Optional[_TCookies] = None, files: Optional[_TFiles] = None,
                auth: Optional[_TAuth] = None, timeout: Optional[float] = None, allow_redirects: Optional[bool] = None,
                proxies: Optional[_TProxies] = None, stream: Optional[bool] = None, verify: Optional[_TVerify] = None,
                json: Optional[_TJSON] = None, unredirected_hdrs: Optional[_THeaders] = None) -> Response:
        return self.request(http.HTTPMethod.OPTIONS, url, params, data, headers, cookies, files,
                            auth, timeout, allow_redirects, proxies, stream, verify, json, unredirected_hdrs)

    def head(self, url: AnyStr, params: Optional[_TParams] = None, data: Optional[_TData] = None,
             headers: Optional[_THeaders] = None, cookies: Optional[_TCookies] = None, files: Optional[_TFiles] = None,
             auth: Optional[_TAuth] = None, timeout: Optional[float] = None, allow_redirects: Optional[bool] = None,
             proxies: Optional[_TProxies] = None, stream: Optional[bool] = None, verify: Optional[_TVerify] = None,
             json: Optional[_TJSON] = None, unredirected_hdrs: Optional[_THeaders] = None) -> Response:
        return self.request(http.HTTPMethod.HEAD, url, params, data, headers, cookies, files,
                            auth, timeout, allow_redirects, proxies, stream, verify, json, unredirected_hdrs)

    def post(self, url: AnyStr, params: Optional[_TParams] = None, data: Optional[_TData] = None,
             headers: Optional[_THeaders] = None, cookies: Optional[_TCookies] = None, files: Optional[_TFiles] = None,
             auth: Optional[_TAuth] = None, timeout: Optional[float] = None, allow_redirects: Optional[bool] = None,
             proxies: Optional[_TProxies] = None, stream: Optional[bool] = None, verify: Optional[_TVerify] = None,
             json: Optional[_TJSON] = None, unredirected_hdrs: Optional[_THeaders] = None) -> Response:
        return self.request(http.HTTPMethod.POST, url, params, data, headers, cookies, files,
                            auth, timeout, allow_redirects, proxies, stream, verify, json, unredirected_hdrs)

    def put(self, url: AnyStr, params: Optional[_TParams] = None, data: Optional[_TData] = None,
            headers: Optional[_THeaders] = None, cookies: Optional[_TCookies] = None, files: Optional[_TFiles] = None,
            auth: Optional[_TAuth] = None, timeout: Optional[float] = None, allow_redirects: Optional[bool] = None,
            proxies: Optional[_TProxies] = None, stream: Optional[bool] = None, verify: Optional[_TVerify] = None,
            json: Optional[_TJSON] = None, unredirected_hdrs: Optional[_THeaders] = None) -> Response:
        return self.request(http.HTTPMethod.PUT, url, params, data, headers, cookies, files,
                            auth, timeout, allow_redirects, proxies, stream, verify, json, unredirected_hdrs)

    def patch(self, url: AnyStr, params: Optional[_TParams] = None, data: Optional[_TData] = None,
              headers: Optional[_THeaders] = None, cookies: Optional[_TCookies] = None, files: Optional[_TFiles] = None,
              auth: Optional[_TAuth] = None, timeout: Optional[float] = None, allow_redirects: Optional[bool] = None,
              proxies: Optional[_TProxies] = None, stream: Optional[bool] = None, verify: Optional[_TVerify] = None,
              json: Optional[_TJSON] = None, unredirected_hdrs: Optional[_THeaders] = None) -> Response:
        return self.request(http.HTTPMethod.PATCH, url, params, data, headers, cookies, files,
                            auth, timeout, allow_redirects, proxies, stream, verify, json, unredirected_hdrs)

    def delete(self, url: AnyStr, params: Optional[_TParams] = None, data: Optional[_TData] = None,
               headers: Optional[_THeaders] = None, cookies: Optional[_TCookies] = None, files: Optional[_TFiles] = None,
               auth: Optional[_TAuth] = None, timeout: Optional[float] = None, allow_redirects: Optional[bool] = None,
               proxies: Optional[_TProxies] = None, stream: Optional[bool] = None, verify: Optional[_TVerify] = None,
               json: Optional[_TJSON] = None, unredirected_hdrs: Optional[_THeaders] = None) -> Response:
        return self.request(http.HTTPMethod.DELETE, url, params, data, headers, cookies, files,
                            auth, timeout, allow_redirects, proxies, stream, verify, json, unredirected_hdrs)

    # noinspection PyShadowingNames
    def send(self, request: urllib.request.Request, proxies: Optional[_TProxies] = None, stream: Optional[bool] = None,
             verify: Optional[_TVerify] = None, timeout: Optional[float] = None, allow_redirects: Optional[bool] = None) -> Response:
        if proxies is not None:
            request.proxies = proxies
        if stream is None:
            stream = False
        if verify is not None:
            request.verify = encode_verify(verify)
        if timeout is not None:
            request.timeout = timeout
        if allow_redirects is not None:
            request.allow_redirects = allow_redirects
        try:
            response = self._opener.open(request)
        except urllib.error.URLError as exc:  # TODO better handling
            response_ = Response(request, exc)
        else:
            response_ = Response(request, response)
            if not stream:
                _ = response_.content
        return response_

    def merge_environment_settings(self, proxies: Optional[_TProxies] = None, stream: Optional[bool] = None,
                                   verify: Optional[_TVerify] = None, timeout: Optional[float] = None,
                                   allow_redirects: Optional[bool] = None) -> dict[str, Any]:
        if proxies is not None:
            proxies = encode_proxies(proxies)
        if self.trust_env:
            proxies = _merge_setting(proxies, urllib.request.getproxies())
        return {
            'proxies': _merge_setting(proxies, self.proxies),
            'stream': _merge_setting(stream, self.stream),
            'verify': _merge_setting(verify, self.verify),
            'timeout': _merge_setting(timeout, self.timeout),
            'allow_redirects': _merge_setting(allow_redirects, self.allow_redirects)}


def _str(o: AnyStr) -> str:
    return o.decode() if isinstance(o, bytes) else o


def _merge_setting(request_setting, session_setting) -> Any:
    if session_setting is None:
        return request_setting
    elif request_setting is None:
        return session_setting
    elif isinstance(session_setting, Mapping):
        return {**session_setting, **request_setting}
    else:
        return request_setting


def is_path(url: AnyStr) -> bool:
    return _FILE_SCHEME == _str(urllib.parse.urlsplit(url).scheme)


def from_path(path: str) -> str:
    # noinspection PyArgumentList
    return urllib.parse.SplitResult(_FILE_SCHEME, '', urllib.request.pathname2url(path), '', '').geturl()


def strip(url: AnyStr, query: bool = True, fragment: bool = True) -> AnyStr:
    components = urllib.parse.urlsplit(url)
    # noinspection PyProtectedMember
    return components._replace(query='' if query else components.query,
                               fragment='' if fragment else components.fragment).geturl()


def join(base: str, *paths: str) -> str:
    if not base.endswith('/'):
        base += '/'
    for path in paths:
        if path:
            base = urllib.parse.urljoin(base, path) + '/'
    return base[:-1]


def extract_params(url: AnyStr) -> dict[AnyStr, list[AnyStr]]:
    return urllib.parse.parse_qs(urllib.parse.urlsplit(url).query)


@typing.overload
def get_params(params: _TParams, decode: Literal[True] = True,
               encode: Literal[False] = False) -> dict[str, list[str]]:
    pass


@typing.overload
def get_params(params: _TParams, decode: Literal[False] = True,
               encode: Literal[True] = False) -> dict[bytes, list[bytes]]:
    pass


@typing.overload
def get_params(params: _TParams, decode: Literal[False] = True,
               encode: Literal[False] = False) -> dict[AnyStr, list[AnyStr]]:
    pass


def get_params(params, decode=True, encode=False):
    assert not (decode and encode)
    query = {}
    for key, val in params.items() if isinstance(params, Mapping) else params:
        if val is not None:
            if key not in query:
                query[key] = []
            if isinstance(val, (bytes, str)):
                if decode and isinstance(val, bytes):
                    val = val.decode()
                elif encode and isinstance(val, str):
                    val = val.encode()
                query[key].append(val)
            else:
                query[key].extend(val)
    return query


def get_headers(keep_alive: bool = True, accept_encoding: str | Iterable[str] = ('gzip', 'deflate'),
                user_agent: Optional[str] = None, basic_auth: Optional[tuple[str, str]] = None,
                proxy_basic_auth: Optional[tuple[str, str]] = None, disable_cache: bool = False) -> dict[str, str]:
    if not isinstance(accept_encoding, str):
        accept_encoding = ', '.join(accept_encoding)
    if user_agent is None:
        user_agent = default_user_agent()
    headers = {
        Header.CONNECTION: 'keep-alive' if keep_alive else 'close',
        Header.ACCEPT_ENCODING: accept_encoding,
        Header.USER_AGENT: user_agent}
    if basic_auth is not None:
        headers[Header.AUTHORIZATION] = encode_auth(basic_auth)
    if proxy_basic_auth is not None:
        headers[Header.PROXY_AUTHORIZATION] = encode_auth(proxy_basic_auth)
    if disable_cache:
        headers[Header.CACHE_CONTROL] = 'no-cache'
    return headers


def get_auth(url: str) -> tuple[str, str]:
    # noinspection PyUnresolvedReferences,PyProtectedMember
    username, password = urllib.parse.urlsplit(url)._userinfo
    return ('' if username is None else urllib.parse.unquote(username),
            '' if password is None else urllib.parse.unquote(password))


@typing.overload
def get_cookie(morsel_or_name: http.cookies.Morsel) -> http.cookiejar.Cookie:
    pass


@typing.overload
def get_cookie(morsel_or_name: str, value: Optional[str] = None, version: int = 0, port: Optional[str] = None,
               domain: str = '', path: str = '/', secure: bool = False, expires: Optional[int] = None,
               discard: bool = True, comment: Optional[str] = None, comment_url: Optional[str] = None,
               rest: Optional[dict[str, str]] = None, rfc2109: bool = False) -> http.cookiejar.Cookie:
    pass


def get_cookie(morsel_or_name, value=None, version=0, port=None, domain='',
               path='/', secure=False, expires=None, discard=True, comment=None,
               comment_url=None, rest=None, rfc2109=False) -> http.cookiejar.Cookie:
    if isinstance(morsel_or_name, http.cookies.Morsel):
        morsel = morsel_or_name
        if morsel['max-age']:
            expires = int(time.time() + int(morsel['max-age']))
        elif morsel['expires']:
            expires = calendar.timegm(time.strptime(morsel['expires'], '%a, %d-%b-%Y %H:%M:%S GMT'))
        else:
            expires = None
        return get_cookie(morsel.key, morsel.value, morsel['version'], None, morsel['domain'], morsel['path'],
                          bool(morsel['secure']), expires, False, morsel['comment'], None, None, False)
    else:
        if rest is None:
            rest = {'HttpOnly': None}
        port_specified = bool(port)
        domain_specified = bool(domain)
        domain_initial_dot = domain.startswith('.')
        path_specified = bool(path)
        return http.cookiejar.Cookie(
            version, morsel_or_name, value, port, port_specified, domain, domain_specified, domain_initial_dot,
            path, path_specified, secure, expires, discard, comment, comment_url, rest, rfc2109)


def get_links(header: str) -> dict[str, dict[str, str]]:
    links = {}
    for link in header.split(','):
        url, *params = link.split(';')
        query = links[url.strip('<> \'"')] = {}
        for param in params:
            key, *value = param.split('=', 1)
            query[key.strip(' \'"')] = value[0].strip(' \'"') if value else ''
    return links


def merge_cookies(*cookies: _TCookie,
                  jar: Optional[http.cookiejar.CookieJar] = None) -> http.cookiejar.CookieJar:
    if jar is None:
        jar = http.cookiejar.CookieJar()
    for cookie in cookies:
        if isinstance(cookie, http.cookiejar.CookieJar):
            for cookie_ in cookie:
                jar.set_cookie(cookie_)
        else:
            if not isinstance(cookie, http.cookiejar.Cookie):
                cookie = get_cookie(*(cookie,) if isinstance(
                    cookie, http.cookies.Morsel) else cookie)
            jar.set_cookie(cookie)
    return jar


# noinspection PyShadowingNames
def encode_method(method: _TMethod, request: Optional[urllib.request.Request] = None) -> str:
    if isinstance(method, http.HTTPMethod):
        method = method.value
    method = method.upper()
    if request is not None:
        request.method = method
    return method


def _upper(match: re.Match) -> AnyStr:
    return match.group(0).upper()


def _encode_component(component: str, valid: AnyStr) -> str:
    component, count_encoded = _RE_ENCODED.subn(_upper, component)
    if count_encoded == component.count('%'):
        valid += b'%'
    return urllib.parse.quote_plus(component, safe=valid)


# noinspection PyShadowingNames
def encode_url(url: AnyStr, request: Optional[urllib.request.Request] = None) -> str:
    components = urllib.parse.urlsplit(_str(url))
    if components.scheme in ('', 'http', 'https'):
        components = components._replace(path=_encode_component(
            components.path, _BYTES_PATH), query=_encode_component(
            components.query, _BYTES_QUERY), fragment=_encode_component(
            components.fragment, _BYTES_FRAGMENT))
    full_url = components.geturl()
    if request is not None:
        request.full_url = full_url
    return full_url


# noinspection PyShadowingNames
def encode_params(url: AnyStr, params: Optional[_TParams] = None,
                  request: Optional[urllib.request.Request] = None) -> AnyStr:
    if params is not None:
        components = urllib.parse.urlsplit(url)
        query = urllib.parse.parse_qs(components.query, True)
        query.update(get_params(params, False))
        # noinspection PyProtectedMember
        url = components._replace(query=_encode_params(query)).geturl()
    return encode_url(url, request)


# noinspection PyShadowingNames
def encode_headers(headers: _THeaders, unredirected: bool = False,
                   request: Optional[urllib.request.Request] = None) -> dict[str, str]:
    if not isinstance(headers, Mapping):
        if isinstance(headers, (bytes, str)):
            headers = open(headers, 'rb')
        if isinstance(headers, io.BufferedIOBase):
            headers = http.client.parse_headers(headers)
        else:
            headers = dict(headers)
    headers = {key.capitalize(): val for key, val in headers.items() if val is not None}
    if request is not None:
        (request.unredirected_hdrs if unredirected else request.headers).update(headers)
    return headers


# noinspection PyShadowingNames
def encode_cookies(cookies: _TCookies,
                   request: Optional[urllib.request.Request] = None) -> http.cookiejar.CookieJar:
    if not isinstance(cookies, http.cookiejar.CookieJar):
        if isinstance(cookies, Mapping):
            cookies = cookies.items()
        cookies = merge_cookies(*cookies)
    if request is not None:
        request.cookies = cookies
    return cookies


def _encode_params(params: Optional[AnyStr | Mapping]) -> str:
    if params is None:
        return ''
    elif isinstance(params, (bytes, str)):
        return _str(params)
    else:
        return urllib.parse.urlencode(params, True)


# noinspection PyShadowingNames
def encode_body(data: Optional[_TData] = None, files: Optional[_TFiles] = None, json: Optional[_TJSON] = None,
                request: Optional[urllib.request.Request] = None) -> tuple[Optional[str], Optional[bytes]]:
    if files is not None:  # TODO escape quotes + iterable[bytes]/readable data
        body = []
        if data is not None:
            for name, vals in data.items():
                if vals is not None:
                    if isinstance(vals, (bytes, str)):
                        vals = vals,
                    body.extend(({Header.CONTENT_DISPOSITION: f'form-data; name="{_str(name)}"'},
                                 val.encode() if isinstance(val, str) else val) for val in vals)
        for name, vals in files.items():
            if isinstance(vals, (bytes, str)):
                vals = vals,
            headers = {
                Header.CONTENT_DISPOSITION: f'form-data; name="{_str(name)}"',
                Header.CONTENT_TYPE: None,
                Header.CONTENT_LOCATION: None}
            filename = None
            if len(vals) > 1:
                filename = vals[1]
                if len(vals) > 2:
                    headers.update(vals[2])
            val = vals[0]
            if filename is None:
                filename = os.path.basename(val if isinstance(val, (
                    bytes, str)) else val.name if hasattr(val, 'name') else name)
            headers[Header.CONTENT_DISPOSITION] += f'; filename="{_str(filename)}"'
            body.append((headers, (open(val, 'rb') if isinstance(
                val, (bytes, str)) else val).read()))
        lines = []
        boundary = uuid.uuid4().hex
        for headers, val in body:
            lines.append(f'--{boundary}'.encode())
            lines.extend(f'{key}: {val}'.encode()
                         for key, val in headers.items() if val is not None)
            lines.append(b'')
            lines.append(val)
        lines.append(f'--{boundary}--'.encode())
        lines.append(b'')
        mime = f'multipart/form-data; boundary={boundary}'
        data = '\r\n'.encode().join(lines)
    elif data is not None:
        mime = 'application/x-www-form-urlencoded'
        data = _encode_params(data).encode()
    elif json is not None:
        mime = 'application/json'
        data = json_.dumps(json, allow_nan=False).encode()
    else:
        mime = None
        data = None
    if request is not None:
        request.add_header(Header.CONTENT_TYPE, mime)
        request.data = data
    return mime, data


# noinspection PyShadowingNames
def encode_auth(auth: _TAuth, request: Optional[urllib.request.Request] = None) -> str:
    auth = (f'Bearer {auth}' if isinstance(auth, str) else
            f'Basic {base64.b64encode(":".join(auth).encode("latin1")).decode()}')
    if request is not None:
        request.add_header(Header.AUTHORIZATION, auth)
    return auth


def encode_proxies(proxies: _TProxies) -> dict[str, str]:
    if not isinstance(proxies, Mapping):
        proxies = {'http': proxies, 'https': proxies}
    elif not isinstance(proxies, dict):
        proxies = dict(proxies)
    return proxies


def encode_verify(verify: _TVerify) -> ssl.SSLContext:
    if not isinstance(verify, ssl.SSLContext):
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        context.set_alpn_protocols(('http/1.1',))
        cafile = capath = cadata = None
        if isinstance(verify, bool):
            context.check_hostname = verify
            context.verify_mode = ssl.CERT_REQUIRED if verify else ssl.CERT_NONE
        else:
            context.check_hostname = True
            context.verify_mode = ssl.CERT_REQUIRED
            if isinstance(verify, (bytes, str)):
                if os.path.isfile(verify):
                    cafile = verify
                else:
                    capath = verify
            else:
                cafile, capath, *cadata = verify
                cadata = cadata[0] if cadata else None
        if verify is not False:
            if cafile is None and capath is None and cadata is None:
                context.load_default_certs()
            else:
                context.load_verify_locations(cafile, capath, cadata)
        verify = context
    return verify


def request(method: Optional[_TMethod], url: AnyStr, params: Optional[_TParams] = None, data: Optional[_TData] = None,
            headers: Optional[_THeaders] = None, cookies: Optional[_TCookies] = None, files: Optional[_TFiles] = None,
            auth: Optional[_TAuth] = None, timeout: Optional[float] = None, allow_redirects: bool = True,
            proxies: Optional[_TProxies] = None, stream: bool = True, verify: _TVerify = True, json: Optional[_TJSON] = None,
            unredirected_hdrs: Optional[_THeaders] = None) -> Response:
    return Session().request(method, url, params, data, headers, cookies, files,
                             auth, timeout, allow_redirects, proxies, stream, verify, json, unredirected_hdrs)


def get(url: AnyStr, params: Optional[_TParams] = None, data: Optional[_TData] = None,
        headers: Optional[_THeaders] = None, cookies: Optional[_TCookies] = None, files: Optional[_TFiles] = None,
        auth: Optional[_TAuth] = None, timeout: Optional[float] = None, allow_redirects: bool = True,
        proxies: Optional[_TProxies] = None, stream: bool = True, verify: _TVerify = True, json: Optional[_TJSON] = None,
        unredirected_hdrs: Optional[_THeaders] = None) -> Response:
    return request(http.HTTPMethod.GET, url, params, data, headers, cookies, files,
                   auth, timeout, allow_redirects, proxies, stream, verify, json, unredirected_hdrs)


def options(url: AnyStr, params: Optional[_TParams] = None, data: Optional[_TData] = None,
            headers: Optional[_THeaders] = None, cookies: Optional[_TCookies] = None, files: Optional[_TFiles] = None,
            auth: Optional[_TAuth] = None, timeout: Optional[float] = None, allow_redirects: bool = False,
            proxies: Optional[_TProxies] = None, stream: bool = True, verify: _TVerify = True, json: Optional[_TJSON] = None,
            unredirected_hdrs: Optional[_THeaders] = None) -> Response:
    return request(http.HTTPMethod.OPTIONS, url, params, data, headers, cookies,
                   files, auth, timeout, allow_redirects, proxies, stream, verify, json, unredirected_hdrs)


def head(url: AnyStr, params: Optional[_TParams] = None, data: Optional[_TData] = None,
         headers: Optional[_THeaders] = None, cookies: Optional[_TCookies] = None, files: Optional[_TFiles] = None,
         auth: Optional[_TAuth] = None, timeout: Optional[float] = None, allow_redirects: bool = False,
         proxies: Optional[_TProxies] = None, stream: bool = True, verify: _TVerify = True, json: Optional[_TJSON] = None,
         unredirected_hdrs: Optional[_THeaders] = None) -> Response:
    return request(http.HTTPMethod.HEAD, url, params, data, headers, cookies, files,
                   auth, timeout, allow_redirects, proxies, stream, verify, json, unredirected_hdrs)


def post(url: AnyStr, data: Optional[_TData] = None, json: Optional[_TJSON] = None, params: Optional[_TParams] = None,
         headers: Optional[_THeaders] = None, cookies: Optional[_TCookies] = None, files: Optional[_TFiles] = None,
         auth: Optional[_TAuth] = None, timeout: Optional[float] = None, allow_redirects: bool = True,
         proxies: Optional[_TProxies] = None, stream: bool = True, verify: _TVerify = True,
         unredirected_hdrs: Optional[_THeaders] = None) -> Response:
    return request(http.HTTPMethod.POST, url, params, data, headers, cookies, files,
                   auth, timeout, allow_redirects, proxies, stream, verify, json, unredirected_hdrs)


def put(url: AnyStr, data: Optional[_TData] = None, params: Optional[_TParams] = None,
        headers: Optional[_THeaders] = None, cookies: Optional[_TCookies] = None, files: Optional[_TFiles] = None,
        auth: Optional[_TAuth] = None, timeout: Optional[float] = None, allow_redirects: bool = True,
        proxies: Optional[_TProxies] = None, stream: bool = True, verify: _TVerify = True, json: Optional[_TJSON] = None,
        unredirected_hdrs: Optional[_THeaders] = None) -> Response:
    return request(http.HTTPMethod.PUT, url, params, data, headers, cookies, files,
                   auth, timeout, allow_redirects, proxies, stream, verify, json, unredirected_hdrs)


def patch(url: AnyStr, data: Optional[_TData] = None, params: Optional[_TParams] = None,
          headers: Optional[_THeaders] = None, cookies: Optional[_TCookies] = None, files: Optional[_TFiles] = None,
          auth: Optional[_TAuth] = None, timeout: Optional[float] = None, allow_redirects: bool = True,
          proxies: Optional[_TProxies] = None, stream: bool = True, verify: _TVerify = True, json: Optional[_TJSON] = None,
          unredirected_hdrs: Optional[_THeaders] = None) -> Response:
    return request(http.HTTPMethod.PATCH, url, params, data, headers, cookies, files,
                   auth, timeout, allow_redirects, proxies, stream, verify, json, unredirected_hdrs)


def delete(url: AnyStr, params: Optional[_TParams] = None, data: Optional[_TData] = None,
           headers: Optional[_THeaders] = None, cookies: Optional[_TCookies] = None, files: Optional[_TFiles] = None,
           auth: Optional[_TAuth] = None, timeout: Optional[float] = None, allow_redirects: bool = True,
           proxies: Optional[_TProxies] = None, stream: bool = True, verify: _TVerify = True, json: Optional[_TJSON] = None,
           unredirected_hdrs: Optional[_THeaders] = None) -> Response:
    return request(http.HTTPMethod.DELETE, url, params, data, headers, cookies, files,
                   auth, timeout, allow_redirects, proxies, stream, verify, json, unredirected_hdrs)


def sizeof(url: AnyStr) -> int:
    return int(head(url).headers.get(Header.CONTENT_LENGTH, 0))


def retrieve(url: AnyStr, path: AnyStr, size: int = 0, chunk_size: Optional[int] = None,
             chunk_count: Optional[int] = None, query_callback: Optional[Callable[[float], bool]] = None) -> bool:
    response = get(url)
    if response:
        if not size:
            size = int(response.headers.get(Header.CONTENT_LENGTH, _UNK_SIZE))
        if chunk_size is None:
            chunk_size = size // (chunk_count or sys.maxsize)
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'wb') as file:
                ratio = 0.0
                for chunk in response.iter_content(max(chunk_size, _MIN_CHUNK)):
                    if size != _UNK_SIZE:
                        ratio += file.write(chunk) / size
                    if query_callback is not None and not query_callback(ratio):
                        return False
            retrieved = size == _UNK_SIZE or size == os.path.getsize(path)
        except OSError:
            retrieved = False
        if retrieved and query_callback is not None:
            query_callback(1.0)
        return retrieved
    return False
