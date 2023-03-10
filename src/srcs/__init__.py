from __future__ import annotations as _

__version__ = '0.1.3'

import os
from typing import Any, Callable, Iterator, Optional, TypedDict

import langs
from libs import callables, files

SOURCES: dict[str, type[Source]] = {}


class Source:
    NAME: str = ''
    VERSION: str = '0.0.0'
    ICON: str = 'ico'
    URL: str = ''
    TCONFIG: type[dict] | type[TypedDict] = dict[str, Any]
    DEFAULT_CONFIG: dict[str, Any] = None
    CURRENT_CONFIG: dict[str, Any] = None

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
    def _fix_config(cls, validator: Callable, key: str, *args, **kwargs) -> bool:
        return validator(cls.CURRENT_CONFIG, cls.DEFAULT_CONFIG, key, *args, **kwargs)

    @classmethod
    def fix_config(cls, saving: bool = False):
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
