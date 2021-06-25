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
_GENERATOR = (_ for _ in ()).__name__
_EXCEPTION = Exception.__name__.lower()
_PATHS = set()
_LEVEL = 0


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
        return callback != _GENERATOR and (event != _EXCEPTION or arg[0] not in (GeneratorExit, StopIteration))
    elif _LEVEL == Level.ERROR:
        return event == _EXCEPTION
    elif _LEVEL == Level.WARNING:
        return event == _EXCEPTION and issubclass(arg[0], Warning)
    elif _LEVEL == Level.NOTSET:
        return False


def _format(event: str,
            string: str) -> str:
    return f'{_PREFIX[event]}{string}{_SUFFIX}'


def _hook_callback(frame,
                   event: str,
                   arg: typing.Any) -> typing.Callable:
    frame.f_trace_lines = False
    if _filter(event, arg, frame.f_code.co_name) and frame.f_code.co_filename in _PATHS:
        log = _format(event, f'{datetime.datetime.now()}: [{os.path.relpath(frame.f_code.co_filename)} '
                             f'{frame.f_lineno}] {_get_prefix(frame)}{frame.f_code.co_name}')
        if event == 'call':
            for key, value in frame.f_locals.items():
                log += _format(f'{event}_details', f'{key}: {value}')
        elif event == 'exception' and arg[0] != StopIteration:
            log += _format(f'{event}_details', f'{arg[0].__name__}: {arg[1]}')
        elif event == 'return':
            log += _format(f'{event}_details', f'return: {arg}')
        logging.debug(log[:-1])
    return _hook_callback


class Level:
    ERROR = logging.ERROR
    WARNING = logging.WARNING
    INFO = logging.INFO
    DEBUG = logging.DEBUG
    NOTSET = logging.NOTSET


def init(*dirs_or_paths: str,
         base: str = os.path.dirname(__file__),
         level: int = Level.DEBUG) -> None:
    global _LEVEL
    for dir_ in (base,) + dirs_or_paths:
        dir_or_path = os.path.realpath(os.path.join(base, dir_))
        if os.path.isdir(dir_or_path):
            for name in os.listdir(dir_or_path):
                path = os.path.join(dir_or_path, name)
                if os.path.isfile(path):
                    _PATHS.add(path)
        elif os.path.isfile(dir_or_path):
            _PATHS.add(dir_or_path)
    _LEVEL = level
    logging.root.setLevel(logging.DEBUG)
    logging.root.addHandler(logging.StreamHandler())
    sys.settrace(_hook_callback)
    threading.settrace(_hook_callback)
