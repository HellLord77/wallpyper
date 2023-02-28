from typing import Generator, Optional

import gui
from libs import files, urls
from . import Source

URL_BASE = urls.join('https://api.500px.com', 'v1', 'photos')
URL_SEARCH = urls.join(URL_BASE, 'search')

CONFIG_FEATURE = 'feature'
CONFIG_ONLY = 'only'
CONFIG_EXCLUDE = 'exclude'
CONFIG_SORT = 'sort'
CONFIG_SORT_DIRECTION = 'sort_direction'

FEATURES = 'popular', 'highest_rated', 'upcoming', 'editors', 'fresh_today', 'fresh_yesterday', 'fresh_week'
CATEGORIES = (
    'Uncategorized', 'Abstract', 'Animals', 'Black and White', 'Celebrities', 'City and Architecture', 'Commercial', 'Concert',
    'Family', 'Fashion', 'Film', 'Fine Art', 'Food', 'Journalism', 'Landscapes', 'Macro', 'Nature', 'Nude', 'People',
    'Performing Arts', 'Sport', 'Still Life', 'Street', 'Transportation', 'Travel', 'Underwater', 'Urban Exploration', 'Wedding')
SORTS = 'created_at', 'rating', 'highest_rating', 'times_viewed', 'votes_count', 'comments_count', 'taken_at'
SORT_DIRECTIONS = 'asc', 'desc'


def _get_sort(feature: str) -> str:
    return SORTS[1] if feature == FEATURES[0] else SORTS[2] if feature == FEATURES[1] else SORTS[0]


