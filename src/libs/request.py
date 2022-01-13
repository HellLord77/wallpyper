__version__ = '0.0.4'

import contextlib
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
    def redirect_request(*_) -> None:
        return


_MIN_CHUNK = 32 * 1024
_OPENERS = urllib.request.build_opener(_HTTPRedirectHandler), urllib.request.build_opener()

USER_AGENT = f'{__name__}/{__version__}'


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
            for i in range(0, len(self._content), self.chunk_size):
                yield self._content[i:i + self.chunk_size]
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


def urljoin(base: str, *urls: str) -> str:
    if not base.endswith('/'):
        base = f'{base}/'
    for url in urls:
        base = f'{urllib.parse.urljoin(base, url)}/'
    return base[:-1]


def urlopen(url: str, params: Optional[Mapping[str, str]] = None, data: Optional[bytes] = None,
            headers: Optional[Mapping[str, str]] = None, redirection: Optional[bool] = None,
            stream: Optional[bool] = None) -> Response:
    query = {}
    for key, value in (params or {}).items():
        query[key] = value
    try:
        request = urllib.request.Request(f'{url}?{urllib.parse.urlencode(query)}', data)
    except ValueError as error:
        return Response(urllib.error.URLError(error))
    else:
        request.add_header('User-Agent', USER_AGENT)
        for head, val in (headers or {}).items():
            request.add_header(head, val)
        try:
            urllib.request.install_opener(_OPENERS[1 if redirection else 0])
            response = urllib.request.urlopen(request)
        except urllib.error.URLError as response:
            return Response(response)
        else:
            lazy_response = Response(response)
            if stream is False:
                lazy_response.get_content()
            return lazy_response


def download(url: str, path: str, size: Optional[int] = None, chunk_size: Optional[int] = None,
             chunk_count: Optional[int] = None, on_write: Optional[Callable[[int, ...], Any]] = None,
             args: Optional[Iterable] = None, kwargs: Optional[Mapping[str, Any]] = None) -> bool:
    response = urlopen(url)
    if response:
        size = size or int(response.get_header('Content-Length', str(sys.maxsize)))
        if os.path.exists(path):
            if os.path.isfile(path) and size == os.path.getsize(path):
                return True
            else:
                os.remove(path)
        else:
            os.makedirs(os.path.dirname(path), exist_ok=True)
        response.chunk_size = max(chunk_size or size // (chunk_count or sys.maxsize), _MIN_CHUNK)
        with open(path, 'wb') as file:
            write = file.write
            args = args or ()
            kwargs = kwargs or {}
            ratio = 0
            for chunk in response:
                write(chunk)
                ratio += len(chunk) / size
                if on_write:
                    on_write(round(ratio * 100), *args, **kwargs)
        return os.path.isfile(path) and size == os.path.getsize(path)
    return False


def upload(url: str, params: Optional[Mapping[str, str]] = None, fields: Optional[Mapping[str, str]] = None,
           files: Optional[Mapping[str, tuple[Optional[str], str]]] = None,  # TODO chunked upload
           headers: Optional[Mapping[str, str]] = None, redirection: Optional[bool] = None) -> Response:
    boundary = uuid.uuid4().hex
    data = b''
    for name, val in (fields or {}).items():
        data += f'--{boundary}{_CRLF}Content-Disposition: form-data; name="{name}"{_CRLF * 2}{val}{_CRLF}'.encode()
    for name, name_path in (files or {}).items():
        data += f'--{boundary}{_CRLF}Content-Disposition: form-data; name="{name}"; ' \
                f'filename="{name_path[0] or os.path.basename(name_path[1])}"{_CRLF * 2}'.encode()
        if os.path.isfile(name_path[1]):
            with open(name_path[1], 'rb') as file:
                buffer = file.read(MAX_CHUNK)
                while buffer:
                    data += buffer
                    buffer = file.read(MAX_CHUNK)
        data += _CRLF.encode()
    data += f'--{boundary}--{_CRLF}'.encode()
    headers_ = {'Content-Type': f'multipart/form-data; boundary={boundary}'}
    headers_.update(headers or {})
    return urlopen(url, params, data, headers_, redirection)
