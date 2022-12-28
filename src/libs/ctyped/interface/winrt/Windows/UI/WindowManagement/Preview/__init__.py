from __future__ import annotations as _

from typing import Callable as _Callable

from ... import WindowManagement as _Windows_UI_WindowManagement
from ..... import inspectable as _inspectable
from ....... import struct as _struct
from ....... import type as _type


class IWindowManagementPreview(_inspectable.IInspectable):
    pass


class IWindowManagementPreviewStatics(_inspectable.IInspectable):
    SetPreferredMinSize: _Callable[[_Windows_UI_WindowManagement.IAppWindow,  # window
                                    _struct.Windows.Foundation.Size],  # preferredFrameMinSize
                                   _type.HRESULT]

    _factory = True
