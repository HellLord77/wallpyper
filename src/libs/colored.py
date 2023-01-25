__version__ = '0.0.2'

import builtins
import io
import sys
from typing import Optional

_ESC = '\x1B'
_CSI = f'{_ESC}['
_CODES = set()
_SUPPORTED = sys.stdout.isatty() if hasattr(sys.stdout, 'isatty') else False


class _Code:
    def __init_subclass__(cls):
        for var, n in vars(cls).items():
            if not var.startswith('_'):
                code = f'{_CSI}{n}m' if _SUPPORTED else ''
                setattr(cls, var, code)
                _CODES.add(code)


class FontStyle(_Code):
    RESET = 0
    BOLD = 1
    FAINT = 2
    ITALIC = 3
    UNDERLINE = 4


class ForeColor(_Code):
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37
    BRIGHT_BLACK = 90
    BRIGHT_RED = 91
    BRIGHT_GREEN = 92
    BRIGHT_YELLOW = 93
    BRIGHT_BLUE = 94
    BRIGHT_MAGENTA = 95
    BRIGHT_CYAN = 96
    BRIGHT_WHITE = 97


class BackColor(_Code):
    BLACK = 40
    RED = 41
    GREEN = 42
    YELLOW = 43
    BLUE = 44
    MAGENTA = 45
    CYAN = 46
    WHITE = 47
    BRIGHT_BLACK = 100
    BRIGHT_RED = 101
    BRIGHT_GREEN = 102
    BRIGHT_YELLOW = 103
    BRIGHT_BLUE = 104
    BRIGHT_MAGENTA = 105
    BRIGHT_CYAN = 106
    BRIGHT_WHITE = 107


# noinspection PyShadowingBuiltins
def print(*strings, reset: bool = True, file: Optional[io.TextIOWrapper] = None, flush: bool = True):
    index = 0
    for string in strings:
        builtins.print(string, end='')
        if string not in _CODES:
            break
        index += 1
    for string in strings[index + 1:]:
        builtins.print(f'{" " * (string not in _CODES)}{string}', end='', file=file, flush=flush)
    if reset:
        builtins.print(FontStyle.RESET, file=file, flush=flush)
