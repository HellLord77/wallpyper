__version__ = '0.0.4'

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
_BASE = '' if hasattr(sys, 'frozen') else os.path.dirname(inspect.stack()[-1].filename)
_PATHS = set()
_LEVEL = 0
_STREAM = io.StringIO()
_WRITE: typing.Optional[typing.Callable] = None


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
                   tee: typing.Optional[bool] = None,
                   write_once: typing.Optional[bool] = None) -> None:
    global _WRITE
    if write_once:
        atexit.register(_flush, path)
    elif os.path.exists(path):
        os.remove(path)

    def write(default: typing.Callable[[str], int],  # TODO: use queue
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
    else:
        return ''


def _hook_callback(frame,
                   event: str,
                   arg: typing.Any) -> typing.Callable:
    frame.f_trace_lines = False
    try:
        rel_path = os.path.relpath(frame.f_code.co_filename, _BASE)
    except ValueError:
        return _hook_callback
    if rel_path in _PATHS and _filter(event, arg, frame.f_code.co_name):
        log = f'{_PREFIXES[event]}{datetime.datetime.now()}: [{rel_path} ' \
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
