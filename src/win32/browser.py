import contextlib
import math
import time
import uuid
from typing import Optional, ContextManager

from libs import ctyped
from . import _mshtml, _utils


@contextlib.contextmanager
def _temp_var(window: _mshtml.HTMLWindow2, val: str) -> ContextManager[str]:
    var = f'_{uuid.uuid4().hex}'
    window.exec_script(f'{var} = {val};')
    try:
        yield var
    finally:
        window.exec_script(f'delete {var}')


class Browser:
    def __init__(self, url: Optional[str] = None, wait: bool = False):
        ctyped.lib.Ole32.CoInitialize(None)
        self._browser_mrsl = ctyped.interface.IStream()
        with ctyped.init_com(ctyped.interface.IWebBrowser2) as browser:
            ctyped.lib.Ole32.CoMarshalInterThreadInterfaceInStream(ctyped.macro.IID_PPV_ARGS(
                browser)[0], browser, ctyped.byref(self._browser_mrsl))
            if url is not None:
                _mshtml.WebBrowser2(browser).navigate(url)
                if wait:
                    self.wait()

    def __del__(self):
        if self._browser_mrsl:
            with ctyped.init_com(ctyped.interface.IWebBrowser2, False) as browser:
                ctyped.lib.Ole32.CoGetInterfaceAndReleaseStream(self._browser_mrsl, *ctyped.macro.IID_PPV_ARGS(browser))
                browser.Quit()
        ctyped.lib.Ole32.CoUninitialize()

    @property
    @contextlib.contextmanager
    def _browser(self) -> ContextManager[_mshtml.WebBrowser2]:
        with ctyped.init_com(ctyped.interface.IWebBrowser2, False) as browser:
            ctyped.lib.Ole32.CoUnmarshalInterface(self._browser_mrsl, *ctyped.macro.IID_PPV_ARGS(browser))
            yield _mshtml.WebBrowser2(browser)

    def navigate(self, url: str) -> bool:
        with self._browser as browser:
            return browser.navigate(url)

    def refresh(self) -> bool:
        with self._browser as browser:
            return browser.refresh()

    def stop(self) -> bool:
        with self._browser as browser:
            return browser.stop()

    def is_ready(self) -> bool:
        with self._browser as browser:
            return browser.ready_state == ctyped.enum.READYSTATE.COMPLETE

    def get_url(self) -> str:
        with self._browser as browser:
            return browser.document.url

    def get_body(self) -> str:
        with self._browser as browser:
            return browser.document.body.outer_html

    def get_title(self) -> str:
        with self._browser as browser:
            return browser.document.title

    def get_html(self) -> str:
        with self._browser as browser:
            return browser.document.body.parent_element.outer_html

    def wait(self, timeout: float = math.inf) -> bool:
        end_time = time.time() + timeout
        while end_time > time.time() and not self.is_ready():
            time.sleep(_utils.POLL_INTERVAL)
        return self.is_ready()

    def get_static_html(self) -> Optional[str]:
        html = None
        # noinspection PyTypeChecker
        stream = ctyped.lib.shlwapi.SHCreateMemStream(None, 0)
        if stream:
            with ctyped.init_com(ctyped.interface.IDispatch, False) as dispatch:
                with self._browser as browser:
                    browser.obj.get_Document(ctyped.byref(dispatch))
                with ctyped.cast_com(dispatch, ctyped.interface.IPersistStreamInit) as persist_stream:
                    persist_stream.Save(stream, ctyped.const.TRUE)
            # noinspection PyTypeChecker
            stream.Seek(ctyped.union.LARGE_INTEGER(QuadPart=0), ctyped.enum.STREAM_SEEK.SET, None)
            stat = ctyped.struct.STATSTG()
            stream.Stat(ctyped.byref(stat), ctyped.enum.STATFLAG.NONAME | ctyped.enum.STATFLAG.NOOPEN)
            with ctyped.buffer(stat.cbSize.QuadPart) as buffer:
                read = ctyped.type.ULONG()
                stream.Read(buffer, stat.cbSize.QuadPart, ctyped.byref(read))
                if read == stat.cbSize.QuadPart:
                    html = ctyped.type.c_char_p(buffer).value.decode()
            stream.Release()
        return html

    def call_js(self, func: str, *args: str) -> Optional[bool | int | float | str | ctyped.interface.IDispatch]:  # TODO argtypes
        with self._browser as browser:
            window = browser.document.parent_window
        with _temp_var(window, func) as var, ctyped.cast_com(
                window.obj, ctyped.interface.IDispatchEx) as window_ex:
            disp_id = ctyped.type.DISPID()
            with _utils.get_bstr(var) as bstr:
                window_ex.GetDispID(bstr, ctyped.const.fdexNameCaseSensitive, ctyped.byref(disp_id))
            if disp_id:
                params = ctyped.struct.DISPPARAMS(ctyped.array(
                    type=ctyped.struct.VARIANTARG, size=len(args)), cArgs=len(args))
                for index, arg in enumerate(reversed(args)):
                    s = params.rgvarg[index].U.S
                    s.vt = ctyped.enum.VARENUM.BSTR.value
                    s.U.bstrVal = ctyped.lib.OleAut32.SysAllocString(arg)
                try:
                    result = ctyped.struct.VARIANT()
                    window.obj.Invoke(disp_id, ctyped.byref(ctyped.struct.IID()), 0, ctyped.const.DISPATCH_METHOD,
                                      ctyped.byref(params), ctyped.byref(result), None, None)
                    try:
                        return _utils.get_variant_value(result)
                    finally:
                        ctyped.lib.OleAut32.VariantClear(ctyped.byref(result))
                finally:
                    for index in range(len(args)):
                        ctyped.lib.OleAut32.VariantClear(ctyped.byref(params.rgvarg[index]))

    def _eval_js(self, code: str) -> Optional[bool | int | float | str | ctyped.interface.IDispatch]:
        source = code.replace('"', '\\"')
        with self._browser as browser:
            window = browser.document.parent_window
        with _temp_var(window, f'eval("{source}")') as var:
            disp_id = ctyped.type.DISPID()
            with ctyped.cast_com(window.obj, ctyped.interface.IDispatchEx) as window_ex, _utils.get_bstr(var) as bstr:
                window_ex.GetDispID(bstr, ctyped.const.fdexNameCaseSensitive, ctyped.byref(disp_id))
            result = ctyped.struct.VARIANT()
            window.obj.Invoke(disp_id, ctyped.byref(
                ctyped.struct.IID()), ctyped.const.LOCALE_SYSTEM_DEFAULT, ctyped.const.DISPATCH_PROPERTYGET,
                              ctyped.byref(ctyped.struct.DISPPARAMS()), ctyped.byref(result), None, None)
            try:
                return _utils.get_variant_value(result)
            finally:
                ctyped.lib.OleAut32.VariantClear(ctyped.byref(result))

    def eval_js(self, code: str) -> Optional[bool | int | float | str | ctyped.interface.IDispatch]:
        return self.call_js('eval', code)
