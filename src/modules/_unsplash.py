__version__ = '0.0.2'  # https://unsplash.com/documentation

import sys
from typing import Generator, Optional, Union

from libs import files, gui, request
from .module import _Module

BASE_URL = 'https://api.unsplash.com'
EDITORIAL_URL = request.join(BASE_URL, 'photos')
SEARCH_URL = request.join(BASE_URL, 'search', 'photos')

CONFIG_ID = 'client_id'
CONFIG_EDITORIAL = 'editorial'
CONFIG_ORDER = 'order_by'
CONFIG_FILTER = 'content_filter'
CONFIG_COLOR = 'color'
CONFIG_ORIENTATION = 'orientation'

ORDERS = 'latest', 'oldest', 'popular'
ORDERS_ = 'latest', 'relevant'
FILTERS = 'low', 'high'
COLORS = '', 'black_and_white', 'black', 'white', 'yellow', 'orange', 'red', 'purple', 'magenta', 'green', 'teal', 'blue'
ORIENTATIONS = '', 'landscape', 'portrait', 'squarish'


def _authenticate(id_: str) -> bool:
    return bool(request.open(EDITORIAL_URL, {CONFIG_ID: id_}))


class Unsplash(_Module):
    ICON = 'Unsplash.png'
    DEFAULT_CONFIG = {
        CONFIG_ID: '',
        CONFIG_EDITORIAL: True,
        'query': '',
        CONFIG_ORDER: '',
        'collections': '',
        CONFIG_FILTER: FILTERS[0],
        CONFIG_COLOR: COLORS[0],
        CONFIG_ORIENTATION: ORIENTATIONS[0]}

    @classmethod
    def fix_config(cls):
        cls._fix_order()
        cls._fix_config(CONFIG_FILTER, FILTERS)
        cls._fix_config(CONFIG_COLOR, COLORS)
        cls._fix_config(CONFIG_ORIENTATION, ORIENTATIONS)

    @classmethod
    def get_next_wallpaper(cls, **params: Union[bool, str]) -> Generator[Optional[files.File], None, None]:
        results: Optional[list] = None
        total_pages = 1
        if params.pop(CONFIG_EDITORIAL):
            query_url = EDITORIAL_URL
            params = {
                CONFIG_ID: params[CONFIG_ID],
                CONFIG_ORDER: params[CONFIG_ORDER]}
        else:
            query_url = SEARCH_URL
        params['page'] = '1'
        params['per_page'] = '30'
        while True:
            if not results:
                params['page'] = str(int(params['page']) % total_pages + 1)
                response = request.open(query_url, params)
                if response:
                    json = response.get_json()
                    total_pages = sys.maxsize if cls.CONFIG[CONFIG_EDITORIAL] else int(json['total_pages'])
                    results = json if cls.CONFIG[CONFIG_EDITORIAL] else json['results']
            result = results.pop(0)
            yield files.File(result['urls']['raw'], files.replace_ext(result['id'], 'jpg'))

    @classmethod
    def create_menu(cls):
        menu_order = gui.add_mapped_submenu(cls.STRINGS.UNSPLASH_MENU_ORDER, {order: getattr(
            cls.STRINGS, f'UNSPLASH_ORDER_{order}') for order in ORDERS + ORDERS_}, cls.CONFIG, CONFIG_ORDER)
        menu_search = gui.add_submenu(cls.STRINGS.UNSPLASH_MENU_SEARCH, not cls.CONFIG[CONFIG_EDITORIAL])
        gui.add_mapped_menu_item(cls.STRINGS.UNSPLASH_LABEL_EDITORIAL, cls.CONFIG, CONFIG_EDITORIAL,
                                 on_click=cls._on_editorial, args=(menu_search, menu_order), position=0)
        cls._on_editorial(cls.CONFIG[CONFIG_EDITORIAL], menu_search, menu_order)
        with gui.set_main_menu(menu_search):
            gui.add_mapped_submenu(cls.STRINGS.UNSPLASH_MENU_FILTER, {filter_: getattr(
                cls.STRINGS, f'UNSPLASH_FILTER_{filter_}') for filter_ in FILTERS}, cls.CONFIG, CONFIG_FILTER)
            gui.add_mapped_submenu(cls.STRINGS.UNSPLASH_MENU_COLOR, {color: getattr(
                cls.STRINGS, f'UNSPLASH_COLOR_{color}') for color in COLORS}, cls.CONFIG, CONFIG_COLOR)
            gui.add_mapped_submenu(cls.STRINGS.UNSPLASH_MENU_ORIENTATION, {orientation: getattr(
                cls.STRINGS, f'UNSPLASH_ORIENTATION_{orientation}') for orientation in ORIENTATIONS}, cls.CONFIG, CONFIG_ORIENTATION)

    @classmethod
    def _fix_order(cls):
        if cls.CONFIG[CONFIG_ORDER] not in (ORDERS if cls.CONFIG[CONFIG_EDITORIAL] else ORDERS_):
            cls.CONFIG[CONFIG_ORDER] = ORDERS[0] if cls.CONFIG[CONFIG_EDITORIAL] else ORDERS_[1]

    @classmethod
    def _on_editorial(cls, editorial: bool, menu_search, menu_order):
        menu_search.Enable(not editorial)
        cls._fix_order()
        for order, item in gui.get_menu_items(menu_order).items():
            item.Check(cls.CONFIG[CONFIG_ORDER] == order)
            item.Enable(order in (ORDERS if editorial else ORDERS_))
