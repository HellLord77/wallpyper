from __future__ import annotations

from typing import Callable as _Callable

from . import ShObjIdl_core as _ShObjIdl_core
from . import Unknwnbase as _Unknwnbase
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class ICredentialProviderCredential(_Unknwnbase.IUnknown):
    Advise: _Callable[[ICredentialProviderCredentialEvents],  # pcpce
                      _type.HRESULT]
    UnAdvise: _Callable[[],
                        _type.HRESULT]
    SetSelected: _Callable[[_Pointer[_type.BOOL]],  # pbAutoLogon
                           _type.HRESULT]
    SetDeselected: _Callable[[],
                             _type.HRESULT]
    GetFieldState: _Callable[[_type.DWORD,  # dwFieldID
                              _Pointer[_enum.CREDENTIAL_PROVIDER_FIELD_STATE],  # pcpfs
                              _Pointer[_enum.CREDENTIAL_PROVIDER_FIELD_INTERACTIVE_STATE]],  # pcpfis
                             _type.HRESULT]
    GetStringValue: _Callable[[_type.DWORD,  # dwFieldID
                               _Pointer[_type.LPWSTR]],  # ppsz
                              _type.HRESULT]
    GetBitmapValue: _Callable[[_type.DWORD,  # dwFieldID
                               _Pointer[_type.HBITMAP]],  # phbmp
                              _type.HRESULT]
    GetCheckboxValue: _Callable[[_type.DWORD,  # dwFieldID
                                 _Pointer[_type.BOOL],  # pbChecked
                                 _Pointer[_type.LPWSTR]],  # ppszLabel
                                _type.HRESULT]
    GetSubmitButtonValue: _Callable[[_type.DWORD,  # dwFieldID
                                     _Pointer[_type.DWORD]],  # pdwAdjacentTo
                                    _type.HRESULT]
    GetComboBoxValueCount: _Callable[[_type.DWORD,  # dwFieldID
                                      _Pointer[_type.DWORD],  # pcItems
                                      _Pointer[_type.DWORD]],  # pdwSelectedItem
                                     _type.HRESULT]
    GetComboBoxValueAt: _Callable[[_type.DWORD,  # dwFieldID
                                   _type.DWORD,  # dwItem
                                   _Pointer[_type.LPWSTR]],  # ppszItem
                                  _type.HRESULT]
    SetStringValue: _Callable[[_type.DWORD,  # dwFieldID
                               _type.LPCWSTR],  # psz
                              _type.HRESULT]
    SetCheckboxValue: _Callable[[_type.DWORD,  # dwFieldID
                                 _type.BOOL],  # bChecked
                                _type.HRESULT]
    SetComboBoxSelectedValue: _Callable[[_type.DWORD,  # dwFieldID
                                         _type.DWORD],  # dwSelectedItem
                                        _type.HRESULT]
    CommandLinkClicked: _Callable[[_type.DWORD],  # dwFieldID
                                  _type.HRESULT]
    GetSerialization: _Callable[[_Pointer[_enum.CREDENTIAL_PROVIDER_GET_SERIALIZATION_RESPONSE],  # pcpgsr
                                 _Pointer[_struct.CREDENTIAL_PROVIDER_CREDENTIAL_SERIALIZATION],  # pcpcs
                                 _Pointer[_type.LPWSTR],  # ppszOptionalStatusText
                                 _Pointer[_enum.CREDENTIAL_PROVIDER_STATUS_ICON]],  # pcpsiOptionalStatusIcon
                                _type.HRESULT]
    ReportResult: _Callable[[_type.NTSTATUS,  # ntsStatus
                             _type.NTSTATUS,  # ntsSubstatus
                             _Pointer[_type.LPWSTR],  # ppszOptionalStatusText
                             _Pointer[_enum.CREDENTIAL_PROVIDER_STATUS_ICON]],  # pcpsiOptionalStatusIcon
                            _type.HRESULT]


