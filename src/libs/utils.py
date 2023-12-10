__version__ = '0.0.27'

import base64
import binascii
import bz2
import collections
import ctypes
import datetime
import enum
import functools
import gzip
import hashlib
import hmac
import inspect
import io
import itertools
import lzma
import math
import os
import pickle
import pprint
import queue
import re
import secrets
import sys
import threading
import time
import typing
import uuid
import zipfile
import zlib
from typing import Any
from typing import AnyStr
from typing import Callable
from typing import Iterable
from typing import Iterator
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence

import _hashlib

T = typing.TypeVar('T')
DEFAULT = object()
ANSI = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')


# noinspection PyPep8Naming
class staticproperty(property):
    # noinspection PyMethodOverriding
    def __get__(self, _, __):
        # noinspection PyArgumentList
        return self.fget()


class ProgressBar(enum.StrEnum):
    BLOCK_VERTICAL = ' ▁▂▃▄▅▆▇█'
    BLOCK_HORIZONTAL = ' ▏▎▍▌▋▊▉▉'
    BLOCK_SHADE = ' ░▒▓█'
    ROD_VERTICAL = ' 𝍩𝍪𝍫𝍬𝍭'
    ROD_HORIZONTAL = ' 𝍠𝍡𝍢𝍣𝍤'
    TALLY = ' 𝍲𝍳𝍴𝍵𝍶'
    OGHAM_LINE = ' ᚋᚌᚍᚎᚏ'
    OGHAM_DOT = ' ᚐᚑᚒᚓᚔ'
    MOON = '🌕🌔🌓🌒🌑'
    MOON_REVERSE = '🌕🌖🌗🌘🌑'
    CLOCK = '🌕🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚🕛'


class PointedList:
    def __init__(self, val: Optional[list] = None, default=DEFAULT):
        self._data = [] if val is None else val.copy()
        self.default = default
        self._current = -1

    def clear(self):
        self.__init__()

    def current_index(self) -> Optional[int]:
        return self._current if self.has() else None

    def has(self, index: Optional[Any] = None):
        return -1 < (self._current if index is None else index) < len(self._data)

    def has_next(self) -> bool:
        return self.has(self._current + 1)

    def has_previous(self) -> bool:
        return self.has(self._current - 1)

    def advance(self, count: int = 1) -> int:
        new = self._current + count
        if self.has(new):
            self._current = new
        return new

    def peek(self, index: Optional[int] = None):
        if index is None:
            index = self._current
        return self._data[index] if self.has(index) else self.default

    def peek_next(self):
        return self.peek(self._current + 1)

    def peek_previous(self):
        return self.peek(self._current - 1)

    def set_previous(self, val):
        self._data.insert(self._current, val)
        return val

    def set_next(self, val):
        self._data.insert(self._current + 1, val)
        self.advance()
        return val

    def next(self):
        val = self.peek_next()
        self.advance()
        return val

    def previous(self):
        val = self.peek_previous()
        self.advance(-1)
        return val


class TimeDeltaEx(datetime.timedelta):
    _search = " *".join(f"(?:(?P<{unit}s>[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)) *{unit}s?)?" for unit
                        in ("week", "day", "hour", "minute", "second", "millisecond", "microsecond"))
    _search = re.compile(f'^ *{_search} *$', re.RegexFlag.IGNORECASE).search
    # noinspection PyUnresolvedReferences,PyProtectedMember
    _units = tuple(inspect._signature_fromstr(inspect.Signature, None, inspect.getdoc(
        datetime.timedelta).splitlines()[2]).parameters)

    def __new__(cls, string: str):
        match = cls._search(string)
        return super().__new__(cls, *(float(match[unit] or 0)
                                      for unit in cls._units) if match else ())

    def __int__(self):
        return int(float(self))

    __float__ = datetime.timedelta.total_seconds


def get_progress(current: float = 0.0, width: int = 100,
                 bars: str | ProgressBar = ProgressBar.BLOCK_HORIZONTAL) -> str:
    if isinstance(bars, ProgressBar):
        bars = bars.value
    if current < 0:
        current = 0
    elif current > 1:
        current = 1
    each = 1 / width
    filled = int(current / each)
    index = int((len(bars) - 1) / each * (current - filled * each))
    return (bars[-1] * filled) + (bars[index] * bool(
        index)) + (bars[0] * (width - filled - bool(index)))


def len_ex(it: Iterable) -> int:
    return sum(1 for _ in it)


def index_ex(it: Iterable, value) -> int:
    for index, ele in enumerate(it):
        if value == ele:
            return index
    return -1


