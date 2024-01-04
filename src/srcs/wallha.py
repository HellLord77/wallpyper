import re
from typing import Iterator
from typing import Optional
from typing import TypedDict

import gui
import validator
from libs import request
from libs import sgml
from . import ImageFile
from . import Source

URL_BASE = 'https://wallha.com'

CONFIG_LIST = 'list'
CONFIG_SEARCH = 'q'

LISTS = 'featured', 'latest', 'toplist', 'random', 'search'

_HEADERS = {request.Header.REFERER: URL_BASE}
_ATTRS = {'href': re.compile(request.join_url(URL_BASE, 'download'))}


class Wallha(Source):
    NAME = 'wallha.com'
    VERSION = '0.0.1'
    URL = URL_BASE
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_LIST: str,
        CONFIG_SEARCH: str})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_LIST: LISTS[0],
        CONFIG_SEARCH: ''}

    @classmethod
    def load_config(cls):
        cls._fix_config(validator.ensure_contains, CONFIG_LIST, LISTS)

    @classmethod
    def create_menu(cls):
        gui.add_submenu_radio(cls._text('MENU_LIST'), {list_: cls._text(
            f'LIST_{list_}') for list_ in LISTS}, cls.CURRENT_CONFIG, CONFIG_LIST)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        images = []
        list_ = params.pop(CONFIG_LIST)
        url = request.join_url(URL_BASE, list_)
        search = list_ == LISTS[4]
        if not search:
            del params[CONFIG_SEARCH]
        params['req'] = 'json'
        page = 1
        while True:
            if not images:
                params['page'] = str(page)
                response = request.get(url if search else request.join_url(
                    url, params.pop('page')), params, headers=_HEADERS)
                if page != 1 and response.status_code == request.Status.NOT_FOUND:
                    page = 1
                    continue
                if response:
                    images = response.json()
                    page += 1
                if not images:
                    yield
                    continue
            image = images.pop(0)
            url = image['url']
            response = request.get(url)
            if not response:
                images.insert(0, image)
                yield
                continue
            width, height = map(int, image['res'].split('x'))
            yield ImageFile(sgml.loads(response.text).find('a', _ATTRS)[
                                'href'], url=url, width=width, height=height)
