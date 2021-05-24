import ctypes
import os
import shlex
import winreg

_MAX_PATH = 160
_SPI_GETDESKWALLPAPER = 115
_SPI_SETDESKWALLPAPER = 20
_SPIF_SENDWININICHANGE = 2
_CSIDL_APPDATA = 26
_CSIDL_LOCAL_APPDATA = 28
_CSIDL_MYPICTURES = 39
_SHGFP_TYPE_CURRENT = 0
_RUN_KEY = os.path.join('SOFTWARE', 'Microsoft', 'Windows', 'CurrentVersion', 'Run')


def _get_dir(csidl: int) -> str:
    dir_ = ctypes.create_unicode_buffer(_MAX_PATH)
    ctypes.windll.shell32.SHGetFolderPathW(None, csidl, None, _SHGFP_TYPE_CURRENT, ctypes.byref(dir_))
    return dir_.value


APPDATA_DIR = _get_dir(_CSIDL_APPDATA)
PICTURES_DIR = _get_dir(_CSIDL_MYPICTURES)
TEMP_DIR = os.path.join(_get_dir(_CSIDL_LOCAL_APPDATA), 'Temp')
WALLPAPER_DIR = os.path.join(APPDATA_DIR, 'Microsoft', 'Windows', 'Themes', 'CachedFiles')


def register_autorun(name: str,
                     path: str,
                     *args: str) -> bool:
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, _RUN_KEY,
                        access=winreg.KEY_QUERY_VALUE | winreg.KEY_SET_VALUE) as key:
        value = shlex.join((path,) + args)
        try:
            winreg.SetValueEx(key, name, None, winreg.REG_SZ, value)
        except PermissionError:
            return False
        return (value, winreg.REG_SZ) == winreg.QueryValueEx(key, name)


def unregister_autorun(name: str) -> bool:
    if register_autorun(name, ''):
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, _RUN_KEY, access=winreg.KEY_SET_VALUE) as key:
            winreg.DeleteValue(key, name)
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
