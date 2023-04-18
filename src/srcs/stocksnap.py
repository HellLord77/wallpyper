import json
import os.path
import os.path
from typing import Iterator, Optional, TypedDict

import gui
import validator
from libs import minihtml, request, utils
from . import ImageFile
from . import Source

_ATTRS_DOWNLOAD = {'action': '/photo/download'}
_ATTRS_JSON = {'type': 'application/ld+json'}

URL_BASE = 'https://stocksnap.io'
URL_PHOTOS = request.join_url(URL_BASE, 'api', 'load-photos')
URL_PHOTO = request.join_url(URL_BASE, 'photo')
URL_DOWNLOAD = request.join_url(URL_PHOTO, 'download')

CONFIG_ORIENTATIONS = '_orientations'
CONFIG_SORT = 'sort'
CONFIG_ORDER = 'order'

SORTS = 'date', 'trending', 'views', 'downloads', 'favorites'
ORDERS = 'desc', 'asc'


class StockSnap(Source):
    NAME = 'StockSnap'
    VERSION = '0.0.1'
    ICON = 'png'
    URL = URL_BASE
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_ORIENTATIONS: list[bool],
        CONFIG_SORT: str,
        CONFIG_ORDER: str})
    DEFAULT_CONFIG = {
        CONFIG_ORIENTATIONS: [True, True],
        CONFIG_SORT: SORTS[0],
        CONFIG_ORDER: ORDERS[0]}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_len, CONFIG_ORIENTATIONS, 2)
        cls._fix_config(validator.ensure_truthy, CONFIG_ORIENTATIONS, any)
        cls._fix_config(validator.ensure_iterable, CONFIG_SORT, SORTS)
        cls._fix_config(validator.ensure_iterable, CONFIG_ORDER, ORDERS)

    @classmethod
    def create_menu(cls):
        gui.add_submenu_radio(cls._text('MENU_SORT'), {sort: cls._text(
            f'SORT_{sort}') for sort in SORTS}, cls.CURRENT_CONFIG, CONFIG_SORT)
        gui.add_submenu_radio(cls._text('MENU_ORDER'), {order: cls._text(
            f'ORDER_{order}') for order in ORDERS}, cls.CURRENT_CONFIG, CONFIG_ORDER)
        gui.add_separator()
        gui.add_submenu_check(cls._text('MENU_ORIENTATIONS'), (cls._text(
            f'ORIENTATION_{orientation}') for orientation in range(2)),
                              (1, None), cls.CURRENT_CONFIG, CONFIG_ORIENTATIONS)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        results: Optional[list] = None
        session = request.Session()
        url = request.join_url(URL_PHOTOS, params[CONFIG_SORT], params[CONFIG_ORDER])
        cookies = {}
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
            response_result = session.get(request.join_url(URL_PHOTO, result['img_id']))
            if not response_result:
                results.insert(0, result)
                yield
                continue
            html = minihtml.loads(response_result.text)
            data_ = {field['name']: field['value'] for field in html.find(
                'form', _ATTRS_DOWNLOAD).children[:2]}
            name = os.path.basename(json.loads(html.find(
                'script', _ATTRS_JSON).get_data())['contentUrl'])
            yield ImageFile(request.Request(
                request.Method.POST, URL_DOWNLOAD, data=data_, cookies=cookies), name,
                width=result['img_width'], height=result['img_height'])

    @classmethod
    def filter_image(cls, image: ImageFile) -> bool:
        if not any(utils.iter_and(cls.CURRENT_CONFIG[CONFIG_ORIENTATIONS], (
                image.is_landscape(), image.is_portrait()))):
            return False
        return True
