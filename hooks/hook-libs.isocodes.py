from PyInstaller.utils.hooks import collect_data_files

datas = collect_data_files('libs.isocodes', includes=['iso_*.json'])
