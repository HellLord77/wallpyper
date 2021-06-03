import typing

_ESC = '\x1b'
_CSI = f'{_ESC}['
_CODES = set()


class _Constant(type):
    def __new__(mcs, *args, **kwargs):
        instance = super(_Constant, mcs).__new__(mcs, *args, **kwargs)
        for var, value in instance.__dict__.items():
            if not var.startswith('__') and not var.endswith('__'):
                value_ = f'{_CSI}{value}m'
                setattr(instance, var, value_)
                _CODES.add(value_)
        return instance


class FontStyle(metaclass=_Constant):
    RESET = 0
    BOLD = 1
    FAINT = 2
    ITALIC = 3
    UNDERLINE = 4


class ForeColor(metaclass=_Constant):
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


class BackColor(metaclass=_Constant):
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


def cprint(*strings: typing.Any) -> None:
    index = 0
    for string in strings:
        print(string, end='')
        if string not in _CODES:
            break
        index += 1
    for string in strings[index + 1:]:
        print(f'{" " * (string not in _CODES)}{string}', end='')
    print(FontStyle.RESET)
