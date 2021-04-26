import typing

import utils

__version__ = '0.0.1'

NAME = 'WALLHAVEN'
BASE_URL = 'https://wallhaven.cc/api/v1'
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
    'seed': ''
}

SEARCH_URl = utils.join_url(BASE_URL, 'search')
CONFIG = {}
BACKUP_CONFIG = {}
DEFAULT_DATA = [{'path': ''}]
DEFAULT_META = {
    'current_page': 1,
    'last_page': 1,
    'seed': None
}
SEARCH_DATA = utils.dummy_generator


def sanitize_config():
    # TODO: validate & sanitize CONFIG with regex, fallback to DEFAULT_CONFIG
    ...


def authenticate(api_key: str) -> bool:
    return utils.open_url(utils.join_url(BASE_URL, 'settings'), {'apikey': api_key}, True).status_code == utils.ok


def update_search(config) -> typing.Generator[str, None, None]:
    search_data = []
    meta = DEFAULT_META
    params = config.copy()
    while True:
        if not search_data:
            params['page'] = str(meta['current_page'] % meta['last_page'] + 1)
            params['seed'] = meta['seed']
            response = utils.open_url(SEARCH_URl, params)
            if response.status_code == utils.ok:
                search_data, meta = response.json().values()
            else:
                search_data = DEFAULT_DATA
        yield search_data.pop(0)['path']


def next_wallpaper() -> str:
    global SEARCH_DATA
    if BACKUP_CONFIG != CONFIG:
        SEARCH_DATA = update_search(CONFIG)
        BACKUP_CONFIG.update(CONFIG)
    return next(SEARCH_DATA)
