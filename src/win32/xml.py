import contextlib
from typing import ContextManager, Optional

import libs.ctyped as ctyped
from . import _utils


@contextlib.contextmanager
def load(path: str) -> ContextManager[Optional[ctyped.interface.Windows.Data.Xml.Dom.IXmlDocument]]:
    with _utils.open_file(path) as file:
        if file:
            with ctyped.get_winrt(ctyped.interface.Windows.Data.Xml.Dom.IXmlDocumentStatics) as statics:
                if statics:
                    operation = ctyped.Async(ctyped.interface.IAsyncOperation)
                    if ctyped.macro.SUCCEEDED(statics.LoadFromFileAsync(file, operation.get_ref())) and (
                            doc := operation.get(ctyped.interface.Windows.Data.Xml.Dom.IXmlDocument)):
                        yield doc
                        return
    yield


@contextlib.contextmanager
def loads(xml: str) -> ContextManager[Optional[ctyped.interface.Windows.Data.Xml.Dom.IXmlDocument]]:
    with ctyped.get_winrt(ctyped.interface.Windows.Data.Xml.Dom.IXmlDocument, True) as doc:
        if doc:
            with ctyped.cast_com(doc, ctyped.interface.Windows.Data.Xml.Dom.IXmlDocumentIO) as io:
                if ctyped.macro.SUCCEEDED(io.LoadXml(ctyped.handle.HSTRING.from_string(xml))):
                    yield doc
                    return
    yield


def dump(xml: ctyped.interface.Windows.Data.Xml.Dom.IXmlDocument, path: str) -> bool:
    open(path, 'w').close()
    with _utils.open_file(path) as file:
        if file:
            with ctyped.cast_com(xml, ctyped.interface.Windows.Data.Xml.Dom.IXmlDocumentIO) as io:
                if io:
                    action = ctyped.Async()
                    if ctyped.macro.SUCCEEDED(io.SaveToFileAsync(file, action.get_ref())):
                        return ctyped.enum.AsyncStatus.Completed == action.wait_for()
    return False


def dumps(xml: ctyped.interface.Windows.Data.Xml.Dom.IXmlDocument) -> Optional[str]:
    with ctyped.cast_com(xml, ctyped.interface.Windows.Data.Xml.Dom.IXmlNodeSerializer) as serializer:
        if serializer:
            hstring = ctyped.handle.HSTRING()
            if ctyped.macro.SUCCEEDED(serializer.GetXml(ctyped.byref(hstring))):
                return hstring.get_string()
