from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import Storage as _Windows_Storage
from ... import System as _Windows_System
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IAdvertisingManagerForUser(_inspectable.IInspectable):
    get_AdvertisingId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]


class IAdvertisingManagerStatics(_inspectable.IInspectable, factory=True):
    get_AdvertisingId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]


class IAdvertisingManagerStatics2(_inspectable.IInspectable, factory=True):
    GetForUser: _Callable[[_Windows_System.IUser,  # user
                           _Pointer[IAdvertisingManagerForUser]],  # value
                          _type.HRESULT]


class IAssignedAccessSettings(_inspectable.IInspectable):
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_IsSingleAppKioskMode: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]


class IAssignedAccessSettingsStatics(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[IAssignedAccessSettings]],  # result
                          _type.HRESULT]
    GetForUser: _Callable[[_Windows_System.IUser,  # user
                           _Pointer[IAssignedAccessSettings]],  # result
                          _type.HRESULT]


class IDiagnosticsSettings(_inspectable.IInspectable):
    get_CanUseDiagnosticsToTailorExperiences: _Callable[[_Pointer[_type.boolean]],  # value
                                                        _type.HRESULT]
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]


class IDiagnosticsSettingsStatics(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[IDiagnosticsSettings]],  # value
                          _type.HRESULT]
    GetForUser: _Callable[[_Windows_System.IUser,  # user
                           _Pointer[IDiagnosticsSettings]],  # value
                          _type.HRESULT]


class IFirstSignInSettings(_inspectable.IInspectable):
    pass


class IFirstSignInSettingsStatics(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[IFirstSignInSettings]],  # result
                          _type.HRESULT]


class IGlobalizationPreferencesForUser(_inspectable.IInspectable):
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]
    get_Calendars: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                             _type.HRESULT]
    get_Clocks: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                          _type.HRESULT]
    get_Currencies: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                              _type.HRESULT]
    get_Languages: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                             _type.HRESULT]
    get_HomeGeographicRegion: _Callable[[_Pointer[_type.HSTRING]],  # value
                                        _type.HRESULT]
    get_WeekStartsOn: _Callable[[_Pointer[_enum.Windows.Globalization.DayOfWeek]],  # value
                                _type.HRESULT]


class IGlobalizationPreferencesStatics(_inspectable.IInspectable, factory=True):
    get_Calendars: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                             _type.HRESULT]
    get_Clocks: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                          _type.HRESULT]
    get_Currencies: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                              _type.HRESULT]
    get_Languages: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                             _type.HRESULT]
    get_HomeGeographicRegion: _Callable[[_Pointer[_type.HSTRING]],  # value
                                        _type.HRESULT]
    get_WeekStartsOn: _Callable[[_Pointer[_enum.Windows.Globalization.DayOfWeek]],  # value
                                _type.HRESULT]


class IGlobalizationPreferencesStatics2(_inspectable.IInspectable, factory=True):
    TrySetHomeGeographicRegion: _Callable[[_type.HSTRING,  # region
                                           _Pointer[_type.boolean]],  # result
                                          _type.HRESULT]
    TrySetLanguages: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # languageTags
                                _Pointer[_type.boolean]],  # result
                               _type.HRESULT]


class IGlobalizationPreferencesStatics3(_inspectable.IInspectable, factory=True):
    GetForUser: _Callable[[_Windows_System.IUser,  # user
                           _Pointer[IGlobalizationPreferencesForUser]],  # value
                          _type.HRESULT]


class ILockScreenImageFeedStatics(_inspectable.IInspectable, factory=True):
    RequestSetImageFeedAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # syndicationFeedUri
                                         _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.System.UserProfile.SetImageFeedResult]]],  # value
                                        _type.HRESULT]
    TryRemoveImageFeed: _Callable[[_Pointer[_type.boolean]],  # result
                                  _type.HRESULT]


class ILockScreenStatics(_inspectable.IInspectable, factory=True):
    get_OriginalImageFile: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                     _type.HRESULT]
    GetImageStream: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStream]],  # value
                              _type.HRESULT]
    SetImageFileAsync: _Callable[[_Windows_Storage.IStorageFile,  # value
                                  _Pointer[_Windows_Foundation.IAsyncAction]],  # Operation
                                 _type.HRESULT]
    SetImageStreamAsync: _Callable[[_Windows_Storage_Streams.IRandomAccessStream,  # value
                                    _Pointer[_Windows_Foundation.IAsyncAction]],  # Operation
                                   _type.HRESULT]


class IUserInformationStatics(_inspectable.IInspectable, factory=True):
    AccountPictureChangeEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    NameAccessAllowed: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    GetAccountPicture: _Callable[[_enum.Windows.System.UserProfile.AccountPictureKind,  # kind
                                  _Pointer[_Windows_Storage.IStorageFile]],  # storageFile
                                 _type.HRESULT]
    SetAccountPictureAsync: _Callable[[_Windows_Storage.IStorageFile,  # image
                                       _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.System.UserProfile.SetAccountPictureResult]]],  # operation
                                      _type.HRESULT]
    SetAccountPicturesAsync: _Callable[[_Windows_Storage.IStorageFile,  # smallImage
                                        _Windows_Storage.IStorageFile,  # largeImage
                                        _Windows_Storage.IStorageFile,  # video
                                        _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.System.UserProfile.SetAccountPictureResult]]],  # operation
                                       _type.HRESULT]
    SetAccountPictureFromStreamAsync: _Callable[[_Windows_Storage_Streams.IRandomAccessStream,  # image
                                                 _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.System.UserProfile.SetAccountPictureResult]]],  # operation
                                                _type.HRESULT]
    SetAccountPicturesFromStreamsAsync: _Callable[[_Windows_Storage_Streams.IRandomAccessStream,  # smallImage
                                                   _Windows_Storage_Streams.IRandomAccessStream,  # largeImage
                                                   _Windows_Storage_Streams.IRandomAccessStream,  # video
                                                   _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.System.UserProfile.SetAccountPictureResult]]],  # operation
                                                  _type.HRESULT]
    AccountPictureChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    GetDisplayNameAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                   _type.HRESULT]
    GetFirstNameAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                 _type.HRESULT]
    GetLastNameAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                _type.HRESULT]
    GetPrincipalNameAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                     _type.HRESULT]
    GetSessionInitiationProtocolUriAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation.IUriRuntimeClass]]],  # operation
                                                    _type.HRESULT]
    GetDomainNameAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                  _type.HRESULT]


class IUserProfilePersonalizationSettings(_inspectable.IInspectable):
    TrySetLockScreenImageAsync: _Callable[[_Windows_Storage.IStorageFile,  # imageFile
                                           _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                          _type.HRESULT]
    TrySetWallpaperImageAsync: _Callable[[_Windows_Storage.IStorageFile,  # imageFile
                                          _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                         _type.HRESULT]


class IUserProfilePersonalizationSettingsStatics(_inspectable.IInspectable, factory=True):
    get_Current: _Callable[[_Pointer[IUserProfilePersonalizationSettings]],  # value
                           _type.HRESULT]
    IsSupported: _Callable[[_Pointer[_type.boolean]],  # result
                           _type.HRESULT]
