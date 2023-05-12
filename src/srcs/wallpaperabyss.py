import colorsys
import functools
import os
from typing import Callable, Iterator, Optional, TypedDict

import gui
import validator
import win32
from libs import colornames, minihtml, request
from libs.request import cloudflare
from . import ImageFile, Source

_TEMPLATE_COLOR = 'CMYK: {}\nHSV: {}\nHSL: {}'
_ATTRS_THUMB = {'class': 'thumb-container'}
_ATTRS_NEXT_PAGE = {'id': 'next_page'}
_ATTRS_PAGINATION = {'class': 'pagination-simple center'}

URL_BASE = 'https://wall.alphacoders.com'
URL_INFO = request.join_url(URL_BASE, 'big.php')

CONFIG_METHOD = 'method'
CONFIG_SEARCH = 'search'
CONFIG_RESOLUTION_FILTER = 'resolution_filter'
CONFIG_RESOLUTION_EQUALS = 'resolution_equals'
CONFIG_SORT = 'sort'
CONFIG_RESOLUTION = 'resolution'
CONFIG_LICENSE = 'filter'
CONFIG_COLOR = 'hex_color'
CONFIG_CATEGORY = 'id'

METHODS = (
    'search', 'newest_wallpapers', 'featured', 'by_creator', 'by_resolution', 'popular', 'by_license',
    'random', 'highest_rated', 'by_views', 'by_favorites', 'by_comments', 'by_color', 'by_category')
RESOLUTION_FILTERS = (
    '0x0', '1366x768', '1600x900', '1920x1080', '1920x1200',
    '2560x1440', '2560x1600', '3840x2160', '5120x2880', '7680x4320')
RESOLUTION_EQUALS = '%3E%3D', '%3D'
SORTS = 'newest', 'rating'
RESOLUTIONS = (
    (1600, 900), (1600, 1000), (1600, 1200), (1680, 1050), (1920, 1080), (1920, 1200),
    (1920, 1280), (1920, 1440), (2000, 1125), (2000, 1333), (2048, 1152), (2048, 1365),
    (2048, 1366), (2048, 1367), (2048, 1536), (2560, 1440), (2560, 1600), (2560, 1707),
    (2560, 1920), (2880, 1800), (2894, 2412), (3000, 2000), (3840, 2160), (3840, 2400),
    (5120, 2880), (5184, 3456), (5616, 3744), (5760, 3840), (6000, 4000), (7680, 4320))
LICENSES = 0, 6, 10, 7, 11, 9, 8, 4
COLORS = (
    '000000', '1c1c1c', '383838', '555555', '717171', '8d8d8d', 'aaaaaa', 'c6c6c6', 'e2e2e2', 'ffffff',
    '980000', 'ff0000', 'ff9900', 'ffff00', '00ff00', '00ffff', '4a86e8', '0000ff', '9900ff', 'ff00ff',
    'e6b8af', 'f4cccc', 'fce5cd', 'fff2cc', 'd9ead3', 'd0e0e3', 'c9daf8', 'cfe2f3', 'd9d2e9', 'ead1dc',
    'dd7e6b', 'ea9999', 'f9cb9c', 'ffe599', 'b6d7a8', 'a2c4c9', 'a4c2f4', '9fc5e8', 'b4a7d6', 'd5a6bd',
    'cc4125', 'e06666', 'f6b26b', 'ffd966', '93c47d', '76a5af', '6d9eeb', '6fa8dc', '8e7cc3', 'c27ba0',
    'a61c00', 'cc0000', 'e69138', 'f1c232', '6aa84f', '45818e', '3c78d8', '3d85c6', '674ea7', 'a64d79',
    '5b0f00', '660000', '783f04', '7f6000', '274e13', '0c343d', '1c4587', '073763', '20124d', '4c1130')
CATEGORIES = (
    1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 14, 15, 13, 16, 17, 18,
    19, 20, 22, 24, 25, 26, 27, 28, 30, 29, 31, 32, 34, 33)


def _on_color_right(event):
    win32.clipboard.copy_text(f'#{event.control.get_uid().upper()}')


