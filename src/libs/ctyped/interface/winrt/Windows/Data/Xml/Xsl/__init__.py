from __future__ import annotations

from typing import Callable as _Callable

from .. import Dom as _Windows_Data_Xml_Dom
from ..... import inspectable as _inspectable
from ....... import type as _type
from ......._utils import _Pointer


class IXsltProcessor(_inspectable.IInspectable):
    TransformToString: _Callable[[_Windows_Data_Xml_Dom.IXmlNode,  # inputNode
                                  _Pointer[_type.HSTRING]],  # output
                                 _type.HRESULT]


class IXsltProcessor2(_inspectable.IInspectable):
    TransformToDocument: _Callable[[_Windows_Data_Xml_Dom.IXmlNode,  # inputNode
                                    _Pointer[_Windows_Data_Xml_Dom.IXmlDocument]],  # output
                                   _type.HRESULT]


class IXsltProcessorFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[_Windows_Data_Xml_Dom.IXmlDocument,  # document
                               _Pointer[IXsltProcessor]],  # xsltProcessor
                              _type.HRESULT]
