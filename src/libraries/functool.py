__version__ = '0.0.9'

import binascii
import collections
import ctypes
import functools
import hashlib
import itertools
import pickle
import pprint
import queue
import re
import secrets
import sys
import threading
import time
import uuid
from typing import Any, Callable, Generator, Iterable, Mapping, NoReturn, Optional


class Bool:  # TODO: threading.Event
    def __init__(self,
                 state: bool = False):
        self._state = state
        self._state_ = state

    def __bool__(self):
        return self._state

    def __str__(self):
        return str(self._state)

    def set(self):
        self._state = True

    def unset(self):
        self._state = False

    def clear(self):
        self._state = self._state_


class Func:
    def __init__(self,
                 func: Optional[Callable] = None,
                 args: Optional[Iterable] = None,
                 kwargs: Optional[Mapping[str, Any]] = None):
        self.func = func
        self.args = args or ()
        self.kwargs = kwargs or {}
        if func:
            functools.update_wrapper(self, self.func)

    def __call__(self) -> Any:
        if self.func:
            return self.func(*self.args, *self.kwargs)


def any_ex(itt: Iterable) -> Any:
    for ele in itt:
        if ele:
            return ele


def cycle_ex(itt: Iterable,
             func: Optional[Callable] = None,
             args: Optional[Iterable] = None,
             kwargs: Optional[Mapping[str, Any]] = None) -> Generator:
    args = args or ()
    kwargs = kwargs or {}
    while True:
        for ele in itt:
            yield ele
        if func:
            func(*args, **kwargs)


def dict_ex(obj: Any) -> dict[str, Any]:
    return getattr(obj, '__dict__', {})


def eq_ex(a: Any,
          b: Any) -> bool:
    sleep_ex()
    if isinstance(a, Iterable) and isinstance(b, Iterable):
        empty = object()
        for a_, b_ in itertools.zip_longest(a, b, fillvalue=empty):
            sleep_ex()
            if eq_ex(a_, empty) or eq_ex(b_, empty) or not eq_ex(a_, b_):
                return False
        return True
    else:
        return a == b


def randint_ex() -> int:
    return secrets.choice(secrets.token_bytes())


def reversed_ex(*items: Any) -> Any:
    for ele in reversed(items):
        yield ele


def replace_ex(string: str,
               a: str,
               b: str) -> str:
    return ''.join(a if char == b else b if char == a else char for char in string)


def setattr_ex(obj: Any,
               name: str,
               value: Any) -> None:
    ctypes.cast(id(obj) + type(obj).__dictoffset__, ctypes.POINTER(ctypes.py_object)).contents.value[name] = value


def sleep_ex(secs: Optional[float] = None) -> None:
    if secs is None:
        while secrets.randbelow(return_any(randint_ex)):
            pass
    elif secs != 0:
        end_time = time.time() + secs
        while end_time > time.time():
            pass


# noinspection PyUnresolvedReferences
def try_ex(*funcs: Callable,
           args: Optional[Iterable[Optional[Iterable]]] = None,
           kwargs: Optional[Iterable[Optional[Mapping[str, Any]]]] = None,
           excs: Optional[Iterable[Optional[Iterable[type[BaseException]]]]] = None) -> Any:
    for func, args_, kwargs_, excs_ in itertools.zip_longest(funcs, args or (), kwargs or {}, excs or ()):
        if not func:
            break
        try:
            ret = func(*args_ or (), **kwargs_ or {})
        except excs_ or ():
            pass
        else:
            return ret


def vars_ex(obj: Any) -> str:
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


def return_any(func: Callable,
               args: Optional[Iterable] = None,
               kwargs: Optional[Mapping[str, Any]] = None,
               max_try: Optional[int] = None) -> Any:
    args = args or ()
    kwargs = kwargs or {}
    for _ in (range if max_try else itertools.repeat)(max_try):
        ret = func(*args, **kwargs)
        if ret:
            return ret


def strip_ansi(string: str) -> str:
    return re.sub(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])', '', string)


def decrypt(data: str,
            default: Any = None) -> Any:
    try:
        decoded = binascii.a2b_base64(data.encode())
    except binascii.Error:
        return default
    size = hashlib.blake2b().digest_size
    return pickle.loads(decoded[size:]) if decoded[:size] == hashlib.blake2b(
        decoded[size:], key=str(uuid.getnode()).encode()).digest() else default


def encrypt(obj: Any) -> str:
    try:
        pickled = pickle.dumps(obj)
    except TypeError:
        return ''
    return binascii.b2a_base64(hashlib.blake2b(pickled, key=str(
        uuid.getnode()).encode()).digest() + pickled, newline=False).decode()


def one_cache(func: Callable) -> Callable:
    cache = collections.deque(maxlen=2)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        params = args + tuple(kwargs.items())
        params = try_ex(hash, pickle.dumps, args=((params,), (params,)), excs=((TypeError,), (ValueError,))) or params
        if cache.maxlen != len(cache) or cache[1] != params:
            cache.append(func(*args, **kwargs))
            cache.append(params)
        return cache[0]

    wrapper.dumps = lambda: encrypt(cache)
    wrapper.loads = lambda data: cache.extend(decrypt(data, cache))
    wrapper.reset = cache.clear
    return wrapper


def once_run(func: Callable) -> Callable:
    ran = Bool()

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not ran:
            ret = func(*args, **kwargs)
            ran.set()
            return ret

    wrapper.reset = ran.clear
    return wrapper


def _worker(func: Callable,
            works: queue.Queue,
            running: Bool) -> NoReturn:
    while True:
        work = works.get()
        running.set()
        try:
            func(*work[0], **work[1])
        finally:
            running.unset()
            if works.unfinished_tasks:
                works.task_done()


def queue_run(func: Callable) -> Callable:
    running = Bool()
    works = queue.Queue()

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        works.put((args, kwargs))

    threading.Thread(target=_worker, name=f'{queue_run.__name__}-{__version__}-{func.__name__}',
                     args=(func, works, running), daemon=True).start()
    wrapper.is_running = lambda: running or bool(works.unfinished_tasks)
    wrapper.reset = lambda: clear_queue(works)
    return wrapper


def singleton_run(func: Callable) -> Callable:
    running = Bool()

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if running:
            return False
        else:
            running.set()
            try:
                return func(*args, **kwargs)
            finally:
                running.unset()

    wrapper.is_running = lambda: bool(running)
    return wrapper


def threaded_run(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        threading.Thread(target=func, name=f'{threaded_run.__name__}-{__version__}-{func.__name__}',
                         args=args, kwargs=kwargs).start()

    return wrapper


def _call(func: Callable,
          args: Iterable,
          kwargs: Mapping[str, Any],
          ret: Any,
          redirect: Optional[bool],
          unpack: Optional[bool]):
    if redirect:
        if unpack:
            if isinstance(ret, Iterable):
                return func(*ret)
            elif isinstance(ret, Mapping):
                return func(**ret)
        return func(ret)
    return func(*args, **kwargs)


def call_after(pre_func: Callable,
               redirect: Optional[bool] = None,
               unpack: Optional[bool] = None) -> Callable[[Callable], Callable]:
    def wrapped(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            ret = pre_func(*args, **kwargs)
            return _call(func, args, kwargs, ret, redirect, unpack)

        return wrapper

    return wrapped


def call_before(post_func: Callable,
                redirect: Optional[bool] = None,
                unpack: Optional[bool] = None) -> Callable[[Callable], Callable]:
    def wrapped(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            ret = func(*args, **kwargs)
            _call(post_func, args, kwargs, ret, redirect, unpack)
            return ret

        return wrapper

    return wrapped
