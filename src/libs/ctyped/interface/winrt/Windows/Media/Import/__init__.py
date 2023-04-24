from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import Storage as _Windows_Storage
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IPhotoImportDeleteImportedItemsFromSourceResult(_inspectable.IInspectable):
    get_Session: _Callable[[_Pointer[IPhotoImportSession]],  # value
                           _type.HRESULT]
    get_HasSucceeded: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_DeletedItems: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IPhotoImportItem]]],  # value
                                _type.HRESULT]
    get_PhotosCount: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]
    get_PhotosSizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                     _type.HRESULT]
    get_VideosCount: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]
    get_VideosSizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                     _type.HRESULT]
    get_SidecarsCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    get_SidecarsSizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                       _type.HRESULT]
    get_SiblingsCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    get_SiblingsSizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                       _type.HRESULT]
    get_TotalCount: _Callable[[_Pointer[_type.UINT32]],  # value
                              _type.HRESULT]
    get_TotalSizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                    _type.HRESULT]


class IPhotoImportFindItemsResult(_inspectable.IInspectable):
    get_Session: _Callable[[_Pointer[IPhotoImportSession]],  # value
                           _type.HRESULT]
    get_HasSucceeded: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_FoundItems: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IPhotoImportItem]]],  # value
                              _type.HRESULT]
    get_PhotosCount: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]
    get_PhotosSizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                     _type.HRESULT]
    get_VideosCount: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]
    get_VideosSizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                     _type.HRESULT]
    get_SidecarsCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    get_SidecarsSizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                       _type.HRESULT]
    get_SiblingsCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    get_SiblingsSizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                       _type.HRESULT]
    get_TotalCount: _Callable[[_Pointer[_type.UINT32]],  # value
                              _type.HRESULT]
    get_TotalSizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                    _type.HRESULT]
    SelectAll: _Callable[[],
                         _type.HRESULT]
    SelectNone: _Callable[[],
                          _type.HRESULT]
    SelectNewAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # action
                              _type.HRESULT]
    SetImportMode: _Callable[[_enum.Windows.Media.Import.PhotoImportImportMode],  # value
                             _type.HRESULT]
    get_ImportMode: _Callable[[_Pointer[_enum.Windows.Media.Import.PhotoImportImportMode]],  # value
                              _type.HRESULT]
    get_SelectedPhotosCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                       _type.HRESULT]
    get_SelectedPhotosSizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                             _type.HRESULT]
    get_SelectedVideosCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                       _type.HRESULT]
    get_SelectedVideosSizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                             _type.HRESULT]
    get_SelectedSidecarsCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                         _type.HRESULT]
    get_SelectedSidecarsSizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                               _type.HRESULT]
    get_SelectedSiblingsCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                         _type.HRESULT]
    get_SelectedSiblingsSizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                               _type.HRESULT]
    get_SelectedTotalCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                      _type.HRESULT]
    get_SelectedTotalSizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                            _type.HRESULT]
    add_SelectionChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IPhotoImportFindItemsResult, IPhotoImportSelectionChangedEventArgs],  # value
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_SelectionChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    ImportItemsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IPhotoImportImportItemsResult, _struct.Windows.Media.Import.PhotoImportProgress]]],  # operation
                                _type.HRESULT]
    add_ItemImported: _Callable[[_Windows_Foundation.ITypedEventHandler[IPhotoImportFindItemsResult, IPhotoImportItemImportedEventArgs],  # value
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_ItemImported: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]


class IPhotoImportFindItemsResult2(_inspectable.IInspectable):
    AddItemsInDateRangeToSelection: _Callable[[_struct.Windows.Foundation.DateTime,  # rangeStart
                                               _struct.Windows.Foundation.TimeSpan],  # rangeLength
                                              _type.HRESULT]


class IPhotoImportImportItemsResult(_inspectable.IInspectable):
    get_Session: _Callable[[_Pointer[IPhotoImportSession]],  # value
                           _type.HRESULT]
    get_HasSucceeded: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_ImportedItems: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IPhotoImportItem]]],  # value
                                 _type.HRESULT]
    get_PhotosCount: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]
    get_PhotosSizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                     _type.HRESULT]
    get_VideosCount: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]
    get_VideosSizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                     _type.HRESULT]
    get_SidecarsCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    get_SidecarsSizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                       _type.HRESULT]
    get_SiblingsCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    get_SiblingsSizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                       _type.HRESULT]
    get_TotalCount: _Callable[[_Pointer[_type.UINT32]],  # value
                              _type.HRESULT]
    get_TotalSizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                    _type.HRESULT]
    DeleteImportedItemsFromSourceAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IPhotoImportDeleteImportedItemsFromSourceResult, _type.DOUBLE]]],  # result
                                                  _type.HRESULT]


