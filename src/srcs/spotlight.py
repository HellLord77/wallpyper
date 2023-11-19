import base64
import json
from typing import Iterator
from typing import Optional
from typing import TypedDict

import gui
import validator
from libs import files
from libs import isocodes
from libs import request
from . import ImageFile
from . import Source

URL_BASE = request.join_url('https://arc.msn.com', 'v3', 'Delivery', 'Placement')

CONFIG_ORIENTATION = '_orientation'
CONFIG_LOCALE = 'pl'

ORIENTATIONS = 'landscape', 'portrait'
LOCALES = 'en-US', 'de-DE', 'fr-FR', 'zh-CN', 'es-ES', 'ru-RU', 'en-GB', 'bn-IN', 'da-DK'


class WindowsSpotlight(Source):  # https://github.com/ORelio/Spotlight-Downloader
    NAME = 'Windows Spotlight'
    VERSION = '0.0.1'
    ICON = 'png'
    URL = 'https://en.wikipedia.org/wiki/Windows_Spotlight'
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_ORIENTATION: str,
        CONFIG_LOCALE: str})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_ORIENTATION: ORIENTATIONS[0],
        CONFIG_LOCALE: LOCALES[0]}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_contains, CONFIG_LOCALE, LOCALES)
        cls._fix_config(validator.ensure_contains, CONFIG_ORIENTATION, ORIENTATIONS)

    @classmethod
    def create_menu(cls):
        gui.add_submenu_radio(cls._text('MENU_LOCALE'), {locale: isocodes.ISO31661.get(
            locale[locale.find('-') + 1:]).name for locale in LOCALES}, cls.CURRENT_CONFIG, CONFIG_LOCALE)
        gui.add_submenu_radio(cls._text('MENU_ORIENTATION'), {orientation: cls._text(
            f'ORIENTATION_{orientation}') for orientation in ORIENTATIONS},
                              cls.CURRENT_CONFIG, CONFIG_ORIENTATION)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        items = []
        params['pid'] = '209567'
        params['fmt'] = 'json'
        params['cdm'] = '1'
        params['lo'] = '80217'
        params['ctry'] = 'us'
        while True:
            if not items:
                response = request.get(URL_BASE, params)
                if response:
                    items = response.json()['batchrsp']['items']
                if not items:
                    yield
                    continue
            image = json.loads(items.pop(0)['item'])['ad'][
                f'image_fullscreen_001_{cls.CURRENT_CONFIG[CONFIG_ORIENTATION]}']
            url = image['u']
            yield ImageFile(url, files.replace_ext(request.split_url(
                request.strip_url(url))[-1], 'jpg'), int(image['fileSize']), width=int(
                image['w']), height=int(image['h']), sha256=base64.b64decode(image['sha256']))
