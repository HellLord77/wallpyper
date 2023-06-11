__version__ = '0.0.13'

import atexit
import datetime
import functools
import io
import logging
import os
import platform
import pprint
import re
import shutil
import sys
import threading
from types import FrameType
from typing import Any, Callable, Iterable, Mapping, Optional

_CALL = 'call'
_EXCEPTION = 'exception'
_RETURN = 'return'
_PREFIXES = {_CALL: '\x1B[92m[>] ', _EXCEPTION: '\x1B[91m[!] ', _RETURN: '\x1B[94m[<] '}
_DETAILS = {_CALL: '\x1B[32m    ', _EXCEPTION: '\x1B[31m    ', _RETURN: '\x1B[34m    '}
_SUFFIX = '\x1B[0m\n'
_ANSI = re.compile(r'\x1B(?:[#-Z\\-_]|\[[0-?]*[ -/]*[#-~])')
_GENERATOR = (_ for _ in ()).__name__
_BASE = os.path.dirname(getattr(sys.modules['__main__'], '__file__', ''))
_INCLUDES = re.compile('.*')
_EXCLUDES = re.compile('')
_STACK = {}
_STREAM = io.StringIO()
_WRITE: Optional[Callable] = None
_DUMP = True


class Level:
    CURRENT = logging.root.level
    ERROR = logging.ERROR
    WARNING = logging.WARNING
    INFO = logging.INFO
    DEBUG = logging.DEBUG
    NOTSET = logging.NOTSET


def _flush(path: str):
    if _DUMP and _STREAM.tell():
        _STREAM.seek(0)
        with open(path, 'w') as file:
            shutil.copyfileobj(_STREAM, file)


def redirect_stdout(path: str, tee: bool = False, write_once: bool = False):
    global _WRITE
    if write_once:
        atexit.register(_flush, path)
    elif os.path.exists(path):
        os.remove(path)

    def write(write_: Callable[[str], int], s: str):
        if s:
            s_ = _ANSI.sub('', s)
            if write_once:
                _STREAM.write(s_)
            else:
                with open(path, 'a') as file:
                    file.write(s_)
        if tee:
            write_(s)

    _WRITE = write


def _excepthook(excepthook: Callable, *args, **kwargs):
    global _DUMP
    _DUMP = True
    excepthook(*args, **kwargs)


def write_on_exception(path: str):
    global _DUMP
    _DUMP = False
    sys.excepthook = functools.partial(_excepthook, sys.excepthook)
    threading.excepthook = functools.partial(_excepthook, threading.excepthook)
    redirect_stdout(path, True, True)


def _fix_compatibility():
    global _SUFFIX
    if not getattr(sys.stderr, 'isatty', lambda: False)():
        for dict_ in (_PREFIXES, _DETAILS):
            for event, prefix in dict_.items():
                dict_[event] = _ANSI.sub('', prefix)
        _SUFFIX = _ANSI.sub('', _SUFFIX)


def _filter(event: str, arg, name: str) -> bool:
    if Level.CURRENT == Level.DEBUG:
        return True
    elif Level.CURRENT == Level.INFO:
        return name != _GENERATOR and (event != _EXCEPTION or arg[0] not in (GeneratorExit, StopIteration))
    elif Level.CURRENT == Level.ERROR:
        return event == _EXCEPTION
    elif Level.CURRENT == Level.WARNING:
        return event == _EXCEPTION and issubclass(arg[0], Warning)
    elif Level.CURRENT == Level.NOTSET:
        return False


def _get_class_name(locals_: Mapping[str, Any]) -> str:
    if 'self' in locals_:
        return f'{type(locals_["self"]).__name__}.'
    elif 'cls' in locals_:
        return f'{locals_["cls"].__name__}.'
    else:
        return ''


