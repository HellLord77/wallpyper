import contextlib
import math
import time
import uuid
from typing import Optional, ContextManager

import libs.ctyped as ctyped
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
        self._browser = _mshtml.WebBrowser2()
        self.stop = self._browser.stop
        self.refresh = self._browser.refresh
        self.navigate = self._browser.navigate
        if url is not None:
            self._browser.navigate(url)
            if wait:
                self.wait()

    def __del__(self):
        if self._browser:
            self._browser.quit()

    def _show(self):
        self._browser.visible = True

    def is_ready(self) -> bool:
        return self._browser.ready_state == ctyped.enum.READYSTATE.COMPLETE

    def get_url(self) -> str:
        return self._browser.document.url

    def get_title(self) -> str:
        return self._browser.document.title

    def wait(self, timeout: float = math.inf) -> bool:
        end_time = time.time() + timeout
        while end_time > time.time() and not self.is_ready():
            time.sleep(_utils.POLL_INTERVAL)
        return self.is_ready()

    def get_html(self) -> Optional[str]:
        # noinspection PyTypeChecker
        stream = ctyped.lib.shlwapi.SHCreateMemStream(None, 0)
        with ctyped.init_com(ctyped.interface.IDispatch, False) as dispatch:
            self._browser.obj.get_Document(ctyped.byref(dispatch))
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
                return ctyped.type.c_char_p(buffer).value.decode()
        stream.Release()

    def call_js(self, func: str, *args: str) -> Optional[bool | int | float | str | ctyped.interface.IDispatch]:  # TODO argtypes
        with _temp_var(window := self._browser.document.parent_window, func) as var, ctyped.cast_com(
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
        with _temp_var(window := self._browser.document.parent_window, f'eval("{source}")') as var:
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
