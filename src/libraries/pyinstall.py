__version__ = '0.0.2'

import glob
import os
import shutil
import sys
import tempfile
from typing import Optional

FROZEN = hasattr(sys, 'frozen')
TEMP_DIR = getattr(sys, '_MEIPASS', '')


def clean_temp(remove_base: Optional[bool] = None) -> bool:
    cleaned = True
    base = os.path.dirname(TEMP_DIR) or tempfile.gettempdir()
    for dir_ in glob.iglob(os.path.join(base, f'_MEI{"[0-9]" * 6}')):
        path = os.path.join(base, dir_)
        if os.path.isdir(path) and path != TEMP_DIR:
            pydll = glob.glob(os.path.join(path, f'python{"[0-9]" * 2}.dll'))
            if pydll and os.path.isfile(pydll[0]):
                try:
                    os.remove(pydll[0])
                except PermissionError:
                    continue
            shutil.rmtree(path, True)
            cleaned = cleaned and not os.path.exists(path)
    if remove_base and not any(os.scandir(base)):
        os.remove(base)
        cleaned = cleaned and not os.path.exists(base)
    return cleaned


def get_argv() -> list[str]:
    argv = sys.argv.copy()
    if not FROZEN:
        argv.insert(0, sys.executable)
    return argv
