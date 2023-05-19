import functools
import json
import re
from typing import Any, Callable, Iterator, Optional, TypedDict

import gui
import validator
from libs import request
from . import ImageFile, Source

_CONTENT_END = (
    b'{\r\n<div style="margin: 100px auto 100px auto; width: 400px; '
    b'text-align: center; "><img src="https://s1.zerochan.net/lost.jpg" '
    b'style="width: 200px; "><br><h2>Page number too high</h2></div>}\r\n')
_PARAMS = {'json': ''}
_RE_HTML = re.compile(r'<div.*</div>', re.DOTALL)

URL_BASE = 'https://www.zerochan.net'

CONFIG_FILTER = 'q'
CONFIG_SORT = 's'
CONFIG_TIME = 't'
CONFIG_DIMENSION = 'd'
CONFIG_COLOR = 'c'
CONFIG_STRICT = 'strict'

SORTS = 'id', 'fav'
TIMES = '1', '2', '0'
DIMENSIONS = '', 'large', 'huge', 'landscape', 'portrait', 'square'
COLORS = '', 'black', 'blue', 'brown', 'green', 'pink', 'purple', 'red', 'white', 'yellow'


def _json_loads(response: request.Response) -> Any:
    return json.loads(_RE_HTML.sub('', response.text, 1).replace(
        'next: ', '"next": ').replace('\\', '\\\\'))


def _on_sort(enable: Callable[[bool], bool], sort: str):
    enable(sort == SORTS[1])


class ZeroChan(Source):  # https://www.zerochan.net/api
    NAME = 'zerochan'
    VERSION = '0.0.1'
    URL = URL_BASE
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_FILTER: str,
        CONFIG_SORT: str,
        CONFIG_TIME: str,
        CONFIG_DIMENSION: str,
        CONFIG_COLOR: str,
        CONFIG_STRICT: bool})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_FILTER: '',
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
        gui.add_submenu_radio(cls._text('MENU_SORT'), {sort: cls._text(
            f'SORT_{sort}') for sort in SORTS}, cls.CURRENT_CONFIG,
                              CONFIG_SORT, on_click=functools.partial(
                _on_sort, enable_time), position=0)
        _on_sort(enable_time, cls.CURRENT_CONFIG[CONFIG_SORT])
        gui.add_submenu_radio(cls._text('MENU_DIMENSION'), {
            dimension: cls._text(f'DIMENSION_{dimension}')
            for dimension in DIMENSIONS}, cls.CURRENT_CONFIG, CONFIG_DIMENSION)
        gui.add_submenu_radio(cls._text('MENU_COLOR'), {
            color: cls._text(f'COLOR_{color}')
            for color in COLORS}, cls.CURRENT_CONFIG, CONFIG_COLOR)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        items: Optional[list] = None
        url = request.join_url(URL_BASE, params.pop(CONFIG_FILTER))
        if params.pop(CONFIG_STRICT):
            params['strict'] = ''
        params['json'] = ''
        page = 1
        while True:
            if not items:
                params['p'] = str(page)
                response = request.get(url, params)
                if (response.status_code == request.Status.FORBIDDEN and
                        response.content == _CONTENT_END):
                    page = 1
                    continue
                if response:
                    items = _json_loads(response)['items']
                    page += 1
                if not items:
                    yield
                    continue
            item = items.pop(0)
            response_item = request.get(request.join_url(URL_BASE, str(item['id'])), _PARAMS)
            if not response_item:
                items.insert(0, item)
                yield
                continue
            json_item = _json_loads(response_item)
            yield ImageFile(json_item['full'], url=request.join_url(URL_BASE, str(
                json_item['id'])), width=json_item['width'], height=json_item['height'],
                            sketchy='Ecchi' in json_item['tags'], md5=json_item['hash'])
