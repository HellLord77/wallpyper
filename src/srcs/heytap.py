import os
from typing import Iterator
from typing import Optional
from typing import TypedDict

import gui
import validator
from libs import request
from . import File
from . import Source

URL_BASE = 'https://osp.haokan.mobi'
URL_API = request.join_url(URL_BASE, 'api', 'list')
URL_DETAILS = request.join_url(URL_BASE, 'detail')

CONFIG_TYPE = 'typeName'

TYPES = (
    'Hot', 'Animals', 'Home Style', 'Food', 'Travel', 'Art', 'Car', 'Universe',
    'Movie', 'Plants', 'Sports', 'Life', 'Technology', 'Cute Pet', 'Male Star')


class HeyTapPictoral(Source):
    NAME = '# HeyTap Pictoral'
    VERSION = '0.0.1'
    URL = URL_BASE
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_TYPE: str})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_TYPE: TYPES[0]}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_contains, CONFIG_TYPE, TYPES)

    @classmethod
    def create_menu(cls):
        gui.add_submenu_radio(cls._text('MENU_TYPE'), {
            type_: cls._text(f'TYPE_{type_}') for type_ in TYPES},
                              cls.CURRENT_CONFIG, CONFIG_TYPE)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[File]]:
        groups = []
        while True:
            if not groups:
                response = request.post(URL_API, params)
                if response:
                    groups = response.json()['pageDataList']
                if not groups:
                    yield
                    continue
            group = groups.pop(0)
            title = group['title']
            url_group = request.join_url(URL_DETAILS, group['groupId'])
            for index, image in enumerate(group['list'], 1):
                link = image['url'].rsplit('@', 1)[0]
                yield File(link, f'{title} ({index}){os.path.splitext(link)[1]}', url=url_group)
