__version__ = '0.0.2'  # https://wallhaven.cc/help/api

import os.path
import re
from typing import Callable, Generator, Optional

from libs import colors, files, gui, request
from .module import _Module

BASE_URL = request.join('https://wallhaven.cc', 'api', 'v1')
SEARCH_URl = request.join(BASE_URL, 'search')
SETTINGS_URL = request.join(BASE_URL, 'settings')

CONFIG_KEY = 'apikey'
CONFIG_CATEGORY = 'categories'
CONFIG_PURITY = 'purity'
CONFIG_SORTING = 'sorting'
CONFIG_ORDER = 'order'
CONFIG_RANGE = 'topRange'
CONFIG_RATIO = 'ratios'
CONFIG_COLORS = 'colors'

CATEGORIES = 'general', 'anime', 'people'
PURITIES = 'sfw', 'sketchy', 'nsfw'
SORTINGS = 'date_added', 'relevance', 'random', 'views', 'favorites', 'toplist', 'hot'
ORDERS = 'desc', 'asc'
RANGES = '1d', '3d', '1w', '1M', '3M', '6M', '1y'
RATIOS = (
    'landscape', '16x9', '16x10', '21x9', '32x9', '48x9',
    'portrait', '9x16', '10x16', '9x18', '1x1', '3x2', '4x3', '5x4')
COLORS = (
    '', '660000', '990000', 'cc0000', 'cc3333', 'ea4c88', '993399', '663399', '333399', '0066cc',
    '0099cc', '66cccc', '77cc33', '669900', '336600', '666600', '999900', 'cccc33', 'ffff00', 'ffcc33',
    'ff9900', 'ff6600', 'cc6633', '996633', '663300', '000000', '999999', 'cccccc', 'ffffff', '424153')
CATEGORIES_PURITIES = re.compile('(?!000)[01]{3}')


def _authenticate(key: str) -> bool:
    return bool(response := request.open(SETTINGS_URL, {'apikey': key})) and 'error' not in response.get_json()


class Wallhaven(_Module):
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
        CONFIG_RATIO: f'{RATIOS[0]},{RATIOS[6]}',
        CONFIG_COLORS: COLORS[0]}

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
        for ratio in cls.CONFIG[CONFIG_RATIO].split(','):
            if ratio not in RATIOS:
                cls.CONFIG[CONFIG_RATIO] = cls.DEFAULT_CONFIG[CONFIG_RATIO]
                break
        cls._fix_config(CONFIG_COLORS, COLORS)

    @classmethod
    def get_next_wallpaper(cls, **params: str) -> Generator[Optional[files.File], None, None]:
        datas: Optional[list] = None
        meta = {
            'current_page': 1,
            'last_page': 1,
            'seed': None}
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
        menu_category = gui.add_submenu(cls.STRINGS.WALLHAVEN_MENU_CATEGORY)
        for index, category in enumerate(CATEGORIES):
            gui.add_menu_item(getattr(cls.STRINGS, f'WALLHAVEN_CATEGORY_{category}'),
                              gui.Item.CHECK, cls.CONFIG[CONFIG_CATEGORY][index] == '1', uid=category,
                              on_click=cls._on_category, args=(menu_category,), menu=menu_category)
        cls._on_category(menu_category)
        menu_purity = gui.add_submenu(cls.STRINGS.WALLHAVEN_MENU_PURITY)
        for index, purity in enumerate(PURITIES):
            gui.add_menu_item(getattr(cls.STRINGS, f'WALLHAVEN_PURITY_{purity}'),
                              gui.Item.CHECK, cls.CONFIG[CONFIG_PURITY][index] == '1', uid=purity,
                              on_click=cls._on_purity, args=(menu_purity,), menu=menu_purity)
        cls._on_purity(menu_purity)
        menu_sorting = gui.add_submenu(cls.STRINGS.WALLHAVEN_MENU_SORTING)
        gui.add_mapped_submenu(cls.STRINGS.WALLHAVEN_MENU_ORDER, {order: getattr(
            cls.STRINGS, f'WALLHAVEN_ORDER_{order}') for order in ORDERS}, cls.CONFIG, CONFIG_ORDER)
        menu_range = gui.add_mapped_submenu(cls.STRINGS.WALLHAVEN_MENU_RANGE, {range_: getattr(
            cls.STRINGS, f'WALLHAVEN_RANGE_{range_}') for range_ in RANGES}, cls.CONFIG, CONFIG_RANGE)
        gui.add_mapped_submenu(menu_sorting, {sorting: getattr(
            cls.STRINGS, f'WALLHAVEN_SORTING_{sorting}') for sorting in SORTINGS}, cls.CONFIG, CONFIG_SORTING,
                               on_click=cls._on_sorting, args=(menu_range.Enable,))
        cls._on_sorting(None, menu_range.Enable)
        ratios = cls.CONFIG[CONFIG_RATIO].split(',')
        menu_ratio = gui.add_submenu(cls.STRINGS.WALLHAVEN_MENU_RATIO)
        for ratio in RATIOS:
            gui.add_menu_item(getattr(cls.STRINGS, f'WALLHAVEN_RATIO_{ratio}'), gui.Item.CHECK, ratio in ratios,
                              uid=ratio, on_click=cls._on_ratio, args=(menu_ratio,), menu=menu_ratio)
        gui.add_separator(6, menu_ratio)
        gui.add_mapped_submenu(cls.STRINGS.WALLHAVEN_MENU_COLOR, {color: colors.get_name(
            color) if color else cls.STRINGS.WALLHAVEN_COLOR_ for color in COLORS}, cls.CONFIG, CONFIG_COLORS)

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
    def _on_ratio(cls, menu):
        ratios = []
        for ratio, item in gui.get_menu_items(menu).items():
            item.Enable()
            if item.IsChecked():
                ratios.append(ratio)
        if len(ratios) == 1:
            gui.get_menu_item_by_uid(ratios[0], menu=menu).Enable(False)
        cls.CONFIG[CONFIG_RATIO] = ','.join(ratios)

    @classmethod
    def _on_sorting(cls, _, enable: Callable):
        enable(cls.CONFIG[CONFIG_SORTING] == SORTINGS[5])
