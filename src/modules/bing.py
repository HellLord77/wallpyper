__version__ = '0.0.1'  # https://github.com/timothymctim/Bing-wallpapers

import os.path
from typing import Generator, Optional

import libs.files as files
import libs.locales as locales
import libs.request as request
import utils
from langs import LANGUAGE as STRINGS

NAME = 'bing'
BASE_URL = 'https://www.bing.com'
ARCHIVE_URL = request.join(BASE_URL, 'HPImageArchive.aspx')
IMAGE_URL = request.join(BASE_URL, 'th')

CONFIG_DAY = 'idx'
CONFIG_MARKET = 'mkt'
CONFIG_RESOLUTION = '_resolution'

MAX_DAY = 8
MARKETS = 'de-DE', 'en-AU', 'en-CA', 'en-GB', 'en-IN', 'en-US', 'fr-CA', 'fr-FR', 'ja-JP', 'zh-CN'
RESOLUTIONS = '800x600', '1024x768', '1280x720', '1366x768', '1920x1200', '1920x1080', 'UHD'

DEFAULT_CONFIG = {
    CONFIG_DAY: '0',
    CONFIG_MARKET: MARKETS[5],
    CONFIG_RESOLUTION: RESOLUTIONS[5]}
CONFIG = {}


def fix_config():
    if not int(DEFAULT_CONFIG[CONFIG_DAY]) <= int(CONFIG[CONFIG_DAY]) < MAX_DAY:
        CONFIG[CONFIG_DAY] = DEFAULT_CONFIG[CONFIG_DAY]
    if CONFIG[CONFIG_MARKET] not in MARKETS:
        CONFIG[CONFIG_MARKET] = DEFAULT_CONFIG[CONFIG_MARKET]
    if CONFIG[CONFIG_RESOLUTION] not in RESOLUTIONS:
        CONFIG[CONFIG_RESOLUTION] = DEFAULT_CONFIG[CONFIG_RESOLUTION]


def get_next_wallpaper(**params: str) -> Generator[Optional[files.File], None, None]:
    images: Optional[list] = None
    params['format'] = 'js'
    params['n'] = '8'
    while True:
        if not images:
            images_ = []
            for day in range(int(params[CONFIG_DAY]), MAX_DAY):
                params[CONFIG_DAY] = str(day)
                response = request.open(ARCHIVE_URL, params)
                if response:
                    for image in response.get_json()['images']:
                        if image not in images_:
                            images_.append(image)
                else:
                    break
            else:
                images = images_
            if not images:
                yield
                continue
        query = request.query(images.pop(0)['url'])
        name_ext = os.path.splitext(query['id'][0])
        query['id'][0] = f'{name_ext[0][:name_ext[0].rfind("_") + 1]}{CONFIG[CONFIG_RESOLUTION]}{name_ext[1]}'
        yield files.File(request.encode(IMAGE_URL, query), query['id'][0][4:])


def create_menu():
    utils.add_synced_items(STRINGS.BING_MENU_DAY, {str(day): getattr(
        STRINGS, f'BING_DAY_{day}') for day in range(int(DEFAULT_CONFIG[CONFIG_DAY]), MAX_DAY)}, CONFIG, CONFIG_DAY)
    utils.add_synced_items(STRINGS.BING_MENU_MARKET, {market: '\t'.join(locales.Locale.get(
        *market.split('-')).name.split(' - ')[::-1]) for market in MARKETS}, CONFIG, CONFIG_MARKET)
    utils.add_synced_items(STRINGS.BING_MENU_RESOLUTION, {resolution: getattr(STRINGS, f'BING_RESOLUTION_{resolution}')
                                                          for resolution in RESOLUTIONS}, CONFIG, CONFIG_RESOLUTION)
