__version__ = '0.1.1'

import base64
import contextlib
import http.client
import io
import json as json_
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
import urllib.response
import uuid
from typing import Any, AnyStr, BinaryIO, Callable, Iterator, Iterable, Mapping, Optional

_TJSON = int | bool | float | str | tuple | list | dict
_TParams = Mapping[AnyStr, Optional[AnyStr | Iterable[AnyStr]]]
_THeaders = Mapping[str, str]
_TFiles = Mapping[str, AnyStr | BinaryIO | tuple[
    AnyStr | BinaryIO] | tuple[AnyStr | BinaryIO, AnyStr] | tuple[
                      AnyStr | BinaryIO, AnyStr, Mapping[str, Optional[str]]]]
_TAuth = str | tuple[str, str]


class _HTTPRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(*_):
        pass


_MIN_CHUNK = 32 * 1024
_CRLF = '\r\n'
_FILE_URI = 'file'
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


class _Response:
    chunk_size = _MIN_CHUNK

    def __init__(self, response: urllib.response.addinfourl | http.client.HTTPResponse | urllib.error.URLError):
        self.response = response
        self.getheader = getattr(response, 'getheader', self._getheader)
        self.status = http.HTTPStatus(getattr(response, 'status', None) or http.HTTPStatus.IM_A_TEAPOT)
        self.local = response.fp.name if isinstance(getattr(self.response, 'file', None), io.BufferedReader) else None

    def __bool__(self) -> bool:
        return self.status == http.HTTPStatus.OK if self.local is None else os.path.isfile(self.local)

    def __iter__(self) -> Iterator[bytes]:
        while chunk := self.response.read(self.chunk_size):
            yield chunk

    @staticmethod
    def _getheader(_: str, default=None):
        return default

    @property
    def content(self) -> bytes:
        return self.response.read()

    @property
    def text(self) -> str:
        return self.content.decode()

    def json(self) -> Any:
        with contextlib.suppress(json_.decoder.JSONDecodeError):
            return json_.loads(self.text)

    def read(self, n: int) -> bytes:
        return self.response.read(n)


def _str(o: AnyStr) -> str:
    return o.decode() if isinstance(o, bytes) else o


def is_path(url: str) -> bool:
    return urllib.parse.urlparse(url).scheme == _FILE_URI


def from_path(path: str) -> str:
    return urllib.parse.urljoin(f'{_FILE_URI}:', urllib.request.pathname2url(path))


def strip(url: str) -> str:
    parts = urllib.parse.urlparse(url)
    return f'{parts.scheme}://{parts.netloc}{parts.path}'


def join(base: str, *paths: str) -> str:
    if not base.endswith('/'):
        base = f'{base}/'
    for path in paths:
        if path:
            base = f'{urllib.parse.urljoin(base, path)}/'
    return base[:-1]


def get_params(url: str) -> dict[str, list[str]]:
    return urllib.parse.parse_qs(urllib.parse.urlparse(url).query)


def encode_params(params: Optional[AnyStr | Mapping]) -> str:
    if params is None:
        return ''
    elif isinstance(params, (bytes, str)):
        return params
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


def extend_param(url: str, params: Optional[_TParams] = None) -> str:
    parts = urllib.parse.urlparse(url)
    query = urllib.parse.parse_qs(parts.query)
    if params is not None:
        for key, val in params.items():
            if val is not None:
                if key not in query:
                    query[key] = []
                if isinstance(val, (bytes, str)):
                    query[key].append(val)
                else:
                    query[key].extend(val)
    return urllib.parse.urlunparse(parts._replace(query=encode_params(query)))


def request(method: str | http.HTTPMethod, url: str, data: Optional[_TParams] = None, json: Optional[_TJSON] = None,
            params: Optional[_TParams] = None, headers: Optional[_THeaders] = None,
            files: Optional[_TFiles] = None, auth: Optional[_TAuth] = None,
            timeout: Optional[float] = None, allow_redirects: bool = True, stream: bool = True) -> _Response:
    if data is not None or files is not None or json is not None:
        mime, data = encode_data(data, files, json)
    else:
        mime = ''
    if params is not None:
        url = extend_param(url, params)
    try:
        _request = urllib.request.Request(url, data, HEADERS, method=str(method))
    except ValueError as exc:
        return _Response(urllib.error.URLError(exc))
    else:
        _request.add_header(Header.CONTENT_TYPE, mime)
        if auth is not None:
            _request.add_header(Header.AUTHORIZATION,
                                f'Bearer {auth}' if isinstance(auth, str) else
                                f'Basic {base64.b64encode(":".join(auth).encode("latin1")).decode()}')
        if headers is not None:
            for header in headers.items():
                _request.add_header(*header)
        try:
            urllib.request.install_opener(_OPENER_DEFAULT if allow_redirects else _OPENER_NO_REDIRECT)
            _response = urllib.request.urlopen(_request, timeout=timeout)
        except urllib.error.URLError as _response:
            return _Response(_response)
        else:
            response = _Response(_response)
            if not stream:
                _ = response.content
            return response


def get(url: str, data: Optional[_TParams] = None, json: Optional[_TJSON] = None,
        params: Optional[_TParams] = None, headers: Optional[_THeaders] = None,
        files: Optional[_TFiles] = None, auth: Optional[_TAuth] = None,
        timeout: Optional[float] = None, allow_redirects: bool = True, stream: bool = True) -> _Response:
    return request(http.HTTPMethod.GET, url, data, json, params, headers, files, auth, timeout, allow_redirects, stream)


def post(url: str, data: Optional[_TParams] = None, json: Optional[_TJSON] = None,
         params: Optional[_TParams] = None, headers: Optional[_THeaders] = None,
         files: Optional[_TFiles] = None, auth: Optional[_TAuth] = None,
         timeout: Optional[float] = None, allow_redirects: bool = True, stream: bool = True) -> _Response:
    return request(http.HTTPMethod.POST, url, data, json, params, headers, files, auth, timeout, allow_redirects, stream)


def retrieve(url: str, path: AnyStr, size: Optional[int] = None,
             chunk_size: Optional[int] = None, chunk_count: Optional[int] = None,
             query_callback: Optional[Callable[[float], bool]] = None) -> bool:
    response = get(url)
    if response:
        if size is None:
            size = int(response.getheader(Header.CONTENT_LENGTH, sys.maxsize)) \
                if response.local is None else os.path.getsize(response.local)
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
