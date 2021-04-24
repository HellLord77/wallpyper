import filecmp
import os
import shutil
import typing

import libs.request


# TODO: move all typing here
# TODO: dynamically load modules with PyCharm stubs

def log(msg: typing.Any) -> None:
    print(f"[!] {msg}")


def exists_file(path: str) -> bool:
    return os.path.isfile(path)


def copy_file(src_path: str, dest_path: str) -> bool:
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    if not os.path.exists(dest_path):
        try:
            shutil.copyfile(src_path, dest_path)
        except FileNotFoundError as err:
            log(err)
        except PermissionError as err:
            log(err)
    else:
        log(f"FileExistsError: '{dest_path}'")
    try:
        if filecmp.cmp(src_path, dest_path):
            return True
        else:
            log(f"MismatchError: '{src_path}' '{dest_path}'")
    except FileNotFoundError as err:
        log(err)
    return False


def delete_file(path: str) -> bool:
    if os.path.isfile(path):
        os.remove(path)
    return os.path.isfile(path)


join_url = libs.request.urljoin
open_url = libs.request.urlopen
download_url = libs.request.urlretrieve
