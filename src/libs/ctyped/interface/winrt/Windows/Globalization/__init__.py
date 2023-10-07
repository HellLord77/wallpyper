from __future__ import annotations as _

from typing import Callable as _Callable

from .. import System as _Windows_System
from ..Foundation import Collections as _Windows_Foundation_Collections
from ... import inspectable as _inspectable
from ..... import enum as _enum
from ..... import struct as _struct
from ..... import type as _type
from ....._utils import _Pointer


class IApplicationLanguagesStatics(_inspectable.IInspectable, factory=True):
    get_PrimaryLanguageOverride: _Callable[[_Pointer[_type.HSTRING]],  # value
                                           _type.HRESULT]
    put_PrimaryLanguageOverride: _Callable[[_type.HSTRING],  # value
                                           _type.HRESULT]
    get_Languages: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                             _type.HRESULT]
    get_ManifestLanguages: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                     _type.HRESULT]


class IApplicationLanguagesStatics2(_inspectable.IInspectable, factory=True):
    GetLanguagesForUser: _Callable[[_Windows_System.IUser,  # user
                                    _Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                   _type.HRESULT]


class ICalendar(_inspectable.IInspectable):
    Clone: _Callable[[_Pointer[ICalendar]],  # value
                     _type.HRESULT]
    SetToMin: _Callable[[],
                        _type.HRESULT]
    SetToMax: _Callable[[],
                        _type.HRESULT]
    get_Languages: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                             _type.HRESULT]
    get_NumeralSystem: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    put_NumeralSystem: _Callable[[_type.HSTRING],  # value
                                 _type.HRESULT]
    GetCalendarSystem: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    ChangeCalendarSystem: _Callable[[_type.HSTRING],  # value
                                    _type.HRESULT]
    GetClock: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    ChangeClock: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    GetDateTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # result
                           _type.HRESULT]
    SetDateTime: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                           _type.HRESULT]
    SetToNow: _Callable[[],
                        _type.HRESULT]
    get_FirstEra: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    get_LastEra: _Callable[[_Pointer[_type.INT32]],  # value
                           _type.HRESULT]
    get_NumberOfEras: _Callable[[_Pointer[_type.INT32]],  # value
                                _type.HRESULT]
    get_Era: _Callable[[_Pointer[_type.INT32]],  # value
                       _type.HRESULT]
    put_Era: _Callable[[_type.INT32],  # value
                       _type.HRESULT]
    AddEras: _Callable[[_type.INT32],  # eras
                       _type.HRESULT]
    EraAsFullString: _Callable[[_Pointer[_type.HSTRING]],  # result
                               _type.HRESULT]
    EraAsString: _Callable[[_type.INT32,  # idealLength
                            _Pointer[_type.HSTRING]],  # result
                           _type.HRESULT]
    get_FirstYearInThisEra: _Callable[[_Pointer[_type.INT32]],  # value
                                      _type.HRESULT]
    get_LastYearInThisEra: _Callable[[_Pointer[_type.INT32]],  # value
                                     _type.HRESULT]
    get_NumberOfYearsInThisEra: _Callable[[_Pointer[_type.INT32]],  # value
                                          _type.HRESULT]
    get_Year: _Callable[[_Pointer[_type.INT32]],  # value
                        _type.HRESULT]
    put_Year: _Callable[[_type.INT32],  # value
                        _type.HRESULT]
    AddYears: _Callable[[_type.INT32],  # years
                        _type.HRESULT]
    YearAsString: _Callable[[_Pointer[_type.HSTRING]],  # result
                            _type.HRESULT]
    YearAsTruncatedString: _Callable[[_type.INT32,  # remainingDigits
                                      _Pointer[_type.HSTRING]],  # result
                                     _type.HRESULT]
    YearAsPaddedString: _Callable[[_type.INT32,  # minDigits
                                   _Pointer[_type.HSTRING]],  # result
                                  _type.HRESULT]
    get_FirstMonthInThisYear: _Callable[[_Pointer[_type.INT32]],  # value
                                        _type.HRESULT]
    get_LastMonthInThisYear: _Callable[[_Pointer[_type.INT32]],  # value
                                       _type.HRESULT]
    get_NumberOfMonthsInThisYear: _Callable[[_Pointer[_type.INT32]],  # value
                                            _type.HRESULT]
    get_Month: _Callable[[_Pointer[_type.INT32]],  # value
                         _type.HRESULT]
    put_Month: _Callable[[_type.INT32],  # value
                         _type.HRESULT]
    AddMonths: _Callable[[_type.INT32],  # months
                         _type.HRESULT]
    MonthAsFullString: _Callable[[_Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]
    MonthAsString: _Callable[[_type.INT32,  # idealLength
                              _Pointer[_type.HSTRING]],  # result
                             _type.HRESULT]
    MonthAsFullSoloString: _Callable[[_Pointer[_type.HSTRING]],  # result
                                     _type.HRESULT]
    MonthAsSoloString: _Callable[[_type.INT32,  # idealLength
                                  _Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]
    MonthAsNumericString: _Callable[[_Pointer[_type.HSTRING]],  # result
                                    _type.HRESULT]
    MonthAsPaddedNumericString: _Callable[[_type.INT32,  # minDigits
                                           _Pointer[_type.HSTRING]],  # result
                                          _type.HRESULT]
    AddWeeks: _Callable[[_type.INT32],  # weeks
                        _type.HRESULT]
    get_FirstDayInThisMonth: _Callable[[_Pointer[_type.INT32]],  # value
                                       _type.HRESULT]
    get_LastDayInThisMonth: _Callable[[_Pointer[_type.INT32]],  # value
                                      _type.HRESULT]
    get_NumberOfDaysInThisMonth: _Callable[[_Pointer[_type.INT32]],  # value
                                           _type.HRESULT]
    get_Day: _Callable[[_Pointer[_type.INT32]],  # value
                       _type.HRESULT]
    put_Day: _Callable[[_type.INT32],  # value
                       _type.HRESULT]
    AddDays: _Callable[[_type.INT32],  # days
                       _type.HRESULT]
    DayAsString: _Callable[[_Pointer[_type.HSTRING]],  # result
                           _type.HRESULT]
    DayAsPaddedString: _Callable[[_type.INT32,  # minDigits
                                  _Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]
    get_DayOfWeek: _Callable[[_Pointer[_enum.Windows.Globalization.DayOfWeek]],  # value
                             _type.HRESULT]
    DayOfWeekAsFullString: _Callable[[_Pointer[_type.HSTRING]],  # result
                                     _type.HRESULT]
    DayOfWeekAsString: _Callable[[_type.INT32,  # idealLength
                                  _Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]
    DayOfWeekAsFullSoloString: _Callable[[_Pointer[_type.HSTRING]],  # result
                                         _type.HRESULT]
    DayOfWeekAsSoloString: _Callable[[_type.INT32,  # idealLength
                                      _Pointer[_type.HSTRING]],  # result
                                     _type.HRESULT]
    get_FirstPeriodInThisDay: _Callable[[_Pointer[_type.INT32]],  # value
                                        _type.HRESULT]
    get_LastPeriodInThisDay: _Callable[[_Pointer[_type.INT32]],  # value
                                       _type.HRESULT]
    get_NumberOfPeriodsInThisDay: _Callable[[_Pointer[_type.INT32]],  # value
                                            _type.HRESULT]
    get_Period: _Callable[[_Pointer[_type.INT32]],  # value
                          _type.HRESULT]
    put_Period: _Callable[[_type.INT32],  # value
                          _type.HRESULT]
    AddPeriods: _Callable[[_type.INT32],  # periods
                          _type.HRESULT]
    PeriodAsFullString: _Callable[[_Pointer[_type.HSTRING]],  # result
                                  _type.HRESULT]
    PeriodAsString: _Callable[[_type.INT32,  # idealLength
                               _Pointer[_type.HSTRING]],  # result
                              _type.HRESULT]
    get_FirstHourInThisPeriod: _Callable[[_Pointer[_type.INT32]],  # value
                                         _type.HRESULT]
    get_LastHourInThisPeriod: _Callable[[_Pointer[_type.INT32]],  # value
                                        _type.HRESULT]
    get_NumberOfHoursInThisPeriod: _Callable[[_Pointer[_type.INT32]],  # value
                                             _type.HRESULT]
    get_Hour: _Callable[[_Pointer[_type.INT32]],  # value
                        _type.HRESULT]
    put_Hour: _Callable[[_type.INT32],  # value
                        _type.HRESULT]
    AddHours: _Callable[[_type.INT32],  # hours
                        _type.HRESULT]
    HourAsString: _Callable[[_Pointer[_type.HSTRING]],  # result
                            _type.HRESULT]
    HourAsPaddedString: _Callable[[_type.INT32,  # minDigits
                                   _Pointer[_type.HSTRING]],  # result
                                  _type.HRESULT]
    get_Minute: _Callable[[_Pointer[_type.INT32]],  # value
                          _type.HRESULT]
    put_Minute: _Callable[[_type.INT32],  # value
                          _type.HRESULT]
    AddMinutes: _Callable[[_type.INT32],  # minutes
                          _type.HRESULT]
    MinuteAsString: _Callable[[_Pointer[_type.HSTRING]],  # result
                              _type.HRESULT]
    MinuteAsPaddedString: _Callable[[_type.INT32,  # minDigits
                                     _Pointer[_type.HSTRING]],  # result
                                    _type.HRESULT]
    get_Second: _Callable[[_Pointer[_type.INT32]],  # value
                          _type.HRESULT]
    put_Second: _Callable[[_type.INT32],  # value
                          _type.HRESULT]
    AddSeconds: _Callable[[_type.INT32],  # seconds
                          _type.HRESULT]
    SecondAsString: _Callable[[_Pointer[_type.HSTRING]],  # result
                              _type.HRESULT]
    SecondAsPaddedString: _Callable[[_type.INT32,  # minDigits
                                     _Pointer[_type.HSTRING]],  # result
                                    _type.HRESULT]
    get_Nanosecond: _Callable[[_Pointer[_type.INT32]],  # value
                              _type.HRESULT]
    put_Nanosecond: _Callable[[_type.INT32],  # value
                              _type.HRESULT]
    AddNanoseconds: _Callable[[_type.INT32],  # nanoseconds
                              _type.HRESULT]
    NanosecondAsString: _Callable[[_Pointer[_type.HSTRING]],  # result
                                  _type.HRESULT]
    NanosecondAsPaddedString: _Callable[[_type.INT32,  # minDigits
                                         _Pointer[_type.HSTRING]],  # result
                                        _type.HRESULT]
    Compare: _Callable[[ICalendar,  # other
                        _Pointer[_type.INT32]],  # result
                       _type.HRESULT]
    CompareDateTime: _Callable[[_struct.Windows.Foundation.DateTime,  # other
                                _Pointer[_type.INT32]],  # result
                               _type.HRESULT]
    CopyTo: _Callable[[ICalendar],  # other
                      _type.HRESULT]
    get_FirstMinuteInThisHour: _Callable[[_Pointer[_type.INT32]],  # value
                                         _type.HRESULT]
    get_LastMinuteInThisHour: _Callable[[_Pointer[_type.INT32]],  # value
                                        _type.HRESULT]
    get_NumberOfMinutesInThisHour: _Callable[[_Pointer[_type.INT32]],  # value
                                             _type.HRESULT]
    get_FirstSecondInThisMinute: _Callable[[_Pointer[_type.INT32]],  # value
                                           _type.HRESULT]
    get_LastSecondInThisMinute: _Callable[[_Pointer[_type.INT32]],  # value
                                          _type.HRESULT]
    get_NumberOfSecondsInThisMinute: _Callable[[_Pointer[_type.INT32]],  # value
                                               _type.HRESULT]
    get_ResolvedLanguage: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_IsDaylightSavingTime: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]


class ICalendarFactory(_inspectable.IInspectable):
    CreateCalendarDefaultCalendarAndClock: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # languages
                                                      _Pointer[ICalendar]],  # result
                                                     _type.HRESULT]
    CreateCalendar: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # languages
                               _type.HSTRING,  # calendar
                               _type.HSTRING,  # clock
                               _Pointer[ICalendar]],  # result
                              _type.HRESULT]


