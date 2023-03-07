from __future__ import annotations as _

__version__ = '0.1.2'

import os
from typing import Any, Iterable, Iterator, Optional

import langs
from libs import callables, files, utils

SOURCES: dict[str, type[Source]] = {}


class Source:
    NAME: str = ''
    VERSION: str = '0.0.0'
    ICON: str = 'ico'
    URL: str
    DEFAULT_CONFIG: Optional[dict[str, Any]] = None
    CURRENT_CONFIG: Optional[dict[str, bool | str]] = None

    strings = langs.DEFAULT

    def __init_subclass__(cls):
        uid = cls.__module__.split('.')[-1]
        if not cls.NAME:
            cls.NAME = cls.__name__
        cls.ICON = os.path.join(os.path.dirname(__file__), 'res', f'{uid}.{cls.ICON}')
        if cls.DEFAULT_CONFIG is None:
            cls.DEFAULT_CONFIG = {}
        cls.CURRENT_CONFIG = {}
        cls.get_image = callables.LastCacheCallable(cls.get_image)
        SOURCES[uid] = cls

    @classmethod
    def _fix_config(cls, key: str, values: Iterable):
        utils.fix_dict_key(cls.CURRENT_CONFIG, key, values, cls.DEFAULT_CONFIG)

    @classmethod
    def fix_config(cls):
        pass

    @classmethod
    def create_menu(cls):
        pass

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[files.File]]:
        raise NotImplementedError

    @classmethod
    def filter_image(cls, image: files.File) -> bool:
        return True


from . import (
    _fivehundredpx,
    _shutterstock,
    bing,
    doesnotexist,
    fivehundredpxlegacy,
    local,
    pexels,
    pixabay,
    reddit,
    spotlight,
    unsplash,
    wallhaven)  # NOQA: E402
