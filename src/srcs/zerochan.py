import functools
import os
import urllib.parse
from typing import Callable
from typing import Iterator
from typing import Optional
from typing import TypedDict

import gui
import validator
from libs import request
from libs.request import cloudflare
from . import ImageFile
from . import Source

URL_BASE = 'https://www.zerochan.net'

CONFIG_FILTER = 'q'
CONFIG_SORT = 's'
CONFIG_TIME = 't'
CONFIG_DIMENSION = 'd'
CONFIG_COLOR = 'c'
CONFIG_STRICT = 'strict'

SORTS = 'id', 'fav', 'random'
TIMES = 1, 2, 0
DIMENSIONS = '', 'large', 'huge', 'landscape', 'portrait', 'square'
COLORS = '', 'black', 'blue', 'brown', 'green', 'pink', 'purple', 'red', 'white', 'yellow'

_CONTENT_END = (
    b'{}', b'{\r\n  "items": [\r\n\r\n  ]\r\n}\r\n',
    b'{"error": "Page number too high, use `o` (ID offset) instead to paginate. "}')
_PARAMS = {'json': ''}


class ZeroChan(Source):  # https://www.zerochan.net/api
    NAME = 'zerochan'
    VERSION = '0.0.5'
    URL = URL_BASE
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_FILTER: list[str],
        CONFIG_SORT: str,
        CONFIG_TIME: int,
        CONFIG_DIMENSION: str,
        CONFIG_COLOR: str,
        CONFIG_STRICT: bool})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_FILTER: [],
        CONFIG_SORT: SORTS[0],
        CONFIG_TIME: TIMES[2],
        CONFIG_DIMENSION: DIMENSIONS[0],
        CONFIG_COLOR: COLORS[0],
        CONFIG_STRICT: False}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_contains, CONFIG_SORT, SORTS)
        cls._fix_config(validator.ensure_contains, CONFIG_TIME, TIMES)
        cls._fix_config(validator.ensure_contains, CONFIG_DIMENSION, DIMENSIONS)
        cls._fix_config(validator.ensure_contains, CONFIG_COLOR, COLORS)

    @classmethod
    def create_menu(cls):
        enable_time = gui.add_submenu_radio(cls._text(
            'MENU_TIME'), {time: cls._text(f'TIME_{time}')
                           for time in TIMES}, cls.CURRENT_CONFIG, CONFIG_TIME).enable
        on_sort = functools.partial(cls._on_sort, enable_time)
        gui.add_submenu_radio(cls._text('MENU_SORT'), {sort: cls._text(
            f'SORT_{sort}') for sort in SORTS}, cls.CURRENT_CONFIG,
                              CONFIG_SORT, on_click=on_sort, position=0)
        on_sort(cls.CURRENT_CONFIG[CONFIG_SORT])
        gui.add_submenu_radio(cls._text('MENU_DIMENSION'), {
            dimension: cls._text(f'DIMENSION_{dimension}')
            for dimension in DIMENSIONS}, cls.CURRENT_CONFIG, CONFIG_DIMENSION)
        gui.add_submenu_radio(cls._text('MENU_COLOR'), {
            color: cls._text(f'COLOR_{color}')
            for color in COLORS}, cls.CURRENT_CONFIG, CONFIG_COLOR)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        items = []
        url = request.join_url(URL_BASE, ','.join(params.pop(CONFIG_FILTER)))
        time = str(params.pop(CONFIG_TIME))
        if params[CONFIG_SORT] == SORTS[1]:
            params[CONFIG_TIME] = time
        if params.pop(CONFIG_STRICT):
            params['strict'] = ''
        params['json'] = ''
        session = cloudflare.Session()
        page = 1
        while True:
            if not items:
                params['p'] = str(page)
                response = session.get(url, params)
                if (page != 1 and response.status_code == request.Status.OK
                        and response.content in _CONTENT_END):
                    page = 1
                    continue
                if response:
                    items = response.json()['items']
                    page += 1
                if not items:
                    yield
                    continue
            item = items.pop(0)
            url_item = request.join_url(URL_BASE, str(item['id']))
            response = session.get(url_item, _PARAMS)
            if not response:
                items.insert(0, item)
                yield
                continue
            json_item = response.json()
            link = json_item['full']
            yield ImageFile(link, ''.join(urllib.parse.unquote_plus(os.path.basename(
                request.strip_url(link))).rsplit('full.', 1)), url=url_item,
                            width=json_item['width'], height=json_item[
                    'height'], sketchy='Ecchi' in json_item['tags'], md5=json_item['hash'])

    @staticmethod
    def _on_sort(enable: Callable[[bool], bool], sort: str):
        enable(sort == SORTS[1])
