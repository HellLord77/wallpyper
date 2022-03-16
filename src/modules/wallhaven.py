__version__ = '0.0.2'  # https://wallhaven.cc/help/api

import os.path
import re
from typing import Callable, Generator, Optional

import libs.files as files
import libs.gui as gui
import libs.misc as misc
import libs.request as request
import utils
from langs import LANGUAGE as STRINGS

NAME = 'wallhaven'
BASE_URL = request.join('https://wallhaven.cc', 'api', 'v1')
SEARCH_URl = request.join(BASE_URL, 'search')
SETTINGS_URL = request.join(BASE_URL, 'settings')

CONFIG_KEY = 'apikey'
CONFIG_CATEGORY = 'categories'
CONFIG_PURITY = 'purity'
CONFIG_SORTING = 'sorting'
CONFIG_ORDER = 'order'
CONFIG_RANGE = 'topRange'

CATEGORIES = 'general', 'anime', 'people'
PURITIES = 'sfw', 'sketchy', 'nsfw'
SORTINGS = 'date_added', 'relevance', 'random', 'views', 'favorites', 'toplist', 'hot'
ORDERS = 'desc', 'asc'
RANGES = '1d', '3d', '1w', '1M', '3M', '6M', '1y'
CATEGORIES_PURITIES = re.compile('(?!000)[01]{3}')

DEFAULT_CONFIG = {
    CONFIG_KEY: '',
    'q': '',
    CONFIG_CATEGORY: '111',
    CONFIG_PURITY: '100',
    CONFIG_SORTING: SORTINGS[0],
    CONFIG_ORDER: ORDERS[0],
    CONFIG_RANGE: RANGES[3],
    'atleast': '',
    'resolutions': '',
    'ratios': '',
    'colors': ''}
CONFIG = {}


def fix_config():
    if not CATEGORIES_PURITIES.fullmatch(CONFIG[CONFIG_CATEGORY]):
        CONFIG[CONFIG_CATEGORY] = DEFAULT_CONFIG[CONFIG_CATEGORY]
    if not CONFIG[CONFIG_KEY]:
        CONFIG[CONFIG_PURITY] = f'{CONFIG[CONFIG_PURITY][:2]}0'
    if not CATEGORIES_PURITIES.fullmatch(CONFIG[CONFIG_PURITY]):
        CONFIG[CONFIG_PURITY] = DEFAULT_CONFIG[CONFIG_PURITY]
    if CONFIG[CONFIG_SORTING] not in SORTINGS:
        CONFIG[CONFIG_SORTING] = DEFAULT_CONFIG[CONFIG_SORTING]
    if CONFIG[CONFIG_ORDER] not in ORDERS:
        CONFIG[CONFIG_ORDER] = DEFAULT_CONFIG[CONFIG_ORDER]
    if CONFIG[CONFIG_RANGE] not in RANGES:
        CONFIG[CONFIG_RANGE] = DEFAULT_CONFIG[CONFIG_RANGE]


@misc.one_cache
def get_next_wallpaper(**params: str) -> Generator[Optional[files.File], None, None]:
    search_datas: Optional[list] = None
    meta = {
        'current_page': 1,
        'last_page': 1,
        'seed': None
    }
    while True:
        if not search_datas:
            params['page'] = str(meta['current_page'] % meta['last_page'] + 1)
            params['seed'] = meta['seed'] or ''
            response = request.open(SEARCH_URl, params)
            if response:
                search_datas, meta = response.get_json().values()
            if not search_datas:
                yield
                continue
        search_data = search_datas.pop(0)
        url = search_data['path']
        yield files.File(url, os.path.basename(url), search_data['file_size'])


def _authenticate(api_key: str) -> bool:
    return bool(response := request.open(SETTINGS_URL, {'apikey': api_key})) and 'error' not in response.get_json()


def on_category(menu):
    CONFIG[CONFIG_CATEGORY] = ''.join(str(int(item.IsChecked())) for item in gui.get_menu_items(menu).values())
    disable = CONFIG[CONFIG_CATEGORY].count('1') == 1
    for item in gui.get_menu_items(menu).values():
        item.Enable(not disable or not item.IsChecked())


def on_purity(menu):
    CONFIG[CONFIG_PURITY] = ''.join(str(int(item.IsChecked())) for item in gui.get_menu_items(menu).values())
    disable = CONFIG[CONFIG_PURITY].count('1') == 1
    for index, item in enumerate(gui.get_menu_items(menu).values()):
        item.Enable((not disable or not item.IsChecked()) and (index != 2 or bool(CONFIG[CONFIG_KEY])))


def on_sorting(_, enable: Callable):
    enable(CONFIG[CONFIG_SORTING] == SORTINGS[5])


def create_menu():
    menu_category = utils.add_menu(STRINGS.WALLHAVEN_MENU_CATEGORY)
    for index, category in enumerate(CATEGORIES):
        utils.add_item(getattr(STRINGS, f'WALLHAVEN_CATEGORY_{category}'),
                       utils.item.CHECK, CONFIG[CONFIG_CATEGORY][index] == '1', uid=category,
                       on_click=on_category, args=(menu_category,), menu=menu_category)
    on_category(menu_category)
    menu_purity = utils.add_menu(STRINGS.WALLHAVEN_MENU_PURITY)
    for index, purity in enumerate(PURITIES):
        utils.add_item(getattr(STRINGS, f'WALLHAVEN_PURITY_{purity}'),
                       utils.item.CHECK, CONFIG[CONFIG_PURITY][index] == '1', uid=purity,
                       on_click=on_purity, args=(menu_purity,), menu=menu_purity)
    on_purity(menu_purity)
    menu_sorting = utils.add_menu(STRINGS.WALLHAVEN_MENU_SORTING)
    utils.add_synced_items(STRINGS.WALLHAVEN_MENU_ORDER, {order: getattr(
        STRINGS, f'WALLHAVEN_ORDER_{order}') for order in ORDERS}, CONFIG, CONFIG_ORDER)
    menu_range = utils.add_synced_items(STRINGS.WALLHAVEN_MENU_RANGE, {range_: getattr(
        STRINGS, f'WALLHAVEN_RANGE_{range_}') for range_ in RANGES}, CONFIG, CONFIG_RANGE,
                                        CONFIG[CONFIG_SORTING] == SORTINGS[5])
    utils.add_synced_items(menu_sorting, {sorting: getattr(
        STRINGS, f'WALLHAVEN_SORTING_{sorting}') for sorting in SORTINGS}, CONFIG, CONFIG_SORTING, on_click=on_sorting,
                           args=(menu_range.Enable,))
