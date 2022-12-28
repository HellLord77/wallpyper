from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import System as _Windows_System
from ...ApplicationModel import DataTransfer as _Windows_ApplicationModel_DataTransfer
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import type as _type
from ......_utils import _Pointer


class ICortanaActionableInsights(_inspectable.IInspectable):
    User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                    _type.HRESULT]
    IsAvailableAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                _type.HRESULT]
    ShowInsightsForImageAsync: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference,  # imageStream
                                          _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                         _type.HRESULT]
    ShowInsightsForImageWithOptionsAsync: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference,  # imageStream
                                                     ICortanaActionableInsightsOptions,  # options
                                                     _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                                    _type.HRESULT]
    ShowInsightsForTextAsync: _Callable[[_type.HSTRING,  # text
                                         _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                        _type.HRESULT]
    ShowInsightsForTextWithOptionsAsync: _Callable[[_type.HSTRING,  # text
                                                    ICortanaActionableInsightsOptions,  # options
                                                    _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                                   _type.HRESULT]
    ShowInsightsAsync: _Callable[[_Windows_ApplicationModel_DataTransfer.IDataPackage,  # datapackage
                                  _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                 _type.HRESULT]
    ShowInsightsWithOptionsAsync: _Callable[[_Windows_ApplicationModel_DataTransfer.IDataPackage,  # datapackage
                                             ICortanaActionableInsightsOptions,  # options
                                             _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                            _type.HRESULT]


class ICortanaActionableInsightsOptions(_inspectable.IInspectable):
    ContentSourceWebLink: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                                    _type.HRESULT]
    SurroundingText: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]


class ICortanaActionableInsightsStatics(_inspectable.IInspectable):
    GetDefault: _Callable[[_Pointer[ICortanaActionableInsights]],  # result
                          _type.HRESULT]
    GetForUser: _Callable[[_Windows_System.IUser,  # user
                           _Pointer[ICortanaActionableInsights]],  # result
                          _type.HRESULT]

    _factory = True


class ICortanaPermissionsManager(_inspectable.IInspectable):
    IsSupported: _Callable[[_Pointer[_type.boolean]],  # result
                           _type.HRESULT]
    ArePermissionsGrantedAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_enum.Windows.Services.Cortana.CortanaPermission],  # permissions
                                           _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # getGrantedPermissionsOperation
                                          _type.HRESULT]
    GrantPermissionsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_enum.Windows.Services.Cortana.CortanaPermission],  # permissions
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Services.Cortana.CortanaPermissionsChangeResult]]],  # grantOperation
                                     _type.HRESULT]
    RevokePermissionsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_enum.Windows.Services.Cortana.CortanaPermission],  # permissions
                                       _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Services.Cortana.CortanaPermissionsChangeResult]]],  # revokeOperation
                                      _type.HRESULT]


class ICortanaPermissionsManagerStatics(_inspectable.IInspectable):
    GetDefault: _Callable[[_Pointer[ICortanaPermissionsManager]],  # result
                          _type.HRESULT]

    _factory = True


class ICortanaSettings(_inspectable.IInspectable):
    HasUserConsentToVoiceActivation: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]
    IsVoiceActivationEnabled: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]


class ICortanaSettingsStatics(_inspectable.IInspectable):
    IsSupported: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    GetDefault: _Callable[[_Pointer[ICortanaSettings]],  # result
                          _type.HRESULT]

    _factory = True
