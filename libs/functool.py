__version__ = '0.0.3'

import functools
import typing


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


class WrappedCallback:
    def __init__(self,
                 callback: typing.Optional[typing.Callable] = None,
                 args: typing.Optional[tuple] = None,
                 kwargs: typing.Optional[dict[str, typing.Any]] = None):
        self.callback = callback or (lambda *_, **__: None)
        self.args = args or ()
        self.kwargs = kwargs or {}
        functools.update_wrapper(self, self.callback)

    def __call__(self) -> typing.Any:
        return self.callback(*self.args, *self.kwargs)


def one_cache(callback: typing.Callable) -> typing.Callable:
    cache = []

    @functools.wraps(callback)
    def wrapper(*args, **kwargs):
        if not cache or cache[0] != args or cache[1] != kwargs:
            cache[:] = args, kwargs, callback(*args, **kwargs)
        return cache[2]

    wrapper.reset = cache.clear
    return wrapper


def once_run(callback: typing.Callable) -> typing.Callable:
    ran = _Bool()

    @functools.wraps(callback)
    def wrapper(*args, **kwargs):
        if not ran:
            return_ = callback(*args, **kwargs)
            ran.set()
            return return_

    wrapper.reset = ran.clear
    return wrapper


def one_run(callback: typing.Callable) -> typing.Callable:
    running = _Bool()

    @functools.wraps(callback)
    def wrapper(*args, **kwargs):
        if running:
            return False
        else:
            running.set()
            try:
                return callback(*args, **kwargs)
            finally:
                running.unset()

    wrapper.is_running = running.__bool__
    return wrapper
