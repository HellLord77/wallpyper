from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class ISocialFeedChildItem(_inspectable.IInspectable):
    Author: _Callable[[_Pointer[ISocialUserInfo]],  # value
                      _type.HRESULT]
    PrimaryContent: _Callable[[_Pointer[ISocialFeedContent]],  # value
                              _type.HRESULT]
    SecondaryContent: _Callable[[_Pointer[ISocialFeedContent]],  # value
                                _type.HRESULT]
    Timestamp: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                         _type.HRESULT]
    TargetUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                         _type.HRESULT]
    Thumbnails: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ISocialItemThumbnail]]],  # value
                          _type.HRESULT]
    SharedItem: _Callable[[ISocialFeedSharedItem],  # value
                          _type.HRESULT]


class ISocialFeedContent(_inspectable.IInspectable):
    Title: _Callable[[_type.HSTRING],  # value
                     _type.HRESULT]
    Message: _Callable[[_type.HSTRING],  # value
                       _type.HRESULT]
    TargetUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                         _type.HRESULT]


class ISocialFeedItem(_inspectable.IInspectable):
    Author: _Callable[[_Pointer[ISocialUserInfo]],  # value
                      _type.HRESULT]
    PrimaryContent: _Callable[[_Pointer[ISocialFeedContent]],  # value
                              _type.HRESULT]
    SecondaryContent: _Callable[[_Pointer[ISocialFeedContent]],  # value
                                _type.HRESULT]
    Timestamp: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                         _type.HRESULT]
    TargetUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                         _type.HRESULT]
    Thumbnails: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ISocialItemThumbnail]]],  # value
                          _type.HRESULT]
    SharedItem: _Callable[[ISocialFeedSharedItem],  # value
                          _type.HRESULT]
    BadgeStyle: _Callable[[_enum.Windows.ApplicationModel.SocialInfo.SocialItemBadgeStyle],  # value
                          _type.HRESULT]
    BadgeCountValue: _Callable[[_type.INT32],  # value
                               _type.HRESULT]
    RemoteId: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    ChildItem: _Callable[[ISocialFeedChildItem],  # value
                         _type.HRESULT]
    Style: _Callable[[_enum.Windows.ApplicationModel.SocialInfo.SocialFeedItemStyle],  # value
                     _type.HRESULT]


class ISocialFeedSharedItem(_inspectable.IInspectable):
    OriginalSource: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                              _type.HRESULT]
    Content: _Callable[[_Pointer[ISocialFeedContent]],  # value
                       _type.HRESULT]
    Timestamp: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                         _type.HRESULT]
    TargetUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                         _type.HRESULT]
    Thumbnail: _Callable[[_Pointer[ISocialItemThumbnail]],  # value
                         _type.HRESULT]


class ISocialItemThumbnail(_inspectable.IInspectable):
    TargetUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                         _type.HRESULT]
    ImageUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                        _type.HRESULT]
    BitmapSize: _Callable[[_struct.Windows.Graphics.Imaging.BitmapSize],  # value
                          _type.HRESULT]
    SetImageAsync: _Callable[[_Windows_Storage_Streams.IInputStream,  # image
                              _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                             _type.HRESULT]


class ISocialUserInfo(_inspectable.IInspectable):
    DisplayName: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    UserName: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    RemoteId: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    TargetUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                         _type.HRESULT]
