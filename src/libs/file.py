__version__ = '0.0.7'

import contextlib
import filecmp
import glob
import os
import shutil
import sys
import time
from typing import Any, Callable, Generator, IO, Iterable, Mapping, Optional

DELAY = 0.01
CHUNK = 1024 * 1024


def join(base: str, *children: str) -> str:
    return os.path.realpath(os.path.join(base, *children))


def replace_ext(path: str, ext: str) -> str:
    return f'{os.path.splitext(path)[0]}.{ext}'


def iter_files(paths: Iterable[str]) -> Generator[str, None, None]:
    for path in paths:
        if os.path.isfile(path):
            yield path


def iter_dir(path: str) -> Generator[str, None, None]:
    dir_: os.DirEntry
    for dir_ in os.scandir(path):
        yield os.path.realpath(dir_.path)


def get_size(path: str) -> int:
    size = 0
    for dir_ in os.listdir(path):
        path_ = os.path.join(path, dir_)
        size += get_size(path_) if os.path.isdir(path_) else os.path.getsize(path_)
    return size


def copyfileobj(src: IO, dst: IO, size: Optional[int] = None, chunk_size: Optional[int] = None,
                callback: Optional[Callable[[int, ...], Any]] = None, args: Optional[Iterable] = None,
                kwargs: Optional[Mapping[str, Any]] = None):
    read = src.read
    write = dst.write
    size = size or sys.maxsize
    chunk_size = chunk_size or CHUNK
    args = () if args is None else {}
    kwargs = {} if kwargs is None else kwargs
    ratio = 0
    chunk = read(chunk_size)
    while chunk:
        write(chunk)
        ratio += len(chunk) / size
        if callback:
            callback(round(ratio * 100), *args, **kwargs)
        chunk = read(chunk_size)


def copy(src_path: str, dest_path: str, chunk_size: Optional[int] = None,
         callback: Optional[Callable[[int, ...], Any]] = None, args: Optional[Iterable] = None,
         kwargs: Optional[Mapping[str, Any]] = None) -> bool:
    if os.path.exists(src_path):
        if not os.path.exists(dest_path):
            with contextlib.suppress(PermissionError):
                with open(src_path, 'rb') as src:
                    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                    with open(dest_path, 'wb') as dst:
                        copyfileobj(src, dst, os.path.getsize(src_path), chunk_size, callback, args, kwargs)
        return os.path.exists(dest_path) and filecmp.cmp(src_path, dest_path)
    return False


def make_dir(path: str) -> bool:
    if os.path.exists(path) and not os.path.isdir(path):
        os.remove(path)
    os.makedirs(path, exist_ok=True)
    return os.path.isdir(path)


def is_empty(path: str, recursive: Optional[bool] = None) -> bool:
    if recursive:
        for dir_ in os.listdir(path):
            path_ = os.path.join(path, dir_)
            if os.path.isfile(path_) or not is_empty(path_, recursive):
                return False
        return True
    return not any(os.scandir(path))


def trim(path: str, target: int) -> bool:
    trimmed = False
    paths = glob.glob(os.path.join(path, '**'), recursive=True)
    paths.sort(key=os.path.getctime, reverse=True)
    itt = iter_files(paths)
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


def remove(path: str, recursive: Optional[bool] = None, timeout: Optional[float] = None) -> bool:
    tried = False
    end_time = time.time() + (timeout or 0)
    while not tried or end_time > time.time():
        with contextlib.suppress(PermissionError):
            try:
                shutil.rmtree(path) if recursive else os.remove(path)
            except (FileNotFoundError, NotADirectoryError):
                break
        tried = True
        time.sleep(DELAY)
    return not os.path.exists(path)
