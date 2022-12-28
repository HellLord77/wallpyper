from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...Data.Xml import Dom as _Windows_Data_Xml_Dom
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Security import Credentials as _Windows_Security_Credentials
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class ISyndicationAttribute(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Name: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_Namespace: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_Namespace: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Value: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]


class ISyndicationAttributeFactory(_inspectable.IInspectable):
    CreateSyndicationAttribute: _Callable[[_type.HSTRING,  # attributeName
                                           _type.HSTRING,  # attributeNamespace
                                           _type.HSTRING,  # attributeValue
                                           _Pointer[ISyndicationAttribute]],  # syndicationAttribute
                                          _type.HRESULT]

    _factory = True


class ISyndicationCategory(_inspectable.IInspectable):
    get_Label: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Label: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Scheme: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    put_Scheme: _Callable[[_type.HSTRING],  # value
                          _type.HRESULT]
    get_Term: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Term: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]


class ISyndicationCategoryFactory(_inspectable.IInspectable):
    CreateSyndicationCategory: _Callable[[_type.HSTRING,  # term
                                          _Pointer[ISyndicationCategory]],  # category
                                         _type.HRESULT]
    CreateSyndicationCategoryEx: _Callable[[_type.HSTRING,  # term
                                            _type.HSTRING,  # scheme
                                            _type.HSTRING,  # label
                                            _Pointer[ISyndicationCategory]],  # category
                                           _type.HRESULT]

    _factory = True


class ISyndicationClient(_inspectable.IInspectable):
    get_ServerCredential: _Callable[[_Pointer[_Windows_Security_Credentials.IPasswordCredential]],  # value
                                    _type.HRESULT]
    put_ServerCredential: _Callable[[_Windows_Security_Credentials.IPasswordCredential],  # value
                                    _type.HRESULT]
    get_ProxyCredential: _Callable[[_Pointer[_Windows_Security_Credentials.IPasswordCredential]],  # value
                                   _type.HRESULT]
    put_ProxyCredential: _Callable[[_Windows_Security_Credentials.IPasswordCredential],  # value
                                   _type.HRESULT]
    get_MaxResponseBufferSize: _Callable[[_Pointer[_type.UINT32]],  # value
                                         _type.HRESULT]
    put_MaxResponseBufferSize: _Callable[[_type.UINT32],  # value
                                         _type.HRESULT]
    get_Timeout: _Callable[[_Pointer[_type.UINT32]],  # value
                           _type.HRESULT]
    put_Timeout: _Callable[[_type.UINT32],  # value
                           _type.HRESULT]
    get_BypassCacheOnRetrieve: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_BypassCacheOnRetrieve: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]
    SetRequestHeader: _Callable[[_type.HSTRING,  # name
                                 _type.HSTRING],  # value
                                _type.HRESULT]
    RetrieveFeedAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                  _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[ISyndicationFeed, _struct.Windows.Web.Syndication.RetrievalProgress]]],  # operation
                                 _type.HRESULT]


class ISyndicationClientFactory(_inspectable.IInspectable):
    CreateSyndicationClient: _Callable[[_Windows_Security_Credentials.IPasswordCredential,  # serverCredential
                                        _Pointer[ISyndicationClient]],  # syndicationClient
                                       _type.HRESULT]

    _factory = True


class ISyndicationContent(_inspectable.IInspectable):
    get_SourceUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                             _type.HRESULT]
    put_SourceUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                             _type.HRESULT]


class ISyndicationContentFactory(_inspectable.IInspectable):
    CreateSyndicationContent: _Callable[[_type.HSTRING,  # text
                                         _enum.Windows.Web.Syndication.SyndicationTextType,  # type
                                         _Pointer[ISyndicationContent]],  # content
                                        _type.HRESULT]
    CreateSyndicationContentWithSourceUri: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # sourceUri
                                                      _Pointer[ISyndicationContent]],  # content
                                                     _type.HRESULT]

    _factory = True


class ISyndicationErrorStatics(_inspectable.IInspectable):
    GetStatus: _Callable[[_type.INT32,  # hresult
                          _Pointer[_enum.Windows.Web.Syndication.SyndicationErrorStatus]],  # status
                         _type.HRESULT]

    _factory = True


