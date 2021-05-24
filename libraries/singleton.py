import atexit
import hashlib
import os
import sys
import tempfile
import typing


def get_uid(path: str = os.path.normpath(sys.argv[0])) -> str:
    with open(path, 'rb') as file:
        return hashlib.md5(file.read()).hexdigest()


def init(name_hint: str = os.path.basename(sys.argv[0]),
         crash_callback: typing.Optional[typing.Callable] = None,
         exit_callback: typing.Optional[typing.Callable] = None,
         crash_callback_args: typing.Optional[tuple] = None,
         exit_callback_args: typing.Optional[tuple] = None,
         crash_callback_kwargs: typing.Optional[dict[str, typing.Any]] = None,
         exit_callback_kwargs: typing.Optional[dict[str, typing.Any]] = None) -> typing.Union[bool, typing.NoReturn]:
    crashed = False
    temp_dir = tempfile.gettempdir()
    os.makedirs(temp_dir, exist_ok=True)
    path = os.path.join(temp_dir, f'{name_hint}_{get_uid()}.lock')
    try:
        file = os.open(path, os.O_CREAT | os.O_EXCL)
    except FileExistsError:
        try:
            os.remove(path)
        except PermissionError:
            if exit_callback:
                exit_callback(*exit_callback_args or (), **exit_callback_kwargs or {})
            raise SystemExit
        else:
            if crash_callback:
                crash_callback(*crash_callback_args or (), **crash_callback_kwargs or {})
            file = os.open(path, os.O_CREAT | os.O_EXCL)
            crashed = True
    atexit.register(os.remove, path)
    atexit.register(os.close, file)
    return crashed
