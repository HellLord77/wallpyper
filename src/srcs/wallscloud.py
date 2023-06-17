import colorsys
import functools
from typing import Callable, Iterator, Optional, TypedDict

import gui
import validator
import win32
from libs import colornames, request, sgml
from . import ImageFile, Source

URL_BASE = request.join_url('https://wallscloud.net', 'en')
URL_CATEGORY = request.join_url(URL_BASE, 'category')
URL_TOP = request.join_url(URL_BASE, 'wallpapers')
URL_RANDOM = request.join_url(URL_TOP, 'random')
URL_SEARCH = request.join_url(URL_BASE, 'search')

CONFIG_MODE = 'mode'
CONFIG_CATEGORY = 'category'
CONFIG_TOP = 'top'
CONFIG_SEARCH = 'q'
CONFIG_COLOR = 'color'
CONFIG_ORIENTATION = 'orientation'
CONFIG_TIME = 'time'
CONFIG_SORT = 'sort'
CONFIG_ORDER = 'order'

MODES = 'category', 'top', 'random', 'search'
CATEGORIES = (
    '3d', 'hi-tech', 'weapon', 'abstract', 'aircraft', 'cars', 'anime',
    'architecture', 'cities', 'graphics', 'food', 'animals', 'games',
    'illustration', 'interiors', 'computers', 'ships', 'space', 'love', 'people',
    'macro', 'minimalism', 'motorcycles', 'music', 'multiplicatios', 'holidays',
    'funny', 'nature', 'others', 'sport', 'textures', 'fantasy', 'films')
TOPS = 'latest', 'download', 'view', 'favorite', 'rating'
COLORS = (
    '', '00ffff', '000000', '0000ff', 'ff00ff', '808080', '008000', '00ff00', '800000',
    '000080', '808000', '800080', 'ff0000', 'c0c0c0', '008080', 'ffffff', 'ffff00')
ORIENTATIONS = 'all', 'portrait', 'landscape'
TIMES = 'all', 'today', '7days', '30days', '60days'
SORTS = 'latest', 'views', 'downloads', 'favorites', 'rating', 'color'
ORDERS = 'desc', 'asc'

_TEMPLATE_COLOR = 'CMYK: {}\nHSV: {}\nHSL: {}'
_ATTRS_WALL_LINK = {'class': 'wall_link'}
_ATTRS_SIZE = {'class': 'size'}


def _on_color_right(event):
    win32.clipboard.copy_text(f'#{event.control.get_uid().upper()}')


