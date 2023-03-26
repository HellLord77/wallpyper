__version__ = '0.1.5'

import base64
import calendar
import contextlib
import http.client
import http.cookiejar
import http.cookies
import io
import itertools
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
_TJSON = int | bool | float | str | tuple | list | dict
_TParams = Mapping[AnyStr, Optional[AnyStr | Iterable[AnyStr]]]
_THeaders = Mapping[str, str]
_TCookie = tuple[str, str] | http.cookies.Morsel | http.cookiejar.Cookie | http.cookiejar.CookieJar
_TFiles = Mapping[str, AnyStr | BinaryIO | tuple[
    AnyStr | BinaryIO] | tuple[AnyStr | BinaryIO, AnyStr] | tuple[
                      AnyStr | BinaryIO, AnyStr, Mapping[str, Optional[str]]]]
_TAuth = str | tuple[str, str]


class _HTTPRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req: urllib.request.Request, fp: IO[bytes],
                         code: int, msg: str, headers: http.client.HTTPMessage,
                         newurl: str) -> Optional[urllib.request.Request]:
        pass


_MIN_CHUNK = 32 * 1024
_CRLF = '\r\n'
_FILE_SCHEME = 'file'
_HTTP_SCHEME = 'http'
_HTTPS_SCHEME = 'https'
_MIME_JSON = 'application/json'
_MIME_FORM = 'application/x-www-form-urlencoded'
_NORMALIZABLE_SCHEMES = '', _HTTP_SCHEME, _HTTPS_SCHEME
_RE_ENCODED = re.compile(r"%[a-fA-F0-9]{2}")
_OPENER_DEFAULT = urllib.request.build_opener()
_OPENER_NO_REDIRECT = urllib.request.build_opener(_HTTPRedirectHandler)

FLAG_REREAD_RESPONSE = True
SUB_DELIM_BYTES = b"!$&'()*+,;="
USERINFO_BYTES = SUB_DELIM_BYTES + b':'
PATH_BYTES = USERINFO_BYTES + b'@/'
QUERY_BYTES = PATH_BYTES + b'?'
FRAGMENT_BYTES = QUERY_BYTES


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


MAX_CHUNK = 1024 * 1024
HEADERS = {
    Header.ACCEPT_LANGUAGE: 'en-US',
    Header.USER_AGENT: f'{__name__}/{__version__}'}


def _getheader(_: str, default=None):
    return default


class Response:
    _content = b''
    chunk_size = _MIN_CHUNK

    def __init__(self, response: urllib.response.addinfourl | http.client.HTTPResponse | urllib.error.URLError):
        self.response = response
        self.status_code = http.HTTPStatus(getattr(
            response, 'status', None) or http.HTTPStatus.IM_A_TEAPOT)
        self.headers = getattr(response, 'headers', {})
        self.local = response.fp.name if isinstance(getattr(
            self.response, 'file', None), io.BufferedReader) else None
        self.getheader = getattr(response, 'getheader', _getheader)

    def __bool__(self) -> bool:
        return self.status_code == http.HTTPStatus.OK if self.local is None else os.path.isfile(self.local)

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}: <{self.status_code.name}>>'

    def __iter__(self) -> Iterator[bytes]:
        while chunk := self.response.read(self.chunk_size):
            if FLAG_REREAD_RESPONSE:
                self._content += chunk
            yield chunk

    @property
    def content(self) -> bytes:
        return b''.join(self) or self._content

    @property
    def text(self) -> str:
        return self.content.decode()

    def json(self) -> Any:
        with contextlib.suppress(json_.decoder.JSONDecodeError):
            return json_.loads(self.content)


def _str(o: AnyStr) -> str:
    return o.decode() if isinstance(o, bytes) else o


def _replace(namedtuple: _TResult, **kwargs) -> _TResult:
    # noinspection PyProtectedMember
    return namedtuple._replace(**kwargs)


def is_path(url: AnyStr) -> bool:
    return _FILE_SCHEME == _str(urllib.parse.urlsplit(url).scheme)


def from_path(path: str) -> str:
    # noinspection PyArgumentList
    return urllib.parse.SplitResult(_FILE_SCHEME, '', urllib.request.pathname2url(path), '', '').geturl()


def strip(url: str) -> str:
    return _replace(urllib.parse.urlsplit(url), query='', fragment='').geturl()


def join(base: str, *paths: str) -> str:
    if not base.endswith('/'):
        base += '/'
    for path in paths:
        if path:
            base = f'{urllib.parse.urljoin(base, path)}/'
    return base[:-1]


@typing.overload
def get_params(url: bytes) -> dict[bytes, list[bytes]]:
    pass


@typing.overload
def get_params(url: str) -> dict[str, list[str]]:
    pass


