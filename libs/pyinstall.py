__version__ = '0.0.1'

import glob
import os
import shutil
import sys
import tempfile

FROZEN = hasattr(sys, 'frozen')
TEMP_DIR = getattr(sys, '_MEIPASS', '')


def clean_mei():
    base = os.path.dirname(TEMP_DIR) or tempfile.gettempdir()
    for dir_ in glob.glob(os.path.join(base, f'_MEI{"[0-9]" * 6}')):
        path = os.path.join(base, dir_)
        if os.path.isdir(path) and path != TEMP_DIR:
            pydll = glob.glob(os.path.join(path, f'python{"[0-9]" * 2}.dll'))
            if pydll and os.path.isfile(pydll[0]):
                try:
                    os.remove(pydll[0])
                except PermissionError:
                    continue
            shutil.rmtree(path, True)
