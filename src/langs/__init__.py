__version__ = '0.0.5'

import builtins
import functools
import keyword
import re
from types import ModuleType
from typing import Optional

from libs import isocodes
from . import ben
from . import eng

_SPLIT_DIGIT = re.compile(r'(\d+)').split
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


# noinspection PyShadowingBuiltins
def int(num: int | str, lang: ModuleType, pad: Optional[int] = None) -> str:
    if isinstance(num, str):
        return ''.join(int(builtins.int(part), lang) if part.isdigit() else part for part in _SPLIT_DIGIT(num))
    return (f'{"".join(lang.__DIGITS__[builtins.int(char)] for char in str(num)):{lang.__DIGITS__[0]}>{pad or 0}}'
            if hasattr(lang, '__DIGITS__') else _getattr(DEFAULT, f'{num:0>{pad or 0}}'))


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
