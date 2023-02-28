import os.path
from typing import Generator, Optional, Callable

import gui
import win32
from libs import files, urls
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
    URL = urls.from_path(win32.PICTURES_DIR)
    ICON = 'png'
    DEFAULT_CONFIG = {
        CONFIG_DIR: win32.PICTURES_DIR,
        CONFIG_SORT: next(iter(SORTS)),
        CONFIG_ORDER: ORDERS[0],
        CONFIG_RECURSE: True}

    @classmethod
    def fix_config(cls):
        if not os.path.isdir(cls.CURRENT_CONFIG[CONFIG_DIR]):
            cls.CURRENT_CONFIG[CONFIG_DIR] = cls.DEFAULT_CONFIG[CONFIG_DIR]
        cls._fix_config(CONFIG_SORT, SORTS)
        cls._fix_config(CONFIG_ORDER, ORDERS)

    @classmethod
    def get_next_wallpaper(cls, **params) -> Generator[Optional[files.File], None, None]:
        results: Optional[list] = None
        while True:
            if not results:
                results = [path for path in files.iter_files(
                    params[CONFIG_DIR], params[CONFIG_RECURSE]) if win32.is_valid_image(path)]
                results.sort(key=SORTS[params[CONFIG_SORT]], reverse=params[CONFIG_ORDER] == ORDERS[1])
            path = results.pop(0)
            yield files.File(urls.from_path(path), os.path.basename(path), os.path.getsize(path))

    @classmethod
    def create_menu(cls):
        gui.add_menu_item(cls.strings.LOCAL_MENU_DIR, on_click=cls._on_modify_dir, args=(
            gui.MenuItemMethod.SET_TOOLTIP,)).set_tooltip(cls.CURRENT_CONFIG[CONFIG_DIR])
        gui.add_mapped_menu_item(cls.strings.LOCAL_MENU_RECURSE, cls.CURRENT_CONFIG, CONFIG_RECURSE)
        gui.add_separator()
        gui.add_mapped_submenu(cls.strings.LOCAL_MENU_SORT, {sort: getattr(
            cls.strings, f'LOCAL_SORT_{sort}') for sort in SORTS}, cls.CURRENT_CONFIG, CONFIG_SORT)
        gui.add_mapped_submenu(cls.strings.LOCAL_MENU_ORDER, {order: getattr(
            cls.strings, f'LOCAL_ORDER_{order}') for order in ORDERS}, cls.CURRENT_CONFIG, CONFIG_ORDER)

    @classmethod
    def _on_modify_dir(cls, set_tooltip: Callable) -> bool:
        if path := win32.dialog.open_folder(cls.CURRENT_CONFIG[CONFIG_DIR], cls.strings.LOCAL_MENU_DIR):
            cls.CURRENT_CONFIG[CONFIG_DIR] = path
            set_tooltip(path)
        return bool(path)
