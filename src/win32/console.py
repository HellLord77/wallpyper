from typing import Optional

from libs import ctyped
from libs.ctyped.lib import kernel32


def is_present() -> bool:
    return bool(kernel32.GetConsoleCP())


def create() -> bool:
    return bool(kernel32.AllocConsole())


def remove() -> bool:
    return bool(kernel32.FreeConsole())


def set_title(title: str) -> bool:
    return bool(kernel32.SetConsoleTitleW(title))


def _get_handle(error: bool) -> int:
    return kernel32.GetStdHandle(ctyped.const.STD_ERROR_HANDLE if error else ctyped.const.STD_OUTPUT_HANDLE)


def write(text: bytes | str, error: bool = False):
    written = ctyped.type.DWORD()
    (kernel32.WriteConsoleA if isinstance(text, bytes) else kernel32.WriteConsoleW)(
        _get_handle(error), text, len(text), ctyped.byref(written), 0)
    return written.value


def _get_font_info_ex(error: bool = False) -> Optional[ctyped.struct.CONSOLE_FONT_INFOEX]:
    info = ctyped.struct.CONSOLE_FONT_INFOEX()
    if kernel32.GetCurrentConsoleFontEx(_get_handle(error), False, ctyped.byref(info)):
        return info


def ignore_ctrl_c(ignore: bool = True) -> bool:
    return bool(kernel32.SetConsoleCtrlHandler(ctyped.type.PHANDLER_ROUTINE(), ignore))


def disable_close() -> bool:
    return bool(ctyped.handle.HMENU.from_hwnd(kernel32.GetConsoleWindow(), True).delete_item(ctyped.const.SC_CLOSE))
