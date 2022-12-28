from __future__ import annotations as _

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from ....Storage import Streams as _Windows_Storage_Streams
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import type as _type
from ......._utils import _Pointer


class ICredentialPickerOptions(_inspectable.IInspectable):
    put_Caption: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    get_Caption: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    put_Message: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    get_Message: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    put_ErrorCode: _Callable[[_type.UINT32],  # value
                             _type.HRESULT]
    get_ErrorCode: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    put_TargetName: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]
    get_TargetName: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_AuthenticationProtocol: _Callable[[_enum.Windows.Security.Credentials.UI.AuthenticationProtocol],  # value
                                          _type.HRESULT]
    get_AuthenticationProtocol: _Callable[[_Pointer[_enum.Windows.Security.Credentials.UI.AuthenticationProtocol]],  # value
                                          _type.HRESULT]
    put_CustomAuthenticationProtocol: _Callable[[_type.HSTRING],  # value
                                                _type.HRESULT]
    get_CustomAuthenticationProtocol: _Callable[[_Pointer[_type.HSTRING]],  # value
                                                _type.HRESULT]
    put_PreviousCredential: _Callable[[_Windows_Storage_Streams.IBuffer],  # value
                                      _type.HRESULT]
    get_PreviousCredential: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                      _type.HRESULT]
    put_AlwaysDisplayDialog: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_AlwaysDisplayDialog: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_CallerSavesCredential: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]
    get_CallerSavesCredential: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_CredentialSaveOption: _Callable[[_enum.Windows.Security.Credentials.UI.CredentialSaveOption],  # value
                                        _type.HRESULT]
    get_CredentialSaveOption: _Callable[[_Pointer[_enum.Windows.Security.Credentials.UI.CredentialSaveOption]],  # value
                                        _type.HRESULT]


class ICredentialPickerResults(_inspectable.IInspectable):
    get_ErrorCode: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    get_CredentialSaveOption: _Callable[[_Pointer[_enum.Windows.Security.Credentials.UI.CredentialSaveOption]],  # value
                                        _type.HRESULT]
    get_CredentialSaved: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_Credential: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                              _type.HRESULT]
    get_CredentialDomainName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                        _type.HRESULT]
    get_CredentialUserName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_CredentialPassword: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]


class ICredentialPickerStatics(_inspectable.IInspectable):
    PickWithOptionsAsync: _Callable[[ICredentialPickerOptions,  # options
                                     _Pointer[_Windows_Foundation.IAsyncOperation[ICredentialPickerResults]]],  # operation
                                    _type.HRESULT]
    PickWithMessageAsync: _Callable[[_type.HSTRING,  # targetName
                                     _type.HSTRING,  # message
                                     _Pointer[_Windows_Foundation.IAsyncOperation[ICredentialPickerResults]]],  # operation
                                    _type.HRESULT]
    PickWithCaptionAsync: _Callable[[_type.HSTRING,  # targetName
                                     _type.HSTRING,  # message
                                     _type.HSTRING,  # caption
                                     _Pointer[_Windows_Foundation.IAsyncOperation[ICredentialPickerResults]]],  # operation
                                    _type.HRESULT]

    _factory = True


class IUserConsentVerifierStatics(_inspectable.IInspectable):
    CheckAvailabilityAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Security.Credentials.UI.UserConsentVerifierAvailability]]],  # result
                                      _type.HRESULT]
    RequestVerificationAsync: _Callable[[_type.HSTRING,  # message
                                         _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Security.Credentials.UI.UserConsentVerificationResult]]],  # result
                                        _type.HRESULT]

    _factory = True
