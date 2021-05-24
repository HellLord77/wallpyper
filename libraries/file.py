import filecmp
import os
import shutil


def exists(path: str) -> bool:
    return os.path.isfile(path)


def copy(src_path: str,
         dest_dir: str,
         *file_names: str) -> bool:
    os.makedirs(dest_dir, exist_ok=True)
    if os.path.isfile(src_path):
        for file_name in file_names:
            dest_path = os.path.join(dest_dir, file_name)
            if not os.path.exists(dest_path):
                try:
                    shutil.copyfile(src_path, dest_path)
                except PermissionError:
                    pass
            if os.path.isfile(dest_path) and filecmp.cmp(src_path, dest_path):
                return True
    return False


def remove(path: str) -> bool:
    if os.path.isfile(path):
        os.remove(path)
    return os.path.isfile(path)


def remove_tree(path: str) -> bool:
    shutil.rmtree(path, True)
    return not os.path.exists(path)
