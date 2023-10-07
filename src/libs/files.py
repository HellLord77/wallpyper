from __future__ import annotations as _

__version__ = '0.0.16'

import filecmp
import functools
import glob
import hashlib
import math
import os
import shutil
import sys
import time
from typing import Any
from typing import AnyStr
from typing import Callable
from typing import IO
from typing import Iterable
from typing import Iterator
from typing import Optional

import _hashlib

# noinspection PyUnresolvedReferences
MAX_CHUNK = shutil.COPY_BUFSIZE
POLL_INTERVAL = 0.1


class Size(int):
    unit = 1024 if sys.platform == 'win32' else 1000
    _units = 'B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'

    @classmethod
    def from_size(cls, b: Optional[int] = None,
                  kb: Optional[float] = None, mb: Optional[float] = None,
                  gb: Optional[float] = None, tb: Optional[float] = None,
                  pb: Optional[float] = None, eb: Optional[float] = None,
                  zb: Optional[float] = None, yb: Optional[float] = None) -> Size:
        byte = 0 if b is None else b
        for index, unit in enumerate((kb, mb, gb, tb, pb, eb, zb, yb), 1):
            if unit is not None:
                byte += unit * cls.unit ** index
        return super().__new__(cls, byte)

    def __repr__(self):
        if self < self.unit:
            return f'{super().__repr__()} {self._units[0]}'
        else:
            index = int(math.log(self, self.unit))
            return f'{self / self.unit ** index:.2f} {self._units[index]}'

    @property
    def byte(self) -> int:
        return self

    @property
    def kilo_byte(self) -> float:
        return self / self.unit

    @property
    def mega_byte(self) -> float:
        return self.kilo_byte / self.unit

    @property
    def giga_byte(self) -> float:
        return self.mega_byte / self.unit

    @property
    def tera_byte(self) -> float:
        return self.giga_byte / self.unit

    @property
    def peta_byte(self) -> float:
        return self.tera_byte / self.unit

    @property
    def exa_byte(self) -> float:
        return self.peta_byte / self.unit

    @property
    def zetta_byte(self) -> float:
        return self.exa_byte / self.unit

    @property
    def yotta_byte(self) -> float:
        return self.zetta_byte / self.unit


def get_ext(path: str, dot: bool = False) -> str:
    ext = os.path.splitext(path)[1]
    if not dot:
        ext = ext[1:]
    return ext


def replace_ext(path: str, ext: str) -> str:
    if ext.startswith('.'):
        ext = ext[1:]
    return f'{os.path.splitext(path)[0]}.{ext}'


def iter_dir(path: str, recursive: bool = False) -> Iterator[str]:
    try:
        # noinspection PyTypeChecker
        it: Iterable[os.DirEntry] = os.scandir(path)
    except FileNotFoundError:
        pass
    else:
        for dir_entry in it:
            yield os.path.realpath(dir_entry.path)
            if recursive and dir_entry.is_dir():
                yield from iter_dir(dir_entry.path, recursive)


def iter_files(path: str, recursive: bool = False) -> Iterator[str]:
    return filter(os.path.isfile, iter_dir(path, recursive))


def get_size(path: str) -> Optional[int]:
    if os.path.isdir(path):
        return sum(get_size(dir_) for dir_ in iter_dir(path))
    elif os.path.isfile(path):
        return os.path.getsize(path)


def copy_obj(src: IO, dst: IO, chunk_size: Optional[int] = None,
             query_callback: Optional[Callable[[int], bool]] = None):
    if chunk_size is None:
        chunk_size = MAX_CHUNK
    written = 0
    while chunk := src.read(chunk_size):
        written += dst.write(chunk)
        if query_callback is not None and not query_callback(written):
            break


def copy(src: AnyStr, dst: AnyStr, chunk_size: Optional[int] = None,
         query_callback: Optional[Callable[[int, int], bool]] = None) -> bool:
    size = get_size(src)
    if query_callback is not None:
        @functools.wraps(query_callback)
        def query_callback(written: int, __query_callback=query_callback) -> bool:
            return __query_callback(written, size)
    with open(src, 'rb') as src_:
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, 'wb') as dst_:
            copy_obj(src_, dst_, chunk_size, query_callback)
    return os.path.exists(dst) and filecmp.cmp(src, dst)


def make_dir(path: str) -> bool:
    if os.path.exists(path) and not os.path.isdir(path):
        os.remove(path)
    os.makedirs(path, exist_ok=True)
    return os.path.isdir(path)


# noinspection PyShadowingBuiltins
def has_no_file(dir: str, recursive: bool = True) -> bool:
    if recursive:
        try:
            for dir_ in iter_dir(dir):
                if os.path.isfile(dir_) or not has_no_file(dir_, recursive):
                    return False
        except PermissionError:
            return False
        return True
    return not any(os.scandir(dir))


def _filter_files(paths: Iterable[str]) -> Iterator[str]:
    for path in paths:
        if os.path.isfile(path):
            yield path


def trim_dir(path: str, target: int, key: Callable[[str], Any] = os.path.getctime) -> bool:
    trimmed = False
    paths = glob.glob(os.path.join(path, '**'), recursive=True)
    try:
        paths.sort(key=key, reverse=True)
    except FileNotFoundError:
        return False
    it = _filter_files(paths)
    size = 0
    for path in it:
        size += os.path.getsize(path)
        if size > target:
            os.remove(path)
            trimmed = True
            break
    for path in it:
        os.remove(path)
    return trimmed


def remove(path: str, recursive: bool = False, timeout: float = math.inf) -> bool:
    tried = False
    end_time = time.monotonic() + timeout
    while not tried or end_time > time.monotonic():
        try:
            shutil.rmtree(path) if recursive else os.remove(path)
        except PermissionError:
            pass
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
def checksum(path: str, hash: AnyStr | _hashlib.HASH, name: str = 'md5') -> bool:
    hash_ = get_hash(path, name)
    if isinstance(hash, _hashlib.HASH):
        hash = hash.digest()
    if isinstance(hash, bytes):
        return hash == hash_.digest()
    else:
        # noinspection PyUnresolvedReferences
        return hash.lower() == hash_.hexdigest()


def get_disk_size(path: str) -> int:
    return shutil.disk_usage(os.path.splitdrive(path)[0]).total
