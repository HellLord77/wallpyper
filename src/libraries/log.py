__version__ = '0.0.5'

import atexit
import datetime
import inspect
import io
import logging
import os
import shutil
import sys
import threading
import types
from typing import Any, Callable, Mapping, Optional

_PREFIXES = {
    'call': '\x1b[92m[>] ',
    'call_details': '\x1b[32m    ',
    'exception': '\x1b[91m[!] ',
    'exception_details': '\x1b[31m    ',
    'return': '\x1b[94m[<] ',
    'return_details': '\x1b[34m    '
}
_SUFFIX = '\x1b[0m\n'
_CALL = 'call'
_EXCEPTION = 'exception'
_RETURN = 'return'
_GENERATOR = (_ for _ in ()).__name__
_BASE = '' if hasattr(sys, 'frozen') else os.path.dirname(inspect.stack()[-1].filename)
_PATHS = set()
_LEVEL = 0
_STACK = 0
_STREAM = io.StringIO()
_WRITE: Optional[Callable] = None


class Level:
    ERROR = logging.ERROR
    WARNING = logging.WARNING
    INFO = logging.INFO
    DEBUG = logging.DEBUG
    NOTSET = logging.NOTSET


def _flush(path: str) -> None:
    if _STREAM.tell():
        _STREAM.seek(0)
        with open(path, 'w') as file:
            shutil.copyfileobj(_STREAM, file)


def redirect_stdio(path: str,
                   tee: Optional[bool] = None,
                   write_once: Optional[bool] = None) -> None:
    global _WRITE
    if write_once:
        atexit.register(_flush, path)
    elif os.path.exists(path):
        os.remove(path)

    def write(default: Callable[[str], int],  # TODO: use queue
              string: str):
        if string:
            if write_once:
                _STREAM.write(string)
            else:
                with open(path, 'a') as file:
                    file.write(string)
        if tee:
            default(string)

    _WRITE = write


def _is_compatible() -> bool:
    global _SUFFIX
    supports = hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
    if not supports:
        for event, prefix in _PREFIXES.items():
            _PREFIXES[event] = prefix[prefix.find('m') + 1:]
        _SUFFIX = _SUFFIX[_SUFFIX.find('m') + 1:]
    return supports


def _filter(event: str,
            arg: Any,
            func: str) -> bool:
    if _LEVEL == Level.DEBUG:
        return True
    elif _LEVEL == Level.INFO:
        return func != _GENERATOR and (event != _EXCEPTION or arg[0] not in (GeneratorExit, StopIteration))
    elif _LEVEL == Level.ERROR:
        return event == _EXCEPTION
    elif _LEVEL == Level.WARNING:
        return event == _EXCEPTION and issubclass(arg[0], Warning)
    elif _LEVEL == Level.NOTSET:
        return False


def _get_class_name(locals_: Mapping[str, Any]) -> str:
    if 'self' in locals_:
        return f'{type(locals_["self"]).__name__}.'
    elif 'cls' in locals_:
        return f'{locals_["cls"].__name__}.'
    else:
        return ''


def _get_stats(key: str,
               val: Any) -> str:
    return f'{key}: [{type(val).__name__} {sys.getsizeof(val)}] {val}'


def _hook_callback(frame,
                   event: str,
                   arg: Any) -> Callable:
    global _STACK
    frame.f_trace_lines = False
    try:
        path = os.path.relpath(frame.f_code.co_filename, _BASE)
    except ValueError:
        return _hook_callback
    if path in _PATHS and _filter(event, arg, frame.f_code.co_name):
        _STACK -= event == _RETURN
        pad = ' ' * _STACK * 4
        log = f'{pad}{_PREFIXES[event]}{datetime.datetime.now()}: ' \
              f'[{path} {frame.f_lineno}] {_get_class_name(frame.f_locals)}{frame.f_code.co_name}{_SUFFIX}'
        if event == _CALL:
            _STACK += 1
            for item in frame.f_locals.items():
                log += f'{pad}{_PREFIXES[f"{_CALL}_details"]}{_get_stats(*item)}{_SUFFIX}'
        elif event == _EXCEPTION:
            log += f'{pad}{_PREFIXES[f"{_EXCEPTION}_details"]}{arg[0].__name__}: {arg[1]}{_SUFFIX}'
        elif event == _RETURN:
            log += f'{pad}{_PREFIXES[f"{_RETURN}_details"]}{_get_stats("return", arg)}{_SUFFIX}'
        logging.debug(log[:-1])
    return _hook_callback


def init(*paths: str,
         level: int = Level.DEBUG,
         redirect_wx: bool = False,
         skip_comp: bool = False) -> None:
    global _LEVEL
    for path in paths:
        _PATHS.add(os.path.relpath(path, _BASE))
    _LEVEL = level
    if redirect_wx:
        import wx
        wx.GetApp().RedirectStdio()
    if not skip_comp:
        _is_compatible()
    if _WRITE:
        sys.stdout.write = types.MethodType(_WRITE, sys.stdout)
        if sys.stdout is not sys.stderr:
            sys.stderr.write = types.MethodType(_WRITE, sys.stderr)
    if 'pytransform' in sys.modules:
        # noinspection PyPackageRequirements,PyUnresolvedReferences
        import pytransform
        print(f'[!] Can not log {pytransform.get_license_code()}')
    else:
        logging.root.setLevel(logging.DEBUG)
        logging.root.addHandler(logging.StreamHandler())
        sys.settrace(_hook_callback)
        threading.settrace(_hook_callback)
