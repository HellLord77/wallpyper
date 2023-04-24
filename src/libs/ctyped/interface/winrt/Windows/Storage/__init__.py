from __future__ import annotations

from typing import Callable as _Callable

from . import FileProperties as _Windows_Storage_FileProperties
from . import Streams as _Windows_Storage_Streams
from .. import Foundation as _Windows_Foundation
from .. import System as _Windows_System
from ..Foundation import Collections as _Windows_Foundation_Collections
from ... import inspectable as _inspectable
from ....um import Unknwnbase as _Unknwnbase
from ..... import enum as _enum
from ..... import struct as _struct
from ..... import type as _type
from ....._utils import _Pointer


class _IApplicationDataSetVersionHandler:
    Invoke: _Callable[[ISetVersionRequest],  # setVersionRequest
                      _type.HRESULT]


class IApplicationDataSetVersionHandler(_IApplicationDataSetVersionHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IApplicationDataSetVersionHandler_impl(_IApplicationDataSetVersionHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IStreamedFileDataRequestedHandler:
    Invoke: _Callable[[_Windows_Storage_Streams.IOutputStream],  # stream
                      _type.HRESULT]


class IStreamedFileDataRequestedHandler(_IStreamedFileDataRequestedHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IStreamedFileDataRequestedHandler_impl(_IStreamedFileDataRequestedHandler, _Unknwnbase.IUnknown_impl):
    pass


class IAppDataPaths(_inspectable.IInspectable):
    get_Cookies: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Desktop: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Documents: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_Favorites: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_History: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_InternetCache: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_LocalAppData: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_ProgramData: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_RoamingAppData: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]


class IAppDataPathsStatics(_inspectable.IInspectable):
    GetForUser: _Callable[[_Windows_System.IUser,  # user
                           _Pointer[IAppDataPaths]],  # result
                          _type.HRESULT]
    GetDefault: _Callable[[_Pointer[IAppDataPaths]],  # result
                          _type.HRESULT]

    _factory = True


class IApplicationData(_inspectable.IInspectable):
    get_Version: _Callable[[_Pointer[_type.UINT32]],  # value
                           _type.HRESULT]
    SetVersionAsync: _Callable[[_type.UINT32,  # desiredVersion
                                IApplicationDataSetVersionHandler,  # handler
                                _Pointer[_Windows_Foundation.IAsyncAction]],  # setVersionOperation
                               _type.HRESULT]
    ClearAllAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # clearOperation
                             _type.HRESULT]
    ClearAsync: _Callable[[_enum.Windows.Storage.ApplicationDataLocality,  # locality
                           _Pointer[_Windows_Foundation.IAsyncAction]],  # clearOperation
                          _type.HRESULT]
    get_LocalSettings: _Callable[[_Pointer[IApplicationDataContainer]],  # value
                                 _type.HRESULT]
    get_RoamingSettings: _Callable[[_Pointer[IApplicationDataContainer]],  # value
                                   _type.HRESULT]
    get_LocalFolder: _Callable[[_Pointer[IStorageFolder]],  # value
                               _type.HRESULT]
    get_RoamingFolder: _Callable[[_Pointer[IStorageFolder]],  # value
                                 _type.HRESULT]
    get_TemporaryFolder: _Callable[[_Pointer[IStorageFolder]],  # value
                                   _type.HRESULT]
    add_DataChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IApplicationData, _inspectable.IInspectable],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_DataChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    SignalDataChanged: _Callable[[],
                                 _type.HRESULT]
    get_RoamingStorageQuota: _Callable[[_Pointer[_type.UINT64]],  # value
                                       _type.HRESULT]


class IApplicationData2(_inspectable.IInspectable):
    get_LocalCacheFolder: _Callable[[_Pointer[IStorageFolder]],  # value
                                    _type.HRESULT]


class IApplicationData3(_inspectable.IInspectable):
    GetPublisherCacheFolder: _Callable[[_type.HSTRING,  # folderName
                                        _Pointer[IStorageFolder]],  # value
                                       _type.HRESULT]
    ClearPublisherCacheFolderAsync: _Callable[[_type.HSTRING,  # folderName
                                               _Pointer[_Windows_Foundation.IAsyncAction]],  # clearOperation
                                              _type.HRESULT]
    get_SharedLocalFolder: _Callable[[_Pointer[IStorageFolder]],  # value
                                     _type.HRESULT]


class IApplicationDataContainer(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Locality: _Callable[[_Pointer[_enum.Windows.Storage.ApplicationDataLocality]],  # value
                            _type.HRESULT]
    get_Values: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                          _type.HRESULT]
    get_Containers: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, IApplicationDataContainer]]],  # value
                              _type.HRESULT]
    CreateContainer: _Callable[[_type.HSTRING,  # name
                                _enum.Windows.Storage.ApplicationDataCreateDisposition,  # disposition
                                _Pointer[IApplicationDataContainer]],  # container
                               _type.HRESULT]
    DeleteContainer: _Callable[[_type.HSTRING],  # name
                               _type.HRESULT]