def _format_dict(dict_: Mapping[str, Any], prefix: str = '', suffix: str = '\n') -> str:
    types_ = tuple(type(val).__name__ for val in dict_.values())
    sizes = tuple(str(sys.getsizeof(val)) for val in dict_.values())
    pads = tuple(len(max(it, key=len)) for it in (dict_, types_, sizes))
    end = f'\n{" " * (len(_ANSI.sub("", prefix)) + sum(pads) + 6)}'
    formatted = ''
    for item, type_, size in zip(dict_.items(), types_, sizes):
        try:
            formatted += (f'{prefix}{f"{item[0]}: ":{pads[0] + 2}}[{type_:{pads[1]}} {size:>{pads[2]}}] '
                          f'{pprint.pformat(item[1], sort_dicts=False).replace(end[0], end)}{suffix}')
        except (AssertionError, AttributeError):
            pass
    return formatted


def _on_trace(frame: FrameType, event: str, arg) -> Optional[Callable]:
    if frame.f_code is logging.shutdown.__code__:
        _on_trace.__code__ = (lambda *args, **kwargs: None).__code__
    else:
        frame.f_trace_lines = False
        path = frame.f_code.co_filename
        try:
            path = os.path.relpath(path, _BASE)
        except ValueError:
            pass
        if (_INCLUDES.fullmatch(path) and not _EXCLUDES.fullmatch(path) and __name__ is not
                frame.f_globals['__name__'] and _filter(event, arg, frame.f_code.co_name)):
            thread = threading.current_thread()
            if thread not in _STACK:
                _STACK[thread] = 0
            _STACK[thread] -= event == _RETURN
            pad = ' ' * _STACK[thread] * 4
            log = (f'{pad}{_PREFIXES[event]}{datetime.datetime.now()}: [{path} {frame.f_lineno}] '
                   f'{_get_class_name(frame.f_locals)}{frame.f_code.co_name}'
                   f'{"" if thread is threading.main_thread() else f" ({thread.name})"}{_SUFFIX}')
            if event == _CALL:
                _STACK[thread] += 1
                if frame.f_locals:
                    log += _format_dict(frame.f_locals, f'{pad}{_DETAILS[event]}', _SUFFIX)
            elif event == _EXCEPTION:
                log += f'{pad}{_DETAILS[event]}{arg[0].__name__}: {arg[1]}{_SUFFIX}'
            elif event == _RETURN:
                log += _format_dict({_RETURN: arg}, f'{pad}{_DETAILS[event]}', _SUFFIX)
            logging.error(log.strip())
    return _on_trace


def _dump_info():
    uname = platform.uname()
    logging.warning('\n[#] '.join((f'[#] {platform.python_implementation()}: {sys.version}', f'System: {uname.system}',
                                   f'Node: {uname.node}', f'Release: {uname.release}', f'Version: {uname.version}',
                                   f'Machine: {uname.machine}', f'Processor: {uname.processor}\n')))


def init(includes: Optional[Iterable[str]] = None, excludes: Optional[Iterable[str]] = None,
         level: int = Level.DEBUG, redirect_wx: bool = False, check_comp: bool = True):
    global _INCLUDES, _EXCLUDES
    if includes is not None:
        _INCLUDES = re.compile(f'({"|".join(includes)})')
    if excludes is not None:
        _EXCLUDES = re.compile(f'({"|".join(excludes)})')
    Level.CURRENT = level
    if redirect_wx:
        __import__('wx').GetApp().RedirectStdio()
    if check_comp:
        _fix_compatibility()
    if _WRITE:
        sys.stdout.write = functools.partial(_WRITE, sys.stdout.write)
        if sys.stdout is not sys.stderr:
            sys.stderr.write = functools.partial(_WRITE, sys.stderr.write)
    logging.root.addHandler(logging.StreamHandler())
    if 'pytransform' in sys.modules:
        raise RuntimeError(f'Cannot log {sys.modules["pytransform"].get_license_code()}')
    else:
        sys.settrace(_on_trace)
        threading.settrace(_on_trace)
    _dump_info()
