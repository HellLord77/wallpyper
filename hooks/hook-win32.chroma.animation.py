from PyInstaller.utils.hooks import collect_data_files

datas = collect_data_files('win32.chroma.animation', includes=[
    'Animations/*.chroma', 'CChromaEditorLibrary64.dll'])
