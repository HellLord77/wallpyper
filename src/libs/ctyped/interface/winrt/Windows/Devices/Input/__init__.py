from __future__ import annotations

from typing import Callable as _Callable

from .. import Haptics as _Windows_Devices_Haptics
from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IKeyboardCapabilities(_inspectable.IInspectable):
    get_KeyboardPresent: _Callable[[_Pointer[_type.INT32]],  # value
                                   _type.HRESULT]


class IMouseCapabilities(_inspectable.IInspectable):
    get_MousePresent: _Callable[[_Pointer[_type.INT32]],  # value
                                _type.HRESULT]
    get_VerticalWheelPresent: _Callable[[_Pointer[_type.INT32]],  # value
                                        _type.HRESULT]
    get_HorizontalWheelPresent: _Callable[[_Pointer[_type.INT32]],  # value
                                          _type.HRESULT]
    get_SwapButtons: _Callable[[_Pointer[_type.INT32]],  # value
                               _type.HRESULT]
    get_NumberOfButtons: _Callable[[_Pointer[_type.UINT32]],  # value
                                   _type.HRESULT]


class IMouseDevice(_inspectable.IInspectable):
    add_MouseMoved: _Callable[[_Windows_Foundation.ITypedEventHandler[IMouseDevice, IMouseEventArgs],  # handler
                               _Pointer[_struct.EventRegistrationToken]],  # cookie
                              _type.HRESULT]
    remove_MouseMoved: _Callable[[_struct.EventRegistrationToken],  # cookie
                                 _type.HRESULT]


class IMouseDeviceStatics(_inspectable.IInspectable, factory=True):
    GetForCurrentView: _Callable[[_Pointer[IMouseDevice]],  # mouseDevice
                                 _type.HRESULT]


class IMouseEventArgs(_inspectable.IInspectable):
    get_MouseDelta: _Callable[[_Pointer[_struct.Windows.Devices.Input.MouseDelta]],  # value
                              _type.HRESULT]


class IPenButtonListener(_inspectable.IInspectable):
    IsSupported: _Callable[[_Pointer[_type.boolean]],  # result
                           _type.HRESULT]
    add_IsSupportedChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IPenButtonListener, _inspectable.IInspectable],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_IsSupportedChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_TailButtonClicked: _Callable[[_Windows_Foundation.ITypedEventHandler[IPenButtonListener, IPenTailButtonClickedEventArgs],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_TailButtonClicked: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    add_TailButtonDoubleClicked: _Callable[[_Windows_Foundation.ITypedEventHandler[IPenButtonListener, IPenTailButtonDoubleClickedEventArgs],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_TailButtonDoubleClicked: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]
    add_TailButtonLongPressed: _Callable[[_Windows_Foundation.ITypedEventHandler[IPenButtonListener, IPenTailButtonLongPressedEventArgs],  # handler
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_TailButtonLongPressed: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]


class IPenButtonListenerStatics(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[IPenButtonListener]],  # result
                          _type.HRESULT]


class IPenDevice(_inspectable.IInspectable):
    get_PenId: _Callable[[_Pointer[_struct.GUID]],  # value
                         _type.HRESULT]


class IPenDevice2(_inspectable.IInspectable):
    get_SimpleHapticsController: _Callable[[_Pointer[_Windows_Devices_Haptics.ISimpleHapticsController]],  # value
                                           _type.HRESULT]


class IPenDeviceStatics(_inspectable.IInspectable, factory=True):
    GetFromPointerId: _Callable[[_type.UINT32,  # pointerId
                                 _Pointer[IPenDevice]],  # result
                                _type.HRESULT]


class IPenDockListener(_inspectable.IInspectable):
    IsSupported: _Callable[[_Pointer[_type.boolean]],  # result
                           _type.HRESULT]
    add_IsSupportedChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IPenDockListener, _inspectable.IInspectable],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_IsSupportedChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_Docked: _Callable[[_Windows_Foundation.ITypedEventHandler[IPenDockListener, IPenDockedEventArgs],  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Docked: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    add_Undocked: _Callable[[_Windows_Foundation.ITypedEventHandler[IPenDockListener, IPenUndockedEventArgs],  # handler
                             _Pointer[_struct.EventRegistrationToken]],  # token
                            _type.HRESULT]
    remove_Undocked: _Callable[[_struct.EventRegistrationToken],  # token
                               _type.HRESULT]


class IPenDockListenerStatics(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[IPenDockListener]],  # result
                          _type.HRESULT]


class IPenDockedEventArgs(_inspectable.IInspectable):
    pass


class IPenTailButtonClickedEventArgs(_inspectable.IInspectable):
    pass


class IPenTailButtonDoubleClickedEventArgs(_inspectable.IInspectable):
    pass


class IPenTailButtonLongPressedEventArgs(_inspectable.IInspectable):
    pass


class IPenUndockedEventArgs(_inspectable.IInspectable):
    pass


class IPointerDevice(_inspectable.IInspectable):
    get_PointerDeviceType: _Callable[[_Pointer[_enum.Windows.Devices.Input.PointerDeviceType]],  # value
                                     _type.HRESULT]
    get_IsIntegrated: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_MaxContacts: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]
    get_PhysicalDeviceRect: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                                      _type.HRESULT]
    get_ScreenRect: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                              _type.HRESULT]
    get_SupportedUsages: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_struct.Windows.Devices.Input.PointerDeviceUsage]]],  # value
                                   _type.HRESULT]


class IPointerDevice2(_inspectable.IInspectable):
    get_MaxPointersWithZDistance: _Callable[[_Pointer[_type.UINT32]],  # value
                                            _type.HRESULT]


class IPointerDeviceStatics(_inspectable.IInspectable, factory=True):
    GetPointerDevice: _Callable[[_type.UINT32,  # pointerId
                                 _Pointer[IPointerDevice]],  # pointerDevice
                                _type.HRESULT]
    GetPointerDevices: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IPointerDevice]]],  # pointerDevices
                                 _type.HRESULT]


class ITouchCapabilities(_inspectable.IInspectable):
    get_TouchPresent: _Callable[[_Pointer[_type.INT32]],  # value
                                _type.HRESULT]
    get_Contacts: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