class ICalendarFactory2(_inspectable.IInspectable, factory=True):
    CreateCalendarWithTimeZone: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # languages
                                           _type.HSTRING,  # calendar
                                           _type.HSTRING,  # clock
                                           _type.HSTRING,  # timeZoneId
                                           _Pointer[ICalendar]],  # result
                                          _type.HRESULT]


class ICalendarIdentifiersStatics(_inspectable.IInspectable, factory=True):
    get_Gregorian: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_Hebrew: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Hijri: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Japanese: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Julian: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Korean: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Taiwan: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Thai: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_UmAlQura: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]


class ICalendarIdentifiersStatics2(_inspectable.IInspectable, factory=True):
    get_Persian: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]


class ICalendarIdentifiersStatics3(_inspectable.IInspectable, factory=True):
    get_ChineseLunar: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_JapaneseLunar: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_KoreanLunar: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_TaiwanLunar: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_VietnameseLunar: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]


class IClockIdentifiersStatics(_inspectable.IInspectable, factory=True):
    get_TwelveHour: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_TwentyFourHour: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]


class ICurrencyAmount(_inspectable.IInspectable):
    get_Amount: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Currency: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]


class ICurrencyAmountFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.HSTRING,  # amount
                       _type.HSTRING,  # currency
                       _Pointer[ICurrencyAmount]],  # result
                      _type.HRESULT]


