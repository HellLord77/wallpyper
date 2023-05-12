import functools
import os.path
import re
from typing import ItemsView, Iterator, Optional, TypedDict

import gui
import validator
from libs import isocodes, request
from . import File, Source

_CONTENT_END = b'[ERROR 400] "page" is out of valid range.'

URL_BASE = 'https://pixabay.com/api'

CONFIG_KEY = 'key'
CONFIG_LANG = 'lang'
CONFIG_TYPE = 'image_type'
CONFIG_ORIENTATION = 'orientation'
CONFIG_CATEGORY = 'category'
CONFIG_COLORS = 'colors'
CONFIG_EDITOR = 'editors_choice'
CONFIG_SAFE = 'safesearch'
CONFIG_ORDER = 'order'

LANGS = (
    'cs', 'da', 'de', 'en', 'es', 'fr', 'id', 'it', 'hu', 'nl', 'no', 'pl', 'pt',
    'ro', 'sk', 'fi', 'sv', 'tr', 'vi', 'th', 'bg', 'ru', 'el', 'ja', 'ko', 'zh')
TYPES = 'all', 'photo', 'illustration', 'vector'
ORIENTATIONS = 'all', 'horizontal', 'vertical'
CATEGORIES = (
    '', 'backgrounds', 'fashion', 'nature', 'science', 'education', 'feelings',
    'health', 'people', 'religion', 'places', 'animals', 'industry', 'computer',
    'food', 'sports', 'transportation', 'travel', 'buildings', 'business', 'music')
COLORS = (
    'grayscale', 'transparent', 'red', 'orange', 'yellow', 'green',
    'turquoise', 'blue', 'lilac', 'pink', 'white', 'gray', 'black', 'brown')
ORDERS = 'popular', 'latest'


def _authenticate(key: str) -> bool:
    return bool(request.get(URL_BASE, {CONFIG_KEY: key, 'per_page': '3'}))


class Pixabay(Source):  # https://pixabay.com/api/docs
    NAME = '# pixabay'
    URL = 'https://pixabay.com'
    ICON = 'png'
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_KEY: str,
        'q': str,
        CONFIG_LANG: str,
        CONFIG_TYPE: str,
        CONFIG_ORIENTATION: str,
        CONFIG_CATEGORY: str,
        CONFIG_COLORS: str,
        CONFIG_EDITOR: bool,
        CONFIG_SAFE: bool,
        CONFIG_ORDER: str})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_KEY: '',
        'q': '',
        CONFIG_LANG: LANGS[3],
        CONFIG_TYPE: TYPES[0],
        CONFIG_ORIENTATION: ORIENTATIONS[0],
        CONFIG_CATEGORY: CATEGORIES[0],
        CONFIG_COLORS: '',
        CONFIG_EDITOR: False,
        CONFIG_SAFE: False,
        CONFIG_ORDER: ORDERS[0]}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_iterable, CONFIG_LANG, LANGS)
        cls._fix_config(validator.ensure_iterable, CONFIG_TYPE, TYPES)
        cls._fix_config(validator.ensure_iterable, CONFIG_ORIENTATION, ORIENTATIONS)
        cls._fix_config(validator.ensure_iterable, CONFIG_CATEGORY, CATEGORIES)
        cls._fix_config(validator.ensure_iterables_joined, CONFIG_COLORS, COLORS)
        cls._fix_config(validator.ensure_iterable, CONFIG_ORDER, ORDERS)

    @classmethod
    def create_menu(cls):
        gui.add_submenu_radio(cls._text('MENU_LANG'), {lang: re.split('[,;]', isocodes.ISO6392.get(
            alpha_2=lang).name)[0] for lang in LANGS}, cls.CURRENT_CONFIG, CONFIG_LANG)
        gui.add_submenu_radio(cls._text('MENU_TYPE'), {type_: cls._text(
            f'TYPE_{type_}') for type_ in TYPES}, cls.CURRENT_CONFIG, CONFIG_TYPE)
        gui.add_submenu_radio(cls._text('MENU_ORIENTATION'), {orientation: cls._text(
            f'ORIENTATION_{orientation}') for orientation in ORIENTATIONS},
                              cls.CURRENT_CONFIG, CONFIG_ORIENTATION)
        gui.add_submenu_radio(cls._text('MENU_CATEGORY'), {category: cls._text(
            f'CATEGORY_{category}') for category in CATEGORIES}, cls.CURRENT_CONFIG, CONFIG_CATEGORY)
        colors = cls.CURRENT_CONFIG[CONFIG_COLORS].split(',')
        menu_color = gui.add_submenu(cls._text('MENU_COLORS')).get_submenu()
        items_color = gui.get_menu_items(menu_color).items()
        for color in COLORS:
            gui.add_menu_item(cls._text(f'COLOR_{color}'), gui.MenuItemType.CHECK, color in colors,
                              uid=color, on_click=functools.partial(cls._on_color, items_color), menu=menu_color)
        gui.add_separator(2, menu_color)
        cls._on_color(items_color)
        gui.add_menu_item_check(cls._text('LABEL_EDITOR'), cls.CURRENT_CONFIG, CONFIG_EDITOR)
        gui.add_menu_item_check(cls._text('LABEL_SAFE'), cls.CURRENT_CONFIG, CONFIG_SAFE)
        gui.add_submenu_radio(cls._text('MENU_ORDER'), {order: cls._text(
            f'ORDER_{order}') for order in ORDERS}, cls.CURRENT_CONFIG, CONFIG_ORDER)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[File]]:
        hits: Optional[list] = None
        params['page'] = '1'
        while True:
            if not hits:
                response = request.get(URL_BASE, params)
                if (request.Status.BAD_REQUEST == response.status_code and
                        response.content == _CONTENT_END):
                    params['page'] = '1'
                    continue
                if response:
                    hits = response.json()['hits']
                if not hits:
                    yield
                    return
            hit = hits.pop(0)
            name = os.path.basename(hit['previewURL'])
            yield File(hit['largeImageURL'], f'{name[:name.rfind("_")]}{name[name.rfind("."):]}')

    @classmethod
    def _on_color(cls, items: ItemsView[str, gui.MenuItem]):
        cls.CURRENT_CONFIG[CONFIG_COLORS] = ','.join(
            color for color, item in items if item.is_checked())
