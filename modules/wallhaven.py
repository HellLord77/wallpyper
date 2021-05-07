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
SEARCH_DATA = None


def sanitize_config():
    # TODO: validate & sanitize CONFIG with regex, fallback to DEFAULT_CONFIG
    ...


def authenticate(api_key: str) -> bool:
    return utils.open_url(utils.join_url(BASE_URL, 'settings'), {'apikey': api_key}, True).status == utils.ok


def _update_search_data(config: dict[str, str]) -> typing.Generator[str, None, None]:
    search_data = []
    meta = {
        'current_page': 1,
        'last_page': 1,
        'seed': None
    }
    params = config.copy()
    while True:
        if not search_data:
            params['page'] = str(meta['current_page'] % meta['last_page'] + 1)
            params['seed'] = meta['seed'] if meta['seed'] else ''
            response = utils.open_url(SEARCH_URl, params)
            if response.status == utils.ok:
                search_data, meta = response.get_json().values()
            else:
                search_data = [{'path': ''}]
        yield search_data.pop(0)['path']


def get_next_url() -> str:
    global SEARCH_DATA
    if BACKUP_CONFIG != CONFIG:
        SEARCH_DATA = _update_search_data(CONFIG)
        BACKUP_CONFIG.update(CONFIG)
    return next(SEARCH_DATA)


def create_menu():
    utils.add_item(NAME)
