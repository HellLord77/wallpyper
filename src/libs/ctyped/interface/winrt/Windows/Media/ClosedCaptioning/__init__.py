from __future__ import annotations as _

from typing import Callable as _Callable

from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IClosedCaptionPropertiesStatics(_inspectable.IInspectable, factory=True):
    get_FontColor: _Callable[[_Pointer[_enum.Windows.Media.ClosedCaptioning.ClosedCaptionColor]],  # value
                             _type.HRESULT]
    get_ComputedFontColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                     _type.HRESULT]
    get_FontOpacity: _Callable[[_Pointer[_enum.Windows.Media.ClosedCaptioning.ClosedCaptionOpacity]],  # value
                               _type.HRESULT]
    get_FontSize: _Callable[[_Pointer[_enum.Windows.Media.ClosedCaptioning.ClosedCaptionSize]],  # value
                            _type.HRESULT]
    get_FontStyle: _Callable[[_Pointer[_enum.Windows.Media.ClosedCaptioning.ClosedCaptionStyle]],  # value
                             _type.HRESULT]
    get_FontEffect: _Callable[[_Pointer[_enum.Windows.Media.ClosedCaptioning.ClosedCaptionEdgeEffect]],  # value
                              _type.HRESULT]
    get_BackgroundColor: _Callable[[_Pointer[_enum.Windows.Media.ClosedCaptioning.ClosedCaptionColor]],  # value
                                   _type.HRESULT]
    get_ComputedBackgroundColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                           _type.HRESULT]
    get_BackgroundOpacity: _Callable[[_Pointer[_enum.Windows.Media.ClosedCaptioning.ClosedCaptionOpacity]],  # value
                                     _type.HRESULT]
    get_RegionColor: _Callable[[_Pointer[_enum.Windows.Media.ClosedCaptioning.ClosedCaptionColor]],  # value
                               _type.HRESULT]
    get_ComputedRegionColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                       _type.HRESULT]
    get_RegionOpacity: _Callable[[_Pointer[_enum.Windows.Media.ClosedCaptioning.ClosedCaptionOpacity]],  # value
                                 _type.HRESULT]
