__version__ = '0.0.3'

import contextlib
import filecmp
import os
import shutil
import time
import typing

DELAY = 0.01


def join(base: str,
         *children: str) -> str:
    return os.path.realpath(os.path.join(base, *children))


def copy(src_path: str,
         dest_path: str) -> bool:
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    if os.path.exists(src_path):
        if not os.path.exists(dest_path):
            with contextlib.suppress(PermissionError):
                shutil.copyfile(src_path, dest_path)
        return os.path.exists(dest_path) and filecmp.cmp(src_path, dest_path)
    return False


def remove(path: str) -> bool:
    if os.path.exists(path):
        os.remove(path)
    return os.path.exists(path)


def remove_tree(path: str,
                timeout: typing.Optional[float] = None) -> bool:
    end_time = time.time() + (timeout or DELAY)
    exists = os.path.exists(path)
    while exists and end_time > time.time():
        shutil.rmtree(path, True)
        time.sleep(DELAY)
        exists = os.path.exists(path)
    return not exists
