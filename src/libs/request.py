from __future__ import annotations as _

__version__ = '0.1.7'

import base64
import calendar
import contextlib
import http.client
import http.cookiejar
import http.cookies
import io
import json as json_
import os
import re
import sys
import time
import typing
import urllib.error
import urllib.parse
import urllib.request
import urllib.response
import uuid
from typing import Any, AnyStr, BinaryIO, Callable, IO, Iterator, Iterable, Mapping, Optional, TypeVar

_TResult = TypeVar('_TResult', urllib.parse.DefragResult, urllib.parse.SplitResult, urllib.parse.ParseResult,
                   urllib.parse.ParseResultBytes, urllib.parse.SplitResultBytes, urllib.parse.DefragResultBytes)
_TMethod = str | http.HTTPMethod
_TParams = Mapping[AnyStr, Optional[AnyStr | Iterable[AnyStr]]]
_TData = Mapping[AnyStr, Optional[AnyStr | Iterable[AnyStr]]]
_THeaders = Mapping[str, str]
_TCookie = tuple[str, str] | http.cookies.Morsel | http.cookiejar.Cookie | http.cookiejar.CookieJar
_TCookies = Mapping[str, str] | http.cookiejar.CookieJar
_TFiles = Mapping[str, AnyStr | BinaryIO | tuple[
    AnyStr | BinaryIO] | tuple[AnyStr | BinaryIO, AnyStr] | tuple[
                      AnyStr | BinaryIO, AnyStr, Mapping[str, Optional[str]]]]
_TAuth = str | tuple[str, str]
_TJSON = bool | int | float | str | tuple | list | dict


class _HTTPRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req: urllib.request.Request, fp: IO[bytes],
                         code: int, msg: str, headers: http.client.HTTPMessage,
                         newurl: str) -> Optional[urllib.request.Request]:
        pass


_UNK_SIZE = -1
_MIN_CHUNK = 32 * 1024
_BYTES_PATH = b"!$&'()*+,;=:@/"
_BYTES_QUERY = _BYTES_PATH + b'?'
_BYTES_FRAGMENT = _BYTES_QUERY
_FILE_SCHEME = 'file'
_STATUS_CODES_REDIRECT = (
    http.HTTPStatus.MOVED_PERMANENTLY, http.HTTPStatus.FOUND, http.HTTPStatus.SEE_OTHER,
    http.HTTPStatus.TEMPORARY_REDIRECT, http.HTTPStatus.PERMANENT_REDIRECT)
_RE_ENCODED = re.compile(r"%[a-fA-F0-9]{2}")
_OPENER_DEFAULT = urllib.request.build_opener()
_OPENER_NO_REDIRECT = urllib.request.build_opener(_HTTPRedirectHandler)


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


HEADERS = {
    Header.USER_AGENT: f'{__name__}/{__version__}',
    Header.ACCEPT: '*/*',
    Header.CONNECTION: 'keep-alive'}


class Response:
    chunk_size = _MIN_CHUNK

    def __init__(self, resp: urllib.response.addinfourl | http.client.HTTPResponse | urllib.error.URLError):
        self.status_code = http.HTTPStatus(getattr(
            resp, 'status', None) or http.HTTPStatus.IM_A_TEAPOT)
        self.headers = getattr(resp, 'headers', {})
        self.url = getattr(resp, 'url', '')
        self.reason = getattr(resp, 'reason', '')

        self.response = resp
        self.local = resp.fp.name if isinstance(getattr(
            self.response, 'file', None), io.BufferedReader) else None

    def __bool__(self) -> bool:
        return self.status_code == http.HTTPStatus.OK if self.local is None else os.path.isfile(self.local)

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}: <{self.status_code.name}>>'

    def __iter__(self) -> Iterator[bytes]:
        while chunk := self.response.read(self.chunk_size):
            yield chunk

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
    def content(self) -> bytes:
        return b''.join(self)

    @property
    def text(self) -> str:
        return self.content.decode()

    def json(self) -> Any:
        with contextlib.suppress(json_.decoder.JSONDecodeError):
            return json_.loads(self.content)

    @property
    def links(self):
        links = {}
        if Header.LINK in self.headers:
            for url, params in get_links(self.headers[Header.LINK]).items():
                links[params.get('rel', url)] = {'url': url, **params}
        return links

    def close(self):
        self.response.close()


