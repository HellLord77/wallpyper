from ctypes import c_void_p, sizeof

from PyInstaller.utils.hooks import collect_data_files

datas = collect_data_files('win32.chroma.animation', includes=[
    'Animations/*.chroma', f'CChromaEditorLibrary{"64" if sizeof(c_void_p) == 8 else ""}.dll'])
