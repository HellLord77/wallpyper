from __future__ import annotations

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from . import oaidl as _oaidl
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class IXMLDOMImplementation(_oaidl.IDispatch):
    hasFeature: _Callable[[_type.BSTR,  # feature
                           _type.BSTR,  # version
                           _Pointer[_type.VARIANT_BOOL]],  # hasFeature
                          _type.HRESULT]


class IXMLDOMNode(_oaidl.IDispatch):
    get_nodeName: _Callable[[_Pointer[_type.BSTR]],  # name
                            _type.HRESULT]
    get_nodeValue: _Callable[[_Pointer[_struct.VARIANT]],  # value
                             _type.HRESULT]
    put_nodeValue: _Callable[[_struct.VARIANT],  # value
                             _type.HRESULT]
    get_nodeType: _Callable[[_Pointer[_enum.DOMNodeType]],  # type
                            _type.HRESULT]
    get_parentNode: _Callable[[_Pointer[IXMLDOMNode]],  # parent
                              _type.HRESULT]
    get_childNodes: _Callable[[_Pointer[IXMLDOMNodeList]],  # childList
                              _type.HRESULT]
    get_firstChild: _Callable[[_Pointer[IXMLDOMNode]],  # firstChild
                              _type.HRESULT]
    get_lastChild: _Callable[[_Pointer[IXMLDOMNode]],  # lastChild
                             _type.HRESULT]
    get_previousSibling: _Callable[[_Pointer[IXMLDOMNode]],  # previousSibling
                                   _type.HRESULT]
    get_nextSibling: _Callable[[_Pointer[IXMLDOMNode]],  # nextSibling
                               _type.HRESULT]
    get_attributes: _Callable[[_Pointer[IXMLDOMNamedNodeMap]],  # attributeMap
                              _type.HRESULT]
    insertBefore: _Callable[[IXMLDOMNode,  # newChild
                             _struct.VARIANT,  # refChild
                             _Pointer[IXMLDOMNode]],  # outNewChild
                            _type.HRESULT]
    replaceChild: _Callable[[IXMLDOMNode,  # newChild
                             IXMLDOMNode,  # oldChild
                             _Pointer[IXMLDOMNode]],  # outOldChild
                            _type.HRESULT]
    removeChild: _Callable[[IXMLDOMNode,  # childNode
                            _Pointer[IXMLDOMNode]],  # oldChild
                           _type.HRESULT]
    appendChild: _Callable[[IXMLDOMNode,  # newChild
                            _Pointer[IXMLDOMNode]],  # outNewChild
                           _type.HRESULT]
    hasChildNodes: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # hasChild
                             _type.HRESULT]
    get_ownerDocument: _Callable[[_Pointer[IXMLDOMDocument]],  # XMLDOMDocument
                                 _type.HRESULT]
    cloneNode: _Callable[[_type.VARIANT_BOOL,  # deep
                          _Pointer[IXMLDOMNode]],  # cloneRoot
                         _type.HRESULT]
    get_nodeTypeString: _Callable[[_Pointer[_type.BSTR]],  # nodeType
                                  _type.HRESULT]
    get_text: _Callable[[_Pointer[_type.BSTR]],  # text
                        _type.HRESULT]
    put_text: _Callable[[_type.BSTR],  # text
                        _type.HRESULT]
    get_specified: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # isSpecified
                             _type.HRESULT]
    get_definition: _Callable[[_Pointer[IXMLDOMNode]],  # definitionNode
                              _type.HRESULT]
    get_nodeTypedValue: _Callable[[_Pointer[_struct.VARIANT]],  # typedValue
                                  _type.HRESULT]
    put_nodeTypedValue: _Callable[[_struct.VARIANT],  # typedValue
                                  _type.HRESULT]
    get_dataType: _Callable[[_Pointer[_struct.VARIANT]],  # dataTypeName
                            _type.HRESULT]
    put_dataType: _Callable[[_type.BSTR],  # dataTypeName
                            _type.HRESULT]
    get_xml: _Callable[[_Pointer[_type.BSTR]],  # xmlString
                       _type.HRESULT]
    transformNode: _Callable[[IXMLDOMNode,  # stylesheet
                              _Pointer[_type.BSTR]],  # xmlString
                             _type.HRESULT]
    selectNodes: _Callable[[_type.BSTR,  # queryString
                            _Pointer[IXMLDOMNodeList]],  # resultList
                           _type.HRESULT]
    selectSingleNode: _Callable[[_type.BSTR,  # queryString
                                 _Pointer[IXMLDOMNode]],  # resultNode
                                _type.HRESULT]
    get_parsed: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # isParsed
                          _type.HRESULT]
    get_namespaceURI: _Callable[[_Pointer[_type.BSTR]],  # namespaceURI
                                _type.HRESULT]
    get_prefix: _Callable[[_Pointer[_type.BSTR]],  # prefixString
                          _type.HRESULT]
    get_baseName: _Callable[[_Pointer[_type.BSTR]],  # nameString
                            _type.HRESULT]
    transformNodeToObject: _Callable[[IXMLDOMNode,  # stylesheet
                                      _struct.VARIANT],  # outputObject
                                     _type.HRESULT]


