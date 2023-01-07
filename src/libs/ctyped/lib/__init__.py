from __future__ import annotations as _

import ctypes as _ctypes
import sys as _sys
import types as _types
from typing import Optional as _Optional

from .._utils import _fmt_annot, _func_doc, _resolve_type


class _CLib(_types.ModuleType):
    _loader = _ctypes.CDLL
    _lib: _Optional[_ctypes.CDLL] = None

    def __init__(self, name: str):
        super().__init__(name)
        module = _sys.modules[name]
        self._dict = module.__dict__
        self._annots = module.__annotations__
        _sys.modules[name] = self

    def __getattr__(self, name: str):
        if name in self._annots:
            if self._lib is None:
                self._lib = self._loader(self.__name__.removeprefix(f'{__name__}.'))
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


class _OleLib(_CLib):
    _loader = _ctypes.OleDLL


class _WinLib(_CLib):
    _loader = _ctypes.WinDLL


class _PyLib(_CLib):
    _loader = _ctypes.PyDLL
    _lib = _ctypes.pythonapi
