from __future__ import annotations as _

__version__ = '0.2.12'

import base64
import bz2
import dataclasses
import datetime
import functools
import hashlib
import http.client
import http.cookiejar
import http.cookies
import io
import itertools
import json as json_
import lzma
import os
import re
import secrets
import socket
import ssl
import sys
import time
import typing
import urllib.error
import urllib.parse
import urllib.request
import urllib.response
import uuid
import zlib
from typing import Any
from typing import AnyStr
from typing import BinaryIO
from typing import Callable
from typing import Iterable
from typing import Iterator
from typing import Mapping
from typing import NoReturn
from typing import Optional
from typing import Sequence

from . import _caseless

CONTENT_CHUNK_SIZE = 10 * 1024
RETRIEVE_UNKNOWN_SIZE = 0

Status = http.HTTPStatus
Method = http.HTTPMethod


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


class _DecoderMeta(type):
    _encoding_: str | Iterable[str]

    _decoders: dict[str, _DecoderMeta] = {}

    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if isinstance(cls._encoding_, str):
            cls._encoding_ = cls._encoding_,
        for encoding in cls._encoding_:
            cls[encoding.lower()] = cls

    def __contains__(self, encoding: str) -> bool:
        return encoding.lower() in self._decoders

    def __getitem__(self, encoding: str) -> _DecoderMeta:
        return self._decoders[encoding.lower()]

    def __setitem__(self, encoding: str, decoder: _DecoderMeta):
        self._decoders[encoding.lower()] = decoder

    def __delitem__(self, encoding: str):
        del self._decoders[encoding.lower()]

    def __iter__(self) -> Iterator[str]:
        return iter(self._decoders)

    def get(cls, encoding: Optional[str | Iterable[str]] = None) -> Optional[Decoder]:
        if isinstance(encoding, str):
            encoding = urllib.request.parse_http_list(encoding)
        if encoding:
            decoders = (cls[token]() for token in encoding)
            return next(decoders) if len(encoding) == 1 else MultiDecoder(*decoders)


class Decoder(metaclass=_DecoderMeta):
    _encoding_: str | Iterable[str] = ()

    def flush(self) -> bytes:
        return b''

    def decompress(self, data: bytes) -> bytes:
        raise NotImplementedError


class IdentityDecoder(Decoder):
    _encoding_ = 'identity'

    def decompress(self, data: bytes) -> bytes:
        return data


class DeflateDecoder(Decoder):
    _encoding_ = 'deflate'

    _tried = False

    def __init__(self, wbits: int = zlib.MAX_WBITS):
        self._decoder = zlib.decompressobj(wbits)

    def flush(self) -> bytes:
        return self._decoder.flush()

    def decompress(self, data: bytes) -> bytes:
        if self._tried:
            return self._decoder.decompress(data)
        else:
            try:
                data = self._decoder.decompress(data)
            except zlib.error:
                self.__init__(-zlib.MAX_WBITS)
                self._tried = True
                data = self.decompress(data)
            else:
                if data:
                    self._tried = True
            return data


class GzipDecoder(DeflateDecoder):
    _encoding_ = 'gzip', 'x-gzip'

    def __init__(self):
        super().__init__(16 + zlib.MAX_WBITS)

    def decompress(self, data: bytes) -> bytes:
        return self._decoder.decompress(data)


class Bzip2Decoder(Decoder):
    _encoding_ = 'bzip2', 'x-bzip2'

    def __init__(self):
        self._decoder = bz2.BZ2Decompressor()

    def flush(self) -> bytes:
        return self._decoder.unused_data

    def decompress(self, data: bytes) -> bytes:
        return self._decoder.decompress(data)


class LzmaDecoder(Bzip2Decoder):
    _encoding_ = 'lzma', 'x-lzma'

    # noinspection PyMissingConstructor
    def __init__(self):
        self._decoder = lzma.LZMADecompressor()


class MultiDecoder(Decoder):
    def __init__(self, *decoders: Decoder):
        self._decoder = tuple(reversed(decoders))

    def flush(self) -> bytes:
        return self._decoder[-1].flush()

    def decompress(self, data: bytes) -> bytes:
        for decoder in self._decoder:
            data = decoder.decompress(data)
        return data


class Auth:
    _scheme_: str

    # noinspection PyShadowingNames
    def add_header(self, auth: str, request: Optional[urllib.request.Request] = None) -> str:
        if request is not None:
            request.add_unredirected_header(
                Header.AUTHORIZATION, f'{self._scheme_} {auth}')
        return auth

    # noinspection PyShadowingNames
    def encode(self, params: Optional[dict[str, list[Optional[str]]]] = None,
               request: Optional[urllib.request.Request] = None) -> Optional[str]:
        raise NotImplementedError


# noinspection PyAbstractClass
class ProxyAuth(Auth):
    # noinspection PyShadowingNames
    def add_header(self, auth: str, request: Optional[urllib.request.Request] = None) -> str:
        if request is not None:
            request.add_unredirected_header(
                Header.PROXY_AUTHORIZATION, f'{self._scheme_} {auth}')
        return auth


@dataclasses.dataclass
class BasicAuth(Auth):
    _scheme_ = 'Basic'

    username: bytes | str
    password: bytes | str

    # noinspection PyShadowingNames
    def encode(self, _: Optional[dict[str, list[Optional[str]]]] = None,
               request: Optional[urllib.request.Request] = None) -> str:
        self.username = _bytes(self.username)
        self.password = _bytes(self.password)
        return self.add_header(base64.b64encode(
            self.username + b":" + self.password).decode(), request)


@dataclasses.dataclass
class ProxyBasicAuth(ProxyAuth, BasicAuth):
    pass


@dataclasses.dataclass
class BearerAuth(Auth):
    _scheme_ = 'Bearer'

    token: bytes | str

    # noinspection PyShadowingNames
    def encode(self, _: Optional[dict[str, list[Optional[str]]]] = None,
               request: Optional[urllib.request.Request] = None) -> str:
        self.token = _bytes(self.token)
        return self.add_header(self.token.decode(), request)


@dataclasses.dataclass
class ProxyBearerAuth(ProxyAuth, BearerAuth):
    pass


