from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Composition as _Microsoft_UI_Composition
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import type as _type
from ......._utils import _Pointer


class ICompositionDebugHeatMaps(_inspectable.IInspectable):
    Hide: _Callable[[_Microsoft_UI_Composition.IVisual],  # subtree
                    _type.HRESULT]
    ShowMemoryUsage: _Callable[[_Microsoft_UI_Composition.IVisual],  # subtree
                               _type.HRESULT]
    ShowOverdraw: _Callable[[_Microsoft_UI_Composition.IVisual,  # subtree
                             _enum.Microsoft.UI.Composition.Diagnostics.CompositionDebugOverdrawContentKinds],  # contentKinds
                            _type.HRESULT]
    ShowRedraw: _Callable[[_Microsoft_UI_Composition.IVisual],  # subtree
                          _type.HRESULT]


class ICompositionDebugSettings(_inspectable.IInspectable):
    get_HeatMaps: _Callable[[_Pointer[ICompositionDebugHeatMaps]],  # value
                            _type.HRESULT]


class ICompositionDebugSettingsStatics(_inspectable.IInspectable, factory=True):
    TryGetSettings: _Callable[[_Microsoft_UI_Composition.ICompositor,  # compositor
                               _Pointer[ICompositionDebugSettings]],  # result
                              _type.HRESULT]
