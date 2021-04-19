import ctypes
import os

MAX_PATH = 0x104
SPI_GETDESKWALLPAPER = 0x73
SPI_SETDESKWALLPAPER = 0x14
SPIF_SENDWININICHANGE = 0x2

APPDATA_DIR = os.environ['APPDATA']
TEMP_DIR = os.environ['TEMP']
WALLPAPER_DIR = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Themes', 'CachedFiles')


def get_wallpaper_path():
    path = ctypes.create_unicode_buffer(MAX_PATH)
    ctypes.windll.user32.SystemParametersInfoW(SPI_GETDESKWALLPAPER, MAX_PATH, ctypes.byref(path), None)
    return path.value


def set_wallpaper(*paths):
    for path in paths:
        if os.path.isfile(path):
            return ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, None, path, SPIF_SENDWININICHANGE)
    return 0


def main():
    pass


if __name__ == '__main__':
    main()
