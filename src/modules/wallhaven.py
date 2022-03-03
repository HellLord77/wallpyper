__version__ = '0.0.1'

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
    'seed': ''
}

SEARCH_URl = utils.join_url(BASE_URL, 'search')
SETTINGS_URL = utils.join_url(BASE_URL, 'settings')
CONFIG = {}


def fix_config():  # TODO validate & sanitize CONFIG with regex, fallback to DEFAULT_CONFIG
    # ^[01]{3}$
    # ^(desc|asc)$
    ...


def authenticate(api_key: str) -> bool:
    return bool(utils.open_url(SETTINGS_URL, {'apikey': api_key}))


@utils.cache
def _update_search_data(config: dict[str, str]) -> Generator[Optional[utils.Wallpaper], None, None]:
    search_datas = []
    meta = {
        'current_page': 1,
        'last_page': 1,
        'seed': None
    }
    params = config.copy()
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


def get_next_wallpaper() -> Optional[utils.Wallpaper]:
    return next(_update_search_data(CONFIG.copy()))


def create_menu():
    utils.add_item(NAME, on_click=utils.not_implemented, args=(NAME,))