class WallpaperAbyss(Source):
    NAME = 'Wallpaper Abyss'
    VERSION = '0.0.1'
    URL = URL_BASE
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_METHOD: str,
        CONFIG_SEARCH: str,
        CONFIG_RESOLUTION_FILTER: str,
        CONFIG_RESOLUTION_EQUALS: str,
        CONFIG_SORT: str,
        CONFIG_RESOLUTION: list[int],
        CONFIG_LICENSE: int,
        CONFIG_COLOR: str,
        CONFIG_CATEGORY: int})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_METHOD: METHODS[2],
        CONFIG_SEARCH: '',
        CONFIG_RESOLUTION_FILTER: RESOLUTION_FILTERS[0],
        CONFIG_RESOLUTION_EQUALS: RESOLUTION_EQUALS[0],
        CONFIG_SORT: SORTS[0],
        CONFIG_RESOLUTION: list(RESOLUTIONS[4]),
        CONFIG_LICENSE: LICENSES[7],
        CONFIG_COLOR: COLORS[67],
        CONFIG_CATEGORY: CATEGORIES[0]}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_iterable, CONFIG_METHOD, METHODS)
        cls._fix_config(validator.ensure_iterable, CONFIG_RESOLUTION_FILTER, RESOLUTION_FILTERS)
        cls._fix_config(validator.ensure_iterable, CONFIG_RESOLUTION_EQUALS, RESOLUTION_EQUALS)
        cls._fix_config(validator.ensure_iterable, CONFIG_SORT, SORTS)
        cls._fix_config(validator.ensure_iterable, CONFIG_LICENSE, LICENSES)
        cls._fix_config(validator.ensure_iterable, CONFIG_COLOR, COLORS)
        cls._fix_config(validator.ensure_iterable, CONFIG_CATEGORY, CATEGORIES)
        if saving:
            cls._fix_config(validator.ensure_iterable, CONFIG_RESOLUTION, RESOLUTIONS)
            cls.CURRENT_CONFIG[CONFIG_RESOLUTION] = list(cls.CURRENT_CONFIG[CONFIG_RESOLUTION])
        else:
            cls.CURRENT_CONFIG[CONFIG_RESOLUTION] = tuple(cls.CURRENT_CONFIG[CONFIG_RESOLUTION])
            cls._fix_config(validator.ensure_iterable, CONFIG_RESOLUTION, RESOLUTIONS)

    @classmethod
    def create_menu(cls):
        enable_resolution_filter = gui.add_submenu_radio(cls._text('MENU_RESOLUTION_FILTER'), {
            resolution_filter: cls._text(f'RESOLUTION_{resolution_filter}')
            for resolution_filter in RESOLUTION_FILTERS}, cls.CURRENT_CONFIG, CONFIG_RESOLUTION_FILTER).enable
        enable_resolution_equals = gui.add_submenu_radio(cls._text('MENU_RESOLUTION_EQUALS'), {
            resolution_equals: cls._text(f'RESOLUTION_EQUALS_{resolution_equals}')
            for resolution_equals in RESOLUTION_EQUALS}, cls.CURRENT_CONFIG, CONFIG_RESOLUTION_EQUALS).enable
        enable_sort = gui.add_submenu_radio(cls._text(
            'MENU_SORT'), {sort: cls._text(f'SORT_{sort}')
                           for sort in SORTS}, cls.CURRENT_CONFIG, CONFIG_SORT).enable
        enable_resolution = gui.add_submenu_radio(cls._text('MENU_RESOLUTION'), {
            resolution: cls._text(f'RESOLUTION_{resolution[0]}x{resolution[1]}').split('\t')[0]
            for resolution in RESOLUTIONS}, cls.CURRENT_CONFIG, CONFIG_RESOLUTION).enable
        enable_license = gui.add_submenu_radio(cls._text('MENU_LICENSE'), {
            license_: cls._text(f'LICENSE_{license_}')
            for license_ in LICENSES}, cls.CURRENT_CONFIG, CONFIG_LICENSE).enable
        item_color = gui.add_submenu_radio(
            cls._text('MENU_COLOR'), {color: colornames.get_nearest_color(
                color)[1] for color in COLORS}, cls.CURRENT_CONFIG, CONFIG_COLOR)
        for item, color in zip(item_color.get_submenu(), COLORS):
            rgb = colornames.hex_to_rgb(color)
            srgb = tuple(c / 255 for c in rgb)
            item.set_tooltip(_TEMPLATE_COLOR.format(colornames.format_cmyk(
                *colornames.cmy_to_cmyk(*colornames.srgb_to_cmy(*srgb))),
                colornames.format_hsv(*colorsys.rgb_to_hsv(*srgb)),
                colornames.format_hls(*colorsys.rgb_to_hls(*srgb))),
                f'HEX: #{color.upper()} {rgb}', win32.get_colored_bitmap(*rgb))
            item.bind(gui.MenuItemEvent.RIGHT_UP, _on_color_right)
        enable_category = gui.add_submenu_radio(cls._text('MENU_CATEGORY'), {
            category: cls._text(f'CATEGORY_{category}')
            for category in CATEGORIES}, cls.CURRENT_CONFIG, CONFIG_CATEGORY).enable
        on_method = functools.partial(
            cls._on_method, enable_resolution_filter, enable_resolution_equals,
            enable_sort, enable_resolution, enable_license, item_color.enable, enable_category)
        gui.add_submenu_radio(cls._text('MENU_METHOD'), {method: cls._text(
            f'METHOD_{method}') for method in METHODS}, cls.CURRENT_CONFIG,
                              CONFIG_METHOD, on_click=on_method, position=0)
        on_method(cls.CURRENT_CONFIG[CONFIG_METHOD])

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        images: Optional[list] = None
        url = request.join_url(URL_BASE, f'{cls.CURRENT_CONFIG[CONFIG_METHOD]}.php')
        query = {}
        if params[CONFIG_METHOD] == METHODS[0]:
            query[CONFIG_SEARCH] = params[CONFIG_SEARCH]
        elif params[CONFIG_METHOD] == METHODS[4]:
            query['w'], query['h'] = cls.CURRENT_CONFIG[CONFIG_RESOLUTION]
        elif params[CONFIG_METHOD] == METHODS[6]:
            query[CONFIG_LICENSE] = str(cls.CURRENT_CONFIG[CONFIG_LICENSE])
        elif params[CONFIG_METHOD] == METHODS[12]:
            query[CONFIG_COLOR] = cls.CURRENT_CONFIG[CONFIG_COLOR]
        elif params[CONFIG_METHOD] == METHODS[13]:
            query[CONFIG_CATEGORY] = str(cls.CURRENT_CONFIG[CONFIG_CATEGORY])
        cookies = {
            'AlphaCodersView': 'paged',
            'ResolutionFilter': params[CONFIG_RESOLUTION_FILTER],
            'ResolutionEquals': params[CONFIG_RESOLUTION_EQUALS],
            'Sorting': params[CONFIG_SORT]}
        page = 1
        session = cloudflare.Session(user_agent=cloudflare.UserAgent(mobile=False))
        session.head(URL_BASE)
        while True:
            if not images:
                query['page'] = str(page)
                response = session.get(url, query, cookies=cookies)
                if response:
                    html = minihtml.loads(response.text)
                    images = list(html.find_all('div', _ATTRS_THUMB))
                    has_next = False
                    if (next_page := html.find('a', _ATTRS_NEXT_PAGE)) is not None:
                        has_next = next_page['href'] != '#'
                    elif (pagination := html.find('div', _ATTRS_PAGINATION)) is not None:
                        has_next = pagination[-1].get_data() == 'Next >>'
                    if has_next:
                        page += 1
                if not images:
                    yield
                    continue
            image = images.pop(0)
            image_grid = image[0][0][0][3]
            url_image = image_grid['src'].replace('thumbbig-', '', 1)
            name = image_grid['alt'].removesuffix('HD Wallpaper | Background Image').strip()
            if name:
                name += '-'
            basename = os.path.basename(url_image)
            width, height = map(int, image[1][0][0].get_data().split('x'))
            yield ImageFile(url_image, name + basename, url=request.encode_params(
                URL_INFO, {'i': basename.split('.', 1)[0]}), width=width, height=height)

    @classmethod
    def _on_method(cls, enable_resolution_filter: Callable[[bool], bool],
                   enable_resolution_equals: Callable[[bool], bool], enable_sorting: Callable[[bool], bool],
                   enable_resolution: Callable[[bool], bool], enable_license: Callable[[bool], bool],
                   enable_color: Callable[[bool], bool], enable_category: Callable[[bool], bool], method: str):
        filter_resolution = method not in (METHODS[4], METHODS[6], METHODS[7], METHODS[12])
        enable_resolution_filter(filter_resolution)
        enable_resolution_equals(filter_resolution)
        enable_sorting(method in (METHODS[2], METHODS[3], METHODS[4], METHODS[13]))
        enable_resolution(method == METHODS[4])
        enable_license(method == METHODS[6])
        enable_color(method == METHODS[12])
        enable_category(method == METHODS[13])
