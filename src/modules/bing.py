__version__ = '0.0.1'  # https://github.com/timothymctim/Bing-wallpapers

from typing import Optional, Generator

import libs.locales as locales
import utils
from langs import LANGUAGE as STRINGS

CONFIG_DAY = 'idx'
CONFIG_MARKET = 'mkt'
CONFIG_RESOLUTION = '_resolution'

MAX_DAY = 8
MARKETS = 'de-DE', 'en-AU', 'en-CA', 'en-GB', 'en-IN', 'en-US', 'fr-CA', 'fr-FR', 'ja-JP', 'zh-CN'
RESOLUTIONS = '800x600', '1024x768', '1280x720', '1366x768', '1920x1200', '1920x1080', 'UHD'

NAME = 'bing'
BASE_URL = 'https://www.bing.com'
DEFAULT_CONFIG = {
    CONFIG_DAY: '0',
    CONFIG_MARKET: MARKETS[5],
    CONFIG_RESOLUTION: RESOLUTIONS[5]}

ARCHIVE_URL = utils.join_url(BASE_URL, 'HPImageArchive.aspx')
IMAGE_URL = utils.join_url(BASE_URL, 'th')
CONFIG = {}


def fix_config():
    if not int(DEFAULT_CONFIG[CONFIG_DAY]) <= int(CONFIG[CONFIG_DAY]) < MAX_DAY:
        CONFIG[CONFIG_DAY] = DEFAULT_CONFIG[CONFIG_DAY]
    if CONFIG[CONFIG_MARKET] not in MARKETS:
        CONFIG[CONFIG_MARKET] = DEFAULT_CONFIG[CONFIG_MARKET]
    if CONFIG[CONFIG_RESOLUTION] not in RESOLUTIONS:
        CONFIG[CONFIG_RESOLUTION] = DEFAULT_CONFIG[CONFIG_RESOLUTION]


def get_next_wallpaper(**params: str) -> Generator[Optional[utils.Wallpaper], None, None]:
    images: Optional[list] = None
    params['format'] = 'js'
    params['n'] = '8'
    while True:
        if not images:
            images_ = []
            for day in range(int(params[CONFIG_DAY]), MAX_DAY):
                params[CONFIG_DAY] = str(day)
                response = utils.open_url(ARCHIVE_URL, params)
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
        query = utils.query_url(images.pop(0)['url'])
        name_ext = utils.split_filename(query['id'][0])
        query['id'] = f'{name_ext[0][:name_ext[0].rfind("_") + 1]}{CONFIG[CONFIG_RESOLUTION]}{name_ext[1]}'
        yield utils.Wallpaper(utils.encode_url(IMAGE_URL, query), query['id'][4:])


def create_menu():
    utils.add_synced_items(STRINGS.BING_LABEL_DAY, {str(day): getattr(
        STRINGS, f'BING_DAY_{day}') for day in range(int(DEFAULT_CONFIG[CONFIG_DAY]), MAX_DAY)}, CONFIG, CONFIG_DAY)
    utils.add_synced_items(STRINGS.BING_LABEL_MARKET, {market: '\t'.join(locales.Locale.get(
        *market.split('-')).name.split(' - ')[::-1]) for market in MARKETS}, CONFIG, CONFIG_MARKET)
    utils.add_synced_items(STRINGS.BING_LABEL_RESOLUTION, {resolution: getattr(STRINGS, f'BING_RESOLUTION_{resolution}')
                                                           for resolution in RESOLUTIONS}, CONFIG, CONFIG_RESOLUTION)
