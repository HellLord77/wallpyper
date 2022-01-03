import ctypes as _ctypes
import sys as _sys
import typing as _typing
from typing import Callable as _Callable
from typing import Union as _Union

from .__head__ import _DEBUG
from .__head__ import _Globals
from .__head__ import _not_internal
from .__head__ import _replace_object


class _Lib:
    _lib = None

    def __init__(self, base, name):
        self._base = base
        self._name = name

    def __getattr__(self, name: str):
        if not self._lib:
            self._lib = self._base(self._name, use_last_error=_DEBUG)
        _replace_object(self, self._lib)
        return getattr(self._lib, name)


GdiPlus: _Union[_Callable, _ctypes.WinDLL]
KernelBase: _Union[_Callable, _ctypes.WinDLL]
Propsys: _Union[_Callable, _ctypes.WinDLL]
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
                  _typing.get_type_hints(_sys.modules[__name__]).items() if _not_internal(name)})


def _init(name: str) -> _ctypes.CDLL:
    _globals.has_item(name)
    # noinspection PyTypeChecker
    return _Lib(_globals.vars_[name], name)


_globals = _Globals(True)