class IXMLDOMDocumentFragment(IXMLDOMNode):
    pass


class IXMLDOMDocument(IXMLDOMNode):
    get_doctype: _Callable[[_Pointer[IXMLDOMDocumentType]],  # documentType
                           _type.HRESULT]
    get_implementation: _Callable[[_Pointer[IXMLDOMImplementation]],  # impl
                                  _type.HRESULT]
    get_documentElement: _Callable[[_Pointer[IXMLDOMElement]],  # DOMElement
                                   _type.HRESULT]
    putref_documentElement: _Callable[[IXMLDOMElement],  # DOMElement
                                      _type.HRESULT]
    createElement: _Callable[[_type.BSTR,  # tagName
                              _Pointer[IXMLDOMElement]],  # element
                             _type.HRESULT]
    createDocumentFragment: _Callable[[_Pointer[IXMLDOMDocumentFragment]],  # docFrag
                                      _type.HRESULT]
    createTextNode: _Callable[[_type.BSTR,  # data
                               _Pointer[IXMLDOMText]],  # text
                              _type.HRESULT]
    createComment: _Callable[[_type.BSTR,  # data
                              _Pointer[IXMLDOMComment]],  # comment
                             _type.HRESULT]
    createCDATASection: _Callable[[_type.BSTR,  # data
                                   _Pointer[IXMLDOMCDATASection]],  # cdata
                                  _type.HRESULT]
    createProcessingInstruction: _Callable[[_type.BSTR,  # target
                                            _type.BSTR,  # data
                                            _Pointer[IXMLDOMProcessingInstruction]],  # pi
                                           _type.HRESULT]
    createAttribute: _Callable[[_type.BSTR,  # name
                                _Pointer[IXMLDOMAttribute]],  # attribute
                               _type.HRESULT]
    createEntityReference: _Callable[[_type.BSTR,  # name
                                      _Pointer[IXMLDOMEntityReference]],  # entityRef
                                     _type.HRESULT]
    getElementsByTagName: _Callable[[_type.BSTR,  # tagName
                                     _Pointer[IXMLDOMNodeList]],  # resultList
                                    _type.HRESULT]
    createNode: _Callable[[_struct.VARIANT,  # Type
                           _type.BSTR,  # name
                           _type.BSTR,  # namespaceURI
                           _Pointer[IXMLDOMNode]],  # node
                          _type.HRESULT]
    nodeFromID: _Callable[[_type.BSTR,  # idString
                           _Pointer[IXMLDOMNode]],  # node
                          _type.HRESULT]
    load: _Callable[[_struct.VARIANT,  # xmlSource
                     _Pointer[_type.VARIANT_BOOL]],  # isSuccessful
                    _type.HRESULT]
    get_readyState: _Callable[[_Pointer[_type.c_long]],  # value
                              _type.HRESULT]
    get_parseError: _Callable[[_Pointer[IXMLDOMParseError]],  # errorObj
                              _type.HRESULT]
    get_url: _Callable[[_Pointer[_type.BSTR]],  # urlString
                       _type.HRESULT]
    get_async: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # isAsync
                         _type.HRESULT]
    put_async: _Callable[[_type.VARIANT_BOOL],  # isAsync
                         _type.HRESULT]
    abort: _Callable[[],
                     _type.HRESULT]
    loadXML: _Callable[[_type.BSTR,  # bstrXML
                        _Pointer[_type.VARIANT_BOOL]],  # isSuccessful
                       _type.HRESULT]
    save: _Callable[[_struct.VARIANT],  # destination
                    _type.HRESULT]
    get_validateOnParse: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # isValidating
                                   _type.HRESULT]
    put_validateOnParse: _Callable[[_type.VARIANT_BOOL],  # isValidating
                                   _type.HRESULT]
    get_resolveExternals: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # isResolving
                                    _type.HRESULT]
    put_resolveExternals: _Callable[[_type.VARIANT_BOOL],  # isResolving
                                    _type.HRESULT]
    get_preserveWhiteSpace: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # isPreserving
                                      _type.HRESULT]
    put_preserveWhiteSpace: _Callable[[_type.VARIANT_BOOL],  # isPreserving
                                      _type.HRESULT]
    put_onreadystatechange: _Callable[[_struct.VARIANT],  # readystatechangeSink
                                      _type.HRESULT]
    put_ondataavailable: _Callable[[_struct.VARIANT],  # ondataavailableSink
                                   _type.HRESULT]
    put_ontransformnode: _Callable[[_struct.VARIANT],  # ontransformnodeSink
                                   _type.HRESULT]


