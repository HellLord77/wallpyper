__version__ = '0.0.1'

import re
import time
from typing import Callable, Generator, Optional

import consts
import gui
import win32.browser
from libs import files, minihtml, request, utils
from . import Source

_TIMEOUT = 30
_PATTERN = re.compile('^Elements__Image.*')

URL_BASE = 'https://500px.com'

CONFIG_CATEGORIES = 'categories'
CONFIG_DISCOVER = 'discover'
CONFIG_FOLLOWERS = 'followers'
CONFIG_SORT = 'sort'
CONFIG_NSFW = '_nsfw'

CATEGORIES = (
    '', 'abstract', 'aerial', 'animals', 'black+and+white', 'celebrities', 'city+%26+architecture',
    'commercial', 'concert', 'family', 'fashion', 'food', 'fine+art', 'film', 'journalism', 'landscapes',
    'macro', 'nature', 'night', 'people', 'performing+arts', 'sport', 'still+life', 'street',
    'transportation', 'travel', 'underwater', 'urban+exploration', 'wedding', 'uncategorized')
DISCOVERS = 'popular', 'upcoming', 'fresh', 'editors'
FOLLOWERS = '', 'undiscovered'
SORTS = '', 'created_at'


def _find_images(browser: win32.browser.Browser) -> Generator[minihtml.Element, None, None]:
    yield from minihtml.find_elements(minihtml.loads(
        browser.get_html()).iter_all_children(), 'img', {'class': _PATTERN})


def _on_category(menu: gui.Menu) -> tuple[str]:
    categories = tuple(item.get_uid() for item in menu if item.is_checked())
    disable = CATEGORIES.index(categories[0]) if len(categories) == 1 else -1
    for index, item in enumerate(menu):
        item.enable(disable != index)
    # noinspection PyTypeChecker
    return categories


class _Source(Source):
    NAME = '500px'
    DEFAULT_CONFIG = {
        CONFIG_CATEGORIES: CATEGORIES[0],
        CONFIG_DISCOVER: DISCOVERS[0],
        CONFIG_FOLLOWERS: FOLLOWERS[0],
        CONFIG_SORT: SORTS[0],
        CONFIG_NSFW: False}

    @classmethod
    def fix_config(cls):
        categories = tuple(category for category in cls.CONFIG[CONFIG_CATEGORIES].lower().split('-') if category in CATEGORIES)
        cls.CONFIG[CONFIG_CATEGORIES] = CATEGORIES[0] if CATEGORIES[0] in categories else '-'.join(categories)
        cls._fix_config(CONFIG_DISCOVER, DISCOVERS)
        cls._fix_config(CONFIG_FOLLOWERS, FOLLOWERS)
        cls._fix_config(CONFIG_SORT, SORTS)

    @classmethod
    def get_next_wallpaper(cls, **params: bool | str) -> Generator[Optional[files.File], None, None]:
        images: Optional[list] = None
        image = None
        url = request.join(URL_BASE, discover := params.pop(CONFIG_DISCOVER), params.pop(CONFIG_CATEGORIES))
        if discover == DISCOVERS[3]:
            params.pop(CONFIG_DISCOVER)
        if discover != DISCOVERS[0]:
            params.pop(CONFIG_SORT)
        browser = win32.browser.Browser(request.encode(url, params))
        browser.wait(_TIMEOUT)
        while True:
            if not images:
                current = utils.len_ex(_find_images(browser))
                if current:
                    browser.eval_js('window.scrollTo(0, document.body.scrollHeight);')
                end_time = time.time() + _TIMEOUT
                while end_time > time.time() and current == utils.len_ex(_find_images(browser)):
                    time.sleep(consts.POLL_BIG_INTERVAL)
                images_ = iter(_find_images(browser))
                if image:
                    utils.consume_ex(images_, image)
                images = list(images_)
                print(len(images))
            if not images:
                yield
                continue
            for img in images:
                print(img)
            image = None
            yield image

    @classmethod
    def create_menu(cls):
        categories = cls.CONFIG[CONFIG_CATEGORIES].split('-')
        # noinspection PyProtectedMember
        with gui.set_menu(gui.add_submenu(cls.STRINGS._500PX_MENU_CATEGORY)) as menu_category:
            for category in CATEGORIES:
                gui.add_menu_item(
                    f'_500PX_CATEGORY_{"".join(filter(str.isalnum, category))}', gui.MenuItemType.CHECK, category in categories,
                    uid=category, on_click=cls._on_category, menu_args=(gui.MenuItemProperty.UID,), args=(menu_category,))
        _on_category(menu_category)
        # noinspection PyProtectedMember
        enable_follower = gui.add_mapped_submenu(cls.STRINGS._500PX_MENU_FOLLOWER, {follower: getattr(
            cls.STRINGS, f'_500PX_FOLLOWER_{follower}') for follower in FOLLOWERS}, cls.CONFIG, CONFIG_FOLLOWERS).enable
        # noinspection PyProtectedMember
        enable_sort = gui.add_mapped_submenu(cls.STRINGS._500PX_MENU_SORT, {sort: getattr(
            cls.STRINGS, f'_500PX_SORT_{sort}') for sort in SORTS}, cls.CONFIG, CONFIG_SORT).enable
        # noinspection PyProtectedMember
        gui.add_mapped_submenu(cls.STRINGS._500PX_MENU_DISCOVER, {discover: getattr(
            cls.STRINGS, f'_500PX_DISCOVER_{discover}') for discover in DISCOVERS}, cls.CONFIG, CONFIG_DISCOVER,
                               on_click=cls._on_discover, args=(enable_follower, enable_sort), position=0)
        cls._on_discover(None, enable_follower, enable_sort)
        # noinspection PyProtectedMember
        gui.add_mapped_menu_item(cls.STRINGS._500PX_MENU_NSFW, cls.CONFIG, CONFIG_NSFW)

    @classmethod
    def _on_category(cls, category: str, menu: gui.Menu):
        if category == CATEGORIES[0]:
            for item in menu[1:]:
                item.check(False)
        else:
            menu[0].check(False)
        cls.CONFIG[CONFIG_CATEGORIES] = '-'.join(_on_category(menu))

    @classmethod
    def _on_discover(cls, _, enable_follower: Callable[[bool], bool], enable_sort: Callable[[bool], bool]):
        enable_follower(cls.CONFIG[CONFIG_DISCOVER] != DISCOVERS[3])
        enable_sort(cls.CONFIG[CONFIG_DISCOVER] == DISCOVERS[0])
