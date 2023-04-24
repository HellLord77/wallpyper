from PyInstaller.utils.hooks import collect_data_files

datas = collect_data_files('win32.cue', includes=['iCUESDK.x64_2019.dll'])
