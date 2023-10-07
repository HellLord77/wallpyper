from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import type as _type
from ......_utils import _Pointer


class ICurrencyFormatter(_inspectable.IInspectable):
    get_Currency: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    Currency: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]


class ICurrencyFormatter2(_inspectable.IInspectable):
    get_Mode: _Callable[[_Pointer[_enum.Windows.Globalization.NumberFormatting.CurrencyFormatterMode]],  # value
                        _type.HRESULT]
    put_Mode: _Callable[[_enum.Windows.Globalization.NumberFormatting.CurrencyFormatterMode],  # value
                        _type.HRESULT]
    ApplyRoundingForCurrency: _Callable[[_enum.Windows.Globalization.NumberFormatting.RoundingAlgorithm],  # roundingAlgorithm
                                        _type.HRESULT]


class ICurrencyFormatterFactory(_inspectable.IInspectable, factory=True):
    CreateCurrencyFormatterCode: _Callable[[_type.HSTRING,  # currencyCode
                                            _Pointer[ICurrencyFormatter]],  # result
                                           _type.HRESULT]
    CreateCurrencyFormatterCodeContext: _Callable[[_type.HSTRING,  # currencyCode
                                                   _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # languages
                                                   _type.HSTRING,  # geographicRegion
                                                   _Pointer[ICurrencyFormatter]],  # result
                                                  _type.HRESULT]


class IDecimalFormatterFactory(_inspectable.IInspectable, factory=True):
    CreateDecimalFormatter: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # languages
                                       _type.HSTRING,  # geographicRegion
                                       _Pointer[INumberFormatter]],  # result
                                      _type.HRESULT]


class IIncrementNumberRounder(_inspectable.IInspectable):
    get_RoundingAlgorithm: _Callable[[_Pointer[_enum.Windows.Globalization.NumberFormatting.RoundingAlgorithm]],  # value
                                     _type.HRESULT]
    put_RoundingAlgorithm: _Callable[[_enum.Windows.Globalization.NumberFormatting.RoundingAlgorithm],  # value
                                     _type.HRESULT]
    get_Increment: _Callable[[_Pointer[_type.DOUBLE]],  # value
                             _type.HRESULT]
    put_Increment: _Callable[[_type.DOUBLE],  # value
                             _type.HRESULT]


class INumberFormatter(_inspectable.IInspectable):
    FormatInt: _Callable[[_type.INT64,  # value
                          _Pointer[_type.HSTRING]],  # result
                         _type.HRESULT]
    FormatUInt: _Callable[[_type.UINT64,  # value
                           _Pointer[_type.HSTRING]],  # result
                          _type.HRESULT]
    FormatDouble: _Callable[[_type.DOUBLE,  # value
                             _Pointer[_type.HSTRING]],  # result
                            _type.HRESULT]


class INumberFormatter2(_inspectable.IInspectable):
    FormatInt: _Callable[[_type.INT64,  # value
                          _Pointer[_type.HSTRING]],  # result
                         _type.HRESULT]
    FormatUInt: _Callable[[_type.UINT64,  # value
                           _Pointer[_type.HSTRING]],  # result
                          _type.HRESULT]
    FormatDouble: _Callable[[_type.DOUBLE,  # value
                             _Pointer[_type.HSTRING]],  # result
                            _type.HRESULT]


class INumberFormatterOptions(_inspectable.IInspectable):
    get_Languages: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                             _type.HRESULT]
    get_GeographicRegion: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_IntegerDigits: _Callable[[_Pointer[_type.INT32]],  # value
                                 _type.HRESULT]
    put_IntegerDigits: _Callable[[_type.INT32],  # value
                                 _type.HRESULT]
    get_FractionDigits: _Callable[[_Pointer[_type.INT32]],  # value
                                  _type.HRESULT]
    put_FractionDigits: _Callable[[_type.INT32],  # value
                                  _type.HRESULT]
    get_IsGrouped: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsGrouped: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    get_IsDecimalPointAlwaysDisplayed: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]
    put_IsDecimalPointAlwaysDisplayed: _Callable[[_type.boolean],  # value
                                                 _type.HRESULT]
    get_NumeralSystem: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    put_NumeralSystem: _Callable[[_type.HSTRING],  # value
                                 _type.HRESULT]
    get_ResolvedLanguage: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_ResolvedGeographicRegion: _Callable[[_Pointer[_type.HSTRING]],  # value
                                            _type.HRESULT]