class IPhotoImportItem(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_ItemKey: _Callable[[_Pointer[_type.UINT64]],  # value
                           _type.HRESULT]
    get_ContentType: _Callable[[_Pointer[_enum.Windows.Media.Import.PhotoImportContentType]],  # value
                               _type.HRESULT]
    get_SizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                               _type.HRESULT]
    get_Date: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                        _type.HRESULT]
    get_Sibling: _Callable[[_Pointer[IPhotoImportSidecar]],  # value
                           _type.HRESULT]
    get_Sidecars: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IPhotoImportSidecar]]],  # value
                            _type.HRESULT]
    get_VideoSegments: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IPhotoImportVideoSegment]]],  # value
                                 _type.HRESULT]
    get_IsSelected: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    put_IsSelected: _Callable[[_type.boolean],  # value
                              _type.HRESULT]
    get_Thumbnail: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # value
                             _type.HRESULT]
    get_ImportedFileNames: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                     _type.HRESULT]
    get_DeletedFileNames: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                    _type.HRESULT]


class IPhotoImportItem2(_inspectable.IInspectable):
    get_Path: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class IPhotoImportItemImportedEventArgs(_inspectable.IInspectable):
    get_ImportedItem: _Callable[[_Pointer[IPhotoImportItem]],  # value
                                _type.HRESULT]


class IPhotoImportManagerStatics(_inspectable.IInspectable):
    IsSupportedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                _type.HRESULT]
    FindAllSourcesAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IPhotoImportSource]]]],  # operation
                                   _type.HRESULT]
    GetPendingOperations: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IPhotoImportOperation]]],  # result
                                    _type.HRESULT]

    _factory = True


class IPhotoImportOperation(_inspectable.IInspectable):
    get_Stage: _Callable[[_Pointer[_enum.Windows.Media.Import.PhotoImportStage]],  # value
                         _type.HRESULT]
    get_Session: _Callable[[_Pointer[IPhotoImportSession]],  # value
                           _type.HRESULT]
    get_ContinueFindingItemsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IPhotoImportFindItemsResult, _type.UINT32]]],  # operation
                                             _type.HRESULT]
    get_ContinueImportingItemsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IPhotoImportImportItemsResult, _struct.Windows.Media.Import.PhotoImportProgress]]],  # operation
                                               _type.HRESULT]
    get_ContinueDeletingImportedItemsFromSourceAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IPhotoImportDeleteImportedItemsFromSourceResult, _type.DOUBLE]]],  # operation
                                                                _type.HRESULT]


class IPhotoImportSelectionChangedEventArgs(_inspectable.IInspectable):
    get_IsSelectionEmpty: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]


