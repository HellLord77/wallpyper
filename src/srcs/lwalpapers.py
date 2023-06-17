import random
from typing import Iterator, Optional, TypedDict

import gui
import validator
from libs import request
from . import File, Source

URL_BASE = request.join_url('https://api.github.com', 'repos', 'whoisYoges',
                            'lwalpapers', 'contents', 'wallpapers')

CONFIG_SORT = 'sort'

SORTS = {
    'oldest': lambda x: x,
    'newest': lambda x: reversed(x),
    'smallest': lambda x: sorted(x, key=lambda y: y['size']),
    'largest': lambda x: sorted(x, key=lambda y: y['size'], reverse=True),
    'random': lambda x: random.sample(x, k=len(x))}


def _get_json() -> Iterator[dict]:
    etag = ''
    json = {}
    while True:
        response = request.get(URL_BASE)
        if response:
            if etag != (etag := response.headers[request.Header.ETAG]):
                json = response.json()
        else:
            json = {}
        yield json


_GET_JSON = _get_json()


class Lwalpapers(Source):
    NAME = 'lwalpapers'
    VERSION = '0.0.2'
    ICON = 'png'
    URL = 'https://wallpaper.castorisdead.xyz'
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_SORT: str})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_SORT: tuple(SORTS)[1]}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_contains, CONFIG_SORT, SORTS)

    @classmethod
    def create_menu(cls):
        gui.add_submenu_radio(cls._text('MENU_SORT'), {sort: cls._text(
            f'SORT_{sort}') for sort in SORTS}, cls.CURRENT_CONFIG, CONFIG_SORT)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[File]]:
        tree: Optional[list] = None
        while True:
            if not tree:
                tree = list(SORTS[params[CONFIG_SORT]](next(_GET_JSON)))
                if not tree:
                    yield
                    continue
            file = tree.pop(0)
            yield File(file['download_url'], size=file[
                'size'], url=file['html_url'])
