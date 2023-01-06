from __future__ import annotations as _

from typing import Optional

from libs import ctyped
from libs.ctyped.interface.um import ExDisp, MsHTML, oaidl
from libs.ctyped.lib import oleaut32
from .. import _com, _utils


class _HTMLDocument2Getter(_com.Getter):
    def __get__(self, instance: _com.Unknown, owner: type[_com.Unknown]) -> HTMLDocument2:
        with ctyped.interface.COM[MsHTML.IHTMLDocument2]() as obj:
            # noinspection PyProtectedMember
            getattr(instance._obj, self._getter)(ctyped.byref(obj))
            return HTMLDocument2(obj)


class _HTMLElementGetter(_com.Getter):
    def __get__(self, instance: _com.Unknown, owner: type[_com.Unknown]) -> HTMLElement:
        with ctyped.interface.COM[MsHTML.IHTMLElement]() as obj:
            # noinspection PyProtectedMember
            getattr(instance._obj, self._getter)(ctyped.byref(obj))
            return HTMLElement(obj)


class _HTMLElementCollectionGetter(_com.Getter):
    def __get__(self, instance: _com.Unknown, owner: type[_com.Unknown]) -> HTMLElementCollection:
        with ctyped.interface.COM[MsHTML.IHTMLElementCollection]() as obj:
            # noinspection PyProtectedMember
            getattr(instance._obj, self._getter)(ctyped.byref(obj))
            return HTMLElementCollection(obj)


class WebBrowser2(_com.Unknown):
    _obj: ExDisp.IWebBrowser2

    def go_back(self) -> bool:
        return ctyped.macro.SUCCEEDED(self._obj.GoBack())

    def go_forward(self) -> bool:
        return ctyped.macro.SUCCEEDED(self._obj.GoForward())

    def go_home(self) -> bool:
        return ctyped.macro.SUCCEEDED(self._obj.GoHome())

    def go_search(self) -> bool:
        return ctyped.macro.SUCCEEDED(self._obj.GoSearch())

    def navigate(self, url: str) -> bool:
        with _utils.get_bstr(url) as bstr:
            return ctyped.macro.SUCCEEDED(self._obj.Navigate(
                bstr, ctyped.NULLPTR, ctyped.NULLPTR, ctyped.NULLPTR, ctyped.NULLPTR))

    def refresh(self) -> bool:
        return ctyped.macro.SUCCEEDED(self._obj.Refresh())

    def stop(self) -> bool:
        return ctyped.macro.SUCCEEDED(self._obj.Stop())

    document = _HTMLDocument2Getter('Document')
    left = _com.CLongGetterSetter('Left')
    top = _com.CLongGetterSetter('Top')
    width = _com.CLongGetterSetter('Width')
    height = _com.CLongGetterSetter('Height')

    def quit(self) -> bool:
        return ctyped.macro.SUCCEEDED(self._obj.Quit())

    visible = _com.VariantBoolGetterSetter('Visible')
    status_bar = _com.VariantBoolGetterSetter('StatusBar')
    status_text = _utils.BSTRGetterSetter('StatusText')
    tool_bar = _com.CIntGetterSetter('ToolBar')
    menu_bar = _com.VariantBoolGetterSetter('MenuBar')
    full_screen = _com.VariantBoolGetterSetter('FullScreen')

    @property
    def ready_state(self) -> ctyped.enum.READYSTATE:
        ready_state = ctyped.enum.READYSTATE()
        self._obj.get_ReadyState(ctyped.byref(ready_state))
        return ready_state

    offline = _com.VariantBoolGetterSetter('Offline')
    silent = _com.VariantBoolGetterSetter('Silent')
    register_as_browser = _com.VariantBoolGetterSetter('RegisterAsBrowser')
    register_as_drop_target = _com.VariantBoolGetterSetter('RegisterAsDropTarget')
    theater_mode = _com.VariantBoolGetterSetter('TheaterMode')
    address_bar = _com.VariantBoolGetterSetter('AddressBar')
    resizable = _com.VariantBoolGetterSetter('Resizable')


class HTMLElement(_com.Unknown):
    _obj: MsHTML.IHTMLElement

    def get_attribute(self, attribute_name: str,
                      flags: int = 0) -> Optional[bool | int | float | str | oaidl.IDispatch]:
        with _utils.get_bstr(attribute_name) as bstr:
            variant = ctyped.struct.VARIANT()
            self._obj.getAttribute(bstr, flags, ctyped.byref(variant))
            try:
                return _utils.get_variant_value(variant)
            finally:
                oleaut32.VariantClear(ctyped.byref(variant))

    class_name = _utils.BSTRGetterSetter('className')
    id = _utils.BSTRGetterSetter('id')
    tag_name = _utils.BSTRGetter('tagName')
    parent_element = _HTMLElementGetter('parentElement')
    title = _utils.BSTRGetterSetter('title')
    language = _utils.BSTRGetterSetter('language')
    lang = _utils.BSTRGetterSetter('lang')
    inner_html = _utils.BSTRGetterSetter('innerHTML')
    inner_text = _utils.BSTRGetterSetter('innerText')
    outer_html = _utils.BSTRGetterSetter('outerHTML')
    outer_text = _utils.BSTRGetterSetter('outerText')
    _to_string = _utils.BSTRGetter('toString')

    def to_string(self) -> str:
        return self._to_string


