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

CONFIG = {}


def sanitize_config():
    # TODO: validate & sanitize CONFIG with regex, fallback to DEFAULT_CONFIG
    ...


def authenticate(api_key: str) -> bool:
    return utils.open_url(utils.join_url(BASE_URL, 'settings'), {'apikey': api_key}, True).status_code == 200
