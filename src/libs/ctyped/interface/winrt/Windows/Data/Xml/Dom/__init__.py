from __future__ import annotations as _

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from .... import Storage as _Windows_Storage
from ....Storage import Streams as _Windows_Storage_Streams
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import type as _type
from ......._utils import _Pointer


class IDtdEntity(_inspectable.IInspectable):
    get_PublicId: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                            _type.HRESULT]
    get_SystemId: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                            _type.HRESULT]
    get_NotationName: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                _type.HRESULT]


class IDtdNotation(_inspectable.IInspectable):
    get_PublicId: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                            _type.HRESULT]
    get_SystemId: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                            _type.HRESULT]


class IXmlAttribute(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Specified: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Value: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]


class IXmlCDataSection(_inspectable.IInspectable):
    pass


class IXmlCharacterData(_inspectable.IInspectable):
    get_Data: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Data: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_Length: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    SubstringData: _Callable[[_type.UINT32,  # offset
                              _type.UINT32,  # count
                              _Pointer[_type.HSTRING]],  # data
                             _type.HRESULT]
    AppendData: _Callable[[_type.HSTRING],  # data
                          _type.HRESULT]
    InsertData: _Callable[[_type.UINT32,  # offset
                           _type.HSTRING],  # data
                          _type.HRESULT]
    DeleteData: _Callable[[_type.UINT32,  # offset
                           _type.UINT32],  # count
                          _type.HRESULT]
    ReplaceData: _Callable[[_type.UINT32,  # offset
                            _type.UINT32,  # count
                            _type.HSTRING],  # data
                           _type.HRESULT]


class IXmlComment(_inspectable.IInspectable):
    pass


class IXmlDocument(_inspectable.IInspectable):
    get_Doctype: _Callable[[_Pointer[IXmlDocumentType]],  # value
                           _type.HRESULT]
    get_Implementation: _Callable[[_Pointer[IXmlDomImplementation]],  # value
                                  _type.HRESULT]
    get_DocumentElement: _Callable[[_Pointer[IXmlElement]],  # value
                                   _type.HRESULT]
    CreateElement: _Callable[[_type.HSTRING,  # tagName
                              _Pointer[IXmlElement]],  # newElement
                             _type.HRESULT]
    CreateDocumentFragment: _Callable[[_Pointer[IXmlDocumentFragment]],  # newDocumentFragment
                                      _type.HRESULT]
    CreateTextNode: _Callable[[_type.HSTRING,  # data
                               _Pointer[IXmlText]],  # newTextNode
                              _type.HRESULT]
    CreateComment: _Callable[[_type.HSTRING,  # data
                              _Pointer[IXmlComment]],  # newComment
                             _type.HRESULT]
    CreateProcessingInstruction: _Callable[[_type.HSTRING,  # target
                                            _type.HSTRING,  # data
                                            _Pointer[IXmlProcessingInstruction]],  # newProcessingInstruction
                                           _type.HRESULT]
    CreateAttribute: _Callable[[_type.HSTRING,  # name
                                _Pointer[IXmlAttribute]],  # newAttribute
                               _type.HRESULT]
    CreateEntityReference: _Callable[[_type.HSTRING,  # name
                                      _Pointer[IXmlEntityReference]],  # newEntityReference
                                     _type.HRESULT]
    GetElementsByTagName: _Callable[[_type.HSTRING,  # tagName
                                     _Pointer[IXmlNodeList]],  # elements
                                    _type.HRESULT]
    CreateCDataSection: _Callable[[_type.HSTRING,  # data
                                   _Pointer[IXmlCDataSection]],  # newCDataSection
                                  _type.HRESULT]
    get_DocumentUri: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    CreateAttributeNS: _Callable[[_inspectable.IInspectable,  # namespaceUri
                                  _type.HSTRING,  # qualifiedName
                                  _Pointer[IXmlAttribute]],  # newAttribute
                                 _type.HRESULT]
    CreateElementNS: _Callable[[_inspectable.IInspectable,  # namespaceUri
                                _type.HSTRING,  # qualifiedName
                                _Pointer[IXmlElement]],  # newElement
                               _type.HRESULT]
    GetElementById: _Callable[[_type.HSTRING,  # elementId
                               _Pointer[IXmlElement]],  # element
                              _type.HRESULT]
    ImportNode: _Callable[[IXmlNode,  # node
                           _type.boolean,  # deep
                           _Pointer[IXmlNode]],  # newNode
                          _type.HRESULT]


class IXmlDocumentFragment(_inspectable.IInspectable):
    pass


