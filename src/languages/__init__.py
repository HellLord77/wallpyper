__version__ = '0.0.1'

from . import en

__all__ = 'en',

DEFAULT = en


def _getattr(name: str) -> str:
    return f'${name}'


def _init():
    globals_ = globals()
    for language in __all__:
        globals_[language].__getattr__ = _getattr


_init()
