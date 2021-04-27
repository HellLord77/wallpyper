import ctypes
import os
import shlex
import winreg

_MAX_PATH = 0x104
_SPI_GETDESKWALLPAPER = 0x73
_SPI_SETDESKWALLPAPER = 0x14
_SPIF_SENDWININICHANGE = 0x2

AUTORUN_DIR = os.path.join('Software', 'Microsoft', 'Windows', 'CurrentVersion', 'Run')
APPDATA_DIR = os.environ['APPDATA']
PICTURES_DIR = os.path.join(os.environ['USERPROFILE'], 'Pictures')
TEMP_DIR = os.environ['TEMP']
WALLPAPER_DIR = os.path.join(APPDATA_DIR, 'Microsoft', 'Windows', 'Themes', 'CachedFiles')


def register_autorun(name: str,
                     path: str,
                     *args: str) -> bool:
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, AUTORUN_DIR, access=winreg.KEY_QUERY_VALUE | winreg.KEY_SET_VALUE)
    value = shlex.join((path,) + args)
    try:
        winreg.SetValueEx(key, name, None, winreg.REG_SZ, value)
    except PermissionError:
        return False
    return (value, winreg.REG_SZ) == winreg.QueryValueEx(key, name)


def unregister_autorun(name: str) -> bool:  # TODO: remove verify through exception
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, AUTORUN_DIR, access=winreg.KEY_SET_VALUE)
    for _ in range(2):
        try:
            winreg.DeleteValue(key, name)
        except FileNotFoundError:
            return True
    return False


def get_wallpaper_path() -> str:
    path = ctypes.create_unicode_buffer(_MAX_PATH)
    ctypes.windll.user32.SystemParametersInfoW(_SPI_GETDESKWALLPAPER, _MAX_PATH, ctypes.byref(path), None)
    return path.value


def set_wallpaper(*paths: str) -> bool:
    for path in paths:
        if os.path.isfile(path):
            ctypes.windll.user32.SystemParametersInfoW(_SPI_SETDESKWALLPAPER, None, path, _SPIF_SENDWININICHANGE)
            return True
    return False