class ISyndicationFeed(_inspectable.IInspectable):
    get_Authors: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ISyndicationPerson]]],  # value
                           _type.HRESULT]
    get_Categories: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ISyndicationCategory]]],  # value
                              _type.HRESULT]
    get_Contributors: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ISyndicationPerson]]],  # value
                                _type.HRESULT]
    get_Generator: _Callable[[_Pointer[ISyndicationGenerator]],  # value
                             _type.HRESULT]
    put_Generator: _Callable[[ISyndicationGenerator],  # value
                             _type.HRESULT]
    get_IconUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                           _type.HRESULT]
    put_IconUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                           _type.HRESULT]
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    put_Id: _Callable[[_type.HSTRING],  # value
                      _type.HRESULT]
    get_Items: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ISyndicationItem]]],  # value
                         _type.HRESULT]
    get_LastUpdatedTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                   _type.HRESULT]
    put_LastUpdatedTime: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                                   _type.HRESULT]
    get_Links: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ISyndicationLink]]],  # value
                         _type.HRESULT]
    get_ImageUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                            _type.HRESULT]
    put_ImageUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                            _type.HRESULT]
    get_Rights: _Callable[[_Pointer[ISyndicationText]],  # value
                          _type.HRESULT]
    put_Rights: _Callable[[ISyndicationText],  # value
                          _type.HRESULT]
    get_Subtitle: _Callable[[_Pointer[ISyndicationText]],  # value
                            _type.HRESULT]
    put_Subtitle: _Callable[[ISyndicationText],  # value
                            _type.HRESULT]
    get_Title: _Callable[[_Pointer[ISyndicationText]],  # value
                         _type.HRESULT]
    put_Title: _Callable[[ISyndicationText],  # value
                         _type.HRESULT]
    get_FirstUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                            _type.HRESULT]
    get_LastUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                           _type.HRESULT]
    get_NextUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                           _type.HRESULT]
    get_PreviousUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                               _type.HRESULT]
    get_SourceFormat: _Callable[[_Pointer[_enum.Windows.Web.Syndication.SyndicationFormat]],  # value
                                _type.HRESULT]
    Load: _Callable[[_type.HSTRING],  # feed
                    _type.HRESULT]
    LoadFromXml: _Callable[[_Windows_Data_Xml_Dom.IXmlDocument],  # feedDocument
                           _type.HRESULT]


class ISyndicationFeedFactory(_inspectable.IInspectable):
    CreateSyndicationFeed: _Callable[[_type.HSTRING,  # title
                                      _type.HSTRING,  # subtitle
                                      _Windows_Foundation.IUriRuntimeClass,  # uri
                                      _Pointer[ISyndicationFeed]],  # feed
                                     _type.HRESULT]

    _factory = True


class ISyndicationGenerator(_inspectable.IInspectable):
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Text: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]
    put_Uri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                       _type.HRESULT]
    get_Version: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    put_Version: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]


class ISyndicationGeneratorFactory(_inspectable.IInspectable):
    CreateSyndicationGenerator: _Callable[[_type.HSTRING,  # text
                                           _Pointer[ISyndicationGenerator]],  # generator
                                          _type.HRESULT]

    _factory = True


class ISyndicationItem(_inspectable.IInspectable):
    get_Authors: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ISyndicationPerson]]],  # value
                           _type.HRESULT]
    get_Categories: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ISyndicationCategory]]],  # value
                              _type.HRESULT]
    get_Contributors: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ISyndicationPerson]]],  # value
                                _type.HRESULT]
    get_Content: _Callable[[_Pointer[ISyndicationContent]],  # value
                           _type.HRESULT]
    put_Content: _Callable[[ISyndicationContent],  # value
                           _type.HRESULT]
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    put_Id: _Callable[[_type.HSTRING],  # value
                      _type.HRESULT]
    get_LastUpdatedTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                   _type.HRESULT]
    put_LastUpdatedTime: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                                   _type.HRESULT]
    get_Links: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ISyndicationLink]]],  # value
                         _type.HRESULT]
    get_PublishedDate: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                 _type.HRESULT]
    put_PublishedDate: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                                 _type.HRESULT]
    get_Rights: _Callable[[_Pointer[ISyndicationText]],  # value
                          _type.HRESULT]
    put_Rights: _Callable[[ISyndicationText],  # value
                          _type.HRESULT]
    get_Source: _Callable[[_Pointer[ISyndicationFeed]],  # value
                          _type.HRESULT]
    put_Source: _Callable[[ISyndicationFeed],  # value
                          _type.HRESULT]
    get_Summary: _Callable[[_Pointer[ISyndicationText]],  # value
                           _type.HRESULT]
    put_Summary: _Callable[[ISyndicationText],  # value
                           _type.HRESULT]
    get_Title: _Callable[[_Pointer[ISyndicationText]],  # value
                         _type.HRESULT]
    put_Title: _Callable[[ISyndicationText],  # value
                         _type.HRESULT]
    get_CommentsUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                               _type.HRESULT]
    put_CommentsUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                               _type.HRESULT]
    get_EditUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                           _type.HRESULT]
    get_EditMediaUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                _type.HRESULT]
    get_ETag: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_ItemUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                           _type.HRESULT]
    Load: _Callable[[_type.HSTRING],  # item
                    _type.HRESULT]
    LoadFromXml: _Callable[[_Windows_Data_Xml_Dom.IXmlDocument],  # itemDocument
                           _type.HRESULT]


