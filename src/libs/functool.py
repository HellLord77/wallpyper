__version__ = '0.0.14'

import binascii
import contextlib
import ctypes
import datetime
import functools
import hashlib
import inspect
import itertools
import os
import pickle
import pprint
import queue
import re
import secrets
import sys
import threading
import time
import uuid
from typing import Any, AnyStr, Callable, Generator, IO, Iterable, Mapping, NoReturn, Optional

DEFAULT = object()
ANSI = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')


class _Mutable:
    _type = type(None)  # FIXME types.NoneType (py 3.10)

    def __init__(self, val: Optional = None):
        self._data = self._type() if val is None else val

    def __int__(self):
        return int(self._data)

    def __float__(self):
        return float(self._data)

    def __bool__(self):
        return bool(self._data)

    def __str__(self):
        return str(self._data)

    def get(self):
        return self._data

    def set(self, val):
        self._data = val
        return val

    def clear(self):
        val = self._type()
        self._data = val
        return val


class MutableInt(_Mutable):
    _type = int
    get: Callable[[], _type]
    set: Callable[[_type], _type]
    clear: Callable[[], _type]


class PointedList:
    DEFAULT = None

    def __init__(self, val: Optional[list] = None, default: Any = DEFAULT):
        self._data = [] if val is None else val.copy()
        if default is not self.DEFAULT:
            self.DEFAULT = default
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
        return self._data[index] if self.has(index) else self.DEFAULT

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


class FrozenDict(dict):
    def __setitem__(self, *_, **__):
        pass

    def update(self, *_, **__):
        pass


class PackedFunction:
    def __init__(self, func: Optional[Callable] = None, args: Optional[Iterable] = None,
                 kwargs: Optional[Mapping[str, Any]] = None):
        self.func = pass_ex if func is None else func
        self.args = () if args is None else args
        self.kwargs = {} if kwargs is None else kwargs
        functools.update_wrapper(self, self.func)

    def __call__(self, args: Optional[Iterable] = None, kwargs: Optional[Mapping[str, Any]] = None) -> Any:
        return self.func(*self.args, *() if args is None else args, **{} if kwargs is None else kwargs, **self.kwargs)


class TimeDelta(datetime.timedelta):
    _match = " *".join(f"(?:(?P<{unit}s>[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)) *{unit}s?)?" for unit in
                       ("week", "day", "hour", "minute", "second", "millisecond", "microsecond"))
    _match = re.compile(f'^(?i) *{_match} *$').match
    # noinspection PyUnresolvedReferences,PyProtectedMember
    _units = tuple(inspect._signature_fromstr(inspect.Signature, None,
                                              inspect.getdoc(datetime.timedelta).splitlines()[2]).parameters)

    def __new__(cls, time_string: str):
        matched = cls._match(time_string)
        return super().__new__(cls, *(float(matched.group(unit) or 0) for unit in cls._units) if matched else ())

    def __int__(self):
        return int(float(self))

    __float__ = datetime.timedelta.total_seconds


def any_ex(itt: Iterable, func: Callable, args: Optional[Iterable] = None,
           kwargs: Optional[Mapping[str, Any]] = None) -> bool:
    for ele in itt:
        ret = func(ele, *() if args is None else args, **{} if kwargs is None else kwargs)
        if ret:
            return True
    return False


def chain_ex(*funcs: Callable, args: Optional[Iterable[Optional[Iterable]]] = None,
             kwargs: Optional[Iterable[Optional[Mapping[str, Any]]]] = None) -> Generator:
    for func, args_, kwargs_ in itertools.zip_longest(funcs, () if args is None else args,
                                                      {} if kwargs is None else kwargs):
        if not func:
            break
        yield func(*args_ or (), **kwargs_ or {})


