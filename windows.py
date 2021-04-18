import ctypes
from os import environ
from os.path import isfile, join

MAX_PATH = 0x104
SPI_GETDESKWALLPAPER = 0x73
SPI_SETDESKWALLPAPER = 0x14
SPIF_SENDWININICHANGE = 0x2
CACHEDFILES_PATH = join(environ['APPDATA'], 'Microsoft', 'Windows', 'Themes', 'CachedFiles')


def get_wallpaper_path():
    path = ctypes.create_unicode_buffer(MAX_PATH)
    ctypes.windll.user32.SystemParametersInfoW(SPI_GETDESKWALLPAPER, MAX_PATH, ctypes.byref(path), None)
    return path.value


def set_wallpaper(*paths):
    for path in paths:
        if isfile(path):
            return ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, None, path, SPIF_SENDWININICHANGE)
    return 0


def test():
    import main
    import os
    set_wallpaper('E:\\Projects\\wallhaven\\img7.jpg')
    print(main.configs['save_path'])
    print(get_wallpaper_path())
    print(os.path.dirname(get_wallpaper_path()))
    # join(CACHEDFILES_PATH, next(walk(CACHEDFILES_PATH))[2][0])


if __name__ == '__main__':
    test()
