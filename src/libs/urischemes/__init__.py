__version__ = '0.0.2'  # https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml

import csv
import enum
import functools
import importlib.resources
from typing import Iterator
from typing import NamedTuple
from typing import Optional

_PATH = 'uri-schemes-1.csv'


class URIStatus(enum.StrEnum):
    PERMANENT = 'Permanent'
    PROVISIONAL = 'Provisional'
    HISTORICAL = 'Historical'


class URIScheme(NamedTuple):
    scheme: str
    description: str
    status: str


def get_scheme(uri: bytes | str) -> str:
    if isinstance(uri, bytes):
        uri = uri.decode()
    return uri.split(':', 1)[0].lower()


def _iter(status: Optional[URIStatus] = None) -> Iterator[URIScheme]:
    urischemes = load()
    return iter(urischemes) if status is None else (
        scheme for scheme in urischemes if scheme.status is status)


def iter_permanent() -> Iterator[URIScheme]:
    return _iter(URIStatus.PERMANENT)


def iter_provisional() -> Iterator[URIScheme]:
    return _iter(URIStatus.PROVISIONAL)


def iter_historical() -> Iterator[URIScheme]:
    return _iter(URIStatus.HISTORICAL)


@functools.lru_cache
def get(scheme_or_uri: bytes | str) -> Optional[URIScheme]:
    scheme_or_uri = get_scheme(scheme_or_uri)
    for scheme in load():
        if scheme.scheme == scheme_or_uri:
            return scheme


@functools.cache
def load() -> tuple[URIScheme, ...]:
    reader = csv.reader((importlib.resources.files(
        __name__) / _PATH).open(encoding='utf-8'))
    next(reader)
    return tuple(URIScheme(row[0], row[
        2], URIStatus(row[3])) for row in reader)


if __debug__:
    def download():
        import urllib.parse
        import urllib.request
        urllib.request.urlretrieve(urllib.parse.urljoin(
            'https://www.iana.org/assignments/uri-schemes/',
            _PATH), str(importlib.resources.files(__name__) / _PATH))
        load.cache_clear()
        load()
