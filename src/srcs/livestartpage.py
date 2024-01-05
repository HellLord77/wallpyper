import functools
import os
from typing import Callable
from typing import Iterator
from typing import Optional
from typing import TypedDict

import gui
import validator
from libs import request
from . import ImageFile
from . import Source

URL_BASE = 'https://livestartpage.com'
URL_PHOTO = request.join_url(URL_BASE, 'gallery', 'api', 'getPhotoByTags')

CONFIG_CATEGORY = 'tags'
CONFIG_RANDOM = 'mode'
CONFIG_CURSOR = 'cursor'

CATEGORIES = 36, 34, 44


class LiveStartPage(Source):
    NAME = 'Live Start Page'
    VERSION = '0.0.3'
    URL = URL_BASE
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_CATEGORY: list[int],
        CONFIG_RANDOM: bool,
        CONFIG_CURSOR: int})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_CATEGORY: list(CATEGORIES),
        CONFIG_RANDOM: True,
        CONFIG_CURSOR: 0}

    _cursor: int
    _set_tooltip: Callable[[str], bool]

    @classmethod
    def load_config(cls):
        cls._fix_config(validator.ensure_subset,
                        CONFIG_CATEGORY, CATEGORIES, casefold=False)
        cls._fix_config(validator.ensure_truthy, CONFIG_CATEGORY)
        cls._fix_config(validator.ensure_positive, CONFIG_CURSOR, False)

        cls._cursor = cls.CURRENT_CONFIG[CONFIG_CURSOR]

    @classmethod
    def dump_config(cls) -> TCONFIG:
        dumped = super().dump_config()
        dumped[CONFIG_CURSOR] = cls._cursor
        return dumped

    @classmethod
    def create_menu(cls):
        gui.add_submenu_check(cls._text('MENU_CATEGORY'), {category: cls._text(
            f'CATEGORY_{category}') for category in CATEGORIES},
                              (1, None), cls.CURRENT_CONFIG, CONFIG_CATEGORY)
        item_random = gui.add_menu_item(cls._text('LABEL_RESET'), on_click=cls._on_reset)
        cls._set_tooltip = item_random.set_tooltip
        cls._on_reset(cls.CURRENT_CONFIG[CONFIG_CURSOR])
        on_random = functools.partial(cls._on_random, item_random.enable)
        gui.add_menu_item_check(cls._text('LABEL_RANDOM'), cls.CURRENT_CONFIG,
                                CONFIG_RANDOM, on_click=on_random, position=1)
        on_random(cls.CURRENT_CONFIG[CONFIG_RANDOM])

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        params[CONFIG_CATEGORY] = ','.join(map(str, params[CONFIG_CATEGORY]))
        random = params.pop(CONFIG_RANDOM)
        if random:
            params[CONFIG_RANDOM] = 'random'
        cls._cursor = params.pop(CONFIG_CURSOR)
        while True:
            file = None
            cls._set_tooltip(cls._text('TOOLTIP_FMT_CURSOR').format(cls._cursor))
            if not random:
                params[CONFIG_CURSOR] = str(cls._cursor)
            response = request.get(URL_PHOTO, params)
            if response:
                body = response.json()['body'][0]
                if random or int(body['id']) < cls._cursor:
                    cls._cursor = cls.DEFAULT_CONFIG[CONFIG_CURSOR]
                    if not random:
                        continue
                else:
                    cls._cursor += 1
                source = body['source']
                file = ImageFile(source, body['title'] + os.path.splitext(source)[1],
                                 url=body['link'], width=int(body['width']), height=int(body['height']))
            yield file

    @classmethod
    def _on_random(cls, enable: Callable[[bool], bool], random: bool):
        enable(not random)

    @classmethod
    def _on_reset(cls, cursor: int = DEFAULT_CONFIG[CONFIG_CURSOR]):
        cls.CURRENT_CONFIG[CONFIG_CURSOR] = cursor
        cls._set_tooltip(cls._text('TOOLTIP_FMT_CURSOR').format(cursor))
