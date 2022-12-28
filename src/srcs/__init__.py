from __future__ import annotations as _

__version__ = '0.1.0'

import inspect
import os
from typing import Any, Generator, Iterable, Optional

import langs
from libs import files, utils

SOURCES: dict[str, type[Source]] = {}


class _SourceMeta(type):
    def __new__(mcs, *args, **kwargs):
        cls = super().__new__(mcs, *args, **kwargs)
        if cls.__name__.startswith('_'):
            name = cls.__module__.split('.')[-1]
            cls.NAME = getattr(cls, 'NAME', name)
            cls.VERSION = getattr(cls, 'VERSION', inspect.currentframe().f_back.f_globals.get('__version__', 'X.Y.Z'))
            cls.ICON = os.path.join(os.path.dirname(__file__), 'res', f'{name}.{getattr(cls, "ICON", "ico")}')
            cls.DEFAULT_CONFIG = getattr(cls, 'DEFAULT_CONFIG', {})
            cls.CONFIG = {}
            cls.get_next_wallpaper = utils.LastCacheCallable(cls.get_next_wallpaper)
            # noinspection PyTypeChecker
            SOURCES[name] = cls
        return cls


class Source(metaclass=_SourceMeta):
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


from . import (
    local,
    wallhaven,
    unsplash, pixabay, pexels, _500px,
    bing, spotlight)  # NOQA: E402
