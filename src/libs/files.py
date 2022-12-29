__version__ = '0.0.12'

import contextlib
import filecmp
import glob
import hashlib
import os
import shutil
import sys
import time
from typing import Any, Callable, Generator, IO, Iterable, Mapping, Optional

import _hashlib

# noinspection PyUnresolvedReferences
MAX_CHUNK = shutil.COPY_BUFSIZE
POLL_INTERVAL = 0.1


class File:
    __slots__ = 'url', 'name', 'size', '_sha256', '_md5'
    _algorithms = {f'_{algorithm}' for algorithm in hashlib.algorithms_available}.intersection(__slots__)

    def __init__(self, url: str, name: str, size: int = 0,
                 sha256: Optional[bytes] = None, md5: Optional[bytes] = None):
        self.url = url
        self.name = name
        self.size = size
        self._sha256 = sha256
        self._md5 = md5

    def __bool__(self):
        return bool(str(self))

    def __int__(self):
        return self.size

    def __eq__(self, other):
        return self.url == (other.url if isinstance(other, File) else other)

    def __hash__(self):
        return hash(self.url)

    def checksum(self, path: str, try_: bool = False) -> bool:
        if os.path.isfile(path):
            for algorithm in self._algorithms:
                if (hash_ := getattr(self, algorithm)) is not None:
                    return check_hash(path, hash_, algorithm[1:])
            if try_:
                return True
        return False

    def fill(self, path: str) -> bool:
        if os.path.isfile(path):
            if self.size is None:
                self.size = os.path.getsize(path)
            for algorithm in self._algorithms:
                if getattr(self, algorithm) is None:
                    setattr(self, algorithm, get_hash(path, algorithm[1:]).digest())
            return True
        return False


def remove_ext(path: str) -> str:
    return os.path.splitext(path)[0]


def replace_ext(path: str, ext: str) -> str:
    return f'{os.path.splitext(path)[0]}.{ext}'


def iter_dir(path: str, recursive: bool = False) -> Generator[str, None, None]:
    dir_entry: os.DirEntry
    for dir_entry in os.scandir(path):
        yield os.path.realpath(dir_entry.path)
        if recursive and dir_entry.is_dir():
            yield from iter_dir(dir_entry.path, recursive)


def iter_files(path: str, recursive: bool = False) -> Generator[str, None, None]:
    yield from filter(os.path.isfile, iter_dir(path, recursive))


def get_size(path: str) -> Optional[int]:
    if os.path.isdir(path):
        return sum(get_size(dir_) for dir_ in iter_dir(path))
    elif os.path.isfile(path):
        return os.path.getsize(path)


def copyfileobj(src: IO, dst: IO, size: Optional[int] = None,
                chunk_size: Optional[int] = None, query_callback: Optional[Callable[[float, ...], bool]] = None,
                args: Optional[Iterable] = None, kwargs: Optional[Mapping[str, Any]] = None):
    size = size or sys.maxsize
    chunk_size = chunk_size or MAX_CHUNK
    args = () if args is None else args
    kwargs = {} if kwargs is None else kwargs
    ratio = 0
    while chunk := src.read(chunk_size):
        dst.write(chunk)
        ratio += len(chunk) / size
        if query_callback and not query_callback(ratio, *args, **kwargs):
            break


def copy(src: str, dst: str,
         chunk_size: Optional[int] = None, query_callback: Optional[Callable[[float, ...], bool]] = None,
         args: Optional[Iterable] = None, kwargs: Optional[Mapping[str, Any]] = None) -> bool:
    if os.path.exists(src):
        if not os.path.exists(dst):
            with contextlib.suppress(PermissionError):
                with open(src, 'rb') as src_:
                    os.makedirs(os.path.dirname(dst), exist_ok=True)
                    with open(dst, 'wb') as dst_:
                        copyfileobj(src_, dst_, os.path.getsize(src), chunk_size, query_callback, args, kwargs)
        return os.path.exists(dst) and filecmp.cmp(src, dst)
    return False


def make_dir(path: str) -> bool:
    if os.path.exists(path) and not os.path.isdir(path):
        os.remove(path)
    os.makedirs(path, exist_ok=True)
    return os.path.isdir(path)


def is_only_dirs(path: str, recursive: bool = False) -> bool:
    if recursive:
        try:
            for dir_ in iter_dir(path):
                if os.path.isfile(dir_) or not is_only_dirs(dir_, recursive):
                    return False
        except PermissionError:
            return False
        return True
    return not any(os.scandir(path))


def _filter_files(paths: Iterable[str]) -> Generator[str, None, None]:
    for path in paths:
        if os.path.isfile(path):
            yield path


def trim_dir(path: str, target: int) -> bool:
    trimmed = False
    paths = glob.glob(os.path.join(path, '**'), recursive=True)
    try:
        paths.sort(key=os.path.getctime, reverse=True)
    except FileNotFoundError:
        return False
    itt = _filter_files(paths)
    size = 0
    for path in itt:
        size += os.path.getsize(path)
        if size > target:
            os.remove(path)
            trimmed = True
            break
    for path in itt:
        os.remove(path)
    return trimmed


def remove(path: str, recursive: bool = False, timeout: Optional[float] = None) -> bool:
    tried = False
    end_time = time.time() + (timeout or 0)
    while not tried or end_time > time.time():
        with contextlib.suppress(PermissionError):
            try:
                shutil.rmtree(path) if recursive else os.remove(path)
            except (FileNotFoundError, NotADirectoryError):
                break
        tried = True
        time.sleep(POLL_INTERVAL)
    return not os.path.exists(path)


def get_hash(path: str, name: str = 'md5', *, __hash=None) -> _hashlib.HASH:
    if __hash is None:
        __hash = hashlib.new(name)
    if os.path.isdir(path):
        for dir_ in iter_dir(path):
            get_hash(dir_, name, __hash=__hash)
    elif os.path.isfile(path):
        with open(path, 'rb') as file:
            while buffer := file.read(MAX_CHUNK):
                __hash.update(buffer)
    return __hash


# noinspection PyShadowingBuiltins
def check_hash(path: str, hash: bytes | str | _hashlib.HASH, name: str = 'md5') -> bool:
    hash_ = get_hash(path, name)
    if isinstance(hash, _hashlib.HASH):
        hash = hash.digest()
    if isinstance(hash, bytes):
        return hash == hash_.digest()
    else:
        return hash.lower() == hash_.hexdigest()
