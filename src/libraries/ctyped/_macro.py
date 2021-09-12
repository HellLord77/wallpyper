import functools as _functools
import types as _types
import typing as _typing
from typing import Callable as _Callable

from . import _const
from . import _type
from .__head__ import Globals as _Globals
from .__head__ import cast as _cast


# noinspection PyPep8Naming
def SUCCEEDED(hr: int) -> bool:
    return hr >= 0


# noinspection PyPep8Naming
def FAILED(hr: int) -> bool:
    return hr < 0


# noinspection PyPep8Naming
def MAKEWORD(a: int, b: int) -> int:
    return a & 0xff | (b & 0xff) << 8


# noinspection PyPep8Naming
def MAKELONG(a: int, b: int) -> int:
    return a & 0xffff | (b & 0xffff) << 16


# noinspection PyPep8Naming
def LOWORD(l_: int) -> int:
    return l_ & 0xffff


# noinspection PyPep8Naming
def HIWORD(l_: int) -> int:
    return l_ >> 16 & 0xffff


# noinspection PyPep8Naming
def LOBYTE(w: int) -> int:
    return w & 0xff


# noinspection PyPep8Naming
def HIBYTE(w: int) -> int:
    return w >> 8 & 0xff


# noinspection PyPep8Naming
def RGB(r: int, g: int, b: int) -> int:
    return r | g << 8 | b << 16


# noinspection PyPep8Naming
def PALETTERGB(r: int, g: int, b: int) -> int:
    return 0x02000000 | RGB(r, g, b)


# noinspection PyPep8Naming
def GetRValue(rgb: int) -> int:
    return LOBYTE(rgb)


# noinspection PyPep8Naming
def GetGValue(rgb: int) -> int:
    return LOBYTE(rgb >> 8)


# noinspection PyPep8Naming
def GetBValue(rgb: int) -> int:
    return LOBYTE(rgb >> 16)


# noinspection PyPep8Naming
def IS_INTRESOURCE(_r: int) -> bool:
    return _r >> 16 == 0


# noinspection PyPep8Naming
def MAKEINTRESOURCEA(i: _type.WORD) -> bytes:
    # noinspection PyTypeChecker
    return _cast(_cast(i, _type.ULONG_PTR), _type.LPSTR).value


# noinspection PyPep8Naming
def MAKEINTRESOURCEW(i: _type.WORD) -> str:
    # noinspection PyTypeChecker
    return _cast(_cast(i, _type.ULONG_PTR), _type.LPWSTR).value


# noinspection PyPep8Naming
def GET_X_LPARAM(lp: int) -> int:
    return LOWORD(lp)


# noinspection PyPep8Naming
def GET_Y_LPARAM(lp: int) -> int:
    return HIWORD(lp)


MAKEINTRESOURCE = MAKEINTRESOURCEW if _const.UNICODE else MAKEINTRESOURCEA


def _init(name: str) -> _Callable:
    _globals.has_item(name)
    types = _typing.get_type_hints(_globals.vars_[name]).values()
    macro = _types.FunctionType(_globals.vars_[name].__code__, _globals)
    return _functools.update_wrapper(lambda *args: macro(*(
        arg if isinstance(arg, type_) else type_(arg) for arg, type_ in zip(args, types))), _globals.vars_[name])


_globals = _Globals()
