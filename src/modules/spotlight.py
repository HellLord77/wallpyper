__version__ = '0.0.1'  # https://github.com/ORelio/Spotlight-Downloader

import base64
import json
from typing import Optional, Generator

import libs.locales as locales
import utils
from langs import LANGUAGE as STRINGS

CONFIG_LOCALE = 'pl'
CONFIG_ORIENTATION = '_orientation'

LOCALES = 'en-US', 'de-DE', 'fr-FR', 'zh-CN', 'es-ES', 'ru-RU', 'en-GB', 'bn-IN', 'da-DK'
ORIENTATIONS = 'landscape', 'portrait'

NAME = 'spotlight'
BASE_URL = utils.join_url('https://arc.msn.com', 'v3', 'Delivery', 'Placement')
DEFAULT_CONFIG = {CONFIG_LOCALE: LOCALES[0],
                  CONFIG_ORIENTATION: ORIENTATIONS[0]}

CONFIG = {}


def fix_config():
    if CONFIG[CONFIG_ORIENTATION] not in ORIENTATIONS:
        CONFIG[CONFIG_ORIENTATION] = DEFAULT_CONFIG[CONFIG_ORIENTATION]


def get_next_wallpaper(**params: str) -> Generator[Optional[utils.Wallpaper], None, None]:
    items: Optional[list] = None
    params['pid'] = '209567'
    params['fmt'] = 'json'
    params['cdm'] = '1'
    params['lo'] = '80217'
    params['ctry'] = CONFIG_LOCALE.split('-')[-1].lower()
    while True:
        if not items:
            response = utils.open_url(BASE_URL, params)
            if response:
                items = response.get_json()['batchrsp']['items']
            if not items:
                yield
                continue
        image = json.loads(items.pop(0)['item'])['ad'][f'image_fullscreen_001_{CONFIG[CONFIG_ORIENTATION]}']
        url = image['u']
        yield utils.Wallpaper(url, utils.set_ext(utils.get_filename(utils.strip_url(url)), 'jpg'),
                              int(image['fileSize']), sha256=base64.b64decode(image['sha256']))


def create_menu():
    utils.add_synced_items(STRINGS.SPOTLIGHT_LABEL_LOCALE, {locale: '\t'.join(locales.Locale.get(
        *locale.split('-')).name.split(' - ')[::-1]) for locale in LOCALES}, CONFIG, CONFIG_LOCALE)
    utils.add_synced_items(STRINGS.SPOTLIGHT_LABEL_ORIENTATION, {orientation: getattr(
        STRINGS, f'SPOTLIGHT_ORIENTATION_{orientation}') for orientation in ORIENTATIONS}, CONFIG, CONFIG_ORIENTATION)
