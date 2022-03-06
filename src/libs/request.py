__version__ = '0.0.5'

import builtins
import contextlib
import hashlib
import http.client
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
import uuid
from typing import Any, Callable, Generator, Iterable, Mapping, Optional, Union

_CRLF = '\r\n'

MAX_CHUNK = 1024 * 1024


class Status:
    OK = 200
    FOUND = 302
    IM_A_TEAPOT = 418


class _HTTPRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(*_):
        return


_MIN_CHUNK = 32 * 1024
_OPENERS = urllib.request.build_opener(_HTTPRedirectHandler), urllib.request.build_opener()

ACCEPT_LANGUAGE = 'en-US'
USER_AGENT = f'{__name__}/{__version__}'


class Header:
    ACCEPT_LANGUAGE = 'Accept-Language'
    USER_AGENT = 'User-Agent'


class Response:
    chunk_size = _MIN_CHUNK

    def __init__(self, response: Union[http.client.HTTPResponse, urllib.error.URLError]):
        self.response = response
        self.reason = response.reason
        self.get_header = getattr(response, 'getheader', lambda _, default=None: default)
        self.status = getattr(response, 'status', Status.IM_A_TEAPOT)
        self._content = b''

    def __bool__(self) -> bool:
        return self.status == Status.OK

    def __iter__(self) -> Generator[bytes, None, None]:
        if self.response.isclosed():
            for index in range(0, len(self._content), self.chunk_size):
                yield self._content[index:index + self.chunk_size]
        else:
            with contextlib.suppress(ConnectionError):
                read = self.response.read
                chunk = read(self.chunk_size)
                while chunk:
                    yield chunk
                    chunk = read(self.chunk_size)

    def get_content(self) -> bytes:
        if not self.response.isclosed():
            self._content = self.response.read()
        return self._content

    def get_json(self) -> Optional[Union[dict, list, str, int, float, bool]]:
        try:
            return json.loads(self.get_text())
        except json.decoder.JSONDecodeError:
            return None

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


def encode(url: str, params: Optional[Mapping[str, Union[str, Iterable[str]]]] = None) -> str:
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
         headers: Optional[Mapping[str, str]] = None, redirect: bool = True, stream: bool = True) -> Response:
    try:
        request = urllib.request.Request(encode(url, params), data)
    except ValueError as error:
        return Response(urllib.error.URLError(error))
    else:
        request.add_header(Header.ACCEPT_LANGUAGE, ACCEPT_LANGUAGE)
        request.add_header(Header.USER_AGENT, USER_AGENT)
        for head, val in (headers or {}).items():
            request.add_header(head, val)
        try:
            urllib.request.install_opener(_OPENERS[redirect])
            response = urllib.request.urlopen(request)
        except urllib.error.URLError as response:
            return Response(response)
        else:
            lazy_response = Response(response)
            if not stream:
                lazy_response.get_content()
            return lazy_response


def _get_hash(path: str, type_: str = 'md5') -> bytes:
    hash_ = hashlib.new(type_)
    with builtins.open(path, 'rb') as file:
        while buffer := file.read(MAX_CHUNK):
            hash_.update(buffer)
    return hash_.digest()


def download(url: str, path: str, size: Optional[int] = None, md5: Optional[bytes] = None,
             sha256: Optional[bytes] = None, chunk_size: Optional[int] = None, chunk_count: Optional[int] = None,
             callback: Optional[Callable[[int, ...], bool]] = None, args: Optional[Iterable] = None,
             kwargs: Optional[Mapping[str, Any]] = None) -> bool:
    response = open(url)
    if os.path.exists(path):
        if os.path.isfile(path) and ((size and size == os.path.getsize(path)) or (md5 and md5 == _get_hash(path)) or (
                sha256 and _get_hash(path, 'sha256'))):
            return True
        elif os.path.isdir(path):
            return False
    else:
        os.makedirs(os.path.dirname(path), exist_ok=True)
    if response:
        size = size or int(response.get_header('Content-Length', str(sys.maxsize)))
        if os.path.isfile(path):
            if size == os.path.getsize(path):
                return True
            else:
                os.remove(path)
        response.chunk_size = max(chunk_size or size // (chunk_count or sys.maxsize), _MIN_CHUNK)
        cancelled = False
        try:
            with builtins.open(path, 'wb') as file:
                write = file.write
                args = () if args is None else args
                kwargs = {} if kwargs is None else kwargs
                ratio = 0
                for chunk in response:
                    write(chunk)
                    ratio += len(chunk) / size
                    if callback and not callback(round(ratio * 100), *args, **kwargs):
                        cancelled = True
                        break
            if cancelled:
                os.remove(path)
                return False
        except PermissionError:
            return False
        if os.path.isfile(path) and size == os.path.getsize(path):
            if callback:
                callback(100, *args, **kwargs)
            return True
    return False


def upload(url: str, params: Optional[Mapping[str, str]] = None, fields: Optional[Mapping[str, str]] = None,
           files: Optional[Mapping[str, tuple[Optional[str], str]]] = None,  # TODO chunked upload
           headers: Optional[Mapping[str, str]] = None, redirect: bool = True) -> Response:
    boundary = uuid.uuid4().hex
    data = b''
    for name, val in (fields or {}).items():
        data += f'--{boundary}{_CRLF}Content-Disposition: form-data; name="{name}"{_CRLF * 2}{val}{_CRLF}'.encode()
    for name, name_path in (files or {}).items():
        data += (f'--{boundary}{_CRLF}Content-Disposition: form-data; name="{name}"; '
                 f'filename="{name_path[0] or os.path.basename(name_path[1])}"{_CRLF * 2}'.encode())
        if os.path.isfile(name_path[1]):
            with builtins.open(name_path[1], 'rb') as file:
                buffer = file.read(MAX_CHUNK)
                while buffer:
                    data += buffer
                    buffer = file.read(MAX_CHUNK)
        data += _CRLF.encode()
    data += f'--{boundary}--{_CRLF}'.encode()
    headers_ = {'Content-Type': f'multipart/form-data; boundary={boundary}'}
    headers_.update(headers or {})
    return open(url, params, data, headers_, redirect)
