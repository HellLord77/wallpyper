import contextlib
import filecmp
import os
import shutil


def join(*paths: str) -> str:
    return os.path.join(*paths)


def exists(path: str) -> bool:
    return os.path.isfile(path)


def copy(src_path: str,
         dest_path: str) -> bool:
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    if exists(src_path):
        if not exists(dest_path):
            with contextlib.suppress(PermissionError):
                shutil.copyfile(src_path, dest_path)
        return exists(dest_path) and filecmp.cmp(src_path, dest_path)
    return False


def remove(path: str) -> bool:
    if exists(path):
        os.remove(path)
    return exists(path)


def remove_tree(path: str) -> bool:
    shutil.rmtree(path, True)
    return not exists(path)
