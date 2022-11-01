__version__ = '0.0.1'

import os.path
from typing import Generator, Optional, Callable

import gui
import win32
from libs import files
from .module import _Module

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


class Local(_Module):
    NAME = 'Local Folder'
    DEFAULT_CONFIG = {
        CONFIG_DIR: win32.PICTURES_DIR,
        CONFIG_SORT: next(iter(SORTS)),
        CONFIG_ORDER: ORDERS[0],
        CONFIG_RECURSE: True}

    @classmethod
    def fix_config(cls):
        if not os.path.isdir(cls.CONFIG[CONFIG_DIR]):
            cls.CONFIG[CONFIG_DIR] = cls.DEFAULT_CONFIG[CONFIG_DIR]
        cls._fix_config(CONFIG_SORT, SORTS)
        cls._fix_config(CONFIG_ORDER, ORDERS)

    @classmethod
    def get_next_wallpaper(cls, **params: bool | str) -> Generator[Optional[files.File], None, None]:
        results: Optional[list] = None
        while True:
            if not results:
                results = [path for path in files.iter_files(
                    params[CONFIG_DIR], params[CONFIG_RECURSE]) if win32.is_valid_image(path)]
                results.sort(key=SORTS[params[CONFIG_SORT]], reverse=params[CONFIG_ORDER] == ORDERS[1])
            result = results.pop(0)
            yield files.File(files.get_uri(result), os.path.basename(result), os.path.getsize(result))

    @classmethod
    def create_menu(cls):
        gui.add_menu_item(cls.STRINGS.LOCAL_MENU_DIR, on_click=cls._on_modify_dir, menu_args=(
            gui.MenuItemMethod.SET_TOOLTIP,)).set_tooltip(cls.CONFIG[CONFIG_DIR])
        gui.add_mapped_menu_item(cls.STRINGS.LOCAL_MENU_RECURSE, cls.CONFIG, CONFIG_RECURSE)
        gui.add_separator()
        gui.add_mapped_submenu(cls.STRINGS.LOCAL_MENU_SORT, {sort: getattr(
            cls.STRINGS, f'LOCAL_SORT_{sort}') for sort in SORTS}, cls.CONFIG, CONFIG_SORT)
        gui.add_mapped_submenu(cls.STRINGS.LOCAL_MENU_ORDER, {order: getattr(
            cls.STRINGS, f'LOCAL_ORDER_{order}') for order in ORDERS}, cls.CONFIG, CONFIG_ORDER)

    @classmethod
    def _on_modify_dir(cls, set_tooltip: Callable) -> bool:
        if path := win32.select_folder(cls.STRINGS.LOCAL_MENU_DIR, cls.CONFIG[CONFIG_DIR]):
            cls.CONFIG[CONFIG_DIR] = path
            set_tooltip(path)
        return bool(path)
