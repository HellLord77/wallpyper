import functools
from typing import Callable, Iterator, Optional, TypedDict

import gui
import validator
from libs import request, sgml
from . import ImageFile, Source

URL_BASE = 'https://wallpapersmug.com'
URL_SORT = request.join_url(URL_BASE, 'w', 'wallpaper')
URL_TAG = request.join_url(URL_SORT, 'tag')

CONFIG_SEARCH = 'search'
CONFIG_TAG = 'tag'
CONFIG_SORT = 'sort'

TAGS = (
    'abstract', 'animals', 'anime', 'bike', 'birds', 'cars', 'city', 'cute', 'fantasy',
    'flowers', 'food', 'game', 'girls', 'holiday', 'close-up', 'love', 'minimal',
    'movie', 'nature', 'space', 'sports', 'superhero', 'texture', 'tv-series', '')
SORTS = 'latest', 'random', 'popular'


class WallpapersMug(Source):
    VERSION = '0.0.2'
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
        cls._fix_config(validator.ensure_contains, CONFIG_SORT, SORTS)
        cls._fix_config(validator.ensure_contains, CONFIG_TAG, TAGS)

    @classmethod
    def create_menu(cls):
        enable_sort = gui.add_submenu_radio(cls._text(
            'MENU_SORT'), {sort: cls._text(f'SORT_{sort}')
                           for sort in SORTS}, cls.CURRENT_CONFIG, CONFIG_SORT).enable
        cls._on_search(gui.add_submenu_radio(cls._text(
            'MENU_TAG'), {tag: cls._text(f'TAG_{tag}')
                          for tag in TAGS}, cls.CURRENT_CONFIG, CONFIG_TAG,
            on_click=functools.partial(cls._on_tag, enable_sort),
            position=0).enable, enable_sort, cls.CURRENT_CONFIG[CONFIG_SEARCH])

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        images = []
        page = 1
        if params[CONFIG_SEARCH]:
            url = request.encode_params(URL_SORT, {CONFIG_SEARCH: params[CONFIG_SEARCH]})
        elif not params[CONFIG_TAG]:
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
                    html = sgml.loads(response.text)
                    images = list(html.find_all('div', classes='item_img'))
                    if page:
                        if html.find_all('span', classes='next') is None:
                            page = 1
                        else:
                            page += 1
                if not images:
                    yield
                    continue
            image = images.pop(0)
            url_image = request.join_url(URL_BASE, image[0]['href'])
            response_image = request.get(request.join_url(url_image, 'download'))
            if not response_image:
                images.insert(0, image)
                yield
                continue
            img = sgml.loads(response_image.text).find('div', classes='business_img')
            width, height = map(int, img.find(
                'span', classes='yellow-color')[0].get_data().split('x'))
            yield ImageFile(img[0][0]['src'], url=url_image, width=width, height=height)

    @classmethod
    def _on_search(cls, enable_tag, enable_sort, search: str):
        enable_tag(not search)
        cls._on_tag(enable_sort, search=search)

    @classmethod
    def _on_tag(cls, enable: Callable[[bool], bool],
                tag: Optional[str] = None, search: Optional[str] = None):
        enable(not (cls.CURRENT_CONFIG[CONFIG_SEARCH] if search is None else search) and TAGS[
            24] == (cls.CURRENT_CONFIG[CONFIG_TAG] if tag is None else tag))