class IXMLDOMNodeList(_oaidl.IDispatch):
    get_item: _Callable[[_type.c_long,  # index
                         _Pointer[IXMLDOMNode]],  # listItem
                        _type.HRESULT]
    get_length: _Callable[[_Pointer[_type.c_long]],  # listLength
                          _type.HRESULT]
    nextNode: _Callable[[_Pointer[IXMLDOMNode]],  # nextItem
                        _type.HRESULT]
    reset: _Callable[[],
                     _type.HRESULT]
    get__newEnum: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # ppUnk
                            _type.HRESULT]


class IXMLDOMNamedNodeMap(_oaidl.IDispatch):
    getNamedItem: _Callable[[_type.BSTR,  # name
                             _Pointer[IXMLDOMNode]],  # namedItem
                            _type.HRESULT]
    setNamedItem: _Callable[[IXMLDOMNode,  # newItem
                             _Pointer[IXMLDOMNode]],  # nameItem
                            _type.HRESULT]
    removeNamedItem: _Callable[[_type.BSTR,  # name
                                _Pointer[IXMLDOMNode]],  # namedItem
                               _type.HRESULT]
    get_item: _Callable[[_type.c_long,  # index
                         _Pointer[IXMLDOMNode]],  # listItem
                        _type.HRESULT]
    get_length: _Callable[[_Pointer[_type.c_long]],  # listLength
                          _type.HRESULT]
    getQualifiedItem: _Callable[[_type.BSTR,  # baseName
                                 _type.BSTR,  # namespaceURI
                                 _Pointer[IXMLDOMNode]],  # qualifiedItem
                                _type.HRESULT]
    removeQualifiedItem: _Callable[[_type.BSTR,  # baseName
                                    _type.BSTR,  # namespaceURI
                                    _Pointer[IXMLDOMNode]],  # qualifiedItem
                                   _type.HRESULT]
    nextNode: _Callable[[_Pointer[IXMLDOMNode]],  # nextItem
                        _type.HRESULT]
    reset: _Callable[[],
                     _type.HRESULT]
    get__newEnum: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # ppUnk
                            _type.HRESULT]