class FiveHundredPxLegacy(Source):
    NAME = '500px Legacy'
    VERSION = '0.0.1'
    URL = 'https://500px.com'
    DEFAULT_CONFIG = {
        CONFIG_FEATURE: FEATURES[4],
        CONFIG_ONLY: '',
        CONFIG_EXCLUDE: '',
        CONFIG_SORT: SORTS[0],
        CONFIG_SORT_DIRECTION: SORT_DIRECTIONS[1]}

    _last_feature: str

    @classmethod
    def fix_config(cls):
        cls._fix_config(CONFIG_FEATURE, FEATURES)
        onlies = cls.CURRENT_CONFIG[CONFIG_ONLY].split(',')
        excludes = cls.CURRENT_CONFIG[CONFIG_EXCLUDE].split(',')
        cls.CURRENT_CONFIG[CONFIG_ONLY] = ','.join(
            category for category in onlies if category in CATEGORIES and category not in excludes)
        cls.CURRENT_CONFIG[CONFIG_EXCLUDE] = ','.join(
            category for category in excludes if category in CATEGORIES and category not in onlies)
        cls._fix_config(CONFIG_SORT, SORTS)
        cls._fix_config(CONFIG_SORT_DIRECTION, SORT_DIRECTIONS)

    @classmethod
    def get_next_wallpaper(cls, **params) -> Generator[Optional[files.File], None, None]:
        photos: Optional[list] = None
        while True:
            if not photos:
                pass
            yield

    @classmethod
    def create_menu(cls):
        menu_only = gui.add_submenu(cls.strings.FIVEHUNREDPXLEGACY_MENU_ONLY).get_submenu()
        menu_exclude = gui.add_submenu(cls.strings.FIVEHUNREDPXLEGACY_MENU_EXCLUDE).get_submenu()
        for category in CATEGORIES:
            label = getattr(cls.strings, f'FIVEHUNREDPXLEGACY_CATEGORY_{category}')
            gui.add_menu_item(label, gui.MenuItemType.CHECK, uid=category, on_click=cls._on_category,
                              args=(CONFIG_ONLY, menu_only, menu_exclude), menu=menu_only)
            gui.add_menu_item(label, gui.MenuItemType.CHECK, uid=category, on_click=cls._on_category,
                              args=(CONFIG_EXCLUDE, menu_exclude, menu_only), menu=menu_exclude)

        menu_sort = gui.add_mapped_submenu(cls.strings.FIVEHUNREDPXLEGACY_MENU_SORT, {sort: getattr(
            cls.strings, f'FIVEHUNREDPXLEGACY_SORT_{sort}') for sort in SORTS}, cls.CURRENT_CONFIG, CONFIG_SORT).get_submenu()
        gui.add_mapped_submenu(cls.strings.FIVEHUNREDPXLEGACY_MENU_FEATURE, {
            feature: getattr(cls.strings, f'FIVEHUNREDPXLEGACY_FEATURE_{feature}') for feature in
            FEATURES}, cls.CURRENT_CONFIG, CONFIG_FEATURE, on_click=cls._on_feature, args=(menu_sort,), position=0)
        cls._last_feature = cls.CURRENT_CONFIG[CONFIG_FEATURE]
        gui.add_mapped_submenu(cls.strings.FIVEHUNREDPXLEGACY_MENU_SORT_DIRECTION, {
            sort_direction: getattr(cls.strings, f'FIVEHUNREDPXLEGACY_SORT_DIRECTION_{sort_direction}')
            for sort_direction in SORT_DIRECTIONS}, cls.CURRENT_CONFIG, CONFIG_SORT_DIRECTION)

        '''
        categories = cls.CURRENT_CONFIG[CONFIG_CATEGORIES].split('-')
        # noinspection PyProtectedMember
        with gui.set_menu(gui.add_submenu(cls.strings._500PX_MENU_CATEGORY)) as menu_category:
            for category in CATEGORIES:
                gui.add_menu_item(
                    f'_500PX_CATEGORY_{"".join(filter(str.isalnum, category))}', gui.MenuItemType.CHECK, category in categories,
                    uid=category, on_click=cls._on_category, menu_args=(gui.MenuItemProperty.UID,), args=(menu_category,))
        _on_category(menu_category)
        # noinspection PyProtectedMember
        enable_follower = gui.add_mapped_submenu(cls.strings._500PX_MENU_FOLLOWER, {follower: getattr(
            cls.strings, f'_500PX_FOLLOWER_{follower}') for follower in FOLLOWERS}, cls.CURRENT_CONFIG, CONFIG_FOLLOWERS).enable
        # noinspection PyProtectedMember
        enable_sort = gui.add_mapped_submenu(cls.strings._500PX_MENU_SORT, {sort: getattr(
            cls.strings, f'_500PX_SORT_{sort}') for sort in SORTS}, cls.CURRENT_CONFIG, CONFIG_SORT).enable
        # noinspection PyProtectedMember
        gui.add_mapped_submenu(cls.strings._500PX_MENU_DISCOVER, {discover: getattr(
            cls.strings, f'_500PX_DISCOVER_{discover}') for discover in DISCOVERS}, cls.CURRENT_CONFIG, CONFIG_DISCOVER,
                               on_click=cls._on_discover, args=(enable_follower, enable_sort), position=0)
        cls._on_discover(None, enable_follower, enable_sort)
        # noinspection PyProtectedMember
        gui.add_mapped_menu_item(cls.strings._500PX_MENU_NSFW, cls.CURRENT_CONFIG, CONFIG_NSFW)
        '''

    @classmethod
    def _on_category(cls, key: str, menu: gui.Menu, menu_other: gui.Menu):
        checked = {item.get_uid() for item in menu if item.is_checked()}
        for item_other in menu_other:
            item_other.enable(item_other.get_uid() not in checked)
        cls.CURRENT_CONFIG[key] = ','.join(checked)

    @classmethod
    def _on_feature(cls, feature: str, menu: gui.Menu):
        if cls._last_feature != feature:
            if cls.CURRENT_CONFIG[CONFIG_SORT] == _get_sort(cls._last_feature):
                item = gui.get_menu_item_by_uid(_get_sort(feature), False, menu)
                item.check()
                item.trigger(gui.MenuItemEvent.LEFT_UP)
            cls._last_feature = feature