class IQueryContinueWithStatus(_ShObjIdl_core.IQueryContinue):
    SetStatusMessage: _Callable[[_type.LPCWSTR],  # psz
                                _type.HRESULT]


class IConnectableCredentialProviderCredential(ICredentialProviderCredential):
    Connect: _Callable[[IQueryContinueWithStatus],  # pqcws
                       _type.HRESULT]
    Disconnect: _Callable[[],
                          _type.HRESULT]


class ICredentialProviderCredentialEvents(_Unknwnbase.IUnknown):
    SetFieldState: _Callable[[ICredentialProviderCredential,  # pcpc
                              _type.DWORD,  # dwFieldID
                              _enum.CREDENTIAL_PROVIDER_FIELD_STATE],  # cpfs
                             _type.HRESULT]
    SetFieldInteractiveState: _Callable[[ICredentialProviderCredential,  # pcpc
                                         _type.DWORD,  # dwFieldID
                                         _enum.CREDENTIAL_PROVIDER_FIELD_INTERACTIVE_STATE],  # cpfis
                                        _type.HRESULT]
    SetFieldString: _Callable[[ICredentialProviderCredential,  # pcpc
                               _type.DWORD,  # dwFieldID
                               _type.LPCWSTR],  # psz
                              _type.HRESULT]
    SetFieldCheckbox: _Callable[[ICredentialProviderCredential,  # pcpc
                                 _type.DWORD,  # dwFieldID
                                 _type.BOOL,  # bChecked
                                 _type.LPCWSTR],  # pszLabel
                                _type.HRESULT]
    SetFieldBitmap: _Callable[[ICredentialProviderCredential,  # pcpc
                               _type.DWORD,  # dwFieldID
                               _type.HBITMAP],  # hbmp
                              _type.HRESULT]
    SetFieldComboBoxSelectedItem: _Callable[[ICredentialProviderCredential,  # pcpc
                                             _type.DWORD,  # dwFieldID
                                             _type.DWORD],  # dwSelectedItem
                                            _type.HRESULT]
    DeleteFieldComboBoxItem: _Callable[[ICredentialProviderCredential,  # pcpc
                                        _type.DWORD,  # dwFieldID
                                        _type.DWORD],  # dwItem
                                       _type.HRESULT]
    AppendFieldComboBoxItem: _Callable[[ICredentialProviderCredential,  # pcpc
                                        _type.DWORD,  # dwFieldID
                                        _type.LPCWSTR],  # pszItem
                                       _type.HRESULT]
    SetFieldSubmitButton: _Callable[[ICredentialProviderCredential,  # pcpc
                                     _type.DWORD,  # dwFieldID
                                     _type.DWORD],  # dwAdjacentTo
                                    _type.HRESULT]
    OnCreatingWindow: _Callable[[_Pointer[_type.HWND]],  # phwndOwner
                                _type.HRESULT]


class ICredentialProvider(_Unknwnbase.IUnknown):
    SetUsageScenario: _Callable[[_enum.CREDENTIAL_PROVIDER_USAGE_SCENARIO,  # cpus
                                 _type.DWORD],  # dwFlags
                                _type.HRESULT]
    SetSerialization: _Callable[[_Pointer[_struct.CREDENTIAL_PROVIDER_CREDENTIAL_SERIALIZATION]],  # pcpcs
                                _type.HRESULT]
    Advise: _Callable[[ICredentialProviderEvents,  # pcpe
                       _type.UINT_PTR],  # upAdviseContext
                      _type.HRESULT]
    UnAdvise: _Callable[[],
                        _type.HRESULT]
    GetFieldDescriptorCount: _Callable[[_Pointer[_type.DWORD]],  # pdwCount
                                       _type.HRESULT]
    GetFieldDescriptorAt: _Callable[[_type.DWORD,  # dwIndex
                                     _Pointer[_Pointer[_struct.CREDENTIAL_PROVIDER_FIELD_DESCRIPTOR]]],  # ppcpfd
                                    _type.HRESULT]
    GetCredentialCount: _Callable[[_Pointer[_type.DWORD],  # pdwCount
                                   _Pointer[_type.DWORD],  # pdwDefault
                                   _Pointer[_type.BOOL]],  # pbAutoLogonWithDefault
                                  _type.HRESULT]
    GetCredentialAt: _Callable[[_type.DWORD,  # dwIndex
                                _Pointer[ICredentialProviderCredential]],  # ppcpc
                               _type.HRESULT]


