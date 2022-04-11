__version__ = '0.0.4'  # TODO send signal and kill if no reply, check error code & crash

import atexit
import hashlib
import multiprocessing.shared_memory
import os
import socket
import sys
import tempfile
import time
from typing import Any, Callable, Iterable, Mapping, NoReturn, Optional, Union

WAIT_INTERVAL = 5
POLL_INTERVAL = 1
MAX_CHUNK = 1024 * 1024
SUFFIX = '.lock'


def _wait_or_exit(end_time: float, on_wait: Optional[Callable], on_wait_args: Iterable,
                  on_wait_kwargs: Mapping[str, Any], on_exit: Optional[Callable], on_exit_args: Iterable,
                  on_exit_kwargs: Mapping[str, Any]) -> Optional[NoReturn]:
    if end_time > time.time():
        if on_wait:
            on_wait(*on_wait_args, **on_wait_kwargs)
        time.sleep(POLL_INTERVAL)
    else:
        if on_exit:
            on_exit(*on_exit_args, **on_exit_kwargs)
        raise SystemExit


def _file(uid: str, wait: bool, on_crash: Optional[Callable], on_crash_args: Iterable,
          on_crash_kwargs: Mapping[str, Any], on_wait: Optional[Callable], on_wait_args: Iterable,
          on_wait_kwargs: Mapping[str, Any], on_exit: Optional[Callable], on_exit_args: Iterable,
          on_exit_kwargs: Mapping[str, Any]) -> Optional[NoReturn]:
    temp_dir = tempfile.gettempdir()
    os.makedirs(temp_dir, exist_ok=True)
    path = os.path.join(temp_dir, uid)
    flags = os.O_CREAT | os.O_EXCL
    end_time = time.time() + wait * WAIT_INTERVAL - POLL_INTERVAL
    while True:
        try:
            file = os.open(path, flags)
        except FileExistsError:
            try:
                os.remove(path)
            except PermissionError:
                _wait_or_exit(end_time, on_wait, on_wait_args, on_wait_kwargs, on_exit, on_exit_args, on_exit_kwargs)
            else:
                if on_crash:
                    on_crash(*on_crash_args, **on_crash_kwargs)
        else:
            atexit.register(os.remove, path)
            atexit.register(os.close, file)
            break


def _memory(uid: str, wait: bool, _, __, ___, on_wait: Optional[Callable], on_wait_args: Iterable,
            on_wait_kwargs: Mapping[str, Any], on_exit: Optional[Callable], on_exit_args: Iterable,
            on_exit_kwargs: Mapping[str, Any]) -> Optional[NoReturn]:
    end_time = time.time() + wait * WAIT_INTERVAL - POLL_INTERVAL
    while True:
        try:
            memory = multiprocessing.shared_memory.SharedMemory(uid, True, 1)
        except FileExistsError:
            _wait_or_exit(end_time, on_wait, on_wait_args, on_wait_kwargs, on_exit, on_exit_args, on_exit_kwargs)
        else:
            atexit.register(memory.unlink)
            atexit.register(memory.close)
            break


def _socket(uid: str, wait: bool, _, __, ___, on_wait: Optional[Callable], on_wait_args: Iterable,
            on_wait_kwargs: Mapping[str, Any], on_exit: Optional[Callable], on_exit_args: Iterable,
            on_exit_kwargs: Mapping[str, Any]) -> Optional[NoReturn]:
    address = socket.gethostname(), int.from_bytes(uid.encode(), sys.byteorder) % 48128 + 1024
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    end_time = time.time() + wait * WAIT_INTERVAL - POLL_INTERVAL
    while True:
        try:
            server.bind(address)
        except OSError:
            _wait_or_exit(end_time, on_wait, on_wait_args, on_wait_kwargs, on_exit, on_exit_args, on_exit_kwargs)
        else:
            atexit.register(server.close)
            break


class Method:
    FILE = _file
    MEMORY = _memory
    SOCKET = _socket


def _get_uid(data_or_path: Union[bytes, str], prefix: Optional[str] = None) -> str:
    md5 = hashlib.md5()
    if isinstance(data_or_path, bytes):
        md5.update(data_or_path)
    elif os.path.isfile(data_or_path):
        with open(data_or_path or sys.argv[0], 'rb') as file:
            while buffer := file.read(MAX_CHUNK):
                md5.update(buffer)
    return f'{prefix or __name__}_{md5.hexdigest()}{SUFFIX}'


def init(uuid: str, uid_prefix: Optional[str] = None, wait: bool = False, on_crash: Optional[Callable] = None,
         on_crash_args: Optional[Iterable] = None, on_crash_kwargs: Optional[Mapping[str, Any]] = None,
         on_wait: Optional[Callable] = None, on_wait_args: Optional[Iterable] = None,
         on_wait_kwargs: Optional[Mapping[str, Any]] = None, on_exit: Optional[Callable] = None,
         on_exit_args: Optional[Iterable] = None, on_exit_kwargs: Optional[Mapping[str, Any]] = None,
         method: Callable = Method.FILE) -> Optional[NoReturn]:
    method(_get_uid(uuid.encode(), uid_prefix), wait, on_crash, () if on_crash_args is None else on_crash_args,
           {} if on_crash_kwargs is None else on_crash_kwargs, on_wait, () if on_wait_args is None else on_wait_args,
           {} if on_wait_kwargs is None else on_wait_kwargs, on_exit, () if on_exit_args is None else on_exit_args,
           {} if on_exit_kwargs is None else on_exit_args)
