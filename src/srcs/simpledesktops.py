from typing import Callable
from typing import Iterator
from typing import Optional
from typing import TypedDict

import gui
import validator
from libs import request
from libs import sgml
from . import File
from . import Source

# noinspection HttpUrlsUsage
URL_BASE = 'http://simpledesktops.com'
URL_BROWSE = request.join_url(URL_BASE, 'browse')

CONFIG_PAGE = 'page'


class SimpleDesktops(Source):
    NAME = 'Simple Desktops'
    VERSION = '0.0.3'
    URL = URL_BASE
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_PAGE: int})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_PAGE: 1}

    _page: int
    _set_tooltip: Callable[[str], bool]

    @classmethod
    def load_config(cls):
        cls._fix_config(validator.ensure_positive, CONFIG_PAGE)

        cls._page = cls.CURRENT_CONFIG[CONFIG_PAGE]

    @classmethod
    def dump_config(cls) -> TCONFIG:
        dumped = super().dump_config()
        dumped[CONFIG_PAGE] = cls._page
        return dumped

    @classmethod
    def create_menu(cls):
        cls._set_tooltip = gui.add_menu_item(cls._text('LABEL_RESET'), on_click=cls._on_reset).set_tooltip
        cls._on_reset(cls.CURRENT_CONFIG[CONFIG_PAGE])

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[File]]:
        desktops = []
        cls._page = params.pop(CONFIG_PAGE)
        while True:
            if not desktops:
                cls._set_tooltip(cls._text('TOOLTIP_FMT_PAGE').format(cls._page))
                response = request.get(request.join_url(URL_BROWSE, str(cls._page)))
                if (int(cls._page) != cls.DEFAULT_CONFIG[CONFIG_PAGE] and
                        response.status_code == request.Status.NOT_FOUND):
                    cls._page = cls.DEFAULT_CONFIG[CONFIG_PAGE]
                    continue
                if response:
                    desktops = list(sgml.loads(response.text).find_all('div', classes='desktop'))
                if not desktops:
                    yield
                    continue
            desktop = desktops.pop(0)[0]
            cls._page += not desktops
            yield File(desktop[0]['src'].rsplit('.', 2)[0],
                       url=request.join_url(URL_BASE, desktop['href']))

    @classmethod
    def _on_reset(cls, page: int = DEFAULT_CONFIG[CONFIG_PAGE]):
        cls.CURRENT_CONFIG[CONFIG_PAGE] = page
        cls._set_tooltip(cls._text('TOOLTIP_FMT_PAGE').format(page))
