import atexit
import multiprocessing.shared_memory
import os
import socket
import sys
import tempfile
import time
import typing
import zlib

DELAY = 1
MAX_WAIT = 5


def _wait_or_exit(end_time: float,
                  wait_callback: typing.Optional[typing.Callable],
                  wait_callback_args: tuple,
                  wait_callback_kwargs: dict[str, typing.Any],
                  exit_callback: typing.Optional[typing.Callable],
                  exit_callback_args: tuple,
                  exit_callback_kwargs: dict[str, typing.Any]) -> typing.Optional[typing.NoReturn]:
    if end_time > time.time():
        if wait_callback:
            wait_callback(*wait_callback_args, **wait_callback_kwargs)
        time.sleep(DELAY)
    else:
        if exit_callback:
            exit_callback(*exit_callback_args, **exit_callback_kwargs)
        raise SystemExit


class Method:
    @staticmethod
    def file(uid: str,
             wait: bool,
             crash_callback: typing.Optional[typing.Callable],
             crash_callback_args: tuple,
             crash_callback_kwargs: dict[str, typing.Any],
             wait_callback: typing.Optional[typing.Callable],
             wait_callback_args: tuple,
             wait_callback_kwargs: dict[str, typing.Any],
             exit_callback: typing.Optional[typing.Callable],
             exit_callback_args: tuple,
             exit_callback_kwargs: dict[str, typing.Any]) -> typing.Optional[typing.NoReturn]:
        temp_dir = tempfile.gettempdir()
        os.makedirs(temp_dir, exist_ok=True)
        path = os.path.join(temp_dir, uid)
        flags = os.O_CREAT | os.O_EXCL
        end_time = time.time() + wait * MAX_WAIT - DELAY
        while True:
            try:
                file = os.open(path, flags)
            except FileExistsError:
                try:
                    os.remove(path)
                except PermissionError:
                    _wait_or_exit(end_time,
                                  wait_callback, wait_callback_args, wait_callback_kwargs,
                                  exit_callback, exit_callback_args, exit_callback_kwargs)
                else:
                    if crash_callback:
                        crash_callback(*crash_callback_args, **crash_callback_kwargs)
            else:
                atexit.register(os.remove, path)
                atexit.register(os.close, file)
                break

    @staticmethod
    def memory(uid: str,
               wait: bool,
               _: typing.Optional[typing.Callable],
               __: tuple,
               ___: dict[str, typing.Any],
               wait_callback: typing.Optional[typing.Callable],
               wait_callback_args: tuple,
               wait_callback_kwargs: dict[str, typing.Any],
               exit_callback: typing.Optional[typing.Callable],
               exit_callback_args: tuple,
               exit_callback_kwargs: dict[str, typing.Any]) -> typing.Optional[typing.NoReturn]:
        end_time = time.time() + wait * MAX_WAIT - DELAY
        while True:
            try:
                memory = multiprocessing.shared_memory.SharedMemory(uid, True, 1)
            except FileExistsError:
                _wait_or_exit(end_time,
                              wait_callback, wait_callback_args, wait_callback_kwargs,
                              exit_callback, exit_callback_args, exit_callback_kwargs)
            else:
                atexit.register(memory.unlink)
                atexit.register(memory.close)
                break

    @staticmethod
    def port(uid: str,
             wait: bool,
             _: typing.Optional[typing.Callable],
             __: tuple,
             ___: dict[str, typing.Any],
             wait_callback: typing.Optional[typing.Callable],
             wait_callback_args: tuple,
             wait_callback_kwargs: dict[str, typing.Any],
             exit_callback: typing.Optional[typing.Callable],
             exit_callback_args: tuple,
             exit_callback_kwargs: dict[str, typing.Any]) -> typing.Optional[typing.NoReturn]:
        address = socket.gethostname(), int.from_bytes(uid.encode(), 'big') % 48128 + 1024
        socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        end_time = time.time() + wait * MAX_WAIT - DELAY
        while True:
            try:
                socket_.bind(address)
            except OSError:
                _wait_or_exit(end_time,
                              wait_callback, wait_callback_args, wait_callback_kwargs,
                              exit_callback, exit_callback_args, exit_callback_kwargs)
            else:
                atexit.register(socket_.close)
                break


def get_uid(path: str = sys.argv[0],
            prefix: typing.Optional[str] = None) -> str:
    with open(path, 'rb') as file:
        return f'{prefix or __name__}_{zlib.adler32(file.read())}.lock'


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
         exit_callback_kwargs: typing.Optional[dict[str, typing.Any]] = None,
         method: typing.Optional[typing.Callable] = None) -> typing.Optional[typing.NoReturn]:
    (method or Method.file)(get_uid(prefix=name_prefix), bool(wait),
                            crash_callback, crash_callback_args or (), crash_callback_kwargs or {},
                            wait_callback, wait_callback_args or (), wait_callback_kwargs or {},
                            exit_callback, exit_callback_args or (), exit_callback_kwargs or {})
