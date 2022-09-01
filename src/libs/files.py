__version__ = '0.0.9'

import contextlib
import filecmp
import glob
import os
import shutil
import sys
import time
from typing import Any, Callable, Generator, IO, Iterable, Mapping, Optional

# noinspection PyUnresolvedReferences
CHUNK = shutil.COPY_BUFSIZE
POLL_INTERVAL = 0.1


class File:
    __slots__ = 'url', 'name', 'size', 'md5', 'sha256'

    def __init__(self, url: str, name: str, size: Optional[int] = None,
                 md5: Optional[bytes] = None, sha256: Optional[bytes] = None):
        self.url = url
        self.name = name
        self.size = size
        self.md5 = md5
        self.sha256 = sha256

    def __bool__(self):
        return bool(str(self))

    def __str__(self):
        return self.url

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))


def remove_ext(path: str) -> str:
    return os.path.splitext(path)[0]


def replace_ext(path: str, ext: str) -> str:
    return f'{os.path.splitext(path)[0]}.{ext}'


def iter_dir(path: str) -> Generator[str, None, None]:
    dir_: os.DirEntry
    for dir_ in os.scandir(path):
        yield os.path.realpath(dir_.path)


def get_size(path: str) -> Optional[int]:
    if os.path.isdir(path):
        return sum(get_size(dir_) for dir_ in iter_dir(path))
    elif os.path.isfile(path):
        return os.path.getsize(path)


def copyfileobj(src: IO, dst: IO, size: Optional[int] = None,
                chunk_size: Optional[int] = None, query_callback: Optional[Callable[[int, ...], bool]] = None,
                args: Optional[Iterable] = None, kwargs: Optional[Mapping[str, Any]] = None):
    size = size or sys.maxsize
    chunk_size = chunk_size or CHUNK
    args = () if args is None else args
    kwargs = {} if kwargs is None else kwargs
    ratio = 0
    while chunk := src.read(chunk_size):
        dst.write(chunk)
        ratio += len(chunk) / size
        if query_callback and not query_callback(round(ratio * 100), *args, **kwargs):
            break


def copy(src_path: str, dst_path: str,
         chunk_size: Optional[int] = None, query_callback: Optional[Callable[[int, ...], bool]] = None,
         args: Optional[Iterable] = None, kwargs: Optional[Mapping[str, Any]] = None) -> bool:
    if os.path.exists(src_path):
        if not os.path.exists(dst_path):
            with contextlib.suppress(PermissionError):
                with open(src_path, 'rb') as src:
                    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
                    with open(dst_path, 'wb') as dst:
                        copyfileobj(src, dst, os.path.getsize(src_path), chunk_size, query_callback, args, kwargs)
        return os.path.exists(dst_path) and filecmp.cmp(src_path, dst_path)
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
