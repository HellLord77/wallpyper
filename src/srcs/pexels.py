import functools
import os
from typing import Generator, Optional

import gui
from libs import files, isocodes, urls
from . import Source

URL_BASE = urls.join('https://api.pexels.com', 'v1')
URL_CURATED = urls.join(URL_BASE, 'curated')
URL_SEARCH = urls.join(URL_BASE, 'search')

CONFIG_KEY = 'key'
CONFIG_CURATED = 'curated'
CONFIG_ORIENTATION = 'orientation'
CONFIG_SIZE = 'size'
CONFIG_COLOR = 'color'
CONFIG_LOCALE = 'locale'

ORIENTATIONS = '', 'landscape', 'portrait', 'square'
SIZES = '', 'large', 'medium', 'small'
COLORS = (
    '', 'red', 'orange', 'yellow', 'green', 'turquoise', 'blue', 'violet', 'pink', 'brown', 'black', 'gray', 'white')
LOCALES = (
    '', 'en-US', 'pt-BR', 'es-ES', 'ca-ES', 'de-DE', 'it-IT', 'fr-FR', 'sv-SE',
    'id-ID', 'pl-PL', 'ja-JP', 'zh-TW', 'zh-CN', 'ko-KR', 'th-TH', 'nl-NL', 'hu-HU', 'vi-VN',
    'cs-CZ', 'da-DK', 'fi-FI', 'uk-UA', 'el-GR', 'ro-RO', 'nb-NO', 'sk-SK', 'tr-TR', 'ru-RU')


def on_curated(menu: gui.MenuItem, curated: bool):
    menu.enable(not curated)


def _authenticate(key: str) -> bool:
    return bool(urls.open(URL_CURATED, {'per_page': '1'}, headers={urls.Header.AUTHORIZATION: key}))


class Pexels(Source):  # https://www.pexels.com/api/documentation
    VERSION = '0.0.2'
    URL = 'https://www.pexels.com'
    DEFAULT_CONFIG = {
        CONFIG_KEY: '',
        CONFIG_CURATED: False,
        'query': '',
        CONFIG_ORIENTATION: ORIENTATIONS[0],
        CONFIG_SIZE: SIZES[0],
        CONFIG_COLOR: COLORS[0],
        CONFIG_LOCALE: LOCALES[0]}

    @classmethod
    def fix_config(cls):
        cls._fix_config(CONFIG_ORIENTATION, ORIENTATIONS)
        cls._fix_config(CONFIG_SIZE, SIZES)
        cls._fix_config(CONFIG_COLOR, COLORS)
        cls._fix_config(CONFIG_LOCALE, LOCALES)

    @classmethod
    def get_next_wallpaper(cls, **params) -> Generator[Optional[files.File], None, None]:
        photos: Optional[list] = None
        headers = {urls.Header.AUTHORIZATION: params.pop(CONFIG_KEY)}
        if params.pop(CONFIG_CURATED):
            query_url = URL_CURATED
            params.clear()
        else:
            query_url = URL_SEARCH
        params['page'] = '1'
        params['per_page'] = '80'
        while True:
            if not photos:
                response = urls.open(query_url, params, headers=headers)
                if response:
                    json = response.get_json()
                    photos = json.get('photos')
                    params['page'] = str(int(params['page']) + 1) if json.get('next_page') else '1'
                if not photos:
                    yield
                    continue
            url = photos.pop(0)['src']['original']
            yield files.File(url, os.path.basename(urls.strip(url)))

    @classmethod
    def create_menu(cls):
        item_search = gui.add_submenu(cls.strings.PEXELS_MENU_SEARCH, not cls.CURRENT_CONFIG[CONFIG_CURATED])
        gui.add_mapped_menu_item(cls.strings.PEXELS_LABEL_CURATED, cls.CURRENT_CONFIG, CONFIG_CURATED,
                                 on_click=functools.partial(on_curated, item_search), position=0)
        with gui.set_menu(item_search):
            gui.add_mapped_submenu(cls.strings.PEXELS_MENU_ORIENTATION,
                                   {orientation: getattr(cls.strings, f'PEXELS_ORIENTATION_{orientation}')
                                    for orientation in ORIENTATIONS}, cls.CURRENT_CONFIG, CONFIG_ORIENTATION)
            gui.add_mapped_submenu(cls.strings.PEXELS_MENU_SIZE, {size: getattr(
                cls.strings, f'PEXELS_SIZE_{size}') for size in SIZES}, cls.CURRENT_CONFIG, CONFIG_SIZE)
            gui.add_mapped_submenu(cls.strings.PEXELS_MENU_COLOR, {color: getattr(
                cls.strings, f'PEXELS_COLOR_{color}') for color in COLORS}, cls.CURRENT_CONFIG, CONFIG_COLOR)
            gui.add_mapped_submenu(cls.strings.PEXELS_MENU_LOCALE, {locale: isocodes.ISO31661.get(
                locale[locale.find('-') + 1:]).name if locale else cls.strings.PEXELS_LOCALE_
                                                                    for locale in LOCALES}, cls.CURRENT_CONFIG, CONFIG_LOCALE)