class ICredentialProviderEvents(_Unknwnbase.IUnknown):
    CredentialsChanged: _Callable[[_type.UINT_PTR],  # upAdviseContext
                                  _type.HRESULT]


class ICredentialProviderFilter(_Unknwnbase.IUnknown):
    Filter: _Callable[[_enum.CREDENTIAL_PROVIDER_USAGE_SCENARIO,  # cpus
                       _type.DWORD,  # dwFlags
                       _Pointer[_struct.GUID],  # rgclsidProviders
                       _Pointer[_type.BOOL],  # rgbAllow
                       _type.DWORD],  # cProviders
                      _type.HRESULT]
    UpdateRemoteCredential: _Callable[[_Pointer[_struct.CREDENTIAL_PROVIDER_CREDENTIAL_SERIALIZATION],  # pcpcsIn
                                       _Pointer[_struct.CREDENTIAL_PROVIDER_CREDENTIAL_SERIALIZATION]],  # pcpcsOut
                                      _type.HRESULT]


class ICredentialProviderCredential2(ICredentialProviderCredential):
    GetUserSid: _Callable[[_Pointer[_type.LPWSTR]],  # sid
                          _type.HRESULT]


class ICredentialProviderCredentialWithFieldOptions(_Unknwnbase.IUnknown):
    GetFieldOptions: _Callable[[_type.DWORD,  # fieldID
                                _Pointer[_enum.CREDENTIAL_PROVIDER_CREDENTIAL_FIELD_OPTIONS]],  # options
                               _type.HRESULT]


class ICredentialProviderCredentialEvents2(ICredentialProviderCredentialEvents):
    BeginFieldUpdates: _Callable[[],
                                 _type.HRESULT]
    EndFieldUpdates: _Callable[[],
                               _type.HRESULT]
    SetFieldOptions: _Callable[[ICredentialProviderCredential,  # credential
                                _type.DWORD,  # fieldID
                                _enum.CREDENTIAL_PROVIDER_CREDENTIAL_FIELD_OPTIONS],  # options
                               _type.HRESULT]


class ICredentialProviderUser(_Unknwnbase.IUnknown):
    GetSid: _Callable[[_Pointer[_type.LPWSTR]],  # sid
                      _type.HRESULT]
    GetProviderID: _Callable[[_Pointer[_struct.GUID]],  # providerID
                             _type.HRESULT]
    GetStringValue: _Callable[[_Pointer[_struct.PROPERTYKEY],  # key
                               _Pointer[_type.LPWSTR]],  # stringValue
                              _type.HRESULT]
    GetValue: _Callable[[_Pointer[_struct.PROPERTYKEY],  # key
                         _Pointer[_struct.PROPVARIANT]],  # value
                        _type.HRESULT]


class ICredentialProviderUserArray(_Unknwnbase.IUnknown):
    SetProviderFilter: _Callable[[_Pointer[_struct.GUID]],  # guidProviderToFilterTo
                                 _type.HRESULT]
    GetAccountOptions: _Callable[[_Pointer[_enum.CREDENTIAL_PROVIDER_ACCOUNT_OPTIONS]],  # credentialProviderAccountOptions
                                 _type.HRESULT]
    GetCount: _Callable[[_Pointer[_type.DWORD]],  # userCount
                        _type.HRESULT]
    GetAt: _Callable[[_type.DWORD,  # userIndex
                      _Pointer[ICredentialProviderUser]],  # user
                     _type.HRESULT]


class ICredentialProviderSetUserArray(_Unknwnbase.IUnknown):
    SetUserArray: _Callable[[ICredentialProviderUserArray],  # users
                            _type.HRESULT]
