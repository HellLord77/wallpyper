import functools
from typing import Callable, Iterator, Optional, TypedDict

import gui
import validator
from libs import request, minihtml
from . import ImageFile, Source

# noinspection HttpUrlsUsage
_ATTRS_ITEM = {
    'itemprop': 'associatedMedia',
    'itemscope': '',
    'itemtype': 'http://schema.org/ImageObject'}
_ATTRS_URL = {'itemprop': 'url'}
_ATTRS_SRC = {'itemprop': 'contentUrl'}
_ATTR_INFO = {'class': 'dld_info'}

URL_BASE = 'https://www.wallpaperflare.com'
URL_INDEX = request.join_url(URL_BASE, 'index.php')
URL_SEARCH = request.join_url(URL_BASE, 'search')

CONFIG_SEARCH = 'search'
CONFIG_WALLPAPER = 'wallpaper'
CONFIG_MOBILE = 'mobile'
CONFIG_SORT = 'sort'

SORTS = '', 'relevance'


class WallpaperFlare(Source):
    NAME = 'Wallpaper Flare'
    VERSION = '0.0.1'
    URL = URL_BASE
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_SEARCH: bool,
        CONFIG_WALLPAPER: str,
        CONFIG_MOBILE: bool,
        CONFIG_SORT: str})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_SEARCH: False,
        CONFIG_WALLPAPER: '',
        CONFIG_MOBILE: False,
        CONFIG_SORT: SORTS[0]}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_iterable, CONFIG_SORT, SORTS)

    @classmethod
    def create_menu(cls):
        enable_sort = gui.add_submenu_radio(cls._text('MENU_SORT'), {
            sort: cls._text(f'SORT_{sort}') for sort in SORTS},
                                            cls.CURRENT_CONFIG, CONFIG_SORT).enable
        on_search = functools.partial(cls._on_search, gui.add_menu_item_check(
            cls._text('LABEL_MOBILE'), cls.CURRENT_CONFIG, CONFIG_MOBILE).enable, enable_sort)
        gui.add_menu_item_check(cls._text(
            'LABEL_SEARCH'), cls.CURRENT_CONFIG, CONFIG_SEARCH, on_click=on_search, position=0)
        on_search(cls.CURRENT_CONFIG[CONFIG_SEARCH])

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        items: Optional[list] = None
        mobile = params.pop(CONFIG_MOBILE)
        if params.pop(CONFIG_SEARCH):
            url = URL_SEARCH
            if mobile:
                params[CONFIG_MOBILE] = 'ok'
            params['page'] = '1'
        else:
            url = URL_INDEX
            params.pop(CONFIG_SORT)
            params['c'] = 'main'
            params['m'] = 'portal_loadmore'
            params['page'] = '0'
        while True:
            if not items:
                response = request.get(url, params)
                if response:
                    items = list(minihtml.loads(
                        f'<html>{response.text}</html>').find_all('li', _ATTRS_ITEM))
                    params['page'] = str(int(params['page']) + 1)
                if not items:
                    yield
                    continue
            item = items.pop(0)
            url_item = request.join_url(item.find('a', _ATTRS_URL)['href'])
            response_item = request.get(request.join_url(url_item, 'download'))
            if not response_item:
                items.insert(0, item)
                yield
                continue
            html = minihtml.loads(response_item.text)
            info = html.find('div', _ATTR_INFO)
            yield ImageFile(html.find('img', _ATTRS_SRC)['src'], url=url_item, width=int(
                info[0][0].get_data()), height=int(info[1][0].get_data()))

    @classmethod
    def _on_search(cls, enable_mobile: Callable[[bool], bool],
                   enable_sort: Callable[[bool], bool], search: bool):
        enable_mobile(search)
        enable_sort(search)