@dataclasses.dataclass
class DigestAuth(Auth):
    _scheme_ = 'Digest'

    username: bytes | str
    password: bytes | str

    _last_nonce = ''
    _nonce_count = 1
    _algorithms = (
        ('sha512', 'SHA-512'), ('sha512_256', 'SHA-512-256'),
        ('sha256', 'SHA-256'), ('md5', 'MD5'))

    # noinspection PyShadowingNames
    def encode(self, params: Optional[dict[str, list[Optional[str]]]] = None,
               request: Optional[urllib.request.Request] = None) -> Optional[str]:
        if params is None:
            return
        self.username = _str(self.username)
        self.password = _str(self.password)
        realm = _caseless.get(params, 'realm')[0]
        nonce = _caseless.get(params, 'nonce')[0]
        qop = _caseless.get(params, 'qop')
        algorithm = _caseless.get(params, 'algorithm', ('MD5',))
        opaque = _caseless.get(params, 'opaque', (None,))[0]
        hash_, algorithm_ = self.get_algorithm(algorithm)
        if hash_ is None:
            return
        uri = request.selector
        a1 = f'{self.username}:{realm}:{self.password}'
        a2 = f'{request.method}:{uri}'
        ha1 = hash_(a1)
        ha2 = hash_(a2)
        if nonce and nonce == self._last_nonce:
            self._nonce_count += 1
        else:
            self._nonce_count = 1
        cnonce = self.get_cnonce(nonce)
        if _caseless.endswith(algorithm_, '-sess'):
            ha1 = f'{ha1}:{nonce}:{cnonce}'
        nc = f'{self._nonce_count:08x}'
        if qop is None:
            qop_ = None
            response = hash_(f'{ha1}:{nonce}:{ha2}')
        else:
            if _caseless.contains(qop, 'auth-int'):
                qop_ = 'auth-int'
                ha2 = hash_(f'{a2}:{hash_(request.data or b"")}')
            elif _caseless.contains(qop, 'auth'):
                qop_ = 'auth'
            else:
                return
            response = hash_(f'{ha1}:{nonce}:{nc}:{cnonce}:{qop_}:{ha2}')
        self._last_nonce = nonce
        params_ = [f'username="{self.username}"', f'realm="{realm}"',
                   f'uri="{uri}"', f'algorithm={algorithm_}', f'nonce="{nonce}"']
        if qop is not None:
            params_.append(f'nc={nc}')
            params_.append(f'cnonce="{cnonce}"')
            params_.append(f'qop="{qop_}"')
        params_.append(f'response="{response}"')
        if opaque is not None:
            params_.append(f'opaque="{opaque}"')
        return self.add_header(','.join(params_), request)

    @classmethod
    def get_algorithm(cls, algorithms: Sequence[str]) -> tuple[Optional[Callable[[bytes | str], str]], str]:
        algorithms_ = {algorithm.upper().removesuffix('-SESS') for algorithm in algorithms}
        for algorithm, algorithm_ in cls._algorithms:
            if algorithm in hashlib.algorithms_available and algorithm_ in algorithms_:
                try:
                    index = _caseless.index(algorithms, algorithm_ + '-SESS')
                except ValueError:
                    index = _caseless.index(algorithms, algorithm_)
                return lambda string: hashlib.new(
                    algorithm, _bytes(string)).hexdigest(), algorithms[index]
        return None, ''

    def get_cnonce(self, nonce: str):
        return hashlib.sha1(f'{self._nonce_count}:{nonce}:{time.ctime()}:'.encode()
                            + secrets.token_bytes()).hexdigest()[:16]


@dataclasses.dataclass
class ProxyDigestAuth(ProxyAuth, DigestAuth):
    pass


class AuthManager(urllib.request.HTTPPasswordMgr):
    passwd: dict[Optional[str], dict[tuple[tuple[str, str], ...], Auth]]

    def __init__(self, *auths: _TAuth):
        super().__init__()
        merge_auths(*auths, man=self)

    def add_auth(self, auth: Auth, url: Optional[str | Iterable[str]] = None, realm: Optional[str] = None):
        if url is None:
            url = ''
        if isinstance(url, str):
            url = url,
        if realm not in self.passwd:
            self.passwd[realm] = {}
        for default_port in True, False:
            # noinspection PyTypeChecker
            self.passwd[realm][tuple(self.reduce_uri(
                uri, default_port) for uri in url)] = auth

    def find_auths(self, url: str, realm: Optional[str] = None) -> Iterator[Auth]:
        if (auth := extract_auth(url)) is not None:
            yield auth
        if (auth := self.find_user_password(realm, url)) != (None, None):
            yield auth
        # noinspection PyTypeChecker
        if (auth := self.find_user_password(None, url)) != (None, None):
            yield auth
        if (domains := self.passwd.get(realm)) is not None and (
                auth := domains.get((('', '/'),))) is not None:
            yield auth
        if (domains := self.passwd.get(None)) is not None and (
                auth := domains.get((('', '/'),))) is not None:
            yield auth

    def get_auth(self, url: str, realm: Optional[str] = None) -> Optional[Auth]:
        for auth in self.find_auths(url, realm):
            return auth


_TMethod = str | Method
_TURL = bytes | str
_TParams = bytes | str | tuple[bytes | str, Optional[bytes | str | Iterable[
    bytes | str]]] | Mapping[bytes | str, Optional[bytes | str | Iterable[bytes | str]]]
_TData = bytes | str | Mapping[bytes | str, Optional[bytes | str | Iterable[bytes | str]]]
_THeaders = bytes | str | Iterable[tuple[str, Optional[
    str]]] | Mapping[str, Optional[str]] | io.BufferedIOBase
_TCookie = tuple[str, str] | http.cookies.Morsel | http.cookiejar.Cookie | http.cookiejar.CookieJar
_TCookies = Iterable[_TCookie] | Mapping[
    str | http.cookies.Morsel, Optional[str]] | http.cookiejar.CookieJar
_TFiles = Mapping[str, bytes | str | BinaryIO | tuple[
    bytes | str | BinaryIO] | tuple[bytes | str | BinaryIO, bytes | str] | tuple[
                           bytes | str | BinaryIO, bytes | str, Mapping[str, Optional[str]]]]
_TAuth = bytes | str | tuple[bytes | str, bytes | str] | Auth | AuthManager
_TAuths = Iterable[_TAuth] | Mapping[str | Iterable[str], _TAuth] | AuthManager
_TJSON = bool | int | float | str | tuple | list | dict
_TProxies = str | Iterable[tuple[str, str]] | Mapping[str, Optional[str]]
_TVerify = bool | bytes | str | tuple[Optional[bytes | str], Optional[bytes | str]] | tuple[
    Optional[bytes | str], Optional[bytes | str], Optional[bytes]] | ssl.SSLContext

_RETRIEVE_CHUNK_SIZE = 64 * 1024
_BYTES_PATH = b"!$&'()*+,;=:@/"
_BYTES_FRAGMENT = _BYTES_QUERY = _BYTES_PATH + b'?'
_FILE_SCHEME = 'file'
_STATUS_REDIRECT_PERMANENT = (
    Status.MOVED_PERMANENTLY, Status.PERMANENT_REDIRECT)
_STATUS_REDIRECT = (
    *_STATUS_REDIRECT_PERMANENT, Status.FOUND,
    Status.SEE_OTHER, Status.TEMPORARY_REDIRECT)
_RE_ENCODED = re.compile(r'%[a-fA-F0-9]{2}')
_RE_LINKS = re.compile(r'\s*?<(\S*?)>;?\s*([^<]*)')


