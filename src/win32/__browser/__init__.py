from __future__ import annotations as _

import contextlib
import math
import ntpath
import threading
import time
import uuid
from typing import ContextManager
from typing import Optional

from libs import ctyped
from libs.ctyped.interface.package import WebView2
from libs.ctyped.interface.um import DispEx
from libs.ctyped.interface.um import ExDisp
from libs.ctyped.interface.um import oaidl
from libs.ctyped.interface.um import ocidl
from libs.ctyped.lib import WebView2Loader
from libs.ctyped.lib import oleaut32
from libs.ctyped.lib import shlwapi
from libs.ctyped.lib import user32
from . import _mshtml
from . import _webview2
from .. import _handle
from .. import _utils

DATA_DIR = ntpath.dirname(__file__)


@contextlib.contextmanager
def _temp_var(window: _mshtml.HTMLWindow2, val: str) -> ContextManager[str]:
    var = f'_{uuid.uuid4().hex}'
    window.exec_script(f'{var} = {val};')
    try:
        yield var
    finally:
        window.exec_script(f'delete {var}')


class Browser:
    def __init__(self, url: str = 'about:blank'):
        with ctyped.interface.COM[ExDisp.IWebBrowser2](ctyped.const.CLSID_InternetExplorer) as browser:
            self._browser = _mshtml.WebBrowser2(browser)
        self.navigate(url)

    def __del__(self):
        if self._browser:
            self._browser.quit()
            self._browser = None

    def navigate(self, url: str) -> bool:
        return self._browser.navigate(url)

    def refresh(self) -> bool:
        return self._browser.refresh()

    def stop(self) -> bool:
        return self._browser.stop()

    def is_ready(self) -> bool:
        return self._browser.ready_state == ctyped.enum.READYSTATE.COMPLETE

    def get_url(self) -> str:
        return self._browser.document.url

    def get_body(self) -> str:
        return self._browser.document.body.outer_html

    def get_title(self) -> str:
        return self._browser.document.title

    def get_html(self) -> str:
        return self._browser.document.body.parent_element.outer_html

    def wait(self, timeout: float = math.inf) -> bool:
        end_time = time.monotonic() + timeout
        while end_time > time.monotonic() and not self.is_ready():
            time.sleep(_utils.POLL_INTERVAL)
        return self.is_ready()

    def get_static_html(self) -> Optional[str]:
        html = None
        stream = shlwapi.SHCreateMemStream(ctyped.NULLPTR, 0)
        if stream:
            dispatch = ctyped.interface.COM[oaidl.IDispatch]()
            # noinspection PyProtectedMember
            if ctyped.macro.SUCCEEDED(self._browser._obj.get_Document(~dispatch)):
                with dispatch[ocidl.IPersistStreamInit] as persist_stream:
                    persist_stream.Save(stream, ctyped.const.TRUE)
                stream.Seek(ctyped.union.LARGE_INTEGER(QuadPart=0), ctyped.enum.STREAM_SEEK.SET, ctyped.NULLPTR)
                stat = ctyped.struct.STATSTG()
                stream.Stat(ctyped.byref(stat), ctyped.enum.STATFLAG.NONAME | ctyped.enum.STATFLAG.NOOPEN)
                with ctyped.buffer(stat.cbSize.QuadPart) as buffer:
                    read = ctyped.type.ULONG()
                    stream.Read(buffer, stat.cbSize.QuadPart, ctyped.byref(read))
                    if read == stat.cbSize.QuadPart:
                        html = ctyped.type.c_char_p(buffer).value.decode()
            stream.Release()
        return html

    def call_js(self, func: str, *args: str) -> Optional[bool | int | float | str | oaidl.IDispatch]:  # TODO argtypes
        # noinspection PyProtectedMember
        with (_temp_var(window := self._browser.document.parent_window, func) as var,
              ctyped.interface.COM[DispEx.IDispatchEx](window._obj) as window_ex):
            disp_id = ctyped.type.DISPID()
            with _utils.get_bstr(var) as bstr:
                window_ex.GetDispID(bstr, ctyped.const.fdexNameCaseSensitive, ctyped.byref(disp_id))
            if disp_id:
                params = ctyped.struct.DISPPARAMS(ctyped.array(
                    type=ctyped.struct.VARIANTARG, size=len(args)), cArgs=len(args))
                for index, arg in enumerate(reversed(args)):
                    s = params.rgvarg[index].U.S
                    s.vt = ctyped.enum.VARENUM.BSTR.value
                    s.U.bstrVal = oleaut32.SysAllocString(arg)
                try:
                    result = ctyped.struct.VARIANT()
                    # noinspection PyProtectedMember
                    window._obj.Invoke(disp_id, ctyped.byref(ctyped.struct.IID()), 0, ctyped.const.DISPATCH_METHOD,
                                       ctyped.byref(params), ctyped.byref(result), None, None)
                    try:
                        return _utils.get_variant_value(result)
                    finally:
                        oleaut32.VariantClear(ctyped.byref(result))
                finally:
                    for index in range(len(args)):
                        oleaut32.VariantClear(ctyped.byref(params.rgvarg[index]))

    def _eval_js(self, code: str) -> Optional[bool | int | float | str | oaidl.IDispatch]:
        code = code.replace('"', '\\"')
        with _temp_var(window := self._browser.document.parent_window, f'eval("{code}")') as var:
            disp_id = ctyped.type.DISPID()
            # noinspection PyProtectedMember
            with ctyped.interface.COM[DispEx.IDispatchEx](window._obj) as window_ex, _utils.get_bstr(var) as bstr:
                window_ex.GetDispID(bstr, ctyped.const.fdexNameCaseSensitive, ctyped.byref(disp_id))
            result = ctyped.struct.VARIANT()
            # noinspection PyProtectedMember
            window._obj.Invoke(disp_id, ctyped.byref(
                ctyped.struct.IID()), ctyped.const.LOCALE_SYSTEM_DEFAULT, ctyped.const.DISPATCH_PROPERTYGET,
                               ctyped.byref(ctyped.struct.DISPPARAMS()), ctyped.byref(result), None, None)
            try:
                return _utils.get_variant_value(result)
            finally:
                oleaut32.VariantClear(ctyped.byref(result))

    def eval_js(self, code: str) -> Optional[bool | int | float | str | oaidl.IDispatch]:
        return self.call_js('eval', code)


