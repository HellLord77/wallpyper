__version__ = '0.0.2'

import enum

NUL = '\x00'
SOH = '\x01'
STX = '\x02'
ETX = '\x03'
EOT = '\x04'
ENQ = '\x05'
ACK = '\x06'
BEL = '\x07'
BS = '\x08'
TAB = '\x09'
HT = '\x09'
LF = '\x0A'
NL = '\x0A'
VT = '\x0B'
FF = '\x0C'
CR = '\x0D'
SO = '\x0E'
SI = '\x0F'
DLE = '\x10'
DC1 = '\x11'
DC2 = '\x12'
DC3 = '\x13'
DC4 = '\x14'
NAK = '\x15'
SYN = '\x16'
ETB = '\x17'
CAN = '\x18'
EM = '\x19'
SUB = '\x1A'
ESC = '\x1B'
FS = '\x1C'
GS = '\x1D'
RS = '\x1E'
US = '\x1F'
SP = '\x20'
DEL = '\x7F'


class Control(enum.IntEnum):
    BELL = 1
    CARRIAGE_RETURN = 2
    HOME = 3
    CLEAR = 4
    SHOW_CURSOR = 5
    HIDE_CURSOR = 6
    ENABLE_ALT_SCREEN = 7
    DISABLE_ALT_SCREEN = 8
    CURSOR_UP = 9
    CURSOR_DOWN = 10
    CURSOR_FORWARD = 11
    CURSOR_BACKWARD = 12
    CURSOR_MOVE_TO_COLUMN = 13
    CURSOR_MOVE_TO = 14
    ERASE_IN_LINE = 15
    SET_WINDOW_TITLE = 16


CONTROL_CODE = {
    Control.BELL: lambda: BEL,
    Control.CARRIAGE_RETURN: lambda: CR,
    Control.HOME: lambda: f'{ESC}[H',
    Control.CLEAR: lambda: f'{ESC}[2J',
    Control.SHOW_CURSOR: lambda: f'{ESC}[?25h',
    Control.HIDE_CURSOR: lambda: f'{ESC}[?25l',
    Control.ENABLE_ALT_SCREEN: lambda: f'{ESC}[?1049h',
    Control.DISABLE_ALT_SCREEN: lambda: f'{ESC}[?1049l',
    Control.CURSOR_UP: lambda param: f'{ESC}[{param}A',
    Control.CURSOR_DOWN: lambda param: f'{ESC}[{param}B',
    Control.CURSOR_FORWARD: lambda param: f'{ESC}[{param}C',
    Control.CURSOR_BACKWARD: lambda param: f'{ESC}[{param}D',
    Control.CURSOR_MOVE_TO_COLUMN: lambda param: f'{ESC}[{param + 1}G',
    Control.ERASE_IN_LINE: lambda param: f'{ESC}[{param}K',
    Control.CURSOR_MOVE_TO: lambda param1, param2: f'{ESC}[{param2 + 1};{param1 + 1}H',
    Control.SET_WINDOW_TITLE: lambda title: f'{ESC}]0;{title}{BEL}'}


def bell() -> str:
    return CONTROL_CODE[Control.BELL]()


def carriage_return() -> str:
    return CONTROL_CODE[Control.CARRIAGE_RETURN]()


def home() -> str:
    return CONTROL_CODE[Control.HOME]()


def clear() -> str:
    return CONTROL_CODE[Control.CLEAR]()


def show_cursor(show: bool = True) -> str:
    return CONTROL_CODE[Control.SHOW_CURSOR if show else Control.HIDE_CURSOR]()


def enable_alt_screen(enable: bool = True) -> str:
    return CONTROL_CODE[Control.ENABLE_ALT_SCREEN if enable else Control.DISABLE_ALT_SCREEN]()


def cursor_up(n: int = 1) -> str:
    return CONTROL_CODE[Control.CURSOR_UP](n)


def cursor_down(n: int = 1) -> str:
    return CONTROL_CODE[Control.CURSOR_DOWN](n)


def cursor_forward(n: int = 1) -> str:
    return CONTROL_CODE[Control.CURSOR_FORWARD](n)


def cursor_backward(n: int = 1) -> str:
    return CONTROL_CODE[Control.CURSOR_BACKWARD](n)


def cursor_move_to_column(n: int = 0) -> str:
    return CONTROL_CODE[Control.CURSOR_MOVE_TO_COLUMN](n)


def erase_in_line(n: int = 0) -> str:
    return CONTROL_CODE[Control.ERASE_IN_LINE](n)


def cursor_move_to(x: int = 0, y: int = 0) -> str:
    # noinspection PyArgumentList
    return CONTROL_CODE[Control.CURSOR_MOVE_TO](x, y)


def set_window_title(title: str) -> str:
    return CONTROL_CODE[Control.SET_WINDOW_TITLE](title)


def cursor_move(x: int = 0, y: int = 0) -> str:
    return (cursor_forward(x) if x > 0 else cursor_backward(
        -x)) + (cursor_down(y) if y > 0 else cursor_up(-y))


def color(text: str, red: int = 0, green: int = 0, blue: int = 0, bg: bool = False) -> str:
    return f'{ESC}[{38 if not bg else 48};2;{red};{green};{blue}m{text}{ESC}[0m'


class ProgressState(enum.IntEnum):
    NOPROGRESS = 0
    NORMAL = 1
    ERROR = 2
    INDETERMINATE = 3
    PAUSED = 4


def progress(state: int | ProgressState, value: int = 0) -> str:
    if isinstance(state, ProgressState):
        state = state.value
    return f'{ESC}]9;4;{state};{value}{BEL}'
