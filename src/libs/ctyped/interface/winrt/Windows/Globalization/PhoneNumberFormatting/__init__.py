from __future__ import annotations

from typing import Callable as _Callable

from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import type as _type
from ......_utils import _Pointer


class IPhoneNumberFormatter(_inspectable.IInspectable):
    Format: _Callable[[IPhoneNumberInfo,  # number
                       _Pointer[_type.HSTRING]],  # result
                      _type.HRESULT]
    FormatWithOutputFormat: _Callable[[IPhoneNumberInfo,  # number
                                       _enum.Windows.Globalization.PhoneNumberFormatting.PhoneNumberFormat,  # numberFormat
                                       _Pointer[_type.HSTRING]],  # result
                                      _type.HRESULT]
    FormatPartialString: _Callable[[_type.HSTRING,  # number
                                    _Pointer[_type.HSTRING]],  # result
                                   _type.HRESULT]
    FormatString: _Callable[[_type.HSTRING,  # number
                             _Pointer[_type.HSTRING]],  # result
                            _type.HRESULT]
    FormatStringWithLeftToRightMarkers: _Callable[[_type.HSTRING,  # number
                                                   _Pointer[_type.HSTRING]],  # result
                                                  _type.HRESULT]


class IPhoneNumberFormatterStatics(_inspectable.IInspectable):
    TryCreate: _Callable[[_type.HSTRING,  # regionCode
                          _Pointer[IPhoneNumberFormatter]],  # phoneNumber
                         _type.HRESULT]
    GetCountryCodeForRegion: _Callable[[_type.HSTRING,  # regionCode
                                        _Pointer[_type.INT32]],  # result
                                       _type.HRESULT]
    GetNationalDirectDialingPrefixForRegion: _Callable[[_type.HSTRING,  # regionCode
                                                        _type.boolean,  # stripNonDigit
                                                        _Pointer[_type.HSTRING]],  # result
                                                       _type.HRESULT]
    WrapWithLeftToRightMarkers: _Callable[[_type.HSTRING,  # number
                                           _Pointer[_type.HSTRING]],  # result
                                          _type.HRESULT]

    _factory = True


class IPhoneNumberInfo(_inspectable.IInspectable):
    get_CountryCode: _Callable[[_Pointer[_type.INT32]],  # value
                               _type.HRESULT]
    get_PhoneNumber: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    GetLengthOfGeographicalAreaCode: _Callable[[_Pointer[_type.INT32]],  # result
                                               _type.HRESULT]
    GetNationalSignificantNumber: _Callable[[_Pointer[_type.HSTRING]],  # result
                                            _type.HRESULT]
    GetLengthOfNationalDestinationCode: _Callable[[_Pointer[_type.INT32]],  # result
                                                  _type.HRESULT]
    PredictNumberKind: _Callable[[_Pointer[_enum.Windows.Globalization.PhoneNumberFormatting.PredictedPhoneNumberKind]],  # result
                                 _type.HRESULT]
    GetGeographicRegionCode: _Callable[[_Pointer[_type.HSTRING]],  # result
                                       _type.HRESULT]
    CheckNumberMatch: _Callable[[IPhoneNumberInfo,  # otherNumber
                                 _Pointer[_enum.Windows.Globalization.PhoneNumberFormatting.PhoneNumberMatchResult]],  # result
                                _type.HRESULT]


class IPhoneNumberInfoFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.HSTRING,  # number
                       _Pointer[IPhoneNumberInfo]],  # result
                      _type.HRESULT]

    _factory = True


class IPhoneNumberInfoStatics(_inspectable.IInspectable):
    TryParse: _Callable[[_type.HSTRING,  # input
                         _Pointer[IPhoneNumberInfo],  # phoneNumber
                         _Pointer[_enum.Windows.Globalization.PhoneNumberFormatting.PhoneNumberParseResult]],  # result
                        _type.HRESULT]
    TryParseWithRegion: _Callable[[_type.HSTRING,  # input
                                   _type.HSTRING,  # regionCode
                                   _Pointer[IPhoneNumberInfo],  # phoneNumber
                                   _Pointer[_enum.Windows.Globalization.PhoneNumberFormatting.PhoneNumberParseResult]],  # result
                                  _type.HRESULT]

    _factory = True
