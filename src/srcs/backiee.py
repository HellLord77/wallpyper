import functools
import os
from typing import Callable
from typing import Iterator
from typing import Optional
from typing import TypedDict

import gui
import validator
from libs import isocodes
from libs import request
from . import ImageFile
from . import Source

URL_BASE = 'https://backiee.com'
URL_LIST = request.join_url(URL_BASE, 'api', 'wallpaper', 'list.php')

CONFIG_ORIENTATION = '_orientation'
CONFIG_LIST = 'list_type'
CONFIG_RESOLUTIONS = 'resolutions'
CONFIG_SORT = 'sort_by'
CONFIG_CATEGORY = 'category'
CONFIG_POPULAR = 'popular'
CONFIG_SELECTION = 'selection'
CONFIG_COUNTRY = 'country'
CONFIG_RESOLUTION = 'resolution'
CONFIG_PUBLISHER = 'publisher'
CONFIG_SEARCH = 'search'

ORIENTATIONS = 'landscape', 'portrait'
LISTS = (
    'search', 'latest', 'popular', 'category', 'selection',
    'country', 'resolution', 'publisher_list', 'timeline')
RESOLUTIONS = '4k', '5k', '8k'
SORTS = 'popularity', 'downloads', 'date'
CATEGORIES = (
    'all', 'abstract', 'animals', 'anime', 'car', 'celebration', 'city',
    'fantasy', 'flowers', 'food', 'funny', 'life', 'military', 'music',
    'nature', 'quotes', 'romantic', 'space', 'sport', 'technics')
POPULARS = 'daily', 'weekly', 'monthly', 'yearly', 'alltime'
SELECTIONS = (
    'purple', '3d', 'bridge', 'autumn', 'bear', 'castle', 'bench', 'bigcat',
    'bird', 'monochrome', 'blue', 'citylights', 'colorful', 'cute', 'digital',
    'dog', 'dragon', 'dreamcar', 'dreamland', 'road', 'europe', 'fantasyworld',
    'fullmoon', 'futuristicworld', 'halloween', 'easter', 'newyear', 'horse',
    'pier', 'cat', 'lighthouse', 'lightning', 'cottage', 'lonetree', 'macro',
    'christmas', 'usa', 'milkyway', 'neon', 'borealis', 'painting', 'planet',
    'boat', 'desert', 'mountain', 'nationalpark', 'spring', 'starry', 'rose',
    'summer', 'sunset', 'motorbike', 'temple', 'trainsandrails', 'twilight',
    'underwater', 'asia', 'valentine', 'vintagecar', 'waterdrop', 'reflection',
    'waterfall', 'wildlife', 'winter', 'butterfly')
COUNTRY = (
    'AF', 'AL', 'DZ', 'AD', 'AI', 'AQ', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ',
    'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BM', 'BT', 'BO', 'BA', 'BA', 'BW',
    'BR', 'VG', 'BN', 'BG', 'KH', 'CM', 'CA', 'KY', 'CL', 'CN', 'CO', 'CK',
    'CR', 'HR', 'CU', 'CW', 'CY', 'CZ', 'DK', 'DO', 'EC', 'EG', 'EE', 'ET',
    'FO', 'FJ', 'FI', 'FR', 'PF', 'TF', 'GE', 'DE', 'GI', 'GR', 'GL', 'GD',
    'GP', 'GU', 'GT', 'GG', 'GY', 'HU', 'IS', 'IN', 'ID', 'IR', 'IQ', 'IE',
    'IL', 'IT', 'JM', 'JP', 'JE', 'JO', 'KZ', 'KE', 'KI', 'KW', 'KG', 'LA',
    'LV', 'LB', 'LY', 'LI', 'LT', 'LU', 'MG', 'MY', 'MV', 'MT', 'MH', 'MQ',
    'MU', 'YT', 'MX', 'MC', 'MN', 'ME', 'MA', 'MM', 'NA', 'NP', 'NL', 'NC',
    'NZ', 'NI', 'KP', 'MK', 'NO', 'OM', 'PK', 'PW', 'PS', 'PA', 'PG', 'PY',
    'PE', 'PH', 'PL', 'PT', 'PR', 'QA', 'RE', 'RO', 'RU', 'LC', 'VC', 'WS',
    'SM', 'SA', 'SN', 'RS', 'SC', 'SG', 'SX', 'SK', 'SI', 'SO', 'ZA', 'KR',
    'ES', 'LK', 'MF', 'SD', 'SJ', 'SE', 'CH', 'SY', 'TZ', 'TH', 'BS', 'GM',
    'TT', 'TN', 'TR', 'TR', 'TM', 'TC', 'TV', 'VI', 'UG', 'UA', 'AE', 'GB',
    'US', 'UZ', 'VU', 'VA', 'VE', 'VN', 'EH', 'YE', 'ZM', 'ZW')

