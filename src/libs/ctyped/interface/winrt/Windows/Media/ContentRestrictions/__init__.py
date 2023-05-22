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


class IContentRestrictionsBrowsePolicy(_inspectable.IInspectable):
    get_GeographicRegion: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_MaxBrowsableAgeRating: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                                         _type.HRESULT]
    get_PreferredAgeRating: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                                      _type.HRESULT]


class IRatedContentDescription(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    put_Id: _Callable[[_type.HSTRING],  # value
                      _type.HRESULT]
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Title: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Image: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # value
                         _type.HRESULT]
    put_Image: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference],  # value
                         _type.HRESULT]
    get_Category: _Callable[[_Pointer[_enum.Windows.Media.ContentRestrictions.RatedContentCategory]],  # value
                            _type.HRESULT]
    put_Category: _Callable[[_enum.Windows.Media.ContentRestrictions.RatedContentCategory],  # value
                            _type.HRESULT]
    get_Ratings: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                           _type.HRESULT]
    put_Ratings: _Callable[[_Windows_Foundation_Collections.IVector[_type.HSTRING]],  # value
                           _type.HRESULT]


class IRatedContentDescriptionFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.HSTRING,  # id
                       _type.HSTRING,  # title
                       _enum.Windows.Media.ContentRestrictions.RatedContentCategory,  # category
                       _Pointer[IRatedContentDescription]],  # RatedContentDescription
                      _type.HRESULT]


class IRatedContentRestrictions(_inspectable.IInspectable):
    GetBrowsePolicyAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IContentRestrictionsBrowsePolicy]]],  # operation
                                    _type.HRESULT]
    GetRestrictionLevelAsync: _Callable[[IRatedContentDescription,  # RatedContentDescription
                                         _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Media.ContentRestrictions.ContentAccessRestrictionLevel]]],  # operation
                                        _type.HRESULT]
    RequestContentAccessAsync: _Callable[[IRatedContentDescription,  # RatedContentDescription
                                          _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                         _type.HRESULT]
    add_RestrictionsChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_RestrictionsChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]


class IRatedContentRestrictionsFactory(_inspectable.IInspectable, factory=True):
    CreateWithMaxAgeRating: _Callable[[_type.UINT32,  # maxAgeRating
                                       _Pointer[IRatedContentRestrictions]],  # ratedContentRestrictions
                                      _type.HRESULT]