def cycle_ex(itt: Iterable, func: Optional[Callable] = None, args: Optional[Iterable] = None,
             kwargs: Optional[Mapping[str, Any]] = None) -> Generator:
    args = () if args is None else args
    kwargs = {} if kwargs is None else kwargs
    while True:
        for ele in itt:
            yield ele
        if func:
            func(*args, **kwargs)


def dict_ex(obj) -> dict[str, Any]:
    return getattr(obj, '__dict__', {})


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


def exhaust(itt: Generator):
    for _ in itt:
        pass


def randint_ex() -> int:
    return secrets.choice(secrets.token_bytes())


def reversed_ex(*items) -> Any:
    for ele in reversed(items):
        yield ele


def replace_ex(string: str, a: str, b: str) -> str:
    return ''.join(a if char == b else b if char == a else char for char in string)


def setattr_ex(obj, name: str, value):
    ctypes.cast(id(obj) + type(obj).__dictoffset__, ctypes.POINTER(ctypes.py_object)).contents.value[name] = value


def sleep_ex(secs: Optional[float] = None):
    if secs is None:
        while secrets.randbelow(return_any(randint_ex)):
            pass
    elif secs != 0:
        end_time = time.time() + secs
        while end_time > time.time():
            pass


def try_ex(*funcs: Callable, args: Optional[Iterable[Optional[Iterable]]] = None,
           kwargs: Optional[Iterable[Optional[Mapping[str, Any]]]] = None,
           excs: Optional[Iterable[Optional[Iterable[type[BaseException]]]]] = None) -> Any:
    for func, args_, kwargs_, excs_ in itertools.zip_longest(funcs, () if args is None else args,
                                                             {} if kwargs is None else kwargs, excs or ()):
        if not func:
            break
        with contextlib.suppress(*excs_ or ()):
            return func(*args_ or (), **kwargs_ or {})


def pass_ex(*_, **__):
    pass


def vars_ex(obj) -> str:
    dict_ = dict_ex(obj)
    attrs = [], []
    for val in dict_.values():
        attrs[0].append(type(val).__name__)
        attrs[1].append(str(sys.getsizeof(val)))
    pads = tuple(len(max(itt, key=len)) for itt in (dict_,) + attrs)
    end = f'\n{" " * (sum(pads) + 6)}'
    fmt = ''
    for item, type_, size in zip(dict_.items(), *attrs):
        fmt += f'{f"{item[0]}: ":{pads[0] + 2}}[{type_:{pads[1]}} {size:>{pads[2]}}] ' \
               f'{pprint.pformat(item[1], sort_dicts=False).replace(end[0], end)}\n'
    return fmt


def clear_queue(queue_: queue.Queue) -> int:
    with queue_.mutex:
        tasks = queue_.unfinished_tasks
        queue_.queue.clear()
        queue_.unfinished_tasks = 0
    return tasks


def iter_io(io: IO, size: Optional[int] = None) -> Generator[AnyStr, None, None]:
    read = io.read
    size = size or sys.maxsize
    chunk = read(size)
    while chunk:
        yield chunk
        chunk = read(size)


def re_join(base: str, *child: str, sep: Optional[str] = None) -> str:
    return re.escape(os.sep if sep is None else sep).join((base,) + child)


def return_any(func: Callable, args: Optional[Iterable] = None, kwargs: Optional[Mapping[str, Any]] = None,
               max_try: Optional[int] = None) -> Any:
    args = () if args is None else args
    kwargs = {} if kwargs is None else kwargs
    for _ in (range if max_try else itertools.repeat)(max_try):
        ret = func(*args, **kwargs)
        if ret:
            return ret


def strip_ansi(string: str) -> str:
    return ANSI.sub('', string)


def decrypt(data: str, default: Any = None) -> Any:
    try:
        decoded = binascii.a2b_base64(data.encode())
    except binascii.Error:
        return default
    size = hashlib.blake2b().digest_size
    return pickle.loads(decoded[size:]) if decoded[:size] == hashlib.blake2b(decoded[size:], key=str(
        uuid.getnode()).encode()).digest() else default


