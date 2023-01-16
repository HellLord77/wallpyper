__version__ = '0.0.23'

import ast
import binascii
import contextlib
import ctypes
import datetime
import functools
import hashlib
import inspect
import io
import itertools
import math
import os
import pickle
import pprint
import queue
import random
import re
import secrets
import sys
import threading
import time
import types
import typing
import uuid
import zipfile
import zlib
from typing import Any, AnyStr, Callable, Generator, IO, Iterable, Mapping, Optional

T = typing.TypeVar('T')
DEFAULT = object()
ANSI = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')


class ProgressBar:
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


class _Mutable:
    __slots__ = '_data', '_changed'
    _type: type = types.NoneType

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


class MutableBool(_Mutable):
    _type = bool
    get: Callable[[], _type]
    set: Callable[[_type], _type]
    clear: Callable[[], _type]


class MutableBytes(_Mutable):
    _type = bytes
    get: Callable[[], _type]
    set: Callable[[_type], _type]
    clear: Callable[[], _type]


class MutableComplex(_Mutable):
    _type = complex
    get: Callable[[], _type]
    set: Callable[[_type], _type]
    clear: Callable[[], _type]


class MutableFloat(_Mutable):
    _type = float
    get: Callable[[], _type]
    set: Callable[[_type], _type]
    clear: Callable[[], _type]


class MutableInt(_Mutable):
    _type = int
    get: Callable[[], _type]
    set: Callable[[_type], _type]
    clear: Callable[[], _type]


class MutableStr(_Mutable):
    _type = str
    get: Callable[[], _type]
    set: Callable[[_type], _type]
    clear: Callable[[], _type]


class MutableTuple(_Mutable):
    _type = tuple
    get: Callable[[], _type]
    set: Callable[[_type], _type]
    clear: Callable[[], _type]


class IntEnumMeta(type):
    def __new__(mcs, *args, **kwargs):
        cls = super().__new__(mcs, *args, **kwargs)
        cls._vars = {var: val for var, val in vars(cls).items() if not var.startswith('_')}
        return cls

    def __contains__(cls, item):
        return item in cls._vars

    def __iter__(cls) -> Generator[str, None, None]:
        yield from cls._vars

    @typing.overload
    def __getitem__(cls, var_or_val: slice) -> tuple[str]:
        pass

    @typing.overload
    def __getitem__(cls, var_or_val: int) -> str:
        pass

    @typing.overload
    def __getitem__(cls, var_or_val: str) -> int:
        pass

    def __getitem__(cls, var_or_val):
        if isinstance(var_or_val, int):
            for var, val_ in cls._vars.items():
                if var_or_val == val_:
                    return var
            raise IndexError
        elif isinstance(var_or_val, slice):
            return tuple(itertools.islice(cls._vars, var_or_val.start, var_or_val.stop, var_or_val.step))
        else:
            return cls._vars[var_or_val]

    def get_random(cls, *excludes: int) -> int:
        return random.choice(tuple(val for val in cls._vars.values() if val not in excludes))


class PointedList:
    def __init__(self, val: Optional[list] = None, default: Any = DEFAULT):
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
    _match = " *".join(f"(?:(?P<{unit}s>[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)) *{unit}s?)?" for unit in
                       ("week", "day", "hour", "minute", "second", "millisecond", "microsecond"))
    _match = re.compile(f'^ *{_match} *$', re.RegexFlag.IGNORECASE).match
    # noinspection PyUnresolvedReferences,PyProtectedMember
    _units = tuple(inspect._signature_fromstr(
        inspect.Signature, None, inspect.getdoc(datetime.timedelta).splitlines()[2]).parameters)

    def __new__(cls, string: str):
        matched = cls._match(string)
        return super().__new__(cls, *(float(matched.group(unit) or 0) for unit in cls._units) if matched else ())

    def __int__(self):
        return int(float(self))

    __float__ = datetime.timedelta.total_seconds


def _to_type(string: str, expected: type[T]) -> T:
    if isinstance(val := ast.literal_eval(string), expected):
        return val
    else:
        raise TypeError


def to_bool(string: str) -> bool:
    return _to_type(string, bool)


def to_bytes(string: str) -> bytes:
    return _to_type(string, bytes)


def to_complex(string: str) -> complex:
    return _to_type(string, complex)


def to_dict(string: str) -> dict:
    return _to_type(string, dict)


def to_float(string: str) -> float:
    return _to_type(string, float)


def to_int(string: str) -> int:
    return _to_type(string, int)


def to_list(string: str) -> list:
    return _to_type(string, list)


