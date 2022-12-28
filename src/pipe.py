from __future__ import annotations as _

import ctypes
import ntpath
import os
import sys
import time
from typing import Optional, TextIO


# FIXME Fatal Python error: init_fs_encoding: failed to get the Python codec of the filesystem encoding (3.11)

# noinspection PyPep8Naming
class ctyped:
    sizeof = ctypes.sizeof
    byref = ctypes.byref
    lib = ctypes.windll

    lib.kernel32.GetLastError.restype = ctypes.c_ulong
    lib.kernel32.GetLastError.argtypes = ()

    lib.kernel32.FlushFileBuffers.restype = ctypes.c_int
    lib.kernel32.FlushFileBuffers.argtypes = ctypes.c_void_p,

    lib.kernel32.WriteFile.restype = ctypes.c_int
    lib.kernel32.WriteFile.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_ulong, ctypes.POINTER(ctypes.c_ulong), ctypes.c_void_p)

    lib.kernel32.CreateFileW.restype = ctypes.c_void_p
    lib.kernel32.CreateFileW.argtypes = (ctypes.c_wchar_p, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_void_p, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_void_p)

    lib.kernel32.ReadFile.restype = ctypes.c_int
    lib.kernel32.ReadFile.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_ulong, ctypes.POINTER(ctypes.c_ulong), ctypes.c_void_p)

    lib.kernel32.CloseHandle.restype = ctypes.c_int
    lib.kernel32.CloseHandle.argtypes = ctypes.c_void_p,

    lib.kernel32.ConnectNamedPipe.restype = ctypes.c_int
    lib.kernel32.ConnectNamedPipe.argtypes = ctypes.c_void_p, ctypes.c_void_p

    lib.kernel32.DisconnectNamedPipe.restype = ctypes.c_int
    lib.kernel32.DisconnectNamedPipe.argtypes = ctypes.c_void_p,

    lib.kernel32.PeekNamedPipe.restype = ctypes.c_int
    lib.kernel32.PeekNamedPipe.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_ulong, ctypes.POINTER(ctypes.c_ulong), ctypes.POINTER(ctypes.c_ulong), ctypes.POINTER(ctypes.c_ulong))

    lib.kernel32.CreateNamedPipeW.restype = ctypes.c_void_p
    lib.kernel32.CreateNamedPipeW.argtypes = (ctypes.c_wchar_p, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_void_p)

    lib.kernel32.WaitNamedPipeW.restype = ctypes.c_int
    lib.kernel32.WaitNamedPipeW.argtypes = ctypes.c_wchar_p, ctypes.c_ulong

    # noinspection PyPep8Naming
    class const:
        PIPE_TYPE_BYTE = PIPE_READMODE_BYTE = PIPE_WAIT = PIPE_ACCEPT_REMOTE_CLIENTS = 0x00000000
        INVALID_HANDLE_VALUE = 0xffffffffffffffff
        NMPWAIT_WAIT_FOREVER = 0xffffffff
        PIPE_ACCESS_INBOUND = 0x00000001
        PIPE_ACCESS_OUTBOUND = 0x00000002
        FILE_FLAG_FIRST_PIPE_INSTANCE = 0x00080000
        GENERIC_READ = 0x80000000
        GENERIC_WRITE = 0x40000000
        OPEN_EXISTING = 3
        ERROR_BROKEN_PIPE = 109

    # noinspection PyPep8Naming
    class type:
        c_char = ctypes.c_char
        c_wchar = ctypes.c_wchar
        HANDLE = ctypes.c_void_p
        DWORD = ctypes.c_ulong

    @staticmethod
    def char_array(string: bytes | str, size: int):
        return ((ctypes.c_char if isinstance(string, bytes) else ctypes.c_wchar) * size)()


_DIR = r'\\.\pipe'

POLL_INTERVAL = 0.1


