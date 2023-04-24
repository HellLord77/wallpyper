from __future__ import annotations

from typing import Callable as _Callable

from ... import Composition as _Windows_UI_Composition
from .... import Foundation as _Windows_Foundation
from ..... import inspectable as _inspectable
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class ICompositorController(_inspectable.IInspectable):
    get_Compositor: _Callable[[_Pointer[_Windows_UI_Composition.ICompositor]],  # value
                              _type.HRESULT]
    Commit: _Callable[[],
                      _type.HRESULT]
    EnsurePreviousCommitCompletedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                                  _type.HRESULT]
    add_CommitNeeded: _Callable[[_Windows_Foundation.ITypedEventHandler[ICompositorController, _inspectable.IInspectable],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_CommitNeeded: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