def to_set(string: str) -> set:
    return _to_type(string, set)


def to_str(string: str) -> str:
    return _to_type(string, str)


def to_tuple(string: str) -> tuple:
    return _to_type(string, tuple)


def get_progress(current: float = 0, width: int = 100, bars: str = ProgressBar.BLOCK_HORIZONTAL) -> str:
    if current < 0:
        current = 0
    elif current > 1:
        current = 1
    each = 1 / width
    filled = int(current / each)
    index = int((len(bars) - 1) / each * (current - filled * each))
    return f'{bars[-1] * filled}{bars[index] * bool(index)}{bars[0] * (width - filled - bool(index))}'


def len_ex(itt: Iterable) -> int:
    return sum(1 for _ in itt)


def index_ex(itt: Iterable, value) -> int:
    for index, ele in enumerate(itt):
        if value == ele:
            return index
    return -1


def any_ex(itt: Iterable, func: Callable, args: Optional[Iterable] = None,
           kwargs: Optional[Mapping[str, Any]] = None) -> bool:
    for ele in itt:
        res = func(ele, *() if args is None else args, **{} if kwargs is None else kwargs)
        if res:
            return True
    return False


def chain_ex(*funcs: Callable, args: Optional[Iterable[Optional[Iterable]]] = None,
             kwargs: Optional[Iterable[Optional[Mapping[str, Any]]]] = None) -> Generator:
    for func, args_, kwargs_ in itertools.zip_longest(
            funcs, () if args is None else args, {} if kwargs is None else kwargs):
        if not func:
            break
        yield func(*() if args_ is None else args_, **{} if kwargs_ is None else kwargs_)


def cycle_ex(itt: Iterable, func: Optional[Callable] = None, args: Optional[Iterable] = None,
             kwargs: Optional[Mapping[str, Any]] = None) -> Generator:
    args = () if args is None else args
    kwargs = {} if kwargs is None else kwargs
    while True:
        for ele in itt:
            yield ele
        if func:
            func(*args, **kwargs)


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


def consume(itt: Iterable, count: int = -1) -> int:
    count_ = itertools.count()
    if count:
        count -= 1
        for _, index in zip(itt, count_):
            if count == index:
                break
    return next(count_)


def consume_ex(itt: Iterable, item) -> Optional[int]:
    count = itertools.count()
    for index, item_ in zip(count, itt):
        if item == item_:
            return index


def randint_ex() -> int:
    return secrets.choice(secrets.token_bytes())


def reversed_ex(*items) -> Any:
    for ele in reversed(items):
        yield ele


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


def try_ex(*funcs: Callable, args: Optional[Iterable[Optional[Iterable]]] = None,
           kwargs: Optional[Iterable[Optional[Mapping[str, Any]]]] = None,
           excs: Optional[Iterable[Optional[Iterable[type[BaseException]]]]] = None) -> Any:
    for func, func_args, func_kwargs, func_excs in itertools.zip_longest(
            funcs, () if args is None else args, () if kwargs is None else kwargs, () if excs is None else excs):
        if func is None:
            break
        with contextlib.suppress(*() if func_excs is None else func_excs):
            return func(*() if func_args is None else func_args, **{} if func_kwargs is None else func_kwargs)


def pass_ex(*_, **__):
    pass


def pretty_vars(obj) -> str:
    dict_ = getattr(obj, '__dict__', {})
    attrs = [], []
    for val in dict_.values():
        attrs[0].append(type(val).__name__)
        attrs[1].append(str(sys.getsizeof(val)))
    pads = tuple(len(max(itt, key=len)) for itt in (dict_,) + attrs)
    end = f'\n{" " * (sum(pads) + 6)}'
    fmt = ''
    for item, type_, size in zip(dict_.items(), *attrs):
        fmt += (f'{f"{item[0]}: ":{pads[0] + 2}}[{type_:{pads[1]}} {size:>{pads[2]}}] '
                f'{pprint.pformat(item[1], sort_dicts=False).replace(end[0], end)}\n')
    return fmt


def fix_dict_key(cur_dict: dict, key: str, vals: Iterable, default_dict: dict):
    cur_val = cur_dict[key]
    if isinstance(cur_val, str):
        cur_val = cur_val.casefold()
        for val in vals:
            if cur_val == val.casefold():
                cur_dict[key] = val
                return
    else:
        if cur_val in vals:
            return
    cur_dict[key] = default_dict[key]


# noinspection PyShadowingNames
def clear_queue(queue: queue.Queue) -> int:
    with queue.mutex:
        tasks = queue.unfinished_tasks
        queue.queue.clear()
        queue.unfinished_tasks = 0
    return tasks