def default_accept_encoding(*encodings: str) -> str:
    return ','.join(itertools.chain(Decoder, encodings))


def default_accept_language(*languages: str | tuple[str | Iterable[str], float]) -> str:
    accept_languages = []
    for language in itertools.chain(((('en-US', 'en'), 0.9),), languages):
        if not isinstance(language, str):
            language, quality = language
            if not isinstance(language, str):
                language = ','.join(language)
            if quality != 1.0:
                language = f'{language};q={quality}'
        accept_languages.append(language)
    return ','.join(accept_languages)


def default_user_agent(name: str = 'python-' + __name__.rsplit('.', 1)[-1]) -> str:
    return f'{name}/{__version__}'


def default_headers() -> dict[str, str]:
    return {
        Header.CONNECTION: 'keep-alive',
        Header.ACCEPT: '*/*',
        Header.ACCEPT_ENCODING: default_accept_encoding(),
        Header.ACCEPT_LANGUAGE: default_accept_language(),
        Header.USER_AGENT: default_user_agent()}


def default_verify() -> ssl.SSLContext:
    # noinspection PyUnresolvedReferences,PyProtectedMember
    return http.client.HTTPSConnection('')._context


class _OpenerDirector(urllib.request.OpenerDirector):
    def __init__(self, *handlers: urllib.request.BaseHandler):
        super().__init__()
        for handler in handlers:
            self.add_handler(handler)

    # noinspection PyUnresolvedReferences
    def remove_handler(self, handler: urllib.request.BaseHandler):
        other = urllib.request.OpenerDirector()
        other.add_handler(handler)
        thandler = type(handler)
        for protocol in set(other.handle_error).intersection(self.handle_error):
            lookup = self.handle_error[protocol]
            lookup_ = other.handle_error[protocol]
            for kind in set(lookup_).intersection(lookup):
                lookup[kind][:] = [handler_ for handler_ in lookup_[
                    kind] if not isinstance(handler_, thandler)]
        for protocol in set(other.handle_open).intersection(self.handle_open):
            self.handle_open[protocol][:] = [handler_ for handler_ in other.handle_open[
                protocol] if not isinstance(handler_, thandler)]
        for protocol in set(other.process_response).intersection(self.process_response):
            self.process_response[protocol][:] = [handler_ for handler_ in other.process_response[
                protocol] if not isinstance(handler_, thandler)]
        for protocol in set(other.process_request).intersection(self.process_request):
            self.process_request[protocol][:] = [handler_ for handler_ in other.process_request[
                protocol] if not isinstance(handler_, thandler)]
        self.handlers[:] = [handler_ for handler_ in self.handlers
                            if not isinstance(handler_, thandler)]

    # noinspection PyShadowingNames
    def open_ex(self, request: urllib.request.Request) -> Response:
        timeout = getattr(request, 'timeout', None)
        if timeout is None:
            timeout = socket.getdefaulttimeout()
        start = time.perf_counter()
        response = self.open(request, timeout=timeout)
        response.elapsed = datetime.timedelta(seconds=time.perf_counter() - start)
        return Response(request, response)


class _HTTPDefaultErrorHandler(urllib.request.HTTPDefaultErrorHandler):
    def http_error_default(self, _: urllib.request.Request, response: http.client.HTTPResponse,
                           __: int, ___: str, ____: http.client.HTTPMessage) -> http.client.HTTPResponse:
        return response


class _ProxyHandler(urllib.request.ProxyHandler):
    def __init__(self):
        super().__init__({})

    # noinspection PyShadowingNames
    def default_open(self, request: urllib.request.Request) -> Optional[urllib.request.Request]:
        if (proxies := getattr(request, '_proxies', None)) is not None and (
                proxy := proxies.get(request.type)) is not None:
            return self.proxy_open(request, proxy, request.type)


class _HTTPHandler(urllib.request.HTTPHandler):
    # noinspection PyShadowingNames
    def http_open(self, request: urllib.request.Request) -> http.client.HTTPResponse:
        return self.do_open(http.client.HTTPConnection, request)


class _HTTPSHandler(urllib.request.HTTPSHandler):
    # noinspection PyShadowingNames
    def https_open(self, request: urllib.request.Request) -> http.client.HTTPResponse:
        # noinspection PyTypeChecker
        return self.do_open(http.client.HTTPSConnection, request,
                            context=getattr(request, '_verify', None))


class _HTTPRedirectHandler(urllib.request.HTTPRedirectHandler):
    # noinspection PyShadowingNames
    def redirect_request(self, request: urllib.request.Request,
                         response: http.client.HTTPResponse, status: int, reason: str,
                         headers: http.client.HTTPMessage, url: str) -> Optional[urllib.request.Request]:
        request_next = request.next = super().redirect_request(
            request, response, status, reason, headers, url)
        _request_set_private(request_next, getattr(request, '_auths', None), getattr(
            request, '_cookies', None), getattr(request, '_proxies', None), getattr(
            request, '_stream', None), getattr(request, '_verify', None), allow_redirects := getattr(
            request, '_allow_redirects', None), getattr(request, '_force_auth', None))
        if allow_redirects is not False:
            return request_next


class _HTTPCookieProcessor(urllib.request.HTTPCookieProcessor):
    # noinspection PyShadowingNames
    def http_request(self, request: urllib.request.Request) -> urllib.request.Request:
        if (cookies := getattr(request, '_cookies', None)) is not None:
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


class _HTTPAuthHandler(urllib.request.BaseHandler):
    _tauth_: type[Auth]

    def __init_subclass__(cls):
        cls.handler_order = cls.handler_order
        _HTTPAuthHandler.handler_order -= 1

    # noinspection PyShadowingNames
    def retry_auth(self, request: urllib.request.Request,
                   auths: Iterable[str]) -> Optional[http.client.HTTPResponse]:
        for auth in auths:
            # noinspection PyProtectedMember
            if (params := _caseless.get(get_chals(
                    auth), self._tauth_._scheme_)) is not None:
                if self.encode(request, params):
                    return self.parent.open(request, timeout=request.timeout)

    # noinspection PyShadowingNames
    def encode(self, request: urllib.request.Request,
               params: list[dict[str, list[Optional[str]]]] = None) -> bool:
        if getattr(request, '_tried_auth', None) is not True and (
                man := getattr(request, '_auths', None)) is not None:
            realm = None
            if params is not None:
                params = params[0]
                if (val := _caseless.get(params, 'realm')) is not None:
                    realm = val[0]
            auth = man.get_auth(request.full_url, realm)
            if isinstance(auth, self._tauth_) and auth.encode(
                    params, request) is not None:
                request._tried_auth = True
                return True
        return False

    # noinspection PyShadowingNames
    def http_request(self, request: urllib.request.Request) -> urllib.request.Request:
        if getattr(request, '_force_auth', None) is not False:
            self.encode(request)
        return request

    # noinspection PyShadowingNames
    def http_error_401(self, request: urllib.request.Request,
                       _: http.client.HTTPResponse, __: int, ___: str,
                       headers: http.client.HTTPMessage) -> http.client.HTTPResponse:
        if not request.has_header(Header.AUTHORIZATION) and (
                auths := headers.get_all(Header.WWW_AUTHENTICATE)) is not None:
            return self.retry_auth(request, auths)

    # noinspection PyShadowingNames
    def http_error_407(self, request: urllib.request.Request,
                       _: http.client.HTTPResponse, __: int, ___: str,
                       headers: http.client.HTTPMessage) -> http.client.HTTPResponse:
        if not request.has_header(Header.PROXY_AUTHORIZATION) and (
                auths := headers.get_all(Header.PROXY_AUTHENTICATE)) is not None:
            return self.retry_auth(request, auths)

    https_request = http_request


