import ctypes

import libs.gui
import platforms.win32

SHGFP_TYPE_CURRENT = 0


def main():
    path = ctypes.create_unicode_buffer(160)
    print(ctypes.windll.shell32.SHGetFolderPathW(None, 0x27, None, SHGFP_TYPE_CURRENT, ctypes.byref(path)))
    print(path.value)
    print(libs.gui.PROPERTY.IS_CHECKED in libs.gui.PROPERTY.__dict__.values())
    print(platforms.win32.APPDATA_DIR, platforms.win32.TEMP_DIR, platforms.win32.PICTURES_DIR)


if __name__ == '__main__':
    main()
