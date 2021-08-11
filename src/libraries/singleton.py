__version__ = '0.0.3'

import atexit
import hashlib
import multiprocessing.shared_memory
import os
import socket
import sys
import tempfile
import time
from typing import Any, Callable, Iterable, Mapping, NoReturn, Optional

DELAY = 1
TIMEOUT = 5
MAX_CHUNK = 1024 * 1024
SUFFIX = '.lock'


def _wait_or_exit(end_time: float,
                  wait_callback: Optional[Callable],
                  wait_callback_args: Iterable,
                  wait_callback_kwargs: Mapping[str, Any],
                  exit_callback: Optional[Callable],
                  exit_callback_args: Iterable,
                  exit_callback_kwargs: Mapping[str, Any]) -> Optional[NoReturn]:
    if end_time > time.time():
        if wait_callback:
            wait_callback(*wait_callback_args, **wait_callback_kwargs)
        time.sleep(DELAY)
    else:
        if exit_callback:
            exit_callback(*exit_callback_args, **exit_callback_kwargs)
        raise SystemExit


def _file(uid: str,
          wait: bool,
          crash_callback: Optional[Callable],
          crash_callback_args: Iterable,
          crash_callback_kwargs: Mapping[str, Any],
          wait_callback: Optional[Callable],
          wait_callback_args: Iterable,
          wait_callback_kwargs: Mapping[str, Any],
          exit_callback: Optional[Callable],
          exit_callback_args: Iterable,
          exit_callback_kwargs: Mapping[str, Any]) -> Optional[NoReturn]:
    temp_dir = tempfile.gettempdir()
    os.makedirs(temp_dir, exist_ok=True)
    path = os.path.join(temp_dir, uid)
    flags = os.O_CREAT | os.O_EXCL
    end_time = time.time() + wait * TIMEOUT - DELAY
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


def _memory(uid: str,
            wait: bool,
            _: Any,
            __: Any,
            ___: Any,
            wait_callback: Optional[Callable],
            wait_callback_args: Iterable,
            wait_callback_kwargs: Mapping[str, Any],
            exit_callback: Optional[Callable],
            exit_callback_args: Iterable,
            exit_callback_kwargs: Mapping[str, Any]) -> Optional[NoReturn]:
    end_time = time.time() + wait * TIMEOUT - DELAY
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


def _socket(uid: str,
            wait: bool,
            _: Any,
            __: Any,
            ___: Any,
            wait_callback: Optional[Callable],
            wait_callback_args: Iterable,
            wait_callback_kwargs: Mapping[str, Any],
            exit_callback: Optional[Callable],
            exit_callback_args: Iterable,
            exit_callback_kwargs: Mapping[str, Any]) -> Optional[NoReturn]:
    address = socket.gethostname(), int.from_bytes(uid.encode(), sys.byteorder) % 48128 + 1024
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    end_time = time.time() + wait * TIMEOUT - DELAY
    while True:
        try:
            server.bind(address)
        except OSError:
            _wait_or_exit(end_time,
                          wait_callback, wait_callback_args, wait_callback_kwargs,
                          exit_callback, exit_callback_args, exit_callback_kwargs)
        else:
            atexit.register(server.close)
            break


class Method:
    FILE = _file
    MEMORY = _memory
    SOCKET = _socket


def _get_uid(path: Optional[str] = None,
             prefix: Optional[str] = None) -> str:
    md5 = hashlib.md5()
    with open(path or sys.argv[0], 'rb') as file:
        buffer = file.read(MAX_CHUNK)
        while buffer:
            md5.update(buffer)
            buffer = file.read(MAX_CHUNK)
    return f'{prefix or __name__}_{md5.hexdigest()}{SUFFIX}'


def init(name_prefix: Optional[str] = None,
         wait: Optional[bool] = None,
         crash_callback: Optional[Callable] = None,
         crash_callback_args: Optional[Iterable] = None,
         crash_callback_kwargs: Optional[Mapping[str, Any]] = None,
         wait_callback: Optional[Callable] = None,
         wait_callback_args: Optional[Iterable] = None,
         wait_callback_kwargs: Optional[Mapping[str, Any]] = None,
         exit_callback: Optional[Callable] = None,
         exit_callback_args: Optional[Iterable] = None,
         exit_callback_kwargs: Optional[Mapping[str, Any]] = None,
         method: Optional[Callable] = None) -> Optional[NoReturn]:
    (method or Method.FILE)(_get_uid(prefix=name_prefix), bool(wait),
                            crash_callback, crash_callback_args or (), crash_callback_kwargs or {},
                            wait_callback, wait_callback_args or (), wait_callback_kwargs or {},
                            exit_callback, exit_callback_args or (), exit_callback_kwargs or {})