def any_ex(it: Iterable, func: Callable) -> bool:
    for ele in it:
        res = func(ele)
        if res:
            return True
    return False


def chain_ex(*funcs: Callable) -> Iterator:
    yield from (func() for func in funcs)


def cycle_ex(it: Iterable, func: Optional[Callable] = None) -> Iterator:
    while True:
        for ele in it:
            yield ele
        if func is not None:
            func()


def get_recursive(it: Mapping | Sequence, *keys, default=DEFAULT) -> Any:
    for key in keys:
        try:
            it = it[key]
        except:  # NOQA E722
            if default is DEFAULT:
                raise
            else:
                it = default
                break
    return it


def enquote(string: str, quote: str = '"') -> str:
    if len(string) < 2 or (string[0] != quote and string[-1] != quote):
        string = f'{quote}{string}{quote}'
    return string


def eq_ex(a, b) -> bool:
    sleep_ex()
    if isinstance(a, Iterable) and isinstance(b, Iterable):
        for a_, b_ in itertools.zip_longest(a, b, fillvalue=DEFAULT):
            sleep_ex()
            if eq_ex(a_, DEFAULT) or eq_ex(b_, DEFAULT) or not eq_ex(a_, b_):
                return False
        return True
    else:
        return a == b


def consume(it: Iterable, count: int = -1) -> int:
    count_ = itertools.count()
    if count:
        count -= 1
        for _, index in zip(it, count_):
            if count == index:
                break
    return next(count_)


def consume_all(it: Iterable):
    collections.deque(it, maxlen=0)


def consume_ex(it: Iterable, item) -> Optional[int]:
    count = itertools.count()
    for index, item_ in zip(count, it):
        if item == item_:
            return index


def randint_ex() -> int:
    return secrets.choice(secrets.token_bytes())


def replace_ex(string: str, a: str, b: str) -> str:
    return ''.join(a if char == b else b if char == a else char for char in string)


def vars_ex(obj) -> dict[str, Any]:
    return ctypes.cast(id(obj) + type(obj).__dictoffset__, ctypes.POINTER(ctypes.py_object)).contents.value


def getattr_ex(obj, name: str) -> Any:
    return vars_ex(obj)[name]


def setattr_ex(obj, name: str, value):
    vars_ex(obj)[name] = value


def sleep_ex(secs: Optional[float] = None):
    if secs is None:
        while secrets.randbelow(return_any(randint_ex)):
            pass
    elif secs != 0:
        end_time = time.monotonic() + secs
        while end_time > time.monotonic():
            pass


def try_ex(*funcs: Callable, excs: Optional[Iterable[Optional[Iterable[type[BaseException]]]]] = None) -> Any:
    for func, func_excs in itertools.zip_longest(
            funcs, () if excs is None else excs):
        if func is None:
            break
        try:
            func()
        except () if func_excs is None else func_excs:
            pass


def pass_ex(*_, **__):
    pass


def pretty_vars(obj) -> str:
    dict_ = getattr(obj, '__dict__', {})
    attrs = [], []
    for val in dict_.values():
        attrs[0].append(type(val).__name__)
        attrs[1].append(str(sys.getsizeof(val)))
    pads = tuple(len(max(it, key=len)) for it in (dict_,) + attrs)
    end = f'\n{" " * (sum(pads) + 6)}'
    fmt = ''
    for item, type_, size in zip(dict_.items(), *attrs):
        fmt += (f'{f"{item[0]}: ":{pads[0] + 2}}[{type_:{pads[1]}} {size:>{pads[2]}}] '
                f'{pprint.pformat(item[1], sort_dicts=False).replace(end[0], end)}\n')
    return fmt


# noinspection PyShadowingNames
def clear_queue(queue: queue.Queue) -> int:
    with queue.mutex:
        tasks = queue.unfinished_tasks
        queue.queue.clear()
        queue.unfinished_tasks = 0
    return tasks


@typing.overload
def iindex(it: Iterable[T], stop, /) -> Iterator[T]:
    pass


@typing.overload
def iindex(it: Iterable[T], start, stop: Optional, step: int = 1, /) -> Iterator[T]:
    pass


def iindex(it, start, stop=DEFAULT, step=1):
    if stop is DEFAULT:
        stop = start
        started = 0
    else:
        started = -1
    for index, ele in enumerate(it):
        if ele == stop:
            break
        elif started == -1:
            if ele == start:
                yield ele
                started = index
        elif not (index - started) % step:
            yield ele


def re_join(base: str, *child: str, sep: str = os.sep) -> str:
    return re.escape(sep).join((base,) + child)


