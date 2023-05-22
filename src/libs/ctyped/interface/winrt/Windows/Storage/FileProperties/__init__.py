from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import Storage as _Windows_Storage
from ...Devices import Geolocation as _Windows_Devices_Geolocation
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IBasicProperties(_inspectable.IInspectable):
    get_Size: _Callable[[_Pointer[_type.UINT64]],  # value
                        _type.HRESULT]
    get_DateModified: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                _type.HRESULT]
    get_ItemDate: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                            _type.HRESULT]


class IDocumentProperties(_inspectable.IInspectable):
    get_Author: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                          _type.HRESULT]
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Title: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Keywords: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                            _type.HRESULT]
    get_Comment: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    put_Comment: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]


class IGeotagHelperStatics(_inspectable.IInspectable, factory=True):
    GetGeotagAsync: _Callable[[_Windows_Storage.IStorageFile,  # file
                               _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Devices_Geolocation.IGeopoint]]],  # operation
                              _type.HRESULT]
    SetGeotagFromGeolocatorAsync: _Callable[[_Windows_Storage.IStorageFile,  # file
                                             _Windows_Devices_Geolocation.IGeolocator,  # geolocator
                                             _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                            _type.HRESULT]
    SetGeotagAsync: _Callable[[_Windows_Storage.IStorageFile,  # file
                               _Windows_Devices_Geolocation.IGeopoint,  # geopoint
                               _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                              _type.HRESULT]


class IImageProperties(_inspectable.IInspectable):
    get_Rating: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    put_Rating: _Callable[[_type.UINT32],  # value
                          _type.HRESULT]
    get_Keywords: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                            _type.HRESULT]
    get_DateTaken: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    put_DateTaken: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                             _type.HRESULT]
    get_Width: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    get_Height: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Title: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Latitude: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                            _type.HRESULT]
    get_Longitude: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                             _type.HRESULT]
    get_CameraManufacturer: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    put_CameraManufacturer: _Callable[[_type.HSTRING],  # value
                                      _type.HRESULT]
    get_CameraModel: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_CameraModel: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_Orientation: _Callable[[_Pointer[_enum.Windows.Storage.FileProperties.PhotoOrientation]],  # value
                               _type.HRESULT]
    get_PeopleNames: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                               _type.HRESULT]


class IMusicProperties(_inspectable.IInspectable):
    get_Album: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Album: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Artist: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    put_Artist: _Callable[[_type.HSTRING],  # value
                          _type.HRESULT]
    get_Genre: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                         _type.HRESULT]
    get_TrackNumber: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]
    put_TrackNumber: _Callable[[_type.UINT32],  # value
                               _type.HRESULT]
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Title: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Rating: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    put_Rating: _Callable[[_type.UINT32],  # value
                          _type.HRESULT]
    get_Duration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    get_Bitrate: _Callable[[_Pointer[_type.UINT32]],  # value
                           _type.HRESULT]
    get_AlbumArtist: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_AlbumArtist: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_Composers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                             _type.HRESULT]
    get_Conductors: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                              _type.HRESULT]
    get_Subtitle: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_Subtitle: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_Producers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                             _type.HRESULT]
    get_Publisher: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_Publisher: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_Writers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                           _type.HRESULT]
    get_Year: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]
    put_Year: _Callable[[_type.UINT32],  # value
                        _type.HRESULT]


class IStorageItemContentProperties(_inspectable.IInspectable):
    GetMusicPropertiesAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IMusicProperties]]],  # operation
                                       _type.HRESULT]
    GetVideoPropertiesAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IVideoProperties]]],  # operation
                                       _type.HRESULT]
    GetImagePropertiesAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IImageProperties]]],  # operation
                                       _type.HRESULT]
    GetDocumentPropertiesAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IDocumentProperties]]],  # operation
                                          _type.HRESULT]


class IStorageItemExtraProperties(_inspectable.IInspectable):
    RetrievePropertiesAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # propertiesToRetrieve
                                        _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IMap[_type.HSTRING, _inspectable.IInspectable]]]],  # operation
                                       _type.HRESULT]
    SavePropertiesAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Foundation_Collections.IKeyValuePair[_type.HSTRING, _inspectable.IInspectable]],  # propertiesToSave
                                    _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                   _type.HRESULT]
    SavePropertiesAsyncOverloadDefault: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                                  _type.HRESULT]


class IThumbnailProperties(_inspectable.IInspectable):
    get_OriginalWidth: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    get_OriginalHeight: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]
    get_ReturnedSmallerCachedSize: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    get_Type: _Callable[[_Pointer[_enum.Windows.Storage.FileProperties.ThumbnailType]],  # value
                        _type.HRESULT]


class IVideoProperties(_inspectable.IInspectable):
    get_Rating: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    put_Rating: _Callable[[_type.UINT32],  # value
                          _type.HRESULT]
    get_Keywords: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                            _type.HRESULT]
    get_Width: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    get_Height: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    get_Duration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    get_Latitude: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                            _type.HRESULT]
    get_Longitude: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                             _type.HRESULT]
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Title: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Subtitle: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_Subtitle: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_Producers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                             _type.HRESULT]
    get_Publisher: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_Publisher: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_Writers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                           _type.HRESULT]
    get_Year: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]
    put_Year: _Callable[[_type.UINT32],  # value
                        _type.HRESULT]
    get_Bitrate: _Callable[[_Pointer[_type.UINT32]],  # value
                           _type.HRESULT]
    get_Directors: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                             _type.HRESULT]
    get_Orientation: _Callable[[_Pointer[_enum.Windows.Storage.FileProperties.VideoOrientation]],  # value
                               _type.HRESULT]
