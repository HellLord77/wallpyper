__version__ = '0.0.1'  # https://www.pexels.com/api/documentation

import os
from typing import Generator, Optional

from libs import files, gui, locales, request
from .module import _Module

BASE_URL = request.join('https://api.pexels.com', 'v1')
SEARCH_URL = request.join(BASE_URL, 'search')
CURATED_URL = request.join(BASE_URL, 'curated')

CONFIG_KEY = 'key'
CONFIG_CURATED = 'curated'
CONFIG_ORIENTATION = 'orientation'
CONFIG_SIZE = 'size'
CONFIG_LOCALE = 'locale'

ORIENTATIONS = '', 'landscape', 'portrait', 'square'
SIZES = '', 'large', 'medium', 'small'
LOCALES = (
    '', 'en-US', 'pt-BR', 'es-ES', 'ca-ES', 'de-DE', 'it-IT', 'fr-FR', 'sv-SE',
    'id-ID', 'pl-PL', 'ja-JP', 'zh-TW', 'zh-CN', 'ko-KR', 'th-TH', 'nl-NL', 'hu-HU', 'vi-VN',
    'cs-CZ', 'da-DK', 'fi-FI', 'uk-UA', 'el-GR', 'ro-RO', 'nb-NO', 'sk-SK', 'tr-TR', 'ru-RU')


def on_curated(curated: bool, menu):
    menu.Enable(not curated)


def _authenticate(key: str) -> bool:
    return bool(response := request.open(SEARCH_URL, {'query': 'people', 'per_page': '1'},
                                         headers={'Authorization': key})) and 'error' not in response.get_json()


class Plexels(_Module):
    NAME = 'Pexels'
    DEFAULT_CONFIG = {
        CONFIG_KEY: '',
        CONFIG_CURATED: False,
        'query': '',
        CONFIG_ORIENTATION: ORIENTATIONS[0],
        CONFIG_SIZE: SIZES[0],
        'color': '',
        CONFIG_LOCALE: LOCALES[0]}

    @classmethod
    def fix_config(cls):
        if not cls.CONFIG[CONFIG_KEY]:
            cls.CONFIG[CONFIG_CURATED] = True
        cls._fix_config(CONFIG_ORIENTATION, ORIENTATIONS)
        cls._fix_config(CONFIG_SIZE, SIZES)
        cls._fix_config(CONFIG_LOCALE, LOCALES)

    @classmethod
    def get_next_wallpaper(cls, **params: str) -> Generator[Optional[files.File], None, None]:
        photos: Optional[list] = None
        key = params.pop(CONFIG_KEY)
        if params.pop(CONFIG_CURATED):
            query_url = CURATED_URL
            params.clear()
        else:
            query_url = SEARCH_URL
        params['page'] = '1'
        params['per_page'] = '80'
        while True:
            if not photos:
                response = request.open(query_url, params, headers={'Authorization': key})
                if response:
                    json = response.get_json()
                    photos = json.get('photos')
                    params['page'] = str(int(params['page']) + bool(json.get('next_page')))
                if not photos:
                    yield
                    continue
            url = photos.pop(0)['src']['original']
            yield files.File(url, os.path.basename(request.strip(url)))

    @classmethod
    def create_menu(cls):
        menu_search = gui.add_submenu(cls.STRINGS.PEXELS_MENU_SEARCH, not cls.CONFIG[CONFIG_CURATED])
        with gui.set_main_menu(menu_search):
            gui.add_mapped_submenu(cls.STRINGS.PEXELS_MENU_ORIENTATION,
                                   {orientation: getattr(cls.STRINGS, f'PEXELS_ORIENTATION_{orientation}')
                                    for orientation in ORIENTATIONS}, cls.CONFIG, CONFIG_ORIENTATION)
            gui.add_mapped_submenu(cls.STRINGS.PEXELS_MENU_SIZE, {size: getattr(cls.STRINGS, f'PEXELS_SIZE_{size}')
                                                                  for size in SIZES}, cls.CONFIG, CONFIG_SIZE)
            gui.add_mapped_submenu(cls.STRINGS.PEXELS_MENU_LOCALE, {locale: locales.Country.get(
                locale[locale.find('-') + 1:]).name if locale else cls.STRINGS.PEXELS_LOCALE_
                                                                    for locale in LOCALES}, cls.CONFIG, CONFIG_LOCALE)
        gui.add_mapped_menu_item(cls.STRINGS.PEXELS_LABEL_CURATED, cls.CONFIG, CONFIG_CURATED,
                                 bool(cls.CONFIG[CONFIG_KEY]), on_curated, (menu_search,))
