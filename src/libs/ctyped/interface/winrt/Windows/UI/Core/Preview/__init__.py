from __future__ import annotations as _

from typing import Callable as _Callable

from ... import WindowManagement as _Windows_UI_WindowManagement
from .... import Foundation as _Windows_Foundation
from ..... import inspectable as _inspectable
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class ICoreAppWindowPreview(_inspectable.IInspectable):
    pass


class ICoreAppWindowPreviewStatics(_inspectable.IInspectable):
    GetIdFromWindow: _Callable[[_Windows_UI_WindowManagement.IAppWindow,  # window
                                _Pointer[_type.INT32]],  # result
                               _type.HRESULT]

    _factory = True


class ISystemNavigationCloseRequestedPreviewEventArgs(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class ISystemNavigationManagerPreview(_inspectable.IInspectable):
    add_CloseRequested: _Callable[[_Windows_Foundation.IEventHandler[ISystemNavigationCloseRequestedPreviewEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_CloseRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]


class ISystemNavigationManagerPreviewStatics(_inspectable.IInspectable):
    GetForCurrentView: _Callable[[_Pointer[ISystemNavigationManagerPreview]],  # loader
                                 _type.HRESULT]

    _factory = True
