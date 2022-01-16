from __future__ import annotations as _

__version__ = '0.0.6'

import contextlib
import ctypes
import functools
import threading
import time
from typing import Any, Callable, Iterable, Mapping, Optional

PASS: Callable = lambda *_, **__: None


class _Bool:
    def __init__(self, state: Optional[bool] = None):
        self._count = 1 if state else 0

    def __bool__(self):
        return bool(self._count)

    def set(self):
        self._count += 1

    def clear(self):
        self._count -= 1

    def reset(self):
        self._count = 0


class _TimerExit(SystemExit):
    pass


_CTimerExit = ctypes.py_object(_TimerExit)


class Timer:
    _Timers: list[Timer] = []
    last_start = -1

    def __init__(self, interval: Optional[float] = None, callback: Optional[Callable] = None,
                 args: Optional[Iterable] = None, kwargs: Optional[Mapping[str, Any]] = None,
                 once: Optional[bool] = None, start: Optional[bool] = None):
        self._interval = 0 if interval is None else interval
        self.callback = PASS if callback is None else callback
        self.args = () if args is None else args
        self.kwargs = {} if kwargs is None else kwargs
        self.once = once
        self._running = _Bool()
        self._timers: list[threading.Timer] = []
        self._Timers.append(self)
        if start:
            self.start()

    @classmethod
    def kill_all(cls) -> bool:
        killed = True
        for timer in cls._Timers:
            killed = timer.kill() and killed
        return killed

    @property
    def running(self) -> bool:
        return bool(self._running)

    def _clean_timers(self) -> int:
        removed = 0
        for timer in tuple(self._timers):
            if not timer.is_alive():
                try:
                    self._timers.remove(timer)
                except ValueError:
                    pass
                else:
                    removed += 1
        return removed

    def _function(self):
        self._running.set()
        self.last_start = time.time()
        if not self.once:
            self.start()
        try:
            with contextlib.suppress(_TimerExit):
                self.result = self.callback(*self.args, **self.kwargs)
        finally:
            self._running.clear()

    def set_next_interval(self, interval: float):
        self._interval = interval

    def is_not_stopped(self, index: int = -1) -> bool:
        with contextlib.suppress(IndexError):
            return self._timers[index].is_alive()
        return False

    def start(self, interval: Optional[float] = None):
        self.stop()
        self._clean_timers()
        if interval is not None:
            self.set_next_interval(interval)
        timer = threading.Timer(self._interval, self._function)
        timer.name = f'{type(self).__name__}-{__version__}-{self.callback.__name__}'
        timer.daemon = True
        timer.start()
        self._timers.append(timer)

    def stop(self, index: int = -1) -> bool:
        try:
            timer = self._timers[index]
        except IndexError:
            pass
        else:
            timer.cancel()
            return not timer.is_alive()
        return False

    def kill(self) -> int:
        killed = 0
        for timer in tuple(self._timers):
            if timer.is_alive():
                killed += ctypes.pythonapi.PyThreadState_SetAsyncExc(timer.ident, _CTimerExit)
        self._clean_timers()
        return killed


def start_once(interval: Optional[float] = None, callback: Optional[Callable] = None, args: Optional[Iterable] = None,
               kwargs: Optional[Mapping[str, Any]] = None) -> Timer:
    return Timer(interval, callback, args, kwargs, True, True)


def on_thread(callback: Callable) -> Callable:
    @functools.wraps(callback)
    def wrapper(*args, **kwargs):
        start_once(callback=callback, args=args, kwargs=kwargs)

    return wrapper