_CONTENT_END = b'[]'


class Backiee(Source):
    NAME = 'backiee'
    VERSION = '0.0.1'
    ICON = 'png'
    URL = URL_BASE
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_ORIENTATION: str,
        CONFIG_LIST:        str,
        CONFIG_RESOLUTIONS: list[bool],
        CONFIG_SORT:        str,
        CONFIG_CATEGORY:    str,
        CONFIG_POPULAR:     str,
        CONFIG_SELECTION:   str,
        CONFIG_COUNTRY:     str,
        CONFIG_RESOLUTION:  str,
        CONFIG_PUBLISHER:   int,
        CONFIG_SEARCH:      str})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_ORIENTATION: ORIENTATIONS[0],
        CONFIG_LIST:        LISTS[1],
        CONFIG_RESOLUTIONS: [False, False, False],
        CONFIG_SORT:        SORTS[0],
        CONFIG_CATEGORY:    CATEGORIES[0],
        CONFIG_POPULAR:     POPULARS[4],
        CONFIG_SELECTION:   SELECTIONS[0],
        CONFIG_COUNTRY:     COUNTRY[0],
        CONFIG_RESOLUTION:  RESOLUTIONS[0],
        CONFIG_PUBLISHER:   0,
        CONFIG_SEARCH:      ''}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_contains, CONFIG_ORIENTATION, ORIENTATIONS)
        cls._fix_config(validator.ensure_contains, CONFIG_LIST, LISTS)
        cls._fix_config(validator.ensure_len, CONFIG_RESOLUTIONS, 3)
        cls._fix_config(validator.ensure_contains, CONFIG_SORT, SORTS)
        cls._fix_config(validator.ensure_contains, CONFIG_CATEGORY, CATEGORIES)
        cls._fix_config(validator.ensure_contains, CONFIG_POPULAR, POPULARS)
        cls._fix_config(validator.ensure_contains, CONFIG_SELECTION, SELECTIONS)
        cls._fix_config(validator.ensure_contains, CONFIG_COUNTRY, COUNTRY)
        cls._fix_config(validator.ensure_contains, CONFIG_RESOLUTION, RESOLUTIONS)

    @classmethod
    def create_menu(cls):
        gui.add_separator()
        enable_resolutions = gui.add_submenu_check(cls._text('MENU_RESOLUTIONS'), (
            cls._text(f'RESOLUTION_{resolution}') for resolution
            in RESOLUTIONS), (None, None), cls.CURRENT_CONFIG, CONFIG_RESOLUTIONS).enable
        enable_sort = gui.add_submenu_radio(cls._text('MENU_SORT'), {sort: cls._text(
            f'SORT_{sort}') for sort in SORTS}, cls.CURRENT_CONFIG, CONFIG_SORT).enable
        item_category = gui.add_submenu_radio(cls._text('MENU_CATEGORY'), {
            category: cls._text(f'CATEGORY_{category}') for category
            in CATEGORIES}, cls.CURRENT_CONFIG, CONFIG_CATEGORY, on_click=cls._on_category,
                                              args=(gui.MenuItemProperty.MENU,))
        gui.add_separator()
        enable_popular = gui.add_submenu_radio(cls._text('MENU_POPULAR'), {
            popular: cls._text(f'POPULAR_{popular}') for popular
            in POPULARS}, cls.CURRENT_CONFIG, CONFIG_POPULAR).enable
        enable_selection = gui.add_submenu_radio(cls._text('MENU_SELECTION'), {
            selection: cls._text(f'SELECTION_{selection}') for selection
            in SELECTIONS}, cls.CURRENT_CONFIG, CONFIG_SELECTION).enable
        enable_country = gui.add_submenu_radio(cls._text('MENU_COUNTRY'), {
            country: isocodes.ISO31661.get(country).name for country
            in COUNTRY}, cls.CURRENT_CONFIG, CONFIG_COUNTRY).enable
        enable_resolution = gui.add_submenu_radio(cls._text('MENU_RESOLUTION'), {
            resolution: cls._text(f'RESOLUTION_{resolution}') for resolution
            in reversed(RESOLUTIONS)}, cls.CURRENT_CONFIG, CONFIG_RESOLUTION).enable
        on_list = functools.partial(
            cls.on_list, enable_resolutions, enable_sort, item_category.enable,
            enable_popular, enable_selection, enable_country, enable_resolution, item_category)
        gui.add_submenu_radio(cls._text('MENU_LIST'), {
            list_: cls._text(f'LIST_{list_}') for list_ in LISTS}, cls.CURRENT_CONFIG,
                              CONFIG_LIST, on_click=on_list, position=0)
        on_list(cls.CURRENT_CONFIG[CONFIG_LIST])
        gui.add_separator()
        gui.add_submenu_radio(cls._text('MENU_ORIENTATION'), {
            orientation: cls._text(f'ORIENTATION_{orientation}')
            for orientation in ORIENTATIONS}, cls.CURRENT_CONFIG, CONFIG_ORIENTATION)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        wallpapers = []
        list_ = params[CONFIG_LIST]
        for res, check in zip(RESOLUTIONS, params.pop(CONFIG_RESOLUTIONS)):
            params[res] = str(check).lower()
        selection = params.pop(CONFIG_SELECTION)
        country = params.pop(CONFIG_COUNTRY)
        if list_ == LISTS[4]:
            params[CONFIG_CATEGORY] = selection
        elif list_ == LISTS[5]:
            params[CONFIG_CATEGORY] = country
        popular = params.pop(CONFIG_POPULAR)
        resolution = params.pop(CONFIG_RESOLUTION)
        publisher = params.pop(CONFIG_PUBLISHER)
        search = params.pop(CONFIG_SEARCH)
        if list_ == LISTS[2]:
            params['args'] = popular
        elif list_ == LISTS[6]:
            params['args'] = resolution
        elif list_ == LISTS[7]:
            params['args'] = str(publisher)
        elif list_ == LISTS[0]:
            params['args'] = search
        else:
            params['args'] = ''
        params['action'] = 'paging_list'
        params['page_size'] = '30'
        page = 0
        while True:
            if not wallpapers:
                params['page'] = str(page)
                response = request.get(URL_LIST, params)
                if (page != 0 and response.status_code == request.Status.OK
                        and response.content == _CONTENT_END):
                    page = 0
                    continue
                if response:
                    wallpapers = response.json()
                    page += 1
                if not wallpapers:
                    yield
                    continue
            wallpaper = wallpapers.pop(0)
            url = wallpaper['FullPhotoUrl' if (
                    cls.CURRENT_CONFIG[CONFIG_ORIENTATION] == ORIENTATIONS[0]) else 'MobileFullPhotoUrl']
            name = wallpaper['Title'].strip()
            if name:
                name += os.path.splitext(url)[1]
            width, height = map(int, os.path.basename(os.path.dirname(url)).split('x'))
            yield ImageFile(url, name, url=wallpaper['WallpaperUrl'], width=width, height=height)

    @classmethod
    def on_list(cls, enable_resolutions: Callable[[bool], bool], enable_sort: Callable[[bool], bool],
                enable_category: Callable[[bool], bool], enable_popular: Callable[[bool], bool],
                enable_selection: Callable[[bool], bool], enable_country: Callable[[bool], bool],
                enable_resolution: Callable[[bool], bool], item_category: gui.MenuItem, list_: str):
        enable_resolutions(list_ not in (LISTS[6], LISTS[8]))
        enable_sort(list_ not in (LISTS[1], LISTS[2], LISTS[8]))
        enable_category(list_ not in (LISTS[4], LISTS[5], LISTS[8]))
        enable_popular(list_ == LISTS[2])
        enable_selection(list_ == LISTS[4])
        enable_country(list_ == LISTS[5])
        enable_resolution(list_ == LISTS[6])
        cls._on_category('', item_category.get_submenu())

    @classmethod
    def _on_category(cls, _: str, menu: gui.Menu):
        category = cls.CURRENT_CONFIG[CONFIG_LIST] == LISTS[3]
        menu[0].enable(not category)
        if category and cls.CURRENT_CONFIG[CONFIG_CATEGORY] == CATEGORIES[0]:
            item = menu[1]
            item.check()
            item.trigger(gui.MenuItemEvent.LEFT_UP)
