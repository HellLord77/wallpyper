import functools as _functools
import typing as _typing

from . import _ctype
from . import _header


# noinspection PyPep8Naming
def MAKEWORD(a: _ctype.BYTE,
             b: _ctype.BYTE) -> _ctype.WORD:
    dwa = _header.cast(a, _ctype.DWORD_PTR).contents
    dwa &= 0xff
    dwb = _header.cast(b, _ctype.DWORD_PTR).contents
    dwb &= 0xff
    wb = _header.cast(_header.cast(dwb, _ctype.BYTE), _ctype.WORD).contents
    wb <<= 8
    return _header.cast(_header.cast(dwa, _ctype.BYTE), _ctype.WORD).contents | wb


# noinspection PyPep8Naming
def MAKELONG(a: _ctype.WORD,
             b: _ctype.WORD) -> _ctype.DWORD:
    dwa = _header.cast(a, _ctype.DWORD_PTR).contents
    dwa &= 0xffff
    dwb = _header.cast(b, _ctype.DWORD_PTR).contents
    dwb &= 0xffff
    wb = _header.cast(_header.cast(dwb, _ctype.WORD), _ctype.DWORD).contents
    wb <<= 16
    return _header.cast(_header.cast(dwa, _ctype.WORD), _ctype.LONG).contents | wb


# noinspection PyPep8Naming
def LOWORD(l_: _ctype.DWORD) -> _ctype.WORD:
    dword = _header.cast(l_, _ctype.DWORD_PTR).contents
    dword &= 0xffff
    return _header.cast(dword, _ctype.WORD).contents


# noinspection PyPep8Naming
def HIWORD(l_: _ctype.DWORD) -> _ctype.WORD:
    dword = _header.cast(l_, _ctype.DWORD_PTR).contents
    dword >>= 16
    dword &= 0xffff
    return _header.cast(dword, _ctype.WORD).contents


# noinspection PyPep8Naming
def LOBYTE(w: _ctype.WORD) -> _ctype.BYTE:
    dword = _header.cast(w, _ctype.DWORD_PTR).contents
    dword &= 0xff
    return _header.cast(dword, _ctype.BYTE).contents


# noinspection PyPep8Naming
def HIBYTE(w: _ctype.WORD) -> _ctype.BYTE:
    dword = _header.cast(w, _ctype.DWORD_PTR).contents
    dword >>= 8
    dword &= 0xff
    return _header.cast(dword, _ctype.BYTE).contents


# noinspection PyPep8Naming
def RGB(r: _ctype.BYTE,
        g: _ctype.BYTE,
        b: _ctype.BYTE) -> _ctype.COLORREF:
    return _header.cast(b, _ctype.DWORD).contents << 16 | _header.cast(g, _ctype.WORD).contents << 8 | r


# noinspection PyPep8Naming
def PALETTERGB(r: _ctype.BYTE,
               g: _ctype.BYTE,
               b: _ctype.BYTE) -> _ctype.COLORREF:
    return 0x02000000 | RGB(r, g, b)


# noinspection PyPep8Naming
def GetRValue(rgb: _ctype.COLORREF) -> _ctype.BYTE:
    return LOBYTE(rgb)


# noinspection PyPep8Naming
def GetGValue(rgb: _ctype.COLORREF) -> _ctype.BYTE:
    return LOBYTE(_header.cast(rgb, _ctype.WORD).contents >> 8)


# noinspection PyPep8Naming
def GetBValue(rgb: _ctype.COLORREF) -> _ctype.BYTE:
    return LOBYTE(rgb >> 16)


def _init():
    globals_ = globals()
    for var, macro in _header.items(globals_):
        globals_[var] = _functools.update_wrapper(
            lambda *args, _func=macro, _types=_typing.get_type_hints(macro).values(): _func(
                *(arg if isinstance(arg, type_) else type_(arg) for arg, type_ in zip(args, _types))), macro)


_init()
