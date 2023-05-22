from __future__ import annotations

from typing import Callable as _Callable

from .. import Syndication as _Windows_Web_Syndication
from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Security import Credentials as _Windows_Security_Credentials
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IAtomPubClient(_inspectable.IInspectable):
    RetrieveServiceDocumentAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                             _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IServiceDocument, _struct.Windows.Web.Syndication.RetrievalProgress]]],  # operation
                                            _type.HRESULT]
    RetrieveMediaResourceAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                           _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[_Windows_Storage_Streams.IInputStream, _struct.Windows.Web.Syndication.RetrievalProgress]]],  # operation
                                          _type.HRESULT]
    RetrieveResourceAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                      _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[_Windows_Web_Syndication.ISyndicationItem, _struct.Windows.Web.Syndication.RetrievalProgress]]],  # operation
                                     _type.HRESULT]
    CreateResourceAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                    _type.HSTRING,  # description
                                    _Windows_Web_Syndication.ISyndicationItem,  # item
                                    _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[_Windows_Web_Syndication.ISyndicationItem, _struct.Windows.Web.Syndication.TransferProgress]]],  # operation
                                   _type.HRESULT]
    CreateMediaResourceAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                         _type.HSTRING,  # mediaType
                                         _type.HSTRING,  # description
                                         _Windows_Storage_Streams.IInputStream,  # mediaStream
                                         _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[_Windows_Web_Syndication.ISyndicationItem, _struct.Windows.Web.Syndication.TransferProgress]]],  # operation
                                        _type.HRESULT]
    UpdateMediaResourceAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                         _type.HSTRING,  # mediaType
                                         _Windows_Storage_Streams.IInputStream,  # mediaStream
                                         _Pointer[_Windows_Foundation.IAsyncActionWithProgress[_struct.Windows.Web.Syndication.TransferProgress]]],  # operation
                                        _type.HRESULT]
    UpdateResourceAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                    _Windows_Web_Syndication.ISyndicationItem,  # item
                                    _Pointer[_Windows_Foundation.IAsyncActionWithProgress[_struct.Windows.Web.Syndication.TransferProgress]]],  # operation
                                   _type.HRESULT]
    UpdateResourceItemAsync: _Callable[[_Windows_Web_Syndication.ISyndicationItem,  # item
                                        _Pointer[_Windows_Foundation.IAsyncActionWithProgress[_struct.Windows.Web.Syndication.TransferProgress]]],  # operation
                                       _type.HRESULT]
    DeleteResourceAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                    _Pointer[_Windows_Foundation.IAsyncActionWithProgress[_struct.Windows.Web.Syndication.TransferProgress]]],  # operation
                                   _type.HRESULT]
    DeleteResourceItemAsync: _Callable[[_Windows_Web_Syndication.ISyndicationItem,  # item
                                        _Pointer[_Windows_Foundation.IAsyncActionWithProgress[_struct.Windows.Web.Syndication.TransferProgress]]],  # operation
                                       _type.HRESULT]
    CancelAsyncOperations: _Callable[[],
                                     _type.HRESULT]


class IAtomPubClientFactory(_inspectable.IInspectable, factory=True):
    CreateAtomPubClientWithCredentials: _Callable[[_Windows_Security_Credentials.IPasswordCredential,  # serverCredential
                                                   _Pointer[IAtomPubClient]],  # atomPubClient
                                                  _type.HRESULT]


class IResourceCollection(_inspectable.IInspectable):
    get_Title: _Callable[[_Pointer[_Windows_Web_Syndication.ISyndicationText]],  # value
                         _type.HRESULT]
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]
    get_Categories: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Web_Syndication.ISyndicationCategory]]],  # value
                              _type.HRESULT]
    get_Accepts: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                           _type.HRESULT]


class IServiceDocument(_inspectable.IInspectable):
    get_Workspaces: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IWorkspace]]],  # value
                              _type.HRESULT]


class IWorkspace(_inspectable.IInspectable):
    get_Title: _Callable[[_Pointer[_Windows_Web_Syndication.ISyndicationText]],  # value
                         _type.HRESULT]
    get_Collections: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IResourceCollection]]],  # value
                               _type.HRESULT]