class IApplicationDataStatics(_inspectable.IInspectable):
    get_Current: _Callable[[_Pointer[IApplicationData]],  # value
                           _type.HRESULT]

    _factory = True


class IApplicationDataStatics2(_inspectable.IInspectable):
    GetForUserAsync: _Callable[[_Windows_System.IUser,  # user
                                _Pointer[_Windows_Foundation.IAsyncOperation[IApplicationData]]],  # getForUserOperation
                               _type.HRESULT]

    _factory = True


class ICachedFileManagerStatics(_inspectable.IInspectable):
    DeferUpdates: _Callable[[IStorageFile],  # file
                            _type.HRESULT]
    CompleteUpdatesAsync: _Callable[[IStorageFile,  # file
                                     _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Storage.Provider.FileUpdateStatus]]],  # operation
                                    _type.HRESULT]

    _factory = True


class IDownloadsFolderStatics(_inspectable.IInspectable):
    CreateFileAsync: _Callable[[_type.HSTRING,  # desiredName
                                _Pointer[_Windows_Foundation.IAsyncOperation[IStorageFile]]],  # operation
                               _type.HRESULT]
    CreateFolderAsync: _Callable[[_type.HSTRING,  # desiredName
                                  _Pointer[_Windows_Foundation.IAsyncOperation[IStorageFolder]]],  # operation
                                 _type.HRESULT]
    CreateFileWithCollisionOptionAsync: _Callable[[_type.HSTRING,  # desiredName
                                                   _enum.Windows.Storage.CreationCollisionOption,  # option
                                                   _Pointer[_Windows_Foundation.IAsyncOperation[IStorageFile]]],  # operation
                                                  _type.HRESULT]
    CreateFolderWithCollisionOptionAsync: _Callable[[_type.HSTRING,  # desiredName
                                                     _enum.Windows.Storage.CreationCollisionOption,  # option
                                                     _Pointer[_Windows_Foundation.IAsyncOperation[IStorageFolder]]],  # operation
                                                    _type.HRESULT]

    _factory = True


class IDownloadsFolderStatics2(_inspectable.IInspectable):
    CreateFileForUserAsync: _Callable[[_Windows_System.IUser,  # user
                                       _type.HSTRING,  # desiredName
                                       _Pointer[_Windows_Foundation.IAsyncOperation[IStorageFile]]],  # operation
                                      _type.HRESULT]
    CreateFolderForUserAsync: _Callable[[_Windows_System.IUser,  # user
                                         _type.HSTRING,  # desiredName
                                         _Pointer[_Windows_Foundation.IAsyncOperation[IStorageFolder]]],  # operation
                                        _type.HRESULT]
    CreateFileForUserWithCollisionOptionAsync: _Callable[[_Windows_System.IUser,  # user
                                                          _type.HSTRING,  # desiredName
                                                          _enum.Windows.Storage.CreationCollisionOption,  # option
                                                          _Pointer[_Windows_Foundation.IAsyncOperation[IStorageFile]]],  # operation
                                                         _type.HRESULT]
    CreateFolderForUserWithCollisionOptionAsync: _Callable[[_Windows_System.IUser,  # user
                                                            _type.HSTRING,  # desiredName
                                                            _enum.Windows.Storage.CreationCollisionOption,  # option
                                                            _Pointer[_Windows_Foundation.IAsyncOperation[IStorageFolder]]],  # operation
                                                           _type.HRESULT]

    _factory = True


