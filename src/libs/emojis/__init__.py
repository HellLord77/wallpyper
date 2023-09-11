__version__ = '0.0.1'  # https://github.com/github/gemoji

import enum
import functools
import json
import os
from typing import NamedTuple

_PATH = 'emoji.json'


class Category(enum.StrEnum):
    SMILEYS_AND_EMOTION = 'Smileys & Emotion'
    PEOPLE_AND_BODY = 'People & Body'
    ANIMALS_AND_NATURE = 'Animals & Nature'
    FOOD_AND_DRINK = 'Food & Drink'
    TRAVEL_AND_PLACES = 'Travel & Places'
    ACTIVITIES = 'Activities'
    OBJECTS = 'Objects'
    SYMBOLS = 'Symbols'
    FLAGS = 'Flags'


class Emoji(NamedTuple):
    emoji: str
    description: str
    category: Category
    aliases: tuple[str, ...]
    tags: tuple[str, ...]
    unicode_version: float
    ios_version: float


def is_emoji(string: str) -> bool:
    return string in load()[0]


def get(emoji: str, default=None) -> Emoji:
    try:
        return load()[0][emoji]
    except KeyError:
        try:
            return get(load()[1][emoji])
        except KeyError:
            return default


# noinspection PyShadowingBuiltins
def format(string: str) -> str:
    return string.format_map(load()[1])


@functools.cache
def load() -> tuple[dict[str, Emoji], dict[str, str]]:
    emojis = {}
    aliases = {}
    with open(os.path.join(os.path.dirname(__file__), _PATH), encoding='utf-8') as file:
        for emoji in json.load(file):
            emoji__ = Emoji(emoji_ := emoji['emoji'], emoji['description'], Category(
                emoji['category']), tuple(emoji['aliases']), tuple(emoji['tags']), float(
                emoji['unicode_version'] or 0.0), float(emoji['ios_version'] or 0.0))
            emojis[emoji_] = emoji__
            for alias in emoji__.aliases:
                aliases[alias] = emoji_
    return emojis, aliases


if __debug__:
    def download():
        import urllib.parse
        import urllib.request
        urllib.request.urlretrieve(urllib.parse.urljoin(
            'https://raw.githubusercontent.com/github/gemoji/master/db/',
            _PATH), os.path.join(os.path.dirname(__file__), _PATH))
        load.cache_clear()
        load()
