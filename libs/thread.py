import threading
import typing


class Timer:
    def __init__(self,
                 interval: float = 0,
                 callback: typing.Optional[typing.Callable] = None,
                 callback_args: typing.Optional[tuple] = None,
                 callback_kwargs: typing.Optional[dict[str, typing.Any]] = None) -> None:
        def wrapped_callback():
            if interval:
                self.start()
            self.running = True
            if callback:
                callback(*callback_args or (), **callback_kwargs or {})
            self.running = False

        self.running = False
        self.__timer = threading.Timer(interval, wrapped_callback)

    @property
    def interval(self) -> float:
        # noinspection PyUnresolvedReferences
        return self.__timer.interval

    @interval.setter
    def interval(self,
                 interval: float) -> None:
        self.__timer.interval = interval

    @property
    def initialized(self) -> bool:
        return self.__timer.is_alive()

    @property
    def waiting(self) -> bool:
        return self.initialized and not self.running

    def start(self):
        self.stop()
        # noinspection PyUnresolvedReferences
        self.__timer = threading.Timer(self.__timer.interval, self.__timer.function)
        self.__timer.start()

    def stop(self):
        self.__timer.cancel()


def start(callback: typing.Optional[typing.Callable] = None,
          callback_args: typing.Optional[tuple] = None,
          callback_kwargs: typing.Optional[dict[str, typing.Any]] = None) -> Timer:
    timer = Timer(0, callback, callback_args, callback_kwargs)
    timer.start()
    return timer
