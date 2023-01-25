import sys
from typing import Callable, Optional

from libs import ctyped
from libs.ctyped.lib import kernel32


def reopen_stream():
    sys.stdin = open('CONIN$')
    sys.stdout = open('CONOUT$', 'w')
    sys.stderr = open('CONOUT$', 'w')


def is_present() -> bool:
    return bool(kernel32.GetConsoleCP())


def create() -> bool:
    return bool(kernel32.AllocConsole())


def remove() -> bool:
    return bool(kernel32.FreeConsole())


def set_title(title: bytes | str) -> bool:
    return bool((kernel32.SetConsoleTitleA if isinstance(
        title, bytes) else kernel32.SetConsoleTitleW)(title))


def _get_handle(error: bool) -> int:
    return kernel32.GetStdHandle(ctyped.const.STD_ERROR_HANDLE if error else ctyped.const.STD_OUTPUT_HANDLE)


def write(text: bytes | str, error: bool = False) -> int:
    written = ctyped.type.DWORD()
    (kernel32.WriteConsoleA if isinstance(text, bytes) else kernel32.WriteConsoleW)(
        _get_handle(error), text, len(text), ctyped.byref(written), ctyped.const.NULL)
    return written.value


def _get_font_info_ex(error: bool = False) -> Optional[ctyped.struct.CONSOLE_FONT_INFOEX]:
    info = ctyped.struct.CONSOLE_FONT_INFOEX()
    if kernel32.GetCurrentConsoleFontEx(_get_handle(error), False, ctyped.byref(info)):
        return info


def ignore_ctrl_c(ignore: bool = True) -> bool:
    return bool(kernel32.SetConsoleCtrlHandler(ctyped.type.PHANDLER_ROUTINE(), ignore))


@ctyped.type.PHANDLER_ROUTINE
def _handler_routine(_: ctyped.type.DWORD) -> ctyped.type.BOOL:
    remove()
    return True


def ignore_ctrl() -> bool:
    return bool(kernel32.SetConsoleCtrlHandler(_handler_routine, True) and
                kernel32.GenerateConsoleCtrlEvent(ctyped.const.CTRL_C_EVENT, 0))


def set_ctrl_handler(handler: Optional[Callable[[int], bool]] = None):
    return bool(kernel32.SetConsoleCtrlHandler(*(
        ctyped.type.PHANDLER_ROUTINE(), False) if handler is None else (
        ctyped.type.PHANDLER_ROUTINE(handler), True)))
