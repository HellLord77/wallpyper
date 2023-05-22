from __future__ import annotations

from typing import Callable as _Callable

from ... import UI as _Windows_Web_UI
from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IWebViewControlAcceleratorKeyPressedEventArgs(_inspectable.IInspectable):
    get_EventType: _Callable[[_Pointer[_enum.Windows.UI.Core.CoreAcceleratorKeyEventType]],  # value
                             _type.HRESULT]
    get_VirtualKey: _Callable[[_Pointer[_enum.Windows.System.VirtualKey]],  # value
                              _type.HRESULT]
    get_KeyStatus: _Callable[[_Pointer[_struct.Windows.UI.Core.CorePhysicalKeyStatus]],  # value
                             _type.HRESULT]
    get_RoutingStage: _Callable[[_Pointer[_enum.Windows.Web.UI.Interop.WebViewControlAcceleratorKeyRoutingStage]],  # value
                                _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class IWebViewControlMoveFocusRequestedEventArgs(_inspectable.IInspectable):
    get_Reason: _Callable[[_Pointer[_enum.Windows.Web.UI.Interop.WebViewControlMoveFocusReason]],  # value
                          _type.HRESULT]


class IWebViewControlProcess(_inspectable.IInspectable):
    get_ProcessId: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    get_EnterpriseId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_IsPrivateNetworkClientServerCapabilityEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                                 _type.HRESULT]
    CreateWebViewControlAsync: _Callable[[_type.INT64,  # hostWindowHandle
                                          _struct.Windows.Foundation.Rect,  # bounds
                                          _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Web_UI.IWebViewControl]]],  # operation
                                         _type.HRESULT]
    GetWebViewControls: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Web_UI.IWebViewControl]]],  # result
                                  _type.HRESULT]
    Terminate: _Callable[[],
                         _type.HRESULT]
    add_ProcessExited: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebViewControlProcess, _inspectable.IInspectable],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_ProcessExited: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]


class IWebViewControlProcessFactory(_inspectable.IInspectable, factory=True):
    CreateWithOptions: _Callable[[IWebViewControlProcessOptions,  # processOptions
                                  _Pointer[IWebViewControlProcess]],  # result
                                 _type.HRESULT]


class IWebViewControlProcessOptions(_inspectable.IInspectable):
    put_EnterpriseId: _Callable[[_type.HSTRING],  # value
                                _type.HRESULT]
    get_EnterpriseId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    put_PrivateNetworkClientServerCapability: _Callable[[_enum.Windows.Web.UI.Interop.WebViewControlProcessCapabilityState],  # value
                                                        _type.HRESULT]
    get_PrivateNetworkClientServerCapability: _Callable[[_Pointer[_enum.Windows.Web.UI.Interop.WebViewControlProcessCapabilityState]],  # value
                                                        _type.HRESULT]


class IWebViewControlSite(_inspectable.IInspectable):
    get_Process: _Callable[[_Pointer[IWebViewControlProcess]],  # value
                           _type.HRESULT]
    put_Scale: _Callable[[_type.DOUBLE],  # value
                         _type.HRESULT]
    get_Scale: _Callable[[_Pointer[_type.DOUBLE]],  # value
                         _type.HRESULT]
    put_Bounds: _Callable[[_struct.Windows.Foundation.Rect],  # value
                          _type.HRESULT]
    get_Bounds: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                          _type.HRESULT]
    put_IsVisible: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    get_IsVisible: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    Close: _Callable[[],
                     _type.HRESULT]
    MoveFocus: _Callable[[_enum.Windows.Web.UI.Interop.WebViewControlMoveFocusReason],  # reason
                         _type.HRESULT]
    add_MoveFocusRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[_Windows_Web_UI.IWebViewControl, IWebViewControlMoveFocusRequestedEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_MoveFocusRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_AcceleratorKeyPressed: _Callable[[_Windows_Foundation.ITypedEventHandler[_Windows_Web_UI.IWebViewControl, IWebViewControlAcceleratorKeyPressedEventArgs],  # handler
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_AcceleratorKeyPressed: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]


class IWebViewControlSite2(_inspectable.IInspectable):
    add_GotFocus: _Callable[[_Windows_Foundation.ITypedEventHandler[_Windows_Web_UI.IWebViewControl, _inspectable.IInspectable],  # handler
                             _Pointer[_struct.EventRegistrationToken]],  # token
                            _type.HRESULT]
    remove_GotFocus: _Callable[[_struct.EventRegistrationToken],  # token
                               _type.HRESULT]
    add_LostFocus: _Callable[[_Windows_Foundation.ITypedEventHandler[_Windows_Web_UI.IWebViewControl, _inspectable.IInspectable],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_LostFocus: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
