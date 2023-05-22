from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...ApplicationModel import Background as _Windows_ApplicationModel_Background
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Security import Credentials as _Windows_Security_Credentials
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IDeviceAccessChangedEventArgs(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Devices.Enumeration.DeviceAccessStatus]],  # value
                          _type.HRESULT]


class IDeviceAccessChangedEventArgs2(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]


class IDeviceAccessInformation(_inspectable.IInspectable):
    add_AccessChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IDeviceAccessInformation, IDeviceAccessChangedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # cookie
                                 _type.HRESULT]
    remove_AccessChanged: _Callable[[_struct.EventRegistrationToken],  # cookie
                                    _type.HRESULT]
    get_CurrentStatus: _Callable[[_Pointer[_enum.Windows.Devices.Enumeration.DeviceAccessStatus]],  # status
                                 _type.HRESULT]


class IDeviceAccessInformationStatics(_inspectable.IInspectable, factory=True):
    CreateFromId: _Callable[[_type.HSTRING,  # deviceId
                             _Pointer[IDeviceAccessInformation]],  # value
                            _type.HRESULT]
    CreateFromDeviceClassId: _Callable[[_struct.GUID,  # deviceClassId
                                        _Pointer[IDeviceAccessInformation]],  # value
                                       _type.HRESULT]
    CreateFromDeviceClass: _Callable[[_enum.Windows.Devices.Enumeration.DeviceClass,  # deviceClass
                                      _Pointer[IDeviceAccessInformation]],  # value
                                     _type.HRESULT]


class IDeviceConnectionChangeTriggerDetails(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]


class IDeviceDisconnectButtonClickedEventArgs(_inspectable.IInspectable):
    get_Device: _Callable[[_Pointer[IDeviceInformation]],  # value
                          _type.HRESULT]


class IDeviceInformation(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_IsDefault: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_EnclosureLocation: _Callable[[_Pointer[IEnclosureLocation]],  # value
                                     _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _inspectable.IInspectable]]],  # value
                              _type.HRESULT]
    Update: _Callable[[IDeviceInformationUpdate],  # updateInfo
                      _type.HRESULT]
    GetThumbnailAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStreamWithContentType]]],  # asyncOp
                                 _type.HRESULT]
    GetGlyphThumbnailAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStreamWithContentType]]],  # asyncOp
                                      _type.HRESULT]


class IDeviceInformation2(_inspectable.IInspectable):
    get_Kind: _Callable[[_Pointer[_enum.Windows.Devices.Enumeration.DeviceInformationKind]],  # value
                        _type.HRESULT]
    get_Pairing: _Callable[[_Pointer[IDeviceInformationPairing]],  # value
                           _type.HRESULT]


class IDeviceInformationCustomPairing(_inspectable.IInspectable):
    PairAsync: _Callable[[_enum.Windows.Devices.Enumeration.DevicePairingKinds,  # pairingKindsSupported
                          _Pointer[_Windows_Foundation.IAsyncOperation[IDevicePairingResult]]],  # result
                         _type.HRESULT]
    PairWithProtectionLevelAsync: _Callable[[_enum.Windows.Devices.Enumeration.DevicePairingKinds,  # pairingKindsSupported
                                             _enum.Windows.Devices.Enumeration.DevicePairingProtectionLevel,  # minProtectionLevel
                                             _Pointer[_Windows_Foundation.IAsyncOperation[IDevicePairingResult]]],  # result
                                            _type.HRESULT]
    PairWithProtectionLevelAndSettingsAsync: _Callable[[_enum.Windows.Devices.Enumeration.DevicePairingKinds,  # pairingKindsSupported
                                                        _enum.Windows.Devices.Enumeration.DevicePairingProtectionLevel,  # minProtectionLevel
                                                        IDevicePairingSettings,  # devicePairingSettings
                                                        _Pointer[_Windows_Foundation.IAsyncOperation[IDevicePairingResult]]],  # result
                                                       _type.HRESULT]
    add_PairingRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IDeviceInformationCustomPairing, IDevicePairingRequestedEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_PairingRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]


class IDeviceInformationPairing(_inspectable.IInspectable):
    get_IsPaired: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_CanPair: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    PairAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IDevicePairingResult]]],  # result
                         _type.HRESULT]
    PairWithProtectionLevelAsync: _Callable[[_enum.Windows.Devices.Enumeration.DevicePairingProtectionLevel,  # minProtectionLevel
                                             _Pointer[_Windows_Foundation.IAsyncOperation[IDevicePairingResult]]],  # result
                                            _type.HRESULT]


