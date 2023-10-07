from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Maps as _Windows_Services_Maps
from .... import Foundation as _Windows_Foundation
from ....Devices import Geolocation as _Windows_Devices_Geolocation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class ILocalCategoriesStatics(_inspectable.IInspectable, factory=True):
    get_BankAndCreditUnions: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    get_EatDrink: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Hospitals: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_HotelsAndMotels: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_All: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_Parking: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_SeeDo: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Shop: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class ILocalLocation(_inspectable.IInspectable):
    get_Address: _Callable[[_Pointer[_Windows_Services_Maps.IMapAddress]],  # value
                           _type.HRESULT]
    get_Identifier: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Point: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeopoint]],  # value
                         _type.HRESULT]
    get_PhoneNumber: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_DataAttribution: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]


class ILocalLocation2(_inspectable.IInspectable):
    get_Category: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_RatingInfo: _Callable[[_Pointer[ILocalLocationRatingInfo]],  # value
                              _type.HRESULT]
    get_HoursOfOperation: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[ILocalLocationHoursOfOperationItem]]],  # value
                                    _type.HRESULT]


class ILocalLocationFinderResult(_inspectable.IInspectable):
    get_LocalLocations: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[ILocalLocation]]],  # value
                                  _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.Services.Maps.LocalSearch.LocalLocationFinderStatus]],  # value
                          _type.HRESULT]


class ILocalLocationFinderStatics(_inspectable.IInspectable, factory=True):
    FindLocalLocationsAsync: _Callable[[_type.HSTRING,  # searchTerm
                                        _Windows_Devices_Geolocation.IGeocircle,  # searchArea
                                        _type.HSTRING,  # localCategory
                                        _type.UINT32,  # maxResults
                                        _Pointer[_Windows_Foundation.IAsyncOperation[ILocalLocationFinderResult]]],  # result
                                       _type.HRESULT]


class ILocalLocationHoursOfOperationItem(_inspectable.IInspectable):
    get_Day: _Callable[[_Pointer[_enum.Windows.Globalization.DayOfWeek]],  # value
                       _type.HRESULT]
    get_Start: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                         _type.HRESULT]
    get_Span: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                        _type.HRESULT]


class ILocalLocationRatingInfo(_inspectable.IInspectable):
    get_AggregateRating: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                                   _type.HRESULT]
    get_RatingCount: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                               _type.HRESULT]
    get_ProviderIdentifier: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]


class IPlaceInfoHelperStatics(_inspectable.IInspectable, factory=True):
    CreateFromLocalLocation: _Callable[[ILocalLocation,  # location
                                        _Pointer[_Windows_Services_Maps.IPlaceInfo]],  # resultValue
                                       _type.HRESULT]
