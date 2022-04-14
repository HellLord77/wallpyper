import contextlib
from typing import ContextManager, Optional

import libs.ctyped as ctyped
from . import _utils


@contextlib.contextmanager
def load(path: str) -> ContextManager[Optional[ctyped.com.IXmlDocument]]:
    with _utils.open_file(path) as file:
        if file:
            with ctyped.get_winrt(ctyped.com.IXmlDocumentStatics) as statics:
                if statics:
                    operation = ctyped.Async(ctyped.com.IAsyncOperation)
                    if ctyped.macro.SUCCEEDED(statics.LoadFromFileAsync(
                            file, operation.get_ref())) and (doc := operation.get(ctyped.com.IXmlDocument)):
                        yield doc
                        return
    yield


@contextlib.contextmanager
def loads(xml: str) -> ContextManager[Optional[ctyped.com.IXmlDocument]]:
    with ctyped.get_winrt(ctyped.com.IXmlDocument, True) as doc:
        if doc:
            with ctyped.cast_com(doc, ctyped.com.IXmlDocumentIO) as io:
                if ctyped.macro.SUCCEEDED(io.LoadXml(ctyped.handle.HSTRING.from_string(xml))):
                    yield doc
                    return
    yield


def dump(xml: ctyped.com.IXmlDocument, path: str) -> bool:
    open(path, 'w').close()
    with _utils.open_file(path) as file:
        if file:
            with ctyped.cast_com(xml, ctyped.com.IXmlDocumentIO) as io:
                if io:
                    action = ctyped.Async()
                    if ctyped.macro.SUCCEEDED(io.SaveToFileAsync(file, action.get_ref())):
                        return ctyped.enum.AsyncStatus.Completed == action.wait_for()
    return False


def dumps(xml: ctyped.com.IXmlDocument) -> Optional[str]:
    with ctyped.cast_com(xml, ctyped.com.IXmlNodeSerializer) as serializer:
        if serializer:
            hstring = ctyped.handle.HSTRING()
            if ctyped.macro.SUCCEEDED(serializer.GetXml(ctyped.byref(hstring))):
                return hstring.get_string()