class HTMLElementCollection(_com.Unknown):
    _obj: MsHTML.IHTMLElementCollection

    _to_string = _utils.BSTRGetter('toString')

    def to_string(self) -> str:
        return self._to_string

    length = _com.CLongGetterSetter('length')

    def item(self, index: int) -> HTMLElement:
        variant = ctyped.struct.VARIANT()
        variant.U.S.vt = ctyped.enum.VARENUM.I4.value
        variant.U.S.U.intVal = index
        with ctyped.interface.COM[oaidl.IDispatch]() as dispatch:
            self._obj.item(variant, variant, ctyped.byref(dispatch))
            return HTMLElement(dispatch)

    def tags(self, tag_name: str) -> HTMLElementCollection:
        variant = ctyped.struct.VARIANT()
        variant.U.S.vt = ctyped.enum.VARENUM.BSTR.value
        with _utils.get_bstr(tag_name) as bstr:
            variant.U.S.U.bstrVal = bstr
            with ctyped.interface.COM[oaidl.IDispatch]() as dispatch:
                self._obj.tags(variant, ctyped.byref(dispatch))
                return HTMLElementCollection(dispatch)


class HTMLDocument7(_com.Unknown):
    _obj: MsHTML.IHTMLDocument7

    head = _HTMLElementGetter('head')


class HTMLDocument2(_com.Unknown):
    _obj: MsHTML.IHTMLDocument2

    all = _HTMLElementCollectionGetter('all')
    body = _HTMLElementGetter('body')
    active_element = _HTMLElementGetter('activeElement')
    images = _HTMLElementCollectionGetter('images')
    applets = _HTMLElementCollectionGetter('applets')
    links = _HTMLElementCollectionGetter('links')
    forms = _HTMLElementCollectionGetter('forms')
    anchors = _HTMLElementCollectionGetter('anchors')
    title = _utils.BSTRGetterSetter('title')
    scripts = _HTMLElementCollectionGetter('scripts')
    design_mode = _utils.BSTRGetterSetter('designMode')
    ready_state = _utils.BSTRGetter('readyState')
    embeds = _HTMLElementCollectionGetter('embeds')
    plugins = _HTMLElementCollectionGetter('plugins')
    url = _utils.BSTRGetterSetter('URL')
    domain = _utils.BSTRGetterSetter('domain')
    cookie = _utils.BSTRGetterSetter('cookie')

    def close(self) -> bool:
        return ctyped.macro.SUCCEEDED(self._obj.close())

    def clear(self) -> bool:
        return ctyped.macro.SUCCEEDED(self._obj.clear())

    @property
    def parent_window(self) -> HTMLWindow2:
        with ctyped.interface.COM[MsHTML.IHTMLWindow2]() as html_window_2:
            self._obj.get_parentWindow(ctyped.byref(html_window_2))
            return HTMLWindow2(html_window_2)

    def to_string(self) -> str:
        with _utils.get_bstr() as bstr:
            self._obj.toString(ctyped.byref(bstr))
            return ctyped.type.c_wchar_p.from_buffer(bstr).value


class HTMLWindow2(_com.Unknown):
    _obj: MsHTML.IHTMLWindow2

    default_status = _utils.BSTRGetterSetter('defaultStatus')
    status = _utils.BSTRGetterSetter('status')

    def alert(self, message: str) -> bool:
        with _utils.get_bstr(message) as bstr:
            return ctyped.macro.SUCCEEDED(self._obj.alert(bstr))

    def close(self) -> bool:
        return ctyped.macro.SUCCEEDED(self._obj.close())

    name = _utils.BSTRGetterSetter('name')

    def navigate(self, url: str) -> bool:
        with _utils.get_bstr(url) as bstr:
            return ctyped.macro.SUCCEEDED(self._obj.navigate(bstr))

    document = _HTMLDocument2Getter('document')

    def focus(self) -> bool:
        return ctyped.macro.SUCCEEDED(self._obj.focus())

    def blur(self) -> bool:
        return ctyped.macro.SUCCEEDED(self._obj.blur())

    def scroll(self, x: int, y: int) -> bool:
        return ctyped.macro.SUCCEEDED(self._obj.scroll(x, y))

    def exec_script(self, code: str, language: str = 'JScript') -> bool:
        with _utils.get_bstr(code) as bstr, _utils.get_bstr(language) as bstr_2:
            return ctyped.macro.SUCCEEDED(self._obj.execScript(bstr, bstr_2, ctyped.byref(ctyped.struct.VARIANT())))

    def to_string(self) -> str:
        with _utils.get_bstr() as bstr:
            self._obj.toString(ctyped.byref(bstr))
            return ctyped.type.c_wchar_p.from_buffer(bstr).value

    def scroll_by(self, x: int, y: int) -> bool:
        return ctyped.macro.SUCCEEDED(self._obj.scrollBy(x, y))

    def scroll_to(self, x: int, y: int) -> bool:
        return ctyped.macro.SUCCEEDED(self._obj.scrollTo(x, y))

    def move_to(self, x: int, y: int) -> bool:
        return ctyped.macro.SUCCEEDED(self._obj.moveTo(x, y))

    def move_by(self, x: int, y: int) -> bool:
        return ctyped.macro.SUCCEEDED(self._obj.moveBy(x, y))

    def resize_to(self, x: int, y: int) -> bool:
        return ctyped.macro.SUCCEEDED(self._obj.resizeTo(x, y))

    def resize_by(self, x: int, y: int) -> bool:
        return ctyped.macro.SUCCEEDED(self._obj.resizeBy(x, y))
