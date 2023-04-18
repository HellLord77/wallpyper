import functools
import os
from typing import Callable, Iterator, Optional, TypedDict

import gui
import validator
from libs import isocodes, request
from . import File
from . import Source

URL_BASE = request.join_url('https://api.pexels.com', 'v1')
URL_CURATED = request.join_url(URL_BASE, 'curated')
URL_SEARCH = request.join_url(URL_BASE, 'search')

CONFIG_KEY = 'key'
CONFIG_CURATED = 'curated'
CONFIG_ORIENTATION = 'orientation'
CONFIG_SIZE = 'size'
CONFIG_COLOR = 'color'
CONFIG_LOCALE = 'locale'

ORIENTATIONS = '', 'landscape', 'portrait', 'square'
SIZES = '', 'large', 'medium', 'small'
COLORS = (
    '', 'red', 'orange', 'yellow', 'green', 'turquoise',
    'blue', 'violet', 'pink', 'brown', 'black', 'gray', 'white')
LOCALES = (
    '', 'en-US', 'pt-BR', 'es-ES', 'ca-ES', 'de-DE', 'it-IT', 'fr-FR', 'sv-SE',
    'id-ID', 'pl-PL', 'ja-JP', 'zh-TW', 'zh-CN', 'ko-KR', 'th-TH', 'nl-NL', 'hu-HU', 'vi-VN',
    'cs-CZ', 'da-DK', 'fi-FI', 'uk-UA', 'el-GR', 'ro-RO', 'nb-NO', 'sk-SK', 'tr-TR', 'ru-RU')


def _on_curated(enable: Callable[[bool], bool], curated: bool):
    enable(not curated)


def _authenticate(key: str) -> bool:
    return bool(request.get(URL_CURATED, {'per_page': '1'}, headers={request.Header.AUTHORIZATION: key}))


class Pexels(Source):  # https://www.pexels.com/api/documentation
    VERSION = '0.0.2'
    URL = 'https://www.pexels.com'
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_KEY: str,
        CONFIG_CURATED: bool,
        'query': str,
        CONFIG_ORIENTATION: str,
        CONFIG_SIZE: str,
        CONFIG_COLOR: str,
        CONFIG_LOCALE: str})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_KEY: '',
        CONFIG_CURATED: False,
        'query': '',
        CONFIG_ORIENTATION: ORIENTATIONS[0],
        CONFIG_SIZE: SIZES[0],
        CONFIG_COLOR: COLORS[0],
        CONFIG_LOCALE: LOCALES[0]}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_iterable, CONFIG_ORIENTATION, ORIENTATIONS)
        cls._fix_config(validator.ensure_iterable, CONFIG_SIZE, SIZES)
        cls._fix_config(validator.ensure_iterable, CONFIG_COLOR, COLORS)
        cls._fix_config(validator.ensure_iterable, CONFIG_LOCALE, LOCALES)

    @classmethod
    def create_menu(cls):
        item_search = gui.add_submenu(cls._text('MENU_SEARCH'))
        gui.add_menu_item_check(cls._text('LABEL_CURATED'), cls.CURRENT_CONFIG, CONFIG_CURATED,
                                on_click=functools.partial(_on_curated, item_search.enable), position=0)
        _on_curated(item_search.enable, cls.CURRENT_CONFIG[CONFIG_CURATED])
        with gui.set_menu(item_search):
            gui.add_submenu_radio(cls._text('MENU_ORIENTATION'), {
                orientation: cls._text(f'ORIENTATION_{orientation}')
                for orientation in ORIENTATIONS}, cls.CURRENT_CONFIG, CONFIG_ORIENTATION)
            gui.add_submenu_radio(cls._text('MENU_SIZE'), {size: cls._text(
                f'SIZE_{size}') for size in SIZES}, cls.CURRENT_CONFIG, CONFIG_SIZE)
            gui.add_submenu_radio(cls._text('MENU_COLOR'), {color: cls._text(
                f'COLOR_{color}') for color in COLORS}, cls.CURRENT_CONFIG, CONFIG_COLOR)
            gui.add_submenu_radio(cls._text('MENU_LOCALE'), {locale: isocodes.ISO31661.get(
                locale[locale.find('-') + 1:]).name if locale else cls._text(
                'LOCALE_') for locale in LOCALES}, cls.CURRENT_CONFIG, CONFIG_LOCALE)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[File]]:
        photos: Optional[list] = None
        headers = {request.Header.AUTHORIZATION: params.pop(CONFIG_KEY)}
        if params.pop(CONFIG_CURATED):
            url = URL_CURATED
            params.clear()
        else:
            url = URL_SEARCH
        params['page'] = '1'
        params['per_page'] = '80'
        while True:
            if not photos:
                response = request.get(url, params, headers=headers)
                if response:
                    json = response.json()
                    photos = json.get('photos')
                    params['page'] = str(int(params['page']) + 1) if json.get('next_page') else '1'
                if not photos:
                    yield
                    continue
            url_photo = photos.pop(0)['src']['original']
            yield File(url_photo, os.path.basename(request.strip_url(url_photo)))