class IFileIOStatics(_inspectable.IInspectable):
    ReadTextAsync: _Callable[[IStorageFile,  # file
                              _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # textOperation
                             _type.HRESULT]
    ReadTextWithEncodingAsync: _Callable[[IStorageFile,  # file
                                          _enum.Windows.Storage.Streams.UnicodeEncoding,  # encoding
                                          _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # textOperation
                                         _type.HRESULT]
    WriteTextAsync: _Callable[[IStorageFile,  # file
                               _type.HSTRING,  # contents
                               _Pointer[_Windows_Foundation.IAsyncAction]],  # textOperation
                              _type.HRESULT]
    WriteTextWithEncodingAsync: _Callable[[IStorageFile,  # file
                                           _type.HSTRING,  # contents
                                           _enum.Windows.Storage.Streams.UnicodeEncoding,  # encoding
                                           _Pointer[_Windows_Foundation.IAsyncAction]],  # textOperation
                                          _type.HRESULT]
    AppendTextAsync: _Callable[[IStorageFile,  # file
                                _type.HSTRING,  # contents
                                _Pointer[_Windows_Foundation.IAsyncAction]],  # textOperation
                               _type.HRESULT]
    AppendTextWithEncodingAsync: _Callable[[IStorageFile,  # file
                                            _type.HSTRING,  # contents
                                            _enum.Windows.Storage.Streams.UnicodeEncoding,  # encoding
                                            _Pointer[_Windows_Foundation.IAsyncAction]],  # textOperation
                                           _type.HRESULT]
    ReadLinesAsync: _Callable[[IStorageFile,  # file
                               _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVector[_type.HSTRING]]]],  # linesOperation
                              _type.HRESULT]
    ReadLinesWithEncodingAsync: _Callable[[IStorageFile,  # file
                                           _enum.Windows.Storage.Streams.UnicodeEncoding,  # encoding
                                           _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVector[_type.HSTRING]]]],  # linesOperation
                                          _type.HRESULT]
    WriteLinesAsync: _Callable[[IStorageFile,  # file
                                _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # lines
                                _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                               _type.HRESULT]
    WriteLinesWithEncodingAsync: _Callable[[IStorageFile,  # file
                                            _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # lines
                                            _enum.Windows.Storage.Streams.UnicodeEncoding,  # encoding
                                            _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                           _type.HRESULT]
    AppendLinesAsync: _Callable[[IStorageFile,  # file
                                 _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # lines
                                 _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                _type.HRESULT]
    AppendLinesWithEncodingAsync: _Callable[[IStorageFile,  # file
                                             _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # lines
                                             _enum.Windows.Storage.Streams.UnicodeEncoding,  # encoding
                                             _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                            _type.HRESULT]
    ReadBufferAsync: _Callable[[IStorageFile,  # file
                                _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IBuffer]]],  # operation
                               _type.HRESULT]
    WriteBufferAsync: _Callable[[IStorageFile,  # file
                                 _Windows_Storage_Streams.IBuffer,  # buffer
                                 _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                _type.HRESULT]
    WriteBytesAsync: _Callable[[IStorageFile,  # file
                                _type.UINT32,  # __bufferSize
                                _Pointer[_type.BYTE],  # buffer
                                _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                               _type.HRESULT]

    _factory = True


class IKnownFoldersCameraRollStatics(_inspectable.IInspectable):
    get_CameraRoll: _Callable[[_Pointer[IStorageFolder]],  # value
                              _type.HRESULT]

    _factory = True


class IKnownFoldersPlaylistsStatics(_inspectable.IInspectable):
    get_Playlists: _Callable[[_Pointer[IStorageFolder]],  # value
                             _type.HRESULT]

    _factory = True


class IKnownFoldersSavedPicturesStatics(_inspectable.IInspectable):
    get_SavedPictures: _Callable[[_Pointer[IStorageFolder]],  # value
                                 _type.HRESULT]

    _factory = True


class IKnownFoldersStatics(_inspectable.IInspectable):
    get_MusicLibrary: _Callable[[_Pointer[IStorageFolder]],  # value
                                _type.HRESULT]
    get_PicturesLibrary: _Callable[[_Pointer[IStorageFolder]],  # value
                                   _type.HRESULT]
    get_VideosLibrary: _Callable[[_Pointer[IStorageFolder]],  # value
                                 _type.HRESULT]
    get_DocumentsLibrary: _Callable[[_Pointer[IStorageFolder]],  # value
                                    _type.HRESULT]
    get_HomeGroup: _Callable[[_Pointer[IStorageFolder]],  # value
                             _type.HRESULT]
    get_RemovableDevices: _Callable[[_Pointer[IStorageFolder]],  # value
                                    _type.HRESULT]
    get_MediaServerDevices: _Callable[[_Pointer[IStorageFolder]],  # value
                                      _type.HRESULT]

    _factory = True


class IKnownFoldersStatics2(_inspectable.IInspectable):
    get_Objects3D: _Callable[[_Pointer[IStorageFolder]],  # value
                             _type.HRESULT]
    get_AppCaptures: _Callable[[_Pointer[IStorageFolder]],  # value
                               _type.HRESULT]
    get_RecordedCalls: _Callable[[_Pointer[IStorageFolder]],  # value
                                 _type.HRESULT]

    _factory = True


class IKnownFoldersStatics3(_inspectable.IInspectable):
    GetFolderForUserAsync: _Callable[[_Windows_System.IUser,  # user
                                      _enum.Windows.Storage.KnownFolderId,  # folderId
                                      _Pointer[_Windows_Foundation.IAsyncOperation[IStorageFolder]]],  # operation
                                     _type.HRESULT]

    _factory = True


class IKnownFoldersStatics4(_inspectable.IInspectable):
    RequestAccessAsync: _Callable[[_enum.Windows.Storage.KnownFolderId,  # folderId
                                   _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Storage.KnownFoldersAccessStatus]]],  # operation
                                  _type.HRESULT]
    RequestAccessForUserAsync: _Callable[[_Windows_System.IUser,  # user
                                          _enum.Windows.Storage.KnownFolderId,  # folderId
                                          _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Storage.KnownFoldersAccessStatus]]],  # operation
                                         _type.HRESULT]
    GetFolderAsync: _Callable[[_enum.Windows.Storage.KnownFolderId,  # folderId
                               _Pointer[_Windows_Foundation.IAsyncOperation[IStorageFolder]]],  # operation
                              _type.HRESULT]

    _factory = True


