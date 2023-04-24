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


class ICastingConnection(_inspectable.IInspectable):
    get_State: _Callable[[_Pointer[_enum.Windows.Media.Casting.CastingConnectionState]],  # value
                         _type.HRESULT]
    get_Device: _Callable[[_Pointer[ICastingDevice]],  # value
                          _type.HRESULT]
    get_Source: _Callable[[_Pointer[ICastingSource]],  # value
                          _type.HRESULT]
    put_Source: _Callable[[ICastingSource],  # value
                          _type.HRESULT]
    add_StateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ICastingConnection, _inspectable.IInspectable],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_StateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    add_ErrorOccurred: _Callable[[_Windows_Foundation.ITypedEventHandler[ICastingConnection, ICastingConnectionErrorOccurredEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_ErrorOccurred: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    RequestStartCastingAsync: _Callable[[ICastingSource,  # value
                                         _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Media.Casting.CastingConnectionErrorStatus]]],  # operation
                                        _type.HRESULT]
    DisconnectAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Media.Casting.CastingConnectionErrorStatus]]],  # operation
                               _type.HRESULT]


class ICastingConnectionErrorOccurredEventArgs(_inspectable.IInspectable):
    get_ErrorStatus: _Callable[[_Pointer[_enum.Windows.Media.Casting.CastingConnectionErrorStatus]],  # value
                               _type.HRESULT]
    get_Message: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]


class ICastingDevice(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_FriendlyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_Icon: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamWithContentType]],  # value
                        _type.HRESULT]
    GetSupportedCastingPlaybackTypesAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Media.Casting.CastingPlaybackTypes]]],  # operation
                                                     _type.HRESULT]
    CreateCastingConnection: _Callable[[_Pointer[ICastingConnection]],  # value
                                       _type.HRESULT]


class ICastingDevicePicker(_inspectable.IInspectable):
    get_Filter: _Callable[[_Pointer[ICastingDevicePickerFilter]],  # value
                          _type.HRESULT]
    get_Appearance: _Callable[[_Pointer[_Windows_Devices_Enumeration.IDevicePickerAppearance]],  # value
                              _type.HRESULT]
    add_CastingDeviceSelected: _Callable[[_Windows_Foundation.ITypedEventHandler[ICastingDevicePicker, ICastingDeviceSelectedEventArgs],  # handler
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_CastingDeviceSelected: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]
    add_CastingDevicePickerDismissed: _Callable[[_Windows_Foundation.ITypedEventHandler[ICastingDevicePicker, _inspectable.IInspectable],  # handler
                                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                                _type.HRESULT]
    remove_CastingDevicePickerDismissed: _Callable[[_struct.EventRegistrationToken],  # token
                                                   _type.HRESULT]
    Show: _Callable[[_struct.Windows.Foundation.Rect],  # selection
                    _type.HRESULT]
    ShowWithPlacement: _Callable[[_struct.Windows.Foundation.Rect,  # selection
                                  _enum.Windows.UI.Popups.Placement],  # preferredPlacement
                                 _type.HRESULT]
    Hide: _Callable[[],
                    _type.HRESULT]


class ICastingDevicePickerFilter(_inspectable.IInspectable):
    get_SupportsAudio: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_SupportsAudio: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_SupportsVideo: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_SupportsVideo: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_SupportsPictures: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_SupportsPictures: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_SupportedCastingSources: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ICastingSource]]],  # value
                                           _type.HRESULT]


class ICastingDeviceSelectedEventArgs(_inspectable.IInspectable):
    get_SelectedCastingDevice: _Callable[[_Pointer[ICastingDevice]],  # value
                                         _type.HRESULT]


class ICastingDeviceStatics(_inspectable.IInspectable):
    GetDeviceSelector: _Callable[[_enum.Windows.Media.Casting.CastingPlaybackTypes,  # type
                                  _Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    GetDeviceSelectorFromCastingSourceAsync: _Callable[[ICastingSource,  # castingSource
                                                        _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                                       _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # value
                            _Pointer[_Windows_Foundation.IAsyncOperation[ICastingDevice]]],  # operation
                           _type.HRESULT]
    DeviceInfoSupportsCastingAsync: _Callable[[_Windows_Devices_Enumeration.IDeviceInformation,  # device
                                               _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                              _type.HRESULT]

    _factory = True


class ICastingSource(_inspectable.IInspectable):
    get_PreferredSourceUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                      _type.HRESULT]
    put_PreferredSourceUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                                      _type.HRESULT]