class IXMLDOMCharacterData(IXMLDOMNode):
    get_data: _Callable[[_Pointer[_type.BSTR]],  # data
                        _type.HRESULT]
    put_data: _Callable[[_type.BSTR],  # data
                        _type.HRESULT]
    get_length: _Callable[[_Pointer[_type.c_long]],  # dataLength
                          _type.HRESULT]
    substringData: _Callable[[_type.c_long,  # offset
                              _type.c_long,  # count
                              _Pointer[_type.BSTR]],  # data
                             _type.HRESULT]
    appendData: _Callable[[_type.BSTR],  # data
                          _type.HRESULT]
    insertData: _Callable[[_type.c_long,  # offset
                           _type.BSTR],  # data
                          _type.HRESULT]
    deleteData: _Callable[[_type.c_long,  # offset
                           _type.c_long],  # count
                          _type.HRESULT]
    replaceData: _Callable[[_type.c_long,  # offset
                            _type.c_long,  # count
                            _type.BSTR],  # data
                           _type.HRESULT]


class IXMLDOMAttribute(IXMLDOMNode):
    get_name: _Callable[[_Pointer[_type.BSTR]],  # attributeName
                        _type.HRESULT]
    get_value: _Callable[[_Pointer[_struct.VARIANT]],  # attributeValue
                         _type.HRESULT]
    put_value: _Callable[[_struct.VARIANT],  # attributeValue
                         _type.HRESULT]


class IXMLDOMElement(IXMLDOMNode):
    get_tagName: _Callable[[_Pointer[_type.BSTR]],  # tagName
                           _type.HRESULT]
    getAttribute: _Callable[[_type.BSTR,  # name
                             _Pointer[_struct.VARIANT]],  # value
                            _type.HRESULT]
    setAttribute: _Callable[[_type.BSTR,  # name
                             _struct.VARIANT],  # value
                            _type.HRESULT]
    removeAttribute: _Callable[[_type.BSTR],  # name
                               _type.HRESULT]
    getAttributeNode: _Callable[[_type.BSTR,  # name
                                 _Pointer[IXMLDOMAttribute]],  # attributeNode
                                _type.HRESULT]
    setAttributeNode: _Callable[[IXMLDOMAttribute,  # DOMAttribute
                                 _Pointer[IXMLDOMAttribute]],  # attributeNode
                                _type.HRESULT]
    removeAttributeNode: _Callable[[IXMLDOMAttribute,  # DOMAttribute
                                    _Pointer[IXMLDOMAttribute]],  # attributeNode
                                   _type.HRESULT]
    getElementsByTagName: _Callable[[_type.BSTR,  # tagName
                                     _Pointer[IXMLDOMNodeList]],  # resultList
                                    _type.HRESULT]
    normalize: _Callable[[],
                         _type.HRESULT]


class IXMLDOMText(IXMLDOMCharacterData):
    splitText: _Callable[[_type.c_long,  # offset
                          _Pointer[IXMLDOMText]],  # rightHandTextNode
                         _type.HRESULT]


class IXMLDOMComment(IXMLDOMCharacterData):
    pass


class IXMLDOMProcessingInstruction(IXMLDOMNode):
    get_target: _Callable[[_Pointer[_type.BSTR]],  # name
                          _type.HRESULT]
    get_data: _Callable[[_Pointer[_type.BSTR]],  # value
                        _type.HRESULT]
    put_data: _Callable[[_type.BSTR],  # value
                        _type.HRESULT]


class IXMLDOMCDATASection(IXMLDOMText):
    pass


class IXMLDOMDocumentType(IXMLDOMNode):
    get_name: _Callable[[_Pointer[_type.BSTR]],  # rootName
                        _type.HRESULT]
    get_entities: _Callable[[_Pointer[IXMLDOMNamedNodeMap]],  # entityMap
                            _type.HRESULT]
    get_notations: _Callable[[_Pointer[IXMLDOMNamedNodeMap]],  # notationMap
                             _type.HRESULT]


