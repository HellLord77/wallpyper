import functools
import re
import time
from typing import Callable, Iterator, Optional, TypedDict

import consts
import gui
import validator
import win32.browser
from libs import files, request, soup, utils
from . import Source

_TIMEOUT = 30
_PATTERN = re.compile('^Elements__Image.*')

CONFIG_NSFW = '_nsfw'
CONFIG_CATEGORIES = 'categories'
CONFIG_DISCOVER = 'discover'
CONFIG_FOLLOWER = 'followers'
CONFIG_SORT = 'sort'

CATEGORIES = (
    '', 'abstract', 'aerial', 'animals', 'black+and+white', 'celebrities', 'city+%26+architecture',
    'commercial', 'concert', 'family', 'fashion', 'food', 'fine+art', 'film', 'journalism', 'landscapes',
    'macro', 'nature', 'night', 'people', 'performing+arts', 'sport', 'still+life', 'street',
    'transportation', 'travel', 'underwater', 'urban+exploration', 'wedding', 'uncategorized')
DISCOVERS = 'popular', 'upcoming', 'fresh', 'editors'
FOLLOWERS = '', 'undiscovered'
SORTS = '', 'created_at'


def _iter_images(browser: win32.browser.Browser) -> Iterator[soup.Element]:
    return soup.find_elements(soup.loads(
        browser.get_html()).iter_all_children(), 'img', {'class': _PATTERN})


def _on_category(menu: gui.Menu) -> tuple[str, ...]:
    categories = tuple(item.get_uid() for item in menu if item.is_checked())
    disable = CATEGORIES.index(categories[0]) if len(categories) == 1 else -1
    for index, item in enumerate(menu):
        item.enable(disable != index)
    return categories


class FiveHundredPx(Source):
    NAME = '# 500px'
    URL = 'https://500px.com'
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_NSFW: bool,
        CONFIG_CATEGORIES: str,
        CONFIG_DISCOVER: str,
        CONFIG_FOLLOWER: str,
        CONFIG_SORT: str})
    DEFAULT_CONFIG = {
        CONFIG_NSFW: False,
        CONFIG_CATEGORIES: CATEGORIES[0],
        CONFIG_DISCOVER: DISCOVERS[0],
        CONFIG_FOLLOWER: FOLLOWERS[0],
        CONFIG_SORT: SORTS[0]}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_iterable, CONFIG_DISCOVER, DISCOVERS)
        cls._fix_config(validator.ensure_iterable, CONFIG_FOLLOWER, FOLLOWERS)
        cls._fix_config(validator.ensure_iterable, CONFIG_SORT, SORTS)
        categories = tuple(category for category in cls.CURRENT_CONFIG[CONFIG_CATEGORIES].lower().split('-') if category in CATEGORIES)
        cls.CURRENT_CONFIG[CONFIG_CATEGORIES] = CATEGORIES[0] if CATEGORIES[0] in categories else '-'.join(categories)

    @classmethod
    def create_menu(cls):
        categories = cls.CURRENT_CONFIG[CONFIG_CATEGORIES].split('-')
        with gui.set_menu(gui.add_submenu(cls.STRINGS.FIVEHUNDREDPX_MENU_CATEGORY)) as menu_category:
            for category in CATEGORIES:
                gui.add_menu_item(
                    f'FIVEHUNDREDPX_CATEGORY_{"".join(filter(str.isalnum, category))}', gui.MenuItemType.CHECK, category in categories,
                    uid=category, on_click=functools.partial(cls._on_category, menu_category, ), args=(gui.MenuItemProperty.UID,))
        _on_category(menu_category)
        enable_follower = gui.add_mapped_submenu(cls.STRINGS.FIVEHUNDREDPX_MENU_FOLLOWER, {follower: getattr(
            cls.STRINGS, f'FIVEHUNDREDPX_FOLLOWER_{follower}') for follower in FOLLOWERS}, cls.CURRENT_CONFIG, CONFIG_FOLLOWER).enable
        enable_sort = gui.add_mapped_submenu(cls.STRINGS.FIVEHUNDREDPX_MENU_SORT, {sort: getattr(
            cls.STRINGS, f'FIVEHUNDREDPX_SORT_{sort}') for sort in SORTS}, cls.CURRENT_CONFIG, CONFIG_SORT).enable
        gui.add_mapped_submenu(cls.STRINGS.FIVEHUNDREDPX_MENU_DISCOVER, {discover: getattr(
            cls.STRINGS, f'FIVEHUNDREDPX_DISCOVER_{discover}') for discover in DISCOVERS}, cls.CURRENT_CONFIG, CONFIG_DISCOVER,
                               on_click=functools.partial(cls._on_discover, enable_follower, enable_sort), position=0)
        cls._on_discover(enable_follower, enable_sort, cls.CURRENT_CONFIG[CONFIG_DISCOVER])
        gui.add_mapped_menu_item(cls.STRINGS.FIVEHUNDREDPX_MENU_NSFW, cls.CURRENT_CONFIG, CONFIG_NSFW)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[files.File]]:
        images: Optional[list] = None
        image = None
        url = request.join(cls.URL, discover := params.pop(CONFIG_DISCOVER), params.pop(CONFIG_CATEGORIES))
        if discover == DISCOVERS[3]:
            params.pop(CONFIG_DISCOVER)
        if discover != DISCOVERS[0]:
            params.pop(CONFIG_SORT)
        browser = win32.browser.Browser(request.extend_param(url, params))
        browser.wait(_TIMEOUT)
        while True:
            if not images:
                current = utils.len_ex(_iter_images(browser))
                if current:
                    browser.eval_js('window.scrollTo(0, document.body.scrollHeight);')
                end_time = time.monotonic() + _TIMEOUT
                while end_time > time.monotonic() and current == utils.len_ex(_iter_images(browser)):
                    time.sleep(consts.POLL_SLOW_SEC)
                images_ = iter(_iter_images(browser))
                if image:
                    utils.consume_ex(images_, image)
                images = list(images_)
            if not images:
                yield
                continue
            for img in images:
                print(img)
            image = None
            yield image

    @classmethod
    def _on_category(cls, menu: gui.Menu, category: str):
        if category == CATEGORIES[0]:
            for item in menu[1:]:
                item.check(False)
        else:
            menu[0].check(False)
        cls.CURRENT_CONFIG[CONFIG_CATEGORIES] = '-'.join(_on_category(menu))

    @classmethod
    def _on_discover(cls, enable_follower: Callable[[bool], bool], enable_sort: Callable[[bool], bool], discover: str):
        enable_follower(discover != DISCOVERS[3])
        enable_sort(discover == DISCOVERS[0])
