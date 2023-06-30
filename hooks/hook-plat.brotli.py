from sys import platform

from PyInstaller.utils.hooks import collect_data_files

includes = 'brotlicommon', 'brotlidec', 'brotlienc'
if platform == 'win32':
    includes = [lib + '.dll' for lib in includes]
else:
    includes = [f'lib{lib}.so' for lib in includes]

datas = collect_data_files('plat.brotli', includes=includes)
