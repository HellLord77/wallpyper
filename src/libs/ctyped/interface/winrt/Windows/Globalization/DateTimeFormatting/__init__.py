from __future__ import annotations as _

from typing import Callable as _Callable

from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IDateTimeFormatter(_inspectable.IInspectable):
    get_Languages: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                             _type.HRESULT]
    get_GeographicRegion: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_Calendar: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Clock: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_NumeralSystem: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    put_NumeralSystem: _Callable[[_type.HSTRING],  # value
                                 _type.HRESULT]
    get_Patterns: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                            _type.HRESULT]
    get_Template: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    Format: _Callable[[_struct.Windows.Foundation.DateTime,  # value
                       _Pointer[_type.HSTRING]],  # result
                      _type.HRESULT]
    get_IncludeYear: _Callable[[_Pointer[_enum.Windows.Globalization.DateTimeFormatting.YearFormat]],  # value
                               _type.HRESULT]
    get_IncludeMonth: _Callable[[_Pointer[_enum.Windows.Globalization.DateTimeFormatting.MonthFormat]],  # value
                                _type.HRESULT]
    get_IncludeDayOfWeek: _Callable[[_Pointer[_enum.Windows.Globalization.DateTimeFormatting.DayOfWeekFormat]],  # value
                                    _type.HRESULT]
    get_IncludeDay: _Callable[[_Pointer[_enum.Windows.Globalization.DateTimeFormatting.DayFormat]],  # value
                              _type.HRESULT]
    get_IncludeHour: _Callable[[_Pointer[_enum.Windows.Globalization.DateTimeFormatting.HourFormat]],  # value
                               _type.HRESULT]
    get_IncludeMinute: _Callable[[_Pointer[_enum.Windows.Globalization.DateTimeFormatting.MinuteFormat]],  # value
                                 _type.HRESULT]
    get_IncludeSecond: _Callable[[_Pointer[_enum.Windows.Globalization.DateTimeFormatting.SecondFormat]],  # value
                                 _type.HRESULT]
    get_ResolvedLanguage: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_ResolvedGeographicRegion: _Callable[[_Pointer[_type.HSTRING]],  # value
                                            _type.HRESULT]


class IDateTimeFormatter2(_inspectable.IInspectable):
    FormatUsingTimeZone: _Callable[[_struct.Windows.Foundation.DateTime,  # datetime
                                    _type.HSTRING,  # timeZoneId
                                    _Pointer[_type.HSTRING]],  # result
                                   _type.HRESULT]


class IDateTimeFormatterFactory(_inspectable.IInspectable, factory=True):
    CreateDateTimeFormatter: _Callable[[_type.HSTRING,  # formatTemplate
                                        _Pointer[IDateTimeFormatter]],  # result
                                       _type.HRESULT]
    CreateDateTimeFormatterLanguages: _Callable[[_type.HSTRING,  # formatTemplate
                                                 _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # languages
                                                 _Pointer[IDateTimeFormatter]],  # result
                                                _type.HRESULT]
    CreateDateTimeFormatterContext: _Callable[[_type.HSTRING,  # formatTemplate
                                               _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # languages
                                               _type.HSTRING,  # geographicRegion
                                               _type.HSTRING,  # calendar
                                               _type.HSTRING,  # clock
                                               _Pointer[IDateTimeFormatter]],  # result
                                              _type.HRESULT]
    CreateDateTimeFormatterDate: _Callable[[_enum.Windows.Globalization.DateTimeFormatting.YearFormat,  # yearFormat
                                            _enum.Windows.Globalization.DateTimeFormatting.MonthFormat,  # monthFormat
                                            _enum.Windows.Globalization.DateTimeFormatting.DayFormat,  # dayFormat
                                            _enum.Windows.Globalization.DateTimeFormatting.DayOfWeekFormat,  # dayOfWeekFormat
                                            _Pointer[IDateTimeFormatter]],  # result
                                           _type.HRESULT]
    CreateDateTimeFormatterTime: _Callable[[_enum.Windows.Globalization.DateTimeFormatting.HourFormat,  # hourFormat
                                            _enum.Windows.Globalization.DateTimeFormatting.MinuteFormat,  # minuteFormat
                                            _enum.Windows.Globalization.DateTimeFormatting.SecondFormat,  # secondFormat
                                            _Pointer[IDateTimeFormatter]],  # result
                                           _type.HRESULT]
    CreateDateTimeFormatterDateTimeLanguages: _Callable[[_enum.Windows.Globalization.DateTimeFormatting.YearFormat,  # yearFormat
                                                         _enum.Windows.Globalization.DateTimeFormatting.MonthFormat,  # monthFormat
                                                         _enum.Windows.Globalization.DateTimeFormatting.DayFormat,  # dayFormat
                                                         _enum.Windows.Globalization.DateTimeFormatting.DayOfWeekFormat,  # dayOfWeekFormat
                                                         _enum.Windows.Globalization.DateTimeFormatting.HourFormat,  # hourFormat
                                                         _enum.Windows.Globalization.DateTimeFormatting.MinuteFormat,  # minuteFormat
                                                         _enum.Windows.Globalization.DateTimeFormatting.SecondFormat,  # secondFormat
                                                         _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # languages
                                                         _Pointer[IDateTimeFormatter]],  # result
                                                        _type.HRESULT]
    CreateDateTimeFormatterDateTimeContext: _Callable[[_enum.Windows.Globalization.DateTimeFormatting.YearFormat,  # yearFormat
                                                       _enum.Windows.Globalization.DateTimeFormatting.MonthFormat,  # monthFormat
                                                       _enum.Windows.Globalization.DateTimeFormatting.DayFormat,  # dayFormat
                                                       _enum.Windows.Globalization.DateTimeFormatting.DayOfWeekFormat,  # dayOfWeekFormat
                                                       _enum.Windows.Globalization.DateTimeFormatting.HourFormat,  # hourFormat
                                                       _enum.Windows.Globalization.DateTimeFormatting.MinuteFormat,  # minuteFormat
                                                       _enum.Windows.Globalization.DateTimeFormatting.SecondFormat,  # secondFormat
                                                       _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # languages
                                                       _type.HSTRING,  # geographicRegion
                                                       _type.HSTRING,  # calendar
                                                       _type.HSTRING,  # clock
                                                       _Pointer[IDateTimeFormatter]],  # result
                                                      _type.HRESULT]


class IDateTimeFormatterStatics(_inspectable.IInspectable, factory=True):
    get_LongDate: _Callable[[_Pointer[IDateTimeFormatter]],  # value
                            _type.HRESULT]
    get_LongTime: _Callable[[_Pointer[IDateTimeFormatter]],  # value
                            _type.HRESULT]
    get_ShortDate: _Callable[[_Pointer[IDateTimeFormatter]],  # value
                             _type.HRESULT]
    get_ShortTime: _Callable[[_Pointer[IDateTimeFormatter]],  # value
                             _type.HRESULT]
