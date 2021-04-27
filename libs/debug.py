import datetime
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


def _get_cls_name(frame):
    if 'self' in frame.f_locals:
        return f'{frame.f_locals["self"].__class__.__name__}.'
    elif 'cls' in frame.f_locals:
        return f'{frame.f_locals["cls"].__name__}.'
    else:
        return ''


def _hook_function(frame,
                   event: str,
                   arg: typing.Any) -> typing.Callable:
    if (event != 'exception' or arg[0] not in (GeneratorExit, StopIteration)) and frame.f_code.co_filename in _PATHS:
        log(event, f'{datetime.datetime.now()}: [{os.path.relpath(frame.f_code.co_filename)} '
                   f'{frame.f_lineno}] {_get_cls_name(frame)}{frame.f_code.co_name}')
        if event == 'call':
            for key, value in frame.f_locals.items():
                log(f'{event}_details', f'{key}: {value}')
        elif event == 'exception' and arg[0] != StopIteration:
            log(f'{event}_details', f'{arg[0].__name__}: {arg[1]}')
        elif event == 'return':
            log(f'{event}_details', f'return: {arg}')
    frame.f_trace_lines = False
    return _hook_function


def log(event: str,
        string: str) -> None:
    sys.stderr.write(f'{_PREFIX[event]}{string}{_SUFFIX}')


def init(*dirs: str,
         base: str = os.getcwd()) -> None:
    for dir_ in (base,) + dirs:
        dir__ = os.path.join(base, dir_)
        for name in os.listdir(dir__):
            if name.endswith('.py') and os.path.isfile(path__ := os.path.join(dir__, name)):
                _PATHS.add(path__)
    sys.settrace(_hook_function)
    threading.settrace(_hook_function)