class IXmlDocumentIO(_inspectable.IInspectable):
    LoadXml: _Callable[[_type.HSTRING],  # xml
                       _type.HRESULT]
    LoadXmlWithSettings: _Callable[[_type.HSTRING,  # xml
                                    IXmlLoadSettings],  # loadSettings
                                   _type.HRESULT]
    SaveToFileAsync: _Callable[[_Windows_Storage.IStorageFile,  # file
                                _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                               _type.HRESULT]


class IXmlDocumentIO2(_inspectable.IInspectable):
    LoadXmlFromBuffer: _Callable[[_Windows_Storage_Streams.IBuffer],  # buffer
                                 _type.HRESULT]
    LoadXmlFromBufferWithSettings: _Callable[[_Windows_Storage_Streams.IBuffer,  # buffer
                                              IXmlLoadSettings],  # loadSettings
                                             _type.HRESULT]


class IXmlDocumentStatics(_inspectable.IInspectable, factory=True):
    LoadFromUriAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                 _Pointer[_Windows_Foundation.IAsyncOperation[IXmlDocument]]],  # asyncInfo
                                _type.HRESULT]
    LoadFromUriWithSettingsAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                             IXmlLoadSettings,  # loadSettings
                                             _Pointer[_Windows_Foundation.IAsyncOperation[IXmlDocument]]],  # asyncInfo
                                            _type.HRESULT]
    LoadFromFileAsync: _Callable[[_Windows_Storage.IStorageFile,  # file
                                  _Pointer[_Windows_Foundation.IAsyncOperation[IXmlDocument]]],  # asyncInfo
                                 _type.HRESULT]
    LoadFromFileWithSettingsAsync: _Callable[[_Windows_Storage.IStorageFile,  # file
                                              IXmlLoadSettings,  # loadSettings
                                              _Pointer[_Windows_Foundation.IAsyncOperation[IXmlDocument]]],  # asyncInfo
                                             _type.HRESULT]


class IXmlDocumentType(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Entities: _Callable[[_Pointer[IXmlNamedNodeMap]],  # value
                            _type.HRESULT]
    get_Notations: _Callable[[_Pointer[IXmlNamedNodeMap]],  # value
                             _type.HRESULT]


class IXmlDomImplementation(_inspectable.IInspectable):
    HasFeature: _Callable[[_type.HSTRING,  # feature
                           _inspectable.IInspectable,  # version
                           _Pointer[_type.boolean]],  # featureSupported
                          _type.HRESULT]


class IXmlElement(_inspectable.IInspectable):
    get_TagName: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    GetAttribute: _Callable[[_type.HSTRING,  # attributeName
                             _Pointer[_type.HSTRING]],  # attributeValue
                            _type.HRESULT]
    SetAttribute: _Callable[[_type.HSTRING,  # attributeName
                             _type.HSTRING],  # attributeValue
                            _type.HRESULT]
    RemoveAttribute: _Callable[[_type.HSTRING],  # attributeName
                               _type.HRESULT]
    GetAttributeNode: _Callable[[_type.HSTRING,  # attributeName
                                 _Pointer[IXmlAttribute]],  # attributeNode
                                _type.HRESULT]
    SetAttributeNode: _Callable[[IXmlAttribute,  # newAttribute
                                 _Pointer[IXmlAttribute]],  # previousAttribute
                                _type.HRESULT]
    RemoveAttributeNode: _Callable[[IXmlAttribute,  # attributeNode
                                    _Pointer[IXmlAttribute]],  # removedAttribute
                                   _type.HRESULT]
    GetElementsByTagName: _Callable[[_type.HSTRING,  # tagName
                                     _Pointer[IXmlNodeList]],  # elements
                                    _type.HRESULT]
    SetAttributeNS: _Callable[[_inspectable.IInspectable,  # namespaceUri
                               _type.HSTRING,  # qualifiedName
                               _type.HSTRING],  # value
                              _type.HRESULT]
    GetAttributeNS: _Callable[[_inspectable.IInspectable,  # namespaceUri
                               _type.HSTRING,  # localName
                               _Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    RemoveAttributeNS: _Callable[[_inspectable.IInspectable,  # namespaceUri
                                  _type.HSTRING],  # localName
                                 _type.HRESULT]
    SetAttributeNodeNS: _Callable[[IXmlAttribute,  # newAttribute
                                   _Pointer[IXmlAttribute]],  # previousAttribute
                                  _type.HRESULT]
    GetAttributeNodeNS: _Callable[[_inspectable.IInspectable,  # namespaceUri
                                   _type.HSTRING,  # localName
                                   _Pointer[IXmlAttribute]],  # previousAttribute
                                  _type.HRESULT]


class IXmlEntityReference(_inspectable.IInspectable):
    pass


class IXmlLoadSettings(_inspectable.IInspectable):
    get_MaxElementDepth: _Callable[[_Pointer[_type.UINT32]],  # value
                                   _type.HRESULT]
    put_MaxElementDepth: _Callable[[_type.UINT32],  # value
                                   _type.HRESULT]
    get_ProhibitDtd: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    put_ProhibitDtd: _Callable[[_type.boolean],  # value
                               _type.HRESULT]
    get_ResolveExternals: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_ResolveExternals: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_ValidateOnParse: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    put_ValidateOnParse: _Callable[[_type.boolean],  # value
                                   _type.HRESULT]
    get_ElementContentWhiteSpace: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_ElementContentWhiteSpace: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]


class IXmlNamedNodeMap(_inspectable.IInspectable):
    get_Length: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    Item: _Callable[[_type.UINT32,  # index
                     _Pointer[IXmlNode]],  # node
                    _type.HRESULT]
    GetNamedItem: _Callable[[_type.HSTRING,  # name
                             _Pointer[IXmlNode]],  # node
                            _type.HRESULT]
    SetNamedItem: _Callable[[IXmlNode,  # node
                             _Pointer[IXmlNode]],  # previousNode
                            _type.HRESULT]
    RemoveNamedItem: _Callable[[_type.HSTRING,  # name
                                _Pointer[IXmlNode]],  # previousNode
                               _type.HRESULT]
    GetNamedItemNS: _Callable[[_inspectable.IInspectable,  # namespaceUri
                               _type.HSTRING,  # name
                               _Pointer[IXmlNode]],  # node
                              _type.HRESULT]
    RemoveNamedItemNS: _Callable[[_inspectable.IInspectable,  # namespaceUri
                                  _type.HSTRING,  # name
                                  _Pointer[IXmlNode]],  # previousNode
                                 _type.HRESULT]
    SetNamedItemNS: _Callable[[IXmlNode,  # node
                               _Pointer[IXmlNode]],  # previousNode
                              _type.HRESULT]


class IXmlNode(_inspectable.IInspectable):
    get_NodeValue: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                             _type.HRESULT]
    put_NodeValue: _Callable[[_inspectable.IInspectable],  # value
                             _type.HRESULT]
    get_NodeType: _Callable[[_Pointer[_enum.Windows.Data.Xml.Dom.NodeType]],  # value
                            _type.HRESULT]
    get_NodeName: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_ParentNode: _Callable[[_Pointer[IXmlNode]],  # value
                              _type.HRESULT]
    get_ChildNodes: _Callable[[_Pointer[IXmlNodeList]],  # value
                              _type.HRESULT]
    get_FirstChild: _Callable[[_Pointer[IXmlNode]],  # value
                              _type.HRESULT]
    get_LastChild: _Callable[[_Pointer[IXmlNode]],  # value
                             _type.HRESULT]
    get_PreviousSibling: _Callable[[_Pointer[IXmlNode]],  # value
                                   _type.HRESULT]
    get_NextSibling: _Callable[[_Pointer[IXmlNode]],  # value
                               _type.HRESULT]
    get_Attributes: _Callable[[_Pointer[IXmlNamedNodeMap]],  # value
                              _type.HRESULT]
    HasChildNodes: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_OwnerDocument: _Callable[[_Pointer[IXmlDocument]],  # value
                                 _type.HRESULT]
    InsertBefore: _Callable[[IXmlNode,  # newChild
                             IXmlNode,  # referenceChild
                             _Pointer[IXmlNode]],  # insertedChild
                            _type.HRESULT]
    ReplaceChild: _Callable[[IXmlNode,  # newChild
                             IXmlNode,  # referenceChild
                             _Pointer[IXmlNode]],  # previousChild
                            _type.HRESULT]
    RemoveChild: _Callable[[IXmlNode,  # childNode
                            _Pointer[IXmlNode]],  # removedChild
                           _type.HRESULT]
    AppendChild: _Callable[[IXmlNode,  # newChild
                            _Pointer[IXmlNode]],  # appendedChild
                           _type.HRESULT]
    CloneNode: _Callable[[_type.boolean,  # deep
                          _Pointer[IXmlNode]],  # newNode
                         _type.HRESULT]
    get_NamespaceUri: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                _type.HRESULT]
    get_LocalName: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                             _type.HRESULT]
    get_Prefix: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                          _type.HRESULT]
    Normalize: _Callable[[],
                         _type.HRESULT]
    put_Prefix: _Callable[[_inspectable.IInspectable],  # value
                          _type.HRESULT]


