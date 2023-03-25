__version__ = '0.0.3'

import functools
import keyword
import re
from types import ModuleType
from typing import Optional

from libs import isocodes
from . import ben
from . import eng

_SUB_INVALID = re.compile(r'[^a-zA-Z0-9_]').sub

DEFAULT: ModuleType = eng


def _getattr(module: ModuleType, name: str) -> str:
    name = _SUB_INVALID('_', name)
    if name[0].isdigit():
        name = f'_{name}'
    if keyword.iskeyword(name):
        name = f'{name}_'
    try:
        return super(ModuleType, module).__getattribute__(name)
    except AttributeError:
        return f'<{name}>'


def to_str(num: int, lang: ModuleType, pad: Optional[int] = None) -> str:
    # noinspection PyProtectedMember
    return (f'{"".join(lang._DIGITS[int(char)] for char in str(num)):{lang._DIGITS[0]}>{pad or 0}}'
            if hasattr(lang, '_DIGITS') else _getattr(f'{num:0>{pad or 0}}'))


def _init():
    globals_ = globals()
    for language in isocodes.ISO6392:
        try:
            module = globals_[language]
        except KeyError:
            pass
        else:
            module.__getattr__ = functools.partial(_getattr, module)


_init()
