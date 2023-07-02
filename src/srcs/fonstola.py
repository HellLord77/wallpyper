import colorsys
import functools
from typing import Callable, Iterator, Optional, TypedDict

import gui
import validator
import win32
from libs import colornames, request, sgml
from . import CONFIG_ORIENTATIONS, ImageFile, Source

URL_BASE = 'https://www.fonstola.ru'

CONFIG_LIST = 'list'
CONFIG_SORT = 'sort'
CONFIG_TAGS = 'tags'
CONFIG_COLOR = 'color'
CONFIG_PERIOD = 'period'
CONFIG_CATEGORY = 'category'

LISTS = '', 'topdownload', 'category', 'live', 'random', 'communication'
SORTS = 'date', 'rate', 'view', 'download', 'favorite'
COLORS = (
    '', '000000', '7D7D7D', '870014', 'EC1C23', 'FF7E26', 'FEF100',
    '22B14B', '00A1E7', '3F47CC', 'A349A4', 'FFFFFF', 'C3C3C3', 'B87957',
    'FEAEC9', 'FFC80D', 'EEE3AF', 'B5E61D', '99D9EA', '7092BE', 'C8BFE7')
PERIODS = '', 'today', 'week', 'month', 'year'
CATEGORIES = (
    '3d', 'abstraction', 'aviation', 'anime', 'city', 'girls', 'food',
    'animals', 'games', 'interior', 'space', 'creative', 'macro', 'auto',
    'mini', 'moto', 'men', 'music', 'emotions', 'newyear', 'weapon',
    'landscapes', 'holiday', 'nature', 'other', 'situations', 'sports',
    'textures', 'tech', 'films', 'fantasy', 'flowers')

_FMT_COLOR = 'CMYK: {}\nHSV: {}\nHSL: {}'


def _on_color_right(event):
    win32.clipboard.copy_text(f'#{event.control.get_uid().upper()}')


class Fonstola(Source):
    VERSION = '0.0.2'
    URL = URL_BASE
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_ORIENTATIONS: list[bool],
        CONFIG_LIST: str,
        CONFIG_SORT: str,
        CONFIG_TAGS: str,
        CONFIG_COLOR: str,
        CONFIG_PERIOD: str,
        CONFIG_CATEGORY: str})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_ORIENTATIONS: [True, True],
        CONFIG_LIST: LISTS[0],
        CONFIG_SORT: SORTS[0],
        CONFIG_TAGS: '',
        CONFIG_COLOR: COLORS[0],
        CONFIG_PERIOD: PERIODS[0],
        CONFIG_CATEGORY: CATEGORIES[0]}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_contains, CONFIG_LIST, LISTS)
        cls._fix_config(validator.ensure_contains, CONFIG_SORT, SORTS)
        cls._fix_config(validator.ensure_contains, CONFIG_COLOR, COLORS)
        cls._fix_config(validator.ensure_contains, CONFIG_PERIOD, PERIODS)
        cls._fix_config(validator.ensure_contains, CONFIG_CATEGORY, CATEGORIES)
        super().fix_config(saving)

    @classmethod
    def create_menu(cls):
        gui.add_separator()
        gui.add_submenu_radio(cls._text('MENU_SORT'), {sort: cls._text(
            f'SORT_{sort}') for sort in SORTS}, cls.CURRENT_CONFIG, CONFIG_SORT)
        colors = {color: colornames.get_nearest_color(color)[
            1] if color else cls._text('COLOR_') for color in COLORS}
        for item, color in zip(gui.add_submenu_radio(
                cls._text('MENU_COLOR'), colors,
                cls.CURRENT_CONFIG, CONFIG_COLOR).get_submenu(), COLORS):
            if color:
                rgb = colornames.hex_to_rgb(color)
                srgb = tuple(c / 255 for c in rgb)
                item.set_tooltip(_FMT_COLOR.format(colornames.format_cmyk(
                    *colornames.cmy_to_cmyk(*colornames.srgb_to_cmy(*srgb))),
                    colornames.format_hsv(*colorsys.rgb_to_hsv(*srgb)),
                    colornames.format_hls(*colorsys.rgb_to_hls(*srgb))),
                    f'HEX: #{color.upper()} {rgb}', win32.get_colored_bitmap(*rgb))
                item.bind(gui.MenuItemEvent.RIGHT_UP, _on_color_right)
        gui.add_submenu_radio(cls._text('MENU_PERIOD'), {period: cls._text(
            f'PERIOD_{period}') for period in PERIODS}, cls.CURRENT_CONFIG, CONFIG_PERIOD)
        enable_category = gui.add_submenu_radio(cls._text('MENU_CATEGORY'), {category: cls._text(
            f'CATEGORY_{category}') for category in CATEGORIES}, cls.CURRENT_CONFIG, CONFIG_CATEGORY).enable
        on_list = functools.partial(cls._on_list, enable_category)
        gui.add_submenu_radio(cls._text('MENU_LIST'), {
            list_: cls._text(f'LIST_{list_}') for list_
            in LISTS}, cls.CURRENT_CONFIG, CONFIG_LIST, on_click=on_list, position=0)
        on_list(cls.CURRENT_CONFIG[CONFIG_LIST])
        gui.add_separator()
        super().create_menu()

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        dribbles = []
        category = params.pop(CONFIG_CATEGORY)
        if params[CONFIG_LIST] == LISTS[2]:
            params[CONFIG_LIST] = category
        url = request.encode_params(request.join_url(URL_BASE, params.pop(
            CONFIG_LIST)), {CONFIG_SORT: params.pop(CONFIG_SORT)})
        session = request.Session()
        page = 1
        if any(params.values()):
            if params[CONFIG_COLOR]:
                params[CONFIG_COLOR] = f'#{params[CONFIG_COLOR]}'
            while True:
                response = session.head(URL_BASE)
                if response:
                    for cookie in response.cookies:
                        if cookie.name == 'csrf-token':
                            params['csrf'] = cookie.value
                            break
                    if 'csrf' in params:
                        break
                yield
        else:
            params.clear()
        while True:
            if not dribbles:
                url_page = request.encode_params(url, {'page': str(page)})
                response = session.post(
                    url_page, data=params) if params else session.get(url_page)
                if response:
                    html = sgml.loads(response.text)
                    if (communication := html.find(
                            'div', classes='communication-sidebar')) is not None:
                        communication.parent.children.remove(communication)
                    dribbles = list(html.find_all('a', classes='dribbble-link'))
                    if ((pagination := html.find('ul', classes='pagenation')) and
                            pagination.children[-1][0][0].name == 'i'):
                        page += 1
                    else:
                        page = 1
                if not dribbles:
                    yield
                    continue
            dribble = dribbles.pop(0)
            url_dribble = request.join_url(URL_BASE, dribble['href'])
            response = session.get(url_dribble)
            if not response:
                dribbles.insert(0, dribble)
                yield
                continue
            resolution = sgml.loads(response.text).find(
                'h3', text='Оригинал').get_next_sibling()[0]
            path = resolution['href']
            width, height = map(int, resolution.get_data().split()[0].split('х'))
            yield ImageFile(request.join_url(URL_BASE, path),
                            f'{dribble[0].get_data()}.{path.split(".", 3)[-1]}',
                            url=url_dribble, width=width, height=height)

    @classmethod
    def _on_list(cls, enable_category: Callable[[bool], bool], list_: str):
        enable_category(list_ == LISTS[2])
