import functools
import sys
from typing import Generator, Optional

import gui
from libs import files, request
from . import Source

URL_BASE = 'https://api.unsplash.com'
URL_EDITORIAL = request.join(URL_BASE, 'photos')
URL_SEARCH = request.join(URL_BASE, 'search', 'photos')

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
    return bool(request.get(URL_EDITORIAL, params={CONFIG_ID: id_}))


class Unsplash(Source):  # https://unsplash.com/documentation
    VERSION = '0.0.2'
    URL = 'https://unsplash.com'
    ICON = 'png'
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
    def get_next_wallpaper(cls, **params) -> Generator[Optional[files.File], None, None]:
        results: Optional[list] = None
        total_pages = 1
        if params.pop(CONFIG_EDITORIAL):
            query_url = URL_EDITORIAL
            params = {
                CONFIG_ID: params[CONFIG_ID],
                CONFIG_ORDER: params[CONFIG_ORDER]}
        else:
            query_url = URL_SEARCH
        params['page'] = '1'
        params['per_page'] = '30'
        while True:
            if not results:
                params['page'] = str(int(params['page']) % total_pages + 1)
                response = request.get(query_url, params=params)
                if response:
                    json = response.get_json()
                    total_pages = sys.maxsize if cls.CURRENT_CONFIG[CONFIG_EDITORIAL] else int(json['total_pages'])
                    results = json if cls.CURRENT_CONFIG[CONFIG_EDITORIAL] else json['results']
            result = results.pop(0)
            yield files.File(result['request']['raw'], files.replace_ext(result['id'], 'jpg'))

    @classmethod
    def create_menu(cls):
        menu_order = gui.add_mapped_submenu(cls.strings.UNSPLASH_MENU_ORDER, {order: getattr(
            cls.strings, f'UNSPLASH_ORDER_{order}') for order in ORDERS + ORDERS_}, cls.CURRENT_CONFIG, CONFIG_ORDER).get_submenu()
        item_search = gui.add_submenu(cls.strings.UNSPLASH_MENU_SEARCH, not cls.CURRENT_CONFIG[CONFIG_EDITORIAL])
        gui.add_mapped_menu_item(cls.strings.UNSPLASH_LABEL_EDITORIAL, cls.CURRENT_CONFIG, CONFIG_EDITORIAL,
                                 on_click=functools.partial(cls._on_editorial, item_search, menu_order), position=0)
        cls._on_editorial(item_search, menu_order, cls.CURRENT_CONFIG[CONFIG_EDITORIAL])
        with gui.set_menu(item_search):
            gui.add_mapped_submenu(cls.strings.UNSPLASH_MENU_FILTER, {filter_: getattr(
                cls.strings, f'UNSPLASH_FILTER_{filter_}') for filter_ in FILTERS}, cls.CURRENT_CONFIG, CONFIG_FILTER)
            gui.add_mapped_submenu(cls.strings.UNSPLASH_MENU_COLOR, {color: getattr(
                cls.strings, f'UNSPLASH_COLOR_{color}') for color in COLORS}, cls.CURRENT_CONFIG, CONFIG_COLOR)
            gui.add_mapped_submenu(cls.strings.UNSPLASH_MENU_ORIENTATION, {orientation: getattr(
                cls.strings, f'UNSPLASH_ORIENTATION_{orientation}') for orientation in ORIENTATIONS}, cls.CURRENT_CONFIG, CONFIG_ORIENTATION)

    @classmethod
    def _fix_order(cls):
        cls.DEFAULT_CONFIG[CONFIG_ORDER] = ORDERS[0] if cls.CURRENT_CONFIG[CONFIG_EDITORIAL] else ORDERS_[1]
        cls._fix_config(CONFIG_ORDER, ORDERS if cls.CURRENT_CONFIG[CONFIG_EDITORIAL] else ORDERS_)

    @classmethod
    def _on_editorial(cls, item_search: gui.MenuItem, menu_order: gui.Menu, editorial: bool):
        item_search.enable(not editorial)
        cls._fix_order()
        for order, item in gui.get_menu_items(menu_order).items():
            item.check(cls.CURRENT_CONFIG[CONFIG_ORDER] == order)
            item.enable(order in (ORDERS if editorial else ORDERS_))
