from __future__ import annotations

from typing import Callable as _Callable

from ... import Contacts as _Windows_ApplicationModel_Contacts
from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IContactPickerUI(_inspectable.IInspectable):
    AddContact: _Callable[[_type.HSTRING,  # id
                           _Windows_ApplicationModel_Contacts.IContact,  # contact
                           _Pointer[_enum.Windows.ApplicationModel.Contacts.Provider.AddContactResult]],  # result
                          _type.HRESULT]
    RemoveContact: _Callable[[_type.HSTRING],  # id
                             _type.HRESULT]
    ContainsContact: _Callable[[_type.HSTRING,  # id
                                _Pointer[_type.boolean]],  # isContained
                               _type.HRESULT]
    DesiredFields: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                             _type.HRESULT]
    get_SelectionMode: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Contacts.ContactSelectionMode]],  # value
                                 _type.HRESULT]
    add_ContactRemoved: _Callable[[_Windows_Foundation.ITypedEventHandler[IContactPickerUI, IContactRemovedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_ContactRemoved: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]


class IContactPickerUI2(_inspectable.IInspectable):
    AddContact: _Callable[[_Windows_ApplicationModel_Contacts.IContact,  # contact
                           _Pointer[_enum.Windows.ApplicationModel.Contacts.Provider.AddContactResult]],  # result
                          _type.HRESULT]
    get_DesiredFieldsWithContactFieldType: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_enum.Windows.ApplicationModel.Contacts.ContactFieldType]]],  # value
                                                     _type.HRESULT]


class IContactRemovedEventArgs(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
