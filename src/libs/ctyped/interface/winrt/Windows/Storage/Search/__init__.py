from __future__ import annotations

from typing import Callable as _Callable

from .. import Streams as _Windows_Storage_Streams
from ... import Foundation as _Windows_Foundation
from ... import Storage as _Windows_Storage
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IContentIndexer(_inspectable.IInspectable):
    AddAsync: _Callable[[IIndexableContent,  # indexableContent
                         _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                        _type.HRESULT]
    UpdateAsync: _Callable[[IIndexableContent,  # indexableContent
                            _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                           _type.HRESULT]
    DeleteAsync: _Callable[[_type.HSTRING,  # contentId
                            _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                           _type.HRESULT]
    DeleteMultipleAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # contentIds
                                    _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                   _type.HRESULT]
    DeleteAllAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                              _type.HRESULT]
    RetrievePropertiesAsync: _Callable[[_type.HSTRING,  # contentId
                                        _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # propertiesToRetrieve
                                        _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _inspectable.IInspectable]]]],  # operation
                                       _type.HRESULT]
    get_Revision: _Callable[[_Pointer[_type.UINT64]],  # value
                            _type.HRESULT]


class IContentIndexerQuery(_inspectable.IInspectable):
    GetCountAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.UINT32]]],  # operation
                             _type.HRESULT]
    GetPropertiesAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _inspectable.IInspectable]]]]],  # operation
                                  _type.HRESULT]
    GetPropertiesRangeAsync: _Callable[[_type.UINT32,  # startIndex
                                        _type.UINT32,  # maxItems
                                        _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _inspectable.IInspectable]]]]],  # operation
                                       _type.HRESULT]
    GetAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IIndexableContent]]]],  # operation
                        _type.HRESULT]
    GetRangeAsync: _Callable[[_type.UINT32,  # startIndex
                              _type.UINT32,  # maxItems
                              _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IIndexableContent]]]],  # operation
                             _type.HRESULT]
    get_QueryFolder: _Callable[[_Pointer[_Windows_Storage.IStorageFolder]],  # value
                               _type.HRESULT]


class IContentIndexerQueryOperations(_inspectable.IInspectable):
    CreateQueryWithSortOrderAndLanguage: _Callable[[_type.HSTRING,  # searchFilter
                                                    _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # propertiesToRetrieve
                                                    _Windows_Foundation_Collections.IIterable[_struct.Windows.Storage.Search.SortEntry],  # sortOrder
                                                    _type.HSTRING,  # searchFilterLanguage
                                                    _Pointer[IContentIndexerQuery]],  # query
                                                   _type.HRESULT]
    CreateQueryWithSortOrder: _Callable[[_type.HSTRING,  # searchFilter
                                         _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # propertiesToRetrieve
                                         _Windows_Foundation_Collections.IIterable[_struct.Windows.Storage.Search.SortEntry],  # sortOrder
                                         _Pointer[IContentIndexerQuery]],  # query
                                        _type.HRESULT]
    CreateQuery: _Callable[[_type.HSTRING,  # searchFilter
                            _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # propertiesToRetrieve
                            _Pointer[IContentIndexerQuery]],  # query
                           _type.HRESULT]


class IContentIndexerStatics(_inspectable.IInspectable, factory=True):
    GetIndexerWithName: _Callable[[_type.HSTRING,  # indexName
                                   _Pointer[IContentIndexer]],  # index
                                  _type.HRESULT]
    GetIndexer: _Callable[[_Pointer[IContentIndexer]],  # index
                          _type.HRESULT]


class IIndexableContent(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    put_Id: _Callable[[_type.HSTRING],  # value
                      _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, _inspectable.IInspectable]]],  # value
                              _type.HRESULT]
    get_Stream: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStream]],  # value
                          _type.HRESULT]
    put_Stream: _Callable[[_Windows_Storage_Streams.IRandomAccessStream],  # value
                          _type.HRESULT]
    get_StreamContentType: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    put_StreamContentType: _Callable[[_type.HSTRING],  # value
                                     _type.HRESULT]


