import os
from typing import Iterator, Optional, TypedDict

import gui
import validator
from libs import request
from . import File, Source

URL_LIST = request.join_url('https://wallpaper.sapphire.microsoftapp.net',
                            'api', 'v1', 'app', 'photo', 'list', 'bing')

CONFIG_QUALITY = '_quality'

QUALITIES = 'small', 'full', 'large', 'raw'


class BingSapphire(Source):
    NAME = 'Bing Wallpaper'
    VERSION = '0.0.1'
    URL = 'https://bing.com'
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_QUALITY: str})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_QUALITY: QUALITIES[3]}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_contains, CONFIG_QUALITY, QUALITIES)

    @classmethod
    def create_menu(cls):
        gui.add_submenu_radio(cls._text('MENU_QUALITY'), {quality: cls._text(
            f'QUALITY_{quality}') for quality in QUALITIES}, cls.CURRENT_CONFIG, CONFIG_QUALITY)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[File]]:
        data = []
        page = 1
        while True:
            if not data:
                response = request.get(request.join_url(URL_LIST, str(page)))
                if response:
                    json = response.json()
                    if json['code'] == 0:
                        data = json['data']
                        if data:
                            page += 1
                        else:
                            page = 1
                            continue
                if not data:
                    yield
                    continue
            wallpaper = data.pop(0)
            url = wallpaper['urls'][cls.CURRENT_CONFIG[CONFIG_QUALITY]]
            yield File(url, f'{wallpaper["title"]}{os.path.splitext(url)[1]}')
