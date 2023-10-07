from __future__ import annotations as _

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import type as _type
from ......._utils import _Pointer


class IIndexedResourceCandidate(_inspectable.IInspectable):
    get_Type: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Resources.Management.IndexedResourceType]],  # value
                        _type.HRESULT]
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]
    get_Metadata: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _type.HSTRING]]],  # value
                            _type.HRESULT]
    get_Qualifiers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IIndexedResourceQualifier]]],  # value
                              _type.HRESULT]
    get_ValueAsString: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    GetQualifierValue: _Callable[[_type.HSTRING,  # qualifierName
                                  _Pointer[_type.HSTRING]],  # qualifierValue
                                 _type.HRESULT]


class IIndexedResourceQualifier(_inspectable.IInspectable):
    get_QualifierName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_QualifierValue: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]


class IResourceIndexer(_inspectable.IInspectable):
    IndexFilePath: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # filePath
                              _Pointer[IIndexedResourceCandidate]],  # candidate
                             _type.HRESULT]
    IndexFileContentsAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # file
                                       _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IIndexedResourceCandidate]]]],  # operation
                                      _type.HRESULT]


class IResourceIndexerFactory(_inspectable.IInspectable):
    CreateResourceIndexer: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # projectRoot
                                      _Pointer[IResourceIndexer]],  # indexer
                                     _type.HRESULT]


class IResourceIndexerFactory2(_inspectable.IInspectable, factory=True):
    CreateResourceIndexerWithExtension: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # projectRoot
                                                   _Windows_Foundation.IUriRuntimeClass,  # extensionDllPath
                                                   _Pointer[IResourceIndexer]],  # indexer
                                                  _type.HRESULT]
