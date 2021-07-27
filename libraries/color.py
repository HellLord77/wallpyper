__version__ = '0.0.2'

import sys

_ESC = '\x1b'
_CSI = f'{_ESC}['
_CODES = set()
_SUPPORTED = getattr(sys.stdout, 'isatty', lambda: False)()


class _Code:
    def __init_subclass__(cls):
        for name in dir(cls):
            if not name.startswith('_'):
                setattr(cls, name, f'{_CSI}{getattr(cls, name)}m' if _SUPPORTED else '')
                _CODES.add(getattr(cls, name))


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


def cprint(*strings) -> None:
    index = 0
    for string in strings:
        print(string, end='')
        if string not in _CODES:
            break
        index += 1
    for string in strings[index + 1:]:
        print(f'{" " * (string not in _CODES)}{string}', end='')
    print(FontStyle.RESET)
