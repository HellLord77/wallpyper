from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import Globalization as _Windows_Globalization
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Graphics import Imaging as _Windows_Graphics_Imaging
from .... import inspectable as _inspectable
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IOcrEngine(_inspectable.IInspectable):
    RecognizeAsync: _Callable[[_Windows_Graphics_Imaging.ISoftwareBitmap,  # bitmap
                               _Pointer[_Windows_Foundation.IAsyncOperation[IOcrResult]]],  # result
                              _type.HRESULT]
    get_RecognizerLanguage: _Callable[[_Pointer[_Windows_Globalization.ILanguage]],  # value
                                      _type.HRESULT]


class IOcrEngineStatics(_inspectable.IInspectable, factory=True):
    get_MaxImageDimension: _Callable[[_Pointer[_type.UINT32]],  # value
                                     _type.HRESULT]
    get_AvailableRecognizerLanguages: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Globalization.ILanguage]]],  # value
                                                _type.HRESULT]
    IsLanguageSupported: _Callable[[_Windows_Globalization.ILanguage,  # language
                                    _Pointer[_type.boolean]],  # result
                                   _type.HRESULT]
    TryCreateFromLanguage: _Callable[[_Windows_Globalization.ILanguage,  # language
                                      _Pointer[IOcrEngine]],  # result
                                     _type.HRESULT]
    TryCreateFromUserProfileLanguages: _Callable[[_Pointer[IOcrEngine]],  # result
                                                 _type.HRESULT]


class IOcrLine(_inspectable.IInspectable):
    get_Words: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IOcrWord]]],  # value
                         _type.HRESULT]
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class IOcrResult(_inspectable.IInspectable):
    get_Lines: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IOcrLine]]],  # value
                         _type.HRESULT]
    get_TextAngle: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                             _type.HRESULT]
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class IOcrWord(_inspectable.IInspectable):
    get_BoundingRect: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                                _type.HRESULT]
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
