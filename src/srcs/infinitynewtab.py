import colorsys
import functools
import re
from typing import Callable, Iterator, Optional, TypedDict

import gui
import validator
import win32
from libs import colornames, request
from . import ImageFile, Source

URL_LIST = request.join_url('https://api.infinitynewtab.com', 'v2', 'get_wallpaper_list')
URL_RANDOM = request.join_url('https://infinity-api.infinitynewtab.com', 'random-wallpaper')

CONFIG_MODE = 'mode'
CONFIG_ORDER = 'order'
CONFIG_COLOR = 'color'
CONFIG_LABEL = 'tag'
CONFIG_SOURCE = 'source'

MODES = 'random', 'cloud', 'source'
ORDERS = 'like', '_id', ''
COLORS = '', 'c00018', 'de8930', 'f7d946', 'cbe582', '506f37', '60a8d8', '184878', 'be7ab9'
LABELS = (
    '', 'nature', 'ocean', 'architecture', 'animals', 'travel',
    'food-drink', 'anime', 'athletics', 'technology', 'street-photography')
SOURCES = (
    'all', 'InfinityLandscape', 'Infinity', 'bing', 'Unsplash',
    'Life Of Pix', 'MMT', 'Realistic Shots', 'Jay Mantri', 'Free Nature Stock',
    'Skitter Photo', 'Startup Stock Photos', 'Barn Images', 'Picography')

_FMT_COLOR = 'CMYK: {}\nHSV: {}\nHSL: {}'
_RE_RESOLUTION = re.compile(r'[x×]')


def _on_color_right(event):
    win32.clipboard.copy_text(f'#{event.control.get_uid().upper()}')


class InfinityNewTab(Source):
    NAME = 'Infinity New Tab'
    VERSION = '0.0.1'
    URL = 'https://www.infinitytab.com'
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_MODE: str,
        CONFIG_ORDER: str,
        CONFIG_COLOR: str,
        CONFIG_LABEL: str,
        CONFIG_SOURCE: str})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_MODE: MODES[0],
        CONFIG_ORDER: ORDERS[2],
        CONFIG_COLOR: COLORS[0],
        CONFIG_LABEL: LABELS[0],
        CONFIG_SOURCE: SOURCES[0]}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_contains, CONFIG_MODE, MODES)
        cls._fix_config(validator.ensure_contains, CONFIG_ORDER, ORDERS)
        cls._fix_config(validator.ensure_contains, CONFIG_COLOR, COLORS)
        cls._fix_config(validator.ensure_contains, CONFIG_LABEL, LABELS)
        cls._fix_config(validator.ensure_contains, CONFIG_SOURCE, SOURCES)

    @classmethod
    def create_menu(cls):
        gui.add_separator()
        enable_order = gui.add_submenu_radio(cls._text('MENU_ORDER'), {
            order: cls._text(f'ORDER_{order}') for order in ORDERS},
                                             cls.CURRENT_CONFIG, CONFIG_ORDER).enable
        colors = {color: colornames.get_nearest_color(color)[
            1] if color else cls._text('COLOR_') for color in COLORS}
        item_color = gui.add_submenu_radio(cls._text(
            'MENU_COLOR'), colors, cls.CURRENT_CONFIG, CONFIG_COLOR)
        for item, color in zip(item_color.get_submenu(), colors):
            if color:
                rgb = colornames.hex_to_rgb(color)
                srgb = tuple(c / 255 for c in rgb)
                item.set_tooltip(_FMT_COLOR.format(colornames.format_cmyk(
                    *colornames.cmy_to_cmyk(*colornames.srgb_to_cmy(*srgb))),
                    colornames.format_hsv(*colorsys.rgb_to_hsv(*srgb)),
                    colornames.format_hls(*colorsys.rgb_to_hls(*srgb))),
                    f'HEX: #{color.upper()} {rgb}', win32.get_colored_bitmap(*rgb))
                item.bind(gui.MenuItemEvent.RIGHT_UP, _on_color_right)
        enable_label = gui.add_submenu_radio(cls._text('MENU_LABEL'), {
            label: cls._text(f'LABEL_{label}') for label in LABELS},
                                             cls.CURRENT_CONFIG, CONFIG_LABEL).enable
        gui.add_separator()
        enable_source = gui.add_submenu_radio(cls._text('MENU_SOURCE'), {
            source: cls._text(f'SOURCE_{source}') for source in SOURCES},
                                              cls.CURRENT_CONFIG, CONFIG_SOURCE).enable
        on_mode = functools.partial(cls._on_mode, enable_order, item_color.enable,
                                    enable_label, enable_source)
        gui.add_submenu_radio(cls._text('MENU_MODE'), {
            mode: cls._text(f'MODE_{mode}') for mode in MODES},
                              cls.CURRENT_CONFIG, CONFIG_MODE, on_click=on_mode, position=0)
        on_mode(cls.CURRENT_CONFIG[CONFIG_MODE])

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        photos = []
        mode = params.pop(CONFIG_MODE)
        random = mode == MODES[0]
        if random:
            url = URL_RANDOM
            params = {}
        else:
            url = URL_LIST
            if mode == MODES[1]:
                del params[CONFIG_SOURCE]
            else:
                params = {CONFIG_SOURCE: params.pop(CONFIG_SOURCE)}
        page = 0
        while True:
            if not photos:
                if not random:
                    params['page'] = str(page)
                response = request.get(url, params)
                if response:
                    data = response.json()['data']
                    if random:
                        photos = data
                    else:
                        photos = data['list']
                        page = (page + 1) % data['totalPages']
                if not photos:
                    yield
                    continue
            photo = photos.pop(0)
            width, height = map(int, _RE_RESOLUTION.split(photo['dimensions'].replace('px', '')))
            yield ImageFile(photo['src']['rawSrc'], width=width, height=height)

    @classmethod
    def _on_mode(cls, enable_order: Callable[[bool], bool],
                 enable_color: Callable[[bool], bool],
                 enable_label: Callable[[bool], bool],
                 enable_source: Callable[[bool], bool], mode: str):
        cloud = mode == MODES[1]
        enable_order(cloud)
        enable_color(cloud)
        enable_label(cloud)
        enable_source(mode == MODES[2])
