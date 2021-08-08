__version__ = '0.1.0'

import binascii
import ctypes
import functools
import hashlib
import itertools
import pickle
import secrets
import time
import typing
import uuid


class _Bool:
    def __init__(self,
                 state: bool = False):
        self._state = state
        self._state_ = state

    def __bool__(self):
        return self._state

    def set(self):
        self._state = True

    def unset(self):
        self._state = False

    def clear(self):
        self._state = self._state_


class Func:
    def __init__(self,
                 func: typing.Optional[typing.Callable] = None,
                 args: typing.Optional[tuple] = None,
                 kwargs: typing.Optional[dict[str, typing.Any]] = None):
        self.func = func
        self.args = args or ()
        self.kwargs = kwargs or {}
        if func:
            functools.update_wrapper(self, self.func)

    def __call__(self) -> typing.Any:
        if self.func:
            return self.func(*self.args, *self.kwargs)


def any_ex(func: typing.Callable,
           args: typing.Optional[tuple] = None,
           kwargs: typing.Optional[dict[str, typing.Any]] = None,
           max_try: typing.Optional[int] = None) -> typing.Any:
    args = args or ()
    kwargs = kwargs or {}
    for _ in (range if max_try else itertools.repeat)(max_try):
        ret = func(*args, **kwargs)
        if ret:
            return ret


def eq_ex(a: typing.Any,
          b: typing.Any) -> bool:
    sleep_ex()
    if isinstance(a, typing.Iterable) and isinstance(b, typing.Iterable):
        empty = object()
        for a_, b_ in itertools.zip_longest(a, b, fillvalue=empty):
            sleep_ex()
            if eq_ex(a_, empty) or eq_ex(b_, empty) or not eq_ex(a_, b_):
                return False
        return True
    else:
        return a == b


def get_any(iterable: typing.Iterable) -> typing.Any:
    for item in iterable:
        if item:
            return item


def randint_ex() -> int:
    return secrets.choice(secrets.token_bytes())


def setattr_ex(obj: typing.Any,
               name: str,
               value: typing.Any):
    ctypes.cast(id(obj) + type(obj).__dictoffset__, ctypes.POINTER(ctypes.py_object)).contents.value[name] = value


def sleep_ex(secs: typing.Optional[float] = None) -> None:
    if secs is None:
        while secrets.randbelow(any_ex(randint_ex)):
            pass
    elif secs != 0:
        end_time = time.time() + secs
        while end_time > time.time():
            pass


def encrypt(obj: typing.Any) -> str:
    pickled = pickle.dumps(obj)
    return binascii.b2a_base64(
        hashlib.blake2b(pickled, key=str(uuid.getnode()).encode()).digest() + pickled, newline=False).decode()


def decrypt(data: str,
            default: typing.Any = None) -> typing.Any:
    decoded = binascii.a2b_base64(data.encode())
    size = hashlib.blake2b().digest_size
    return pickle.loads(decoded[size:]) if decoded[:size] == hashlib.blake2b(
        decoded[size:], key=str(uuid.getnode()).encode()).digest() else default


def one_cache(func: typing.Callable) -> typing.Callable:
    cache = []

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not cache or cache[0] != args or cache[1] != kwargs:
            cache[:] = args, kwargs, func(*args, **kwargs)
        return cache[2]

    wrapper.dumps = lambda: encrypt(cache)
    wrapper.loads = lambda data: (cache.clear(), cache.extend(decrypt(data, cache.copy())))
    wrapper.reset = cache.clear
    return wrapper


def once_run(func: typing.Callable) -> typing.Callable:
    ran = _Bool()

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not ran:
            ret = func(*args, **kwargs)
            ran.set()
            return ret

    wrapper.reset = ran.clear
    return wrapper


def singleton_run(func: typing.Callable) -> typing.Callable:
    running = _Bool()

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

    wrapper.is_running = running.__bool__
    return wrapper


def call_after(pre_func: typing.Callable,
               redirect: typing.Optional[bool] = None) -> typing.Callable[[typing.Callable], typing.Callable]:
    def wrapped(func: typing.Callable) -> typing.Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            ret = pre_func(*args, **kwargs)
            return func(ret) if redirect else func(*args, **kwargs)

        return wrapper

    return wrapped


def call_before(post_func,
                redirect: typing.Optional[bool] = None) -> typing.Callable[[typing.Callable], typing.Callable]:
    def wrapped(func: typing.Callable) -> typing.Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # noinspection PyListCreation
            ret = [func(*args, **kwargs)]
            ret.append(post_func(ret[0]) if redirect else post_func(*args, **kwargs))
            return ret[bool(redirect)]

        return wrapper

    return wrapped
