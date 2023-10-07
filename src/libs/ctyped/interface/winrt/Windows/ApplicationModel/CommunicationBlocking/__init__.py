from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import type as _type
from ......_utils import _Pointer


class ICommunicationBlockingAccessManagerStatics(_inspectable.IInspectable, factory=True):
    get_IsBlockingActive: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    IsBlockedNumberAsync: _Callable[[_type.HSTRING,  # number
                                     _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                    _type.HRESULT]
    ShowBlockNumbersUI: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # phoneNumbers
                                   _Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    ShowUnblockNumbersUI: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # phoneNumbers
                                     _Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    ShowBlockedCallsUI: _Callable[[],
                                  _type.HRESULT]
    ShowBlockedMessagesUI: _Callable[[],
                                     _type.HRESULT]


class ICommunicationBlockingAppManagerStatics(_inspectable.IInspectable, factory=True):
    get_IsCurrentAppActiveBlockingApp: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]
    ShowCommunicationBlockingSettingsUI: _Callable[[],
                                                   _type.HRESULT]


class ICommunicationBlockingAppManagerStatics2(_inspectable.IInspectable, factory=True):
    RequestSetAsActiveBlockingAppAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                                  _type.HRESULT]
