import datetime
import http.cookiejar
import urllib.request
from typing import AnyStr, Iterable, Mapping, MutableMapping, Optional

from . import Header
from . import Request
from . import __name__
from . import __version__
from . import _str
from . import extract_cookies
from . import extract_params
from . import strip_url

_TRequest = urllib.request.Request | Request


def default_har(name: str = __name__, version: str = __version__) -> dict:
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
                   request: Optional[MutableMapping] = None) -> list:
    encoded = []
    for header in headers:
        encoded.append({'name': header[0], 'value': header[1]})
    if request is not None:
        request['headers'] = encoded
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


def encode_request(request: _TRequest,
                   entry: Optional[MutableMapping] = None) -> dict:
    if isinstance(request, Request):
        request = request.prepare()
    encoded = {
        'method': request.method,
        'url': strip_url(request.full_url, False),
        'httpVersion': 'HTTP/1.1'}
    cookies = getattr(request, '_cookies', None)
    encode_cookies([] if cookies is None else extract_cookies(cookies), encoded)
    encode_headers(request.header_items(), encoded)
    encode_params(extract_params(request.full_url), encoded)
    encoded['headersSize'] = -1
    if request.data is not None:
        encode_body(request.headers[Header.CONTENT_TYPE], request.data, encoded)
    if entry is not None:
        entry['request'] = encoded
    return encoded


def encode(*requests: _TRequest | tuple[_TRequest, float | datetime.datetime]) -> dict:
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