class _HTTPBasicAuthHandler(_HTTPAuthHandler):
    _tauth_ = BasicAuth


class _HTTPBearerAuthHandler(_HTTPAuthHandler):
    _tauth_ = BearerAuth


class _HTTPDigestAuthHandler(_HTTPAuthHandler):
    _tauth_ = DigestAuth

    # noinspection PyShadowingNames
    def http_request(self, request: urllib.request.Request) -> urllib.request.Request:
        return request

    https_request = http_request


@dataclasses.dataclass
class Request:
    method: Optional[_TMethod] = None
    url: Optional[_TURL] = None
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
        if method is None:
            method = Method.POST if self.data else Method.GET
        encode_method(method, self._request)

    def prepare_url(self, url: Optional[_TURL] = None, params: Optional[_TParams] = None):
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
        if auth is not None:
            encode_auth(auth, self._request)

    def prepare_cookies(self, cookies: Optional[_TCookies] = None):
        if cookies is not None:
            encode_cookies(cookies, self._request)


class Response:
    status_code: int | Status
    headers: http.client.HTTPMessage
    url: str
    raw: urllib.response.addinfourl | http.client.HTTPResponse | urllib.error.URLError
    encoding: Optional[str]
    reason: str
    cookies: http.cookiejar.CookieJar
    elapsed: datetime.timedelta
    request: urllib.request.Request

    # noinspection PyShadowingNames
    def __init__(self, request: urllib.request.Request,
                 raw: urllib.response.addinfourl | http.client.HTTPResponse | urllib.error.URLError):
        self._next = getattr(request, 'next', None)
        if isinstance(raw, urllib.error.URLError):
            status = getattr(raw, 'status', Status.IM_A_TEAPOT)
            try:
                self.status_code = Status(status)
            except ValueError:
                self.status_code = status
        elif isinstance(raw, urllib.response.addinfourl):
            self.status_code = Status.OK
        else:
            self.status_code = Status(raw.status)
        self.headers = getattr(raw, 'headers', http.client.HTTPMessage())
        self.raw = raw
        self.url = getattr(raw, 'url', '')
        self.encoding = None
        self.reason = getattr(raw, 'reason', '')
        self.cookies = http.cookiejar.CookieJar()
        if isinstance(raw, http.client.HTTPResponse):
            self.cookies.extract_cookies(raw, request)
        self.elapsed = getattr(raw, 'elapsed', datetime.timedelta())
        self.request = request
        self._decoder = Decoder.get(self.headers.get(Header.CONTENT_ENCODING))

    def __bool__(self) -> bool:
        return self.ok

    def __repr__(self) -> str:
        return f'<{type(self).__name__}: {self.status_code!r}>'

    def __iter__(self) -> Iterator[bytes]:
        return self.iter_content(128)

    def __enter__(self) -> Response:
        return self

    def __exit__(self, *_, **__):
        self.close()

    @property
    def ok(self) -> bool:
        try:
            self.raise_for_status()
        except urllib.error.HTTPError:
            return False
        else:
            return True

    @property
    def is_redirect(self) -> bool:
        return Header.LOCATION in self.headers and self.status_code in _STATUS_REDIRECT

    @property
    def is_permanent_redirect(self) -> bool:
        return self.is_redirect and self.status_code in _STATUS_REDIRECT_PERMANENT

    @property
    def next(self) -> Optional[urllib.request.Request]:
        if self.is_redirect:
            return self._next

    @property
    def apparent_encoding(self) -> str:
        return 'utf-8'

    def iter_content(self, chunk_size: int = 1) -> Iterator[bytes]:
        while chunk := self.read(chunk_size):
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
        return json_.loads(self.text)

    @property
    def links(self):
        links = {}
        if (header := _caseless.get(self.headers, Header.LINK)) is not None:
            for url, params in get_links(header, self.url).items():
                links[params.get('rel', url)] = {'url': url, **params}
        return links

    def raise_for_status(self) -> Optional[NoReturn]:
        if 400 <= self.status_code < 600:
            raise urllib.error.HTTPError(
                self.url, self.status_code, self.reason, self.headers, self.raw)

    def close(self):
        self.raw.close()

    def read(self, amt: Optional[int] = None, decode_content: bool = True) -> bytes:
        data = self.raw.read(amt)
        if decode_content and self._decoder is not None:
            data = self._decoder.decompress(data)
            if not data:
                data = self._decoder.flush()
        return data


