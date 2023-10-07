from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import System as _Windows_System
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import type as _type
from ......_utils import _Pointer


class ICredentialFactory(_inspectable.IInspectable, factory=True):
    CreatePasswordCredential: _Callable[[_type.HSTRING,  # resource
                                         _type.HSTRING,  # userName
                                         _type.HSTRING,  # password
                                         _Pointer[IPasswordCredential]],  # credential
                                        _type.HRESULT]


class IKeyCredential(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    RetrievePublicKeyWithDefaultBlobType: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                                    _type.HRESULT]
    RetrievePublicKeyWithBlobType: _Callable[[_enum.Windows.Security.Cryptography.Core.CryptographicPublicKeyBlobType,  # blobType
                                              _Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                             _type.HRESULT]
    RequestSignAsync: _Callable[[_Windows_Storage_Streams.IBuffer,  # data
                                 _Pointer[_Windows_Foundation.IAsyncOperation[IKeyCredentialOperationResult]]],  # value
                                _type.HRESULT]
    GetAttestationAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IKeyCredentialAttestationResult]]],  # value
                                   _type.HRESULT]


class IKeyCredentialAttestationResult(_inspectable.IInspectable):
    get_CertificateChainBuffer: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                          _type.HRESULT]
    get_AttestationBuffer: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                     _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.Security.Credentials.KeyCredentialAttestationStatus]],  # value
                          _type.HRESULT]


class IKeyCredentialManagerStatics(_inspectable.IInspectable, factory=True):
    IsSupportedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # value
                                _type.HRESULT]
    RenewAttestationAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                     _type.HRESULT]
    RequestCreateAsync: _Callable[[_type.HSTRING,  # name
                                   _enum.Windows.Security.Credentials.KeyCredentialCreationOption,  # option
                                   _Pointer[_Windows_Foundation.IAsyncOperation[IKeyCredentialRetrievalResult]]],  # value
                                  _type.HRESULT]
    OpenAsync: _Callable[[_type.HSTRING,  # name
                          _Pointer[_Windows_Foundation.IAsyncOperation[IKeyCredentialRetrievalResult]]],  # value
                         _type.HRESULT]
    DeleteAsync: _Callable[[_type.HSTRING,  # name
                            _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                           _type.HRESULT]


class IKeyCredentialOperationResult(_inspectable.IInspectable):
    get_Result: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                          _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.Security.Credentials.KeyCredentialStatus]],  # value
                          _type.HRESULT]


class IKeyCredentialRetrievalResult(_inspectable.IInspectable):
    get_Credential: _Callable[[_Pointer[IKeyCredential]],  # value
                              _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.Security.Credentials.KeyCredentialStatus]],  # value
                          _type.HRESULT]


class IPasswordCredential(_inspectable.IInspectable):
    get_Resource: _Callable[[_Pointer[_type.HSTRING]],  # resource
                            _type.HRESULT]
    put_Resource: _Callable[[_type.HSTRING],  # resource
                            _type.HRESULT]
    get_UserName: _Callable[[_Pointer[_type.HSTRING]],  # userName
                            _type.HRESULT]
    put_UserName: _Callable[[_type.HSTRING],  # userName
                            _type.HRESULT]
    get_Password: _Callable[[_Pointer[_type.HSTRING]],  # password
                            _type.HRESULT]
    put_Password: _Callable[[_type.HSTRING],  # password
                            _type.HRESULT]
    RetrievePassword: _Callable[[],
                                _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # props
                              _type.HRESULT]


class IPasswordVault(_inspectable.IInspectable):
    Add: _Callable[[IPasswordCredential],  # credential
                   _type.HRESULT]
    Remove: _Callable[[IPasswordCredential],  # credential
                      _type.HRESULT]
    Retrieve: _Callable[[_type.HSTRING,  # resource
                         _type.HSTRING,  # userName
                         _Pointer[IPasswordCredential]],  # credential
                        _type.HRESULT]
    FindAllByResource: _Callable[[_type.HSTRING,  # resource
                                  _Pointer[_Windows_Foundation_Collections.IVectorView[IPasswordCredential]]],  # credentials
                                 _type.HRESULT]
    FindAllByUserName: _Callable[[_type.HSTRING,  # userName
                                  _Pointer[_Windows_Foundation_Collections.IVectorView[IPasswordCredential]]],  # credentials
                                 _type.HRESULT]
    RetrieveAll: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IPasswordCredential]]],  # credentials
                           _type.HRESULT]


class IWebAccount(_inspectable.IInspectable):
    get_WebAccountProvider: _Callable[[_Pointer[IWebAccountProvider]],  # value
                                      _type.HRESULT]
    get_UserName: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_State: _Callable[[_Pointer[_enum.Windows.Security.Credentials.WebAccountState]],  # value
                         _type.HRESULT]


class IWebAccount2(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _type.HSTRING]]],  # value
                              _type.HRESULT]
    GetPictureAsync: _Callable[[_enum.Windows.Security.Credentials.WebAccountPictureSize,  # desizedSize
                                _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStream]]],  # asyncInfo
                               _type.HRESULT]
    SignOutAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                            _type.HRESULT]
    SignOutWithClientIdAsync: _Callable[[_type.HSTRING,  # clientId
                                         _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                        _type.HRESULT]


class IWebAccountFactory(_inspectable.IInspectable, factory=True):
    CreateWebAccount: _Callable[[IWebAccountProvider,  # webAccountProvider
                                 _type.HSTRING,  # userName
                                 _enum.Windows.Security.Credentials.WebAccountState,  # state
                                 _Pointer[IWebAccount]],  # instance
                                _type.HRESULT]


class IWebAccountProvider(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    IconUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]


class IWebAccountProvider2(_inspectable.IInspectable):
    get_DisplayPurpose: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_Authority: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]


class IWebAccountProvider3(_inspectable.IInspectable):
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # user
                        _type.HRESULT]


class IWebAccountProvider4(_inspectable.IInspectable):
    get_IsSystemProvider: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]


class IWebAccountProviderFactory(_inspectable.IInspectable, factory=True):
    CreateWebAccountProvider: _Callable[[_type.HSTRING,  # id
                                         _type.HSTRING,  # displayName
                                         _Windows_Foundation.IUriRuntimeClass,  # iconUri
                                         _Pointer[IWebAccountProvider]],  # instance
                                        _type.HRESULT]
