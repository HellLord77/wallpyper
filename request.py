import json
import os
import urllib.error
import urllib.parse
import urllib.request

CHUNK_SIZE = 1
USER_AGENT = 'request/0.0.1'


class Response:
    def __init__(self, response, stream=False):
        self._content = b''
        self.chunk_size = CHUNK_SIZE
        self.reason = response.msg
        self.response = response
        self.status_code = response.status
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


def urlretrieve(url, path, chunk_size=CHUNK_SIZE, content_length=-1, callback=lambda arg: None):
    response = urlopen(url, stream=True)
    if response.status_code == 200:
        response.chunk_size = chunk_size
        chunk_number = 0
        content_length = int(response.response.getheader('content-length')) or content_length
        if not os.path.exists(path):
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'wb') as file:
                for chunk in response:
                    file.write(chunk)
                    chunk_number += len(chunk) / content_length * 100
                    callback(int(chunk_number))
        return content_length == os.stat(path).st_size
    return False


def urlopen(url, params=None, stream=False):
    request = urllib.request.Request(prepare_url(url, params or {}), headers={'User-Agent': USER_AGENT})
    try:
        return Response(urllib.request.urlopen(request), stream)
    except (urllib.error.HTTPError, urllib.error.URLError) as response:
        # noinspection PyTypeChecker
        return Response(response, stream)


def prepare_url(url, params):
    query = {}
    for key, value in params.items():
        if isinstance(value, str):
            query[key] = value
    return f'{url}?{urllib.parse.urlencode(query)}'
