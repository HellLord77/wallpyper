__version__ = '0.0.2'

import contextlib
from types import ModuleType
from typing import Optional

from libs import isocodes
from . import ben
from . import eng

DEFAULT = eng


def _getattr(name: str) -> str:
    return f'<{name}>'


def to_str(num: int, lang: ModuleType, pad: Optional[int] = None) -> str:
    # noinspection PyProtectedMember
    return (f'{"".join(lang._DIGITS[int(char)] for char in str(num)):{lang._DIGITS[0]}>{pad or 0}}'
            if hasattr(lang, '_DIGITS') else _getattr(f'{num:0>{pad or 0}}'))


def _init():
    globals_ = globals()
    for language in isocodes.ISO6392:
        with contextlib.suppress(KeyError):
            globals_[language].__getattr__ = _getattr


_init()
