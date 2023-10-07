import json
import os
from typing import Iterator
from typing import Optional
from typing import TypedDict

import gui
import validator
from libs import request
from libs import sgml
from libs.request import cloudflare
from . import CONFIG_ORIENTATIONS
from . import ImageFile
from . import Source

URL_BASE = 'https://stocksnap.io'
URL_PHOTOS = request.join_url(URL_BASE, 'api', 'load-photos')
URL_PHOTO = request.join_url(URL_BASE, 'photo')
URL_DOWNLOAD = request.join_url(URL_PHOTO, 'download')

CONFIG_SORT = 'sort'
CONFIG_ORDER = 'order'

SORTS = 'date', 'trending', 'views', 'downloads', 'favorites'
ORDERS = 'desc', 'asc'

_ATTRS_DOWNLOAD = {'action': '/photo/download'}
_ATTRS_JSON = {'type': 'application/ld+json'}


class StockSnap(Source):
    NAME = 'StockSnap'
    VERSION = '0.0.2'
    ICON = 'png'
    URL = URL_BASE
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_ORIENTATIONS: list[bool],
        CONFIG_SORT:         str,
        CONFIG_ORDER:        str})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_ORIENTATIONS: [True, True],
        CONFIG_SORT:         SORTS[0],
        CONFIG_ORDER:        ORDERS[0]}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_contains, CONFIG_SORT, SORTS)
        cls._fix_config(validator.ensure_contains, CONFIG_ORDER, ORDERS)
        super().fix_config(saving)

    @classmethod
    def create_menu(cls):
        gui.add_submenu_radio(cls._text('MENU_SORT'), {sort: cls._text(
            f'SORT_{sort}') for sort in SORTS}, cls.CURRENT_CONFIG, CONFIG_SORT)
        gui.add_submenu_radio(cls._text('MENU_ORDER'), {order: cls._text(
            f'ORDER_{order}') for order in ORDERS}, cls.CURRENT_CONFIG, CONFIG_ORDER)
        gui.add_separator()
        super().create_menu()

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        results = []
        url = request.join_url(URL_PHOTOS, params[CONFIG_SORT], params[CONFIG_ORDER])
        cookies = {}
        session = cloudflare.Session()
        page = 1
        while True:
            if not results:
                response = session.get(request.join_url(url, str(page)))
                if response:
                    for cookie in session.cookies:
                        if cookie.name == '_csrf':
                            cookies[cookie.name] = cookie.value
                            break
                    data = response.json()
                    results = data['results']
                    if data['nextPage']:
                        page += 1
                    else:
                        page = 1
                if not results:
                    yield
                    continue
            result = results.pop(0)
            url_result = request.join_url(URL_PHOTO, result['img_id'])
            response = session.get(url_result)
            if not response:
                results.insert(0, result)
                yield
                continue
            html = sgml.loads(response.text, sgml.VOID_HTML5)
            data_ = {field['name']: field['value'] for field in html.find(
                'form', _ATTRS_DOWNLOAD).children[:2]}
            name = os.path.basename(json.loads(html.find(
                'script', _ATTRS_JSON).get_data())['contentUrl'])
            yield ImageFile(request.Request(
                request.Method.POST, URL_DOWNLOAD, headers=session.headers,
                data=data_, cookies=cookies), name, url=url_result,
                width=result['img_width'], height=result['img_height'])
