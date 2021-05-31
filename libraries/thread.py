import threading
import typing


class Timer:
    def __init__(self,
                 interval: float,
                 callback: typing.Callable,
                 callback_args: typing.Optional[tuple] = None,
                 callback_kwargs: typing.Optional[dict[str, typing.Any]] = None) -> None:
        def wrapper() -> None:
            if interval:
                self.start()
            self.running = True
            try:
                callback(*callback_args or (), **callback_kwargs or {})
            finally:
                self.running = False

        self.running = False
        self._timer = threading.Timer(interval, wrapper)

    @property
    def initialized(self) -> bool:
        return self._timer.is_alive()

    @property
    def waiting(self) -> bool:
        return self.initialized and not self.running

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
        return self.initialized


def start(callback: typing.Callable,
          callback_args: typing.Optional[tuple] = None,
          callback_kwargs: typing.Optional[dict[str, typing.Any]] = None) -> Timer:
    timer = Timer(0, callback, callback_args, callback_kwargs)
    timer.start()
    return timer
