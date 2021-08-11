__version__ = '0.0.3'

import collections
import contextlib
import ctypes
import functools
import threading
from typing import Optional, Any, Callable, Mapping, Iterable

MAX_LEN = ctypes.sizeof(ctypes.c_void_p)


class _TimerExit(SystemExit):
    pass


class Timer:
    _instances = []

    @classmethod
    def kill_all(cls) -> bool:
        killed = True
        for timer in cls._instances:
            killed = timer.kill() and killed
        return killed

    def __init__(self,
                 callback: Callable,
                 callback_args: Optional[Iterable] = None,
                 callback_kwargs: Optional[Mapping[str, Any]] = None,
                 interval: Optional[float] = None,
                 once: Optional[bool] = None) -> None:
        @functools.wraps(callback)
        def wrapper() -> None:
            self._running = True
            if not once:
                self.start()
            try:
                with contextlib.suppress(_TimerExit):
                    callback(*callback_args, **callback_kwargs)
            finally:
                self._running = False

        self._running = False
        self._timer = threading.Timer(interval or 0.0, wrapper)
        self._timers = collections.deque(maxlen=MAX_LEN)
        self._instances.append(self)

    @property
    def initialized(self) -> bool:
        return self._timer.is_alive()

    @property
    def running(self) -> bool:
        return self._running

    def start(self,
              interval: Optional[float] = None) -> bool:
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
        timer_exit = ctypes.py_object(_TimerExit)
        for timer in self._timers:
            if timer.is_alive():
                killed = ctypes.pythonapi.PyThreadState_SetAsyncExc(timer.ident, timer_exit) == 1 or killed
        return killed


def start_once(callback: Callable,
               callback_args: Optional[Iterable] = None,
               callback_kwargs: Optional[Mapping[str, Any]] = None,
               interval: Optional[float] = None) -> Timer:
    timer = Timer(callback, callback_args, callback_kwargs, interval, True)
    timer.start()
    return timer


def on_thread(callback: Callable) -> Callable:
    @functools.wraps(callback)
    def wrapper(*args, **kwargs):
        start_once(callback, args, kwargs)

    return wrapper
