import threading
import typing


class Timer:
    def __init__(self,
                 interval: float,
                 callback: typing.Callable,
                 callback_args: typing.Optional[tuple] = None,
                 callback_kwargs: typing.Optional[dict[str, typing.Any]] = None) -> None:
        def wrapped_callback():
            if interval:
                self.start()
            self.running = True
            callback(*callback_args or (), **callback_kwargs or {})
            self.running = False

        self.running = False
        self.__timer = threading.Timer(interval, wrapped_callback)

    @property
    def initialized(self) -> bool:
        return self.__timer.is_alive()

    @property
    def waiting(self) -> bool:
        return self.initialized and not self.running

    def start(self,
              interval: typing.Optional[float] = None) -> bool:
        self.stop()
        if interval is not None:
            self.__timer.interval = interval
        # noinspection PyUnresolvedReferences
        self.__timer = threading.Timer(self.__timer.interval, self.__timer.function)
        self.__timer.start()
        return self.initialized

    def stop(self) -> bool:
        self.__timer.cancel()
        return self.initialized


def start(callback: typing.Callable,
          callback_args: typing.Optional[tuple] = None,
          callback_kwargs: typing.Optional[dict[str, typing.Any]] = None) -> Timer:
    timer = Timer(0, callback, callback_args, callback_kwargs)
    timer.start()
    return timer