class IQueryOptions(_inspectable.IInspectable):
    get_FileTypeFilter: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                  _type.HRESULT]
    get_FolderDepth: _Callable[[_Pointer[_enum.Windows.Storage.Search.FolderDepth]],  # value
                               _type.HRESULT]
    put_FolderDepth: _Callable[[_enum.Windows.Storage.Search.FolderDepth],  # value
                               _type.HRESULT]
    get_ApplicationSearchFilter: _Callable[[_Pointer[_type.HSTRING]],  # value
                                           _type.HRESULT]
    put_ApplicationSearchFilter: _Callable[[_type.HSTRING],  # value
                                           _type.HRESULT]
    get_UserSearchFilter: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    put_UserSearchFilter: _Callable[[_type.HSTRING],  # value
                                    _type.HRESULT]
    get_Language: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_Language: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_IndexerOption: _Callable[[_Pointer[_enum.Windows.Storage.Search.IndexerOption]],  # value
                                 _type.HRESULT]
    put_IndexerOption: _Callable[[_enum.Windows.Storage.Search.IndexerOption],  # value
                                 _type.HRESULT]
    get_SortOrder: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_struct.Windows.Storage.Search.SortEntry]]],  # value
                             _type.HRESULT]
    get_GroupPropertyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    get_DateStackOption: _Callable[[_Pointer[_enum.Windows.Storage.Search.DateStackOption]],  # value
                                   _type.HRESULT]
    SaveToString: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    LoadFromString: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]
    SetThumbnailPrefetch: _Callable[[_enum.Windows.Storage.FileProperties.ThumbnailMode,  # mode
                                     _type.UINT32,  # requestedSize
                                     _enum.Windows.Storage.FileProperties.ThumbnailOptions],  # options
                                    _type.HRESULT]
    SetPropertyPrefetch: _Callable[[_enum.Windows.Storage.FileProperties.PropertyPrefetchOptions,  # options
                                    _Windows_Foundation_Collections.IIterable[_type.HSTRING]],  # propertiesToRetrieve
                                   _type.HRESULT]


class IQueryOptionsFactory(_inspectable.IInspectable, factory=True):
    CreateCommonFileQuery: _Callable[[_enum.Windows.Storage.Search.CommonFileQuery,  # query
                                      _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # fileTypeFilter
                                      _Pointer[IQueryOptions]],  # queryOptions
                                     _type.HRESULT]
    CreateCommonFolderQuery: _Callable[[_enum.Windows.Storage.Search.CommonFolderQuery,  # query
                                        _Pointer[IQueryOptions]],  # queryOptions
                                       _type.HRESULT]


class IQueryOptionsWithProviderFilter(_inspectable.IInspectable):
    get_StorageProviderIdFilter: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                           _type.HRESULT]


class IStorageFileQueryResult(_inspectable.IInspectable):
    GetFilesAsync: _Callable[[_type.UINT32,  # startIndex
                              _type.UINT32,  # maxNumberOfItems
                              _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_Storage.IStorageFile]]]],  # operation
                             _type.HRESULT]
    GetFilesAsyncDefaultStartAndCount: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_Storage.IStorageFile]]]],  # operation
                                                 _type.HRESULT]


class IStorageFileQueryResult2(_inspectable.IInspectable):
    GetMatchingPropertiesWithRanges: _Callable[[_Windows_Storage.IStorageFile,  # file
                                                _Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, _Windows_Foundation_Collections.IVectorView[_struct.Windows.Data.Text.TextSegment]]]],  # result
                                               _type.HRESULT]


