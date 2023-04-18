import colorsys
import functools
import re
from typing import Callable, Iterator, Optional, TypedDict, ValuesView

import gui
import validator
import win32
from libs import colornames, request
from . import ImageFile
from . import Source

_TEMPLATE_COLOR = 'CMYK: {}\nHSV: {}\nHSL: {}'

URL_BASE = 'https://wallhaven.cc'
URL_API = request.join_url(URL_BASE, 'api', 'v1')
URL_SEARCH = request.join_url(URL_API, 'search')
URL_SETTINGS = request.join_url(URL_API, 'settings')

CONFIG_KEY = 'apikey'
CONFIG_CATEGORIES = 'categories'
CONFIG_PURITY = 'purity'
CONFIG_SORTING = 'sorting'
CONFIG_ORDER = 'order'
CONFIG_RANGE = 'topRange'
CONFIG_RATIO = 'ratios'
CONFIG_COLORS = 'colors'
CONFIG_AI_FILTER = 'ai_art_filter'

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
AI_FILTERS = '0', '1'
PATTERN_PURITY = re.compile('(?!000)[01]{3}')


def _on_color_right(event):
    win32.clipboard.copy_text(f'#{event.control.get_uid().upper()}')


def _authenticate(key: str) -> bool:
    return bool(request.get(URL_SETTINGS, {'apikey': key}))


