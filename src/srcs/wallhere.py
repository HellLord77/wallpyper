import colorsys
import functools
import json
from typing import Callable, Iterator, Optional, TypedDict

import gui
import validator
import win32
from libs import colornames, request, sgml
from . import ImageFile, Source

URL_BASE = 'https://wallhere.com'
URL_API = request.join_url(URL_BASE, 'en')
URL_WALLPAPERS = request.join_url(URL_API, 'wallpapers')
URL_RANDOM = request.join_url(URL_WALLPAPERS, 'random')
URL_WALLPAPER = request.join_url(URL_API, 'wallpaper')
URL_PHOTO = request.join_url('https://get.wallhere.com', 'photo')

CONFIG_RANDOM = 'random'
CONFIG_SEARCH = 'q'
CONFIG_ORDER = 'order'
CONFIG_ORIENTATION = 'direction'
CONFIG_WIDTH = 'min_width'
CONFIG_HEIGHT = 'min_height'
CONFIG_COLOR = 'color'
CONFIG_NSFW = 'NSFW'

ORDERS = 'latest', 'popular'
ORIENTATIONS = '', 'horizontal', 'vertical'
COLORS = (
    '', 'FF2000', 'A24615', 'FF7C00', 'FF9F9C', 'FFFA00', 'FFCF00', '90E200',
    '00AB00', '00B2D4', '0062C6', '8C20BA', 'F52394', 'FFFFFF', '7C7C7C', '000000')

_TEMPLATE_COLOR = 'CMYK: {}\nHSV: {}\nHSL: {}'
_ATTRS_END = {'data-score': ''}
_ATTRS_JSON = {'type': 'application/ld+json'}


def _on_color_right(event):
    win32.clipboard.copy_text(f'#{event.control.get_uid().upper()}')


class WallHere(Source):
    VERSION = '0.0.2'
    URL = URL_BASE
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_RANDOM: bool,
        CONFIG_SEARCH: str,
        CONFIG_ORDER: str,
        CONFIG_ORIENTATION: str,
        CONFIG_WIDTH: str,
        CONFIG_HEIGHT: str,
        CONFIG_COLOR: str,
        CONFIG_NSFW: bool})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_RANDOM: False,
        CONFIG_SEARCH: '',
        CONFIG_ORDER: ORDERS[1],
        CONFIG_ORIENTATION: ORIENTATIONS[0],
        CONFIG_WIDTH: '',
        CONFIG_HEIGHT: '',
        CONFIG_COLOR: COLORS[0],
        CONFIG_NSFW: True}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_contains, CONFIG_ORDER, ORDERS)
        cls._fix_config(validator.ensure_contains, CONFIG_ORIENTATION, ORIENTATIONS)
        cls._fix_config(validator.ensure_contains, CONFIG_COLOR, COLORS)

    @classmethod
    def create_menu(cls):
        enable_order = gui.add_submenu_radio(cls._text('MENU_ORDER'), {
            order: cls._text(f'ORDER_{order}') for order in ORDERS},
                                             cls.CURRENT_CONFIG, CONFIG_ORDER).enable
        on_random = functools.partial(cls._on_random, enable_order)
        gui.add_menu_item_check(cls._text(
            'LABEL_RANDOM'), cls.CURRENT_CONFIG,
            CONFIG_RANDOM, on_click=on_random, position=0)
        on_random(cls.CURRENT_CONFIG[CONFIG_RANDOM])
        gui.add_submenu_radio(cls._text('MENU_ORIENTATION'), {
            orientation: cls._text(f'ORIENTATION_{orientation}')
            for orientation in ORIENTATIONS}, cls.CURRENT_CONFIG, CONFIG_ORIENTATION)
        colors = {color: colornames.get_nearest_color(color)[
            1] if color else cls._text('COLOR_') for color in COLORS}
        for item, color in zip(gui.add_submenu_radio(
                cls._text('MENU_COLOR'), colors,
                cls.CURRENT_CONFIG, CONFIG_COLOR).get_submenu(), COLORS):
            if color:
                rgb = colornames.hex_to_rgb(color)
                srgb = tuple(c / 255 for c in rgb)
                item.set_tooltip(_TEMPLATE_COLOR.format(colornames.format_cmyk(
                    *colornames.cmy_to_cmyk(*colornames.srgb_to_cmy(*srgb))),
                    colornames.format_hsv(*colorsys.rgb_to_hsv(*srgb)),
                    colornames.format_hls(*colorsys.rgb_to_hls(*srgb))),
                    f'HEX: #{color.upper()} {rgb}', win32.get_colored_bitmap(*rgb))
                item.bind(gui.MenuItemEvent.RIGHT_UP, _on_color_right)
        gui.add_menu_item_check(cls._text('LABEL_NSFW'),
                                cls.CURRENT_CONFIG, CONFIG_NSFW)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        items = []
        if params.pop(CONFIG_RANDOM):
            url = URL_RANDOM
            del params[CONFIG_SEARCH]
            del params[CONFIG_ORDER]
        else:
            url = URL_WALLPAPERS
        if not params.pop(CONFIG_NSFW):
            params[CONFIG_NSFW] = 'off'
        params['format'] = 'json'
        page = 1
        while True:
            if not items:
                params['page'] = str(page)
                response = request.get(url, params)
                if response:
                    html = sgml.loads(f'<html>{response.json()["data"]}</html>')
                    items = list(html.find_all('div', classes='item'))
                    if html.find('a', _ATTRS_END) is None:
                        page += 1
                    else:
                        page = 1
                if not items:
                    yield
                    continue
            item = items.pop(0)
            url_item = request.join_url(URL_WALLPAPER, item[0][0]['href'])
            response = request.get(url_item)
            if not response:
                items.insert(0, item)
                yield
                continue
            data = json.loads(sgml.loads(response.text).find(
                'script', _ATTRS_JSON).get_data())
            classes = item.get_class()
            yield ImageFile(data['contentUrl'], url=url_item, width=int(data['width'][:-2]), height=int(
                data['height'][:-2]), sketchy='item-sketchy' in classes, nsfw='item-nsfw' in classes)

    @classmethod
    def _on_random(cls, enable: Callable[[bool], bool], random: bool):
        enable(not random)
