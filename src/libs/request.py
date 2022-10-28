__version__ = '0.0.7'

import builtins
import contextlib
import http.client
import io
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
import urllib.response
import uuid
from typing import Any, Callable, Generator, Iterable, Mapping, Optional

_CRLF = '\r\n'

MAX_CHUNK = 1024 * 1024


class Status:
    OK = 200
    FOUND = 302
    BAD_REQUEST = 400
    NOT_FOUND = 404
    IM_A_TEAPOT = 418


class _HTTPRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(*_):
        return


_MIN_CHUNK = 32 * 1024
_OPENER_DEFAULT = urllib.request.build_opener()
_OPENER_NO_REDIRECT = urllib.request.build_opener(_HTTPRedirectHandler)

ACCEPT_LANGUAGE = 'en-US'
USER_AGENT = f'{__name__}/{__version__}'


class Header:
    ACCEPT_LANGUAGE = 'Accept-Language'
    CONTENT_DISPOSITION = 'Content-Disposition'
    CONTENT_LENGTH = 'Content-Length'
    CONTENT_TYPE = 'Content-Type'
    USER_AGENT = 'User-Agent'


class _Response:
    chunk_size = _MIN_CHUNK

    def __init__(self, response: urllib.response.addinfourl | http.client.HTTPResponse | urllib.error.URLError):
        self.response = response
        self.getheader = getattr(response, 'getheader', self._getheader)
        self.status = getattr(response, 'status', Status.IM_A_TEAPOT)
        self.file = isinstance(getattr(self.response, 'file', None), io.BufferedReader)

    def __bool__(self) -> bool:
        return self.file or self.status == Status.OK

    def __iter__(self) -> Generator[bytes, None, None]:
        with contextlib.suppress(ConnectionError):
            while chunk := self.response.read(self.chunk_size):
                yield chunk

    @staticmethod
    def _getheader(_: str, default=None):
        return default

    def get_content(self) -> bytes:
        return self.response.read()

    def get_json(self) -> Optional[dict | list | str | int | float | bool]:
        with contextlib.suppress(json.decoder.JSONDecodeError):
            return json.loads(self.get_text())

    def get_text(self) -> str:
        return self.get_content().decode()

    def read(self, n: int) -> bytes:
        return self.response.read(n)


def strip(url: str) -> str:
    parts = urllib.parse.urlparse(url)
    return f'{parts.scheme}://{parts.netloc}{parts.path}'


def join(base: str, *urls: str) -> str:
    if not base.endswith('/'):
        base = f'{base}/'
    for url in urls:
        base = f'{urllib.parse.urljoin(base, url)}/'
    return base[:-1]


def query(url: str) -> dict[str, list[str]]:
    return urllib.parse.parse_qs(urllib.parse.urlparse(url).query)


def encode(url: str, params: Optional[Mapping[str, str | Iterable[str]]] = None) -> str:
    if params is None:
        return url
    parts = urllib.parse.urlparse(url)
    query_ = urllib.parse.parse_qs(parts.query)
    for key, val in params.items():
        if key not in query_:
            query_[key] = []
        if isinstance(val, str):
            query_[key].append(val)
        else:
            query_[key].extend(val)
    return urllib.parse.urlunparse(parts._replace(query=urllib.parse.urlencode(query_, True)))


# noinspection PyShadowingBuiltins
def open(url: str, params: Optional[Mapping[str, str]] = None, data: Optional[bytes] = None,
         headers: Optional[Mapping[str, str]] = None, redirect: bool = True, stream: bool = True) -> _Response:
    try:
        request = urllib.request.Request(encode(url, params), data)
    except ValueError as e:
        return _Response(urllib.error.URLError(e))
    else:
        request.add_header(Header.ACCEPT_LANGUAGE, ACCEPT_LANGUAGE)
        request.add_header(Header.USER_AGENT, USER_AGENT)
        for head, val in (headers or {}).items():
            request.add_header(head, val)
        try:
            urllib.request.install_opener(_OPENER_DEFAULT if redirect else _OPENER_NO_REDIRECT)
            response = urllib.request.urlopen(request)
        except urllib.error.URLError as response:
            return _Response(response)
        else:
            lazy_response = _Response(response)
            if not stream:
                lazy_response.get_content()
            return lazy_response


def download(url: str, path: str, size: Optional[int] = None, chunk_size: Optional[int] = None,
             chunk_count: Optional[int] = None, query_callback: Optional[Callable[[float, ...], bool]] = None,
             args: Optional[Iterable] = None, kwargs: Optional[Mapping[str, Any]] = None) -> bool:
    if args is None:
        args = ()
    if kwargs is None:
        kwargs = {}
    response = open(url)
    if os.path.exists(path):
        if os.path.isfile(path) and size and size == os.path.getsize(path):
            if query_callback:
                query_callback(1.0, *args, **kwargs)
            return True
        elif os.path.isdir(path):
            return False
    else:
        os.makedirs(os.path.dirname(path), exist_ok=True)
    if response:
        size = size or int(response.getheader(Header.CONTENT_LENGTH, str(
            os.path.getsize(response.response.fp.name) if response.file else sys.maxsize)))
        if os.path.isfile(path):
            if size == os.path.getsize(path):
                if query_callback:
                    query_callback(1.0, *args, **kwargs)
                return True
            else:
                os.remove(path)
        response.chunk_size = max(chunk_size or size // (chunk_count or sys.maxsize), _MIN_CHUNK)
        try:
            with builtins.open(path, 'wb') as file:
                ratio = 0
                for chunk in response:
                    ratio += file.write(chunk) / size
                    if query_callback and not query_callback(ratio, *args, **kwargs):
                        file.close()
                        os.remove(path)
                        break
        except PermissionError:
            return False
        if os.path.isfile(path) and size == os.path.getsize(path):
            if query_callback:
                query_callback(1.0, *args, **kwargs)
            return True
    return False


def upload(url: str, params: Optional[Mapping[str, str]] = None, fields: Optional[Mapping[str, str]] = None,
           files: Optional[Mapping[str, tuple[Optional[str], str]]] = None,  # TODO chunked upload
           headers: Optional[Mapping[str, str]] = None, redirect: bool = True) -> _Response:
    boundary = uuid.uuid4().hex
    prefix = f'--{boundary}{_CRLF}{Header.CONTENT_DISPOSITION}: form-data; name='
    data = b''
    if fields is not None:
        for name, val in fields.items():
            data += f'{prefix}"{name}"{_CRLF * 2}{val}{_CRLF}'.encode()
    if files is not None:
        for name, name_path in files.items():
            data += f'{prefix}"{name}"; filename="{name_path[0] or os.path.basename(name_path[1])}"{_CRLF * 2}'.encode()
            if os.path.isfile(name_path[1]):
                with builtins.open(name_path[1], 'rb') as file:
                    buffer = file.read(MAX_CHUNK)
                    while buffer:
                        data += buffer
                        buffer = file.read(MAX_CHUNK)
            data += _CRLF.encode()
    data += f'--{boundary}--{_CRLF}'.encode()
    headers_ = {Header.CONTENT_TYPE: f'multipart/form-data; boundary={boundary}'}
    headers_.update(headers or {})
    return open(url, params, data, headers_, redirect)