class IDeviceInformationPairing2(_inspectable.IInspectable):
    get_ProtectionLevel: _Callable[[_Pointer[_enum.Windows.Devices.Enumeration.DevicePairingProtectionLevel]],  # value
                                   _type.HRESULT]
    get_Custom: _Callable[[_Pointer[IDeviceInformationCustomPairing]],  # value
                          _type.HRESULT]
    PairWithProtectionLevelAndSettingsAsync: _Callable[[_enum.Windows.Devices.Enumeration.DevicePairingProtectionLevel,  # minProtectionLevel
                                                        IDevicePairingSettings,  # devicePairingSettings
                                                        _Pointer[_Windows_Foundation.IAsyncOperation[IDevicePairingResult]]],  # result
                                                       _type.HRESULT]
    UnpairAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IDeviceUnpairingResult]]],  # result
                           _type.HRESULT]


class IDeviceInformationPairingStatics(_inspectable.IInspectable, factory=True):
    TryRegisterForAllInboundPairingRequests: _Callable[[_enum.Windows.Devices.Enumeration.DevicePairingKinds,  # pairingKindsSupported
                                                        _Pointer[_type.boolean]],  # result
                                                       _type.HRESULT]


class IDeviceInformationPairingStatics2(_inspectable.IInspectable, factory=True):
    TryRegisterForAllInboundPairingRequestsWithProtectionLevel: _Callable[[_enum.Windows.Devices.Enumeration.DevicePairingKinds,  # pairingKindsSupported
                                                                           _enum.Windows.Devices.Enumeration.DevicePairingProtectionLevel,  # minProtectionLevel
                                                                           _Pointer[_type.boolean]],  # result
                                                                          _type.HRESULT]


class IDeviceInformationStatics(_inspectable.IInspectable, factory=True):
    CreateFromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                                  _Pointer[_Windows_Foundation.IAsyncOperation[IDeviceInformation]]],  # asyncOp
                                 _type.HRESULT]
    CreateFromIdAsyncAdditionalProperties: _Callable[[_type.HSTRING,  # deviceId
                                                      _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # additionalProperties
                                                      _Pointer[_Windows_Foundation.IAsyncOperation[IDeviceInformation]]],  # asyncOp
                                                     _type.HRESULT]
    FindAllAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IDeviceInformation]]]],  # asyncOp
                            _type.HRESULT]
    FindAllAsyncDeviceClass: _Callable[[_enum.Windows.Devices.Enumeration.DeviceClass,  # deviceClass
                                        _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IDeviceInformation]]]],  # asyncOp
                                       _type.HRESULT]
    FindAllAsyncAqsFilter: _Callable[[_type.HSTRING,  # aqsFilter
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IDeviceInformation]]]],  # asyncOp
                                     _type.HRESULT]
    FindAllAsyncAqsFilterAndAdditionalProperties: _Callable[[_type.HSTRING,  # aqsFilter
                                                             _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # additionalProperties
                                                             _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IDeviceInformation]]]],  # asyncOp
                                                            _type.HRESULT]
    CreateWatcher: _Callable[[_Pointer[IDeviceWatcher]],  # watcher
                             _type.HRESULT]
    CreateWatcherDeviceClass: _Callable[[_enum.Windows.Devices.Enumeration.DeviceClass,  # deviceClass
                                         _Pointer[IDeviceWatcher]],  # watcher
                                        _type.HRESULT]
    CreateWatcherAqsFilter: _Callable[[_type.HSTRING,  # aqsFilter
                                       _Pointer[IDeviceWatcher]],  # watcher
                                      _type.HRESULT]
    CreateWatcherAqsFilterAndAdditionalProperties: _Callable[[_type.HSTRING,  # aqsFilter
                                                              _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # additionalProperties
                                                              _Pointer[IDeviceWatcher]],  # watcher
                                                             _type.HRESULT]


