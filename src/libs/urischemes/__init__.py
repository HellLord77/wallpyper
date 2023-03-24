from __future__ import annotations as _

__version__ = '0.0.1'  # https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml

import csv
import enum
import functools
import os
import typing
from typing import Iterator, Optional

_PATH = 'uri-schemes-1.csv'
_URISCHEMES: Optional[tuple[URIScheme, ...]] = None


class URIStatus(enum.StrEnum):
    PERMANENT = 'Permanent'
    PROVISIONAL = 'Provisional'
    HISTORICAL = 'Historical'


class URIScheme(typing.NamedTuple):
    scheme: str
    description: str
    status: str


def get_scheme(uri: bytes | str) -> str:
    if isinstance(uri, bytes):
        uri = uri.decode()
    return uri.split(':', 1)[0].lower()


def _iter(status: Optional[URIStatus] = None) -> Iterator[URIScheme]:
    global _URISCHEMES
    if _URISCHEMES is None:
        with open(os.path.join(os.path.dirname(__file__), _PATH)) as file:
            reader = csv.reader(file)
            next(reader, None)
            _URISCHEMES = tuple(URIScheme(row[0], row[
                2], URIStatus(row[3])) for row in reader)
    return iter(_URISCHEMES) if status is None else (
        scheme for scheme in _URISCHEMES if scheme.status is status)


def iter_permanent() -> Iterator[URIScheme]:
    return _iter(URIStatus.PERMANENT)


def iter_provisional() -> Iterator[URIScheme]:
    return _iter(URIStatus.PROVISIONAL)


def iter_historical() -> Iterator[URIScheme]:
    return _iter(URIStatus.HISTORICAL)


@functools.lru_cache
def get(scheme_or_uri: bytes | str) -> Optional[URIScheme]:
    scheme_or_uri = get_scheme(scheme_or_uri)
    for scheme in _iter():
        if scheme.scheme == scheme_or_uri:
            return scheme


if __debug__:
    def _download():
        import urllib.parse
        import urllib.request
        path = os.path.join(os.path.dirname(__file__), _PATH)
        urllib.request.urlretrieve(urllib.parse.urljoin(
            'https://www.iana.org/assignments/uri-schemes/', _PATH), path)
        with open(path) as file:
            all(csv.reader(file))
