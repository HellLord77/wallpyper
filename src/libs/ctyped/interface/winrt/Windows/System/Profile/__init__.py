from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import System as _Windows_System
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IAnalyticsInfoStatics(_inspectable.IInspectable):
    get_VersionInfo: _Callable[[_Pointer[IAnalyticsVersionInfo]],  # value
                               _type.HRESULT]
    get_DeviceForm: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]

    _factory = True


class IAnalyticsInfoStatics2(_inspectable.IInspectable):
    GetSystemPropertiesAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # attributeNames
                                         _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _type.HSTRING]]]],  # operation
                                        _type.HRESULT]

    _factory = True


class IAnalyticsVersionInfo(_inspectable.IInspectable):
    get_DeviceFamily: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_DeviceFamilyVersion: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]


class IAnalyticsVersionInfo2(_inspectable.IInspectable):
    get_ProductName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class IAppApplicabilityStatics(_inspectable.IInspectable):
    GetUnsupportedAppRequirements: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # capabilities
                                              _Pointer[_Windows_Foundation_Collections.IVectorView[IUnsupportedAppRequirement]]],  # result
                                             _type.HRESULT]

    _factory = True


class IEducationSettingsStatics(_inspectable.IInspectable):
    get_IsEducationEnvironment: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]

    _factory = True


class IHardwareIdentificationStatics(_inspectable.IInspectable):
    GetPackageSpecificToken: _Callable[[_Windows_Storage_Streams.IBuffer,  # nonce
                                        _Pointer[IHardwareToken]],  # packageSpecificHardwareToken
                                       _type.HRESULT]

    _factory = True


class IHardwareToken(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                      _type.HRESULT]
    get_Signature: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                             _type.HRESULT]
    get_Certificate: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                               _type.HRESULT]


class IKnownRetailInfoPropertiesStatics(_inspectable.IInspectable):
    get_RetailAccessCode: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_ManufacturerName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_ModelName: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_DisplayModelName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_Price: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_IsFeatured: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_FormFactor: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_ScreenSize: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_Weight: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_DisplayDescription: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_BatteryLifeDescription: _Callable[[_Pointer[_type.HSTRING]],  # value
                                          _type.HRESULT]
    get_ProcessorDescription: _Callable[[_Pointer[_type.HSTRING]],  # value
                                        _type.HRESULT]
    get_Memory: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_StorageDescription: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_GraphicsDescription: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    get_FrontCameraDescription: _Callable[[_Pointer[_type.HSTRING]],  # value
                                          _type.HRESULT]
    get_RearCameraDescription: _Callable[[_Pointer[_type.HSTRING]],  # value
                                         _type.HRESULT]
    get_HasNfc: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_HasSdSlot: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_HasOpticalDrive: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_IsOfficeInstalled: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    get_WindowsEdition: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]

    _factory = True


class IPlatformDiagnosticsAndUsageDataSettingsStatics(_inspectable.IInspectable):
    get_CollectionLevel: _Callable[[_Pointer[_enum.Windows.System.Profile.PlatformDataCollectionLevel]],  # value
                                   _type.HRESULT]
    add_CollectionLevelChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_CollectionLevelChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]
    CanCollectDiagnostics: _Callable[[_enum.Windows.System.Profile.PlatformDataCollectionLevel,  # level
                                      _Pointer[_type.boolean]],  # result
                                     _type.HRESULT]

    _factory = True


class IRetailInfoStatics(_inspectable.IInspectable):
    get_IsDemoModeEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _inspectable.IInspectable]]],  # value
                              _type.HRESULT]

    _factory = True


class ISharedModeSettingsStatics(_inspectable.IInspectable):
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]

    _factory = True


class ISharedModeSettingsStatics2(_inspectable.IInspectable):
    get_ShouldAvoidLocalStorage: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]

    _factory = True


class ISmartAppControlPolicyStatics(_inspectable.IInspectable):
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    add_Changed: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Changed: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]

    _factory = True


class ISystemIdentificationInfo(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                      _type.HRESULT]
    get_Source: _Callable[[_Pointer[_enum.Windows.System.Profile.SystemIdentificationSource]],  # value
                          _type.HRESULT]


class ISystemIdentificationStatics(_inspectable.IInspectable):
    GetSystemIdForPublisher: _Callable[[_Pointer[ISystemIdentificationInfo]],  # result
                                       _type.HRESULT]
    GetSystemIdForUser: _Callable[[_Windows_System.IUser,  # user
                                   _Pointer[ISystemIdentificationInfo]],  # result
                                  _type.HRESULT]

    _factory = True


class ISystemSetupInfoStatics(_inspectable.IInspectable):
    get_OutOfBoxExperienceState: _Callable[[_Pointer[_enum.Windows.System.Profile.SystemOutOfBoxExperienceState]],  # value
                                           _type.HRESULT]
    add_OutOfBoxExperienceStateChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                                  _type.HRESULT]
    remove_OutOfBoxExperienceStateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                     _type.HRESULT]

    _factory = True


class IUnsupportedAppRequirement(_inspectable.IInspectable):
    get_Requirement: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Reasons: _Callable[[_Pointer[_enum.Windows.System.Profile.UnsupportedAppRequirementReasons]],  # value
                           _type.HRESULT]


class IWindowsIntegrityPolicyStatics(_inspectable.IInspectable):
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_IsEnabledForTrial: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    get_CanDisable: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_IsDisableSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    add_PolicyChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_PolicyChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]

    _factory = True