class IXMLDOMNotation(IXMLDOMNode):
    get_publicId: _Callable[[_Pointer[_struct.VARIANT]],  # publicID
                            _type.HRESULT]
    get_systemId: _Callable[[_Pointer[_struct.VARIANT]],  # systemID
                            _type.HRESULT]


class IXMLDOMEntity(IXMLDOMNode):
    get_publicId: _Callable[[_Pointer[_struct.VARIANT]],  # publicID
                            _type.HRESULT]
    get_systemId: _Callable[[_Pointer[_struct.VARIANT]],  # systemID
                            _type.HRESULT]
    get_notationName: _Callable[[_Pointer[_type.BSTR]],  # name
                                _type.HRESULT]


class IXMLDOMEntityReference(IXMLDOMNode):
    pass


class IXMLDOMParseError(_oaidl.IDispatch):
    get_errorCode: _Callable[[_Pointer[_type.c_long]],  # errorCode
                             _type.HRESULT]
    get_url: _Callable[[_Pointer[_type.BSTR]],  # urlString
                       _type.HRESULT]
    get_reason: _Callable[[_Pointer[_type.BSTR]],  # reasonString
                          _type.HRESULT]
    get_srcText: _Callable[[_Pointer[_type.BSTR]],  # sourceString
                           _type.HRESULT]
    get_line: _Callable[[_Pointer[_type.c_long]],  # lineNumber
                        _type.HRESULT]
    get_linepos: _Callable[[_Pointer[_type.c_long]],  # linePosition
                           _type.HRESULT]
    get_filepos: _Callable[[_Pointer[_type.c_long]],  # filePosition
                           _type.HRESULT]


class IXTLRuntime(IXMLDOMNode):
    uniqueID: _Callable[[IXMLDOMNode,  # pNode
                         _Pointer[_type.c_long]],  # pID
                        _type.HRESULT]
    depth: _Callable[[IXMLDOMNode,  # pNode
                      _Pointer[_type.c_long]],  # pDepth
                     _type.HRESULT]
    childNumber: _Callable[[IXMLDOMNode,  # pNode
                            _Pointer[_type.c_long]],  # pNumber
                           _type.HRESULT]
    ancestorChildNumber: _Callable[[_type.BSTR,  # bstrNodeName
                                    IXMLDOMNode,  # pNode
                                    _Pointer[_type.c_long]],  # pNumber
                                   _type.HRESULT]
    absoluteChildNumber: _Callable[[IXMLDOMNode,  # pNode
                                    _Pointer[_type.c_long]],  # pNumber
                                   _type.HRESULT]
    formatIndex: _Callable[[_type.c_long,  # lIndex
                            _type.BSTR,  # bstrFormat
                            _Pointer[_type.BSTR]],  # pbstrFormattedString
                           _type.HRESULT]
    formatNumber: _Callable[[_type.c_double,  # dblNumber
                             _type.BSTR,  # bstrFormat
                             _Pointer[_type.BSTR]],  # pbstrFormattedString
                            _type.HRESULT]
    formatDate: _Callable[[_struct.VARIANT,  # varDate
                           _type.BSTR,  # bstrFormat
                           _struct.VARIANT,  # varDestLocale
                           _Pointer[_type.BSTR]],  # pbstrFormattedString
                          _type.HRESULT]
    formatTime: _Callable[[_struct.VARIANT,  # varTime
                           _type.BSTR,  # bstrFormat
                           _struct.VARIANT,  # varDestLocale
                           _Pointer[_type.BSTR]],  # pbstrFormattedString
                          _type.HRESULT]


class XMLDOMDocumentEvents(_oaidl.IDispatch):
    pass