class Session:
    _tredirect_ = _HTTPRedirectHandler
    _thttp_ = _HTTPHandler
    _thttps_ = _HTTPSHandler
    _tcookie_ = _HTTPCookieProcessor
    _shared_handlers_ = (
        urllib.request.HTTPErrorProcessor(), _HTTPDefaultErrorHandler(), _ProxyHandler(),
        urllib.request.UnknownHandler(), urllib.request.FileHandler(), urllib.request.FTPHandler(),
        _HTTPBasicAuthHandler(), _HTTPBearerAuthHandler(), _HTTPDigestAuthHandler())

    _attrs = ('headers', 'auth', 'proxies', 'params', 'stream', 'verify', 'trust_env', 'cookies', 'timeout',
              'allow_redirects', 'force_auth', 'max_repeats', 'max_redirections', 'http_debug_level', 'unredirected_hdrs')

    def __init__(self, headers: Optional[_THeaders] = None, auth: Optional[_TAuth] = None,
                 proxies: Optional[_TProxies] = None, params: Optional[_TParams] = None, stream: Optional[bool] = None,
                 verify: Optional[_TVerify] = None, trust_env: bool = True, cookies: Optional[_TCookies] = None,
                 timeout: Optional[float] = None, allow_redirects: Optional[bool] = None, force_auth: Optional[bool] = None,
                 max_repeats: Optional[int] = None, max_redirections: Optional[int] = None,
                 http_debug_level: Optional[bool | int] = None, unredirected_hdrs: Optional[_THeaders] = None):
        self._redirect_handler = self._tredirect_()
        self._http_handler = self._thttp_()
        self._https_handler = self._thttps_()
        self._cookie_handler = self._tcookie_()

        if headers is None:
            headers = default_headers()
        self.headers = headers
        self.auth = auth
        self.proxies = proxies
        self.params = params
        self.stream = stream
        if verify is None:
            verify = default_verify()
        self.verify = verify
        self.trust_env = trust_env  # TODO extend
        if cookies is not None:
            self.cookies = cookies
        self.timeout = timeout
        self.allow_redirects = allow_redirects
        self.force_auth = force_auth
        if max_repeats is not None:
            self.max_repeats = max_repeats
        if max_redirections is not None:
            self.max_redirections = max_redirections
        if http_debug_level is not None:
            self.http_debug_level = http_debug_level
        self.unredirected_hdrs = unredirected_hdrs

        self._opener = _OpenerDirector(*self._shared_handlers_, self._redirect_handler,
                                       self._http_handler, self._https_handler, self._cookie_handler)

    def __repr__(self):
        attrs = (f'{name}={val}' for name in self._attrs
                 if (val := getattr(self, name)) is not None)
        return f'<{type(self).__name__}: <{", ".join(attrs)}>>'

    @property
    def headers(self) -> Optional[dict[str, str]]:
        return self._headers

    @headers.setter
    def headers(self, headers: Optional[_THeaders]):
        if headers is not None:
            headers = encode_headers(headers)
        self._headers = headers

    @property
    def auth(self) -> Optional[urllib.request.HTTPBasicAuthHandler]:
        return self._auth

    @auth.setter
    def auth(self, auth: Optional[_TAuth]):
        if auth is not None:
            auth = encode_auth(auth)
        self._auth = auth

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
        return self._cookie_handler.cookiejar

    @cookies.setter
    def cookies(self, cookies: Optional[_TCookies]):
        if cookies is not None:
            cookies = encode_cookies(cookies)
        self._cookie_handler.cookiejar = cookies

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
    def http_debug_level(self) -> int:
        # noinspection PyUnresolvedReferences,PyProtectedMember
        return self._http_handler._debuglevel

    @http_debug_level.setter
    def http_debug_level(self, http_debug_level: bool | int):
        self._http_handler._debuglevel = self._https_handler._debuglevel = int(http_debug_level)

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
        auths = []
        if self.auth is not None:
            auths.append(self.auth)
        if request.auth is not None:
            auths.append(request.auth)
        request.auth = merge_auths(*auths) if auths else None
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

    def request(self, method: Optional[_TMethod], url: _TURL,
                params: Optional[_TParams] = None, data: Optional[_TData] = None, headers: Optional[_THeaders] = None,
                cookies: Optional[_TCookies] = None, files: Optional[_TFiles] = None, auth: Optional[_TAuth] = None,
                timeout: Optional[float] = None, allow_redirects: Optional[bool] = None, proxies: Optional[_TProxies] = None,
                stream: Optional[bool] = None, verify: Optional[_TVerify] = None, json: Optional[_TJSON] = None,
                force_auth: Optional[bool] = None, unredirected_hdrs: Optional[_THeaders] = None) -> Response:
        request_prep = self.prepare_request(Request(method, url, headers, files, data, params,
                                                    auth, cookies, json, unredirected_hdrs))
        return self.send(request_prep, **self.merge_environment_settings(
            proxies, stream, verify, timeout, allow_redirects, force_auth))

    def get(self, url: _TURL, params: Optional[_TParams] = None, data: Optional[_TData] = None,
            headers: Optional[_THeaders] = None, cookies: Optional[_TCookies] = None, files: Optional[_TFiles] = None,
            auth: Optional[_TAuth] = None, timeout: Optional[float] = None, allow_redirects: Optional[bool] = None,
            proxies: Optional[_TProxies] = None, stream: Optional[bool] = None, verify: Optional[_TVerify] = None,
            json: Optional[_TJSON] = None, force_auth: Optional[bool] = None, unredirected_hdrs: Optional[_THeaders] = None) -> Response:
        return self.request(Method.GET, url, params, data, headers, cookies, files, auth,
                            timeout, allow_redirects, proxies, stream, verify, json, force_auth, unredirected_hdrs)

    def options(self, url: _TURL, params: Optional[_TParams] = None, data: Optional[_TData] = None,
                headers: Optional[_THeaders] = None, cookies: Optional[_TCookies] = None, files: Optional[_TFiles] = None,
                auth: Optional[_TAuth] = None, timeout: Optional[float] = None, allow_redirects: Optional[bool] = None,
                proxies: Optional[_TProxies] = None, stream: Optional[bool] = None, verify: Optional[_TVerify] = None,
                json: Optional[_TJSON] = None, force_auth: Optional[bool] = None, unredirected_hdrs: Optional[_THeaders] = None) -> Response:
        return self.request(Method.OPTIONS, url, params, data, headers, cookies, files, auth,
                            timeout, allow_redirects, proxies, stream, verify, json, force_auth, unredirected_hdrs)

    def head(self, url: _TURL, params: Optional[_TParams] = None, data: Optional[_TData] = None,
             headers: Optional[_THeaders] = None, cookies: Optional[_TCookies] = None, files: Optional[_TFiles] = None,
             auth: Optional[_TAuth] = None, timeout: Optional[float] = None, allow_redirects: Optional[bool] = None,
             proxies: Optional[_TProxies] = None, stream: Optional[bool] = None, verify: Optional[_TVerify] = None,
             json: Optional[_TJSON] = None, force_auth: Optional[bool] = None, unredirected_hdrs: Optional[_THeaders] = None) -> Response:
        return self.request(Method.HEAD, url, params, data, headers, cookies, files, auth,
                            timeout, allow_redirects, proxies, stream, verify, json, force_auth, unredirected_hdrs)

    def post(self, url: _TURL, params: Optional[_TParams] = None, data: Optional[_TData] = None,
             headers: Optional[_THeaders] = None, cookies: Optional[_TCookies] = None, files: Optional[_TFiles] = None,
             auth: Optional[_TAuth] = None, timeout: Optional[float] = None, allow_redirects: Optional[bool] = None,
             proxies: Optional[_TProxies] = None, stream: Optional[bool] = None, verify: Optional[_TVerify] = None,
             json: Optional[_TJSON] = None, force_auth: Optional[bool] = None, unredirected_hdrs: Optional[_THeaders] = None) -> Response:
        return self.request(Method.POST, url, params, data, headers, cookies, files, auth,
                            timeout, allow_redirects, proxies, stream, verify, json, force_auth, unredirected_hdrs)

    def put(self, url: _TURL, params: Optional[_TParams] = None, data: Optional[_TData] = None,
            headers: Optional[_THeaders] = None, cookies: Optional[_TCookies] = None, files: Optional[_TFiles] = None,
            auth: Optional[_TAuth] = None, timeout: Optional[float] = None, allow_redirects: Optional[bool] = None,
            proxies: Optional[_TProxies] = None, stream: Optional[bool] = None, verify: Optional[_TVerify] = None,
            json: Optional[_TJSON] = None, force_auth: Optional[bool] = None, unredirected_hdrs: Optional[_THeaders] = None) -> Response:
        return self.request(Method.PUT, url, params, data, headers, cookies, files, auth,
                            timeout, allow_redirects, proxies, stream, verify, json, force_auth, unredirected_hdrs)

    def patch(self, url: _TURL, params: Optional[_TParams] = None, data: Optional[_TData] = None,
              headers: Optional[_THeaders] = None, cookies: Optional[_TCookies] = None, files: Optional[_TFiles] = None,
              auth: Optional[_TAuth] = None, timeout: Optional[float] = None, allow_redirects: Optional[bool] = None,
              proxies: Optional[_TProxies] = None, stream: Optional[bool] = None, verify: Optional[_TVerify] = None,
              json: Optional[_TJSON] = None, force_auth: Optional[bool] = None, unredirected_hdrs: Optional[_THeaders] = None) -> Response:
        return self.request(Method.PATCH, url, params, data, headers, cookies, files, auth,
                            timeout, allow_redirects, proxies, stream, verify, json, force_auth, unredirected_hdrs)

    def delete(self, url: _TURL, params: Optional[_TParams] = None, data: Optional[_TData] = None,
               headers: Optional[_THeaders] = None, cookies: Optional[_TCookies] = None, files: Optional[_TFiles] = None,
               auth: Optional[_TAuth] = None, timeout: Optional[float] = None, allow_redirects: Optional[bool] = None,
               proxies: Optional[_TProxies] = None, stream: Optional[bool] = None, verify: Optional[_TVerify] = None,
               json: Optional[_TJSON] = None, force_auth: Optional[bool] = None, unredirected_hdrs: Optional[_THeaders] = None) -> Response:
        return self.request(Method.DELETE, url, params, data, headers, cookies, files, auth,
                            timeout, allow_redirects, proxies, stream, verify, json, force_auth, unredirected_hdrs)

    # noinspection PyShadowingNames
    def send(self, request: urllib.request.Request, proxies: Optional[_TProxies] = None,
             stream: Optional[bool] = None, verify: Optional[_TVerify] = None, timeout: Optional[float] = None,
             allow_redirects: Optional[bool] = None, force_auth: Optional[bool] = None) -> Response:
        if proxies is not None:
            proxies = encode_proxies(proxies)
        if verify is not None:
            verify = encode_verify(verify)
        if timeout is not None:
            request.timeout = timeout
        _request_set_private(request, getattr(request, '_auths', None), getattr(
            request, '_cookies', None), proxies, stream, verify, allow_redirects, force_auth)
        try:
            response = self._opener.open_ex(request)
        except urllib.error.URLError as exc:  # TODO better handling
            response = Response(request, exc)
        else:
            if stream is not True:
                _ = response.content
        return response

    def merge_environment_settings(self, proxies: Optional[_TProxies] = None, stream: Optional[bool] = None,
                                   verify: Optional[_TVerify] = None, timeout: Optional[float] = None,
                                   allow_redirects: Optional[bool] = None, force_auth: Optional[bool] = None) -> dict[str, Any]:
        if proxies is not None:
            proxies = encode_proxies(proxies)
        if self.trust_env:
            proxies = _merge_setting(proxies, urllib.request.getproxies())
        return {
            'proxies': _merge_setting(proxies, self.proxies),
            'stream': _merge_setting(stream, self.stream),
            'verify': _merge_setting(verify, self.verify),
            'timeout': _merge_setting(timeout, self.timeout),
            'allow_redirects': _merge_setting(allow_redirects, self.allow_redirects),
            'force_auth': _merge_setting(force_auth, self.force_auth)}


