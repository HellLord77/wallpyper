import ctypes as _ctypes
import typing as _typing

_DEBUG = True

gdi32: _ctypes.WinDLL
gdiplus: _ctypes.WinDLL
kernel32: _ctypes.WinDLL
msvcrt: _ctypes.WinDLL
ntdll: _ctypes.WinDLL
ole32: _ctypes.WinDLL
shell32: _ctypes.WinDLL
user32: _ctypes.WinDLL


def _init():
    globals_ = globals()
    for var, type_ in _typing.get_type_hints(type('', (), globals_)()).items():
        globals_[var] = type_(var, use_last_error=_DEBUG)


_init()
