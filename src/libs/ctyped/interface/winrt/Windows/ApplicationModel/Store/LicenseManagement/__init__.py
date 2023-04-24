from __future__ import annotations

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ....Storage import Streams as _Windows_Storage_Streams
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import type as _type
from ......._utils import _Pointer


class ILicenseManagerStatics(_inspectable.IInspectable):
    AddLicenseAsync: _Callable[[_Windows_Storage_Streams.IBuffer,  # license
                                _Pointer[_Windows_Foundation.IAsyncAction]],  # action
                               _type.HRESULT]
    GetSatisfactionInfosAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # contentIds
                                          _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # keyIds
                                          _Pointer[_Windows_Foundation.IAsyncOperation[ILicenseSatisfactionResult]]],  # operation
                                         _type.HRESULT]

    _factory = True


class ILicenseManagerStatics2(_inspectable.IInspectable):
    RefreshLicensesAsync: _Callable[[_enum.Windows.ApplicationModel.Store.LicenseManagement.LicenseRefreshOption,  # refreshOption
                                     _Pointer[_Windows_Foundation.IAsyncAction]],  # action
                                    _type.HRESULT]

    _factory = True


class ILicenseSatisfactionInfo(_inspectable.IInspectable):
    get_SatisfiedByDevice: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    get_SatisfiedByOpenLicense: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    get_SatisfiedByTrial: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_SatisfiedByPass: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_SatisfiedByInstallMedia: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    get_SatisfiedBySignedInUser: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    get_IsSatisfied: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]


class ILicenseSatisfactionResult(_inspectable.IInspectable):
    get_LicenseSatisfactionInfos: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, ILicenseSatisfactionInfo]]],  # value
                                            _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]
