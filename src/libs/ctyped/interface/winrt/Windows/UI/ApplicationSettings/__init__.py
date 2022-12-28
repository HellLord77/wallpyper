from __future__ import annotations as _

from typing import Callable as _Callable

from .. import Popups as _Windows_UI_Popups
from ... import Foundation as _Windows_Foundation
from ... import System as _Windows_System
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Security import Credentials as _Windows_Security_Credentials
from .... import inspectable as _inspectable
from .....um import Unknwnbase as _Unknwnbase
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class _ICredentialCommandCredentialDeletedHandler:
    Invoke: _Callable[[ICredentialCommand],  # command
                      _type.HRESULT]


class ICredentialCommandCredentialDeletedHandler(_ICredentialCommandCredentialDeletedHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICredentialCommandCredentialDeletedHandler_impl(_ICredentialCommandCredentialDeletedHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IWebAccountCommandInvokedHandler:
    Invoke: _Callable[[IWebAccountCommand,  # command
                       IWebAccountInvokedArgs],  # args
                      _type.HRESULT]


class IWebAccountCommandInvokedHandler(_IWebAccountCommandInvokedHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IWebAccountCommandInvokedHandler_impl(_IWebAccountCommandInvokedHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IWebAccountProviderCommandInvokedHandler:
    Invoke: _Callable[[IWebAccountProviderCommand],  # command
                      _type.HRESULT]


class IWebAccountProviderCommandInvokedHandler(_IWebAccountProviderCommandInvokedHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IWebAccountProviderCommandInvokedHandler_impl(_IWebAccountProviderCommandInvokedHandler, _Unknwnbase.IUnknown_impl):
    pass


class IAccountsSettingsPane(_inspectable.IInspectable):
    add_AccountCommandsRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IAccountsSettingsPane, IAccountsSettingsPaneCommandsRequestedEventArgs],  # handler
                                             _Pointer[_struct.EventRegistrationToken]],  # cookie
                                            _type.HRESULT]
    remove_AccountCommandsRequested: _Callable[[_struct.EventRegistrationToken],  # cookie
                                               _type.HRESULT]


class IAccountsSettingsPaneCommandsRequestedEventArgs(_inspectable.IInspectable):
    get_WebAccountProviderCommands: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IWebAccountProviderCommand]]],  # value
                                              _type.HRESULT]
    get_WebAccountCommands: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IWebAccountCommand]]],  # value
                                      _type.HRESULT]
    get_CredentialCommands: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ICredentialCommand]]],  # value
                                      _type.HRESULT]
    get_Commands: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Popups.IUICommand]]],  # value
                            _type.HRESULT]
    get_HeaderText: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_HeaderText: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[IAccountsSettingsPaneEventDeferral]],  # deferral
                           _type.HRESULT]


class IAccountsSettingsPaneCommandsRequestedEventArgs2(_inspectable.IInspectable):
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]


class IAccountsSettingsPaneEventDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class IAccountsSettingsPaneStatics(_inspectable.IInspectable):
    GetForCurrentView: _Callable[[_Pointer[IAccountsSettingsPane]],  # current
                                 _type.HRESULT]
    Show: _Callable[[],
                    _type.HRESULT]

    _factory = True


class IAccountsSettingsPaneStatics2(_inspectable.IInspectable):
    ShowManageAccountsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                       _type.HRESULT]
    ShowAddAccountAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                   _type.HRESULT]

    _factory = True


