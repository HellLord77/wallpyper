from __future__ import annotations as _

from typing import Callable as _Callable

from .. import Dispatching as _Microsoft_UI_Dispatching
from .... import inspectable as _inspectable
from ....Windows import Foundation as _Windows_Foundation
from ....Windows.Foundation import Collections as _Windows_Foundation_Collections
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IAppWindow(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_struct.Microsoft.UI.WindowId]],  # value
                      _type.HRESULT]
    get_IsShownInSwitchers: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_IsShownInSwitchers: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    get_IsVisible: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_OwnerWindowId: _Callable[[_Pointer[_struct.Microsoft.UI.WindowId]],  # value
                                 _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Graphics.PointInt32]],  # value
                            _type.HRESULT]
    get_Presenter: _Callable[[_Pointer[IAppWindowPresenter]],  # value
                             _type.HRESULT]
    get_Size: _Callable[[_Pointer[_struct.Windows.Graphics.SizeInt32]],  # value
                        _type.HRESULT]
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Title: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_TitleBar: _Callable[[_Pointer[IAppWindowTitleBar]],  # value
                            _type.HRESULT]
    Destroy: _Callable[[],
                       _type.HRESULT]
    Hide: _Callable[[],
                    _type.HRESULT]
    Move: _Callable[[_struct.Windows.Graphics.PointInt32],  # position
                    _type.HRESULT]
    MoveAndResize: _Callable[[_struct.Windows.Graphics.RectInt32],  # rect
                             _type.HRESULT]
    MoveAndResizeRelativeToDisplayArea: _Callable[[_struct.Windows.Graphics.RectInt32,  # rect
                                                   IDisplayArea],  # displayarea
                                                  _type.HRESULT]
    Resize: _Callable[[_struct.Windows.Graphics.SizeInt32],  # size
                      _type.HRESULT]
    SetIcon: _Callable[[_type.HSTRING],  # iconPath
                       _type.HRESULT]
    SetIconWithIconId: _Callable[[_struct.Microsoft.UI.IconId],  # iconId
                                 _type.HRESULT]
    SetPresenter: _Callable[[IAppWindowPresenter],  # appWindowPresenter
                            _type.HRESULT]
    SetPresenterByKind: _Callable[[_enum.Microsoft.UI.Windowing.AppWindowPresenterKind],  # appWindowPresenterKind
                                  _type.HRESULT]
    Show: _Callable[[],
                    _type.HRESULT]
    ShowWithActivation: _Callable[[_type.boolean],  # activateWindow
                                  _type.HRESULT]
    add_Changed: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppWindow, IAppWindowChangedEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Changed: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_Closing: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppWindow, IAppWindowClosingEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Closing: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_Destroying: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppWindow, _inspectable.IInspectable],  # handler
                               _Pointer[_struct.EventRegistrationToken]],  # token
                              _type.HRESULT]
    remove_Destroying: _Callable[[_struct.EventRegistrationToken],  # token
                                 _type.HRESULT]


class IAppWindow2(_inspectable.IInspectable):
    get_ClientSize: _Callable[[_Pointer[_struct.Windows.Graphics.SizeInt32]],  # value
                              _type.HRESULT]
    MoveInZOrderAtBottom: _Callable[[],
                                    _type.HRESULT]
    MoveInZOrderAtTop: _Callable[[],
                                 _type.HRESULT]
    MoveInZOrderBelow: _Callable[[_struct.Microsoft.UI.WindowId],  # windowId
                                 _type.HRESULT]
    ResizeClient: _Callable[[_struct.Windows.Graphics.SizeInt32],  # size
                            _type.HRESULT]
    ShowOnceWithRequestedStartupState: _Callable[[],
                                                 _type.HRESULT]


class IAppWindow3(_inspectable.IInspectable):
    AssociateWithDispatcherQueue: _Callable[[_Microsoft_UI_Dispatching.IDispatcherQueue],  # dispatcherQueue
                                            _type.HRESULT]
    get_DispatcherQueue: _Callable[[_Pointer[_Microsoft_UI_Dispatching.IDispatcherQueue]],  # value
                                   _type.HRESULT]


class IAppWindowChangedEventArgs(_inspectable.IInspectable):
    get_DidPositionChange: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    get_DidPresenterChange: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    get_DidSizeChange: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_DidVisibilityChange: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]


class IAppWindowChangedEventArgs2(_inspectable.IInspectable):
    get_DidZOrderChange: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_IsZOrderAtBottom: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_IsZOrderAtTop: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_ZOrderBelowWindowId: _Callable[[_Pointer[_struct.Microsoft.UI.WindowId]],  # value
                                       _type.HRESULT]


class IAppWindowClosingEventArgs(_inspectable.IInspectable):
    get_Cancel: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_Cancel: _Callable[[_type.boolean],  # value
                          _type.HRESULT]


class IAppWindowPresenter(_inspectable.IInspectable):
    get_Kind: _Callable[[_Pointer[_enum.Microsoft.UI.Windowing.AppWindowPresenterKind]],  # value
                        _type.HRESULT]


