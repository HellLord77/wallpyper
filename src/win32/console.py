from typing import Optional

from libs import ctyped


def is_present() -> bool:
    return bool(ctyped.lib.Kernel32.GetConsoleCP())


def create() -> bool:
    return bool(ctyped.lib.Kernel32.AllocConsole())


def remove() -> bool:
    return bool(ctyped.lib.Kernel32.FreeConsole())


def set_title(title: str) -> bool:
    return bool(ctyped.lib.Kernel32.SetConsoleTitleW(title))


def _get_handle(error: bool) -> int:
    return ctyped.lib.Kernel32.GetStdHandle(ctyped.const.STD_ERROR_HANDLE if error else ctyped.const.STD_OUTPUT_HANDLE)


def write(text: bytes | str, error: bool = False):
    written = ctyped.type.DWORD()
    (ctyped.lib.Kernel32.WriteConsoleA if isinstance(text, bytes) else ctyped.lib.Kernel32.WriteConsoleW)(
        _get_handle(error), text, len(text), ctyped.byref(written), 0)
    return written.value


def _get_font_info_ex(error: bool = False) -> Optional[ctyped.struct.CONSOLE_FONT_INFOEX]:
    info = ctyped.struct.CONSOLE_FONT_INFOEX()
    if ctyped.lib.Kernel32.GetCurrentConsoleFontEx(_get_handle(error), False, ctyped.byref(info)):
        return info


def ignore_ctrl_c(ignore: bool = True) -> bool:
    return bool(ctyped.lib.Kernel32.SetConsoleCtrlHandler(ctyped.type.PHANDLER_ROUTINE(), ignore))


def disable_close() -> bool:
    return bool(ctyped.handle.HMENU.from_hwnd(ctyped.lib.Kernel32.GetConsoleWindow(), True).delete_item(ctyped.const.SC_CLOSE))
