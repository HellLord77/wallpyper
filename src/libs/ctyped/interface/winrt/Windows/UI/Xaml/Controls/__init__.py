from __future__ import annotations as _

from typing import Callable as _Callable

from . import Primitives as _Windows_UI_Xaml_Controls_Primitives
from .. import Data as _Windows_UI_Xaml_Data
from .. import Documents as _Windows_UI_Xaml_Documents
from .. import Input as _Windows_UI_Xaml_Input
from .. import Media as _Windows_UI_Xaml_Media
from .. import Navigation as _Windows_UI_Xaml_Navigation
from ..Media import Animation as _Windows_UI_Xaml_Media_Animation
from ... import Composition as _Windows_UI_Composition
from ... import Core as _Windows_UI_Core
from ... import Text as _Windows_UI_Text
from ... import Xaml as _Windows_UI_Xaml
from ...Input import Inking as _Windows_UI_Input_Inking
from .... import Foundation as _Windows_Foundation
from .... import Web as _Windows_Web
from ....ApplicationModel import Contacts as _Windows_ApplicationModel_Contacts
from ....ApplicationModel import DataTransfer as _Windows_ApplicationModel_DataTransfer
from ....ApplicationModel import Search as _Windows_ApplicationModel_Search
from ....Foundation import Collections as _Windows_Foundation_Collections
from ....Media import Capture as _Windows_Media_Capture
from ....Media import Casting as _Windows_Media_Casting
from ....Media import Core as _Windows_Media_Core
from ....Media import PlayTo as _Windows_Media_PlayTo
from ....Media import Playback as _Windows_Media_Playback
from ....Media import Protection as _Windows_Media_Protection
from ....Storage import Streams as _Windows_Storage_Streams
from ....Web import Http as _Windows_Web_Http
from ..... import inspectable as _inspectable
from ......um import Unknwnbase as _Unknwnbase
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class _IBackClickEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       IBackClickEventArgs],  # e
                      _type.HRESULT]


class IBackClickEventHandler(_IBackClickEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IBackClickEventHandler_impl(_IBackClickEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ICalendarViewDayItemChangingEventHandler:
    Invoke: _Callable[[ICalendarView,  # sender
                       ICalendarViewDayItemChangingEventArgs],  # e
                      _type.HRESULT]


class ICalendarViewDayItemChangingEventHandler(_ICalendarViewDayItemChangingEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICalendarViewDayItemChangingEventHandler_impl(_ICalendarViewDayItemChangingEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ICleanUpVirtualizedItemEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       ICleanUpVirtualizedItemEventArgs],  # e
                      _type.HRESULT]


class ICleanUpVirtualizedItemEventHandler(_ICleanUpVirtualizedItemEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICleanUpVirtualizedItemEventHandler_impl(_ICleanUpVirtualizedItemEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IContextMenuOpeningEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       IContextMenuEventArgs],  # e
                      _type.HRESULT]


class IContextMenuOpeningEventHandler(_IContextMenuOpeningEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IContextMenuOpeningEventHandler_impl(_IContextMenuOpeningEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IDragItemsStartingEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       IDragItemsStartingEventArgs],  # e
                      _type.HRESULT]


class IDragItemsStartingEventHandler(_IDragItemsStartingEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IDragItemsStartingEventHandler_impl(_IDragItemsStartingEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IHubSectionHeaderClickEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       IHubSectionHeaderClickEventArgs],  # e
                      _type.HRESULT]


class IHubSectionHeaderClickEventHandler(_IHubSectionHeaderClickEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IHubSectionHeaderClickEventHandler_impl(_IHubSectionHeaderClickEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IItemClickEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       IItemClickEventArgs],  # e
                      _type.HRESULT]


class IItemClickEventHandler(_IItemClickEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IItemClickEventHandler_impl(_IItemClickEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IListViewItemToKeyHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # item
                       _Pointer[_type.HSTRING]],  # result
                      _type.HRESULT]


class IListViewItemToKeyHandler(_IListViewItemToKeyHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IListViewItemToKeyHandler_impl(_IListViewItemToKeyHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IListViewKeyToItemHandler:
    Invoke: _Callable[[_type.HSTRING,  # key
                       _Pointer[_Windows_Foundation.IAsyncOperation[_inspectable.IInspectable]]],  # operation
                      _type.HRESULT]


class IListViewKeyToItemHandler(_IListViewKeyToItemHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IListViewKeyToItemHandler_impl(_IListViewKeyToItemHandler, _Unknwnbase.IUnknown_impl):
    pass


class _INotifyEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       INotifyEventArgs],  # e
                      _type.HRESULT]


class INotifyEventHandler(_INotifyEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class INotifyEventHandler_impl(_INotifyEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ISectionsInViewChangedEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       ISectionsInViewChangedEventArgs],  # e
                      _type.HRESULT]


class ISectionsInViewChangedEventHandler(_ISectionsInViewChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ISectionsInViewChangedEventHandler_impl(_ISectionsInViewChangedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ISelectionChangedEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       ISelectionChangedEventArgs],  # e
                      _type.HRESULT]


class ISelectionChangedEventHandler(_ISelectionChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ISelectionChangedEventHandler_impl(_ISelectionChangedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ISemanticZoomViewChangedEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       ISemanticZoomViewChangedEventArgs],  # e
                      _type.HRESULT]


class ISemanticZoomViewChangedEventHandler(_ISemanticZoomViewChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ISemanticZoomViewChangedEventHandler_impl(_ISemanticZoomViewChangedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ITextChangedEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       ITextChangedEventArgs],  # e
                      _type.HRESULT]


class ITextChangedEventHandler(_ITextChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ITextChangedEventHandler_impl(_ITextChangedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ITextControlPasteEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       ITextControlPasteEventArgs],  # e
                      _type.HRESULT]


class ITextControlPasteEventHandler(_ITextControlPasteEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ITextControlPasteEventHandler_impl(_ITextControlPasteEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IWebViewNavigationFailedEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       IWebViewNavigationFailedEventArgs],  # e
                      _type.HRESULT]


class IWebViewNavigationFailedEventHandler(_IWebViewNavigationFailedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IWebViewNavigationFailedEventHandler_impl(_IWebViewNavigationFailedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class IAnchorRequestedEventArgs(_inspectable.IInspectable):
    get_Anchor: _Callable[[_Pointer[_Windows_UI_Xaml.IUIElement]],  # value
                          _type.HRESULT]
    put_Anchor: _Callable[[_Windows_UI_Xaml.IUIElement],  # value
                          _type.HRESULT]
    get_AnchorCandidates: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml.IUIElement]]],  # value
                                    _type.HRESULT]


class IAppBar(_inspectable.IInspectable):
    get_IsOpen: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_IsOpen: _Callable[[_type.boolean],  # value
                          _type.HRESULT]
    get_IsSticky: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    put_IsSticky: _Callable[[_type.boolean],  # value
                            _type.HRESULT]
    add_Opened: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Opened: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    add_Closed: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Closed: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]


class IAppBar2(_inspectable.IInspectable):
    get_ClosedDisplayMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.AppBarClosedDisplayMode]],  # value
                                     _type.HRESULT]
    put_ClosedDisplayMode: _Callable[[_enum.Windows.UI.Xaml.Controls.AppBarClosedDisplayMode],  # value
                                     _type.HRESULT]


class IAppBar3(_inspectable.IInspectable):
    get_TemplateSettings: _Callable[[_Pointer[_Windows_UI_Xaml_Controls_Primitives.IAppBarTemplateSettings]],  # value
                                    _type.HRESULT]
    add_Opening: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Opening: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_Closing: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Closing: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]


class IAppBar4(_inspectable.IInspectable):
    get_LightDismissOverlayMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.LightDismissOverlayMode]],  # value
                                           _type.HRESULT]
    put_LightDismissOverlayMode: _Callable[[_enum.Windows.UI.Xaml.Controls.LightDismissOverlayMode],  # value
                                           _type.HRESULT]


class IAppBarButton(_inspectable.IInspectable):
    get_Label: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Label: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Icon: _Callable[[_Pointer[IIconElement]],  # value
                        _type.HRESULT]
    put_Icon: _Callable[[IIconElement],  # value
                        _type.HRESULT]


class IAppBarButton3(_inspectable.IInspectable):
    get_LabelPosition: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.CommandBarLabelPosition]],  # value
                                 _type.HRESULT]
    put_LabelPosition: _Callable[[_enum.Windows.UI.Xaml.Controls.CommandBarLabelPosition],  # value
                                 _type.HRESULT]


class IAppBarButton4(_inspectable.IInspectable):
    get_KeyboardAcceleratorTextOverride: _Callable[[_Pointer[_type.HSTRING]],  # value
                                                   _type.HRESULT]
    put_KeyboardAcceleratorTextOverride: _Callable[[_type.HSTRING],  # value
                                                   _type.HRESULT]


class IAppBarButton5(_inspectable.IInspectable):
    get_TemplateSettings: _Callable[[_Pointer[_Windows_UI_Xaml_Controls_Primitives.IAppBarButtonTemplateSettings]],  # value
                                    _type.HRESULT]


class IAppBarButtonFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IAppBarButton]],  # value
                              _type.HRESULT]


class IAppBarButtonStatics(_inspectable.IInspectable):
    get_LabelProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_IconProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]
    get_IsCompactProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]

    _factory = True


class IAppBarButtonStatics3(_inspectable.IInspectable):
    get_LabelPositionProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_IsInOverflowProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_DynamicOverflowOrderProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]

    _factory = True


class IAppBarButtonStatics4(_inspectable.IInspectable):
    get_KeyboardAcceleratorTextOverrideProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                           _type.HRESULT]

    _factory = True


class IAppBarElementContainer(_inspectable.IInspectable):
    pass


class IAppBarElementContainerFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IAppBarElementContainer]],  # value
                              _type.HRESULT]


class IAppBarElementContainerStatics(_inspectable.IInspectable):
    get_IsCompactProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_IsInOverflowProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_DynamicOverflowOrderProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]

    _factory = True


class IAppBarFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IAppBar]],  # value
                              _type.HRESULT]


class IAppBarOverrides(_inspectable.IInspectable):
    OnClosed: _Callable[[_inspectable.IInspectable],  # e
                        _type.HRESULT]
    OnOpened: _Callable[[_inspectable.IInspectable],  # e
                        _type.HRESULT]


class IAppBarOverrides3(_inspectable.IInspectable):
    OnClosing: _Callable[[_inspectable.IInspectable],  # e
                         _type.HRESULT]
    OnOpening: _Callable[[_inspectable.IInspectable],  # e
                         _type.HRESULT]


class IAppBarSeparator(_inspectable.IInspectable):
    pass


class IAppBarSeparatorFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IAppBarSeparator]],  # value
                              _type.HRESULT]


class IAppBarSeparatorStatics(_inspectable.IInspectable):
    get_IsCompactProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]

    _factory = True


class IAppBarSeparatorStatics3(_inspectable.IInspectable):
    get_IsInOverflowProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_DynamicOverflowOrderProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]

    _factory = True


class IAppBarStatics(_inspectable.IInspectable):
    get_IsOpenProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_IsStickyProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]

    _factory = True


class IAppBarStatics2(_inspectable.IInspectable):
    get_ClosedDisplayModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]

    _factory = True


class IAppBarStatics4(_inspectable.IInspectable):
    get_LightDismissOverlayModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]

    _factory = True


class IAppBarToggleButton(_inspectable.IInspectable):
    get_Label: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Label: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Icon: _Callable[[_Pointer[IIconElement]],  # value
                        _type.HRESULT]
    put_Icon: _Callable[[IIconElement],  # value
                        _type.HRESULT]


class IAppBarToggleButton3(_inspectable.IInspectable):
    get_LabelPosition: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.CommandBarLabelPosition]],  # value
                                 _type.HRESULT]
    put_LabelPosition: _Callable[[_enum.Windows.UI.Xaml.Controls.CommandBarLabelPosition],  # value
                                 _type.HRESULT]


class IAppBarToggleButton4(_inspectable.IInspectable):
    get_KeyboardAcceleratorTextOverride: _Callable[[_Pointer[_type.HSTRING]],  # value
                                                   _type.HRESULT]
    put_KeyboardAcceleratorTextOverride: _Callable[[_type.HSTRING],  # value
                                                   _type.HRESULT]


class IAppBarToggleButton5(_inspectable.IInspectable):
    get_TemplateSettings: _Callable[[_Pointer[_Windows_UI_Xaml_Controls_Primitives.IAppBarToggleButtonTemplateSettings]],  # value
                                    _type.HRESULT]


class IAppBarToggleButtonFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IAppBarToggleButton]],  # value
                              _type.HRESULT]


class IAppBarToggleButtonStatics(_inspectable.IInspectable):
    get_LabelProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_IconProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]
    get_IsCompactProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]

    _factory = True


class IAppBarToggleButtonStatics3(_inspectable.IInspectable):
    get_LabelPositionProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_IsInOverflowProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_DynamicOverflowOrderProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]

    _factory = True


class IAppBarToggleButtonStatics4(_inspectable.IInspectable):
    get_KeyboardAcceleratorTextOverrideProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                           _type.HRESULT]

    _factory = True


class IAutoSuggestBox(_inspectable.IInspectable):
    get_MaxSuggestionListHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                           _type.HRESULT]
    put_MaxSuggestionListHeight: _Callable[[_type.DOUBLE],  # value
                                           _type.HRESULT]
    get_IsSuggestionListOpen: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    put_IsSuggestionListOpen: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]
    get_TextMemberPath: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    put_TextMemberPath: _Callable[[_type.HSTRING],  # value
                                  _type.HRESULT]
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Text: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_UpdateTextOnSelect: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_UpdateTextOnSelect: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    get_PlaceholderText: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    put_PlaceholderText: _Callable[[_type.HSTRING],  # value
                                   _type.HRESULT]
    get_Header: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                          _type.HRESULT]
    put_Header: _Callable[[_inspectable.IInspectable],  # value
                          _type.HRESULT]
    get_AutoMaximizeSuggestionArea: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]
    put_AutoMaximizeSuggestionArea: _Callable[[_type.boolean],  # value
                                              _type.HRESULT]
    get_TextBoxStyle: _Callable[[_Pointer[_Windows_UI_Xaml.IStyle]],  # value
                                _type.HRESULT]
    put_TextBoxStyle: _Callable[[_Windows_UI_Xaml.IStyle],  # value
                                _type.HRESULT]
    add_SuggestionChosen: _Callable[[_Windows_Foundation.ITypedEventHandler[IAutoSuggestBox, IAutoSuggestBoxSuggestionChosenEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_SuggestionChosen: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    add_TextChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAutoSuggestBox, IAutoSuggestBoxTextChangedEventArgs],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_TextChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]


class IAutoSuggestBox2(_inspectable.IInspectable):
    get_QueryIcon: _Callable[[_Pointer[IIconElement]],  # value
                             _type.HRESULT]
    put_QueryIcon: _Callable[[IIconElement],  # value
                             _type.HRESULT]
    add_QuerySubmitted: _Callable[[_Windows_Foundation.ITypedEventHandler[IAutoSuggestBox, IAutoSuggestBoxQuerySubmittedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_QuerySubmitted: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]


class IAutoSuggestBox3(_inspectable.IInspectable):
    get_LightDismissOverlayMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.LightDismissOverlayMode]],  # value
                                           _type.HRESULT]
    put_LightDismissOverlayMode: _Callable[[_enum.Windows.UI.Xaml.Controls.LightDismissOverlayMode],  # value
                                           _type.HRESULT]


class IAutoSuggestBox4(_inspectable.IInspectable):
    get_Description: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_inspectable.IInspectable],  # value
                               _type.HRESULT]


class IAutoSuggestBoxQuerySubmittedEventArgs(_inspectable.IInspectable):
    get_QueryText: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_ChosenSuggestion: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                    _type.HRESULT]


class IAutoSuggestBoxStatics(_inspectable.IInspectable):
    get_MaxSuggestionListHeightProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_IsSuggestionListOpenProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_TextMemberPathProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_TextProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]
    get_UpdateTextOnSelectProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_PlaceholderTextProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_HeaderProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_AutoMaximizeSuggestionAreaProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                      _type.HRESULT]
    get_TextBoxStyleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]

    _factory = True


class IAutoSuggestBoxStatics2(_inspectable.IInspectable):
    get_QueryIconProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]

    _factory = True


class IAutoSuggestBoxStatics3(_inspectable.IInspectable):
    get_LightDismissOverlayModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]

    _factory = True


class IAutoSuggestBoxStatics4(_inspectable.IInspectable):
    get_DescriptionProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]

    _factory = True


class IAutoSuggestBoxSuggestionChosenEventArgs(_inspectable.IInspectable):
    get_SelectedItem: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                _type.HRESULT]


class IAutoSuggestBoxTextChangedEventArgs(_inspectable.IInspectable):
    get_Reason: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.AutoSuggestionBoxTextChangeReason]],  # value
                          _type.HRESULT]
    put_Reason: _Callable[[_enum.Windows.UI.Xaml.Controls.AutoSuggestionBoxTextChangeReason],  # value
                          _type.HRESULT]
    CheckCurrent: _Callable[[_Pointer[_type.boolean]],  # result
                            _type.HRESULT]


class IAutoSuggestBoxTextChangedEventArgsStatics(_inspectable.IInspectable):
    get_ReasonProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]

    _factory = True


class IBackClickEventArgs(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class IBitmapIcon(_inspectable.IInspectable):
    get_UriSource: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                             _type.HRESULT]
    put_UriSource: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                             _type.HRESULT]


class IBitmapIcon2(_inspectable.IInspectable):
    get_ShowAsMonochrome: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_ShowAsMonochrome: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]


class IBitmapIconFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IBitmapIcon]],  # value
                              _type.HRESULT]


class IBitmapIconSource(_inspectable.IInspectable):
    get_UriSource: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                             _type.HRESULT]
    put_UriSource: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                             _type.HRESULT]
    get_ShowAsMonochrome: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_ShowAsMonochrome: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]


class IBitmapIconSourceFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IBitmapIconSource]],  # value
                              _type.HRESULT]


class IBitmapIconSourceStatics(_inspectable.IInspectable):
    get_UriSourceProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_ShowAsMonochromeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]

    _factory = True


class IBitmapIconStatics(_inspectable.IInspectable):
    get_UriSourceProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]

    _factory = True


class IBitmapIconStatics2(_inspectable.IInspectable):
    get_ShowAsMonochromeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]

    _factory = True


class IBorder(_inspectable.IInspectable):
    get_BorderBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                               _type.HRESULT]
    put_BorderBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                               _type.HRESULT]
    get_BorderThickness: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                                   _type.HRESULT]
    put_BorderThickness: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                                   _type.HRESULT]
    get_Background: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                              _type.HRESULT]
    put_Background: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                              _type.HRESULT]
    get_CornerRadius: _Callable[[_Pointer[_struct.Windows.UI.Xaml.CornerRadius]],  # value
                                _type.HRESULT]
    put_CornerRadius: _Callable[[_struct.Windows.UI.Xaml.CornerRadius],  # value
                                _type.HRESULT]
    get_Padding: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                           _type.HRESULT]
    put_Padding: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                           _type.HRESULT]
    get_Child: _Callable[[_Pointer[_Windows_UI_Xaml.IUIElement]],  # value
                         _type.HRESULT]
    put_Child: _Callable[[_Windows_UI_Xaml.IUIElement],  # value
                         _type.HRESULT]
    get_ChildTransitions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Media_Animation.ITransition]]],  # value
                                    _type.HRESULT]
    put_ChildTransitions: _Callable[[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Media_Animation.ITransition]],  # value
                                    _type.HRESULT]


class IBorder2(_inspectable.IInspectable):
    get_BackgroundSizing: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.BackgroundSizing]],  # value
                                    _type.HRESULT]
    put_BackgroundSizing: _Callable[[_enum.Windows.UI.Xaml.Controls.BackgroundSizing],  # value
                                    _type.HRESULT]
    get_BackgroundTransition: _Callable[[_Pointer[_Windows_UI_Xaml.IBrushTransition]],  # value
                                        _type.HRESULT]
    put_BackgroundTransition: _Callable[[_Windows_UI_Xaml.IBrushTransition],  # value
                                        _type.HRESULT]


class IBorderStatics(_inspectable.IInspectable):
    get_BorderBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_BorderThicknessProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_BackgroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_CornerRadiusProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_PaddingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_ChildTransitionsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]

    _factory = True


class IBorderStatics2(_inspectable.IInspectable):
    get_BackgroundSizingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]

    _factory = True


class IButton(_inspectable.IInspectable):
    pass


class IButtonFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IButton]],  # value
                              _type.HRESULT]


class IButtonStaticsWithFlyout(_inspectable.IInspectable):
    get_FlyoutProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]

    _factory = True


class IButtonWithFlyout(_inspectable.IInspectable):
    get_Flyout: _Callable[[_Pointer[_Windows_UI_Xaml_Controls_Primitives.IFlyoutBase]],  # value
                          _type.HRESULT]
    put_Flyout: _Callable[[_Windows_UI_Xaml_Controls_Primitives.IFlyoutBase],  # value
                          _type.HRESULT]


class ICalendarDatePicker(_inspectable.IInspectable):
    get_Date: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                        _type.HRESULT]
    put_Date: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                        _type.HRESULT]
    get_IsCalendarOpen: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    put_IsCalendarOpen: _Callable[[_type.boolean],  # value
                                  _type.HRESULT]
    get_DateFormat: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_DateFormat: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]
    get_PlaceholderText: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    put_PlaceholderText: _Callable[[_type.HSTRING],  # value
                                   _type.HRESULT]
    get_Header: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                          _type.HRESULT]
    put_Header: _Callable[[_inspectable.IInspectable],  # value
                          _type.HRESULT]
    get_HeaderTemplate: _Callable[[_Pointer[_Windows_UI_Xaml.IDataTemplate]],  # value
                                  _type.HRESULT]
    put_HeaderTemplate: _Callable[[_Windows_UI_Xaml.IDataTemplate],  # value
                                  _type.HRESULT]
    get_CalendarViewStyle: _Callable[[_Pointer[_Windows_UI_Xaml.IStyle]],  # value
                                     _type.HRESULT]
    put_CalendarViewStyle: _Callable[[_Windows_UI_Xaml.IStyle],  # value
                                     _type.HRESULT]
    get_MinDate: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                           _type.HRESULT]
    put_MinDate: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                           _type.HRESULT]
    get_MaxDate: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                           _type.HRESULT]
    put_MaxDate: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                           _type.HRESULT]
    get_IsTodayHighlighted: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_IsTodayHighlighted: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    get_DisplayMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.CalendarViewDisplayMode]],  # value
                               _type.HRESULT]
    put_DisplayMode: _Callable[[_enum.Windows.UI.Xaml.Controls.CalendarViewDisplayMode],  # value
                               _type.HRESULT]
    get_FirstDayOfWeek: _Callable[[_Pointer[_enum.Windows.Globalization.DayOfWeek]],  # value
                                  _type.HRESULT]
    put_FirstDayOfWeek: _Callable[[_enum.Windows.Globalization.DayOfWeek],  # value
                                  _type.HRESULT]
    get_DayOfWeekFormat: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    put_DayOfWeekFormat: _Callable[[_type.HSTRING],  # value
                                   _type.HRESULT]
    get_CalendarIdentifier: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    put_CalendarIdentifier: _Callable[[_type.HSTRING],  # value
                                      _type.HRESULT]
    get_IsOutOfScopeEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_IsOutOfScopeEnabled: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_IsGroupLabelVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_IsGroupLabelVisible: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    add_CalendarViewDayItemChanging: _Callable[[ICalendarViewDayItemChangingEventHandler,  # handler
                                                _Pointer[_struct.EventRegistrationToken]],  # token
                                               _type.HRESULT]
    remove_CalendarViewDayItemChanging: _Callable[[_struct.EventRegistrationToken],  # token
                                                  _type.HRESULT]
    add_DateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ICalendarDatePicker, ICalendarDatePickerDateChangedEventArgs],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_DateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    add_Opened: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Opened: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    add_Closed: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Closed: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    SetDisplayDate: _Callable[[_struct.Windows.Foundation.DateTime],  # date
                              _type.HRESULT]
    SetYearDecadeDisplayDimensions: _Callable[[_type.INT32,  # columns
                                               _type.INT32],  # rows
                                              _type.HRESULT]


class ICalendarDatePicker2(_inspectable.IInspectable):
    get_LightDismissOverlayMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.LightDismissOverlayMode]],  # value
                                           _type.HRESULT]
    put_LightDismissOverlayMode: _Callable[[_enum.Windows.UI.Xaml.Controls.LightDismissOverlayMode],  # value
                                           _type.HRESULT]


class ICalendarDatePicker3(_inspectable.IInspectable):
    get_Description: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_inspectable.IInspectable],  # value
                               _type.HRESULT]


class ICalendarDatePickerDateChangedEventArgs(_inspectable.IInspectable):
    get_NewDate: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                           _type.HRESULT]
    get_OldDate: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                           _type.HRESULT]


class ICalendarDatePickerFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ICalendarDatePicker]],  # value
                              _type.HRESULT]


class ICalendarDatePickerStatics(_inspectable.IInspectable):
    get_DateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]
    get_IsCalendarOpenProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_DateFormatProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_PlaceholderTextProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_HeaderProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_HeaderTemplateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_CalendarViewStyleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_MinDateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_MaxDateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_IsTodayHighlightedProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_DisplayModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_FirstDayOfWeekProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_DayOfWeekFormatProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_CalendarIdentifierProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_IsOutOfScopeEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_IsGroupLabelVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]

    _factory = True


class ICalendarDatePickerStatics2(_inspectable.IInspectable):
    get_LightDismissOverlayModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]

    _factory = True


class ICalendarDatePickerStatics3(_inspectable.IInspectable):
    get_DescriptionProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]

    _factory = True


class ICalendarView(_inspectable.IInspectable):
    get_CalendarIdentifier: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    put_CalendarIdentifier: _Callable[[_type.HSTRING],  # value
                                      _type.HRESULT]
    get_DayOfWeekFormat: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    put_DayOfWeekFormat: _Callable[[_type.HSTRING],  # value
                                   _type.HRESULT]
    get_IsGroupLabelVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_IsGroupLabelVisible: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_DisplayMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.CalendarViewDisplayMode]],  # value
                               _type.HRESULT]
    put_DisplayMode: _Callable[[_enum.Windows.UI.Xaml.Controls.CalendarViewDisplayMode],  # value
                               _type.HRESULT]
    get_FirstDayOfWeek: _Callable[[_Pointer[_enum.Windows.Globalization.DayOfWeek]],  # value
                                  _type.HRESULT]
    put_FirstDayOfWeek: _Callable[[_enum.Windows.Globalization.DayOfWeek],  # value
                                  _type.HRESULT]
    get_IsOutOfScopeEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_IsOutOfScopeEnabled: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_IsTodayHighlighted: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_IsTodayHighlighted: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    get_MaxDate: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                           _type.HRESULT]
    put_MaxDate: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                           _type.HRESULT]
    get_MinDate: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                           _type.HRESULT]
    put_MinDate: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                           _type.HRESULT]
    get_NumberOfWeeksInView: _Callable[[_Pointer[_type.INT32]],  # value
                                       _type.HRESULT]
    put_NumberOfWeeksInView: _Callable[[_type.INT32],  # value
                                       _type.HRESULT]
    get_SelectedDates: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_struct.Windows.Foundation.DateTime]]],  # value
                                 _type.HRESULT]
    get_SelectionMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.CalendarViewSelectionMode]],  # value
                                 _type.HRESULT]
    put_SelectionMode: _Callable[[_enum.Windows.UI.Xaml.Controls.CalendarViewSelectionMode],  # value
                                 _type.HRESULT]
    get_TemplateSettings: _Callable[[_Pointer[_Windows_UI_Xaml_Controls_Primitives.ICalendarViewTemplateSettings]],  # value
                                    _type.HRESULT]
    get_FocusBorderBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                    _type.HRESULT]
    put_FocusBorderBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                    _type.HRESULT]
    get_SelectedHoverBorderBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                            _type.HRESULT]
    put_SelectedHoverBorderBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                            _type.HRESULT]
    get_SelectedPressedBorderBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                              _type.HRESULT]
    put_SelectedPressedBorderBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                              _type.HRESULT]
    get_SelectedBorderBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                       _type.HRESULT]
    put_SelectedBorderBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                       _type.HRESULT]
    get_HoverBorderBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                    _type.HRESULT]
    put_HoverBorderBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                    _type.HRESULT]
    get_PressedBorderBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                      _type.HRESULT]
    put_PressedBorderBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                      _type.HRESULT]
    get_CalendarItemBorderBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                           _type.HRESULT]
    put_CalendarItemBorderBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                           _type.HRESULT]
    get_OutOfScopeBackground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                        _type.HRESULT]
    put_OutOfScopeBackground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                        _type.HRESULT]
    get_CalendarItemBackground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                          _type.HRESULT]
    put_CalendarItemBackground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                          _type.HRESULT]
    get_PressedForeground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                     _type.HRESULT]
    put_PressedForeground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                     _type.HRESULT]
    get_TodayForeground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                   _type.HRESULT]
    put_TodayForeground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                   _type.HRESULT]
    get_BlackoutForeground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                      _type.HRESULT]
    put_BlackoutForeground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                      _type.HRESULT]
    get_SelectedForeground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                      _type.HRESULT]
    put_SelectedForeground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                      _type.HRESULT]
    get_OutOfScopeForeground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                        _type.HRESULT]
    put_OutOfScopeForeground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                        _type.HRESULT]
    get_CalendarItemForeground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                          _type.HRESULT]
    put_CalendarItemForeground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                          _type.HRESULT]
    get_DayItemFontFamily: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IFontFamily]],  # value
                                     _type.HRESULT]
    put_DayItemFontFamily: _Callable[[_Windows_UI_Xaml_Media.IFontFamily],  # value
                                     _type.HRESULT]
    get_DayItemFontSize: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                   _type.HRESULT]
    put_DayItemFontSize: _Callable[[_type.DOUBLE],  # value
                                   _type.HRESULT]
    get_DayItemFontStyle: _Callable[[_Pointer[_enum.Windows.UI.Text.FontStyle]],  # value
                                    _type.HRESULT]
    put_DayItemFontStyle: _Callable[[_enum.Windows.UI.Text.FontStyle],  # value
                                    _type.HRESULT]
    get_DayItemFontWeight: _Callable[[_Pointer[_struct.Windows.UI.Text.FontWeight]],  # value
                                     _type.HRESULT]
    put_DayItemFontWeight: _Callable[[_struct.Windows.UI.Text.FontWeight],  # value
                                     _type.HRESULT]
    get_TodayFontWeight: _Callable[[_Pointer[_struct.Windows.UI.Text.FontWeight]],  # value
                                   _type.HRESULT]
    put_TodayFontWeight: _Callable[[_struct.Windows.UI.Text.FontWeight],  # value
                                   _type.HRESULT]
    get_FirstOfMonthLabelFontFamily: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IFontFamily]],  # value
                                               _type.HRESULT]
    put_FirstOfMonthLabelFontFamily: _Callable[[_Windows_UI_Xaml_Media.IFontFamily],  # value
                                               _type.HRESULT]
    get_FirstOfMonthLabelFontSize: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                             _type.HRESULT]
    put_FirstOfMonthLabelFontSize: _Callable[[_type.DOUBLE],  # value
                                             _type.HRESULT]
    get_FirstOfMonthLabelFontStyle: _Callable[[_Pointer[_enum.Windows.UI.Text.FontStyle]],  # value
                                              _type.HRESULT]
    put_FirstOfMonthLabelFontStyle: _Callable[[_enum.Windows.UI.Text.FontStyle],  # value
                                              _type.HRESULT]
    get_FirstOfMonthLabelFontWeight: _Callable[[_Pointer[_struct.Windows.UI.Text.FontWeight]],  # value
                                               _type.HRESULT]
    put_FirstOfMonthLabelFontWeight: _Callable[[_struct.Windows.UI.Text.FontWeight],  # value
                                               _type.HRESULT]
    get_MonthYearItemFontFamily: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IFontFamily]],  # value
                                           _type.HRESULT]
    put_MonthYearItemFontFamily: _Callable[[_Windows_UI_Xaml_Media.IFontFamily],  # value
                                           _type.HRESULT]
    get_MonthYearItemFontSize: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                         _type.HRESULT]
    put_MonthYearItemFontSize: _Callable[[_type.DOUBLE],  # value
                                         _type.HRESULT]
    get_MonthYearItemFontStyle: _Callable[[_Pointer[_enum.Windows.UI.Text.FontStyle]],  # value
                                          _type.HRESULT]
    put_MonthYearItemFontStyle: _Callable[[_enum.Windows.UI.Text.FontStyle],  # value
                                          _type.HRESULT]
    get_MonthYearItemFontWeight: _Callable[[_Pointer[_struct.Windows.UI.Text.FontWeight]],  # value
                                           _type.HRESULT]
    put_MonthYearItemFontWeight: _Callable[[_struct.Windows.UI.Text.FontWeight],  # value
                                           _type.HRESULT]
    get_FirstOfYearDecadeLabelFontFamily: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IFontFamily]],  # value
                                                    _type.HRESULT]
    put_FirstOfYearDecadeLabelFontFamily: _Callable[[_Windows_UI_Xaml_Media.IFontFamily],  # value
                                                    _type.HRESULT]
    get_FirstOfYearDecadeLabelFontSize: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                  _type.HRESULT]
    put_FirstOfYearDecadeLabelFontSize: _Callable[[_type.DOUBLE],  # value
                                                  _type.HRESULT]
    get_FirstOfYearDecadeLabelFontStyle: _Callable[[_Pointer[_enum.Windows.UI.Text.FontStyle]],  # value
                                                   _type.HRESULT]
    put_FirstOfYearDecadeLabelFontStyle: _Callable[[_enum.Windows.UI.Text.FontStyle],  # value
                                                   _type.HRESULT]
    get_FirstOfYearDecadeLabelFontWeight: _Callable[[_Pointer[_struct.Windows.UI.Text.FontWeight]],  # value
                                                    _type.HRESULT]
    put_FirstOfYearDecadeLabelFontWeight: _Callable[[_struct.Windows.UI.Text.FontWeight],  # value
                                                    _type.HRESULT]
    get_HorizontalDayItemAlignment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.HorizontalAlignment]],  # value
                                              _type.HRESULT]
    put_HorizontalDayItemAlignment: _Callable[[_enum.Windows.UI.Xaml.HorizontalAlignment],  # value
                                              _type.HRESULT]
    get_VerticalDayItemAlignment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.VerticalAlignment]],  # value
                                            _type.HRESULT]
    put_VerticalDayItemAlignment: _Callable[[_enum.Windows.UI.Xaml.VerticalAlignment],  # value
                                            _type.HRESULT]
    get_HorizontalFirstOfMonthLabelAlignment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.HorizontalAlignment]],  # value
                                                        _type.HRESULT]
    put_HorizontalFirstOfMonthLabelAlignment: _Callable[[_enum.Windows.UI.Xaml.HorizontalAlignment],  # value
                                                        _type.HRESULT]
    get_VerticalFirstOfMonthLabelAlignment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.VerticalAlignment]],  # value
                                                      _type.HRESULT]
    put_VerticalFirstOfMonthLabelAlignment: _Callable[[_enum.Windows.UI.Xaml.VerticalAlignment],  # value
                                                      _type.HRESULT]
    get_CalendarItemBorderThickness: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                                               _type.HRESULT]
    put_CalendarItemBorderThickness: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                                               _type.HRESULT]
    get_CalendarViewDayItemStyle: _Callable[[_Pointer[_Windows_UI_Xaml.IStyle]],  # value
                                            _type.HRESULT]
    put_CalendarViewDayItemStyle: _Callable[[_Windows_UI_Xaml.IStyle],  # value
                                            _type.HRESULT]
    add_CalendarViewDayItemChanging: _Callable[[_Windows_Foundation.ITypedEventHandler[ICalendarView, ICalendarViewDayItemChangingEventArgs],  # handler
                                                _Pointer[_struct.EventRegistrationToken]],  # token
                                               _type.HRESULT]
    remove_CalendarViewDayItemChanging: _Callable[[_struct.EventRegistrationToken],  # token
                                                  _type.HRESULT]
    add_SelectedDatesChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ICalendarView, ICalendarViewSelectedDatesChangedEventArgs],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_SelectedDatesChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    SetDisplayDate: _Callable[[_struct.Windows.Foundation.DateTime],  # date
                              _type.HRESULT]
    SetYearDecadeDisplayDimensions: _Callable[[_type.INT32,  # columns
                                               _type.INT32],  # rows
                                              _type.HRESULT]


class ICalendarView2(_inspectable.IInspectable):
    get_SelectedDisabledBorderBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                               _type.HRESULT]
    put_SelectedDisabledBorderBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                               _type.HRESULT]
    get_TodaySelectedInnerBorderBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                                 _type.HRESULT]
    put_TodaySelectedInnerBorderBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                                 _type.HRESULT]
    get_BlackoutStrikethroughBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                              _type.HRESULT]
    put_BlackoutStrikethroughBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                              _type.HRESULT]
    get_BlackoutBackground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                      _type.HRESULT]
    put_BlackoutBackground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                      _type.HRESULT]
    get_CalendarItemHoverBackground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                               _type.HRESULT]
    put_CalendarItemHoverBackground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                               _type.HRESULT]
    get_CalendarItemPressedBackground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                                 _type.HRESULT]
    put_CalendarItemPressedBackground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                                 _type.HRESULT]
    get_CalendarItemDisabledBackground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                                  _type.HRESULT]
    put_CalendarItemDisabledBackground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                                  _type.HRESULT]
    get_TodayBackground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                   _type.HRESULT]
    put_TodayBackground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                   _type.HRESULT]
    get_TodayBlackoutBackground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                           _type.HRESULT]
    put_TodayBlackoutBackground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                           _type.HRESULT]
    get_TodayHoverBackground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                        _type.HRESULT]
    put_TodayHoverBackground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                        _type.HRESULT]
    get_TodayPressedBackground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                          _type.HRESULT]
    put_TodayPressedBackground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                          _type.HRESULT]
    get_TodayDisabledBackground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                           _type.HRESULT]
    put_TodayDisabledBackground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                           _type.HRESULT]
    get_TodayBlackoutForeground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                           _type.HRESULT]
    put_TodayBlackoutForeground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                           _type.HRESULT]
    get_SelectedHoverForeground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                           _type.HRESULT]
    put_SelectedHoverForeground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                           _type.HRESULT]
    get_SelectedPressedForeground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                             _type.HRESULT]
    put_SelectedPressedForeground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                             _type.HRESULT]
    get_SelectedDisabledForeground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                              _type.HRESULT]
    put_SelectedDisabledForeground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                              _type.HRESULT]
    get_OutOfScopeHoverForeground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                             _type.HRESULT]
    put_OutOfScopeHoverForeground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                             _type.HRESULT]
    get_OutOfScopePressedForeground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                               _type.HRESULT]
    put_OutOfScopePressedForeground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                               _type.HRESULT]
    get_DisabledForeground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                      _type.HRESULT]
    put_DisabledForeground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                      _type.HRESULT]
    get_DayItemMargin: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                                 _type.HRESULT]
    put_DayItemMargin: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                                 _type.HRESULT]
    get_MonthYearItemMargin: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                                       _type.HRESULT]
    put_MonthYearItemMargin: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                                       _type.HRESULT]
    get_FirstOfMonthLabelMargin: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                                           _type.HRESULT]
    put_FirstOfMonthLabelMargin: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                                           _type.HRESULT]
    get_FirstOfYearDecadeLabelMargin: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                                                _type.HRESULT]
    put_FirstOfYearDecadeLabelMargin: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                                                _type.HRESULT]
    get_CalendarItemCornerRadius: _Callable[[_Pointer[_struct.Windows.UI.Xaml.CornerRadius]],  # value
                                            _type.HRESULT]
    put_CalendarItemCornerRadius: _Callable[[_struct.Windows.UI.Xaml.CornerRadius],  # value
                                            _type.HRESULT]


class ICalendarViewDayItem(_inspectable.IInspectable):
    get_IsBlackout: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    put_IsBlackout: _Callable[[_type.boolean],  # value
                              _type.HRESULT]
    get_Date: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                        _type.HRESULT]
    SetDensityColors: _Callable[[_Windows_Foundation_Collections.IIterable[_struct.Windows.UI.Color]],  # colors
                                _type.HRESULT]


class ICalendarViewDayItemChangingEventArgs(_inspectable.IInspectable):
    get_InRecycleQueue: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    get_Item: _Callable[[_Pointer[ICalendarViewDayItem]],  # value
                        _type.HRESULT]
    get_Phase: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    RegisterUpdateCallback: _Callable[[_Windows_Foundation.ITypedEventHandler[ICalendarView, ICalendarViewDayItemChangingEventArgs]],  # callback
                                      _type.HRESULT]
    RegisterUpdateCallbackWithPhase: _Callable[[_type.UINT32,  # callbackPhase
                                                _Windows_Foundation.ITypedEventHandler[ICalendarView, ICalendarViewDayItemChangingEventArgs]],  # callback
                                               _type.HRESULT]


class ICalendarViewDayItemFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ICalendarViewDayItem]],  # value
                              _type.HRESULT]


class ICalendarViewDayItemStatics(_inspectable.IInspectable):
    get_IsBlackoutProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_DateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]

    _factory = True


class ICalendarViewFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ICalendarView]],  # value
                              _type.HRESULT]


class ICalendarViewSelectedDatesChangedEventArgs(_inspectable.IInspectable):
    get_AddedDates: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_struct.Windows.Foundation.DateTime]]],  # value
                              _type.HRESULT]
    get_RemovedDates: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_struct.Windows.Foundation.DateTime]]],  # value
                                _type.HRESULT]


class ICalendarViewStatics(_inspectable.IInspectable):
    get_CalendarIdentifierProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_DayOfWeekFormatProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_IsGroupLabelVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_DisplayModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_FirstDayOfWeekProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_IsOutOfScopeEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_IsTodayHighlightedProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_MaxDateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_MinDateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_NumberOfWeeksInViewProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_SelectedDatesProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_SelectionModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_TemplateSettingsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_FocusBorderBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_SelectedHoverBorderBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]
    get_SelectedPressedBorderBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                      _type.HRESULT]
    get_SelectedBorderBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_HoverBorderBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_PressedBorderBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_CalendarItemBorderBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_OutOfScopeBackgroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_CalendarItemBackgroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]
    get_PressedForegroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_TodayForegroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_BlackoutForegroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_SelectedForegroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_OutOfScopeForegroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_CalendarItemForegroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]
    get_DayItemFontFamilyProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_DayItemFontSizeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_DayItemFontStyleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_DayItemFontWeightProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_TodayFontWeightProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_FirstOfMonthLabelFontFamilyProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]
    get_FirstOfMonthLabelFontSizeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                     _type.HRESULT]
    get_FirstOfMonthLabelFontStyleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                      _type.HRESULT]
    get_FirstOfMonthLabelFontWeightProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]
    get_MonthYearItemFontFamilyProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_MonthYearItemFontSizeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_MonthYearItemFontStyleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]
    get_MonthYearItemFontWeightProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_FirstOfYearDecadeLabelFontFamilyProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                            _type.HRESULT]
    get_FirstOfYearDecadeLabelFontSizeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                          _type.HRESULT]
    get_FirstOfYearDecadeLabelFontStyleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                           _type.HRESULT]
    get_FirstOfYearDecadeLabelFontWeightProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                            _type.HRESULT]
    get_HorizontalDayItemAlignmentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                      _type.HRESULT]
    get_VerticalDayItemAlignmentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]
    get_HorizontalFirstOfMonthLabelAlignmentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                                _type.HRESULT]
    get_VerticalFirstOfMonthLabelAlignmentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                              _type.HRESULT]
    get_CalendarItemBorderThicknessProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]
    get_CalendarViewDayItemStyleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]

    _factory = True


class ICalendarViewStatics2(_inspectable.IInspectable):
    get_SelectedDisabledBorderBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]
    get_TodaySelectedInnerBorderBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                         _type.HRESULT]
    get_BlackoutStrikethroughBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                      _type.HRESULT]
    get_BlackoutBackgroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_CalendarItemHoverBackgroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]
    get_CalendarItemPressedBackgroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                         _type.HRESULT]
    get_CalendarItemDisabledBackgroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                          _type.HRESULT]
    get_TodayBackgroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_TodayBlackoutBackgroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_TodayHoverBackgroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_TodayPressedBackgroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]
    get_TodayDisabledBackgroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_TodayBlackoutForegroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_SelectedHoverForegroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_SelectedPressedForegroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                     _type.HRESULT]
    get_SelectedDisabledForegroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                      _type.HRESULT]
    get_OutOfScopeHoverForegroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                     _type.HRESULT]
    get_OutOfScopePressedForegroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]
    get_DisabledForegroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_DayItemMarginProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_MonthYearItemMarginProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_FirstOfMonthLabelMarginProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_FirstOfYearDecadeLabelMarginProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                        _type.HRESULT]
    get_CalendarItemCornerRadiusProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]

    _factory = True


class ICandidateWindowBoundsChangedEventArgs(_inspectable.IInspectable):
    get_Bounds: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                          _type.HRESULT]


class ICanvas(_inspectable.IInspectable):
    pass


class ICanvasFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ICanvas]],  # value
                              _type.HRESULT]


class ICanvasStatics(_inspectable.IInspectable):
    get_LeftProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]
    GetLeft: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                        _Pointer[_type.DOUBLE]],  # result
                       _type.HRESULT]
    SetLeft: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                        _type.DOUBLE],  # length
                       _type.HRESULT]
    get_TopProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                               _type.HRESULT]
    GetTop: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                       _Pointer[_type.DOUBLE]],  # result
                      _type.HRESULT]
    SetTop: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                       _type.DOUBLE],  # length
                      _type.HRESULT]
    get_ZIndexProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    GetZIndex: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                          _Pointer[_type.INT32]],  # result
                         _type.HRESULT]
    SetZIndex: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                          _type.INT32],  # value
                         _type.HRESULT]

    _factory = True


class ICaptureElement(_inspectable.IInspectable):
    get_Source: _Callable[[_Pointer[_Windows_Media_Capture.IMediaCapture]],  # value
                          _type.HRESULT]
    put_Source: _Callable[[_Windows_Media_Capture.IMediaCapture],  # value
                          _type.HRESULT]
    get_Stretch: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Media.Stretch]],  # value
                           _type.HRESULT]
    put_Stretch: _Callable[[_enum.Windows.UI.Xaml.Media.Stretch],  # value
                           _type.HRESULT]


class ICaptureElementStatics(_inspectable.IInspectable):
    get_SourceProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_StretchProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]

    _factory = True


class ICheckBox(_inspectable.IInspectable):
    pass


class ICheckBoxFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ICheckBox]],  # value
                              _type.HRESULT]


class IChoosingGroupHeaderContainerEventArgs(_inspectable.IInspectable):
    get_GroupHeaderContainer: _Callable[[_Pointer[IListViewBaseHeaderItem]],  # value
                                        _type.HRESULT]
    put_GroupHeaderContainer: _Callable[[IListViewBaseHeaderItem],  # value
                                        _type.HRESULT]
    get_GroupIndex: _Callable[[_Pointer[_type.INT32]],  # value
                              _type.HRESULT]
    get_Group: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                         _type.HRESULT]


class IChoosingItemContainerEventArgs(_inspectable.IInspectable):
    get_ItemIndex: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]
    get_Item: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                        _type.HRESULT]
    get_ItemContainer: _Callable[[_Pointer[_Windows_UI_Xaml_Controls_Primitives.ISelectorItem]],  # value
                                 _type.HRESULT]
    put_ItemContainer: _Callable[[_Windows_UI_Xaml_Controls_Primitives.ISelectorItem],  # value
                                 _type.HRESULT]
    get_IsContainerPrepared: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_IsContainerPrepared: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]


class ICleanUpVirtualizedItemEventArgs(_inspectable.IInspectable):
    get_Value: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                         _type.HRESULT]
    get_UIElement: _Callable[[_Pointer[_Windows_UI_Xaml.IUIElement]],  # value
                             _type.HRESULT]
    get_Cancel: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_Cancel: _Callable[[_type.boolean],  # value
                          _type.HRESULT]


class IColorChangedEventArgs(_inspectable.IInspectable):
    get_OldColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                            _type.HRESULT]
    get_NewColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                            _type.HRESULT]


class IColorPicker(_inspectable.IInspectable):
    get_Color: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                         _type.HRESULT]
    put_Color: _Callable[[_struct.Windows.UI.Color],  # value
                         _type.HRESULT]
    get_PreviousColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                 _type.HRESULT]
    put_PreviousColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                 _type.HRESULT]
    get_IsAlphaEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    put_IsAlphaEnabled: _Callable[[_type.boolean],  # value
                                  _type.HRESULT]
    get_IsColorSpectrumVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_IsColorSpectrumVisible: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    get_IsColorPreviewVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_IsColorPreviewVisible: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]
    get_IsColorSliderVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    put_IsColorSliderVisible: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]
    get_IsAlphaSliderVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    put_IsAlphaSliderVisible: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]
    get_IsMoreButtonVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_IsMoreButtonVisible: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_IsColorChannelTextInputVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                                  _type.HRESULT]
    put_IsColorChannelTextInputVisible: _Callable[[_type.boolean],  # value
                                                  _type.HRESULT]
    get_IsAlphaTextInputVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    put_IsAlphaTextInputVisible: _Callable[[_type.boolean],  # value
                                           _type.HRESULT]
    get_IsHexInputVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    put_IsHexInputVisible: _Callable[[_type.boolean],  # value
                                     _type.HRESULT]
    get_MinHue: _Callable[[_Pointer[_type.INT32]],  # value
                          _type.HRESULT]
    put_MinHue: _Callable[[_type.INT32],  # value
                          _type.HRESULT]
    get_MaxHue: _Callable[[_Pointer[_type.INT32]],  # value
                          _type.HRESULT]
    put_MaxHue: _Callable[[_type.INT32],  # value
                          _type.HRESULT]
    get_MinSaturation: _Callable[[_Pointer[_type.INT32]],  # value
                                 _type.HRESULT]
    put_MinSaturation: _Callable[[_type.INT32],  # value
                                 _type.HRESULT]
    get_MaxSaturation: _Callable[[_Pointer[_type.INT32]],  # value
                                 _type.HRESULT]
    put_MaxSaturation: _Callable[[_type.INT32],  # value
                                 _type.HRESULT]
    get_MinValue: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    put_MinValue: _Callable[[_type.INT32],  # value
                            _type.HRESULT]
    get_MaxValue: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    put_MaxValue: _Callable[[_type.INT32],  # value
                            _type.HRESULT]
    get_ColorSpectrumShape: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.ColorSpectrumShape]],  # value
                                      _type.HRESULT]
    put_ColorSpectrumShape: _Callable[[_enum.Windows.UI.Xaml.Controls.ColorSpectrumShape],  # value
                                      _type.HRESULT]
    get_ColorSpectrumComponents: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.ColorSpectrumComponents]],  # value
                                           _type.HRESULT]
    put_ColorSpectrumComponents: _Callable[[_enum.Windows.UI.Xaml.Controls.ColorSpectrumComponents],  # value
                                           _type.HRESULT]
    add_ColorChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IColorPicker, IColorChangedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_ColorChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]


class IColorPickerFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IColorPicker]],  # value
                              _type.HRESULT]


class IColorPickerStatics(_inspectable.IInspectable):
    get_ColorProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_PreviousColorProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_IsAlphaEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_IsColorSpectrumVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]
    get_IsColorPreviewVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_IsColorSliderVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_IsAlphaSliderVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_IsMoreButtonVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_IsColorChannelTextInputVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                          _type.HRESULT]
    get_IsAlphaTextInputVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_IsHexInputVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_MinHueProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_MaxHueProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_MinSaturationProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_MaxSaturationProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_MinValueProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_MaxValueProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_ColorSpectrumShapeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_ColorSpectrumComponentsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]

    _factory = True


class IColumnDefinition(_inspectable.IInspectable):
    get_Width: _Callable[[_Pointer[_struct.Windows.UI.Xaml.GridLength]],  # value
                         _type.HRESULT]
    put_Width: _Callable[[_struct.Windows.UI.Xaml.GridLength],  # value
                         _type.HRESULT]
    get_MaxWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                            _type.HRESULT]
    put_MaxWidth: _Callable[[_type.DOUBLE],  # value
                            _type.HRESULT]
    get_MinWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                            _type.HRESULT]
    put_MinWidth: _Callable[[_type.DOUBLE],  # value
                            _type.HRESULT]
    get_ActualWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                               _type.HRESULT]


class IColumnDefinitionStatics(_inspectable.IInspectable):
    get_WidthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_MaxWidthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_MinWidthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]

    _factory = True


class IComboBox(_inspectable.IInspectable):
    get_IsDropDownOpen: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    put_IsDropDownOpen: _Callable[[_type.boolean],  # value
                                  _type.HRESULT]
    get_IsEditable: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_IsSelectionBoxHighlighted: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    get_MaxDropDownHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                     _type.HRESULT]
    put_MaxDropDownHeight: _Callable[[_type.DOUBLE],  # value
                                     _type.HRESULT]
    get_SelectionBoxItem: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                    _type.HRESULT]
    get_SelectionBoxItemTemplate: _Callable[[_Pointer[_Windows_UI_Xaml.IDataTemplate]],  # value
                                            _type.HRESULT]
    get_TemplateSettings: _Callable[[_Pointer[_Windows_UI_Xaml_Controls_Primitives.IComboBoxTemplateSettings]],  # value
                                    _type.HRESULT]
    add_DropDownClosed: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_DropDownClosed: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_DropDownOpened: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_DropDownOpened: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]


class IComboBox2(_inspectable.IInspectable):
    get_Header: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                          _type.HRESULT]
    put_Header: _Callable[[_inspectable.IInspectable],  # value
                          _type.HRESULT]
    get_HeaderTemplate: _Callable[[_Pointer[_Windows_UI_Xaml.IDataTemplate]],  # value
                                  _type.HRESULT]
    put_HeaderTemplate: _Callable[[_Windows_UI_Xaml.IDataTemplate],  # value
                                  _type.HRESULT]
    get_PlaceholderText: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    put_PlaceholderText: _Callable[[_type.HSTRING],  # value
                                   _type.HRESULT]


class IComboBox3(_inspectable.IInspectable):
    get_LightDismissOverlayMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.LightDismissOverlayMode]],  # value
                                           _type.HRESULT]
    put_LightDismissOverlayMode: _Callable[[_enum.Windows.UI.Xaml.Controls.LightDismissOverlayMode],  # value
                                           _type.HRESULT]
    get_IsTextSearchEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_IsTextSearchEnabled: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]


class IComboBox4(_inspectable.IInspectable):
    get_SelectionChangedTrigger: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.ComboBoxSelectionChangedTrigger]],  # value
                                           _type.HRESULT]
    put_SelectionChangedTrigger: _Callable[[_enum.Windows.UI.Xaml.Controls.ComboBoxSelectionChangedTrigger],  # value
                                           _type.HRESULT]


class IComboBox5(_inspectable.IInspectable):
    get_PlaceholderForeground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                         _type.HRESULT]
    put_PlaceholderForeground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                         _type.HRESULT]


class IComboBox6(_inspectable.IInspectable):
    put_IsEditable: _Callable[[_type.boolean],  # value
                              _type.HRESULT]
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Text: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_TextBoxStyle: _Callable[[_Pointer[_Windows_UI_Xaml.IStyle]],  # value
                                _type.HRESULT]
    put_TextBoxStyle: _Callable[[_Windows_UI_Xaml.IStyle],  # value
                                _type.HRESULT]
    get_Description: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_inspectable.IInspectable],  # value
                               _type.HRESULT]
    add_TextSubmitted: _Callable[[_Windows_Foundation.ITypedEventHandler[IComboBox, IComboBoxTextSubmittedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_TextSubmitted: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]


class IComboBoxFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IComboBox]],  # value
                              _type.HRESULT]


class IComboBoxItem(_inspectable.IInspectable):
    pass


class IComboBoxItemFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IComboBoxItem]],  # value
                              _type.HRESULT]


class IComboBoxOverrides(_inspectable.IInspectable):
    OnDropDownClosed: _Callable[[_inspectable.IInspectable],  # e
                                _type.HRESULT]
    OnDropDownOpened: _Callable[[_inspectable.IInspectable],  # e
                                _type.HRESULT]


class IComboBoxStatics(_inspectable.IInspectable):
    get_IsDropDownOpenProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_MaxDropDownHeightProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]

    _factory = True


class IComboBoxStatics2(_inspectable.IInspectable):
    get_HeaderProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_HeaderTemplateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_PlaceholderTextProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]

    _factory = True


class IComboBoxStatics3(_inspectable.IInspectable):
    get_LightDismissOverlayModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_IsTextSearchEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]

    _factory = True


class IComboBoxStatics4(_inspectable.IInspectable):
    get_SelectionChangedTriggerProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]

    _factory = True


class IComboBoxStatics5(_inspectable.IInspectable):
    get_PlaceholderForegroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]

    _factory = True


class IComboBoxStatics6(_inspectable.IInspectable):
    get_IsEditableProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_TextProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]
    get_TextBoxStyleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_DescriptionProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]

    _factory = True


class IComboBoxTextSubmittedEventArgs(_inspectable.IInspectable):
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class ICommandBar(_inspectable.IInspectable):
    get_PrimaryCommands: _Callable[[_Pointer[_Windows_Foundation_Collections.IObservableVector[ICommandBarElement]]],  # value
                                   _type.HRESULT]
    get_SecondaryCommands: _Callable[[_Pointer[_Windows_Foundation_Collections.IObservableVector[ICommandBarElement]]],  # value
                                     _type.HRESULT]


class ICommandBar2(_inspectable.IInspectable):
    get_CommandBarOverflowPresenterStyle: _Callable[[_Pointer[_Windows_UI_Xaml.IStyle]],  # value
                                                    _type.HRESULT]
    put_CommandBarOverflowPresenterStyle: _Callable[[_Windows_UI_Xaml.IStyle],  # value
                                                    _type.HRESULT]
    get_CommandBarTemplateSettings: _Callable[[_Pointer[_Windows_UI_Xaml_Controls_Primitives.ICommandBarTemplateSettings]],  # value
                                              _type.HRESULT]


class ICommandBar3(_inspectable.IInspectable):
    get_DefaultLabelPosition: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.CommandBarDefaultLabelPosition]],  # value
                                        _type.HRESULT]
    put_DefaultLabelPosition: _Callable[[_enum.Windows.UI.Xaml.Controls.CommandBarDefaultLabelPosition],  # value
                                        _type.HRESULT]
    get_OverflowButtonVisibility: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.CommandBarOverflowButtonVisibility]],  # value
                                            _type.HRESULT]
    put_OverflowButtonVisibility: _Callable[[_enum.Windows.UI.Xaml.Controls.CommandBarOverflowButtonVisibility],  # value
                                            _type.HRESULT]
    get_IsDynamicOverflowEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_IsDynamicOverflowEnabled: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]
    add_DynamicOverflowItemsChanging: _Callable[[_Windows_Foundation.ITypedEventHandler[ICommandBar, IDynamicOverflowItemsChangingEventArgs],  # handler
                                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                                _type.HRESULT]
    remove_DynamicOverflowItemsChanging: _Callable[[_struct.EventRegistrationToken],  # token
                                                   _type.HRESULT]


class ICommandBarElement(_inspectable.IInspectable):
    get_IsCompact: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsCompact: _Callable[[_type.boolean],  # value
                             _type.HRESULT]


class ICommandBarElement2(_inspectable.IInspectable):
    get_IsInOverflow: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_DynamicOverflowOrder: _Callable[[_Pointer[_type.INT32]],  # value
                                        _type.HRESULT]
    put_DynamicOverflowOrder: _Callable[[_type.INT32],  # value
                                        _type.HRESULT]


class ICommandBarFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ICommandBar]],  # value
                              _type.HRESULT]


class ICommandBarFlyout(_inspectable.IInspectable):
    get_PrimaryCommands: _Callable[[_Pointer[_Windows_Foundation_Collections.IObservableVector[ICommandBarElement]]],  # value
                                   _type.HRESULT]
    get_SecondaryCommands: _Callable[[_Pointer[_Windows_Foundation_Collections.IObservableVector[ICommandBarElement]]],  # value
                                     _type.HRESULT]


class ICommandBarFlyoutFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ICommandBarFlyout]],  # value
                              _type.HRESULT]


class ICommandBarOverflowPresenter(_inspectable.IInspectable):
    pass


class ICommandBarOverflowPresenterFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ICommandBarOverflowPresenter]],  # value
                              _type.HRESULT]


class ICommandBarStatics(_inspectable.IInspectable):
    get_PrimaryCommandsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_SecondaryCommandsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]

    _factory = True


class ICommandBarStatics2(_inspectable.IInspectable):
    get_CommandBarOverflowPresenterStyleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                            _type.HRESULT]

    _factory = True


class ICommandBarStatics3(_inspectable.IInspectable):
    get_DefaultLabelPositionProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_OverflowButtonVisibilityProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]
    get_IsDynamicOverflowEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]

    _factory = True


class IContainerContentChangingEventArgs(_inspectable.IInspectable):
    get_ItemContainer: _Callable[[_Pointer[_Windows_UI_Xaml_Controls_Primitives.ISelectorItem]],  # value
                                 _type.HRESULT]
    get_InRecycleQueue: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    get_ItemIndex: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]
    get_Item: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                        _type.HRESULT]
    get_Phase: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    RegisterUpdateCallback: _Callable[[_Windows_Foundation.ITypedEventHandler[IListViewBase, IContainerContentChangingEventArgs]],  # callback
                                      _type.HRESULT]
    RegisterUpdateCallbackWithPhase: _Callable[[_type.UINT32,  # callbackPhase
                                                _Windows_Foundation.ITypedEventHandler[IListViewBase, IContainerContentChangingEventArgs]],  # callback
                                               _type.HRESULT]


class IContentControl(_inspectable.IInspectable):
    get_Content: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                           _type.HRESULT]
    put_Content: _Callable[[_inspectable.IInspectable],  # value
                           _type.HRESULT]
    get_ContentTemplate: _Callable[[_Pointer[_Windows_UI_Xaml.IDataTemplate]],  # value
                                   _type.HRESULT]
    put_ContentTemplate: _Callable[[_Windows_UI_Xaml.IDataTemplate],  # value
                                   _type.HRESULT]
    get_ContentTemplateSelector: _Callable[[_Pointer[IDataTemplateSelector]],  # value
                                           _type.HRESULT]
    put_ContentTemplateSelector: _Callable[[IDataTemplateSelector],  # value
                                           _type.HRESULT]
    get_ContentTransitions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Media_Animation.ITransition]]],  # value
                                      _type.HRESULT]
    put_ContentTransitions: _Callable[[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Media_Animation.ITransition]],  # value
                                      _type.HRESULT]


class IContentControl2(_inspectable.IInspectable):
    get_ContentTemplateRoot: _Callable[[_Pointer[_Windows_UI_Xaml.IUIElement]],  # value
                                       _type.HRESULT]


class IContentControlFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IContentControl]],  # value
                              _type.HRESULT]


class IContentControlOverrides(_inspectable.IInspectable):
    OnContentChanged: _Callable[[_inspectable.IInspectable,  # oldContent
                                 _inspectable.IInspectable],  # newContent
                                _type.HRESULT]
    OnContentTemplateChanged: _Callable[[_Windows_UI_Xaml.IDataTemplate,  # oldContentTemplate
                                         _Windows_UI_Xaml.IDataTemplate],  # newContentTemplate
                                        _type.HRESULT]
    OnContentTemplateSelectorChanged: _Callable[[IDataTemplateSelector,  # oldContentTemplateSelector
                                                 IDataTemplateSelector],  # newContentTemplateSelector
                                                _type.HRESULT]


class IContentControlStatics(_inspectable.IInspectable):
    get_ContentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_ContentTemplateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_ContentTemplateSelectorProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_ContentTransitionsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]

    _factory = True


class IContentDialog(_inspectable.IInspectable):
    get_Title: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                         _type.HRESULT]
    put_Title: _Callable[[_inspectable.IInspectable],  # value
                         _type.HRESULT]
    get_TitleTemplate: _Callable[[_Pointer[_Windows_UI_Xaml.IDataTemplate]],  # value
                                 _type.HRESULT]
    put_TitleTemplate: _Callable[[_Windows_UI_Xaml.IDataTemplate],  # value
                                 _type.HRESULT]
    get_FullSizeDesired: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    put_FullSizeDesired: _Callable[[_type.boolean],  # value
                                   _type.HRESULT]
    get_PrimaryButtonText: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    put_PrimaryButtonText: _Callable[[_type.HSTRING],  # value
                                     _type.HRESULT]
    get_SecondaryButtonText: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    put_SecondaryButtonText: _Callable[[_type.HSTRING],  # value
                                       _type.HRESULT]
    get_PrimaryButtonCommand: _Callable[[_Pointer[_Windows_UI_Xaml_Input.ICommand]],  # value
                                        _type.HRESULT]
    put_PrimaryButtonCommand: _Callable[[_Windows_UI_Xaml_Input.ICommand],  # value
                                        _type.HRESULT]
    get_SecondaryButtonCommand: _Callable[[_Pointer[_Windows_UI_Xaml_Input.ICommand]],  # value
                                          _type.HRESULT]
    put_SecondaryButtonCommand: _Callable[[_Windows_UI_Xaml_Input.ICommand],  # value
                                          _type.HRESULT]
    get_PrimaryButtonCommandParameter: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                                 _type.HRESULT]
    put_PrimaryButtonCommandParameter: _Callable[[_inspectable.IInspectable],  # value
                                                 _type.HRESULT]
    get_SecondaryButtonCommandParameter: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                                   _type.HRESULT]
    put_SecondaryButtonCommandParameter: _Callable[[_inspectable.IInspectable],  # value
                                                   _type.HRESULT]
    get_IsPrimaryButtonEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_IsPrimaryButtonEnabled: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    get_IsSecondaryButtonEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_IsSecondaryButtonEnabled: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]
    add_Closing: _Callable[[_Windows_Foundation.ITypedEventHandler[IContentDialog, IContentDialogClosingEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Closing: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_Closed: _Callable[[_Windows_Foundation.ITypedEventHandler[IContentDialog, IContentDialogClosedEventArgs],  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Closed: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    add_Opened: _Callable[[_Windows_Foundation.ITypedEventHandler[IContentDialog, IContentDialogOpenedEventArgs],  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Opened: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    add_PrimaryButtonClick: _Callable[[_Windows_Foundation.ITypedEventHandler[IContentDialog, IContentDialogButtonClickEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_PrimaryButtonClick: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_SecondaryButtonClick: _Callable[[_Windows_Foundation.ITypedEventHandler[IContentDialog, IContentDialogButtonClickEventArgs],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_SecondaryButtonClick: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    Hide: _Callable[[],
                    _type.HRESULT]
    ShowAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.UI.Xaml.Controls.ContentDialogResult]]],  # operation
                         _type.HRESULT]


class IContentDialog2(_inspectable.IInspectable):
    get_CloseButtonText: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    put_CloseButtonText: _Callable[[_type.HSTRING],  # value
                                   _type.HRESULT]
    get_CloseButtonCommand: _Callable[[_Pointer[_Windows_UI_Xaml_Input.ICommand]],  # value
                                      _type.HRESULT]
    put_CloseButtonCommand: _Callable[[_Windows_UI_Xaml_Input.ICommand],  # value
                                      _type.HRESULT]
    get_CloseButtonCommandParameter: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                               _type.HRESULT]
    put_CloseButtonCommandParameter: _Callable[[_inspectable.IInspectable],  # value
                                               _type.HRESULT]
    get_PrimaryButtonStyle: _Callable[[_Pointer[_Windows_UI_Xaml.IStyle]],  # value
                                      _type.HRESULT]
    put_PrimaryButtonStyle: _Callable[[_Windows_UI_Xaml.IStyle],  # value
                                      _type.HRESULT]
    get_SecondaryButtonStyle: _Callable[[_Pointer[_Windows_UI_Xaml.IStyle]],  # value
                                        _type.HRESULT]
    put_SecondaryButtonStyle: _Callable[[_Windows_UI_Xaml.IStyle],  # value
                                        _type.HRESULT]
    get_CloseButtonStyle: _Callable[[_Pointer[_Windows_UI_Xaml.IStyle]],  # value
                                    _type.HRESULT]
    put_CloseButtonStyle: _Callable[[_Windows_UI_Xaml.IStyle],  # value
                                    _type.HRESULT]
    get_DefaultButton: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.ContentDialogButton]],  # value
                                 _type.HRESULT]
    put_DefaultButton: _Callable[[_enum.Windows.UI.Xaml.Controls.ContentDialogButton],  # value
                                 _type.HRESULT]
    add_CloseButtonClick: _Callable[[_Windows_Foundation.ITypedEventHandler[IContentDialog, IContentDialogButtonClickEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_CloseButtonClick: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]


class IContentDialog3(_inspectable.IInspectable):
    ShowAsyncWithPlacement: _Callable[[_enum.Windows.UI.Xaml.Controls.ContentDialogPlacement,  # placement
                                       _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.UI.Xaml.Controls.ContentDialogResult]]],  # operation
                                      _type.HRESULT]


class IContentDialogButtonClickDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class IContentDialogButtonClickEventArgs(_inspectable.IInspectable):
    get_Cancel: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_Cancel: _Callable[[_type.boolean],  # value
                          _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[IContentDialogButtonClickDeferral]],  # result
                           _type.HRESULT]


class IContentDialogClosedEventArgs(_inspectable.IInspectable):
    get_Result: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.ContentDialogResult]],  # value
                          _type.HRESULT]


class IContentDialogClosingDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class IContentDialogClosingEventArgs(_inspectable.IInspectable):
    get_Result: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.ContentDialogResult]],  # value
                          _type.HRESULT]
    get_Cancel: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_Cancel: _Callable[[_type.boolean],  # value
                          _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[IContentDialogClosingDeferral]],  # result
                           _type.HRESULT]


class IContentDialogFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IContentDialog]],  # value
                              _type.HRESULT]


class IContentDialogOpenedEventArgs(_inspectable.IInspectable):
    pass


class IContentDialogStatics(_inspectable.IInspectable):
    get_TitleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_TitleTemplateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_FullSizeDesiredProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_PrimaryButtonTextProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_SecondaryButtonTextProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_PrimaryButtonCommandProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_SecondaryButtonCommandProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]
    get_PrimaryButtonCommandParameterProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                         _type.HRESULT]
    get_SecondaryButtonCommandParameterProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                           _type.HRESULT]
    get_IsPrimaryButtonEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]
    get_IsSecondaryButtonEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]

    _factory = True


class IContentDialogStatics2(_inspectable.IInspectable):
    get_CloseButtonTextProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_CloseButtonCommandProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_CloseButtonCommandParameterProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]
    get_PrimaryButtonStyleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_SecondaryButtonStyleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_CloseButtonStyleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_DefaultButtonProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]

    _factory = True


class IContentLinkChangedEventArgs(_inspectable.IInspectable):
    get_ChangeKind: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.ContentLinkChangeKind]],  # value
                              _type.HRESULT]
    get_ContentLinkInfo: _Callable[[_Pointer[_Windows_UI_Text.IContentLinkInfo]],  # value
                                   _type.HRESULT]
    get_TextRange: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Documents.TextRange]],  # value
                             _type.HRESULT]


class IContentPresenter(_inspectable.IInspectable):
    get_Content: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                           _type.HRESULT]
    put_Content: _Callable[[_inspectable.IInspectable],  # value
                           _type.HRESULT]
    get_ContentTemplate: _Callable[[_Pointer[_Windows_UI_Xaml.IDataTemplate]],  # value
                                   _type.HRESULT]
    put_ContentTemplate: _Callable[[_Windows_UI_Xaml.IDataTemplate],  # value
                                   _type.HRESULT]
    get_ContentTemplateSelector: _Callable[[_Pointer[IDataTemplateSelector]],  # value
                                           _type.HRESULT]
    put_ContentTemplateSelector: _Callable[[IDataTemplateSelector],  # value
                                           _type.HRESULT]
    get_ContentTransitions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Media_Animation.ITransition]]],  # value
                                      _type.HRESULT]
    put_ContentTransitions: _Callable[[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Media_Animation.ITransition]],  # value
                                      _type.HRESULT]
    get_FontSize: _Callable[[_Pointer[_type.DOUBLE]],  # value
                            _type.HRESULT]
    put_FontSize: _Callable[[_type.DOUBLE],  # value
                            _type.HRESULT]
    get_FontFamily: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IFontFamily]],  # value
                              _type.HRESULT]
    put_FontFamily: _Callable[[_Windows_UI_Xaml_Media.IFontFamily],  # value
                              _type.HRESULT]
    get_FontWeight: _Callable[[_Pointer[_struct.Windows.UI.Text.FontWeight]],  # value
                              _type.HRESULT]
    put_FontWeight: _Callable[[_struct.Windows.UI.Text.FontWeight],  # value
                              _type.HRESULT]
    get_FontStyle: _Callable[[_Pointer[_enum.Windows.UI.Text.FontStyle]],  # value
                             _type.HRESULT]
    put_FontStyle: _Callable[[_enum.Windows.UI.Text.FontStyle],  # value
                             _type.HRESULT]
    get_FontStretch: _Callable[[_Pointer[_enum.Windows.UI.Text.FontStretch]],  # value
                               _type.HRESULT]
    put_FontStretch: _Callable[[_enum.Windows.UI.Text.FontStretch],  # value
                               _type.HRESULT]
    get_CharacterSpacing: _Callable[[_Pointer[_type.INT32]],  # value
                                    _type.HRESULT]
    put_CharacterSpacing: _Callable[[_type.INT32],  # value
                                    _type.HRESULT]
    get_Foreground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                              _type.HRESULT]
    put_Foreground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                              _type.HRESULT]


class IContentPresenter2(_inspectable.IInspectable):
    get_OpticalMarginAlignment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.OpticalMarginAlignment]],  # value
                                          _type.HRESULT]
    put_OpticalMarginAlignment: _Callable[[_enum.Windows.UI.Xaml.OpticalMarginAlignment],  # value
                                          _type.HRESULT]
    get_TextLineBounds: _Callable[[_Pointer[_enum.Windows.UI.Xaml.TextLineBounds]],  # value
                                  _type.HRESULT]
    put_TextLineBounds: _Callable[[_enum.Windows.UI.Xaml.TextLineBounds],  # value
                                  _type.HRESULT]


class IContentPresenter3(_inspectable.IInspectable):
    get_IsTextScaleFactorEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_IsTextScaleFactorEnabled: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]


class IContentPresenter4(_inspectable.IInspectable):
    get_TextWrapping: _Callable[[_Pointer[_enum.Windows.UI.Xaml.TextWrapping]],  # value
                                _type.HRESULT]
    put_TextWrapping: _Callable[[_enum.Windows.UI.Xaml.TextWrapping],  # value
                                _type.HRESULT]
    get_MaxLines: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    put_MaxLines: _Callable[[_type.INT32],  # value
                            _type.HRESULT]
    get_LineStackingStrategy: _Callable[[_Pointer[_enum.Windows.UI.Xaml.LineStackingStrategy]],  # value
                                        _type.HRESULT]
    put_LineStackingStrategy: _Callable[[_enum.Windows.UI.Xaml.LineStackingStrategy],  # value
                                        _type.HRESULT]
    get_LineHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                              _type.HRESULT]
    put_LineHeight: _Callable[[_type.DOUBLE],  # value
                              _type.HRESULT]
    get_BorderBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                               _type.HRESULT]
    put_BorderBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                               _type.HRESULT]
    get_BorderThickness: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                                   _type.HRESULT]
    put_BorderThickness: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                                   _type.HRESULT]
    get_CornerRadius: _Callable[[_Pointer[_struct.Windows.UI.Xaml.CornerRadius]],  # value
                                _type.HRESULT]
    put_CornerRadius: _Callable[[_struct.Windows.UI.Xaml.CornerRadius],  # value
                                _type.HRESULT]
    get_Padding: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                           _type.HRESULT]
    put_Padding: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                           _type.HRESULT]
    get_Background: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                              _type.HRESULT]
    put_Background: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                              _type.HRESULT]
    get_HorizontalContentAlignment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.HorizontalAlignment]],  # value
                                              _type.HRESULT]
    put_HorizontalContentAlignment: _Callable[[_enum.Windows.UI.Xaml.HorizontalAlignment],  # value
                                              _type.HRESULT]
    get_VerticalContentAlignment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.VerticalAlignment]],  # value
                                            _type.HRESULT]
    put_VerticalContentAlignment: _Callable[[_enum.Windows.UI.Xaml.VerticalAlignment],  # value
                                            _type.HRESULT]


class IContentPresenter5(_inspectable.IInspectable):
    get_BackgroundTransition: _Callable[[_Pointer[_Windows_UI_Xaml.IBrushTransition]],  # value
                                        _type.HRESULT]
    put_BackgroundTransition: _Callable[[_Windows_UI_Xaml.IBrushTransition],  # value
                                        _type.HRESULT]
    get_BackgroundSizing: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.BackgroundSizing]],  # value
                                    _type.HRESULT]
    put_BackgroundSizing: _Callable[[_enum.Windows.UI.Xaml.Controls.BackgroundSizing],  # value
                                    _type.HRESULT]


class IContentPresenterFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IContentPresenter]],  # value
                              _type.HRESULT]


class IContentPresenterOverrides(_inspectable.IInspectable):
    OnContentTemplateChanged: _Callable[[_Windows_UI_Xaml.IDataTemplate,  # oldContentTemplate
                                         _Windows_UI_Xaml.IDataTemplate],  # newContentTemplate
                                        _type.HRESULT]
    OnContentTemplateSelectorChanged: _Callable[[IDataTemplateSelector,  # oldContentTemplateSelector
                                                 IDataTemplateSelector],  # newContentTemplateSelector
                                                _type.HRESULT]


class IContentPresenterStatics(_inspectable.IInspectable):
    get_ContentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_ContentTemplateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_ContentTemplateSelectorProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_ContentTransitionsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_FontSizeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_FontFamilyProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_FontWeightProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_FontStyleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_FontStretchProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_CharacterSpacingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_ForegroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]

    _factory = True


class IContentPresenterStatics2(_inspectable.IInspectable):
    get_OpticalMarginAlignmentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]
    get_TextLineBoundsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]

    _factory = True


class IContentPresenterStatics3(_inspectable.IInspectable):
    get_IsTextScaleFactorEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]

    _factory = True


class IContentPresenterStatics4(_inspectable.IInspectable):
    get_TextWrappingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_MaxLinesProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_LineStackingStrategyProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_LineHeightProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_BorderBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_BorderThicknessProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_CornerRadiusProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_PaddingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_BackgroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_HorizontalContentAlignmentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                      _type.HRESULT]
    get_VerticalContentAlignmentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]

    _factory = True


class IContentPresenterStatics5(_inspectable.IInspectable):
    get_BackgroundSizingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]

    _factory = True


class IContextMenuEventArgs(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_CursorLeft: _Callable[[_Pointer[_type.DOUBLE]],  # value
                              _type.HRESULT]
    get_CursorTop: _Callable[[_Pointer[_type.DOUBLE]],  # value
                             _type.HRESULT]


class IControl(_inspectable.IInspectable):
    get_FontSize: _Callable[[_Pointer[_type.DOUBLE]],  # value
                            _type.HRESULT]
    put_FontSize: _Callable[[_type.DOUBLE],  # value
                            _type.HRESULT]
    get_FontFamily: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IFontFamily]],  # value
                              _type.HRESULT]
    put_FontFamily: _Callable[[_Windows_UI_Xaml_Media.IFontFamily],  # value
                              _type.HRESULT]
    get_FontWeight: _Callable[[_Pointer[_struct.Windows.UI.Text.FontWeight]],  # value
                              _type.HRESULT]
    put_FontWeight: _Callable[[_struct.Windows.UI.Text.FontWeight],  # value
                              _type.HRESULT]
    get_FontStyle: _Callable[[_Pointer[_enum.Windows.UI.Text.FontStyle]],  # value
                             _type.HRESULT]
    put_FontStyle: _Callable[[_enum.Windows.UI.Text.FontStyle],  # value
                             _type.HRESULT]
    get_FontStretch: _Callable[[_Pointer[_enum.Windows.UI.Text.FontStretch]],  # value
                               _type.HRESULT]
    put_FontStretch: _Callable[[_enum.Windows.UI.Text.FontStretch],  # value
                               _type.HRESULT]
    get_CharacterSpacing: _Callable[[_Pointer[_type.INT32]],  # value
                                    _type.HRESULT]
    put_CharacterSpacing: _Callable[[_type.INT32],  # value
                                    _type.HRESULT]
    get_Foreground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                              _type.HRESULT]
    put_Foreground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                              _type.HRESULT]
    get_IsTabStop: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsTabStop: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsEnabled: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    get_TabIndex: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    put_TabIndex: _Callable[[_type.INT32],  # value
                            _type.HRESULT]
    get_TabNavigation: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Input.KeyboardNavigationMode]],  # value
                                 _type.HRESULT]
    put_TabNavigation: _Callable[[_enum.Windows.UI.Xaml.Input.KeyboardNavigationMode],  # value
                                 _type.HRESULT]
    get_Template: _Callable[[_Pointer[IControlTemplate]],  # value
                            _type.HRESULT]
    put_Template: _Callable[[IControlTemplate],  # value
                            _type.HRESULT]
    get_Padding: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                           _type.HRESULT]
    put_Padding: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                           _type.HRESULT]
    get_HorizontalContentAlignment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.HorizontalAlignment]],  # value
                                              _type.HRESULT]
    put_HorizontalContentAlignment: _Callable[[_enum.Windows.UI.Xaml.HorizontalAlignment],  # value
                                              _type.HRESULT]
    get_VerticalContentAlignment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.VerticalAlignment]],  # value
                                            _type.HRESULT]
    put_VerticalContentAlignment: _Callable[[_enum.Windows.UI.Xaml.VerticalAlignment],  # value
                                            _type.HRESULT]
    get_Background: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                              _type.HRESULT]
    put_Background: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                              _type.HRESULT]
    get_BorderThickness: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                                   _type.HRESULT]
    put_BorderThickness: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                                   _type.HRESULT]
    get_BorderBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                               _type.HRESULT]
    put_BorderBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                               _type.HRESULT]
    get_FocusState: _Callable[[_Pointer[_enum.Windows.UI.Xaml.FocusState]],  # value
                              _type.HRESULT]
    add_IsEnabledChanged: _Callable[[_Windows_UI_Xaml.IDependencyPropertyChangedEventHandler,  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_IsEnabledChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    ApplyTemplate: _Callable[[_Pointer[_type.boolean]],  # result
                             _type.HRESULT]
    Focus: _Callable[[_enum.Windows.UI.Xaml.FocusState,  # value
                      _Pointer[_type.boolean]],  # result
                     _type.HRESULT]


class IControl2(_inspectable.IInspectable):
    get_IsTextScaleFactorEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_IsTextScaleFactorEnabled: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]


class IControl3(_inspectable.IInspectable):
    get_UseSystemFocusVisuals: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_UseSystemFocusVisuals: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]


class IControl4(_inspectable.IInspectable):
    get_IsFocusEngagementEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_IsFocusEngagementEnabled: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]
    get_IsFocusEngaged: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    put_IsFocusEngaged: _Callable[[_type.boolean],  # value
                                  _type.HRESULT]
    get_RequiresPointer: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.RequiresPointer]],  # value
                                   _type.HRESULT]
    put_RequiresPointer: _Callable[[_enum.Windows.UI.Xaml.Controls.RequiresPointer],  # value
                                   _type.HRESULT]
    get_XYFocusLeft: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyObject]],  # value
                               _type.HRESULT]
    put_XYFocusLeft: _Callable[[_Windows_UI_Xaml.IDependencyObject],  # value
                               _type.HRESULT]
    get_XYFocusRight: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyObject]],  # value
                                _type.HRESULT]
    put_XYFocusRight: _Callable[[_Windows_UI_Xaml.IDependencyObject],  # value
                                _type.HRESULT]
    get_XYFocusUp: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyObject]],  # value
                             _type.HRESULT]
    put_XYFocusUp: _Callable[[_Windows_UI_Xaml.IDependencyObject],  # value
                             _type.HRESULT]
    get_XYFocusDown: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyObject]],  # value
                               _type.HRESULT]
    put_XYFocusDown: _Callable[[_Windows_UI_Xaml.IDependencyObject],  # value
                               _type.HRESULT]
    get_ElementSoundMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.ElementSoundMode]],  # value
                                    _type.HRESULT]
    put_ElementSoundMode: _Callable[[_enum.Windows.UI.Xaml.ElementSoundMode],  # value
                                    _type.HRESULT]
    add_FocusEngaged: _Callable[[_Windows_Foundation.ITypedEventHandler[IControl, IFocusEngagedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_FocusEngaged: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    add_FocusDisengaged: _Callable[[_Windows_Foundation.ITypedEventHandler[IControl, IFocusDisengagedEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_FocusDisengaged: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    RemoveFocusEngagement: _Callable[[],
                                     _type.HRESULT]


class IControl5(_inspectable.IInspectable):
    get_DefaultStyleResourceUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                           _type.HRESULT]
    put_DefaultStyleResourceUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                                           _type.HRESULT]


class IControl7(_inspectable.IInspectable):
    get_BackgroundSizing: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.BackgroundSizing]],  # value
                                    _type.HRESULT]
    put_BackgroundSizing: _Callable[[_enum.Windows.UI.Xaml.Controls.BackgroundSizing],  # value
                                    _type.HRESULT]
    get_CornerRadius: _Callable[[_Pointer[_struct.Windows.UI.Xaml.CornerRadius]],  # value
                                _type.HRESULT]
    put_CornerRadius: _Callable[[_struct.Windows.UI.Xaml.CornerRadius],  # value
                                _type.HRESULT]


class IControlFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IControl]],  # value
                              _type.HRESULT]


class IControlOverrides(_inspectable.IInspectable):
    OnPointerEntered: _Callable[[_Windows_UI_Xaml_Input.IPointerRoutedEventArgs],  # e
                                _type.HRESULT]
    OnPointerPressed: _Callable[[_Windows_UI_Xaml_Input.IPointerRoutedEventArgs],  # e
                                _type.HRESULT]
    OnPointerMoved: _Callable[[_Windows_UI_Xaml_Input.IPointerRoutedEventArgs],  # e
                              _type.HRESULT]
    OnPointerReleased: _Callable[[_Windows_UI_Xaml_Input.IPointerRoutedEventArgs],  # e
                                 _type.HRESULT]
    OnPointerExited: _Callable[[_Windows_UI_Xaml_Input.IPointerRoutedEventArgs],  # e
                               _type.HRESULT]
    OnPointerCaptureLost: _Callable[[_Windows_UI_Xaml_Input.IPointerRoutedEventArgs],  # e
                                    _type.HRESULT]
    OnPointerCanceled: _Callable[[_Windows_UI_Xaml_Input.IPointerRoutedEventArgs],  # e
                                 _type.HRESULT]
    OnPointerWheelChanged: _Callable[[_Windows_UI_Xaml_Input.IPointerRoutedEventArgs],  # e
                                     _type.HRESULT]
    OnTapped: _Callable[[_Windows_UI_Xaml_Input.ITappedRoutedEventArgs],  # e
                        _type.HRESULT]
    OnDoubleTapped: _Callable[[_Windows_UI_Xaml_Input.IDoubleTappedRoutedEventArgs],  # e
                              _type.HRESULT]
    OnHolding: _Callable[[_Windows_UI_Xaml_Input.IHoldingRoutedEventArgs],  # e
                         _type.HRESULT]
    OnRightTapped: _Callable[[_Windows_UI_Xaml_Input.IRightTappedRoutedEventArgs],  # e
                             _type.HRESULT]
    OnManipulationStarting: _Callable[[_Windows_UI_Xaml_Input.IManipulationStartingRoutedEventArgs],  # e
                                      _type.HRESULT]
    OnManipulationInertiaStarting: _Callable[[_Windows_UI_Xaml_Input.IManipulationInertiaStartingRoutedEventArgs],  # e
                                             _type.HRESULT]
    OnManipulationStarted: _Callable[[_Windows_UI_Xaml_Input.IManipulationStartedRoutedEventArgs],  # e
                                     _type.HRESULT]
    OnManipulationDelta: _Callable[[_Windows_UI_Xaml_Input.IManipulationDeltaRoutedEventArgs],  # e
                                   _type.HRESULT]
    OnManipulationCompleted: _Callable[[_Windows_UI_Xaml_Input.IManipulationCompletedRoutedEventArgs],  # e
                                       _type.HRESULT]
    OnKeyUp: _Callable[[_Windows_UI_Xaml_Input.IKeyRoutedEventArgs],  # e
                       _type.HRESULT]
    OnKeyDown: _Callable[[_Windows_UI_Xaml_Input.IKeyRoutedEventArgs],  # e
                         _type.HRESULT]
    OnGotFocus: _Callable[[_Windows_UI_Xaml.IRoutedEventArgs],  # e
                          _type.HRESULT]
    OnLostFocus: _Callable[[_Windows_UI_Xaml.IRoutedEventArgs],  # e
                           _type.HRESULT]
    OnDragEnter: _Callable[[_Windows_UI_Xaml.IDragEventArgs],  # e
                           _type.HRESULT]
    OnDragLeave: _Callable[[_Windows_UI_Xaml.IDragEventArgs],  # e
                           _type.HRESULT]
    OnDragOver: _Callable[[_Windows_UI_Xaml.IDragEventArgs],  # e
                          _type.HRESULT]
    OnDrop: _Callable[[_Windows_UI_Xaml.IDragEventArgs],  # e
                      _type.HRESULT]


class IControlOverrides6(_inspectable.IInspectable):
    OnPreviewKeyDown: _Callable[[_Windows_UI_Xaml_Input.IKeyRoutedEventArgs],  # e
                                _type.HRESULT]
    OnPreviewKeyUp: _Callable[[_Windows_UI_Xaml_Input.IKeyRoutedEventArgs],  # e
                              _type.HRESULT]
    OnCharacterReceived: _Callable[[_Windows_UI_Xaml_Input.ICharacterReceivedRoutedEventArgs],  # e
                                   _type.HRESULT]


class IControlProtected(_inspectable.IInspectable):
    get_DefaultStyleKey: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                   _type.HRESULT]
    put_DefaultStyleKey: _Callable[[_inspectable.IInspectable],  # value
                                   _type.HRESULT]
    GetTemplateChild: _Callable[[_type.HSTRING,  # childName
                                 _Pointer[_Windows_UI_Xaml.IDependencyObject]],  # result
                                _type.HRESULT]


class IControlStatics(_inspectable.IInspectable):
    get_FontSizeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_FontFamilyProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_FontWeightProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_FontStyleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_FontStretchProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_CharacterSpacingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_ForegroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_IsTabStopProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_IsEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_TabIndexProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_TabNavigationProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_TemplateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_PaddingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_HorizontalContentAlignmentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                      _type.HRESULT]
    get_VerticalContentAlignmentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]
    get_BackgroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_BorderThicknessProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_BorderBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_DefaultStyleKeyProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_FocusStateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]

    _factory = True


class IControlStatics2(_inspectable.IInspectable):
    get_IsTextScaleFactorEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]

    _factory = True


class IControlStatics3(_inspectable.IInspectable):
    get_UseSystemFocusVisualsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_IsTemplateFocusTargetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    GetIsTemplateFocusTarget: _Callable[[_Windows_UI_Xaml.IFrameworkElement,  # element
                                         _Pointer[_type.boolean]],  # result
                                        _type.HRESULT]
    SetIsTemplateFocusTarget: _Callable[[_Windows_UI_Xaml.IFrameworkElement,  # element
                                         _type.boolean],  # value
                                        _type.HRESULT]

    _factory = True


class IControlStatics4(_inspectable.IInspectable):
    get_IsFocusEngagementEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]
    get_IsFocusEngagedProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_RequiresPointerProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_XYFocusLeftProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_XYFocusRightProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_XYFocusUpProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_XYFocusDownProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_ElementSoundModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]

    _factory = True


class IControlStatics5(_inspectable.IInspectable):
    get_DefaultStyleResourceUriProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_IsTemplateKeyTipTargetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]
    GetIsTemplateKeyTipTarget: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                          _Pointer[_type.boolean]],  # result
                                         _type.HRESULT]
    SetIsTemplateKeyTipTarget: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                          _type.boolean],  # value
                                         _type.HRESULT]

    _factory = True


class IControlStatics7(_inspectable.IInspectable):
    get_BackgroundSizingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_CornerRadiusProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]

    _factory = True


class IControlTemplate(_inspectable.IInspectable):
    get_TargetType: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Interop.TypeName]],  # value
                              _type.HRESULT]
    put_TargetType: _Callable[[_struct.Windows.UI.Xaml.Interop.TypeName],  # value
                              _type.HRESULT]


class IDataTemplateSelector(_inspectable.IInspectable):
    SelectTemplate: _Callable[[_inspectable.IInspectable,  # item
                               _Windows_UI_Xaml.IDependencyObject,  # container
                               _Pointer[_Windows_UI_Xaml.IDataTemplate]],  # result
                              _type.HRESULT]


class IDataTemplateSelector2(_inspectable.IInspectable):
    SelectTemplateForItem: _Callable[[_inspectable.IInspectable,  # item
                                      _Pointer[_Windows_UI_Xaml.IDataTemplate]],  # result
                                     _type.HRESULT]


class IDataTemplateSelectorFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IDataTemplateSelector]],  # value
                              _type.HRESULT]


class IDataTemplateSelectorOverrides(_inspectable.IInspectable):
    SelectTemplateCore: _Callable[[_inspectable.IInspectable,  # item
                                   _Windows_UI_Xaml.IDependencyObject,  # container
                                   _Pointer[_Windows_UI_Xaml.IDataTemplate]],  # result
                                  _type.HRESULT]


class IDataTemplateSelectorOverrides2(_inspectable.IInspectable):
    SelectTemplateForItemCore: _Callable[[_inspectable.IInspectable,  # item
                                          _Pointer[_Windows_UI_Xaml.IDataTemplate]],  # result
                                         _type.HRESULT]


class IDatePickedEventArgs(_inspectable.IInspectable):
    get_OldDate: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                           _type.HRESULT]
    get_NewDate: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                           _type.HRESULT]


class IDatePicker(_inspectable.IInspectable):
    get_Header: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                          _type.HRESULT]
    put_Header: _Callable[[_inspectable.IInspectable],  # value
                          _type.HRESULT]
    get_HeaderTemplate: _Callable[[_Pointer[_Windows_UI_Xaml.IDataTemplate]],  # value
                                  _type.HRESULT]
    put_HeaderTemplate: _Callable[[_Windows_UI_Xaml.IDataTemplate],  # value
                                  _type.HRESULT]
    get_CalendarIdentifier: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    put_CalendarIdentifier: _Callable[[_type.HSTRING],  # value
                                      _type.HRESULT]
    get_Date: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                        _type.HRESULT]
    put_Date: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                        _type.HRESULT]
    get_DayVisible: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    put_DayVisible: _Callable[[_type.boolean],  # value
                              _type.HRESULT]
    get_MonthVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_MonthVisible: _Callable[[_type.boolean],  # value
                                _type.HRESULT]
    get_YearVisible: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    put_YearVisible: _Callable[[_type.boolean],  # value
                               _type.HRESULT]
    get_DayFormat: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_DayFormat: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_MonthFormat: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_MonthFormat: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_YearFormat: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_YearFormat: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]
    get_MinYear: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                           _type.HRESULT]
    put_MinYear: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                           _type.HRESULT]
    get_MaxYear: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                           _type.HRESULT]
    put_MaxYear: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                           _type.HRESULT]
    get_Orientation: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Orientation]],  # value
                               _type.HRESULT]
    put_Orientation: _Callable[[_enum.Windows.UI.Xaml.Controls.Orientation],  # value
                               _type.HRESULT]
    add_DateChanged: _Callable[[_Windows_Foundation.IEventHandler[IDatePickerValueChangedEventArgs],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_DateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]


class IDatePicker2(_inspectable.IInspectable):
    get_LightDismissOverlayMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.LightDismissOverlayMode]],  # value
                                           _type.HRESULT]
    put_LightDismissOverlayMode: _Callable[[_enum.Windows.UI.Xaml.Controls.LightDismissOverlayMode],  # value
                                           _type.HRESULT]


class IDatePicker3(_inspectable.IInspectable):
    get_SelectedDate: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                _type.HRESULT]
    put_SelectedDate: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                                _type.HRESULT]
    add_SelectedDateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IDatePicker, IDatePickerSelectedValueChangedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_SelectedDateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]


class IDatePickerFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IDatePicker]],  # value
                              _type.HRESULT]


class IDatePickerFlyout(_inspectable.IInspectable):
    get_CalendarIdentifier: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    put_CalendarIdentifier: _Callable[[_type.HSTRING],  # value
                                      _type.HRESULT]
    get_Date: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                        _type.HRESULT]
    put_Date: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                        _type.HRESULT]
    get_DayVisible: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    put_DayVisible: _Callable[[_type.boolean],  # value
                              _type.HRESULT]
    get_MonthVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_MonthVisible: _Callable[[_type.boolean],  # value
                                _type.HRESULT]
    get_YearVisible: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    put_YearVisible: _Callable[[_type.boolean],  # value
                               _type.HRESULT]
    get_MinYear: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                           _type.HRESULT]
    put_MinYear: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                           _type.HRESULT]
    get_MaxYear: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                           _type.HRESULT]
    put_MaxYear: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                           _type.HRESULT]
    add_DatePicked: _Callable[[_Windows_Foundation.ITypedEventHandler[IDatePickerFlyout, IDatePickedEventArgs],  # handler
                               _Pointer[_struct.EventRegistrationToken]],  # token
                              _type.HRESULT]
    remove_DatePicked: _Callable[[_struct.EventRegistrationToken],  # token
                                 _type.HRESULT]
    ShowAtAsync: _Callable[[_Windows_UI_Xaml.IFrameworkElement,  # target
                            _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]]],  # operation
                           _type.HRESULT]


class IDatePickerFlyout2(_inspectable.IInspectable):
    get_DayFormat: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_DayFormat: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_MonthFormat: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_MonthFormat: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_YearFormat: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_YearFormat: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]


class IDatePickerFlyoutItem(_inspectable.IInspectable):
    get_PrimaryText: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_PrimaryText: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_SecondaryText: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    put_SecondaryText: _Callable[[_type.HSTRING],  # value
                                 _type.HRESULT]


class IDatePickerFlyoutItemStatics(_inspectable.IInspectable):
    get_PrimaryTextProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_SecondaryTextProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]

    _factory = True


class IDatePickerFlyoutPresenter(_inspectable.IInspectable):
    pass


class IDatePickerFlyoutPresenter2(_inspectable.IInspectable):
    get_IsDefaultShadowEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_IsDefaultShadowEnabled: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]


class IDatePickerFlyoutPresenterStatics2(_inspectable.IInspectable):
    get_IsDefaultShadowEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]

    _factory = True


class IDatePickerFlyoutStatics(_inspectable.IInspectable):
    get_CalendarIdentifierProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_DateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]
    get_DayVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_MonthVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_YearVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_MinYearProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_MaxYearProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]

    _factory = True


class IDatePickerFlyoutStatics2(_inspectable.IInspectable):
    get_DayFormatProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_MonthFormatProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_YearFormatProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]

    _factory = True


class IDatePickerSelectedValueChangedEventArgs(_inspectable.IInspectable):
    get_OldDate: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                           _type.HRESULT]
    get_NewDate: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                           _type.HRESULT]


class IDatePickerStatics(_inspectable.IInspectable):
    get_HeaderProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_HeaderTemplateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_CalendarIdentifierProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_DateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]
    get_DayVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_MonthVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_YearVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_DayFormatProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_MonthFormatProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_YearFormatProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_MinYearProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_MaxYearProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_OrientationProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]

    _factory = True


class IDatePickerStatics2(_inspectable.IInspectable):
    get_LightDismissOverlayModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]

    _factory = True


class IDatePickerStatics3(_inspectable.IInspectable):
    get_SelectedDateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]

    _factory = True


class IDatePickerValueChangedEventArgs(_inspectable.IInspectable):
    get_OldDate: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                           _type.HRESULT]
    get_NewDate: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                           _type.HRESULT]


class IDragItemsCompletedEventArgs(_inspectable.IInspectable):
    get_Items: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_inspectable.IInspectable]]],  # value
                         _type.HRESULT]
    get_DropResult: _Callable[[_Pointer[_enum.Windows.ApplicationModel.DataTransfer.DataPackageOperation]],  # value
                              _type.HRESULT]


class IDragItemsStartingEventArgs(_inspectable.IInspectable):
    get_Cancel: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_Cancel: _Callable[[_type.boolean],  # value
                          _type.HRESULT]
    get_Items: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_inspectable.IInspectable]]],  # value
                         _type.HRESULT]
    get_Data: _Callable[[_Pointer[_Windows_ApplicationModel_DataTransfer.IDataPackage]],  # value
                        _type.HRESULT]


class IDropDownButton(_inspectable.IInspectable):
    pass


class IDropDownButtonAutomationPeer(_inspectable.IInspectable):
    pass


class IDropDownButtonAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[IDropDownButton,  # owner
                               _inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IDropDownButtonAutomationPeer]],  # value
                              _type.HRESULT]


class IDropDownButtonFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IDropDownButton]],  # value
                              _type.HRESULT]


class IDynamicOverflowItemsChangingEventArgs(_inspectable.IInspectable):
    get_Action: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.CommandBarDynamicOverflowAction]],  # value
                          _type.HRESULT]


class IFlipView(_inspectable.IInspectable):
    pass


class IFlipView2(_inspectable.IInspectable):
    get_UseTouchAnimationsForAllNavigation: _Callable[[_Pointer[_type.boolean]],  # value
                                                      _type.HRESULT]
    put_UseTouchAnimationsForAllNavigation: _Callable[[_type.boolean],  # value
                                                      _type.HRESULT]


class IFlipViewFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IFlipView]],  # value
                              _type.HRESULT]


class IFlipViewItem(_inspectable.IInspectable):
    pass


class IFlipViewItemFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IFlipViewItem]],  # value
                              _type.HRESULT]


class IFlipViewStatics2(_inspectable.IInspectable):
    get_UseTouchAnimationsForAllNavigationProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                              _type.HRESULT]

    _factory = True


class IFlyout(_inspectable.IInspectable):
    get_Content: _Callable[[_Pointer[_Windows_UI_Xaml.IUIElement]],  # value
                           _type.HRESULT]
    put_Content: _Callable[[_Windows_UI_Xaml.IUIElement],  # value
                           _type.HRESULT]
    get_FlyoutPresenterStyle: _Callable[[_Pointer[_Windows_UI_Xaml.IStyle]],  # value
                                        _type.HRESULT]
    put_FlyoutPresenterStyle: _Callable[[_Windows_UI_Xaml.IStyle],  # value
                                        _type.HRESULT]


class IFlyoutFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IFlyout]],  # value
                              _type.HRESULT]


class IFlyoutPresenter(_inspectable.IInspectable):
    pass


class IFlyoutPresenter2(_inspectable.IInspectable):
    get_IsDefaultShadowEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_IsDefaultShadowEnabled: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]


class IFlyoutPresenterFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IFlyoutPresenter]],  # value
                              _type.HRESULT]


class IFlyoutPresenterStatics2(_inspectable.IInspectable):
    get_IsDefaultShadowEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]

    _factory = True


class IFlyoutStatics(_inspectable.IInspectable):
    get_ContentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_FlyoutPresenterStyleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]

    _factory = True


class IFocusDisengagedEventArgs(_inspectable.IInspectable):
    pass


class IFocusEngagedEventArgs(_inspectable.IInspectable):
    pass


class IFocusEngagedEventArgs2(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class IFontIcon(_inspectable.IInspectable):
    get_Glyph: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Glyph: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_FontSize: _Callable[[_Pointer[_type.DOUBLE]],  # value
                            _type.HRESULT]
    put_FontSize: _Callable[[_type.DOUBLE],  # value
                            _type.HRESULT]
    get_FontFamily: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IFontFamily]],  # value
                              _type.HRESULT]
    put_FontFamily: _Callable[[_Windows_UI_Xaml_Media.IFontFamily],  # value
                              _type.HRESULT]
    get_FontWeight: _Callable[[_Pointer[_struct.Windows.UI.Text.FontWeight]],  # value
                              _type.HRESULT]
    put_FontWeight: _Callable[[_struct.Windows.UI.Text.FontWeight],  # value
                              _type.HRESULT]
    get_FontStyle: _Callable[[_Pointer[_enum.Windows.UI.Text.FontStyle]],  # value
                             _type.HRESULT]
    put_FontStyle: _Callable[[_enum.Windows.UI.Text.FontStyle],  # value
                             _type.HRESULT]


class IFontIcon2(_inspectable.IInspectable):
    get_IsTextScaleFactorEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_IsTextScaleFactorEnabled: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]


class IFontIcon3(_inspectable.IInspectable):
    get_MirroredWhenRightToLeft: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    put_MirroredWhenRightToLeft: _Callable[[_type.boolean],  # value
                                           _type.HRESULT]


class IFontIconFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IFontIcon]],  # value
                              _type.HRESULT]


class IFontIconSource(_inspectable.IInspectable):
    get_Glyph: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Glyph: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_FontSize: _Callable[[_Pointer[_type.DOUBLE]],  # value
                            _type.HRESULT]
    put_FontSize: _Callable[[_type.DOUBLE],  # value
                            _type.HRESULT]
    get_FontFamily: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IFontFamily]],  # value
                              _type.HRESULT]
    put_FontFamily: _Callable[[_Windows_UI_Xaml_Media.IFontFamily],  # value
                              _type.HRESULT]
    get_FontWeight: _Callable[[_Pointer[_struct.Windows.UI.Text.FontWeight]],  # value
                              _type.HRESULT]
    put_FontWeight: _Callable[[_struct.Windows.UI.Text.FontWeight],  # value
                              _type.HRESULT]
    get_FontStyle: _Callable[[_Pointer[_enum.Windows.UI.Text.FontStyle]],  # value
                             _type.HRESULT]
    put_FontStyle: _Callable[[_enum.Windows.UI.Text.FontStyle],  # value
                             _type.HRESULT]
    get_IsTextScaleFactorEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_IsTextScaleFactorEnabled: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]
    get_MirroredWhenRightToLeft: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    put_MirroredWhenRightToLeft: _Callable[[_type.boolean],  # value
                                           _type.HRESULT]


class IFontIconSourceFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IFontIconSource]],  # value
                              _type.HRESULT]


class IFontIconSourceStatics(_inspectable.IInspectable):
    get_GlyphProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_FontSizeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_FontFamilyProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_FontWeightProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_FontStyleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_IsTextScaleFactorEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]
    get_MirroredWhenRightToLeftProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]

    _factory = True


class IFontIconStatics(_inspectable.IInspectable):
    get_GlyphProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_FontSizeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_FontFamilyProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_FontWeightProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_FontStyleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]

    _factory = True


class IFontIconStatics2(_inspectable.IInspectable):
    get_IsTextScaleFactorEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]

    _factory = True


class IFontIconStatics3(_inspectable.IInspectable):
    get_MirroredWhenRightToLeftProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]

    _factory = True


class IFrame(_inspectable.IInspectable):
    get_CacheSize: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]
    put_CacheSize: _Callable[[_type.INT32],  # value
                             _type.HRESULT]
    get_CanGoBack: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_CanGoForward: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_CurrentSourcePageType: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Interop.TypeName]],  # value
                                         _type.HRESULT]
    get_SourcePageType: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Interop.TypeName]],  # value
                                  _type.HRESULT]
    put_SourcePageType: _Callable[[_struct.Windows.UI.Xaml.Interop.TypeName],  # value
                                  _type.HRESULT]
    get_BackStackDepth: _Callable[[_Pointer[_type.INT32]],  # value
                                  _type.HRESULT]
    add_Navigated: _Callable[[_Windows_UI_Xaml_Navigation.INavigatedEventHandler,  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_Navigated: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    add_Navigating: _Callable[[_Windows_UI_Xaml_Navigation.INavigatingCancelEventHandler,  # handler
                               _Pointer[_struct.EventRegistrationToken]],  # token
                              _type.HRESULT]
    remove_Navigating: _Callable[[_struct.EventRegistrationToken],  # token
                                 _type.HRESULT]
    add_NavigationFailed: _Callable[[_Windows_UI_Xaml_Navigation.INavigationFailedEventHandler,  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_NavigationFailed: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    add_NavigationStopped: _Callable[[_Windows_UI_Xaml_Navigation.INavigationStoppedEventHandler,  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_NavigationStopped: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    GoBack: _Callable[[],
                      _type.HRESULT]
    GoForward: _Callable[[],
                         _type.HRESULT]
    Navigate: _Callable[[_struct.Windows.UI.Xaml.Interop.TypeName,  # sourcePageType
                         _inspectable.IInspectable,  # parameter
                         _Pointer[_type.boolean]],  # result
                        _type.HRESULT]
    GetNavigationState: _Callable[[_Pointer[_type.HSTRING]],  # result
                                  _type.HRESULT]
    SetNavigationState: _Callable[[_type.HSTRING],  # navigationState
                                  _type.HRESULT]


class IFrame2(_inspectable.IInspectable):
    get_BackStack: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Navigation.IPageStackEntry]]],  # value
                             _type.HRESULT]
    get_ForwardStack: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Navigation.IPageStackEntry]]],  # value
                                _type.HRESULT]
    Navigate: _Callable[[_struct.Windows.UI.Xaml.Interop.TypeName,  # sourcePageType
                         _inspectable.IInspectable,  # parameter
                         _Windows_UI_Xaml_Media_Animation.INavigationTransitionInfo,  # infoOverride
                         _Pointer[_type.boolean]],  # result
                        _type.HRESULT]


class IFrame3(_inspectable.IInspectable):
    GoBack: _Callable[[_Windows_UI_Xaml_Media_Animation.INavigationTransitionInfo],  # transitionInfoOverride
                      _type.HRESULT]


class IFrame4(_inspectable.IInspectable):
    SetNavigationStateWithNavigationControl: _Callable[[_type.HSTRING,  # navigationState
                                                        _type.boolean],  # suppressNavigate
                                                       _type.HRESULT]


class IFrame5(_inspectable.IInspectable):
    get_IsNavigationStackEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_IsNavigationStackEnabled: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]
    NavigateToType: _Callable[[_struct.Windows.UI.Xaml.Interop.TypeName,  # sourcePageType
                               _inspectable.IInspectable,  # parameter
                               _Windows_UI_Xaml_Navigation.IFrameNavigationOptions,  # navigationOptions
                               _Pointer[_type.boolean]],  # result
                              _type.HRESULT]


class IFrameFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IFrame]],  # value
                              _type.HRESULT]


class IFrameStatics(_inspectable.IInspectable):
    get_CacheSizeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_CanGoBackProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_CanGoForwardProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_CurrentSourcePageTypeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_SourcePageTypeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_BackStackDepthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]

    _factory = True


class IFrameStatics2(_inspectable.IInspectable):
    get_BackStackProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_ForwardStackProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]

    _factory = True


class IFrameStatics5(_inspectable.IInspectable):
    get_IsNavigationStackEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]

    _factory = True


class IGrid(_inspectable.IInspectable):
    get_RowDefinitions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IRowDefinition]]],  # value
                                  _type.HRESULT]
    get_ColumnDefinitions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IColumnDefinition]]],  # value
                                     _type.HRESULT]


class IGrid2(_inspectable.IInspectable):
    get_BorderBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                               _type.HRESULT]
    put_BorderBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                               _type.HRESULT]
    get_BorderThickness: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                                   _type.HRESULT]
    put_BorderThickness: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                                   _type.HRESULT]
    get_CornerRadius: _Callable[[_Pointer[_struct.Windows.UI.Xaml.CornerRadius]],  # value
                                _type.HRESULT]
    put_CornerRadius: _Callable[[_struct.Windows.UI.Xaml.CornerRadius],  # value
                                _type.HRESULT]
    get_Padding: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                           _type.HRESULT]
    put_Padding: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                           _type.HRESULT]


class IGrid3(_inspectable.IInspectable):
    get_RowSpacing: _Callable[[_Pointer[_type.DOUBLE]],  # value
                              _type.HRESULT]
    put_RowSpacing: _Callable[[_type.DOUBLE],  # value
                              _type.HRESULT]
    get_ColumnSpacing: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                 _type.HRESULT]
    put_ColumnSpacing: _Callable[[_type.DOUBLE],  # value
                                 _type.HRESULT]


class IGrid4(_inspectable.IInspectable):
    get_BackgroundSizing: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.BackgroundSizing]],  # value
                                    _type.HRESULT]
    put_BackgroundSizing: _Callable[[_enum.Windows.UI.Xaml.Controls.BackgroundSizing],  # value
                                    _type.HRESULT]


class IGridFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IGrid]],  # value
                              _type.HRESULT]


class IGridStatics(_inspectable.IInspectable):
    get_RowProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                               _type.HRESULT]
    GetRow: _Callable[[_Windows_UI_Xaml.IFrameworkElement,  # element
                       _Pointer[_type.INT32]],  # result
                      _type.HRESULT]
    SetRow: _Callable[[_Windows_UI_Xaml.IFrameworkElement,  # element
                       _type.INT32],  # value
                      _type.HRESULT]
    get_ColumnProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    GetColumn: _Callable[[_Windows_UI_Xaml.IFrameworkElement,  # element
                          _Pointer[_type.INT32]],  # result
                         _type.HRESULT]
    SetColumn: _Callable[[_Windows_UI_Xaml.IFrameworkElement,  # element
                          _type.INT32],  # value
                         _type.HRESULT]
    get_RowSpanProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    GetRowSpan: _Callable[[_Windows_UI_Xaml.IFrameworkElement,  # element
                           _Pointer[_type.INT32]],  # result
                          _type.HRESULT]
    SetRowSpan: _Callable[[_Windows_UI_Xaml.IFrameworkElement,  # element
                           _type.INT32],  # value
                          _type.HRESULT]
    get_ColumnSpanProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    GetColumnSpan: _Callable[[_Windows_UI_Xaml.IFrameworkElement,  # element
                              _Pointer[_type.INT32]],  # result
                             _type.HRESULT]
    SetColumnSpan: _Callable[[_Windows_UI_Xaml.IFrameworkElement,  # element
                              _type.INT32],  # value
                             _type.HRESULT]

    _factory = True


class IGridStatics2(_inspectable.IInspectable):
    get_BorderBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_BorderThicknessProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_CornerRadiusProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_PaddingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]

    _factory = True


class IGridStatics3(_inspectable.IInspectable):
    get_RowSpacingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_ColumnSpacingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]

    _factory = True


class IGridStatics4(_inspectable.IInspectable):
    get_BackgroundSizingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]

    _factory = True


class IGridView(_inspectable.IInspectable):
    pass


class IGridViewFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IGridView]],  # value
                              _type.HRESULT]


class IGridViewHeaderItem(_inspectable.IInspectable):
    pass


class IGridViewHeaderItemFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IGridViewHeaderItem]],  # value
                              _type.HRESULT]


class IGridViewItem(_inspectable.IInspectable):
    get_TemplateSettings: _Callable[[_Pointer[_Windows_UI_Xaml_Controls_Primitives.IGridViewItemTemplateSettings]],  # value
                                    _type.HRESULT]


class IGridViewItemFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IGridViewItem]],  # value
                              _type.HRESULT]


class IGroupItem(_inspectable.IInspectable):
    pass


class IGroupItemFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IGroupItem]],  # value
                              _type.HRESULT]


class IGroupStyle(_inspectable.IInspectable):
    get_Panel: _Callable[[_Pointer[IItemsPanelTemplate]],  # value
                         _type.HRESULT]
    put_Panel: _Callable[[IItemsPanelTemplate],  # value
                         _type.HRESULT]
    ContainerStyle: _Callable[[_Windows_UI_Xaml.IStyle],  # value
                              _type.HRESULT]
    ContainerStyleSelector: _Callable[[IStyleSelector],  # value
                                      _type.HRESULT]
    get_HeaderTemplate: _Callable[[_Pointer[_Windows_UI_Xaml.IDataTemplate]],  # value
                                  _type.HRESULT]
    put_HeaderTemplate: _Callable[[_Windows_UI_Xaml.IDataTemplate],  # value
                                  _type.HRESULT]
    get_HeaderTemplateSelector: _Callable[[_Pointer[IDataTemplateSelector]],  # value
                                          _type.HRESULT]
    put_HeaderTemplateSelector: _Callable[[IDataTemplateSelector],  # value
                                          _type.HRESULT]
    get_HidesIfEmpty: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_HidesIfEmpty: _Callable[[_type.boolean],  # value
                                _type.HRESULT]


class IGroupStyle2(_inspectable.IInspectable):
    get_HeaderContainerStyle: _Callable[[_Pointer[_Windows_UI_Xaml.IStyle]],  # value
                                        _type.HRESULT]
    put_HeaderContainerStyle: _Callable[[_Windows_UI_Xaml.IStyle],  # value
                                        _type.HRESULT]


class IGroupStyleFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IGroupStyle]],  # value
                              _type.HRESULT]


class IGroupStyleSelector(_inspectable.IInspectable):
    SelectGroupStyle: _Callable[[_inspectable.IInspectable,  # group
                                 _type.UINT32,  # level
                                 _Pointer[IGroupStyle]],  # result
                                _type.HRESULT]


class IGroupStyleSelectorFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IGroupStyleSelector]],  # value
                              _type.HRESULT]


class IGroupStyleSelectorOverrides(_inspectable.IInspectable):
    SelectGroupStyleCore: _Callable[[_inspectable.IInspectable,  # group
                                     _type.UINT32,  # level
                                     _Pointer[IGroupStyle]],  # result
                                    _type.HRESULT]


class IHandwritingPanelClosedEventArgs(_inspectable.IInspectable):
    pass


class IHandwritingPanelOpenedEventArgs(_inspectable.IInspectable):
    pass


class IHandwritingView(_inspectable.IInspectable):
    get_PlacementTarget: _Callable[[_Pointer[_Windows_UI_Xaml.IUIElement]],  # value
                                   _type.HRESULT]
    put_PlacementTarget: _Callable[[_Windows_UI_Xaml.IUIElement],  # value
                                   _type.HRESULT]
    get_PlacementAlignment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.HandwritingPanelPlacementAlignment]],  # value
                                      _type.HRESULT]
    put_PlacementAlignment: _Callable[[_enum.Windows.UI.Xaml.Controls.HandwritingPanelPlacementAlignment],  # value
                                      _type.HRESULT]
    get_IsOpen: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    get_AreCandidatesEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    put_AreCandidatesEnabled: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]
    add_Opened: _Callable[[_Windows_Foundation.ITypedEventHandler[IHandwritingView, IHandwritingPanelOpenedEventArgs],  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Opened: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    add_Closed: _Callable[[_Windows_Foundation.ITypedEventHandler[IHandwritingView, IHandwritingPanelClosedEventArgs],  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Closed: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    TryClose: _Callable[[_Pointer[_type.boolean]],  # result
                        _type.HRESULT]
    TryOpen: _Callable[[_Pointer[_type.boolean]],  # result
                       _type.HRESULT]


class IHandwritingView2(_inspectable.IInspectable):
    get_IsSwitchToKeyboardEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    put_IsSwitchToKeyboardEnabled: _Callable[[_type.boolean],  # value
                                             _type.HRESULT]
    get_IsCommandBarOpen: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_IsCommandBarOpen: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_InputDeviceTypes: _Callable[[_Pointer[_enum.Windows.UI.Core.CoreInputDeviceTypes]],  # value
                                    _type.HRESULT]
    put_InputDeviceTypes: _Callable[[_enum.Windows.UI.Core.CoreInputDeviceTypes],  # value
                                    _type.HRESULT]
    add_CandidatesChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IHandwritingView, IHandwritingViewCandidatesChangedEventArgs],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_CandidatesChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    add_TextSubmitted: _Callable[[_Windows_Foundation.ITypedEventHandler[IHandwritingView, IHandwritingViewTextSubmittedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_TextSubmitted: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    GetCandidates: _Callable[[_type.UINT32,  # candidatesSessionId
                              _Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # result
                             _type.HRESULT]
    SelectCandidate: _Callable[[_type.UINT32,  # candidatesSessionId
                                _type.UINT32],  # selectedCandidateIndex
                               _type.HRESULT]


class IHandwritingViewCandidatesChangedEventArgs(_inspectable.IInspectable):
    get_CandidatesSessionId: _Callable[[_Pointer[_type.UINT32]],  # value
                                       _type.HRESULT]


class IHandwritingViewFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IHandwritingView]],  # value
                              _type.HRESULT]


class IHandwritingViewStatics(_inspectable.IInspectable):
    get_PlacementTargetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_PlacementAlignmentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_IsOpenProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_AreCandidatesEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]

    _factory = True


class IHandwritingViewStatics2(_inspectable.IInspectable):
    get_IsSwitchToKeyboardEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                     _type.HRESULT]
    get_IsCommandBarOpenProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]

    _factory = True


class IHandwritingViewTextSubmittedEventArgs(_inspectable.IInspectable):
    pass


class IHub(_inspectable.IInspectable):
    get_Header: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                          _type.HRESULT]
    put_Header: _Callable[[_inspectable.IInspectable],  # value
                          _type.HRESULT]
    get_HeaderTemplate: _Callable[[_Pointer[_Windows_UI_Xaml.IDataTemplate]],  # value
                                  _type.HRESULT]
    put_HeaderTemplate: _Callable[[_Windows_UI_Xaml.IDataTemplate],  # value
                                  _type.HRESULT]
    get_Orientation: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Orientation]],  # value
                               _type.HRESULT]
    put_Orientation: _Callable[[_enum.Windows.UI.Xaml.Controls.Orientation],  # value
                               _type.HRESULT]
    get_DefaultSectionIndex: _Callable[[_Pointer[_type.INT32]],  # value
                                       _type.HRESULT]
    put_DefaultSectionIndex: _Callable[[_type.INT32],  # value
                                       _type.HRESULT]
    get_Sections: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IHubSection]]],  # value
                            _type.HRESULT]
    get_SectionsInView: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IHubSection]]],  # value
                                  _type.HRESULT]
    get_SectionHeaders: _Callable[[_Pointer[_Windows_Foundation_Collections.IObservableVector[_inspectable.IInspectable]]],  # value
                                  _type.HRESULT]
    add_SectionHeaderClick: _Callable[[IHubSectionHeaderClickEventHandler,  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_SectionHeaderClick: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_SectionsInViewChanged: _Callable[[ISectionsInViewChangedEventHandler,  # handler
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_SectionsInViewChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]
    ScrollToSection: _Callable[[IHubSection],  # section
                               _type.HRESULT]


class IHubFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IHub]],  # value
                              _type.HRESULT]


class IHubSection(_inspectable.IInspectable):
    get_Header: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                          _type.HRESULT]
    put_Header: _Callable[[_inspectable.IInspectable],  # value
                          _type.HRESULT]
    get_HeaderTemplate: _Callable[[_Pointer[_Windows_UI_Xaml.IDataTemplate]],  # value
                                  _type.HRESULT]
    put_HeaderTemplate: _Callable[[_Windows_UI_Xaml.IDataTemplate],  # value
                                  _type.HRESULT]
    get_ContentTemplate: _Callable[[_Pointer[_Windows_UI_Xaml.IDataTemplate]],  # value
                                   _type.HRESULT]
    put_ContentTemplate: _Callable[[_Windows_UI_Xaml.IDataTemplate],  # value
                                   _type.HRESULT]
    get_IsHeaderInteractive: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_IsHeaderInteractive: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]


class IHubSectionFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IHubSection]],  # value
                              _type.HRESULT]


class IHubSectionHeaderClickEventArgs(_inspectable.IInspectable):
    get_Section: _Callable[[_Pointer[IHubSection]],  # value
                           _type.HRESULT]


class IHubSectionStatics(_inspectable.IInspectable):
    get_HeaderProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_HeaderTemplateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_ContentTemplateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_IsHeaderInteractiveProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]

    _factory = True


class IHubStatics(_inspectable.IInspectable):
    get_HeaderProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_HeaderTemplateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_OrientationProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_DefaultSectionIndexProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_SemanticZoomOwnerProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_IsActiveViewProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_IsZoomedInViewProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]

    _factory = True


class IHyperlinkButton(_inspectable.IInspectable):
    get_NavigateUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                               _type.HRESULT]
    put_NavigateUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                               _type.HRESULT]


class IHyperlinkButtonFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IHyperlinkButton]],  # value
                              _type.HRESULT]


class IHyperlinkButtonStatics(_inspectable.IInspectable):
    get_NavigateUriProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]

    _factory = True


class IIconElement(_inspectable.IInspectable):
    get_Foreground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                              _type.HRESULT]
    put_Foreground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                              _type.HRESULT]


class IIconElementFactory(_inspectable.IInspectable):
    pass


class IIconElementStatics(_inspectable.IInspectable):
    get_ForegroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]

    _factory = True


class IIconSource(_inspectable.IInspectable):
    get_Foreground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                              _type.HRESULT]
    put_Foreground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                              _type.HRESULT]


class IIconSourceElement(_inspectable.IInspectable):
    get_IconSource: _Callable[[_Pointer[IIconSource]],  # value
                              _type.HRESULT]
    put_IconSource: _Callable[[IIconSource],  # value
                              _type.HRESULT]


class IIconSourceElementFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IIconSourceElement]],  # value
                              _type.HRESULT]


class IIconSourceElementStatics(_inspectable.IInspectable):
    get_IconSourceProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]

    _factory = True


class IIconSourceFactory(_inspectable.IInspectable):
    pass


class IIconSourceStatics(_inspectable.IInspectable):
    get_ForegroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]

    _factory = True


class IImage(_inspectable.IInspectable):
    get_Source: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IImageSource]],  # value
                          _type.HRESULT]
    put_Source: _Callable[[_Windows_UI_Xaml_Media.IImageSource],  # value
                          _type.HRESULT]
    get_Stretch: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Media.Stretch]],  # value
                           _type.HRESULT]
    put_Stretch: _Callable[[_enum.Windows.UI.Xaml.Media.Stretch],  # value
                           _type.HRESULT]
    get_NineGrid: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                            _type.HRESULT]
    put_NineGrid: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                            _type.HRESULT]
    PlayToSource: _Callable[[_Pointer[_Windows_Media_PlayTo.IPlayToSource]],  # value
                            _type.HRESULT]
    add_ImageFailed: _Callable[[_Windows_UI_Xaml.IExceptionRoutedEventHandler,  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_ImageFailed: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    add_ImageOpened: _Callable[[_Windows_UI_Xaml.IRoutedEventHandler,  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_ImageOpened: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]


class IImage2(_inspectable.IInspectable):
    GetAsCastingSource: _Callable[[_Pointer[_Windows_Media_Casting.ICastingSource]],  # result
                                  _type.HRESULT]


class IImage3(_inspectable.IInspectable):
    GetAlphaMask: _Callable[[_Pointer[_Windows_UI_Composition.ICompositionBrush]],  # result
                            _type.HRESULT]


class IImageStatics(_inspectable.IInspectable):
    get_SourceProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_StretchProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_NineGridProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    PlayToSourceProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]

    _factory = True


class IInkCanvas(_inspectable.IInspectable):
    get_InkPresenter: _Callable[[_Pointer[_Windows_UI_Input_Inking.IInkPresenter]],  # value
                                _type.HRESULT]


class IInkCanvasFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IInkCanvas]],  # value
                              _type.HRESULT]


class IInkToolbar(_inspectable.IInspectable):
    get_InitialControls: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.InkToolbarInitialControls]],  # value
                                   _type.HRESULT]
    put_InitialControls: _Callable[[_enum.Windows.UI.Xaml.Controls.InkToolbarInitialControls],  # value
                                   _type.HRESULT]
    get_Children: _Callable[[_Pointer[_Windows_Foundation_Collections.IObservableVector[_Windows_UI_Xaml.IDependencyObject]]],  # value
                            _type.HRESULT]
    get_ActiveTool: _Callable[[_Pointer[IInkToolbarToolButton]],  # value
                              _type.HRESULT]
    put_ActiveTool: _Callable[[IInkToolbarToolButton],  # value
                              _type.HRESULT]
    get_InkDrawingAttributes: _Callable[[_Pointer[_Windows_UI_Input_Inking.IInkDrawingAttributes]],  # value
                                        _type.HRESULT]
    get_IsRulerButtonChecked: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    put_IsRulerButtonChecked: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]
    get_TargetInkCanvas: _Callable[[_Pointer[IInkCanvas]],  # value
                                   _type.HRESULT]
    put_TargetInkCanvas: _Callable[[IInkCanvas],  # value
                                   _type.HRESULT]
    add_ActiveToolChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IInkToolbar, _inspectable.IInspectable],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_ActiveToolChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    add_InkDrawingAttributesChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IInkToolbar, _inspectable.IInspectable],  # handler
                                                _Pointer[_struct.EventRegistrationToken]],  # token
                                               _type.HRESULT]
    remove_InkDrawingAttributesChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                  _type.HRESULT]
    add_EraseAllClicked: _Callable[[_Windows_Foundation.ITypedEventHandler[IInkToolbar, _inspectable.IInspectable],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_EraseAllClicked: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    IsRulerButtonCheckedChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    GetToolButton: _Callable[[_enum.Windows.UI.Xaml.Controls.InkToolbarTool,  # tool
                              _Pointer[IInkToolbarToolButton]],  # result
                             _type.HRESULT]
    GetToggleButton: _Callable[[_enum.Windows.UI.Xaml.Controls.InkToolbarToggle,  # tool
                                _Pointer[IInkToolbarToggleButton]],  # result
                               _type.HRESULT]


class IInkToolbar2(_inspectable.IInspectable):
    get_IsStencilButtonChecked: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_IsStencilButtonChecked: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    get_ButtonFlyoutPlacement: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.InkToolbarButtonFlyoutPlacement]],  # value
                                         _type.HRESULT]
    put_ButtonFlyoutPlacement: _Callable[[_enum.Windows.UI.Xaml.Controls.InkToolbarButtonFlyoutPlacement],  # value
                                         _type.HRESULT]
    get_Orientation: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Orientation]],  # value
                               _type.HRESULT]
    put_Orientation: _Callable[[_enum.Windows.UI.Xaml.Controls.Orientation],  # value
                               _type.HRESULT]
    add_IsStencilButtonCheckedChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IInkToolbar, IInkToolbarIsStencilButtonCheckedChangedEventArgs],  # handler
                                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                                 _type.HRESULT]
    remove_IsStencilButtonCheckedChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                    _type.HRESULT]
    GetMenuButton: _Callable[[_enum.Windows.UI.Xaml.Controls.InkToolbarMenuKind,  # menu
                              _Pointer[IInkToolbarMenuButton]],  # result
                             _type.HRESULT]


class IInkToolbar3(_inspectable.IInspectable):
    get_TargetInkPresenter: _Callable[[_Pointer[_Windows_UI_Input_Inking.IInkPresenter]],  # value
                                      _type.HRESULT]
    put_TargetInkPresenter: _Callable[[_Windows_UI_Input_Inking.IInkPresenter],  # value
                                      _type.HRESULT]


class IInkToolbarBallpointPenButton(_inspectable.IInspectable):
    pass


class IInkToolbarBallpointPenButtonFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IInkToolbarBallpointPenButton]],  # value
                              _type.HRESULT]


class IInkToolbarCustomPen(_inspectable.IInspectable):
    CreateInkDrawingAttributes: _Callable[[_Windows_UI_Xaml_Media.IBrush,  # brush
                                           _type.DOUBLE,  # strokeWidth
                                           _Pointer[_Windows_UI_Input_Inking.IInkDrawingAttributes]],  # result
                                          _type.HRESULT]


class IInkToolbarCustomPenButton(_inspectable.IInspectable):
    get_CustomPen: _Callable[[_Pointer[IInkToolbarCustomPen]],  # value
                             _type.HRESULT]
    put_CustomPen: _Callable[[IInkToolbarCustomPen],  # value
                             _type.HRESULT]
    get_ConfigurationContent: _Callable[[_Pointer[_Windows_UI_Xaml.IUIElement]],  # value
                                        _type.HRESULT]
    put_ConfigurationContent: _Callable[[_Windows_UI_Xaml.IUIElement],  # value
                                        _type.HRESULT]


class IInkToolbarCustomPenButtonFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IInkToolbarCustomPenButton]],  # value
                              _type.HRESULT]


class IInkToolbarCustomPenButtonStatics(_inspectable.IInspectable):
    get_CustomPenProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_ConfigurationContentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]

    _factory = True


class IInkToolbarCustomPenFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IInkToolbarCustomPen]],  # value
                              _type.HRESULT]


class IInkToolbarCustomPenOverrides(_inspectable.IInspectable):
    CreateInkDrawingAttributesCore: _Callable[[_Windows_UI_Xaml_Media.IBrush,  # brush
                                               _type.DOUBLE,  # strokeWidth
                                               _Pointer[_Windows_UI_Input_Inking.IInkDrawingAttributes]],  # result
                                              _type.HRESULT]


class IInkToolbarCustomToggleButton(_inspectable.IInspectable):
    pass


class IInkToolbarCustomToggleButtonFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IInkToolbarCustomToggleButton]],  # value
                              _type.HRESULT]


class IInkToolbarCustomToolButton(_inspectable.IInspectable):
    get_ConfigurationContent: _Callable[[_Pointer[_Windows_UI_Xaml.IUIElement]],  # value
                                        _type.HRESULT]
    put_ConfigurationContent: _Callable[[_Windows_UI_Xaml.IUIElement],  # value
                                        _type.HRESULT]


class IInkToolbarCustomToolButtonFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IInkToolbarCustomToolButton]],  # value
                              _type.HRESULT]


class IInkToolbarCustomToolButtonStatics(_inspectable.IInspectable):
    get_ConfigurationContentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]

    _factory = True


class IInkToolbarEraserButton(_inspectable.IInspectable):
    pass


class IInkToolbarEraserButton2(_inspectable.IInspectable):
    get_IsClearAllVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    put_IsClearAllVisible: _Callable[[_type.boolean],  # value
                                     _type.HRESULT]


class IInkToolbarEraserButtonFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IInkToolbarEraserButton]],  # value
                              _type.HRESULT]


class IInkToolbarEraserButtonStatics2(_inspectable.IInspectable):
    get_IsClearAllVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]

    _factory = True


class IInkToolbarFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IInkToolbar]],  # value
                              _type.HRESULT]


class IInkToolbarFlyoutItem(_inspectable.IInspectable):
    get_Kind: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.InkToolbarFlyoutItemKind]],  # value
                        _type.HRESULT]
    put_Kind: _Callable[[_enum.Windows.UI.Xaml.Controls.InkToolbarFlyoutItemKind],  # value
                        _type.HRESULT]
    get_IsChecked: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsChecked: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    add_Checked: _Callable[[_Windows_Foundation.ITypedEventHandler[IInkToolbarFlyoutItem, _inspectable.IInspectable],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Checked: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_Unchecked: _Callable[[_Windows_Foundation.ITypedEventHandler[IInkToolbarFlyoutItem, _inspectable.IInspectable],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_Unchecked: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]


class IInkToolbarFlyoutItemFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IInkToolbarFlyoutItem]],  # value
                              _type.HRESULT]


class IInkToolbarFlyoutItemStatics(_inspectable.IInspectable):
    get_KindProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]
    get_IsCheckedProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]

    _factory = True


class IInkToolbarHighlighterButton(_inspectable.IInspectable):
    pass


class IInkToolbarHighlighterButtonFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IInkToolbarHighlighterButton]],  # value
                              _type.HRESULT]


class IInkToolbarIsStencilButtonCheckedChangedEventArgs(_inspectable.IInspectable):
    get_StencilButton: _Callable[[_Pointer[IInkToolbarStencilButton]],  # value
                                 _type.HRESULT]
    get_StencilKind: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.InkToolbarStencilKind]],  # value
                               _type.HRESULT]


class IInkToolbarMenuButton(_inspectable.IInspectable):
    get_MenuKind: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.InkToolbarMenuKind]],  # value
                            _type.HRESULT]
    get_IsExtensionGlyphShown: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_IsExtensionGlyphShown: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]


class IInkToolbarMenuButtonFactory(_inspectable.IInspectable):
    pass


class IInkToolbarMenuButtonStatics(_inspectable.IInspectable):
    get_IsExtensionGlyphShownProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]

    _factory = True


class IInkToolbarPenButton(_inspectable.IInspectable):
    get_Palette: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Media.IBrush]]],  # value
                           _type.HRESULT]
    put_Palette: _Callable[[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Media.IBrush]],  # value
                           _type.HRESULT]
    get_MinStrokeWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    put_MinStrokeWidth: _Callable[[_type.DOUBLE],  # value
                                  _type.HRESULT]
    get_MaxStrokeWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    put_MaxStrokeWidth: _Callable[[_type.DOUBLE],  # value
                                  _type.HRESULT]
    get_SelectedBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                 _type.HRESULT]
    get_SelectedBrushIndex: _Callable[[_Pointer[_type.INT32]],  # value
                                      _type.HRESULT]
    put_SelectedBrushIndex: _Callable[[_type.INT32],  # value
                                      _type.HRESULT]
    get_SelectedStrokeWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                       _type.HRESULT]
    put_SelectedStrokeWidth: _Callable[[_type.DOUBLE],  # value
                                       _type.HRESULT]


class IInkToolbarPenButtonFactory(_inspectable.IInspectable):
    pass


class IInkToolbarPenButtonStatics(_inspectable.IInspectable):
    get_PaletteProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_MinStrokeWidthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_MaxStrokeWidthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_SelectedBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_SelectedBrushIndexProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_SelectedStrokeWidthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]

    _factory = True


class IInkToolbarPenConfigurationControl(_inspectable.IInspectable):
    get_PenButton: _Callable[[_Pointer[IInkToolbarPenButton]],  # value
                             _type.HRESULT]


class IInkToolbarPenConfigurationControlFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IInkToolbarPenConfigurationControl]],  # value
                              _type.HRESULT]


class IInkToolbarPenConfigurationControlStatics(_inspectable.IInspectable):
    get_PenButtonProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]

    _factory = True


class IInkToolbarPencilButton(_inspectable.IInspectable):
    pass


class IInkToolbarPencilButtonFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IInkToolbarPencilButton]],  # value
                              _type.HRESULT]


class IInkToolbarRulerButton(_inspectable.IInspectable):
    Ruler: _Callable[[_Pointer[_Windows_UI_Input_Inking.IInkPresenterRuler]],  # value
                     _type.HRESULT]


class IInkToolbarRulerButtonFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IInkToolbarRulerButton]],  # value
                              _type.HRESULT]


class IInkToolbarRulerButtonStatics(_inspectable.IInspectable):
    RulerProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                             _type.HRESULT]

    _factory = True


class IInkToolbarStatics(_inspectable.IInspectable):
    get_InitialControlsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_ChildrenProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_ActiveToolProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_InkDrawingAttributesProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_IsRulerButtonCheckedProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_TargetInkCanvasProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]

    _factory = True


class IInkToolbarStatics2(_inspectable.IInspectable):
    get_IsStencilButtonCheckedProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]
    get_ButtonFlyoutPlacementProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_OrientationProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]

    _factory = True


class IInkToolbarStatics3(_inspectable.IInspectable):
    get_TargetInkPresenterProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]

    _factory = True


class IInkToolbarStencilButton(_inspectable.IInspectable):
    get_Ruler: _Callable[[_Pointer[_Windows_UI_Input_Inking.IInkPresenterRuler]],  # value
                         _type.HRESULT]
    get_Protractor: _Callable[[_Pointer[_Windows_UI_Input_Inking.IInkPresenterProtractor]],  # value
                              _type.HRESULT]
    get_SelectedStencil: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.InkToolbarStencilKind]],  # value
                                   _type.HRESULT]
    put_SelectedStencil: _Callable[[_enum.Windows.UI.Xaml.Controls.InkToolbarStencilKind],  # value
                                   _type.HRESULT]
    get_IsRulerItemVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_IsRulerItemVisible: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    get_IsProtractorItemVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    put_IsProtractorItemVisible: _Callable[[_type.boolean],  # value
                                           _type.HRESULT]


class IInkToolbarStencilButtonFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IInkToolbarStencilButton]],  # value
                              _type.HRESULT]


class IInkToolbarStencilButtonStatics(_inspectable.IInspectable):
    get_RulerProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_ProtractorProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_SelectedStencilProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_IsRulerItemVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_IsProtractorItemVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]

    _factory = True


class IInkToolbarToggleButton(_inspectable.IInspectable):
    get_ToggleKind: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.InkToolbarToggle]],  # value
                              _type.HRESULT]


class IInkToolbarToggleButtonFactory(_inspectable.IInspectable):
    pass


class IInkToolbarToolButton(_inspectable.IInspectable):
    get_ToolKind: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.InkToolbarTool]],  # value
                            _type.HRESULT]
    get_IsExtensionGlyphShown: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_IsExtensionGlyphShown: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]


class IInkToolbarToolButtonFactory(_inspectable.IInspectable):
    pass


class IInkToolbarToolButtonStatics(_inspectable.IInspectable):
    get_IsExtensionGlyphShownProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]

    _factory = True


class IInsertionPanel(_inspectable.IInspectable):
    GetInsertionIndexes: _Callable[[_struct.Windows.Foundation.Point,  # position
                                    _Pointer[_type.INT32],  # first
                                    _Pointer[_type.INT32]],  # second
                                   _type.HRESULT]


class IIsTextTrimmedChangedEventArgs(_inspectable.IInspectable):
    pass


class IItemClickEventArgs(_inspectable.IInspectable):
    get_ClickedItem: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                               _type.HRESULT]


class IItemContainerGenerator(_inspectable.IInspectable):
    add_ItemsChanged: _Callable[[_Windows_UI_Xaml_Controls_Primitives.IItemsChangedEventHandler,  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_ItemsChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    ItemFromContainer: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # container
                                  _Pointer[_inspectable.IInspectable]],  # result
                                 _type.HRESULT]
    ContainerFromItem: _Callable[[_inspectable.IInspectable,  # item
                                  _Pointer[_Windows_UI_Xaml.IDependencyObject]],  # result
                                 _type.HRESULT]
    IndexFromContainer: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # container
                                   _Pointer[_type.INT32]],  # result
                                  _type.HRESULT]
    ContainerFromIndex: _Callable[[_type.INT32,  # index
                                   _Pointer[_Windows_UI_Xaml.IDependencyObject]],  # result
                                  _type.HRESULT]
    GetItemContainerGeneratorForPanel: _Callable[[IPanel,  # panel
                                                  _Pointer[IItemContainerGenerator]],  # result
                                                 _type.HRESULT]
    StartAt: _Callable[[_struct.Windows.UI.Xaml.Controls.Primitives.GeneratorPosition,  # position
                        _enum.Windows.UI.Xaml.Controls.Primitives.GeneratorDirection,  # direction
                        _type.boolean],  # allowStartAtRealizedItem
                       _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    GenerateNext: _Callable[[_Pointer[_type.boolean],  # isNewlyRealized
                             _Pointer[_Windows_UI_Xaml.IDependencyObject]],  # returnValue
                            _type.HRESULT]
    PrepareItemContainer: _Callable[[_Windows_UI_Xaml.IDependencyObject],  # container
                                    _type.HRESULT]
    RemoveAll: _Callable[[],
                         _type.HRESULT]
    Remove: _Callable[[_struct.Windows.UI.Xaml.Controls.Primitives.GeneratorPosition,  # position
                       _type.INT32],  # count
                      _type.HRESULT]
    GeneratorPositionFromIndex: _Callable[[_type.INT32,  # itemIndex
                                           _Pointer[_struct.Windows.UI.Xaml.Controls.Primitives.GeneratorPosition]],  # result
                                          _type.HRESULT]
    IndexFromGeneratorPosition: _Callable[[_struct.Windows.UI.Xaml.Controls.Primitives.GeneratorPosition,  # position
                                           _Pointer[_type.INT32]],  # result
                                          _type.HRESULT]
    Recycle: _Callable[[_struct.Windows.UI.Xaml.Controls.Primitives.GeneratorPosition,  # position
                        _type.INT32],  # count
                       _type.HRESULT]


class IItemContainerMapping(_inspectable.IInspectable):
    ItemFromContainer: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # container
                                  _Pointer[_inspectable.IInspectable]],  # result
                                 _type.HRESULT]
    ContainerFromItem: _Callable[[_inspectable.IInspectable,  # item
                                  _Pointer[_Windows_UI_Xaml.IDependencyObject]],  # result
                                 _type.HRESULT]
    IndexFromContainer: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # container
                                   _Pointer[_type.INT32]],  # result
                                  _type.HRESULT]
    ContainerFromIndex: _Callable[[_type.INT32,  # index
                                   _Pointer[_Windows_UI_Xaml.IDependencyObject]],  # result
                                  _type.HRESULT]


class IItemsControl(_inspectable.IInspectable):
    get_ItemsSource: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                               _type.HRESULT]
    put_ItemsSource: _Callable[[_inspectable.IInspectable],  # value
                               _type.HRESULT]
    get_Items: _Callable[[_Pointer[_Windows_Foundation_Collections.IObservableVector[_inspectable.IInspectable]]],  # value
                         _type.HRESULT]
    get_ItemTemplate: _Callable[[_Pointer[_Windows_UI_Xaml.IDataTemplate]],  # value
                                _type.HRESULT]
    put_ItemTemplate: _Callable[[_Windows_UI_Xaml.IDataTemplate],  # value
                                _type.HRESULT]
    get_ItemTemplateSelector: _Callable[[_Pointer[IDataTemplateSelector]],  # value
                                        _type.HRESULT]
    put_ItemTemplateSelector: _Callable[[IDataTemplateSelector],  # value
                                        _type.HRESULT]
    get_ItemsPanel: _Callable[[_Pointer[IItemsPanelTemplate]],  # value
                              _type.HRESULT]
    put_ItemsPanel: _Callable[[IItemsPanelTemplate],  # value
                              _type.HRESULT]
    get_DisplayMemberPath: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    put_DisplayMemberPath: _Callable[[_type.HSTRING],  # value
                                     _type.HRESULT]
    get_ItemContainerStyle: _Callable[[_Pointer[_Windows_UI_Xaml.IStyle]],  # value
                                      _type.HRESULT]
    put_ItemContainerStyle: _Callable[[_Windows_UI_Xaml.IStyle],  # value
                                      _type.HRESULT]
    get_ItemContainerStyleSelector: _Callable[[_Pointer[IStyleSelector]],  # value
                                              _type.HRESULT]
    put_ItemContainerStyleSelector: _Callable[[IStyleSelector],  # value
                                              _type.HRESULT]
    get_ItemContainerGenerator: _Callable[[_Pointer[IItemContainerGenerator]],  # value
                                          _type.HRESULT]
    get_ItemContainerTransitions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Media_Animation.ITransition]]],  # value
                                            _type.HRESULT]
    put_ItemContainerTransitions: _Callable[[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Media_Animation.ITransition]],  # value
                                            _type.HRESULT]
    get_GroupStyle: _Callable[[_Pointer[_Windows_Foundation_Collections.IObservableVector[IGroupStyle]]],  # value
                              _type.HRESULT]
    get_GroupStyleSelector: _Callable[[_Pointer[IGroupStyleSelector]],  # value
                                      _type.HRESULT]
    put_GroupStyleSelector: _Callable[[IGroupStyleSelector],  # value
                                      _type.HRESULT]
    get_IsGrouping: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]


class IItemsControl2(_inspectable.IInspectable):
    get_ItemsPanelRoot: _Callable[[_Pointer[IPanel]],  # value
                                  _type.HRESULT]


class IItemsControl3(_inspectable.IInspectable):
    GroupHeaderContainerFromItemContainer: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # itemContainer
                                                      _Pointer[_Windows_UI_Xaml.IDependencyObject]],  # result
                                                     _type.HRESULT]


class IItemsControlFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IItemsControl]],  # value
                              _type.HRESULT]


class IItemsControlOverrides(_inspectable.IInspectable):
    IsItemItsOwnContainerOverride: _Callable[[_inspectable.IInspectable,  # item
                                              _Pointer[_type.boolean]],  # result
                                             _type.HRESULT]
    GetContainerForItemOverride: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyObject]],  # result
                                           _type.HRESULT]
    ClearContainerForItemOverride: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                              _inspectable.IInspectable],  # item
                                             _type.HRESULT]
    PrepareContainerForItemOverride: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                                _inspectable.IInspectable],  # item
                                               _type.HRESULT]
    OnItemsChanged: _Callable[[_inspectable.IInspectable],  # e
                              _type.HRESULT]
    OnItemContainerStyleChanged: _Callable[[_Windows_UI_Xaml.IStyle,  # oldItemContainerStyle
                                            _Windows_UI_Xaml.IStyle],  # newItemContainerStyle
                                           _type.HRESULT]
    OnItemContainerStyleSelectorChanged: _Callable[[IStyleSelector,  # oldItemContainerStyleSelector
                                                    IStyleSelector],  # newItemContainerStyleSelector
                                                   _type.HRESULT]
    OnItemTemplateChanged: _Callable[[_Windows_UI_Xaml.IDataTemplate,  # oldItemTemplate
                                      _Windows_UI_Xaml.IDataTemplate],  # newItemTemplate
                                     _type.HRESULT]
    OnItemTemplateSelectorChanged: _Callable[[IDataTemplateSelector,  # oldItemTemplateSelector
                                              IDataTemplateSelector],  # newItemTemplateSelector
                                             _type.HRESULT]
    OnGroupStyleSelectorChanged: _Callable[[IGroupStyleSelector,  # oldGroupStyleSelector
                                            IGroupStyleSelector],  # newGroupStyleSelector
                                           _type.HRESULT]


class IItemsControlStatics(_inspectable.IInspectable):
    get_ItemsSourceProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_ItemTemplateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_ItemTemplateSelectorProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_ItemsPanelProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_DisplayMemberPathProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_ItemContainerStyleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_ItemContainerStyleSelectorProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                      _type.HRESULT]
    get_ItemContainerTransitionsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]
    get_GroupStyleSelectorProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_IsGroupingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    GetItemsOwner: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                              _Pointer[IItemsControl]],  # result
                             _type.HRESULT]
    ItemsControlFromItemContainer: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # container
                                              _Pointer[IItemsControl]],  # result
                                             _type.HRESULT]

    _factory = True


class IItemsPanelTemplate(_inspectable.IInspectable):
    pass


class IItemsPickedEventArgs(_inspectable.IInspectable):
    get_AddedItems: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_inspectable.IInspectable]]],  # value
                              _type.HRESULT]
    get_RemovedItems: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_inspectable.IInspectable]]],  # value
                                _type.HRESULT]


class IItemsPresenter(_inspectable.IInspectable):
    get_Header: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                          _type.HRESULT]
    put_Header: _Callable[[_inspectable.IInspectable],  # value
                          _type.HRESULT]
    get_HeaderTemplate: _Callable[[_Pointer[_Windows_UI_Xaml.IDataTemplate]],  # value
                                  _type.HRESULT]
    put_HeaderTemplate: _Callable[[_Windows_UI_Xaml.IDataTemplate],  # value
                                  _type.HRESULT]
    get_HeaderTransitions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Media_Animation.ITransition]]],  # value
                                     _type.HRESULT]
    put_HeaderTransitions: _Callable[[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Media_Animation.ITransition]],  # value
                                     _type.HRESULT]
    get_Padding: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                           _type.HRESULT]
    put_Padding: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                           _type.HRESULT]


class IItemsPresenter2(_inspectable.IInspectable):
    get_Footer: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                          _type.HRESULT]
    put_Footer: _Callable[[_inspectable.IInspectable],  # value
                          _type.HRESULT]
    get_FooterTemplate: _Callable[[_Pointer[_Windows_UI_Xaml.IDataTemplate]],  # value
                                  _type.HRESULT]
    put_FooterTemplate: _Callable[[_Windows_UI_Xaml.IDataTemplate],  # value
                                  _type.HRESULT]
    get_FooterTransitions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Media_Animation.ITransition]]],  # value
                                     _type.HRESULT]
    put_FooterTransitions: _Callable[[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Media_Animation.ITransition]],  # value
                                     _type.HRESULT]


class IItemsPresenterStatics(_inspectable.IInspectable):
    get_HeaderProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_HeaderTemplateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_HeaderTransitionsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_PaddingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]

    _factory = True


class IItemsPresenterStatics2(_inspectable.IInspectable):
    get_FooterProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_FooterTemplateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_FooterTransitionsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]

    _factory = True


class IItemsStackPanel(_inspectable.IInspectable):
    get_GroupPadding: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                                _type.HRESULT]
    put_GroupPadding: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                                _type.HRESULT]
    get_Orientation: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Orientation]],  # value
                               _type.HRESULT]
    put_Orientation: _Callable[[_enum.Windows.UI.Xaml.Controls.Orientation],  # value
                               _type.HRESULT]
    get_FirstCacheIndex: _Callable[[_Pointer[_type.INT32]],  # value
                                   _type.HRESULT]
    get_FirstVisibleIndex: _Callable[[_Pointer[_type.INT32]],  # value
                                     _type.HRESULT]
    get_LastVisibleIndex: _Callable[[_Pointer[_type.INT32]],  # value
                                    _type.HRESULT]
    get_LastCacheIndex: _Callable[[_Pointer[_type.INT32]],  # value
                                  _type.HRESULT]
    get_ScrollingDirection: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.PanelScrollingDirection]],  # value
                                      _type.HRESULT]
    get_GroupHeaderPlacement: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Primitives.GroupHeaderPlacement]],  # value
                                        _type.HRESULT]
    put_GroupHeaderPlacement: _Callable[[_enum.Windows.UI.Xaml.Controls.Primitives.GroupHeaderPlacement],  # value
                                        _type.HRESULT]
    get_ItemsUpdatingScrollMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.ItemsUpdatingScrollMode]],  # value
                                           _type.HRESULT]
    put_ItemsUpdatingScrollMode: _Callable[[_enum.Windows.UI.Xaml.Controls.ItemsUpdatingScrollMode],  # value
                                           _type.HRESULT]
    get_CacheLength: _Callable[[_Pointer[_type.DOUBLE]],  # value
                               _type.HRESULT]
    put_CacheLength: _Callable[[_type.DOUBLE],  # value
                               _type.HRESULT]


class IItemsStackPanel2(_inspectable.IInspectable):
    get_AreStickyGroupHeadersEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                _type.HRESULT]
    put_AreStickyGroupHeadersEnabled: _Callable[[_type.boolean],  # value
                                                _type.HRESULT]


class IItemsStackPanelStatics(_inspectable.IInspectable):
    get_GroupPaddingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_OrientationProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_GroupHeaderPlacementProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_CacheLengthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]

    _factory = True


class IItemsStackPanelStatics2(_inspectable.IInspectable):
    get_AreStickyGroupHeadersEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                        _type.HRESULT]

    _factory = True


class IItemsWrapGrid(_inspectable.IInspectable):
    get_GroupPadding: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                                _type.HRESULT]
    put_GroupPadding: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                                _type.HRESULT]
    get_Orientation: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Orientation]],  # value
                               _type.HRESULT]
    put_Orientation: _Callable[[_enum.Windows.UI.Xaml.Controls.Orientation],  # value
                               _type.HRESULT]
    get_MaximumRowsOrColumns: _Callable[[_Pointer[_type.INT32]],  # value
                                        _type.HRESULT]
    put_MaximumRowsOrColumns: _Callable[[_type.INT32],  # value
                                        _type.HRESULT]
    get_ItemWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                             _type.HRESULT]
    put_ItemWidth: _Callable[[_type.DOUBLE],  # value
                             _type.HRESULT]
    get_ItemHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                              _type.HRESULT]
    put_ItemHeight: _Callable[[_type.DOUBLE],  # value
                              _type.HRESULT]
    get_FirstCacheIndex: _Callable[[_Pointer[_type.INT32]],  # value
                                   _type.HRESULT]
    get_FirstVisibleIndex: _Callable[[_Pointer[_type.INT32]],  # value
                                     _type.HRESULT]
    get_LastVisibleIndex: _Callable[[_Pointer[_type.INT32]],  # value
                                    _type.HRESULT]
    get_LastCacheIndex: _Callable[[_Pointer[_type.INT32]],  # value
                                  _type.HRESULT]
    get_ScrollingDirection: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.PanelScrollingDirection]],  # value
                                      _type.HRESULT]
    get_GroupHeaderPlacement: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Primitives.GroupHeaderPlacement]],  # value
                                        _type.HRESULT]
    put_GroupHeaderPlacement: _Callable[[_enum.Windows.UI.Xaml.Controls.Primitives.GroupHeaderPlacement],  # value
                                        _type.HRESULT]
    get_CacheLength: _Callable[[_Pointer[_type.DOUBLE]],  # value
                               _type.HRESULT]
    put_CacheLength: _Callable[[_type.DOUBLE],  # value
                               _type.HRESULT]


class IItemsWrapGrid2(_inspectable.IInspectable):
    get_AreStickyGroupHeadersEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                _type.HRESULT]
    put_AreStickyGroupHeadersEnabled: _Callable[[_type.boolean],  # value
                                                _type.HRESULT]


class IItemsWrapGridStatics(_inspectable.IInspectable):
    get_GroupPaddingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_OrientationProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_MaximumRowsOrColumnsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_ItemWidthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_ItemHeightProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_GroupHeaderPlacementProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_CacheLengthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]

    _factory = True


class IItemsWrapGridStatics2(_inspectable.IInspectable):
    get_AreStickyGroupHeadersEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                        _type.HRESULT]

    _factory = True


class IListBox(_inspectable.IInspectable):
    get_SelectedItems: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_inspectable.IInspectable]]],  # value
                                 _type.HRESULT]
    get_SelectionMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.SelectionMode]],  # value
                                 _type.HRESULT]
    put_SelectionMode: _Callable[[_enum.Windows.UI.Xaml.Controls.SelectionMode],  # value
                                 _type.HRESULT]
    ScrollIntoView: _Callable[[_inspectable.IInspectable],  # item
                              _type.HRESULT]
    SelectAll: _Callable[[],
                         _type.HRESULT]


class IListBox2(_inspectable.IInspectable):
    get_SingleSelectionFollowsFocus: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]
    put_SingleSelectionFollowsFocus: _Callable[[_type.boolean],  # value
                                               _type.HRESULT]


class IListBoxFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IListBox]],  # value
                              _type.HRESULT]


class IListBoxItem(_inspectable.IInspectable):
    pass


class IListBoxItemFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IListBoxItem]],  # value
                              _type.HRESULT]


class IListBoxStatics(_inspectable.IInspectable):
    get_SelectionModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]

    _factory = True


class IListBoxStatics2(_inspectable.IInspectable):
    get_SingleSelectionFollowsFocusProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]

    _factory = True


class IListPickerFlyout(_inspectable.IInspectable):
    get_ItemsSource: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                               _type.HRESULT]
    put_ItemsSource: _Callable[[_inspectable.IInspectable],  # value
                               _type.HRESULT]
    get_ItemTemplate: _Callable[[_Pointer[_Windows_UI_Xaml.IDataTemplate]],  # value
                                _type.HRESULT]
    put_ItemTemplate: _Callable[[_Windows_UI_Xaml.IDataTemplate],  # value
                                _type.HRESULT]
    get_DisplayMemberPath: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    put_DisplayMemberPath: _Callable[[_type.HSTRING],  # value
                                     _type.HRESULT]
    get_SelectionMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.ListPickerFlyoutSelectionMode]],  # value
                                 _type.HRESULT]
    put_SelectionMode: _Callable[[_enum.Windows.UI.Xaml.Controls.ListPickerFlyoutSelectionMode],  # value
                                 _type.HRESULT]
    get_SelectedIndex: _Callable[[_Pointer[_type.INT32]],  # value
                                 _type.HRESULT]
    put_SelectedIndex: _Callable[[_type.INT32],  # value
                                 _type.HRESULT]
    get_SelectedItem: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                _type.HRESULT]
    put_SelectedItem: _Callable[[_inspectable.IInspectable],  # value
                                _type.HRESULT]
    get_SelectedValue: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                 _type.HRESULT]
    put_SelectedValue: _Callable[[_inspectable.IInspectable],  # value
                                 _type.HRESULT]
    get_SelectedValuePath: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    put_SelectedValuePath: _Callable[[_type.HSTRING],  # value
                                     _type.HRESULT]
    get_SelectedItems: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_inspectable.IInspectable]]],  # value
                                 _type.HRESULT]
    add_ItemsPicked: _Callable[[_Windows_Foundation.ITypedEventHandler[IListPickerFlyout, IItemsPickedEventArgs],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_ItemsPicked: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    ShowAtAsync: _Callable[[_Windows_UI_Xaml.IFrameworkElement,  # target
                            _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_inspectable.IInspectable]]]],  # operation
                           _type.HRESULT]


class IListPickerFlyoutPresenter(_inspectable.IInspectable):
    pass


class IListPickerFlyoutStatics(_inspectable.IInspectable):
    get_ItemsSourceProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_ItemTemplateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_DisplayMemberPathProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_SelectionModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_SelectedIndexProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_SelectedItemProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_SelectedValueProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_SelectedValuePathProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]

    _factory = True


class IListView(_inspectable.IInspectable):
    pass


class IListViewBase(_inspectable.IInspectable):
    get_SelectedItems: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_inspectable.IInspectable]]],  # value
                                 _type.HRESULT]
    get_SelectionMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.ListViewSelectionMode]],  # value
                                 _type.HRESULT]
    put_SelectionMode: _Callable[[_enum.Windows.UI.Xaml.Controls.ListViewSelectionMode],  # value
                                 _type.HRESULT]
    get_IsSwipeEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    put_IsSwipeEnabled: _Callable[[_type.boolean],  # value
                                  _type.HRESULT]
    get_CanDragItems: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_CanDragItems: _Callable[[_type.boolean],  # value
                                _type.HRESULT]
    get_CanReorderItems: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    put_CanReorderItems: _Callable[[_type.boolean],  # value
                                   _type.HRESULT]
    get_IsItemClickEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_IsItemClickEnabled: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    get_DataFetchSize: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                 _type.HRESULT]
    put_DataFetchSize: _Callable[[_type.DOUBLE],  # value
                                 _type.HRESULT]
    get_IncrementalLoadingThreshold: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                               _type.HRESULT]
    put_IncrementalLoadingThreshold: _Callable[[_type.DOUBLE],  # value
                                               _type.HRESULT]
    get_IncrementalLoadingTrigger: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.IncrementalLoadingTrigger]],  # value
                                             _type.HRESULT]
    put_IncrementalLoadingTrigger: _Callable[[_enum.Windows.UI.Xaml.Controls.IncrementalLoadingTrigger],  # value
                                             _type.HRESULT]
    add_ItemClick: _Callable[[IItemClickEventHandler,  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_ItemClick: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    add_DragItemsStarting: _Callable[[IDragItemsStartingEventHandler,  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_DragItemsStarting: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    ScrollIntoView: _Callable[[_inspectable.IInspectable],  # item
                              _type.HRESULT]
    SelectAll: _Callable[[],
                         _type.HRESULT]
    LoadMoreItemsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_struct.Windows.UI.Xaml.Data.LoadMoreItemsResult]]],  # operation
                                  _type.HRESULT]
    ScrollIntoViewWithAlignment: _Callable[[_inspectable.IInspectable,  # item
                                            _enum.Windows.UI.Xaml.Controls.ScrollIntoViewAlignment],  # alignment
                                           _type.HRESULT]
    get_Header: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                          _type.HRESULT]
    put_Header: _Callable[[_inspectable.IInspectable],  # value
                          _type.HRESULT]
    get_HeaderTemplate: _Callable[[_Pointer[_Windows_UI_Xaml.IDataTemplate]],  # value
                                  _type.HRESULT]
    put_HeaderTemplate: _Callable[[_Windows_UI_Xaml.IDataTemplate],  # value
                                  _type.HRESULT]
    get_HeaderTransitions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Media_Animation.ITransition]]],  # value
                                     _type.HRESULT]
    put_HeaderTransitions: _Callable[[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Media_Animation.ITransition]],  # value
                                     _type.HRESULT]


class IListViewBase2(_inspectable.IInspectable):
    get_ShowsScrollingPlaceholders: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]
    put_ShowsScrollingPlaceholders: _Callable[[_type.boolean],  # value
                                              _type.HRESULT]
    add_ContainerContentChanging: _Callable[[_Windows_Foundation.ITypedEventHandler[IListViewBase, IContainerContentChangingEventArgs],  # handler
                                             _Pointer[_struct.EventRegistrationToken]],  # token
                                            _type.HRESULT]
    remove_ContainerContentChanging: _Callable[[_struct.EventRegistrationToken],  # token
                                               _type.HRESULT]
    SetDesiredContainerUpdateDuration: _Callable[[_struct.Windows.Foundation.TimeSpan],  # duration
                                                 _type.HRESULT]
    get_Footer: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                          _type.HRESULT]
    put_Footer: _Callable[[_inspectable.IInspectable],  # value
                          _type.HRESULT]
    get_FooterTemplate: _Callable[[_Pointer[_Windows_UI_Xaml.IDataTemplate]],  # value
                                  _type.HRESULT]
    put_FooterTemplate: _Callable[[_Windows_UI_Xaml.IDataTemplate],  # value
                                  _type.HRESULT]
    get_FooterTransitions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Media_Animation.ITransition]]],  # value
                                     _type.HRESULT]
    put_FooterTransitions: _Callable[[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Media_Animation.ITransition]],  # value
                                     _type.HRESULT]


class IListViewBase3(_inspectable.IInspectable):
    get_ReorderMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.ListViewReorderMode]],  # value
                               _type.HRESULT]
    put_ReorderMode: _Callable[[_enum.Windows.UI.Xaml.Controls.ListViewReorderMode],  # value
                               _type.HRESULT]


class IListViewBase4(_inspectable.IInspectable):
    get_SelectedRanges: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_UI_Xaml_Data.IItemIndexRange]]],  # value
                                  _type.HRESULT]
    get_IsMultiSelectCheckBoxEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                _type.HRESULT]
    put_IsMultiSelectCheckBoxEnabled: _Callable[[_type.boolean],  # value
                                                _type.HRESULT]
    add_DragItemsCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IListViewBase, IDragItemsCompletedEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_DragItemsCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_ChoosingItemContainer: _Callable[[_Windows_Foundation.ITypedEventHandler[IListViewBase, IChoosingItemContainerEventArgs],  # handler
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_ChoosingItemContainer: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]
    add_ChoosingGroupHeaderContainer: _Callable[[_Windows_Foundation.ITypedEventHandler[IListViewBase, IChoosingGroupHeaderContainerEventArgs],  # handler
                                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                                _type.HRESULT]
    remove_ChoosingGroupHeaderContainer: _Callable[[_struct.EventRegistrationToken],  # token
                                                   _type.HRESULT]
    SelectRange: _Callable[[_Windows_UI_Xaml_Data.IItemIndexRange],  # itemIndexRange
                           _type.HRESULT]
    DeselectRange: _Callable[[_Windows_UI_Xaml_Data.IItemIndexRange],  # itemIndexRange
                             _type.HRESULT]


class IListViewBase5(_inspectable.IInspectable):
    get_SingleSelectionFollowsFocus: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]
    put_SingleSelectionFollowsFocus: _Callable[[_type.boolean],  # value
                                               _type.HRESULT]
    IsDragSource: _Callable[[_Pointer[_type.boolean]],  # result
                            _type.HRESULT]


class IListViewBase6(_inspectable.IInspectable):
    TryStartConnectedAnimationAsync: _Callable[[_Windows_UI_Xaml_Media_Animation.IConnectedAnimation,  # animation
                                                _inspectable.IInspectable,  # item
                                                _type.HSTRING,  # elementName
                                                _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                               _type.HRESULT]
    PrepareConnectedAnimation: _Callable[[_type.HSTRING,  # key
                                          _inspectable.IInspectable,  # item
                                          _type.HSTRING,  # elementName
                                          _Pointer[_Windows_UI_Xaml_Media_Animation.IConnectedAnimation]],  # result
                                         _type.HRESULT]


class IListViewBaseFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IListViewBase]],  # value
                              _type.HRESULT]


class IListViewBaseHeaderItem(_inspectable.IInspectable):
    pass


class IListViewBaseHeaderItemFactory(_inspectable.IInspectable):
    pass


class IListViewBaseStatics(_inspectable.IInspectable):
    get_SelectionModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_IsSwipeEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_CanDragItemsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_CanReorderItemsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_IsItemClickEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_DataFetchSizeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_IncrementalLoadingThresholdProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]
    get_IncrementalLoadingTriggerProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                     _type.HRESULT]
    get_SemanticZoomOwnerProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_IsActiveViewProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_IsZoomedInViewProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_HeaderProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_HeaderTemplateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_HeaderTransitionsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]

    _factory = True


class IListViewBaseStatics2(_inspectable.IInspectable):
    get_ShowsScrollingPlaceholdersProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                      _type.HRESULT]
    get_FooterProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_FooterTemplateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_FooterTransitionsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]

    _factory = True


class IListViewBaseStatics3(_inspectable.IInspectable):
    get_ReorderModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]

    _factory = True


class IListViewBaseStatics4(_inspectable.IInspectable):
    get_IsMultiSelectCheckBoxEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                        _type.HRESULT]

    _factory = True


class IListViewBaseStatics5(_inspectable.IInspectable):
    get_SingleSelectionFollowsFocusProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]

    _factory = True


class IListViewFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IListView]],  # value
                              _type.HRESULT]


class IListViewHeaderItem(_inspectable.IInspectable):
    pass


class IListViewHeaderItemFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IListViewHeaderItem]],  # value
                              _type.HRESULT]


class IListViewItem(_inspectable.IInspectable):
    get_TemplateSettings: _Callable[[_Pointer[_Windows_UI_Xaml_Controls_Primitives.IListViewItemTemplateSettings]],  # value
                                    _type.HRESULT]


class IListViewItemFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IListViewItem]],  # value
                              _type.HRESULT]


class IListViewPersistenceHelper(_inspectable.IInspectable):
    pass


class IListViewPersistenceHelperStatics(_inspectable.IInspectable):
    GetRelativeScrollPosition: _Callable[[IListViewBase,  # listViewBase
                                          IListViewItemToKeyHandler,  # itemToKeyHandler
                                          _Pointer[_type.HSTRING]],  # result
                                         _type.HRESULT]
    SetRelativeScrollPositionAsync: _Callable[[IListViewBase,  # listViewBase
                                               _type.HSTRING,  # relativeScrollPosition
                                               IListViewKeyToItemHandler,  # keyToItemHandler
                                               _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                              _type.HRESULT]

    _factory = True


class IMediaElement(_inspectable.IInspectable):
    get_PosterSource: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IImageSource]],  # value
                                _type.HRESULT]
    put_PosterSource: _Callable[[_Windows_UI_Xaml_Media.IImageSource],  # value
                                _type.HRESULT]
    get_Source: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                          _type.HRESULT]
    put_Source: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                          _type.HRESULT]
    get_IsMuted: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_IsMuted: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_IsAudioOnly: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_AutoPlay: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    put_AutoPlay: _Callable[[_type.boolean],  # value
                            _type.HRESULT]
    get_Volume: _Callable[[_Pointer[_type.DOUBLE]],  # value
                          _type.HRESULT]
    put_Volume: _Callable[[_type.DOUBLE],  # value
                          _type.HRESULT]
    get_Balance: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    put_Balance: _Callable[[_type.DOUBLE],  # value
                           _type.HRESULT]
    get_NaturalVideoHeight: _Callable[[_Pointer[_type.INT32]],  # value
                                      _type.HRESULT]
    get_NaturalVideoWidth: _Callable[[_Pointer[_type.INT32]],  # value
                                     _type.HRESULT]
    get_NaturalDuration: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Duration]],  # value
                                   _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    put_Position: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                            _type.HRESULT]
    get_DownloadProgress: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]
    get_BufferingProgress: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                     _type.HRESULT]
    get_DownloadProgressOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                          _type.HRESULT]
    get_CurrentState: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Media.MediaElementState]],  # value
                                _type.HRESULT]
    get_Markers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Media.ITimelineMarker]]],  # value
                           _type.HRESULT]
    get_CanSeek: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_CanPause: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_AudioStreamCount: _Callable[[_Pointer[_type.INT32]],  # value
                                    _type.HRESULT]
    get_AudioStreamIndex: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                    _type.HRESULT]
    put_AudioStreamIndex: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                                    _type.HRESULT]
    get_PlaybackRate: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    put_PlaybackRate: _Callable[[_type.DOUBLE],  # value
                                _type.HRESULT]
    get_IsLooping: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsLooping: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    PlayToSource: _Callable[[_Pointer[_Windows_Media_PlayTo.IPlayToSource]],  # value
                            _type.HRESULT]
    get_DefaultPlaybackRate: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                       _type.HRESULT]
    put_DefaultPlaybackRate: _Callable[[_type.DOUBLE],  # value
                                       _type.HRESULT]
    get_AspectRatioWidth: _Callable[[_Pointer[_type.INT32]],  # value
                                    _type.HRESULT]
    get_AspectRatioHeight: _Callable[[_Pointer[_type.INT32]],  # value
                                     _type.HRESULT]
    get_RealTimePlayback: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_RealTimePlayback: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_AudioCategory: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Media.AudioCategory]],  # value
                                 _type.HRESULT]
    put_AudioCategory: _Callable[[_enum.Windows.UI.Xaml.Media.AudioCategory],  # value
                                 _type.HRESULT]
    get_AudioDeviceType: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Media.AudioDeviceType]],  # value
                                   _type.HRESULT]
    put_AudioDeviceType: _Callable[[_enum.Windows.UI.Xaml.Media.AudioDeviceType],  # value
                                   _type.HRESULT]
    get_ProtectionManager: _Callable[[_Pointer[_Windows_Media_Protection.IMediaProtectionManager]],  # value
                                     _type.HRESULT]
    put_ProtectionManager: _Callable[[_Windows_Media_Protection.IMediaProtectionManager],  # value
                                     _type.HRESULT]
    get_Stereo3DVideoPackingMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Media.Stereo3DVideoPackingMode]],  # value
                                            _type.HRESULT]
    put_Stereo3DVideoPackingMode: _Callable[[_enum.Windows.UI.Xaml.Media.Stereo3DVideoPackingMode],  # value
                                            _type.HRESULT]
    get_Stereo3DVideoRenderMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Media.Stereo3DVideoRenderMode]],  # value
                                           _type.HRESULT]
    put_Stereo3DVideoRenderMode: _Callable[[_enum.Windows.UI.Xaml.Media.Stereo3DVideoRenderMode],  # value
                                           _type.HRESULT]
    get_IsStereo3DVideo: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    add_MediaOpened: _Callable[[_Windows_UI_Xaml.IRoutedEventHandler,  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_MediaOpened: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    add_MediaEnded: _Callable[[_Windows_UI_Xaml.IRoutedEventHandler,  # handler
                               _Pointer[_struct.EventRegistrationToken]],  # token
                              _type.HRESULT]
    remove_MediaEnded: _Callable[[_struct.EventRegistrationToken],  # token
                                 _type.HRESULT]
    add_MediaFailed: _Callable[[_Windows_UI_Xaml.IExceptionRoutedEventHandler,  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_MediaFailed: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    add_DownloadProgressChanged: _Callable[[_Windows_UI_Xaml.IRoutedEventHandler,  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_DownloadProgressChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]
    add_BufferingProgressChanged: _Callable[[_Windows_UI_Xaml.IRoutedEventHandler,  # handler
                                             _Pointer[_struct.EventRegistrationToken]],  # token
                                            _type.HRESULT]
    remove_BufferingProgressChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                               _type.HRESULT]
    add_CurrentStateChanged: _Callable[[_Windows_UI_Xaml.IRoutedEventHandler,  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_CurrentStateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_MarkerReached: _Callable[[_Windows_UI_Xaml_Media.ITimelineMarkerRoutedEventHandler,  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_MarkerReached: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_RateChanged: _Callable[[_Windows_UI_Xaml_Media.IRateChangedRoutedEventHandler,  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_RateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    add_VolumeChanged: _Callable[[_Windows_UI_Xaml.IRoutedEventHandler,  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_VolumeChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_SeekCompleted: _Callable[[_Windows_UI_Xaml.IRoutedEventHandler,  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_SeekCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    Play: _Callable[[],
                    _type.HRESULT]
    Pause: _Callable[[],
                     _type.HRESULT]
    CanPlayType: _Callable[[_type.HSTRING,  # type
                            _Pointer[_enum.Windows.UI.Xaml.Media.MediaCanPlayResponse]],  # result
                           _type.HRESULT]
    SetSource: _Callable[[_Windows_Storage_Streams.IRandomAccessStream,  # stream
                          _type.HSTRING],  # mimeType
                         _type.HRESULT]
    GetAudioStreamLanguage: _Callable[[_Windows_Foundation.IReference[_type.INT32],  # index
                                       _Pointer[_type.HSTRING]],  # result
                                      _type.HRESULT]
    AddAudioEffect: _Callable[[_type.HSTRING,  # effectID
                               _type.boolean,  # effectOptional
                               _Windows_Foundation_Collections.IPropertySet],  # effectConfiguration
                              _type.HRESULT]
    AddVideoEffect: _Callable[[_type.HSTRING,  # effectID
                               _type.boolean,  # effectOptional
                               _Windows_Foundation_Collections.IPropertySet],  # effectConfiguration
                              _type.HRESULT]
    RemoveAllEffects: _Callable[[],
                                _type.HRESULT]
    get_ActualStereo3DVideoPackingMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Media.Stereo3DVideoPackingMode]],  # value
                                                  _type.HRESULT]


class IMediaElement2(_inspectable.IInspectable):
    get_AreTransportControlsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]
    put_AreTransportControlsEnabled: _Callable[[_type.boolean],  # value
                                               _type.HRESULT]
    get_Stretch: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Media.Stretch]],  # value
                           _type.HRESULT]
    put_Stretch: _Callable[[_enum.Windows.UI.Xaml.Media.Stretch],  # value
                           _type.HRESULT]
    get_IsFullWindow: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_IsFullWindow: _Callable[[_type.boolean],  # value
                                _type.HRESULT]
    SetMediaStreamSource: _Callable[[_Windows_Media_Core.IMediaSource],  # source
                                    _type.HRESULT]
    PlayToPreferredSourceUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                                        _type.HRESULT]


class IMediaElement3(_inspectable.IInspectable):
    get_TransportControls: _Callable[[_Pointer[IMediaTransportControls]],  # value
                                     _type.HRESULT]
    put_TransportControls: _Callable[[IMediaTransportControls],  # value
                                     _type.HRESULT]
    add_PartialMediaFailureDetected: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaElement, _Windows_UI_Xaml_Media.IPartialMediaFailureDetectedEventArgs],  # handler
                                                _Pointer[_struct.EventRegistrationToken]],  # token
                                               _type.HRESULT]
    remove_PartialMediaFailureDetected: _Callable[[_struct.EventRegistrationToken],  # token
                                                  _type.HRESULT]
    SetPlaybackSource: _Callable[[_Windows_Media_Playback.IMediaPlaybackSource],  # source
                                 _type.HRESULT]
    GetAsCastingSource: _Callable[[_Pointer[_Windows_Media_Casting.ICastingSource]],  # result
                                  _type.HRESULT]


class IMediaElementStatics(_inspectable.IInspectable):
    get_PosterSourceProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_SourceProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_IsMutedProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_IsAudioOnlyProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_AutoPlayProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_VolumeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_BalanceProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_NaturalVideoHeightProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_NaturalVideoWidthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_NaturalDurationProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_PositionProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_DownloadProgressProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_BufferingProgressProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_DownloadProgressOffsetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]
    get_CurrentStateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_CanSeekProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_CanPauseProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_AudioStreamCountProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_AudioStreamIndexProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_PlaybackRateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_IsLoopingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    PlayToSourceProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_DefaultPlaybackRateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_AspectRatioWidthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_AspectRatioHeightProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_RealTimePlaybackProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_AudioCategoryProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_AudioDeviceTypeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_ProtectionManagerProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_Stereo3DVideoPackingModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]
    get_Stereo3DVideoRenderModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_IsStereo3DVideoProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_ActualStereo3DVideoPackingModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                          _type.HRESULT]

    _factory = True


class IMediaElementStatics2(_inspectable.IInspectable):
    get_AreTransportControlsEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]
    get_StretchProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_IsFullWindowProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    PlayToPreferredSourceUriProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]

    _factory = True


class IMediaPlayerElement(_inspectable.IInspectable):
    get_Source: _Callable[[_Pointer[_Windows_Media_Playback.IMediaPlaybackSource]],  # value
                          _type.HRESULT]
    put_Source: _Callable[[_Windows_Media_Playback.IMediaPlaybackSource],  # value
                          _type.HRESULT]
    get_TransportControls: _Callable[[_Pointer[IMediaTransportControls]],  # value
                                     _type.HRESULT]
    put_TransportControls: _Callable[[IMediaTransportControls],  # value
                                     _type.HRESULT]
    get_AreTransportControlsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]
    put_AreTransportControlsEnabled: _Callable[[_type.boolean],  # value
                                               _type.HRESULT]
    get_PosterSource: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IImageSource]],  # value
                                _type.HRESULT]
    put_PosterSource: _Callable[[_Windows_UI_Xaml_Media.IImageSource],  # value
                                _type.HRESULT]
    get_Stretch: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Media.Stretch]],  # value
                           _type.HRESULT]
    put_Stretch: _Callable[[_enum.Windows.UI.Xaml.Media.Stretch],  # value
                           _type.HRESULT]
    get_AutoPlay: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    put_AutoPlay: _Callable[[_type.boolean],  # value
                            _type.HRESULT]
    get_IsFullWindow: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_IsFullWindow: _Callable[[_type.boolean],  # value
                                _type.HRESULT]
    get_MediaPlayer: _Callable[[_Pointer[_Windows_Media_Playback.IMediaPlayer]],  # value
                               _type.HRESULT]
    SetMediaPlayer: _Callable[[_Windows_Media_Playback.IMediaPlayer],  # mediaPlayer
                              _type.HRESULT]


class IMediaPlayerElementFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IMediaPlayerElement]],  # value
                              _type.HRESULT]


class IMediaPlayerElementStatics(_inspectable.IInspectable):
    get_SourceProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_AreTransportControlsEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]
    get_PosterSourceProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_StretchProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_AutoPlayProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_IsFullWindowProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_MediaPlayerProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]

    _factory = True


class IMediaPlayerPresenter(_inspectable.IInspectable):
    get_MediaPlayer: _Callable[[_Pointer[_Windows_Media_Playback.IMediaPlayer]],  # value
                               _type.HRESULT]
    put_MediaPlayer: _Callable[[_Windows_Media_Playback.IMediaPlayer],  # value
                               _type.HRESULT]
    get_Stretch: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Media.Stretch]],  # value
                           _type.HRESULT]
    put_Stretch: _Callable[[_enum.Windows.UI.Xaml.Media.Stretch],  # value
                           _type.HRESULT]
    get_IsFullWindow: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_IsFullWindow: _Callable[[_type.boolean],  # value
                                _type.HRESULT]


class IMediaPlayerPresenterFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IMediaPlayerPresenter]],  # value
                              _type.HRESULT]


class IMediaPlayerPresenterStatics(_inspectable.IInspectable):
    get_MediaPlayerProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_StretchProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_IsFullWindowProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]

    _factory = True


class IMediaTransportControls(_inspectable.IInspectable):
    get_IsFullWindowButtonVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    put_IsFullWindowButtonVisible: _Callable[[_type.boolean],  # value
                                             _type.HRESULT]
    get_IsFullWindowEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_IsFullWindowEnabled: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_IsZoomButtonVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_IsZoomButtonVisible: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_IsZoomEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_IsZoomEnabled: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_IsFastForwardButtonVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]
    put_IsFastForwardButtonVisible: _Callable[[_type.boolean],  # value
                                              _type.HRESULT]
    get_IsFastForwardEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    put_IsFastForwardEnabled: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]
    get_IsFastRewindButtonVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    put_IsFastRewindButtonVisible: _Callable[[_type.boolean],  # value
                                             _type.HRESULT]
    get_IsFastRewindEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_IsFastRewindEnabled: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_IsStopButtonVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_IsStopButtonVisible: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_IsStopEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_IsStopEnabled: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_IsVolumeButtonVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_IsVolumeButtonVisible: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]
    get_IsVolumeEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    put_IsVolumeEnabled: _Callable[[_type.boolean],  # value
                                   _type.HRESULT]
    get_IsPlaybackRateButtonVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]
    put_IsPlaybackRateButtonVisible: _Callable[[_type.boolean],  # value
                                               _type.HRESULT]
    get_IsPlaybackRateEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_IsPlaybackRateEnabled: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]
    get_IsSeekBarVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_IsSeekBarVisible: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_IsSeekEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_IsSeekEnabled: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_IsCompact: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsCompact: _Callable[[_type.boolean],  # value
                             _type.HRESULT]


class IMediaTransportControls2(_inspectable.IInspectable):
    get_IsSkipForwardButtonVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]
    put_IsSkipForwardButtonVisible: _Callable[[_type.boolean],  # value
                                              _type.HRESULT]
    get_IsSkipForwardEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    put_IsSkipForwardEnabled: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]
    get_IsSkipBackwardButtonVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]
    put_IsSkipBackwardButtonVisible: _Callable[[_type.boolean],  # value
                                               _type.HRESULT]
    get_IsSkipBackwardEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_IsSkipBackwardEnabled: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]
    get_IsNextTrackButtonVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_IsNextTrackButtonVisible: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]
    get_IsPreviousTrackButtonVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                                _type.HRESULT]
    put_IsPreviousTrackButtonVisible: _Callable[[_type.boolean],  # value
                                                _type.HRESULT]
    get_FastPlayFallbackBehaviour: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Media.FastPlayFallbackBehaviour]],  # value
                                             _type.HRESULT]
    put_FastPlayFallbackBehaviour: _Callable[[_enum.Windows.UI.Xaml.Media.FastPlayFallbackBehaviour],  # value
                                             _type.HRESULT]
    add_ThumbnailRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaTransportControls, _Windows_UI_Xaml_Media.IMediaTransportControlsThumbnailRequestedEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_ThumbnailRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]


class IMediaTransportControls3(_inspectable.IInspectable):
    get_ShowAndHideAutomatically: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_ShowAndHideAutomatically: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]
    get_IsRepeatEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    put_IsRepeatEnabled: _Callable[[_type.boolean],  # value
                                   _type.HRESULT]
    get_IsRepeatButtonVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_IsRepeatButtonVisible: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]
    Show: _Callable[[],
                    _type.HRESULT]
    Hide: _Callable[[],
                    _type.HRESULT]


class IMediaTransportControls4(_inspectable.IInspectable):
    get_IsCompactOverlayButtonVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]
    put_IsCompactOverlayButtonVisible: _Callable[[_type.boolean],  # value
                                                 _type.HRESULT]
    get_IsCompactOverlayEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    put_IsCompactOverlayEnabled: _Callable[[_type.boolean],  # value
                                           _type.HRESULT]


class IMediaTransportControlsFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IMediaTransportControls]],  # value
                              _type.HRESULT]


class IMediaTransportControlsHelper(_inspectable.IInspectable):
    pass


class IMediaTransportControlsHelperStatics(_inspectable.IInspectable):
    get_DropoutOrderProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    GetDropoutOrder: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                _Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # result
                               _type.HRESULT]
    SetDropoutOrder: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                _Windows_Foundation.IReference[_type.INT32]],  # value
                               _type.HRESULT]

    _factory = True


class IMediaTransportControlsStatics(_inspectable.IInspectable):
    get_IsFullWindowButtonVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                     _type.HRESULT]
    get_IsFullWindowEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_IsZoomButtonVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_IsZoomEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_IsFastForwardButtonVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                      _type.HRESULT]
    get_IsFastForwardEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_IsFastRewindButtonVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                     _type.HRESULT]
    get_IsFastRewindEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_IsStopButtonVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_IsStopEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_IsVolumeButtonVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_IsVolumeEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_IsPlaybackRateButtonVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]
    get_IsPlaybackRateEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_IsSeekBarVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_IsSeekEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_IsCompactProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]

    _factory = True


class IMediaTransportControlsStatics2(_inspectable.IInspectable):
    get_IsSkipForwardButtonVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                      _type.HRESULT]
    get_IsSkipForwardEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_IsSkipBackwardButtonVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]
    get_IsSkipBackwardEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_IsNextTrackButtonVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]
    get_IsPreviousTrackButtonVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                        _type.HRESULT]
    get_FastPlayFallbackBehaviourProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                     _type.HRESULT]

    _factory = True


class IMediaTransportControlsStatics3(_inspectable.IInspectable):
    get_ShowAndHideAutomaticallyProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]
    get_IsRepeatEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_IsRepeatButtonVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]

    _factory = True


class IMediaTransportControlsStatics4(_inspectable.IInspectable):
    get_IsCompactOverlayButtonVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                         _type.HRESULT]
    get_IsCompactOverlayEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]

    _factory = True


class IMenuBar(_inspectable.IInspectable):
    get_Items: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IMenuBarItem]]],  # value
                         _type.HRESULT]


class IMenuBarFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IMenuBar]],  # value
                              _type.HRESULT]


class IMenuBarItem(_inspectable.IInspectable):
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Title: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Items: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IMenuFlyoutItemBase]]],  # value
                         _type.HRESULT]


class IMenuBarItemFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IMenuBarItem]],  # value
                              _type.HRESULT]


class IMenuBarItemFlyout(_inspectable.IInspectable):
    pass


class IMenuBarItemFlyoutFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IMenuBarItemFlyout]],  # value
                              _type.HRESULT]


class IMenuBarItemStatics(_inspectable.IInspectable):
    get_TitleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_ItemsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]

    _factory = True


class IMenuBarStatics(_inspectable.IInspectable):
    get_ItemsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]

    _factory = True


class IMenuFlyout(_inspectable.IInspectable):
    get_Items: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IMenuFlyoutItemBase]]],  # value
                         _type.HRESULT]
    get_MenuFlyoutPresenterStyle: _Callable[[_Pointer[_Windows_UI_Xaml.IStyle]],  # value
                                            _type.HRESULT]
    put_MenuFlyoutPresenterStyle: _Callable[[_Windows_UI_Xaml.IStyle],  # value
                                            _type.HRESULT]


class IMenuFlyout2(_inspectable.IInspectable):
    ShowAt: _Callable[[_Windows_UI_Xaml.IUIElement,  # targetElement
                       _struct.Windows.Foundation.Point],  # point
                      _type.HRESULT]


class IMenuFlyoutFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IMenuFlyout]],  # value
                              _type.HRESULT]


class IMenuFlyoutItem(_inspectable.IInspectable):
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Text: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_Command: _Callable[[_Pointer[_Windows_UI_Xaml_Input.ICommand]],  # value
                           _type.HRESULT]
    put_Command: _Callable[[_Windows_UI_Xaml_Input.ICommand],  # value
                           _type.HRESULT]
    get_CommandParameter: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                    _type.HRESULT]
    put_CommandParameter: _Callable[[_inspectable.IInspectable],  # value
                                    _type.HRESULT]
    add_Click: _Callable[[_Windows_UI_Xaml.IRoutedEventHandler,  # handler
                          _Pointer[_struct.EventRegistrationToken]],  # token
                         _type.HRESULT]
    remove_Click: _Callable[[_struct.EventRegistrationToken],  # token
                            _type.HRESULT]


class IMenuFlyoutItem2(_inspectable.IInspectable):
    get_Icon: _Callable[[_Pointer[IIconElement]],  # value
                        _type.HRESULT]
    put_Icon: _Callable[[IIconElement],  # value
                        _type.HRESULT]


class IMenuFlyoutItem3(_inspectable.IInspectable):
    get_KeyboardAcceleratorTextOverride: _Callable[[_Pointer[_type.HSTRING]],  # value
                                                   _type.HRESULT]
    put_KeyboardAcceleratorTextOverride: _Callable[[_type.HSTRING],  # value
                                                   _type.HRESULT]
    get_TemplateSettings: _Callable[[_Pointer[_Windows_UI_Xaml_Controls_Primitives.IMenuFlyoutItemTemplateSettings]],  # value
                                    _type.HRESULT]


class IMenuFlyoutItemBase(_inspectable.IInspectable):
    pass


class IMenuFlyoutItemBaseFactory(_inspectable.IInspectable):
    pass


class IMenuFlyoutItemFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IMenuFlyoutItem]],  # value
                              _type.HRESULT]


class IMenuFlyoutItemStatics(_inspectable.IInspectable):
    get_TextProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]
    get_CommandProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_CommandParameterProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]

    _factory = True


class IMenuFlyoutItemStatics2(_inspectable.IInspectable):
    get_IconProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]

    _factory = True


class IMenuFlyoutItemStatics3(_inspectable.IInspectable):
    get_KeyboardAcceleratorTextOverrideProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                           _type.HRESULT]

    _factory = True


class IMenuFlyoutPresenter(_inspectable.IInspectable):
    pass


class IMenuFlyoutPresenter2(_inspectable.IInspectable):
    get_TemplateSettings: _Callable[[_Pointer[_Windows_UI_Xaml_Controls_Primitives.IMenuFlyoutPresenterTemplateSettings]],  # value
                                    _type.HRESULT]


class IMenuFlyoutPresenter3(_inspectable.IInspectable):
    get_IsDefaultShadowEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_IsDefaultShadowEnabled: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]


class IMenuFlyoutPresenterFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IMenuFlyoutPresenter]],  # value
                              _type.HRESULT]


class IMenuFlyoutPresenterStatics3(_inspectable.IInspectable):
    get_IsDefaultShadowEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]

    _factory = True


class IMenuFlyoutSeparator(_inspectable.IInspectable):
    pass


class IMenuFlyoutSeparatorFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IMenuFlyoutSeparator]],  # value
                              _type.HRESULT]


class IMenuFlyoutStatics(_inspectable.IInspectable):
    get_MenuFlyoutPresenterStyleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]

    _factory = True


class IMenuFlyoutSubItem(_inspectable.IInspectable):
    get_Items: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IMenuFlyoutItemBase]]],  # value
                         _type.HRESULT]
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Text: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]


class IMenuFlyoutSubItem2(_inspectable.IInspectable):
    get_Icon: _Callable[[_Pointer[IIconElement]],  # value
                        _type.HRESULT]
    put_Icon: _Callable[[IIconElement],  # value
                        _type.HRESULT]


class IMenuFlyoutSubItemStatics(_inspectable.IInspectable):
    get_TextProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]

    _factory = True


class IMenuFlyoutSubItemStatics2(_inspectable.IInspectable):
    get_IconProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]

    _factory = True


class INavigate(_inspectable.IInspectable):
    Navigate: _Callable[[_struct.Windows.UI.Xaml.Interop.TypeName,  # sourcePageType
                         _Pointer[_type.boolean]],  # result
                        _type.HRESULT]


class INavigationView(_inspectable.IInspectable):
    get_IsPaneOpen: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    put_IsPaneOpen: _Callable[[_type.boolean],  # value
                              _type.HRESULT]
    get_CompactModeThresholdWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                             _type.HRESULT]
    put_CompactModeThresholdWidth: _Callable[[_type.DOUBLE],  # value
                                             _type.HRESULT]
    get_ExpandedModeThresholdWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                              _type.HRESULT]
    put_ExpandedModeThresholdWidth: _Callable[[_type.DOUBLE],  # value
                                              _type.HRESULT]
    get_PaneFooter: _Callable[[_Pointer[_Windows_UI_Xaml.IUIElement]],  # value
                              _type.HRESULT]
    put_PaneFooter: _Callable[[_Windows_UI_Xaml.IUIElement],  # value
                              _type.HRESULT]
    get_Header: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                          _type.HRESULT]
    put_Header: _Callable[[_inspectable.IInspectable],  # value
                          _type.HRESULT]
    get_HeaderTemplate: _Callable[[_Pointer[_Windows_UI_Xaml.IDataTemplate]],  # value
                                  _type.HRESULT]
    put_HeaderTemplate: _Callable[[_Windows_UI_Xaml.IDataTemplate],  # value
                                  _type.HRESULT]
    get_DisplayMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.NavigationViewDisplayMode]],  # value
                               _type.HRESULT]
    get_IsSettingsVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    put_IsSettingsVisible: _Callable[[_type.boolean],  # value
                                     _type.HRESULT]
    get_IsPaneToggleButtonVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    put_IsPaneToggleButtonVisible: _Callable[[_type.boolean],  # value
                                             _type.HRESULT]
    get_AlwaysShowHeader: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_AlwaysShowHeader: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_CompactPaneLength: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                     _type.HRESULT]
    put_CompactPaneLength: _Callable[[_type.DOUBLE],  # value
                                     _type.HRESULT]
    get_OpenPaneLength: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    put_OpenPaneLength: _Callable[[_type.DOUBLE],  # value
                                  _type.HRESULT]
    get_PaneToggleButtonStyle: _Callable[[_Pointer[_Windows_UI_Xaml.IStyle]],  # value
                                         _type.HRESULT]
    put_PaneToggleButtonStyle: _Callable[[_Windows_UI_Xaml.IStyle],  # value
                                         _type.HRESULT]
    get_SelectedItem: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                _type.HRESULT]
    put_SelectedItem: _Callable[[_inspectable.IInspectable],  # value
                                _type.HRESULT]
    get_MenuItems: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_inspectable.IInspectable]]],  # value
                             _type.HRESULT]
    get_MenuItemsSource: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                   _type.HRESULT]
    put_MenuItemsSource: _Callable[[_inspectable.IInspectable],  # value
                                   _type.HRESULT]
    get_SettingsItem: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                _type.HRESULT]
    get_AutoSuggestBox: _Callable[[_Pointer[IAutoSuggestBox]],  # value
                                  _type.HRESULT]
    put_AutoSuggestBox: _Callable[[IAutoSuggestBox],  # value
                                  _type.HRESULT]
    get_MenuItemTemplate: _Callable[[_Pointer[_Windows_UI_Xaml.IDataTemplate]],  # value
                                    _type.HRESULT]
    put_MenuItemTemplate: _Callable[[_Windows_UI_Xaml.IDataTemplate],  # value
                                    _type.HRESULT]
    get_MenuItemTemplateSelector: _Callable[[_Pointer[IDataTemplateSelector]],  # value
                                            _type.HRESULT]
    put_MenuItemTemplateSelector: _Callable[[IDataTemplateSelector],  # value
                                            _type.HRESULT]
    get_MenuItemContainerStyle: _Callable[[_Pointer[_Windows_UI_Xaml.IStyle]],  # value
                                          _type.HRESULT]
    put_MenuItemContainerStyle: _Callable[[_Windows_UI_Xaml.IStyle],  # value
                                          _type.HRESULT]
    get_MenuItemContainerStyleSelector: _Callable[[_Pointer[IStyleSelector]],  # value
                                                  _type.HRESULT]
    put_MenuItemContainerStyleSelector: _Callable[[IStyleSelector],  # value
                                                  _type.HRESULT]
    MenuItemFromContainer: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # container
                                      _Pointer[_inspectable.IInspectable]],  # result
                                     _type.HRESULT]
    ContainerFromMenuItem: _Callable[[_inspectable.IInspectable,  # item
                                      _Pointer[_Windows_UI_Xaml.IDependencyObject]],  # result
                                     _type.HRESULT]
    add_SelectionChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[INavigationView, INavigationViewSelectionChangedEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_SelectionChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    add_ItemInvoked: _Callable[[_Windows_Foundation.ITypedEventHandler[INavigationView, INavigationViewItemInvokedEventArgs],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_ItemInvoked: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    add_DisplayModeChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[INavigationView, INavigationViewDisplayModeChangedEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_DisplayModeChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]


class INavigationView2(_inspectable.IInspectable):
    get_IsBackButtonVisible: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.NavigationViewBackButtonVisible]],  # value
                                       _type.HRESULT]
    put_IsBackButtonVisible: _Callable[[_enum.Windows.UI.Xaml.Controls.NavigationViewBackButtonVisible],  # value
                                       _type.HRESULT]
    get_IsBackEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_IsBackEnabled: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_PaneTitle: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_PaneTitle: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    add_BackRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[INavigationView, INavigationViewBackRequestedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_BackRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_PaneClosed: _Callable[[_Windows_Foundation.ITypedEventHandler[INavigationView, _inspectable.IInspectable],  # handler
                               _Pointer[_struct.EventRegistrationToken]],  # token
                              _type.HRESULT]
    remove_PaneClosed: _Callable[[_struct.EventRegistrationToken],  # token
                                 _type.HRESULT]
    add_PaneClosing: _Callable[[_Windows_Foundation.ITypedEventHandler[INavigationView, INavigationViewPaneClosingEventArgs],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_PaneClosing: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    add_PaneOpened: _Callable[[_Windows_Foundation.ITypedEventHandler[INavigationView, _inspectable.IInspectable],  # handler
                               _Pointer[_struct.EventRegistrationToken]],  # token
                              _type.HRESULT]
    remove_PaneOpened: _Callable[[_struct.EventRegistrationToken],  # token
                                 _type.HRESULT]
    add_PaneOpening: _Callable[[_Windows_Foundation.ITypedEventHandler[INavigationView, _inspectable.IInspectable],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_PaneOpening: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]


class INavigationView3(_inspectable.IInspectable):
    get_PaneDisplayMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.NavigationViewPaneDisplayMode]],  # value
                                   _type.HRESULT]
    put_PaneDisplayMode: _Callable[[_enum.Windows.UI.Xaml.Controls.NavigationViewPaneDisplayMode],  # value
                                   _type.HRESULT]
    get_PaneHeader: _Callable[[_Pointer[_Windows_UI_Xaml.IUIElement]],  # value
                              _type.HRESULT]
    put_PaneHeader: _Callable[[_Windows_UI_Xaml.IUIElement],  # value
                              _type.HRESULT]
    get_PaneCustomContent: _Callable[[_Pointer[_Windows_UI_Xaml.IUIElement]],  # value
                                     _type.HRESULT]
    put_PaneCustomContent: _Callable[[_Windows_UI_Xaml.IUIElement],  # value
                                     _type.HRESULT]
    get_ContentOverlay: _Callable[[_Pointer[_Windows_UI_Xaml.IUIElement]],  # value
                                  _type.HRESULT]
    put_ContentOverlay: _Callable[[_Windows_UI_Xaml.IUIElement],  # value
                                  _type.HRESULT]
    get_IsPaneVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_IsPaneVisible: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_SelectionFollowsFocus: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.NavigationViewSelectionFollowsFocus]],  # value
                                         _type.HRESULT]
    put_SelectionFollowsFocus: _Callable[[_enum.Windows.UI.Xaml.Controls.NavigationViewSelectionFollowsFocus],  # value
                                         _type.HRESULT]
    get_TemplateSettings: _Callable[[_Pointer[INavigationViewTemplateSettings]],  # value
                                    _type.HRESULT]
    get_ShoulderNavigationEnabled: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.NavigationViewShoulderNavigationEnabled]],  # value
                                             _type.HRESULT]
    put_ShoulderNavigationEnabled: _Callable[[_enum.Windows.UI.Xaml.Controls.NavigationViewShoulderNavigationEnabled],  # value
                                             _type.HRESULT]
    get_OverflowLabelMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.NavigationViewOverflowLabelMode]],  # value
                                     _type.HRESULT]
    put_OverflowLabelMode: _Callable[[_enum.Windows.UI.Xaml.Controls.NavigationViewOverflowLabelMode],  # value
                                     _type.HRESULT]


class INavigationViewBackRequestedEventArgs(_inspectable.IInspectable):
    pass


class INavigationViewDisplayModeChangedEventArgs(_inspectable.IInspectable):
    get_DisplayMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.NavigationViewDisplayMode]],  # value
                               _type.HRESULT]


class INavigationViewFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[INavigationView]],  # value
                              _type.HRESULT]


class INavigationViewItem(_inspectable.IInspectable):
    get_Icon: _Callable[[_Pointer[IIconElement]],  # value
                        _type.HRESULT]
    put_Icon: _Callable[[IIconElement],  # value
                        _type.HRESULT]
    get_CompactPaneLength: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                     _type.HRESULT]


class INavigationViewItem2(_inspectable.IInspectable):
    get_SelectsOnInvoked: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_SelectsOnInvoked: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]


class INavigationViewItemBase(_inspectable.IInspectable):
    pass


class INavigationViewItemBaseFactory(_inspectable.IInspectable):
    pass


class INavigationViewItemFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[INavigationViewItem]],  # value
                              _type.HRESULT]


class INavigationViewItemHeader(_inspectable.IInspectable):
    pass


class INavigationViewItemHeaderFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[INavigationViewItemHeader]],  # value
                              _type.HRESULT]


class INavigationViewItemInvokedEventArgs(_inspectable.IInspectable):
    get_InvokedItem: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                               _type.HRESULT]
    get_IsSettingsInvoked: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]


class INavigationViewItemInvokedEventArgs2(_inspectable.IInspectable):
    get_InvokedItemContainer: _Callable[[_Pointer[INavigationViewItemBase]],  # value
                                        _type.HRESULT]
    get_RecommendedNavigationTransitionInfo: _Callable[[_Pointer[_Windows_UI_Xaml_Media_Animation.INavigationTransitionInfo]],  # value
                                                       _type.HRESULT]


class INavigationViewItemSeparator(_inspectable.IInspectable):
    pass


class INavigationViewItemSeparatorFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[INavigationViewItemSeparator]],  # value
                              _type.HRESULT]


class INavigationViewItemStatics(_inspectable.IInspectable):
    get_IconProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]
    get_CompactPaneLengthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]

    _factory = True


class INavigationViewItemStatics2(_inspectable.IInspectable):
    get_SelectsOnInvokedProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]

    _factory = True


class INavigationViewList(_inspectable.IInspectable):
    pass


class INavigationViewListFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[INavigationViewList]],  # value
                              _type.HRESULT]


class INavigationViewPaneClosingEventArgs(_inspectable.IInspectable):
    get_Cancel: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_Cancel: _Callable[[_type.boolean],  # value
                          _type.HRESULT]


class INavigationViewSelectionChangedEventArgs(_inspectable.IInspectable):
    get_SelectedItem: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                _type.HRESULT]
    get_IsSettingsSelected: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]


class INavigationViewSelectionChangedEventArgs2(_inspectable.IInspectable):
    get_SelectedItemContainer: _Callable[[_Pointer[INavigationViewItemBase]],  # value
                                         _type.HRESULT]
    get_RecommendedNavigationTransitionInfo: _Callable[[_Pointer[_Windows_UI_Xaml_Media_Animation.INavigationTransitionInfo]],  # value
                                                       _type.HRESULT]


class INavigationViewStatics(_inspectable.IInspectable):
    get_IsPaneOpenProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_CompactModeThresholdWidthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                     _type.HRESULT]
    get_ExpandedModeThresholdWidthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                      _type.HRESULT]
    get_PaneFooterProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_HeaderProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_HeaderTemplateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_DisplayModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_IsSettingsVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_IsPaneToggleButtonVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                     _type.HRESULT]
    get_AlwaysShowHeaderProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_CompactPaneLengthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_OpenPaneLengthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_PaneToggleButtonStyleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_MenuItemsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_MenuItemsSourceProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_SelectedItemProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_SettingsItemProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_AutoSuggestBoxProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_MenuItemTemplateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_MenuItemTemplateSelectorProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]
    get_MenuItemContainerStyleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]
    get_MenuItemContainerStyleSelectorProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                          _type.HRESULT]

    _factory = True


class INavigationViewStatics2(_inspectable.IInspectable):
    get_IsBackButtonVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_IsBackEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_PaneTitleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]

    _factory = True


class INavigationViewStatics3(_inspectable.IInspectable):
    get_PaneDisplayModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_PaneHeaderProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_PaneCustomContentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_ContentOverlayProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_IsPaneVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_SelectionFollowsFocusProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_TemplateSettingsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_ShoulderNavigationEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                     _type.HRESULT]
    get_OverflowLabelModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]

    _factory = True


class INavigationViewTemplateSettings(_inspectable.IInspectable):
    get_TopPadding: _Callable[[_Pointer[_type.DOUBLE]],  # value
                              _type.HRESULT]
    get_OverflowButtonVisibility: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Visibility]],  # value
                                            _type.HRESULT]
    get_PaneToggleButtonVisibility: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Visibility]],  # value
                                              _type.HRESULT]
    get_BackButtonVisibility: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Visibility]],  # value
                                        _type.HRESULT]
    get_TopPaneVisibility: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Visibility]],  # value
                                     _type.HRESULT]
    get_LeftPaneVisibility: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Visibility]],  # value
                                      _type.HRESULT]
    get_SingleSelectionFollowsFocus: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]


class INavigationViewTemplateSettingsFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[INavigationViewTemplateSettings]],  # value
                              _type.HRESULT]


class INavigationViewTemplateSettingsStatics(_inspectable.IInspectable):
    get_TopPaddingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_OverflowButtonVisibilityProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]
    get_PaneToggleButtonVisibilityProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                      _type.HRESULT]
    get_BackButtonVisibilityProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_TopPaneVisibilityProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_LeftPaneVisibilityProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_SingleSelectionFollowsFocusProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]

    _factory = True


class INotifyEventArgs(_inspectable.IInspectable):
    get_Value: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]


class INotifyEventArgs2(_inspectable.IInspectable):
    get_CallingUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                              _type.HRESULT]


class IPage(_inspectable.IInspectable):
    get_Frame: _Callable[[_Pointer[IFrame]],  # value
                         _type.HRESULT]
    get_NavigationCacheMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Navigation.NavigationCacheMode]],  # value
                                       _type.HRESULT]
    put_NavigationCacheMode: _Callable[[_enum.Windows.UI.Xaml.Navigation.NavigationCacheMode],  # value
                                       _type.HRESULT]
    get_TopAppBar: _Callable[[_Pointer[IAppBar]],  # value
                             _type.HRESULT]
    put_TopAppBar: _Callable[[IAppBar],  # value
                             _type.HRESULT]
    get_BottomAppBar: _Callable[[_Pointer[IAppBar]],  # value
                                _type.HRESULT]
    put_BottomAppBar: _Callable[[IAppBar],  # value
                                _type.HRESULT]


class IPageFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IPage]],  # value
                              _type.HRESULT]


class IPageOverrides(_inspectable.IInspectable):
    OnNavigatedFrom: _Callable[[_Windows_UI_Xaml_Navigation.INavigationEventArgs],  # e
                               _type.HRESULT]
    OnNavigatedTo: _Callable[[_Windows_UI_Xaml_Navigation.INavigationEventArgs],  # e
                             _type.HRESULT]
    OnNavigatingFrom: _Callable[[_Windows_UI_Xaml_Navigation.INavigatingCancelEventArgs],  # e
                                _type.HRESULT]


class IPageStatics(_inspectable.IInspectable):
    get_FrameProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_TopAppBarProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_BottomAppBarProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]

    _factory = True


class IPanel(_inspectable.IInspectable):
    get_Children: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml.IUIElement]]],  # value
                            _type.HRESULT]
    get_Background: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                              _type.HRESULT]
    put_Background: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                              _type.HRESULT]
    get_IsItemsHost: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_ChildrenTransitions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Media_Animation.ITransition]]],  # value
                                       _type.HRESULT]
    put_ChildrenTransitions: _Callable[[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Media_Animation.ITransition]],  # value
                                       _type.HRESULT]


class IPanel2(_inspectable.IInspectable):
    get_BackgroundTransition: _Callable[[_Pointer[_Windows_UI_Xaml.IBrushTransition]],  # value
                                        _type.HRESULT]
    put_BackgroundTransition: _Callable[[_Windows_UI_Xaml.IBrushTransition],  # value
                                        _type.HRESULT]


class IPanelFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IPanel]],  # value
                              _type.HRESULT]


class IPanelStatics(_inspectable.IInspectable):
    get_BackgroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_IsItemsHostProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_ChildrenTransitionsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]

    _factory = True


class IParallaxView(_inspectable.IInspectable):
    get_Child: _Callable[[_Pointer[_Windows_UI_Xaml.IUIElement]],  # value
                         _type.HRESULT]
    put_Child: _Callable[[_Windows_UI_Xaml.IUIElement],  # value
                         _type.HRESULT]
    get_HorizontalShift: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                   _type.HRESULT]
    put_HorizontalShift: _Callable[[_type.DOUBLE],  # value
                                   _type.HRESULT]
    get_HorizontalSourceEndOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                             _type.HRESULT]
    put_HorizontalSourceEndOffset: _Callable[[_type.DOUBLE],  # value
                                             _type.HRESULT]
    get_HorizontalSourceOffsetKind: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.ParallaxSourceOffsetKind]],  # value
                                              _type.HRESULT]
    put_HorizontalSourceOffsetKind: _Callable[[_enum.Windows.UI.Xaml.Controls.ParallaxSourceOffsetKind],  # value
                                              _type.HRESULT]
    get_HorizontalSourceStartOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                               _type.HRESULT]
    put_HorizontalSourceStartOffset: _Callable[[_type.DOUBLE],  # value
                                               _type.HRESULT]
    get_IsHorizontalShiftClamped: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_IsHorizontalShiftClamped: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]
    get_IsVerticalShiftClamped: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_IsVerticalShiftClamped: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    get_MaxHorizontalShiftRatio: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                           _type.HRESULT]
    put_MaxHorizontalShiftRatio: _Callable[[_type.DOUBLE],  # value
                                           _type.HRESULT]
    get_MaxVerticalShiftRatio: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                         _type.HRESULT]
    put_MaxVerticalShiftRatio: _Callable[[_type.DOUBLE],  # value
                                         _type.HRESULT]
    get_Source: _Callable[[_Pointer[_Windows_UI_Xaml.IUIElement]],  # value
                          _type.HRESULT]
    put_Source: _Callable[[_Windows_UI_Xaml.IUIElement],  # value
                          _type.HRESULT]
    get_VerticalShift: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                 _type.HRESULT]
    put_VerticalShift: _Callable[[_type.DOUBLE],  # value
                                 _type.HRESULT]
    get_VerticalSourceEndOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                           _type.HRESULT]
    put_VerticalSourceEndOffset: _Callable[[_type.DOUBLE],  # value
                                           _type.HRESULT]
    get_VerticalSourceOffsetKind: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.ParallaxSourceOffsetKind]],  # value
                                            _type.HRESULT]
    put_VerticalSourceOffsetKind: _Callable[[_enum.Windows.UI.Xaml.Controls.ParallaxSourceOffsetKind],  # value
                                            _type.HRESULT]
    get_VerticalSourceStartOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                             _type.HRESULT]
    put_VerticalSourceStartOffset: _Callable[[_type.DOUBLE],  # value
                                             _type.HRESULT]
    RefreshAutomaticHorizontalOffsets: _Callable[[],
                                                 _type.HRESULT]
    RefreshAutomaticVerticalOffsets: _Callable[[],
                                               _type.HRESULT]


class IParallaxViewFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IParallaxView]],  # value
                              _type.HRESULT]


class IParallaxViewStatics(_inspectable.IInspectable):
    get_ChildProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_HorizontalSourceEndOffsetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                     _type.HRESULT]
    get_HorizontalSourceOffsetKindProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                      _type.HRESULT]
    get_HorizontalSourceStartOffsetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]
    get_MaxHorizontalShiftRatioProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_HorizontalShiftProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_IsHorizontalShiftClampedProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]
    get_IsVerticalShiftClampedProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]
    get_SourceProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_VerticalSourceEndOffsetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_VerticalSourceOffsetKindProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]
    get_VerticalSourceStartOffsetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                     _type.HRESULT]
    get_MaxVerticalShiftRatioProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_VerticalShiftProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]

    _factory = True


class IPasswordBox(_inspectable.IInspectable):
    get_Password: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_Password: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_PasswordChar: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    put_PasswordChar: _Callable[[_type.HSTRING],  # value
                                _type.HRESULT]
    IsPasswordRevealButtonEnabled: _Callable[[_type.boolean],  # value
                                             _type.HRESULT]
    get_MaxLength: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]
    put_MaxLength: _Callable[[_type.INT32],  # value
                             _type.HRESULT]
    add_PasswordChanged: _Callable[[_Windows_UI_Xaml.IRoutedEventHandler,  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_PasswordChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    add_ContextMenuOpening: _Callable[[IContextMenuOpeningEventHandler,  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_ContextMenuOpening: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    SelectAll: _Callable[[],
                         _type.HRESULT]


class IPasswordBox2(_inspectable.IInspectable):
    get_Header: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                          _type.HRESULT]
    put_Header: _Callable[[_inspectable.IInspectable],  # value
                          _type.HRESULT]
    get_HeaderTemplate: _Callable[[_Pointer[_Windows_UI_Xaml.IDataTemplate]],  # value
                                  _type.HRESULT]
    put_HeaderTemplate: _Callable[[_Windows_UI_Xaml.IDataTemplate],  # value
                                  _type.HRESULT]
    get_PlaceholderText: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    put_PlaceholderText: _Callable[[_type.HSTRING],  # value
                                   _type.HRESULT]
    get_SelectionHighlightColor: _Callable[[_Pointer[_Windows_UI_Xaml_Media.ISolidColorBrush]],  # value
                                           _type.HRESULT]
    put_SelectionHighlightColor: _Callable[[_Windows_UI_Xaml_Media.ISolidColorBrush],  # value
                                           _type.HRESULT]
    get_PreventKeyboardDisplayOnProgrammaticFocus: _Callable[[_Pointer[_type.boolean]],  # value
                                                             _type.HRESULT]
    put_PreventKeyboardDisplayOnProgrammaticFocus: _Callable[[_type.boolean],  # value
                                                             _type.HRESULT]
    add_Paste: _Callable[[ITextControlPasteEventHandler,  # handler
                          _Pointer[_struct.EventRegistrationToken]],  # token
                         _type.HRESULT]
    remove_Paste: _Callable[[_struct.EventRegistrationToken],  # token
                            _type.HRESULT]


class IPasswordBox3(_inspectable.IInspectable):
    get_PasswordRevealMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.PasswordRevealMode]],  # value
                                      _type.HRESULT]
    put_PasswordRevealMode: _Callable[[_enum.Windows.UI.Xaml.Controls.PasswordRevealMode],  # value
                                      _type.HRESULT]
    get_TextReadingOrder: _Callable[[_Pointer[_enum.Windows.UI.Xaml.TextReadingOrder]],  # value
                                    _type.HRESULT]
    put_TextReadingOrder: _Callable[[_enum.Windows.UI.Xaml.TextReadingOrder],  # value
                                    _type.HRESULT]
    get_InputScope: _Callable[[_Pointer[_Windows_UI_Xaml_Input.IInputScope]],  # value
                              _type.HRESULT]
    put_InputScope: _Callable[[_Windows_UI_Xaml_Input.IInputScope],  # value
                              _type.HRESULT]


class IPasswordBox4(_inspectable.IInspectable):
    add_PasswordChanging: _Callable[[_Windows_Foundation.ITypedEventHandler[IPasswordBox, IPasswordBoxPasswordChangingEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_PasswordChanging: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]


class IPasswordBox5(_inspectable.IInspectable):
    get_CanPasteClipboardContent: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    get_SelectionFlyout: _Callable[[_Pointer[_Windows_UI_Xaml_Controls_Primitives.IFlyoutBase]],  # value
                                   _type.HRESULT]
    put_SelectionFlyout: _Callable[[_Windows_UI_Xaml_Controls_Primitives.IFlyoutBase],  # value
                                   _type.HRESULT]
    get_Description: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_inspectable.IInspectable],  # value
                               _type.HRESULT]
    PasteFromClipboard: _Callable[[],
                                  _type.HRESULT]


class IPasswordBoxPasswordChangingEventArgs(_inspectable.IInspectable):
    get_IsContentChanging: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]


class IPasswordBoxStatics(_inspectable.IInspectable):
    get_PasswordProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_PasswordCharProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    IsPasswordRevealButtonEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                     _type.HRESULT]
    get_MaxLengthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]

    _factory = True


class IPasswordBoxStatics2(_inspectable.IInspectable):
    get_HeaderProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_HeaderTemplateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_PlaceholderTextProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_SelectionHighlightColorProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_PreventKeyboardDisplayOnProgrammaticFocusProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                                     _type.HRESULT]

    _factory = True


class IPasswordBoxStatics3(_inspectable.IInspectable):
    get_PasswordRevealModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_TextReadingOrderProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_InputScopeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]

    _factory = True


class IPasswordBoxStatics5(_inspectable.IInspectable):
    get_CanPasteClipboardContentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]
    get_SelectionFlyoutProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_DescriptionProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]

    _factory = True


class IPathIcon(_inspectable.IInspectable):
    get_Data: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IGeometry]],  # value
                        _type.HRESULT]
    put_Data: _Callable[[_Windows_UI_Xaml_Media.IGeometry],  # value
                        _type.HRESULT]


class IPathIconFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IPathIcon]],  # value
                              _type.HRESULT]


class IPathIconSource(_inspectable.IInspectable):
    get_Data: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IGeometry]],  # value
                        _type.HRESULT]
    put_Data: _Callable[[_Windows_UI_Xaml_Media.IGeometry],  # value
                        _type.HRESULT]


class IPathIconSourceFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IPathIconSource]],  # value
                              _type.HRESULT]


class IPathIconSourceStatics(_inspectable.IInspectable):
    get_DataProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]

    _factory = True


class IPathIconStatics(_inspectable.IInspectable):
    get_DataProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]

    _factory = True


class IPersonPicture(_inspectable.IInspectable):
    get_BadgeNumber: _Callable[[_Pointer[_type.INT32]],  # value
                               _type.HRESULT]
    put_BadgeNumber: _Callable[[_type.INT32],  # value
                               _type.HRESULT]
    get_BadgeGlyph: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_BadgeGlyph: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]
    get_BadgeImageSource: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IImageSource]],  # value
                                    _type.HRESULT]
    put_BadgeImageSource: _Callable[[_Windows_UI_Xaml_Media.IImageSource],  # value
                                    _type.HRESULT]
    get_BadgeText: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_BadgeText: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_IsGroup: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_IsGroup: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_Contact: _Callable[[_Pointer[_Windows_ApplicationModel_Contacts.IContact]],  # value
                           _type.HRESULT]
    put_Contact: _Callable[[_Windows_ApplicationModel_Contacts.IContact],  # value
                           _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_DisplayName: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_Initials: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_Initials: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_PreferSmallImage: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_PreferSmallImage: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_ProfilePicture: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IImageSource]],  # value
                                  _type.HRESULT]
    put_ProfilePicture: _Callable[[_Windows_UI_Xaml_Media.IImageSource],  # value
                                  _type.HRESULT]


class IPersonPictureFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IPersonPicture]],  # value
                              _type.HRESULT]


class IPersonPictureStatics(_inspectable.IInspectable):
    get_BadgeNumberProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_BadgeGlyphProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_BadgeImageSourceProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_BadgeTextProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_IsGroupProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_ContactProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_DisplayNameProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_InitialsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_PreferSmallImageProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_ProfilePictureProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]

    _factory = True


class IPickerConfirmedEventArgs(_inspectable.IInspectable):
    pass


class IPickerFlyout(_inspectable.IInspectable):
    get_Content: _Callable[[_Pointer[_Windows_UI_Xaml.IUIElement]],  # value
                           _type.HRESULT]
    put_Content: _Callable[[_Windows_UI_Xaml.IUIElement],  # value
                           _type.HRESULT]
    get_ConfirmationButtonsVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]
    put_ConfirmationButtonsVisible: _Callable[[_type.boolean],  # value
                                              _type.HRESULT]
    add_Confirmed: _Callable[[_Windows_Foundation.ITypedEventHandler[IPickerFlyout, IPickerConfirmedEventArgs],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_Confirmed: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    ShowAtAsync: _Callable[[_Windows_UI_Xaml.IFrameworkElement,  # target
                            _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                           _type.HRESULT]


class IPickerFlyoutPresenter(_inspectable.IInspectable):
    pass


class IPickerFlyoutStatics(_inspectable.IInspectable):
    get_ContentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_ConfirmationButtonsVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                      _type.HRESULT]

    _factory = True


class IPivot(_inspectable.IInspectable):
    get_Title: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                         _type.HRESULT]
    put_Title: _Callable[[_inspectable.IInspectable],  # value
                         _type.HRESULT]
    get_TitleTemplate: _Callable[[_Pointer[_Windows_UI_Xaml.IDataTemplate]],  # value
                                 _type.HRESULT]
    put_TitleTemplate: _Callable[[_Windows_UI_Xaml.IDataTemplate],  # value
                                 _type.HRESULT]
    get_HeaderTemplate: _Callable[[_Pointer[_Windows_UI_Xaml.IDataTemplate]],  # value
                                  _type.HRESULT]
    put_HeaderTemplate: _Callable[[_Windows_UI_Xaml.IDataTemplate],  # value
                                  _type.HRESULT]
    get_SelectedIndex: _Callable[[_Pointer[_type.INT32]],  # value
                                 _type.HRESULT]
    put_SelectedIndex: _Callable[[_type.INT32],  # value
                                 _type.HRESULT]
    get_SelectedItem: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                _type.HRESULT]
    put_SelectedItem: _Callable[[_inspectable.IInspectable],  # value
                                _type.HRESULT]
    get_IsLocked: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    put_IsLocked: _Callable[[_type.boolean],  # value
                            _type.HRESULT]
    add_SelectionChanged: _Callable[[ISelectionChangedEventHandler,  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_SelectionChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    add_PivotItemLoading: _Callable[[_Windows_Foundation.ITypedEventHandler[IPivot, IPivotItemEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_PivotItemLoading: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    add_PivotItemLoaded: _Callable[[_Windows_Foundation.ITypedEventHandler[IPivot, IPivotItemEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_PivotItemLoaded: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    add_PivotItemUnloading: _Callable[[_Windows_Foundation.ITypedEventHandler[IPivot, IPivotItemEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_PivotItemUnloading: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_PivotItemUnloaded: _Callable[[_Windows_Foundation.ITypedEventHandler[IPivot, IPivotItemEventArgs],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_PivotItemUnloaded: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]


class IPivot2(_inspectable.IInspectable):
    get_LeftHeader: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                              _type.HRESULT]
    put_LeftHeader: _Callable[[_inspectable.IInspectable],  # value
                              _type.HRESULT]
    get_LeftHeaderTemplate: _Callable[[_Pointer[_Windows_UI_Xaml.IDataTemplate]],  # value
                                      _type.HRESULT]
    put_LeftHeaderTemplate: _Callable[[_Windows_UI_Xaml.IDataTemplate],  # value
                                      _type.HRESULT]
    get_RightHeader: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                               _type.HRESULT]
    put_RightHeader: _Callable[[_inspectable.IInspectable],  # value
                               _type.HRESULT]
    get_RightHeaderTemplate: _Callable[[_Pointer[_Windows_UI_Xaml.IDataTemplate]],  # value
                                       _type.HRESULT]
    put_RightHeaderTemplate: _Callable[[_Windows_UI_Xaml.IDataTemplate],  # value
                                       _type.HRESULT]


class IPivot3(_inspectable.IInspectable):
    get_HeaderFocusVisualPlacement: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.PivotHeaderFocusVisualPlacement]],  # value
                                              _type.HRESULT]
    put_HeaderFocusVisualPlacement: _Callable[[_enum.Windows.UI.Xaml.Controls.PivotHeaderFocusVisualPlacement],  # value
                                              _type.HRESULT]
    get_IsHeaderItemsCarouselEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                _type.HRESULT]
    put_IsHeaderItemsCarouselEnabled: _Callable[[_type.boolean],  # value
                                                _type.HRESULT]


class IPivotFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IPivot]],  # value
                              _type.HRESULT]


class IPivotItem(_inspectable.IInspectable):
    get_Header: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                          _type.HRESULT]
    put_Header: _Callable[[_inspectable.IInspectable],  # value
                          _type.HRESULT]


class IPivotItemEventArgs(_inspectable.IInspectable):
    get_Item: _Callable[[_Pointer[IPivotItem]],  # value
                        _type.HRESULT]
    put_Item: _Callable[[IPivotItem],  # value
                        _type.HRESULT]


class IPivotItemFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IPivotItem]],  # value
                              _type.HRESULT]


class IPivotItemStatics(_inspectable.IInspectable):
    get_HeaderProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]

    _factory = True


class IPivotStatics(_inspectable.IInspectable):
    get_TitleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_TitleTemplateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_HeaderTemplateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_SelectedIndexProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_SelectedItemProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_IsLockedProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_SlideInAnimationGroupProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    GetSlideInAnimationGroup: _Callable[[_Windows_UI_Xaml.IFrameworkElement,  # element
                                         _Pointer[_enum.Windows.UI.Xaml.Controls.PivotSlideInAnimationGroup]],  # result
                                        _type.HRESULT]
    SetSlideInAnimationGroup: _Callable[[_Windows_UI_Xaml.IFrameworkElement,  # element
                                         _enum.Windows.UI.Xaml.Controls.PivotSlideInAnimationGroup],  # value
                                        _type.HRESULT]

    _factory = True


class IPivotStatics2(_inspectable.IInspectable):
    get_LeftHeaderProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_LeftHeaderTemplateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_RightHeaderProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_RightHeaderTemplateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]

    _factory = True


class IPivotStatics3(_inspectable.IInspectable):
    get_HeaderFocusVisualPlacementProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                      _type.HRESULT]
    get_IsHeaderItemsCarouselEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                        _type.HRESULT]

    _factory = True


class IProgressBar(_inspectable.IInspectable):
    get_IsIndeterminate: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    put_IsIndeterminate: _Callable[[_type.boolean],  # value
                                   _type.HRESULT]
    get_ShowError: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_ShowError: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    get_ShowPaused: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    put_ShowPaused: _Callable[[_type.boolean],  # value
                              _type.HRESULT]
    get_TemplateSettings: _Callable[[_Pointer[_Windows_UI_Xaml_Controls_Primitives.IProgressBarTemplateSettings]],  # value
                                    _type.HRESULT]


class IProgressBarFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IProgressBar]],  # value
                              _type.HRESULT]


class IProgressBarStatics(_inspectable.IInspectable):
    get_IsIndeterminateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_ShowErrorProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_ShowPausedProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]

    _factory = True


class IProgressRing(_inspectable.IInspectable):
    get_IsActive: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    put_IsActive: _Callable[[_type.boolean],  # value
                            _type.HRESULT]
    get_TemplateSettings: _Callable[[_Pointer[_Windows_UI_Xaml_Controls_Primitives.IProgressRingTemplateSettings]],  # value
                                    _type.HRESULT]


class IProgressRingStatics(_inspectable.IInspectable):
    get_IsActiveProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]

    _factory = True


class IRadioButton(_inspectable.IInspectable):
    get_GroupName: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_GroupName: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]


class IRadioButtonFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IRadioButton]],  # value
                              _type.HRESULT]


class IRadioButtonStatics(_inspectable.IInspectable):
    get_GroupNameProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]

    _factory = True


class IRatingControl(_inspectable.IInspectable):
    get_Caption: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    put_Caption: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    get_InitialSetValue: _Callable[[_Pointer[_type.INT32]],  # value
                                   _type.HRESULT]
    put_InitialSetValue: _Callable[[_type.INT32],  # value
                                   _type.HRESULT]
    get_IsClearEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    put_IsClearEnabled: _Callable[[_type.boolean],  # value
                                  _type.HRESULT]
    get_IsReadOnly: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    put_IsReadOnly: _Callable[[_type.boolean],  # value
                              _type.HRESULT]
    get_MaxRating: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]
    put_MaxRating: _Callable[[_type.INT32],  # value
                             _type.HRESULT]
    get_PlaceholderValue: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]
    put_PlaceholderValue: _Callable[[_type.DOUBLE],  # value
                                    _type.HRESULT]
    get_ItemInfo: _Callable[[_Pointer[IRatingItemInfo]],  # value
                            _type.HRESULT]
    put_ItemInfo: _Callable[[IRatingItemInfo],  # value
                            _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.DOUBLE]],  # value
                         _type.HRESULT]
    put_Value: _Callable[[_type.DOUBLE],  # value
                         _type.HRESULT]
    add_ValueChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IRatingControl, _inspectable.IInspectable],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_ValueChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]


class IRatingControlFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IRatingControl]],  # value
                              _type.HRESULT]


class IRatingControlStatics(_inspectable.IInspectable):
    get_CaptionProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_InitialSetValueProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_IsClearEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_IsReadOnlyProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_MaxRatingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_PlaceholderValueProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_ItemInfoProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_ValueProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]

    _factory = True


class IRatingItemFontInfo(_inspectable.IInspectable):
    get_DisabledGlyph: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    put_DisabledGlyph: _Callable[[_type.HSTRING],  # value
                                 _type.HRESULT]
    get_Glyph: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Glyph: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_PointerOverGlyph: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    put_PointerOverGlyph: _Callable[[_type.HSTRING],  # value
                                    _type.HRESULT]
    get_PointerOverPlaceholderGlyph: _Callable[[_Pointer[_type.HSTRING]],  # value
                                               _type.HRESULT]
    put_PointerOverPlaceholderGlyph: _Callable[[_type.HSTRING],  # value
                                               _type.HRESULT]
    get_PlaceholderGlyph: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    put_PlaceholderGlyph: _Callable[[_type.HSTRING],  # value
                                    _type.HRESULT]
    get_UnsetGlyph: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_UnsetGlyph: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]


class IRatingItemFontInfoFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IRatingItemFontInfo]],  # value
                              _type.HRESULT]


class IRatingItemFontInfoStatics(_inspectable.IInspectable):
    get_DisabledGlyphProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_GlyphProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_PlaceholderGlyphProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_PointerOverGlyphProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_PointerOverPlaceholderGlyphProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]
    get_UnsetGlyphProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]

    _factory = True


class IRatingItemImageInfo(_inspectable.IInspectable):
    get_DisabledImage: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IImageSource]],  # value
                                 _type.HRESULT]
    put_DisabledImage: _Callable[[_Windows_UI_Xaml_Media.IImageSource],  # value
                                 _type.HRESULT]
    get_Image: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IImageSource]],  # value
                         _type.HRESULT]
    put_Image: _Callable[[_Windows_UI_Xaml_Media.IImageSource],  # value
                         _type.HRESULT]
    get_PlaceholderImage: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IImageSource]],  # value
                                    _type.HRESULT]
    put_PlaceholderImage: _Callable[[_Windows_UI_Xaml_Media.IImageSource],  # value
                                    _type.HRESULT]
    get_PointerOverImage: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IImageSource]],  # value
                                    _type.HRESULT]
    put_PointerOverImage: _Callable[[_Windows_UI_Xaml_Media.IImageSource],  # value
                                    _type.HRESULT]
    get_PointerOverPlaceholderImage: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IImageSource]],  # value
                                               _type.HRESULT]
    put_PointerOverPlaceholderImage: _Callable[[_Windows_UI_Xaml_Media.IImageSource],  # value
                                               _type.HRESULT]
    get_UnsetImage: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IImageSource]],  # value
                              _type.HRESULT]
    put_UnsetImage: _Callable[[_Windows_UI_Xaml_Media.IImageSource],  # value
                              _type.HRESULT]


class IRatingItemImageInfoFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IRatingItemImageInfo]],  # value
                              _type.HRESULT]


class IRatingItemImageInfoStatics(_inspectable.IInspectable):
    get_DisabledImageProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_ImageProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_PlaceholderImageProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_PointerOverImageProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_PointerOverPlaceholderImageProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]
    get_UnsetImageProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]

    _factory = True


class IRatingItemInfo(_inspectable.IInspectable):
    pass


class IRatingItemInfoFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IRatingItemInfo]],  # value
                              _type.HRESULT]


class IRefreshContainer(_inspectable.IInspectable):
    get_Visualizer: _Callable[[_Pointer[IRefreshVisualizer]],  # value
                              _type.HRESULT]
    put_Visualizer: _Callable[[IRefreshVisualizer],  # value
                              _type.HRESULT]
    get_PullDirection: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.RefreshPullDirection]],  # value
                                 _type.HRESULT]
    put_PullDirection: _Callable[[_enum.Windows.UI.Xaml.Controls.RefreshPullDirection],  # value
                                 _type.HRESULT]
    add_RefreshRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IRefreshContainer, IRefreshRequestedEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_RefreshRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    RequestRefresh: _Callable[[],
                              _type.HRESULT]


class IRefreshContainerFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IRefreshContainer]],  # value
                              _type.HRESULT]


class IRefreshContainerStatics(_inspectable.IInspectable):
    get_VisualizerProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_PullDirectionProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]

    _factory = True


class IRefreshInteractionRatioChangedEventArgs(_inspectable.IInspectable):
    get_InteractionRatio: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]


class IRefreshRequestedEventArgs(_inspectable.IInspectable):
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IRefreshStateChangedEventArgs(_inspectable.IInspectable):
    get_OldState: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.RefreshVisualizerState]],  # value
                            _type.HRESULT]
    get_NewState: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.RefreshVisualizerState]],  # value
                            _type.HRESULT]


class IRefreshVisualizer(_inspectable.IInspectable):
    RequestRefresh: _Callable[[],
                              _type.HRESULT]
    get_Orientation: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.RefreshVisualizerOrientation]],  # value
                               _type.HRESULT]
    put_Orientation: _Callable[[_enum.Windows.UI.Xaml.Controls.RefreshVisualizerOrientation],  # value
                               _type.HRESULT]
    get_Content: _Callable[[_Pointer[_Windows_UI_Xaml.IUIElement]],  # value
                           _type.HRESULT]
    put_Content: _Callable[[_Windows_UI_Xaml.IUIElement],  # value
                           _type.HRESULT]
    get_State: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.RefreshVisualizerState]],  # value
                         _type.HRESULT]
    add_RefreshRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IRefreshVisualizer, IRefreshRequestedEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_RefreshRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    add_RefreshStateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IRefreshVisualizer, IRefreshStateChangedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_RefreshStateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]


class IRefreshVisualizerFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IRefreshVisualizer]],  # value
                              _type.HRESULT]


class IRefreshVisualizerStatics(_inspectable.IInspectable):
    get_InfoProviderProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_OrientationProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_ContentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_StateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]

    _factory = True


class IRelativePanel(_inspectable.IInspectable):
    get_BorderBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                               _type.HRESULT]
    put_BorderBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                               _type.HRESULT]
    get_BorderThickness: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                                   _type.HRESULT]
    put_BorderThickness: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                                   _type.HRESULT]
    get_CornerRadius: _Callable[[_Pointer[_struct.Windows.UI.Xaml.CornerRadius]],  # value
                                _type.HRESULT]
    put_CornerRadius: _Callable[[_struct.Windows.UI.Xaml.CornerRadius],  # value
                                _type.HRESULT]
    get_Padding: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                           _type.HRESULT]
    put_Padding: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                           _type.HRESULT]


class IRelativePanel2(_inspectable.IInspectable):
    get_BackgroundSizing: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.BackgroundSizing]],  # value
                                    _type.HRESULT]
    put_BackgroundSizing: _Callable[[_enum.Windows.UI.Xaml.Controls.BackgroundSizing],  # value
                                    _type.HRESULT]


class IRelativePanelFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IRelativePanel]],  # value
                              _type.HRESULT]


class IRelativePanelStatics(_inspectable.IInspectable):
    get_LeftOfProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    GetLeftOf: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                          _Pointer[_inspectable.IInspectable]],  # result
                         _type.HRESULT]
    SetLeftOf: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                          _inspectable.IInspectable],  # value
                         _type.HRESULT]
    get_AboveProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    GetAbove: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                         _Pointer[_inspectable.IInspectable]],  # result
                        _type.HRESULT]
    SetAbove: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                         _inspectable.IInspectable],  # value
                        _type.HRESULT]
    get_RightOfProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    GetRightOf: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                           _Pointer[_inspectable.IInspectable]],  # result
                          _type.HRESULT]
    SetRightOf: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                           _inspectable.IInspectable],  # value
                          _type.HRESULT]
    get_BelowProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    GetBelow: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                         _Pointer[_inspectable.IInspectable]],  # result
                        _type.HRESULT]
    SetBelow: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                         _inspectable.IInspectable],  # value
                        _type.HRESULT]
    get_AlignHorizontalCenterWithProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                     _type.HRESULT]
    GetAlignHorizontalCenterWith: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                             _Pointer[_inspectable.IInspectable]],  # result
                                            _type.HRESULT]
    SetAlignHorizontalCenterWith: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                             _inspectable.IInspectable],  # value
                                            _type.HRESULT]
    get_AlignVerticalCenterWithProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    GetAlignVerticalCenterWith: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                           _Pointer[_inspectable.IInspectable]],  # result
                                          _type.HRESULT]
    SetAlignVerticalCenterWith: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                           _inspectable.IInspectable],  # value
                                          _type.HRESULT]
    get_AlignLeftWithProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    GetAlignLeftWith: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                 _Pointer[_inspectable.IInspectable]],  # result
                                _type.HRESULT]
    SetAlignLeftWith: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                 _inspectable.IInspectable],  # value
                                _type.HRESULT]
    get_AlignTopWithProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    GetAlignTopWith: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                _Pointer[_inspectable.IInspectable]],  # result
                               _type.HRESULT]
    SetAlignTopWith: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                _inspectable.IInspectable],  # value
                               _type.HRESULT]
    get_AlignRightWithProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    GetAlignRightWith: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                  _Pointer[_inspectable.IInspectable]],  # result
                                 _type.HRESULT]
    SetAlignRightWith: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                  _inspectable.IInspectable],  # value
                                 _type.HRESULT]
    get_AlignBottomWithProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    GetAlignBottomWith: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                   _Pointer[_inspectable.IInspectable]],  # result
                                  _type.HRESULT]
    SetAlignBottomWith: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                   _inspectable.IInspectable],  # value
                                  _type.HRESULT]
    get_AlignLeftWithPanelProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    GetAlignLeftWithPanel: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                      _Pointer[_type.boolean]],  # result
                                     _type.HRESULT]
    SetAlignLeftWithPanel: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                      _type.boolean],  # value
                                     _type.HRESULT]
    get_AlignTopWithPanelProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    GetAlignTopWithPanel: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                     _Pointer[_type.boolean]],  # result
                                    _type.HRESULT]
    SetAlignTopWithPanel: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                     _type.boolean],  # value
                                    _type.HRESULT]
    get_AlignRightWithPanelProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    GetAlignRightWithPanel: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                       _Pointer[_type.boolean]],  # result
                                      _type.HRESULT]
    SetAlignRightWithPanel: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                       _type.boolean],  # value
                                      _type.HRESULT]
    get_AlignBottomWithPanelProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    GetAlignBottomWithPanel: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                        _Pointer[_type.boolean]],  # result
                                       _type.HRESULT]
    SetAlignBottomWithPanel: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                        _type.boolean],  # value
                                       _type.HRESULT]
    get_AlignHorizontalCenterWithPanelProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                          _type.HRESULT]
    GetAlignHorizontalCenterWithPanel: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                                  _Pointer[_type.boolean]],  # result
                                                 _type.HRESULT]
    SetAlignHorizontalCenterWithPanel: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                                  _type.boolean],  # value
                                                 _type.HRESULT]
    get_AlignVerticalCenterWithPanelProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                        _type.HRESULT]
    GetAlignVerticalCenterWithPanel: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                                _Pointer[_type.boolean]],  # result
                                               _type.HRESULT]
    SetAlignVerticalCenterWithPanel: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                                _type.boolean],  # value
                                               _type.HRESULT]
    get_BorderBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_BorderThicknessProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_CornerRadiusProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_PaddingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]

    _factory = True


class IRelativePanelStatics2(_inspectable.IInspectable):
    get_BackgroundSizingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]

    _factory = True


class IRichEditBox(_inspectable.IInspectable):
    get_IsReadOnly: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    put_IsReadOnly: _Callable[[_type.boolean],  # value
                              _type.HRESULT]
    get_AcceptsReturn: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_AcceptsReturn: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_TextAlignment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.TextAlignment]],  # value
                                 _type.HRESULT]
    put_TextAlignment: _Callable[[_enum.Windows.UI.Xaml.TextAlignment],  # value
                                 _type.HRESULT]
    get_TextWrapping: _Callable[[_Pointer[_enum.Windows.UI.Xaml.TextWrapping]],  # value
                                _type.HRESULT]
    put_TextWrapping: _Callable[[_enum.Windows.UI.Xaml.TextWrapping],  # value
                                _type.HRESULT]
    get_IsSpellCheckEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_IsSpellCheckEnabled: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_IsTextPredictionEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    put_IsTextPredictionEnabled: _Callable[[_type.boolean],  # value
                                           _type.HRESULT]
    get_Document: _Callable[[_Pointer[_Windows_UI_Text.ITextDocument]],  # value
                            _type.HRESULT]
    get_InputScope: _Callable[[_Pointer[_Windows_UI_Xaml_Input.IInputScope]],  # value
                              _type.HRESULT]
    put_InputScope: _Callable[[_Windows_UI_Xaml_Input.IInputScope],  # value
                              _type.HRESULT]
    add_TextChanged: _Callable[[_Windows_UI_Xaml.IRoutedEventHandler,  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_TextChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    add_SelectionChanged: _Callable[[_Windows_UI_Xaml.IRoutedEventHandler,  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_SelectionChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    add_ContextMenuOpening: _Callable[[IContextMenuOpeningEventHandler,  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_ContextMenuOpening: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]


class IRichEditBox2(_inspectable.IInspectable):
    get_Header: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                          _type.HRESULT]
    put_Header: _Callable[[_inspectable.IInspectable],  # value
                          _type.HRESULT]
    get_HeaderTemplate: _Callable[[_Pointer[_Windows_UI_Xaml.IDataTemplate]],  # value
                                  _type.HRESULT]
    put_HeaderTemplate: _Callable[[_Windows_UI_Xaml.IDataTemplate],  # value
                                  _type.HRESULT]
    get_PlaceholderText: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    put_PlaceholderText: _Callable[[_type.HSTRING],  # value
                                   _type.HRESULT]
    get_SelectionHighlightColor: _Callable[[_Pointer[_Windows_UI_Xaml_Media.ISolidColorBrush]],  # value
                                           _type.HRESULT]
    put_SelectionHighlightColor: _Callable[[_Windows_UI_Xaml_Media.ISolidColorBrush],  # value
                                           _type.HRESULT]
    get_PreventKeyboardDisplayOnProgrammaticFocus: _Callable[[_Pointer[_type.boolean]],  # value
                                                             _type.HRESULT]
    put_PreventKeyboardDisplayOnProgrammaticFocus: _Callable[[_type.boolean],  # value
                                                             _type.HRESULT]
    get_IsColorFontEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_IsColorFontEnabled: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    add_Paste: _Callable[[ITextControlPasteEventHandler,  # handler
                          _Pointer[_struct.EventRegistrationToken]],  # token
                         _type.HRESULT]
    remove_Paste: _Callable[[_struct.EventRegistrationToken],  # token
                            _type.HRESULT]


class IRichEditBox3(_inspectable.IInspectable):
    add_TextCompositionStarted: _Callable[[_Windows_Foundation.ITypedEventHandler[IRichEditBox, ITextCompositionStartedEventArgs],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_TextCompositionStarted: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]
    add_TextCompositionChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IRichEditBox, ITextCompositionChangedEventArgs],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_TextCompositionChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]
    add_TextCompositionEnded: _Callable[[_Windows_Foundation.ITypedEventHandler[IRichEditBox, ITextCompositionEndedEventArgs],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_TextCompositionEnded: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    get_TextReadingOrder: _Callable[[_Pointer[_enum.Windows.UI.Xaml.TextReadingOrder]],  # value
                                    _type.HRESULT]
    put_TextReadingOrder: _Callable[[_enum.Windows.UI.Xaml.TextReadingOrder],  # value
                                    _type.HRESULT]
    get_DesiredCandidateWindowAlignment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.CandidateWindowAlignment]],  # value
                                                   _type.HRESULT]
    put_DesiredCandidateWindowAlignment: _Callable[[_enum.Windows.UI.Xaml.Controls.CandidateWindowAlignment],  # value
                                                   _type.HRESULT]
    add_CandidateWindowBoundsChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IRichEditBox, ICandidateWindowBoundsChangedEventArgs],  # handler
                                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                                _type.HRESULT]
    remove_CandidateWindowBoundsChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                   _type.HRESULT]
    add_TextChanging: _Callable[[_Windows_Foundation.ITypedEventHandler[IRichEditBox, IRichEditBoxTextChangingEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_TextChanging: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]


class IRichEditBox4(_inspectable.IInspectable):
    GetLinguisticAlternativesAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]]],  # operation
                                              _type.HRESULT]
    get_ClipboardCopyFormat: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.RichEditClipboardFormat]],  # value
                                       _type.HRESULT]
    put_ClipboardCopyFormat: _Callable[[_enum.Windows.UI.Xaml.Controls.RichEditClipboardFormat],  # value
                                       _type.HRESULT]


class IRichEditBox5(_inspectable.IInspectable):
    get_SelectionHighlightColorWhenNotFocused: _Callable[[_Pointer[_Windows_UI_Xaml_Media.ISolidColorBrush]],  # value
                                                         _type.HRESULT]
    put_SelectionHighlightColorWhenNotFocused: _Callable[[_Windows_UI_Xaml_Media.ISolidColorBrush],  # value
                                                         _type.HRESULT]
    get_MaxLength: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]
    put_MaxLength: _Callable[[_type.INT32],  # value
                             _type.HRESULT]


class IRichEditBox6(_inspectable.IInspectable):
    get_HorizontalTextAlignment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.TextAlignment]],  # value
                                           _type.HRESULT]
    put_HorizontalTextAlignment: _Callable[[_enum.Windows.UI.Xaml.TextAlignment],  # value
                                           _type.HRESULT]
    get_CharacterCasing: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.CharacterCasing]],  # value
                                   _type.HRESULT]
    put_CharacterCasing: _Callable[[_enum.Windows.UI.Xaml.Controls.CharacterCasing],  # value
                                   _type.HRESULT]
    get_DisabledFormattingAccelerators: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.DisabledFormattingAccelerators]],  # value
                                                  _type.HRESULT]
    put_DisabledFormattingAccelerators: _Callable[[_enum.Windows.UI.Xaml.Controls.DisabledFormattingAccelerators],  # value
                                                  _type.HRESULT]
    add_CopyingToClipboard: _Callable[[_Windows_Foundation.ITypedEventHandler[IRichEditBox, ITextControlCopyingToClipboardEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_CopyingToClipboard: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_CuttingToClipboard: _Callable[[_Windows_Foundation.ITypedEventHandler[IRichEditBox, ITextControlCuttingToClipboardEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_CuttingToClipboard: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]


class IRichEditBox7(_inspectable.IInspectable):
    get_ContentLinkForegroundColor: _Callable[[_Pointer[_Windows_UI_Xaml_Media.ISolidColorBrush]],  # value
                                              _type.HRESULT]
    put_ContentLinkForegroundColor: _Callable[[_Windows_UI_Xaml_Media.ISolidColorBrush],  # value
                                              _type.HRESULT]
    get_ContentLinkBackgroundColor: _Callable[[_Pointer[_Windows_UI_Xaml_Media.ISolidColorBrush]],  # value
                                              _type.HRESULT]
    put_ContentLinkBackgroundColor: _Callable[[_Windows_UI_Xaml_Media.ISolidColorBrush],  # value
                                              _type.HRESULT]
    get_ContentLinkProviders: _Callable[[_Pointer[_Windows_UI_Xaml_Documents.IContentLinkProviderCollection]],  # value
                                        _type.HRESULT]
    put_ContentLinkProviders: _Callable[[_Windows_UI_Xaml_Documents.IContentLinkProviderCollection],  # value
                                        _type.HRESULT]
    get_HandwritingView: _Callable[[_Pointer[IHandwritingView]],  # value
                                   _type.HRESULT]
    put_HandwritingView: _Callable[[IHandwritingView],  # value
                                   _type.HRESULT]
    get_IsHandwritingViewEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_IsHandwritingViewEnabled: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]
    add_ContentLinkChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IRichEditBox, IContentLinkChangedEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_ContentLinkChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_ContentLinkInvoked: _Callable[[_Windows_Foundation.ITypedEventHandler[IRichEditBox, _Windows_UI_Xaml_Documents.IContentLinkInvokedEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_ContentLinkInvoked: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]


class IRichEditBox8(_inspectable.IInspectable):
    get_TextDocument: _Callable[[_Pointer[_Windows_UI_Text.ITextDocument]],  # value
                                _type.HRESULT]
    get_SelectionFlyout: _Callable[[_Pointer[_Windows_UI_Xaml_Controls_Primitives.IFlyoutBase]],  # value
                                   _type.HRESULT]
    put_SelectionFlyout: _Callable[[_Windows_UI_Xaml_Controls_Primitives.IFlyoutBase],  # value
                                   _type.HRESULT]
    get_ProofingMenuFlyout: _Callable[[_Pointer[_Windows_UI_Xaml_Controls_Primitives.IFlyoutBase]],  # value
                                      _type.HRESULT]
    get_Description: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_inspectable.IInspectable],  # value
                               _type.HRESULT]
    add_SelectionChanging: _Callable[[_Windows_Foundation.ITypedEventHandler[IRichEditBox, IRichEditBoxSelectionChangingEventArgs],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_SelectionChanging: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]


class IRichEditBoxFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IRichEditBox]],  # value
                              _type.HRESULT]


class IRichEditBoxSelectionChangingEventArgs(_inspectable.IInspectable):
    get_SelectionStart: _Callable[[_Pointer[_type.INT32]],  # value
                                  _type.HRESULT]
    get_SelectionLength: _Callable[[_Pointer[_type.INT32]],  # value
                                   _type.HRESULT]
    get_Cancel: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_Cancel: _Callable[[_type.boolean],  # value
                          _type.HRESULT]


class IRichEditBoxStatics(_inspectable.IInspectable):
    get_IsReadOnlyProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_AcceptsReturnProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_TextAlignmentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_TextWrappingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_IsSpellCheckEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_IsTextPredictionEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_InputScopeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]

    _factory = True


class IRichEditBoxStatics2(_inspectable.IInspectable):
    get_HeaderProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_HeaderTemplateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_PlaceholderTextProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_SelectionHighlightColorProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_PreventKeyboardDisplayOnProgrammaticFocusProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                                     _type.HRESULT]
    get_IsColorFontEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]

    _factory = True


class IRichEditBoxStatics3(_inspectable.IInspectable):
    get_DesiredCandidateWindowAlignmentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                           _type.HRESULT]
    get_TextReadingOrderProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]

    _factory = True


class IRichEditBoxStatics4(_inspectable.IInspectable):
    get_ClipboardCopyFormatProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]

    _factory = True


class IRichEditBoxStatics5(_inspectable.IInspectable):
    get_SelectionHighlightColorWhenNotFocusedProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                                 _type.HRESULT]
    get_MaxLengthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]

    _factory = True


class IRichEditBoxStatics6(_inspectable.IInspectable):
    get_HorizontalTextAlignmentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_CharacterCasingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_DisabledFormattingAcceleratorsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                          _type.HRESULT]

    _factory = True


class IRichEditBoxStatics7(_inspectable.IInspectable):
    get_ContentLinkForegroundColorProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                      _type.HRESULT]
    get_ContentLinkBackgroundColorProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                      _type.HRESULT]
    get_ContentLinkProvidersProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_HandwritingViewProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_IsHandwritingViewEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]

    _factory = True


class IRichEditBoxStatics8(_inspectable.IInspectable):
    get_SelectionFlyoutProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_ProofingMenuFlyoutProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_DescriptionProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]

    _factory = True


class IRichEditBoxTextChangingEventArgs(_inspectable.IInspectable):
    pass


class IRichEditBoxTextChangingEventArgs2(_inspectable.IInspectable):
    get_IsContentChanging: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]


class IRichTextBlock(_inspectable.IInspectable):
    get_FontSize: _Callable[[_Pointer[_type.DOUBLE]],  # value
                            _type.HRESULT]
    put_FontSize: _Callable[[_type.DOUBLE],  # value
                            _type.HRESULT]
    get_FontFamily: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IFontFamily]],  # value
                              _type.HRESULT]
    put_FontFamily: _Callable[[_Windows_UI_Xaml_Media.IFontFamily],  # value
                              _type.HRESULT]
    get_FontWeight: _Callable[[_Pointer[_struct.Windows.UI.Text.FontWeight]],  # value
                              _type.HRESULT]
    put_FontWeight: _Callable[[_struct.Windows.UI.Text.FontWeight],  # value
                              _type.HRESULT]
    get_FontStyle: _Callable[[_Pointer[_enum.Windows.UI.Text.FontStyle]],  # value
                             _type.HRESULT]
    put_FontStyle: _Callable[[_enum.Windows.UI.Text.FontStyle],  # value
                             _type.HRESULT]
    get_FontStretch: _Callable[[_Pointer[_enum.Windows.UI.Text.FontStretch]],  # value
                               _type.HRESULT]
    put_FontStretch: _Callable[[_enum.Windows.UI.Text.FontStretch],  # value
                               _type.HRESULT]
    get_Foreground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                              _type.HRESULT]
    put_Foreground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                              _type.HRESULT]
    get_TextWrapping: _Callable[[_Pointer[_enum.Windows.UI.Xaml.TextWrapping]],  # value
                                _type.HRESULT]
    put_TextWrapping: _Callable[[_enum.Windows.UI.Xaml.TextWrapping],  # value
                                _type.HRESULT]
    get_TextTrimming: _Callable[[_Pointer[_enum.Windows.UI.Xaml.TextTrimming]],  # value
                                _type.HRESULT]
    put_TextTrimming: _Callable[[_enum.Windows.UI.Xaml.TextTrimming],  # value
                                _type.HRESULT]
    get_TextAlignment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.TextAlignment]],  # value
                                 _type.HRESULT]
    put_TextAlignment: _Callable[[_enum.Windows.UI.Xaml.TextAlignment],  # value
                                 _type.HRESULT]
    get_Blocks: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Documents.IBlock]]],  # value
                          _type.HRESULT]
    get_Padding: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                           _type.HRESULT]
    put_Padding: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                           _type.HRESULT]
    get_LineHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                              _type.HRESULT]
    put_LineHeight: _Callable[[_type.DOUBLE],  # value
                              _type.HRESULT]
    get_LineStackingStrategy: _Callable[[_Pointer[_enum.Windows.UI.Xaml.LineStackingStrategy]],  # value
                                        _type.HRESULT]
    put_LineStackingStrategy: _Callable[[_enum.Windows.UI.Xaml.LineStackingStrategy],  # value
                                        _type.HRESULT]
    get_CharacterSpacing: _Callable[[_Pointer[_type.INT32]],  # value
                                    _type.HRESULT]
    put_CharacterSpacing: _Callable[[_type.INT32],  # value
                                    _type.HRESULT]
    get_OverflowContentTarget: _Callable[[_Pointer[IRichTextBlockOverflow]],  # value
                                         _type.HRESULT]
    put_OverflowContentTarget: _Callable[[IRichTextBlockOverflow],  # value
                                         _type.HRESULT]
    get_IsTextSelectionEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_IsTextSelectionEnabled: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    get_HasOverflowContent: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    get_SelectedText: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_ContentStart: _Callable[[_Pointer[_Windows_UI_Xaml_Documents.ITextPointer]],  # value
                                _type.HRESULT]
    get_ContentEnd: _Callable[[_Pointer[_Windows_UI_Xaml_Documents.ITextPointer]],  # value
                              _type.HRESULT]
    get_SelectionStart: _Callable[[_Pointer[_Windows_UI_Xaml_Documents.ITextPointer]],  # value
                                  _type.HRESULT]
    get_SelectionEnd: _Callable[[_Pointer[_Windows_UI_Xaml_Documents.ITextPointer]],  # value
                                _type.HRESULT]
    get_BaselineOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    add_SelectionChanged: _Callable[[_Windows_UI_Xaml.IRoutedEventHandler,  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_SelectionChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    add_ContextMenuOpening: _Callable[[IContextMenuOpeningEventHandler,  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_ContextMenuOpening: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    SelectAll: _Callable[[],
                         _type.HRESULT]
    Select: _Callable[[_Windows_UI_Xaml_Documents.ITextPointer,  # start
                       _Windows_UI_Xaml_Documents.ITextPointer],  # end
                      _type.HRESULT]
    GetPositionFromPoint: _Callable[[_struct.Windows.Foundation.Point,  # point
                                     _Pointer[_Windows_UI_Xaml_Documents.ITextPointer]],  # result
                                    _type.HRESULT]
    Focus: _Callable[[_enum.Windows.UI.Xaml.FocusState,  # value
                      _Pointer[_type.boolean]],  # result
                     _type.HRESULT]
    get_TextIndent: _Callable[[_Pointer[_type.DOUBLE]],  # value
                              _type.HRESULT]
    put_TextIndent: _Callable[[_type.DOUBLE],  # value
                              _type.HRESULT]


class IRichTextBlock2(_inspectable.IInspectable):
    get_MaxLines: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    put_MaxLines: _Callable[[_type.INT32],  # value
                            _type.HRESULT]
    get_TextLineBounds: _Callable[[_Pointer[_enum.Windows.UI.Xaml.TextLineBounds]],  # value
                                  _type.HRESULT]
    put_TextLineBounds: _Callable[[_enum.Windows.UI.Xaml.TextLineBounds],  # value
                                  _type.HRESULT]
    get_SelectionHighlightColor: _Callable[[_Pointer[_Windows_UI_Xaml_Media.ISolidColorBrush]],  # value
                                           _type.HRESULT]
    put_SelectionHighlightColor: _Callable[[_Windows_UI_Xaml_Media.ISolidColorBrush],  # value
                                           _type.HRESULT]
    get_OpticalMarginAlignment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.OpticalMarginAlignment]],  # value
                                          _type.HRESULT]
    put_OpticalMarginAlignment: _Callable[[_enum.Windows.UI.Xaml.OpticalMarginAlignment],  # value
                                          _type.HRESULT]
    get_IsColorFontEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_IsColorFontEnabled: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    get_TextReadingOrder: _Callable[[_Pointer[_enum.Windows.UI.Xaml.TextReadingOrder]],  # value
                                    _type.HRESULT]
    put_TextReadingOrder: _Callable[[_enum.Windows.UI.Xaml.TextReadingOrder],  # value
                                    _type.HRESULT]


class IRichTextBlock3(_inspectable.IInspectable):
    get_IsTextScaleFactorEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_IsTextScaleFactorEnabled: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]


class IRichTextBlock4(_inspectable.IInspectable):
    get_TextDecorations: _Callable[[_Pointer[_enum.Windows.UI.Text.TextDecorations]],  # value
                                   _type.HRESULT]
    put_TextDecorations: _Callable[[_enum.Windows.UI.Text.TextDecorations],  # value
                                   _type.HRESULT]


class IRichTextBlock5(_inspectable.IInspectable):
    get_IsTextTrimmed: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_HorizontalTextAlignment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.TextAlignment]],  # value
                                           _type.HRESULT]
    put_HorizontalTextAlignment: _Callable[[_enum.Windows.UI.Xaml.TextAlignment],  # value
                                           _type.HRESULT]
    get_TextHighlighters: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Documents.ITextHighlighter]]],  # value
                                    _type.HRESULT]
    add_IsTextTrimmedChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IRichTextBlock, IIsTextTrimmedChangedEventArgs],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_IsTextTrimmedChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]


class IRichTextBlock6(_inspectable.IInspectable):
    get_SelectionFlyout: _Callable[[_Pointer[_Windows_UI_Xaml_Controls_Primitives.IFlyoutBase]],  # value
                                   _type.HRESULT]
    put_SelectionFlyout: _Callable[[_Windows_UI_Xaml_Controls_Primitives.IFlyoutBase],  # value
                                   _type.HRESULT]
    CopySelectionToClipboard: _Callable[[],
                                        _type.HRESULT]


class IRichTextBlockOverflow(_inspectable.IInspectable):
    get_OverflowContentTarget: _Callable[[_Pointer[IRichTextBlockOverflow]],  # value
                                         _type.HRESULT]
    put_OverflowContentTarget: _Callable[[IRichTextBlockOverflow],  # value
                                         _type.HRESULT]
    get_Padding: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                           _type.HRESULT]
    put_Padding: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                           _type.HRESULT]
    get_ContentSource: _Callable[[_Pointer[IRichTextBlock]],  # value
                                 _type.HRESULT]
    get_HasOverflowContent: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    get_ContentStart: _Callable[[_Pointer[_Windows_UI_Xaml_Documents.ITextPointer]],  # value
                                _type.HRESULT]
    get_ContentEnd: _Callable[[_Pointer[_Windows_UI_Xaml_Documents.ITextPointer]],  # value
                              _type.HRESULT]
    get_BaselineOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    GetPositionFromPoint: _Callable[[_struct.Windows.Foundation.Point,  # point
                                     _Pointer[_Windows_UI_Xaml_Documents.ITextPointer]],  # result
                                    _type.HRESULT]
    Focus: _Callable[[_enum.Windows.UI.Xaml.FocusState,  # value
                      _Pointer[_type.boolean]],  # result
                     _type.HRESULT]


class IRichTextBlockOverflow2(_inspectable.IInspectable):
    get_MaxLines: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    put_MaxLines: _Callable[[_type.INT32],  # value
                            _type.HRESULT]


class IRichTextBlockOverflow3(_inspectable.IInspectable):
    get_IsTextTrimmed: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    add_IsTextTrimmedChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IRichTextBlockOverflow, IIsTextTrimmedChangedEventArgs],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_IsTextTrimmedChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]


class IRichTextBlockOverflowStatics(_inspectable.IInspectable):
    get_OverflowContentTargetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_PaddingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_HasOverflowContentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]

    _factory = True


class IRichTextBlockOverflowStatics2(_inspectable.IInspectable):
    get_MaxLinesProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]

    _factory = True


class IRichTextBlockOverflowStatics3(_inspectable.IInspectable):
    get_IsTextTrimmedProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]

    _factory = True


class IRichTextBlockStatics(_inspectable.IInspectable):
    get_FontSizeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_FontFamilyProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_FontWeightProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_FontStyleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_FontStretchProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_ForegroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_TextWrappingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_TextTrimmingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_TextAlignmentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_PaddingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_LineHeightProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_LineStackingStrategyProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_CharacterSpacingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_OverflowContentTargetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_IsTextSelectionEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]
    get_HasOverflowContentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_SelectedTextProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_TextIndentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]

    _factory = True


class IRichTextBlockStatics2(_inspectable.IInspectable):
    get_MaxLinesProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_TextLineBoundsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_SelectionHighlightColorProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_OpticalMarginAlignmentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]
    get_IsColorFontEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_TextReadingOrderProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]

    _factory = True


class IRichTextBlockStatics3(_inspectable.IInspectable):
    get_IsTextScaleFactorEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]

    _factory = True


class IRichTextBlockStatics4(_inspectable.IInspectable):
    get_TextDecorationsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]

    _factory = True


class IRichTextBlockStatics5(_inspectable.IInspectable):
    get_IsTextTrimmedProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_HorizontalTextAlignmentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]

    _factory = True


class IRichTextBlockStatics6(_inspectable.IInspectable):
    get_SelectionFlyoutProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]

    _factory = True


class IRowDefinition(_inspectable.IInspectable):
    get_Height: _Callable[[_Pointer[_struct.Windows.UI.Xaml.GridLength]],  # value
                          _type.HRESULT]
    put_Height: _Callable[[_struct.Windows.UI.Xaml.GridLength],  # value
                          _type.HRESULT]
    get_MaxHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                             _type.HRESULT]
    put_MaxHeight: _Callable[[_type.DOUBLE],  # value
                             _type.HRESULT]
    get_MinHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                             _type.HRESULT]
    put_MinHeight: _Callable[[_type.DOUBLE],  # value
                             _type.HRESULT]
    get_ActualHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]


class IRowDefinitionStatics(_inspectable.IInspectable):
    get_HeightProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_MaxHeightProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_MinHeightProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]

    _factory = True


class IScrollAnchorProvider(_inspectable.IInspectable):
    get_CurrentAnchor: _Callable[[_Pointer[_Windows_UI_Xaml.IUIElement]],  # value
                                 _type.HRESULT]
    RegisterAnchorCandidate: _Callable[[_Windows_UI_Xaml.IUIElement],  # element
                                       _type.HRESULT]
    UnregisterAnchorCandidate: _Callable[[_Windows_UI_Xaml.IUIElement],  # element
                                         _type.HRESULT]


class IScrollContentPresenter(_inspectable.IInspectable):
    get_CanVerticallyScroll: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_CanVerticallyScroll: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_CanHorizontallyScroll: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_CanHorizontallyScroll: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]
    get_ExtentWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                               _type.HRESULT]
    get_ExtentHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    get_ViewportWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                 _type.HRESULT]
    get_ViewportHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    get_HorizontalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]
    get_VerticalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    get_ScrollOwner: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                               _type.HRESULT]
    put_ScrollOwner: _Callable[[_inspectable.IInspectable],  # value
                               _type.HRESULT]
    LineUp: _Callable[[],
                      _type.HRESULT]
    LineDown: _Callable[[],
                        _type.HRESULT]
    LineLeft: _Callable[[],
                        _type.HRESULT]
    LineRight: _Callable[[],
                         _type.HRESULT]
    PageUp: _Callable[[],
                      _type.HRESULT]
    PageDown: _Callable[[],
                        _type.HRESULT]
    PageLeft: _Callable[[],
                        _type.HRESULT]
    PageRight: _Callable[[],
                         _type.HRESULT]
    MouseWheelUp: _Callable[[],
                            _type.HRESULT]
    MouseWheelDown: _Callable[[],
                              _type.HRESULT]
    MouseWheelLeft: _Callable[[],
                              _type.HRESULT]
    MouseWheelRight: _Callable[[],
                               _type.HRESULT]
    SetHorizontalOffset: _Callable[[_type.DOUBLE],  # offset
                                   _type.HRESULT]
    SetVerticalOffset: _Callable[[_type.DOUBLE],  # offset
                                 _type.HRESULT]
    MakeVisible: _Callable[[_Windows_UI_Xaml.IUIElement,  # visual
                            _struct.Windows.Foundation.Rect,  # rectangle
                            _Pointer[_struct.Windows.Foundation.Rect]],  # result
                           _type.HRESULT]


class IScrollContentPresenter2(_inspectable.IInspectable):
    get_CanContentRenderOutsideBounds: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]
    put_CanContentRenderOutsideBounds: _Callable[[_type.boolean],  # value
                                                 _type.HRESULT]
    get_SizesContentToTemplatedParent: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]
    put_SizesContentToTemplatedParent: _Callable[[_type.boolean],  # value
                                                 _type.HRESULT]


class IScrollContentPresenterStatics2(_inspectable.IInspectable):
    get_CanContentRenderOutsideBoundsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                         _type.HRESULT]
    get_SizesContentToTemplatedParentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                         _type.HRESULT]

    _factory = True


class IScrollViewer(_inspectable.IInspectable):
    get_HorizontalScrollBarVisibility: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.ScrollBarVisibility]],  # value
                                                 _type.HRESULT]
    put_HorizontalScrollBarVisibility: _Callable[[_enum.Windows.UI.Xaml.Controls.ScrollBarVisibility],  # value
                                                 _type.HRESULT]
    get_VerticalScrollBarVisibility: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.ScrollBarVisibility]],  # value
                                               _type.HRESULT]
    put_VerticalScrollBarVisibility: _Callable[[_enum.Windows.UI.Xaml.Controls.ScrollBarVisibility],  # value
                                               _type.HRESULT]
    get_IsHorizontalRailEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    put_IsHorizontalRailEnabled: _Callable[[_type.boolean],  # value
                                           _type.HRESULT]
    get_IsVerticalRailEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_IsVerticalRailEnabled: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]
    get_IsHorizontalScrollChainingEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                     _type.HRESULT]
    put_IsHorizontalScrollChainingEnabled: _Callable[[_type.boolean],  # value
                                                     _type.HRESULT]
    get_IsVerticalScrollChainingEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                   _type.HRESULT]
    put_IsVerticalScrollChainingEnabled: _Callable[[_type.boolean],  # value
                                                   _type.HRESULT]
    get_IsZoomChainingEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_IsZoomChainingEnabled: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]
    get_IsScrollInertiaEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_IsScrollInertiaEnabled: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    get_IsZoomInertiaEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    put_IsZoomInertiaEnabled: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]
    get_HorizontalScrollMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.ScrollMode]],  # value
                                        _type.HRESULT]
    put_HorizontalScrollMode: _Callable[[_enum.Windows.UI.Xaml.Controls.ScrollMode],  # value
                                        _type.HRESULT]
    get_VerticalScrollMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.ScrollMode]],  # value
                                      _type.HRESULT]
    put_VerticalScrollMode: _Callable[[_enum.Windows.UI.Xaml.Controls.ScrollMode],  # value
                                      _type.HRESULT]
    get_ZoomMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.ZoomMode]],  # value
                            _type.HRESULT]
    put_ZoomMode: _Callable[[_enum.Windows.UI.Xaml.Controls.ZoomMode],  # value
                            _type.HRESULT]
    get_HorizontalSnapPointsAlignment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Primitives.SnapPointsAlignment]],  # value
                                                 _type.HRESULT]
    put_HorizontalSnapPointsAlignment: _Callable[[_enum.Windows.UI.Xaml.Controls.Primitives.SnapPointsAlignment],  # value
                                                 _type.HRESULT]
    get_VerticalSnapPointsAlignment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Primitives.SnapPointsAlignment]],  # value
                                               _type.HRESULT]
    put_VerticalSnapPointsAlignment: _Callable[[_enum.Windows.UI.Xaml.Controls.Primitives.SnapPointsAlignment],  # value
                                               _type.HRESULT]
    get_HorizontalSnapPointsType: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.SnapPointsType]],  # value
                                            _type.HRESULT]
    put_HorizontalSnapPointsType: _Callable[[_enum.Windows.UI.Xaml.Controls.SnapPointsType],  # value
                                            _type.HRESULT]
    get_VerticalSnapPointsType: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.SnapPointsType]],  # value
                                          _type.HRESULT]
    put_VerticalSnapPointsType: _Callable[[_enum.Windows.UI.Xaml.Controls.SnapPointsType],  # value
                                          _type.HRESULT]
    get_ZoomSnapPointsType: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.SnapPointsType]],  # value
                                      _type.HRESULT]
    put_ZoomSnapPointsType: _Callable[[_enum.Windows.UI.Xaml.Controls.SnapPointsType],  # value
                                      _type.HRESULT]
    get_HorizontalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]
    get_ViewportWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                 _type.HRESULT]
    get_ScrollableWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                   _type.HRESULT]
    get_ComputedHorizontalScrollBarVisibility: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Visibility]],  # value
                                                         _type.HRESULT]
    get_ExtentWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                               _type.HRESULT]
    get_VerticalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    get_ViewportHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    get_ScrollableHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]
    get_ComputedVerticalScrollBarVisibility: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Visibility]],  # value
                                                       _type.HRESULT]
    get_ExtentHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    get_MinZoomFactor: _Callable[[_Pointer[_type.FLOAT]],  # value
                                 _type.HRESULT]
    put_MinZoomFactor: _Callable[[_type.FLOAT],  # value
                                 _type.HRESULT]
    get_MaxZoomFactor: _Callable[[_Pointer[_type.FLOAT]],  # value
                                 _type.HRESULT]
    put_MaxZoomFactor: _Callable[[_type.FLOAT],  # value
                                 _type.HRESULT]
    get_ZoomFactor: _Callable[[_Pointer[_type.FLOAT]],  # value
                              _type.HRESULT]
    get_ZoomSnapPoints: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.FLOAT]]],  # value
                                  _type.HRESULT]
    add_ViewChanged: _Callable[[_Windows_Foundation.IEventHandler[IScrollViewerViewChangedEventArgs],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_ViewChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    ScrollToHorizontalOffset: _Callable[[_type.DOUBLE],  # offset
                                        _type.HRESULT]
    ScrollToVerticalOffset: _Callable[[_type.DOUBLE],  # offset
                                      _type.HRESULT]
    ZoomToFactor: _Callable[[_type.FLOAT],  # factor
                            _type.HRESULT]
    InvalidateScrollInfo: _Callable[[],
                                    _type.HRESULT]
    get_IsDeferredScrollingEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]
    put_IsDeferredScrollingEnabled: _Callable[[_type.boolean],  # value
                                              _type.HRESULT]
    get_BringIntoViewOnFocusChange: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]
    put_BringIntoViewOnFocusChange: _Callable[[_type.boolean],  # value
                                              _type.HRESULT]


class IScrollViewer2(_inspectable.IInspectable):
    get_TopLeftHeader: _Callable[[_Pointer[_Windows_UI_Xaml.IUIElement]],  # value
                                 _type.HRESULT]
    put_TopLeftHeader: _Callable[[_Windows_UI_Xaml.IUIElement],  # value
                                 _type.HRESULT]
    get_LeftHeader: _Callable[[_Pointer[_Windows_UI_Xaml.IUIElement]],  # value
                              _type.HRESULT]
    put_LeftHeader: _Callable[[_Windows_UI_Xaml.IUIElement],  # value
                              _type.HRESULT]
    get_TopHeader: _Callable[[_Pointer[_Windows_UI_Xaml.IUIElement]],  # value
                             _type.HRESULT]
    put_TopHeader: _Callable[[_Windows_UI_Xaml.IUIElement],  # value
                             _type.HRESULT]
    add_ViewChanging: _Callable[[_Windows_Foundation.IEventHandler[IScrollViewerViewChangingEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_ViewChanging: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    ChangeView: _Callable[[_Windows_Foundation.IReference[_type.DOUBLE],  # horizontalOffset
                           _Windows_Foundation.IReference[_type.DOUBLE],  # verticalOffset
                           _Windows_Foundation.IReference[_type.FLOAT],  # zoomFactor
                           _Pointer[_type.boolean]],  # result
                          _type.HRESULT]
    ChangeViewWithOptionalAnimation: _Callable[[_Windows_Foundation.IReference[_type.DOUBLE],  # horizontalOffset
                                                _Windows_Foundation.IReference[_type.DOUBLE],  # verticalOffset
                                                _Windows_Foundation.IReference[_type.FLOAT],  # zoomFactor
                                                _type.boolean,  # disableAnimation
                                                _Pointer[_type.boolean]],  # result
                                               _type.HRESULT]


class IScrollViewer3(_inspectable.IInspectable):
    add_DirectManipulationStarted: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                              _Pointer[_struct.EventRegistrationToken]],  # token
                                             _type.HRESULT]
    remove_DirectManipulationStarted: _Callable[[_struct.EventRegistrationToken],  # token
                                                _type.HRESULT]
    add_DirectManipulationCompleted: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                                _Pointer[_struct.EventRegistrationToken]],  # token
                                               _type.HRESULT]
    remove_DirectManipulationCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                                  _type.HRESULT]


class IScrollViewer4(_inspectable.IInspectable):
    get_ReduceViewportForCoreInputViewOcclusions: _Callable[[_Pointer[_type.boolean]],  # value
                                                            _type.HRESULT]
    put_ReduceViewportForCoreInputViewOcclusions: _Callable[[_type.boolean],  # value
                                                            _type.HRESULT]
    get_HorizontalAnchorRatio: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                         _type.HRESULT]
    put_HorizontalAnchorRatio: _Callable[[_type.DOUBLE],  # value
                                         _type.HRESULT]
    get_VerticalAnchorRatio: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                       _type.HRESULT]
    put_VerticalAnchorRatio: _Callable[[_type.DOUBLE],  # value
                                       _type.HRESULT]
    get_CanContentRenderOutsideBounds: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]
    put_CanContentRenderOutsideBounds: _Callable[[_type.boolean],  # value
                                                 _type.HRESULT]
    add_AnchorRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IScrollViewer, IAnchorRequestedEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_AnchorRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]


class IScrollViewerStatics(_inspectable.IInspectable):
    get_HorizontalSnapPointsAlignmentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                         _type.HRESULT]
    get_VerticalSnapPointsAlignmentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]
    get_HorizontalSnapPointsTypeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]
    get_VerticalSnapPointsTypeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]
    get_ZoomSnapPointsTypeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_HorizontalOffsetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_ViewportWidthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_ScrollableWidthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_ComputedHorizontalScrollBarVisibilityProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                                 _type.HRESULT]
    get_ExtentWidthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_VerticalOffsetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_ViewportHeightProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_ScrollableHeightProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_ComputedVerticalScrollBarVisibilityProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                               _type.HRESULT]
    get_ExtentHeightProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_MinZoomFactorProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_MaxZoomFactorProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_ZoomFactorProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_ZoomSnapPointsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_HorizontalScrollBarVisibilityProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                         _type.HRESULT]
    GetHorizontalScrollBarVisibility: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                                 _Pointer[_enum.Windows.UI.Xaml.Controls.ScrollBarVisibility]],  # result
                                                _type.HRESULT]
    SetHorizontalScrollBarVisibility: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                                 _enum.Windows.UI.Xaml.Controls.ScrollBarVisibility],  # horizontalScrollBarVisibility
                                                _type.HRESULT]
    get_VerticalScrollBarVisibilityProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]
    GetVerticalScrollBarVisibility: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                               _Pointer[_enum.Windows.UI.Xaml.Controls.ScrollBarVisibility]],  # result
                                              _type.HRESULT]
    SetVerticalScrollBarVisibility: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                               _enum.Windows.UI.Xaml.Controls.ScrollBarVisibility],  # verticalScrollBarVisibility
                                              _type.HRESULT]
    get_IsHorizontalRailEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    GetIsHorizontalRailEnabled: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                           _Pointer[_type.boolean]],  # result
                                          _type.HRESULT]
    SetIsHorizontalRailEnabled: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                           _type.boolean],  # isHorizontalRailEnabled
                                          _type.HRESULT]
    get_IsVerticalRailEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    GetIsVerticalRailEnabled: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                         _Pointer[_type.boolean]],  # result
                                        _type.HRESULT]
    SetIsVerticalRailEnabled: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                         _type.boolean],  # isVerticalRailEnabled
                                        _type.HRESULT]
    get_IsHorizontalScrollChainingEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                             _type.HRESULT]
    GetIsHorizontalScrollChainingEnabled: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                                     _Pointer[_type.boolean]],  # result
                                                    _type.HRESULT]
    SetIsHorizontalScrollChainingEnabled: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                                     _type.boolean],  # isHorizontalScrollChainingEnabled
                                                    _type.HRESULT]
    get_IsVerticalScrollChainingEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                           _type.HRESULT]
    GetIsVerticalScrollChainingEnabled: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                                   _Pointer[_type.boolean]],  # result
                                                  _type.HRESULT]
    SetIsVerticalScrollChainingEnabled: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                                   _type.boolean],  # isVerticalScrollChainingEnabled
                                                  _type.HRESULT]
    get_IsZoomChainingEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    GetIsZoomChainingEnabled: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                         _Pointer[_type.boolean]],  # result
                                        _type.HRESULT]
    SetIsZoomChainingEnabled: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                         _type.boolean],  # isZoomChainingEnabled
                                        _type.HRESULT]
    get_IsScrollInertiaEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]
    GetIsScrollInertiaEnabled: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                          _Pointer[_type.boolean]],  # result
                                         _type.HRESULT]
    SetIsScrollInertiaEnabled: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                          _type.boolean],  # isScrollInertiaEnabled
                                         _type.HRESULT]
    get_IsZoomInertiaEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    GetIsZoomInertiaEnabled: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                        _Pointer[_type.boolean]],  # result
                                       _type.HRESULT]
    SetIsZoomInertiaEnabled: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                        _type.boolean],  # isZoomInertiaEnabled
                                       _type.HRESULT]
    get_HorizontalScrollModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    GetHorizontalScrollMode: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                        _Pointer[_enum.Windows.UI.Xaml.Controls.ScrollMode]],  # result
                                       _type.HRESULT]
    SetHorizontalScrollMode: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                        _enum.Windows.UI.Xaml.Controls.ScrollMode],  # horizontalScrollMode
                                       _type.HRESULT]
    get_VerticalScrollModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    GetVerticalScrollMode: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                      _Pointer[_enum.Windows.UI.Xaml.Controls.ScrollMode]],  # result
                                     _type.HRESULT]
    SetVerticalScrollMode: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                      _enum.Windows.UI.Xaml.Controls.ScrollMode],  # verticalScrollMode
                                     _type.HRESULT]
    get_ZoomModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    GetZoomMode: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                            _Pointer[_enum.Windows.UI.Xaml.Controls.ZoomMode]],  # result
                           _type.HRESULT]
    SetZoomMode: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                            _enum.Windows.UI.Xaml.Controls.ZoomMode],  # zoomMode
                           _type.HRESULT]
    get_IsDeferredScrollingEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                      _type.HRESULT]
    GetIsDeferredScrollingEnabled: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                              _Pointer[_type.boolean]],  # result
                                             _type.HRESULT]
    SetIsDeferredScrollingEnabled: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                              _type.boolean],  # isDeferredScrollingEnabled
                                             _type.HRESULT]
    get_BringIntoViewOnFocusChangeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                      _type.HRESULT]
    GetBringIntoViewOnFocusChange: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                              _Pointer[_type.boolean]],  # result
                                             _type.HRESULT]
    SetBringIntoViewOnFocusChange: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                              _type.boolean],  # bringIntoViewOnFocusChange
                                             _type.HRESULT]

    _factory = True


class IScrollViewerStatics2(_inspectable.IInspectable):
    get_TopLeftHeaderProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_LeftHeaderProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_TopHeaderProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]

    _factory = True


class IScrollViewerStatics4(_inspectable.IInspectable):
    get_ReduceViewportForCoreInputViewOcclusionsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                                    _type.HRESULT]
    get_HorizontalAnchorRatioProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_VerticalAnchorRatioProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_CanContentRenderOutsideBoundsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                         _type.HRESULT]
    GetCanContentRenderOutsideBounds: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                                 _Pointer[_type.boolean]],  # result
                                                _type.HRESULT]
    SetCanContentRenderOutsideBounds: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                                 _type.boolean],  # canContentRenderOutsideBounds
                                                _type.HRESULT]

    _factory = True


class IScrollViewerView(_inspectable.IInspectable):
    get_HorizontalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]
    get_VerticalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    get_ZoomFactor: _Callable[[_Pointer[_type.FLOAT]],  # value
                              _type.HRESULT]


class IScrollViewerViewChangedEventArgs(_inspectable.IInspectable):
    get_IsIntermediate: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]


class IScrollViewerViewChangingEventArgs(_inspectable.IInspectable):
    get_NextView: _Callable[[_Pointer[IScrollViewerView]],  # value
                            _type.HRESULT]
    get_FinalView: _Callable[[_Pointer[IScrollViewerView]],  # value
                             _type.HRESULT]
    get_IsInertial: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]


class ISearchBox(_inspectable.IInspectable):
    get_SearchHistoryEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    put_SearchHistoryEnabled: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]
    get_SearchHistoryContext: _Callable[[_Pointer[_type.HSTRING]],  # value
                                        _type.HRESULT]
    put_SearchHistoryContext: _Callable[[_type.HSTRING],  # value
                                        _type.HRESULT]
    get_PlaceholderText: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    put_PlaceholderText: _Callable[[_type.HSTRING],  # value
                                   _type.HRESULT]
    get_QueryText: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_QueryText: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_FocusOnKeyboardInput: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    put_FocusOnKeyboardInput: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]
    get_ChooseSuggestionOnEnter: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    put_ChooseSuggestionOnEnter: _Callable[[_type.boolean],  # value
                                           _type.HRESULT]
    add_QueryChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ISearchBox, ISearchBoxQueryChangedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_QueryChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    add_SuggestionsRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[ISearchBox, ISearchBoxSuggestionsRequestedEventArgs],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_SuggestionsRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    add_QuerySubmitted: _Callable[[_Windows_Foundation.ITypedEventHandler[ISearchBox, ISearchBoxQuerySubmittedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_QuerySubmitted: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_ResultSuggestionChosen: _Callable[[_Windows_Foundation.ITypedEventHandler[ISearchBox, ISearchBoxResultSuggestionChosenEventArgs],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_ResultSuggestionChosen: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]
    add_PrepareForFocusOnKeyboardInput: _Callable[[_Windows_Foundation.ITypedEventHandler[ISearchBox, _Windows_UI_Xaml.IRoutedEventArgs],  # handler
                                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                                  _type.HRESULT]
    remove_PrepareForFocusOnKeyboardInput: _Callable[[_struct.EventRegistrationToken],  # token
                                                     _type.HRESULT]
    SetLocalContentSuggestionSettings: _Callable[[_Windows_ApplicationModel_Search.ILocalContentSuggestionSettings],  # settings
                                                 _type.HRESULT]


class ISearchBoxFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ISearchBox]],  # value
                              _type.HRESULT]


class ISearchBoxQueryChangedEventArgs(_inspectable.IInspectable):
    get_QueryText: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_Language: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_LinguisticDetails: _Callable[[_Pointer[_Windows_ApplicationModel_Search.ISearchQueryLinguisticDetails]],  # value
                                     _type.HRESULT]


class ISearchBoxQuerySubmittedEventArgs(_inspectable.IInspectable):
    get_QueryText: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_Language: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_LinguisticDetails: _Callable[[_Pointer[_Windows_ApplicationModel_Search.ISearchQueryLinguisticDetails]],  # value
                                     _type.HRESULT]
    get_KeyModifiers: _Callable[[_Pointer[_enum.Windows.System.VirtualKeyModifiers]],  # value
                                _type.HRESULT]


class ISearchBoxResultSuggestionChosenEventArgs(_inspectable.IInspectable):
    get_Tag: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_KeyModifiers: _Callable[[_Pointer[_enum.Windows.System.VirtualKeyModifiers]],  # value
                                _type.HRESULT]


class ISearchBoxStatics(_inspectable.IInspectable):
    get_SearchHistoryEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_SearchHistoryContextProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_PlaceholderTextProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_QueryTextProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_FocusOnKeyboardInputProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_ChooseSuggestionOnEnterProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]

    _factory = True


class ISearchBoxSuggestionsRequestedEventArgs(_inspectable.IInspectable):
    get_QueryText: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_Language: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_LinguisticDetails: _Callable[[_Pointer[_Windows_ApplicationModel_Search.ISearchQueryLinguisticDetails]],  # value
                                     _type.HRESULT]
    get_Request: _Callable[[_Pointer[_Windows_ApplicationModel_Search.ISearchSuggestionsRequest]],  # value
                           _type.HRESULT]


class ISectionsInViewChangedEventArgs(_inspectable.IInspectable):
    get_AddedSections: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IHubSection]]],  # value
                                 _type.HRESULT]
    get_RemovedSections: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IHubSection]]],  # value
                                   _type.HRESULT]


class ISectionsInViewChangedEventArgsFactory(_inspectable.IInspectable):
    pass


class ISelectionChangedEventArgs(_inspectable.IInspectable):
    get_AddedItems: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_inspectable.IInspectable]]],  # value
                              _type.HRESULT]
    get_RemovedItems: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_inspectable.IInspectable]]],  # value
                                _type.HRESULT]


class ISelectionChangedEventArgsFactory(_inspectable.IInspectable):
    CreateInstanceWithRemovedItemsAndAddedItems: _Callable[[_Windows_Foundation_Collections.IVector[_inspectable.IInspectable],  # removedItems
                                                            _Windows_Foundation_Collections.IVector[_inspectable.IInspectable],  # addedItems
                                                            _inspectable.IInspectable,  # baseInterface
                                                            _Pointer[_inspectable.IInspectable],  # innerInterface
                                                            _Pointer[ISelectionChangedEventArgs]],  # value
                                                           _type.HRESULT]


class ISemanticZoom(_inspectable.IInspectable):
    get_ZoomedInView: _Callable[[_Pointer[ISemanticZoomInformation]],  # value
                                _type.HRESULT]
    put_ZoomedInView: _Callable[[ISemanticZoomInformation],  # value
                                _type.HRESULT]
    get_ZoomedOutView: _Callable[[_Pointer[ISemanticZoomInformation]],  # value
                                 _type.HRESULT]
    put_ZoomedOutView: _Callable[[ISemanticZoomInformation],  # value
                                 _type.HRESULT]
    get_IsZoomedInViewActive: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    put_IsZoomedInViewActive: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]
    get_CanChangeViews: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    put_CanChangeViews: _Callable[[_type.boolean],  # value
                                  _type.HRESULT]
    add_ViewChangeStarted: _Callable[[ISemanticZoomViewChangedEventHandler,  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_ViewChangeStarted: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    add_ViewChangeCompleted: _Callable[[ISemanticZoomViewChangedEventHandler,  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_ViewChangeCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    ToggleActiveView: _Callable[[],
                                _type.HRESULT]
    get_IsZoomOutButtonEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_IsZoomOutButtonEnabled: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]


class ISemanticZoomInformation(_inspectable.IInspectable):
    get_SemanticZoomOwner: _Callable[[_Pointer[ISemanticZoom]],  # value
                                     _type.HRESULT]
    put_SemanticZoomOwner: _Callable[[ISemanticZoom],  # value
                                     _type.HRESULT]
    get_IsActiveView: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_IsActiveView: _Callable[[_type.boolean],  # value
                                _type.HRESULT]
    get_IsZoomedInView: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    put_IsZoomedInView: _Callable[[_type.boolean],  # value
                                  _type.HRESULT]
    InitializeViewChange: _Callable[[],
                                    _type.HRESULT]
    CompleteViewChange: _Callable[[],
                                  _type.HRESULT]
    MakeVisible: _Callable[[ISemanticZoomLocation],  # item
                           _type.HRESULT]
    StartViewChangeFrom: _Callable[[ISemanticZoomLocation,  # source
                                    ISemanticZoomLocation],  # destination
                                   _type.HRESULT]
    StartViewChangeTo: _Callable[[ISemanticZoomLocation,  # source
                                  ISemanticZoomLocation],  # destination
                                 _type.HRESULT]
    CompleteViewChangeFrom: _Callable[[ISemanticZoomLocation,  # source
                                       ISemanticZoomLocation],  # destination
                                      _type.HRESULT]
    CompleteViewChangeTo: _Callable[[ISemanticZoomLocation,  # source
                                     ISemanticZoomLocation],  # destination
                                    _type.HRESULT]


class ISemanticZoomLocation(_inspectable.IInspectable):
    get_Item: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                        _type.HRESULT]
    put_Item: _Callable[[_inspectable.IInspectable],  # value
                        _type.HRESULT]
    get_Bounds: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                          _type.HRESULT]
    put_Bounds: _Callable[[_struct.Windows.Foundation.Rect],  # value
                          _type.HRESULT]


class ISemanticZoomStatics(_inspectable.IInspectable):
    get_ZoomedInViewProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_ZoomedOutViewProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_IsZoomedInViewActiveProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_CanChangeViewsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_IsZoomOutButtonEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]

    _factory = True


class ISemanticZoomViewChangedEventArgs(_inspectable.IInspectable):
    get_IsSourceZoomedInView: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    put_IsSourceZoomedInView: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]
    get_SourceItem: _Callable[[_Pointer[ISemanticZoomLocation]],  # value
                              _type.HRESULT]
    put_SourceItem: _Callable[[ISemanticZoomLocation],  # value
                              _type.HRESULT]
    get_DestinationItem: _Callable[[_Pointer[ISemanticZoomLocation]],  # value
                                   _type.HRESULT]
    put_DestinationItem: _Callable[[ISemanticZoomLocation],  # value
                                   _type.HRESULT]


class ISettingsFlyout(_inspectable.IInspectable):
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Title: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_HeaderBackground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                    _type.HRESULT]
    put_HeaderBackground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                    _type.HRESULT]
    get_HeaderForeground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                    _type.HRESULT]
    put_HeaderForeground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                    _type.HRESULT]
    get_IconSource: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IImageSource]],  # value
                              _type.HRESULT]
    put_IconSource: _Callable[[_Windows_UI_Xaml_Media.IImageSource],  # value
                              _type.HRESULT]
    get_TemplateSettings: _Callable[[_Pointer[_Windows_UI_Xaml_Controls_Primitives.ISettingsFlyoutTemplateSettings]],  # value
                                    _type.HRESULT]
    add_BackClick: _Callable[[IBackClickEventHandler,  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_BackClick: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    Show: _Callable[[],
                    _type.HRESULT]
    ShowIndependent: _Callable[[],
                               _type.HRESULT]
    Hide: _Callable[[],
                    _type.HRESULT]


class ISettingsFlyoutFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ISettingsFlyout]],  # value
                              _type.HRESULT]


class ISettingsFlyoutStatics(_inspectable.IInspectable):
    get_TitleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_HeaderBackgroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_HeaderForegroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_IconSourceProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]

    _factory = True


class ISlider(_inspectable.IInspectable):
    get_IntermediateValue: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                     _type.HRESULT]
    put_IntermediateValue: _Callable[[_type.DOUBLE],  # value
                                     _type.HRESULT]
    get_StepFrequency: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                 _type.HRESULT]
    put_StepFrequency: _Callable[[_type.DOUBLE],  # value
                                 _type.HRESULT]
    get_SnapsTo: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Primitives.SliderSnapsTo]],  # value
                           _type.HRESULT]
    put_SnapsTo: _Callable[[_enum.Windows.UI.Xaml.Controls.Primitives.SliderSnapsTo],  # value
                           _type.HRESULT]
    get_TickFrequency: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                 _type.HRESULT]
    put_TickFrequency: _Callable[[_type.DOUBLE],  # value
                                 _type.HRESULT]
    get_TickPlacement: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Primitives.TickPlacement]],  # value
                                 _type.HRESULT]
    put_TickPlacement: _Callable[[_enum.Windows.UI.Xaml.Controls.Primitives.TickPlacement],  # value
                                 _type.HRESULT]
    get_Orientation: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Orientation]],  # value
                               _type.HRESULT]
    put_Orientation: _Callable[[_enum.Windows.UI.Xaml.Controls.Orientation],  # value
                               _type.HRESULT]
    get_IsDirectionReversed: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_IsDirectionReversed: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_IsThumbToolTipEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_IsThumbToolTipEnabled: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]
    get_ThumbToolTipValueConverter: _Callable[[_Pointer[_Windows_UI_Xaml_Data.IValueConverter]],  # value
                                              _type.HRESULT]
    put_ThumbToolTipValueConverter: _Callable[[_Windows_UI_Xaml_Data.IValueConverter],  # value
                                              _type.HRESULT]


class ISlider2(_inspectable.IInspectable):
    get_Header: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                          _type.HRESULT]
    put_Header: _Callable[[_inspectable.IInspectable],  # value
                          _type.HRESULT]
    get_HeaderTemplate: _Callable[[_Pointer[_Windows_UI_Xaml.IDataTemplate]],  # value
                                  _type.HRESULT]
    put_HeaderTemplate: _Callable[[_Windows_UI_Xaml.IDataTemplate],  # value
                                  _type.HRESULT]


class ISliderFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ISlider]],  # value
                              _type.HRESULT]


class ISliderStatics(_inspectable.IInspectable):
    get_IntermediateValueProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_StepFrequencyProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_SnapsToProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_TickFrequencyProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_TickPlacementProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_OrientationProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_IsDirectionReversedProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_IsThumbToolTipEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_ThumbToolTipValueConverterProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                      _type.HRESULT]

    _factory = True


class ISliderStatics2(_inspectable.IInspectable):
    get_HeaderProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_HeaderTemplateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]

    _factory = True


class ISplitButton(_inspectable.IInspectable):
    get_Flyout: _Callable[[_Pointer[_Windows_UI_Xaml_Controls_Primitives.IFlyoutBase]],  # value
                          _type.HRESULT]
    put_Flyout: _Callable[[_Windows_UI_Xaml_Controls_Primitives.IFlyoutBase],  # value
                          _type.HRESULT]
    get_Command: _Callable[[_Pointer[_Windows_UI_Xaml_Input.ICommand]],  # value
                           _type.HRESULT]
    put_Command: _Callable[[_Windows_UI_Xaml_Input.ICommand],  # value
                           _type.HRESULT]
    get_CommandParameter: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                    _type.HRESULT]
    put_CommandParameter: _Callable[[_inspectable.IInspectable],  # value
                                    _type.HRESULT]
    add_Click: _Callable[[_Windows_Foundation.ITypedEventHandler[ISplitButton, ISplitButtonClickEventArgs],  # handler
                          _Pointer[_struct.EventRegistrationToken]],  # token
                         _type.HRESULT]
    remove_Click: _Callable[[_struct.EventRegistrationToken],  # token
                            _type.HRESULT]


class ISplitButtonAutomationPeer(_inspectable.IInspectable):
    pass


class ISplitButtonAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[ISplitButton,  # owner
                               _inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ISplitButtonAutomationPeer]],  # value
                              _type.HRESULT]


class ISplitButtonClickEventArgs(_inspectable.IInspectable):
    pass


class ISplitButtonFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ISplitButton]],  # value
                              _type.HRESULT]


class ISplitButtonStatics(_inspectable.IInspectable):
    get_FlyoutProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_CommandProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_CommandParameterProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]

    _factory = True


class ISplitView(_inspectable.IInspectable):
    get_Content: _Callable[[_Pointer[_Windows_UI_Xaml.IUIElement]],  # value
                           _type.HRESULT]
    put_Content: _Callable[[_Windows_UI_Xaml.IUIElement],  # value
                           _type.HRESULT]
    get_Pane: _Callable[[_Pointer[_Windows_UI_Xaml.IUIElement]],  # value
                        _type.HRESULT]
    put_Pane: _Callable[[_Windows_UI_Xaml.IUIElement],  # value
                        _type.HRESULT]
    get_IsPaneOpen: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    put_IsPaneOpen: _Callable[[_type.boolean],  # value
                              _type.HRESULT]
    get_OpenPaneLength: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    put_OpenPaneLength: _Callable[[_type.DOUBLE],  # value
                                  _type.HRESULT]
    get_CompactPaneLength: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                     _type.HRESULT]
    put_CompactPaneLength: _Callable[[_type.DOUBLE],  # value
                                     _type.HRESULT]
    get_PanePlacement: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.SplitViewPanePlacement]],  # value
                                 _type.HRESULT]
    put_PanePlacement: _Callable[[_enum.Windows.UI.Xaml.Controls.SplitViewPanePlacement],  # value
                                 _type.HRESULT]
    get_DisplayMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.SplitViewDisplayMode]],  # value
                               _type.HRESULT]
    put_DisplayMode: _Callable[[_enum.Windows.UI.Xaml.Controls.SplitViewDisplayMode],  # value
                               _type.HRESULT]
    get_TemplateSettings: _Callable[[_Pointer[_Windows_UI_Xaml_Controls_Primitives.ISplitViewTemplateSettings]],  # value
                                    _type.HRESULT]
    get_PaneBackground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                  _type.HRESULT]
    put_PaneBackground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                  _type.HRESULT]
    add_PaneClosing: _Callable[[_Windows_Foundation.ITypedEventHandler[ISplitView, ISplitViewPaneClosingEventArgs],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_PaneClosing: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    add_PaneClosed: _Callable[[_Windows_Foundation.ITypedEventHandler[ISplitView, _inspectable.IInspectable],  # handler
                               _Pointer[_struct.EventRegistrationToken]],  # token
                              _type.HRESULT]
    remove_PaneClosed: _Callable[[_struct.EventRegistrationToken],  # token
                                 _type.HRESULT]


class ISplitView2(_inspectable.IInspectable):
    get_LightDismissOverlayMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.LightDismissOverlayMode]],  # value
                                           _type.HRESULT]
    put_LightDismissOverlayMode: _Callable[[_enum.Windows.UI.Xaml.Controls.LightDismissOverlayMode],  # value
                                           _type.HRESULT]


class ISplitView3(_inspectable.IInspectable):
    add_PaneOpening: _Callable[[_Windows_Foundation.ITypedEventHandler[ISplitView, _inspectable.IInspectable],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_PaneOpening: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    add_PaneOpened: _Callable[[_Windows_Foundation.ITypedEventHandler[ISplitView, _inspectable.IInspectable],  # handler
                               _Pointer[_struct.EventRegistrationToken]],  # token
                              _type.HRESULT]
    remove_PaneOpened: _Callable[[_struct.EventRegistrationToken],  # token
                                 _type.HRESULT]


class ISplitViewFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ISplitView]],  # value
                              _type.HRESULT]


class ISplitViewPaneClosingEventArgs(_inspectable.IInspectable):
    get_Cancel: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_Cancel: _Callable[[_type.boolean],  # value
                          _type.HRESULT]


class ISplitViewStatics(_inspectable.IInspectable):
    get_ContentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_PaneProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]
    get_IsPaneOpenProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_OpenPaneLengthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_CompactPaneLengthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_PanePlacementProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_DisplayModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_TemplateSettingsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_PaneBackgroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]

    _factory = True


class ISplitViewStatics2(_inspectable.IInspectable):
    get_LightDismissOverlayModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]

    _factory = True


class IStackPanel(_inspectable.IInspectable):
    get_AreScrollSnapPointsRegular: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]
    put_AreScrollSnapPointsRegular: _Callable[[_type.boolean],  # value
                                              _type.HRESULT]
    get_Orientation: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Orientation]],  # value
                               _type.HRESULT]
    put_Orientation: _Callable[[_enum.Windows.UI.Xaml.Controls.Orientation],  # value
                               _type.HRESULT]


class IStackPanel2(_inspectable.IInspectable):
    get_BorderBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                               _type.HRESULT]
    put_BorderBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                               _type.HRESULT]
    get_BorderThickness: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                                   _type.HRESULT]
    put_BorderThickness: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                                   _type.HRESULT]
    get_CornerRadius: _Callable[[_Pointer[_struct.Windows.UI.Xaml.CornerRadius]],  # value
                                _type.HRESULT]
    put_CornerRadius: _Callable[[_struct.Windows.UI.Xaml.CornerRadius],  # value
                                _type.HRESULT]
    get_Padding: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                           _type.HRESULT]
    put_Padding: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                           _type.HRESULT]


class IStackPanel4(_inspectable.IInspectable):
    get_Spacing: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    put_Spacing: _Callable[[_type.DOUBLE],  # value
                           _type.HRESULT]


class IStackPanel5(_inspectable.IInspectable):
    get_BackgroundSizing: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.BackgroundSizing]],  # value
                                    _type.HRESULT]
    put_BackgroundSizing: _Callable[[_enum.Windows.UI.Xaml.Controls.BackgroundSizing],  # value
                                    _type.HRESULT]


class IStackPanelFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IStackPanel]],  # value
                              _type.HRESULT]


class IStackPanelStatics(_inspectable.IInspectable):
    get_AreScrollSnapPointsRegularProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                      _type.HRESULT]
    get_OrientationProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]

    _factory = True


class IStackPanelStatics2(_inspectable.IInspectable):
    get_BorderBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_BorderThicknessProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_CornerRadiusProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_PaddingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]

    _factory = True


class IStackPanelStatics4(_inspectable.IInspectable):
    get_SpacingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]

    _factory = True


class IStackPanelStatics5(_inspectable.IInspectable):
    get_BackgroundSizingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]

    _factory = True


class IStyleSelector(_inspectable.IInspectable):
    SelectStyle: _Callable[[_inspectable.IInspectable,  # item
                            _Windows_UI_Xaml.IDependencyObject,  # container
                            _Pointer[_Windows_UI_Xaml.IStyle]],  # result
                           _type.HRESULT]


class IStyleSelectorFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IStyleSelector]],  # value
                              _type.HRESULT]


class IStyleSelectorOverrides(_inspectable.IInspectable):
    SelectStyleCore: _Callable[[_inspectable.IInspectable,  # item
                                _Windows_UI_Xaml.IDependencyObject,  # container
                                _Pointer[_Windows_UI_Xaml.IStyle]],  # result
                               _type.HRESULT]


class ISwapChainBackgroundPanel(_inspectable.IInspectable):
    pass


class ISwapChainBackgroundPanel2(_inspectable.IInspectable):
    CreateCoreIndependentInputSource: _Callable[[_enum.Windows.UI.Core.CoreInputDeviceTypes,  # deviceTypes
                                                 _Pointer[_Windows_UI_Core.ICoreInputSourceBase]],  # result
                                                _type.HRESULT]


class ISwapChainBackgroundPanelFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ISwapChainBackgroundPanel]],  # value
                              _type.HRESULT]


class ISwapChainPanel(_inspectable.IInspectable):
    get_CompositionScaleX: _Callable[[_Pointer[_type.FLOAT]],  # value
                                     _type.HRESULT]
    get_CompositionScaleY: _Callable[[_Pointer[_type.FLOAT]],  # value
                                     _type.HRESULT]
    add_CompositionScaleChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ISwapChainPanel, _inspectable.IInspectable],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_CompositionScaleChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]
    CreateCoreIndependentInputSource: _Callable[[_enum.Windows.UI.Core.CoreInputDeviceTypes,  # deviceTypes
                                                 _Pointer[_Windows_UI_Core.ICoreInputSourceBase]],  # result
                                                _type.HRESULT]


class ISwapChainPanelFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ISwapChainPanel]],  # value
                              _type.HRESULT]


class ISwapChainPanelStatics(_inspectable.IInspectable):
    get_CompositionScaleXProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_CompositionScaleYProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]

    _factory = True


class ISwipeControl(_inspectable.IInspectable):
    get_LeftItems: _Callable[[_Pointer[ISwipeItems]],  # value
                             _type.HRESULT]
    put_LeftItems: _Callable[[ISwipeItems],  # value
                             _type.HRESULT]
    get_RightItems: _Callable[[_Pointer[ISwipeItems]],  # value
                              _type.HRESULT]
    put_RightItems: _Callable[[ISwipeItems],  # value
                              _type.HRESULT]
    get_TopItems: _Callable[[_Pointer[ISwipeItems]],  # value
                            _type.HRESULT]
    put_TopItems: _Callable[[ISwipeItems],  # value
                            _type.HRESULT]
    get_BottomItems: _Callable[[_Pointer[ISwipeItems]],  # value
                               _type.HRESULT]
    put_BottomItems: _Callable[[ISwipeItems],  # value
                               _type.HRESULT]
    Close: _Callable[[],
                     _type.HRESULT]


class ISwipeControlFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ISwipeControl]],  # value
                              _type.HRESULT]


class ISwipeControlStatics(_inspectable.IInspectable):
    get_LeftItemsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_RightItemsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_TopItemsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_BottomItemsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]

    _factory = True


class ISwipeItem(_inspectable.IInspectable):
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Text: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_IconSource: _Callable[[_Pointer[IIconSource]],  # value
                              _type.HRESULT]
    put_IconSource: _Callable[[IIconSource],  # value
                              _type.HRESULT]
    get_Background: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                              _type.HRESULT]
    put_Background: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                              _type.HRESULT]
    get_Foreground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                              _type.HRESULT]
    put_Foreground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                              _type.HRESULT]
    get_Command: _Callable[[_Pointer[_Windows_UI_Xaml_Input.ICommand]],  # value
                           _type.HRESULT]
    put_Command: _Callable[[_Windows_UI_Xaml_Input.ICommand],  # value
                           _type.HRESULT]
    get_CommandParameter: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                    _type.HRESULT]
    put_CommandParameter: _Callable[[_inspectable.IInspectable],  # value
                                    _type.HRESULT]
    get_BehaviorOnInvoked: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.SwipeBehaviorOnInvoked]],  # value
                                     _type.HRESULT]
    put_BehaviorOnInvoked: _Callable[[_enum.Windows.UI.Xaml.Controls.SwipeBehaviorOnInvoked],  # value
                                     _type.HRESULT]
    add_Invoked: _Callable[[_Windows_Foundation.ITypedEventHandler[ISwipeItem, ISwipeItemInvokedEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Invoked: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]


class ISwipeItemFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ISwipeItem]],  # value
                              _type.HRESULT]


class ISwipeItemInvokedEventArgs(_inspectable.IInspectable):
    get_SwipeControl: _Callable[[_Pointer[ISwipeControl]],  # value
                                _type.HRESULT]


class ISwipeItemStatics(_inspectable.IInspectable):
    get_IconSourceProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_TextProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]
    get_BackgroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_ForegroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_CommandProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_CommandParameterProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_BehaviorOnInvokedProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]

    _factory = True


class ISwipeItems(_inspectable.IInspectable):
    get_Mode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.SwipeMode]],  # value
                        _type.HRESULT]
    put_Mode: _Callable[[_enum.Windows.UI.Xaml.Controls.SwipeMode],  # value
                        _type.HRESULT]


class ISwipeItemsFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ISwipeItems]],  # value
                              _type.HRESULT]


class ISwipeItemsStatics(_inspectable.IInspectable):
    get_ModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]

    _factory = True


class ISymbolIcon(_inspectable.IInspectable):
    get_Symbol: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Symbol]],  # value
                          _type.HRESULT]
    put_Symbol: _Callable[[_enum.Windows.UI.Xaml.Controls.Symbol],  # value
                          _type.HRESULT]


class ISymbolIconFactory(_inspectable.IInspectable):
    CreateInstanceWithSymbol: _Callable[[_enum.Windows.UI.Xaml.Controls.Symbol,  # symbol
                                         _Pointer[ISymbolIcon]],  # value
                                        _type.HRESULT]

    _factory = True


class ISymbolIconSource(_inspectable.IInspectable):
    get_Symbol: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Symbol]],  # value
                          _type.HRESULT]
    put_Symbol: _Callable[[_enum.Windows.UI.Xaml.Controls.Symbol],  # value
                          _type.HRESULT]


class ISymbolIconSourceFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ISymbolIconSource]],  # value
                              _type.HRESULT]


class ISymbolIconSourceStatics(_inspectable.IInspectable):
    get_SymbolProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]

    _factory = True


class ISymbolIconStatics(_inspectable.IInspectable):
    get_SymbolProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]

    _factory = True


class ITextBlock(_inspectable.IInspectable):
    get_FontSize: _Callable[[_Pointer[_type.DOUBLE]],  # value
                            _type.HRESULT]
    put_FontSize: _Callable[[_type.DOUBLE],  # value
                            _type.HRESULT]
    get_FontFamily: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IFontFamily]],  # value
                              _type.HRESULT]
    put_FontFamily: _Callable[[_Windows_UI_Xaml_Media.IFontFamily],  # value
                              _type.HRESULT]
    get_FontWeight: _Callable[[_Pointer[_struct.Windows.UI.Text.FontWeight]],  # value
                              _type.HRESULT]
    put_FontWeight: _Callable[[_struct.Windows.UI.Text.FontWeight],  # value
                              _type.HRESULT]
    get_FontStyle: _Callable[[_Pointer[_enum.Windows.UI.Text.FontStyle]],  # value
                             _type.HRESULT]
    put_FontStyle: _Callable[[_enum.Windows.UI.Text.FontStyle],  # value
                             _type.HRESULT]
    get_FontStretch: _Callable[[_Pointer[_enum.Windows.UI.Text.FontStretch]],  # value
                               _type.HRESULT]
    put_FontStretch: _Callable[[_enum.Windows.UI.Text.FontStretch],  # value
                               _type.HRESULT]
    get_CharacterSpacing: _Callable[[_Pointer[_type.INT32]],  # value
                                    _type.HRESULT]
    put_CharacterSpacing: _Callable[[_type.INT32],  # value
                                    _type.HRESULT]
    get_Foreground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                              _type.HRESULT]
    put_Foreground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                              _type.HRESULT]
    get_TextWrapping: _Callable[[_Pointer[_enum.Windows.UI.Xaml.TextWrapping]],  # value
                                _type.HRESULT]
    put_TextWrapping: _Callable[[_enum.Windows.UI.Xaml.TextWrapping],  # value
                                _type.HRESULT]
    get_TextTrimming: _Callable[[_Pointer[_enum.Windows.UI.Xaml.TextTrimming]],  # value
                                _type.HRESULT]
    put_TextTrimming: _Callable[[_enum.Windows.UI.Xaml.TextTrimming],  # value
                                _type.HRESULT]
    get_TextAlignment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.TextAlignment]],  # value
                                 _type.HRESULT]
    put_TextAlignment: _Callable[[_enum.Windows.UI.Xaml.TextAlignment],  # value
                                 _type.HRESULT]
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Text: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_Inlines: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Documents.IInline]]],  # value
                           _type.HRESULT]
    get_Padding: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                           _type.HRESULT]
    put_Padding: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                           _type.HRESULT]
    get_LineHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                              _type.HRESULT]
    put_LineHeight: _Callable[[_type.DOUBLE],  # value
                              _type.HRESULT]
    get_LineStackingStrategy: _Callable[[_Pointer[_enum.Windows.UI.Xaml.LineStackingStrategy]],  # value
                                        _type.HRESULT]
    put_LineStackingStrategy: _Callable[[_enum.Windows.UI.Xaml.LineStackingStrategy],  # value
                                        _type.HRESULT]
    get_IsTextSelectionEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_IsTextSelectionEnabled: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    get_SelectedText: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_ContentStart: _Callable[[_Pointer[_Windows_UI_Xaml_Documents.ITextPointer]],  # value
                                _type.HRESULT]
    get_ContentEnd: _Callable[[_Pointer[_Windows_UI_Xaml_Documents.ITextPointer]],  # value
                              _type.HRESULT]
    get_SelectionStart: _Callable[[_Pointer[_Windows_UI_Xaml_Documents.ITextPointer]],  # value
                                  _type.HRESULT]
    get_SelectionEnd: _Callable[[_Pointer[_Windows_UI_Xaml_Documents.ITextPointer]],  # value
                                _type.HRESULT]
    get_BaselineOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    add_SelectionChanged: _Callable[[_Windows_UI_Xaml.IRoutedEventHandler,  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_SelectionChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    add_ContextMenuOpening: _Callable[[IContextMenuOpeningEventHandler,  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_ContextMenuOpening: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    SelectAll: _Callable[[],
                         _type.HRESULT]
    Select: _Callable[[_Windows_UI_Xaml_Documents.ITextPointer,  # start
                       _Windows_UI_Xaml_Documents.ITextPointer],  # end
                      _type.HRESULT]
    Focus: _Callable[[_enum.Windows.UI.Xaml.FocusState,  # value
                      _Pointer[_type.boolean]],  # result
                     _type.HRESULT]


class ITextBlock2(_inspectable.IInspectable):
    get_SelectionHighlightColor: _Callable[[_Pointer[_Windows_UI_Xaml_Media.ISolidColorBrush]],  # value
                                           _type.HRESULT]
    put_SelectionHighlightColor: _Callable[[_Windows_UI_Xaml_Media.ISolidColorBrush],  # value
                                           _type.HRESULT]
    get_MaxLines: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    put_MaxLines: _Callable[[_type.INT32],  # value
                            _type.HRESULT]
    get_TextLineBounds: _Callable[[_Pointer[_enum.Windows.UI.Xaml.TextLineBounds]],  # value
                                  _type.HRESULT]
    put_TextLineBounds: _Callable[[_enum.Windows.UI.Xaml.TextLineBounds],  # value
                                  _type.HRESULT]
    get_OpticalMarginAlignment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.OpticalMarginAlignment]],  # value
                                          _type.HRESULT]
    put_OpticalMarginAlignment: _Callable[[_enum.Windows.UI.Xaml.OpticalMarginAlignment],  # value
                                          _type.HRESULT]
    get_IsColorFontEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_IsColorFontEnabled: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    get_TextReadingOrder: _Callable[[_Pointer[_enum.Windows.UI.Xaml.TextReadingOrder]],  # value
                                    _type.HRESULT]
    put_TextReadingOrder: _Callable[[_enum.Windows.UI.Xaml.TextReadingOrder],  # value
                                    _type.HRESULT]


class ITextBlock3(_inspectable.IInspectable):
    get_IsTextScaleFactorEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_IsTextScaleFactorEnabled: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]


class ITextBlock4(_inspectable.IInspectable):
    GetAlphaMask: _Callable[[_Pointer[_Windows_UI_Composition.ICompositionBrush]],  # result
                            _type.HRESULT]


class ITextBlock5(_inspectable.IInspectable):
    get_TextDecorations: _Callable[[_Pointer[_enum.Windows.UI.Text.TextDecorations]],  # value
                                   _type.HRESULT]
    put_TextDecorations: _Callable[[_enum.Windows.UI.Text.TextDecorations],  # value
                                   _type.HRESULT]


class ITextBlock6(_inspectable.IInspectable):
    get_IsTextTrimmed: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_HorizontalTextAlignment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.TextAlignment]],  # value
                                           _type.HRESULT]
    put_HorizontalTextAlignment: _Callable[[_enum.Windows.UI.Xaml.TextAlignment],  # value
                                           _type.HRESULT]
    get_TextHighlighters: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Documents.ITextHighlighter]]],  # value
                                    _type.HRESULT]
    add_IsTextTrimmedChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ITextBlock, IIsTextTrimmedChangedEventArgs],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_IsTextTrimmedChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]


class ITextBlock7(_inspectable.IInspectable):
    get_SelectionFlyout: _Callable[[_Pointer[_Windows_UI_Xaml_Controls_Primitives.IFlyoutBase]],  # value
                                   _type.HRESULT]
    put_SelectionFlyout: _Callable[[_Windows_UI_Xaml_Controls_Primitives.IFlyoutBase],  # value
                                   _type.HRESULT]
    CopySelectionToClipboard: _Callable[[],
                                        _type.HRESULT]


class ITextBlockStatics(_inspectable.IInspectable):
    get_FontSizeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_FontFamilyProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_FontWeightProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_FontStyleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_FontStretchProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_CharacterSpacingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_ForegroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_TextWrappingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_TextTrimmingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_TextAlignmentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_TextProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]
    get_PaddingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_LineHeightProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_LineStackingStrategyProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_IsTextSelectionEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]
    get_SelectedTextProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]

    _factory = True


class ITextBlockStatics2(_inspectable.IInspectable):
    get_SelectionHighlightColorProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_MaxLinesProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_TextLineBoundsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_OpticalMarginAlignmentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]
    get_IsColorFontEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_TextReadingOrderProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]

    _factory = True


class ITextBlockStatics3(_inspectable.IInspectable):
    get_IsTextScaleFactorEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]

    _factory = True


class ITextBlockStatics5(_inspectable.IInspectable):
    get_TextDecorationsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]

    _factory = True


class ITextBlockStatics6(_inspectable.IInspectable):
    get_IsTextTrimmedProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_HorizontalTextAlignmentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]

    _factory = True


class ITextBlockStatics7(_inspectable.IInspectable):
    get_SelectionFlyoutProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]

    _factory = True


class ITextBox(_inspectable.IInspectable):
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Text: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_SelectedText: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    put_SelectedText: _Callable[[_type.HSTRING],  # value
                                _type.HRESULT]
    get_SelectionLength: _Callable[[_Pointer[_type.INT32]],  # value
                                   _type.HRESULT]
    put_SelectionLength: _Callable[[_type.INT32],  # value
                                   _type.HRESULT]
    get_SelectionStart: _Callable[[_Pointer[_type.INT32]],  # value
                                  _type.HRESULT]
    put_SelectionStart: _Callable[[_type.INT32],  # value
                                  _type.HRESULT]
    get_MaxLength: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]
    put_MaxLength: _Callable[[_type.INT32],  # value
                             _type.HRESULT]
    get_IsReadOnly: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    put_IsReadOnly: _Callable[[_type.boolean],  # value
                              _type.HRESULT]
    get_AcceptsReturn: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_AcceptsReturn: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_TextAlignment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.TextAlignment]],  # value
                                 _type.HRESULT]
    put_TextAlignment: _Callable[[_enum.Windows.UI.Xaml.TextAlignment],  # value
                                 _type.HRESULT]
    get_TextWrapping: _Callable[[_Pointer[_enum.Windows.UI.Xaml.TextWrapping]],  # value
                                _type.HRESULT]
    put_TextWrapping: _Callable[[_enum.Windows.UI.Xaml.TextWrapping],  # value
                                _type.HRESULT]
    get_IsSpellCheckEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_IsSpellCheckEnabled: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_IsTextPredictionEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    put_IsTextPredictionEnabled: _Callable[[_type.boolean],  # value
                                           _type.HRESULT]
    get_InputScope: _Callable[[_Pointer[_Windows_UI_Xaml_Input.IInputScope]],  # value
                              _type.HRESULT]
    put_InputScope: _Callable[[_Windows_UI_Xaml_Input.IInputScope],  # value
                              _type.HRESULT]
    add_TextChanged: _Callable[[ITextChangedEventHandler,  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_TextChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    add_SelectionChanged: _Callable[[_Windows_UI_Xaml.IRoutedEventHandler,  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_SelectionChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    add_ContextMenuOpening: _Callable[[IContextMenuOpeningEventHandler,  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_ContextMenuOpening: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    Select: _Callable[[_type.INT32,  # start
                       _type.INT32],  # length
                      _type.HRESULT]
    SelectAll: _Callable[[],
                         _type.HRESULT]
    GetRectFromCharacterIndex: _Callable[[_type.INT32,  # charIndex
                                          _type.boolean,  # trailingEdge
                                          _Pointer[_struct.Windows.Foundation.Rect]],  # result
                                         _type.HRESULT]


class ITextBox2(_inspectable.IInspectable):
    get_Header: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                          _type.HRESULT]
    put_Header: _Callable[[_inspectable.IInspectable],  # value
                          _type.HRESULT]
    get_HeaderTemplate: _Callable[[_Pointer[_Windows_UI_Xaml.IDataTemplate]],  # value
                                  _type.HRESULT]
    put_HeaderTemplate: _Callable[[_Windows_UI_Xaml.IDataTemplate],  # value
                                  _type.HRESULT]
    get_PlaceholderText: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    put_PlaceholderText: _Callable[[_type.HSTRING],  # value
                                   _type.HRESULT]
    get_SelectionHighlightColor: _Callable[[_Pointer[_Windows_UI_Xaml_Media.ISolidColorBrush]],  # value
                                           _type.HRESULT]
    put_SelectionHighlightColor: _Callable[[_Windows_UI_Xaml_Media.ISolidColorBrush],  # value
                                           _type.HRESULT]
    get_PreventKeyboardDisplayOnProgrammaticFocus: _Callable[[_Pointer[_type.boolean]],  # value
                                                             _type.HRESULT]
    put_PreventKeyboardDisplayOnProgrammaticFocus: _Callable[[_type.boolean],  # value
                                                             _type.HRESULT]
    get_IsColorFontEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_IsColorFontEnabled: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    add_Paste: _Callable[[ITextControlPasteEventHandler,  # handler
                          _Pointer[_struct.EventRegistrationToken]],  # token
                         _type.HRESULT]
    remove_Paste: _Callable[[_struct.EventRegistrationToken],  # token
                            _type.HRESULT]


class ITextBox3(_inspectable.IInspectable):
    add_TextCompositionStarted: _Callable[[_Windows_Foundation.ITypedEventHandler[ITextBox, ITextCompositionStartedEventArgs],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_TextCompositionStarted: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]
    add_TextCompositionChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ITextBox, ITextCompositionChangedEventArgs],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_TextCompositionChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]
    add_TextCompositionEnded: _Callable[[_Windows_Foundation.ITypedEventHandler[ITextBox, ITextCompositionEndedEventArgs],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_TextCompositionEnded: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    get_TextReadingOrder: _Callable[[_Pointer[_enum.Windows.UI.Xaml.TextReadingOrder]],  # value
                                    _type.HRESULT]
    put_TextReadingOrder: _Callable[[_enum.Windows.UI.Xaml.TextReadingOrder],  # value
                                    _type.HRESULT]
    get_DesiredCandidateWindowAlignment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.CandidateWindowAlignment]],  # value
                                                   _type.HRESULT]
    put_DesiredCandidateWindowAlignment: _Callable[[_enum.Windows.UI.Xaml.Controls.CandidateWindowAlignment],  # value
                                                   _type.HRESULT]
    add_CandidateWindowBoundsChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ITextBox, ICandidateWindowBoundsChangedEventArgs],  # handler
                                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                                _type.HRESULT]
    remove_CandidateWindowBoundsChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                   _type.HRESULT]
    add_TextChanging: _Callable[[_Windows_Foundation.ITypedEventHandler[ITextBox, ITextBoxTextChangingEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_TextChanging: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]


class ITextBox4(_inspectable.IInspectable):
    GetLinguisticAlternativesAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]]],  # operation
                                              _type.HRESULT]


class ITextBox5(_inspectable.IInspectable):
    get_SelectionHighlightColorWhenNotFocused: _Callable[[_Pointer[_Windows_UI_Xaml_Media.ISolidColorBrush]],  # value
                                                         _type.HRESULT]
    put_SelectionHighlightColorWhenNotFocused: _Callable[[_Windows_UI_Xaml_Media.ISolidColorBrush],  # value
                                                         _type.HRESULT]


class ITextBox6(_inspectable.IInspectable):
    get_HorizontalTextAlignment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.TextAlignment]],  # value
                                           _type.HRESULT]
    put_HorizontalTextAlignment: _Callable[[_enum.Windows.UI.Xaml.TextAlignment],  # value
                                           _type.HRESULT]
    get_CharacterCasing: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.CharacterCasing]],  # value
                                   _type.HRESULT]
    put_CharacterCasing: _Callable[[_enum.Windows.UI.Xaml.Controls.CharacterCasing],  # value
                                   _type.HRESULT]
    get_PlaceholderForeground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                         _type.HRESULT]
    put_PlaceholderForeground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                         _type.HRESULT]
    add_CopyingToClipboard: _Callable[[_Windows_Foundation.ITypedEventHandler[ITextBox, ITextControlCopyingToClipboardEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_CopyingToClipboard: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_CuttingToClipboard: _Callable[[_Windows_Foundation.ITypedEventHandler[ITextBox, ITextControlCuttingToClipboardEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_CuttingToClipboard: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_BeforeTextChanging: _Callable[[_Windows_Foundation.ITypedEventHandler[ITextBox, ITextBoxBeforeTextChangingEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_BeforeTextChanging: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]


class ITextBox7(_inspectable.IInspectable):
    get_HandwritingView: _Callable[[_Pointer[IHandwritingView]],  # value
                                   _type.HRESULT]
    put_HandwritingView: _Callable[[IHandwritingView],  # value
                                   _type.HRESULT]
    get_IsHandwritingViewEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_IsHandwritingViewEnabled: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]


class ITextBox8(_inspectable.IInspectable):
    get_CanPasteClipboardContent: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    get_CanUndo: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_CanRedo: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_SelectionFlyout: _Callable[[_Pointer[_Windows_UI_Xaml_Controls_Primitives.IFlyoutBase]],  # value
                                   _type.HRESULT]
    put_SelectionFlyout: _Callable[[_Windows_UI_Xaml_Controls_Primitives.IFlyoutBase],  # value
                                   _type.HRESULT]
    get_ProofingMenuFlyout: _Callable[[_Pointer[_Windows_UI_Xaml_Controls_Primitives.IFlyoutBase]],  # value
                                      _type.HRESULT]
    get_Description: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_inspectable.IInspectable],  # value
                               _type.HRESULT]
    add_SelectionChanging: _Callable[[_Windows_Foundation.ITypedEventHandler[ITextBox, ITextBoxSelectionChangingEventArgs],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_SelectionChanging: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    Undo: _Callable[[],
                    _type.HRESULT]
    Redo: _Callable[[],
                    _type.HRESULT]
    PasteFromClipboard: _Callable[[],
                                  _type.HRESULT]
    CopySelectionToClipboard: _Callable[[],
                                        _type.HRESULT]
    CutSelectionToClipboard: _Callable[[],
                                       _type.HRESULT]
    ClearUndoRedoHistory: _Callable[[],
                                    _type.HRESULT]


class ITextBoxBeforeTextChangingEventArgs(_inspectable.IInspectable):
    get_NewText: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Cancel: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_Cancel: _Callable[[_type.boolean],  # value
                          _type.HRESULT]


class ITextBoxFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ITextBox]],  # value
                              _type.HRESULT]


class ITextBoxSelectionChangingEventArgs(_inspectable.IInspectable):
    get_SelectionStart: _Callable[[_Pointer[_type.INT32]],  # value
                                  _type.HRESULT]
    get_SelectionLength: _Callable[[_Pointer[_type.INT32]],  # value
                                   _type.HRESULT]
    get_Cancel: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_Cancel: _Callable[[_type.boolean],  # value
                          _type.HRESULT]


class ITextBoxStatics(_inspectable.IInspectable):
    get_TextProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]
    get_MaxLengthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_IsReadOnlyProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_AcceptsReturnProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_TextAlignmentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_TextWrappingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_IsSpellCheckEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_IsTextPredictionEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_InputScopeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]

    _factory = True


class ITextBoxStatics2(_inspectable.IInspectable):
    get_HeaderProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_HeaderTemplateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_PlaceholderTextProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_SelectionHighlightColorProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_PreventKeyboardDisplayOnProgrammaticFocusProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                                     _type.HRESULT]
    get_IsColorFontEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]

    _factory = True


class ITextBoxStatics3(_inspectable.IInspectable):
    get_DesiredCandidateWindowAlignmentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                           _type.HRESULT]
    get_TextReadingOrderProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]

    _factory = True


class ITextBoxStatics5(_inspectable.IInspectable):
    get_SelectionHighlightColorWhenNotFocusedProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                                 _type.HRESULT]

    _factory = True


class ITextBoxStatics6(_inspectable.IInspectable):
    get_HorizontalTextAlignmentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_CharacterCasingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_PlaceholderForegroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]

    _factory = True


class ITextBoxStatics7(_inspectable.IInspectable):
    get_HandwritingViewProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_IsHandwritingViewEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]

    _factory = True


class ITextBoxStatics8(_inspectable.IInspectable):
    get_CanPasteClipboardContentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]
    get_CanUndoProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_CanRedoProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_SelectionFlyoutProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_ProofingMenuFlyoutProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_DescriptionProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]

    _factory = True


class ITextBoxTextChangingEventArgs(_inspectable.IInspectable):
    pass


class ITextBoxTextChangingEventArgs2(_inspectable.IInspectable):
    get_IsContentChanging: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]


class ITextChangedEventArgs(_inspectable.IInspectable):
    pass


class ITextCommandBarFlyout(_inspectable.IInspectable):
    pass


class ITextCommandBarFlyoutFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ITextCommandBarFlyout]],  # value
                              _type.HRESULT]


class ITextCompositionChangedEventArgs(_inspectable.IInspectable):
    get_StartIndex: _Callable[[_Pointer[_type.INT32]],  # value
                              _type.HRESULT]
    get_Length: _Callable[[_Pointer[_type.INT32]],  # value
                          _type.HRESULT]


class ITextCompositionEndedEventArgs(_inspectable.IInspectable):
    get_StartIndex: _Callable[[_Pointer[_type.INT32]],  # value
                              _type.HRESULT]
    get_Length: _Callable[[_Pointer[_type.INT32]],  # value
                          _type.HRESULT]


class ITextCompositionStartedEventArgs(_inspectable.IInspectable):
    get_StartIndex: _Callable[[_Pointer[_type.INT32]],  # value
                              _type.HRESULT]
    get_Length: _Callable[[_Pointer[_type.INT32]],  # value
                          _type.HRESULT]


class ITextControlCopyingToClipboardEventArgs(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class ITextControlCuttingToClipboardEventArgs(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class ITextControlPasteEventArgs(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class ITimePickedEventArgs(_inspectable.IInspectable):
    get_OldTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                           _type.HRESULT]
    get_NewTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                           _type.HRESULT]


class ITimePicker(_inspectable.IInspectable):
    get_Header: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                          _type.HRESULT]
    put_Header: _Callable[[_inspectable.IInspectable],  # value
                          _type.HRESULT]
    get_HeaderTemplate: _Callable[[_Pointer[_Windows_UI_Xaml.IDataTemplate]],  # value
                                  _type.HRESULT]
    put_HeaderTemplate: _Callable[[_Windows_UI_Xaml.IDataTemplate],  # value
                                  _type.HRESULT]
    get_ClockIdentifier: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    put_ClockIdentifier: _Callable[[_type.HSTRING],  # value
                                   _type.HRESULT]
    get_MinuteIncrement: _Callable[[_Pointer[_type.INT32]],  # value
                                   _type.HRESULT]
    put_MinuteIncrement: _Callable[[_type.INT32],  # value
                                   _type.HRESULT]
    get_Time: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                        _type.HRESULT]
    put_Time: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                        _type.HRESULT]
    add_TimeChanged: _Callable[[_Windows_Foundation.IEventHandler[ITimePickerValueChangedEventArgs],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_TimeChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]


class ITimePicker2(_inspectable.IInspectable):
    get_LightDismissOverlayMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.LightDismissOverlayMode]],  # value
                                           _type.HRESULT]
    put_LightDismissOverlayMode: _Callable[[_enum.Windows.UI.Xaml.Controls.LightDismissOverlayMode],  # value
                                           _type.HRESULT]


class ITimePicker3(_inspectable.IInspectable):
    get_SelectedTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                _type.HRESULT]
    put_SelectedTime: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]],  # value
                                _type.HRESULT]
    add_SelectedTimeChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ITimePicker, ITimePickerSelectedValueChangedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_SelectedTimeChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]


class ITimePickerFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ITimePicker]],  # value
                              _type.HRESULT]


class ITimePickerFlyout(_inspectable.IInspectable):
    get_ClockIdentifier: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    put_ClockIdentifier: _Callable[[_type.HSTRING],  # value
                                   _type.HRESULT]
    get_Time: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                        _type.HRESULT]
    put_Time: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                        _type.HRESULT]
    get_MinuteIncrement: _Callable[[_Pointer[_type.INT32]],  # value
                                   _type.HRESULT]
    put_MinuteIncrement: _Callable[[_type.INT32],  # value
                                   _type.HRESULT]
    add_TimePicked: _Callable[[_Windows_Foundation.ITypedEventHandler[ITimePickerFlyout, ITimePickedEventArgs],  # handler
                               _Pointer[_struct.EventRegistrationToken]],  # token
                              _type.HRESULT]
    remove_TimePicked: _Callable[[_struct.EventRegistrationToken],  # token
                                 _type.HRESULT]
    ShowAtAsync: _Callable[[_Windows_UI_Xaml.IFrameworkElement,  # target
                            _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]]],  # operation
                           _type.HRESULT]


class ITimePickerFlyoutPresenter(_inspectable.IInspectable):
    pass


class ITimePickerFlyoutPresenter2(_inspectable.IInspectable):
    get_IsDefaultShadowEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_IsDefaultShadowEnabled: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]


class ITimePickerFlyoutPresenterStatics2(_inspectable.IInspectable):
    get_IsDefaultShadowEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]

    _factory = True


class ITimePickerFlyoutStatics(_inspectable.IInspectable):
    get_ClockIdentifierProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_TimeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]
    get_MinuteIncrementProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]

    _factory = True


class ITimePickerSelectedValueChangedEventArgs(_inspectable.IInspectable):
    get_OldTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                           _type.HRESULT]
    get_NewTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                           _type.HRESULT]


class ITimePickerStatics(_inspectable.IInspectable):
    get_HeaderProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_HeaderTemplateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_ClockIdentifierProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_MinuteIncrementProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_TimeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]

    _factory = True


class ITimePickerStatics2(_inspectable.IInspectable):
    get_LightDismissOverlayModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]

    _factory = True


class ITimePickerStatics3(_inspectable.IInspectable):
    get_SelectedTimeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]

    _factory = True


class ITimePickerValueChangedEventArgs(_inspectable.IInspectable):
    get_OldTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                           _type.HRESULT]
    get_NewTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                           _type.HRESULT]


class IToggleMenuFlyoutItem(_inspectable.IInspectable):
    get_IsChecked: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsChecked: _Callable[[_type.boolean],  # value
                             _type.HRESULT]


class IToggleMenuFlyoutItemFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IToggleMenuFlyoutItem]],  # value
                              _type.HRESULT]


class IToggleMenuFlyoutItemStatics(_inspectable.IInspectable):
    get_IsCheckedProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]

    _factory = True


class IToggleSplitButton(_inspectable.IInspectable):
    get_IsChecked: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsChecked: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    add_IsCheckedChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IToggleSplitButton, IToggleSplitButtonIsCheckedChangedEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_IsCheckedChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]


class IToggleSplitButtonAutomationPeer(_inspectable.IInspectable):
    pass


class IToggleSplitButtonAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[IToggleSplitButton,  # owner
                               _inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IToggleSplitButtonAutomationPeer]],  # value
                              _type.HRESULT]


class IToggleSplitButtonFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IToggleSplitButton]],  # value
                              _type.HRESULT]


class IToggleSplitButtonIsCheckedChangedEventArgs(_inspectable.IInspectable):
    pass


class IToggleSwitch(_inspectable.IInspectable):
    get_IsOn: _Callable[[_Pointer[_type.boolean]],  # value
                        _type.HRESULT]
    put_IsOn: _Callable[[_type.boolean],  # value
                        _type.HRESULT]
    get_Header: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                          _type.HRESULT]
    put_Header: _Callable[[_inspectable.IInspectable],  # value
                          _type.HRESULT]
    get_HeaderTemplate: _Callable[[_Pointer[_Windows_UI_Xaml.IDataTemplate]],  # value
                                  _type.HRESULT]
    put_HeaderTemplate: _Callable[[_Windows_UI_Xaml.IDataTemplate],  # value
                                  _type.HRESULT]
    get_OnContent: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                             _type.HRESULT]
    put_OnContent: _Callable[[_inspectable.IInspectable],  # value
                             _type.HRESULT]
    get_OnContentTemplate: _Callable[[_Pointer[_Windows_UI_Xaml.IDataTemplate]],  # value
                                     _type.HRESULT]
    put_OnContentTemplate: _Callable[[_Windows_UI_Xaml.IDataTemplate],  # value
                                     _type.HRESULT]
    get_OffContent: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                              _type.HRESULT]
    put_OffContent: _Callable[[_inspectable.IInspectable],  # value
                              _type.HRESULT]
    get_OffContentTemplate: _Callable[[_Pointer[_Windows_UI_Xaml.IDataTemplate]],  # value
                                      _type.HRESULT]
    put_OffContentTemplate: _Callable[[_Windows_UI_Xaml.IDataTemplate],  # value
                                      _type.HRESULT]
    get_TemplateSettings: _Callable[[_Pointer[_Windows_UI_Xaml_Controls_Primitives.IToggleSwitchTemplateSettings]],  # value
                                    _type.HRESULT]
    add_Toggled: _Callable[[_Windows_UI_Xaml.IRoutedEventHandler,  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Toggled: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]


class IToggleSwitchOverrides(_inspectable.IInspectable):
    OnToggled: _Callable[[],
                         _type.HRESULT]
    OnOnContentChanged: _Callable[[_inspectable.IInspectable,  # oldContent
                                   _inspectable.IInspectable],  # newContent
                                  _type.HRESULT]
    OnOffContentChanged: _Callable[[_inspectable.IInspectable,  # oldContent
                                    _inspectable.IInspectable],  # newContent
                                   _type.HRESULT]
    OnHeaderChanged: _Callable[[_inspectable.IInspectable,  # oldContent
                                _inspectable.IInspectable],  # newContent
                               _type.HRESULT]


class IToggleSwitchStatics(_inspectable.IInspectable):
    get_IsOnProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]
    get_HeaderProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_HeaderTemplateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_OnContentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_OnContentTemplateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_OffContentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_OffContentTemplateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]

    _factory = True


class IToolTip(_inspectable.IInspectable):
    get_HorizontalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]
    put_HorizontalOffset: _Callable[[_type.DOUBLE],  # value
                                    _type.HRESULT]
    get_IsOpen: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_IsOpen: _Callable[[_type.boolean],  # value
                          _type.HRESULT]
    get_Placement: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Primitives.PlacementMode]],  # value
                             _type.HRESULT]
    put_Placement: _Callable[[_enum.Windows.UI.Xaml.Controls.Primitives.PlacementMode],  # value
                             _type.HRESULT]
    get_PlacementTarget: _Callable[[_Pointer[_Windows_UI_Xaml.IUIElement]],  # value
                                   _type.HRESULT]
    put_PlacementTarget: _Callable[[_Windows_UI_Xaml.IUIElement],  # value
                                   _type.HRESULT]
    get_VerticalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    put_VerticalOffset: _Callable[[_type.DOUBLE],  # value
                                  _type.HRESULT]
    get_TemplateSettings: _Callable[[_Pointer[_Windows_UI_Xaml_Controls_Primitives.IToolTipTemplateSettings]],  # value
                                    _type.HRESULT]
    add_Closed: _Callable[[_Windows_UI_Xaml.IRoutedEventHandler,  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Closed: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    add_Opened: _Callable[[_Windows_UI_Xaml.IRoutedEventHandler,  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Opened: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]


class IToolTip2(_inspectable.IInspectable):
    get_PlacementRect: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.Rect]]],  # value
                                 _type.HRESULT]
    put_PlacementRect: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.Rect]],  # value
                                 _type.HRESULT]


class IToolTipFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IToolTip]],  # value
                              _type.HRESULT]


class IToolTipService(_inspectable.IInspectable):
    pass


class IToolTipServiceStatics(_inspectable.IInspectable):
    get_PlacementProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    GetPlacement: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                             _Pointer[_enum.Windows.UI.Xaml.Controls.Primitives.PlacementMode]],  # result
                            _type.HRESULT]
    SetPlacement: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                             _enum.Windows.UI.Xaml.Controls.Primitives.PlacementMode],  # value
                            _type.HRESULT]
    get_PlacementTargetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    GetPlacementTarget: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                   _Pointer[_Windows_UI_Xaml.IUIElement]],  # result
                                  _type.HRESULT]
    SetPlacementTarget: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                   _Windows_UI_Xaml.IUIElement],  # value
                                  _type.HRESULT]
    get_ToolTipProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    GetToolTip: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                           _Pointer[_inspectable.IInspectable]],  # result
                          _type.HRESULT]
    SetToolTip: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                           _inspectable.IInspectable],  # value
                          _type.HRESULT]

    _factory = True


class IToolTipStatics(_inspectable.IInspectable):
    get_HorizontalOffsetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_IsOpenProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_PlacementProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_PlacementTargetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_VerticalOffsetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]

    _factory = True


class IToolTipStatics2(_inspectable.IInspectable):
    get_PlacementRectProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]

    _factory = True


class ITreeView(_inspectable.IInspectable):
    get_RootNodes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ITreeViewNode]]],  # value
                             _type.HRESULT]
    get_SelectionMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.TreeViewSelectionMode]],  # value
                                 _type.HRESULT]
    put_SelectionMode: _Callable[[_enum.Windows.UI.Xaml.Controls.TreeViewSelectionMode],  # value
                                 _type.HRESULT]
    get_SelectedNodes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ITreeViewNode]]],  # value
                                 _type.HRESULT]
    Expand: _Callable[[ITreeViewNode],  # value
                      _type.HRESULT]
    Collapse: _Callable[[ITreeViewNode],  # value
                        _type.HRESULT]
    SelectAll: _Callable[[],
                         _type.HRESULT]
    add_ItemInvoked: _Callable[[_Windows_Foundation.ITypedEventHandler[ITreeView, ITreeViewItemInvokedEventArgs],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_ItemInvoked: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    add_Expanding: _Callable[[_Windows_Foundation.ITypedEventHandler[ITreeView, ITreeViewExpandingEventArgs],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_Expanding: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    add_Collapsed: _Callable[[_Windows_Foundation.ITypedEventHandler[ITreeView, ITreeViewCollapsedEventArgs],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_Collapsed: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]


class ITreeView2(_inspectable.IInspectable):
    NodeFromContainer: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # container
                                  _Pointer[ITreeViewNode]],  # result
                                 _type.HRESULT]
    ContainerFromNode: _Callable[[ITreeViewNode,  # node
                                  _Pointer[_Windows_UI_Xaml.IDependencyObject]],  # result
                                 _type.HRESULT]
    ItemFromContainer: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # container
                                  _Pointer[_inspectable.IInspectable]],  # result
                                 _type.HRESULT]
    ContainerFromItem: _Callable[[_inspectable.IInspectable,  # item
                                  _Pointer[_Windows_UI_Xaml.IDependencyObject]],  # result
                                 _type.HRESULT]
    get_CanDragItems: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_CanDragItems: _Callable[[_type.boolean],  # value
                                _type.HRESULT]
    get_CanReorderItems: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    put_CanReorderItems: _Callable[[_type.boolean],  # value
                                   _type.HRESULT]
    get_ItemTemplate: _Callable[[_Pointer[_Windows_UI_Xaml.IDataTemplate]],  # value
                                _type.HRESULT]
    put_ItemTemplate: _Callable[[_Windows_UI_Xaml.IDataTemplate],  # value
                                _type.HRESULT]
    get_ItemTemplateSelector: _Callable[[_Pointer[IDataTemplateSelector]],  # value
                                        _type.HRESULT]
    put_ItemTemplateSelector: _Callable[[IDataTemplateSelector],  # value
                                        _type.HRESULT]
    get_ItemContainerStyle: _Callable[[_Pointer[_Windows_UI_Xaml.IStyle]],  # value
                                      _type.HRESULT]
    put_ItemContainerStyle: _Callable[[_Windows_UI_Xaml.IStyle],  # value
                                      _type.HRESULT]
    get_ItemContainerStyleSelector: _Callable[[_Pointer[IStyleSelector]],  # value
                                              _type.HRESULT]
    put_ItemContainerStyleSelector: _Callable[[IStyleSelector],  # value
                                              _type.HRESULT]
    get_ItemContainerTransitions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Media_Animation.ITransition]]],  # value
                                            _type.HRESULT]
    put_ItemContainerTransitions: _Callable[[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Media_Animation.ITransition]],  # value
                                            _type.HRESULT]
    get_ItemsSource: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                               _type.HRESULT]
    put_ItemsSource: _Callable[[_inspectable.IInspectable],  # value
                               _type.HRESULT]
    add_DragItemsStarting: _Callable[[_Windows_Foundation.ITypedEventHandler[ITreeView, ITreeViewDragItemsStartingEventArgs],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_DragItemsStarting: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    add_DragItemsCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[ITreeView, ITreeViewDragItemsCompletedEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_DragItemsCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]


class ITreeViewCollapsedEventArgs(_inspectable.IInspectable):
    get_Node: _Callable[[_Pointer[ITreeViewNode]],  # value
                        _type.HRESULT]


class ITreeViewCollapsedEventArgs2(_inspectable.IInspectable):
    get_Item: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                        _type.HRESULT]


class ITreeViewDragItemsCompletedEventArgs(_inspectable.IInspectable):
    get_DropResult: _Callable[[_Pointer[_enum.Windows.ApplicationModel.DataTransfer.DataPackageOperation]],  # value
                              _type.HRESULT]
    get_Items: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_inspectable.IInspectable]]],  # value
                         _type.HRESULT]


class ITreeViewDragItemsStartingEventArgs(_inspectable.IInspectable):
    get_Cancel: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_Cancel: _Callable[[_type.boolean],  # value
                          _type.HRESULT]
    get_Data: _Callable[[_Pointer[_Windows_ApplicationModel_DataTransfer.IDataPackage]],  # value
                        _type.HRESULT]
    get_Items: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_inspectable.IInspectable]]],  # value
                         _type.HRESULT]


class ITreeViewExpandingEventArgs(_inspectable.IInspectable):
    get_Node: _Callable[[_Pointer[ITreeViewNode]],  # value
                        _type.HRESULT]


class ITreeViewExpandingEventArgs2(_inspectable.IInspectable):
    get_Item: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                        _type.HRESULT]


class ITreeViewFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ITreeView]],  # value
                              _type.HRESULT]


class ITreeViewItem(_inspectable.IInspectable):
    get_GlyphOpacity: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    put_GlyphOpacity: _Callable[[_type.DOUBLE],  # value
                                _type.HRESULT]
    get_GlyphBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                              _type.HRESULT]
    put_GlyphBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                              _type.HRESULT]
    get_ExpandedGlyph: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    put_ExpandedGlyph: _Callable[[_type.HSTRING],  # value
                                 _type.HRESULT]
    get_CollapsedGlyph: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    put_CollapsedGlyph: _Callable[[_type.HSTRING],  # value
                                  _type.HRESULT]
    get_GlyphSize: _Callable[[_Pointer[_type.DOUBLE]],  # value
                             _type.HRESULT]
    put_GlyphSize: _Callable[[_type.DOUBLE],  # value
                             _type.HRESULT]
    get_IsExpanded: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    put_IsExpanded: _Callable[[_type.boolean],  # value
                              _type.HRESULT]
    get_TreeViewItemTemplateSettings: _Callable[[_Pointer[ITreeViewItemTemplateSettings]],  # value
                                                _type.HRESULT]


class ITreeViewItem2(_inspectable.IInspectable):
    get_HasUnrealizedChildren: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_HasUnrealizedChildren: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]
    get_ItemsSource: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                               _type.HRESULT]
    put_ItemsSource: _Callable[[_inspectable.IInspectable],  # value
                               _type.HRESULT]


class ITreeViewItemFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ITreeViewItem]],  # value
                              _type.HRESULT]


class ITreeViewItemInvokedEventArgs(_inspectable.IInspectable):
    get_InvokedItem: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                               _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]


class ITreeViewItemStatics(_inspectable.IInspectable):
    get_GlyphOpacityProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_GlyphBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_ExpandedGlyphProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_CollapsedGlyphProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_GlyphSizeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_IsExpandedProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_TreeViewItemTemplateSettingsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                        _type.HRESULT]

    _factory = True


class ITreeViewItemStatics2(_inspectable.IInspectable):
    get_HasUnrealizedChildrenProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_ItemsSourceProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]

    _factory = True


class ITreeViewItemTemplateSettings(_inspectable.IInspectable):
    get_ExpandedGlyphVisibility: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Visibility]],  # value
                                           _type.HRESULT]
    get_CollapsedGlyphVisibility: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Visibility]],  # value
                                            _type.HRESULT]
    get_Indentation: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                               _type.HRESULT]
    get_DragItemsCount: _Callable[[_Pointer[_type.INT32]],  # value
                                  _type.HRESULT]


class ITreeViewItemTemplateSettingsFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ITreeViewItemTemplateSettings]],  # value
                              _type.HRESULT]


class ITreeViewItemTemplateSettingsStatics(_inspectable.IInspectable):
    get_ExpandedGlyphVisibilityProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_CollapsedGlyphVisibilityProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]
    get_IndentationProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_DragItemsCountProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]

    _factory = True


class ITreeViewList(_inspectable.IInspectable):
    pass


class ITreeViewListFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ITreeViewList]],  # value
                              _type.HRESULT]


class ITreeViewNode(_inspectable.IInspectable):
    get_Content: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                           _type.HRESULT]
    put_Content: _Callable[[_inspectable.IInspectable],  # value
                           _type.HRESULT]
    get_Parent: _Callable[[_Pointer[ITreeViewNode]],  # value
                          _type.HRESULT]
    get_IsExpanded: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    put_IsExpanded: _Callable[[_type.boolean],  # value
                              _type.HRESULT]
    get_HasChildren: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_Depth: _Callable[[_Pointer[_type.INT32]],  # value
                         _type.HRESULT]
    get_HasUnrealizedChildren: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_HasUnrealizedChildren: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]
    get_Children: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ITreeViewNode]]],  # value
                            _type.HRESULT]


class ITreeViewNodeFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ITreeViewNode]],  # value
                              _type.HRESULT]


class ITreeViewNodeStatics(_inspectable.IInspectable):
    get_ContentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_DepthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_IsExpandedProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_HasChildrenProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]

    _factory = True


class ITreeViewStatics(_inspectable.IInspectable):
    get_SelectionModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]

    _factory = True


class ITreeViewStatics2(_inspectable.IInspectable):
    get_CanDragItemsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_CanReorderItemsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_ItemTemplateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_ItemTemplateSelectorProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_ItemContainerStyleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_ItemContainerStyleSelectorProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                      _type.HRESULT]
    get_ItemContainerTransitionsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]
    get_ItemsSourceProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]

    _factory = True


class ITwoPaneView(_inspectable.IInspectable):
    get_Pane1: _Callable[[_Pointer[_Windows_UI_Xaml.IUIElement]],  # value
                         _type.HRESULT]
    put_Pane1: _Callable[[_Windows_UI_Xaml.IUIElement],  # value
                         _type.HRESULT]
    get_Pane2: _Callable[[_Pointer[_Windows_UI_Xaml.IUIElement]],  # value
                         _type.HRESULT]
    put_Pane2: _Callable[[_Windows_UI_Xaml.IUIElement],  # value
                         _type.HRESULT]
    get_Pane1Length: _Callable[[_Pointer[_struct.Windows.UI.Xaml.GridLength]],  # value
                               _type.HRESULT]
    put_Pane1Length: _Callable[[_struct.Windows.UI.Xaml.GridLength],  # value
                               _type.HRESULT]
    get_Pane2Length: _Callable[[_Pointer[_struct.Windows.UI.Xaml.GridLength]],  # value
                               _type.HRESULT]
    put_Pane2Length: _Callable[[_struct.Windows.UI.Xaml.GridLength],  # value
                               _type.HRESULT]
    get_PanePriority: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.TwoPaneViewPriority]],  # value
                                _type.HRESULT]
    put_PanePriority: _Callable[[_enum.Windows.UI.Xaml.Controls.TwoPaneViewPriority],  # value
                                _type.HRESULT]
    get_Mode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.TwoPaneViewMode]],  # value
                        _type.HRESULT]
    get_WideModeConfiguration: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.TwoPaneViewWideModeConfiguration]],  # value
                                         _type.HRESULT]
    put_WideModeConfiguration: _Callable[[_enum.Windows.UI.Xaml.Controls.TwoPaneViewWideModeConfiguration],  # value
                                         _type.HRESULT]
    get_TallModeConfiguration: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.TwoPaneViewTallModeConfiguration]],  # value
                                         _type.HRESULT]
    put_TallModeConfiguration: _Callable[[_enum.Windows.UI.Xaml.Controls.TwoPaneViewTallModeConfiguration],  # value
                                         _type.HRESULT]
    get_MinWideModeWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]
    put_MinWideModeWidth: _Callable[[_type.DOUBLE],  # value
                                    _type.HRESULT]
    get_MinTallModeHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                     _type.HRESULT]
    put_MinTallModeHeight: _Callable[[_type.DOUBLE],  # value
                                     _type.HRESULT]
    add_ModeChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ITwoPaneView, _inspectable.IInspectable],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_ModeChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]


class ITwoPaneViewFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ITwoPaneView]],  # value
                              _type.HRESULT]


class ITwoPaneViewStatics(_inspectable.IInspectable):
    get_Pane1Property: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_Pane2Property: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_Pane1LengthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_Pane2LengthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_PanePriorityProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_ModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]
    get_WideModeConfigurationProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_TallModeConfigurationProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_MinWideModeWidthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_MinTallModeHeightProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]

    _factory = True


class IUIElementCollection(_inspectable.IInspectable):
    Move: _Callable[[_type.UINT32,  # oldIndex
                     _type.UINT32],  # newIndex
                    _type.HRESULT]


class IUserControl(_inspectable.IInspectable):
    get_Content: _Callable[[_Pointer[_Windows_UI_Xaml.IUIElement]],  # value
                           _type.HRESULT]
    put_Content: _Callable[[_Windows_UI_Xaml.IUIElement],  # value
                           _type.HRESULT]


class IUserControlFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IUserControl]],  # value
                              _type.HRESULT]


class IUserControlStatics(_inspectable.IInspectable):
    get_ContentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]

    _factory = True


class IVariableSizedWrapGrid(_inspectable.IInspectable):
    get_ItemHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                              _type.HRESULT]
    put_ItemHeight: _Callable[[_type.DOUBLE],  # value
                              _type.HRESULT]
    get_ItemWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                             _type.HRESULT]
    put_ItemWidth: _Callable[[_type.DOUBLE],  # value
                             _type.HRESULT]
    get_Orientation: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Orientation]],  # value
                               _type.HRESULT]
    put_Orientation: _Callable[[_enum.Windows.UI.Xaml.Controls.Orientation],  # value
                               _type.HRESULT]
    get_HorizontalChildrenAlignment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.HorizontalAlignment]],  # value
                                               _type.HRESULT]
    put_HorizontalChildrenAlignment: _Callable[[_enum.Windows.UI.Xaml.HorizontalAlignment],  # value
                                               _type.HRESULT]
    get_VerticalChildrenAlignment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.VerticalAlignment]],  # value
                                             _type.HRESULT]
    put_VerticalChildrenAlignment: _Callable[[_enum.Windows.UI.Xaml.VerticalAlignment],  # value
                                             _type.HRESULT]
    get_MaximumRowsOrColumns: _Callable[[_Pointer[_type.INT32]],  # value
                                        _type.HRESULT]
    put_MaximumRowsOrColumns: _Callable[[_type.INT32],  # value
                                        _type.HRESULT]


class IVariableSizedWrapGridStatics(_inspectable.IInspectable):
    get_ItemHeightProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_ItemWidthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_OrientationProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_HorizontalChildrenAlignmentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]
    get_VerticalChildrenAlignmentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                     _type.HRESULT]
    get_MaximumRowsOrColumnsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_RowSpanProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    GetRowSpan: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                           _Pointer[_type.INT32]],  # result
                          _type.HRESULT]
    SetRowSpan: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                           _type.INT32],  # value
                          _type.HRESULT]
    get_ColumnSpanProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    GetColumnSpan: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                              _Pointer[_type.INT32]],  # result
                             _type.HRESULT]
    SetColumnSpan: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                              _type.INT32],  # value
                             _type.HRESULT]

    _factory = True


class IViewbox(_inspectable.IInspectable):
    get_Child: _Callable[[_Pointer[_Windows_UI_Xaml.IUIElement]],  # value
                         _type.HRESULT]
    put_Child: _Callable[[_Windows_UI_Xaml.IUIElement],  # value
                         _type.HRESULT]
    get_Stretch: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Media.Stretch]],  # value
                           _type.HRESULT]
    put_Stretch: _Callable[[_enum.Windows.UI.Xaml.Media.Stretch],  # value
                           _type.HRESULT]
    get_StretchDirection: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.StretchDirection]],  # value
                                    _type.HRESULT]
    put_StretchDirection: _Callable[[_enum.Windows.UI.Xaml.Controls.StretchDirection],  # value
                                    _type.HRESULT]


class IViewboxStatics(_inspectable.IInspectable):
    get_StretchProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_StretchDirectionProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]

    _factory = True


class IVirtualizingPanel(_inspectable.IInspectable):
    get_ItemContainerGenerator: _Callable[[_Pointer[IItemContainerGenerator]],  # value
                                          _type.HRESULT]


class IVirtualizingPanelFactory(_inspectable.IInspectable):
    pass


class IVirtualizingPanelOverrides(_inspectable.IInspectable):
    OnItemsChanged: _Callable[[_inspectable.IInspectable,  # sender
                               _Windows_UI_Xaml_Controls_Primitives.IItemsChangedEventArgs],  # args
                              _type.HRESULT]
    OnClearChildren: _Callable[[],
                               _type.HRESULT]
    BringIndexIntoView: _Callable[[_type.INT32],  # index
                                  _type.HRESULT]


class IVirtualizingPanelProtected(_inspectable.IInspectable):
    AddInternalChild: _Callable[[_Windows_UI_Xaml.IUIElement],  # child
                                _type.HRESULT]
    InsertInternalChild: _Callable[[_type.INT32,  # index
                                    _Windows_UI_Xaml.IUIElement],  # child
                                   _type.HRESULT]
    RemoveInternalChildRange: _Callable[[_type.INT32,  # index
                                         _type.INT32],  # range
                                        _type.HRESULT]


class IVirtualizingStackPanel(_inspectable.IInspectable):
    get_AreScrollSnapPointsRegular: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]
    put_AreScrollSnapPointsRegular: _Callable[[_type.boolean],  # value
                                              _type.HRESULT]
    get_Orientation: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Orientation]],  # value
                               _type.HRESULT]
    put_Orientation: _Callable[[_enum.Windows.UI.Xaml.Controls.Orientation],  # value
                               _type.HRESULT]
    add_CleanUpVirtualizedItemEvent: _Callable[[ICleanUpVirtualizedItemEventHandler,  # handler
                                                _Pointer[_struct.EventRegistrationToken]],  # token
                                               _type.HRESULT]
    remove_CleanUpVirtualizedItemEvent: _Callable[[_struct.EventRegistrationToken],  # token
                                                  _type.HRESULT]


class IVirtualizingStackPanelOverrides(_inspectable.IInspectable):
    OnCleanUpVirtualizedItem: _Callable[[ICleanUpVirtualizedItemEventArgs],  # e
                                        _type.HRESULT]


class IVirtualizingStackPanelStatics(_inspectable.IInspectable):
    get_AreScrollSnapPointsRegularProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                      _type.HRESULT]
    get_OrientationProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_VirtualizationModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    GetVirtualizationMode: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                      _Pointer[_enum.Windows.UI.Xaml.Controls.VirtualizationMode]],  # result
                                     _type.HRESULT]
    SetVirtualizationMode: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                      _enum.Windows.UI.Xaml.Controls.VirtualizationMode],  # value
                                     _type.HRESULT]
    get_IsVirtualizingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    GetIsVirtualizing: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # o
                                  _Pointer[_type.boolean]],  # result
                                 _type.HRESULT]

    _factory = True


class IWebView(_inspectable.IInspectable):
    get_Source: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                          _type.HRESULT]
    put_Source: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                          _type.HRESULT]
    AllowedScriptNotifyUris: _Callable[[_Windows_Foundation_Collections.IVector[_Windows_Foundation.IUriRuntimeClass]],  # value
                                       _type.HRESULT]
    DataTransferPackage: _Callable[[_Pointer[_Windows_ApplicationModel_DataTransfer.IDataPackage]],  # value
                                   _type.HRESULT]
    LoadCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    add_ScriptNotify: _Callable[[INotifyEventHandler,  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_ScriptNotify: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    NavigationFailed: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    InvokeScript: _Callable[[_type.HSTRING,  # scriptName
                             _type.UINT32,  # __argumentsSize
                             _Pointer[_type.HSTRING],  # arguments
                             _Pointer[_type.HSTRING]],  # result
                            _type.HRESULT]
    Navigate: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # source
                        _type.HRESULT]
    NavigateToString: _Callable[[_type.HSTRING],  # text
                                _type.HRESULT]


class IWebView2(_inspectable.IInspectable):
    get_CanGoBack: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_CanGoForward: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_DocumentTitle: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    add_NavigationStarting: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebView, IWebViewNavigationStartingEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_NavigationStarting: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_ContentLoading: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebView, IWebViewContentLoadingEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_ContentLoading: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_DOMContentLoaded: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebView, IWebViewDOMContentLoadedEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_DOMContentLoaded: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    GoForward: _Callable[[],
                         _type.HRESULT]
    GoBack: _Callable[[],
                      _type.HRESULT]
    Refresh: _Callable[[],
                       _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    CapturePreviewToStreamAsync: _Callable[[_Windows_Storage_Streams.IRandomAccessStream,  # stream
                                            _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                           _type.HRESULT]
    InvokeScriptAsync: _Callable[[_type.HSTRING,  # scriptName
                                  _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # arguments
                                  _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                 _type.HRESULT]
    CaptureSelectedContentToDataPackageAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_ApplicationModel_DataTransfer.IDataPackage]]],  # operation
                                                        _type.HRESULT]
    NavigateToLocalStreamUri: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # source
                                         _Windows_Web.IUriToStreamResolver],  # streamResolver
                                        _type.HRESULT]
    BuildLocalStreamUri: _Callable[[_type.HSTRING,  # contentIdentifier
                                    _type.HSTRING,  # relativePath
                                    _Pointer[_Windows_Foundation.IUriRuntimeClass]],  # result
                                   _type.HRESULT]
    get_DefaultBackgroundColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                          _type.HRESULT]
    put_DefaultBackgroundColor: _Callable[[_struct.Windows.UI.Color],  # value
                                          _type.HRESULT]
    add_NavigationCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebView, IWebViewNavigationCompletedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_NavigationCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_FrameNavigationStarting: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebView, IWebViewNavigationStartingEventArgs],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_FrameNavigationStarting: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]
    add_FrameContentLoading: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebView, IWebViewContentLoadingEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_FrameContentLoading: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_FrameDOMContentLoaded: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebView, IWebViewDOMContentLoadedEventArgs],  # handler
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_FrameDOMContentLoaded: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]
    add_FrameNavigationCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebView, IWebViewNavigationCompletedEventArgs],  # handler
                                             _Pointer[_struct.EventRegistrationToken]],  # token
                                            _type.HRESULT]
    remove_FrameNavigationCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                               _type.HRESULT]
    add_LongRunningScriptDetected: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebView, IWebViewLongRunningScriptDetectedEventArgs],  # handler
                                              _Pointer[_struct.EventRegistrationToken]],  # token
                                             _type.HRESULT]
    remove_LongRunningScriptDetected: _Callable[[_struct.EventRegistrationToken],  # token
                                                _type.HRESULT]
    add_UnsafeContentWarningDisplaying: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebView, _inspectable.IInspectable],  # handler
                                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                                  _type.HRESULT]
    remove_UnsafeContentWarningDisplaying: _Callable[[_struct.EventRegistrationToken],  # token
                                                     _type.HRESULT]
    add_UnviewableContentIdentified: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebView, IWebViewUnviewableContentIdentifiedEventArgs],  # handler
                                                _Pointer[_struct.EventRegistrationToken]],  # token
                                               _type.HRESULT]
    remove_UnviewableContentIdentified: _Callable[[_struct.EventRegistrationToken],  # token
                                                  _type.HRESULT]
    NavigateWithHttpRequestMessage: _Callable[[_Windows_Web_Http.IHttpRequestMessage],  # requestMessage
                                              _type.HRESULT]
    Focus: _Callable[[_enum.Windows.UI.Xaml.FocusState,  # value
                      _Pointer[_type.boolean]],  # result
                     _type.HRESULT]


class IWebView3(_inspectable.IInspectable):
    get_ContainsFullScreenElement: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    add_ContainsFullScreenElementChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebView, _inspectable.IInspectable],  # handler
                                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                                    _type.HRESULT]
    remove_ContainsFullScreenElementChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                       _type.HRESULT]


class IWebView4(_inspectable.IInspectable):
    get_ExecutionMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.WebViewExecutionMode]],  # value
                                 _type.HRESULT]
    get_DeferredPermissionRequests: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IWebViewDeferredPermissionRequest]]],  # value
                                              _type.HRESULT]
    get_Settings: _Callable[[_Pointer[IWebViewSettings]],  # value
                            _type.HRESULT]
    add_UnsupportedUriSchemeIdentified: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebView, IWebViewUnsupportedUriSchemeIdentifiedEventArgs],  # handler
                                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                                  _type.HRESULT]
    remove_UnsupportedUriSchemeIdentified: _Callable[[_struct.EventRegistrationToken],  # token
                                                     _type.HRESULT]
    add_NewWindowRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebView, IWebViewNewWindowRequestedEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_NewWindowRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_PermissionRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebView, IWebViewPermissionRequestedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_PermissionRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    AddWebAllowedObject: _Callable[[_type.HSTRING,  # name
                                    _inspectable.IInspectable],  # pObject
                                   _type.HRESULT]
    DeferredPermissionRequestById: _Callable[[_type.UINT32,  # id
                                              _Pointer[IWebViewDeferredPermissionRequest]],  # result
                                             _type.HRESULT]


class IWebView5(_inspectable.IInspectable):
    get_XYFocusLeft: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyObject]],  # value
                               _type.HRESULT]
    put_XYFocusLeft: _Callable[[_Windows_UI_Xaml.IDependencyObject],  # value
                               _type.HRESULT]
    get_XYFocusRight: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyObject]],  # value
                                _type.HRESULT]
    put_XYFocusRight: _Callable[[_Windows_UI_Xaml.IDependencyObject],  # value
                                _type.HRESULT]
    get_XYFocusUp: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyObject]],  # value
                             _type.HRESULT]
    put_XYFocusUp: _Callable[[_Windows_UI_Xaml.IDependencyObject],  # value
                             _type.HRESULT]
    get_XYFocusDown: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyObject]],  # value
                               _type.HRESULT]
    put_XYFocusDown: _Callable[[_Windows_UI_Xaml.IDependencyObject],  # value
                               _type.HRESULT]


class IWebView6(_inspectable.IInspectable):
    add_SeparateProcessLost: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebView, IWebViewSeparateProcessLostEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_SeparateProcessLost: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]


class IWebView7(_inspectable.IInspectable):
    add_WebResourceRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebView, IWebViewWebResourceRequestedEventArgs],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_WebResourceRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]


class IWebViewBrush(_inspectable.IInspectable):
    get_SourceName: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_SourceName: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]
    Redraw: _Callable[[],
                      _type.HRESULT]
    SetSource: _Callable[[IWebView],  # source
                         _type.HRESULT]


class IWebViewBrushStatics(_inspectable.IInspectable):
    get_SourceNameProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]

    _factory = True


class IWebViewContentLoadingEventArgs(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]


class IWebViewDOMContentLoadedEventArgs(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]


class IWebViewDeferredPermissionRequest(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]
    get_PermissionType: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.WebViewPermissionType]],  # value
                                  _type.HRESULT]
    get_Id: _Callable[[_Pointer[_type.UINT32]],  # value
                      _type.HRESULT]
    Allow: _Callable[[],
                     _type.HRESULT]
    Deny: _Callable[[],
                    _type.HRESULT]


class IWebViewFactory4(_inspectable.IInspectable):
    CreateInstanceWithExecutionMode: _Callable[[_enum.Windows.UI.Xaml.Controls.WebViewExecutionMode,  # executionMode
                                                _Pointer[IWebView]],  # value
                                               _type.HRESULT]

    _factory = True


class IWebViewLongRunningScriptDetectedEventArgs(_inspectable.IInspectable):
    get_ExecutionTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                 _type.HRESULT]
    get_StopPageScriptExecution: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    put_StopPageScriptExecution: _Callable[[_type.boolean],  # value
                                           _type.HRESULT]


class IWebViewNavigationCompletedEventArgs(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]
    get_IsSuccess: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_WebErrorStatus: _Callable[[_Pointer[_enum.Windows.Web.WebErrorStatus]],  # value
                                  _type.HRESULT]


class IWebViewNavigationFailedEventArgs(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]
    get_WebErrorStatus: _Callable[[_Pointer[_enum.Windows.Web.WebErrorStatus]],  # value
                                  _type.HRESULT]


class IWebViewNavigationStartingEventArgs(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]
    get_Cancel: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_Cancel: _Callable[[_type.boolean],  # value
                          _type.HRESULT]


class IWebViewNewWindowRequestedEventArgs(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]
    get_Referrer: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                            _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class IWebViewPermissionRequest(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]
    get_PermissionType: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.WebViewPermissionType]],  # value
                                  _type.HRESULT]
    get_Id: _Callable[[_Pointer[_type.UINT32]],  # value
                      _type.HRESULT]
    get_State: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.WebViewPermissionState]],  # value
                         _type.HRESULT]
    Defer: _Callable[[],
                     _type.HRESULT]
    Allow: _Callable[[],
                     _type.HRESULT]
    Deny: _Callable[[],
                    _type.HRESULT]


class IWebViewPermissionRequestedEventArgs(_inspectable.IInspectable):
    get_PermissionRequest: _Callable[[_Pointer[IWebViewPermissionRequest]],  # value
                                     _type.HRESULT]


class IWebViewSeparateProcessLostEventArgs(_inspectable.IInspectable):
    pass


class IWebViewSettings(_inspectable.IInspectable):
    get_IsJavaScriptEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_IsJavaScriptEnabled: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_IsIndexedDBEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_IsIndexedDBEnabled: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]


class IWebViewStatics(_inspectable.IInspectable):
    AnyScriptNotifyUri: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_Foundation.IUriRuntimeClass]]],  # value
                                  _type.HRESULT]
    get_SourceProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    AllowedScriptNotifyUrisProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    DataTransferPackageProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]

    _factory = True


class IWebViewStatics2(_inspectable.IInspectable):
    get_CanGoBackProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_CanGoForwardProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_DocumentTitleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_DefaultBackgroundColorProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]

    _factory = True


class IWebViewStatics3(_inspectable.IInspectable):
    get_ContainsFullScreenElementProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                     _type.HRESULT]

    _factory = True


class IWebViewStatics4(_inspectable.IInspectable):
    get_DefaultExecutionMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.WebViewExecutionMode]],  # value
                                        _type.HRESULT]
    ClearTemporaryWebDataAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                          _type.HRESULT]

    _factory = True


class IWebViewStatics5(_inspectable.IInspectable):
    get_XYFocusLeftProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_XYFocusRightProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_XYFocusUpProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_XYFocusDownProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]

    _factory = True


class IWebViewUnsupportedUriSchemeIdentifiedEventArgs(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class IWebViewUnviewableContentIdentifiedEventArgs(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]
    get_Referrer: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                            _type.HRESULT]


class IWebViewUnviewableContentIdentifiedEventArgs2(_inspectable.IInspectable):
    get_MediaType: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]


class IWebViewWebResourceRequestedEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[_Windows_Web_Http.IHttpRequestMessage]],  # value
                           _type.HRESULT]
    get_Response: _Callable[[_Pointer[_Windows_Web_Http.IHttpResponseMessage]],  # value
                            _type.HRESULT]
    put_Response: _Callable[[_Windows_Web_Http.IHttpResponseMessage],  # value
                            _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IWrapGrid(_inspectable.IInspectable):
    get_ItemWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                             _type.HRESULT]
    put_ItemWidth: _Callable[[_type.DOUBLE],  # value
                             _type.HRESULT]
    get_ItemHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                              _type.HRESULT]
    put_ItemHeight: _Callable[[_type.DOUBLE],  # value
                              _type.HRESULT]
    get_Orientation: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Orientation]],  # value
                               _type.HRESULT]
    put_Orientation: _Callable[[_enum.Windows.UI.Xaml.Controls.Orientation],  # value
                               _type.HRESULT]
    get_HorizontalChildrenAlignment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.HorizontalAlignment]],  # value
                                               _type.HRESULT]
    put_HorizontalChildrenAlignment: _Callable[[_enum.Windows.UI.Xaml.HorizontalAlignment],  # value
                                               _type.HRESULT]
    get_VerticalChildrenAlignment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.VerticalAlignment]],  # value
                                             _type.HRESULT]
    put_VerticalChildrenAlignment: _Callable[[_enum.Windows.UI.Xaml.VerticalAlignment],  # value
                                             _type.HRESULT]
    get_MaximumRowsOrColumns: _Callable[[_Pointer[_type.INT32]],  # value
                                        _type.HRESULT]
    put_MaximumRowsOrColumns: _Callable[[_type.INT32],  # value
                                        _type.HRESULT]


class IWrapGridStatics(_inspectable.IInspectable):
    get_ItemWidthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_ItemHeightProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_OrientationProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_HorizontalChildrenAlignmentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]
    get_VerticalChildrenAlignmentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                     _type.HRESULT]
    get_MaximumRowsOrColumnsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]

    _factory = True
