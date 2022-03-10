__version__ = '0.0.1'  # https://wallhaven.cc/help/api

import os.path
from typing import Generator, Optional

import libs.files as files
import libs.request as request

NAME = 'wallhaven'
BASE_URL = request.join('https://wallhaven.cc', 'api', 'v1')
SEARCH_URl = request.join(BASE_URL, 'search')
SETTINGS_URL = request.join(BASE_URL, 'settings')

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
CONFIG = {}


def fix_config():
    # ^[01]{3}$
    ...


def get_next_wallpaper(**params: str) -> Generator[Optional[files.File], None, None]:
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
            response = request.open(SEARCH_URl, params)
            if response:
                search_datas, meta = response.get_json().values()
            if not search_datas:
                yield
                continue
        search_data = search_datas.pop(0)
        url = search_data['path']
        yield files.File(url, os.path.basename(url), search_data['file_size'])


def _authenticate(api_key: str) -> bool:
    return bool(request.open(SETTINGS_URL, {'apikey': api_key}))


def create_menu():
    ...
