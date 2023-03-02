import copy
import functools
import math
import os.path
import time
from typing import Callable, Generator, Optional

import gui
from libs import callables, files, request
from . import Source

_TOKEN_TOLERANCE = 30.0
_TOKEN_DATA = {
    'grant_type': 'https://oauth.reddit.com/grants/installed_client',
    'device_id': 'DO_NOT_TRACK_THIS_DEVICE'}

URL_BASE = request.join('https://oauth.reddit.com', 'r')
URL_TOKEN = request.join('https://www.reddit.com', 'api', 'v1', 'access_token')
URL_IMAGE = request.join('https://i.redd.it')

CONFIG_ID = '_client_id'
CONFIG_ORIENTATION = '_orientation'
CONFIG_SUBS = 'subreddit'
CONFIG_SORT = 'sort'
CONFIG_TIME = 't'

ORIENTATIONS = '', 'landscape', 'portrait'
SORTS = 'hot', 'new', 'top', 'controversial', 'rising'
TIMES = 'hour', 'day', 'week', 'month', 'year', 'all'


@callables.LastCacheCallable
def _get_auth(client_id: str) -> Generator[Optional[str], None, None]:
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


def _iter_children(children: list[dict]) -> Generator[dict, None, None]:
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
                media = media_metadata[media_id]
                if media['e'] == 'Image':
                    s = media['s']
                    gallery = copy.deepcopy(child)
                    data = gallery['data']
                    data['preview'] = {'images': [
                        {'source': {'width': s['x'], 'height': s['y']}}]}
                    data['url'] = request.join(
                        URL_IMAGE, f'{media_id}.{os.path.basename(media["m"])}')
                    data['title'] = f'{title} ({index})'
                    yield gallery


def _on_sort(enable: Callable[[bool], bool], sort: str):
    enable(sort in (SORTS[2], SORTS[3]))


def _authenticate(client_id: str) -> bool:
    return next(_get_auth(client_id)) is not None


class Reddit(Source):  # https://www.reddit.com/dev/api
    NAME = 'reddit'
    VERSION = '0.0.1'
    ICON = 'png'
    URL = 'https://reddit.com'
    DEFAULT_CONFIG = {
        CONFIG_ID: '',
        CONFIG_ORIENTATION: ORIENTATIONS[0],
        CONFIG_SUBS: 'wallpaper',
        CONFIG_SORT: SORTS[0],
        CONFIG_TIME: TIMES[1]}

    @classmethod
    def fix_config(cls):
        cls._fix_config(CONFIG_ORIENTATION, ORIENTATIONS)
        cls._fix_config(CONFIG_SORT, SORTS)
        cls._fix_config(CONFIG_TIME, TIMES)

    @classmethod
    def get_next_wallpaper(cls, **params) -> Generator[Optional[files.File], None, None]:
        children: Optional[list] = None
        sort = params.pop(CONFIG_SORT)
        url = request.join(URL_BASE, params.pop(CONFIG_SUBS), sort)
        if sort not in (SORTS[2], SORTS[4]):
            del params[CONFIG_TIME]
        params['limit'] = '100'
        while True:
            if not children:
                auth = next(_get_auth(cls.CURRENT_CONFIG[CONFIG_ID]))
                if auth is not None:
                    response = request.get(url, params=params, auth=auth)
                    if response:
                        data = response.json()['data']
                        params['after'] = data['after']
                        children = list(_iter_children(data['children']))
                if not children:
                    yield
                    continue
            data = children.pop(0)['data']
            while not cls._filter_orientation(data['preview']['images'][0]['source']):
                if not children:
                    break
                data = children.pop(0)['data']
            else:
                url_child = data['url']
                yield files.File(url_child, f'{data["title"]}{os.path.splitext(url_child)[1]}')

    @classmethod
    def create_menu(cls):
        item_time_enable = gui.add_mapped_submenu(cls.strings.REDDIT_MENU_TIME, {time_: getattr(
            cls.strings, f'REDDIT_TIME_{time_}') for time_ in TIMES}, cls.CURRENT_CONFIG, CONFIG_TIME).enable
        gui.add_mapped_submenu(cls.strings.REDDIT_MENU_SORT, {sort: getattr(
            cls.strings, f'REDDIT_SORT_{sort}') for sort in SORTS}, cls.CURRENT_CONFIG,
                               CONFIG_SORT, on_click=functools.partial(_on_sort, item_time_enable), position=0)
        _on_sort(item_time_enable, cls.CURRENT_CONFIG[CONFIG_SORT])
        gui.add_mapped_submenu(cls.strings.REDDIT_MENU_ORIENTATION, {orientation: getattr(
            cls.strings, f'REDDIT_ORIENTATION_{orientation}') for orientation
            in ORIENTATIONS}, cls.CURRENT_CONFIG, CONFIG_ORIENTATION)

    @classmethod
    def _filter_orientation(cls, source: dict) -> bool:
        orientation = cls.CURRENT_CONFIG[CONFIG_ORIENTATION]
        return orientation == ORIENTATIONS[0] or orientation == ORIENTATIONS[
            math.ceil(source['height'] / source['width'])]