def _bytes(o: bytes | str, encoding: str = 'latin1') -> bytes:
    return o.encode(encoding) if isinstance(o, str) else o


def _str(o: bytes | str, encoding: str = 'latin1') -> str:
    return o.decode(encoding) if isinstance(o, bytes) else o


# noinspection PyShadowingNames
def _request_set_private(request: urllib.request.Request, auths: Optional[AuthManager],
                         cookies: Optional[http.cookiejar.CookieJar], proxies: Optional[_TProxies],
                         stream: Optional[bool], verify: Optional[_TVerify],
                         allow_redirects: Optional[bool], force_auth: Optional[bool]):
    request._auths = auths
    request._cookies = cookies
    request._proxies = proxies
    request._stream = stream
    request._verify = verify
    request._allow_redirects = allow_redirects
    request._force_auth = force_auth


def _merge_setting(request_setting, session_setting) -> Any:
    if session_setting is None:
        return request_setting
    elif request_setting is None:
        return session_setting
    elif isinstance(session_setting, Mapping):
        return {**session_setting, **request_setting}
    else:
        return request_setting


def is_path(url: str) -> bool:
    return _FILE_SCHEME == urllib.parse.urlsplit(url).scheme


def from_path(path: str) -> str:
    # noinspection PyArgumentList
    return urllib.parse.SplitResult(_FILE_SCHEME, '', urllib.request.pathname2url(path), '', '').geturl()


def strip_url(url: str, *, userinfo: bool = True, path: bool = False,
              query: bool = True, fragment: bool = True) -> str:
    components = urllib.parse.urlsplit(url)
    replace = {}
    if userinfo:
        replace['netloc'] = components.hostname
    if path:
        replace['path'] = ''
    if query:
        replace['query'] = ''
    if fragment:
        replace['fragment'] = ''
    # noinspection PyProtectedMember
    return components._replace(**replace).geturl()


def split_url(url: str) -> tuple[str, ...]:
    return strip_url(url, path=True), *(filter(
        None, urllib.parse.urlsplit(url).path.split('/')))


def join_url(base: str, *paths: str) -> str:
    if not base.endswith('/'):
        base += '/'
    for path in paths:
        if path:
            base = urllib.parse.urljoin(base, path) + '/'
    return base[:-1]


def extract_params(url: AnyStr) -> dict[AnyStr, list[AnyStr]]:
    return urllib.parse.parse_qs(urllib.parse.urlsplit(url).query, True)


# noinspection PyShadowingNames
def extract_cookies(cookies: _TCookies,
                    request: Optional[urllib.request.Request] = None) -> list[http.cookiejar.Cookie]:
    cookies = encode_cookies(cookies)
    # noinspection PyUnresolvedReferences,PyProtectedMember
    return list(cookies) if request is None else cookies._cookies_for_request(request)


def extract_auth(url: _TURL) -> Optional[BasicAuth]:
    # noinspection PyUnresolvedReferences,PyProtectedMember
    username, password = urllib.parse.urlsplit(url)._userinfo
    if username is not None or password is not None:
        username = '' if username is None else urllib.parse.unquote(username)
        password = '' if password is None else urllib.parse.unquote(password)
        return BasicAuth(username, password)


