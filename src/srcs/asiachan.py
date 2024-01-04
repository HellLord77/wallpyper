import functools
import json
import os
import re
import urllib.parse
from typing import Callable
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

URL_BASE = 'https://kpop.asiachan.com'

CONFIG_FILTER = 'q'
CONFIG_SORT = 's'
CONFIG_TIME = 't'

SORTS = 'id', 'fav', 'random'
TIMES = 1, 2, 0

_CONTENT_END = b'{}'
_ATTRS = {'type': 'application/ld+json'}
_RE_HTML = re.compile(r'<div.*</div>', re.DOTALL)


class AsiaChan(Source):
    NAME = 'asiachan'
    VERSION = '0.0.2'
    URL = URL_BASE
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_ORIENTATIONS: list[bool],
        CONFIG_FILTER: list[str],
        CONFIG_SORT: str,
        CONFIG_TIME: int})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_ORIENTATIONS: [True, True],
        CONFIG_FILTER: [],
        CONFIG_SORT: SORTS[1],
        CONFIG_TIME: TIMES[2]}

    @classmethod
    def load_config(cls):
        cls._fix_config(validator.ensure_contains, CONFIG_SORT, SORTS)
        cls._fix_config(validator.ensure_contains, CONFIG_TIME, TIMES)
        super().load_config()

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
        gui.add_separator()
        super().create_menu()

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        items = []
        url = request.join_url(URL_BASE, ','.join(params.pop(CONFIG_FILTER)))
        time = str(params.pop(CONFIG_TIME))
        if params[CONFIG_SORT] == SORTS[1]:
            params[CONFIG_TIME] = time
        params['json'] = ''
        session = cloudflare.Session()
        page = 1
        while True:
            if not items:
                params['p'] = str(page)
                response = session.get(url, params)
                if (page != 1 and response.status_code == request.Status.OK
                        and response.content == _CONTENT_END):
                    page = 1
                    continue
                if response:
                    items = json.loads(_RE_HTML.sub('', response.text, 1))['items']
                    page += 1
                if not items:
                    yield
                    continue
            item = items.pop(0)
            url_item = request.join_url(URL_BASE, str(item['id']))
            response = session.get(url_item)
            if not response:
                items.insert(0, item)
                yield
                continue
            json_item = json.loads(sgml.loads(
                response.text).find('script', _ATTRS).get_data())
            link = json_item['contentUrl']
            yield ImageFile(link, ''.join(urllib.parse.unquote_plus(os.path.basename(
                request.strip_url(link))).rsplit('full.', 1)), url=url_item,
                            width=int(json_item['width'].removesuffix('px')),
                            height=int(json_item['height'].removesuffix('px')),
                            sketchy='Suggestive' in item['tags'])

    @staticmethod
    def _on_sort(enable: Callable[[bool], bool], sort: str):
        enable(sort == SORTS[1])
