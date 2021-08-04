__version__ = '0.0.1'

import typing

from src import utils

NAME = 'wallhaven'
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
SEARCH_DATA = None


def sanitize_config():  # TODO: validate & sanitize CONFIG with regex, fallback to DEFAULT_CONFIG
    # ^[01]{3}$
    # ^(desc|asc)$
    ...


def authenticate(api_key: str) -> bool:
    return bool(utils.open_url(utils.join_url(BASE_URL, 'settings'), {'apikey': api_key}))


@utils.cache
def _update_search_data(config: dict[str, str]) -> typing.Generator[str, None, None]:
    search_data = []
    meta = {'current_page': 1,
            'last_page': 1,
            'seed': None}
    params = config.copy()
    while True:
        if not search_data:
            params['page'] = str(meta['current_page'] % meta['last_page'] + 1)
            params['seed'] = meta['seed'] or ''
            response = utils.open_url(SEARCH_URl, params)
            if response:
                search_data, meta = response.get_json().values()
            else:
                search_data = [{'path': ''}]
        yield search_data.pop(0)['path']


def get_next_url() -> str:
    return next(_update_search_data(CONFIG))  # TODO: handle no result


def create_menu():
    utils.add_item(NAME, callback=utils.notify, callback_args=(NAME, 'Unimplemented'))
