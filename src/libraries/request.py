__version__ = '0.0.3'

import contextlib
import http.client
import json
import os
import sys
import typing
import urllib.error
import urllib.parse
import urllib.request
import uuid


class Status:
    OK = 200
    FOUND = 302
    IM_A_TEAPOT = 418


class _HTTPRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(*_) -> None:
        return


_MIN_CHUNK = 32 * 1024
_OPENERS = urllib.request.build_opener(_HTTPRedirectHandler), urllib.request.build_opener()

USER_AGENT = f'request/{__version__}'


class Response:
    def __init__(self,
                 response: typing.Union[http.client.HTTPResponse, urllib.error.URLError]):
        self.chunk_size = _MIN_CHUNK
        self.response = response
        self.reason = response.reason
        self.get_header = getattr(response, 'getheader', lambda _, default=None: default)
        self.status = getattr(response, 'status', Status.IM_A_TEAPOT)
        self._content = bytes()
        self._ok = self.status == Status.OK

    def __bool__(self) -> bool:
        return self._ok

    def __iter__(self) -> typing.Generator[bytes, None, None]:
        if self.response.isclosed():
            for i in range(0, len(self._content), self.chunk_size):
                yield self._content[i:i + self.chunk_size]
        else:
            with contextlib.suppress(ConnectionError):
                chunk = self.response.read(self.chunk_size)
                while chunk:
                    yield chunk
                    chunk = self.response.read(self.chunk_size)

    def get_content(self) -> bytes:
        if not self.response.isclosed():
            self._content = self.response.read()
        return self._content

    def get_json(self) -> typing.Optional[typing.Union[dict, list, str, int, float, bool]]:
        try:
            return json.loads(self.get_text())
        except json.decoder.JSONDecodeError:
            return None

    def get_text(self) -> str:
        return self.get_content().decode()


def urljoin(base: str,
            *urls: str) -> str:
    if not base.endswith('/'):
        base = f'{base}/'
    for url in urls:
        base = f'{urllib.parse.urljoin(base, url)}/'
    return base[:-1]


def urlopen(url: str,
            params: typing.Optional[dict[str, str]] = None,
            data: typing.Optional[bytes] = None,
            headers: typing.Optional[dict[str, str]] = None,
            redirection: typing.Optional[bool] = None,
            stream: typing.Optional[bool] = None) -> Response:
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


def download(url: str,
             path: str,
             size: typing.Optional[int] = None,
             chunk_size: typing.Optional[int] = None,
             chunk_count: typing.Optional[int] = None,
             callback: typing.Optional[typing.Callable[[int, ...], typing.Any]] = None,
             callback_args: typing.Optional[tuple] = None,
             callback_kwargs: typing.Optional[dict[str, typing.Any]] = None) -> bool:
    response = urlopen(url)
    if response:
        size = size or int(response.get_header('Content-Length', str(sys.maxsize)))
        response.chunk_size = max(chunk_size or size // (chunk_count or sys.maxsize), _MIN_CHUNK)
        ratio = 0
        os.makedirs(os.path.dirname(path), exist_ok=True)
        if os.path.isfile(path) and size == os.stat(path).st_size:
            return True
        if os.path.isdir(path):
            os.remove(path)
        with open(path, 'wb') as file:
            for chunk in response:
                file.write(chunk)
                ratio += len(chunk) / size
                if callback:
                    callback(round(ratio * 100), *callback_args or (), **callback_kwargs or {})
        return size == os.stat(path).st_size
    return False


def upload(url: str,
           params: typing.Optional[dict[str, str]] = None,
           fields: typing.Optional[dict[str, str]] = None,
           files: typing.Optional[dict[str, tuple[typing.Optional[str], str]]] = None,
           headers: typing.Optional[dict[str, str]] = None,
           redirection: typing.Optional[bool] = None) -> Response:
    boundary = uuid.uuid4().hex
    data = b''
    for name, val in (fields or {}).items():
        data += f'--{boundary}\r\nContent-Disposition: form-data; name="{name}"\r\n\r\n{val}\r\n'.encode()
    for name, name_path in (files or {}).items():
        data += f'--{boundary}\r\nContent-Disposition: form-data; name="{name}"; ' \
                f'filename="{name_path[0] or os.path.basename(name_path[1])}"\r\n\r\n'.encode()
        if os.path.isfile(name_path[1]):
            with open(name_path[1], 'rb') as file:
                data += file.read()
        data += '\r\n'.encode()
    data += f'--{boundary}--\r\n'.encode()
    headers_ = {'Content-Type': f'multipart/form-data; boundary={boundary}'}
    headers_.update(headers or {})
    return urlopen(url, params, data, headers_, redirection)
