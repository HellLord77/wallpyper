from PyInstaller.utils.hooks import collect_data_files

datas = collect_data_files('libs.request', includes=['browser.json'])
