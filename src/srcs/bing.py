import os.path
from typing import Iterator, Optional

import gui
from libs import files, isocodes, request
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


class BingWallpaper(Source):  # https://github.com/timothymctim/Bing-wallpapers
    NAME = 'Bing Wallpaper'
    VERSION = '0.0.1'
    URL = URL_BASE
    DEFAULT_CONFIG = {
        CONFIG_DAY: '0',
        CONFIG_MARKET: MARKETS[5],
        CONFIG_RESOLUTION: RESOLUTIONS[5]}

    @classmethod
    def fix_config(cls):
        if not int(cls.DEFAULT_CONFIG[CONFIG_DAY]) <= int(cls.CURRENT_CONFIG[CONFIG_DAY]) < MAX_DAY:
            cls.CURRENT_CONFIG[CONFIG_DAY] = cls.DEFAULT_CONFIG[CONFIG_DAY]
        cls._fix_config(CONFIG_MARKET, MARKETS)
        cls._fix_config(CONFIG_RESOLUTION, RESOLUTIONS)

    @classmethod
    def create_menu(cls):
        gui.add_mapped_submenu(cls.strings.BING_MENU_DAY, {str(day): getattr(
            cls.strings, f'BING_DAY_{day}') for day in range(int(cls.DEFAULT_CONFIG[CONFIG_DAY]), MAX_DAY)},
                               cls.CURRENT_CONFIG, CONFIG_DAY)
        gui.add_mapped_submenu(cls.strings.BING_MENU_MARKET, {market: isocodes.ISO31661.get(
            market[market.find('-') + 1:]).name for market in MARKETS}, cls.CURRENT_CONFIG, CONFIG_MARKET)
        gui.add_mapped_submenu(cls.strings.BING_MENU_RESOLUTION,
                               {resolution: getattr(cls.strings, f'BING_RESOLUTION_{resolution}')
                                for resolution in RESOLUTIONS}, cls.CURRENT_CONFIG, CONFIG_RESOLUTION)

    @classmethod
    def get_image(cls, **params: str) -> Iterator[Optional[files.File]]:
        images: Optional[list] = None
        params['format'] = 'js'
        params['n'] = '8'
        while True:
            if not images:
                images_ = []
                for day in range(int(params[CONFIG_DAY]), MAX_DAY):
                    params[CONFIG_DAY] = str(day)
                    response = request.get(URL_ARCHIVE, params=params)
                    if response:
                        for image in response.json()['images']:
                            if image not in images_:
                                images_.append(image)
                    else:
                        break
                else:
                    images = images_
                if not images:
                    yield
                    continue
            query = request.get_params(images.pop(0)['url'])
            name, ext = os.path.splitext(query['id'][0])
            query['id'][0] = f'{name[:name.rfind("_") + 1]}{cls.CURRENT_CONFIG[CONFIG_RESOLUTION]}{ext}'
            yield files.File(request.extend_param(URL_IMAGE, query), query['id'][0][4:])
