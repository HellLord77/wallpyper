__version__ = '0.0.1'  # https://wallhaven.cc/help/api

from typing import Generator, Optional

import utils

NAME = 'wallhaven'
BASE_URL = utils.join_url('https://wallhaven.cc', 'api', 'v1')
DEFAULT_CONFIG = {
    'apikey': '',
    'q': '',
    'categories': '111',
    'purity': '100',
    'sorting': 'date_added',
    'order': 'desc',
    'topRange': '1M',
    'atleast': '',
    'resolutions': '',
    'ratios': '',
    'colors': '',
    'page': '',
    'seed': ''}

SEARCH_URl = utils.join_url(BASE_URL, 'search')
SETTINGS_URL = utils.join_url(BASE_URL, 'settings')
CONFIG = {}


def fix_config():  # TODO validate & sanitize CONFIG with regex, fallback to DEFAULT_CONFIG
    # ^[01]{3}$
    # ^(desc|asc)$
    ...


def get_next_wallpaper(**params: str) -> Generator[Optional[utils.Wallpaper], None, None]:
    search_datas: Optional[list] = None
    meta = {
        'current_page': 1,
        'last_page': 1,
        'seed': None
    }
    while True:
        if not search_datas:
            params['page'] = str(meta['current_page'] % meta['last_page'] + 1)
            params['seed'] = meta['seed'] or ''
            response = utils.open_url(SEARCH_URl, params)
            if response:
                search_datas, meta = response.get_json().values()
            if not search_datas:
                yield
                continue
        search_data = search_datas.pop(0)
        url = search_data['path']
        yield utils.Wallpaper(url, utils.get_filename(url), search_data['file_size'])


def _authenticate(api_key: str) -> bool:
    return bool(utils.open_url(SETTINGS_URL, {'apikey': api_key}))


def create_menu():
    ...
