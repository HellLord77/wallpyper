import functools as _functools
import types as _types
import typing as _typing
from typing import Callable as _Callable

from . import _header
from . import _type


# noinspection PyPep8Naming
def SUCCEEDED(hr: _type.HRESULT) -> _type.c_bool:
    return _type.c_bool(hr >= 0)


# noinspection PyPep8Naming
def FAILED(hr: _type.HRESULT) -> _type.c_bool:
    return _type.c_bool(hr < 0)


# noinspection PyPep8Naming
def MAKEWORD(a: _type.DWORD_PTR,
             b: _type.DWORD_PTR) -> _type.WORD:
    wb = _header.cast(_header.cast(b & 0xff, _type.BYTE), _type.WORD).contents
    wb <<= 8
    # noinspection PyUnresolvedReferences
    return _header.cast(_header.cast(a & 0xff, _type.BYTE), _type.WORD).contents | wb


# noinspection PyPep8Naming
def MAKELONG(a: _type.WORD,
             b: _type.WORD) -> _type.LONG:
    wb = _header.cast(_header.cast(b & 0xffff, _type.WORD), _type.DWORD).contents
    wb <<= 16
    # noinspection PyUnresolvedReferences
    return _header.cast(_header.cast(a & 0xffff, _type.WORD), _type.LONG).contents | wb


# noinspection PyPep8Naming
def LOWORD(l_: _type.DWORD_PTR) -> _type.WORD:
    return _header.cast(l_ & 0xffff, _type.WORD).contents


# noinspection PyPep8Naming
def HIWORD(l_: _type.DWORD_PTR) -> _type.WORD:
    l_ = l_ >> 16
    l_ &= 0xffff
    return _header.cast(l_, _type.WORD).contents


# noinspection PyPep8Naming
def LOBYTE(w: _type.DWORD_PTR) -> _type.BYTE:
    return _header.cast(w & 0xff, _type.BYTE).contents


# noinspection PyPep8Naming
def HIBYTE(w: _type.WORD) -> _type.BYTE:
    w = w >> 8
    w &= 0xff
    return _header.cast(w, _type.BYTE).contents


# noinspection PyPep8Naming
def RGB(r: _type.BYTE,
        g: _type.BYTE,
        b: _type.BYTE) -> _type.COLORREF:
    # noinspection PyTypeChecker
    return _header.cast(b, _type.DWORD).contents << 16 | _header.cast(g, _type.WORD).contents << 8 | r


# noinspection PyPep8Naming
def PALETTERGB(r: _type.BYTE,
               g: _type.BYTE,
               b: _type.BYTE) -> _type.COLORREF:
    return 0x02000000 | RGB(r, g, b)


# noinspection PyPep8Naming
def GetRValue(rgb: _type.COLORREF) -> _type.BYTE:
    return LOBYTE(rgb)


# noinspection PyPep8Naming
def GetGValue(rgb: _type.COLORREF) -> _type.BYTE:
    # noinspection PyTypeChecker
    return LOBYTE(_header.cast(rgb, _type.WORD).contents >> 8)


# noinspection PyPep8Naming
def GetBValue(rgb: _type.COLORREF) -> _type.BYTE:
    return LOBYTE(rgb >> 16)


def __getattr__(name: str) -> _Callable:
    types = _typing.get_type_hints(_macro[name]).values()
    macro = _types.FunctionType(_macro[name].__code__, _globals, name,
                                _macro[name].__defaults__, _macro[name].__closure__)
    _globals[name] = _functools.update_wrapper(lambda *args: macro(*(
        arg if isinstance(arg, type_) else type_(arg) for arg, type_ in zip(args, types))), _macro[name])
    return _globals[name]


_macro = _header.init(globals())
_globals = _header.Dict(globals(), __getattr__)
if _header.INIT:
    for _macro_ in _macro:
        __getattr__(_macro_)