def get_header_list(*headers: str) -> Iterator[tuple[str, Optional[str]]]:
    # noinspection PyUnresolvedReferences
    for words in http.cookiejar.split_header_words(headers):
        yield from words


def get_params(params: _TParams) -> dict[bytes | str, list[bytes | str]]:
    if isinstance(params, (bytes, str)):
        start = b'?' if isinstance(params, bytes) else '?'
        if start not in params:
            params = start + params
        return extract_params(params)
    else:
        query = {}
        for key, val in params.items() if isinstance(params, Mapping) else params:
            if val is not None:
                if key not in query:
                    query[key] = []
                if isinstance(val, (bytes, str)):
                    query[key].append(val)
                else:
                    query[key].extend(val)
        return query


def get_headers(keep_alive: Optional[bool] = True, accept_encoding: bool | str | Iterable[str] = True,
                user_agent: bool | str = True, basic_auth: Optional[tuple[bytes | str, bytes | str]] = None,
                proxy_basic_auth: Optional[tuple[bytes | str, bytes | str]] = None, disable_cache: bool = False) -> dict[str, str]:
    headers = {}
    if keep_alive is not None:
        headers[Header.CONNECTION] = 'keep-alive' if keep_alive else 'close'
    if accept_encoding:
        if accept_encoding is True:
            accept_encoding = default_accept_encoding()
        elif not isinstance(accept_encoding, str):
            accept_encoding = ','.join(accept_encoding)
        headers[Header.ACCEPT_ENCODING] = accept_encoding
    if user_agent:
        if user_agent is True:
            user_agent = default_user_agent()
        headers[Header.USER_AGENT] = user_agent
    if basic_auth is not None:
        headers[Header.AUTHORIZATION] = BasicAuth(*basic_auth).encode()
    if proxy_basic_auth is not None:
        headers[Header.PROXY_AUTHORIZATION] = BasicAuth(*proxy_basic_auth).encode()
    if disable_cache:
        headers[Header.CACHE_CONTROL] = 'no-cache'
    return headers


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
            expires = datetime.datetime.strptime(
                morsel['expires'], '%a, %d-%b-%Y %H:%M:%S GMT').timestamp()
        else:
            expires = None
        return get_cookie(morsel.key, morsel.value, morsel['version'], None, morsel['domain'], morsel['path'],
                          bool(morsel['secure']), expires, False, morsel['comment'], None, None, False)
    else:
        if rest is None:
            rest = {'HttpOnly': ''}
        port_specified = bool(port)
        domain_specified = bool(domain)
        domain_initial_dot = domain.startswith('.')
        path_specified = bool(path)
        return http.cookiejar.Cookie(
            version, morsel_or_name, value, port, port_specified, domain, domain_specified, domain_initial_dot,
            path, path_specified, secure, expires, discard, comment, comment_url, rest, rfc2109)


def get_chals(header: str) -> dict[str, list[dict[str, list[Optional[str]]]]]:
    chals = {}
    params = None
    for key, val in get_header_list(header):
        if val is None:
            if key not in chals:
                chals[key] = []
            chals[key].append(params := {})
        else:
            if key not in params:
                params[key] = []
            params[key].extend(dict(get_header_list(val)))
    return chals


def get_links(header: str, url: str = '') -> dict[str, dict[str, str]]:
    links = {}
    for match in _RE_LINKS.finditer(header):
        groups = match.groups()
        links[join_url(url, groups[0])] = dict(get_header_list(groups[1]))
    return links


def merge_auths(*auths: _TAuth, man: Optional[AuthManager] = None) -> AuthManager:
    if man is None:
        man = AuthManager()
    for auth in auths:
        if isinstance(auth, AuthManager):
            man.passwd.update(auth.passwd)
        else:
            if isinstance(auth, (bytes, str)):
                auth = BearerAuth(auth)
            elif not isinstance(auth, Auth):
                auth = BasicAuth(*auth)
            man.add_auth(auth)
    return man


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
    if isinstance(method, Method):
        method = method.value
    method = method.upper()
    if request is not None:
        request.method = method
    return method


def _upper(match: re.Match) -> bytes | str:
    return match[0].upper()


def _encode_component(component: str, valid: bytes) -> str:
    component, count_encoded = _RE_ENCODED.subn(_upper, component)
    if count_encoded == component.count('%'):
        valid += b'%'
    return urllib.parse.quote_plus(component, safe=valid)


# noinspection PyShadowingNames
def encode_url(url: _TURL, request: Optional[urllib.request.Request] = None) -> str:
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
def encode_params(url: _TURL, params: Optional[_TParams] = None,
                  request: Optional[urllib.request.Request] = None) -> bytes | str:
    if params is not None:
        components = urllib.parse.urlsplit(url)
        query = urllib.parse.parse_qs(components.query, True)
        query.update(get_params(params))
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
        add_header = request.add_unredirected_header if unredirected else request.add_header
        for header in headers.items():
            add_header(*header)
    return headers


# noinspection PyShadowingNames
def encode_cookies(cookies: _TCookies,  # TODO lock simple cookies to host + same with auth (?)
                   request: Optional[urllib.request.Request] = None) -> http.cookiejar.CookieJar:
    if not isinstance(cookies, http.cookiejar.CookieJar):
        if isinstance(cookies, Mapping):
            cookies = cookies.items()
        cookies = merge_cookies(*cookies)
    if request is not None:
        request._cookies = cookies
    return cookies


def _encode_params(params: Optional[bytes | str | Mapping]) -> str:
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
                                 _bytes(val)) for val in vals)
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
                    # noinspection PyTypeChecker
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
        data = b'\r\n'.join(lines)
    elif data is not None:
        mime = 'application/x-www-form-urlencoded'
        data = _encode_params(data).encode()
    elif json is not None:
        mime = 'application/json'
        data = json_.dumps(json, allow_nan=False, separators=(',', ':')).encode()
    else:
        mime = None
        data = None
    if request is not None:
        request.add_header(Header.CONTENT_TYPE, mime)
        request.data = data
    return mime, data


# noinspection PyShadowingNames
def encode_auth(auth: _TAuth, request: Optional[urllib.request.Request] = None) -> AuthManager:
    if isinstance(auth, (bytes, str, Auth, AuthManager)):
        auth = auth,
    elif isinstance(auth, tuple) and len(auth) == 2:
        auth = auth,
    return encode_auths(auth, request)


# noinspection PyShadowingNames
def encode_auths(auths: _TAuths, request: Optional[urllib.request.Request] = None) -> AuthManager:
    if not isinstance(auths, AuthManager):
        man = AuthManager()
        if isinstance(auths, Mapping):
            for url, auth in auths.items():
                man.add_auth(auth, url)
        else:
            merge_auths(*auths, man=man)
        auths = man
    if request is not None:
        request._auths = auths
    return auths


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