class IPathIOStatics(_inspectable.IInspectable):
    ReadTextAsync: _Callable[[_type.HSTRING,  # absolutePath
                              _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # textOperation
                             _type.HRESULT]
    ReadTextWithEncodingAsync: _Callable[[_type.HSTRING,  # absolutePath
                                          _enum.Windows.Storage.Streams.UnicodeEncoding,  # encoding
                                          _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # textOperation
                                         _type.HRESULT]
    WriteTextAsync: _Callable[[_type.HSTRING,  # absolutePath
                               _type.HSTRING,  # contents
                               _Pointer[_Windows_Foundation.IAsyncAction]],  # textOperation
                              _type.HRESULT]
    WriteTextWithEncodingAsync: _Callable[[_type.HSTRING,  # absolutePath
                                           _type.HSTRING,  # contents
                                           _enum.Windows.Storage.Streams.UnicodeEncoding,  # encoding
                                           _Pointer[_Windows_Foundation.IAsyncAction]],  # textOperation
                                          _type.HRESULT]
    AppendTextAsync: _Callable[[_type.HSTRING,  # absolutePath
                                _type.HSTRING,  # contents
                                _Pointer[_Windows_Foundation.IAsyncAction]],  # textOperation
                               _type.HRESULT]
    AppendTextWithEncodingAsync: _Callable[[_type.HSTRING,  # absolutePath
                                            _type.HSTRING,  # contents
                                            _enum.Windows.Storage.Streams.UnicodeEncoding,  # encoding
                                            _Pointer[_Windows_Foundation.IAsyncAction]],  # textOperation
                                           _type.HRESULT]
    ReadLinesAsync: _Callable[[_type.HSTRING,  # absolutePath
                               _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVector[_type.HSTRING]]]],  # linesOperation
                              _type.HRESULT]
    ReadLinesWithEncodingAsync: _Callable[[_type.HSTRING,  # absolutePath
                                           _enum.Windows.Storage.Streams.UnicodeEncoding,  # encoding
                                           _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVector[_type.HSTRING]]]],  # linesOperation
                                          _type.HRESULT]
    WriteLinesAsync: _Callable[[_type.HSTRING,  # absolutePath
                                _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # lines
                                _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                               _type.HRESULT]
    WriteLinesWithEncodingAsync: _Callable[[_type.HSTRING,  # absolutePath
                                            _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # lines
                                            _enum.Windows.Storage.Streams.UnicodeEncoding,  # encoding
                                            _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                           _type.HRESULT]
    AppendLinesAsync: _Callable[[_type.HSTRING,  # absolutePath
                                 _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # lines
                                 _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                _type.HRESULT]
    AppendLinesWithEncodingAsync: _Callable[[_type.HSTRING,  # absolutePath
                                             _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # lines
                                             _enum.Windows.Storage.Streams.UnicodeEncoding,  # encoding
                                             _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                            _type.HRESULT]
    ReadBufferAsync: _Callable[[_type.HSTRING,  # absolutePath
                                _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IBuffer]]],  # operation
                               _type.HRESULT]
    WriteBufferAsync: _Callable[[_type.HSTRING,  # absolutePath
                                 _Windows_Storage_Streams.IBuffer,  # buffer
                                 _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                _type.HRESULT]
    WriteBytesAsync: _Callable[[_type.HSTRING,  # absolutePath
                                _type.UINT32,  # __bufferSize
                                _Pointer[_type.BYTE],  # buffer
                                _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                               _type.HRESULT]

    _factory = True


class ISetVersionDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class ISetVersionRequest(_inspectable.IInspectable):
    get_CurrentVersion: _Callable[[_Pointer[_type.UINT32]],  # currentVersion
                                  _type.HRESULT]
    get_DesiredVersion: _Callable[[_Pointer[_type.UINT32]],  # desiredVersion
                                  _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[ISetVersionDeferral]],  # deferral
                           _type.HRESULT]


class IStorageFile(_inspectable.IInspectable):
    get_FileType: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_ContentType: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    OpenAsync: _Callable[[_enum.Windows.Storage.FileAccessMode,  # accessMode
                          _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStream]]],  # operation
                         _type.HRESULT]
    OpenTransactedWriteAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IStorageStreamTransaction]]],  # operation
                                        _type.HRESULT]
    CopyOverloadDefaultNameAndOptions: _Callable[[IStorageFolder,  # destinationFolder
                                                  _Pointer[_Windows_Foundation.IAsyncOperation[IStorageFile]]],  # operation
                                                 _type.HRESULT]
    CopyOverloadDefaultOptions: _Callable[[IStorageFolder,  # destinationFolder
                                           _type.HSTRING,  # desiredNewName
                                           _Pointer[_Windows_Foundation.IAsyncOperation[IStorageFile]]],  # operation
                                          _type.HRESULT]
    CopyOverload: _Callable[[IStorageFolder,  # destinationFolder
                             _type.HSTRING,  # desiredNewName
                             _enum.Windows.Storage.NameCollisionOption,  # option
                             _Pointer[_Windows_Foundation.IAsyncOperation[IStorageFile]]],  # operation
                            _type.HRESULT]
    CopyAndReplaceAsync: _Callable[[IStorageFile,  # fileToReplace
                                    _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                   _type.HRESULT]
    MoveOverloadDefaultNameAndOptions: _Callable[[IStorageFolder,  # destinationFolder
                                                  _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                                 _type.HRESULT]
    MoveOverloadDefaultOptions: _Callable[[IStorageFolder,  # destinationFolder
                                           _type.HSTRING,  # desiredNewName
                                           _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                          _type.HRESULT]
    MoveOverload: _Callable[[IStorageFolder,  # destinationFolder
                             _type.HSTRING,  # desiredNewName
                             _enum.Windows.Storage.NameCollisionOption,  # option
                             _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                            _type.HRESULT]
    MoveAndReplaceAsync: _Callable[[IStorageFile,  # fileToReplace
                                    _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                   _type.HRESULT]


class IStorageFile2(_inspectable.IInspectable):
    OpenWithOptionsAsync: _Callable[[_enum.Windows.Storage.FileAccessMode,  # accessMode
                                     _enum.Windows.Storage.StorageOpenOptions,  # options
                                     _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStream]]],  # operation
                                    _type.HRESULT]
    OpenTransactedWriteWithOptionsAsync: _Callable[[_enum.Windows.Storage.StorageOpenOptions,  # options
                                                    _Pointer[_Windows_Foundation.IAsyncOperation[IStorageStreamTransaction]]],  # operation
                                                   _type.HRESULT]


class IStorageFilePropertiesWithAvailability(_inspectable.IInspectable):
    get_IsAvailable: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]


class IStorageFileStatics(_inspectable.IInspectable):
    GetFileFromPathAsync: _Callable[[_type.HSTRING,  # path
                                     _Pointer[_Windows_Foundation.IAsyncOperation[IStorageFile]]],  # operation
                                    _type.HRESULT]
    GetFileFromApplicationUriAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                               _Pointer[_Windows_Foundation.IAsyncOperation[IStorageFile]]],  # operation
                                              _type.HRESULT]
    CreateStreamedFileAsync: _Callable[[_type.HSTRING,  # displayNameWithExtension
                                        IStreamedFileDataRequestedHandler,  # dataRequested
                                        _Windows_Storage_Streams.IRandomAccessStreamReference,  # thumbnail
                                        _Pointer[_Windows_Foundation.IAsyncOperation[IStorageFile]]],  # operation
                                       _type.HRESULT]
    ReplaceWithStreamedFileAsync: _Callable[[IStorageFile,  # fileToReplace
                                             IStreamedFileDataRequestedHandler,  # dataRequested
                                             _Windows_Storage_Streams.IRandomAccessStreamReference,  # thumbnail
                                             _Pointer[_Windows_Foundation.IAsyncOperation[IStorageFile]]],  # operation
                                            _type.HRESULT]
    CreateStreamedFileFromUriAsync: _Callable[[_type.HSTRING,  # displayNameWithExtension
                                               _Windows_Foundation.IUriRuntimeClass,  # uri
                                               _Windows_Storage_Streams.IRandomAccessStreamReference,  # thumbnail
                                               _Pointer[_Windows_Foundation.IAsyncOperation[IStorageFile]]],  # operation
                                              _type.HRESULT]
    ReplaceWithStreamedFileFromUriAsync: _Callable[[IStorageFile,  # fileToReplace
                                                    _Windows_Foundation.IUriRuntimeClass,  # uri
                                                    _Windows_Storage_Streams.IRandomAccessStreamReference,  # thumbnail
                                                    _Pointer[_Windows_Foundation.IAsyncOperation[IStorageFile]]],  # operation
                                                   _type.HRESULT]

    _factory = True


