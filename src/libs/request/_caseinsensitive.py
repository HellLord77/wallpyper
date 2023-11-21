from typing import Any
from typing import Iterable
from typing import Iterator
from typing import Mapping
from typing import MutableMapping
from typing import Sequence


def eq(string: str, other: str) -> bool:
    return string.lower() == other.lower()


def startswith(string: str, prefix: str) -> bool:
    return string.lower().startswith(prefix.lower())


def endswith(string: str, suffix: str) -> bool:
    return string.lower().endswith(suffix.lower())


# noinspection PyShadowingBuiltins
def iter(iterable: Iterable[str]) -> Iterator[str]:
    for key in iterable:
        yield key.lower()


def match(iterable: Iterable[str], key: str) -> str:
    key = key.lower()
    for key_ in iterable:
        if key == key_.lower():
            return key_
    raise ValueError(f'{key!r} is not in iterable')


def index(iterable: Sequence[str], key: str) -> int:
    return iterable.index(match(iterable, key))


def contains(iterable: Iterable[str], key: str) -> bool:
    try:
        match(iterable, key)
    except ValueError:
        return False
    else:
        return True


def getitem(mapping: Mapping[str, Any], key: str) -> Any:
    try:
        key = match(mapping, key)
    except ValueError:
        raise KeyError(key)
    else:
        return mapping[key]


def setitem(mapping: MutableMapping[str, Any], key: str, value: Any):
    try:
        key = match(mapping, key)
    except ValueError:
        pass
    mapping[key] = value


def get(mapping: Mapping[str, Any], key: str, default: Any = None) -> Any:
    try:
        return getitem(mapping, key)
    except KeyError:
        return default
