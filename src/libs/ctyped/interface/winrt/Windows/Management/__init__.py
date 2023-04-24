from __future__ import annotations

from typing import Callable as _Callable

from .. import Foundation as _Windows_Foundation
from ..Foundation import Collections as _Windows_Foundation_Collections
from ... import inspectable as _inspectable
from ..... import enum as _enum
from ..... import type as _type
from ....._utils import _Pointer


class IMdmAlert(_inspectable.IInspectable):
    get_Data: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Data: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_Format: _Callable[[_Pointer[_enum.Windows.Management.MdmAlertDataType]],  # value
                          _type.HRESULT]
    put_Format: _Callable[[_enum.Windows.Management.MdmAlertDataType],  # value
                          _type.HRESULT]
    get_Mark: _Callable[[_Pointer[_enum.Windows.Management.MdmAlertMark]],  # value
                        _type.HRESULT]
    put_Mark: _Callable[[_enum.Windows.Management.MdmAlertMark],  # value
                        _type.HRESULT]
    get_Source: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    put_Source: _Callable[[_type.HSTRING],  # value
                          _type.HRESULT]
    get_Status: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    get_Target: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    put_Target: _Callable[[_type.HSTRING],  # value
                          _type.HRESULT]
    get_Type: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Type: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]


class IMdmSession(_inspectable.IInspectable):
    get_Alerts: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMdmAlert]]],  # value
                          _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_State: _Callable[[_Pointer[_enum.Windows.Management.MdmSessionState]],  # value
                         _type.HRESULT]
    AttachAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # action
                           _type.HRESULT]
    Delete: _Callable[[],
                      _type.HRESULT]
    StartAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # action
                          _type.HRESULT]
    StartWithAlertsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[IMdmAlert],  # alerts
                                     _Pointer[_Windows_Foundation.IAsyncAction]],  # action
                                    _type.HRESULT]


class IMdmSessionManagerStatics(_inspectable.IInspectable):
    get_SessionIds: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                              _type.HRESULT]
    TryCreateSession: _Callable[[_Pointer[IMdmSession]],  # result
                                _type.HRESULT]
    DeleteSessionById: _Callable[[_type.HSTRING],  # sessionId
                                 _type.HRESULT]
    GetSessionById: _Callable[[_type.HSTRING,  # sessionId
                               _Pointer[IMdmSession]],  # result
                              _type.HRESULT]

    _factory = True
