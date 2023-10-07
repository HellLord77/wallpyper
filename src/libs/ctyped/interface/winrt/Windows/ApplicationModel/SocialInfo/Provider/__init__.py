from __future__ import annotations as _

from typing import Callable as _Callable

from ... import SocialInfo as _Windows_ApplicationModel_SocialInfo
from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class ISocialDashboardItemUpdater(_inspectable.IInspectable):
    OwnerRemoteId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    Content: _Callable[[_Pointer[_Windows_ApplicationModel_SocialInfo.ISocialFeedContent]],  # value
                       _type.HRESULT]
    Timestamp: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                         _type.HRESULT]
    Thumbnail: _Callable[[_Pointer[_Windows_ApplicationModel_SocialInfo.ISocialItemThumbnail]],  # value
                         _type.HRESULT]
    CommitAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                           _type.HRESULT]
    TargetUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                         _type.HRESULT]


class ISocialFeedUpdater(_inspectable.IInspectable):
    OwnerRemoteId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    Kind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.SocialInfo.SocialFeedKind]],  # value
                    _type.HRESULT]
    Items: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_ApplicationModel_SocialInfo.ISocialFeedItem]]],  # value
                     _type.HRESULT]
    CommitAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                           _type.HRESULT]


class ISocialInfoProviderManagerStatics(_inspectable.IInspectable, factory=True):
    CreateSocialFeedUpdaterAsync: _Callable[[_enum.Windows.ApplicationModel.SocialInfo.SocialFeedKind,  # kind
                                             _enum.Windows.ApplicationModel.SocialInfo.SocialFeedUpdateMode,  # mode
                                             _type.HSTRING,  # ownerRemoteId
                                             _Pointer[_Windows_Foundation.IAsyncOperation[ISocialFeedUpdater]]],  # operation
                                            _type.HRESULT]
    CreateDashboardItemUpdaterAsync: _Callable[[_type.HSTRING,  # ownerRemoteId
                                                _Pointer[_Windows_Foundation.IAsyncOperation[ISocialDashboardItemUpdater]]],  # operation
                                               _type.HRESULT]
    UpdateBadgeCountValue: _Callable[[_type.HSTRING,  # itemRemoteId
                                      _type.INT32],  # newCount
                                     _type.HRESULT]
    ReportNewContentAvailable: _Callable[[_type.HSTRING,  # contactRemoteId
                                          _enum.Windows.ApplicationModel.SocialInfo.SocialFeedKind],  # kind
                                         _type.HRESULT]
    ProvisionAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                              _type.HRESULT]
    DeprovisionAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                _type.HRESULT]
