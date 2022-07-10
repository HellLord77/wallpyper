from __future__ import annotations as _

__version__ = '0.0.2'

import collections
import json
import os
from typing import Optional, Union


class _ISOMeta(type):
    _BASE_: collections.namedtuple

    def __new__(mcs, *args, **kwargs):
        self = super().__new__(mcs, *args, **kwargs)
        # noinspection PyUnresolvedReferences
        if iso := self._ISO_:
            with open(os.path.join(os.path.dirname(__file__), f'iso_{iso}.json'), 'r') as file:
                self._items = json.load(file)[iso]
        return self

    def __iter__(self):
        # noinspection PyProtectedMember
        return (item[self._BASE_._fields[0]] for item in self._items)


class _ISO(metaclass=_ISOMeta):
    _ISO_ = ''

    @classmethod
    def get(cls, *args, **kwargs):
        # noinspection PyProtectedMember
        fields = cls._BASE_._fields
        kwargs.update(zip(fields, args))
        for key in fields:
            if (val := kwargs[key]) is not None:
                for index, item in enumerate(cls._items):
                    if isinstance(item, dict):
                        if item.get(key, '') == val:
                            item_ = cls._BASE_(**item)
                            cls._items[index] = item_
                            return item_
                    elif getattr(item, key) == val:
                        return item
                break
        return cls._BASE_(**kwargs)


class Language(_ISO):
    _ISO_ = '639-2'
    _BASE_ = collections.namedtuple('Language', ('alpha_3', 'name', 'alpha_2', 'bibliographic', 'common_name'), defaults=('', '', ''))

    @classmethod
    def get(cls, alpha_3: Optional[str] = None, name: Optional[str] = None, alpha_2: Optional[str] = None, bibliographic: Optional[str] = None, common_name: Optional[str] = None) -> _BASE_:
        pass

    del get


class Country(_ISO):
    _ISO_ = '3166-1'
    _BASE_ = collections.namedtuple('Country', ('alpha_2', 'alpha_3', 'flag', 'name', 'numeric', 'official_name', 'common_name'), defaults=('', ''))

    @classmethod
    def get(cls, alpha_2: Optional[str] = None, alpha_3: Optional[str] = None, flag: Optional[str] = None, name: Optional[str] = None, numeric: Optional[str] = None, official_name: Optional[str] = None, common_name: Optional[str] = None) -> _BASE_:
        pass

    del get


class Locale:
    _BASE_ = collections.namedtuple('Locale', ('language', 'country', 'tag', 'name'))

    # noinspection PyProtectedMember
    @classmethod
    def get(cls, language: Optional[Union[str, Language._BASE_]] = None, country: Optional[Union[str, Country._BASE_]] = None) -> _BASE_:
        if not isinstance(language, Language._BASE_):
            language = Language.get(alpha_2=language)
        if not isinstance(country, Country._BASE_):
            country = Country.get(country)
        return cls._BASE_(language, country, f'{language.alpha_2}-{country.alpha_2}', f'{language.name} - {country.name}')
