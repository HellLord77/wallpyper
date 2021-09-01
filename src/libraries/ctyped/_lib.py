import ctypes as _ctypes
import typing as _typing

from . import _header

_DEBUG = True

GdiPlus: _ctypes.WinDLL
KernelBase: _ctypes.WinDLL
SHCore: _ctypes.WinDLL
advapi32: _ctypes.WinDLL
combase: _ctypes.WinDLL
gdi32: _ctypes.WinDLL
gdi32full: _ctypes.WinDLL
kernel32: _ctypes.WinDLL
kernel_appcore: _ctypes.WinDLL
msvcp140: _ctypes.WinDLL
msvcrt: _ctypes.WinDLL
ntdll: _ctypes.WinDLL
ole32: _ctypes.WinDLL
oleaut32: _ctypes.WinDLL
rpcrt4: _ctypes.WinDLL
shdocvw: _ctypes.WinDLL
shell32: _ctypes.WinDLL
ucrtbase: _ctypes.WinDLL
user32: _ctypes.WinDLL
uxtheme: _ctypes.WinDLL
vcruntime140: _ctypes.WinDLL


def __getattr__(name: str) -> _ctypes.WinDLL:
    # noinspection PyTypeChecker
    _header.Globals.hasattr(_lib, name)
    globals_ = globals()
    globals_[name] = _lib[name](f'{name.replace("_", ".")}.dll', use_last_error=_DEBUG)
    return globals_[name]


_lib = _typing.get_type_hints(type('', (), globals()))
if _header.INIT:
    for _lib_ in _lib:
        __getattr__(_lib_)