def return_any(func: Callable, max_try: Optional[int] = None) -> Any:
    for _ in (range if max_try else itertools.repeat)(max_try):
        res = func()
        if res:
            return res


def strip_ansi(string: str) -> str:
    return ANSI.sub('', string)


def split_ex(string: str, length: int = 64) -> Iterator[str]:
    return (string[index: length + index] for index in range(0, len(string), length))


def shrink_string(string: str, max_len: int, filler: str = '...') -> str:
    return f'{string[:max_len - len(filler)]}{filler}' if len(string) > max_len else string


def shrink_string_mid(string: str, max_len: int, filler: str = '...') -> str:
    if len(string) > max_len:
        max_ = max_len - len(filler)
        left = math.ceil(max_ / 2)
        string = f'{string[:left]}{filler}{string[left - max_:]}'
    return string


def compress(datas: Mapping[str, AnyStr], compression: int = zipfile.ZIP_STORED) -> bytes:
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, 'w', compression) as file:
        for name, data in datas.items():
            file.writestr(name, data)
    return stream.getvalue()


def decompress(data: bytes, *names: str, password: Optional[bytes] = None) -> Mapping[str, Optional[bytes]]:
    datas = dict.fromkeys(names)
    try:
        with zipfile.ZipFile(io.BytesIO(data)) as file:
            if not names:
                names = file.namelist()
            file.setpassword(password)
            for name in names:
                datas[name] = file.read(name)
    except zipfile.BadZipFile:
        pass
    return datas


def _get_key(data: bytes | bytearray, key: Optional[bytes | bytearray | int | float | str],
             hash_: Optional[str | _hashlib.HASH] | Callable) -> bytes:
    if key is None:
        key = uuid.getnode()
    if isinstance(key, (int, float)):
        key = str(key)
    if isinstance(key, str):
        key = key.encode()
    if hash_ is None:
        key = hashlib.blake2b(data, key=key).digest()
    else:
        key = hmac.digest(key, data, hash_)
    return key


# noinspection PyShadowingBuiltins,PyShadowingNames,PyTypeHints
def encrypt(obj, key: Optional[bytes | bytearray | int | float | str] = None,
            hash: Optional[str | _hashlib.HASH | Callable] = hashlib.sha256,
            compress: Optional[Literal[zlib, gzip, bz2, lzma] | Callable] = zlib,
            as_string: bool = False) -> Optional[bytes | str]:
    try:
        pickled = pickle.dumps(obj, pickle.HIGHEST_PROTOCOL)
    except TypeError:
        pass
    else:
        data = _get_key(pickled, key, hash) + pickled
        if compress is not None:
            if not callable(compress):
                compress = compress.compress
            data = compress(data)
        if as_string:
            data = base64.b64encode(data).decode()
        return data


# noinspection PyShadowingBuiltins,PyShadowingNames,PyTypeHints
def decrypt(data: bytes | bytearray | str,
            key: Optional[bytes | bytearray | int | float | str] = None,
            hash: Optional[str | _hashlib.HASH | Callable] = hashlib.sha256,
            decompress: Optional[Literal[zlib, gzip, bz2, lzma] | Callable] = zlib,
            on_error=DEFAULT) -> Any:
    if isinstance(data, str):
        try:
            data = base64.b64decode(data.encode(), validate=True)
        except binascii.Error:
            return on_error
    if decompress is not None:
        if not callable(decompress):
            decompress = decompress.decompress
        try:
            data = decompress(data)
        except (OSError, zlib.error, gzip.BadGzipFile, lzma.LZMAError):
            return on_error
    size = hashlib.blake2b.MAX_DIGEST_SIZE if hash is None else hmac.new(
        b'', digestmod=hash).digest_size
    pickled = data[size:]
    if data[:size] == _get_key(pickled, key, hash):
        try:
            return pickle.loads(pickled)
        except pickle.UnpicklingError:
            pass
    return on_error


# noinspection PyShadowingBuiltins
def hook_except(func: Callable, format: bool = False):
    @functools.wraps(func)
    def wrapper(hook: Callable, *hook_args, **hook_kwargs):
        if format:
            stderr = sys.stderr
            stream = io.StringIO()
            sys.stderr = stream
        hook(*hook_args, **hook_kwargs)
        if format:
            # noinspection PyUnboundLocalVariable
            stderr.write(stream.getvalue())
            sys.stderr = stderr
            while not isinstance(hook_args, type):
                hook_args = hook_args[0]
            hook_args = (hook_args, stream.getvalue())
        func(*hook_args, **hook_kwargs)

    sys.excepthook = functools.partial(wrapper, sys.excepthook)
    threading.excepthook = functools.partial(wrapper, threading.excepthook)
