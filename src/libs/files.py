from __future__ import annotations as _

__version__ = '0.0.16'

import contextlib
import dataclasses
import filecmp
import glob
import hashlib
import math
import os
import shutil
import sys
import time
import urllib.parse
from typing import Any, AnyStr, Callable, IO, Iterable, Iterator, Optional

import _hashlib

# noinspection PyUnresolvedReferences
MAX_CHUNK = shutil.COPY_BUFSIZE
POLL_INTERVAL = 0.1


@dataclasses.dataclass
class File:
    url: str
    name: str = ''
    size: int = 0
    sha256: bytes | str = dataclasses.field(default=b'', repr=False, kw_only=True)
    md5: bytes | str = dataclasses.field(default=b'', repr=False, kw_only=True)

    def __init_subclass__(cls):
        super().__init_subclass__()
        cls.__hash__ = cls.__hash__
        cls.__eq__ = cls.__eq__

    def __post_init__(self):
        if not self.name:
            self.name = urllib.parse.unquote(os.path.basename(self.url))
        for algorithm, hash_ in self._iter_hashes():
            if not isinstance(hash_, bytes):
                setattr(self, algorithm, bytes.fromhex(hash_))

    def __hash__(self):
        return hash(self.url)

    def __str__(self):
        return repr(self).replace(f' size={self.size}, ', f' size={Size(self.size)}, ', 1)

    def __eq__(self, other):
        if isinstance(other, File):
            return self.url == other.url
        return NotImplemented

    def _iter_hashes(self) -> Iterable[tuple[str, bytes | str]]:
        for algorithm in hashlib.algorithms_available:
            if hasattr(self, algorithm):
                yield algorithm, getattr(self, algorithm)

    def _iter_filled_hashes(self) -> Iterable[tuple[str, bytes]]:
        for algorithm, hash_ in self._iter_hashes():
            if hash_:
                yield algorithm, hash_

    def asdict(self) -> dict[str, Any]:
        result: dict = {'url': self.url, 'name': self.name}
        if self.size:
            result['size'] = self.size
        for algorithm, hash_ in self._iter_filled_hashes():
            result[algorithm] = ''.join(f'{b:02x}' for b in hash_)
        return result

    def checksize(self, path: str) -> bool:
        if self.size:
            try:
                return self.size == os.path.getsize(path)
            except OSError:
                pass
        return False

    def checksum(self, path: str) -> bool:
        for algorithm, hash_ in self._iter_filled_hashes():
            try:
                return checksum(path, hash_, algorithm)
            except OSError:
                break
        return False

    def fill(self, path: str) -> bool:
        if not self.size:
            try:
                self.size = os.path.getsize(path)
            except OSError:
                return False
        if not any(self._iter_filled_hashes()):
            for algorithm, hash_ in self._iter_hashes():
                if not hash_:
                    try:
                        hash_ = get_hash(path, algorithm)
                    except OSError:
                        return False
                    else:
                        setattr(self, algorithm, hash_.digest())
                        break
        return True


@dataclasses.dataclass
class ImageFile(File):
    width: int = 0
    height: int = 0
    sketchy: bool = False
    nsfw: bool = False

    def asdict(self) -> dict[str, Any]:
        result = super().asdict()
        if self.width:
            result['width'] = self.width
        if self.height:
            result['height'] = self.height
        if self.nsfw:
            result['nsfw'] = self.nsfw
        for algorithm, _ in self._iter_filled_hashes():
            result[algorithm] = result.pop(algorithm)
        return result

    def is_animated(self) -> bool:  # TODO
        return os.path.splitext(self.name)[1].lower() in ('.gif', '.webp')

    def is_portrait(self) -> bool:
        return self.width < self.height

    def is_landscape(self) -> bool:
        return self.width > self.height

    def is_sfw(self) -> bool:
        return not self.sketchy and not self.nsfw


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
            return f'{super().__repr__()}{self._units[0]}'
        else:
            index = int(math.log(self, self.unit))
            return f'{self / self.unit ** index:.2f}{self._units[index]}'

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


def copyfileobj(src: IO, dst: IO, size: Optional[int] = None, chunk_size: Optional[int] = None,
                query_callback: Optional[Callable[[float], bool]] = None):
    size = size or sys.maxsize
    chunk_size = chunk_size or MAX_CHUNK
    ratio = 0
    while chunk := src.read(chunk_size):
        dst.write(chunk)
        ratio += len(chunk) / size
        if query_callback and not query_callback(ratio):
            break


def copy(src: str, dst: str, chunk_size: Optional[int] = None,
         query_callback: Optional[Callable[[float, ...], bool]] = None) -> bool:
    if os.path.exists(src):
        if not os.path.exists(dst):
            with contextlib.suppress(PermissionError):
                with open(src, 'rb') as src_:
                    os.makedirs(os.path.dirname(dst), exist_ok=True)
                    with open(dst, 'wb') as dst_:
                        copyfileobj(src_, dst_, os.path.getsize(src), chunk_size, query_callback)
        return os.path.exists(dst) and filecmp.cmp(src, dst)
    return False


def make_dir(path: str) -> bool:
    if os.path.exists(path) and not os.path.isdir(path):
        os.remove(path)
    os.makedirs(path, exist_ok=True)
    return os.path.isdir(path)


def is_only_dirs(path: str, recursive: bool = True) -> bool:
    if recursive:
        try:
            for dir_ in iter_dir(path):
                if os.path.isfile(dir_) or not is_only_dirs(dir_, recursive):
                    return False
        except PermissionError:
            return False
        return True
    return not any(os.scandir(path))


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
