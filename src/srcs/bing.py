import os
from typing import Iterator
from typing import Optional
from typing import TypedDict

import gui
import validator
from libs import isocodes
from libs import request
from . import ImageFile
from . import Source

URL_BASE = 'https://www.bing.com'
URL_ARCHIVE = request.join_url(URL_BASE, 'HPImageArchive.aspx')
URL_IMAGE = request.join_url(URL_BASE, 'th')

CONFIG_RESOLUTION = '_resolution'
CONFIG_DAY = 'idx'
CONFIG_MARKET = 'mkt'

RESOLUTIONS = '800x600', '1024x768', '1280x720', '1366x768', '1920x1200', '1920x1080', 'UHD'
DAYS = range(8)
MARKETS = '', 'de-DE', 'en-AU', 'en-CA', 'en-GB', 'en-IN', 'en-US', 'fr-CA', 'fr-FR', 'ja-JP', 'zh-CN'


class Bing(Source):  # https://github.com/timothymctim/Bing-wallpapers
    NAME = 'Bing'
    VERSION = '0.0.2'
    URL = URL_BASE
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_RESOLUTION: str,
        CONFIG_DAY:        int,
        CONFIG_MARKET:     str})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_RESOLUTION: RESOLUTIONS[5],
        CONFIG_DAY:        next(iter(DAYS)),
        CONFIG_MARKET:     MARKETS[0]}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_contains, CONFIG_DAY, DAYS)
        cls._fix_config(validator.ensure_contains, CONFIG_MARKET, MARKETS)
        cls._fix_config(validator.ensure_contains, CONFIG_RESOLUTION, RESOLUTIONS)

    @classmethod
    def create_menu(cls):
        gui.add_submenu_radio(cls._text('MENU_DAY'), {day: cls._text(
            f'DAY_{day}') for day in DAYS}, cls.CURRENT_CONFIG, CONFIG_DAY)
        gui.add_submenu_radio(cls._text('MENU_MARKET'), {market: isocodes.ISO31661.get(
            market[market.find('-') + 1:]).name if market else cls._text(
            'MARKET_') for market in MARKETS}, cls.CURRENT_CONFIG, CONFIG_MARKET)
        gui.add_submenu_radio(cls._text('MENU_RESOLUTION'), {resolution: cls._text(
            f'RESOLUTION_{resolution}') for resolution in RESOLUTIONS},
                              cls.CURRENT_CONFIG, CONFIG_RESOLUTION)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        images = []
        params['format'] = 'js'
        params['n'] = '7'
        day = 0
        while True:
            if not images:
                params[CONFIG_DAY] = str(day)
                response = request.get(URL_ARCHIVE, params)
                if response:
                    images = response.json()['images']
                    day %= DAYS.stop
                if not images:
                    yield
                    continue
            query = request.extract_params(images.pop(0)['url'])
            name, ext = os.path.splitext(query['id'][0])
            resolution = cls.CURRENT_CONFIG[CONFIG_RESOLUTION]
            query['id'][0] = f'{name[:name.rfind("_") + 1]}{resolution}{ext}'
            width, height = (0, 0) if resolution == RESOLUTIONS[6] else map(int, resolution.split('x'))
            yield ImageFile(request.Request(request.Method.GET, URL_IMAGE, params=query),
                            query['id'][0][4:], width=width, height=height)
