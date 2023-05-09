import os.path
from typing import Callable, Iterator, Optional, TypedDict

import gui
import validator
import win32
from libs import files, request
from . import File, Source

CONFIG_DIR = 'dir'
CONFIG_RECURSE = 'recursive'
CONFIG_SORT = 'sort_by'
CONFIG_ORDER = 'sort_order'

SORTS = {
    'name': str,
    'size': os.path.getsize,
    'created': os.path.getctime,
    'modified': os.path.getmtime,
    'accessed': os.path.getatime}
ORDERS = 'ascending', 'descending'


class Folder(Source):
    NAME = 'Folder [local]'
    VERSION = '0.0.2'
    ICON = 'png'
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_DIR: str,
        CONFIG_RECURSE: bool,
        CONFIG_SORT: str,
        CONFIG_ORDER: str})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_DIR: win32.PICTURES_DIR,
        CONFIG_RECURSE: True,
        CONFIG_SORT: next(iter(SORTS)),
        CONFIG_ORDER: ORDERS[0]}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_disk, CONFIG_DIR, False)
        cls._fix_config(validator.ensure_iterable, CONFIG_SORT, SORTS)
        cls._fix_config(validator.ensure_iterable, CONFIG_ORDER, ORDERS)

    @classmethod
    def create_menu(cls):
        gui.add_menu_item(cls._text('MENU_DIR'), on_click=cls._on_dir, args=(
            gui.MenuItemMethod.SET_TOOLTIP,)).set_tooltip(cls.CURRENT_CONFIG[CONFIG_DIR])
        gui.add_menu_item_check(cls._text('MENU_RECURSE'), cls.CURRENT_CONFIG, CONFIG_RECURSE)
        gui.add_separator()
        gui.add_submenu_radio(cls._text('MENU_SORT'), {sort: cls._text(
            f'SORT_{sort}') for sort in SORTS}, cls.CURRENT_CONFIG, CONFIG_SORT)
        gui.add_submenu_radio(cls._text('MENU_ORDER'), {order: cls._text(
            f'ORDER_{order}') for order in ORDERS}, cls.CURRENT_CONFIG, CONFIG_ORDER)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[File]]:
        results: Optional[list] = None
        while True:
            if not results:
                results = [path for path in files.iter_files(
                    params[CONFIG_DIR], params[CONFIG_RECURSE]) if win32.is_valid_image(path)]
                results.sort(key=SORTS[params[CONFIG_SORT]], reverse=params[CONFIG_ORDER] == ORDERS[1])
                if not results:
                    yield
                    continue
            path = results.pop(0)
            yield File(request.from_path(path), size=os.path.getsize(path))

    @classmethod
    def _on_dir(cls, set_tooltip: Callable) -> bool:
        if (path := win32.dialog.open_folder(
                cls.CURRENT_CONFIG[CONFIG_DIR], cls._text('MENU_DIR'))) is not None:
            cls.CURRENT_CONFIG[CONFIG_DIR] = path
            set_tooltip(path)
        return bool(path)