def _str(o: AnyStr) -> str:
    return o.decode() if isinstance(o, bytes) else o


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


def get_params(url: AnyStr) -> dict[AnyStr, list[AnyStr]]:
    return urllib.parse.parse_qs(urllib.parse.urlsplit(url).query)


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


def merge_params(url: AnyStr, params: Optional[_TParams] = None) -> AnyStr:
    components = urllib.parse.urlsplit(url)
    query = urllib.parse.parse_qs(components.query, True)
    if params is not None:
        for key, val in params.items():
            if val is not None:
                if key not in query:
                    query[key] = []
                if isinstance(val, (bytes, str)):
                    query[key].append(val)
                else:
                    query[key].extend(val)
    # noinspection PyProtectedMember
    return components._replace(query=encode_params(query)).geturl()


def merge_cookies(*cookies: _TCookie, jar: Optional[http.cookiejar.CookieJar] = None) -> http.cookiejar.CookieJar:
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


def encode_cookies(cookies: _TCookies, url_or_request: str | urllib.request.Request) -> dict[str, str]:
    if not isinstance(cookies, http.cookiejar.CookieJar):
        cookies = merge_cookies(*cookies.items())
    if not isinstance(url_or_request, urllib.request.Request):
        url_or_request = urllib.request.Request(url_or_request)
    cookies.add_cookie_header(url_or_request)
    return url_or_request.unredirected_hdrs


def encode_params(params: Optional[AnyStr | Mapping]) -> str:
    if params is None:
        return ''
    elif isinstance(params, (bytes, str)):
        return _str(params)
    else:
        return urllib.parse.urlencode(params, True)


# noinspection PyShadowingNames
def encode_body(data: Optional[_TData] = None, files: Optional[_TFiles] = None, json: Optional[_TJSON] = None,
                request: Optional[urllib.request.Request] = None) -> tuple[Optional[str], Optional[bytes]]:
    if files is not None:  # TODO escape quotes + data can be iterable/readable bytes
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
        data = encode_params(data).encode()
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


def request(method: Optional[_TMethod], url: AnyStr, params: Optional[_TParams] = None,
            data: Optional[_TData] = None, headers: Optional[_THeaders] = None, cookies: Optional[_TCookies] = None,
            files: Optional[_TFiles] = None, auth: Optional[_TAuth] = None, timeout: Optional[float] = None,
            allow_redirects: bool = True, stream: bool = True, json: Optional[_TJSON] = None) -> Response:
    if params is not None:
        url = merge_params(url, params)
    request_ = urllib.request.Request(encode_url(url), headers=HEADERS)
    if method is not None:
        encode_method(method, request_)
    if data is not None or files is not None or json is not None:
        encode_body(data, files, json, request_)
    if cookies is not None:
        encode_cookies(cookies, request_)
    if auth is not None:
        encode_auth(auth, request_)
    if headers is not None:
        for header in headers.items():
            request_.add_header(*header)
    try:
        response = (_OPENER_DEFAULT if allow_redirects else
                    _OPENER_NO_REDIRECT).open(request_, timeout=timeout)
    except urllib.error.URLError as response:
        return Response(response)
    else:
        response_ = Response(response)
        if not stream:
            response_.content = response_.content
        return response_


def get(url: AnyStr, params: Optional[_TParams] = None,
        data: Optional[_TData] = None, headers: Optional[_THeaders] = None, cookies: Optional[_TCookie] = None,
        files: Optional[_TFiles] = None, auth: Optional[_TAuth] = None, timeout: Optional[float] = None,
        allow_redirects: bool = True, stream: bool = True, json: Optional[_TJSON] = None) -> Response:
    return request(http.HTTPMethod.GET, url, params, data, headers, cookies, files, auth, timeout, allow_redirects, stream, json)