class INumberParser(_inspectable.IInspectable):
    ParseInt: _Callable[[_type.HSTRING,  # text
                         _Pointer[_Windows_Foundation.IReference[_type.INT64]]],  # result
                        _type.HRESULT]
    ParseUInt: _Callable[[_type.HSTRING,  # text
                          _Pointer[_Windows_Foundation.IReference[_type.UINT64]]],  # result
                         _type.HRESULT]
    ParseDouble: _Callable[[_type.HSTRING,  # text
                            _Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # result
                           _type.HRESULT]


class INumberRounder(_inspectable.IInspectable):
    RoundInt32: _Callable[[_type.INT32,  # value
                           _Pointer[_type.INT32]],  # result
                          _type.HRESULT]
    RoundUInt32: _Callable[[_type.UINT32,  # value
                            _Pointer[_type.UINT32]],  # result
                           _type.HRESULT]
    RoundInt64: _Callable[[_type.INT64,  # value
                           _Pointer[_type.INT64]],  # result
                          _type.HRESULT]
    RoundUInt64: _Callable[[_type.UINT64,  # value
                            _Pointer[_type.UINT64]],  # result
                           _type.HRESULT]
    RoundSingle: _Callable[[_type.FLOAT,  # value
                            _Pointer[_type.FLOAT]],  # result
                           _type.HRESULT]
    RoundDouble: _Callable[[_type.DOUBLE,  # value
                            _Pointer[_type.DOUBLE]],  # result
                           _type.HRESULT]


class INumberRounderOption(_inspectable.IInspectable):
    get_NumberRounder: _Callable[[_Pointer[INumberRounder]],  # value
                                 _type.HRESULT]
    put_NumberRounder: _Callable[[INumberRounder],  # value
                                 _type.HRESULT]


class INumeralSystemTranslator(_inspectable.IInspectable):
    get_Languages: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                             _type.HRESULT]
    get_ResolvedLanguage: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_NumeralSystem: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    put_NumeralSystem: _Callable[[_type.HSTRING],  # value
                                 _type.HRESULT]
    TranslateNumerals: _Callable[[_type.HSTRING,  # value
                                  _Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]


class INumeralSystemTranslatorFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # languages
                       _Pointer[INumeralSystemTranslator]],  # result
                      _type.HRESULT]


class IPercentFormatterFactory(_inspectable.IInspectable, factory=True):
    CreatePercentFormatter: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # languages
                                       _type.HSTRING,  # geographicRegion
                                       _Pointer[INumberFormatter]],  # result
                                      _type.HRESULT]


class IPermilleFormatterFactory(_inspectable.IInspectable, factory=True):
    CreatePermilleFormatter: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # languages
                                        _type.HSTRING,  # geographicRegion
                                        _Pointer[INumberFormatter]],  # result
                                       _type.HRESULT]


class ISignedZeroOption(_inspectable.IInspectable):
    get_IsZeroSigned: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_IsZeroSigned: _Callable[[_type.boolean],  # value
                                _type.HRESULT]


class ISignificantDigitsNumberRounder(_inspectable.IInspectable):
    get_RoundingAlgorithm: _Callable[[_Pointer[_enum.Windows.Globalization.NumberFormatting.RoundingAlgorithm]],  # value
                                     _type.HRESULT]
    put_RoundingAlgorithm: _Callable[[_enum.Windows.Globalization.NumberFormatting.RoundingAlgorithm],  # value
                                     _type.HRESULT]
    get_SignificantDigits: _Callable[[_Pointer[_type.UINT32]],  # value
                                     _type.HRESULT]
    put_SignificantDigits: _Callable[[_type.UINT32],  # value
                                     _type.HRESULT]


class ISignificantDigitsOption(_inspectable.IInspectable):
    get_SignificantDigits: _Callable[[_Pointer[_type.INT32]],  # value
                                     _type.HRESULT]
    put_SignificantDigits: _Callable[[_type.INT32],  # value
                                     _type.HRESULT]
