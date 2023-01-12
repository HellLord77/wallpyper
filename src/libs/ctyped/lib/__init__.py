from __future__ import annotations as _

import ctypes as _ctypes
import functools as _functools
import sys as _sys
import types as _types

from . import kernel32 as _kernel32
from .. import const as _const
from .. import type as _type
from .._utils import _fmt_annot, _func_doc, _resolve_type


class _CLib(_types.ModuleType):
    _loader = _ctypes.CDLL

    def __init__(self, name: str):
        super().__init__(name)
        module = _sys.modules[name]
        self._dict = module.__dict__
        self._annots = module.__annotations__
        _sys.modules[name] = self

    def __getattr__(self, name: str):
        if name in self._annots:
            func = self._lib[self._dict.get(name, name)]
            annot = self._annots[name]
            func.restype, *func.argtypes = _resolve_type(eval(annot, self._dict))
            func.__name__ = name
            func.__doc__ = _func_doc(name, func.restype, func.argtypes, _fmt_annot(annot))
            setattr(self, name, func)
            return func
        return super().__getattribute__(name)

    def __dir__(self):
        return *self.__dict__, *self._annots

    @_functools.cached_property
    def _lib(self) -> _ctypes.CDLL:
        return self._loader(self.__name__.removeprefix(f'{__name__}.'))


class _OleLib(_CLib):
    _loader = _ctypes.OleDLL


class _WinLib(_CLib):
    _loader = _ctypes.WinDLL


class _PyLib(_CLib):
    _loader = _ctypes.PyDLL
    _lib = _ctypes.pythonapi


def get_path(library: _CLib) -> str:
    buff = _type.LPWSTR('\0' * _const.MAX_PATH)
    # noinspection PyProtectedMember
    _kernel32.GetModuleFileNameW(library._lib._handle, buff, _const.MAX_PATH)
    return buff.value
