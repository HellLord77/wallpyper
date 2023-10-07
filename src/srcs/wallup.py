import os
from typing import Iterator
from typing import Optional
from typing import TypedDict

import gui
import validator
from libs import request
from libs import sgml
from . import ImageFile
from . import Source

URL_BASE = 'https://wallup.net'
URL_AJAX = request.join_url(URL_BASE, 'wp-admin', 'admin-ajax.php')

CONFIG_SEARCH = 'search'
CONFIG_CATEGORIES = 'category'
CONFIG_SKETCHY = 'sketchy'
CONFIG_RESOLUTIONS = 'resolution'
CONFIG_SORT = 'orderby'
CONFIG_ORDER = 'order'

CATEGORIES = (
    'abstract-wallpapers', 'landscape-nature-wallpapers', 'animal-wallpapers',
    'anime-wallpaper', 'fantasy-wallpapers', '3d-wallpapers', 'cars-wallpaper',
    'comics-wallpapers', 'cosmos-space-wallpapers', 'funny-wallpapers',
    'game-wallpapers', 'girl-wallpapers', 'holiday-wallpapers', 'love-wallpapers',
    'military-wallpapers', 'mixed-wallpapers', 'movie-wallpapers', 'people-wallpapers')
RESOLUTIONS = (
    '1600x900', '1280x1024', '1600x1200', '1680x1050', '1920x1080', '1920x1200',
    '2560x1440', '2560x1600', '3840x1080', '5760x1080', '3840x2160', '5120x2880')
SORTS = 'date_added', 'post_views_count', 'ratings_average', 'rand'
ORDERS = 'ASC', 'DESC'

_SKETCHY = {
    'sexy', 'cleavage', 'lingerie', 'tongues',
    'underwear', 'erotic', 'boobs', 'bikini', 'ass'}


class Wallup(Source):
    NAME = 'wallup.net'
    VERSION = '0.0.1'
    URL = URL_BASE
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_SEARCH:      str,
        CONFIG_CATEGORIES:  list[str],
        CONFIG_SKETCHY:     bool,
        CONFIG_RESOLUTIONS: list[str],
        CONFIG_SORT:        str,
        CONFIG_ORDER:       str})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_SEARCH:      '',
        CONFIG_CATEGORIES:  [],
        CONFIG_SKETCHY:     False,
        CONFIG_RESOLUTIONS: [],
        CONFIG_SORT:        SORTS[3],
        CONFIG_ORDER:       ORDERS[1]}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_subset, CONFIG_CATEGORIES, CATEGORIES)
        cls._fix_config(validator.ensure_subset, CONFIG_RESOLUTIONS, RESOLUTIONS)
        cls._fix_config(validator.ensure_contains, CONFIG_SORT, SORTS)
        cls._fix_config(validator.ensure_contains, CONFIG_ORDER, ORDERS)

    @classmethod
    def create_menu(cls):
        gui.add_submenu_check(cls._text('MENU_CATEGORIES'), {category: cls._text(
            f'CATEGORY_{category}') for category in CATEGORIES},
                              (None, None), cls.CURRENT_CONFIG, CONFIG_CATEGORIES)
        gui.add_menu_item_check(cls._text('LABEL_SKETCHY'), cls.CURRENT_CONFIG, CONFIG_SKETCHY)
        gui.add_submenu_check(cls._text('MENU_RESOLUTIONS'), {resolution: cls._text(
            resolution, number=True) for resolution in RESOLUTIONS},
                              (None, None), cls.CURRENT_CONFIG, CONFIG_RESOLUTIONS)
        menu_sort = gui.add_submenu_radio(cls._text('MENU_SORT'), {
            sort: cls._text(f'SORT_{sort}') for sort in SORTS},
                                          cls.CURRENT_CONFIG, CONFIG_SORT).get_submenu()
        menu_sort[1].enable(False)
        menu_sort[2].enable(False)
        gui.add_submenu_radio(cls._text('MENU_ORDER'), {order: cls._text(
            f'ORDER_{order}') for order in ORDERS}, cls.CURRENT_CONFIG, CONFIG_ORDER)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        links = []
        tags = []
        params[CONFIG_CATEGORIES] = ','.join(params[CONFIG_CATEGORIES])
        if params.pop(CONFIG_SKETCHY):
            tags.extend(_SKETCHY)
        tags.extend(resolution + '-px' for resolution in params.pop(CONFIG_RESOLUTIONS))
        if params[CONFIG_SORT] in (SORTS[1], SORTS[2]):
            params['meta_key'] = params[CONFIG_SORT]
            params[CONFIG_SORT] = 'meta_value_num'
        params['tag'] = ','.join(tags)
        params['action'] = 'alm_get_posts'
        page = 0
        while True:
            if not links:
                params['page'] = str(page)
                response = request.get(URL_AJAX, params)
                if response:
                    json = response.json()
                    links = list(sgml.loads(f"<html>{json['html']}</html>").find_all('a'))
                    meta = json['meta']
                    page = (page + 1) % (meta['totalposts'] // meta['postcount'])
                if not links:
                    yield
                    continue
            link = links.pop(0)
            img = link[0]
            parts = img['src'].rsplit('-', 1)
            yield ImageFile(parts[0] + os.path.splitext(parts[1])[1], url=link['href'], sketchy=bool(
                _SKETCHY.intersection(tag.casefold() for tag in img['alt'].replace(',', '').split())))
