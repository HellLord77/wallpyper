from __future__ import annotations

from typing import Callable as _Callable

from ....Graphics import Effects as _Windows_Graphics_Effects
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import type as _type
from ......._utils import _Pointer


class ISceneLightingEffect(_inspectable.IInspectable):
    get_AmbientAmount: _Callable[[_Pointer[_type.FLOAT]],  # value
                                 _type.HRESULT]
    put_AmbientAmount: _Callable[[_type.FLOAT],  # value
                                 _type.HRESULT]
    get_DiffuseAmount: _Callable[[_Pointer[_type.FLOAT]],  # value
                                 _type.HRESULT]
    put_DiffuseAmount: _Callable[[_type.FLOAT],  # value
                                 _type.HRESULT]
    get_NormalMapSource: _Callable[[_Pointer[_Windows_Graphics_Effects.IGraphicsEffectSource]],  # value
                                   _type.HRESULT]
    put_NormalMapSource: _Callable[[_Windows_Graphics_Effects.IGraphicsEffectSource],  # value
                                   _type.HRESULT]
    get_SpecularAmount: _Callable[[_Pointer[_type.FLOAT]],  # value
                                  _type.HRESULT]
    put_SpecularAmount: _Callable[[_type.FLOAT],  # value
                                  _type.HRESULT]
    get_SpecularShine: _Callable[[_Pointer[_type.FLOAT]],  # value
                                 _type.HRESULT]
    put_SpecularShine: _Callable[[_type.FLOAT],  # value
                                 _type.HRESULT]


class ISceneLightingEffect2(_inspectable.IInspectable):
    get_ReflectanceModel: _Callable[[_Pointer[_enum.Windows.UI.Composition.Effects.SceneLightingEffectReflectanceModel]],  # value
                                    _type.HRESULT]
    put_ReflectanceModel: _Callable[[_enum.Windows.UI.Composition.Effects.SceneLightingEffectReflectanceModel],  # value
                                    _type.HRESULT]
