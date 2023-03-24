__version__ = '0.1.4'

import base64
import contextlib
import http.client
import io
import itertools
import json as json_
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import urllib.response
import uuid
from typing import Any, AnyStr, BinaryIO, Callable, IO, Iterator, Iterable, Mapping, Optional

_TJSON = int | bool | float | str | tuple | list | dict
_TParams = Mapping[AnyStr, Optional[AnyStr | Iterable[AnyStr]]]
_THeaders = Mapping[str, str]
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
_NORMALIZABLE_SCHEMES = '', _HTTP_SCHEME, _HTTPS_SCHEME
_RE_ENCODED = re.compile(r"%[a-fA-F0-9]{2}")
_OPENER_DEFAULT = urllib.request.build_opener()
_OPENER_NO_REDIRECT = urllib.request.build_opener(_HTTPRedirectHandler)

FLAG_REREAD_RESPONSE = True
UNRESERVED_CHARS = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~'
SUB_DELIM_CHARS = b"!$&'()*+,;"
USERINFO_CHARS = UNRESERVED_CHARS + SUB_DELIM_CHARS + b':'
PATH_CHARS = USERINFO_CHARS + b'@/'
QUERY_CHARS = UNRESERVED_CHARS + PATH_CHARS + b'?'
FRAGMENT_CHARS = QUERY_CHARS


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


class MIMEType:
    AAC = 'audio/aac'
    ABW = 'application/x-abiword'
    ARC = 'application/x-freearc'
    AVIF = 'image/avif'
    AVI = 'video/x-msvideo'
    AZW = 'application/vnd.amazon.ebook'
    BIN = 'application/octet-stream'
    BMP = 'image/bmp'
    BZ = 'application/x-bzip'
    BZ2 = 'application/x-bzip2'
    CDA = 'application/x-cdf'
    CSH = 'application/x-csh'
    CSS = 'text/css'
    CSV = 'text/csv'
    DOC = 'application/msword'
    DOCX = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    EOT = 'application/vnd.ms-fontobject'
    EPUB = 'application/epub+zip'
    GZ = 'application/gzip'
    GIF = 'image/gif'
    HTM = HTML = 'text/html'
    ICO = 'image/vnd.microsoft.icon'
    ICS = 'text/calendar'
    JAR = 'application/java-archive'
    JPEG = JPG = 'image/jpeg'
    JS = 'text/javascript'
    JSONLD = 'application/ld+json'
    MID = MIDI = 'audio/midi'
    MJS = 'text/javascript'
    MP3 = 'audio/mpeg'
    MP4 = 'video/mp4'
    MPEG = 'video/mpeg'
    MPKG = 'application/vnd.apple.installer+xml'
    ODP = 'application/vnd.oasis.opendocument.presentation'
    ODS = 'application/vnd.oasis.opendocument.spreadsheet'
    ODT = 'application/vnd.oasis.opendocument.text'
    OGA = 'audio/ogg'
    OGV = 'video/ogg'
    OGX = 'application/ogg'
    OPUS = 'audio/opus'
    OTF = 'font/otf'
    PNG = 'image/png'
    PDF = 'application/pdf'
    PHP = 'application/x-httpd-php'
    PPT = 'application/vnd.ms-powerpoint'
    PPTX = 'application/vnd.openxmlformats-officedocument.presentationml.presentation'
    RAR = 'application/vnd.rar'
    RTF = 'application/rtf'
    SH = 'application/x-sh'
    SVG = 'image/svg+xml'
    TAR = 'application/x-tar'
    TIF = TIFF = 'image/tiff'
    TS = 'video/mp2t'
    TTF = 'font/ttf'
    TXT = 'text/plain'
    VSD = 'application/vnd.visio'
    WAV = 'audio/wav'
    WEBA = 'audio/webm'
    WEBM = 'video/webm'
    WEBP = 'image/webp'
    WOFF = 'font/woff'
    WOFF2 = 'font/woff2'
    XHTML = 'application/xhtml+xml'
    XLS = 'application/vnd.ms-excel'
    XLSX = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    XML = 'application/xml'
    XUL = 'application/vnd.mozilla.xul+xml'
    ZIP = 'application/zip'
    _3GP = 'video/3gpp'
    _3G2 = 'video/3gpp2'
    _7Z = 'application/x-7z-compressed'
    FORM = 'application/x-www-form-urlencoded'
    JSON = 'application/json'


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


def is_path(url: AnyStr) -> bool:
    return _FILE_SCHEME == _str(urllib.parse.urlsplit(url).scheme)


def from_path(path: str) -> str:
    # noinspection PyArgumentList
    return urllib.parse.SplitResult(_FILE_SCHEME, '', urllib.request.pathname2url(path), '', '').geturl()


def strip(url: str) -> str:
    return urllib.parse.urlsplit(url)._replace(query='', fragment='').geturl()


def join(base: str, *paths: str) -> str:
    if not base.endswith('/'):
        base += '/'
    for path in paths:
        if path:
            base = f'{urllib.parse.urljoin(base, path)}/'
    return base[:-1]


def get_params(url: str) -> dict[str, list[str]]:
    return urllib.parse.parse_qs(urllib.parse.urlsplit(url).query)


def _upper_encoded(match: re.Match) -> str:
    return match.group(0).upper()


def _encode_component(component: str, valid: bytes) -> str:
    component, count_encoded = _RE_ENCODED.subn(_upper_encoded, component)
    component_ = component.encode(errors='surrogatepass')
    pc_encoded = count_encoded == component_.count(37)
    encoded = b''
    for ord_ in component_:
        if (pc_encoded and ord_ == 37) or ord_ in valid:
            encoded += chr(ord_).encode()
        else:
            encoded += b'%' + hex(ord_)[2:].encode().zfill(2).upper()
    return encoded.decode()


