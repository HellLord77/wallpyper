from __future__ import annotations as _

from typing import Callable as _Callable

from ... import inspectable as _inspectable
from ..... import struct as _struct
from ..... import type as _type
from ....._utils import _Pointer


class IColorHelper(_inspectable.IInspectable):
    pass


class IColorHelperStatics(_inspectable.IInspectable):
    FromArgb: _Callable[[_type.BYTE,  # a
                         _type.BYTE,  # r
                         _type.BYTE,  # g
                         _type.BYTE,  # b
                         _Pointer[_struct.Windows.UI.Color]],  # returnValue
                        _type.HRESULT]

    _factory = True


class IColorHelperStatics2(_inspectable.IInspectable):
    ToDisplayName: _Callable[[_struct.Windows.UI.Color,  # color
                              _Pointer[_type.HSTRING]],  # returnValue
                             _type.HRESULT]

    _factory = True


class IColors(_inspectable.IInspectable):
    pass


class IColorsStatics(_inspectable.IInspectable):
    get_AliceBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    get_AntiqueWhite: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                _type.HRESULT]
    get_Aqua: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                        _type.HRESULT]
    get_Aquamarine: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                              _type.HRESULT]
    get_Azure: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                         _type.HRESULT]
    get_Beige: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                         _type.HRESULT]
    get_Bisque: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                          _type.HRESULT]
    get_Black: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                         _type.HRESULT]
    get_BlanchedAlmond: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                  _type.HRESULT]
    get_Blue: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                        _type.HRESULT]
    get_BlueViolet: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                              _type.HRESULT]
    get_Brown: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                         _type.HRESULT]
    get_BurlyWood: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    get_CadetBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    get_Chartreuse: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                              _type.HRESULT]
    get_Chocolate: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    get_Coral: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                         _type.HRESULT]
    get_CornflowerBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                  _type.HRESULT]
    get_Cornsilk: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                            _type.HRESULT]
    get_Crimson: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                           _type.HRESULT]
    get_Cyan: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                        _type.HRESULT]
    get_DarkBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                            _type.HRESULT]
    get_DarkCyan: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                            _type.HRESULT]
    get_DarkGoldenrod: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                 _type.HRESULT]
    get_DarkGray: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                            _type.HRESULT]
    get_DarkGreen: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    get_DarkKhaki: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    get_DarkMagenta: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                               _type.HRESULT]
    get_DarkOliveGreen: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                  _type.HRESULT]
    get_DarkOrange: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                              _type.HRESULT]
    get_DarkOrchid: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                              _type.HRESULT]
    get_DarkRed: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                           _type.HRESULT]
    get_DarkSalmon: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                              _type.HRESULT]
    get_DarkSeaGreen: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                _type.HRESULT]
    get_DarkSlateBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                 _type.HRESULT]
    get_DarkSlateGray: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                 _type.HRESULT]
    get_DarkTurquoise: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                 _type.HRESULT]
    get_DarkViolet: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                              _type.HRESULT]
    get_DeepPink: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                            _type.HRESULT]
    get_DeepSkyBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                               _type.HRESULT]
    get_DimGray: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                           _type.HRESULT]
    get_DodgerBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                              _type.HRESULT]
    get_Firebrick: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    get_FloralWhite: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                               _type.HRESULT]
    get_ForestGreen: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                               _type.HRESULT]
    get_Fuchsia: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                           _type.HRESULT]
    get_Gainsboro: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    get_GhostWhite: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                              _type.HRESULT]
    get_Gold: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                        _type.HRESULT]
    get_Goldenrod: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    get_Gray: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                        _type.HRESULT]
    get_Green: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                         _type.HRESULT]
    get_GreenYellow: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                               _type.HRESULT]
    get_Honeydew: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                            _type.HRESULT]
    get_HotPink: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                           _type.HRESULT]
    get_IndianRed: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    get_Indigo: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                          _type.HRESULT]
    get_Ivory: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                         _type.HRESULT]
    get_Khaki: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                         _type.HRESULT]
    get_Lavender: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                            _type.HRESULT]
    get_LavenderBlush: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                 _type.HRESULT]
    get_LawnGreen: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    get_LemonChiffon: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                _type.HRESULT]
    get_LightBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    get_LightCoral: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                              _type.HRESULT]
    get_LightCyan: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    get_LightGoldenrodYellow: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                        _type.HRESULT]
    get_LightGreen: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                              _type.HRESULT]
    get_LightGray: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    get_LightPink: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    get_LightSalmon: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                               _type.HRESULT]
    get_LightSeaGreen: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                 _type.HRESULT]
    get_LightSkyBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                _type.HRESULT]
    get_LightSlateGray: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                  _type.HRESULT]
    get_LightSteelBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                  _type.HRESULT]
    get_LightYellow: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                               _type.HRESULT]
    get_Lime: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                        _type.HRESULT]
    get_LimeGreen: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    get_Linen: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                         _type.HRESULT]
    get_Magenta: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                           _type.HRESULT]
    get_Maroon: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                          _type.HRESULT]
    get_MediumAquamarine: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                    _type.HRESULT]
    get_MediumBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                              _type.HRESULT]
    get_MediumOrchid: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                _type.HRESULT]
    get_MediumPurple: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                _type.HRESULT]
    get_MediumSeaGreen: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                  _type.HRESULT]
    get_MediumSlateBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                   _type.HRESULT]
    get_MediumSpringGreen: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                     _type.HRESULT]
    get_MediumTurquoise: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                   _type.HRESULT]
    get_MediumVioletRed: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                   _type.HRESULT]
    get_MidnightBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                _type.HRESULT]
    get_MintCream: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    get_MistyRose: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    get_Moccasin: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                            _type.HRESULT]
    get_NavajoWhite: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                               _type.HRESULT]
    get_Navy: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                        _type.HRESULT]
    get_OldLace: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                           _type.HRESULT]
    get_Olive: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                         _type.HRESULT]
    get_OliveDrab: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    get_Orange: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                          _type.HRESULT]
    get_OrangeRed: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    get_Orchid: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                          _type.HRESULT]
    get_PaleGoldenrod: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                 _type.HRESULT]
    get_PaleGreen: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    get_PaleTurquoise: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                 _type.HRESULT]
    get_PaleVioletRed: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                 _type.HRESULT]
    get_PapayaWhip: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                              _type.HRESULT]
    get_PeachPuff: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    get_Peru: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                        _type.HRESULT]
    get_Pink: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                        _type.HRESULT]
    get_Plum: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                        _type.HRESULT]
    get_PowderBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                              _type.HRESULT]
    get_Purple: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                          _type.HRESULT]
    get_Red: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                       _type.HRESULT]
    get_RosyBrown: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    get_RoyalBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    get_SaddleBrown: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                               _type.HRESULT]
    get_Salmon: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                          _type.HRESULT]
    get_SandyBrown: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                              _type.HRESULT]
    get_SeaGreen: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                            _type.HRESULT]
    get_SeaShell: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                            _type.HRESULT]
    get_Sienna: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                          _type.HRESULT]
    get_Silver: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                          _type.HRESULT]
    get_SkyBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                           _type.HRESULT]
    get_SlateBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    get_SlateGray: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    get_Snow: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                        _type.HRESULT]
    get_SpringGreen: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                               _type.HRESULT]
    get_SteelBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    get_Tan: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                       _type.HRESULT]
    get_Teal: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                        _type.HRESULT]
    get_Thistle: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                           _type.HRESULT]
    get_Tomato: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                          _type.HRESULT]
    get_Transparent: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                               _type.HRESULT]
    get_Turquoise: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    get_Violet: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                          _type.HRESULT]
    get_Wheat: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                         _type.HRESULT]
    get_White: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                         _type.HRESULT]
    get_WhiteSmoke: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                              _type.HRESULT]
    get_Yellow: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                          _type.HRESULT]
    get_YellowGreen: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                               _type.HRESULT]

    _factory = True


class IUIContentRoot(_inspectable.IInspectable):
    get_UIContext: _Callable[[_Pointer[IUIContext]],  # value
                             _type.HRESULT]


class IUIContext(_inspectable.IInspectable):
    pass
