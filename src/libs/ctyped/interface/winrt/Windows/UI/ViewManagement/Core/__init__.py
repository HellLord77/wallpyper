from __future__ import annotations

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from .... import UI as _Windows_UI
from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class ICoreFrameworkInputView(_inspectable.IInspectable):
    add_PrimaryViewAnimationStarting: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreFrameworkInputView, ICoreFrameworkInputViewAnimationStartingEventArgs],  # handler
                                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                                _type.HRESULT]
    remove_PrimaryViewAnimationStarting: _Callable[[_struct.EventRegistrationToken],  # token
                                                   _type.HRESULT]
    add_OcclusionsChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreFrameworkInputView, ICoreFrameworkInputViewOcclusionsChangedEventArgs],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_OcclusionsChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]


class ICoreFrameworkInputViewAnimationStartingEventArgs(_inspectable.IInspectable):
    get_Occlusions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[ICoreInputViewOcclusion]]],  # value
                              _type.HRESULT]
    get_FrameworkAnimationRecommended: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]
    get_AnimationDuration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                     _type.HRESULT]


class ICoreFrameworkInputViewOcclusionsChangedEventArgs(_inspectable.IInspectable):
    get_Occlusions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[ICoreInputViewOcclusion]]],  # value
                              _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]


class ICoreFrameworkInputViewStatics(_inspectable.IInspectable, factory=True):
    GetForUIContext: _Callable[[_Windows_UI.IUIContext,  # context
                                _Pointer[ICoreFrameworkInputView]],  # result
                               _type.HRESULT]
    GetForCurrentView: _Callable[[_Pointer[ICoreFrameworkInputView]],  # result
                                 _type.HRESULT]


class ICoreInputView(_inspectable.IInspectable):
    add_OcclusionsChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreInputView, ICoreInputViewOcclusionsChangedEventArgs],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_OcclusionsChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    GetCoreInputViewOcclusions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[ICoreInputViewOcclusion]]],  # result
                                          _type.HRESULT]
    TryShowPrimaryView: _Callable[[_Pointer[_type.boolean]],  # result
                                  _type.HRESULT]
    TryHidePrimaryView: _Callable[[_Pointer[_type.boolean]],  # result
                                  _type.HRESULT]


class ICoreInputView2(_inspectable.IInspectable):
    add_XYFocusTransferringFromPrimaryView: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreInputView, ICoreInputViewTransferringXYFocusEventArgs],  # handler
                                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                                      _type.HRESULT]
    remove_XYFocusTransferringFromPrimaryView: _Callable[[_struct.EventRegistrationToken],  # token
                                                         _type.HRESULT]
    add_XYFocusTransferredToPrimaryView: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreInputView, _inspectable.IInspectable],  # handler
                                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                                   _type.HRESULT]
    remove_XYFocusTransferredToPrimaryView: _Callable[[_struct.EventRegistrationToken],  # token
                                                      _type.HRESULT]
    TryTransferXYFocusToPrimaryView: _Callable[[_struct.Windows.Foundation.Rect,  # origin
                                                _enum.Windows.UI.ViewManagement.Core.CoreInputViewXYFocusTransferDirection,  # direction
                                                _Pointer[_type.boolean]],  # result
                                               _type.HRESULT]


class ICoreInputView3(_inspectable.IInspectable):
    TryShow: _Callable[[_Pointer[_type.boolean]],  # result
                       _type.HRESULT]
    TryShowWithKind: _Callable[[_enum.Windows.UI.ViewManagement.Core.CoreInputViewKind,  # type
                                _Pointer[_type.boolean]],  # result
                               _type.HRESULT]
    TryHide: _Callable[[_Pointer[_type.boolean]],  # result
                       _type.HRESULT]


class ICoreInputView4(_inspectable.IInspectable):
    add_PrimaryViewShowing: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreInputView, ICoreInputViewShowingEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_PrimaryViewShowing: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_PrimaryViewHiding: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreInputView, ICoreInputViewHidingEventArgs],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_PrimaryViewHiding: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]


class ICoreInputView5(_inspectable.IInspectable):
    IsKindSupported: _Callable[[_enum.Windows.UI.ViewManagement.Core.CoreInputViewKind,  # type
                                _Pointer[_type.boolean]],  # result
                               _type.HRESULT]
    add_SupportedKindsChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreInputView, _inspectable.IInspectable],  # handler
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_SupportedKindsChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]
    add_PrimaryViewAnimationStarting: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreInputView, ICoreInputViewAnimationStartingEventArgs],  # handler
                                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                                _type.HRESULT]
    remove_PrimaryViewAnimationStarting: _Callable[[_struct.EventRegistrationToken],  # token
                                                   _type.HRESULT]


class ICoreInputViewAnimationStartingEventArgs(_inspectable.IInspectable):
    get_Occlusions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[ICoreInputViewOcclusion]]],  # value
                              _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_AnimationDuration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                     _type.HRESULT]


class ICoreInputViewHidingEventArgs(_inspectable.IInspectable):
    TryCancel: _Callable[[_Pointer[_type.boolean]],  # result
                         _type.HRESULT]


class ICoreInputViewOcclusion(_inspectable.IInspectable):
    get_OccludingRect: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                                 _type.HRESULT]
    get_OcclusionKind: _Callable[[_Pointer[_enum.Windows.UI.ViewManagement.Core.CoreInputViewOcclusionKind]],  # value
                                 _type.HRESULT]


class ICoreInputViewOcclusionsChangedEventArgs(_inspectable.IInspectable):
    get_Occlusions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[ICoreInputViewOcclusion]]],  # value
                              _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class ICoreInputViewShowingEventArgs(_inspectable.IInspectable):
    TryCancel: _Callable[[_Pointer[_type.boolean]],  # result
                         _type.HRESULT]


class ICoreInputViewStatics(_inspectable.IInspectable, factory=True):
    GetForCurrentView: _Callable[[_Pointer[ICoreInputView]],  # result
                                 _type.HRESULT]


class ICoreInputViewStatics2(_inspectable.IInspectable, factory=True):
    GetForUIContext: _Callable[[_Windows_UI.IUIContext,  # context
                                _Pointer[ICoreInputView]],  # result
                               _type.HRESULT]


class ICoreInputViewTransferringXYFocusEventArgs(_inspectable.IInspectable):
    get_Origin: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                          _type.HRESULT]
    get_Direction: _Callable[[_Pointer[_enum.Windows.UI.ViewManagement.Core.CoreInputViewXYFocusTransferDirection]],  # value
                             _type.HRESULT]
    put_TransferHandled: _Callable[[_type.boolean],  # value
                                   _type.HRESULT]
    get_TransferHandled: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    put_KeepPrimaryViewVisible: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    get_KeepPrimaryViewVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]


class IUISettingsController(_inspectable.IInspectable):
    SetAdvancedEffectsEnabled: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]
    SetAnimationsEnabled: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    SetAutoHideScrollBars: _Callable[[_type.boolean],  # value
                                     _type.HRESULT]
    SetMessageDuration: _Callable[[_type.UINT32],  # value
                                  _type.HRESULT]
    SetTextScaleFactor: _Callable[[_type.DOUBLE],  # value
                                  _type.HRESULT]


class IUISettingsControllerStatics(_inspectable.IInspectable, factory=True):
    RequestDefaultAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IUISettingsController]]],  # operation
                                   _type.HRESULT]
