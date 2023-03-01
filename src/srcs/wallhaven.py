import colorsys
import functools
import os.path
import re
from typing import Callable, Generator, Optional

import gui
import win32
from libs import colornames, files, request
from . import Source

_COLOR_TEMPLATE = 'CMYK: {}\nHSV: {}\nHSL: {}'

URL_BASE = request.join('https://wallhaven.cc', 'api', 'v1')
URL_SEARCH = request.join(URL_BASE, 'search')
URL_SETTINGS = request.join(URL_BASE, 'settings')

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


def on_color_right(_: int, item_color: gui.MenuItem):
    win32.clipboard.copy_text(f'#{item_color.get_uid().upper()}')


def _authenticate(key: str) -> bool:
    return bool(response := request.get(URL_SETTINGS, params={'apikey': key})) and 'error' not in response.get_json()


class Wallhaven(Source):  # https://wallhaven.cc/help/api
    NAME = 'wallhaven'
    VERSION = '0.0.4'
    URL = 'https://wallhaven.cc'
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
        if not CATEGORIES_PURITIES.fullmatch(cls.CURRENT_CONFIG[CONFIG_CATEGORY]):
            cls.CURRENT_CONFIG[CONFIG_CATEGORY] = cls.DEFAULT_CONFIG[CONFIG_CATEGORY]
        if not cls.CURRENT_CONFIG[CONFIG_KEY]:
            cls.CURRENT_CONFIG[CONFIG_PURITY] = f'{cls.CURRENT_CONFIG[CONFIG_PURITY][:2]}0'
        if not CATEGORIES_PURITIES.fullmatch(cls.CURRENT_CONFIG[CONFIG_PURITY]):
            cls.CURRENT_CONFIG[CONFIG_PURITY] = cls.DEFAULT_CONFIG[CONFIG_PURITY]
        cls._fix_config(CONFIG_SORTING, SORTINGS)
        cls._fix_config(CONFIG_ORDER, ORDERS)
        cls._fix_config(CONFIG_RANGE, RANGES)
        for ratio in cls.CURRENT_CONFIG[CONFIG_RATIO].split(','):
            if ratio not in RATIOS:
                cls.CURRENT_CONFIG[CONFIG_RATIO] = cls.DEFAULT_CONFIG[CONFIG_RATIO]
                break
        cls._fix_config(CONFIG_COLORS, COLORS)

    @classmethod
    def get_next_wallpaper(cls, **params: str) -> Generator[Optional[files.File], None, None]:
        datas: Optional[list] = None
        meta: dict[str, Optional[int | str]] = {
            'current_page': 1,
            'last_page': 1,
            'seed': None}
        while True:
            if not datas:
                params['page'] = str(meta['current_page'] % meta['last_page'] + 1)
                params['seed'] = meta['seed'] or ''
                response = request.get(URL_SEARCH, params=params)
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
        menu_category = gui.add_submenu(cls.strings.WALLHAVEN_MENU_CATEGORY).get_submenu()
        for index, category in enumerate(CATEGORIES):
            gui.add_menu_item(getattr(cls.strings, f'WALLHAVEN_CATEGORY_{category}'),
                              gui.MenuItemType.CHECK, cls.CURRENT_CONFIG[CONFIG_CATEGORY][index] == '1', uid=category,
                              on_click=functools.partial(cls._on_category, menu_category), menu=menu_category)
        cls._on_category(menu_category)
        menu_purity = gui.add_submenu(cls.strings.WALLHAVEN_MENU_PURITY).get_submenu()
        for index, purity in enumerate(PURITIES):
            gui.add_menu_item(getattr(cls.strings, f'WALLHAVEN_PURITY_{purity}'),
                              gui.MenuItemType.CHECK, cls.CURRENT_CONFIG[CONFIG_PURITY][index] == '1', uid=purity,
                              on_click=functools.partial(cls._on_purity, menu_purity), menu=menu_purity)
        cls._on_purity(menu_purity)
        item_sorting = gui.add_submenu(cls.strings.WALLHAVEN_MENU_SORTING)
        gui.add_mapped_submenu(cls.strings.WALLHAVEN_MENU_ORDER, {order: getattr(
            cls.strings, f'WALLHAVEN_ORDER_{order}') for order in ORDERS}, cls.CURRENT_CONFIG, CONFIG_ORDER)
        enable_range = gui.add_mapped_submenu(cls.strings.WALLHAVEN_MENU_RANGE, {range_: getattr(
            cls.strings, f'WALLHAVEN_RANGE_{range_}') for range_ in RANGES}, cls.CURRENT_CONFIG, CONFIG_RANGE).enable
        gui.add_mapped_submenu(item_sorting, {sorting: getattr(
            cls.strings, f'WALLHAVEN_SORTING_{sorting}') for sorting in SORTINGS}, cls.CURRENT_CONFIG, CONFIG_SORTING,
                               on_click=functools.partial(cls._on_sorting, enable_range))
        cls._on_sorting(enable_range, cls.CURRENT_CONFIG[CONFIG_SORTING])
        ratios = cls.CURRENT_CONFIG[CONFIG_RATIO].split(',')
        menu_ratio = gui.add_submenu(cls.strings.WALLHAVEN_MENU_RATIO).get_submenu()
        for ratio in RATIOS:
            gui.add_menu_item(getattr(cls.strings, f'WALLHAVEN_RATIO_{ratio}'), gui.MenuItemType.CHECK, ratio in ratios,
                              uid=ratio, on_click=functools.partial(cls._on_ratio, menu_ratio), menu=menu_ratio)
        gui.add_separator(6, menu_ratio)
        colors = {color: colornames.get_nearest_color(color)[1] if color else cls.strings.WALLHAVEN_COLOR_ for color in COLORS}
        for item, color in zip(gui.add_mapped_submenu(
                cls.strings.WALLHAVEN_MENU_COLOR, colors, cls.CURRENT_CONFIG, CONFIG_COLORS).get_submenu(), colors):
            if color:
                rgb = colornames.hex_to_rgb(color)
                srgb = tuple(c / 255 for c in rgb)
                item.set_tooltip(_COLOR_TEMPLATE.format(colornames.format_cmyk(*colornames.cmy_to_cmyk(*colornames.srgb_to_cmy(
                    *srgb))), colornames.format_hsv(*colorsys.rgb_to_hsv(*srgb)), colornames.format_hls(
                    *colorsys.rgb_to_hls(*srgb))), f'HEX: #{color.upper()} {rgb}', win32.get_colored_bitmap(*rgb))
                item.bind(gui.MenuItemEvent.RIGHT_UP, on_color_right)

    @classmethod
    def _on_category(cls, menu: gui.Menu):
        cls.CURRENT_CONFIG[CONFIG_CATEGORY] = ''.join(str(int(item.is_checked())) for item in gui.get_menu_items(menu).values())
        disable = cls.CURRENT_CONFIG[CONFIG_CATEGORY].count('1') == 1
        for item in gui.get_menu_items(menu).values():
            item.enable(not disable or not item.is_checked())

    @classmethod
    def _on_purity(cls, menu: gui.Menu):
        cls.CURRENT_CONFIG[CONFIG_PURITY] = ''.join(str(int(item.is_checked())) for item in gui.get_menu_items(menu).values())
        disable = cls.CURRENT_CONFIG[CONFIG_PURITY].count('1') == 1
        for index, item in enumerate(gui.get_menu_items(menu).values()):
            item.enable((not disable or not item.is_checked()) and (index != 2 or bool(cls.CURRENT_CONFIG[CONFIG_KEY])))

    @classmethod
    def _on_ratio(cls, menu: gui.Menu):
        ratios = []
        for ratio, item in gui.get_menu_items(menu).items():
            item.enable()
            if item.is_checked():
                ratios.append(ratio)
        if len(ratios) == 1:
            gui.get_menu_item_by_uid(ratios[0], menu=menu).enable(False)
        cls.CURRENT_CONFIG[CONFIG_RATIO] = ','.join(ratios)

    @classmethod
    def _on_sorting(cls, enable_range: Callable[[bool], bool], sorting: str):
        enable_range(sorting == SORTINGS[5])