class Wallscloud(Source):
    VERSION = '0.0.1'
    URL = URL_BASE
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_MODE: str,
        CONFIG_CATEGORY: str,
        CONFIG_TOP: str,
        CONFIG_SEARCH: str,
        CONFIG_COLOR: str,
        CONFIG_ORIENTATION: str,
        CONFIG_TIME: str,
        CONFIG_SORT: str,
        CONFIG_ORDER: str})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_MODE: MODES[1],
        CONFIG_CATEGORY: CATEGORIES[0],
        CONFIG_TOP: TOPS[0],
        CONFIG_SEARCH: '',
        CONFIG_COLOR: COLORS[0],
        CONFIG_ORIENTATION: ORIENTATIONS[0],
        CONFIG_TIME: TIMES[0],
        CONFIG_SORT: SORTS[0],
        CONFIG_ORDER: ORDERS[0]}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_contains, CONFIG_MODE, MODES)
        cls._fix_config(validator.ensure_contains, CONFIG_CATEGORY, CATEGORIES)
        cls._fix_config(validator.ensure_contains, CONFIG_TOP, TOPS)
        cls._fix_config(validator.ensure_contains, CONFIG_COLOR, COLORS)
        cls._fix_config(validator.ensure_contains, CONFIG_ORIENTATION, ORIENTATIONS)
        cls._fix_config(validator.ensure_contains, CONFIG_TIME, TIMES)
        cls._fix_config(validator.ensure_contains, CONFIG_SORT, SORTS)
        cls._fix_config(validator.ensure_contains, CONFIG_ORDER, ORDERS)

    @classmethod
    def create_menu(cls):
        enable_category = gui.add_submenu_radio(cls._text('MENU_CATEGORY'), {
            category: cls._text(f'CATEGORY_{category}') for category in CATEGORIES},
                                                cls.CURRENT_CONFIG, CONFIG_CATEGORY).enable
        enable_top = gui.add_submenu_radio(cls._text('MENU_TOP'), {top: cls._text(
            f'TOP_{top}') for top in TOPS}, cls.CURRENT_CONFIG, CONFIG_TOP).enable
        gui.add_separator()
        enable_orientation = gui.add_submenu_radio(cls._text('MENU_ORIENTATION'), {
            orientation: cls._text(f'ORIENTATION_{orientation}')
            for orientation in ORIENTATIONS}, cls.CURRENT_CONFIG, CONFIG_ORIENTATION).enable
        enable_time = gui.add_submenu_radio(cls._text('MENU_TIME'), {time: cls._text(
            f'TIME_{time}') for time in TIMES}, cls.CURRENT_CONFIG, CONFIG_TIME).enable
        item_sort = gui.add_submenu_radio(cls._text('MENU_SORT'), {sort: cls._text(
            f'SORT_{sort}') for sort in SORTS}, cls.CURRENT_CONFIG, CONFIG_SORT)
        colors = {color: colornames.get_nearest_color(color)[
            1] if color else cls._text('COLOR_') for color in COLORS}
        menu_sort = item_sort.get_submenu()
        on_color = functools.partial(cls._on_color, menu_sort[0], menu_sort[5].enable)
        item_color = gui.add_submenu_radio(cls._text('MENU_COLOR'), colors, cls.CURRENT_CONFIG,
                                           CONFIG_COLOR, on_click=on_color, position=3)
        for item, color in zip(item_color.get_submenu(), COLORS):
            if color:
                rgb = colornames.hex_to_rgb(color)
                srgb = tuple(c / 255 for c in rgb)
                item.set_tooltip(_TEMPLATE_COLOR.format(colornames.format_cmyk(
                    *colornames.cmy_to_cmyk(*colornames.srgb_to_cmy(*srgb))),
                    colornames.format_hsv(*colorsys.rgb_to_hsv(*srgb)),
                    colornames.format_hls(*colorsys.rgb_to_hls(*srgb))),
                    f'HEX: #{color.upper()} {rgb}', win32.get_colored_bitmap(*rgb))
                item.bind(gui.MenuItemEvent.RIGHT_UP, _on_color_right)
        on_color(cls.CURRENT_CONFIG[CONFIG_COLOR])
        enable_order = gui.add_submenu_radio(cls._text('MENU_ORDER'), {order: cls._text(
            f'ORDER_{order}') for order in ORDERS}, cls.CURRENT_CONFIG, CONFIG_ORDER).enable
        on_mode = functools.partial(
            cls._on_mode, enable_category, enable_top, item_color.enable,
            enable_orientation, enable_time, item_sort.enable, enable_order)
        gui.add_submenu_radio(cls._text('MENU_MODE'), {mode: cls._text(
            f'MODE_{mode}') for mode in MODES}, cls.CURRENT_CONFIG,
                              CONFIG_MODE, on_click=on_mode, position=0)
        on_mode(cls.CURRENT_CONFIG[CONFIG_MODE])

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        wall_links: Optional[list] = None
        mode = params.pop(CONFIG_MODE)
        category = params.pop(CONFIG_CATEGORY)
        top = params.pop(CONFIG_TOP)
        if mode == MODES[0]:
            url = request.join_url(URL_CATEGORY, category)
            del params[CONFIG_SEARCH]
            del params[CONFIG_COLOR]
        elif mode == MODES[1]:
            url = request.join_url(URL_TOP, top)
            params = {
                CONFIG_ORIENTATION: params[CONFIG_ORIENTATION],
                CONFIG_TIME: params[CONFIG_TIME]}
        elif mode == MODES[2]:
            url = URL_RANDOM
            params = {}
        else:
            url = URL_SEARCH
        page = 1
        while True:
            if not wall_links:
                response = request.post(url, {
                    'offset': '1', 'page': str(page)}, params=params)
                if response:
                    json = response.json()
                    wall_links = list(sgml.loads(
                        f'<html>{json["html"]}</html>').find_all('a', _ATTRS_WALL_LINK))
                    page = page % (json['total_pages'] or 1) + 1
                if not wall_links:
                    yield
                    continue
            wall_link = wall_links.pop(0)
            url = wall_link['href']
            url_wall_link = request.join_url(url, 'original', 'download')
            if not (name := request.get_filename(url_wall_link)):
                wall_links.insert(0, wall_link)
                yield
                continue
            width, height = map(int, wall_link.find(
                'div', _ATTRS_SIZE).get_data().split('x'))
            yield ImageFile(url_wall_link, name, url=url, width=width, height=height)

    @classmethod
    def _on_mode(cls, enable_category: Callable[[bool], bool], enable_top: Callable[[bool], bool],
                 enable_color: Callable[[bool], bool], enable_orientation: Callable[[bool], bool],
                 enable_time: Callable[[bool], bool], enable_sort: Callable[[bool], bool],
                 enable_order: Callable[[bool], bool], mode: str):
        enable_category(mode == MODES[0])
        enable_top(mode == MODES[1])
        enable_color(mode == MODES[3])
        enable_orientation(mode != MODES[2])
        enable_time(mode != MODES[2])
        enable_sort(mode in (MODES[0], MODES[3]))
        enable_order(mode in (MODES[0], MODES[3]))

    @classmethod
    def _on_color(cls, item_latest: gui.MenuItem, enable_color: Callable[[bool], bool], color: str):
        no_color = color == COLORS[0]
        if no_color:
            item_latest.check()
            item_latest.trigger(gui.MenuItemEvent.LEFT_UP)
        enable_color(not no_color)
