import functools
import itertools
import operator
import os
from typing import Callable, Iterator, Optional, TypedDict

import gui
import validator
from libs import request, utils
from . import ImageFile, Source

URL_BASE = 'https://livestartpage.com'
URL_PHOTO = request.join_url(URL_BASE, 'gallery', 'api', 'getPhotoByTags')

CONFIG_CATEGORY = 'tags'
CONFIG_RANDOM = 'mode'
CONFIG_CURSOR = 'cursor'

CATEGORIES = 36, 34, 44

_CURSOR = utils.MutableInt()


class LiveStartPage(Source):
    NAME = 'Live Start Page'
    VERSION = '0.0.1'
    URL = URL_BASE
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_CATEGORY: list[bool],
        CONFIG_RANDOM: bool,
        CONFIG_CURSOR: int})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_CATEGORY: [True] * len(CATEGORIES),
        CONFIG_RANDOM: True,
        CONFIG_CURSOR: 0}

    _set_tooltip: Callable[[str], bool]

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_truthy, CONFIG_CATEGORY)
        if saving:
            cls.CURRENT_CONFIG[CONFIG_CURSOR] = _CURSOR.get()
        else:
            _CURSOR.set(cls.CURRENT_CONFIG[CONFIG_CURSOR])

    @classmethod
    def create_menu(cls):
        gui.add_submenu_check(cls._text('MENU_CATEGORY'), (cls._text(
            f'CATEGORY_{category}') for category in CATEGORIES),
                              (1, None), cls.CURRENT_CONFIG, CONFIG_CATEGORY)
        item_random = gui.add_menu_item(
            cls._text('LABEL_RESET'), on_click=cls._on_reset)
        cls._set_tooltip = item_random.set_tooltip
        cls._set_tooltip(cls._text('TOOLTIP_TEMPLATE_CURSOR').format(_CURSOR))
        on_random = functools.partial(cls._on_random, item_random.enable)
        gui.add_menu_item_check(cls._text('LABEL_RANDOM'), cls.CURRENT_CONFIG,
                                CONFIG_RANDOM, on_click=on_random, position=1)
        on_random(cls.CURRENT_CONFIG[CONFIG_RANDOM])

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        params[CONFIG_CATEGORY] = ','.join(map(
            str, itertools.compress(CATEGORIES, params[CONFIG_CATEGORY])))
        random = params.pop(CONFIG_RANDOM)
        if random:
            params[CONFIG_RANDOM] = 'random'
        _CURSOR.set(params.pop(CONFIG_CURSOR))
        while True:
            cls._set_tooltip(
                cls._text('TOOLTIP_TEMPLATE_CURSOR').format(_CURSOR))
            if not random:
                params[CONFIG_CURSOR] = str(_CURSOR)
            response = request.get(URL_PHOTO, params)
            if response:
                body = response.json()['body'][0]
                if random or int(body['id']) < _CURSOR.get():
                    _CURSOR.set(cls.DEFAULT_CONFIG[CONFIG_CURSOR])
                    if not random:
                        continue
                else:
                    operator.iadd(_CURSOR, 1)
                source = body['source']
                yield ImageFile(source, body['title'] + os.path.splitext(
                    source)[1], url=body['link'], width=int(body['width']),
                                height=int(body['height']))
            else:
                yield

    @classmethod
    def _on_random(cls, enable: Callable[[bool], bool], random: bool):
        enable(not random)

    @classmethod
    def _on_reset(cls):
        cursor = cls.CURRENT_CONFIG[CONFIG_CURSOR] = cls.DEFAULT_CONFIG[CONFIG_CURSOR]
        cls._set_tooltip(cls._text('TOOLTIP_TEMPLATE_CURSOR').format(cursor))