def encrypt(obj) -> str:
    try:
        pickled = pickle.dumps(obj)
    except TypeError:
        return ''
    return binascii.b2a_base64(hashlib.blake2b(pickled, key=str(uuid.getnode()).encode()).digest() + pickled,
                               newline=False).decode()


def one_cache(func: Callable) -> Callable:
    cache = []

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        params = args + tuple(kwargs.items())
        params = try_ex(hash, pickle.dumps, args=((params,), (params,)), excs=((TypeError,), (ValueError,))) or params
        if not len(cache) or cache[0] != params:
            cache[:] = params, func(*args, **kwargs)
        return cache[1]

    wrapper.dumps = lambda: encrypt(cache)
    wrapper.loads = lambda data: cache.extend(decrypt(data, cache))
    wrapper.reset = cache.clear
    return wrapper


def once_run(func: Callable) -> Callable:
    ran = threading.Event()

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not ran.is_set():
            ret = func(*args, **kwargs)
            ran.set()
            return ret

    wrapper.reset = ran.clear
    return wrapper


def _queue_worker(func: Callable, works: queue.Queue[tuple[Iterable, Mapping[str, Any]]], running: threading.Event,
                  wrapper: Callable) -> NoReturn:
    while True:
        work = works.get()
        running.set()
        with contextlib.suppress(BaseException):
            try:
                wrapper.result = func(*work[0], **work[1])
            finally:
                running.clear()
                if works.unfinished_tasks:
                    works.task_done()


def queue_run(func: Callable) -> Callable:
    running = threading.Event()
    works = queue.Queue()

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        works.put((args, kwargs))

    threading.Thread(target=_queue_worker, name=f'{queue_run.__name__}-{__version__}-{func.__name__}',
                     args=(func, works, running, wrapper), daemon=True).start()
    wrapper.is_running = lambda: running.is_set() or bool(works.unfinished_tasks)
    wrapper.reset = lambda: clear_queue(works)
    wrapper.result = None
    return wrapper


def singleton_run(func: Callable) -> Callable:
    running = threading.Event()

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if running.is_set():
            return False
        else:
            running.set()
            try:
                return func(*args, **kwargs)
            finally:
                running.clear()

    wrapper.is_running = running.is_set
    return wrapper


def _set_result(func: Callable, args: Iterable, kwargs: Mapping[str, Any], wrapper: Callable):
    wrapper.result = func(*args, **kwargs)


def threaded_run(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        threading.Thread(target=_set_result, name=f'{threaded_run.__name__}-{__version__}-{func.__name__}',
                         args=(func, args, kwargs, wrapper)).start()

    wrapper.result = None
    return wrapper


def _call(func: Callable, args: Iterable, kwargs: Mapping[str, Any], ret, ret_as_arg: Optional[bool],
          unpack_ret: Optional[bool]) -> Any:
    if ret_as_arg:
        if unpack_ret:
            if isinstance(ret, Iterable):
                return func(*ret)
            elif isinstance(ret, Mapping):
                return func(**ret)
        return func(ret)
    return func(*args, **kwargs)


def call_after(pre_func: Callable, ret_as_arg: Optional[bool] = None, unpack_ret_arg: Optional[bool] = None) -> \
        Callable[[Callable], Callable]:
    def wrapped(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            ret = pre_func(*args, **kwargs)
            return _call(func, args, kwargs, ret, ret_as_arg, unpack_ret_arg)

        return wrapper

    return wrapped


def call_before(post_func: Callable, ret_as_arg: Optional[bool] = None, unpack_ret_arg: Optional[bool] = None) -> \
        Callable[[Callable], Callable]:
    def wrapped(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            ret = func(*args, **kwargs)
            _call(post_func, args, kwargs, ret, ret_as_arg, unpack_ret_arg)
            return ret

        return wrapper

    return wrapped