class IStorageFileStatics2(_inspectable.IInspectable):
    GetFileFromPathForUserAsync: _Callable[[_Windows_System.IUser,  # user
                                            _type.HSTRING,  # path
                                            _Pointer[_Windows_Foundation.IAsyncOperation[IStorageFile]]],  # operation
                                           _type.HRESULT]

    _factory = True


class IStorageFolder(_inspectable.IInspectable):
    CreateFileAsyncOverloadDefaultOptions: _Callable[[_type.HSTRING,  # desiredName
                                                      _Pointer[_Windows_Foundation.IAsyncOperation[IStorageFile]]],  # operation
                                                     _type.HRESULT]
    CreateFileAsync: _Callable[[_type.HSTRING,  # desiredName
                                _enum.Windows.Storage.CreationCollisionOption,  # options
                                _Pointer[_Windows_Foundation.IAsyncOperation[IStorageFile]]],  # operation
                               _type.HRESULT]
    CreateFolderAsyncOverloadDefaultOptions: _Callable[[_type.HSTRING,  # desiredName
                                                        _Pointer[_Windows_Foundation.IAsyncOperation[IStorageFolder]]],  # operation
                                                       _type.HRESULT]
    CreateFolderAsync: _Callable[[_type.HSTRING,  # desiredName
                                  _enum.Windows.Storage.CreationCollisionOption,  # options
                                  _Pointer[_Windows_Foundation.IAsyncOperation[IStorageFolder]]],  # operation
                                 _type.HRESULT]
    GetFileAsync: _Callable[[_type.HSTRING,  # name
                             _Pointer[_Windows_Foundation.IAsyncOperation[IStorageFile]]],  # operation
                            _type.HRESULT]
    GetFolderAsync: _Callable[[_type.HSTRING,  # name
                               _Pointer[_Windows_Foundation.IAsyncOperation[IStorageFolder]]],  # operation
                              _type.HRESULT]
    GetItemAsync: _Callable[[_type.HSTRING,  # name
                             _Pointer[_Windows_Foundation.IAsyncOperation[IStorageItem]]],  # operation
                            _type.HRESULT]
    GetFilesAsyncOverloadDefaultOptionsStartAndCount: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IStorageFile]]]],  # operation
                                                                _type.HRESULT]
    GetFoldersAsyncOverloadDefaultOptionsStartAndCount: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IStorageFolder]]]],  # operation
                                                                  _type.HRESULT]
    GetItemsAsyncOverloadDefaultStartAndCount: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IStorageItem]]]],  # operation
                                                         _type.HRESULT]