def iter_stream(stream: IO, size: Optional[int] = None) -> Generator[AnyStr, None, None]:
    read = stream.read
    size = size or sys.maxsize
    chunk = read(size)
    while chunk:
        yield chunk
        chunk = read(size)


def re_join(base: str, *child: str, sep: str = os.sep) -> str:
    return re.escape(sep).join((base,) + child)


def return_any(func: Callable, args: Optional[Iterable] = None,
               kwargs: Optional[Mapping[str, Any]] = None, max_try: Optional[int] = None) -> Any:
    args = () if args is None else args
    kwargs = {} if kwargs is None else kwargs
    for _ in (range if max_try else itertools.repeat)(max_try):
        res = func(*args, **kwargs)
        if res:
            return res


def strip_ansi(string: str) -> str:
    return ANSI.sub('', string)


def split_ex(string: str, length: int = 64) -> tuple[str]:
    return tuple(string[index: length + index] for index in range(0, len(string), length))


def shrink_string(string: str, max_len: int, filler: str = '...') -> str:
    return f'{string[:max_len - len(filler)]}{filler}' if len(string) > max_len else string


def shrink_string_mid(string: str, max_len: int, filler: str = '...') -> str:
    if len(string) > max_len:
        max_ = max_len - len(filler)
        left = math.ceil(max_ / 2)
        string = f'{string[:left]}{filler}{string[left - max_:]}'
    return string


def compress(datas: Mapping[str, bytes | str], compression: int = zipfile.ZIP_STORED) -> bytes:
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, 'w', compression) as file:
        for name, data in datas.items():
            file.writestr(name, data)
    return stream.getvalue()


def decompress(data: bytes, *names: str, password: Optional[bytes] = None) -> Mapping[str, Optional[bytes]]:
    datas = {name: None for name in names}
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


def _get_key(key: Optional[bytes | int | str]) -> bytes:
    if key is None:
        key = uuid.getnode()
    if isinstance(key, int):
        key = str(key)
    if isinstance(key, str):
        key = key.encode()
    return key


def encrypt(obj, key: Optional[bytes | int | str] = None, split: bool = False, proto: int = pickle.HIGHEST_PROTOCOL) -> str:
    try:
        pickled = pickle.dumps(obj, proto)
    except TypeError:
        return ''
    base64 = binascii.b2a_base64(zlib.compress(hashlib.blake2b(
        pickled, key=_get_key(key)).digest() + pickled), newline=False).decode()
    return '\n'.join(split_ex(base64)) if split else base64


def decrypt(data: str, default: Any = None, key: Optional[bytes | int | str] = None) -> Any:
    try:
        decoded = zlib.decompress(binascii.a2b_base64(''.join(data.split('\n')).encode()))
    except (binascii.Error, zlib.error):
        return default
    size = hashlib.blake2b().digest_size
    if decoded[:size] == hashlib.blake2b(decoded[size:], key=_get_key(key)).digest():
        try:
            return pickle.loads(decoded[size:])
        except (AttributeError, ModuleNotFoundError, pickle.UnpicklingError):
            return default
    else:
        return default


# noinspection PyShadowingBuiltins
def hook_except(func: Callable, args: Optional[Iterable] = None,
                kwargs: Optional[Mapping[str, Any]] = None, format: bool = False):
    if args is None:
        args = ()
    if kwargs is None:
        kwargs = {}

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
        func(*hook_args, *args, **hook_kwargs, **kwargs)

    sys.excepthook = functools.partial(wrapper, sys.excepthook)
    threading.excepthook = functools.partial(wrapper, threading.excepthook)


def _call(func: Callable, args: Iterable, kwargs: Mapping[str, Any], res, res_as_arg: bool, unpack_res: bool) -> Any:
    if res_as_arg:
        if unpack_res:
            if isinstance(res, Mapping):
                return func(**res)
            elif isinstance(res, Iterable):
                return func(*res)
        return func(res)
    return func(*args, **kwargs)


def call_after(pre_func: Callable, res_as_arg: bool = False, unpack_res: bool = False) -> Callable:
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            return _call(func, args, kwargs, pre_func(*args, **kwargs), res_as_arg, unpack_res)

        return wrapped

    return wrapper


def call_before(post_func: Callable, res_as_arg: bool = False, unpack_res: bool = False) -> Callable:
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            res = func(*args, **kwargs)
            _call(post_func, args, kwargs, res, res_as_arg, unpack_res)
            return res

        return wrapped

    return wrapper
