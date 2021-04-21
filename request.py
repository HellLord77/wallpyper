import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

CHUNK_SIZE = 1024
CONTENT_LENGTH = 'content-length'
MAX = sys.maxsize
USER_AGENT = 'request/0.0.1'


class Response:
    def __init__(self, response, stream=False):
        self._content = b''
        self.chunk_size = CHUNK_SIZE
        self.reason = response.reason
        self.response = response
        self.status = 418 if isinstance(response, urllib.error.URLError) else response.status
        if not stream:
            self._content = response.read()

    def __iter__(self):
        if self.response.isclosed():
            for i in range(0, len(self._content), self.chunk_size):
                yield self._content[i:i + self.chunk_size]
        else:
            chunk = self.response.read(self.chunk_size)
            while chunk:
                yield chunk
                chunk = self.response.read(self.chunk_size)

    @property
    def content(self):
        if not self.response.isclosed():
            self._content += self.response.read()
        return self._content

    def json(self):
        return json.loads(self.text())

    def text(self):
        return self.content.decode()


def urlopen(url, params=None, stream=False):
    query = {}
    if params:
        for key, value in params.items():
            if isinstance(value, str):
                query[key] = value
    request = urllib.request.Request(f'{url}?{urllib.parse.urlencode(query)}', headers={'User-Agent': USER_AGENT})
    try:
        return Response(urllib.request.urlopen(request), stream)
    except (urllib.error.HTTPError, urllib.error.URLError) as response:
        # noinspection PyTypeChecker
        return Response(response, True)


def urlretrieve(url, path, chunk_size=CHUNK_SIZE, content_length=0, chunk_count=0, callback=lambda arg: None):
    response = urlopen(url, stream=True)
    if response.status == 200:
        if not content_length:
            content_length_header = response.response.getheader(CONTENT_LENGTH)
            content_length = int(content_length_header) if content_length_header else MAX
        response.chunk_size = content_length // chunk_count if content_length != MAX and chunk_count else chunk_size
        chunk_number = 0
        if not os.path.exists(path):
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'wb') as file:
                for chunk in response:
                    file.write(chunk)
                    chunk_number += len(chunk) / content_length * 100
                    callback(round(chunk_number))
        return content_length == os.stat(path).st_size
    return False
