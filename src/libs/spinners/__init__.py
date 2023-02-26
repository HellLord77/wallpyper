__version__ = '0.0.2'  # https://github.com/sindresorhus/cli-spinners

import itertools
import json
import os
from typing import Iterator, Optional

_PATH = 'spinners.json'
_SPINNERS: Optional[dict[str, dict[str, int | list[str]]]] = None


def get(spinner: str) -> tuple[float, Iterator[str]]:
    global _SPINNERS
    if _SPINNERS is None:
        with open(os.path.join(os.path.dirname(__file__), _PATH), encoding='utf-8') as file:
            _SPINNERS = json.load(file)
    data = _SPINNERS[spinner]
    return data['interval'] / 1000, itertools.cycle(data['frames'])


if __debug__:
    def _download():
        import urllib.parse
        import urllib.request
        path = os.path.join(os.path.dirname(__file__), _PATH)
        urllib.request.urlretrieve(urllib.parse.urljoin(
            'https://raw.githubusercontent.com/sindresorhus/cli-spinners/main/', _PATH), path)
        with open(path, encoding='utf-8') as file:
            json.load(file)