class IStorageFolder2(_inspectable.IInspectable):
    TryGetItemAsync: _Callable[[_type.HSTRING,  # name
                                _Pointer[_Windows_Foundation.IAsyncOperation[IStorageItem]]],  # operation
                               _type.HRESULT]


class IStorageFolder3(_inspectable.IInspectable):
    TryGetChangeTracker: _Callable[[_Pointer[IStorageLibraryChangeTracker]],  # result
                                   _type.HRESULT]


class IStorageFolderStatics(_inspectable.IInspectable):
    GetFolderFromPathAsync: _Callable[[_type.HSTRING,  # path
                                       _Pointer[_Windows_Foundation.IAsyncOperation[IStorageFolder]]],  # operation
                                      _type.HRESULT]

    _factory = True


class IStorageFolderStatics2(_inspectable.IInspectable):
    GetFolderFromPathForUserAsync: _Callable[[_Windows_System.IUser,  # user
                                              _type.HSTRING,  # path
                                              _Pointer[_Windows_Foundation.IAsyncOperation[IStorageFolder]]],  # operation
                                             _type.HRESULT]

    _factory = True


class IStorageItem(_inspectable.IInspectable):
    RenameAsyncOverloadDefaultOptions: _Callable[[_type.HSTRING,  # desiredName
                                                  _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                                 _type.HRESULT]
    RenameAsync: _Callable[[_type.HSTRING,  # desiredName
                            _enum.Windows.Storage.NameCollisionOption,  # option
                            _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                           _type.HRESULT]
    DeleteAsyncOverloadDefaultOptions: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                                 _type.HRESULT]
    DeleteAsync: _Callable[[_enum.Windows.Storage.StorageDeleteOption,  # option
                            _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                           _type.HRESULT]
    GetBasicPropertiesAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_FileProperties.IBasicProperties]]],  # operation
                                       _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Path: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Attributes: _Callable[[_Pointer[_enum.Windows.Storage.FileAttributes]],  # value
                              _type.HRESULT]
    get_DateCreated: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                               _type.HRESULT]
    IsOfType: _Callable[[_enum.Windows.Storage.StorageItemTypes,  # type
                         _Pointer[_type.boolean]],  # value
                        _type.HRESULT]


class IStorageItem2(_inspectable.IInspectable):
    GetParentAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IStorageFolder]]],  # operation
                              _type.HRESULT]
    IsEqual: _Callable[[IStorageItem,  # item
                        _Pointer[_type.boolean]],  # value
                       _type.HRESULT]


