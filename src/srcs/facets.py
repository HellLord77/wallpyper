import os.path
import os.path
import uuid
from typing import Iterator, Optional, TypedDict

import gui
import validator
from libs import files, request
from . import Source

_SEP = uuid.uuid4().hex
_NFT = []

URL_BASE = request.join('https://facets.api.manifoldxyz.dev', 'art')

CONFIG_YEAR = '_year'
CONFIG_SERIES = '_series'
CONFIG_PURCHASABLE = '_purchasable'
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


def _is_purchasable(id_: int) -> bool:
    for nft in _NFT:
        if id_ == nft['artId']:
            return nft['ownerAddress'] == '0xa52578c6ada18248d95805083ed148957573e4eb'
    return False


class Facets(Source):
    NAME = 'FACETS'
    VERSION = '0.0.1'
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

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_len, CONFIG_YEAR, len(YEARS))
        cls._fix_config(validator.ensure_iterable, CONFIG_SERIES, SERIES)

    @classmethod
    def create_menu(cls):
        for year, item in zip(YEARS, gui.add_submenu_check(
                cls.STRINGS.FACETS_MENU_YEAR, (getattr(
                    cls.STRINGS, f'FACETS_YEAR_{year}') for year in YEARS), (
                        1, None), cls.CURRENT_CONFIG, CONFIG_YEAR).get_submenu()):
            item.set_tooltip(getattr(cls.STRINGS, f'FACETS_TOOLTIP_YEAR_{year}'))
        gui.add_submenu_radio(cls.STRINGS.FACETS_MENU_SERIES, {
            series: getattr(cls.STRINGS, f'FACETS_SERIES_{series}')
            for series in SERIES}, cls.CURRENT_CONFIG, CONFIG_SERIES)
        gui.add_menu_item_check(cls.STRINGS.FACETS_LABEL_PURCHASABLE,
                                cls.CURRENT_CONFIG, CONFIG_PURCHASABLE)
        gui.add_submenu_radio(cls.STRINGS.FACETS_MENU_DEVICE, {
            device: getattr(cls.STRINGS, f'FACETS_DEVICE_{device}')
            for device in DEVICES}, cls.CURRENT_CONFIG, CONFIG_DEVICE)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[files.File]]:
        arts: Optional[list] = None
        while True:
            if not arts:
                response = request.get(URL_BASE)
                if response:
                    json = response.json()
                    arts = [art for art in json['art'] if art['pathThumbnail']]
                    _NFT.extend(json['nft'])
            if not arts:
                yield
                continue
            art = arts.pop(0)
            yield files.File(art[f'path{cls.CURRENT_CONFIG[CONFIG_DEVICE]}'], name=_SEP.join(
                (art['date'], art['series'] or '', str(art['id']),
                 f'{art["name"]}{os.path.splitext(art["pathThumbnail"])[1]}')))

    @classmethod
    def filter_image(cls, image: files.File) -> bool:
        year, series, id_, image.name = image.name.split(_SEP)
        if not cls.CURRENT_CONFIG[CONFIG_YEAR][YEARS.index(int(year))]:
            return False
        if cls.CURRENT_CONFIG[CONFIG_SERIES] not in (SERIES[0], series):
            return False
        if cls.CURRENT_CONFIG[CONFIG_PURCHASABLE] and not _is_purchasable(int(id_)):
            return False
        return True
