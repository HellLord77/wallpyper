import functools
from typing import Iterator
from typing import Optional
from typing import TypedDict

import gui
import validator
from libs import request
from . import ImageFile
from . import Source

URL_BASE = request.join_url('https://api.500px.com', 'v1', 'photos')
URL_SEARCH = request.join_url(URL_BASE, 'search')

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
SORT_DIRECTIONS = 'desc', 'asc'

_PARAMS = {'ids': '', 'image_size': '4096'}


def _get_sort(feature: str) -> str:
    return SORTS[1] if feature == FEATURES[0] else SORTS[2] if feature == FEATURES[1] else SORTS[0]


class FiveHundredPx(Source):  # https://github.com/500px/legacy-api-documentation
    NAME = '500px [legacy]'
    VERSION = '0.0.3'
    ICON = 'png'
    URL = 'https://500px.com'
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_FEATURE:        str,
        CONFIG_ONLY:           str,
        CONFIG_EXCLUDE:        str,
        CONFIG_SORT:           str,
        CONFIG_SORT_DIRECTION: str})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_FEATURE:        FEATURES[4],
        CONFIG_ONLY:           '',
        CONFIG_EXCLUDE:        '',
        CONFIG_SORT:           SORTS[0],
        CONFIG_SORT_DIRECTION: SORT_DIRECTIONS[0]}

    _last_feature: str

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_contains, CONFIG_FEATURE, FEATURES)
        cls._fix_config(validator.ensure_contains, CONFIG_SORT, SORTS)
        cls._fix_config(validator.ensure_contains, CONFIG_SORT_DIRECTION, SORT_DIRECTIONS)
        onlies = cls.CURRENT_CONFIG[CONFIG_ONLY].split(',')
        excludes = cls.CURRENT_CONFIG[CONFIG_EXCLUDE].split(',')
        cls.CURRENT_CONFIG[CONFIG_ONLY] = ','.join(
            category for category in onlies if category in CATEGORIES and category not in excludes)
        cls.CURRENT_CONFIG[CONFIG_EXCLUDE] = ','.join(
            category for category in excludes if category in CATEGORIES and category not in onlies)

    @classmethod
    def create_menu(cls):
        onlies = cls.CURRENT_CONFIG[CONFIG_ONLY].split(',')
        excludes = cls.CURRENT_CONFIG[CONFIG_EXCLUDE].split(',')
        menu_only = gui.add_submenu(cls._text('MENU_ONLY')).get_submenu()
        menu_exclude = gui.add_submenu(cls._text('MENU_EXCLUDE')).get_submenu()
        on_only = functools.partial(cls._on_category, CONFIG_ONLY, menu_only, menu_exclude)
        on_exclude = functools.partial(cls._on_category, CONFIG_EXCLUDE, menu_exclude, menu_only)
        for category in CATEGORIES:
            label = cls._text(f'CATEGORY_{category}')
            gui.add_menu_item(label, gui.MenuItemType.CHECK, category in onlies,
                              category not in excludes, uid=category, on_click=on_only, menu=menu_only)
            gui.add_menu_item(label, gui.MenuItemType.CHECK, category in excludes,
                              category not in onlies, uid=category, on_click=on_exclude, menu=menu_exclude)
        menu_sort = gui.add_submenu_radio(cls._text('MENU_SORT'), {sort: cls._text(
            f'SORT_{sort}') for sort in SORTS}, cls.CURRENT_CONFIG, CONFIG_SORT).get_submenu()
        gui.add_submenu_radio(cls._text('MENU_FEATURE'), {feature: cls._text(
            f'FEATURE_{feature}') for feature in FEATURES}, cls.CURRENT_CONFIG, CONFIG_FEATURE,
                              on_click=functools.partial(cls._on_feature, menu_sort), position=0)
        cls._last_feature = cls.CURRENT_CONFIG[CONFIG_FEATURE]
        gui.add_submenu_radio(cls._text('MENU_SORT_DIRECTION'), {
            sort_direction: cls._text(f'SORT_DIRECTION_{sort_direction}')
            for sort_direction in SORT_DIRECTIONS}, cls.CURRENT_CONFIG, CONFIG_SORT_DIRECTION)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        photos = []
        while True:
            if not photos:
                response = request.get(URL_BASE, params)
                if response:
                    json = response.json()
                    _PARAMS['ids'] = ','.join(str(photo['id']) for photo in json['photos'])
                    response = request.get(URL_BASE, _PARAMS)
                    if response:
                        photos = list(response.json()['photos'].values())
                        params['page'] = str(json['current_page'] % json['total_pages'] + 1)
                if not photos:
                    yield
                    continue
            photo = photos.pop(0)
            yield ImageFile(photo['image_url'][0], f'{photo["name"]}.{photo["image_format"]}',
                            url=request.join_url(cls.URL, photo['url']), width=photo[
                    'width'], height=photo['height'], sketchy=photo['has_nsfw_tags'], nsfw=photo['nsfw'])

    @classmethod
    def _on_category(cls, key: str, menu: gui.Menu, menu_other: gui.Menu):
        checked = {item.get_uid() for item in menu if item.is_checked()}
        for item_other in menu_other:
            item_other.enable(item_other.get_uid() not in checked)
        cls.CURRENT_CONFIG[key] = ','.join(checked)

    @classmethod
    def _on_feature(cls, menu: gui.Menu, feature: str):
        if cls._last_feature != feature:
            if cls.CURRENT_CONFIG[CONFIG_SORT] == _get_sort(cls._last_feature):
                item = gui.get_menu_item_by_uid(_get_sort(feature), False, menu)
                item.check()
                item.trigger(gui.MenuItemEvent.LEFT_UP)
            cls._last_feature = feature
