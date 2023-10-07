from __future__ import annotations as _

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from ....Devices import Geolocation as _Windows_Devices_Geolocation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IOfflineMapPackage(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Services.Maps.OfflineMaps.OfflineMapPackageStatus]],  # value
                          _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_EnclosingRegionName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    get_EstimatedSizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                        _type.HRESULT]
    remove_StatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_StatusChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IOfflineMapPackage, _inspectable.IInspectable],  # value
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    RequestStartDownloadAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IOfflineMapPackageStartDownloadResult]]],  # value
                                         _type.HRESULT]


class IOfflineMapPackageQueryResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Services.Maps.OfflineMaps.OfflineMapPackageQueryStatus]],  # value
                          _type.HRESULT]
    get_Packages: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IOfflineMapPackage]]],  # value
                            _type.HRESULT]


class IOfflineMapPackageStartDownloadResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Services.Maps.OfflineMaps.OfflineMapPackageStartDownloadStatus]],  # value
                          _type.HRESULT]


class IOfflineMapPackageStatics(_inspectable.IInspectable, factory=True):
    FindPackagesAsync: _Callable[[_Windows_Devices_Geolocation.IGeopoint,  # queryPoint
                                  _Pointer[_Windows_Foundation.IAsyncOperation[IOfflineMapPackageQueryResult]]],  # result
                                 _type.HRESULT]
    FindPackagesInBoundingBoxAsync: _Callable[[_Windows_Devices_Geolocation.IGeoboundingBox,  # queryBoundingBox
                                               _Pointer[_Windows_Foundation.IAsyncOperation[IOfflineMapPackageQueryResult]]],  # result
                                              _type.HRESULT]
    FindPackagesInGeocircleAsync: _Callable[[_Windows_Devices_Geolocation.IGeocircle,  # queryCircle
                                             _Pointer[_Windows_Foundation.IAsyncOperation[IOfflineMapPackageQueryResult]]],  # result
                                            _type.HRESULT]
