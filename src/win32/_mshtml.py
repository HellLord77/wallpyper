from __future__ import annotations as _

from typing import Optional

from libs import ctyped
from . import _utils


class _Property:
    def __init__(self, name: str):
        self._getter = f'get_{name}'
        self._setter = f'put_{name}'


class _Getter(_Property):
    def __get__(self, instance, owner):
        raise NotImplementedError


class _Setter(_Property):
    def __set__(self, instance, value: int):
        getattr(instance.obj, self._setter)(value)


class _VariantBoolGetter(_Getter):
    def __get__(self, instance, owner) -> bool:
        variant_bool = ctyped.type.VARIANT_BOOL()
        getattr(instance.obj, self._getter)(ctyped.byref(variant_bool))
        return bool(variant_bool.value)


class _VariantBoolSetter(_Setter):
    pass


class _VariantBoolGetterSetter(_VariantBoolSetter, _VariantBoolGetter):
    pass


class _CIntGetter(_Getter):
    def __get__(self, instance, owner) -> int:
        c_int = ctyped.type.c_int()
        getattr(instance.obj, self._getter)(ctyped.byref(c_int))
        return c_int.value


class _CIntSetter(_Setter):
    pass


class _CIntGetterSetter(_CIntSetter, _CIntGetter):
    pass


class _CLongGetter(_Getter):
    def __get__(self, instance, owner) -> int:
        c_long = ctyped.type.c_long()
        getattr(instance.obj, self._getter)(ctyped.byref(c_long))
        return c_long.value


class _CLongSetter(_Setter):
    pass


class _CLongGetterSetter(_CLongSetter, _CLongGetter):
    pass
    pass


class _BSTRGetter(_Property):
    def __get__(self, instance, owner) -> Optional[str]:
        with _utils.get_bstr() as bstr:
            getattr(instance.obj, self._getter)(ctyped.byref(bstr))
            return ctyped.type.c_wchar_p.from_buffer(bstr).value


class _BSTRSetter(_Property):
    def __set__(self, instance, value: str):
        with _utils.get_bstr(value) as value:
            getattr(instance.obj, self._setter)(value)


class _BSTRGetterSetter(_BSTRSetter, _BSTRGetter):
    pass


class _HTMLDocument2Getter(_Property):
    def __get__(self, instance, owner) -> HTMLDocument2:
        with ctyped.init_com(ctyped.interface.IHTMLDocument2, False) as html_document_2:
            getattr(instance.obj, self._getter)(ctyped.byref(html_document_2))
            return HTMLDocument2(html_document_2)


class _HTMLElementGetter(_Property):
    def __get__(self, instance, owner) -> HTMLElement:
        with ctyped.init_com(ctyped.interface.IHTMLElement, False) as html_element:
            getattr(instance.obj, self._getter)(ctyped.byref(html_element))
            return HTMLElement(html_element)


class _HTMLElementCollectionGetter(_Property):
    def __get__(self, instance, owner) -> HTMLElementCollection:
        with ctyped.init_com(ctyped.interface.IHTMLElementCollection, False) as html_element_collection:
            getattr(instance.obj, self._getter)(ctyped.byref(html_element_collection))
            return HTMLElementCollection(html_element_collection)


class WebBrowser2:
    def __init__(self, obj: ctyped.interface.IWebBrowser2):
        self.obj = ctyped.interface.IWebBrowser2()
        obj.QueryInterface(*ctyped.macro.IID_PPV_ARGS(self.obj))

    def __del__(self):
        if self.obj:
            self.obj.Release()

    def go_back(self) -> bool:
        return ctyped.macro.SUCCEEDED(self.obj.GoBack())

    def go_forward(self) -> bool:
        return ctyped.macro.SUCCEEDED(self.obj.GoForward())

    def go_home(self) -> bool:
        return ctyped.macro.SUCCEEDED(self.obj.GoHome())

    def go_search(self) -> bool:
        return ctyped.macro.SUCCEEDED(self.obj.GoSearch())

    def navigate(self, url: str) -> bool:
        with _utils.get_bstr(url) as bstr:
            return ctyped.macro.SUCCEEDED(self.obj.Navigate(bstr, None, None, None, None))

    def refresh(self) -> bool:
        return ctyped.macro.SUCCEEDED(self.obj.Refresh())

    def stop(self) -> bool:
        return ctyped.macro.SUCCEEDED(self.obj.Stop())

    document = _HTMLDocument2Getter('Document')
    left = _CLongGetterSetter('Left')
    top = _CLongGetterSetter('Top')
    width = _CLongGetterSetter('Width')
    height = _CLongGetterSetter('Height')

    def quit(self) -> bool:
        return ctyped.macro.SUCCEEDED(self.obj.Quit())

    visible = _VariantBoolGetterSetter('Visible')
    status_bar = _VariantBoolGetterSetter('StatusBar')
    status_text = _BSTRGetterSetter('StatusText')
    tool_bar = _CIntGetterSetter('ToolBar')
    menu_bar = _VariantBoolGetterSetter('MenuBar')
    full_screen = _VariantBoolGetterSetter('FullScreen')

    @property
    def ready_state(self) -> ctyped.enum.READYSTATE:
        ready_state = ctyped.enum.READYSTATE()
        self.obj.get_ReadyState(ctyped.byref(ready_state))
        return ready_state

    offline = _VariantBoolGetterSetter('Offline')
    silent = _VariantBoolGetterSetter('Silent')
    register_as_browser = _VariantBoolGetterSetter('RegisterAsBrowser')
    register_as_drop_target = _VariantBoolGetterSetter('RegisterAsDropTarget')
    theater_mode = _VariantBoolGetterSetter('TheaterMode')
    address_bar = _VariantBoolGetterSetter('AddressBar')
    resizable = _VariantBoolGetterSetter('Resizable')


