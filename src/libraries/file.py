__version__ = '0.0.5'

import contextlib
import filecmp
import glob
import os
import shutil
import time
import typing

DELAY = 0.01


def join(base: str,
         *children: str) -> str:
    return os.path.realpath(os.path.join(base, *children))


def get_size(path: str) -> int:
    size = 0
    for dir_ in os.listdir(path):
        path_ = os.path.join(path, dir_)
        size += get_size(path_) if os.path.isdir(path_) else os.path.getsize(path_)
    return size


def copy(src_path: str,
         dest_path: str) -> bool:
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    if os.path.exists(src_path):
        if not os.path.exists(dest_path):
            with contextlib.suppress(PermissionError):
                shutil.copyfile(src_path, dest_path)
        return os.path.exists(dest_path) and filecmp.cmp(src_path, dest_path)
    return False


def make_dir(path: str) -> bool:
    if os.path.exists(path) and not os.path.isdir(path):
        os.remove(path)
    os.makedirs(path, exist_ok=True)
    return os.path.isdir(path)


def is_empty(path: str,
             recursive: typing.Optional[bool] = None) -> bool:
    if recursive:
        for dir_ in os.listdir(path):
            path_ = os.path.join(path, dir_)
            if os.path.isfile(path_) or not is_empty(path_, recursive):
                return False
        return True
    return not any(os.scandir(path))


def trim(path: str,
         target: int,
         sort: typing.Optional[typing.Callable] = None) -> bool:
    trimmed = False
    if target:
        paths = glob.glob(os.path.join(path, '**'), recursive=True)
        paths.sort(key=sort or os.path.getctime)
        size = 0
        for path_ in paths:
            size_ = os.path.getsize(path_)
            if os.path.isfile(path_):
                if size + size_ > target:
                    os.remove(path_)
                    trimmed = True
                else:
                    size += size_
    else:
        shutil.rmtree(path, True)
        trimmed = True
    return trimmed


def remove(path: str,
           recursive: typing.Optional[bool] = None,
           timeout: typing.Optional[float] = None) -> bool:
    end_time = time.time() + (timeout or DELAY)
    exists = os.path.exists(path)
    while exists and end_time > time.time():
        shutil.rmtree(path, True) if recursive else os.remove(path)
        time.sleep(DELAY)
        exists = os.path.exists(path)
    return not exists
