from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from .....um import Unknwnbase as _Unknwnbase
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class _IUICommandInvokedHandler:
    Invoke: _Callable[[IUICommand],  # command
                      _type.HRESULT]


class IUICommandInvokedHandler(_IUICommandInvokedHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IUICommandInvokedHandler_impl(_IUICommandInvokedHandler, _Unknwnbase.IUnknown_impl):
    pass


class IMessageDialog(_inspectable.IInspectable):
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Title: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Commands: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IUICommand]]],  # value
                            _type.HRESULT]
    get_DefaultCommandIndex: _Callable[[_Pointer[_type.UINT32]],  # value
                                       _type.HRESULT]
    put_DefaultCommandIndex: _Callable[[_type.UINT32],  # value
                                       _type.HRESULT]
    get_CancelCommandIndex: _Callable[[_Pointer[_type.UINT32]],  # value
                                      _type.HRESULT]
    put_CancelCommandIndex: _Callable[[_type.UINT32],  # value
                                      _type.HRESULT]
    get_Content: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    put_Content: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    ShowAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IUICommand]]],  # messageDialogAsyncOperation
                         _type.HRESULT]
    get_Options: _Callable[[_Pointer[_enum.Windows.UI.Popups.MessageDialogOptions]],  # value
                           _type.HRESULT]
    put_Options: _Callable[[_enum.Windows.UI.Popups.MessageDialogOptions],  # value
                           _type.HRESULT]


class IMessageDialogFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.HSTRING,  # content
                       _Pointer[IMessageDialog]],  # messageDialog
                      _type.HRESULT]
    CreateWithTitle: _Callable[[_type.HSTRING,  # content
                                _type.HSTRING,  # title
                                _Pointer[IMessageDialog]],  # messageDialog
                               _type.HRESULT]

    _factory = True


class IPopupMenu(_inspectable.IInspectable):
    get_Commands: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IUICommand]]],  # value
                            _type.HRESULT]
    ShowAsync: _Callable[[_struct.Windows.Foundation.Point,  # invocationPoint
                          _Pointer[_Windows_Foundation.IAsyncOperation[IUICommand]]],  # asyncOperation
                         _type.HRESULT]
    ShowAsyncWithRect: _Callable[[_struct.Windows.Foundation.Rect,  # selection
                                  _Pointer[_Windows_Foundation.IAsyncOperation[IUICommand]]],  # asyncOperation
                                 _type.HRESULT]
    ShowAsyncWithRectAndPlacement: _Callable[[_struct.Windows.Foundation.Rect,  # selection
                                              _enum.Windows.UI.Popups.Placement,  # preferredPlacement
                                              _Pointer[_Windows_Foundation.IAsyncOperation[IUICommand]]],  # asyncOperation
                                             _type.HRESULT]


class IUICommand(_inspectable.IInspectable):
    get_Label: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Label: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Invoked: _Callable[[_Pointer[IUICommandInvokedHandler]],  # value
                           _type.HRESULT]
    put_Invoked: _Callable[[IUICommandInvokedHandler],  # value
                           _type.HRESULT]
    get_Id: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                      _type.HRESULT]
    put_Id: _Callable[[_inspectable.IInspectable],  # value
                      _type.HRESULT]


class IUICommandFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.HSTRING,  # label
                       _Pointer[IUICommand]],  # instance
                      _type.HRESULT]
    CreateWithHandler: _Callable[[_type.HSTRING,  # label
                                  IUICommandInvokedHandler,  # action
                                  _Pointer[IUICommand]],  # instance
                                 _type.HRESULT]
    CreateWithHandlerAndId: _Callable[[_type.HSTRING,  # label
                                       IUICommandInvokedHandler,  # action
                                       _inspectable.IInspectable,  # commandId
                                       _Pointer[IUICommand]],  # instance
                                      _type.HRESULT]

    _factory = True
