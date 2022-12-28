__version__ = '0.0.1'  # https://github.com/timothymctim/Bing-wallpapers

import os.path
from typing import Generator, Optional

import gui
from libs import files, iso_codes, request
from . import Source

URL_BASE = 'https://www.bing.com'
URL_ARCHIVE = request.join(URL_BASE, 'HPImageArchive.aspx')
URL_IMAGE = request.join(URL_BASE, 'th')

CONFIG_DAY = 'idx'
CONFIG_MARKET = 'mkt'
CONFIG_RESOLUTION = '_resolution'

MAX_DAY = 8
MARKETS = 'de-DE', 'en-AU', 'en-CA', 'en-GB', 'en-IN', 'en-US', 'fr-CA', 'fr-FR', 'ja-JP', 'zh-CN'
RESOLUTIONS = '800x600', '1024x768', '1280x720', '1366x768', '1920x1200', '1920x1080', 'UHD'


class _Source(Source):
    NAME = 'Bing Wallpaper'
    DEFAULT_CONFIG = {
        CONFIG_DAY: '0',
        CONFIG_MARKET: MARKETS[5],
        CONFIG_RESOLUTION: RESOLUTIONS[5]}

    @classmethod
    def fix_config(cls):
        if not int(cls.DEFAULT_CONFIG[CONFIG_DAY]) <= int(cls.CONFIG[CONFIG_DAY]) < MAX_DAY:
            cls.CONFIG[CONFIG_DAY] = cls.DEFAULT_CONFIG[CONFIG_DAY]
        cls._fix_config(CONFIG_MARKET, MARKETS)
        cls._fix_config(CONFIG_RESOLUTION, RESOLUTIONS)

    @classmethod
    def get_next_wallpaper(cls, **params: str) -> Generator[Optional[files.File], None, None]:
        images: Optional[list] = None
        params['format'] = 'js'
        params['n'] = '8'
        while True:
            if not images:
                images_ = []
                for day in range(int(params[CONFIG_DAY]), MAX_DAY):
                    params[CONFIG_DAY] = str(day)
                    response = request.open(URL_ARCHIVE, params)
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
            name, ext = os.path.splitext(query['id'][0])
            query['id'][0] = f'{name[:name.rfind("_") + 1]}{cls.CONFIG[CONFIG_RESOLUTION]}{ext}'
            yield files.File(request.encode(URL_IMAGE, query), query['id'][0][4:])

    @classmethod
    def create_menu(cls):
        gui.add_mapped_submenu(cls.STRINGS.BING_MENU_DAY, {str(day): getattr(
            cls.STRINGS, f'BING_DAY_{day}') for day in range(int(cls.DEFAULT_CONFIG[CONFIG_DAY]), MAX_DAY)},
                               cls.CONFIG, CONFIG_DAY)
        gui.add_mapped_submenu(cls.STRINGS.BING_MENU_MARKET, {market: iso_codes.ISO31661.get(
            market[market.find('-') + 1:]).name for market in MARKETS}, cls.CONFIG, CONFIG_MARKET)
        gui.add_mapped_submenu(cls.STRINGS.BING_MENU_RESOLUTION,
                               {resolution: getattr(cls.STRINGS, f'BING_RESOLUTION_{resolution}')
                                for resolution in RESOLUTIONS}, cls.CONFIG, CONFIG_RESOLUTION)
