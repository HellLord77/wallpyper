from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...Devices import Enumeration as _Windows_Devices_Enumeration
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IDialApp(_inspectable.IInspectable):
    get_AppName: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    RequestLaunchAsync: _Callable[[_type.HSTRING,  # appArgument
                                   _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Media.DialProtocol.DialAppLaunchResult]]],  # value
                                  _type.HRESULT]
    StopAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Media.DialProtocol.DialAppStopResult]]],  # value
                         _type.HRESULT]
    GetAppStateAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IDialAppStateDetails]]],  # value
                                _type.HRESULT]


class IDialAppStateDetails(_inspectable.IInspectable):
    get_State: _Callable[[_Pointer[_enum.Windows.Media.DialProtocol.DialAppState]],  # value
                         _type.HRESULT]
    get_FullXml: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]


class IDialDevice(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    GetDialApp: _Callable[[_type.HSTRING,  # appName
                           _Pointer[IDialApp]],  # value
                          _type.HRESULT]


class IDialDevice2(_inspectable.IInspectable):
    get_FriendlyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_Thumbnail: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # value
                             _type.HRESULT]


class IDialDevicePicker(_inspectable.IInspectable):
    get_Filter: _Callable[[_Pointer[IDialDevicePickerFilter]],  # value
                          _type.HRESULT]
    get_Appearance: _Callable[[_Pointer[_Windows_Devices_Enumeration.IDevicePickerAppearance]],  # value
                              _type.HRESULT]
    add_DialDeviceSelected: _Callable[[_Windows_Foundation.ITypedEventHandler[IDialDevicePicker, IDialDeviceSelectedEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_DialDeviceSelected: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_DisconnectButtonClicked: _Callable[[_Windows_Foundation.ITypedEventHandler[IDialDevicePicker, IDialDisconnectButtonClickedEventArgs],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_DisconnectButtonClicked: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]
    add_DialDevicePickerDismissed: _Callable[[_Windows_Foundation.ITypedEventHandler[IDialDevicePicker, _inspectable.IInspectable],  # handler
                                              _Pointer[_struct.EventRegistrationToken]],  # token
                                             _type.HRESULT]
    remove_DialDevicePickerDismissed: _Callable[[_struct.EventRegistrationToken],  # token
                                                _type.HRESULT]
    Show: _Callable[[_struct.Windows.Foundation.Rect],  # selection
                    _type.HRESULT]
    ShowWithPlacement: _Callable[[_struct.Windows.Foundation.Rect,  # selection
                                  _enum.Windows.UI.Popups.Placement],  # preferredPlacement
                                 _type.HRESULT]
    PickSingleDialDeviceAsync: _Callable[[_struct.Windows.Foundation.Rect,  # selection
                                          _Pointer[_Windows_Foundation.IAsyncOperation[IDialDevice]]],  # operation
                                         _type.HRESULT]
    PickSingleDialDeviceAsyncWithPlacement: _Callable[[_struct.Windows.Foundation.Rect,  # selection
                                                       _enum.Windows.UI.Popups.Placement,  # preferredPlacement
                                                       _Pointer[_Windows_Foundation.IAsyncOperation[IDialDevice]]],  # operation
                                                      _type.HRESULT]
    Hide: _Callable[[],
                    _type.HRESULT]
    SetDisplayStatus: _Callable[[IDialDevice,  # device
                                 _enum.Windows.Media.DialProtocol.DialDeviceDisplayStatus],  # status
                                _type.HRESULT]


class IDialDevicePickerFilter(_inspectable.IInspectable):
    get_SupportedAppNames: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                     _type.HRESULT]


class IDialDeviceSelectedEventArgs(_inspectable.IInspectable):
    get_SelectedDialDevice: _Callable[[_Pointer[IDialDevice]],  # value
                                      _type.HRESULT]


class IDialDeviceStatics(_inspectable.IInspectable):
    GetDeviceSelector: _Callable[[_type.HSTRING,  # appName
                                  _Pointer[_type.HSTRING]],  # selector
                                 _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # value
                            _Pointer[_Windows_Foundation.IAsyncOperation[IDialDevice]]],  # operation
                           _type.HRESULT]
    DeviceInfoSupportsDialAsync: _Callable[[_Windows_Devices_Enumeration.IDeviceInformation,  # device
                                            _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                           _type.HRESULT]

    _factory = True


class IDialDisconnectButtonClickedEventArgs(_inspectable.IInspectable):
    get_Device: _Callable[[_Pointer[IDialDevice]],  # value
                          _type.HRESULT]


class IDialReceiverApp(_inspectable.IInspectable):
    GetAdditionalDataAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IMap[_type.HSTRING, _type.HSTRING]]]],  # operation
                                      _type.HRESULT]
    SetAdditionalDataAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Foundation_Collections.IKeyValuePair[_type.HSTRING, _type.HSTRING]],  # additionalData
                                       _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                      _type.HRESULT]


class IDialReceiverApp2(_inspectable.IInspectable):
    GetUniqueDeviceNameAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                        _type.HRESULT]


class IDialReceiverAppStatics(_inspectable.IInspectable):
    get_Current: _Callable[[_Pointer[IDialReceiverApp]],  # value
                           _type.HRESULT]

    _factory = True
