from __future__ import annotations as _

from typing import Optional

from libs import ctyped
from libs.ctyped.interface.package import WebView2
from .. import _com


class _CoreWebView2Getter(_com.Getter):
    def __get__(self, instance: _com.Unknown, owner: type[_com.Unknown]) -> CoreWebView2:
        with ctyped.interface.COM[WebView2.ICoreWebView2]() as obj:
            # noinspection PyProtectedMember
            getattr(instance._obj, self._getter)(ctyped.byref(obj))
            return CoreWebView2(obj)


class _CoreWebView2WebResourceRequestGetter(_com.Getter):
    def __get__(self, instance: _com.Unknown, owner: type[_com.Unknown]) -> CoreWebView2WebResourceRequest:
        with ctyped.interface.COM[WebView2.ICoreWebView2WebResourceRequest]() as obj:
            # noinspection PyProtectedMember
            getattr(instance._obj, self._getter)(ctyped.byref(obj))
            return CoreWebView2WebResourceRequest(obj)


class _CoreWebView2WebResourceResponseGetter(_com.Getter):
    def __get__(self, instance: _com.Unknown, owner: type[_com.Unknown]) -> CoreWebView2WebResourceResponse:
        with ctyped.interface.COM[WebView2.ICoreWebView2WebResourceResponse]() as obj:
            # noinspection PyProtectedMember
            getattr(instance._obj, self._getter)(ctyped.byref(obj))
            return CoreWebView2WebResourceResponse(obj)


class _CoreWebView2WebResourceResponseSetter(_com.Setter):
    def __set__(self, instance: _com.Unknown, value: CoreWebView2WebResourceResponse):
        # noinspection PyProtectedMember
        getattr(instance._obj, self._setter)(value._obj)


class _CoreWebView2WebResourceResponseGetterSetter(_CoreWebView2WebResourceResponseSetter, _CoreWebView2WebResourceResponseGetter):
    pass


class CoreWebView2(_com.Unknown):
    _obj: WebView2.ICoreWebView2

    def navigate(self, uri: str) -> bool:
        return ctyped.macro.SUCCEEDED(self._obj.Navigate(uri))

    def navigate_to_string(self, html_content: str) -> bool:
        return ctyped.macro.SUCCEEDED(self._obj.NavigateToString(html_content))

    def reload(self) -> bool:
        return ctyped.macro.SUCCEEDED(self._obj.Reload())

    def post_web_message_as_json(self, web_message_as_json: str) -> bool:
        return ctyped.macro.SUCCEEDED(self._obj.PostWebMessageAsJson(web_message_as_json))

    def post_web_message_as_string(self, web_message_as_string: str) -> bool:
        return ctyped.macro.SUCCEEDED(self._obj.PostWebMessageAsString(web_message_as_string))

    browser_process_id = _com.UINT32Getter('BrowserProcessId')
    can_go_back = _com.BOOLGetter('CanGoBack')
    can_go_forward = _com.BOOLGetter('CanGoForward')

    def go_back(self) -> bool:
        return ctyped.macro.SUCCEEDED(self._obj.GoBack())

    def go_forward(self) -> bool:
        return ctyped.macro.SUCCEEDED(self._obj.GoForward())

    def stop(self) -> bool:
        return ctyped.macro.SUCCEEDED(self._obj.Stop())

    document_title = _com.LPWSTRGetter('DocumentTitle')


class CoreWebView23(_com.Unknown):
    _obj = WebView2.ICoreWebView2_3

    def resume(self) -> bool:
        return ctyped.macro.SUCCEEDED(self._obj.Resume())

    is_suspended = _com.BOOLGetter('IsSuspended')


class CoreWebView26(_com.Unknown):
    _obj: WebView2.ICoreWebView2_6

    def open_task_manager_window(self) -> bool:
        return ctyped.macro.SUCCEEDED(self._obj.OpenTaskManagerWindow())


class CoreWebView28(_com.Unknown):
    _obj: WebView2.ICoreWebView2_8

    is_muted = _com.BOOLGetterSetter('IsMuted')
    is_document_playing_audio = _com.BOOLGetter('IsDocumentPlayingAudio')


class CoreWebView29(_com.Unknown):
    _obj: WebView2.ICoreWebView2_9

    is_default_download_dialog_open = _com.BOOLGetter('IsDefaultDownloadDialogOpen')

    def open_default_download_dialog(self) -> bool:
        return ctyped.macro.SUCCEEDED(self._obj.OpenDefaultDownloadDialog())

    def close_default_download_dialog(self) -> bool:
        return ctyped.macro.SUCCEEDED(self._obj.CloseDefaultDownloadDialog())


class CoreWebView212(_com.Unknown):
    _obj: WebView2.ICoreWebView2_12

    status_bar_text = _com.LPWSTRGetter('StatusBarText')


class CoreWebView2Controller(_com.Unknown):
    _obj: WebView2.ICoreWebView2Controller

    is_visible = _com.BOOLGetterSetter('IsVisible')
    bounds = _com.RECTGetterSetter('Bounds')
    zoom_factor = _com.CDoubleGetterSetter('ZoomFactor')

    def set_bounds_and_zoom_factor(self, bounds: ctyped.struct.RECT, zoom_factor: float) -> bool:
        return ctyped.macro.SUCCEEDED(self._obj.SetBoundsAndZoomFactor(bounds, zoom_factor))

    def move_focus(self, reason: ctyped.enum.COREWEBVIEW2_MOVE_FOCUS_REASON) -> bool:
        return ctyped.macro.SUCCEEDED(self._obj.MoveFocus(reason))

    parent_window = _com.HWNDGetterSetter('ParentWindow')

    def close(self) -> bool:
        return ctyped.macro.SUCCEEDED(self._obj.Close())

    core_web_view_2 = _CoreWebView2Getter('CoreWebView2')


class CoreWebView2Environment(_com.Unknown):
    _obj: WebView2.ICoreWebView2Environment

    def create_core_web_view_2_controller(self, parent_window: ctyped.type.HWND,
                                          handler: WebView2.ICoreWebView2CreateCoreWebView2ControllerCompletedHandler) -> bool:
        return ctyped.macro.SUCCEEDED(self._obj.CreateCoreWebView2Controller(parent_window, handler))

    def create_web_resource_response(self, content, status_code: int, reason_phrase: str,
                                     headers: str) -> Optional[CoreWebView2WebResourceResponse]:
        core_web_view_2_web_resource_response = CoreWebView2WebResourceResponse()
        # noinspection PyProtectedMember
        if ctyped.macro.SUCCEEDED(self._obj.CreateWebResourceResponse(
                content, status_code, reason_phrase, headers, ctyped.byref(
                    core_web_view_2_web_resource_response._obj))):
            return core_web_view_2_web_resource_response

    browser_version_string = _com.LPWSTRGetter('BrowserVersionString')


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
