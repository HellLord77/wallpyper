from __future__ import annotations

import contextlib
import ctypes
import ntpath
import os
import sys
import time
from typing import AnyStr


# noinspection PyPep8Naming
class ctyped:
    sizeof = ctypes.sizeof
    byref = ctypes.byref

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
    def char_array(string: AnyStr, size: int):
        return ((ctypes.c_char if isinstance(string, bytes) else ctypes.c_wchar) * size)()


# noinspection PyPep8Naming
class kernel32:
    SetConsoleTitleW = ctypes.windll.kernel32.SetConsoleTitleW
    SetConsoleTitleW.restype = ctypes.c_int
    SetConsoleTitleW.argtypes = ctypes.c_wchar_p,

    GetLastError = ctypes.windll.kernel32.GetLastError
    GetLastError.restype = ctypes.c_ulong
    GetLastError.argtypes = ()

    FlushFileBuffers = ctypes.windll.kernel32.FlushFileBuffers
    FlushFileBuffers.restype = ctypes.c_int
    FlushFileBuffers.argtypes = ctypes.c_void_p,

    WriteFile = ctypes.windll.kernel32.WriteFile
    WriteFile.restype = ctypes.c_int
    WriteFile.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_ulong,
                          ctypes.POINTER(ctypes.c_ulong), ctypes.c_void_p)

    CreateFileW = ctypes.windll.kernel32.CreateFileW
    CreateFileW.restype = ctypes.c_void_p
    CreateFileW.argtypes = (ctypes.c_wchar_p, ctypes.c_ulong, ctypes.c_ulong,
                            ctypes.c_void_p, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_void_p)

    ReadFile = ctypes.windll.kernel32.ReadFile
    ReadFile.restype = ctypes.c_int
    ReadFile.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_ulong,
                         ctypes.POINTER(ctypes.c_ulong), ctypes.c_void_p)

    CloseHandle = ctypes.windll.kernel32.CloseHandle
    CloseHandle.restype = ctypes.c_int
    CloseHandle.argtypes = ctypes.c_void_p,

    ConnectNamedPipe = ctypes.windll.kernel32.ConnectNamedPipe
    ConnectNamedPipe.restype = ctypes.c_int
    ConnectNamedPipe.argtypes = ctypes.c_void_p, ctypes.c_void_p

    DisconnectNamedPipe = ctypes.windll.kernel32.DisconnectNamedPipe
    DisconnectNamedPipe.restype = ctypes.c_int
    DisconnectNamedPipe.argtypes = ctypes.c_void_p,

    PeekNamedPipe = ctypes.windll.kernel32.PeekNamedPipe
    PeekNamedPipe.restype = ctypes.c_int
    PeekNamedPipe.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_ulong, ctypes.POINTER(
        ctypes.c_ulong), ctypes.POINTER(ctypes.c_ulong), ctypes.POINTER(ctypes.c_ulong))

    CreateNamedPipeW = ctypes.windll.kernel32.CreateNamedPipeW
    CreateNamedPipeW.restype = ctypes.c_void_p
    CreateNamedPipeW.argtypes = (ctypes.c_wchar_p, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_ulong,
                                 ctypes.c_ulong, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_void_p)

    WaitNamedPipeW = ctypes.windll.kernel32.WaitNamedPipeW
    WaitNamedPipeW.restype = ctypes.c_int
    WaitNamedPipeW.argtypes = ctypes.c_wchar_p, ctypes.c_ulong


_DIR = r'\\.\pipe'

POLL_INTERVAL = 0.1


