from __future__ import annotations as _

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from .... import Storage as _Windows_Storage
from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IFileOpenPickerUI(_inspectable.IInspectable):
    AddFile: _Callable[[_type.HSTRING,  # id
                        _Windows_Storage.IStorageFile,  # file
                        _Pointer[_enum.Windows.Storage.Pickers.Provider.AddFileResult]],  # addResult
                       _type.HRESULT]
    RemoveFile: _Callable[[_type.HSTRING],  # id
                          _type.HRESULT]
    ContainsFile: _Callable[[_type.HSTRING,  # id
                             _Pointer[_type.boolean]],  # isContained
                            _type.HRESULT]
    CanAddFile: _Callable[[_Windows_Storage.IStorageFile,  # file
                           _Pointer[_type.boolean]],  # canAdd
                          _type.HRESULT]
    get_AllowedFileTypes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                    _type.HRESULT]
    get_SelectionMode: _Callable[[_Pointer[_enum.Windows.Storage.Pickers.Provider.FileSelectionMode]],  # value
                                 _type.HRESULT]
    get_SettingsIdentifier: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Title: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    FileRemoved: _Callable[[_struct.EventRegistrationToken],  # token
                           _type.HRESULT]
    add_Closing: _Callable[[_Windows_Foundation.ITypedEventHandler[IFileOpenPickerUI, IPickerClosingEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Closing: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]


class IFileRemovedEventArgs(_inspectable.IInspectable):
    Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                  _type.HRESULT]


class IFileSavePickerUI(_inspectable.IInspectable):
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Title: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_AllowedFileTypes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                    _type.HRESULT]
    get_SettingsIdentifier: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_FileName: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    TrySetFileName: _Callable[[_type.HSTRING,  # value
                               _Pointer[_enum.Windows.Storage.Pickers.Provider.SetFileNameResult]],  # result
                              _type.HRESULT]
    add_FileNameChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IFileSavePickerUI, _inspectable.IInspectable],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_FileNameChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    add_TargetFileRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IFileSavePickerUI, ITargetFileRequestedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_TargetFileRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]


class IPickerClosingDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class IPickerClosingEventArgs(_inspectable.IInspectable):
    get_ClosingOperation: _Callable[[_Pointer[IPickerClosingOperation]],  # value
                                    _type.HRESULT]
    get_IsCanceled: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]


class IPickerClosingOperation(_inspectable.IInspectable):
    GetDeferral: _Callable[[_Pointer[IPickerClosingDeferral]],  # value
                           _type.HRESULT]
    get_Deadline: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                            _type.HRESULT]


class ITargetFileRequest(_inspectable.IInspectable):
    get_TargetFile: _Callable[[_Pointer[_Windows_Storage.IStorageFile]],  # value
                              _type.HRESULT]
    put_TargetFile: _Callable[[_Windows_Storage.IStorageFile],  # value
                              _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[ITargetFileRequestDeferral]],  # value
                           _type.HRESULT]


class ITargetFileRequestDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class ITargetFileRequestedEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[ITargetFileRequest]],  # value
                           _type.HRESULT]