def encode_url(url: AnyStr) -> str:
    components = urllib.parse.urlsplit(_str(url))
    if components.scheme in _NORMALIZABLE_SCHEMES:
        if components.path:
            components = components._replace(
                path=_encode_component(components.path, PATH_CHARS))
        if components.query:
            components = components._replace(
                query=_encode_component(components.query, QUERY_CHARS))
        if components.fragment:
            components = components._replace(
                fragment=_encode_component(components.fragment, FRAGMENT_CHARS))
    return components.geturl()


def encode_params(params: Optional[AnyStr | Mapping]) -> str:
    if params is None:
        return ''
    elif isinstance(params, (bytes, str)):
        return _str(params)
    else:
        return urllib.parse.urlencode(params, True)


def encode_data(fields: Optional[_TParams] = None, files: Optional[_TFiles] = None,
                json: Optional[_TJSON] = None) -> tuple[str, bytes]:
    if files is not None:  # TODO escape quotes
        data = []
        if fields is not None:
            for name, vals in fields.items():
                if vals is not None:
                    if isinstance(vals, (bytes, str)):
                        vals = vals,
                    data.extend(({Header.CONTENT_DISPOSITION: f'form-data; name="{_str(name)}"'},
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
            data.append((headers, (open(val, "rb") if isinstance(
                val, bytes | str) else val).read()))
        lines = []
        boundary = uuid.uuid4().hex
        for headers, val in data:
            lines.append(f'--{boundary}'.encode())
            lines.extend(f'{key}: {val}'.encode()
                         for key, val in headers.items() if val is not None)
            lines.append(b'')
            lines.append(val)
        lines.append(f'--{boundary}--'.encode())
        lines.append(b'')
        return f'multipart/form-data; boundary={boundary}', _CRLF.encode().join(lines)
    elif fields is not None:
        return MIMEType.FORM, encode_params(fields).encode()
    elif json is not None:
        return MIMEType.JSON, json_.dumps(json, allow_nan=False).encode()


def extend_param(url: AnyStr, params: Optional[_TParams] = None) -> AnyStr:
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
    return components._replace(query=_str(encode_params(query))).geturl()


def request(method: str | http.HTTPMethod, url: AnyStr, data: Optional[_TParams] = None, json: Optional[_TJSON] = None,
            params: Optional[_TParams] = None, headers: Optional[_THeaders] = None,
            files: Optional[_TFiles] = None, auth: Optional[_TAuth] = None,
            timeout: Optional[float] = None, allow_redirects: bool = True, stream: bool = True) -> Response:
    if params is not None:
        url = extend_param(url, params)
    try:
        request_ = urllib.request.Request(encode_url(url), data, headers=HEADERS, method=str(method))
    except ValueError as exc:
        return Response(urllib.error.URLError(exc))
    else:
        if data is not None or files is not None or json is not None:
            mime, request_.data = encode_data(data, files, json)
            request_.add_header(Header.CONTENT_TYPE, mime)
        if auth is not None:
            request_.add_header(Header.AUTHORIZATION,
                                f'Bearer {auth}' if isinstance(auth, str) else
                                f'Basic {base64.b64encode(":".join(auth).encode("latin1")).decode()}')
        if headers is not None:
            itertools.starmap(request_.add_header, headers.items())
        urllib.request.install_opener(_OPENER_DEFAULT if allow_redirects else _OPENER_NO_REDIRECT)
        try:
            _response = urllib.request.urlopen(request_, timeout=timeout)
        except urllib.error.URLError as _response:
            return Response(_response)
        else:
            response = Response(_response)
            if not stream:  # TODO probably exhausts the stream
                _ = response.content
            return response


def get(url: AnyStr, data: Optional[_TParams] = None, json: Optional[_TJSON] = None,
        params: Optional[_TParams] = None, headers: Optional[_THeaders] = None,
        files: Optional[_TFiles] = None, auth: Optional[_TAuth] = None,
        timeout: Optional[float] = None, allow_redirects: bool = True, stream: bool = True) -> Response:
    return request(http.HTTPMethod.GET, url, data, json, params, headers, files, auth, timeout, allow_redirects, stream)


def head(url: AnyStr, data: Optional[_TParams] = None, json: Optional[_TJSON] = None,
         params: Optional[_TParams] = None, headers: Optional[_THeaders] = None,
         files: Optional[_TFiles] = None, auth: Optional[_TAuth] = None,
         timeout: Optional[float] = None, allow_redirects: bool = True, stream: bool = True) -> Response:
    return request(http.HTTPMethod.HEAD, url, data, json, params, headers, files, auth, timeout, allow_redirects, stream)


def post(url: AnyStr, data: Optional[_TParams] = None, json: Optional[_TJSON] = None,
         params: Optional[_TParams] = None, headers: Optional[_THeaders] = None,
         files: Optional[_TFiles] = None, auth: Optional[_TAuth] = None,
         timeout: Optional[float] = None, allow_redirects: bool = True, stream: bool = True) -> Response:
    return request(http.HTTPMethod.POST, url, data, json, params, headers, files, auth, timeout, allow_redirects, stream)


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
            retrieved = size == os.path.getsize(path)
        except OSError:
            retrieved = False
        if retrieved and query_callback is not None:
            query_callback(1.0)
        return retrieved
    return False
