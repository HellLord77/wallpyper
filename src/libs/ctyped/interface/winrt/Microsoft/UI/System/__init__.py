from __future__ import annotations as _

from typing import Callable as _Callable

from .... import inspectable as _inspectable
from ....Windows import Foundation as _Windows_Foundation
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IThemeSettings(_inspectable.IInspectable):
    add_Changed: _Callable[[_Windows_Foundation.ITypedEventHandler[IThemeSettings, _inspectable.IInspectable],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Changed: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    get_HighContrast: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_HighContrastScheme: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]


class IThemeSettingsStatics(_inspectable.IInspectable, factory=True):
    CreateForWindowId: _Callable[[_struct.Microsoft.UI.WindowId,  # windowId
                                  _Pointer[IThemeSettings]],  # result
                                 _type.HRESULT]
