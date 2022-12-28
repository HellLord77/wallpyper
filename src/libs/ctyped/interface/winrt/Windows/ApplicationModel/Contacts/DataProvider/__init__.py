from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Contacts as _Windows_ApplicationModel_Contacts
from .... import Foundation as _Windows_Foundation
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IContactDataProviderConnection(_inspectable.IInspectable):
    add_SyncRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IContactDataProviderConnection, IContactListSyncManagerSyncRequestEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_SyncRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_ServerSearchReadBatchRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IContactDataProviderConnection, IContactListServerSearchReadBatchRequestEventArgs],  # handler
                                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                                  _type.HRESULT]
    remove_ServerSearchReadBatchRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                     _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]


class IContactDataProviderConnection2(_inspectable.IInspectable):
    add_CreateOrUpdateContactRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IContactDataProviderConnection, IContactListCreateOrUpdateContactRequestEventArgs],  # handler
                                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                                  _type.HRESULT]
    remove_CreateOrUpdateContactRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                     _type.HRESULT]
    add_DeleteContactRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IContactDataProviderConnection, IContactListDeleteContactRequestEventArgs],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_DeleteContactRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]


class IContactDataProviderTriggerDetails(_inspectable.IInspectable):
    get_Connection: _Callable[[_Pointer[IContactDataProviderConnection]],  # value
                              _type.HRESULT]


class IContactListCreateOrUpdateContactRequest(_inspectable.IInspectable):
    get_ContactListId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_Contact: _Callable[[_Pointer[_Windows_ApplicationModel_Contacts.IContact]],  # value
                           _type.HRESULT]
    ReportCompletedAsync: _Callable[[_Windows_ApplicationModel_Contacts.IContact,  # createdOrUpdatedContact
                                     _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IContactListCreateOrUpdateContactRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IContactListCreateOrUpdateContactRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IContactListDeleteContactRequest(_inspectable.IInspectable):
    get_ContactListId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_ContactId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    ReportCompletedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IContactListDeleteContactRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IContactListDeleteContactRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IContactListServerSearchReadBatchRequest(_inspectable.IInspectable):
    get_SessionId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_ContactListId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_Options: _Callable[[_Pointer[_Windows_ApplicationModel_Contacts.IContactQueryOptions]],  # value
                           _type.HRESULT]
    get_SuggestedBatchSize: _Callable[[_Pointer[_type.UINT32]],  # value
                                      _type.HRESULT]
    SaveContactAsync: _Callable[[_Windows_ApplicationModel_Contacts.IContact,  # contact
                                 _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                _type.HRESULT]
    ReportCompletedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_enum.Windows.ApplicationModel.Contacts.ContactBatchStatus,  # batchStatus
                                  _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IContactListServerSearchReadBatchRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IContactListServerSearchReadBatchRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IContactListSyncManagerSyncRequest(_inspectable.IInspectable):
    get_ContactListId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    ReportCompletedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IContactListSyncManagerSyncRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IContactListSyncManagerSyncRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]
