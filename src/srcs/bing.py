import os.path
from typing import Iterator, Optional, TypedDict

import gui
import validator
from libs import files, isocodes, request
from . import Source

URL_BASE = 'https://www.bing.com'
URL_ARCHIVE = request.join(URL_BASE, 'HPImageArchive.aspx')
URL_IMAGE = request.join(URL_BASE, 'th')

CONFIG_RESOLUTION = '_resolution'
CONFIG_DAY = 'idx'
CONFIG_MARKET = 'mkt'

RESOLUTIONS = '800x600', '1024x768', '1280x720', '1366x768', '1920x1200', '1920x1080', 'UHD'
DAYS = range(8)
MARKETS = 'de-DE', 'en-AU', 'en-CA', 'en-GB', 'en-IN', 'en-US', 'fr-CA', 'fr-FR', 'ja-JP', 'zh-CN'


class BingWallpaper(Source):  # https://github.com/timothymctim/Bing-wallpapers
    NAME = 'Bing Wallpaper'
    VERSION = '0.0.1'
    URL = URL_BASE
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_RESOLUTION: str,
        CONFIG_DAY: int,
        CONFIG_MARKET: str})
    DEFAULT_CONFIG = {
        CONFIG_RESOLUTION: RESOLUTIONS[5],
        CONFIG_DAY: next(iter(DAYS)),
        CONFIG_MARKET: MARKETS[5]}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_iterable, CONFIG_DAY, DAYS)
        cls._fix_config(validator.ensure_iterable, CONFIG_MARKET, MARKETS)
        cls._fix_config(validator.ensure_iterable, CONFIG_RESOLUTION, RESOLUTIONS)

    @classmethod
    def create_menu(cls):
        gui.add_mapped_submenu(cls.STRINGS.BING_MENU_DAY, {day: getattr(
            cls.STRINGS, f'BING_DAY_{day}') for day in DAYS}, cls.CURRENT_CONFIG, CONFIG_DAY)
        gui.add_mapped_submenu(cls.STRINGS.BING_MENU_MARKET, {market: isocodes.ISO31661.get(
            market[market.find('-') + 1:]).name for market in MARKETS}, cls.CURRENT_CONFIG, CONFIG_MARKET)
        gui.add_mapped_submenu(cls.STRINGS.BING_MENU_RESOLUTION,
                               {resolution: getattr(cls.STRINGS, f'BING_RESOLUTION_{resolution}')
                                for resolution in RESOLUTIONS}, cls.CURRENT_CONFIG, CONFIG_RESOLUTION)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[files.File]]:
        images: Optional[list] = None
        params['format'] = 'js'
        params['n'] = '8'
        while True:
            if not images:
                images_ = []
                for day in range(params[CONFIG_DAY], DAYS.stop):
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
            resolution = cls.CURRENT_CONFIG[CONFIG_RESOLUTION]
            query['id'][0] = f'{name[:name.rfind("_") + 1]}{resolution}{ext}'
            width, height = (0, 0) if RESOLUTIONS[6] == resolution else map(int, resolution.split('x'))
            yield files.ImageFile(request.extend_param(URL_IMAGE, query),
                                  query['id'][0][4:], width=width, height=height)
