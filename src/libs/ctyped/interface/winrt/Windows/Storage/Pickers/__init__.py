from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import Storage as _Windows_Storage
from ... import System as _Windows_System
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import type as _type
from ......_utils import _Pointer


class IFileOpenPicker(_inspectable.IInspectable):
    get_ViewMode: _Callable[[_Pointer[_enum.Windows.Storage.Pickers.PickerViewMode]],  # value
                            _type.HRESULT]
    put_ViewMode: _Callable[[_enum.Windows.Storage.Pickers.PickerViewMode],  # value
                            _type.HRESULT]
    get_SettingsIdentifier: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    put_SettingsIdentifier: _Callable[[_type.HSTRING],  # value
                                      _type.HRESULT]
    get_SuggestedStartLocation: _Callable[[_Pointer[_enum.Windows.Storage.Pickers.PickerLocationId]],  # value
                                          _type.HRESULT]
    put_SuggestedStartLocation: _Callable[[_enum.Windows.Storage.Pickers.PickerLocationId],  # value
                                          _type.HRESULT]
    get_CommitButtonText: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    put_CommitButtonText: _Callable[[_type.HSTRING],  # value
                                    _type.HRESULT]
    get_FileTypeFilter: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                  _type.HRESULT]
    PickSingleFileAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage.IStorageFile]]],  # operation
                                   _type.HRESULT]
    PickMultipleFilesAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_Storage.IStorageFile]]]],  # operation
                                      _type.HRESULT]


class IFileOpenPicker2(_inspectable.IInspectable):
    ContinuationData: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                                _type.HRESULT]
    PickSingleFileAndContinue: _Callable[[],
                                         _type.HRESULT]
    PickMultipleFilesAndContinue: _Callable[[],
                                            _type.HRESULT]


class IFileOpenPicker3(_inspectable.IInspectable):
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]


class IFileOpenPickerStatics(_inspectable.IInspectable):
    ResumePickSingleFileAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage.IStorageFile]]],  # operation
                                         _type.HRESULT]

    _factory = True


class IFileOpenPickerStatics2(_inspectable.IInspectable):
    CreateForUser: _Callable[[_Windows_System.IUser,  # user
                              _Pointer[IFileOpenPicker]],  # result
                             _type.HRESULT]

    _factory = True


class IFileOpenPickerWithOperationId(_inspectable.IInspectable):
    PickSingleFileAsync: _Callable[[_type.HSTRING,  # pickerOperationId
                                    _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage.IStorageFile]]],  # operation
                                   _type.HRESULT]


class IFileSavePicker(_inspectable.IInspectable):
    get_SettingsIdentifier: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    put_SettingsIdentifier: _Callable[[_type.HSTRING],  # value
                                      _type.HRESULT]
    get_SuggestedStartLocation: _Callable[[_Pointer[_enum.Windows.Storage.Pickers.PickerLocationId]],  # value
                                          _type.HRESULT]
    put_SuggestedStartLocation: _Callable[[_enum.Windows.Storage.Pickers.PickerLocationId],  # value
                                          _type.HRESULT]
    get_CommitButtonText: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    put_CommitButtonText: _Callable[[_type.HSTRING],  # value
                                    _type.HRESULT]
    get_FileTypeChoices: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, _Windows_Foundation_Collections.IVector[_type.HSTRING]]]],  # value
                                   _type.HRESULT]
    get_DefaultFileExtension: _Callable[[_Pointer[_type.HSTRING]],  # value
                                        _type.HRESULT]
    put_DefaultFileExtension: _Callable[[_type.HSTRING],  # value
                                        _type.HRESULT]
    get_SuggestedSaveFile: _Callable[[_Pointer[_Windows_Storage.IStorageFile]],  # value
                                     _type.HRESULT]
    put_SuggestedSaveFile: _Callable[[_Windows_Storage.IStorageFile],  # value
                                     _type.HRESULT]
    get_SuggestedFileName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    put_SuggestedFileName: _Callable[[_type.HSTRING],  # value
                                     _type.HRESULT]
    PickSaveFileAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage.IStorageFile]]],  # operation
                                 _type.HRESULT]


class IFileSavePicker2(_inspectable.IInspectable):
    get_ContinuationData: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                                    _type.HRESULT]
    PickSaveFileAndContinue: _Callable[[],
                                       _type.HRESULT]


class IFileSavePicker3(_inspectable.IInspectable):
    get_EnterpriseId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    put_EnterpriseId: _Callable[[_type.HSTRING],  # value
                                _type.HRESULT]


class IFileSavePicker4(_inspectable.IInspectable):
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]


class IFileSavePickerStatics(_inspectable.IInspectable):
    CreateForUser: _Callable[[_Windows_System.IUser,  # user
                              _Pointer[IFileSavePicker]],  # result
                             _type.HRESULT]

    _factory = True


class IFolderPicker(_inspectable.IInspectable):
    get_ViewMode: _Callable[[_Pointer[_enum.Windows.Storage.Pickers.PickerViewMode]],  # value
                            _type.HRESULT]
    put_ViewMode: _Callable[[_enum.Windows.Storage.Pickers.PickerViewMode],  # value
                            _type.HRESULT]
    get_SettingsIdentifier: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    put_SettingsIdentifier: _Callable[[_type.HSTRING],  # value
                                      _type.HRESULT]
    get_SuggestedStartLocation: _Callable[[_Pointer[_enum.Windows.Storage.Pickers.PickerLocationId]],  # value
                                          _type.HRESULT]
    put_SuggestedStartLocation: _Callable[[_enum.Windows.Storage.Pickers.PickerLocationId],  # value
                                          _type.HRESULT]
    get_CommitButtonText: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    put_CommitButtonText: _Callable[[_type.HSTRING],  # value
                                    _type.HRESULT]
    get_FileTypeFilter: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                  _type.HRESULT]
    PickSingleFolderAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage.IStorageFolder]]],  # operation
                                     _type.HRESULT]


class IFolderPicker2(_inspectable.IInspectable):
    get_ContinuationData: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                                    _type.HRESULT]
    PickFolderAndContinue: _Callable[[],
                                     _type.HRESULT]


class IFolderPicker3(_inspectable.IInspectable):
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]


class IFolderPickerStatics(_inspectable.IInspectable):
    CreateForUser: _Callable[[_Windows_System.IUser,  # user
                              _Pointer[IFolderPicker]],  # result
                             _type.HRESULT]

    _factory = True
