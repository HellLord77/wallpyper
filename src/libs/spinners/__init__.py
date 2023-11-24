__version__ = '0.0.3'  # https://github.com/sindresorhus/cli-spinners

import functools
import importlib.resources
import itertools
import json
from typing import Iterator

_PATH = 'spinners.json'


def get(spinner: str) -> tuple[float, Iterator[str]]:
    data = load()[spinner]
    return data['interval'] / 1000, itertools.cycle(data['frames'])


@functools.cache
def load() -> dict[str, dict[str, int | list[str]]]:
    return json.load((importlib.resources.files(__name__) / _PATH).open(encoding='utf-8'))


if __debug__:
    def download():
        import urllib.parse
        import urllib.request
        urllib.request.urlretrieve(urllib.parse.urljoin(
            'https://raw.githubusercontent.com/sindresorhus/cli-spinners/main/',
            _PATH), str(importlib.resources.files(__name__) / _PATH))
        load.cache_clear()
        load()
