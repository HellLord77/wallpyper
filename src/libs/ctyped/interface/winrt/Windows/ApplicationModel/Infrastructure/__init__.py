from __future__ import annotations

from typing import Callable as _Callable

from ...UI import Core as _Windows_UI_Core
from .... import inspectable as _inspectable
from ...... import type as _type
from ......_utils import _Pointer


class ISetWindowWithWindowFactory(_inspectable.IInspectable):
    SetWindow: _Callable[[_Windows_UI_Core.ICoreWindowFactory,  # windowFactory
                          _Pointer[_Windows_UI_Core.ICoreWindow]],  # window
                         _type.HRESULT]
