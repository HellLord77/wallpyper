from __future__ import annotations as _

from typing import Callable as _Callable

from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class ILanguageFont(_inspectable.IInspectable):
    get_FontFamily: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_FontWeight: _Callable[[_Pointer[_struct.Windows.UI.Text.FontWeight]],  # weight
                              _type.HRESULT]
    get_FontStretch: _Callable[[_Pointer[_enum.Windows.UI.Text.FontStretch]],  # stretch
                               _type.HRESULT]
    get_FontStyle: _Callable[[_Pointer[_enum.Windows.UI.Text.FontStyle]],  # style
                             _type.HRESULT]
    get_ScaleFactor: _Callable[[_Pointer[_type.DOUBLE]],  # scale
                               _type.HRESULT]


class ILanguageFontGroup(_inspectable.IInspectable):
    get_UITextFont: _Callable[[_Pointer[ILanguageFont]],  # value
                              _type.HRESULT]
    get_UIHeadingFont: _Callable[[_Pointer[ILanguageFont]],  # value
                                 _type.HRESULT]
    get_UITitleFont: _Callable[[_Pointer[ILanguageFont]],  # value
                               _type.HRESULT]
    get_UICaptionFont: _Callable[[_Pointer[ILanguageFont]],  # value
                                 _type.HRESULT]
    get_UINotificationHeadingFont: _Callable[[_Pointer[ILanguageFont]],  # value
                                             _type.HRESULT]
    get_TraditionalDocumentFont: _Callable[[_Pointer[ILanguageFont]],  # value
                                           _type.HRESULT]
    get_ModernDocumentFont: _Callable[[_Pointer[ILanguageFont]],  # value
                                      _type.HRESULT]
    get_DocumentHeadingFont: _Callable[[_Pointer[ILanguageFont]],  # value
                                       _type.HRESULT]
    get_FixedWidthTextFont: _Callable[[_Pointer[ILanguageFont]],  # value
                                      _type.HRESULT]
    get_DocumentAlternate1Font: _Callable[[_Pointer[ILanguageFont]],  # value
                                          _type.HRESULT]
    get_DocumentAlternate2Font: _Callable[[_Pointer[ILanguageFont]],  # value
                                          _type.HRESULT]


class ILanguageFontGroupFactory(_inspectable.IInspectable):
    CreateLanguageFontGroup: _Callable[[_type.HSTRING,  # languageTag
                                        _Pointer[ILanguageFontGroup]],  # recommendedFonts
                                       _type.HRESULT]

    _factory = True
