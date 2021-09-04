import functools as _functools
import types as _types
import typing as _typing
from typing import Callable as _Callable

from . import __head__
from . import _const
from . import _type


# noinspection PyPep8Naming
def SUCCEEDED(hr: _type.HRESULT) -> _type.c_bool:
    return _type.c_bool(hr >= 0)


# noinspection PyPep8Naming
def FAILED(hr: _type.HRESULT) -> _type.c_bool:
    return _type.c_bool(hr < 0)


# noinspection PyPep8Naming
def MAKEWORD(a: _type.DWORD_PTR, b: _type.DWORD_PTR) -> _type.WORD:
    wb = __head__.cast(__head__.cast(b & 0xff, _type.BYTE), _type.WORD).contents
    wb <<= 8
    # noinspection PyUnresolvedReferences
    return __head__.cast(__head__.cast(a & 0xff, _type.BYTE), _type.WORD).contents | wb


# noinspection PyPep8Naming
def MAKELONG(a: _type.WORD, b: _type.WORD) -> _type.LONG:
    wb = __head__.cast(__head__.cast(b & 0xffff, _type.WORD), _type.DWORD).contents
    wb <<= 16
    # noinspection PyUnresolvedReferences
    return __head__.cast(__head__.cast(a & 0xffff, _type.WORD), _type.LONG).contents | wb


# noinspection PyPep8Naming
def LOWORD(l_: _type.DWORD_PTR) -> _type.WORD:
    return __head__.cast(l_ & 0xffff, _type.WORD).contents


# noinspection PyPep8Naming
def HIWORD(l_: _type.DWORD_PTR) -> _type.WORD:
    l_ = l_ >> 16
    l_ &= 0xffff
    return __head__.cast(l_, _type.WORD).contents


# noinspection PyPep8Naming
def LOBYTE(w: _type.DWORD_PTR) -> _type.BYTE:
    return __head__.cast(w & 0xff, _type.BYTE).contents


# noinspection PyPep8Naming
def HIBYTE(w: _type.WORD) -> _type.BYTE:
    w = w >> 8
    w &= 0xff
    return __head__.cast(w, _type.BYTE).contents


# noinspection PyPep8Naming
def RGB(r: _type.BYTE, g: _type.BYTE, b: _type.BYTE) -> _type.COLORREF:
    # noinspection PyTypeChecker
    return __head__.cast(b, _type.DWORD).contents << 16 | __head__.cast(g, _type.WORD).contents << 8 | r


# noinspection PyPep8Naming
def PALETTERGB(r: _type.BYTE, g: _type.BYTE, b: _type.BYTE) -> _type.COLORREF:
    return 0x02000000 | RGB(r, g, b)


# noinspection PyPep8Naming
def GetRValue(rgb: _type.COLORREF) -> _type.BYTE:
    return LOBYTE(rgb)


# noinspection PyPep8Naming
def GetGValue(rgb: _type.COLORREF) -> _type.BYTE:
    # noinspection PyTypeChecker
    return LOBYTE(__head__.cast(rgb, _type.WORD).contents >> 8)


# noinspection PyPep8Naming
def GetBValue(rgb: _type.COLORREF) -> _type.BYTE:
    return LOBYTE(rgb >> 16)


# noinspection PyPep8Naming
def IS_INTRESOURCE(_r: _type.ULONG_PTR) -> _type.c_bool:
    return _type.c_bool(_r >> 16 == 0)


# noinspection PyPep8Naming
def MAKEINTRESOURCEA(i: _type.WORD) -> _type.LPSTR:
    return __head__.cast(__head__.cast(i, _type.ULONG_PTR), _type.LPSTR).contents


# noinspection PyPep8Naming
def MAKEINTRESOURCEW(i: _type.WORD) -> _type.LPWSTR:
    return __head__.cast(__head__.cast(i, _type.ULONG_PTR), _type.LPWSTR).contents


MAKEINTRESOURCE = MAKEINTRESOURCEW if _const.UNICODE else MAKEINTRESOURCEA


def _init(name: str) -> _Callable:
    _globals.has_item(name)
    types = _typing.get_type_hints(_globals.vars_[name]).values()
    macro = _types.FunctionType(_globals.vars_[name].__code__, _globals, name,
                                _globals.vars_[name].__defaults__, _globals.vars_[name].__closure__)
    return _functools.update_wrapper(lambda *args: macro(*(
        arg if isinstance(arg, type_) else type_(arg) for arg, type_ in zip(args, types))), _globals.vars_[name])


_globals = __head__.Globals()
