from __future__ import annotations as _

import libs.ctyped as ctyped
from . import _utils


class _Descriptor:
    def __init__(self, name: str):
        self._getter = f'get_{name}'
        self._setter = f'put_{name}'


class _VariantBool(_Descriptor):
    def __get__(self, instance, owner) -> bool:
        variant_bool = ctyped.type.VARIANT_BOOL()
        getattr(instance.obj, self._getter)(ctyped.byref(variant_bool))
        return bool(variant_bool.value)

    def __set__(self, instance, value: bool):
        getattr(instance.obj, self._setter)(value)

class _CInt(_Descriptor):
    def __get__(self, instance, owner) -> int:
        c_int = ctyped.type.c_int()
        getattr(instance.obj, self._getter)(ctyped.byref(c_int))
        return c_int.value

    def __set__(self, instance, value: int):
        getattr(instance.obj, self._setter)(value)

class _CLong(_Descriptor):
    def __get__(self, instance, owner) -> int:
        c_long = ctyped.type.c_long()
        getattr(instance.obj, self._getter)(ctyped.byref(c_long))
        return c_long.value

    def __set__(self, instance, value: int):
        getattr(instance.obj, self._setter)(value)


class _BSTR(_Descriptor):
    def __get__(self, instance, owner) -> str:
        with _utils.get_bstr() as bstr:
            getattr(instance.obj, self._getter)(ctyped.byref(bstr))
            return ctyped.type.c_wchar_p.from_buffer(bstr).value

    def __set__(self, instance, value: str):
        with _utils.get_bstr(value) as value:
            getattr(instance.obj, self._setter)(value)


class WebBrowser2:
    def __init__(self):
        self.obj = ctyped.interface.IWebBrowser2()
        # noinspection PyProtectedMember
        ctyped.lib.Ole32.CoCreateInstance(ctyped.byref(ctyped.get_guid(self.obj._CLSID)),
                                          None, ctyped.const.CLSCTX_ALL, *ctyped.macro.IID_PPV_ARGS(self.obj))

    def __del__(self):
        if self.obj:
            self.obj.Release()
        ctyped.lib.Ole32.CoUninitialize()

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

    @property
    def document(self) -> HTMLDocument2:
        with ctyped.init_com(ctyped.interface.IDispatch, False) as dispatch:
            self.obj.get_Document(ctyped.byref(dispatch))
            return HTMLDocument2(dispatch)

    left = _CLong('Left')
    top = _CLong('Top')
    width = _CLong('Width')
    height = _CLong('Height')

    def quit(self) -> bool:
        return ctyped.macro.SUCCEEDED(self.obj.Quit())

    visible = _VariantBool('Visible')
    status_bar = _VariantBool('StatusBar')
    status_text = _BSTR('StatusText')
    tool_bar = _CInt('ToolBar')
    menu_bar = _VariantBool('MenuBar')
    full_screen = _VariantBool('FullScreen')

    @property
    def ready_state(self) -> ctyped.enum.READYSTATE:
        ready_state = ctyped.enum.READYSTATE()
        self.obj.get_ReadyState(ctyped.byref(ready_state))
        return ready_state

    offline = _VariantBool('Offline')
    silent = _VariantBool('Silent')
    register_as_browser = _VariantBool('RegisterAsBrowser')
    register_as_drop_target = _VariantBool('RegisterAsDropTarget')
    theater_mode = _VariantBool('TheaterMode')
    address_bar = _VariantBool('AddressBar')
    resizable = _VariantBool('Resizable')


class HTMLDocument2:
    def __init__(self, obj: ctyped.interface.IDispatch):
        self.obj = ctyped.interface.IHTMLDocument2()
        obj.QueryInterface(*ctyped.macro.IID_PPV_ARGS(self.obj))

    def __del__(self):
        if self.obj:
            self.obj.Release()

    @property
    def all(self):
        with ctyped.init_com(ctyped.interface.IHTMLElementCollection, False) as html_element_collection:
            self.obj.get_all(ctyped.byref(html_element_collection))
            return HTMLElementCollection(html_element_collection)

    @property
    def body(self):
        with ctyped.init_com(ctyped.interface.IHTMLElement, False) as html_element:
            self.obj.get_body(ctyped.byref(html_element))
            return HTMLElement(html_element)

    title = _BSTR('title')
    design_mode = _BSTR('designMode')
    url = _BSTR('URL')
    domain = _BSTR('domain')
    cookie = _BSTR('cookie')

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


class HTMLWindow2:
    def __init__(self, obj: ctyped.interface.IHTMLWindow2):
        self.obj = ctyped.interface.IHTMLWindow2()
        obj.QueryInterface(*ctyped.macro.IID_PPV_ARGS(self.obj))

    def __del__(self):
        if self.obj:
            self.obj.Release()

    default_status = _BSTR('defaultStatus')
    status = _BSTR('status')

    def alert(self, message: str) -> bool:
        with _utils.get_bstr(message) as bstr:
            return ctyped.macro.SUCCEEDED(self.obj.alert(bstr))

    def close(self) -> bool:
        return ctyped.macro.SUCCEEDED(self.obj.close())

    name = _BSTR('name')

    def navigate(self, url: str) -> bool:
        with _utils.get_bstr(url) as bstr:
            return ctyped.macro.SUCCEEDED(self.obj.navigate(bstr))

    @property
    def document(self) -> HTMLDocument2:
        with ctyped.init_com(ctyped.interface.IHTMLDocument2, False) as html_document_2:
            self.obj.get_document(ctyped.byref(html_document_2))
            return HTMLDocument2(html_document_2)

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
    def __init__(self, obj: ctyped.interface.IHTMLElement):
        self.obj = ctyped.interface.IHTMLElement()
        obj.QueryInterface(*ctyped.macro.IID_PPV_ARGS(self.obj))

    def __del__(self):
        if self.obj:
            self.obj.Release()

    class_name = _BSTR('className')
    id = _BSTR('id')
    title = _BSTR('title')
    language = _BSTR('language')
    lang = _BSTR('lang')
    inner_html = _BSTR('innerHTML')
    inner_text = _BSTR('innerText')
    outer_html = _BSTR('outerHTML')
    outer_text = _BSTR('outerText')

    def to_string(self) -> str:
        with _utils.get_bstr() as bstr:
            self.obj.toString(ctyped.byref(bstr))
            return ctyped.type.c_wchar_p.from_buffer(bstr).value


class HTMLElementCollection:
    def __init__(self, obj: ctyped.interface.IHTMLElementCollection):
        self.obj = ctyped.interface.IHTMLElementCollection()
        obj.QueryInterface(*ctyped.macro.IID_PPV_ARGS(self.obj))

    def __del__(self):
        if self.obj:
            self.obj.Release()

    length = _CLong('length')
