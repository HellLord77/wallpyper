import atexit
import hashlib
import os
import sys
import tempfile
import time
import typing

DELAY = 1
MAX_WAIT = 5


def get_uid(path: str = os.path.normpath(sys.argv[0])) -> str:
    with open(path, 'rb') as file:
        return hashlib.md5(file.read()).hexdigest()


def init(name_prefix: str = os.path.basename(sys.argv[0]),
         wait: typing.Optional[bool] = None,
         crash_callback: typing.Optional[typing.Callable] = None,
         crash_callback_args: typing.Optional[tuple] = None,
         crash_callback_kwargs: typing.Optional[dict[str, typing.Any]] = None,
         wait_callback: typing.Optional[typing.Callable] = None,
         wait_callback_args: typing.Optional[tuple] = None,
         wait_callback_kwargs: typing.Optional[dict[str, typing.Any]] = None,
         exit_callback: typing.Optional[typing.Callable] = None,
         exit_callback_args: typing.Optional[tuple] = None,
         exit_callback_kwargs: typing.Optional[dict[str, typing.Any]] = None) -> typing.Optional[typing.NoReturn]:
    temp_dir = tempfile.gettempdir()
    os.makedirs(temp_dir, exist_ok=True)
    file_path = os.path.join(temp_dir, f'{name_prefix}_{get_uid()}.lock')
    retry = True
    end_time = time.time() + (wait or False) * MAX_WAIT - DELAY
    while retry:
        try:
            file = os.open(file_path, os.O_CREAT | os.O_EXCL)
        except FileExistsError:
            try:
                os.remove(file_path)
            except PermissionError:
                retry = end_time > time.time()
                if retry:
                    if wait_callback:
                        wait_callback(*wait_callback_args or (), **wait_callback_kwargs or {})
                    time.sleep(DELAY)
                    continue
                if exit_callback:
                    exit_callback(*exit_callback_args or (), **exit_callback_kwargs or {})
                raise SystemExit
            else:
                if crash_callback:
                    crash_callback(*crash_callback_args or (), **crash_callback_kwargs or {})
                continue
        retry = False
        atexit.register(os.remove, file_path)
        atexit.register(os.close, file)

# TODO: add com, mutex method