class ICurrencyIdentifiersStatics(_inspectable.IInspectable, factory=True):
    get_AED: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_AFN: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_ALL: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_AMD: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_ANG: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_AOA: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_ARS: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_AUD: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_AWG: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_AZN: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_BAM: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_BBD: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_BDT: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_BGN: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_BHD: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_BIF: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_BMD: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_BND: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_BOB: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_BRL: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_BSD: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_BTN: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_BWP: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_BYR: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_BZD: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_CAD: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_CDF: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_CHF: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_CLP: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_CNY: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_COP: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_CRC: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_CUP: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_CVE: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_CZK: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_DJF: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_DKK: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_DOP: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_DZD: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_EGP: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_ERN: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_ETB: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_EUR: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_FJD: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_FKP: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_GBP: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_GEL: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_GHS: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_GIP: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_GMD: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_GNF: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_GTQ: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_GYD: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_HKD: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_HNL: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_HRK: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_HTG: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_HUF: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_IDR: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_ILS: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_INR: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_IQD: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_IRR: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_ISK: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_JMD: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_JOD: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_JPY: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_KES: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_KGS: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_KHR: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_KMF: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_KPW: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_KRW: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_KWD: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_KYD: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_KZT: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_LAK: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_LBP: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_LKR: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_LRD: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_LSL: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_LTL: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_LVL: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_LYD: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_MAD: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_MDL: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_MGA: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_MKD: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_MMK: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_MNT: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_MOP: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_MRO: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_MUR: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_MVR: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_MWK: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_MXN: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_MYR: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_MZN: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_NAD: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_NGN: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_NIO: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_NOK: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_NPR: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_NZD: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_OMR: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_PAB: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_PEN: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_PGK: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_PHP: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_PKR: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_PLN: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_PYG: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_QAR: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_RON: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_RSD: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_RUB: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_RWF: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_SAR: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_SBD: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_SCR: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_SDG: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_SEK: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_SGD: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_SHP: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_SLL: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_SOS: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_SRD: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_STD: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_SYP: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_SZL: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_THB: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_TJS: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_TMT: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_TND: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_TOP: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_TRY: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_TTD: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_TWD: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_TZS: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_UAH: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_UGX: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_USD: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_UYU: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_UZS: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_VEF: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_VND: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_VUV: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_WST: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_XAF: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_XCD: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_XOF: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_XPF: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_XXX: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_YER: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_ZAR: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_ZMW: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_ZWL: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]


