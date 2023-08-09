import datetime
import http.cookiejar
import urllib.request
from typing import AnyStr, Iterable, Mapping, MutableMapping, NotRequired, Optional, TypedDict

from . import Header as _Header
from . import Request as _Request
from . import __name__ as _name
from . import __version__ as _version
from . import _caseinsensitive
from . import _str
from . import extract_cookies as _extract_cookies
from . import extract_params as _extract_params
from . import strip_url as _strip_url

_TTimings = TypedDict('_TTimings', {
    'blocked': NotRequired[float],
    'dns': NotRequired[float],
    'connect': NotRequired[float],
    'send': float,
    'wait': float,
    'receive': float,
    'ssl': NotRequired[float],
    'comment': NotRequired[str]})
_TBeforeAfterRequest = TypedDict('_TBeforeAfterRequest', {
    'expires': NotRequired[str],
    'lastAccess': str,
    'eTag': str,
    'hitCount': int,
    'comment': NotRequired[str]})
_TCache = TypedDict('_TCache', {
    'beforeRequest': NotRequired[_TBeforeAfterRequest],
    'afterRequest': NotRequired[_TBeforeAfterRequest],
    'comment': NotRequired[str]})
_TContent = TypedDict('_TContent', {
    'size': int,
    'compression': NotRequired[int],
    'mimeType': str,
    'text': NotRequired[str],
    'encoding': NotRequired[str],
    'comment': NotRequired[str]})
_TParam = TypedDict('_TParam', {
    'name': str,
    'value': NotRequired[str],
    'fileName': NotRequired[str],
    'contentType': NotRequired[str],
    'comment': NotRequired[str]})
_TPostData = TypedDict('_TPostData', {
    'mimeType': str,
    'params': NotRequired[list[_TParam]],
    'text': NotRequired[str],
    'comment': NotRequired[str]})
_TQueryString = TypedDict('_TQueryString', {
    'name': str,
    'value': str,
    'comment': NotRequired[str]})
_THeader = TypedDict('_THeader', {
    'name': str,
    'value': str,
    'comment': NotRequired[str]})
_TCookie = TypedDict('_TCookie', {
    'name': str,
    'value': str,
    'path': NotRequired[str],
    'domain': NotRequired[str],
    'expires': NotRequired[str],
    'httpOnly': NotRequired[bool],
    'secure': NotRequired[bool],
    'comment': NotRequired[str]})
_TResponse = TypedDict('_TResponse', {
    'status': int,
    'statusText': str,
    'httpVersion': str,
    'cookies': list[_TCookie],
    'headers': list[_THeader],
    'content': _TContent,
    'redirectURL': str,
    'headersSize': int,
    'bodySize': int,
    'comment': NotRequired[str]})
_TRequest = TypedDict('_TRequest', {
    'method': str,
    'url': str,
    'httpVersion': str,
    'cookies': list[_TCookie],
    'headers': list[_THeader],
    'queryString': list[_TQueryString],
    'postData': NotRequired[_TPostData],
    'headersSize': int,
    'bodySize': int,
    'comment': NotRequired[str]})
_TEntry = TypedDict('_TEntry', {
    'pageref': NotRequired[str],
    'startedDateTime': str,
    'time': float,
    'request': _TRequest,
    'response': _TResponse,
    'cache': _TCache,
    'timings': _TTimings,
    'serverIPAddress': NotRequired[str],
    'connection': NotRequired[str],
    'comment': NotRequired[str]})
_THARPageTimings = TypedDict('_THARPageTimings', {
    'onContentLoad': NotRequired[float],
    'onLoad': NotRequired[float],
    'comment': NotRequired[str]})
_TPage = TypedDict('_TPage', {
    'startedDateTime': str,
    'id': str,
    'title': str,
    'pageTimings': _THARPageTimings,
    'comment': NotRequired[str]})
_TBrowser = TypedDict('_TBrowser', {
    'name': str,
    'version': str,
    'comment': NotRequired[str]})
_TCreator = TypedDict('_TCreator', {
    'name': str,
    'version': str,
    'comment': NotRequired[str]})
_TLog = TypedDict('_TLog', {
    'version': str,
    'creator': _TCreator,
    'browser': NotRequired[_TBrowser],
    'pages': NotRequired[list[_TPage]],
    'entries': list[_TEntry],
    'comment': NotRequired[str]})


def default_har(name: str = _name, version: str = _version) -> dict:
    return {'log': {'version': '1.2', 'creator': {
        'name': name, 'version': version}, 'entries': []}}


def encode_cookies(cookies: Iterable[http.cookiejar.Cookie],
                   request: Optional[MutableMapping] = None) -> list:
    encoded = []
    for cookie in cookies:
        encoded_cookie = {'name': cookie.name, 'value': cookie.value}
        if cookie.path != '/':
            encoded_cookie['path'] = cookie.path
        if cookie.domain:
            encoded_cookie['domain'] = cookie.domain
        if cookie.expires is not None:
            encoded_cookie['expires'] = datetime.datetime.utcfromtimestamp(cookie.expires).isoformat()
        # noinspection PyUnresolvedReferences,PyProtectedMember
        encoded_cookie['httpOnly'] = 'HttpOnly' in cookie._rest
        encoded_cookie['secure'] = cookie.secure
        encoded.append(encoded_cookie)
    if request is not None:
        request['cookies'] = encoded
    return encoded


def encode_headers(headers: Iterable[tuple[str, str]],
                   request: Optional[MutableMapping] = None) -> tuple[list[dict[str, str]], int]:
    encoded = [{'name': name, 'value': value} for name, value in headers], -1
    if request is not None:
        request['headers'], request['headersSize'] = encoded
    return encoded


def encode_params(params: Mapping[AnyStr, Iterable[AnyStr]],
                  request: Optional[MutableMapping] = None) -> list:
    encoded = []
    for key, vals in params.items():
        for val in vals:
            encoded.append({'name': key, 'value': val})
    if request is not None:
        request['queryString'] = encoded
    return encoded


def encode_body(mime: str, body: bytes | str,
                request: Optional[MutableMapping] = None) -> tuple[dict[str, str], int]:
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


def encode(*requests: urllib.request.Request | _Request | tuple[urllib.request.Request | _Request,
                                                                float | datetime.datetime]) -> dict:
    encoded = default_har()
    for request_started in requests:
        if isinstance(request_started, tuple):
            request, started = request_started
        else:
            request = request_started
            started = datetime.datetime.utcnow()
        if not isinstance(started, datetime.datetime):
            started = datetime.datetime.utcfromtimestamp(started)
        entry = {'startedDateTime': started.isoformat()}
        encode_request(request, entry)
        encoded['log']['entries'].append(entry)
    return encoded