class IXmlNodeList(_inspectable.IInspectable):
    get_Length: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    Item: _Callable[[_type.UINT32,  # index
                     _Pointer[IXmlNode]],  # node
                    _type.HRESULT]


class IXmlNodeSelector(_inspectable.IInspectable):
    SelectSingleNode: _Callable[[_type.HSTRING,  # xpath
                                 _Pointer[IXmlNode]],  # node
                                _type.HRESULT]
    SelectNodes: _Callable[[_type.HSTRING,  # xpath
                            _Pointer[IXmlNodeList]],  # nodelist
                           _type.HRESULT]
    SelectSingleNodeNS: _Callable[[_type.HSTRING,  # xpath
                                   _inspectable.IInspectable,  # namespaces
                                   _Pointer[IXmlNode]],  # node
                                  _type.HRESULT]
    SelectNodesNS: _Callable[[_type.HSTRING,  # xpath
                              _inspectable.IInspectable,  # namespaces
                              _Pointer[IXmlNodeList]],  # nodelist
                             _type.HRESULT]


class IXmlNodeSerializer(_inspectable.IInspectable):
    GetXml: _Callable[[_Pointer[_type.HSTRING]],  # outerXml
                      _type.HRESULT]
    get_InnerText: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_InnerText: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]


class IXmlProcessingInstruction(_inspectable.IInspectable):
    get_Target: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Data: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Data: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]


class IXmlText(_inspectable.IInspectable):
    SplitText: _Callable[[_type.UINT32,  # offset
                          _Pointer[IXmlText]],  # secondPart
                         _type.HRESULT]
