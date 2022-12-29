from __future__ import annotations as _

from typing import Optional

from libs import ctyped
from libs.ctyped.interface.package import WebView2
from . import _com


class _CoreWebView2WebResourceRequestGetter(_com.Getter):
    def __get__(self, instance: _com.Unknown, owner: type[_com.Unknown]) -> CoreWebView2WebResourceRequest:
        with ctyped.interface.COM[WebView2.ICoreWebView2WebResourceRequest]() as core_webview_2_web_resource_request:
            # noinspection PyProtectedMember
            getattr(instance._obj, self._getter)(ctyped.byref(core_webview_2_web_resource_request))
            return CoreWebView2WebResourceRequest(core_webview_2_web_resource_request)


class _CoreWebView2WebResourceResponseGetter(_com.Getter):
    def __get__(self, instance: _com.Unknown, owner: type[_com.Unknown]) -> CoreWebView2WebResourceResponse:
        with ctyped.interface.COM[WebView2.ICoreWebView2WebResourceResponse]() as core_webview_2_web_resource_response:
            # noinspection PyProtectedMember
            getattr(instance._obj, self._getter)(ctyped.byref(core_webview_2_web_resource_response))
            return CoreWebView2WebResourceResponse(core_webview_2_web_resource_response)


class _CoreWebView2WebResourceResponseSetter(_com.Setter):
    def __set__(self, instance: _com.Unknown, value: CoreWebView2WebResourceResponse):
        # noinspection PyProtectedMember
        getattr(instance._obj, self._setter)(value._obj)


class _CoreWebView2WebResourceResponseGetterSetter(_CoreWebView2WebResourceResponseSetter, _CoreWebView2WebResourceResponseGetter):
    pass


class CoreWebView2WebResourceRequest(_com.Unknown):
    _obj: WebView2.ICoreWebView2WebResourceRequest
    uri = _com.LPWSTRGetterSetter('Uri')
    method = _com.LPWSTRGetterSetter('Method')


class CoreWebView2WebResourceResponse(_com.Unknown):
    _obj: WebView2.ICoreWebView2WebResourceResponse
    status_code = _com.CIntGetterSetter('StatusCode')
    reason_phrase = _com.LPWSTRGetterSetter('ReasonPhrase')


class CoreWebView2WebResourceRequestedEventArgs(_com.Unknown):
    _obj: WebView2.ICoreWebView2WebResourceRequestedEventArgs
    request = _CoreWebView2WebResourceRequestGetter('Request')
    response = _CoreWebView2WebResourceResponseGetterSetter('Response')

    @property
    def resource_context(self) -> ctyped.enum.COREWEBVIEW2_WEB_RESOURCE_CONTEXT:
        corewebview2_web_resource_context = ctyped.enum.COREWEBVIEW2_WEB_RESOURCE_CONTEXT()
        self._obj.get_ResourceContext(ctyped.byref(corewebview2_web_resource_context))
        return corewebview2_web_resource_context


class CoreWebView2Settings(_com.Unknown):
    _obj: WebView2.ICoreWebView2Settings
    is_script_enabled = _com.BOOLGetterSetter('IsScriptEnabled')
    is_web_message_enabled = _com.BOOLGetterSetter('IsWebMessageEnabled')
    are_default_script_dialogs_enabled = _com.BOOLGetterSetter('AreDefaultScriptDialogsEnabled')
    is_status_bar_enabled = _com.BOOLGetterSetter('IsStatusBarEnabled')
    are_dev_tools_enabled = _com.BOOLGetterSetter('AreDevToolsEnabled')
    are_default_context_menus_enabled = _com.BOOLGetterSetter('AreDefaultContextMenusEnabled')
    are_host_objects_allowed = _com.BOOLGetterSetter('AreHostObjectsAllowed')
    is_zoom_control_enabled = _com.BOOLGetterSetter('IsZoomControlEnabled')
    is_built_in_error_page_enabled = _com.BOOLGetterSetter('IsBuiltInErrorPageEnabled')


class CoreWebView2Environment(_com.Unknown):
    _obj: WebView2.ICoreWebView2Environment

    def create_web_resource_response(self, content, status_code: int, reason_phrase: str, headers: str) -> Optional[CoreWebView2WebResourceResponse]:
        core_webview_2_web_resource_response = CoreWebView2WebResourceResponse()
        # noinspection PyProtectedMember
        if ctyped.macro.SUCCEEDED(self._obj.CreateWebResourceResponse(
                content, status_code, reason_phrase, headers, ctyped.byref(core_webview_2_web_resource_response._obj))):
            return core_webview_2_web_resource_response

    browser_version_string = _com.LPWSTRGetter('BrowserVersionString')
