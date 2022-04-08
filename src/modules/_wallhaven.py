__version__ = '0.0.2'  # https://wallhaven.cc/help/api

import os.path
import re
from typing import Callable, Generator, Optional

import utils
from langs import STRINGS
from libs import files, gui, misc, request
from .module import _Module

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


def _authenticate(key: str) -> bool:
    return bool(response := request.open(SETTINGS_URL, {'apikey': key})) and 'error' not in response.get_json()


class Wallhaven(_Module):
    NAME = 'Wallhaven'
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

    @classmethod
    def fix_config(cls):
        if not CATEGORIES_PURITIES.fullmatch(cls.CONFIG[CONFIG_CATEGORY]):
            cls.CONFIG[CONFIG_CATEGORY] = cls.DEFAULT_CONFIG[CONFIG_CATEGORY]
        if not cls.CONFIG[CONFIG_KEY]:
            cls.CONFIG[CONFIG_PURITY] = f'{cls.CONFIG[CONFIG_PURITY][:2]}0'
        if not CATEGORIES_PURITIES.fullmatch(cls.CONFIG[CONFIG_PURITY]):
            cls.CONFIG[CONFIG_PURITY] = cls.DEFAULT_CONFIG[CONFIG_PURITY]
        cls._fix_config(CONFIG_SORTING, SORTINGS)
        cls._fix_config(CONFIG_ORDER, ORDERS)
        cls._fix_config(CONFIG_RANGE, RANGES)

    @classmethod
    @misc.one_cache
    def get_next_wallpaper(cls, **params: str) -> Generator[Optional[files.File], None, None]:
        datas: Optional[list] = None
        meta = {
            'current_page': 1,
            'last_page': 1,
            'seed': None
        }
        while True:
            if not datas:
                params['page'] = str(meta['current_page'] % meta['last_page'] + 1)
                params['seed'] = meta['seed'] or ''
                response = request.open(SEARCH_URl, params)
                if response:
                    json = response.get_json()
                    datas = json['data']
                    meta = json['meta']
                if not datas:
                    yield
                    continue
            data = datas.pop(0)
            url = data['path']
            yield files.File(url, os.path.basename(url), data['file_size'])

    @classmethod
    def create_menu(cls):
        menu_category = utils.add_menu(STRINGS.WALLHAVEN_MENU_CATEGORY)
        for index, category in enumerate(CATEGORIES):
            utils.add_item(getattr(STRINGS, f'WALLHAVEN_CATEGORY_{category}'),
                           utils.item.CHECK, cls.CONFIG[CONFIG_CATEGORY][index] == '1', uid=category,
                           on_click=cls._on_category, args=(menu_category,), menu=menu_category)
        cls._on_category(menu_category)
        menu_purity = utils.add_menu(STRINGS.WALLHAVEN_MENU_PURITY)
        for index, purity in enumerate(PURITIES):
            utils.add_item(getattr(STRINGS, f'WALLHAVEN_PURITY_{purity}'),
                           utils.item.CHECK, cls.CONFIG[CONFIG_PURITY][index] == '1', uid=purity,
                           on_click=cls._on_purity, args=(menu_purity,), menu=menu_purity)
        cls._on_purity(menu_purity)
        menu_sorting = utils.add_menu(STRINGS.WALLHAVEN_MENU_SORTING)
        utils.add_synced_items(STRINGS.WALLHAVEN_MENU_ORDER, {order: getattr(
            STRINGS, f'WALLHAVEN_ORDER_{order}') for order in ORDERS}, cls.CONFIG, CONFIG_ORDER)
        menu_range = utils.add_synced_items(STRINGS.WALLHAVEN_MENU_RANGE, {range_: getattr(
            STRINGS, f'WALLHAVEN_RANGE_{range_}') for range_ in RANGES}, cls.CONFIG, CONFIG_RANGE)
        utils.add_synced_items(menu_sorting, {sorting: getattr(
            STRINGS, f'WALLHAVEN_SORTING_{sorting}') for sorting in SORTINGS}, cls.CONFIG, CONFIG_SORTING,
                               on_click=cls._on_sorting, args=(menu_range.Enable,))
        cls._on_sorting(None, menu_range.Enable)

    @classmethod
    def _on_category(cls, menu):
        cls.CONFIG[CONFIG_CATEGORY] = ''.join(str(int(item.IsChecked())) for item in gui.get_menu_items(menu).values())
        disable = cls.CONFIG[CONFIG_CATEGORY].count('1') == 1
        for item in gui.get_menu_items(menu).values():
            item.Enable(not disable or not item.IsChecked())

    @classmethod
    def _on_purity(cls, menu):
        cls.CONFIG[CONFIG_PURITY] = ''.join(str(int(item.IsChecked())) for item in gui.get_menu_items(menu).values())
        disable = cls.CONFIG[CONFIG_PURITY].count('1') == 1
        for index, item in enumerate(gui.get_menu_items(menu).values()):
            item.Enable((not disable or not item.IsChecked()) and (index != 2 or bool(cls.CONFIG[CONFIG_KEY])))

    @classmethod
    def _on_sorting(cls, _, enable: Callable):
        enable(cls.CONFIG[CONFIG_SORTING] == SORTINGS[5])