class HTMLDocument2:
    def __init__(self, obj: ctyped.interface.IDispatch):
        self.obj = ctyped.interface.IHTMLDocument2()
        obj.QueryInterface(*ctyped.macro.IID_PPV_ARGS(self.obj))

    def __del__(self):
        if self.obj:
            self.obj.Release()

    all = _HTMLElementCollectionGetter('all')
    body = _HTMLElementGetter('body')
    active_element = _HTMLElementGetter('activeElement')
    images = _HTMLElementCollectionGetter('images')
    applets = _HTMLElementCollectionGetter('applets')
    links = _HTMLElementCollectionGetter('links')
    forms = _HTMLElementCollectionGetter('forms')
    anchors = _HTMLElementCollectionGetter('anchors')
    title = _BSTRGetterSetter('title')
    scripts = _HTMLElementCollectionGetter('scripts')
    design_mode = _BSTRGetterSetter('designMode')
    ready_state = _BSTRGetter('readyState')
    embeds = _HTMLElementCollectionGetter('embeds')
    plugins = _HTMLElementCollectionGetter('plugins')
    url = _BSTRGetterSetter('URL')
    domain = _BSTRGetterSetter('domain')
    cookie = _BSTRGetterSetter('cookie')

    def close(self) -> bool:
        return ctyped.macro.SUCCEEDED(self.obj.close())

    def clear(self) -> bool:
        return ctyped.macro.SUCCEEDED(self.obj.clear())

    @property
    def parent_window(self) -> HTMLWindow2:
        with ctyped.init_com(ctyped.interface.IHTMLWindow2, False) as html_window_2:
            self.obj.get_parentWindow(ctyped.byref(html_window_2))
            return HTMLWindow2(html_window_2)

    def to_string(self) -> str:
        with _utils.get_bstr() as bstr:
            self.obj.toString(ctyped.byref(bstr))
            return ctyped.type.c_wchar_p.from_buffer(bstr).value


class HTMLDocument7:
    def __init__(self, obj: ctyped.interface.IDispatch):
        self.obj = ctyped.interface.IHTMLDocument7()
        obj.QueryInterface(*ctyped.macro.IID_PPV_ARGS(self.obj))

    def __del__(self):
        if self.obj:
            self.obj.Release()

    head = _HTMLElementGetter('head')


