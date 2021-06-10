import functools
import threading
import typing


class RepeatableTimer:
    def __init__(self,
                 interval: float,
                 callback: typing.Callable,
                 callback_args: typing.Optional[tuple] = None,
                 callback_kwargs: typing.Optional[dict[str, typing.Any]] = None,
                 repeat: bool = True) -> None:
        @functools.wraps(callback)
        def wrapper() -> None:
            if repeat:
                self.start()
            self._running = True
            try:
                callback(*callback_args or (), **callback_kwargs or {})
            finally:
                self._running = False

        self._running = False
        self._timer = threading.Timer(interval, wrapper)

    @property
    def initialized(self) -> bool:
        return self._timer.is_alive()

    @property
    def running(self):
        return self._running

    def is_waiting(self) -> bool:
        return self.initialized and not self._running

    def start(self,
              interval: typing.Optional[float] = None) -> bool:
        self.stop()
        if interval is not None:
            self._timer.interval = interval
        # noinspection PyUnresolvedReferences
        self._timer = threading.Timer(self._timer.interval, self._timer.function)
        self._timer.start()
        return self.initialized

    def stop(self) -> bool:
        self._timer.cancel()
        return self._running


def start_once(interval: float,
               callback: typing.Callable,
               callback_args: typing.Optional[tuple] = None,
               callback_kwargs: typing.Optional[dict[str, typing.Any]] = None) -> RepeatableTimer:
    timer = RepeatableTimer(interval, callback, callback_args, callback_kwargs, False)
    timer.start()
    return timer


def start_now(callback: typing.Callable,
              callback_args: typing.Optional[tuple] = None,
              callback_kwargs: typing.Optional[dict[str, typing.Any]] = None) -> RepeatableTimer:
    return start_once(0, callback, callback_args, callback_kwargs)


def on_thread(callback):
    @functools.wraps(callback)
    def wrapper(*args, **kwargs) -> None:
        start_now(callback, args, kwargs)

    return wrapper
