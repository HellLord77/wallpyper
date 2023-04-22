from PyInstaller.utils.hooks import collect_data_files

datas = collect_data_files('win32.cue.game', includes=['CgSDK.x64_2019.dll'])
