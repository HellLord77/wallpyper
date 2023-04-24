from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from .... import inspectable as _inspectable
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IScreenReaderPositionChangedEventArgs(_inspectable.IInspectable):
    get_ScreenPositionInRawPixels: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                                             _type.HRESULT]
    get_IsReadingText: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]


class IScreenReaderService(_inspectable.IInspectable):
    get_CurrentScreenReaderPosition: _Callable[[_Pointer[IScreenReaderPositionChangedEventArgs]],  # value
                                               _type.HRESULT]
    add_ScreenReaderPositionChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IScreenReaderService, IScreenReaderPositionChangedEventArgs],  # handler
                                                _Pointer[_struct.EventRegistrationToken]],  # token
                                               _type.HRESULT]
    remove_ScreenReaderPositionChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                  _type.HRESULT]
