import ctypes
import os
import winreg

MAX_PATH = 0x104
SPI_GETDESKWALLPAPER = 0x73
SPI_SETDESKWALLPAPER = 0x14
SPIF_SENDWININICHANGE = 0x2

AUTORUN_DIR = os.path.join('Software', 'Microsoft', 'Windows', 'CurrentVersion', 'Run')
APPDATA_DIR = os.environ['APPDATA']
TEMP_DIR = os.environ['TEMP']
WALLPAPER_DIR = os.path.join(APPDATA_DIR, 'Microsoft', 'Windows', 'Themes', 'CachedFiles')


def _autorun_key_handle():
    return winreg.OpenKey(winreg.HKEY_CURRENT_USER, AUTORUN_DIR, 0, winreg.KEY_SET_VALUE)


def register_autorun(name, path, *args):
    handle = _autorun_key_handle()
    value = f'"{path}"' + ' '.join(arg for arg in args if arg)
    try:
        winreg.SetValueEx(handle, name, 0, winreg.REG_SZ, value)
    except PermissionError:
        return False
    return True


def unregister_autorun(name):
    handle = _autorun_key_handle()
    try:
        winreg.DeleteValue(handle, name)
    except FileNotFoundError:
        pass


def get_wallpaper_path():
    path = ctypes.create_unicode_buffer(MAX_PATH)
    ctypes.windll.user32.SystemParametersInfoW(SPI_GETDESKWALLPAPER, MAX_PATH, ctypes.byref(path), None)
    return path.value


def set_wallpaper(*paths):
    for path in paths:
        if os.path.isfile(path):
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, None, path, SPIF_SENDWININICHANGE)
            return True
    return False
