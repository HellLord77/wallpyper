import ctypes as _ctypes

from .__head__ import DEBUG as _DEBUG
from .__head__ import Globals as _Globals

GdiPlus = _ctypes.WinDLL
KernelBase = _ctypes.WinDLL
SHCore = _ctypes.WinDLL
advapi32 = _ctypes.WinDLL
combase = _ctypes.WinDLL
gdi32 = _ctypes.WinDLL
gdi32full = _ctypes.WinDLL
kernel32 = _ctypes.WinDLL
msvcp140 = _ctypes.WinDLL
msvcrt = _ctypes.WinDLL
ntdll = _ctypes.WinDLL
ole32 = _ctypes.WinDLL
oleaut32 = _ctypes.WinDLL
rpcrt4 = _ctypes.WinDLL
shdocvw = _ctypes.WinDLL
shell32 = _ctypes.WinDLL
ucrtbase = _ctypes.WinDLL
user32 = _ctypes.WinDLL
uxtheme = _ctypes.WinDLL
vcruntime140 = _ctypes.WinDLL


def _init(name: str) -> _ctypes.CDLL:
    _globals.has_item(name)
    return _globals.vars_[name](name, use_last_error=_DEBUG)


_globals = _Globals(True)
