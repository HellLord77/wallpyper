from __future__ import annotations as _

import inspect
from typing import Generator, Iterable, Optional, Union

import langs
from libs import files, misc

MODULES: dict[str, type[_Module]] = {}


class _ModuleMeta(type):
    def __new__(mcs, *args, **kwargs):
        _self = super().__new__(mcs, *args, **kwargs)
        _self.NAME = getattr(_self, 'NAME', _self.__name__)
        _self.VERSION = inspect.currentframe().f_back.f_globals.get('__version__', '0.0.0')
        _self.DEFAULT_CONFIG = getattr(_self, 'DEFAULT_CONFIG', {})
        _self.CONFIG = {}
        _self.get_next_wallpaper = misc.one_cache(_self.get_next_wallpaper)
        if not _self.NAME.startswith('_'):
            # noinspection PyTypeChecker
            MODULES[_self.__name__] = _self
        return _self


class _Module(metaclass=_ModuleMeta):
    NAME: str
    VERSION: str
    DEFAULT_CONFIG: dict[str, str]
    CONFIG: dict[str, Union[bool, str]]
    STRINGS = langs.DEFAULT

    @classmethod
    def _fix_config(cls, key: str, values: Iterable[str]):
        if cls.CONFIG[key] not in values:
            cls.CONFIG[key] = cls.DEFAULT_CONFIG[key]

    @classmethod
    def fix_config(cls):
        pass

    @classmethod
    def get_next_wallpaper(cls, **params: str) -> Generator[Optional[files.File], None, None]:
        raise NotImplementedError

    @classmethod
    def create_menu(cls):
        pass
