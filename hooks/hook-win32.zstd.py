from PyInstaller.utils.hooks import collect_data_files

datas = collect_data_files('win32.zstd', includes=['libzstd.dll'])
