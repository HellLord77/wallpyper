import functools
from typing import Callable
from typing import Iterator
from typing import Optional
from typing import TypedDict

import gui
import validator
from libs import request
from libs import sgml
from . import ImageFile
from . import Source

URL_BASE = 'https://www.wallpaperflare.com'
URL_INDEX = request.join_url(URL_BASE, 'index.php')
URL_SEARCH = request.join_url(URL_BASE, 'search')

CONFIG_SEARCH = 'search'
CONFIG_WALLPAPER = 'wallpaper'
CONFIG_MOBILE = 'mobile'
CONFIG_SORT = 'sort'

SORTS = '', 'relevance'

_CONTENT_END = (
    b'<html lang="en"><head><title>ERROR 404:Page not found</title><meta '
    b'name="viewport" content="width=device-width, initial-scale=1.0, '
    b'maximum-scale=1.0, user-scalable=0" /><meta charset="utf-8"><meta '
    b'http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" /><meta '
    b'name="viewport" content="width=device-width, initial-scale=1.0, '
    b'maximum-scale=1.0, user-scalable=0" /><style>body{margin:0;padding:0;'
    b'background:#F7F7F7;font-family:"Arial","sans-serif"}main{width:304px;'
    b'height:500px;position:absolute;left:50%;top:50%;margin-left:-152px;'
    b'margin-top:-270px;background:url("/public/css/404.png")no-repeat top '
    b'center;text-align:center}p{margin-top:360px;color:#959595;font-size:24px;'
    b'font-family:Helvetica,Arial,sans-serif}a{background:#f37b1d;display:block;'
    b'background:linear-gradient(#f3982a,#f37b1d);box-shadow:inset 0 1px 0 '
    b'rgba(255,255,255,.08),0 1px 0 rgba(255,255,255,.3);text-shadow:0-1px 0 '
    b'rgba(0,0,0,.2);color:#fff;display:block;border:0px solid#C90000;'
    b'border-radius:3px;cursor:pointer;width:304px;height:40px;line-height:40px;'
    b'text-decoration:none;text-align:center}a:hover{background:linear-gradient('
    b'#F45D68,#E54646);background:linear-gradient(#f3a748,#f3883c);color:#fff;'
    b'box-shadow:inset 0 1px 0 rgba(255,255,255,.08),0 1px 0 rgba(255,255,255,.1);'
    b'border:0px solid#C90000}a:active{background:linear-gradient(#f3982a,#f39730);'
    b'box-shadow:inset 0 1px 2px rgba(128,0,0,.3),0 1px 0 rgba(255,255,255,.3);'
    b'line-height:42px}</style></head><body><main align="center"><p>ERROR 404:'
    b'Page not found</p><a role="button" href="https://www.wallpaperflare.com">'
    b'Back to HomePage</a></main></body></html>')
# noinspection HttpUrlsUsage
_ATTRS_ITEM = {
    'itemprop':  'associatedMedia',
    'itemscope': '',
    'itemtype':  'http://schema.org/ImageObject'}
_ATTRS_URL = {'itemprop': 'url'}
_ATTRS_SRC = {'itemprop': 'contentUrl'}


class WallpaperFlare(Source):
    NAME = 'Wallpaper Flare'
    VERSION = '0.0.2'
    URL = URL_BASE
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_SEARCH:    bool,
        CONFIG_WALLPAPER: str,
        CONFIG_MOBILE:    bool,
        CONFIG_SORT:      str})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_SEARCH:    False,
        CONFIG_WALLPAPER: '',
        CONFIG_MOBILE:    False,
        CONFIG_SORT:      SORTS[0]}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_contains, CONFIG_SORT, SORTS)

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
        items = []
        mobile = params.pop(CONFIG_MOBILE)
        if params.pop(CONFIG_SEARCH):
            url = URL_SEARCH
            if mobile:
                params[CONFIG_MOBILE] = 'ok'
            page = 1
        else:
            url = URL_INDEX
            del params[CONFIG_SORT]
            params['c'] = 'main'
            params['m'] = 'portal_loadmore'
            page = 0
        while True:
            if not items:
                params['page'] = str(page)
                response = request.get(url, params)
                if (page != 1 and response.status_code == request.Status.NOT_FOUND
                        and response.content == _CONTENT_END):
                    page = 1
                    continue
                if response:
                    text = response.text
                    if not text:
                        page = 0
                        continue
                    items = list(sgml.loads(
                        f'<html>{text}</html>').find_all('li', _ATTRS_ITEM))
                    page += 1
                if not items:
                    yield
                    continue
            item = items.pop(0)
            url_item = request.join_url(item.find('a', _ATTRS_URL)['href'])
            response = request.get(request.join_url(url_item, 'download'))
            if not response:
                items.insert(0, item)
                yield
                continue
            html = sgml.loads(response.text)
            info = html.find('div', classes='dld_info')
            yield ImageFile(html.find('img', _ATTRS_SRC)['src'], url=url_item, width=int(
                info[0][0].get_data()), height=int(info[1][0].get_data()))

    @classmethod
    def _on_search(cls, enable_mobile: Callable[[bool], bool],
                   enable_sort: Callable[[bool], bool], search: bool):
        enable_mobile(search)
        enable_sort(search)
