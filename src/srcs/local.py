import os.path
from typing import Callable, Iterator, Optional, TypedDict

import gui
import validator
import win32
from libs import files, request
from . import Source

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


class LocalFolder(Source):
    NAME = 'Local Folder'
    VERSION = '0.0.1'
    ICON = 'png'
    URL = request.from_path(win32.PICTURES_DIR)
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
        gui.add_menu_item(cls.STRINGS.LOCAL_MENU_DIR, on_click=cls._on_modify_dir, args=(
            gui.MenuItemMethod.SET_TOOLTIP,)).set_tooltip(cls.CURRENT_CONFIG[CONFIG_DIR])
        gui.add_menu_item_check(cls.STRINGS.LOCAL_MENU_RECURSE, cls.CURRENT_CONFIG, CONFIG_RECURSE)
        gui.add_separator()
        gui.add_submenu_radio(cls.STRINGS.LOCAL_MENU_SORT, {sort: getattr(
            cls.STRINGS, f'LOCAL_SORT_{sort}') for sort in SORTS}, cls.CURRENT_CONFIG, CONFIG_SORT)
        gui.add_submenu_radio(cls.STRINGS.LOCAL_MENU_ORDER, {order: getattr(
            cls.STRINGS, f'LOCAL_ORDER_{order}') for order in ORDERS}, cls.CURRENT_CONFIG, CONFIG_ORDER)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[files.File]]:
        results: Optional[list] = None
        while True:
            if not results:
                results = [path for path in files.iter_files(
                    params[CONFIG_DIR], params[CONFIG_RECURSE]) if win32.is_valid_image(path)]
                results.sort(key=SORTS[params[CONFIG_SORT]], reverse=params[CONFIG_ORDER] == ORDERS[1])
            path = results.pop(0)
            yield files.File(request.from_path(path), size=os.path.getsize(path))

    @classmethod
    def _on_modify_dir(cls, set_tooltip: Callable) -> bool:
        if path := win32.dialog.open_folder(cls.CURRENT_CONFIG[CONFIG_DIR], cls.STRINGS.LOCAL_MENU_DIR):
            cls.CURRENT_CONFIG[CONFIG_DIR] = path
            set_tooltip(path)
        return bool(path)
