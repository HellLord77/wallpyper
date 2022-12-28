from __future__ import annotations as _

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from .... import System as _Windows_System
from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IOnlineIdAuthenticator(_inspectable.IInspectable):
    AuthenticateUserAsync: _Callable[[IOnlineIdServiceTicketRequest,  # request
                                      _Pointer[_Windows_Foundation.IAsyncOperation[IUserIdentity]]],  # authenticationOperation
                                     _type.HRESULT]
    AuthenticateUserAsyncAdvanced: _Callable[[_Windows_Foundation_Collections.IIterable[IOnlineIdServiceTicketRequest],  # requests
                                              _enum.Windows.Security.Authentication.OnlineId.CredentialPromptType,  # credentialPromptType
                                              _Pointer[_Windows_Foundation.IAsyncOperation[IUserIdentity]]],  # authenticationOperation
                                             _type.HRESULT]
    SignOutUserAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # signOutUserOperation
                                _type.HRESULT]
    put_ApplicationId: _Callable[[_struct.GUID],  # value
                                 _type.HRESULT]
    get_ApplicationId: _Callable[[_Pointer[_struct.GUID]],  # value
                                 _type.HRESULT]
    get_CanSignOut: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_AuthenticatedSafeCustomerId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                               _type.HRESULT]


class IOnlineIdServiceTicket(_inspectable.IInspectable):
    get_Value: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Request: _Callable[[_Pointer[IOnlineIdServiceTicketRequest]],  # value
                           _type.HRESULT]
    get_ErrorCode: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]


class IOnlineIdServiceTicketRequest(_inspectable.IInspectable):
    get_Service: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Policy: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]


class IOnlineIdServiceTicketRequestFactory(_inspectable.IInspectable):
    CreateOnlineIdServiceTicketRequest: _Callable[[_type.HSTRING,  # service
                                                   _type.HSTRING,  # policy
                                                   _Pointer[IOnlineIdServiceTicketRequest]],  # onlineIdServiceTicketRequest
                                                  _type.HRESULT]
    CreateOnlineIdServiceTicketRequestAdvanced: _Callable[[_type.HSTRING,  # service
                                                           _Pointer[IOnlineIdServiceTicketRequest]],  # onlineIdServiceTicketRequest
                                                          _type.HRESULT]

    _factory = True


class IOnlineIdSystemAuthenticatorForUser(_inspectable.IInspectable):
    GetTicketAsync: _Callable[[IOnlineIdServiceTicketRequest,  # request
                               _Pointer[_Windows_Foundation.IAsyncOperation[IOnlineIdSystemTicketResult]]],  # operation
                              _type.HRESULT]
    put_ApplicationId: _Callable[[_struct.GUID],  # value
                                 _type.HRESULT]
    get_ApplicationId: _Callable[[_Pointer[_struct.GUID]],  # value
                                 _type.HRESULT]
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # user
                        _type.HRESULT]


class IOnlineIdSystemAuthenticatorStatics(_inspectable.IInspectable):
    get_Default: _Callable[[_Pointer[IOnlineIdSystemAuthenticatorForUser]],  # value
                           _type.HRESULT]
    GetForUser: _Callable[[_Windows_System.IUser,  # user
                           _Pointer[IOnlineIdSystemAuthenticatorForUser]],  # value
                          _type.HRESULT]

    _factory = True


class IOnlineIdSystemIdentity(_inspectable.IInspectable):
    get_Ticket: _Callable[[_Pointer[IOnlineIdServiceTicket]],  # value
                          _type.HRESULT]
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]


class IOnlineIdSystemTicketResult(_inspectable.IInspectable):
    get_Identity: _Callable[[_Pointer[IOnlineIdSystemIdentity]],  # value
                            _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.Security.Authentication.OnlineId.OnlineIdSystemTicketStatus]],  # value
                          _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class IUserIdentity(_inspectable.IInspectable):
    get_Tickets: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IOnlineIdServiceTicket]]],  # value
                           _type.HRESULT]
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_SafeCustomerId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_SignInName: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_FirstName: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_LastName: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_IsBetaAccount: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_IsConfirmedPC: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
