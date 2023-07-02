import functools
import os
from typing import Callable, Iterator, Optional, TypedDict

import gui
import validator
from libs import request, sgml
from . import ImageFile, Source

URL_BASE = 'https://wallpapertip.com'
URL_SEARCH = request.join_url(URL_BASE, 'search.html')
URL_IMAGE = request.join_url(URL_BASE, 'wmimgs')

CONFIG_MODE = 'mode'
CONFIG_SEARCH = 'k'
CONFIG_RESOLUTION = 'resolution'
CONFIG_DEVICE = 'm'
CONFIG_COLOR = 'color'

MODES = 'top', 'search'
RESOLUTIONS = (
    '1', '2', '3', '4', '6', '8', '9', '10',
    '11', '12', '13', '14', '16', '19', '21', '')
DEVICES = 'c', 'p', 'm', ''
COLORS = (
    'red', 'orange', 'yellow', 'green', 'turquoise', 'blue',
    'lilac', 'pink', 'white', 'gray', 'black', 'brown', '')

_FMT_TOP = f'{URL_BASE}/top/{{}}/'
_FMT_PICTURE = f'{URL_BASE}/wpic/{{}}_{{}}/'


class WallpaperTip(Source):
    VERSION = '0.0.1'
    URL = URL_BASE
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_MODE: str,
        CONFIG_SEARCH: str,
        CONFIG_RESOLUTION: str,
        CONFIG_DEVICE: str,
        CONFIG_COLOR: str})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_MODE: MODES[0],
        CONFIG_SEARCH: '',
        CONFIG_RESOLUTION: RESOLUTIONS[15],
        CONFIG_DEVICE: DEVICES[3],
        CONFIG_COLOR: COLORS[12]}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_contains, CONFIG_MODE, MODES)
        cls._fix_config(validator.ensure_contains, CONFIG_RESOLUTION, RESOLUTIONS)
        cls._fix_config(validator.ensure_contains, CONFIG_DEVICE, DEVICES)
        cls._fix_config(validator.ensure_contains, CONFIG_COLOR, COLORS)

    @classmethod
    def create_menu(cls):
        gui.add_separator()
        enable_resolution = gui.add_submenu_radio(cls._text('MENU_RESOLUTION'), {
            resolution: cls._text(f'RESOLUTION_{resolution}') for resolution
            in RESOLUTIONS}, cls.CURRENT_CONFIG, CONFIG_RESOLUTION).enable
        enable_device = gui.add_submenu_radio(cls._text('MENU_DEVICE'), {
            device: cls._text(f'DEVICE_{device}') for device
            in DEVICES}, cls.CURRENT_CONFIG, CONFIG_DEVICE).enable
        enable_color = gui.add_submenu_radio(cls._text('MENU_COLOR'), {
            color: cls._text(f'COLOR_{color}') for color
            in COLORS}, cls.CURRENT_CONFIG, CONFIG_COLOR).enable
        on_mode = functools.partial(
            cls._on_mode, enable_resolution, enable_device, enable_color)
        gui.add_submenu_radio(cls._text('MENU_MODE'), {mode: cls._text(
            f'MODE_{mode}') for mode in MODES}, cls.CURRENT_CONFIG,
                              CONFIG_MODE, on_click=on_mode, position=0)
        on_mode(cls.CURRENT_CONFIG[CONFIG_MODE])

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        items = []
        search = MODES[1] == params.pop(CONFIG_MODE)
        if not search:
            params.clear()
        page = 1
        while True:
            if not items:
                params['page'] = str(page)
                response = request.get(URL_SEARCH if search else
                                       _FMT_TOP.format(params.pop('page')), params)
                if response:
                    html = sgml.loads(response.text)
                    items = list(html.find_all('div', classes='item'))
                    if html.find('a', text='Next') is None:
                        page = 1
                    else:
                        if search:
                            page %= 50
                        page += 1
                if not items:
                    yield
                    continue
            item = items.pop(0)
            link = item[0]
            path = request.split_url(link[0]['data-original'])[-1]
            name = path.split('_', 1)[1]
            width, height = map(int, item[1][1][0].get_text().split('x'))
            yield ImageFile(request.join_url(URL_IMAGE, path), name, url=_FMT_PICTURE.format(
                request.split_url(link['href'])[-1].split('_', 1)[0], os.path.splitext(name)[0]),
                            width=width, height=height)

    @classmethod
    def _on_mode(cls, enable_resolution: Callable[[bool], bool],
                 enable_device: Callable[[bool], bool],
                 enable_color: Callable[[bool], bool], mode: str):
        search = mode == MODES[1]
        enable_resolution(search)
        enable_device(search)
        enable_color(search)
