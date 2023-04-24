from __future__ import annotations

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class ICoreSelectionChangedEventArgs(_inspectable.IInspectable):
    get_Start: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    get_Length: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]


class ICoreTextChangedEventArgs(_inspectable.IInspectable):
    get_Start: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    get_OldLength: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    get_NewText: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]


class ICoreWindowKeyboardInput(_inspectable.IInspectable):
    get_IsKeyboardInputEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_IsKeyboardInputEnabled: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    get_KeyboardInputBuffer: _Callable[[_Pointer[IKeyboardInputBuffer]],  # value
                                       _type.HRESULT]
    put_KeyboardInputBuffer: _Callable[[IKeyboardInputBuffer],  # value
                                       _type.HRESULT]


class IKeyboardInputBuffer(_inspectable.IInspectable):
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Text: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_SelectionStart: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]
    get_SelectionLength: _Callable[[_Pointer[_type.UINT32]],  # value
                                   _type.HRESULT]
    Select: _Callable[[_type.UINT32,  # start
                       _type.UINT32],  # length
                      _type.HRESULT]
    SelectFromTap: _Callable[[_type.UINT32],  # characterIndex
                             _type.HRESULT]
    get_InputScope: _Callable[[_Pointer[_enum.Windows.Phone.UI.Core.CoreInputScope]],  # value
                              _type.HRESULT]
    put_InputScope: _Callable[[_enum.Windows.Phone.UI.Core.CoreInputScope],  # value
                              _type.HRESULT]
    add_TextChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IKeyboardInputBuffer, ICoreTextChangedEventArgs],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # cookie
                               _type.HRESULT]
    remove_TextChanged: _Callable[[_struct.EventRegistrationToken],  # cookie
                                  _type.HRESULT]
    add_SelectionChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IKeyboardInputBuffer, ICoreSelectionChangedEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # cookie
                                    _type.HRESULT]
    remove_SelectionChanged: _Callable[[_struct.EventRegistrationToken],  # cookie
                                       _type.HRESULT]