class IAppWindowPresenterFactory(_inspectable.IInspectable):
    pass


class IAppWindowStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Pointer[IAppWindow]],  # result
                      _type.HRESULT]
    CreateWithPresenter: _Callable[[IAppWindowPresenter,  # appWindowPresenter
                                    _Pointer[IAppWindow]],  # result
                                   _type.HRESULT]
    CreateWithPresenterAndOwner: _Callable[[IAppWindowPresenter,  # appWindowPresenter
                                            _struct.Microsoft.UI.WindowId,  # ownerWindowId
                                            _Pointer[IAppWindow]],  # result
                                           _type.HRESULT]
    GetFromWindowId: _Callable[[_struct.Microsoft.UI.WindowId,  # windowId
                                _Pointer[IAppWindow]],  # result
                               _type.HRESULT]


class IAppWindowStatics2(_inspectable.IInspectable, factory=True):
    CreateWithDispatcherQueue: _Callable[[IAppWindowPresenter,  # appWindowPresenter
                                          _struct.Microsoft.UI.WindowId,  # ownerWindowId
                                          _Microsoft_UI_Dispatching.IDispatcherQueue,  # DispatcherQueue
                                          _Pointer[IAppWindow]],  # result
                                         _type.HRESULT]


class IAppWindowTitleBar(_inspectable.IInspectable):
    get_BackgroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                   _type.HRESULT]
    put_BackgroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                   _type.HRESULT]
    get_ButtonBackgroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                         _type.HRESULT]
    put_ButtonBackgroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                         _type.HRESULT]
    get_ButtonForegroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                         _type.HRESULT]
    put_ButtonForegroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                         _type.HRESULT]
    get_ButtonHoverBackgroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                              _type.HRESULT]
    put_ButtonHoverBackgroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                              _type.HRESULT]
    get_ButtonHoverForegroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                              _type.HRESULT]
    put_ButtonHoverForegroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                              _type.HRESULT]
    get_ButtonInactiveBackgroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                                 _type.HRESULT]
    put_ButtonInactiveBackgroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                                 _type.HRESULT]
    get_ButtonInactiveForegroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                                 _type.HRESULT]
    put_ButtonInactiveForegroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                                 _type.HRESULT]
    get_ButtonPressedBackgroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                                _type.HRESULT]
    put_ButtonPressedBackgroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                                _type.HRESULT]
    get_ButtonPressedForegroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                                _type.HRESULT]
    put_ButtonPressedForegroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                                _type.HRESULT]
    get_ExtendsContentIntoTitleBar: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]
    put_ExtendsContentIntoTitleBar: _Callable[[_type.boolean],  # value
                                              _type.HRESULT]
    get_ForegroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                   _type.HRESULT]
    put_ForegroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                   _type.HRESULT]
    get_Height: _Callable[[_Pointer[_type.INT32]],  # value
                          _type.HRESULT]
    get_IconShowOptions: _Callable[[_Pointer[_enum.Microsoft.UI.Windowing.IconShowOptions]],  # value
                                   _type.HRESULT]
    put_IconShowOptions: _Callable[[_enum.Microsoft.UI.Windowing.IconShowOptions],  # value
                                   _type.HRESULT]
    get_InactiveBackgroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                           _type.HRESULT]
    put_InactiveBackgroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                           _type.HRESULT]
    get_InactiveForegroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                           _type.HRESULT]
    put_InactiveForegroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                           _type.HRESULT]
    get_LeftInset: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]
    get_RightInset: _Callable[[_Pointer[_type.INT32]],  # value
                              _type.HRESULT]
    ResetToDefault: _Callable[[],
                              _type.HRESULT]
    SetDragRectangles: _Callable[[_type.UINT32,  # __valueSize
                                  _Pointer[_struct.Windows.Graphics.RectInt32]],  # value
                                 _type.HRESULT]


class IAppWindowTitleBar2(_inspectable.IInspectable):
    get_PreferredHeightOption: _Callable[[_Pointer[_enum.Microsoft.UI.Windowing.TitleBarHeightOption]],  # value
                                         _type.HRESULT]
    put_PreferredHeightOption: _Callable[[_enum.Microsoft.UI.Windowing.TitleBarHeightOption],  # value
                                         _type.HRESULT]


class IAppWindowTitleBarStatics(_inspectable.IInspectable, factory=True):
    IsCustomizationSupported: _Callable[[_Pointer[_type.boolean]],  # result
                                        _type.HRESULT]


class ICompactOverlayPresenter(_inspectable.IInspectable):
    get_InitialSize: _Callable[[_Pointer[_enum.Microsoft.UI.Windowing.CompactOverlaySize]],  # value
                               _type.HRESULT]
    put_InitialSize: _Callable[[_enum.Microsoft.UI.Windowing.CompactOverlaySize],  # value
                               _type.HRESULT]


class ICompactOverlayPresenterStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Pointer[ICompactOverlayPresenter]],  # result
                      _type.HRESULT]