class IPhotoImportSession(_inspectable.IInspectable):
    get_Source: _Callable[[_Pointer[IPhotoImportSource]],  # value
                          _type.HRESULT]
    get_SessionId: _Callable[[_Pointer[_struct.GUID]],  # value
                             _type.HRESULT]
    put_DestinationFolder: _Callable[[_Windows_Storage.IStorageFolder],  # value
                                     _type.HRESULT]
    get_DestinationFolder: _Callable[[_Pointer[_Windows_Storage.IStorageFolder]],  # value
                                     _type.HRESULT]
    put_AppendSessionDateToDestinationFolder: _Callable[[_type.boolean],  # value
                                                        _type.HRESULT]
    get_AppendSessionDateToDestinationFolder: _Callable[[_Pointer[_type.boolean]],  # value
                                                        _type.HRESULT]
    put_SubfolderCreationMode: _Callable[[_enum.Windows.Media.Import.PhotoImportSubfolderCreationMode],  # value
                                         _type.HRESULT]
    get_SubfolderCreationMode: _Callable[[_Pointer[_enum.Windows.Media.Import.PhotoImportSubfolderCreationMode]],  # value
                                         _type.HRESULT]
    put_DestinationFileNamePrefix: _Callable[[_type.HSTRING],  # value
                                             _type.HRESULT]
    get_DestinationFileNamePrefix: _Callable[[_Pointer[_type.HSTRING]],  # value
                                             _type.HRESULT]
    FindItemsAsync: _Callable[[_enum.Windows.Media.Import.PhotoImportContentTypeFilter,  # contentTypeFilter
                               _enum.Windows.Media.Import.PhotoImportItemSelectionMode,  # itemSelectionMode
                               _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IPhotoImportFindItemsResult, _type.UINT32]]],  # operation
                              _type.HRESULT]


class IPhotoImportSession2(_inspectable.IInspectable):
    put_SubfolderDateFormat: _Callable[[_enum.Windows.Media.Import.PhotoImportSubfolderDateFormat],  # value
                                       _type.HRESULT]
    get_SubfolderDateFormat: _Callable[[_Pointer[_enum.Windows.Media.Import.PhotoImportSubfolderDateFormat]],  # value
                                       _type.HRESULT]
    put_RememberDeselectedItems: _Callable[[_type.boolean],  # value
                                           _type.HRESULT]
    get_RememberDeselectedItems: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]


class IPhotoImportSidecar(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_SizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                               _type.HRESULT]
    get_Date: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                        _type.HRESULT]


class IPhotoImportSource(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Manufacturer: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_Model: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_SerialNumber: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_ConnectionProtocol: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_ConnectionTransport: _Callable[[_Pointer[_enum.Windows.Media.Import.PhotoImportConnectionTransport]],  # value
                                       _type.HRESULT]
    get_Type: _Callable[[_Pointer[_enum.Windows.Media.Import.PhotoImportSourceType]],  # value
                        _type.HRESULT]
    get_PowerSource: _Callable[[_Pointer[_enum.Windows.Media.Import.PhotoImportPowerSource]],  # value
                               _type.HRESULT]
    get_BatteryLevelPercent: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                                       _type.HRESULT]
    get_DateTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                            _type.HRESULT]
    get_StorageMedia: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IPhotoImportStorageMedium]]],  # value
                                _type.HRESULT]
    get_IsLocked: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.boolean]]],  # value
                            _type.HRESULT]
    get_IsMassStorage: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_Thumbnail: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # value
                             _type.HRESULT]
    CreateImportSession: _Callable[[_Pointer[IPhotoImportSession]],  # result
                                   _type.HRESULT]


class IPhotoImportSourceStatics(_inspectable.IInspectable):
    FromIdAsync: _Callable[[_type.HSTRING,  # sourceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IPhotoImportSource]]],  # operation
                           _type.HRESULT]
    FromFolderAsync: _Callable[[_Windows_Storage.IStorageFolder,  # sourceRootFolder
                                _Pointer[_Windows_Foundation.IAsyncOperation[IPhotoImportSource]]],  # operation
                               _type.HRESULT]

    _factory = True


class IPhotoImportStorageMedium(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_SerialNumber: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_StorageMediumType: _Callable[[_Pointer[_enum.Windows.Media.Import.PhotoImportStorageMediumType]],  # value
                                     _type.HRESULT]
    get_SupportedAccessMode: _Callable[[_Pointer[_enum.Windows.Media.Import.PhotoImportAccessMode]],  # value
                                       _type.HRESULT]
    get_CapacityInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                   _type.HRESULT]
    get_AvailableSpaceInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                         _type.HRESULT]
    Refresh: _Callable[[],
                       _type.HRESULT]


class IPhotoImportVideoSegment(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_SizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                               _type.HRESULT]
    get_Date: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                        _type.HRESULT]
    get_Sibling: _Callable[[_Pointer[IPhotoImportSidecar]],  # value
                           _type.HRESULT]
    get_Sidecars: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IPhotoImportSidecar]]],  # value
                            _type.HRESULT]
