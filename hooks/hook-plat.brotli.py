from sys import platform

from PyInstaller.utils.hooks import collect_data_files

fmt = '{}.dll' if platform == 'win32' else 'lib{}.so'
datas = collect_data_files('plat.brotli', includes=[
    fmt.format(lib) for lib in ('brotlicommon', 'brotlidec', 'brotlienc')])
