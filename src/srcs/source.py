from __future__ import annotations as _

import inspect
import os
from typing import Any, Generator, Iterable, Optional

import langs
from libs import files, utils

SOURCES: dict[str, type[_Source]] = {}


class _SourceMeta(type):
    def __new__(mcs, *args, **kwargs):
        cls = super().__new__(mcs, *args, **kwargs)
        if not cls.__name__.startswith('_'):
            cls.NAME = getattr(cls, 'NAME', cls.__name__)
            cls.VERSION = inspect.currentframe().f_back.f_globals.get('__version__', 'X.Y.Z')
            cls.ICON = os.path.join(os.path.dirname(__file__), 'res', getattr(cls, 'ICON', f'{cls.__name__}.png'))
            cls.DEFAULT_CONFIG = getattr(cls, 'DEFAULT_CONFIG', {})
            cls.CONFIG = {}
            cls.get_next_wallpaper = utils.LastCacheCallable(cls.get_next_wallpaper)
            # noinspection PyTypeChecker
            SOURCES[cls.__name__] = cls
        return cls


class _Source(metaclass=_SourceMeta):
    NAME: str
    VERSION: str
    ICON: str
    DEFAULT_CONFIG: dict[str, Any]
    CONFIG: dict[str, bool | str]
    STRINGS = langs.DEFAULT

    @classmethod
    def update_config(cls):
        pass

    @classmethod
    def _fix_config(cls, key: str, values: Iterable):
        utils.fix_dict_key(cls.CONFIG, key, values, cls.DEFAULT_CONFIG)

    @classmethod
    def fix_config(cls):
        pass

    @classmethod
    def get_next_wallpaper(cls, **params: bool | str) -> Generator[Optional[files.File], None, None]:
        raise NotImplementedError

    @classmethod
    def create_menu(cls):
        pass
