from typing import Any, Iterator, Iterable, Mapping


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


def index(iterable: Iterable[str], key: str) -> int:
    key = key.lower()
    for index_, key_ in enumerate(iter(iterable)):
        if key == key_:
            return index_
    raise ValueError(f'{key!r} is not in iterable')


def contains(iterable: Iterable[str], key: str) -> bool:
    try:
        index(iterable, key)
    except ValueError:
        return False
    else:
        return True


def getitem(mapping: Mapping[str, Any], key: str) -> Any:
    key = key.lower()
    for key_, val in zip(iter(mapping), mapping.values()):
        if key == key_:
            return val
    raise KeyError(key)


def get(mapping: Mapping[str, Any], key: str, default: Any = None) -> Any:
    try:
        return getitem(mapping, key)
    except KeyError:
        return default
