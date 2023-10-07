import os
import pprint
from typing import Iterator
from typing import Optional
from typing import TypedDict

import gui
import validator
from libs import request
from libs import sgml
from . import CONFIG_ORIENTATIONS
from . import CONFIG_RATINGS
from . import ImageFile
from . import Source

URL_BASE = request.join_url('https://backend.deviantart.com', 'rss.xml')

CONFIG_STATIC = '_static'
CONFIG_SEARCH = 'q'
CONFIG_ORDER = 'order'

ORDERS = '5', '14', '15', '9',

_ATTRS_NEXT = {'rel': 'next'}


class DeviantArt(Source):
    NAME = 'DeviantArt [legacy]'
    VERSION = '0.0.1'
    URL = 'https://www.deviantart.com'
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_ORIENTATIONS: list[bool],
        CONFIG_RATINGS:      list[bool],
        CONFIG_STATIC:       bool,
        CONFIG_SEARCH:       str,
        CONFIG_ORDER:        str})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_ORIENTATIONS: [True, True],
        CONFIG_RATINGS:      [True, True],
        CONFIG_STATIC:       True,
        CONFIG_SEARCH:       '',
        CONFIG_ORDER:        ORDERS[3]}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_contains, CONFIG_ORDER, ORDERS)
        super().fix_config(saving)

    @classmethod
    def create_menu(cls):
        gui.add_submenu_radio(cls._text('MENU_ORDER'), {order: cls._text(
            f'ORDER_{order}') for order in ORDERS}, cls.CURRENT_CONFIG, CONFIG_ORDER)
        gui.add_separator()
        gui.add_menu_item_check(cls._text('LABEL_STATIC'),
                                cls.CURRENT_CONFIG, CONFIG_STATIC)
        super().create_menu()

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        items = []
        params['type'] = 'deviation'
        while True:
            if not items:
                response = request.get(URL_BASE, params)
                if response:
                    channel = sgml.loads(response.text)[0]
                    items = list(channel.find_all('item', recursive=False))
                    if (next_ := channel.find('atom:link', _ATTRS_NEXT)) is not None:
                        params['offset'] = request.extract_params(
                            next_['href'])['offset'][0]
                if not items:
                    yield
                    continue
            item = items.pop(0)
            pprint.pprint(item, sort_dicts=False)
            content = item.find('media:content')
            url_content = content['url']
            url_original = request.join_url(*request.split_url(url_content)[:4])
            yield ImageFile(request.encode_params(url_original, request.extract_params(
                url_content)), item.find('title').get_data() + os.path.splitext(
                url_original)[1], url=item.find('link').get_data(), ratio=int(content['width']) / int(
                content['height']), nsfw=item.find('media:rating').get_text() == 'adult')

    @classmethod
    def filter_image(cls, image: ImageFile) -> bool:
        if cls.CURRENT_CONFIG[CONFIG_STATIC] and not image.is_static():
            return False
        return super().filter_image(image)
