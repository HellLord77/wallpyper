__version__ = '0.0.3'  # https://github.com/sindresorhus/cli-spinners

import functools
import itertools
import json
import os
from typing import Iterator

_PATH = 'spinners.json'


def get(spinner: str) -> tuple[float, Iterator[str]]:
    data = load()[spinner]
    return data['interval'] / 1000, itertools.cycle(data['frames'])


@functools.cache
def load() -> dict[str, dict[str, int | list[str]]]:
    with open(os.path.join(os.path.dirname(__file__), _PATH), encoding='utf-8') as file:
        return json.load(file)


if __debug__:
    def download():
        import urllib.parse
        import urllib.request
        urllib.request.urlretrieve(urllib.parse.urljoin(
            'https://raw.githubusercontent.com/sindresorhus/cli-spinners/main',
            _PATH), os.path.join(os.path.dirname(__file__), _PATH))
        load.cache_clear()
        load()