class _NamedPipe(ctyped.type.HANDLE):
    __size__: int
    __base__: AnyStr

    _mode = (ctyped.const.PIPE_TYPE_BYTE | ctyped.const.PIPE_READMODE_BYTE |
             ctyped.const.PIPE_WAIT | ctyped.const.PIPE_ACCEPT_REMOTE_CLIENTS)

    def __init__(self, name: str):
        self._name = ntpath.join(_DIR, name)
        super().__init__()

    def __del__(self):
        self.close()

    def __bool__(self):
        return self.value not in (None, ctyped.const.INVALID_HANDLE_VALUE)

    @property
    def name(self) -> str:
        return self._name

    def wait(self, timeout: float = ctyped.const.NMPWAIT_WAIT_FOREVER / 1000) -> bool:
        return bool(kernel32.WaitNamedPipeW(self._name, int(timeout * 1000)))

    def create(self, read: bool = True, write: bool = False) -> bool:
        self.value = kernel32.CreateNamedPipeW(self._name, (read * ctyped.const.PIPE_ACCESS_INBOUND) | (
                write * ctyped.const.PIPE_ACCESS_OUTBOUND) | ctyped.const.FILE_FLAG_FIRST_PIPE_INSTANCE,
                                               self._mode, 1, 0, 0, 0, None)
        return bool(self)

    def connect(self) -> bool:
        return bool(kernel32.ConnectNamedPipe(self, None))

    def disconnect(self) -> bool:
        return bool(kernel32.DisconnectNamedPipe(self))

    def open(self, read: bool = True, write: bool = False) -> bool:
        self.value = kernel32.CreateFileW(self._name, (read * ctyped.const.GENERIC_READ) | (
                write * ctyped.const.GENERIC_WRITE), 0, None, ctyped.const.OPEN_EXISTING, 0, None)
        return bool(self)

    def close(self) -> bool:
        if closed := bool(kernel32.CloseHandle(self)):
            self.value = 0
        return closed

    def _wait_bytes(self, size: int = 0):
        buff = ctyped.char_array(0 * self.__base__, size=size + 1)
        kernel32.ReadFile(self, buff, size * self.__size__, None, None)
        self.__base__ += buff.value

    def _avail_bytes(self) -> int:
        size = ctyped.type.DWORD()
        if not kernel32.PeekNamedPipe(self, None, 0, None, ctyped.byref(size), None):
            if ctyped.const.ERROR_BROKEN_PIPE == kernel32.GetLastError():
                raise BrokenPipeError
        return len(self.__base__) * self.__size__ + size.value

    def read(self, size: int = -1, wait: bool = False) -> AnyStr:
        if wait:
            self._wait_bytes()
        if size == -1:
            size = self._avail_bytes() // self.__size__ - len(self.__base__)
        read = 0 * self.__base__
        if size > 0:
            buff = ctyped.char_array(0 * self.__base__, size=size + 1)
            kernel32.ReadFile(self, buff, size * self.__size__, None, None)
            read = self.__base__ + buff.value
            self.__base__ = 0 * self.__base__
        return read

    def write(self, text: AnyStr, flush: bool = True) -> int:
        written = ctyped.type.DWORD()
        kernel32.WriteFile(self, text, len(text if isinstance(
            text, bytes) else text.encode('utf-16')), ctyped.byref(written), None)
        if flush:
            self.flush()
        return written.value // self.__size__

    def flush(self) -> bool:
        return bool(kernel32.FlushFileBuffers(self))

    def exists(self) -> bool:
        return ntpath.basename(self._name) in os.listdir(_DIR)


class BytesNamedPipe(_NamedPipe):
    __size__ = ctyped.sizeof(ctyped.type.c_char)
    __base__ = type(ctyped.type.c_char().value)()


class StringNamedPipe(_NamedPipe):
    __size__ = ctyped.sizeof(ctyped.type.c_wchar)
    __base__ = type(ctyped.type.c_wchar().value)()


class StringNamedPipeClient:
    def __init__(self, name: str):
        self._pipe = StringNamedPipe(name)
        # noinspection PyTypeChecker
        self._stdout = contextlib.redirect_stdout(self._pipe)
        # noinspection PyTypeChecker
        self._stderr = contextlib.redirect_stderr(self._pipe)

    def __bool__(self):
        return bool(self._pipe) and self._pipe.exists()

    def __str__(self):
        return self._pipe.name

    def connect(self, timeout: float = 0.0) -> bool:
        end_time = time.monotonic() + timeout
        while end_time > time.monotonic() and not self._pipe.open(False, True):
            time.sleep(POLL_INTERVAL)
        if connected := bool(self):
            self._stdout.__enter__()
            self._stderr.__enter__()
        return connected

    def disconnect(self) -> bool:
        self._stdout.__exit__(None, None, None)
        self._stderr.__exit__(None, None, None)
        return self._pipe.close()


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


def main():
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        kernel32.SetConsoleTitleW(ntpath.basename(arg).rsplit('.', 1)[0])
        create_server(arg)
    sys.exit()


if __name__ == '__main__':
    main()
