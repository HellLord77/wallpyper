import contextlib
import http.client
import json
import math
import os
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
    def redirect_request(*_):
        pass


_OPENERS = urllib.request.build_opener(_HTTPRedirectHandler), urllib.request.build_opener()
_CHUNK_SIZE = 1024

USER_AGENT = 'request/0.0.1'


class LazyResponse:
    def __init__(self,
                 response: typing.Union[http.client.HTTPResponse, urllib.error.URLError]):
        self._content = bytes()
        self.chunk_size = _CHUNK_SIZE
        self.response = response
        self.headers = getattr(response, 'headers', http.client.HTTPMessage())
        self.reason = response.reason
        self.status = getattr(response, 'status', Status.IM_A_TEAPOT)
        self.ok = self.status == Status.OK

    def __iter__(self):
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
            self._content = self.response.read()  # TODO: handle exception
        return self._content

    def get_json(self) -> typing.Union[dict, list, str, int, float, bool, None]:
        try:
            return json.loads(self.get_text())
        except json.decoder.JSONDecodeError:
            return {}

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
            stream: typing.Optional[bool] = None) -> LazyResponse:
    query = {}
    for key, value in (params or {}).items():
        query[key] = value
    try:
        request = urllib.request.Request(f'{url}?{urllib.parse.urlencode(query)}', data)
    except ValueError as request:
        return LazyResponse(urllib.error.URLError(request))
    else:
        request.add_header('User-Agent', USER_AGENT)
        for head, val in (headers or {}).items():
            request.add_header(head, val)
        try:
            urllib.request.install_opener(_OPENERS[1 if redirection else 0])
            response = urllib.request.urlopen(request)
        except urllib.error.URLError as response:
            return LazyResponse(response)
        else:
            lazy_response = LazyResponse(response)
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
    if response.ok:
        if not size:
            content_length = response.response.getheader('Content-Length')
            size = int(content_length) if content_length else math.inf
        response.chunk_size = size // chunk_count if size != math.inf and chunk_count else chunk_size or _CHUNK_SIZE
        ratio = 0
        os.makedirs(os.path.dirname(path), exist_ok=True)
        if not os.path.isfile(path) or size != os.stat(path).st_size:
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
           redirection: typing.Optional[bool] = None) -> LazyResponse:
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
