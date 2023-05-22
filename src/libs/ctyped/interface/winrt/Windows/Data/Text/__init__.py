from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from .....um import Unknwnbase as _Unknwnbase
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class _ISelectableWordSegmentsTokenizingHandler:
    Invoke: _Callable[[_Windows_Foundation_Collections.IIterable[ISelectableWordSegment],  # precedingWords
                       _Windows_Foundation_Collections.IIterable[ISelectableWordSegment]],  # words
                      _type.HRESULT]


class ISelectableWordSegmentsTokenizingHandler(_ISelectableWordSegmentsTokenizingHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ISelectableWordSegmentsTokenizingHandler_impl(_ISelectableWordSegmentsTokenizingHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IWordSegmentsTokenizingHandler:
    Invoke: _Callable[[_Windows_Foundation_Collections.IIterable[IWordSegment],  # precedingWords
                       _Windows_Foundation_Collections.IIterable[IWordSegment]],  # words
                      _type.HRESULT]


class IWordSegmentsTokenizingHandler(_IWordSegmentsTokenizingHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IWordSegmentsTokenizingHandler_impl(_IWordSegmentsTokenizingHandler, _Unknwnbase.IUnknown_impl):
    pass


class IAlternateWordForm(_inspectable.IInspectable):
    get_SourceTextSegment: _Callable[[_Pointer[_struct.Windows.Data.Text.TextSegment]],  # value
                                     _type.HRESULT]
    get_AlternateText: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_NormalizationFormat: _Callable[[_Pointer[_enum.Windows.Data.Text.AlternateNormalizationFormat]],  # value
                                       _type.HRESULT]


class ISelectableWordSegment(_inspectable.IInspectable):
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_SourceTextSegment: _Callable[[_Pointer[_struct.Windows.Data.Text.TextSegment]],  # value
                                     _type.HRESULT]


class ISelectableWordsSegmenter(_inspectable.IInspectable):
    get_ResolvedLanguage: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    GetTokenAt: _Callable[[_type.HSTRING,  # text
                           _type.UINT32,  # startIndex
                           _Pointer[ISelectableWordSegment]],  # result
                          _type.HRESULT]
    GetTokens: _Callable[[_type.HSTRING,  # text
                          _Pointer[_Windows_Foundation_Collections.IVectorView[ISelectableWordSegment]]],  # result
                         _type.HRESULT]
    Tokenize: _Callable[[_type.HSTRING,  # text
                         _type.UINT32,  # startIndex
                         ISelectableWordSegmentsTokenizingHandler],  # handler
                        _type.HRESULT]


class ISelectableWordsSegmenterFactory(_inspectable.IInspectable, factory=True):
    CreateWithLanguage: _Callable[[_type.HSTRING,  # language
                                   _Pointer[ISelectableWordsSegmenter]],  # result
                                  _type.HRESULT]


class ISemanticTextQuery(_inspectable.IInspectable):
    Find: _Callable[[_type.HSTRING,  # content
                     _Pointer[_Windows_Foundation_Collections.IVectorView[_struct.Windows.Data.Text.TextSegment]]],  # result
                    _type.HRESULT]
    FindInProperty: _Callable[[_type.HSTRING,  # propertyContent
                               _type.HSTRING,  # propertyName
                               _Pointer[_Windows_Foundation_Collections.IVectorView[_struct.Windows.Data.Text.TextSegment]]],  # result
                              _type.HRESULT]


class ISemanticTextQueryFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.HSTRING,  # aqsFilter
                       _Pointer[ISemanticTextQuery]],  # result
                      _type.HRESULT]
    CreateWithLanguage: _Callable[[_type.HSTRING,  # aqsFilter
                                   _type.HSTRING,  # filterLanguage
                                   _Pointer[ISemanticTextQuery]],  # result
                                  _type.HRESULT]


class ITextConversionGenerator(_inspectable.IInspectable):
    get_ResolvedLanguage: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_LanguageAvailableButNotInstalled: _Callable[[_Pointer[_type.boolean]],  # value
                                                    _type.HRESULT]
    GetCandidatesAsync: _Callable[[_type.HSTRING,  # input
                                   _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]]],  # result
                                  _type.HRESULT]
    GetCandidatesWithMaxCountAsync: _Callable[[_type.HSTRING,  # input
                                               _type.UINT32,  # maxCandidates
                                               _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]]],  # result
                                              _type.HRESULT]


class ITextConversionGeneratorFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.HSTRING,  # languageTag
                       _Pointer[ITextConversionGenerator]],  # result
                      _type.HRESULT]


class ITextPhoneme(_inspectable.IInspectable):
    get_DisplayText: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_ReadingText: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class ITextPredictionGenerator(_inspectable.IInspectable):
    get_ResolvedLanguage: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_LanguageAvailableButNotInstalled: _Callable[[_Pointer[_type.boolean]],  # value
                                                    _type.HRESULT]
    GetCandidatesAsync: _Callable[[_type.HSTRING,  # input
                                   _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]]],  # result
                                  _type.HRESULT]
    GetCandidatesWithMaxCountAsync: _Callable[[_type.HSTRING,  # input
                                               _type.UINT32,  # maxCandidates
                                               _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]]],  # result
                                              _type.HRESULT]


