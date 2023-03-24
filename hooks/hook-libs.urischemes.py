from PyInstaller.utils.hooks import collect_data_files

datas = collect_data_files('libs.urischemes', includes=['uri-schemes-1.csv'])
