from __future__ import annotations as _

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from .... import System as _Windows_System
from ....Foundation import Collections as _Windows_Foundation_Collections
from ....Storage import Streams as _Windows_Storage_Streams
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IGameSaveBlobGetResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Gaming.XboxLive.Storage.GameSaveErrorStatus]],  # value
                          _type.HRESULT]
    get_Value: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _Windows_Storage_Streams.IBuffer]]],  # value
                         _type.HRESULT]


class IGameSaveBlobInfo(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Size: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]


class IGameSaveBlobInfoGetResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Gaming.XboxLive.Storage.GameSaveErrorStatus]],  # value
                          _type.HRESULT]
    get_Value: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IGameSaveBlobInfo]]],  # value
                         _type.HRESULT]


class IGameSaveBlobInfoQuery(_inspectable.IInspectable):
    GetBlobInfoAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IGameSaveBlobInfoGetResult]]],  # operation
                                _type.HRESULT]
    GetBlobInfoWithIndexAndMaxAsync: _Callable[[_type.UINT32,  # startIndex
                                                _type.UINT32,  # maxNumberOfItems
                                                _Pointer[_Windows_Foundation.IAsyncOperation[IGameSaveBlobInfoGetResult]]],  # operation
                                               _type.HRESULT]
    GetItemCountAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.UINT32]]],  # operation
                                 _type.HRESULT]


class IGameSaveContainer(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Provider: _Callable[[_Pointer[IGameSaveProvider]],  # value
                            _type.HRESULT]
    SubmitUpdatesAsync: _Callable[[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _Windows_Storage_Streams.IBuffer],  # blobsToWrite
                                   _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # blobsToDelete
                                   _type.HSTRING,  # displayName
                                   _Pointer[_Windows_Foundation.IAsyncOperation[IGameSaveOperationResult]]],  # operation
                                  _type.HRESULT]
    ReadAsync: _Callable[[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _Windows_Storage_Streams.IBuffer],  # blobsToRead
                          _Pointer[_Windows_Foundation.IAsyncOperation[IGameSaveOperationResult]]],  # action
                         _type.HRESULT]
    GetAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # blobsToRead
                         _Pointer[_Windows_Foundation.IAsyncOperation[IGameSaveBlobGetResult]]],  # operation
                        _type.HRESULT]
    SubmitPropertySetUpdatesAsync: _Callable[[_Windows_Foundation_Collections.IPropertySet,  # blobsToWrite
                                              _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # blobsToDelete
                                              _type.HSTRING,  # displayName
                                              _Pointer[_Windows_Foundation.IAsyncOperation[IGameSaveOperationResult]]],  # operation
                                             _type.HRESULT]
    CreateBlobInfoQuery: _Callable[[_type.HSTRING,  # blobNamePrefix
                                    _Pointer[IGameSaveBlobInfoQuery]],  # query
                                   _type.HRESULT]


class IGameSaveContainerInfo(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_TotalSize: _Callable[[_Pointer[_type.UINT64]],  # value
                             _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_LastModifiedTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                    _type.HRESULT]
    get_NeedsSync: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]


class IGameSaveContainerInfoGetResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Gaming.XboxLive.Storage.GameSaveErrorStatus]],  # value
                          _type.HRESULT]
    get_Value: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IGameSaveContainerInfo]]],  # value
                         _type.HRESULT]


class IGameSaveContainerInfoQuery(_inspectable.IInspectable):
    GetContainerInfoAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IGameSaveContainerInfoGetResult]]],  # operation
                                     _type.HRESULT]
    GetContainerInfoWithIndexAndMaxAsync: _Callable[[_type.UINT32,  # startIndex
                                                     _type.UINT32,  # maxNumberOfItems
                                                     _Pointer[_Windows_Foundation.IAsyncOperation[IGameSaveContainerInfoGetResult]]],  # operation
                                                    _type.HRESULT]
    GetItemCountAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.UINT32]]],  # operation
                                 _type.HRESULT]


class IGameSaveOperationResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Gaming.XboxLive.Storage.GameSaveErrorStatus]],  # value
                          _type.HRESULT]


class IGameSaveProvider(_inspectable.IInspectable):
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]
    CreateContainer: _Callable[[_type.HSTRING,  # name
                                _Pointer[IGameSaveContainer]],  # result
                               _type.HRESULT]
    DeleteContainerAsync: _Callable[[_type.HSTRING,  # name
                                     _Pointer[_Windows_Foundation.IAsyncOperation[IGameSaveOperationResult]]],  # action
                                    _type.HRESULT]
    CreateContainerInfoQuery: _Callable[[_Pointer[IGameSaveContainerInfoQuery]],  # query
                                        _type.HRESULT]
    CreateContainerInfoQueryWithName: _Callable[[_type.HSTRING,  # containerNamePrefix
                                                 _Pointer[IGameSaveContainerInfoQuery]],  # query
                                                _type.HRESULT]
    GetRemainingBytesInQuotaAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.INT64]]],  # operation
                                             _type.HRESULT]
    get_ContainersChangedSinceLastSync: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                                  _type.HRESULT]


class IGameSaveProviderGetResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Gaming.XboxLive.Storage.GameSaveErrorStatus]],  # value
                          _type.HRESULT]
    get_Value: _Callable[[_Pointer[IGameSaveProvider]],  # value
                         _type.HRESULT]


class IGameSaveProviderStatics(_inspectable.IInspectable):
    GetForUserAsync: _Callable[[_Windows_System.IUser,  # user
                                _type.HSTRING,  # serviceConfigId
                                _Pointer[_Windows_Foundation.IAsyncOperation[IGameSaveProviderGetResult]]],  # operation
                               _type.HRESULT]
    GetSyncOnDemandForUserAsync: _Callable[[_Windows_System.IUser,  # user
                                            _type.HSTRING,  # serviceConfigId
                                            _Pointer[_Windows_Foundation.IAsyncOperation[IGameSaveProviderGetResult]]],  # operation
                                           _type.HRESULT]

    _factory = True
