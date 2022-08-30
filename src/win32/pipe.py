import ntpath
import os
import sys
import time

import libs.ctyped as ctyped

_DIR = r'\\.\pipe'
_INVALID = ctyped.type.HANDLE(ctyped.const.INVALID_HANDLE_VALUE)

POLL_INTERVAL = 0.1


class _NamedPipe(ctyped.type.HANDLE):
    _size: int
    _base: bytes | str

    _pipe_mode = (ctyped.const.PIPE_TYPE_BYTE | ctyped.const.PIPE_READMODE_BYTE |
                  ctyped.const.PIPE_WAIT | ctyped.const.PIPE_ACCEPT_REMOTE_CLIENTS)

    def __init__(self, name: str):
        self._name = ntpath.join(_DIR, name)
        super().__init__()

    def __del__(self):
        self.close()

    def __bool__(self):
        return self.value and self != _INVALID

    def __str__(self):
        return self._name

    def wait(self, timeout: float = ctyped.const.NMPWAIT_WAIT_FOREVER / 1000) -> bool:
        return bool(ctyped.lib.kernel32.WaitNamedPipeW(self._name, int(timeout * 1000)))

    def create(self, read: bool = True, write: bool = False) -> bool:
        open_mode = ((read * ctyped.const.PIPE_ACCESS_INBOUND) |
                     (write * ctyped.const.PIPE_ACCESS_OUTBOUND) | ctyped.const.FILE_FLAG_FIRST_PIPE_INSTANCE)
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
        ctyped.lib.kernel32.ReadFile(self, ctyped.byref(buff), size * self._size, None, None)
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


class BytesNamedPipe(_NamedPipe):
    _size = 1
    _base = b''


class TextNamedPipe(_NamedPipe):
    _size = 2
    _base = ''


def exists(name: str) -> bool:
    name = name.casefold()
    for name_ in os.listdir(_DIR):
        if name == name_.casefold():
            return True
    return False


def server(name: str):
    pipe = TextNamedPipe(name)
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


def client(name: str, timeout: int = 0) -> TextNamedPipe:
    pipe = TextNamedPipe(name)
    end_time = time.time() + timeout
    while end_time > time.time() and not pipe.open(False, True):
        time.sleep(POLL_INTERVAL)
    return pipe


def main():
    server(sys.argv[1])


if __name__ == '__main__':
    main()