def options(url: AnyStr, params: Optional[_TParams] = None,
            data: Optional[_TData] = None, headers: Optional[_THeaders] = None, cookies: Optional[_TCookie] = None,
            files: Optional[_TFiles] = None, auth: Optional[_TAuth] = None, timeout: Optional[float] = None,
            allow_redirects: bool = False, stream: bool = True, json: Optional[_TJSON] = None) -> Response:
    return request(http.HTTPMethod.OPTIONS, url, params, data, headers, cookies, files, auth, timeout, allow_redirects, stream, json)


def head(url: AnyStr, params: Optional[_TParams] = None,
         data: Optional[_TData] = None, headers: Optional[_THeaders] = None, cookies: Optional[_TCookie] = None,
         files: Optional[_TFiles] = None, auth: Optional[_TAuth] = None, timeout: Optional[float] = None,
         allow_redirects: bool = False, stream: bool = True, json: Optional[_TJSON] = None) -> Response:
    return request(http.HTTPMethod.HEAD, url, params, data, headers, cookies, files, auth, timeout, allow_redirects, stream, json)


def post(url: AnyStr, data: Optional[_TData] = None,
         json: Optional[_TJSON] = None, params: Optional[_TParams] = None, headers: Optional[_THeaders] = None,
         cookies: Optional[_TCookie] = None, files: Optional[_TFiles] = None, auth: Optional[_TAuth] = None,
         timeout: Optional[float] = None, allow_redirects: bool = True, stream: bool = True) -> Response:
    return request(http.HTTPMethod.POST, url, params, data, headers, cookies, files, auth, timeout, allow_redirects, stream, json)


def put(url: AnyStr, data: Optional[_TData] = None,
        params: Optional[_TParams] = None, headers: Optional[_THeaders] = None, cookies: Optional[_TCookie] = None,
        files: Optional[_TFiles] = None, auth: Optional[_TAuth] = None, timeout: Optional[float] = None,
        allow_redirects: bool = True, stream: bool = True, json: Optional[_TJSON] = None, ) -> Response:
    return request(http.HTTPMethod.PUT, url, params, data, headers, cookies, files, auth, timeout, allow_redirects, stream, json)


def patch(url: AnyStr, data: Optional[_TData] = None,
          params: Optional[_TParams] = None, headers: Optional[_THeaders] = None, cookies: Optional[_TCookie] = None,
          files: Optional[_TFiles] = None, auth: Optional[_TAuth] = None, timeout: Optional[float] = None,
          allow_redirects: bool = True, stream: bool = True, json: Optional[_TJSON] = None, ) -> Response:
    return request(http.HTTPMethod.PATCH, url, params, data, headers, cookies, files, auth, timeout, allow_redirects, stream, json)


def delete(url: AnyStr, params: Optional[_TParams] = None,
           data: Optional[_TData] = None, headers: Optional[_THeaders] = None, cookies: Optional[_TCookie] = None,
           files: Optional[_TFiles] = None, auth: Optional[_TAuth] = None, timeout: Optional[float] = None,
           allow_redirects: bool = True, stream: bool = True, json: Optional[_TJSON] = None) -> Response:
    return request(http.HTTPMethod.DELETE, url, params, data, headers, cookies, files, auth, timeout, allow_redirects, stream, json)


def sizeof(url: AnyStr) -> int:
    return int(head(url).headers.get(Header.CONTENT_LENGTH, 0))


def retrieve(url: AnyStr, path: AnyStr, size: int = 0, chunk_size: Optional[int] = None,
             chunk_count: Optional[int] = None, query_callback: Optional[Callable[[float], bool]] = None) -> bool:
    response = get(url)
    if response:
        if not size:
            size = (int(response.headers.get(Header.CONTENT_LENGTH, _UNK_SIZE))
                    if response.local is None else os.path.getsize(response.local))
        response.chunk_size = max(chunk_size or size // (chunk_count or sys.maxsize), _MIN_CHUNK)
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'wb') as file:
                ratio = 0.0
                for chunk in response:
                    if size != _UNK_SIZE:
                        ratio += file.write(chunk) / size
                    if query_callback is not None and not query_callback(ratio):
                        return False
        except PermissionError:
            return False
        try:
            retrieved = size == _UNK_SIZE or size == os.path.getsize(path)
        except OSError:
            retrieved = False
        if retrieved and query_callback is not None:
            query_callback(1.0)
        return retrieved
    return False
