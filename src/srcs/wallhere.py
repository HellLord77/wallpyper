import colorsys
import functools
import json
from typing import Callable, Iterator, Optional, TypedDict

import gui
import validator
import win32
from libs import colornames, files, request, soup
from . import Source

_TEMPLATE_COLOR = 'CMYK: {}\nHSV: {}\nHSL: {}'
_ATTRS = {'type': 'application/ld+json'}

URL_BASE = 'https://wallhere.com'
URL_API = request.join(URL_BASE, 'en')
URL_WALLPAPERS = request.join(URL_API, 'wallpapers')
URL_RANDOM = request.join(URL_WALLPAPERS, 'random')
URL_WALLPAPER = request.join(URL_API, 'wallpaper')
URL_PHOTO = request.join('https://get.wallhere.com', 'photo')

CONFIG_RANDOM = 'random'
CONFIG_QUERY = 'q'
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


def _on_random(enable: Callable[[bool], bool], random: bool):
    enable(not random)


def _on_color_right(_: int, item_color: gui.MenuItem):
    win32.clipboard.copy_text(f'#{item_color.get_uid().upper()}')


class WallHere(Source):
    VERSION = '0.0.1'
    URL = URL_BASE
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_RANDOM: bool,
        CONFIG_QUERY: str,
        CONFIG_ORDER: str,
        CONFIG_ORIENTATION: str,
        CONFIG_WIDTH: str,
        CONFIG_HEIGHT: str,
        CONFIG_COLOR: str,
        CONFIG_NSFW: bool})
    DEFAULT_CONFIG = {
        CONFIG_RANDOM: False,
        CONFIG_QUERY: '',
        CONFIG_ORDER: ORDERS[1],
        CONFIG_ORIENTATION: ORIENTATIONS[0],
        CONFIG_WIDTH: '',
        CONFIG_HEIGHT: '',
        CONFIG_COLOR: COLORS[0],
        CONFIG_NSFW: True}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_iterable, CONFIG_ORDER, ORDERS)
        cls._fix_config(validator.ensure_iterable, CONFIG_ORIENTATION, ORIENTATIONS)
        cls._fix_config(validator.ensure_iterable, CONFIG_COLOR, COLORS)

    @classmethod
    def create_menu(cls):
        enable_order = gui.add_submenu_radio(cls.STRINGS.WALLHERE_MENU_ORDER, {
            order: getattr(cls.STRINGS, f'WALLHERE_ORDER_{order}')
            for order in ORDERS}, cls.CURRENT_CONFIG, CONFIG_ORDER).enable
        gui.add_menu_item_check(
            cls.STRINGS.WALLHERE_LABEL_RANDOM, cls.CURRENT_CONFIG, CONFIG_RANDOM,
            on_click=functools.partial(_on_random, enable_order), position=0)
        _on_random(enable_order, cls.CURRENT_CONFIG[CONFIG_RANDOM])
        gui.add_submenu_radio(cls.STRINGS.WALLHERE_MENU_ORIENTATION, {
            orientation: getattr(cls.STRINGS, f'WALLHERE_ORIENTATION_{orientation}')
            for orientation in ORIENTATIONS}, cls.CURRENT_CONFIG, CONFIG_ORIENTATION)
        colors = {color: colornames.get_nearest_color(color)[
            1] if color else cls.STRINGS.WALLHERE_COLOR_ for color in COLORS}
        for item, color in zip(gui.add_submenu_radio(
                cls.STRINGS.WALLHERE_MENU_COLOR, colors,
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
        gui.add_menu_item_check(cls.STRINGS.WALLHERE_LABEL_NSFW, cls.CURRENT_CONFIG, CONFIG_NSFW)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[files.File]]:
        items: Optional[list] = None
        if params.pop(CONFIG_RANDOM):
            url = URL_RANDOM
            del params[CONFIG_QUERY]
            del params[CONFIG_ORDER]
        else:
            url = URL_WALLPAPERS
        if not params.pop(CONFIG_NSFW):
            params[CONFIG_NSFW] = 'off'
        params['page'] = '1'
        params['format'] = 'json'
        while True:
            if not items:
                response = request.get(url, params=params)
                if response:
                    items = soup.loads(f'<html>{response.json()["data"]}</html>').children
                    params['page'] = str(int(params['page']) + 1)
                if not items:
                    yield
                    continue
            item = items.pop(0)
            response_item = request.get(request.join(
                URL_WALLPAPER, item.get_child().get_child().attributes['href']))
            if not response_item:
                items.insert(0, item)
                yield
                continue
            classes = item.attributes['class'].split()
            data = json.loads(soup.find_element(soup.loads(
                response_item.text).iter_all_children(), 'script', _ATTRS).datas[0])
            content_url = data['contentUrl']
            yield files.ImageFile(content_url, width=int(data['width'][:-2]), height=int(
                data['height'][:-2]), sketchy='item-sketchy' in classes, nsfw='item-nsfw' in classes)