class _NamedPipe(ctyped.type.HANDLE):
    _size: int
    _base: bytes | str

    _pipe_mode = (ctyped.const.PIPE_TYPE_BYTE | ctyped.const.PIPE_READMODE_BYTE | ctyped.const.PIPE_WAIT | ctyped.const.PIPE_ACCEPT_REMOTE_CLIENTS)

    def __init__(self, name: str):
        self._name = ntpath.join(_DIR, name)
        super().__init__()

    def __del__(self):
        self.close()

    def __bool__(self):
        return self.value not in (None, ctyped.const.INVALID_HANDLE_VALUE)

    def __str__(self):
        return self._name

    def wait(self, timeout: float = ctyped.const.NMPWAIT_WAIT_FOREVER / 1000) -> bool:
        return bool(ctyped.lib.kernel32.WaitNamedPipeW(self._name, int(timeout * 1000)))

    def create(self, read: bool = True, write: bool = False) -> bool:
        open_mode = ((read * ctyped.const.PIPE_ACCESS_INBOUND) | (write * ctyped.const.PIPE_ACCESS_OUTBOUND) | ctyped.const.FILE_FLAG_FIRST_PIPE_INSTANCE)
        self.value = ctyped.lib.kernel32.CreateNamedPipeW(self._name, open_mode, self._pipe_mode, 1, 0, 0, 0, None)
        return bool(self)

    def connect(self) -> bool:
        return bool(ctyped.lib.kernel32.ConnectNamedPipe(self, None))

    def disconnect(self) -> bool:
        return bool(ctyped.lib.kernel32.DisconnectNamedPipe(self))

    def open(self, read: bool = True, write: bool = False) -> bool:
        access = (read * ctyped.const.GENERIC_READ) | (write * ctyped.const.GENERIC_WRITE)
        self.value = ctyped.lib.kernel32.CreateFileW(self._name, access, 0, None, ctyped.const.OPEN_EXISTING, 0, None)
        return bool(self)

    def close(self) -> bool:
        if closed := bool(ctyped.lib.kernel32.CloseHandle(self)):
            self.value = 0
        return closed

    def _wait_bytes(self, size: int = 0):
        buff = ctyped.char_array(type(self)._base, size=size + 1)
        ctyped.lib.kernel32.ReadFile(self, buff, size * self._size, None, None)
        self._base += buff.value

    def _avail_bytes(self) -> int:
        size = ctyped.type.DWORD()
        if not ctyped.lib.kernel32.PeekNamedPipe(self, None, 0, None, ctyped.byref(size), None):
            if ctyped.const.ERROR_BROKEN_PIPE == ctyped.lib.kernel32.GetLastError():
                raise BrokenPipeError
        return len(self._base) * self._size + size.value

    def read(self, size: int = -1, wait: bool = False) -> bytes | str:
        if wait:
            self._wait_bytes()
        if size == -1:
            size = self._avail_bytes() // self._size - len(self._base)
        read = type(self)._base
        if size > 0:
            buff = ctyped.char_array(type(self)._base, size=size + 1)
            ctyped.lib.kernel32.ReadFile(self, buff, size * self._size, None, None)
            read = self._base + buff.value
            self._base = type(self)._base
        return read

    def write(self, text: bytes | str, flush: bool = True) -> int:
        written = ctyped.type.DWORD()
        ctyped.lib.kernel32.WriteFile(self, text, len(text) * self._size, ctyped.byref(written), None)
        if flush:
            self.flush()
        return written.value // self._size

    def flush(self) -> bool:
        return bool(ctyped.lib.kernel32.FlushFileBuffers(self))

    def exists(self) -> bool:
        return ntpath.basename(self._name) in os.listdir(_DIR)


class BytesNamedPipe(_NamedPipe):
    _size = ctyped.sizeof(ctyped.type.c_char)
    _base = type(ctyped.type.c_char().value)()


class StringNamedPipe(_NamedPipe):
    _size = ctyped.sizeof(ctyped.type.c_wchar)
    _base = type(ctyped.type.c_wchar().value)()


class _Writer:
    def __init__(self, pipe: StringNamedPipeClient, target: Optional[TextIO]):
        self.target = target
        if target is None:
            self.write = pipe.write
            self.flush = pipe.flush
        else:
            self._pipe = pipe

    def write(self, text: str) -> int:
        self._pipe.write(text)
        return self.target.write(text)

    def flush(self):
        self._pipe.flush()
        self.target.flush()


class StringNamedPipeClient:
    def __init__(self, name: str):
        self._console = StringNamedPipe(name)
        self._out = sys.stdout = _Writer(self, sys.stdout)
        self._err = sys.stderr = _Writer(self, sys.stderr)

    def __bool__(self):
        return bool(self._console) and self._console.exists()

    def __str__(self):
        return str(self._console)

    def connect(self, timeout: int = 0) -> bool:
        end_time = time.time() + timeout
        while end_time > time.time() and not self._console.open(False, True):
            time.sleep(POLL_INTERVAL)
        return bool(self)

    def disconnect(self) -> bool:
        sys.stdout = self._out.target
        sys.stderr = self._err.target
        return self._console.close()

    def write(self, text: str) -> int:
        return self._console.write(text) if self else 0

    def flush(self):
        if self:
            self._console.flush()


def create_server(name: str):
    pipe = StringNamedPipe(name)
    if pipe.create():
        if pipe.connect():
            while True:
                try:
                    data = pipe.read(wait=True)
                except BrokenPipeError:
                    break
                else:
                    print(data, end='', flush=True)
            pipe.disconnect()
        pipe.close()
    sys.exit()


def main():
    if len(sys.argv) > 1:
        create_server(sys.argv[1])
    sys.exit()


if __name__ == '__main__':
    main()
