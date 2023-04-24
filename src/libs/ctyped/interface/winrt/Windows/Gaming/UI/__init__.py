from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IGameBarStatics(_inspectable.IInspectable):
    add_VisibilityChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_VisibilityChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    add_IsInputRedirectedChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                             _Pointer[_struct.EventRegistrationToken]],  # token
                                            _type.HRESULT]
    remove_IsInputRedirectedChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                               _type.HRESULT]
    get_Visible: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_IsInputRedirected: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]

    _factory = True


class IGameChatMessageReceivedEventArgs(_inspectable.IInspectable):
    get_AppId: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_AppDisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_SenderName: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_Message: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Origin: _Callable[[_Pointer[_enum.Windows.Gaming.UI.GameChatMessageOrigin]],  # value
                          _type.HRESULT]


class IGameChatOverlay(_inspectable.IInspectable):
    get_DesiredPosition: _Callable[[_Pointer[_enum.Windows.Gaming.UI.GameChatOverlayPosition]],  # value
                                   _type.HRESULT]
    put_DesiredPosition: _Callable[[_enum.Windows.Gaming.UI.GameChatOverlayPosition],  # value
                                   _type.HRESULT]
    AddMessage: _Callable[[_type.HSTRING,  # sender
                           _type.HSTRING,  # message
                           _enum.Windows.Gaming.UI.GameChatMessageOrigin],  # origin
                          _type.HRESULT]


class IGameChatOverlayMessageSource(_inspectable.IInspectable):
    add_MessageReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[IGameChatOverlayMessageSource, IGameChatMessageReceivedEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_MessageReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    SetDelayBeforeClosingAfterMessageReceived: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                                         _type.HRESULT]


class IGameChatOverlayStatics(_inspectable.IInspectable):
    GetDefault: _Callable[[_Pointer[IGameChatOverlay]],  # value
                          _type.HRESULT]

    _factory = True


class IGameUIProviderActivatedEventArgs(_inspectable.IInspectable):
    get_GameUIArgs: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                              _type.HRESULT]
    ReportCompleted: _Callable[[_Windows_Foundation_Collections.IPropertySet],  # results
                               _type.HRESULT]
