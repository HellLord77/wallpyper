import http.client
import json
import math
import os
import typing
import urllib.error
import urllib.parse
import urllib.request

_CONTENT_LENGTH = 'content-length'
_USER_AGENT = 'user-agent'
_CHUNK_SIZE = 1024

USER_AGENT = 'request/0.0.1'


class LazyResponse:
    def __init__(self,
                 response: typing.Union[http.client.HTTPResponse, urllib.error.URLError]) -> None:
        self._content = bytes()
        self.chunk_size = _CHUNK_SIZE
        self.response = response
        self.reason = response.reason
        self.status = response.status if hasattr(response, 'status') else 418

    def __iter__(self) -> bytes:
        if self.response.isclosed():
            for i in range(0, len(self._content), self.chunk_size):
                yield self._content[i:i + self.chunk_size]
        else:
            try:
                chunk = self.response.read(self.chunk_size)
                while chunk:
                    yield chunk
                    chunk = self.response.read(self.chunk_size)
            except ConnectionError:
                pass

    def get_content(self) -> bytes:
        if not self.response.isclosed():
            self._content = self.response.read()
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
            stream: typing.Optional[bool] = None) -> LazyResponse:
    query = {}
    if params:
        for key, value in params.items():
            if isinstance(value, str):
                query[key] = value
    try:
        request = urllib.request.Request(f'{url}?{urllib.parse.urlencode(query)}', headers={_USER_AGENT: USER_AGENT})
    except ValueError as err:
        return LazyResponse(urllib.error.URLError(err))
    else:
        try:
            response = urllib.request.urlopen(request)
        except urllib.error.URLError as response:
            return LazyResponse(response)
        else:
            lazy_response = LazyResponse(response)
            if stream is False:
                lazy_response._content = response.read()  # TODO: handle exception
            return lazy_response


def urlretrieve(url: str,
                path: str,
                size: typing.Optional[int] = None,
                chunk_size: typing.Optional[int] = None,
                chunk_count: typing.Optional[int] = None,
                callback: typing.Optional[typing.Callable[[int, ...], typing.Any]] = None,
                callback_args: typing.Optional[tuple] = None,
                callback_kwargs: typing.Optional[dict[str, typing.Any]] = None) -> bool:
    response = urlopen(url)
    if response.status == 200:
        if not size:
            content_length = response.response.getheader(_CONTENT_LENGTH)
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
                        callback(min(round(ratio * 100), 99), *callback_args or (), **callback_kwargs or {})
        return size == os.stat(path).st_size
    return False
