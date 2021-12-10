import ctypes as _ctypes
import sys as _sys
import typing as _typing
from typing import Callable as _Callable
from typing import Union as _Union

from .__head__ import _DEBUG
from .__head__ import _Globals
from .__head__ import _replace_object


class _Lib:
    lib = None

    def __init__(self, base, name):
        self.base = base
        self.name = name

    def __getattribute__(self, name: str):
        if name in ('lib', 'base', 'name'):
            return super().__getattribute__(name)
        if not self.lib:
            self.lib = self.base(self.name, use_last_error=_DEBUG)
        _replace_object(self, self.lib)
        return getattr(self.lib, name)


GdiPlus: _Union[_Callable, _ctypes.WinDLL]
KernelBase: _Union[_Callable, _ctypes.WinDLL]
SHCore: _Union[_Callable, _ctypes.WinDLL]
advapi32: _Union[_Callable, _ctypes.WinDLL]
combase: _Union[_Callable, _ctypes.WinDLL]
gdi32: _Union[_Callable, _ctypes.WinDLL]
gdi32full: _Union[_Callable, _ctypes.WinDLL]
kernel32: _Union[_Callable, _ctypes.WinDLL]
msvcp140: _Union[_Callable, _ctypes.WinDLL]
msvcrt: _Union[_Callable, _ctypes.WinDLL]
ntdll: _Union[_Callable, _ctypes.WinDLL]
ole32: _Union[_Callable, _ctypes.WinDLL]
oleaut32: _Union[_Callable, _ctypes.WinDLL]
rpcrt4: _Union[_Callable, _ctypes.WinDLL]
shdocvw: _Union[_Callable, _ctypes.WinDLL]
shell32: _Union[_Callable, _ctypes.WinDLL]
ucrtbase: _Union[_Callable, _ctypes.WinDLL]
user32: _Union[_Callable, _ctypes.WinDLL]
uxtheme: _Union[_Callable, _ctypes.WinDLL]
vcruntime140: _Union[_Callable, _ctypes.WinDLL]

globals().update({name: _typing.get_args(type_)[1] for name, type_ in
                  _typing.get_type_hints(_sys.modules[__name__]).items() if not name.startswith('_')})


def _init(name: str) -> _ctypes.CDLL:
    _globals.has_item(name)
    # noinspection PyTypeChecker
    return _Lib(_globals.vars_[name], name)


_globals = _Globals(True)
