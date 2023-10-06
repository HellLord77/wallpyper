from __future__ import annotations as _

import ctypes as _ctypes
import ctypes.util as _ctypes_util
import functools as _functools
import os as _os
import sys as _sys
from typing import Optional as _Optional

from .. import const as _const
from .._utils import _fmt_annot, _func_doc, _resolve_type


class _CLib:
    _loader = _ctypes.CDLL

    def __init__(self, name: str, name_fmt: _Optional[str] = None,
                 arg_32: str = '', arg_64: str = '', prefix: str = ''):
        module = _sys.modules[name]
        self._annots = module.__annotations__
        self._dict = module.__dict__
        self._name = (name.removeprefix(f'{__name__}.') if name_fmt is None else
                      name_fmt.format(arg_32 if _const.is_32bits else arg_64))
        self._prefix = prefix
        self._ord = {}
        for name, val in tuple(self._dict.items()):
            if name in self._annots and isinstance(val, int):
                self._ord[name] = val
                delattr(module, name)
        module.__getattr__ = self.__getattr__
        module.__dir__ = self.__dir__
        module.__file__ = self.__file__

    def __getattr__(self, name: str):
        if name in self._annots:
            func = self._lib[self._ord.get(name, self._prefix + name)]
            annot = self._annots[name]
            func.restype, *func.argtypes = _resolve_type(eval(annot, self._dict))
            func.__name__ = name
            func.__doc__ = _func_doc(name, func.restype, func.argtypes, _fmt_annot(annot))
            self._dict[name] = func
        return self._dict[name]

    def __dir__(self):
        return self._annots

    @property
    def __file__(self) -> str:
        return _ctypes_util.find_library(self._name) or self._name

    @_functools.cached_property
    def _lib(self) -> _ctypes.CDLL:
        return self._loader(self.__file__)


class _OleLib(_CLib):
    _loader = _ctypes.OleDLL


class _WinLib(_CLib):
    _loader = _ctypes.WinDLL


class _PyLib(_CLib):
    _loader = _ctypes.PyDLL
    _lib = _ctypes.pythonapi


def add_path(path: str):
    if _const.is_windows:
        var = 'PATH'
    elif _sys.platform.startswith(('freebsd', 'openbsd', 'dragonfly')):
        raise NotImplementedError
    elif _sys.platform == 'sunos5':
        raise NotImplementedError
    else:
        var = 'LD_LIBRARY_PATH'
    paths = _os.environ.get(var, '')
    if paths:
        path += _os.pathsep
    _os.environ[var] = path + paths
