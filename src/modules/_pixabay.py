__version__ = '0.0.1'  # 'https://pixabay.com/api/docs'

import os.path
import re
from typing import Generator, Optional

import gui
from libs import files, iso_codes, request
from .module import _Module

BASE_URL = 'https://pixabay.com/api'

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
    return bool(request.open(BASE_URL, {CONFIG_KEY: key, 'per_page': '3'}))


class Pixabay(_Module):
    ICON = 'Pixabay.png'
    DEFAULT_CONFIG = {
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
    def fix_config(cls):
        cls._fix_config(CONFIG_LANG, LANGS)
        cls._fix_config(CONFIG_TYPE, TYPES)
        cls._fix_config(CONFIG_ORIENTATION, ORIENTATIONS)
        cls._fix_config(CONFIG_CATEGORY, CATEGORIES)
        for color in cls.CONFIG[CONFIG_COLORS].split(','):
            if color not in COLORS:
                cls.CONFIG[CONFIG_COLORS] = cls.DEFAULT_CONFIG[CONFIG_COLORS]
                break
        cls._fix_config(CONFIG_ORDER, ORDERS)

    @classmethod
    def get_next_wallpaper(cls, **params: str) -> Generator[Optional[files.File], None, None]:
        hits: Optional[list] = None
        params['page'] = '1'
        params['per_page'] = '200'
        while True:
            if not hits:
                pass
                response = request.open(BASE_URL, params)
                if (response.status == request.Status.BAD_REQUEST and
                        response.get_content() == b'[ERROR 400] "page" is out of valid range.'):
                    params['page'] = '1'
                    continue
                if response:
                    hits = response.get_json()['hits']
                if not hits:
                    yield
                    return
            hit = hits.pop(0)
            name = os.path.basename(hit['previewURL'])
            yield files.File(hit['largeImageURL'], f'{name[:name.rfind("_")]}{name[name.rfind("."):]}')

    @classmethod
    def create_menu(cls):
        gui.add_mapped_submenu(cls.STRINGS.PIXABAY_MENU_LANG, {lang: re.split('[,;]', iso_codes.ISO6392.get(
            alpha_2=lang).name)[0] for lang in LANGS}, cls.CONFIG, CONFIG_LANG)
        gui.add_mapped_submenu(cls.STRINGS.PIXABAY_MENU_TYPE, {type_: getattr(
            cls.STRINGS, f'PIXABAY_TYPE_{type_}') for type_ in TYPES}, cls.CONFIG, CONFIG_TYPE)
        gui.add_mapped_submenu(cls.STRINGS.PIXABAY_MENU_ORIENTATION, {orientation: getattr(
            cls.STRINGS, f'PIXABAY_ORIENTATION_{orientation}') for orientation in ORIENTATIONS},
                               cls.CONFIG, CONFIG_ORIENTATION)
        gui.add_mapped_submenu(cls.STRINGS.PIXABAY_MENU_CATEGORY, {category: getattr(
            cls.STRINGS, f'PIXABAY_CATEGORY_{category}') for category in CATEGORIES}, cls.CONFIG, CONFIG_CATEGORY)
        colors = cls.CONFIG[CONFIG_COLORS].split(',')
        menu_color = gui.add_submenu(cls.STRINGS.PIXABAY_MENU_COLORS).get_submenu()
        for color in COLORS:
            gui.add_menu_item(getattr(cls.STRINGS, f'PIXABAY_COLOR_{color}'), gui.MenuItemType.CHECK, color in colors,
                              uid=color, on_click=cls._on_color, args=(menu_color,), menu=menu_color)
        gui.add_separator(2, menu_color)
        cls._on_color(menu_color)
        gui.add_mapped_menu_item(cls.STRINGS.PIXABAY_LABEL_EDITOR, cls.CONFIG, CONFIG_EDITOR)
        gui.add_mapped_menu_item(cls.STRINGS.PIXABAY_LABEL_SAFE, cls.CONFIG, CONFIG_SAFE)
        gui.add_mapped_submenu(cls.STRINGS.PIXABAY_MENU_ORDER, {order: getattr(
            cls.STRINGS, f'PIXABAY_ORDER_{order}') for order in ORDERS}, cls.CONFIG, CONFIG_ORDER)

    @classmethod
    def _on_color(cls, menu: gui.Menu):
        cls.CONFIG[CONFIG_COLORS] = ','.join(
            color for color, item in gui.get_menu_items(menu).items() if item.is_checked())
