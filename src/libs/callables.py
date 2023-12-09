from __future__ import annotations as _

__version__ = '0.0.5'

import collections
import functools
import inspect
import itertools
import math
import pickle
import queue
import sys
import threading
import time
import weakref
from types import NoneType
from typing import Any
from typing import Callable
from typing import Container
from typing import Iterable
from typing import Iterator
from typing import Mapping
from typing import NoReturn
from typing import Optional

_FMT_THREAD_NAME = f'{__name__}-{__version__}-{{}}({{}})'


def _get_params(args: tuple, kwargs: dict[str, Any],
                typed: bool = False) -> Any:
    params = args + tuple(kwargs.items())
    if typed:
        params += tuple(type(arg) for arg in args)
        params += tuple(type(arg) for arg in kwargs.values())
    try:
        params = hash(params)
    except TypeError:
        try:
            params = pickle.dumps(params, pickle.HIGHEST_PROTOCOL)
        except ValueError:
            pass
    return params


class _Callable(Callable):
    def __init__(self, func: Optional[Callable]):
        if func is None:
            raise TypeError(f'{NoneType.__name__!r} object is not callable')
        self.__func__ = func
        super().__init__()

    def __call__(self, *args, **kwargs) -> Any:
        raise NotImplementedError


class _RunningQueryable:
    _selves: weakref.WeakSet[_RunningQueryable]

    def __init_subclass__(cls, *args, **kwargs):
        cls._selves = weakref.WeakSet()
        super().__init_subclass__(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        self._selves.add(self)
        super().__init__(*args, **kwargs)

    def is_running(self) -> bool:
        raise NotImplementedError

    @classmethod
    def iter_running(cls) -> Iterator[_RunningQueryable]:
        for self in cls._selves:
            if self.is_running():
                yield self


class SingletonCallable(_Callable, _RunningQueryable):
    _run = False

    def __call__(self, *args, **kwargs) -> Any:
        if not self._run:
            self._run = True
            try:
                return self.__func__(*args, **kwargs)
            finally:
                self._run = False

    def is_running(self) -> bool:
        return self._run


class OnceCallable(_Callable):
    _run = False

    def __call__(self, *args, **kwargs) -> Any:
        if not self._run:
            self._run = True
            return self.__func__(*args, **kwargs)

    def reset(self) -> bool:
        try:
            return self._run
        finally:
            self._run = False

    def has_run(self) -> bool:
        return self._run


class ThreadedCallable(_Callable):
    _res = None

    def __call__(self, *args, **kwargs):
        threading.Thread(target=lambda: setattr(self, '_res', self.__func__(
            *args, **kwargs)), name=_FMT_THREAD_NAME.format(
            type(self).__name__, self.__func__.__name__)).start()

    def get_result(self) -> Any:
        return self._res


class FilteredCallable(_Callable):
    def __new__(cls, *args, **kwargs):
        if args:
            return super().__new__(cls)
        else:
            return functools.partial(cls, **kwargs)

    def __init__(self, func: Optional[Callable] = None, *,
                 args: Container[int] = (), kwargs: Container[str] = ()):
        self._args = args
        self._kwargs = kwargs
        super().__init__(func)

    def __call__(self, *args, **kwargs) -> Any:
        return self.__func__(*(arg for index, arg in enumerate(
            args) if index not in self._args), **{
            key: value for key, value in kwargs.items()
            if key not in self._kwargs})


class ReducedCallable(_Callable):
    _args: int = sys.maxsize
    _kwargs: Optional[tuple[str, ...]] = None

    def __init__(self, func: Callable):
        params = inspect.signature(func).parameters.values()
        if not any(param.kind == inspect.Parameter.VAR_POSITIONAL for param in params):
            self._args = sum(1 for param in params if param.kind in (
                inspect.Parameter.POSITIONAL_OR_KEYWORD, inspect.Parameter.POSITIONAL_ONLY))
        if not any(param.kind == inspect.Parameter.VAR_KEYWORD for param in params):
            self._kwargs = tuple(param.name for param in params if param.kind in (
                inspect.Parameter.POSITIONAL_OR_KEYWORD, inspect.Parameter.KEYWORD_ONLY))
        super().__init__(func)

    def __call__(self, *args, **kwargs):
        if (stop := self._args - len(args)) >= 0:
            args = itertools.islice(args, None, stop)
        if self._kwargs is not None:
            kwargs = {key: value for key, value in kwargs.items() if key in self._kwargs}
        return self.__func__(*args, **kwargs)


class QueueCallable(_Callable, _RunningQueryable):
    def __init__(self, func: Callable):
        self._lock = threading.Lock()
        super().__init__(func)

    def __call__(self, *args, **kwargs) -> Any:
        with self._lock:
            return self.__func__(*args, **kwargs)

    def is_running(self) -> bool:
        return self._lock.locked()


class QueueThreadCallable(_Callable, _RunningQueryable):
    _res = None

    def __init__(self, func: Callable):
        self._works = queue.Queue()
        threading.Thread(
            target=self._worker, name=_FMT_THREAD_NAME.format(
                type(self).__name__, func.__name__), daemon=True).start()
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


class WeakCacheCallable(_Callable):
    def __init__(self, func: Callable):
        self._cache = weakref.WeakValueDictionary()
        super().__init__(func)

    def __call__(self, *args, **kwargs) -> Any:
        params = _get_params(args, kwargs)
        try:
            res = self._cache[params]
        except KeyError:
            res = self._cache[params] = self.__func__(*args, **kwargs)
        return res


class LastCacheCallable(_Callable):
    _cache: Optional[tuple[Any, Any]] = None

    def __call__(self, *args, **kwargs) -> Any:
        params = _get_params(args, kwargs)
        if self._cache is None or self._cache[0] != params:
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


class TimedCacheCallable(_Callable):
    def __new__(cls, *args, **kwargs):
        if args:
            return super().__new__(cls)
        else:
            return functools.partial(cls, **kwargs)

    def __init__(self, func: Optional[Callable] = None, *,
                 secs: float = math.inf, size: Optional[int] = None):
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
            params_res_timeout = params, self.__func__(
                *args, **kwargs), current + self._timeout
            self._cache.append(params_res_timeout)
        return params_res_timeout[1]

    def reset(self) -> bool:
        try:
            return bool(self._cache)
        finally:
            self._cache.clear()


def _call_pre_post(func: Callable, args: Iterable, kwargs: Mapping[str, Any],
                   res, pipe_res: bool, unpack_res: bool) -> Any:
    if pipe_res:
        if unpack_res:
            if isinstance(res, Mapping):
                return func(**res)
            elif isinstance(res, Iterable):
                return func(*res)
        return func(res)
    return func(*args, **kwargs)


class PreCallable(_Callable):
    def __new__(cls, *args, **kwargs):
        if args:
            return super().__new__(cls)
        else:
            return functools.partial(cls, **kwargs)

    def __init__(self, func: Optional[Callable] = None, *,
                 pre_func: Callable = lambda *_, **__: None,
                 pipe_res: bool = False, unpack_res: bool = False):
        self._pre_func = pre_func
        self._pipe_res = pipe_res
        self._unpack_res = unpack_res
        super().__init__(func)

    def __call__(self, *args, **kwargs):
        return _call_pre_post(self.__func__, args, kwargs, self._pre_func(
            *args, **kwargs), self._pipe_res, self._unpack_res)


class PostCallable(_Callable):
    def __new__(cls, *args, **kwargs):
        if args:
            return super().__new__(cls)
        else:
            return functools.partial(cls, **kwargs)

    def __init__(self, func: Optional[Callable] = None, *,
                 post_func: Callable = lambda *_, **__: None,
                 pipe_res: bool = False, unpack_res: bool = False):
        self._post_func = post_func
        self._pipe_res = pipe_res
        self._unpack_res = unpack_res
        super().__init__(func)

    def __call__(self, *args, **kwargs):
        res = self.__func__(*args, **kwargs)
        _call_pre_post(self._post_func, args, kwargs, res,
                       self._pipe_res, self._unpack_res)
        return res
