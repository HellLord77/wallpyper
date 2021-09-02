import ctypes as _ctypes
import sys as _sys
import typing as _typing

_DEBUG = True

GdiPlus: _ctypes.WinDLL
KernelBase: _ctypes.WinDLL
SHCore: _ctypes.WinDLL
advapi32: _ctypes.WinDLL
combase: _ctypes.WinDLL
gdi32: _ctypes.WinDLL
gdi32full: _ctypes.WinDLL
kernel32: _ctypes.WinDLL
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

_module = _sys.modules[__name__]
for _lib, _type in _typing.get_type_hints(_module).items():
    setattr(_module, _lib, _type(_lib, use_last_error=_DEBUG))