class HTMLWindow2:
    def __init__(self, obj: ctyped.interface.IHTMLWindow2):
        self.obj = ctyped.interface.IHTMLWindow2()
        obj.QueryInterface(*ctyped.macro.IID_PPV_ARGS(self.obj))

    def __del__(self):
        if self.obj:
            self.obj.Release()

    default_status = _BSTRGetterSetter('defaultStatus')
    status = _BSTRGetterSetter('status')

    def alert(self, message: str) -> bool:
        with _utils.get_bstr(message) as bstr:
            return ctyped.macro.SUCCEEDED(self.obj.alert(bstr))

    def close(self) -> bool:
        return ctyped.macro.SUCCEEDED(self.obj.close())

    name = _BSTRGetterSetter('name')

    def navigate(self, url: str) -> bool:
        with _utils.get_bstr(url) as bstr:
            return ctyped.macro.SUCCEEDED(self.obj.navigate(bstr))

    document = _HTMLDocument2Getter('document')

    def focus(self) -> bool:
        return ctyped.macro.SUCCEEDED(self.obj.focus())

    def blur(self) -> bool:
        return ctyped.macro.SUCCEEDED(self.obj.blur())

    def scroll(self, x: int, y: int) -> bool:
        return ctyped.macro.SUCCEEDED(self.obj.scroll(x, y))

    def exec_script(self, code: str, language: str = 'JScript') -> bool:
        with _utils.get_bstr(code) as bstr, _utils.get_bstr(language) as bstr_2:
            return ctyped.macro.SUCCEEDED(self.obj.execScript(bstr, bstr_2, ctyped.byref(ctyped.struct.VARIANT())))

    def to_string(self) -> str:
        with _utils.get_bstr() as bstr:
            self.obj.toString(ctyped.byref(bstr))
            return ctyped.type.c_wchar_p.from_buffer(bstr).value

    def scroll_by(self, x: int, y: int) -> bool:
        return ctyped.macro.SUCCEEDED(self.obj.scrollBy(x, y))

    def scroll_to(self, x: int, y: int) -> bool:
        return ctyped.macro.SUCCEEDED(self.obj.scrollTo(x, y))

    def move_to(self, x: int, y: int) -> bool:
        return ctyped.macro.SUCCEEDED(self.obj.moveTo(x, y))

    def move_by(self, x: int, y: int) -> bool:
        return ctyped.macro.SUCCEEDED(self.obj.moveBy(x, y))

    def resize_to(self, x: int, y: int) -> bool:
        return ctyped.macro.SUCCEEDED(self.obj.resizeTo(x, y))

    def resize_by(self, x: int, y: int) -> bool:
        return ctyped.macro.SUCCEEDED(self.obj.resizeBy(x, y))


class HTMLElement:
    def __init__(self, obj: ctyped.interface.IDispatch):
        self.obj = ctyped.interface.IHTMLElement()
        obj.QueryInterface(*ctyped.macro.IID_PPV_ARGS(self.obj))

    def __del__(self):
        if self.obj:
            self.obj.Release()

    def get_attribute(self, attribute_name: str, flags: int = 0) -> Optional[bool | int | float | str | ctyped.interface.IDispatch]:
        with _utils.get_bstr(attribute_name) as bstr:
            variant = ctyped.struct.VARIANT()
            self.obj.getAttribute(bstr, flags, ctyped.byref(variant))
            try:
                return _utils.get_variant_value(variant)
            finally:
                ctyped.lib.OleAut32.VariantClear(ctyped.byref(variant))

    class_name = _BSTRGetterSetter('className')
    id = _BSTRGetterSetter('id')
    tag_name = _BSTRGetter('tagName')
    parent_element = _HTMLElementGetter('parentElement')
    title = _BSTRGetterSetter('title')
    language = _BSTRGetterSetter('language')
    lang = _BSTRGetterSetter('lang')
    inner_html = _BSTRGetterSetter('innerHTML')
    inner_text = _BSTRGetterSetter('innerText')
    outer_html = _BSTRGetterSetter('outerHTML')
    outer_text = _BSTRGetterSetter('outerText')

    def to_string(self) -> str:
        with _utils.get_bstr() as bstr:
            self.obj.toString(ctyped.byref(bstr))
            return ctyped.type.c_wchar_p.from_buffer(bstr).value


class HTMLElementCollection:
    def __init__(self, obj: ctyped.interface.IDispatch):
        self.obj = ctyped.interface.IHTMLElementCollection()
        obj.QueryInterface(*ctyped.macro.IID_PPV_ARGS(self.obj))

    def __del__(self):
        if self.obj:
            self.obj.Release()

    def to_string(self) -> str:
        with _utils.get_bstr() as bstr:
            self.obj.toString(ctyped.byref(bstr))
            return ctyped.type.c_wchar_p.from_buffer(bstr).value

    length = _CLongGetterSetter('length')

    def item(self, index: int) -> HTMLElement:
        variant = ctyped.struct.VARIANT()
        variant.U.S.vt = ctyped.enum.VARENUM.I4.value
        variant.U.S.U.intVal = index
        with ctyped.init_com(ctyped.interface.IDispatch, False) as dispatch:
            self.obj.item(variant, variant, ctyped.byref(dispatch))
            return HTMLElement(dispatch)

    def tags(self, tag_name: str) -> HTMLElementCollection:
        variant = ctyped.struct.VARIANT()
        variant.U.S.vt = ctyped.enum.VARENUM.BSTR.value
        with _utils.get_bstr(tag_name) as bstr:
            variant.U.S.U.bstrVal = bstr
            with ctyped.init_com(ctyped.interface.IDispatch, False) as dispatch:
                self.obj.tags(variant, ctyped.byref(dispatch))
                return HTMLElementCollection(dispatch)
