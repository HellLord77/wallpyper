__version__ = '0.0.3'

import atexit
import datetime
import inspect
import io
import logging
import os
import sys
import threading
import typing

_PREFIXES = {
    'call': '\x1b[92m[>] ',
    'call_details': '\x1b[32m    ',
    'exception': '\x1b[91m[!] ',
    'exception_details': '\x1b[31m    ',
    'return': '\x1b[94m[<] ',
    'return_details': '\x1b[34m    '
}
_SUFFIX = '\x1b[0m\n'
_GENERATOR = (_ for _ in ()).__name__
_EXCEPTION = Exception.__name__.lower()
_PATHS = set()
_LEVEL = 0
_STREAM = io.StringIO()
_WRITE = None


class Level:
    ERROR = logging.ERROR
    WARNING = logging.WARNING
    INFO = logging.INFO
    DEBUG = logging.DEBUG
    NOTSET = logging.NOTSET


def _flush(path: str) -> None:
    _STREAM.seek(0)
    string = _STREAM.read()
    if string:
        with open(path, 'w') as file:
            file.write(string)


def redirect_stdio(path: str,
                   tee: typing.Optional[bool] = None,
                   write_once: typing.Optional[bool] = None) -> None:
    global _WRITE
    path = os.path.realpath(path)
    if write_once:
        atexit.register(_flush, path)
    elif os.path.exists(path):
        os.remove(path)

    def write(string: str,  # TODO: use queue
              write_: typing.Callable[[str], int]):
        if string:
            if write_once:
                _STREAM.write(string)
            else:
                with open(path, 'a') as file:
                    file.write(string)
        if tee:
            write_(string)

    _WRITE = write


def _is_compatible() -> bool:
    global _SUFFIX
    supports = getattr(sys.stdout, 'isatty', lambda: False)()
    if not supports:
        for event, prefix in _PREFIXES.items():
            _PREFIXES[event] = prefix[prefix.find('m') + 1:]
        _SUFFIX = _SUFFIX[_SUFFIX.find('m') + 1:]
    return supports


def _filter(event: str,
            arg: typing.Any,
            callback: str) -> bool:
    if _LEVEL == Level.DEBUG:
        return True
    elif _LEVEL == Level.INFO:
        return callback != _GENERATOR and (event != _EXCEPTION or arg[0] not in (GeneratorExit, StopIteration))
    elif _LEVEL == Level.ERROR:
        return event == _EXCEPTION
    elif _LEVEL == Level.WARNING:
        return event == _EXCEPTION and issubclass(arg[0], Warning)
    elif _LEVEL == Level.NOTSET:
        return False


def _get_class_name(frame) -> str:
    if 'self' in frame.f_locals:
        return f'{type(frame.f_locals["self"]).__name__}.'
    elif 'cls' in frame.f_locals:
        return f'{frame.f_locals["cls"].__name__}.'
    return ''


def _hook_callback(frame,
                   event: str,
                   arg: typing.Any) -> typing.Callable:
    frame.f_trace_lines = False
    if __file__ != frame.f_code.co_filename and frame.f_code.co_filename in _PATHS and _filter(event, arg,
                                                                                               frame.f_code.co_name):
        log = f'{_PREFIXES[event]}{datetime.datetime.now()}: [{os.path.relpath(frame.f_code.co_filename)} ' \
              f'{frame.f_lineno}] {_get_class_name(frame)}{frame.f_code.co_name}{_SUFFIX}'
        if event == 'call':
            for key, value in frame.f_locals.items():
                log += f'{_PREFIXES[f"call_details"]}{key}: {value}{_SUFFIX}'
        elif event == _EXCEPTION:
            log += f'{_PREFIXES[f"exception_details"]}{arg[0].__name__}: {arg[1]}{_SUFFIX}'
        elif event == 'return':
            log += f'{_PREFIXES[f"return_details"]}return: {arg}{_SUFFIX}'
        logging.debug(log[:-1])
    return _hook_callback


# noinspection PyCallingNonCallable
def init(*dirs_or_paths: str,  # TODO: debug frozen
         base: str = os.path.dirname(inspect.stack()[-1].filename),
         level: int = Level.DEBUG,
         redirect_wx: bool = False,
         skip_comp: bool = False) -> None:
    global _LEVEL
    logging.root.setLevel(logging.DEBUG)
    for dir_ in dirs_or_paths:
        dir_or_path = os.path.realpath(os.path.join(base, dir_))
        if os.path.isdir(dir_or_path):
            for root, _, names in os.walk(dir_or_path):
                for name in names:
                    _PATHS.add(os.path.join(root, name))
        elif os.path.isfile(dir_or_path):
            _PATHS.add(dir_or_path)
    _LEVEL = level
    if redirect_wx:
        import wx
        wx.GetApp().RedirectStdio()
    if not skip_comp:
        _is_compatible()
    if _WRITE:
        sys.stdout.write = lambda string, write_=sys.stdout.write: _WRITE(string, write_)
        if sys.stdout is not sys.stderr:
            sys.stderr.write = lambda string, write_=sys.stderr.write: _WRITE(string, write_)
    logging.root.addHandler(logging.StreamHandler())
    sys.settrace(_hook_callback)
    threading.settrace(_hook_callback)
