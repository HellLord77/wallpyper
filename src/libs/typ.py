__version__ = '0.0.2'

import ast
import threading
import time
import typing
from typing import Callable
from typing import Optional

_T = typing.TypeVar('_T')


def _to_type(string: str, expected: type[_T] | tuple[type, ...]) -> _T:
    value = ast.literal_eval(string)
    if isinstance(value, expected):
        return value
    else:
        raise TypeError


def to_bool(string: str, strict: bool = True) -> bool:
    value = _to_type(string, (bool, int, str))
    if not strict:
        if isinstance(value, int):
            value = bool(value)
        elif isinstance(value, str):
            value = value.strip().lower()
            if value in ('false', 'no', 'off', '0', 'f', 'n'):
                value = False
            elif value in ('true', 'yes', 'on', '1', 't', 'y'):
                value = True
    if isinstance(value, bool):
        return value
    else:
        raise TypeError


def to_bytes(string: str) -> bytes:
    return _to_type(string, bytes)


def to_complex(string: str) -> complex:
    return _to_type(string, complex)


def to_dict(string: str) -> dict:
    return _to_type(string, dict)


def to_float(string: str, strict: bool = True) -> float:
    value = _to_type(string, (bool, int, float, str))
    if not strict:
        if isinstance(value, (bool, int)):
            value = float(value)
        elif isinstance(value, str):
            try:
                value = float(value.strip())
            except ValueError:
                pass
    if isinstance(value, float):
        return value
    else:
        raise TypeError


def to_int(string: str, strict: bool = True) -> int:
    value = _to_type(string, (bool, int, float, str))
    if not strict:
        if isinstance(value, str):
            try:
                value = float(value.strip())
            except ValueError:
                pass
        if isinstance(value, (bool, float)):
            value = int(value)
    if isinstance(value, int):
        return value
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
    __slots__ = '_value', '_default', '_changed'

    _type: type

    def __init__(self, value: Optional[bool | bytes | complex | float | int | str | tuple] = None):
        if value is None:
            value = self._type()
        self._default = self._value = value
        self._changed = threading.Event()

    def __bool__(self):
        return bool(self._value)

    def __complex__(self):
        return complex(self._value)

    def __int__(self):
        return int(self._value)

    def __float__(self):
        return float(self._value)

    def __round__(self, ndigits=None):
        return round(self._value, ndigits)

    def __str__(self):
        return str(self._value)

    def __bytes__(self):
        return bytes(self._value)

    def __format__(self, format_spec=''):
        return format(self._value, format_spec)

    def __iadd__(self, other):
        self._value += other
        self._changed.set()
        return self

    def __isub__(self, other):
        self._value -= other
        self._changed.set()
        return self

    def __imul__(self, other):
        self._value *= other
        self._changed.set()
        return self

    def __imatmul__(self, other):
        self._value @= other
        self._changed.set()
        return self

    def __itruediv__(self, other):
        self._value /= other
        self._changed.set()
        return self

    def __ifloordiv__(self, other):
        self._value //= other
        self._changed.set()
        return self

    def __imod__(self, other):
        self._value %= other
        self._changed.set()
        return self

    def __ipow__(self, other):
        self._value **= other
        self._changed.set()
        return self

    def __ilshift__(self, other):
        self._value <<= other
        self._changed.set()
        return self

    def __irshift__(self, other):
        self._value >>= other
        self._changed.set()
        return self

    def __iand__(self, other):
        self._value &= other
        self._changed.set()
        return self

    def __ixor__(self, other):
        self._value ^= other
        self._changed.set()
        return self

    def __ior__(self, other):
        self._value |= other
        self._changed.set()
        return self

    def get(self):
        return self._value

    def set(self, value):
        self._value = value
        self._changed.set()
        return value

    def clear(self):
        value = self._value = self._type()
        self._changed.set()
        return value

    # noinspection PyTypeChecker,PyPropertyDefinition
    value = property(get, set, clear)

    def reset(self):
        value = self._value = self._default
        self._changed.set()
        return value

    def wait(self, timeout: Optional[float] = None, value=None) -> bool:
        if value is None:
            self._changed.clear()
            return self._changed.wait(timeout)
        else:
            if timeout is None:
                while self._value != value:
                    self._changed.clear()
                    self._changed.wait()
            else:
                end_time = time.monotonic() + timeout
                while self._value != value:
                    self._changed.clear()
                    if not self._changed.wait(end_time - time.monotonic()):
                        break
            return self._value == value


class MutableBool(MutableObject):
    _type = bool
    get: Callable[[], _type]
    set: Callable[[_type], _type]
    clear: Callable[[], _type]
    value: _type
    reset: Callable[[], _type]


class MutableBytes(MutableObject):
    _type = bytes
    get: Callable[[], _type]
    set: Callable[[_type], _type]
    clear: Callable[[], _type]
    value: _type
    reset: Callable[[], _type]


class MutableComplex(MutableObject):
    _type = complex
    get: Callable[[], _type]
    set: Callable[[_type], _type]
    clear: Callable[[], _type]
    value: _type
    reset: Callable[[], _type]


class MutableFloat(MutableObject):
    _type = float
    get: Callable[[], _type]
    set: Callable[[_type], _type]
    clear: Callable[[], _type]
    value: _type
    reset: Callable[[], _type]


class MutableInt(MutableObject):
    _type = int
    get: Callable[[], _type]
    set: Callable[[_type], _type]
    clear: Callable[[], _type]
    value: _type
    reset: Callable[[], _type]


class MutableStr(MutableObject):
    _type = str
    get: Callable[[], _type]
    set: Callable[[_type], _type]
    clear: Callable[[], _type]
    value: _type
    reset: Callable[[], _type]


class MutableTuple(MutableObject):
    _type = tuple
    get: Callable[[], _type]
    set: Callable[[_type], _type]
    clear: Callable[[], _type]
    value: _type
    reset: Callable[[], _type]
