import datetime
import logging
import os
import sys
import threading
import typing

_PREFIX = {
    'call': '\x1b[92m[>] ',
    'call_details': '\x1b[32m    ',
    'exception': '\x1b[91m[!] ',
    'exception_details': '\x1b[31m    ',
    'return': '\x1b[94m[<] ',
    'return_details': '\x1b[34m    '
}
_SUFFIX = '\x1b[0m\n'
_PATHS = set()
_LEVEL = 0

####################################
logging.root.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
logging.root.addHandler(handler)


def _get_prefix(frame) -> str:
    if 'self' in frame.f_locals:
        return f'{frame.f_locals["self"].__class__.__name__}.'
    elif 'cls' in frame.f_locals:
        return f'{frame.f_locals["cls"].__name__}.'
    else:
        return ''


def _filter(event: str,
            arg: typing.Any,
            callback: str) -> bool:
    if _LEVEL == Level.DEBUG:
        return True
    elif _LEVEL == Level.INFO:
        return callback != '<genexpr>' and (event != 'exception' or arg[0] not in (GeneratorExit, StopIteration))
    elif _LEVEL == Level.ERROR:
        return event == 'exception'
    elif _LEVEL == Level.WARNING:
        return event == 'exception' and issubclass(arg[0], Warning)
    elif _LEVEL == Level.NOTSET:
        return False


def _hook_callback(frame,
                   event: str,
                   arg: typing.Any) -> typing.Callable:
    frame.f_trace_lines = False
    if _filter(event, arg, frame.f_code.co_name) and frame.f_code.co_filename in _PATHS:
        log = f'{_PREFIX[event]}{datetime.datetime.now()}: [{os.path.relpath(frame.f_code.co_filename)} ' \
              f'{frame.f_lineno}] {_get_prefix(frame)}{frame.f_code.co_name}{_SUFFIX}'
        if event == 'call':
            for key, value in frame.f_locals.items():
                log = f'{log}{_PREFIX[f"{event}_details"]}{key}: {value}{_SUFFIX}'
        elif event == 'exception' and arg[0] != StopIteration:
            log = f'{log}{_PREFIX[f"{event}_details"]}{arg[0].__name__}: {arg[1]}{_SUFFIX}'
        elif event == 'return':
            log = f'{log}{_PREFIX[f"{event}_details"]}return: {arg}{_SUFFIX}'
        logging.debug(log[:-1])
    return _hook_callback


class Level:
    ERROR = logging.ERROR
    WARNING = logging.WARNING
    INFO = logging.INFO
    DEBUG = logging.DEBUG
    NOTSET = logging.NOTSET


def init(*dirs_or_paths: str,
         base: str = os.path.dirname(sys.argv[0]),
         level: int = Level.DEBUG) -> None:
    global _LEVEL
    for dir_ in (base,) + dirs_or_paths:
        dir__ = os.path.realpath(os.path.join(base, dir_))
        if os.path.isdir(dir__):
            for name in os.listdir(dir__):
                path = os.path.join(dir__, name)
                if name.endswith('.py') and os.path.isfile(path):
                    _PATHS.add(path)
        elif os.path.isfile(dir__):
            _PATHS.add(dir__)
    _LEVEL = level
    sys.settrace(_hook_callback)
    threading.settrace(_hook_callback)
