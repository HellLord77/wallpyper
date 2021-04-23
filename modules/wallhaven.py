import os

import request

NAME = 'WALLHAVEN'
VERSION = '0.0.1'
BASE_URL = 'https://wallhaven.cc/api/v1/'
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


def init():
    # TODO: verify CONFIG, fallback to DEFAULT_CONFIG
    ...


def authenticate(api_key: str) -> bool:
    return request.urlopen(os.path.join(BASE_URL, 'settings'), {'apikey': api_key}, True).status_code == 200
