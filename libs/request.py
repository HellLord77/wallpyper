import http.client
import json
import os
import sys
import typing
import urllib.error
import urllib.parse
import urllib.request

_CONTENT_LENGTH = 'content-length'
_MAX_SIZE = sys.maxsize

CHUNK_SIZE = 1024
USER_AGENT = 'request/0.0.1'


class Response:
    def __init__(self,
                 response: typing.Union[http.client.HTTPResponse, urllib.error.HTTPError, urllib.error.URLError],
                 stream: bool = False) -> None:
        self._content = bytes()
        self.chunk_size = CHUNK_SIZE
        self.reason = response.reason
        self.raw = response
        self.status_code = 418 if isinstance(response, urllib.error.URLError) else response.status
        if not stream:
            self._content = response.read()

    def __iter__(self) -> bytes:
        if self.raw.isclosed():
            for i in range(0, len(self._content), self.chunk_size):
                yield self._content[i:i + self.chunk_size]
        else:
            try:
                chunk = self.raw.read(self.chunk_size)
                while chunk:
                    yield chunk
                    chunk = self.raw.read(self.chunk_size)
            except ConnectionError:
                pass

    @property
    def content(self) -> bytes:
        if not self.raw.isclosed():
            self._content = self.raw.read()
        return self._content

    def json(self) -> typing.Union[dict, list, str, int, float, bool, None]:
        try:
            return json.loads(self.text())
        except json.decoder.JSONDecodeError:
            return {}

    def text(self) -> str:
        return self.content.decode()


def urljoin(base: str,
            *urls: str) -> str:
    for url in urls:
        base = f'{urllib.parse.urljoin(base, url)}/'
    return base if base.endswith('/') else f'{base}/'


# noinspection PyDefaultArgument
def urlopen(url: str,
            params: typing.Mapping[str, str] = {},
            stream: bool = False) -> Response:
    query = {}
    if params:
        for key, value in params.items():
            if value:
                query[key] = value
    try:
        request = urllib.request.Request(f'{url}?{urllib.parse.urlencode(query)}', headers={'User-Agent': USER_AGENT})
    except ValueError as err:
        return Response(urllib.error.URLError(err), True)
    else:
        try:
            return Response(urllib.request.urlopen(request), stream)
        except urllib.error.URLError as response:
            return Response(response, True)


# noinspection PyDefaultArgument
def urlretrieve(url: str,
                path: str,
                size: int = 0,
                chunk_size: int = CHUNK_SIZE,
                chunk_count: int = 0,
                callback: typing.Callable[[int, ...], typing.Any] = lambda arg: None,
                callback_args: typing.Iterable = (),
                callback_kwargs: typing.Mapping[str, typing.Any] = {}) -> bool:
    response = urlopen(url, stream=True)
    if response.status_code == 200:
        if not size:
            content_length = response.raw.getheader(_CONTENT_LENGTH)
            size = int(content_length) if content_length else _MAX_SIZE
        response.chunk_size = max(size // chunk_count if size != _MAX_SIZE and chunk_count else chunk_size, CHUNK_SIZE)
        ratio = 0
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'wb') as file:
            for chunk in response:
                file.write(chunk)
                ratio += len(chunk) / size
                callback(round(ratio * 100), *callback_args, **callback_kwargs)
        if size == os.stat(path).st_size:
            callback(100, *callback_args, **callback_kwargs)
            return True
    return False
