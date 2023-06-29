import os
import re
from typing import Iterator, Optional, TypedDict

import gui
import validator
from libs import isocodes, request
from . import ImageFile, Source

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

_CONTENT_END = b'[ERROR 400] "page" is out of valid range.'


def _authenticate(key: str) -> bool:
    return bool(request.get(URL_BASE, {CONFIG_KEY: key, 'per_page': '3'}))


class Pixabay(Source):  # https://pixabay.com/api/docs
    NAME = '# pixabay [recaptcha]'
    URL = 'https://pixabay.com'
    ICON = 'png'
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_KEY: str,
        'q': str,
        CONFIG_LANG: str,
        CONFIG_TYPE: str,
        CONFIG_ORIENTATION: str,
        CONFIG_CATEGORY: str,
        CONFIG_COLORS: list[str],
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
        CONFIG_COLORS: [],
        CONFIG_EDITOR: False,
        CONFIG_SAFE: False,
        CONFIG_ORDER: ORDERS[0]}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_contains, CONFIG_LANG, LANGS)
        cls._fix_config(validator.ensure_contains, CONFIG_TYPE, TYPES)
        cls._fix_config(validator.ensure_contains, CONFIG_ORIENTATION, ORIENTATIONS)
        cls._fix_config(validator.ensure_contains, CONFIG_CATEGORY, CATEGORIES)
        cls._fix_config(validator.ensure_subset, CONFIG_COLORS, COLORS)
        cls._fix_config(validator.ensure_contains, CONFIG_ORDER, ORDERS)

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
        menu_color = gui.add_submenu_check(cls._text('MENU_COLORS'), {color: cls._text(
            f'COLOR_{color}') for color in COLORS}, (None, None), cls.CURRENT_CONFIG, CONFIG_COLORS).get_submenu()
        gui.add_separator(2, menu_color)
        gui.add_menu_item_check(cls._text('LABEL_EDITOR'), cls.CURRENT_CONFIG, CONFIG_EDITOR)
        gui.add_menu_item_check(cls._text('LABEL_SAFE'), cls.CURRENT_CONFIG, CONFIG_SAFE)
        gui.add_submenu_radio(cls._text('MENU_ORDER'), {order: cls._text(
            f'ORDER_{order}') for order in ORDERS}, cls.CURRENT_CONFIG, CONFIG_ORDER)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        hits = []
        params[CONFIG_COLORS] = ','.join(params[CONFIG_COLORS])
        params[CONFIG_EDITOR] = str(params[CONFIG_EDITOR]).lower()
        params[CONFIG_SAFE] = str(params[CONFIG_SAFE]).lower()
        page = 1
        while True:
            if not hits:
                params['page'] = str(page)
                response = request.get(URL_BASE, params)
                if (page != 1 and response.status_code == request.Status.BAD_REQUEST
                        and response.content == _CONTENT_END):
                    page = 1
                    continue
                if response:
                    hits = response.json()['hits']
                    page += 1
                if not hits:
                    yield
                    return
            hit = hits.pop(0)
            name = os.path.basename(hit['previewURL'])
            yield ImageFile(hit['largeImageURL'], name[:name.rfind('_')] +
                            name[name.rfind('.'):], url=hit[
                'pageURL'], width=hit['imageWidth'], height=hit['imageHeight'])
