import functools
import sys
from typing import Callable, ItemsView, Iterator, Optional, TypedDict

import gui
import validator
from libs import files, request
from . import File, Source

URL_BASE = 'https://api.unsplash.com'
URL_EDITORIAL = request.join_url(URL_BASE, 'photos')
URL_SEARCH = request.join_url(URL_BASE, 'search', 'photos')

CONFIG_ID = 'client_id'
CONFIG_EDITORIAL = 'editorial'
CONFIG_ORDER = 'order_by'
CONFIG_FILTER = 'content_filter'
CONFIG_COLOR = 'color'
CONFIG_ORIENTATION = 'orientation'

ORDERS = 'latest', 'oldest', 'popular'
ORDERS_ = 'latest', 'relevant'
FILTERS = 'low', 'high'
COLORS = ('', 'black_and_white', 'black', 'white', 'yellow', 'orange',
          'red', 'purple', 'magenta', 'green', 'teal', 'blue')
ORIENTATIONS = '', 'landscape', 'portrait', 'squarish'


def _authenticate(id_: str) -> bool:
    return bool(request.get(URL_EDITORIAL, {CONFIG_ID: id_}))


class Unsplash(Source):  # https://unsplash.com/documentation
    VERSION = '0.0.2'
    ICON = 'png'
    URL = 'https://unsplash.com'
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_ID: str,
        CONFIG_EDITORIAL: bool,
        'query': str,
        CONFIG_ORDER: str,
        'collections': str,
        CONFIG_FILTER: str,
        CONFIG_COLOR: str,
        CONFIG_ORIENTATION: str})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_ID: '',
        CONFIG_EDITORIAL: True,
        'query': '',
        CONFIG_ORDER: '',
        'collections': '',
        CONFIG_FILTER: FILTERS[0],
        CONFIG_COLOR: COLORS[0],
        CONFIG_ORIENTATION: ORIENTATIONS[0]}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_iterable, CONFIG_FILTER, FILTERS)
        cls._fix_config(validator.ensure_iterable, CONFIG_COLOR, COLORS)
        cls._fix_config(validator.ensure_iterable, CONFIG_ORIENTATION, ORIENTATIONS)
        cls._fix_order()

    @classmethod
    def create_menu(cls):
        items_order = gui.get_menu_items(gui.add_submenu_radio(cls._text(
            'MENU_ORDER'), {order: cls._text(f'ORDER_{order}')
                            for order in ORDERS + ORDERS_}, cls.CURRENT_CONFIG, CONFIG_ORDER)).items()
        item_search = gui.add_submenu(cls._text('MENU_SEARCH'), not cls.CURRENT_CONFIG[CONFIG_EDITORIAL])
        gui.add_menu_item_check(cls._text('LABEL_EDITORIAL'), cls.CURRENT_CONFIG, CONFIG_EDITORIAL,
                                on_click=functools.partial(cls._on_editorial, item_search.enable, items_order), position=0)
        cls._on_editorial(item_search.enable, items_order, cls.CURRENT_CONFIG[CONFIG_EDITORIAL])
        with gui.set_menu(item_search):
            gui.add_submenu_radio(cls._text('MENU_FILTER'), {
                filter_: cls._text(f'UNSPLASH_FILTER_{filter_}')
                for filter_ in FILTERS}, cls.CURRENT_CONFIG, CONFIG_FILTER)
            gui.add_submenu_radio(cls._text('MENU_COLOR'), {
                color: cls._text(f'UNSPLASH_COLOR_{color}')
                for color in COLORS}, cls.CURRENT_CONFIG, CONFIG_COLOR)
            gui.add_submenu_radio(cls._text('MENU_ORIENTATION'), {
                orientation: cls._text(f'UNSPLASH_ORIENTATION_{orientation}')
                for orientation in ORIENTATIONS}, cls.CURRENT_CONFIG, CONFIG_ORIENTATION)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[File]]:
        results: Optional[list] = None
        if params.pop(CONFIG_EDITORIAL):
            url = URL_EDITORIAL
            params = {
                CONFIG_ID: params[CONFIG_ID],
                CONFIG_ORDER: params[CONFIG_ORDER]}
        else:
            url = URL_SEARCH
        params['page'] = '1'
        params['per_page'] = '30'
        while True:
            if not results:
                response = request.get(url, params)
                if response:
                    json = response.json()
                    results = json if cls.CURRENT_CONFIG[CONFIG_EDITORIAL] else json['results']
                    params['page'] = str(int(params['page']) % (sys.maxsize if cls.CURRENT_CONFIG[
                        CONFIG_EDITORIAL] else int(json['total_pages'])) + 1)
                if not results:
                    yield
                    continue
            result = results.pop(0)
            yield File(result['urls']['raw'], files.replace_ext(
                result['id'], 'jpg'), url=result['links']['html'])

    @classmethod
    def _fix_order(cls):
        cls.DEFAULT_CONFIG[CONFIG_ORDER] = ORDERS[0] if cls.CURRENT_CONFIG[CONFIG_EDITORIAL] else ORDERS_[1]
        cls._fix_config(validator.ensure_iterable, CONFIG_ORDER, ORDERS if cls.CURRENT_CONFIG[CONFIG_EDITORIAL] else ORDERS_)

    @classmethod
    def _on_editorial(cls, enable: Callable[[bool], bool],
                      items: ItemsView[str, gui.MenuItem], editorial: bool):
        enable(not editorial)
        cls._fix_order()
        for order, item in items:
            item.check(cls.CURRENT_CONFIG[CONFIG_ORDER] == order)
            item.enable(order in (ORDERS if editorial else ORDERS_))