class Wallhaven(Source):  # https://wallhaven.cc/help/api
    NAME = 'wallhaven'
    VERSION = '0.0.7'
    URL = URL_BASE
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_KEY: str,
        'q': str,
        CONFIG_CATEGORIES: list[bool],
        CONFIG_PURITY: str,
        CONFIG_SORTING: str,
        CONFIG_ORDER: str,
        CONFIG_RANGE: str,
        'atleast': str,
        'resolutions': str,
        CONFIG_RATIO: str,
        CONFIG_COLORS: str,
        CONFIG_AI_FILTER: str})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_KEY: '',
        'q': '',
        CONFIG_CATEGORIES: [True, True, True],
        CONFIG_PURITY: '100',
        CONFIG_SORTING: SORTINGS[0],
        CONFIG_ORDER: ORDERS[0],
        CONFIG_RANGE: RANGES[3],
        'atleast': '',
        'resolutions': '',
        CONFIG_RATIO: f'{RATIOS[0]},{RATIOS[6]}',
        CONFIG_COLORS: COLORS[0],
        CONFIG_AI_FILTER: AI_FILTERS[0]}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_len, CONFIG_CATEGORIES, 3)
        cls._fix_config(validator.ensure_truthy, CONFIG_CATEGORIES, any)
        cls._fix_config(validator.ensure_pattern, CONFIG_PURITY, PATTERN_PURITY)
        cls._fix_config(validator.ensure_iterable, CONFIG_SORTING, SORTINGS)
        cls._fix_config(validator.ensure_iterable, CONFIG_ORDER, ORDERS)
        cls._fix_config(validator.ensure_iterable, CONFIG_RANGE, RANGES)
        cls._fix_config(validator.ensure_iterables_joined, CONFIG_RATIO, RATIOS)
        cls._fix_config(validator.ensure_truthy, CONFIG_RATIO)
        cls._fix_config(validator.ensure_iterable, CONFIG_COLORS, COLORS)
        cls._fix_config(validator.ensure_iterable, CONFIG_AI_FILTER, AI_FILTERS)
        if not cls.CURRENT_CONFIG[CONFIG_KEY]:
            cls.CURRENT_CONFIG[CONFIG_PURITY] = f'{cls.CURRENT_CONFIG[CONFIG_PURITY][:2]}0'

    @classmethod
    def create_menu(cls):
        gui.add_submenu_check(cls._text('MENU_CATEGORY'), (
            cls._text(f'CATEGORY_{rating}') for rating in range(3)),
                              (1, None), cls.CURRENT_CONFIG, CONFIG_CATEGORIES)
        gui.add_menu_item_check(cls._text('LABEL_AI_FILTER'), cls.CURRENT_CONFIG,
                                CONFIG_AI_FILTER, on_click=cls._on_ai_filter).check(
            cls.CURRENT_CONFIG[CONFIG_AI_FILTER] == AI_FILTERS[0])
        with gui.set_menu(gui.add_submenu(cls._text('MENU_PURITY'))) as menu_purity:
            for index, purity in enumerate(PURITIES):
                gui.add_menu_item(
                    cls._text(f'PURITY_{purity}'), gui.MenuItemType.CHECK,
                    cls.CURRENT_CONFIG[CONFIG_PURITY][index] == '1', uid=purity)
        values_purity = gui.get_menu_items(menu_purity).values()
        on_purity = functools.partial(cls._on_purity, values_purity)
        for item_purity in values_purity:
            gui.set_on_click(item_purity, on_purity)
        on_purity()
        item_sorting = gui.add_submenu(cls._text('MENU_SORTING'))
        gui.add_submenu_radio(cls._text('MENU_ORDER'), {
            order: cls._text(f'ORDER_{order}')
            for order in ORDERS}, cls.CURRENT_CONFIG, CONFIG_ORDER)
        enable_range = gui.add_submenu_radio(cls._text('MENU_RANGE'), {
            range_: cls._text(f'RANGE_{range_}')
            for range_ in RANGES}, cls.CURRENT_CONFIG, CONFIG_RANGE).enable
        gui.add_submenu_radio(item_sorting, {
            sorting: cls._text(f'SORTING_{sorting}')
            for sorting in SORTINGS}, cls.CURRENT_CONFIG, CONFIG_SORTING,
                              on_click=functools.partial(cls._on_sorting, enable_range))
        cls._on_sorting(enable_range, cls.CURRENT_CONFIG[CONFIG_SORTING])
        ratios = cls.CURRENT_CONFIG[CONFIG_RATIO].split(',')
        with gui.set_menu(gui.add_submenu(cls._text('MENU_RATIO'))) as menu_ratio:
            on_ratio = functools.partial(cls._on_ratio, menu_ratio)
            for ratio in RATIOS:
                gui.add_menu_item(
                    cls._text(f'RATIO_{ratio}'), gui.MenuItemType.CHECK,
                    ratio in ratios, uid=ratio, on_click=on_ratio)
        cls._on_ratio(menu_ratio)
        gui.add_separator(6, menu_ratio)
        colors = {color: colornames.get_nearest_color(color)[
            1] if color else cls._text('COLOR_') for color in COLORS}
        for item, color in zip(gui.add_submenu_radio(
                cls._text('MENU_COLOR'), colors,
                cls.CURRENT_CONFIG, CONFIG_COLORS).get_submenu(), colors):
            if color:
                rgb = colornames.hex_to_rgb(color)
                srgb = tuple(c / 255 for c in rgb)
                item.set_tooltip(_TEMPLATE_COLOR.format(colornames.format_cmyk(
                    *colornames.cmy_to_cmyk(*colornames.srgb_to_cmy(*srgb))),
                    colornames.format_hsv(*colorsys.rgb_to_hsv(*srgb)),
                    colornames.format_hls(*colorsys.rgb_to_hls(*srgb))),
                    f'HEX: #{color.upper()} {rgb}', win32.get_colored_bitmap(*rgb))
                item.bind(gui.MenuItemEvent.RIGHT_UP, _on_color_right)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        datas: Optional[list] = None
        if params[CONFIG_SORTING] != SORTINGS[5]:
            del params[CONFIG_RANGE]
        params[CONFIG_CATEGORIES] = ''.join(map(str, map(int, params[CONFIG_CATEGORIES])))
        while True:
            if not datas:
                response = request.get(URL_SEARCH, params)
                if response:
                    json = response.json()
                    datas = json['data']
                    meta = json['meta']
                    params['page'] = str(meta['current_page'] % meta['last_page'] + 1)
                    params['seed'] = meta['seed']
                if not datas:
                    yield
                    continue
            data = datas.pop(0)
            url = data['path']
            purity = data['purity']
            yield ImageFile(url, size=data['file_size'], width=data[
                'dimension_x'], height=data['dimension_y'],
                            sketchy=purity == PURITIES[1], nsfw=purity == PURITIES[2])

    @classmethod
    def _on_purity(cls, items: ValuesView[gui.MenuItem]):
        cls.CURRENT_CONFIG[CONFIG_PURITY] = ''.join(str(int(
            item.is_checked())) for item in items)
        disable = cls.CURRENT_CONFIG[CONFIG_PURITY].count('1') == 1
        for index, item in enumerate(items):
            item.enable((not disable or not item.is_checked()) and (
                    index != 2 or bool(cls.CURRENT_CONFIG[CONFIG_KEY])))

    @classmethod
    def _on_ratio(cls, menu: gui.Menu):
        ratios = []
        for ratio, item in gui.get_menu_items(menu).items():
            item.enable()
            if item.is_checked():
                ratios.append(ratio)
        if len(ratios) == 1:
            gui.get_menu_item_by_uid(ratios[0], False, menu).enable(False)
        cls.CURRENT_CONFIG[CONFIG_RATIO] = ','.join(ratios)

    @classmethod
    def _on_sorting(cls, enable: Callable[[bool], bool], sorting: str):
        enable(sorting == SORTINGS[5])

    @classmethod
    def _on_ai_filter(cls, checked: bool):
        cls.CURRENT_CONFIG[CONFIG_AI_FILTER] = str(1 - int(checked))
