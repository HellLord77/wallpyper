from __future__ import annotations as _

from typing import Callable as _Callable

from .... import Composition as _Windows_UI_Composition
from ...... import inspectable as _inspectable
from ........ import struct as _struct
from ........ import type as _type
from ........_utils import _Pointer


class IPalmRejectionDelayZonePreview(_inspectable.IInspectable):
    pass


class IPalmRejectionDelayZonePreviewStatics(_inspectable.IInspectable):
    CreateForVisual: _Callable[[_Windows_UI_Composition.IVisual,  # inputPanelVisual
                                _struct.Windows.Foundation.Rect,  # inputPanelRect
                                _Pointer[IPalmRejectionDelayZonePreview]],  # result
                               _type.HRESULT]
    CreateForVisualWithViewportClip: _Callable[[_Windows_UI_Composition.IVisual,  # inputPanelVisual
                                                _struct.Windows.Foundation.Rect,  # inputPanelRect
                                                _Windows_UI_Composition.IVisual,  # viewportVisual
                                                _struct.Windows.Foundation.Rect,  # viewportRect
                                                _Pointer[IPalmRejectionDelayZonePreview]],  # result
                                               _type.HRESULT]

    _factory = True
