__version__ = '0.0.7'  # TODO send signal and kill if no reply, check error code & crash

import atexit
import enum
import hashlib
import multiprocessing.shared_memory
import os
import shutil
import socket
import sys
import tempfile
import time
import uuid
from typing import AnyStr
from typing import Callable
from typing import NoReturn
from typing import Optional

WAIT_INTERVAL = 5
POLL_INTERVAL = 1
# noinspection PyUnresolvedReferences
MAX_CHUNK = shutil.COPY_BUFSIZE
SUFFIX = '.lock'


def _not_crashed(end_time: float, on_waiting: Optional[Callable],
                 on_exiting: Optional[Callable]) -> Optional[NoReturn]:
    if end_time > time.monotonic():
        if on_waiting is not None:
            on_waiting()
        time.sleep(POLL_INTERVAL)
    else:
        if on_exiting is not None:
            on_exiting()
        raise SystemExit


def _file(uid: str, wait: bool, on_crashed: Optional[Callable],
          on_waiting: Optional[Callable], on_exiting: Optional[Callable]) -> Optional[NoReturn]:
    temp_dir = tempfile.gettempdir()
    os.makedirs(temp_dir, exist_ok=True)
    path = os.path.join(temp_dir, uid)
    flags = os.O_CREAT | os.O_EXCL
    end_time = time.monotonic() + wait * WAIT_INTERVAL
    while True:
        try:
            file = os.open(path, flags)
        except FileExistsError:
            try:
                os.remove(path)
            except PermissionError:
                _not_crashed(end_time, on_waiting, on_exiting)
            else:
                if on_crashed is not None:
                    on_crashed()
        else:
            atexit.register(os.remove, path)
            atexit.register(os.close, file)
            break


def _memory(uid: str, wait: bool, _, on_waiting: Optional[Callable],
            on_exiting: Optional[Callable]) -> Optional[NoReturn]:
    end_time = time.monotonic() + wait * WAIT_INTERVAL
    while True:
        try:
            memory = multiprocessing.shared_memory.SharedMemory(uid, True, 1)
        except FileExistsError:
            _not_crashed(end_time, on_waiting, on_exiting)
        else:
            atexit.register(memory.unlink)
            atexit.register(memory.close)
            break


def _socket(uid: str, wait: bool, _, on_waiting: Optional[Callable],
            on_exiting: Optional[Callable]) -> Optional[NoReturn]:
    address = socket.gethostname(), int.from_bytes(
        uid.encode(), sys.byteorder) % 48128 + 1024
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    end_time = time.monotonic() + wait * WAIT_INTERVAL
    while True:
        try:
            server.bind(address)
        except OSError:
            _not_crashed(end_time, on_waiting, on_exiting)
        else:
            atexit.register(server.close)
            break


class Method(enum.Enum):
    FILE = enum.member(_file)
    MEMORY = enum.member(_memory)
    SOCKET = enum.member(_socket)


def _get_uid(data_or_path: bytes | bytearray, prefix: Optional[str]) -> str:
    md5 = hashlib.md5(data_or_path)
    if os.path.isfile(data_or_path):
        with open(data_or_path or sys.argv[0], 'rb') as file:
            while buffer := file.read(MAX_CHUNK):
                md5.update(buffer)
    prefix = '' if prefix is None else f'{prefix}_'
    return f'{prefix}{md5.hexdigest()}{SUFFIX}'


def init(uid: bytearray | uuid.UUID | AnyStr, uid_prefix: Optional[str] = __name__,
         wait: bool = False, on_crashed: Optional[Callable] = None, on_waiting: Optional[Callable] = None,
         on_exiting: Optional[Callable] = None, method: Method = Method.FILE) -> Optional[NoReturn]:
    if isinstance(uid, uuid.UUID):
        uid = uid.bytes
    elif isinstance(uid, str):
        uid = uid.encode()
    method.value(_get_uid(uid, uid_prefix), wait, on_crashed, on_waiting, on_exiting)
