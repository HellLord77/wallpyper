from __future__ import annotations

from typing import Callable as _Callable

from ... import Input as _Windows_UI_Input
from ... import WindowManagement as _Windows_UI_WindowManagement
from ..... import inspectable as _inspectable
from ....... import type as _type
from ......._utils import _Pointer


class IInputActivationListenerPreviewStatics(_inspectable.IInspectable, factory=True):
    CreateForApplicationWindow: _Callable[[_Windows_UI_WindowManagement.IAppWindow,  # window
                                           _Pointer[_Windows_UI_Input.IInputActivationListener]],  # result
                                          _type.HRESULT]
