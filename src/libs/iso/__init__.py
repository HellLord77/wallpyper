from __future__ import annotations as _

__version__ = '0.0.3'  # https://salsa.debian.org/iso-codes-team/iso-codes

import collections
import json
import os
from typing import Optional


class _ISOMeta(type):
    _BASE_: collections.namedtuple

    _iso = ''
    _items = None

    def __iter__(cls):
        if cls._items is None:
            iso = cls._iso or f'{cls.__name__[3:-1]}-{cls.__name__[-1]}'
            with open(os.path.join(os.path.dirname(__file__), 'res', f'iso_{iso}.json'), encoding='utf-8') as file:
                cls._items = json.load(file)[iso]
        # noinspection PyProtectedMember
        return (item[cls._BASE_._fields[0]] for item in cls._items)

    def __getitem__(cls, key: str):
        return cls.get(key)

    def get(cls, *args, **kwargs):
        iter(cls)
        # noinspection PyProtectedMember
        fields = cls._BASE_._fields
        kwargs.update(zip(fields, args))
        for key in fields:
            if val := kwargs.get(key):
                for index, item in enumerate(cls._items):
                    if isinstance(item, dict):
                        if item.get(key, '') == val:
                            item_ = cls._BASE_(**item)
                            cls._items[index] = item_
                            return item_
                    elif getattr(item, key) == val:
                        return item
                break
        raise KeyError(kwargs)


class ISO6392(metaclass=_ISOMeta):
    _BASE_ = collections.namedtuple('ISO_639_2', ('alpha_3', 'name', 'alpha_2',
                                                  'bibliographic', 'common_name'), defaults=('', '', ''))

    @classmethod
    def get(cls, alpha_3: Optional[str] = None, name: Optional[str] = None, alpha_2: Optional[str] = None,
            bibliographic: Optional[str] = None, common_name: Optional[str] = None) -> _BASE_:
        pass

    del get


class ISO6393(metaclass=_ISOMeta):
    _BASE_ = collections.namedtuple('ISO_639_3', ('alpha_3', 'name', 'scope', 'type', 'alpha_2', 'common_name',
                                                  'inverted_name', 'bibliographic'), defaults=('', '', '', ''))

    # noinspection PyShadowingBuiltins
    @classmethod
    def get(cls, alpha_3: Optional[str] = None, name: Optional[str] = None, scope: Optional[str] = None,
            type: Optional[str] = None, alpha_2: Optional[str] = None, common_name: Optional[str] = None,
            inverted_name: Optional[str] = None, bibliographic: Optional[str] = None) -> _BASE_:
        pass

    del get


class ISO6395(metaclass=_ISOMeta):
    _BASE_ = collections.namedtuple('ISO_639_5', ('alpha_3', 'name'))

    # noinspection PyShadowingBuiltins
    @classmethod
    def get(cls, alpha_3: Optional[str] = None, name: Optional[str] = None) -> _BASE_:
        pass

    del get


class ISO31661(metaclass=_ISOMeta):
    _BASE_ = collections.namedtuple('ISO_3166_1', ('alpha_2', 'alpha_3', 'flag', 'name', 'numeric',
                                                   'official_name', 'common_name'), defaults=('', ''))

    @classmethod
    def get(cls, alpha_2: Optional[str] = None, alpha_3: Optional[str] = None,
            flag: Optional[str] = None, name: Optional[str] = None, numeric: Optional[str] = None,
            official_name: Optional[str] = None, common_name: Optional[str] = None) -> _BASE_:
        pass

    del get


class ISO31662(metaclass=_ISOMeta):
    _BASE_ = collections.namedtuple('ISO_3166_2', ('code', 'name', 'type'))

    # noinspection PyShadowingBuiltins
    @classmethod
    def get(cls, code: Optional[str] = None, name: Optional[str] = None, type: Optional[str] = None) -> _BASE_:
        pass

    del get


class ISO31663(metaclass=_ISOMeta):
    _BASE_ = collections.namedtuple('ISO_3166_3', ('alpha_2', 'alpha_3', 'alpha_4', 'name',
                                                   'numeric', 'comment', 'withdrawal_date'), defaults=('', '', ''))

    @classmethod
    def get(cls, alpha_2: Optional[str] = None, alpha_3: Optional[str] = None,
            alpha_4: Optional[str] = None, name: Optional[str] = None, numeric: Optional[str] = None,
            comment: Optional[str] = None, withdrawal_date: Optional[str] = None) -> _BASE_:
        pass

    del get


class ISO4217(metaclass=_ISOMeta):
    _iso = '4217'
    _BASE_ = collections.namedtuple('ISO_4217', ('alpha_3', 'name', 'numeric'))

    @classmethod
    def get(cls, alpha_3: Optional[str] = None, name: Optional[str] = None, numeric: Optional[str] = None) -> _BASE_:
        pass

    del get


class ISO15924(metaclass=_ISOMeta):
    _iso = '15924'
    _BASE_ = collections.namedtuple('ISO_15924', ('alpha_4', 'name', 'numeric'))

    @classmethod
    def get(cls, alpha_4: Optional[str] = None, name: Optional[str] = None, numeric: Optional[str] = None) -> _BASE_:
        pass

    del get


class __Locale:
    _BASE_ = collections.namedtuple('Locale', ('language', 'country', 'tag', 'name'))

    # noinspection PyProtectedMember
    @classmethod
    def get(cls, language: Optional[str | ISO6392._BASE_] = None,
            country: Optional[str | ISO31661._BASE_] = None) -> _BASE_:
        if not isinstance(language, ISO6392._BASE_):
            language = ISO6392.get(alpha_2=language)
        if not isinstance(country, ISO31661._BASE_):
            country = ISO31661.get(country)
        return cls._BASE_(language, country, f'{language.alpha_2}-{country.alpha_2}', f'{language.name} - {country.name}')
