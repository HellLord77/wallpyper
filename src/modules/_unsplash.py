__version__ = '0.0.1'  # https://unsplash.com/documentation

from typing import Generator, Optional

from libs import files, gui, request
from .module import _Module

BASE_URL = 'https://api.unsplash.com'
EDITORIAL_URL = request.join(BASE_URL, 'photos')
SEARCH_URL = request.join(BASE_URL, 'search', 'photos')

CONFIG_ID = 'client_id'
CONFIG_ORDER = 'order_by'
CONFIG_FILTER = 'content_filter'
CONFIG_COLOR = 'color'
CONFIG_ORIENTATION = 'orientation'

ORDERS = 'latest', 'relevant'
FILTERS = 'low', 'high'
COLORS = '', 'black_and_white', 'black', 'white', 'yellow', 'orange', 'red', 'purple', 'magenta', 'green', 'teal', 'blue'
ORIENTATIONS = '', 'landscape', 'portrait', 'squarish'


def _authenticate(id_: str) -> bool:
    return bool(request.open(EDITORIAL_URL, {CONFIG_ID: id_}))


class Unsplash(_Module):
    DEFAULT_CONFIG = {
        CONFIG_ID: '',
        'query': '',
        CONFIG_ORDER: ORDERS[1],
        'collections': '',
        CONFIG_FILTER: FILTERS[0],
        CONFIG_COLOR: COLORS[0],
        CONFIG_ORIENTATION: ORIENTATIONS[0]}

    @classmethod
    def fix_config(cls):
        cls._fix_config(CONFIG_ORDER, ORDERS)
        cls._fix_config(CONFIG_FILTER, FILTERS)
        cls._fix_config(CONFIG_COLOR, COLORS)
        cls._fix_config(CONFIG_ORIENTATION, ORIENTATIONS)

    @classmethod
    def get_next_wallpaper(cls, **params: str) -> Generator[Optional[files.File], None, None]:
        results: Optional[list] = None
        total_pages = 1
        params['page'] = '1'
        params['per_page'] = '30'
        while True:
            if not results:
                params['page'] = str(int(params['page']) % total_pages + 1)
                response = request.open(SEARCH_URL, params)
                if response:
                    json = response.get_json()
                    total_pages = int(json['total_pages'])
                    results = json['results']
            result = results.pop(0)
            yield files.File(result['urls']['raw'], files.replace_ext(result['id'], 'jpg'))

    @classmethod
    def create_menu(cls):
        gui.add_mapped_submenu(cls.STRINGS.UNSPLASH_MENU_ORDER, {order: getattr(
            cls.STRINGS, f'UNSPLASH_ORDER_{order}') for order in ORDERS}, cls.CONFIG, CONFIG_ORDER)
        gui.add_mapped_submenu(cls.STRINGS.UNSPLASH_MENU_FILTER, {filter_: getattr(
            cls.STRINGS, f'UNSPLASH_FILTER_{filter_}') for filter_ in FILTERS}, cls.CONFIG, CONFIG_FILTER)
        gui.add_mapped_submenu(cls.STRINGS.UNSPLASH_MENU_COLOR, {color: getattr(
            cls.STRINGS, f'UNSPLASH_COLOR_{color}') for color in COLORS}, cls.CONFIG, CONFIG_COLOR)
        gui.add_mapped_submenu(cls.STRINGS.UNSPLASH_MENU_ORIENTATION, {orientation: getattr(
            cls.STRINGS, f'UNSPLASH_ORIENTATION_{orientation}') for orientation in ORIENTATIONS}, cls.CONFIG, CONFIG_ORIENTATION)
