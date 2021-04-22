import json
import os
import sys
import urllib.parse
import urllib.request
from http.client import HTTPResponse
from typing import Callable, Mapping, Union
from urllib.error import HTTPError, URLError

CHUNK_SIZE = 1024
CONTENT_LENGTH = 'content-length'
MAX_SIZE = sys.maxsize
USER_AGENT = 'request/0.0.1'


class Response:
    def __init__(self, response: Union[HTTPResponse, HTTPError, URLError], stream: bool = False) -> None:
        self._content = b''
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
            chunk = self.raw.read(self.chunk_size)
            while chunk:
                yield chunk
                chunk = self.raw.read(self.chunk_size)

    @property
    def content(self) -> bytes:
        if not self.raw.isclosed():
            self._content = self.raw.read()
        return self._content

    def json(self) -> str:
        return json.loads(self.text())

    def text(self) -> str:
        return self.content.decode()


def urlopen(url: str, params: Mapping = None, stream: bool = False) -> Response:
    query = {}
    if params:
        for key, value in params.items():
            if isinstance(value, str):
                query[key] = value
    request = urllib.request.Request(f'{url}?{urllib.parse.urlencode(query)}', headers={'User-Agent': USER_AGENT})
    try:
        return Response(urllib.request.urlopen(request), stream)
    except URLError as response:
        # noinspection PyTypeChecker
        return Response(response, True)


def urlretrieve(url: str, path: str, size: int = 0,
                chunk_size: int = CHUNK_SIZE, chunk_count: int = 0, callback: Callable = lambda arg: None) -> bool:
    response = urlopen(url, stream=True)
    if response.status_code == 200:
        if not size:
            content_length = response.raw.getheader(CONTENT_LENGTH)
            size = int(content_length) if content_length else MAX_SIZE
        response.chunk_size = size // chunk_count if size != MAX_SIZE and chunk_count else chunk_size
        percentage = 0
        if not os.path.exists(path):
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'wb') as file:
                for chunk in response:
                    file.write(chunk)
                    percentage += len(chunk) / size * 100
                    callback(round(percentage))
        return size in (MAX_SIZE, os.stat(path).st_size)
    return False
