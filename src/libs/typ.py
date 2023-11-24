__version__ = '0.0.1'

import ast
import threading
import time
import typing
from typing import Callable
from typing import Optional

_T = typing.TypeVar('_T')


def _to_type(string: str, expected: type[_T] | tuple[type, ...]) -> _T:
    val = ast.literal_eval(string)
    if isinstance(val, expected):
        return val
    else:
        raise TypeError


def to_bool(string: str, strict: bool = True) -> bool:
    val = _to_type(string, (bool, int, str))
    if not strict:
        if isinstance(val, int):
            val = bool(val)
        elif isinstance(val, str):
            val = val.strip().lower()
            if val in ('false', 'no', 'off', '0', 'f', 'n'):
                val = False
            elif val in ('true', 'yes', 'on', '1', 't', 'y'):
                val = True
    if isinstance(val, bool):
        return val
    else:
        raise TypeError


def to_bytes(string: str) -> bytes:
    return _to_type(string, bytes)


def to_complex(string: str) -> complex:
    return _to_type(string, complex)


def to_dict(string: str) -> dict:
    return _to_type(string, dict)


def to_float(string: str, strict: bool = True) -> float:
    val = _to_type(string, (bool, int, float, str))
    if not strict:
        if isinstance(val, (bool, int)):
            val = float(val)
        elif isinstance(val, str):
            try:
                val = float(val.strip())
            except ValueError:
                pass
    if isinstance(val, float):
        return val
    else:
        raise TypeError


def to_int(string: str, strict: bool = True) -> int:
    val = _to_type(string, (bool, int, float, str))
    if not strict:
        if isinstance(val, str):
            try:
                val = float(val.strip())
            except ValueError:
                pass
        if isinstance(val, (bool, float)):
            val = int(val)
    if isinstance(val, int):
        return val
    else:
        raise TypeError


def to_list(string: str) -> list:
    return _to_type(string, list)


def to_set(string: str) -> set:
    return _to_type(string, set)


def to_str(string: str) -> str:
    return _to_type(string, str)


def to_tuple(string: str) -> tuple:
    return _to_type(string, tuple)


class MutableObject:
    __slots__ = '_data', '_changed'

    _type: type = object

    def __init__(self, val: Optional[bool | bytes | complex | float | int | str | tuple] = None):
        self._data = self._type() if val is None else val
        self._changed = threading.Event()

    def __bool__(self):
        return bool(self._data)

    def __complex__(self):
        return complex(self._data)

    def __int__(self):
        return int(self._data)

    def __float__(self):
        return float(self._data)

    def __str__(self):
        return str(self._data)

    def __bytes__(self):
        return bytes(self._data)

    def __iadd__(self, other):
        self._data += other
        self._changed.set()
        return self

    def __isub__(self, other):
        self._data -= other
        self._changed.set()
        return self

    def __imul__(self, other):
        self._data *= other
        self._changed.set()
        return self

    def __imatmul__(self, other):
        self._data @= other
        self._changed.set()
        return self

    def __itruediv__(self, other):
        self._data /= other
        self._changed.set()
        return self

    def __ifloordiv__(self, other):
        self._data //= other
        self._changed.set()
        return self

    def __imod__(self, other):
        self._data %= other
        self._changed.set()
        return self

    def __ipow__(self, other):
        self._data **= other
        self._changed.set()
        return self

    def __ilshift__(self, other):
        self._data <<= other
        self._changed.set()
        return self

    def __irshift__(self, other):
        self._data >>= other
        self._changed.set()
        return self

    def __iand__(self, other):
        self._data &= other
        self._changed.set()
        return self

    def __ixor__(self, other):
        self._data ^= other
        self._changed.set()
        return self

    def __ior__(self, other):
        self._data |= other
        self._changed.set()
        return self

    def get(self):
        return self._data

    def set(self, val):
        self._data = val
        self._changed.set()
        return val

    def clear(self):
        val = self._type()
        self._data = val
        self._changed.set()
        return val

    def wait(self, timeout: Optional[float] = None, val=None) -> bool:
        if val is None:
            self._changed.clear()
            return self._changed.wait(timeout)
        else:
            if timeout is None:
                while self._data != val:
                    self._changed.clear()
                    self._changed.wait()
            else:
                end_time = time.monotonic() + timeout
                while self._data != val:
                    self._changed.clear()
                    if not self._changed.wait(end_time - time.monotonic()):
                        break
            return self._data == val


class MutableBool(MutableObject):
    _type = bool
    get: Callable[[], _type]
    set: Callable[[_type], _type]
    clear: Callable[[], _type]


class MutableBytes(MutableObject):
    _type = bytes
    get: Callable[[], _type]
    set: Callable[[_type], _type]
    clear: Callable[[], _type]


class MutableComplex(MutableObject):
    _type = complex
    get: Callable[[], _type]
    set: Callable[[_type], _type]
    clear: Callable[[], _type]


class MutableFloat(MutableObject):
    _type = float
    get: Callable[[], _type]
    set: Callable[[_type], _type]
    clear: Callable[[], _type]


class MutableInt(MutableObject):
    _type = int
    get: Callable[[], _type]
    set: Callable[[_type], _type]
    clear: Callable[[], _type]


class MutableStr(MutableObject):
    _type = str
    get: Callable[[], _type]
    set: Callable[[_type], _type]
    clear: Callable[[], _type]


class MutableTuple(MutableObject):
    _type = tuple
    get: Callable[[], _type]
    set: Callable[[_type], _type]
    clear: Callable[[], _type]