class IXMLHttpRequest(_oaidl.IDispatch):
    open: _Callable[[_type.BSTR,  # bstrMethod
                     _type.BSTR,  # bstrUrl
                     _struct.VARIANT,  # varAsync
                     _struct.VARIANT,  # bstrUser
                     _struct.VARIANT],  # bstrPassword
                    _type.HRESULT]
    setRequestHeader: _Callable[[_type.BSTR,  # bstrHeader
                                 _type.BSTR],  # bstrValue
                                _type.HRESULT]
    getResponseHeader: _Callable[[_type.BSTR,  # bstrHeader
                                  _Pointer[_type.BSTR]],  # pbstrValue
                                 _type.HRESULT]
    getAllResponseHeaders: _Callable[[_Pointer[_type.BSTR]],  # pbstrHeaders
                                     _type.HRESULT]
    send: _Callable[[_struct.VARIANT],  # varBody
                    _type.HRESULT]
    abort: _Callable[[],
                     _type.HRESULT]
    get_status: _Callable[[_Pointer[_type.c_long]],  # plStatus
                          _type.HRESULT]
    get_statusText: _Callable[[_Pointer[_type.BSTR]],  # pbstrStatus
                              _type.HRESULT]
    get_responseXML: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppBody
                               _type.HRESULT]
    get_responseText: _Callable[[_Pointer[_type.BSTR]],  # pbstrBody
                                _type.HRESULT]
    get_responseBody: _Callable[[_Pointer[_struct.VARIANT]],  # pvarBody
                                _type.HRESULT]
    get_responseStream: _Callable[[_Pointer[_struct.VARIANT]],  # pvarBody
                                  _type.HRESULT]
    get_readyState: _Callable[[_Pointer[_type.c_long]],  # plState
                              _type.HRESULT]
    put_onreadystatechange: _Callable[[_oaidl.IDispatch],  # pReadyStateSink
                                      _type.HRESULT]


class IXMLDSOControl(_oaidl.IDispatch):
    get_XMLDocument: _Callable[[_Pointer[IXMLDOMDocument]],  # ppDoc
                               _type.HRESULT]
    put_XMLDocument: _Callable[[IXMLDOMDocument],  # ppDoc
                               _type.HRESULT]
    get_JavaDSOCompatible: _Callable[[_Pointer[_type.BOOL]],  # fJavaDSOCompatible
                                     _type.HRESULT]
    put_JavaDSOCompatible: _Callable[[_type.BOOL],  # fJavaDSOCompatible
                                     _type.HRESULT]
    get_readyState: _Callable[[_Pointer[_type.c_long]],  # state
                              _type.HRESULT]


class IXMLElementCollection(_oaidl.IDispatch):
    put_length: _Callable[[_type.c_long],  # v
                          _type.HRESULT]
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    get__newEnum: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # ppUnk
                            _type.HRESULT]
    item: _Callable[[_struct.VARIANT,  # var1
                     _struct.VARIANT,  # var2
                     _Pointer[_oaidl.IDispatch]],  # ppDisp
                    _type.HRESULT]


class IXMLDocument(_oaidl.IDispatch):
    get_root: _Callable[[_Pointer[IXMLElement]],  # p
                        _type.HRESULT]
    get_fileSize: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    get_fileModifiedDate: _Callable[[_Pointer[_type.BSTR]],  # p
                                    _type.HRESULT]
    get_fileUpdatedDate: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    get_URL: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    put_URL: _Callable[[_type.BSTR],  # p
                       _type.HRESULT]
    get_mimeType: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    get_readyState: _Callable[[_Pointer[_type.c_long]],  # pl
                              _type.HRESULT]
    get_charset: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_charset: _Callable[[_type.BSTR],  # p
                           _type.HRESULT]
    get_version: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    get_doctype: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    get_dtdURL: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    createElement: _Callable[[_struct.VARIANT,  # vType
                              _struct.VARIANT,  # var1
                              _Pointer[IXMLElement]],  # ppElem
                             _type.HRESULT]


