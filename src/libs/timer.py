__version__ = '0.0.6'  # TODO revamp

import contextlib
import ctypes
import functools
import math
import threading
import time
from typing import Any, Callable, Iterable, Mapping, Optional


class _TimerExit(SystemExit):
    pass


_CTimerExit = ctypes.py_object(_TimerExit)


class Timer:
    _selves = []
    last_start = math.inf

    def __init__(self, interval: float, target: Callable, args: Optional[Iterable] = None,
                 kwargs: Optional[Mapping[str, Any]] = None, once: bool = False, start: bool = False):
        self._interval = interval
        self.target = target
        self.args = () if args is None else args
        self.kwargs = {} if kwargs is None else kwargs
        self.once = once
        self._running = 0
        self._timers: list[threading.Timer] = []
        self._selves.append(self)
        if start:
            self.start()

    @classmethod
    def kill_all(cls):
        for self in cls._selves:
            self.kill()

    @property
    def running(self) -> bool:
        return bool(self._running)

    def _clean_timers(self):
        for timer in tuple(self._timers):
            if not timer.is_alive():
                try:
                    self._timers.remove(timer)
                except ValueError:
                    pass

    def _callback(self):
        self._running += 1
        self.last_start = time.time()
        if self._interval != 0 and not self.once:
            self.start()
        try:
            with contextlib.suppress(_TimerExit):
                self.result = self.target(*self.args, **self.kwargs)
        finally:
            self._running -= 1

    def set_next_interval(self, interval: float):
        self._interval = interval

    def is_not_stopped(self, index: int = -1) -> bool:
        try:
            return self._timers[index].is_alive()
        except IndexError:
            return False

    def start(self, after: Optional[float] = None):
        self.stop()
        self._clean_timers()
        timer = threading.Timer(self._interval if after is None else after, self._callback)
        timer.name = f'{__name__}-{__version__}-{type(self).__name__}({self.target.__name__})'
        timer.daemon = True
        timer.start()
        self._timers.append(timer)

    def start_once(self):
        once = self.once
        self.once = True
        self.start(0)
        self.once = once

    def stop(self, _index: int = -1) -> bool:
        try:
            timer = self._timers[_index]
        except IndexError:
            pass
        else:
            timer.cancel()
            return not timer.is_alive()
        return False

    def kill(self):
        for timer in tuple(self._timers):
            if timer.is_alive():
                ctypes.pythonapi.PyThreadState_SetAsyncExc(timer.ident, _CTimerExit)
        self._clean_timers()


def start_once(interval: Optional[float], target: Callable, args: Optional[Iterable] = None,
               kwargs: Optional[Mapping[str, Any]] = None) -> Timer:
    return Timer(0 if interval is None else interval, target, args, kwargs, True, True)


def on_thread(target: Callable) -> Callable:
    @functools.wraps(target)
    def wrapped(*args, **kwargs) -> Timer:
        return start_once(None, target, args, kwargs)

    return wrapped