class IDeviceInformationStatics2(_inspectable.IInspectable, factory=True):
    GetAqsFilterFromDeviceClass: _Callable[[_enum.Windows.Devices.Enumeration.DeviceClass,  # deviceClass
                                            _Pointer[_type.HSTRING]],  # aqsFilter
                                           _type.HRESULT]
    CreateFromIdAsyncWithKindAndAdditionalProperties: _Callable[[_type.HSTRING,  # deviceId
                                                                 _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # additionalProperties
                                                                 _enum.Windows.Devices.Enumeration.DeviceInformationKind,  # kind
                                                                 _Pointer[_Windows_Foundation.IAsyncOperation[IDeviceInformation]]],  # asyncOp
                                                                _type.HRESULT]
    FindAllAsyncWithKindAqsFilterAndAdditionalProperties: _Callable[[_type.HSTRING,  # aqsFilter
                                                                     _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # additionalProperties
                                                                     _enum.Windows.Devices.Enumeration.DeviceInformationKind,  # kind
                                                                     _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IDeviceInformation]]]],  # asyncOp
                                                                    _type.HRESULT]
    CreateWatcherWithKindAqsFilterAndAdditionalProperties: _Callable[[_type.HSTRING,  # aqsFilter
                                                                      _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # additionalProperties
                                                                      _enum.Windows.Devices.Enumeration.DeviceInformationKind,  # kind
                                                                      _Pointer[IDeviceWatcher]],  # watcher
                                                                     _type.HRESULT]


class IDeviceInformationUpdate(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _inspectable.IInspectable]]],  # value
                              _type.HRESULT]


class IDeviceInformationUpdate2(_inspectable.IInspectable):
    get_Kind: _Callable[[_Pointer[_enum.Windows.Devices.Enumeration.DeviceInformationKind]],  # value
                        _type.HRESULT]


class IDevicePairingRequestedEventArgs(_inspectable.IInspectable):
    get_DeviceInformation: _Callable[[_Pointer[IDeviceInformation]],  # value
                                     _type.HRESULT]
    get_PairingKind: _Callable[[_Pointer[_enum.Windows.Devices.Enumeration.DevicePairingKinds]],  # value
                               _type.HRESULT]
    get_Pin: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    Accept: _Callable[[],
                      _type.HRESULT]
    AcceptWithPin: _Callable[[_type.HSTRING],  # pin
                             _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IDevicePairingRequestedEventArgs2(_inspectable.IInspectable):
    AcceptWithPasswordCredential: _Callable[[_Windows_Security_Credentials.IPasswordCredential],  # passwordCredential
                                            _type.HRESULT]


class IDevicePairingResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Devices.Enumeration.DevicePairingResultStatus]],  # status
                          _type.HRESULT]
    get_ProtectionLevelUsed: _Callable[[_Pointer[_enum.Windows.Devices.Enumeration.DevicePairingProtectionLevel]],  # value
                                       _type.HRESULT]


class IDevicePairingSettings(_inspectable.IInspectable):
    pass


class IDevicePicker(_inspectable.IInspectable):
    get_Filter: _Callable[[_Pointer[IDevicePickerFilter]],  # filter
                          _type.HRESULT]
    get_Appearance: _Callable[[_Pointer[IDevicePickerAppearance]],  # value
                              _type.HRESULT]
    get_RequestedProperties: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                       _type.HRESULT]
    add_DeviceSelected: _Callable[[_Windows_Foundation.ITypedEventHandler[IDevicePicker, IDeviceSelectedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_DeviceSelected: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_DisconnectButtonClicked: _Callable[[_Windows_Foundation.ITypedEventHandler[IDevicePicker, IDeviceDisconnectButtonClickedEventArgs],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_DisconnectButtonClicked: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]
    add_DevicePickerDismissed: _Callable[[_Windows_Foundation.ITypedEventHandler[IDevicePicker, _inspectable.IInspectable],  # handler
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_DevicePickerDismissed: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]
    Show: _Callable[[_struct.Windows.Foundation.Rect],  # selection
                    _type.HRESULT]
    ShowWithPlacement: _Callable[[_struct.Windows.Foundation.Rect,  # selection
                                  _enum.Windows.UI.Popups.Placement],  # placement
                                 _type.HRESULT]
    PickSingleDeviceAsync: _Callable[[_struct.Windows.Foundation.Rect,  # selection
                                      _Pointer[_Windows_Foundation.IAsyncOperation[IDeviceInformation]]],  # operation
                                     _type.HRESULT]
    PickSingleDeviceAsyncWithPlacement: _Callable[[_struct.Windows.Foundation.Rect,  # selection
                                                   _enum.Windows.UI.Popups.Placement,  # placement
                                                   _Pointer[_Windows_Foundation.IAsyncOperation[IDeviceInformation]]],  # operation
                                                  _type.HRESULT]
    Hide: _Callable[[],
                    _type.HRESULT]
    SetDisplayStatus: _Callable[[IDeviceInformation,  # device
                                 _type.HSTRING,  # status
                                 _enum.Windows.Devices.Enumeration.DevicePickerDisplayStatusOptions],  # options
                                _type.HRESULT]


class IDevicePickerAppearance(_inspectable.IInspectable):
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Title: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_ForegroundColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                   _type.HRESULT]
    put_ForegroundColor: _Callable[[_struct.Windows.UI.Color],  # value
                                   _type.HRESULT]
    get_BackgroundColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                   _type.HRESULT]
    put_BackgroundColor: _Callable[[_struct.Windows.UI.Color],  # value
                                   _type.HRESULT]
    get_AccentColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                               _type.HRESULT]
    put_AccentColor: _Callable[[_struct.Windows.UI.Color],  # value
                               _type.HRESULT]
    get_SelectedForegroundColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                           _type.HRESULT]
    put_SelectedForegroundColor: _Callable[[_struct.Windows.UI.Color],  # value
                                           _type.HRESULT]
    get_SelectedBackgroundColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                           _type.HRESULT]
    put_SelectedBackgroundColor: _Callable[[_struct.Windows.UI.Color],  # value
                                           _type.HRESULT]
    get_SelectedAccentColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                       _type.HRESULT]
    put_SelectedAccentColor: _Callable[[_struct.Windows.UI.Color],  # value
                                       _type.HRESULT]