class IStorageItemProperties(_inspectable.IInspectable):
    GetThumbnailAsyncOverloadDefaultSizeDefaultOptions: _Callable[[_enum.Windows.Storage.FileProperties.ThumbnailMode,  # mode
                                                                   _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStreamWithContentType]]],  # operation
                                                                  _type.HRESULT]
    GetThumbnailAsyncOverloadDefaultOptions: _Callable[[_enum.Windows.Storage.FileProperties.ThumbnailMode,  # mode
                                                        _type.UINT32,  # requestedSize
                                                        _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStreamWithContentType]]],  # operation
                                                       _type.HRESULT]
    GetThumbnailAsync: _Callable[[_enum.Windows.Storage.FileProperties.ThumbnailMode,  # mode
                                  _type.UINT32,  # requestedSize
                                  _enum.Windows.Storage.FileProperties.ThumbnailOptions,  # options
                                  _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStreamWithContentType]]],  # operation
                                 _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_DisplayType: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_FolderRelativeId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Storage_FileProperties.IStorageItemContentProperties]],  # value
                              _type.HRESULT]


class IStorageItemProperties2(_inspectable.IInspectable):
    GetScaledImageAsThumbnailAsyncOverloadDefaultSizeDefaultOptions: _Callable[[_enum.Windows.Storage.FileProperties.ThumbnailMode,  # mode
                                                                                _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStreamWithContentType]]],  # operation
                                                                               _type.HRESULT]
    GetScaledImageAsThumbnailAsyncOverloadDefaultOptions: _Callable[[_enum.Windows.Storage.FileProperties.ThumbnailMode,  # mode
                                                                     _type.UINT32,  # requestedSize
                                                                     _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStreamWithContentType]]],  # operation
                                                                    _type.HRESULT]
    GetScaledImageAsThumbnailAsync: _Callable[[_enum.Windows.Storage.FileProperties.ThumbnailMode,  # mode
                                               _type.UINT32,  # requestedSize
                                               _enum.Windows.Storage.FileProperties.ThumbnailOptions,  # options
                                               _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStreamWithContentType]]],  # operation
                                              _type.HRESULT]


class IStorageItemPropertiesWithProvider(_inspectable.IInspectable):
    get_Provider: _Callable[[_Pointer[IStorageProvider]],  # value
                            _type.HRESULT]


class IStorageLibrary(_inspectable.IInspectable):
    RequestAddFolderAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IStorageFolder]]],  # operation
                                     _type.HRESULT]
    RequestRemoveFolderAsync: _Callable[[IStorageFolder,  # folder
                                         _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                        _type.HRESULT]
    get_Folders: _Callable[[_Pointer[_Windows_Foundation_Collections.IObservableVector[IStorageFolder]]],  # value
                           _type.HRESULT]
    get_SaveFolder: _Callable[[_Pointer[IStorageFolder]],  # value
                              _type.HRESULT]
    add_DefinitionChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IStorageLibrary, _inspectable.IInspectable],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                                     _type.HRESULT]
    remove_DefinitionChanged: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                        _type.HRESULT]


class IStorageLibrary2(_inspectable.IInspectable):
    get_ChangeTracker: _Callable[[_Pointer[IStorageLibraryChangeTracker]],  # value
                                 _type.HRESULT]


class IStorageLibrary3(_inspectable.IInspectable):
    AreFolderSuggestionsAvailableAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                                  _type.HRESULT]


class IStorageLibraryChange(_inspectable.IInspectable):
    get_ChangeType: _Callable[[_Pointer[_enum.Windows.Storage.StorageLibraryChangeType]],  # value
                              _type.HRESULT]
    get_Path: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_PreviousPath: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    IsOfType: _Callable[[_enum.Windows.Storage.StorageItemTypes,  # type
                         _Pointer[_type.boolean]],  # value
                        _type.HRESULT]
    GetStorageItemAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IStorageItem]]],  # operation
                                   _type.HRESULT]


class IStorageLibraryChangeReader(_inspectable.IInspectable):
    ReadBatchAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IStorageLibraryChange]]]],  # operation
                              _type.HRESULT]
    AcceptChangesAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                  _type.HRESULT]


class IStorageLibraryChangeReader2(_inspectable.IInspectable):
    GetLastChangeId: _Callable[[_Pointer[_type.UINT64]],  # result
                               _type.HRESULT]


class IStorageLibraryChangeTracker(_inspectable.IInspectable):
    GetChangeReader: _Callable[[_Pointer[IStorageLibraryChangeReader]],  # value
                               _type.HRESULT]
    Enable: _Callable[[],
                      _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]


class IStorageLibraryChangeTracker2(_inspectable.IInspectable):
    EnableWithOptions: _Callable[[IStorageLibraryChangeTrackerOptions],  # options
                                 _type.HRESULT]
    Disable: _Callable[[],
                       _type.HRESULT]


class IStorageLibraryChangeTrackerOptions(_inspectable.IInspectable):
    get_TrackChangeDetails: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_TrackChangeDetails: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]


class IStorageLibraryLastChangeId(_inspectable.IInspectable):
    pass


class IStorageLibraryLastChangeIdStatics(_inspectable.IInspectable):
    get_Unknown: _Callable[[_Pointer[_type.UINT64]],  # value
                           _type.HRESULT]

    _factory = True