def get_params(url):
    return urllib.parse.parse_qs(urllib.parse.urlsplit(url).query)


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
        expires = None
        if morsel["max-age"]:
            expires = int(time.time() + int(morsel['max-age']))
        elif morsel['expires']:
            expires = calendar.timegm(time.strptime(morsel['expires'], '%a, %d-%b-%Y %H:%M:%S GMT'))
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
    return _replace(components, query=encode_params(query)).geturl()


def merge_cookies(*cookies: _TCookie,
                  cookie_jar: Optional[http.cookiejar.CookieJar] = None) -> http.cookiejar.CookieJar:
    if cookie_jar is None:
        cookie_jar = http.cookiejar.CookieJar()
    for cookie in cookies:
        if isinstance(cookie, http.cookiejar.CookieJar):
            for cookie_ in cookie:
                cookie_jar.set_cookie(cookie_)
        else:
            if isinstance(cookie, http.cookies.Morsel):
                cookie = get_cookie(cookie)
            elif isinstance(cookie, tuple):
                cookie = get_cookie(*cookie)
            cookie_jar.set_cookie(cookie)
    return cookie_jar


def _upper_encoded(match: re.Match) -> AnyStr:
    return match.group(0).upper()


def _encode_component(component: str, valid: AnyStr) -> str:
    component, count_encoded = _RE_ENCODED.subn(_upper_encoded, component)
    if count_encoded == component.count('%'):
        valid += b'%'
    return urllib.parse.quote_plus(component, safe=valid)


def encode_url(url: AnyStr) -> str:
    components = urllib.parse.urlsplit(_str(url))
    if components.scheme in _NORMALIZABLE_SCHEMES:
        components = _replace(components, path=_encode_component(
            components.path, PATH_BYTES), query=_encode_component(
            components.query, QUERY_BYTES), fragment=_encode_component(
            components.fragment, FRAGMENT_BYTES))
    return components.geturl()


def encode_cookies(cookies: http.cookiejar.CookieJar, url: str) -> dict[str, str]:
    request_ = urllib.request.Request(url)
    cookies.add_cookie_header(request_)
    return request_.unredirected_hdrs


def encode_params(params: Optional[AnyStr | Mapping]) -> str:
    if params is None:
        return ''
    elif isinstance(params, (bytes, str)):
        return _str(params)
    else:
        return urllib.parse.urlencode(params, True)


def encode_body(data: Optional[_TParams] = None, files: Optional[_TFiles] = None,
                json: Optional[_TJSON] = None) -> tuple[str, bytes]:
    if files is not None:  # TODO escape quotes
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
        return f'multipart/form-data; boundary={boundary}', _CRLF.encode().join(lines)
    elif data is not None:
        return _MIME_FORM, encode_params(data).encode()
    elif json is not None:
        return _MIME_JSON, json_.dumps(json, allow_nan=False).encode()


def encode_auth(auth: _TAuth) -> str:
    return (f'Bearer {auth}' if isinstance(auth, str) else
            f'Basic {base64.b64encode(":".join(auth).encode("latin1")).decode()}')


def request(method: str | http.HTTPMethod, url: AnyStr, data: Optional[_TParams] = None,
            json: Optional[_TJSON] = None, params: Optional[_TParams] = None, headers: Optional[_THeaders] = None,
            cookies: Optional[_TCookie] = None, files: Optional[_TFiles] = None, auth: Optional[_TAuth] = None,
            timeout: Optional[float] = None, allow_redirects: bool = True, stream: bool = True) -> Response:
    if params is not None:
        url = merge_params(url, params)
    try:
        request_ = urllib.request.Request(encode_url(
            url), data, headers=HEADERS, method=str(method))
    except ValueError as exc:
        return Response(urllib.error.URLError(exc))
    else:
        if data is not None or files is not None or json is not None:
            mime, request_.data = encode_body(data, files, json)
            request_.add_header(Header.CONTENT_TYPE, mime)
        if cookies is not None:
            itertools.starmap(request_.add_header, encode_cookies(
                cookies, request_.full_url).items())
        if auth is not None:
            request_.add_header(Header.AUTHORIZATION, encode_auth(auth))
        if headers is not None:
            itertools.starmap(request_.add_header, headers.items())
        urllib.request.install_opener(
            _OPENER_DEFAULT if allow_redirects else _OPENER_NO_REDIRECT)
        try:
            _response = urllib.request.urlopen(request_, timeout=timeout)
        except urllib.error.URLError as _response:
            return Response(_response)
        else:
            response = Response(_response)
            if not stream:
                _ = response.content
            return response


