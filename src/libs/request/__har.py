import datetime
import http.cookiejar
import urllib.request
from typing import AnyStr
from typing import Iterable
from typing import Mapping
from typing import MutableMapping
from typing import NotRequired
from typing import Optional
from typing import TypedDict

from . import Header as _Header
from . import Request as _Request
from . import __name__ as _name
from . import __version__ as _version
from . import _caseinsensitive
from . import _str
from . import extract_cookies as _extract_cookies
from . import extract_params as _extract_params
from . import strip_url as _strip_url


class TTimings(TypedDict):
    blocked: NotRequired[float]
    dns: NotRequired[float]
    connect: NotRequired[float]
    send: float
    wait: float
    receive: float
    ssl: NotRequired[float]
    comment: NotRequired[str]


class TBeforeAfterRequest(TypedDict):
    expires: NotRequired[str]
    lastAccess: str
    eTag: str
    hitCount: int
    comment: NotRequired[str]


class TCache(TypedDict):
    beforeRequest: NotRequired[TBeforeAfterRequest]
    afterRequest: NotRequired[TBeforeAfterRequest]
    comment: NotRequired[str]


class TContent(TypedDict):
    size: int
    compression: NotRequired[int]
    mimeType: str
    text: NotRequired[str]
    encoding: NotRequired[str]
    comment: NotRequired[str]


class TParam(TypedDict):
    name: str
    value: NotRequired[str]
    fileName: NotRequired[str]
    contentType: NotRequired[str]
    comment: NotRequired[str]


class TPostData(TypedDict):
    mimeType: str
    params: NotRequired[list[TParam]]
    text: NotRequired[str]
    comment: NotRequired[str]


class TQueryString(TypedDict):
    name: str
    value: str
    comment: NotRequired[str]


class THeader(TypedDict):
    name: str
    value: str
    comment: NotRequired[str]


class TCookie(TypedDict):
    name: str
    value: str
    path: NotRequired[str]
    domain: NotRequired[str]
    expires: NotRequired[str]
    httpOnly: NotRequired[bool]
    secure: NotRequired[bool]
    comment: NotRequired[str]


class TResponse(TypedDict):
    status: int
    statusText: str
    httpVersion: str
    cookies: list[TCookie]
    headers: list[THeader]
    content: TContent
    redirectURL: str
    headersSize: int
    bodySize: int
    comment: NotRequired[str]


class TRequest(TypedDict):
    method: str
    url: str
    httpVersion: str
    cookies: list[TCookie]
    headers: list[THeader]
    queryString: list[TQueryString]
    postData: NotRequired[TPostData]
    headersSize: int
    bodySize: int
    comment: NotRequired[str]


class TEntry(TypedDict):
    pageref: NotRequired[str]
    startedDateTime: str
    time: float
    request: TRequest
    response: TResponse
    cache: TCache
    timings: TTimings
    serverIPAddress: NotRequired[str]
    connection: NotRequired[str]
    comment: NotRequired[str]


class THARPageTimings(TypedDict):
    onContentLoad: NotRequired[float]
    onLoad: NotRequired[float]
    comment: NotRequired[str]


class TPage(TypedDict):
    startedDateTime: str
    id: str
    title: str
    pageTimings: THARPageTimings
    comment: NotRequired[str]


class TBrowser(TypedDict):
    name: str
    version: str
    comment: NotRequired[str]


class TCreator(TypedDict):
    name: str
    version: str
    comment: NotRequired[str]


class TLog(TypedDict):
    version: str
    creator: TCreator
    browser: NotRequired[TBrowser]
    pages: NotRequired[list[TPage]]
    entries: list[TEntry]
    comment: NotRequired[str]


class THAR(TypedDict):
    log: TLog
    comment: NotRequired[str]


def default_har(name: str = _name, version: str = _version) -> THAR:
    return {'log': {'version': '1.2', 'creator': {
        'name': name, 'version': version}, 'entries': []}}


def encode_cookies(cookies: Iterable[http.cookiejar.Cookie],
                   request: Optional[MutableMapping] = None) -> list[TCookie]:
    encoded = []
    for cookie in cookies:
        encoded_cookie = {'name': cookie.name, 'value': cookie.value or ''}
        if cookie.path != '/':
            encoded_cookie['path'] = cookie.path
        if cookie.domain:
            encoded_cookie['domain'] = cookie.domain
        if cookie.expires is not None:
            encoded_cookie['expires'] = datetime.datetime.fromtimestamp(
                cookie.expires, datetime.UTC).isoformat()
        # noinspection PyUnresolvedReferences,PyProtectedMember
        encoded_cookie['httpOnly'] = 'HttpOnly' in cookie._rest
        encoded_cookie['secure'] = cookie.secure
        encoded.append(encoded_cookie)
    if request is not None:
        request['cookies'] = encoded
    # noinspection PyTypeChecker
    return encoded


def encode_headers(headers: Iterable[tuple[str, str]],
                   request: Optional[MutableMapping] = None) -> tuple[list[THeader], int]:
    encoded = [{'name': name, 'value': value} for name, value in headers], -1
    if request is not None:
        request['headers'], request['headersSize'] = encoded
    return encoded


def encode_params(params: Mapping[AnyStr, Iterable[AnyStr]],
                  request: Optional[MutableMapping] = None) -> list[TQueryString]:
    encoded = []
    for key, vals in params.items():
        for val in vals:
            encode_param = {'name': key}
            if val:
                encode_param['value'] = val
            encoded.append(encode_param)
    if request is not None:
        request['queryString'] = encoded
    return encoded


def encode_body(mime: str, body: bytes | str,
                request: Optional[MutableMapping] = None) -> tuple[TPostData, int]:
    encoded = {'mimeType': mime, 'text': _str(body)}, len(body)
    if request is not None:
        request['postData'], request['bodySize'] = encoded
    return encoded


def encode_request(request: urllib.request.Request | _Request,
                   entry: Optional[MutableMapping] = None) -> dict:
    if isinstance(request, _Request):
        request = request.prepare()
    encoded = {
        'method': request.method,
        'url': _strip_url(request.full_url, fragment=False),
        'httpVersion': 'HTTP/1.1'}
    cookies = getattr(request, '_cookies', None)
    encode_cookies([] if cookies is None else _extract_cookies(cookies), encoded)
    encode_headers(request.header_items(), encoded)
    encode_params(_extract_params(request.full_url), encoded)
    if request.data is not None:
        encode_body(_caseinsensitive.getitem(
            request.headers, _Header.CONTENT_TYPE), request.data, encoded)
    if entry is not None:
        entry['request'] = encoded
    return encoded


def encode(*requests: urllib.request.Request | _Request | tuple[
        urllib.request.Request | _Request, float | datetime.datetime]) -> THAR:
    encoded = default_har()
    for request_started in requests:
        if isinstance(request_started, tuple):
            request, started = request_started
        else:
            request = request_started
            started = datetime.datetime.now(datetime.UTC)
        if not isinstance(started, datetime.datetime):
            started = datetime.datetime.fromtimestamp(
                started, datetime.UTC)
        entry = {'startedDateTime': started.isoformat()}
        encode_request(request, entry)
        # noinspection PyTypeChecker
        encoded['log']['entries'].append(entry)
    return encoded
