import filecmp
import os
import shutil


def exists(path: str) -> bool:
    return os.path.isfile(path)


def copy(src_path: str,
         dest_path: str) -> bool:
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    try:
        shutil.copyfile(src_path, dest_path)
    except (FileNotFoundError, PermissionError):
        pass
    try:
        return filecmp.cmp(src_path, dest_path)
    except FileNotFoundError:
        pass
    return False


def remove(path: str) -> bool:
    if os.path.isfile(path):
        os.remove(path)
    return os.path.isfile(path)