def get(url: AnyStr, data: Optional[_TParams] = None,
        json: Optional[_TJSON] = None, params: Optional[_TParams] = None, headers: Optional[_THeaders] = None,
        cookies: Optional[_TCookie] = None, files: Optional[_TFiles] = None, auth: Optional[_TAuth] = None,
        timeout: Optional[float] = None, allow_redirects: bool = True, stream: bool = True) -> Response:
    return request(http.HTTPMethod.GET, url, data, json, params, headers, cookies, files, auth, timeout, allow_redirects, stream)


def options(url: AnyStr, data: Optional[_TParams] = None,
            json: Optional[_TJSON] = None, params: Optional[_TParams] = None, headers: Optional[_THeaders] = None,
            cookies: Optional[_TCookie] = None, files: Optional[_TFiles] = None, auth: Optional[_TAuth] = None,
            timeout: Optional[float] = None, allow_redirects: bool = False, stream: bool = True) -> Response:
    return request(http.HTTPMethod.OPTIONS, url, data, json, params, headers, cookies, files, auth, timeout, allow_redirects, stream)


def head(url: AnyStr, data: Optional[_TParams] = None,
         json: Optional[_TJSON] = None, params: Optional[_TParams] = None, headers: Optional[_THeaders] = None,
         cookies: Optional[_TCookie] = None, files: Optional[_TFiles] = None, auth: Optional[_TAuth] = None,
         timeout: Optional[float] = None, allow_redirects: bool = False, stream: bool = True) -> Response:
    return request(http.HTTPMethod.HEAD, url, data, json, params, headers, cookies, files, auth, timeout, allow_redirects, stream)


def post(url: AnyStr, data: Optional[_TParams] = None,
         json: Optional[_TJSON] = None, params: Optional[_TParams] = None, headers: Optional[_THeaders] = None,
         cookies: Optional[_TCookie] = None, files: Optional[_TFiles] = None, auth: Optional[_TAuth] = None,
         timeout: Optional[float] = None, allow_redirects: bool = True, stream: bool = True) -> Response:
    return request(http.HTTPMethod.POST, url, data, json, params, headers, cookies, files, auth, timeout, allow_redirects, stream)


def put(url: AnyStr, data: Optional[_TParams] = None,
        json: Optional[_TJSON] = None, params: Optional[_TParams] = None, headers: Optional[_THeaders] = None,
        cookies: Optional[_TCookie] = None, files: Optional[_TFiles] = None, auth: Optional[_TAuth] = None,
        timeout: Optional[float] = None, allow_redirects: bool = True, stream: bool = True) -> Response:
    return request(http.HTTPMethod.PUT, url, data, json, params, headers, cookies, files, auth, timeout, allow_redirects, stream)


def patch(url: AnyStr, data: Optional[_TParams] = None,
          json: Optional[_TJSON] = None, params: Optional[_TParams] = None, headers: Optional[_THeaders] = None,
          cookies: Optional[_TCookie] = None, files: Optional[_TFiles] = None, auth: Optional[_TAuth] = None,
          timeout: Optional[float] = None, allow_redirects: bool = True, stream: bool = True) -> Response:
    return request(http.HTTPMethod.PATCH, url, data, json, params, headers, cookies, files, auth, timeout, allow_redirects, stream)


def delete(url: AnyStr, data: Optional[_TParams] = None,
           json: Optional[_TJSON] = None, params: Optional[_TParams] = None, headers: Optional[_THeaders] = None,
           cookies: Optional[_TCookie] = None, files: Optional[_TFiles] = None, auth: Optional[_TAuth] = None,
           timeout: Optional[float] = None, allow_redirects: bool = True, stream: bool = True) -> Response:
    return request(http.HTTPMethod.DELETE, url, data, json, params, headers, cookies, files, auth, timeout, allow_redirects, stream)


def sizeof(url: AnyStr) -> int:
    return int(head(url).getheader(Header.CONTENT_LENGTH, 0))


def retrieve(url: AnyStr, path: AnyStr, size: int = 0, chunk_size: Optional[int] = None,
             chunk_count: Optional[int] = None, query_callback: Optional[Callable[[float], bool]] = None) -> bool:
    response = get(url)
    if response:
        if not size:
            size = (int(response.getheader(Header.CONTENT_LENGTH, sys.maxsize))
                    if response.local is None else os.path.getsize(response.local))
        response.chunk_size = max(chunk_size or size // (chunk_count or sys.maxsize), _MIN_CHUNK)
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'wb') as file:
                ratio = 0
                for chunk in response:
                    ratio += file.write(chunk) / size
                    if query_callback is not None and not query_callback(ratio):
                        return False
        except PermissionError:
            return False
        try:
            retrieved = size in (sys.maxsize, os.path.getsize(path))
        except OSError:
            retrieved = False
        if retrieved and query_callback is not None:
            query_callback(1.0)
        return retrieved
    return False