class IDisplayArea(_inspectable.IInspectable):
    get_DisplayId: _Callable[[_Pointer[_struct.Microsoft.UI.DisplayId]],  # value
                             _type.HRESULT]
    get_IsPrimary: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_OuterBounds: _Callable[[_Pointer[_struct.Windows.Graphics.RectInt32]],  # value
                               _type.HRESULT]
    get_WorkArea: _Callable[[_Pointer[_struct.Windows.Graphics.RectInt32]],  # value
                            _type.HRESULT]


class IDisplayAreaStatics(_inspectable.IInspectable, factory=True):
    get_Primary: _Callable[[_Pointer[IDisplayArea]],  # value
                           _type.HRESULT]
    CreateWatcher: _Callable[[_Pointer[IDisplayAreaWatcher]],  # result
                             _type.HRESULT]
    FindAll: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IDisplayArea]]],  # result
                       _type.HRESULT]
    GetFromWindowId: _Callable[[_struct.Microsoft.UI.WindowId,  # windowId
                                _enum.Microsoft.UI.Windowing.DisplayAreaFallback,  # displayAreaFallback
                                _Pointer[IDisplayArea]],  # result
                               _type.HRESULT]
    GetFromPoint: _Callable[[_struct.Windows.Graphics.PointInt32,  # point
                             _enum.Microsoft.UI.Windowing.DisplayAreaFallback,  # displayAreaFallback
                             _Pointer[IDisplayArea]],  # result
                            _type.HRESULT]
    GetFromRect: _Callable[[_struct.Windows.Graphics.RectInt32,  # rect
                            _enum.Microsoft.UI.Windowing.DisplayAreaFallback,  # displayAreaFallback
                            _Pointer[IDisplayArea]],  # result
                           _type.HRESULT]


class IDisplayAreaStatics2(_inspectable.IInspectable, factory=True):
    GetFromDisplayId: _Callable[[_struct.Microsoft.UI.DisplayId,  # displayId
                                 _Pointer[IDisplayArea]],  # result
                                _type.HRESULT]


class IDisplayAreaWatcher(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Microsoft.UI.Windowing.DisplayAreaWatcherStatus]],  # value
                          _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    add_Added: _Callable[[_Windows_Foundation.ITypedEventHandler[IDisplayAreaWatcher, IDisplayArea],  # handler
                          _Pointer[_struct.EventRegistrationToken]],  # token
                         _type.HRESULT]
    remove_Added: _Callable[[_struct.EventRegistrationToken],  # token
                            _type.HRESULT]
    add_EnumerationCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IDisplayAreaWatcher, _inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_EnumerationCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    add_Removed: _Callable[[_Windows_Foundation.ITypedEventHandler[IDisplayAreaWatcher, IDisplayArea],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Removed: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_Stopped: _Callable[[_Windows_Foundation.ITypedEventHandler[IDisplayAreaWatcher, _inspectable.IInspectable],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Stopped: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_Updated: _Callable[[_Windows_Foundation.ITypedEventHandler[IDisplayAreaWatcher, IDisplayArea],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Updated: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]


class IFullScreenPresenter(_inspectable.IInspectable):
    pass


class IFullScreenPresenterStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Pointer[IFullScreenPresenter]],  # result
                      _type.HRESULT]


class IOverlappedPresenter(_inspectable.IInspectable):
    get_HasBorder: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_HasTitleBar: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_IsAlwaysOnTop: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_IsAlwaysOnTop: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_IsMaximizable: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_IsMaximizable: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_IsMinimizable: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_IsMinimizable: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_IsModal: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_IsModal: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_IsResizable: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    put_IsResizable: _Callable[[_type.boolean],  # value
                               _type.HRESULT]
    get_State: _Callable[[_Pointer[_enum.Microsoft.UI.Windowing.OverlappedPresenterState]],  # value
                         _type.HRESULT]
    Maximize: _Callable[[],
                        _type.HRESULT]
    Minimize: _Callable[[],
                        _type.HRESULT]
    Restore: _Callable[[],
                       _type.HRESULT]
    SetBorderAndTitleBar: _Callable[[_type.boolean,  # hasBorder
                                     _type.boolean],  # hasTitleBar
                                    _type.HRESULT]


class IOverlappedPresenter2(_inspectable.IInspectable):
    MinimizeWithActivation: _Callable[[_type.boolean],  # activateWindow
                                      _type.HRESULT]
    RestoreWithActivation: _Callable[[_type.boolean],  # activateWindow
                                     _type.HRESULT]


class IOverlappedPresenterStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Pointer[IOverlappedPresenter]],  # result
                      _type.HRESULT]
    CreateForContextMenu: _Callable[[_Pointer[IOverlappedPresenter]],  # result
                                    _type.HRESULT]
    CreateForDialog: _Callable[[_Pointer[IOverlappedPresenter]],  # result
                               _type.HRESULT]
    CreateForToolWindow: _Callable[[_Pointer[IOverlappedPresenter]],  # result
                                   _type.HRESULT]


class IOverlappedPresenterStatics2(_inspectable.IInspectable, factory=True):
    get_RequestedStartupState: _Callable[[_Pointer[_enum.Microsoft.UI.Windowing.OverlappedPresenterState]],  # value
                                         _type.HRESULT]
