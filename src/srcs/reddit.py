import copy
import functools
import os
import time
from typing import Callable, Iterator, Optional, TypedDict

import gui
import validator
from libs import callables, files, request
from . import CONFIG_ORIENTATIONS, CONFIG_RATINGS, ImageFile, Source

URL_BASE = request.join_url('https://oauth.reddit.com', 'r')
URL_TOKEN = request.join_url(
    'https://www.reddit.com', 'api', 'v1', 'access_token')
URL_IMAGE = request.join_url('https://i.redd.it')

CONFIG_ID = '_client_id'
CONFIG_STATIC = '_skip_animated'
CONFIG_SUBS = 'subreddits'
CONFIG_SORT = 'sort'
CONFIG_TIME = 't'

SORTS = 'hot', 'new', 'top', 'controversial', 'rising'
TIMES = 'hour', 'day', 'week', 'month', 'year', 'all'

_TOKEN_TOLERANCE = 30.0
_TOKEN_DATA = {
    'grant_type': 'https://oauth.reddit.com/grants/installed_client',
    'device_id': 'DO_NOT_TRACK_THIS_DEVICE'}


@callables.LastCacheCallable
def _get_auth(client_id: str) -> Iterator[Optional[str]]:
    token = {'access_token': None}
    expires_at = 0.0
    while True:
        if time.monotonic() >= expires_at:
            response = request.post(URL_TOKEN, _TOKEN_DATA, auth=(client_id, ''))
            if response:
                token = response.json()
                expires_at = time.monotonic() + token['expires_in'] - _TOKEN_TOLERANCE
            else:
                token['access_token'] = None
        yield token['access_token']


def _iter_children(children: list[dict]) -> Iterator[dict]:
    for child in children:
        data = child['data']
        post_hint = data.get('post_hint')
        if post_hint == 'link':
            pass  # TODO
        elif post_hint == 'image':
            yield child
        elif data.get('is_gallery'):
            media_metadata = data['media_metadata']
            title = data['title']
            for index, item in enumerate(data['gallery_data']['items'], 1):
                media_id = item['media_id']
                if (media := media_metadata[media_id])['status'] == 'valid':
                    if media['e'] == 'Image':
                        s = media['s']
                        gallery = copy.deepcopy(child)
                        data = gallery['data']
                        data['preview'] = {'images': [{'source': {
                            'width': s['x'], 'height': s['y']}}]}
                        data['url'] = request.join_url(
                            URL_IMAGE, f'{media_id}.{os.path.basename(media["m"])}')
                        data['title'] = f'{title} ({index})'
                        yield gallery


def _on_sort(enable: Callable[[bool], bool], sort: str):
    enable(sort in (SORTS[2], SORTS[3]))


def _authenticate(client_id: str) -> bool:
    return next(_get_auth(client_id)) is not None


class Reddit(Source):  # https://www.reddit.com/dev/api
    NAME = 'reddit'
    VERSION = '0.0.3'
    ICON = 'png'
    URL = 'https://reddit.com'
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_ID: str,
        CONFIG_ORIENTATIONS: list[bool],
        CONFIG_RATINGS: list[bool],
        CONFIG_STATIC: bool,
        CONFIG_SUBS: str,
        CONFIG_SORT: str,
        CONFIG_TIME: str})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_ID: '',
        CONFIG_ORIENTATIONS: [True, True],
        CONFIG_RATINGS: [True, False],
        CONFIG_STATIC: True,
        CONFIG_SUBS: 'wallpaper',
        CONFIG_SORT: SORTS[0],
        CONFIG_TIME: TIMES[1]}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_len, CONFIG_ORIENTATIONS, 2)
        cls._fix_config(validator.ensure_truthy, CONFIG_ORIENTATIONS, any)
        cls._fix_config(validator.ensure_len, CONFIG_RATINGS, 2)
        cls._fix_config(validator.ensure_truthy, CONFIG_RATINGS, any)
        cls._fix_config(validator.ensure_contains, CONFIG_SORT, SORTS)
        cls._fix_config(validator.ensure_contains, CONFIG_TIME, TIMES)

    @classmethod
    def create_menu(cls):
        item_time_enable = gui.add_submenu_radio(cls._text('MENU_TIME'), {time_: cls._text(
            f'TIME_{time_}') for time_ in TIMES}, cls.CURRENT_CONFIG, CONFIG_TIME).enable
        gui.add_submenu_radio(cls._text('MENU_SORT'), {sort: cls._text(
            f'SORT_{sort}') for sort in SORTS}, cls.CURRENT_CONFIG, CONFIG_SORT,
                              on_click=functools.partial(_on_sort, item_time_enable), position=0)
        _on_sort(item_time_enable, cls.CURRENT_CONFIG[CONFIG_SORT])
        gui.add_separator()
        gui.add_submenu_check(cls._text('MENU_ORIENTATIONS'), (
            cls._text(f'ORIENTATION_{orientation}') for orientation in range(2)),
                              (1, None), cls.CURRENT_CONFIG, CONFIG_ORIENTATIONS)
        gui.add_submenu_check(cls._text('MENU_RATINGS'), (
            cls._text(f'RATING_{rating}') for rating in range(2)),
                              (1, None), cls.CURRENT_CONFIG, CONFIG_RATINGS)
        gui.add_menu_item_check(cls._text('LABEL_STATIC'), cls.CURRENT_CONFIG, CONFIG_STATIC)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        children: Optional[list] = None
        sort = params.pop(CONFIG_SORT)
        url = request.join_url(URL_BASE, params.pop(CONFIG_SUBS), sort)
        if sort not in (SORTS[2], SORTS[4]):
            del params[CONFIG_TIME]
        while True:
            if not children:
                auth = next(_get_auth(cls.CURRENT_CONFIG[CONFIG_ID]))
                if auth is not None:
                    response = request.get(url, params, auth=auth)
                    if response:
                        data = response.json()['data']
                        params['after'] = data['after']
                        children = list(_iter_children(data['children']))
                if not children:
                    yield
                    continue
            data = children.pop(0)['data']
            url_child = data['url']
            source = data['preview']['images'][0]['source']
            yield ImageFile(url_child, files.replace_ext(data["title"], os.path.splitext(url_child)[1]),
                            url=request.join_url(cls.URL, data['permalink']),
                            width=source['width'], height=source['height'], nsfw=data['over_18'])

    @classmethod
    def filter_image(cls, image: ImageFile) -> bool:
        if cls.CURRENT_CONFIG[CONFIG_STATIC] and image.is_animated():
            return False
        return super().filter_image(image)
