from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class ISystemUpdateItem(_inspectable.IInspectable):
    get_State: _Callable[[_Pointer[_enum.Windows.System.Update.SystemUpdateItemState]],  # value
                         _type.HRESULT]
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_Revision: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    get_DownloadProgress: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]
    get_InstallProgress: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                   _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class ISystemUpdateLastErrorInfo(_inspectable.IInspectable):
    get_State: _Callable[[_Pointer[_enum.Windows.System.Update.SystemUpdateManagerState]],  # value
                         _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]
    get_IsInteractive: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]


class ISystemUpdateManagerStatics(_inspectable.IInspectable, factory=True):
    IsSupported: _Callable[[_Pointer[_type.boolean]],  # result
                           _type.HRESULT]
    get_State: _Callable[[_Pointer[_enum.Windows.System.Update.SystemUpdateManagerState]],  # value
                         _type.HRESULT]
    add_StateChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_StateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    get_DownloadProgress: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]
    get_InstallProgress: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                   _type.HRESULT]
    get_UserActiveHoursStart: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                        _type.HRESULT]
    get_UserActiveHoursEnd: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                      _type.HRESULT]
    get_UserActiveHoursMax: _Callable[[_Pointer[_type.INT32]],  # value
                                      _type.HRESULT]
    TrySetUserActiveHours: _Callable[[_struct.Windows.Foundation.TimeSpan,  # start
                                      _struct.Windows.Foundation.TimeSpan,  # end
                                      _Pointer[_type.boolean]],  # result
                                     _type.HRESULT]
    get_LastUpdateCheckTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                       _type.HRESULT]
    get_LastUpdateInstallTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                         _type.HRESULT]
    get_LastErrorInfo: _Callable[[_Pointer[ISystemUpdateLastErrorInfo]],  # value
                                 _type.HRESULT]
    GetAutomaticRebootBlockIds: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # result
                                          _type.HRESULT]
    BlockAutomaticRebootAsync: _Callable[[_type.HSTRING,  # lockId
                                          _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                         _type.HRESULT]
    UnblockAutomaticRebootAsync: _Callable[[_type.HSTRING,  # lockId
                                            _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                           _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]
    GetUpdateItems: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[ISystemUpdateItem]]],  # result
                              _type.HRESULT]
    get_AttentionRequiredReason: _Callable[[_Pointer[_enum.Windows.System.Update.SystemUpdateAttentionRequiredReason]],  # value
                                           _type.HRESULT]
    SetFlightRing: _Callable[[_type.HSTRING,  # flightRing
                              _Pointer[_type.boolean]],  # result
                             _type.HRESULT]
    GetFlightRing: _Callable[[_Pointer[_type.HSTRING]],  # result
                             _type.HRESULT]
    StartInstall: _Callable[[_enum.Windows.System.Update.SystemUpdateStartInstallAction],  # action
                            _type.HRESULT]
    RebootToCompleteInstall: _Callable[[],
                                       _type.HRESULT]
    StartCancelUpdates: _Callable[[],
                                  _type.HRESULT]
