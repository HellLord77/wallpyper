from __future__ import annotations as _

from typing import Callable as _Callable

from .. import FileProperties as _Windows_Storage_FileProperties
from .. import Search as _Windows_Storage_Search
from .. import Streams as _Windows_Storage_Streams
from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IFileInformationFactory(_inspectable.IInspectable):
    GetItemsAsync: _Callable[[_type.UINT32,  # startIndex
                              _type.UINT32,  # maxItemsToRetrieve
                              _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IStorageItemInformation]]]],  # operation
                             _type.HRESULT]
    GetItemsAsyncDefaultStartAndCount: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IStorageItemInformation]]]],  # operation
                                                 _type.HRESULT]
    GetFilesAsync: _Callable[[_type.UINT32,  # startIndex
                              _type.UINT32,  # maxItemsToRetrieve
                              _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IStorageItemInformation]]]],  # operation
                             _type.HRESULT]
    GetFilesAsyncDefaultStartAndCount: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IStorageItemInformation]]]],  # operation
                                                 _type.HRESULT]
    GetFoldersAsync: _Callable[[_type.UINT32,  # startIndex
                                _type.UINT32,  # maxItemsToRetrieve
                                _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IStorageItemInformation]]]],  # operation
                               _type.HRESULT]
    GetFoldersAsyncDefaultStartAndCount: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IStorageItemInformation]]]],  # operation
                                                   _type.HRESULT]
    GetVirtualizedItemsVector: _Callable[[_Pointer[_inspectable.IInspectable]],  # vector
                                         _type.HRESULT]
    GetVirtualizedFilesVector: _Callable[[_Pointer[_inspectable.IInspectable]],  # vector
                                         _type.HRESULT]
    GetVirtualizedFoldersVector: _Callable[[_Pointer[_inspectable.IInspectable]],  # vector
                                           _type.HRESULT]


class IFileInformationFactoryFactory(_inspectable.IInspectable, factory=True):
    CreateWithMode: _Callable[[_Windows_Storage_Search.IStorageQueryResultBase,  # queryResult
                               _enum.Windows.Storage.FileProperties.ThumbnailMode,  # mode
                               _Pointer[IFileInformationFactory]],  # value
                              _type.HRESULT]
    CreateWithModeAndSize: _Callable[[_Windows_Storage_Search.IStorageQueryResultBase,  # queryResult
                                      _enum.Windows.Storage.FileProperties.ThumbnailMode,  # mode
                                      _type.UINT32,  # requestedThumbnailSize
                                      _Pointer[IFileInformationFactory]],  # value
                                     _type.HRESULT]
    CreateWithModeAndSizeAndOptions: _Callable[[_Windows_Storage_Search.IStorageQueryResultBase,  # queryResult
                                                _enum.Windows.Storage.FileProperties.ThumbnailMode,  # mode
                                                _type.UINT32,  # requestedThumbnailSize
                                                _enum.Windows.Storage.FileProperties.ThumbnailOptions,  # thumbnailOptions
                                                _Pointer[IFileInformationFactory]],  # value
                                               _type.HRESULT]
    CreateWithModeAndSizeAndOptionsAndFlags: _Callable[[_Windows_Storage_Search.IStorageQueryResultBase,  # queryResult
                                                        _enum.Windows.Storage.FileProperties.ThumbnailMode,  # mode
                                                        _type.UINT32,  # requestedThumbnailSize
                                                        _enum.Windows.Storage.FileProperties.ThumbnailOptions,  # thumbnailOptions
                                                        _type.boolean,  # delayLoad
                                                        _Pointer[IFileInformationFactory]],  # value
                                                       _type.HRESULT]


class IStorageItemInformation(_inspectable.IInspectable):
    get_MusicProperties: _Callable[[_Pointer[_Windows_Storage_FileProperties.IMusicProperties]],  # value
                                   _type.HRESULT]
    get_VideoProperties: _Callable[[_Pointer[_Windows_Storage_FileProperties.IVideoProperties]],  # value
                                   _type.HRESULT]
    get_ImageProperties: _Callable[[_Pointer[_Windows_Storage_FileProperties.IImageProperties]],  # value
                                   _type.HRESULT]
    get_DocumentProperties: _Callable[[_Pointer[_Windows_Storage_FileProperties.IDocumentProperties]],  # value
                                      _type.HRESULT]
    get_BasicProperties: _Callable[[_Pointer[_Windows_Storage_FileProperties.IBasicProperties]],  # value
                                   _type.HRESULT]
    get_Thumbnail: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamWithContentType]],  # value
                             _type.HRESULT]
    add_ThumbnailUpdated: _Callable[[_Windows_Foundation.ITypedEventHandler[IStorageItemInformation, _inspectable.IInspectable],  # changedHandler
                                     _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                                    _type.HRESULT]
    remove_ThumbnailUpdated: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                       _type.HRESULT]
    add_PropertiesUpdated: _Callable[[_Windows_Foundation.ITypedEventHandler[IStorageItemInformation, _inspectable.IInspectable],  # changedHandler
                                      _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                                     _type.HRESULT]
    remove_PropertiesUpdated: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                        _type.HRESULT]
