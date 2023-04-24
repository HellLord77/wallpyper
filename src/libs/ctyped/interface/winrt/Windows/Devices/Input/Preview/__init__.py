from __future__ import annotations

from typing import Callable as _Callable

from ... import HumanInterfaceDevice as _Windows_Devices_HumanInterfaceDevice
from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IGazeDevicePreview(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.UINT32]],  # value
                      _type.HRESULT]
    get_CanTrackEyes: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_CanTrackHead: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_ConfigurationState: _Callable[[_Pointer[_enum.Windows.Devices.Input.Preview.GazeDeviceConfigurationStatePreview]],  # value
                                      _type.HRESULT]
    RequestCalibrationAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                       _type.HRESULT]
    GetNumericControlDescriptions: _Callable[[_type.UINT16,  # usagePage
                                              _type.UINT16,  # usageId
                                              _Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Devices_HumanInterfaceDevice.IHidNumericControlDescription]]],  # result
                                             _type.HRESULT]
    GetBooleanControlDescriptions: _Callable[[_type.UINT16,  # usagePage
                                              _type.UINT16,  # usageId
                                              _Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Devices_HumanInterfaceDevice.IHidBooleanControlDescription]]],  # result
                                             _type.HRESULT]


class IGazeDeviceWatcherAddedPreviewEventArgs(_inspectable.IInspectable):
    get_Device: _Callable[[_Pointer[IGazeDevicePreview]],  # value
                          _type.HRESULT]


class IGazeDeviceWatcherPreview(_inspectable.IInspectable):
    add_Added: _Callable[[_Windows_Foundation.ITypedEventHandler[IGazeDeviceWatcherPreview, IGazeDeviceWatcherAddedPreviewEventArgs],  # handler
                          _Pointer[_struct.EventRegistrationToken]],  # token
                         _type.HRESULT]
    remove_Added: _Callable[[_struct.EventRegistrationToken],  # token
                            _type.HRESULT]
    add_Removed: _Callable[[_Windows_Foundation.ITypedEventHandler[IGazeDeviceWatcherPreview, IGazeDeviceWatcherRemovedPreviewEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Removed: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_Updated: _Callable[[_Windows_Foundation.ITypedEventHandler[IGazeDeviceWatcherPreview, IGazeDeviceWatcherUpdatedPreviewEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Updated: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_EnumerationCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IGazeDeviceWatcherPreview, _inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_EnumerationCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]


class IGazeDeviceWatcherRemovedPreviewEventArgs(_inspectable.IInspectable):
    get_Device: _Callable[[_Pointer[IGazeDevicePreview]],  # value
                          _type.HRESULT]


class IGazeDeviceWatcherUpdatedPreviewEventArgs(_inspectable.IInspectable):
    get_Device: _Callable[[_Pointer[IGazeDevicePreview]],  # value
                          _type.HRESULT]


class IGazeEnteredPreviewEventArgs(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_CurrentPoint: _Callable[[_Pointer[IGazePointPreview]],  # value
                                _type.HRESULT]


class IGazeExitedPreviewEventArgs(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_CurrentPoint: _Callable[[_Pointer[IGazePointPreview]],  # value
                                _type.HRESULT]


class IGazeInputSourcePreview(_inspectable.IInspectable):
    add_GazeMoved: _Callable[[_Windows_Foundation.ITypedEventHandler[IGazeInputSourcePreview, IGazeMovedPreviewEventArgs],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_GazeMoved: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    add_GazeEntered: _Callable[[_Windows_Foundation.ITypedEventHandler[IGazeInputSourcePreview, IGazeEnteredPreviewEventArgs],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_GazeEntered: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    add_GazeExited: _Callable[[_Windows_Foundation.ITypedEventHandler[IGazeInputSourcePreview, IGazeExitedPreviewEventArgs],  # handler
                               _Pointer[_struct.EventRegistrationToken]],  # token
                              _type.HRESULT]
    remove_GazeExited: _Callable[[_struct.EventRegistrationToken],  # token
                                 _type.HRESULT]


class IGazeInputSourcePreviewStatics(_inspectable.IInspectable):
    GetForCurrentView: _Callable[[_Pointer[IGazeInputSourcePreview]],  # result
                                 _type.HRESULT]
    CreateWatcher: _Callable[[_Pointer[IGazeDeviceWatcherPreview]],  # result
                             _type.HRESULT]

    _factory = True


class IGazeMovedPreviewEventArgs(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_CurrentPoint: _Callable[[_Pointer[IGazePointPreview]],  # value
                                _type.HRESULT]
    GetIntermediatePoints: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IGazePointPreview]]],  # result
                                     _type.HRESULT]


class IGazePointPreview(_inspectable.IInspectable):
    get_SourceDevice: _Callable[[_Pointer[IGazeDevicePreview]],  # value
                                _type.HRESULT]
    get_EyeGazePosition: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.Point]]],  # value
                                   _type.HRESULT]
    get_HeadGazePosition: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.Point]]],  # value
                                    _type.HRESULT]
    get_Timestamp: _Callable[[_Pointer[_type.UINT64]],  # value
                             _type.HRESULT]
    get_HidInputReport: _Callable[[_Pointer[_Windows_Devices_HumanInterfaceDevice.IHidInputReport]],  # value
                                  _type.HRESULT]
