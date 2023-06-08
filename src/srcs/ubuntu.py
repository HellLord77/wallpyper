import itertools
import os
import random
from typing import Iterator, Optional, TypedDict

import gui
import validator
from libs import request, sgml
from . import File, Source

URL_PLAIN = request.join_url('https://git.launchpad.net', 'ubuntu', '+source', 'ubuntu-wallpapers', 'plain')
URL_CONTEST = request.join_url(URL_PLAIN, 'contest')

CONFIG_CONTEST = 'contest'
CONFIG_SORT = 'sort'

CONTESTS = (
    'karmic', 'lucid', 'maverick', 'natty', 'oneiric', 'precise',
    'quantal', 'raring', 'saucy', 'trusty', 'utopic', 'vivid', 'wily',
    'xenial', 'yakkety', 'zesty', 'artful', 'bionic', 'cosmic', 'disco',
    'eoan', 'focal', 'groovy', 'hirsute', 'impish', 'jammy', 'kinetic', 'lunar')
SORTS = {
    'oldest': lambda x: x,
    'newest': lambda x: reversed(x),
    'random': lambda x: random.sample(x, k=len(x))}


class UbuntuWallpapers(Source):
    NAME = 'ubuntu-wallpapers'
    VERSION = '0.0.2'
    ICON = 'png'
    URL = 'https://launchpad.net/ubuntu-wallpapers'
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_CONTEST: list[bool],
        CONFIG_SORT: str})
    DEFAULT_CONFIG = {
        CONFIG_CONTEST: [True] * len(CONTESTS),
        CONFIG_SORT: next(itertools.islice(SORTS, 1, None))}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_len, CONFIG_CONTEST, len(CONTESTS))
        cls._fix_config(validator.ensure_truthy, CONFIG_CONTEST, any)
        cls._fix_config(validator.ensure_contains, CONFIG_SORT, SORTS)

    @classmethod
    def create_menu(cls):
        gui.add_submenu_check(cls._text('MENU_CONTESTS'), (cls._text(
            f'CONTEST_{contest}') for contest in CONTESTS),
                              (1, None), cls.CURRENT_CONFIG, CONFIG_CONTEST)
        gui.add_submenu_radio(cls._text('MENU_SORT'), {sort: cls._text(
            f'SORT_{sort}') for sort in SORTS}, cls.CURRENT_CONFIG, CONFIG_SORT)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[File]]:
        files_: Optional[list] = None
        contests = itertools.cycle(SORTS[params.pop(CONFIG_SORT)](tuple(
            itertools.compress(CONTESTS, params.pop(CONFIG_CONTEST)))))
        while True:
            if not files_:
                response = request.get(request.join_url(
                    URL_CONTEST, f'{next(contests)}.xml'))
                if response:
                    files_ = list(sgml.loads(
                        f'<xml>{response.text}</xml>').find_all('file'))
                if not files_:
                    yield
                    continue
            yield File(request.join_url(
                URL_PLAIN, os.path.basename(files_.pop(0).get_text())))
