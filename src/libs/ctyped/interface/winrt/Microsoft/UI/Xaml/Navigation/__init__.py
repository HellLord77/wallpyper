from __future__ import annotations as _

from typing import Callable as _Callable

from ..Media import Animation as _Microsoft_UI_Xaml_Media_Animation
from ... import Xaml as _Microsoft_UI_Xaml
from ..... import inspectable as _inspectable
from .....Windows import Foundation as _Windows_Foundation
from ......um import Unknwnbase as _Unknwnbase
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class _INavigatedEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       INavigationEventArgs],  # e
                      _type.HRESULT]


class INavigatedEventHandler(_INavigatedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class INavigatedEventHandler_impl(_INavigatedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _INavigatingCancelEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       INavigatingCancelEventArgs],  # e
                      _type.HRESULT]


class INavigatingCancelEventHandler(_INavigatingCancelEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class INavigatingCancelEventHandler_impl(_INavigatingCancelEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _INavigationFailedEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       INavigationFailedEventArgs],  # e
                      _type.HRESULT]


class INavigationFailedEventHandler(_INavigationFailedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class INavigationFailedEventHandler_impl(_INavigationFailedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _INavigationStoppedEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       INavigationEventArgs],  # e
                      _type.HRESULT]


class INavigationStoppedEventHandler(_INavigationStoppedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class INavigationStoppedEventHandler_impl(_INavigationStoppedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class IFrameNavigationOptions(_inspectable.IInspectable):
    get_IsNavigationStackEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_IsNavigationStackEnabled: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]
    get_TransitionInfoOverride: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media_Animation.INavigationTransitionInfo]],  # value
                                          _type.HRESULT]
    put_TransitionInfoOverride: _Callable[[_Microsoft_UI_Xaml_Media_Animation.INavigationTransitionInfo],  # value
                                          _type.HRESULT]


class IFrameNavigationOptionsFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IFrameNavigationOptions]],  # value
                              _type.HRESULT]


class INavigatingCancelEventArgs(_inspectable.IInspectable):
    get_Cancel: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_Cancel: _Callable[[_type.boolean],  # value
                          _type.HRESULT]
    get_NavigationMode: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Navigation.NavigationMode]],  # value
                                  _type.HRESULT]
    get_SourcePageType: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Interop.TypeName]],  # value
                                  _type.HRESULT]
    get_Parameter: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                             _type.HRESULT]
    get_NavigationTransitionInfo: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media_Animation.INavigationTransitionInfo]],  # value
                                            _type.HRESULT]


class INavigationEventArgs(_inspectable.IInspectable):
    get_Content: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                           _type.HRESULT]
    get_Parameter: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                             _type.HRESULT]
    get_NavigationTransitionInfo: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media_Animation.INavigationTransitionInfo]],  # value
                                            _type.HRESULT]
    get_SourcePageType: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Interop.TypeName]],  # value
                                  _type.HRESULT]
    get_NavigationMode: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Navigation.NavigationMode]],  # value
                                  _type.HRESULT]
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]
    put_Uri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                       _type.HRESULT]


class INavigationFailedEventArgs(_inspectable.IInspectable):
    get_Exception: _Callable[[_Pointer[_type.HRESULT]],  # value
                             _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_SourcePageType: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Interop.TypeName]],  # value
                                  _type.HRESULT]


class IPageStackEntry(_inspectable.IInspectable):
    get_SourcePageType: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Interop.TypeName]],  # value
                                  _type.HRESULT]
    get_Parameter: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                             _type.HRESULT]
    get_NavigationTransitionInfo: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media_Animation.INavigationTransitionInfo]],  # value
                                            _type.HRESULT]


class IPageStackEntryFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[_struct.Windows.UI.Xaml.Interop.TypeName,  # sourcePageType
                               _inspectable.IInspectable,  # parameter
                               _Microsoft_UI_Xaml_Media_Animation.INavigationTransitionInfo,  # navigationTransitionInfo
                               _Pointer[IPageStackEntry]],  # value
                              _type.HRESULT]


class IPageStackEntryStatics(_inspectable.IInspectable, factory=True):
    get_SourcePageTypeProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
