from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import Storage as _Windows_Storage
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import type as _type
from ......_utils import _Pointer


class IPlaylist(_inspectable.IInspectable):
    get_Files: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_Storage.IStorageFile]]],  # value
                         _type.HRESULT]
    SaveAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                         _type.HRESULT]
    SaveAsAsync: _Callable[[_Windows_Storage.IStorageFolder,  # saveLocation
                            _type.HSTRING,  # desiredName
                            _enum.Windows.Storage.NameCollisionOption,  # option
                            _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage.IStorageFile]]],  # operation
                           _type.HRESULT]
    SaveAsWithFormatAsync: _Callable[[_Windows_Storage.IStorageFolder,  # saveLocation
                                      _type.HSTRING,  # desiredName
                                      _enum.Windows.Storage.NameCollisionOption,  # option
                                      _enum.Windows.Media.Playlists.PlaylistFormat,  # playlistFormat
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage.IStorageFile]]],  # operation
                                     _type.HRESULT]


class IPlaylistStatics(_inspectable.IInspectable):
    LoadAsync: _Callable[[_Windows_Storage.IStorageFile,  # file
                          _Pointer[_Windows_Foundation.IAsyncOperation[IPlaylist]]],  # operation
                         _type.HRESULT]

    _factory = True
