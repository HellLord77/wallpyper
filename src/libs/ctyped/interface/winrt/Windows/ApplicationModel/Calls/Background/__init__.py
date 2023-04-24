from __future__ import annotations

from typing import Callable as _Callable

from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IPhoneCallBlockedTriggerDetails(_inspectable.IInspectable):
    get_PhoneNumber: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_LineId: _Callable[[_Pointer[_struct.GUID]],  # value
                          _type.HRESULT]
    get_CallBlockedReason: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Calls.Background.PhoneCallBlockedReason]],  # value
                                     _type.HRESULT]


class IPhoneCallOriginDataRequestTriggerDetails(_inspectable.IInspectable):
    RequestId: _Callable[[_Pointer[_struct.GUID]],  # result
                         _type.HRESULT]
    PhoneNumber: _Callable[[_Pointer[_type.HSTRING]],  # result
                           _type.HRESULT]


class IPhoneIncomingCallDismissedTriggerDetails(_inspectable.IInspectable):
    LineId: _Callable[[_Pointer[_struct.GUID]],  # value
                      _type.HRESULT]
    PhoneNumber: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    DismissalTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    TextReplyMessage: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    Reason: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Calls.Background.PhoneIncomingCallDismissedReason]],  # value
                      _type.HRESULT]


class IPhoneIncomingCallNotificationTriggerDetails(_inspectable.IInspectable):
    get_LineId: _Callable[[_Pointer[_struct.GUID]],  # value
                          _type.HRESULT]
    get_CallId: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]


class IPhoneLineChangedTriggerDetails(_inspectable.IInspectable):
    get_LineId: _Callable[[_Pointer[_struct.GUID]],  # result
                          _type.HRESULT]
    get_ChangeType: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Calls.Background.PhoneLineChangeKind]],  # result
                              _type.HRESULT]
    HasLinePropertyChanged: _Callable[[_enum.Windows.ApplicationModel.Calls.Background.PhoneLineProperties,  # lineProperty
                                       _Pointer[_type.boolean]],  # result
                                      _type.HRESULT]


class IPhoneNewVoicemailMessageTriggerDetails(_inspectable.IInspectable):
    get_LineId: _Callable[[_Pointer[_struct.GUID]],  # result
                          _type.HRESULT]
    get_VoicemailCount: _Callable[[_Pointer[_type.INT32]],  # result
                                  _type.HRESULT]
    get_OperatorMessage: _Callable[[_Pointer[_type.HSTRING]],  # result
                                   _type.HRESULT]
