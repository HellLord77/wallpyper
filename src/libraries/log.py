__version__ = '0.0.7'

import _io
import atexit
import datetime
import inspect
import io
import logging
import os
import pprint
import re
import shutil
import sys
import threading
import types
from typing import Any, Callable, Mapping, Optional

_PREFIXES = {
    'call': '\x1b[92m[>] ',
    'exception': '\x1b[91m[!] ',
    'return': '\x1b[94m[<] '
}
_DETAILS = {
    'call': '\x1b[32m    ',
    'exception': '\x1b[31m    ',
    'return': '\x1b[34m    '
}
_SUFFIX = '\x1b[0m\n'
_ANSI = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
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
_WRITE_ = {}


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

    def write(stream: _io.TextIOWrapper,  # TODO: use queue
              string: str):
        if string:
            if write_once:
                _STREAM.write(string)
            else:
                with open(path, 'a') as file:
                    file.write(string)
        if tee:
            _WRITE_[stream](string)

    _WRITE = write


def _is_compatible() -> bool:
    global _SUFFIX
    supports = hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
    if not supports:
        for dict_ in (_PREFIXES, _DETAILS):
            for event, prefix in dict_.items():
                dict_[event] = _ANSI.sub('', prefix)
        _SUFFIX = _ANSI.sub('', _SUFFIX)
    return supports


def _format_dict(dict_: Mapping[str, Any],
                 prefix: str = '',
                 suffix: str = '\n') -> str:
    types_ = tuple(type(val).__name__ for val in dict_.values())
    sizes = tuple(str(sys.getsizeof(val)) for val in dict_.values())
    pads = tuple(len(max(itt, key=len)) for itt in (dict_, types_, sizes))
    end = f'\n{" " * (len(_ANSI.sub("", prefix)) + sum(pads) + 6)}'
    formatted = ''
    for item, type_, size in zip(dict_.items(), types_, sizes):
        formatted += f'{prefix}{f"{item[0]}: ":{pads[0] + 2}}[{type_:{pads[1]}} {size:>{pads[2]}}] ' \
                     f'{pprint.pformat(item[1], sort_dicts=False).replace(end[0], end)}{suffix}'
    return formatted


def _get_thread_name() -> str:
    thread = threading.current_thread()
    return '' if thread == threading.main_thread() else f' ({thread.name})'


def _get_class_name(locals_: Mapping[str, Any]) -> str:
    if 'self' in locals_:
        return f'{type(locals_["self"]).__name__}.'
    elif 'cls' in locals_:
        return f'{locals_["cls"].__name__}.'
    else:
        return ''


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


def _hook_callback(frame: types.FrameType,
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
        log = f'{pad}{_PREFIXES[event]}{datetime.datetime.now()}: [{path} {frame.f_lineno}] ' \
              f'{_get_class_name(frame.f_locals)}{frame.f_code.co_name}{_get_thread_name()}{_SUFFIX}'
        if event == _CALL:
            _STACK += 1
            if frame.f_locals:
                log += _format_dict(frame.f_locals, f'{pad}{_DETAILS[event]}', _SUFFIX)
        elif event == _EXCEPTION:
            log += f'{pad}{_DETAILS[event]}{arg[0].__name__}: {arg[1]}{_SUFFIX}'
        elif event == _RETURN:
            log += _format_dict({'return': arg}, f'{pad}{_DETAILS[event]}', _SUFFIX)
        logging.error(log[:-1])
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
        __import__('wx').GetApp().RedirectStdio()
    if _WRITE:
        sys.stdout.isatty = types.MethodType(lambda _: False, sys.stdout)
        _WRITE_[sys.stdout] = sys.stdout.write
        sys.stdout.write = types.MethodType(_WRITE, sys.stdout)
        if sys.stdout is not sys.stderr:
            _WRITE_[sys.stderr] = sys.stderr.write
            sys.stderr.write = types.MethodType(_WRITE, sys.stderr)
    if _WRITE or not skip_comp:
        _is_compatible()
    logging.root.addHandler(logging.StreamHandler())
    if 'pytransform' in sys.modules:
        # noinspection PyUnresolvedReferences
        logging.error(
            f'{_PREFIXES[_EXCEPTION]}Can not log {sys.modules["pytransform"].get_license_code()}{_SUFFIX}'[:-1])
    else:
        sys.settrace(_hook_callback)
        threading.settrace(_hook_callback)