class ICurrencyIdentifiersStatics2(_inspectable.IInspectable, factory=True):
    get_BYN: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]


class ICurrencyIdentifiersStatics3(_inspectable.IInspectable, factory=True):
    get_MRU: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_SSP: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_STN: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_VES: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]


class IGeographicRegion(_inspectable.IInspectable):
    get_Code: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_CodeTwoLetter: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_CodeThreeLetter: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_CodeThreeDigit: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_NativeName: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_CurrenciesInUse: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                   _type.HRESULT]


class IGeographicRegionFactory(_inspectable.IInspectable, factory=True):
    CreateGeographicRegion: _Callable[[_type.HSTRING,  # geographicRegionCode
                                       _Pointer[IGeographicRegion]],  # result
                                      _type.HRESULT]


class IGeographicRegionStatics(_inspectable.IInspectable, factory=True):
    IsSupported: _Callable[[_type.HSTRING,  # geographicRegionCode
                            _Pointer[_type.boolean]],  # result
                           _type.HRESULT]


class IJapanesePhoneme(_inspectable.IInspectable):
    get_DisplayText: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_YomiText: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_IsPhraseStart: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]


class IJapanesePhoneticAnalyzerStatics(_inspectable.IInspectable, factory=True):
    GetWords: _Callable[[_type.HSTRING,  # input
                         _Pointer[_Windows_Foundation_Collections.IVectorView[IJapanesePhoneme]]],  # result
                        _type.HRESULT]
    GetWordsWithMonoRubyOption: _Callable[[_type.HSTRING,  # input
                                           _type.boolean,  # monoRuby
                                           _Pointer[_Windows_Foundation_Collections.IVectorView[IJapanesePhoneme]]],  # result
                                          _type.HRESULT]