class IXMLDocument2(_oaidl.IDispatch):
    get_root: _Callable[[_Pointer[IXMLElement2]],  # p
                        _type.HRESULT]
    get_fileSize: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    get_fileModifiedDate: _Callable[[_Pointer[_type.BSTR]],  # p
                                    _type.HRESULT]
    get_fileUpdatedDate: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    get_URL: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    put_URL: _Callable[[_type.BSTR],  # p
                       _type.HRESULT]
    get_mimeType: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    get_readyState: _Callable[[_Pointer[_type.c_long]],  # pl
                              _type.HRESULT]
    get_charset: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_charset: _Callable[[_type.BSTR],  # p
                           _type.HRESULT]
    get_version: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    get_doctype: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    get_dtdURL: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    createElement: _Callable[[_struct.VARIANT,  # vType
                              _struct.VARIANT,  # var1
                              _Pointer[IXMLElement2]],  # ppElem
                             _type.HRESULT]
    get_async: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pf
                         _type.HRESULT]
    put_async: _Callable[[_type.VARIANT_BOOL],  # f
                         _type.HRESULT]


class IXMLElement(_oaidl.IDispatch):
    get_tagName: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_tagName: _Callable[[_type.BSTR],  # p
                           _type.HRESULT]
    get_parent: _Callable[[_Pointer[IXMLElement]],  # ppParent
                          _type.HRESULT]
    setAttribute: _Callable[[_type.BSTR,  # strPropertyName
                             _struct.VARIANT],  # PropertyValue
                            _type.HRESULT]
    getAttribute: _Callable[[_type.BSTR,  # strPropertyName
                             _Pointer[_struct.VARIANT]],  # PropertyValue
                            _type.HRESULT]
    removeAttribute: _Callable[[_type.BSTR],  # strPropertyName
                               _type.HRESULT]
    get_children: _Callable[[_Pointer[IXMLElementCollection]],  # pp
                            _type.HRESULT]
    get_type: _Callable[[_Pointer[_type.c_long]],  # plType
                        _type.HRESULT]
    get_text: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_text: _Callable[[_type.BSTR],  # p
                        _type.HRESULT]
    addChild: _Callable[[IXMLElement,  # pChildElem
                         _type.c_long,  # lIndex
                         _type.c_long],  # lReserved
                        _type.HRESULT]
    removeChild: _Callable[[IXMLElement],  # pChildElem
                           _type.HRESULT]


class IXMLElement2(_oaidl.IDispatch):
    get_tagName: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_tagName: _Callable[[_type.BSTR],  # p
                           _type.HRESULT]
    get_parent: _Callable[[_Pointer[IXMLElement2]],  # ppParent
                          _type.HRESULT]
    setAttribute: _Callable[[_type.BSTR,  # strPropertyName
                             _struct.VARIANT],  # PropertyValue
                            _type.HRESULT]
    getAttribute: _Callable[[_type.BSTR,  # strPropertyName
                             _Pointer[_struct.VARIANT]],  # PropertyValue
                            _type.HRESULT]
    removeAttribute: _Callable[[_type.BSTR],  # strPropertyName
                               _type.HRESULT]
    get_children: _Callable[[_Pointer[IXMLElementCollection]],  # pp
                            _type.HRESULT]
    get_type: _Callable[[_Pointer[_type.c_long]],  # plType
                        _type.HRESULT]
    get_text: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_text: _Callable[[_type.BSTR],  # p
                        _type.HRESULT]
    addChild: _Callable[[IXMLElement2,  # pChildElem
                         _type.c_long,  # lIndex
                         _type.c_long],  # lReserved
                        _type.HRESULT]
    removeChild: _Callable[[IXMLElement2],  # pChildElem
                           _type.HRESULT]
    get_attributes: _Callable[[_Pointer[IXMLElementCollection]],  # pp
                              _type.HRESULT]


class IXMLAttribute(_oaidl.IDispatch):
    get_name: _Callable[[_Pointer[_type.BSTR]],  # n
                        _type.HRESULT]
    get_value: _Callable[[_Pointer[_type.BSTR]],  # v
                         _type.HRESULT]


class IXMLError(_Unknwnbase.IUnknown):
    GetErrorInfo: _Callable[[_Pointer[_struct.XML_ERROR]],  # pErrorReturn
                            _type.HRESULT]
