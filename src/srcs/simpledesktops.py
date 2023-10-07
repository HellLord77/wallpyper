import operator
from typing import Callable
from typing import Iterator
from typing import Optional
from typing import TypedDict

import gui
import validator
from libs import request
from libs import sgml
from libs import utils
from . import File
from . import Source

# noinspection HttpUrlsUsage
URL_BASE = 'http://simpledesktops.com'
URL_BROWSE = request.join_url(URL_BASE, 'browse')

CONFIG_PAGE = 'page'

_PAGE = utils.MutableInt()


class SimpleDesktops(Source):
    NAME = 'Simple Desktops'
    VERSION = '0.0.2'
    URL = URL_BASE
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_PAGE: int})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_PAGE: 1}

    _set_tooltip: Callable[[str], bool]

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_positive, CONFIG_PAGE)
        if saving:
            cls.CURRENT_CONFIG[CONFIG_PAGE] = _PAGE.get()
        else:
            _PAGE.set(cls.CURRENT_CONFIG[CONFIG_PAGE])

    @classmethod
    def create_menu(cls):
        cls._set_tooltip = gui.add_menu_item(
            cls._text('LABEL_RESET'), on_click=cls._on_reset).set_tooltip
        cls._set_tooltip(cls._text('TOOLTIP_FMT_PAGE').format(_PAGE))

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[File]]:
        desktops = []
        _PAGE.set(params.pop(CONFIG_PAGE))
        while True:
            if not desktops:
                cls._set_tooltip(
                    cls._text('TOOLTIP_FMT_PAGE').format(_PAGE))
                response = request.get(request.join_url(URL_BROWSE, str(_PAGE)))
                if int(_PAGE) != 1 and response.status_code == request.Status.NOT_FOUND:
                    _PAGE.set(1)
                    continue
                if response:
                    desktops = list(sgml.loads(
                        response.text).find_all('div', classes='desktop'))
                if not desktops:
                    yield
                    continue
            desktop = desktops.pop(0)[0]
            operator.iadd(_PAGE, not desktops)
            yield File(desktop[0]['src'].rsplit('.', 2)[0],
                       url=request.join_url(URL_BASE, desktop['href']))

    @classmethod
    def _on_reset(cls):
        cls.CURRENT_CONFIG[CONFIG_PAGE] = 1
        cls._set_tooltip(cls._text('TOOLTIP_FMT_PAGE').format(1))
