import atexit
import hashlib
import os
import sys
import tempfile
import typing


# noinspection PyUnusedLocal
def _hook(*args: typing.Any,
          **kwargs: typing.Any) -> None:
    pass


def uid(path: str = os.path.normpath(sys.argv[0])) -> str:
    with open(path, 'rb') as file:
        return hashlib.md5(file.read()).hexdigest()


# noinspection PyDefaultArgument
def init(name_hint: str = os.path.basename(sys.argv[0]),
         crash_hook: typing.Callable = _hook,
         exit_hook: typing.Callable = _hook,
         crash_hook_args: typing.Iterable = (),
         exit_hook_args: typing.Iterable = (),
         crash_hook_kwargs: typing.Mapping[str, typing.Any] = {},
         exit_hook_kwargs: typing.Mapping[str, typing.Any] = {}) -> typing.Union[bool, typing.NoReturn]:
    crashed = False
    temp_dir = tempfile.gettempdir()
    os.makedirs(temp_dir, exist_ok=True)
    path = os.path.join(temp_dir, f'{name_hint}_{uid()}.lock')
    try:
        file = os.open(path, os.O_CREAT | os.O_EXCL)
    except FileExistsError:
        try:
            os.remove(path)
        except PermissionError:
            exit_hook(*exit_hook_args, **exit_hook_kwargs)
            raise SystemExit
        else:
            crash_hook(*crash_hook_args, **crash_hook_kwargs)
            file = os.open(path, os.O_CREAT | os.O_EXCL)
            crashed = True
    atexit.register(os.remove, path)
    atexit.register(os.close, file)
    return crashed