class IAccountsSettingsPaneStatics3(_inspectable.IInspectable):
    ShowManageAccountsForUserAsync: _Callable[[_Windows_System.IUser,  # user
                                               _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                              _type.HRESULT]
    ShowAddAccountForUserAsync: _Callable[[_Windows_System.IUser,  # user
                                           _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                          _type.HRESULT]

    _factory = True


class ICredentialCommand(_inspectable.IInspectable):
    get_PasswordCredential: _Callable[[_Pointer[_Windows_Security_Credentials.IPasswordCredential]],  # value
                                      _type.HRESULT]
    get_CredentialDeleted: _Callable[[_Pointer[ICredentialCommandCredentialDeletedHandler]],  # value
                                     _type.HRESULT]


class ICredentialCommandFactory(_inspectable.IInspectable):
    CreateCredentialCommand: _Callable[[_Windows_Security_Credentials.IPasswordCredential,  # passwordCredential
                                        _Pointer[ICredentialCommand]],  # instance
                                       _type.HRESULT]
    CreateCredentialCommandWithHandler: _Callable[[_Windows_Security_Credentials.IPasswordCredential,  # passwordCredential
                                                   ICredentialCommandCredentialDeletedHandler,  # deleted
                                                   _Pointer[ICredentialCommand]],  # instance
                                                  _type.HRESULT]

    _factory = True


class ISettingsCommandFactory(_inspectable.IInspectable):
    CreateSettingsCommand: _Callable[[_inspectable.IInspectable,  # settingsCommandId
                                      _type.HSTRING,  # label
                                      _Windows_UI_Popups.IUICommandInvokedHandler,  # handler
                                      _Pointer[_Windows_UI_Popups.IUICommand]],  # instance
                                     _type.HRESULT]

    _factory = True


class ISettingsCommandStatics(_inspectable.IInspectable):
    get_AccountsCommand: _Callable[[_Pointer[_Windows_UI_Popups.IUICommand]],  # value
                                   _type.HRESULT]

    _factory = True


class ISettingsPane(_inspectable.IInspectable):
    CommandsRequested: _Callable[[_struct.EventRegistrationToken],  # cookie
                                 _type.HRESULT]


class ISettingsPaneCommandsRequest(_inspectable.IInspectable):
    ApplicationCommands: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Popups.IUICommand]]],  # value
                                   _type.HRESULT]


class ISettingsPaneCommandsRequestedEventArgs(_inspectable.IInspectable):
    Request: _Callable[[_Pointer[ISettingsPaneCommandsRequest]],  # request
                       _type.HRESULT]


class ISettingsPaneStatics(_inspectable.IInspectable):
    GetForCurrentView: _Callable[[_Pointer[ISettingsPane]],  # current
                                 _type.HRESULT]
    Show: _Callable[[],
                    _type.HRESULT]
    Edge: _Callable[[_Pointer[_enum.Windows.UI.ApplicationSettings.SettingsEdgeLocation]],  # value
                    _type.HRESULT]

    _factory = True


class IWebAccountCommand(_inspectable.IInspectable):
    get_WebAccount: _Callable[[_Pointer[_Windows_Security_Credentials.IWebAccount]],  # value
                              _type.HRESULT]
    get_Invoked: _Callable[[_Pointer[IWebAccountCommandInvokedHandler]],  # value
                           _type.HRESULT]
    get_Actions: _Callable[[_Pointer[_enum.Windows.UI.ApplicationSettings.SupportedWebAccountActions]],  # value
                           _type.HRESULT]


class IWebAccountCommandFactory(_inspectable.IInspectable):
    CreateWebAccountCommand: _Callable[[_Windows_Security_Credentials.IWebAccount,  # webAccount
                                        IWebAccountCommandInvokedHandler,  # invoked
                                        _enum.Windows.UI.ApplicationSettings.SupportedWebAccountActions,  # actions
                                        _Pointer[IWebAccountCommand]],  # instance
                                       _type.HRESULT]

    _factory = True


class IWebAccountInvokedArgs(_inspectable.IInspectable):
    get_Action: _Callable[[_Pointer[_enum.Windows.UI.ApplicationSettings.WebAccountAction]],  # action
                          _type.HRESULT]


class IWebAccountProviderCommand(_inspectable.IInspectable):
    get_WebAccountProvider: _Callable[[_Pointer[_Windows_Security_Credentials.IWebAccountProvider]],  # value
                                      _type.HRESULT]
    get_Invoked: _Callable[[_Pointer[IWebAccountProviderCommandInvokedHandler]],  # value
                           _type.HRESULT]


class IWebAccountProviderCommandFactory(_inspectable.IInspectable):
    CreateWebAccountProviderCommand: _Callable[[_Windows_Security_Credentials.IWebAccountProvider,  # webAccountProvider
                                                IWebAccountProviderCommandInvokedHandler,  # invoked
                                                _Pointer[IWebAccountProviderCommand]],  # instance
                                               _type.HRESULT]

    _factory = True