class ILanguage(_inspectable.IInspectable):
    get_LanguageTag: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_NativeName: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_Script: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]


class ILanguage2(_inspectable.IInspectable):
    get_LayoutDirection: _Callable[[_Pointer[_enum.Windows.Globalization.LanguageLayoutDirection]],  # value
                                   _type.HRESULT]


class ILanguage3(_inspectable.IInspectable):
    get_AbbreviatedName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]


class ILanguageExtensionSubtags(_inspectable.IInspectable):
    GetExtensionSubtags: _Callable[[_type.HSTRING,  # singleton
                                    _Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                   _type.HRESULT]


class ILanguageFactory(_inspectable.IInspectable, factory=True):
    CreateLanguage: _Callable[[_type.HSTRING,  # languageTag
                               _Pointer[ILanguage]],  # result
                              _type.HRESULT]


class ILanguageStatics(_inspectable.IInspectable, factory=True):
    IsWellFormed: _Callable[[_type.HSTRING,  # languageTag
                             _Pointer[_type.boolean]],  # result
                            _type.HRESULT]
    get_CurrentInputMethodLanguageTag: _Callable[[_Pointer[_type.HSTRING]],  # value
                                                 _type.HRESULT]


class ILanguageStatics2(_inspectable.IInspectable, factory=True):
    TrySetInputMethodLanguageTag: _Callable[[_type.HSTRING,  # languageTag
                                             _Pointer[_type.boolean]],  # result
                                            _type.HRESULT]


class ILanguageStatics3(_inspectable.IInspectable, factory=True):
    GetMuiCompatibleLanguageListFromLanguageTags: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # languageTags
                                                             _Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # result
                                                            _type.HRESULT]


class INumeralSystemIdentifiersStatics(_inspectable.IInspectable, factory=True):
    get_Arab: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_ArabExt: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Bali: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Beng: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Cham: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Deva: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_FullWide: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Gujr: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Guru: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_HaniDec: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Java: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Kali: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Khmr: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Knda: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Lana: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_LanaTham: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Laoo: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Latn: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Lepc: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Limb: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Mlym: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Mong: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Mtei: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Mymr: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_MymrShan: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Nkoo: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Olck: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Orya: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Saur: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Sund: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Talu: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_TamlDec: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Telu: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Thai: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Tibt: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Vaii: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class INumeralSystemIdentifiersStatics2(_inspectable.IInspectable, factory=True):
    get_Brah: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Osma: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_MathBold: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_MathDbl: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_MathSans: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_MathSanb: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_MathMono: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_ZmthBold: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_ZmthDbl: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_ZmthSans: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_ZmthSanb: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_ZmthMono: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]


class ITimeZoneOnCalendar(_inspectable.IInspectable):
    GetTimeZone: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    ChangeTimeZone: _Callable[[_type.HSTRING],  # timeZoneId
                              _type.HRESULT]
    TimeZoneAsFullString: _Callable[[_Pointer[_type.HSTRING]],  # result
                                    _type.HRESULT]
    TimeZoneAsString: _Callable[[_type.INT32,  # idealLength
                                 _Pointer[_type.HSTRING]],  # result
                                _type.HRESULT]
