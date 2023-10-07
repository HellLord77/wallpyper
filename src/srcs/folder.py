import os
from typing import Callable
from typing import Iterator
from typing import Optional
from typing import TypedDict

import gui
import validator
import win32
from libs import files
from libs import request
from . import CONFIG_ORIENTATIONS
from . import ImageFile
from . import Source

CONFIG_DIR = 'dir'
CONFIG_RECURSE = 'recursive'
CONFIG_SORT = 'sort_by'
CONFIG_ORDER = 'sort_order'

SORTS = {
    'name':     str,
    'modified': os.path.getmtime,
    'type':     files.get_ext,
    'size':     os.path.getsize}
ORDERS = 'ascending', 'descending'


class Folder(Source):
    NAME = 'Folder [offline]'
    VERSION = '0.0.4'
    ICON = 'png'
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_ORIENTATIONS: list[bool, bool],
        CONFIG_DIR:          str,
        CONFIG_RECURSE:      bool,
        CONFIG_SORT:         str,
        CONFIG_ORDER:        str})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_ORIENTATIONS: [True, True],
        CONFIG_DIR:          win32.PICTURES_DIR,
        CONFIG_RECURSE:      True,
        CONFIG_SORT:         next(iter(SORTS)),
        CONFIG_ORDER:        ORDERS[0]}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_disk, CONFIG_DIR, False)
        cls._fix_config(validator.ensure_contains, CONFIG_SORT, SORTS)
        cls._fix_config(validator.ensure_contains, CONFIG_ORDER, ORDERS)
        super().fix_config(saving)

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
        gui.add_separator()
        super().create_menu()

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        results = []
        while True:
            if not results:
                results = [path for path in files.iter_files(
                    params[CONFIG_DIR], params[CONFIG_RECURSE])
                           if win32.is_valid_image(path)]
                results.sort(key=SORTS[params[CONFIG_SORT]],
                             reverse=params[CONFIG_ORDER] == ORDERS[1])
                if not results:
                    yield
                    continue
            path = results.pop(0)
            width, height = win32.get_dimensions_image(path)
            yield ImageFile(request.from_path(path), size=os.path.getsize(
                path), width=width, height=height)

    @classmethod
    def _on_dir(cls, set_tooltip: Callable) -> bool:
        if (path := win32.dialog.open_folder(
                cls.CURRENT_CONFIG[CONFIG_DIR], cls._text('MENU_DIR'))) is not None:
            cls.CURRENT_CONFIG[CONFIG_DIR] = path
            set_tooltip(path)
        return bool(path)
