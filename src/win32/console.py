import libs.ctyped as ctyped


def is_present() -> bool:
    return bool(ctyped.lib.kernel32.GetConsoleCP())


def create() -> bool:
    return bool(ctyped.lib.kernel32.AllocConsole())


def remove() -> bool:
    return bool(ctyped.lib.kernel32.FreeConsole())


def set_title(title: str) -> bool:
    return bool(ctyped.lib.kernel32.SetConsoleTitleW(title))


def ignore_ctrl_c(ignore: bool = True) -> bool:
    return bool(ctyped.lib.kernel32.SetConsoleCtrlHandler(ctyped.type.PHANDLER_ROUTINE(), ignore))


def disable_close() -> bool:
    return bool(ctyped.handle.HMENU.from_hwnd(ctyped.lib.kernel32.GetConsoleWindow(), True).delete_item(ctyped.const.SC_CLOSE))
