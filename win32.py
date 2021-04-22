import ctypes
import os
import winreg

MAX_PATH = 0x104
SPI_GETDESKWALLPAPER = 0x73
SPI_SETDESKWALLPAPER = 0x14
SPIF_SENDWININICHANGE = 0x2


def join_path(*paths: str) -> str:
    return '\\'.join(paths)


AUTORUN_DIR = join_path('Software', 'Microsoft', 'Windows', 'CurrentVersion', 'Run')
APPDATA_DIR = os.environ['APPDATA']
PICTURES_DIR = join_path(os.environ['USERPROFILE'], 'Pictures')
TEMP_DIR = os.environ['TEMP']
WALLPAPER_DIR = join_path(APPDATA_DIR, 'Microsoft', 'Windows', 'Themes', 'CachedFiles')


def register_autorun(name: str, path: str, *args: str) -> bool:
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, AUTORUN_DIR, access=winreg.KEY_QUERY_VALUE | winreg.KEY_SET_VALUE)
    value = f'"{path}"' + ' '.join(arg for arg in args if arg)
    try:
        winreg.SetValueEx(key, name, None, winreg.REG_SZ, value)
    except PermissionError:
        return False
    return (value, winreg.REG_SZ) == winreg.QueryValueEx(key, name)


def unregister_autorun(name: str) -> bool:
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, AUTORUN_DIR, access=winreg.KEY_SET_VALUE)
    for _ in range(2):
        try:
            winreg.DeleteValue(key, name)
        except FileNotFoundError:
            return True
    return False


def get_wallpaper_path() -> str:
    path = ctypes.create_unicode_buffer(MAX_PATH)
    ctypes.windll.user32.SystemParametersInfoW(SPI_GETDESKWALLPAPER, MAX_PATH, ctypes.byref(path), None)
    return path.value


def set_wallpaper(*paths: str) -> bool:
    for path in paths:
        if os.path.isfile(path):
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, None, path, SPIF_SENDWININICHANGE)
            return True
    return False
