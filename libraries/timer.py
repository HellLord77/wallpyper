__version__ = '0.0.2'

import collections
import contextlib
import ctypes
import functools
import threading
import typing

MAX_LEN = 5

_TIMERS = []


class _ThreadExit(SystemExit):
    pass


class Timer:
    def __init__(self,
                 callback: typing.Callable,
                 callback_args: typing.Optional[tuple] = None,
                 callback_kwargs: typing.Optional[dict[str, typing.Any]] = None,
                 interval: typing.Optional[float] = None,
                 once: typing.Optional[bool] = None) -> None:
        @functools.wraps(callback)
        def wrapper() -> None:
            self._running = True
            if not once:
                self.start()
            try:
                with contextlib.suppress(_ThreadExit):
                    callback(*callback_args or (), **callback_kwargs or {})
            finally:
                self._running = False

        self._running = False
        self._timer = threading.Timer(interval or 0.0, wrapper)
        self._timers = collections.deque((), MAX_LEN)
        _TIMERS.append(self)

    @property
    def initialized(self) -> bool:
        return self._timer.is_alive()

    @property
    def running(self) -> bool:
        return self._running

    def start(self,
              interval: typing.Optional[float] = None) -> bool:
        self.stop()
        if interval is not None:
            self._timer.interval = interval
        # noinspection PyUnresolvedReferences
        self._timer = threading.Timer(self._timer.interval, self._timer.function)
        self._timer.daemon = True
        # noinspection PyUnresolvedReferences
        self._timer.name = self._timer.function.__name__
        self._timer.start()
        self._timers.append(self._timer)
        return self.initialized

    def stop(self) -> None:
        self._timer.cancel()

    def kill(self) -> bool:
        killed = False
        for timer in self._timers:
            if timer.is_alive():
                killed = ctypes.pythonapi.PyThreadState_SetAsyncExc(timer.ident,
                                                                    ctypes.py_object(_ThreadExit)) == 1 or killed
        return killed


def start_once(callback: typing.Callable,
               callback_args: typing.Optional[tuple] = None,
               callback_kwargs: typing.Optional[dict[str, typing.Any]] = None,
               interval: typing.Optional[float] = None) -> Timer:
    timer = Timer(callback, callback_args, callback_kwargs, interval, True)
    timer.start()
    return timer


def start_now(callback: typing.Callable,
              callback_args: typing.Optional[tuple] = None,
              callback_kwargs: typing.Optional[dict[str, typing.Any]] = None) -> Timer:
    return start_once(callback, callback_args, callback_kwargs)


def on_thread(callback: typing.Callable) -> typing.Callable:
    @functools.wraps(callback)
    def wrapper(*args, **kwargs):
        start_now(callback, args, kwargs)

    return wrapper


def kill_all() -> bool:
    killed = True
    for timer in _TIMERS:
        killed = timer.kill() and killed
    return killed
