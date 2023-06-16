import functools
import sys
from typing import Iterator, Optional, TypedDict

import gui
import validator
from libs import request, sgml
from . import CONFIG_ORIENTATIONS, ImageFile, Source

URL_BASE = 'https://www.besthdwallpaper.com'
URL_DETAILS = request.join_url(URL_BASE, 'Wallpaper', 'WallpaperDetail')

CONFIG_SEARCH = 'q'
CONFIG_SORT = 'sortBy'
CONFIG_CATEGORY = 'fCategoryID'
CONFIG_RESOLUTION = 'fResolution'

SORTS = 'recent', 'popular', 'downloaded'
CATEGORIES = (
    '', '40', '41', '156', '73', '46', '42', '43', '44', '45', '47', '48', '74', '75', '49', '150', '50', '51', '153',
    '165', '52', '53', '160', '54', '55', '159', '164', '56', '57', '58', '76', '1', '12', '13', '14', '186', '154',
    '111', '15', '16', '152', '59', '17', '72', '18', '19', '22', '167', '20', '21', '151', '2', '193', '191', '189',
    '190', '23', '187', '155', '24', '77', '78', '79', '71', '192', '143', '142', '3', '136', '25', '137', '138', '139',
    '140', '141', '26', '4', '129', '130', '134', '131', '132', '133', '5', '135', '128', '6', '175', '181', '172',
    '174', '170', '171', '176', '168', '173', '185', '180', '169', '179', '177', '178', '127', '114', '112', '7', '110',
    '8', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '9', '162', '28', '29', '161', '144', '145', '146',
    '147', '148', '149', '10', '30', '31', '32', '33', '34', '184', '183', '182', '157', '35', '188', '36', '37', '109',
    '115', '116', '117', '118', '119', '120', '121', '166', '122', '158', '123', '124', '125', '195', '126', '163',
    '11', '82', '39', '83', '84', '85', '38', '86', '87', '88', '97', '89', '81', '90', '91', '92', '93', '94', '95',
    '96', '113', '98', '99', '101', '107', '100', '108', '102', '104', '105', '103', '106', '80', '194')
RESOLUTIONS = '', 'hd-wallpapers', '2k', '4k-uhd', '5k', '6k', '8k-ultra-hd', 'iphone', 'ipad'

_PARAMS = {'lang': 'en-US'}


def _get_resolution(element: sgml.Element) -> tuple[int, int]:
    # noinspection PyTypeChecker
    return tuple(map(int, element[0].get_data().split('x')))


def _key(resolution: tuple[int, int], element: sgml.Element) -> int:
    resolution_ = _get_resolution(element)
    return sys.maxsize if resolution_ == resolution else resolution_[0] * resolution_[1]


class BestHDWallpaper(Source):
    NAME = 'Best HD Wallpaper'
    VERSION = '0.0.2'
    URL = URL_BASE
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_ORIENTATIONS: list[bool],
        CONFIG_SEARCH: str,
        CONFIG_SORT: str,
        CONFIG_CATEGORY: str,
        CONFIG_RESOLUTION: str})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_ORIENTATIONS: [True, True],
        CONFIG_SEARCH: '',
        CONFIG_SORT: SORTS[1],
        CONFIG_CATEGORY: CATEGORIES[0],
        CONFIG_RESOLUTION: RESOLUTIONS[0]}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_len, CONFIG_ORIENTATIONS, 2)
        cls._fix_config(validator.ensure_truthy, CONFIG_ORIENTATIONS, any)
        cls._fix_config(validator.ensure_contains, CONFIG_CATEGORY, CATEGORIES)
        cls._fix_config(validator.ensure_contains,
                        CONFIG_RESOLUTION, RESOLUTIONS)

    @classmethod
    def create_menu(cls):
        gui.add_submenu_radio(cls._text('MENU_SORT'), {sort: cls._text(
            f'SORT_{sort}') for sort in SORTS}, cls.CURRENT_CONFIG, CONFIG_SORT)
        gui.add_submenu_radio(cls._text('MENU_CATEGORY'), {category: cls._text(
            f'CATEGORY_{category}') for category in CATEGORIES}, cls.CURRENT_CONFIG, CONFIG_CATEGORY)
        gui.add_submenu_radio(cls._text('MENU_RESOLUTION'), {resolution: cls._text(
            f'RESOLUTION_{resolution}') for resolution in RESOLUTIONS}, cls.CURRENT_CONFIG, CONFIG_RESOLUTION)
        gui.add_separator()
        gui.add_submenu_check(cls._text('MENU_ORIENTATIONS'), (cls._text(
            f'ORIENTATION_{orientation}') for orientation in range(2)),
                              (1, None), cls.CURRENT_CONFIG, CONFIG_ORIENTATIONS)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        data: Optional[list] = None
        url = request.join_url(
            URL_BASE, f'most-{params.pop(CONFIG_SORT)}-wallpapers')
        params['isJson'] = 'true'
        page = 1
        while True:
            if not data:
                params['currentPage'] = str(page)
                response = request.get(url, params)
                if response:
                    json = response.json()
                    data = json['data']
                    page = page % json['pagingInfo']['pageCount'] + 1
                if not data:
                    yield
                    continue
            photo = data.pop(0)
            response_photo = request.get(request.join_url(
                URL_DETAILS, str(photo['photoID'])), _PARAMS)
            if not response_photo:
                data.insert(0, photo)
                yield
                continue
            option = max(sgml.loads(response_photo.text).find_all('optgroup'),
                         key=functools.partial(_key, (photo['imWidth'], photo['imHeight'])))
            resolution = _get_resolution(option)
            yield ImageFile(option[0]['data-download'], url=request.join_url(
                URL_BASE, photo['detailPageUrl']), width=resolution[0],
                            height=resolution[1], nsfw=photo['isOver18'])
