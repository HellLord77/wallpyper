import atexit
import hashlib
import multiprocessing.shared_memory
import os
import random
import socket
import sys
import tempfile
import time
import typing


def _wait_or_exit(end_time: float,
                  wait_callback: typing.Callable,
                  wait_callback_args: tuple,
                  wait_callback_kwargs: dict[str, typing.Any],
                  exit_callback: typing.Callable,
                  exit_callback_args: tuple,
                  exit_callback_kwargs: dict[str, typing.Any]) -> typing.Optional[typing.NoReturn]:
    if end_time > time.time():
        wait_callback(*wait_callback_args, **wait_callback_kwargs)
        time.sleep(DELAY)
    else:
        exit_callback(*exit_callback_args, **exit_callback_kwargs)
        raise SystemExit


def method_file(name_prefix: str,
                wait: bool,
                crash_callback: typing.Callable,
                crash_callback_args: tuple,
                crash_callback_kwargs: dict[str, typing.Any],
                wait_callback: typing.Callable,
                wait_callback_args: tuple,
                wait_callback_kwargs: dict[str, typing.Any],
                exit_callback: typing.Callable,
                exit_callback_args: tuple,
                exit_callback_kwargs: dict[str, typing.Any]) -> typing.Optional[typing.NoReturn]:
    temp_dir = tempfile.gettempdir()
    os.makedirs(temp_dir, exist_ok=True)
    path = os.path.join(temp_dir, get_uid(prefix=name_prefix))
    flags = os.O_CREAT | os.O_EXCL
    end_time = time.time() + (wait or False) * MAX_WAIT - DELAY
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
                continue
            else:
                crash_callback(*crash_callback_args, **crash_callback_kwargs)
                continue
        atexit.register(os.remove, path)
        atexit.register(os.close, file)
        break


def method_memory(name_prefix: str,
                  wait: bool,
                  _: typing.Callable,
                  __: tuple,
                  ___: dict[str, typing.Any],
                  wait_callback: typing.Callable,
                  wait_callback_args: tuple,
                  wait_callback_kwargs: dict[str, typing.Any],
                  exit_callback: typing.Callable,
                  exit_callback_args: tuple,
                  exit_callback_kwargs: dict[str, typing.Any]) -> typing.Optional[typing.NoReturn]:
    name = get_uid(prefix=name_prefix)
    end_time = time.time() + (wait or False) * MAX_WAIT - DELAY
    while True:
        try:
            memory = multiprocessing.shared_memory.SharedMemory(name, True, 1)
        except FileExistsError:
            _wait_or_exit(end_time,
                          wait_callback, wait_callback_args, wait_callback_kwargs,
                          exit_callback, exit_callback_args, exit_callback_kwargs)
            continue
        atexit.register(memory.unlink)
        atexit.register(memory.close)
        break


def method_port(name_prefix: str,
                wait: bool,
                _: typing.Callable,
                __: tuple,
                ___: dict[str, typing.Any],
                wait_callback: typing.Callable,
                wait_callback_args: tuple,
                wait_callback_kwargs: dict[str, typing.Any],
                exit_callback: typing.Callable,
                exit_callback_args: tuple,
                exit_callback_kwargs: dict[str, typing.Any]) -> typing.Optional[typing.NoReturn]:
    random.seed(get_uid(prefix=name_prefix))
    address = socket.gethostname(), random.randint(1024, 49152)
    socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    end_time = time.time() + (wait or False) * MAX_WAIT - DELAY
    while True:
        try:
            socket_.bind(address)
        except OSError:
            _wait_or_exit(end_time,
                          wait_callback, wait_callback_args, wait_callback_kwargs,
                          exit_callback, exit_callback_args, exit_callback_kwargs)
            continue
        atexit.register(socket_.close)
        break


DELAY = 1
MAX_WAIT = 5
METHOD = method_file


def get_uid(path: str = os.path.normpath(sys.argv[0]),
            prefix: typing.Optional[str] = None) -> str:
    with open(path, 'rb') as file:
        return f'{prefix or ""}_{hashlib.md5(file.read()).hexdigest()}.lock'


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
    METHOD(name_prefix, bool(wait),
           crash_callback or (lambda: None), crash_callback_args or (), crash_callback_kwargs or {},
           wait_callback or (lambda: None), wait_callback_args or (), wait_callback_kwargs or {},
           exit_callback or (lambda: None), exit_callback_args or (), exit_callback_kwargs or {})