class ISyndicationItemFactory(_inspectable.IInspectable):
    CreateSyndicationItem: _Callable[[_type.HSTRING,  # title
                                      ISyndicationContent,  # content
                                      _Windows_Foundation.IUriRuntimeClass,  # uri
                                      _Pointer[ISyndicationItem]],  # item
                                     _type.HRESULT]

    _factory = True


class ISyndicationLink(_inspectable.IInspectable):
    get_Length: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    put_Length: _Callable[[_type.UINT32],  # value
                          _type.HRESULT]
    get_MediaType: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_MediaType: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_Relationship: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    put_Relationship: _Callable[[_type.HSTRING],  # value
                                _type.HRESULT]
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Title: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]
    put_Uri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                       _type.HRESULT]
    get_ResourceLanguage: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    put_ResourceLanguage: _Callable[[_type.HSTRING],  # value
                                    _type.HRESULT]


class ISyndicationLinkFactory(_inspectable.IInspectable):
    CreateSyndicationLink: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                      _Pointer[ISyndicationLink]],  # link
                                     _type.HRESULT]
    CreateSyndicationLinkEx: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                        _type.HSTRING,  # relationship
                                        _type.HSTRING,  # title
                                        _type.HSTRING,  # mediaType
                                        _type.UINT32,  # length
                                        _Pointer[ISyndicationLink]],  # link
                                       _type.HRESULT]

    _factory = True


class ISyndicationNode(_inspectable.IInspectable):
    get_NodeName: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_NodeName: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_NodeNamespace: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    put_NodeNamespace: _Callable[[_type.HSTRING],  # value
                                 _type.HRESULT]
    get_NodeValue: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_NodeValue: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_Language: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_Language: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_BaseUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                           _type.HRESULT]
    put_BaseUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                           _type.HRESULT]
    get_AttributeExtensions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ISyndicationAttribute]]],  # value
                                       _type.HRESULT]
    get_ElementExtensions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ISyndicationNode]]],  # value
                                     _type.HRESULT]
    GetXmlDocument: _Callable[[_enum.Windows.Web.Syndication.SyndicationFormat,  # format
                               _Pointer[_Windows_Data_Xml_Dom.IXmlDocument]],  # xmlDocument
                              _type.HRESULT]


class ISyndicationNodeFactory(_inspectable.IInspectable):
    CreateSyndicationNode: _Callable[[_type.HSTRING,  # nodeName
                                      _type.HSTRING,  # nodeNamespace
                                      _type.HSTRING,  # nodeValue
                                      _Pointer[ISyndicationNode]],  # node
                                     _type.HRESULT]

    _factory = True


class ISyndicationPerson(_inspectable.IInspectable):
    get_Email: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Email: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Name: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]
    put_Uri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                       _type.HRESULT]


class ISyndicationPersonFactory(_inspectable.IInspectable):
    CreateSyndicationPerson: _Callable[[_type.HSTRING,  # name
                                        _Pointer[ISyndicationPerson]],  # person
                                       _type.HRESULT]
    CreateSyndicationPersonEx: _Callable[[_type.HSTRING,  # name
                                          _type.HSTRING,  # email
                                          _Windows_Foundation.IUriRuntimeClass,  # uri
                                          _Pointer[ISyndicationPerson]],  # person
                                         _type.HRESULT]

    _factory = True


class ISyndicationText(_inspectable.IInspectable):
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Text: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_Type: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Type: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_Xml: _Callable[[_Pointer[_Windows_Data_Xml_Dom.IXmlDocument]],  # value
                       _type.HRESULT]
    put_Xml: _Callable[[_Windows_Data_Xml_Dom.IXmlDocument],  # value
                       _type.HRESULT]


class ISyndicationTextFactory(_inspectable.IInspectable):
    CreateSyndicationText: _Callable[[_type.HSTRING,  # text
                                      _Pointer[ISyndicationText]],  # syndicationText
                                     _type.HRESULT]
    CreateSyndicationTextEx: _Callable[[_type.HSTRING,  # text
                                        _enum.Windows.Web.Syndication.SyndicationTextType,  # type
                                        _Pointer[ISyndicationText]],  # syndicationText
                                       _type.HRESULT]

    _factory = True