def request(method: Optional[_TMethod], url: _TURL, params: Optional[_TParams] = None, data: Optional[_TData] = None,
            headers: Optional[_THeaders] = None, cookies: Optional[_TCookies] = None, files: Optional[_TFiles] = None,
            auth: Optional[_TAuth] = None, timeout: Optional[float] = None, allow_redirects: bool = True,
            proxies: Optional[_TProxies] = None, stream: bool = True, verify: _TVerify = True, json: Optional[_TJSON] = None,
            force_auth: Optional[bool] = None, unredirected_hdrs: Optional[_THeaders] = None) -> Response:
    return Session().request(method, url, params, data, headers, cookies, files, auth, timeout,
                             allow_redirects, proxies, stream, verify, json, force_auth, unredirected_hdrs)


def get(url: _TURL, params: Optional[_TParams] = None, data: Optional[_TData] = None, headers: Optional[_THeaders] = None,
        cookies: Optional[_TCookies] = None, files: Optional[_TFiles] = None, auth: Optional[_TAuth] = None,
        timeout: Optional[float] = None, allow_redirects: bool = True, proxies: Optional[_TProxies] = None,
        stream: bool = True, verify: _TVerify = True, json: Optional[_TJSON] = None) -> Response:
    return request(Method.GET, url, params, data, headers, cookies, files,
                   auth, timeout, allow_redirects, proxies, stream, verify, json)


def options(url: _TURL, params: Optional[_TParams] = None, data: Optional[_TData] = None, headers: Optional[_THeaders] = None,
            cookies: Optional[_TCookies] = None, files: Optional[_TFiles] = None, auth: Optional[_TAuth] = None,
            timeout: Optional[float] = None, allow_redirects: bool = False, proxies: Optional[_TProxies] = None,
            stream: bool = True, verify: _TVerify = True, json: Optional[_TJSON] = None) -> Response:
    return request(Method.OPTIONS, url, params, data, headers, cookies,
                   files, auth, timeout, allow_redirects, proxies, stream, verify, json)


def head(url: _TURL, params: Optional[_TParams] = None, data: Optional[_TData] = None, headers: Optional[_THeaders] = None,
         cookies: Optional[_TCookies] = None, files: Optional[_TFiles] = None, auth: Optional[_TAuth] = None,
         timeout: Optional[float] = None, allow_redirects: bool = False, proxies: Optional[_TProxies] = None,
         stream: bool = True, verify: _TVerify = True, json: Optional[_TJSON] = None) -> Response:
    return request(Method.HEAD, url, params, data, headers, cookies, files,
                   auth, timeout, allow_redirects, proxies, stream, verify, json)


def post(url: _TURL, data: Optional[_TData] = None, json: Optional[_TJSON] = None, params: Optional[_TParams] = None,
         headers: Optional[_THeaders] = None, cookies: Optional[_TCookies] = None, files: Optional[_TFiles] = None,
         auth: Optional[_TAuth] = None, timeout: Optional[float] = None, allow_redirects: bool = True,
         proxies: Optional[_TProxies] = None, stream: bool = True, verify: _TVerify = True) -> Response:
    return request(Method.POST, url, params, data, headers, cookies, files,
                   auth, timeout, allow_redirects, proxies, stream, verify, json)


def put(url: _TURL, data: Optional[_TData] = None, params: Optional[_TParams] = None, headers: Optional[_THeaders] = None,
        cookies: Optional[_TCookies] = None, files: Optional[_TFiles] = None, auth: Optional[_TAuth] = None,
        timeout: Optional[float] = None, allow_redirects: bool = True, proxies: Optional[_TProxies] = None,
        stream: bool = True, verify: _TVerify = True, json: Optional[_TJSON] = None) -> Response:
    return request(Method.PUT, url, params, data, headers, cookies, files,
                   auth, timeout, allow_redirects, proxies, stream, verify, json)


def patch(url: _TURL, data: Optional[_TData] = None, params: Optional[_TParams] = None, headers: Optional[_THeaders] = None,
          cookies: Optional[_TCookies] = None, files: Optional[_TFiles] = None, auth: Optional[_TAuth] = None,
          timeout: Optional[float] = None, allow_redirects: bool = True, proxies: Optional[_TProxies] = None,
          stream: bool = True, verify: _TVerify = True, json: Optional[_TJSON] = None) -> Response:
    return request(Method.PATCH, url, params, data, headers, cookies, files,
                   auth, timeout, allow_redirects, proxies, stream, verify, json)


def delete(url: _TURL, params: Optional[_TParams] = None, data: Optional[_TData] = None, headers: Optional[_THeaders] = None,
           cookies: Optional[_TCookies] = None, files: Optional[_TFiles] = None, auth: Optional[_TAuth] = None,
           timeout: Optional[float] = None, allow_redirects: bool = True, proxies: Optional[_TProxies] = None,
           stream: bool = True, verify: _TVerify = True, json: Optional[_TJSON] = None) -> Response:
    return request(Method.DELETE, url, params, data, headers, cookies, files,
                   auth, timeout, allow_redirects, proxies, stream, verify, json)


def _get_response(url_or_request_or_response: _TURL | Request | Response, method: _TMethod) -> Response:
    if not isinstance(url_or_request_or_response, Response):
        if not isinstance(url_or_request_or_response, Request):
            url_or_request_or_response = Request(method, url_or_request_or_response)
        url_or_request_or_response = request(**dataclasses.asdict(url_or_request_or_response))
    return url_or_request_or_response


def get_size(url_or_request_or_response: _TURL | Request | Response) -> int:
    response = _get_response(url_or_request_or_response, Method.HEAD)
    return int(response.headers.get(
        Header.CONTENT_LENGTH, RETRIEVE_UNKNOWN_SIZE)) if response else RETRIEVE_UNKNOWN_SIZE


def get_filename(url_or_request_or_response: _TURL | Request | Response) -> str:
    response = _get_response(url_or_request_or_response, Method.HEAD)
    return dict(get_header_list(response.headers.get(
        Header.CONTENT_DISPOSITION, ''))).get('filename', '') if response else ''


def retrieve(url_or_request_or_response: _TURL | Request | Response, path: bytes | str,
             size: int = RETRIEVE_UNKNOWN_SIZE, chunk_size: Optional[int] = None,
             chunk_count: Optional[int] = None, response_callback: Callable[[Response], bool] = bool,
             query_callback: Optional[Callable[[int, int], bool]] = None) -> bool:
    response = _get_response(url_or_request_or_response, Method.GET)
    if response_callback(response):
        if size == RETRIEVE_UNKNOWN_SIZE:
            size = get_size(response)
        if chunk_size is None:
            chunk_size = size // (chunk_count or sys.maxsize)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'wb') as file:
            written = 0
            for chunk in response.iter_content(max(chunk_size, _RETRIEVE_CHUNK_SIZE)):
                written += file.write(chunk)
                if query_callback is not None and not query_callback(written, size):
                    return False
        return size == RETRIEVE_UNKNOWN_SIZE or size == os.path.getsize(path)
    else:
        return False