def _create_environment(timeout: Optional[float] = None) -> _webview2.CoreWebView2Environment:
    environment = _webview2.CoreWebView2Environment()
    event = threading.Event()

    def on_completed(hr: ctyped.type.HRESULT, env: WebView2.ICoreWebView2Environment) -> ctyped.type.HRESULT:
        if ctyped.macro.SUCCEEDED(hr):
            environment.__init__(env)
        event.set()
        return hr

    with ctyped.interface.create_handler(
            on_completed, WebView2.ICoreWebView2CreateCoreWebView2EnvironmentCompletedHandler) as handler:
        if ctyped.macro.SUCCEEDED(WebView2Loader.CreateCoreWebView2EnvironmentWithOptions(
                ctyped.NULLPTR, DATA_DIR, ctyped.NULLPTR, handler)):
            event.wait(timeout)
    return environment


class _BrowserEx:  # TODO
    def __init__(self):
        self._class = ctyped.struct.WNDCLASSEXW(
            style=ctyped.const.CS_HREDRAW | ctyped.const.CS_VREDRAW,
            lpfnWndProc=ctyped.type.WNDPROC(self._wnd_proc), hInstance=_utils.HINSTANCE,
            hCursor=_handle.HCURSOR.from_idc(ctyped.const.IDC_ARROW),
            lpszClassName=f'{__name__}-{type(self).__name__}')
        self._environment = _create_environment()
        if not self._environment or not user32.RegisterClassExW(ctyped.byref(self._class)):
            raise RuntimeError(f'Cannot initialize {type(self).__name__!r}')
        self._hwnd = _handle.HWND(user32.CreateWindowExW(
            0, self._class.lpszClassName, type(self).__name__, ctyped.const.WS_OVERLAPPEDWINDOW,
            ctyped.const.CW_USEDEFAULT, ctyped.const.CW_USEDEFAULT, ctyped.const.CW_USEDEFAULT,
            ctyped.const.CW_USEDEFAULT, None, None, _utils.HINSTANCE, None))
        self._controller: Optional[_webview2.CoreWebView2Controller] = None
        with ctyped.interface.create_handler(
                self._controller_created, WebView2.ICoreWebView2CreateCoreWebView2ControllerCompletedHandler) as handler:
            self._environment.create_core_web_view_2_controller(self._hwnd, handler)

    def _controller_created(self, hr: ctyped.type.HRESULT,
                            ctrl: WebView2.ICoreWebView2Controller) -> ctyped.type.HRESULT:
        if ctyped.macro.SUCCEEDED(hr):
            self._controller = _webview2.CoreWebView2Controller(ctrl)
        return hr

    def destroy(self):
        if self._controller:
            self._controller.close()
        self._hwnd = None
        user32.UnregisterClassW(self._class.lpszClassName, _utils.HINSTANCE)

    def _wnd_proc(self, hwnd: ctyped.type.HWND, message: ctyped.type.UINT,
                  wparam: ctyped.type.WPARAM, lparam: ctyped.type.LPARAM) -> ctyped.type.LRESULT:
        if message == ctyped.const.WM_SIZE:
            if self._controller:
                bounds = ctyped.struct.RECT()
                user32.GetClientRect(hwnd, ctyped.byref(bounds))
                self._controller.bounds = bounds
        if message == ctyped.const.WM_DESTROY:
            user32.PostQuitMessage(0)
        else:
            return user32.DefWindowProcW(hwnd, message, wparam, lparam)
        return 0

    def _mainloop(self) -> int:
        msg = ctyped.struct.MSG()
        msg_ref = ctyped.byref(msg)
        while user32.GetMessageW(msg_ref, self._hwnd, 0, 0):
            user32.TranslateMessage(msg_ref)
            user32.DispatchMessageW(msg_ref)
        return msg.wParam

    def navigate(self, url: str) -> bool:
        return self._controller and self._controller.core_web_view_2.navigate(url)


ctyped.interface.init_com(False)
ctyped.lib.add_path(ntpath.join(ntpath.dirname(__file__)))
