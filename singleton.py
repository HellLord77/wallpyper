import atexit
import os
import tempfile
from hashlib import md5
from sys import argv
from typing import Any, Callable, Iterable, Mapping


# noinspection PyUnusedLocal
def _hook(*args: Any, **kwargs: Any) -> None:
    pass


def _uid(path: str = argv[0]) -> str:
    with open(path, 'rb') as file:
        return md5(file.read()).hexdigest()


def init(uid: str = _uid(),
         crash_hook: Callable = _hook, crash_hook_args: Iterable = (), crash_hook_kwargs: Mapping = None,
         exit_hook: Callable = _hook, exit_hook_args: Iterable = (), exit_hook_kwargs: Mapping = None) -> None:
    temp_dir = tempfile.gettempdir()
    os.makedirs(temp_dir, exist_ok=True)
    path = os.path.join(temp_dir, uid)
    flags = os.O_CREAT | os.O_EXCL
    try:
        file = os.open(path, flags)
    except FileExistsError:
        try:
            os.remove(path)
        except PermissionError:
            exit_hook(*exit_hook_args, **exit_hook_kwargs or {})
            raise SystemExit
        else:
            crash_hook(*crash_hook_args, **crash_hook_kwargs or {})
            file = os.open(path, flags)
    atexit.register(os.remove, path)
    atexit.register(os.close, file)
