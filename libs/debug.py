import datetime
import os
import sys
import threading
import typing

_PREFIX = {
    '': '',
    'call': '\x1b[92m[>] ',
    'call_details': '\x1b[32m    ',
    'exception': '\x1b[91m[!] ',
    'exception_details': '\x1b[31m    ',
    'return': '\x1b[94m[<] ',
    'return_details': '\x1b[34m    '
}
_SUFFIX = '\x1b[0m\n'
_PATHS = set()


def _hook(frame,
          event: str,
          arg: typing.Any) -> typing.Callable:
    if (event != 'exception' or arg[0] != StopIteration) and frame.f_code.co_filename in _PATHS:
        log(event, f'{datetime.datetime.now().replace(microsecond=0)}: '
                   f'[{os.path.relpath(frame.f_code.co_filename)} {frame.f_lineno}] {frame.f_code.co_name}')
        if event == 'call':
            for key, value in frame.f_locals.items():
                log(f'{event}_details', f'{key}: {value}')
        elif event == 'exception' and arg[0] != StopIteration:
            log(f'{event}_details', f'{arg[0].__name__}: {arg[1]}')
        elif event == 'return':
            log(f'{event}_details', f'return: {arg}')
    frame.f_trace_lines = False
    return _hook


def log(event: str,
        string: str) -> None:
    sys.stderr.write(f'{_PREFIX[event]}{string}{_SUFFIX}')


def init(*paths: str,
         base: str = os.getcwd()) -> None:
    for path in (base,) + paths:
        path_ = os.path.join(base, path)
        for name in os.listdir(path_):
            if name.endswith('.py') and os.path.isfile(path__ := os.path.join(path_, name)):
                _PATHS.add(path__)
    sys.settrace(_hook)
    threading.settrace(_hook)
