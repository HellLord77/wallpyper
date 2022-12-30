from __future__ import annotations as _

import contextlib
import math
import time
import uuid
from typing import ContextManager, Optional

from libs import ctyped
from libs.ctyped.interface.um import DispEx, ExDisp, oaidl, ocidl
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
    def __init__(self, url: str = 'about:blank'):
        with ctyped.interface.COM[ExDisp.IWebBrowser2](ctyped.const.CLSID_InternetExplorer) as browser:
            self._browser = _mshtml.WebBrowser2(browser)
        self._browser.navigate(url)

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
        end_time = time.time() + timeout
        while end_time > time.time() and not self.is_ready():
            time.sleep(_utils.POLL_INTERVAL)
        return self.is_ready()

    def get_static_html(self) -> Optional[str]:
        html = None
        stream = ctyped.lib.shlwapi.SHCreateMemStream(ctyped.NULLPTR, 0)
        if stream:
            dispatch = ctyped.interface.COM[oaidl.IDispatch]()
            # noinspection PyProtectedMember
            self._browser._obj.get_Document(~dispatch)
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
        with _temp_var(window := self._browser.document.parent_window, func) as var, \
                ctyped.interface.COM[DispEx.IDispatchEx](window._obj) as window_ex:
            disp_id = ctyped.type.DISPID()
            with _utils.get_bstr(var) as bstr:
                window_ex.GetDispID(bstr, ctyped.const.fdexNameCaseSensitive, ctyped.byref(disp_id))
            if disp_id:
                params = ctyped.struct.DISPPARAMS(ctyped.array(
                    type=ctyped.struct.VARIANTARG, size=len(args)), cArgs=len(args))
                for index, arg in enumerate(reversed(args)):
                    s = params.rgvarg[index].U.S
                    s.vt = ctyped.enum.VARENUM.BSTR.value
                    s.U.bstrVal = ctyped.lib.oleaut32.SysAllocString(arg)
                try:
                    result = ctyped.struct.VARIANT()
                    # noinspection PyProtectedMember
                    window._obj.Invoke(disp_id, ctyped.byref(ctyped.struct.IID()), 0, ctyped.const.DISPATCH_METHOD,
                                       ctyped.byref(params), ctyped.byref(result), None, None)
                    try:
                        return _utils.get_variant_value(result)
                    finally:
                        ctyped.lib.oleaut32.VariantClear(ctyped.byref(result))
                finally:
                    for index in range(len(args)):
                        ctyped.lib.oleaut32.VariantClear(ctyped.byref(params.rgvarg[index]))

    def _eval_js(self, code: str) -> Optional[bool | int | float | str | oaidl.IDispatch]:
        source = code.replace('"', '\\"')
        with _temp_var(window := self._browser.document.parent_window, f'eval("{source}")') as var:
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
                ctyped.lib.oleaut32.VariantClear(ctyped.byref(result))

    def eval_js(self, code: str) -> Optional[bool | int | float | str | oaidl.IDispatch]:
        return self.call_js('eval', code)
