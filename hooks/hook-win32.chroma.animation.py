from sys import maxsize

from PyInstaller.utils.hooks import collect_data_files

arg = '64' if maxsize > 2 ** 32 else ''
datas = collect_data_files('win32.chroma.animation', includes=[
    'Animations/*.chroma', 'CChromaEditorLibrary{}.dll'.format(arg)])
