import http
import operator
from typing import Callable, Iterator, Optional, TypedDict

import gui
import validator
from libs import files, request, minihtml, utils
from . import Source

_ATTRS = {'class': 'desktop'}
_PAGE = utils.MutableInt()

# noinspection HttpUrlsUsage
URL_BASE = 'http://simpledesktops.com'
URL_BROWSE = request.join(URL_BASE, 'browse')

CONFIG_PAGE = 'page'


class SimpleDesktops(Source):
    NAME = 'Simple Desktops'
    VERSION = '0.0.1'
    URL = URL_BASE
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_PAGE: int})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_PAGE: 1}

    _set_tooltip: Optional[Callable[[str], bool]] = None

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
            cls.STRINGS.SIMPLEDESKTOPS_LABEL_RESET, on_click=cls._on_reset).set_tooltip
        cls._set_tooltip(cls.STRINGS.SIMPLEDESKTOPS_TOOLTIP_TEMPLATE_PAGE.format(_PAGE))

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[files.File]]:
        desktops: Optional[list] = None
        _PAGE.set(params.pop(CONFIG_PAGE))
        while True:
            if not desktops:
                cls._set_tooltip(
                    cls.STRINGS.SIMPLEDESKTOPS_TOOLTIP_TEMPLATE_PAGE.format(_PAGE))
                response = request.get(request.join(URL_BROWSE, str(_PAGE)))
                if response.status_code == http.HTTPStatus.NOT_FOUND:
                    _PAGE.set(cls.DEFAULT_CONFIG[CONFIG_PAGE])
                    continue
                if response:
                    desktops = list(minihtml.find_elements(
                        minihtml.loads(response.text).iter_all_children(), 'div', _ATTRS))
            if not desktops:
                yield
                continue
            desktop = files.File(desktops.pop(
                0).get_child().get_child().attributes['src'].rsplit('.', 2)[0])
            operator.iadd(_PAGE, not desktops)
            yield desktop

    @classmethod
    def _on_reset(cls):
        page = cls.CURRENT_CONFIG[CONFIG_PAGE] = cls.DEFAULT_CONFIG[CONFIG_PAGE]
        cls._set_tooltip(cls.STRINGS.SIMPLEDESKTOPS_TOOLTIP_TEMPLATE_PAGE.format(page))
