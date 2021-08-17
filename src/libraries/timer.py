__version__ = '0.0.4'

import collections
import contextlib
import ctypes
import functools
import threading
from typing import Any, Callable, Iterable, Mapping, Optional

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
                 args: Optional[Iterable] = None,
                 kwargs: Optional[Mapping[str, Any]] = None,
                 interval: Optional[float] = None,
                 once: Optional[bool] = None) -> None:
        @functools.wraps(callback)
        def wrapper() -> None:
            self._running = True
            if not once:
                self.start()
            try:
                with contextlib.suppress(_TimerExit):
                    self._result = callback(*args, **kwargs)
            finally:
                self._running = False

        self._result = None
        self._running = False
        self._interval = interval or 0.0
        self._function = wrapper
        self._name = f'{type(self).__name__}-{__version__}-{callback.__name__}'
        self._timers = collections.deque(maxlen=MAX_LEN)
        self._instances.append(self)

    @property
    def initialized(self) -> bool:
        return self._timers and self._timers[-1].is_alive()

    @property
    def result(self) -> Any:
        return self._result

    @property
    def running(self) -> bool:
        return self._running

    def start(self,
              interval: Optional[float] = None) -> bool:
        self.stop()
        if interval is not None:
            self._interval = interval
        timer = threading.Timer(self._interval, self._function)
        timer.name = self._name
        timer.daemon = True
        timer.start()
        self._timers.append(timer)
        return self.initialized

    def stop(self) -> None:
        self._timers and self._timers[-1].cancel()

    def kill(self) -> bool:
        killed = False
        timer_exit = ctypes.py_object(_TimerExit)
        for timer in self._timers:
            if timer.is_alive():
                killed = ctypes.pythonapi.PyThreadState_SetAsyncExc(timer.ident, timer_exit) == 1 or killed
        return killed


def start_once(callback: Callable,
               args: Optional[Iterable] = None,
               kwargs: Optional[Mapping[str, Any]] = None,
               interval: Optional[float] = None) -> Timer:
    timer = Timer(callback, args, kwargs, interval, True)
    timer.start()
    return timer


def on_thread(callback: Callable) -> Callable:
    @functools.wraps(callback)
    def wrapper(*args, **kwargs):
        start_once(callback, args, kwargs)

    return wrapper
