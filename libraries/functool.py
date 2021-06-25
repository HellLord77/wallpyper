import functools
import typing


class WrappedCallback:
    def __init__(self,
                 callback: typing.Optional[typing.Callable] = None,
                 args: typing.Optional[tuple] = None,
                 kwargs: typing.Optional[dict[str, typing.Any]] = None):
        self.callback = callback or (lambda *_, **__: None)
        self.args = args or ()
        self.kwargs = kwargs or {}

    def __call__(self):
        return self.callback(*self.args, *self.kwargs)


def one_cache(callback: typing.Callable) -> typing.Callable:
    @functools.wraps(callback)
    def wrapper(*args, **kwargs):
        if wrapper.cache[0] != args or wrapper.cache[1] != kwargs or len(wrapper.cache) == 2:
            wrapper.cache[:] = args, kwargs, callback(*args, **kwargs)
        return wrapper.cache[2]

    wrapper.cache = [(), {}]
    return wrapper


def one_run(callback: typing.Callable) -> typing.Callable:
    @functools.wraps(callback)
    def wrapper(*args, **kwargs):
        if not wrapper.ran:
            wrapper.ran = True
            return callback(*args, **kwargs)

    wrapper.ran = False
    return wrapper


def singleton(callback: typing.Callable) -> typing.Callable:
    @functools.wraps(callback)
    def wrapper(*args, **kwargs):
        if wrapper.running:
            return False
        else:
            wrapper.running = True
            try:
                return callback(*args, **kwargs)
            finally:
                wrapper.running = False

    wrapper.running = False
    return wrapper
