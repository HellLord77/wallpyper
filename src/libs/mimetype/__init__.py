__version__ = '0.0.2'  # https://github.com/jshttp/mime-types

import functools
import json
import os
from typing import Any, Iterator, Optional

_PATH = 'db.json'


def _iter(key: str, default=None, type_: Optional[str] = None) -> Iterator[tuple[str, Any]]:
    mimetypes = load()
    if type_ is None:
        for type_, mimetype in mimetypes.items():
            yield type_, mimetype.get(key, default)
    else:
        yield type_, mimetypes.get(type_, {}).get(key, default)


# noinspection PyShadowingBuiltins
@functools.lru_cache
def get_source(type: str) -> Optional[str]:
    return next(_iter('source', type_=type))[1]


# noinspection PyShadowingBuiltins
@functools.lru_cache
def get_charset(type: str) -> Optional[str]:
    return next(_iter('charset', type_=type))[1]


# noinspection PyShadowingBuiltins
def is_compressible(type: str) -> bool:
    compressible = next(_iter('compressible', False, type))[1]
    _ = load()[type]
    return compressible


# noinspection PyShadowingBuiltins
def iter_extensions(type: Optional[str] = None) -> Iterator[tuple[str, list[str]]]:
    yield from _iter('extensions', [], type)


# noinspection PyShadowingBuiltins
@functools.lru_cache
def get_extension(type: str) -> Optional[str]:
    for mimetype in iter_extensions(type):
        if extensions := mimetype[1]:
            return extensions[0]


def iter_types(path_or_extension: Optional[str] = None) -> Iterator[str]:
    if path_or_extension is None:
        yield from (type_ for type_, _ in iter_extensions())
    else:
        extension = os.path.splitext(f'_.{os.path.basename(path_or_extension)}')[1].lstrip('.').lower()
        yield from (type_ for type_, extensions in iter_extensions() if extension in extensions)


@functools.lru_cache
def get_type(path_or_extension: str = None) -> Optional[str]:
    return next(iter_types(path_or_extension), None)


@functools.cache
def load() -> dict[str, dict[str, bool | str | list[str]]]:
    with open(os.path.join(os.path.dirname(__file__), _PATH), encoding='utf-8') as file:
        return json.load(file)


if __debug__:
    def download():
        import urllib.parse
        import urllib.request
        urllib.request.urlretrieve(urllib.parse.urljoin(
            'https://raw.githubusercontent.com/jshttp/mime-db/master',
            _PATH), os.path.join(os.path.dirname(__file__), _PATH))
        load.cache_clear()
        load()
