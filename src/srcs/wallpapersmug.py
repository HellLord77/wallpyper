import functools
from typing import Callable, Iterator, Optional, TypedDict

import gui
import validator
from libs import files, request, minihtml
from . import Source

_ATTRS_IMAGES = {'class': 'item_img'}
_ATTRS_NEXT = {'class': 'page next'}
_ATTRS_IMAGE = {'class': 'business_img'}
_ATTRS_RESOLUTION = {'class': 'yellow-color'}

URL_BASE = 'https://wallpapersmug.com'
URL_SORT = request.join_url(URL_BASE, 'w', 'wallpaper')
URL_TAG = request.join_url(URL_SORT, 'tag')

CONFIG_SEARCH = 'search'
CONFIG_TAG = 'tag'
CONFIG_SORT = 'sort'

TAGS = ('abstract', 'animals', 'anime', 'bike', 'birds', 'cars', 'city', 'cute', 'fantasy',
        'flowers', 'food', 'game', 'girls', 'holiday', 'close-up', 'love', 'minimal',
        'movie', 'nature', 'space', 'sports', 'superhero', 'texture', 'tv-series', '')
SORTS = 'latest', 'random', 'popular'


class WallpapersMug(Source):
    VERSION = '0.0.1'
    URL = URL_BASE
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_SEARCH: str,
        CONFIG_TAG: str,
        CONFIG_SORT: str})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_SEARCH: '',
        CONFIG_TAG: TAGS[24],
        CONFIG_SORT: SORTS[0]}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_iterable, CONFIG_SORT, SORTS)
        cls._fix_config(validator.ensure_iterable, CONFIG_TAG, TAGS)

    @classmethod
    def create_menu(cls):
        enable_sort = gui.add_submenu_radio(cls.STRINGS.WALLPAPERSMUG_MENU_SORT, {
            sort: getattr(cls.STRINGS, f'WALLPAPERSMUG_SORT_{sort}')
            for sort in SORTS}, cls.CURRENT_CONFIG, CONFIG_SORT).enable
        cls._on_search(gui.add_submenu_radio(cls.STRINGS.WALLPAPERSMUG_MENU_TAG, {
            tag: getattr(cls.STRINGS, f'WALLPAPERSMUG_TAG_{tag}')
            for tag in TAGS}, cls.CURRENT_CONFIG, CONFIG_TAG, on_click=functools.partial(
            cls._on_tag, enable_sort), position=0).enable, enable_sort,
                       cls.CURRENT_CONFIG[CONFIG_SEARCH])

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[files.File]]:
        images: Optional[list] = None
        page = 1
        if params[CONFIG_SEARCH]:
            url = request.encode_params(URL_SORT, {CONFIG_SEARCH: params[CONFIG_SEARCH]})
        elif params[CONFIG_TAG] == TAGS[24]:
            if (sort := params[CONFIG_SORT]) == SORTS[1]:
                page = 0
            url = request.join_url(URL_SORT, sort)
        else:
            url = request.join_url(URL_TAG, params[CONFIG_TAG])
        while True:
            if not images:
                if page:
                    url = request.join_url(url, 'page', str(page))
                response = request.get(url)
                if response:
                    html = minihtml.loads(response.text)
                    images = list(html.find_all('div', _ATTRS_IMAGES))
                    if page and html.find_all('span', _ATTRS_NEXT) is not None:
                        page += 1
                if not images:
                    yield
                    continue
            image = images.pop(0)
            response_image = request.get(request.join_url(
                URL_BASE, image.get_child().attributes['href'], 'download'))
            if not response_image:
                images.insert(0, image)
                yield
                continue
            img = minihtml.loads(response_image.text).find('div', _ATTRS_IMAGE)
            width, height = map(int, img.find(
                'span', _ATTRS_RESOLUTION).get_child().get_data().strip().split('x'))
            yield files.ImageFile(img.get_child().get_child().attributes[
                                      'src'], width=width, height=height)

    @classmethod
    def _on_search(cls, enable_tag, enable_sort, search: str):
        enable_tag(not search)
        cls._on_tag(enable_sort, search=search)

    @classmethod
    def _on_tag(cls, enable: Callable[[bool], bool], tag: Optional[str] = None, search: Optional[str] = None):
        enable(not (cls.CURRENT_CONFIG[CONFIG_SEARCH] if search is None else search) and TAGS[
            24] == (cls.CURRENT_CONFIG[CONFIG_TAG] if tag is None else tag))
