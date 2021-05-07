import filecmp
import os
import shutil


def exists(path: str) -> bool:
    return os.path.isfile(path)


def copy(src_path: str,
         dest_path: str) -> bool:
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    if os.path.isfile(src_path) and not os.path.exists(dest_path):
        try:
            shutil.copyfile(src_path, dest_path)
        except PermissionError:
            pass
    if os.path.isfile(src_path) and os.path.isfile(dest_path):
        return filecmp.cmp(src_path, dest_path)
    return False


def remove(path: str) -> bool:
    if os.path.isfile(path):
        os.remove(path)
    return os.path.isfile(path)


def remove_tree(path: str) -> bool:
    shutil.rmtree(path, True)
    return not os.path.exists(path)
