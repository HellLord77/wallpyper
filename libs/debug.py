import os
import sys
import typing

_PREFIX = {
    'call': f'\x1b[92m[>] ',
    'exception': f'\x1b[91m[!] ',
    'return': f'\x1b[94m[<] '
}
_TAB = '    '
_PATHS = set()

RESET = '\x1b[0m'
COLORS = {
    'red': '\x1b[31m',
    'green': '\x1b[32m',
    'blue': '\x1b[34m'
}


def _hook(frame,
          event: str,
          arg: typing.Any) -> typing.Callable:
    if (event != 'exception' or arg[0] != StopIteration) and frame.f_code.co_filename in _PATHS:
        log(_PREFIX[event], f'{frame.f_code.co_name}: {os.path.relpath(frame.f_code.co_filename)}')
        if event == 'call':
            for key, value in frame.f_locals.items():
                log(COLORS['green'], f'{_TAB}{key}: {value}')
        elif event == 'exception' and arg[0] != StopIteration:
            log(COLORS['red'], f'{_TAB}{arg[0].__name__}: {arg[1]}')
        elif event == 'return':
            log(COLORS['blue'], f'{_TAB}return: {arg}')
        log()
    frame.f_trace_lines = False
    return _hook


# TODO: combine color and string
def log(color: str = RESET,
        *strings: str) -> None:
    print(f'{color}{" ".join(strings)}{RESET}')


def init(*paths: str,
         base: str = os.getcwd()) -> None:
    for path in (base,) + paths:
        path_ = os.path.join(base, path)
        for name in os.listdir(path_):
            if name.endswith('.py') and os.path.isfile(path__ := os.path.join(path_, name)):
                _PATHS.add(path__)
    sys.settrace(_hook)