class IStorageFolderQueryOperations(_inspectable.IInspectable):
    GetIndexedStateAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Storage.Search.IndexedState]]],  # operation
                                    _type.HRESULT]
    CreateFileQueryOverloadDefault: _Callable[[_Pointer[IStorageFileQueryResult]],  # value
                                              _type.HRESULT]
    CreateFileQuery: _Callable[[_enum.Windows.Storage.Search.CommonFileQuery,  # query
                                _Pointer[IStorageFileQueryResult]],  # value
                               _type.HRESULT]
    CreateFileQueryWithOptions: _Callable[[IQueryOptions,  # queryOptions
                                           _Pointer[IStorageFileQueryResult]],  # value
                                          _type.HRESULT]
    CreateFolderQueryOverloadDefault: _Callable[[_Pointer[IStorageFolderQueryResult]],  # value
                                                _type.HRESULT]
    CreateFolderQuery: _Callable[[_enum.Windows.Storage.Search.CommonFolderQuery,  # query
                                  _Pointer[IStorageFolderQueryResult]],  # value
                                 _type.HRESULT]
    CreateFolderQueryWithOptions: _Callable[[IQueryOptions,  # queryOptions
                                             _Pointer[IStorageFolderQueryResult]],  # value
                                            _type.HRESULT]
    CreateItemQuery: _Callable[[_Pointer[IStorageItemQueryResult]],  # value
                               _type.HRESULT]
    CreateItemQueryWithOptions: _Callable[[IQueryOptions,  # queryOptions
                                           _Pointer[IStorageItemQueryResult]],  # value
                                          _type.HRESULT]
    GetFilesAsync: _Callable[[_enum.Windows.Storage.Search.CommonFileQuery,  # query
                              _type.UINT32,  # startIndex
                              _type.UINT32,  # maxItemsToRetrieve
                              _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_Storage.IStorageFile]]]],  # operation
                             _type.HRESULT]
    GetFilesAsyncOverloadDefaultStartAndCount: _Callable[[_enum.Windows.Storage.Search.CommonFileQuery,  # query
                                                          _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_Storage.IStorageFile]]]],  # operation
                                                         _type.HRESULT]
    GetFoldersAsync: _Callable[[_enum.Windows.Storage.Search.CommonFolderQuery,  # query
                                _type.UINT32,  # startIndex
                                _type.UINT32,  # maxItemsToRetrieve
                                _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_Storage.IStorageFolder]]]],  # operation
                               _type.HRESULT]
    GetFoldersAsyncOverloadDefaultStartAndCount: _Callable[[_enum.Windows.Storage.Search.CommonFolderQuery,  # query
                                                            _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_Storage.IStorageFolder]]]],  # operation
                                                           _type.HRESULT]
    GetItemsAsync: _Callable[[_type.UINT32,  # startIndex
                              _type.UINT32,  # maxItemsToRetrieve
                              _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_Storage.IStorageItem]]]],  # operation
                             _type.HRESULT]
    AreQueryOptionsSupported: _Callable[[IQueryOptions,  # queryOptions
                                         _Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    IsCommonFolderQuerySupported: _Callable[[_enum.Windows.Storage.Search.CommonFolderQuery,  # query
                                             _Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    IsCommonFileQuerySupported: _Callable[[_enum.Windows.Storage.Search.CommonFileQuery,  # query
                                           _Pointer[_type.boolean]],  # value
                                          _type.HRESULT]


class IStorageFolderQueryResult(_inspectable.IInspectable):
    GetFoldersAsync: _Callable[[_type.UINT32,  # startIndex
                                _type.UINT32,  # maxNumberOfItems
                                _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_Storage.IStorageFolder]]]],  # operation
                               _type.HRESULT]
    GetFoldersAsyncDefaultStartAndCount: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_Storage.IStorageFolder]]]],  # operation
                                                   _type.HRESULT]


class IStorageItemQueryResult(_inspectable.IInspectable):
    GetItemsAsync: _Callable[[_type.UINT32,  # startIndex
                              _type.UINT32,  # maxNumberOfItems
                              _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_Storage.IStorageItem]]]],  # operation
                             _type.HRESULT]
    GetItemsAsyncDefaultStartAndCount: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_Storage.IStorageItem]]]],  # operation
                                                 _type.HRESULT]


class IStorageLibraryChangeTrackerTriggerDetails(_inspectable.IInspectable):
    get_Folder: _Callable[[_Pointer[_Windows_Storage.IStorageFolder]],  # value
                          _type.HRESULT]
    get_ChangeTracker: _Callable[[_Pointer[_Windows_Storage.IStorageLibraryChangeTracker]],  # value
                                 _type.HRESULT]


class IStorageLibraryContentChangedTriggerDetails(_inspectable.IInspectable):
    get_Folder: _Callable[[_Pointer[_Windows_Storage.IStorageFolder]],  # value
                          _type.HRESULT]
    CreateModifiedSinceQuery: _Callable[[_struct.Windows.Foundation.DateTime,  # lastQueryTime
                                         _Pointer[IStorageItemQueryResult]],  # result
                                        _type.HRESULT]


class IStorageQueryResultBase(_inspectable.IInspectable):
    GetItemCountAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.UINT32]]],  # operation
                                 _type.HRESULT]
    get_Folder: _Callable[[_Pointer[_Windows_Storage.IStorageFolder]],  # container
                          _type.HRESULT]
    add_ContentsChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IStorageQueryResultBase, _inspectable.IInspectable],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                                   _type.HRESULT]
    remove_ContentsChanged: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                      _type.HRESULT]
    add_OptionsChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IStorageQueryResultBase, _inspectable.IInspectable],  # changedHandler
                                   _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                                  _type.HRESULT]
    remove_OptionsChanged: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                     _type.HRESULT]
    FindStartIndexAsync: _Callable[[_inspectable.IInspectable,  # value
                                    _Pointer[_Windows_Foundation.IAsyncOperation[_type.UINT32]]],  # operation
                                   _type.HRESULT]
    GetCurrentQueryOptions: _Callable[[_Pointer[IQueryOptions]],  # value
                                      _type.HRESULT]
    ApplyNewQueryOptions: _Callable[[IQueryOptions],  # newQueryOptions
                                    _type.HRESULT]


class IValueAndLanguage(_inspectable.IInspectable):
    get_Language: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_Language: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_Value: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                         _type.HRESULT]
    put_Value: _Callable[[_inspectable.IInspectable],  # value
                         _type.HRESULT]
