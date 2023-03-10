import base64
import json
import os.path
from typing import Iterator, Optional, TypedDict

import gui
import validator
from libs import files, isocodes, request
from . import Source

URL_BASE = request.join('https://arc.msn.com', 'v3', 'Delivery', 'Placement')

CONFIG_LOCALE = 'pl'
CONFIG_ORIENTATION = '_orientation'

LOCALES = 'en-US', 'de-DE', 'fr-FR', 'zh-CN', 'es-ES', 'ru-RU', 'en-GB', 'bn-IN', 'da-DK'
ORIENTATIONS = 'landscape', 'portrait'


class WindowsSpotlight(Source):  # https://github.com/ORelio/Spotlight-Downloader
    NAME = 'Windows Spotlight'
    VERSION = '0.0.1'
    ICON = 'png'
    URL = 'https://en.wikipedia.org/wiki/Windows_Spotlight'
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_LOCALE: str,
        CONFIG_ORIENTATION: str})
    DEFAULT_CONFIG = {
        CONFIG_LOCALE: LOCALES[0],
        CONFIG_ORIENTATION: ORIENTATIONS[0]}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_iterable, CONFIG_LOCALE, LOCALES)
        cls._fix_config(validator.ensure_iterable, CONFIG_ORIENTATION, ORIENTATIONS)

    @classmethod
    def create_menu(cls):
        gui.add_mapped_submenu(cls.strings.SPOTLIGHT_MENU_LOCALE, {locale: isocodes.ISO31661.get(
            locale[locale.find('-') + 1:]).name for locale in LOCALES}, cls.CURRENT_CONFIG, CONFIG_LOCALE)
        gui.add_mapped_submenu(cls.strings.SPOTLIGHT_MENU_ORIENTATION, {orientation: getattr(
            cls.strings, f'SPOTLIGHT_ORIENTATION_{orientation}') for orientation in ORIENTATIONS},
                               cls.CURRENT_CONFIG, CONFIG_ORIENTATION)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[files.File]]:
        items: Optional[list] = None
        params['pid'] = '209567'
        params['fmt'] = 'json'
        params['cdm'] = '1'
        params['lo'] = '80217'
        params['ctry'] = CONFIG_LOCALE.split('-')[-1].lower()
        while True:
            if not items:
                response = request.get(URL_BASE, params=params)
                if response:
                    items = response.json()['batchrsp']['items']
                if not items:
                    yield
                    continue
            image = json.loads(items.pop(0)['item'])['ad'][
                f'image_fullscreen_001_{cls.CURRENT_CONFIG[CONFIG_ORIENTATION]}']
            url = image['u']
            yield files.ImageFile(url, files.replace_ext(os.path.basename(
                request.strip(url)), 'jpg'), int(image['fileSize']), width=int(
                image['w']), height=int(image['h']), sha256=base64.b64decode(image['sha256']))