class IStorageLibraryStatics(_inspectable.IInspectable):
    GetLibraryAsync: _Callable[[_enum.Windows.Storage.KnownLibraryId,  # libraryId
                                _Pointer[_Windows_Foundation.IAsyncOperation[IStorageLibrary]]],  # operation
                               _type.HRESULT]

    _factory = True


class IStorageLibraryStatics2(_inspectable.IInspectable):
    GetLibraryForUserAsync: _Callable[[_Windows_System.IUser,  # user
                                       _enum.Windows.Storage.KnownLibraryId,  # libraryId
                                       _Pointer[_Windows_Foundation.IAsyncOperation[IStorageLibrary]]],  # operation
                                      _type.HRESULT]

    _factory = True


class IStorageProvider(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class IStorageProvider2(_inspectable.IInspectable):
    IsPropertySupportedForPartialFileAsync: _Callable[[_type.HSTRING,  # propertyCanonicalName
                                                       _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                                      _type.HRESULT]


class IStorageStreamTransaction(_inspectable.IInspectable):
    get_Stream: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStream]],  # value
                          _type.HRESULT]
    CommitAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                           _type.HRESULT]


class IStreamedFileDataRequest(_inspectable.IInspectable):
    FailAndClose: _Callable[[_enum.Windows.Storage.StreamedFileFailureMode],  # failureMode
                            _type.HRESULT]


class ISystemAudioProperties(_inspectable.IInspectable):
    get_EncodingBitrate: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]


class ISystemDataPaths(_inspectable.IInspectable):
    get_Fonts: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_ProgramData: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Public: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_PublicDesktop: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_PublicDocuments: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_PublicDownloads: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_PublicMusic: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_PublicPictures: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_PublicVideos: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_System: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_SystemHost: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_SystemX86: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_SystemX64: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_SystemArm: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_UserProfiles: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_Windows: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]


class ISystemDataPathsStatics(_inspectable.IInspectable):
    GetDefault: _Callable[[_Pointer[ISystemDataPaths]],  # result
                          _type.HRESULT]

    _factory = True


class ISystemGPSProperties(_inspectable.IInspectable):
    get_LatitudeDecimal: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_LongitudeDecimal: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]


class ISystemImageProperties(_inspectable.IInspectable):
    get_HorizontalSize: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_VerticalSize: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]


class ISystemMediaProperties(_inspectable.IInspectable):
    get_Duration: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Producer: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Publisher: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_SubTitle: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Writer: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Year: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class ISystemMusicProperties(_inspectable.IInspectable):
    get_AlbumArtist: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_AlbumTitle: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_Artist: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Composer: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Conductor: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_DisplayArtist: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_Genre: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_TrackNumber: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class ISystemPhotoProperties(_inspectable.IInspectable):
    get_CameraManufacturer: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_CameraModel: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_DateTaken: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_Orientation: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_PeopleNames: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class ISystemProperties(_inspectable.IInspectable):
    get_Author: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Comment: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_ItemNameDisplay: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_Keywords: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Rating: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Audio: _Callable[[_Pointer[ISystemAudioProperties]],  # value
                         _type.HRESULT]
    get_GPS: _Callable[[_Pointer[ISystemGPSProperties]],  # value
                       _type.HRESULT]
    get_Media: _Callable[[_Pointer[ISystemMediaProperties]],  # value
                         _type.HRESULT]
    get_Music: _Callable[[_Pointer[ISystemMusicProperties]],  # value
                         _type.HRESULT]
    get_Photo: _Callable[[_Pointer[ISystemPhotoProperties]],  # value
                         _type.HRESULT]
    get_Video: _Callable[[_Pointer[ISystemVideoProperties]],  # value
                         _type.HRESULT]
    get_Image: _Callable[[_Pointer[ISystemImageProperties]],  # value
                         _type.HRESULT]

    _factory = True


class ISystemVideoProperties(_inspectable.IInspectable):
    get_Director: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_FrameHeight: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_FrameWidth: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_Orientation: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_TotalBitrate: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]


class IUserDataPaths(_inspectable.IInspectable):
    get_CameraRoll: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_Cookies: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Desktop: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Documents: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_Downloads: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_Favorites: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_History: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_InternetCache: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_LocalAppData: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_LocalAppDataLow: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_Music: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Pictures: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Profile: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Recent: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_RoamingAppData: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_SavedPictures: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_Screenshots: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Templates: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_Videos: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]


class IUserDataPathsStatics(_inspectable.IInspectable):
    GetForUser: _Callable[[_Windows_System.IUser,  # user
                           _Pointer[IUserDataPaths]],  # result
                          _type.HRESULT]
    GetDefault: _Callable[[_Pointer[IUserDataPaths]],  # result
                          _type.HRESULT]

    _factory = True