class IDevicePickerFilter(_inspectable.IInspectable):
    get_SupportedDeviceClasses: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_enum.Windows.Devices.Enumeration.DeviceClass]]],  # value
                                          _type.HRESULT]
    get_SupportedDeviceSelectors: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                            _type.HRESULT]


class IDeviceSelectedEventArgs(_inspectable.IInspectable):
    get_SelectedDevice: _Callable[[_Pointer[IDeviceInformation]],  # value
                                  _type.HRESULT]


class IDeviceUnpairingResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Devices.Enumeration.DeviceUnpairingResultStatus]],  # status
                          _type.HRESULT]


class IDeviceWatcher(_inspectable.IInspectable):
    add_Added: _Callable[[_Windows_Foundation.ITypedEventHandler[IDeviceWatcher, IDeviceInformation],  # handler
                          _Pointer[_struct.EventRegistrationToken]],  # token
                         _type.HRESULT]
    remove_Added: _Callable[[_struct.EventRegistrationToken],  # token
                            _type.HRESULT]
    add_Updated: _Callable[[_Windows_Foundation.ITypedEventHandler[IDeviceWatcher, IDeviceInformationUpdate],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Updated: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_Removed: _Callable[[_Windows_Foundation.ITypedEventHandler[IDeviceWatcher, IDeviceInformationUpdate],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Removed: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_EnumerationCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IDeviceWatcher, _inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_EnumerationCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    add_Stopped: _Callable[[_Windows_Foundation.ITypedEventHandler[IDeviceWatcher, _inspectable.IInspectable],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Stopped: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.Devices.Enumeration.DeviceWatcherStatus]],  # status
                          _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]


class IDeviceWatcher2(_inspectable.IInspectable):
    GetBackgroundTrigger: _Callable[[_Windows_Foundation_Collections.IIterable[_enum.Windows.Devices.Enumeration.DeviceWatcherEventKind],  # requestedEventKinds
                                     _Pointer[_Windows_ApplicationModel_Background.IDeviceWatcherTrigger]],  # trigger
                                    _type.HRESULT]


class IDeviceWatcherEvent(_inspectable.IInspectable):
    get_Kind: _Callable[[_Pointer[_enum.Windows.Devices.Enumeration.DeviceWatcherEventKind]],  # value
                        _type.HRESULT]
    get_DeviceInformation: _Callable[[_Pointer[IDeviceInformation]],  # value
                                     _type.HRESULT]
    get_DeviceInformationUpdate: _Callable[[_Pointer[IDeviceInformationUpdate]],  # value
                                           _type.HRESULT]


class IDeviceWatcherTriggerDetails(_inspectable.IInspectable):
    get_DeviceWatcherEvents: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IDeviceWatcherEvent]]],  # value
                                       _type.HRESULT]


class IEnclosureLocation(_inspectable.IInspectable):
    get_InDock: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    get_InLid: _Callable[[_Pointer[_type.boolean]],  # value
                         _type.HRESULT]
    get_Panel: _Callable[[_Pointer[_enum.Windows.Devices.Enumeration.Panel]],  # value
                         _type.HRESULT]


class IEnclosureLocation2(_inspectable.IInspectable):
    get_RotationAngleInDegreesClockwise: _Callable[[_Pointer[_type.UINT32]],  # value
                                                   _type.HRESULT]
