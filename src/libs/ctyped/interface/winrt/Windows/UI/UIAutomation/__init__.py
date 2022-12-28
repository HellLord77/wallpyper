from __future__ import annotations as _

from typing import Callable as _Callable

from .... import inspectable as _inspectable
from ...... import type as _type
from ......_utils import _Pointer


class IAutomationConnection(_inspectable.IInspectable):
    get_IsRemoteSystem: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    get_AppUserModelId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_ExecutableFileName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]


class IAutomationConnectionBoundObject(_inspectable.IInspectable):
    get_Connection: _Callable[[_Pointer[IAutomationConnection]],  # value
                              _type.HRESULT]


class IAutomationElement(_inspectable.IInspectable):
    get_IsRemoteSystem: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    get_AppUserModelId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_ExecutableFileName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]


class IAutomationTextRange(_inspectable.IInspectable):
    pass
