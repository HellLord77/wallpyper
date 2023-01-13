from __future__ import annotations as _

__version__ = '0.0.1'

import collections
import functools
import math
import pickle
import queue
import threading
import time
import weakref
from typing import Any, Callable, Generator, NoReturn, Optional


def _get_params(args: tuple, kwargs: dict[str, Any]) -> Any:
    params = args + tuple(kwargs.items())
    try:
        params = hash(params)
    except TypeError:
        try:
            params = pickle.dumps(params, pickle.HIGHEST_PROTOCOL)
        except ValueError:
            pass
    return params


class _IsRunningMixin:
    _selves: weakref.WeakSet[_IsRunningMixin]

    def __init_subclass__(cls, **kwargs):
        cls._selves = weakref.WeakSet()
        super().__init_subclass__(**kwargs)

    def __init__(self, *args, **kwargs):
        self._selves.add(self)
        super().__init__(*args, **kwargs)

    def is_running(self) -> bool:
        raise NotImplementedError

    @classmethod
    def get_running(cls) -> Generator[_IsRunningMixin, None, None]:
        for self in cls._selves:
            if self.is_running():
                yield self


class _Callable(Callable):
    def __init__(self, func: Callable):
        self.__func__ = func
        super().__init__()

    def __call__(self, *args, **kwargs) -> Any:
        raise NotImplementedError


class LastCacheCallable(_Callable):
    _cache = None

    def __call__(self, *args, **kwargs) -> Any:
        params = _get_params(args, kwargs)
        if not self._cache or self._cache[0] != params:
            self._cache = params, self.__func__(*args, **kwargs)
        return self._cache[1]

    def dumps(self) -> bytes:
        return pickle.dumps(self._cache, pickle.HIGHEST_PROTOCOL)

    def loads(self, data: bytes) -> bool:
        try:
            cache = pickle.loads(data)
        except (AttributeError, ModuleNotFoundError, pickle.UnpicklingError):
            return False
        else:
            self._cache = cache
            return True

    def reset(self) -> bool:
        try:
            return bool(self._cache)
        finally:
            self._cache = None


class OnceCallable(_Callable):
    _run = False

    def __call__(self, *args, **kwargs) -> Any:
        if not self._run:
            try:
                return self.__func__(*args, **kwargs)
            finally:
                self._run = True

    def reset(self) -> bool:
        try:
            return self._run
        finally:
            self._run = False

    def has_run(self) -> bool:
        return self._run


class QueueCallable(_Callable, _IsRunningMixin):
    def __init__(self, func: Callable):
        self._lock = threading.Lock()
        super().__init__(func)

    def __call__(self, *args, **kwargs) -> Any:
        with self._lock:
            return self.__func__(*args, **kwargs)

    def is_running(self) -> bool:
        return self._lock.locked()


class QueueThreadCallable(_Callable, _IsRunningMixin):
    _res = None

    def __init__(self, func: Callable):
        self._works = queue.Queue()
        threading.Thread(target=self._worker,
                         name=f'{__name__}-{__version__}-{type(self).__name__}({func.__name__})', daemon=True).start()
        super().__init__(func)

    def __call__(self, *args, **kwargs):
        self._works.put((args, kwargs))

    def _worker(self) -> NoReturn:
        while True:
            params = self._works.get()
            try:
                self._res = self.__func__(*params[0], **params[1])
            finally:
                if self._works.unfinished_tasks:
                    self._works.task_done()

    def is_running(self) -> bool:
        return bool(self._works.unfinished_tasks)

    def reset(self) -> bool:
        try:
            return not self._works.unfinished_tasks
        finally:
            self._works.queue.clear()
            self._works.unfinished_tasks = 0

    def get_result(self) -> Any:
        return self._res


class SingletonCallable(_Callable, _IsRunningMixin):
    _run = False

    def __call__(self, *args, **kwargs) -> Any:
        if not self._run:
            self._run = True
            try:
                return self.__func__(*args, **kwargs)
            finally:
                self._run = False

    def is_running(self) -> bool:
        return bool(self._run)


class ThreadedCallable(_Callable):
    _res = None

    def __call__(self, *args, **kwargs):
        threading.Thread(target=lambda: setattr(self, '_res', self.__func__(
            *args, **kwargs)), name=f'{__name__}-{__version__}-{type(self).__name__}'
                                    f'({self.__func__.__name__})').start()

    def get_result(self) -> Any:
        return self._res


class TimedCacheCallable(_Callable):
    def __new__(cls, *args, **kwargs):
        if args:
            return super().__new__(cls)
        else:
            return functools.partial(cls, *args, **kwargs)

    def __init__(self, func: Callable, secs: float = math.inf, size: Optional[int] = None):
        self._timeout = secs
        self._cache = collections.deque(maxlen=size)
        super().__init__(func)

    def __call__(self, *args, **kwargs) -> Any:
        remove = []
        params = _get_params(args, kwargs)
        params_res_timeout = None
        current = time.monotonic()
        for params_res_timeout_ in self._cache:
            if current > params_res_timeout_[2]:
                remove.append(params_res_timeout_)
            elif params == params_res_timeout_[0]:
                params_res_timeout = params_res_timeout_
        for params_res_timeout_ in remove:
            self._cache.remove(params_res_timeout_)
        if params_res_timeout is None:
            params_res_timeout = params, self.__func__(*args, **kwargs), current + self._timeout
            self._cache.append(params_res_timeout)
        return params_res_timeout[1]

    def reset(self) -> bool:
        try:
            return bool(self._cache)
        finally:
            self._cache.clear()
