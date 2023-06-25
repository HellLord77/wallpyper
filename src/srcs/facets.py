import os
from typing import Iterator, Optional, TypedDict

import gui
import validator
from libs import request
from . import File, Source

URL_BASE = request.join_url('https://facets.api.manifoldxyz.dev', 'art')

CONFIG_YEAR = 'year'
CONFIG_SERIES = 'series'
CONFIG_PURCHASABLE = 'purchasable'
CONFIG_DEVICE = '_device'

YEARS = 2013, 2014, 2022, 2023
SERIES = (
    '', 'Elements', 'Maze', 'Beach Dreams', 'Mirrors', 'Bond', 'Platonics',
    'Beast Dreams', 'Artefacts', 'Hacienda', 'Ghosts', 'Nest', 'Structure',
    'Lux', 'Tangerine Dreams', 'Oracle', 'Crystal Silo', 'Terra', 'Imprism',
    'Edges', 'Mandala', 'Habitats', 'Beast Dreams II', 'Ugly', 'Navigator',
    'Bestia ex Machina', 'Self Care', 'Time', 'Human', 'Helios', 'Personal',
    'Essence', 'Relics', 'The Deep', 'Anima', 'Deus', 'Poem', 'Spores',
    'Drama', 'Liquid Dreams')
DEVICES = '', 'Desktop', 'Mobile'

_OWNER = '0xa52578c6ada18248d95805083ed148957573e4eb'


def _get_json() -> Iterator[dict]:
    etag = ''
    json = {}
    while True:
        response = request.get(URL_BASE)
        if response:
            if etag != (etag := response.headers[request.Header.ETAG]):
                json = response.json()
        else:
            json = {}
        yield json


_GET_JSON = _get_json()


class Facets(Source):
    NAME = 'FACETS'
    VERSION = '0.0.5'
    ICON = 'png'
    URL = 'https://facets.la'
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_YEAR: list[bool],
        CONFIG_SERIES: str,
        CONFIG_PURCHASABLE: bool,
        CONFIG_DEVICE: str})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_YEAR: [True] * len(YEARS),
        CONFIG_SERIES: SERIES[0],
        CONFIG_PURCHASABLE: False,
        CONFIG_DEVICE: DEVICES[1]}

    _purchasable: dict[int, bool]

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_len, CONFIG_YEAR, len(YEARS))
        cls._fix_config(validator.ensure_contains, CONFIG_SERIES, SERIES)

    @classmethod
    def create_menu(cls):
        for year, item in zip(YEARS, gui.add_submenu_check(cls._text(
                'MENU_YEAR'), (cls._text(year) for year in YEARS), (
                1, None), cls.CURRENT_CONFIG, CONFIG_YEAR).get_submenu()):
            item.set_tooltip(cls._text(f'TOOLTIP_YEAR_{year}'))
        gui.add_submenu_radio(cls._text('MENU_SERIES'), {
            series: cls._text(f'SERIES_{series}')
            for series in SERIES}, cls.CURRENT_CONFIG, CONFIG_SERIES)
        gui.add_menu_item_check(cls._text('LABEL_PURCHASABLE'),
                                cls.CURRENT_CONFIG, CONFIG_PURCHASABLE)
        gui.add_separator()
        gui.add_submenu_radio(cls._text('MENU_DEVICE'), {
            device: cls._text(f'DEVICE_{device}')
            for device in DEVICES}, cls.CURRENT_CONFIG, CONFIG_DEVICE)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[File]]:
        arts = []
        while True:
            if not arts:
                json = next(_GET_JSON)
                arts = [art for art in json['art'] if art['pathThumbnail']]
                cls._purchasable = {int(
                    nft['tokenId']): nft['ownerAddress'] == _OWNER for nft in json['nft']}
                if not arts:
                    yield
                    continue
            art = arts.pop(0)
            file = File(art[f'path{cls.CURRENT_CONFIG[CONFIG_DEVICE]}'],
                        name=f'{art["name"]}{os.path.splitext(art["pathThumbnail"])[1]}')
            file._year = int(art['date'])
            file._series = art['series'] or ''
            file._id = art['id']
            yield file

    @classmethod
    def filter_image(cls, image: File) -> bool:
        if ((year := getattr(image, '_year', None)) is not None and
                not cls.CURRENT_CONFIG[CONFIG_YEAR][YEARS.index(year)]):
            return False
        if ((series := getattr(image, '_series', None)) is not None and
                cls.CURRENT_CONFIG[CONFIG_SERIES] not in (SERIES[0], series)):
            return False
        if ((id_ := getattr(image, '_id', None)) is not None and
                cls.CURRENT_CONFIG[CONFIG_PURCHASABLE] and not cls._purchasable[id_]):
            return False
        return True