class ITextPredictionGenerator2(_inspectable.IInspectable):
    GetCandidatesWithParametersAsync: _Callable[[_type.HSTRING,  # input
                                                 _type.UINT32,  # maxCandidates
                                                 _enum.Windows.Data.Text.TextPredictionOptions,  # predictionOptions
                                                 _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # previousStrings
                                                 _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]]],  # result
                                                _type.HRESULT]
    GetNextWordCandidatesAsync: _Callable[[_type.UINT32,  # maxCandidates
                                           _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # previousStrings
                                           _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]]],  # result
                                          _type.HRESULT]
    get_InputScope: _Callable[[_Pointer[_enum.Windows.UI.Text.Core.CoreTextInputScope]],  # value
                              _type.HRESULT]
    put_InputScope: _Callable[[_enum.Windows.UI.Text.Core.CoreTextInputScope],  # value
                              _type.HRESULT]


class ITextPredictionGeneratorFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.HSTRING,  # languageTag
                       _Pointer[ITextPredictionGenerator]],  # result
                      _type.HRESULT]


class ITextReverseConversionGenerator(_inspectable.IInspectable):
    get_ResolvedLanguage: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_LanguageAvailableButNotInstalled: _Callable[[_Pointer[_type.boolean]],  # value
                                                    _type.HRESULT]
    ConvertBackAsync: _Callable[[_type.HSTRING,  # input
                                 _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # result
                                _type.HRESULT]


class ITextReverseConversionGenerator2(_inspectable.IInspectable):
    GetPhonemesAsync: _Callable[[_type.HSTRING,  # input
                                 _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[ITextPhoneme]]]],  # result
                                _type.HRESULT]


class ITextReverseConversionGeneratorFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.HSTRING,  # languageTag
                       _Pointer[ITextReverseConversionGenerator]],  # result
                      _type.HRESULT]


class IUnicodeCharactersStatics(_inspectable.IInspectable, factory=True):
    GetCodepointFromSurrogatePair: _Callable[[_type.UINT32,  # highSurrogate
                                              _type.UINT32,  # lowSurrogate
                                              _Pointer[_type.UINT32]],  # codepoint
                                             _type.HRESULT]
    GetSurrogatePairFromCodepoint: _Callable[[_type.UINT32,  # codepoint
                                              _Pointer[_type.WCHAR],  # highSurrogate
                                              _Pointer[_type.WCHAR]],  # lowSurrogate
                                             _type.HRESULT]
    IsHighSurrogate: _Callable[[_type.UINT32,  # codepoint
                                _Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    IsLowSurrogate: _Callable[[_type.UINT32,  # codepoint
                               _Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    IsSupplementary: _Callable[[_type.UINT32,  # codepoint
                                _Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    IsNoncharacter: _Callable[[_type.UINT32,  # codepoint
                               _Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    IsWhitespace: _Callable[[_type.UINT32,  # codepoint
                             _Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    IsAlphabetic: _Callable[[_type.UINT32,  # codepoint
                             _Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    IsCased: _Callable[[_type.UINT32,  # codepoint
                        _Pointer[_type.boolean]],  # value
                       _type.HRESULT]
    IsUppercase: _Callable[[_type.UINT32,  # codepoint
                            _Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    IsLowercase: _Callable[[_type.UINT32,  # codepoint
                            _Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    IsIdStart: _Callable[[_type.UINT32,  # codepoint
                          _Pointer[_type.boolean]],  # value
                         _type.HRESULT]
    IsIdContinue: _Callable[[_type.UINT32,  # codepoint
                             _Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    IsGraphemeBase: _Callable[[_type.UINT32,  # codepoint
                               _Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    IsGraphemeExtend: _Callable[[_type.UINT32,  # codepoint
                                 _Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    GetNumericType: _Callable[[_type.UINT32,  # codepoint
                               _Pointer[_enum.Windows.Data.Text.UnicodeNumericType]],  # value
                              _type.HRESULT]
    GetGeneralCategory: _Callable[[_type.UINT32,  # codepoint
                                   _Pointer[_enum.Windows.Data.Text.UnicodeGeneralCategory]],  # value
                                  _type.HRESULT]


class IWordSegment(_inspectable.IInspectable):
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_SourceTextSegment: _Callable[[_Pointer[_struct.Windows.Data.Text.TextSegment]],  # value
                                     _type.HRESULT]
    get_AlternateForms: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IAlternateWordForm]]],  # value
                                  _type.HRESULT]


class IWordsSegmenter(_inspectable.IInspectable):
    get_ResolvedLanguage: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    GetTokenAt: _Callable[[_type.HSTRING,  # text
                           _type.UINT32,  # startIndex
                           _Pointer[IWordSegment]],  # result
                          _type.HRESULT]
    GetTokens: _Callable[[_type.HSTRING,  # text
                          _Pointer[_Windows_Foundation_Collections.IVectorView[IWordSegment]]],  # result
                         _type.HRESULT]
    Tokenize: _Callable[[_type.HSTRING,  # text
                         _type.UINT32,  # startIndex
                         IWordSegmentsTokenizingHandler],  # handler
                        _type.HRESULT]


class IWordsSegmenterFactory(_inspectable.IInspectable, factory=True):
    CreateWithLanguage: _Callable[[_type.HSTRING,  # language
                                   _Pointer[IWordsSegmenter]],  # result
                                  _type.HRESULT]
