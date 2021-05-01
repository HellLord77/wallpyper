import atexit
import hashlib
import os
import sys
import tempfile
import typing


# noinspection PyUnusedLocal
def _dummy_function(*args: typing.Any,
                    **kwargs: typing.Any) -> None:
    pass


def get_uid(path: str = os.path.normpath(sys.argv[0])) -> str:
    with open(path, 'rb') as file:
        return hashlib.md5(file.read()).hexdigest()


# noinspection PyDefaultArgument
def init(name_hint: str = os.path.basename(sys.argv[0]),
         crash_callback: typing.Callable = _dummy_function,
         exit_callback: typing.Callable = _dummy_function,
         crash_callback_args: tuple = (),
         exit_callback_args: tuple = (),
         crash_callback_kwargs: dict[str, typing.Any] = {},
         exit_callback_kwargs: dict[str, typing.Any] = {}) -> typing.Union[bool, typing.NoReturn]:
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
            exit_callback(*exit_callback_args, **exit_callback_kwargs)
            raise SystemExit
        else:
            crash_callback(*crash_callback_args, **crash_callback_kwargs)
            file = os.open(path, os.O_CREAT | os.O_EXCL)
            crashed = True
    atexit.register(os.remove, path)
    atexit.register(os.close, file)
    return crashed
