__version__ = '0.0.2'

import datetime
import inspect
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


class Level:
    ERROR = logging.ERROR
    WARNING = logging.WARNING
    INFO = logging.INFO
    DEBUG = logging.DEBUG
    NOTSET = logging.NOTSET


def _supports_ansi() -> bool:
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
        return f'{frame.f_locals["self"].__class__.__name__}.'
    elif 'cls' in frame.f_locals:
        return f'{frame.f_locals["cls"].__name__}.'
    else:
        return ''


def _hook_callback(frame,
                   event: str,
                   arg: typing.Any) -> typing.Callable:
    frame.f_trace_lines = False
    if _filter(event, arg, frame.f_code.co_name) and frame.f_code.co_filename in _PATHS:
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


def init(*dirs_or_paths: str,
         base: str = os.path.dirname(inspect.stack()[-1].filename),
         level: int = Level.DEBUG,
         redirect_wx: bool = False,
         skip_ansi_check: bool = False) -> None:  # TODO: debug frozen
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
    if not skip_ansi_check:
        _supports_ansi()
    logging.root.addHandler(logging.StreamHandler())
    sys.settrace(_hook_callback)
    threading.settrace(_hook_callback)
