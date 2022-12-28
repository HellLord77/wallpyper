from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Controls as _Windows_UI_Xaml_Controls
from ... import Input as _Windows_UI_Xaml_Input
from ... import Media as _Windows_UI_Xaml_Media
from ...Media import Animation as _Windows_UI_Xaml_Media_Animation
from .... import Xaml as _Windows_UI_Xaml
from ..... import Foundation as _Windows_Foundation
from .....Foundation import Collections as _Windows_Foundation_Collections
from ...... import inspectable as _inspectable
from .......um import Unknwnbase as _Unknwnbase
from ........ import enum as _enum
from ........ import struct as _struct
from ........ import type as _type
from ........_utils import _Pointer


class _IDragCompletedEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       IDragCompletedEventArgs],  # e
                      _type.HRESULT]


class IDragCompletedEventHandler(_IDragCompletedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IDragCompletedEventHandler_impl(_IDragCompletedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IDragDeltaEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       IDragDeltaEventArgs],  # e
                      _type.HRESULT]


class IDragDeltaEventHandler(_IDragDeltaEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IDragDeltaEventHandler_impl(_IDragDeltaEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IDragStartedEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       IDragStartedEventArgs],  # e
                      _type.HRESULT]


class IDragStartedEventHandler(_IDragStartedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IDragStartedEventHandler_impl(_IDragStartedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IItemsChangedEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       IItemsChangedEventArgs],  # e
                      _type.HRESULT]


class IItemsChangedEventHandler(_IItemsChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IItemsChangedEventHandler_impl(_IItemsChangedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IRangeBaseValueChangedEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       IRangeBaseValueChangedEventArgs],  # e
                      _type.HRESULT]


class IRangeBaseValueChangedEventHandler(_IRangeBaseValueChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IRangeBaseValueChangedEventHandler_impl(_IRangeBaseValueChangedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IScrollEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       IScrollEventArgs],  # e
                      _type.HRESULT]


class IScrollEventHandler(_IScrollEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IScrollEventHandler_impl(_IScrollEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class IAppBarButtonTemplateSettings(_inspectable.IInspectable):
    get_KeyboardAcceleratorTextMinWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                   _type.HRESULT]


class IAppBarTemplateSettings(_inspectable.IInspectable):
    get_ClipRect: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                            _type.HRESULT]
    get_CompactVerticalDelta: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                        _type.HRESULT]
    get_CompactRootMargin: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                                     _type.HRESULT]
    get_MinimalVerticalDelta: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                        _type.HRESULT]
    get_MinimalRootMargin: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                                     _type.HRESULT]
    get_HiddenVerticalDelta: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                       _type.HRESULT]
    get_HiddenRootMargin: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                                    _type.HRESULT]


class IAppBarTemplateSettings2(_inspectable.IInspectable):
    get_NegativeCompactVerticalDelta: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                _type.HRESULT]
    get_NegativeMinimalVerticalDelta: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                _type.HRESULT]
    get_NegativeHiddenVerticalDelta: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                               _type.HRESULT]


class IAppBarToggleButtonTemplateSettings(_inspectable.IInspectable):
    get_KeyboardAcceleratorTextMinWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                   _type.HRESULT]


class IButtonBase(_inspectable.IInspectable):
    get_ClickMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.ClickMode]],  # value
                             _type.HRESULT]
    put_ClickMode: _Callable[[_enum.Windows.UI.Xaml.Controls.ClickMode],  # value
                             _type.HRESULT]
    get_IsPointerOver: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_IsPressed: _Callable[[_Pointer[_type.boolean]],  # value
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


class IButtonBaseFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IButtonBase]],  # value
                              _type.HRESULT]


class IButtonBaseStatics(_inspectable.IInspectable):
    get_ClickModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_IsPointerOverProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_IsPressedProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_CommandProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_CommandParameterProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]

    _factory = True


class ICalendarPanel(_inspectable.IInspectable):
    pass


class ICalendarViewTemplateSettings(_inspectable.IInspectable):
    get_MinViewWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    get_HeaderText: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_WeekDay1: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_WeekDay2: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_WeekDay3: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_WeekDay4: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_WeekDay5: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_WeekDay6: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_WeekDay7: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_HasMoreContentAfter: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    get_HasMoreContentBefore: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_HasMoreViews: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_ClipRect: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                            _type.HRESULT]
    get_CenterX: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    get_CenterY: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]


class ICarouselPanel(_inspectable.IInspectable):
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


class ICarouselPanelFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ICarouselPanel]],  # value
                              _type.HRESULT]


class IColorPickerSlider(_inspectable.IInspectable):
    get_ColorChannel: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.ColorPickerHsvChannel]],  # value
                                _type.HRESULT]
    put_ColorChannel: _Callable[[_enum.Windows.UI.Xaml.Controls.ColorPickerHsvChannel],  # value
                                _type.HRESULT]


class IColorPickerSliderFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IColorPickerSlider]],  # value
                              _type.HRESULT]


class IColorPickerSliderStatics(_inspectable.IInspectable):
    get_ColorChannelProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]

    _factory = True


class IColorSpectrum(_inspectable.IInspectable):
    get_Color: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                         _type.HRESULT]
    put_Color: _Callable[[_struct.Windows.UI.Color],  # value
                         _type.HRESULT]
    get_HsvColor: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector4]],  # value
                            _type.HRESULT]
    put_HsvColor: _Callable[[_struct.Windows.Foundation.Numerics.Vector4],  # value
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
    get_Shape: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.ColorSpectrumShape]],  # value
                         _type.HRESULT]
    put_Shape: _Callable[[_enum.Windows.UI.Xaml.Controls.ColorSpectrumShape],  # value
                         _type.HRESULT]
    get_Components: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.ColorSpectrumComponents]],  # value
                              _type.HRESULT]
    put_Components: _Callable[[_enum.Windows.UI.Xaml.Controls.ColorSpectrumComponents],  # value
                              _type.HRESULT]
    add_ColorChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IColorSpectrum, _Windows_UI_Xaml_Controls.IColorChangedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_ColorChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]


class IColorSpectrumFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IColorSpectrum]],  # value
                              _type.HRESULT]


class IColorSpectrumStatics(_inspectable.IInspectable):
    get_ColorProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_HsvColorProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
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
    get_ShapeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_ComponentsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]

    _factory = True


class IComboBoxTemplateSettings(_inspectable.IInspectable):
    get_DropDownOpenedHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                        _type.HRESULT]
    get_DropDownClosedHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                        _type.HRESULT]
    get_DropDownOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    get_SelectedItemDirection: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Primitives.AnimationDirection]],  # value
                                         _type.HRESULT]


class IComboBoxTemplateSettings2(_inspectable.IInspectable):
    get_DropDownContentMinWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                           _type.HRESULT]


class ICommandBarFlyoutCommandBar(_inspectable.IInspectable):
    get_FlyoutTemplateSettings: _Callable[[_Pointer[ICommandBarFlyoutCommandBarTemplateSettings]],  # value
                                          _type.HRESULT]


class ICommandBarFlyoutCommandBarFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ICommandBarFlyoutCommandBar]],  # value
                              _type.HRESULT]


class ICommandBarFlyoutCommandBarTemplateSettings(_inspectable.IInspectable):
    get_OpenAnimationStartPosition: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                              _type.HRESULT]
    get_OpenAnimationEndPosition: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                            _type.HRESULT]
    get_CloseAnimationEndPosition: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                             _type.HRESULT]
    get_CurrentWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    get_ExpandedWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                 _type.HRESULT]
    get_WidthExpansionDelta: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                       _type.HRESULT]
    get_WidthExpansionAnimationStartPosition: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                        _type.HRESULT]
    get_WidthExpansionAnimationEndPosition: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                      _type.HRESULT]
    get_WidthExpansionMoreButtonAnimationStartPosition: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                                  _type.HRESULT]
    get_WidthExpansionMoreButtonAnimationEndPosition: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                                _type.HRESULT]
    get_ExpandUpOverflowVerticalPosition: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                    _type.HRESULT]
    get_ExpandDownOverflowVerticalPosition: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                      _type.HRESULT]
    get_ExpandUpAnimationStartPosition: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                  _type.HRESULT]
    get_ExpandUpAnimationEndPosition: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                _type.HRESULT]
    get_ExpandUpAnimationHoldPosition: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                 _type.HRESULT]
    get_ExpandDownAnimationStartPosition: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                    _type.HRESULT]
    get_ExpandDownAnimationEndPosition: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                  _type.HRESULT]
    get_ExpandDownAnimationHoldPosition: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                   _type.HRESULT]
    get_ContentClipRect: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                                   _type.HRESULT]
    get_OverflowContentClipRect: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                                           _type.HRESULT]


class ICommandBarTemplateSettings(_inspectable.IInspectable):
    get_ContentHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                 _type.HRESULT]
    get_OverflowContentClipRect: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                                           _type.HRESULT]
    get_OverflowContentMinWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                           _type.HRESULT]
    get_OverflowContentMaxHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                            _type.HRESULT]
    get_OverflowContentHorizontalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                   _type.HRESULT]
    get_OverflowContentHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                         _type.HRESULT]
    get_NegativeOverflowContentHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                 _type.HRESULT]


class ICommandBarTemplateSettings2(_inspectable.IInspectable):
    get_OverflowContentMaxWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                           _type.HRESULT]


class ICommandBarTemplateSettings3(_inspectable.IInspectable):
    get_EffectiveOverflowButtonVisibility: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Visibility]],  # value
                                                     _type.HRESULT]


class ICommandBarTemplateSettings4(_inspectable.IInspectable):
    get_OverflowContentCompactYTranslation: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                      _type.HRESULT]
    get_OverflowContentMinimalYTranslation: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                      _type.HRESULT]
    get_OverflowContentHiddenYTranslation: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                     _type.HRESULT]


class IDragCompletedEventArgs(_inspectable.IInspectable):
    get_HorizontalChange: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]
    get_VerticalChange: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    get_Canceled: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]


class IDragCompletedEventArgsFactory(_inspectable.IInspectable):
    CreateInstanceWithHorizontalChangeVerticalChangeAndCanceled: _Callable[[_type.DOUBLE,  # horizontalChange
                                                                            _type.DOUBLE,  # verticalChange
                                                                            _type.boolean,  # canceled
                                                                            _inspectable.IInspectable,  # baseInterface
                                                                            _Pointer[_inspectable.IInspectable],  # innerInterface
                                                                            _Pointer[IDragCompletedEventArgs]],  # value
                                                                           _type.HRESULT]


class IDragDeltaEventArgs(_inspectable.IInspectable):
    get_HorizontalChange: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]
    get_VerticalChange: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]


class IDragDeltaEventArgsFactory(_inspectable.IInspectable):
    CreateInstanceWithHorizontalChangeAndVerticalChange: _Callable[[_type.DOUBLE,  # horizontalChange
                                                                    _type.DOUBLE,  # verticalChange
                                                                    _inspectable.IInspectable,  # baseInterface
                                                                    _Pointer[_inspectable.IInspectable],  # innerInterface
                                                                    _Pointer[IDragDeltaEventArgs]],  # value
                                                                   _type.HRESULT]


class IDragStartedEventArgs(_inspectable.IInspectable):
    get_HorizontalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]
    get_VerticalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]


class IDragStartedEventArgsFactory(_inspectable.IInspectable):
    CreateInstanceWithHorizontalOffsetAndVerticalOffset: _Callable[[_type.DOUBLE,  # horizontalOffset
                                                                    _type.DOUBLE,  # verticalOffset
                                                                    _inspectable.IInspectable,  # baseInterface
                                                                    _Pointer[_inspectable.IInspectable],  # innerInterface
                                                                    _Pointer[IDragStartedEventArgs]],  # value
                                                                   _type.HRESULT]


class IFlyoutBase(_inspectable.IInspectable):
    get_Placement: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode]],  # value
                             _type.HRESULT]
    put_Placement: _Callable[[_enum.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode],  # value
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
    add_Opening: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Opening: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    ShowAt: _Callable[[_Windows_UI_Xaml.IFrameworkElement],  # placementTarget
                      _type.HRESULT]
    Hide: _Callable[[],
                    _type.HRESULT]


class IFlyoutBase2(_inspectable.IInspectable):
    get_Target: _Callable[[_Pointer[_Windows_UI_Xaml.IFrameworkElement]],  # value
                          _type.HRESULT]
    get_AllowFocusOnInteraction: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    put_AllowFocusOnInteraction: _Callable[[_type.boolean],  # value
                                           _type.HRESULT]
    get_LightDismissOverlayMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.LightDismissOverlayMode]],  # value
                                           _type.HRESULT]
    put_LightDismissOverlayMode: _Callable[[_enum.Windows.UI.Xaml.Controls.LightDismissOverlayMode],  # value
                                           _type.HRESULT]
    get_AllowFocusWhenDisabled: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_AllowFocusWhenDisabled: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    get_ElementSoundMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.ElementSoundMode]],  # value
                                    _type.HRESULT]
    put_ElementSoundMode: _Callable[[_enum.Windows.UI.Xaml.ElementSoundMode],  # value
                                    _type.HRESULT]
    add_Closing: _Callable[[_Windows_Foundation.ITypedEventHandler[IFlyoutBase, IFlyoutBaseClosingEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Closing: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]


class IFlyoutBase3(_inspectable.IInspectable):
    get_OverlayInputPassThroughElement: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyObject]],  # value
                                                  _type.HRESULT]
    put_OverlayInputPassThroughElement: _Callable[[_Windows_UI_Xaml.IDependencyObject],  # value
                                                  _type.HRESULT]


class IFlyoutBase4(_inspectable.IInspectable):
    TryInvokeKeyboardAccelerator: _Callable[[_Windows_UI_Xaml_Input.IProcessKeyboardAcceleratorEventArgs],  # args
                                            _type.HRESULT]


class IFlyoutBase5(_inspectable.IInspectable):
    get_ShowMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Primitives.FlyoutShowMode]],  # value
                            _type.HRESULT]
    put_ShowMode: _Callable[[_enum.Windows.UI.Xaml.Controls.Primitives.FlyoutShowMode],  # value
                            _type.HRESULT]
    get_InputDevicePrefersPrimaryCommands: _Callable[[_Pointer[_type.boolean]],  # value
                                                     _type.HRESULT]
    get_AreOpenCloseAnimationsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]
    put_AreOpenCloseAnimationsEnabled: _Callable[[_type.boolean],  # value
                                                 _type.HRESULT]
    get_IsOpen: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    ShowAt: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # placementTarget
                       IFlyoutShowOptions],  # showOptions
                      _type.HRESULT]


class IFlyoutBase6(_inspectable.IInspectable):
    get_ShouldConstrainToRootBounds: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]
    put_ShouldConstrainToRootBounds: _Callable[[_type.boolean],  # value
                                               _type.HRESULT]
    get_IsConstrainedToRootBounds: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    get_XamlRoot: _Callable[[_Pointer[_Windows_UI_Xaml.IXamlRoot]],  # value
                            _type.HRESULT]
    put_XamlRoot: _Callable[[_Windows_UI_Xaml.IXamlRoot],  # value
                            _type.HRESULT]


class IFlyoutBaseClosingEventArgs(_inspectable.IInspectable):
    get_Cancel: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_Cancel: _Callable[[_type.boolean],  # value
                          _type.HRESULT]


class IFlyoutBaseFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IFlyoutBase]],  # value
                              _type.HRESULT]


class IFlyoutBaseOverrides(_inspectable.IInspectable):
    CreatePresenter: _Callable[[_Pointer[_Windows_UI_Xaml_Controls.IControl]],  # result
                               _type.HRESULT]


class IFlyoutBaseOverrides4(_inspectable.IInspectable):
    OnProcessKeyboardAccelerators: _Callable[[_Windows_UI_Xaml_Input.IProcessKeyboardAcceleratorEventArgs],  # args
                                             _type.HRESULT]


class IFlyoutBaseStatics(_inspectable.IInspectable):
    get_PlacementProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_AttachedFlyoutProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    GetAttachedFlyout: _Callable[[_Windows_UI_Xaml.IFrameworkElement,  # element
                                  _Pointer[IFlyoutBase]],  # result
                                 _type.HRESULT]
    SetAttachedFlyout: _Callable[[_Windows_UI_Xaml.IFrameworkElement,  # element
                                  IFlyoutBase],  # value
                                 _type.HRESULT]
    ShowAttachedFlyout: _Callable[[_Windows_UI_Xaml.IFrameworkElement],  # flyoutOwner
                                  _type.HRESULT]

    _factory = True


class IFlyoutBaseStatics2(_inspectable.IInspectable):
    get_AllowFocusOnInteractionProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_LightDismissOverlayModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_AllowFocusWhenDisabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]
    get_ElementSoundModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]

    _factory = True


class IFlyoutBaseStatics3(_inspectable.IInspectable):
    get_OverlayInputPassThroughElementProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                          _type.HRESULT]

    _factory = True


class IFlyoutBaseStatics5(_inspectable.IInspectable):
    get_TargetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_ShowModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_InputDevicePrefersPrimaryCommandsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                             _type.HRESULT]
    get_AreOpenCloseAnimationsEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                         _type.HRESULT]
    get_IsOpenProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]

    _factory = True


class IFlyoutBaseStatics6(_inspectable.IInspectable):
    get_ShouldConstrainToRootBoundsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]

    _factory = True


class IFlyoutShowOptions(_inspectable.IInspectable):
    get_Position: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.Point]]],  # value
                            _type.HRESULT]
    put_Position: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    get_ExclusionRect: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.Rect]]],  # value
                                 _type.HRESULT]
    put_ExclusionRect: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.Rect]],  # value
                                 _type.HRESULT]
    get_ShowMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Primitives.FlyoutShowMode]],  # value
                            _type.HRESULT]
    put_ShowMode: _Callable[[_enum.Windows.UI.Xaml.Controls.Primitives.FlyoutShowMode],  # value
                            _type.HRESULT]
    get_Placement: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode]],  # value
                             _type.HRESULT]
    put_Placement: _Callable[[_enum.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode],  # value
                             _type.HRESULT]


class IFlyoutShowOptionsFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IFlyoutShowOptions]],  # value
                              _type.HRESULT]


class IGeneratorPositionHelper(_inspectable.IInspectable):
    pass


class IGeneratorPositionHelperStatics(_inspectable.IInspectable):
    FromIndexAndOffset: _Callable[[_type.INT32,  # index
                                   _type.INT32,  # offset
                                   _Pointer[_struct.Windows.UI.Xaml.Controls.Primitives.GeneratorPosition]],  # result
                                  _type.HRESULT]

    _factory = True


class IGridViewItemPresenter(_inspectable.IInspectable):
    get_SelectionCheckMarkVisualEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                   _type.HRESULT]
    put_SelectionCheckMarkVisualEnabled: _Callable[[_type.boolean],  # value
                                                   _type.HRESULT]
    get_CheckHintBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                  _type.HRESULT]
    put_CheckHintBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                  _type.HRESULT]
    get_CheckSelectingBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                       _type.HRESULT]
    put_CheckSelectingBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                       _type.HRESULT]
    get_CheckBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                              _type.HRESULT]
    put_CheckBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                              _type.HRESULT]
    get_DragBackground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                  _type.HRESULT]
    put_DragBackground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                  _type.HRESULT]
    get_DragForeground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                  _type.HRESULT]
    put_DragForeground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                  _type.HRESULT]
    get_FocusBorderBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                    _type.HRESULT]
    put_FocusBorderBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                    _type.HRESULT]
    get_PlaceholderBackground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                         _type.HRESULT]
    put_PlaceholderBackground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                         _type.HRESULT]
    get_PointerOverBackground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                         _type.HRESULT]
    put_PointerOverBackground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                         _type.HRESULT]
    get_SelectedBackground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                      _type.HRESULT]
    put_SelectedBackground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                      _type.HRESULT]
    get_SelectedForeground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                      _type.HRESULT]
    put_SelectedForeground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                      _type.HRESULT]
    get_SelectedPointerOverBackground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                                 _type.HRESULT]
    put_SelectedPointerOverBackground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                                 _type.HRESULT]
    get_SelectedPointerOverBorderBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                                  _type.HRESULT]
    put_SelectedPointerOverBorderBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                                  _type.HRESULT]
    get_SelectedBorderThickness: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                                           _type.HRESULT]
    put_SelectedBorderThickness: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                                           _type.HRESULT]
    get_DisabledOpacity: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                   _type.HRESULT]
    put_DisabledOpacity: _Callable[[_type.DOUBLE],  # value
                                   _type.HRESULT]
    get_DragOpacity: _Callable[[_Pointer[_type.DOUBLE]],  # value
                               _type.HRESULT]
    put_DragOpacity: _Callable[[_type.DOUBLE],  # value
                               _type.HRESULT]
    get_ReorderHintOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                     _type.HRESULT]
    put_ReorderHintOffset: _Callable[[_type.DOUBLE],  # value
                                     _type.HRESULT]
    GridViewItemPresenterHorizontalContentAlignment: _Callable[[_enum.Windows.UI.Xaml.HorizontalAlignment],  # value
                                                               _type.HRESULT]
    GridViewItemPresenterVerticalContentAlignment: _Callable[[_enum.Windows.UI.Xaml.VerticalAlignment],  # value
                                                             _type.HRESULT]
    GridViewItemPresenterPadding: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                                            _type.HRESULT]
    get_PointerOverBackgroundMargin: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                                               _type.HRESULT]
    put_PointerOverBackgroundMargin: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                                               _type.HRESULT]
    get_ContentMargin: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                                 _type.HRESULT]
    put_ContentMargin: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                                 _type.HRESULT]


class IGridViewItemPresenterFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IGridViewItemPresenter]],  # value
                              _type.HRESULT]


class IGridViewItemPresenterStatics(_inspectable.IInspectable):
    get_SelectionCheckMarkVisualEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                           _type.HRESULT]
    get_CheckHintBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_CheckSelectingBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_CheckBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_DragBackgroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_DragForegroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_FocusBorderBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_PlaceholderBackgroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_PointerOverBackgroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_SelectedBackgroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_SelectedForegroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_SelectedPointerOverBackgroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                         _type.HRESULT]
    get_SelectedPointerOverBorderBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                          _type.HRESULT]
    get_SelectedBorderThicknessProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_DisabledOpacityProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_DragOpacityProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_ReorderHintOffsetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    GridViewItemPresenterHorizontalContentAlignmentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                                       _type.HRESULT]
    GridViewItemPresenterVerticalContentAlignmentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                                     _type.HRESULT]
    GridViewItemPresenterPaddingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]
    get_PointerOverBackgroundMarginProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]
    get_ContentMarginProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]

    _factory = True


class IGridViewItemTemplateSettings(_inspectable.IInspectable):
    get_DragItemsCount: _Callable[[_Pointer[_type.INT32]],  # value
                                  _type.HRESULT]


class IItemsChangedEventArgs(_inspectable.IInspectable):
    get_Action: _Callable[[_Pointer[_type.INT32]],  # value
                          _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Controls.Primitives.GeneratorPosition]],  # value
                            _type.HRESULT]
    get_OldPosition: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Controls.Primitives.GeneratorPosition]],  # value
                               _type.HRESULT]
    get_ItemCount: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]
    get_ItemUICount: _Callable[[_Pointer[_type.INT32]],  # value
                               _type.HRESULT]


class IJumpListItemBackgroundConverter(_inspectable.IInspectable):
    get_Enabled: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                           _type.HRESULT]
    put_Enabled: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                           _type.HRESULT]
    get_Disabled: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                            _type.HRESULT]
    put_Disabled: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                            _type.HRESULT]


class IJumpListItemBackgroundConverterStatics(_inspectable.IInspectable):
    get_EnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_DisabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]

    _factory = True


class IJumpListItemForegroundConverter(_inspectable.IInspectable):
    get_Enabled: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                           _type.HRESULT]
    put_Enabled: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                           _type.HRESULT]
    get_Disabled: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                            _type.HRESULT]
    put_Disabled: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                            _type.HRESULT]


class IJumpListItemForegroundConverterStatics(_inspectable.IInspectable):
    get_EnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_DisabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]

    _factory = True


class ILayoutInformation(_inspectable.IInspectable):
    pass


class ILayoutInformationStatics(_inspectable.IInspectable):
    GetLayoutExceptionElement: _Callable[[_inspectable.IInspectable,  # dispatcher
                                          _Pointer[_Windows_UI_Xaml.IUIElement]],  # result
                                         _type.HRESULT]
    GetLayoutSlot: _Callable[[_Windows_UI_Xaml.IFrameworkElement,  # element
                              _Pointer[_struct.Windows.Foundation.Rect]],  # result
                             _type.HRESULT]

    _factory = True


class ILayoutInformationStatics2(_inspectable.IInspectable):
    GetAvailableSize: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                 _Pointer[_struct.Windows.Foundation.Size]],  # result
                                _type.HRESULT]

    _factory = True


class IListViewItemPresenter(_inspectable.IInspectable):
    get_SelectionCheckMarkVisualEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                   _type.HRESULT]
    put_SelectionCheckMarkVisualEnabled: _Callable[[_type.boolean],  # value
                                                   _type.HRESULT]
    get_CheckHintBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                  _type.HRESULT]
    put_CheckHintBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                  _type.HRESULT]
    get_CheckSelectingBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                       _type.HRESULT]
    put_CheckSelectingBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                       _type.HRESULT]
    get_CheckBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                              _type.HRESULT]
    put_CheckBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                              _type.HRESULT]
    get_DragBackground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                  _type.HRESULT]
    put_DragBackground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                  _type.HRESULT]
    get_DragForeground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                  _type.HRESULT]
    put_DragForeground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                  _type.HRESULT]
    get_FocusBorderBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                    _type.HRESULT]
    put_FocusBorderBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                    _type.HRESULT]
    get_PlaceholderBackground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                         _type.HRESULT]
    put_PlaceholderBackground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                         _type.HRESULT]
    get_PointerOverBackground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                         _type.HRESULT]
    put_PointerOverBackground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                         _type.HRESULT]
    get_SelectedBackground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                      _type.HRESULT]
    put_SelectedBackground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                      _type.HRESULT]
    get_SelectedForeground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                      _type.HRESULT]
    put_SelectedForeground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                      _type.HRESULT]
    get_SelectedPointerOverBackground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                                 _type.HRESULT]
    put_SelectedPointerOverBackground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                                 _type.HRESULT]
    get_SelectedPointerOverBorderBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                                  _type.HRESULT]
    put_SelectedPointerOverBorderBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                                  _type.HRESULT]
    get_SelectedBorderThickness: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                                           _type.HRESULT]
    put_SelectedBorderThickness: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                                           _type.HRESULT]
    get_DisabledOpacity: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                   _type.HRESULT]
    put_DisabledOpacity: _Callable[[_type.DOUBLE],  # value
                                   _type.HRESULT]
    get_DragOpacity: _Callable[[_Pointer[_type.DOUBLE]],  # value
                               _type.HRESULT]
    put_DragOpacity: _Callable[[_type.DOUBLE],  # value
                               _type.HRESULT]
    get_ReorderHintOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                     _type.HRESULT]
    put_ReorderHintOffset: _Callable[[_type.DOUBLE],  # value
                                     _type.HRESULT]
    ListViewItemPresenterHorizontalContentAlignment: _Callable[[_enum.Windows.UI.Xaml.HorizontalAlignment],  # value
                                                               _type.HRESULT]
    ListViewItemPresenterVerticalContentAlignment: _Callable[[_enum.Windows.UI.Xaml.VerticalAlignment],  # value
                                                             _type.HRESULT]
    ListViewItemPresenterPadding: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                                            _type.HRESULT]
    get_PointerOverBackgroundMargin: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                                               _type.HRESULT]
    put_PointerOverBackgroundMargin: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                                               _type.HRESULT]
    get_ContentMargin: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                                 _type.HRESULT]
    put_ContentMargin: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                                 _type.HRESULT]


class IListViewItemPresenter2(_inspectable.IInspectable):
    get_SelectedPressedBackground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                             _type.HRESULT]
    put_SelectedPressedBackground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                             _type.HRESULT]
    get_PressedBackground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                     _type.HRESULT]
    put_PressedBackground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                     _type.HRESULT]
    get_CheckBoxBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                 _type.HRESULT]
    put_CheckBoxBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                 _type.HRESULT]
    get_FocusSecondaryBorderBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                             _type.HRESULT]
    put_FocusSecondaryBorderBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                             _type.HRESULT]
    get_CheckMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Primitives.ListViewItemPresenterCheckMode]],  # value
                             _type.HRESULT]
    put_CheckMode: _Callable[[_enum.Windows.UI.Xaml.Controls.Primitives.ListViewItemPresenterCheckMode],  # value
                             _type.HRESULT]
    get_PointerOverForeground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                         _type.HRESULT]
    put_PointerOverForeground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                         _type.HRESULT]


class IListViewItemPresenter3(_inspectable.IInspectable):
    get_RevealBackground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                    _type.HRESULT]
    put_RevealBackground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                    _type.HRESULT]
    get_RevealBorderBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                     _type.HRESULT]
    put_RevealBorderBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                     _type.HRESULT]
    get_RevealBorderThickness: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                                         _type.HRESULT]
    put_RevealBorderThickness: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                                         _type.HRESULT]
    get_RevealBackgroundShowsAboveContent: _Callable[[_Pointer[_type.boolean]],  # value
                                                     _type.HRESULT]
    put_RevealBackgroundShowsAboveContent: _Callable[[_type.boolean],  # value
                                                     _type.HRESULT]


class IListViewItemPresenter4(_inspectable.IInspectable):
    get_SelectedDisabledBackground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                              _type.HRESULT]
    put_SelectedDisabledBackground: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                              _type.HRESULT]
    get_CheckPressedBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                     _type.HRESULT]
    put_CheckPressedBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                     _type.HRESULT]
    get_CheckDisabledBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                      _type.HRESULT]
    put_CheckDisabledBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                      _type.HRESULT]
    get_CheckBoxPointerOverBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                            _type.HRESULT]
    put_CheckBoxPointerOverBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                            _type.HRESULT]
    get_CheckBoxPressedBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                        _type.HRESULT]
    put_CheckBoxPressedBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                        _type.HRESULT]
    get_CheckBoxDisabledBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                         _type.HRESULT]
    put_CheckBoxDisabledBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                         _type.HRESULT]
    get_CheckBoxSelectedBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                         _type.HRESULT]
    put_CheckBoxSelectedBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                         _type.HRESULT]
    get_CheckBoxSelectedPointerOverBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                                    _type.HRESULT]
    put_CheckBoxSelectedPointerOverBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                                    _type.HRESULT]
    get_CheckBoxSelectedPressedBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                                _type.HRESULT]
    put_CheckBoxSelectedPressedBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                                _type.HRESULT]
    get_CheckBoxSelectedDisabledBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                                 _type.HRESULT]
    put_CheckBoxSelectedDisabledBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                                 _type.HRESULT]
    get_CheckBoxBorderBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                       _type.HRESULT]
    put_CheckBoxBorderBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                       _type.HRESULT]
    get_CheckBoxPointerOverBorderBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                                  _type.HRESULT]
    put_CheckBoxPointerOverBorderBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                                  _type.HRESULT]
    get_CheckBoxPressedBorderBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                              _type.HRESULT]
    put_CheckBoxPressedBorderBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                              _type.HRESULT]
    get_CheckBoxDisabledBorderBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                               _type.HRESULT]
    put_CheckBoxDisabledBorderBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                               _type.HRESULT]
    get_CheckBoxCornerRadius: _Callable[[_Pointer[_struct.Windows.UI.Xaml.CornerRadius]],  # value
                                        _type.HRESULT]
    put_CheckBoxCornerRadius: _Callable[[_struct.Windows.UI.Xaml.CornerRadius],  # value
                                        _type.HRESULT]
    get_SelectionIndicatorCornerRadius: _Callable[[_Pointer[_struct.Windows.UI.Xaml.CornerRadius]],  # value
                                                  _type.HRESULT]
    put_SelectionIndicatorCornerRadius: _Callable[[_struct.Windows.UI.Xaml.CornerRadius],  # value
                                                  _type.HRESULT]
    get_SelectionIndicatorVisualEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                   _type.HRESULT]
    put_SelectionIndicatorVisualEnabled: _Callable[[_type.boolean],  # value
                                                   _type.HRESULT]
    get_SelectionIndicatorMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Primitives.ListViewItemPresenterSelectionIndicatorMode]],  # value
                                          _type.HRESULT]
    put_SelectionIndicatorMode: _Callable[[_enum.Windows.UI.Xaml.Controls.Primitives.ListViewItemPresenterSelectionIndicatorMode],  # value
                                          _type.HRESULT]
    get_SelectionIndicatorBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                           _type.HRESULT]
    put_SelectionIndicatorBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                           _type.HRESULT]
    get_SelectionIndicatorPointerOverBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                                      _type.HRESULT]
    put_SelectionIndicatorPointerOverBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                                      _type.HRESULT]
    get_SelectionIndicatorPressedBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                                  _type.HRESULT]
    put_SelectionIndicatorPressedBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                                  _type.HRESULT]
    get_SelectionIndicatorDisabledBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                                   _type.HRESULT]
    put_SelectionIndicatorDisabledBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                                   _type.HRESULT]
    get_SelectedBorderBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                       _type.HRESULT]
    put_SelectedBorderBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                       _type.HRESULT]
    get_SelectedPressedBorderBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                              _type.HRESULT]
    put_SelectedPressedBorderBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                              _type.HRESULT]
    get_SelectedDisabledBorderBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                               _type.HRESULT]
    put_SelectedDisabledBorderBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                               _type.HRESULT]
    get_SelectedInnerBorderBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                            _type.HRESULT]
    put_SelectedInnerBorderBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                            _type.HRESULT]
    get_PointerOverBorderBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                          _type.HRESULT]
    put_PointerOverBorderBrush: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                                          _type.HRESULT]


class IListViewItemPresenterFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IListViewItemPresenter]],  # value
                              _type.HRESULT]


class IListViewItemPresenterStatics(_inspectable.IInspectable):
    get_SelectionCheckMarkVisualEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                           _type.HRESULT]
    get_CheckHintBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_CheckSelectingBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_CheckBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_DragBackgroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_DragForegroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_FocusBorderBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_PlaceholderBackgroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_PointerOverBackgroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_SelectedBackgroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_SelectedForegroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_SelectedPointerOverBackgroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                         _type.HRESULT]
    get_SelectedPointerOverBorderBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                          _type.HRESULT]
    get_SelectedBorderThicknessProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_DisabledOpacityProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_DragOpacityProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_ReorderHintOffsetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    ListViewItemPresenterHorizontalContentAlignmentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                                       _type.HRESULT]
    ListViewItemPresenterVerticalContentAlignmentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                                     _type.HRESULT]
    ListViewItemPresenterPaddingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]
    get_PointerOverBackgroundMarginProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]
    get_ContentMarginProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]

    _factory = True


class IListViewItemPresenterStatics2(_inspectable.IInspectable):
    get_SelectedPressedBackgroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                     _type.HRESULT]
    get_PressedBackgroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_CheckBoxBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_FocusSecondaryBorderBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                     _type.HRESULT]
    get_CheckModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_PointerOverForegroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]

    _factory = True


class IListViewItemPresenterStatics3(_inspectable.IInspectable):
    get_RevealBackgroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_RevealBorderBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_RevealBorderThicknessProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_RevealBackgroundShowsAboveContentProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                             _type.HRESULT]

    _factory = True


class IListViewItemPresenterStatics4(_inspectable.IInspectable):
    get_SelectedDisabledBackgroundProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                      _type.HRESULT]
    get_CheckPressedBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_CheckDisabledBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_CheckBoxPointerOverBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]
    get_CheckBoxPressedBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_CheckBoxDisabledBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_CheckBoxSelectedBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_CheckBoxSelectedPointerOverBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                            _type.HRESULT]
    get_CheckBoxSelectedPressedBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                        _type.HRESULT]
    get_CheckBoxSelectedDisabledBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                         _type.HRESULT]
    get_CheckBoxBorderBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_CheckBoxPointerOverBorderBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                          _type.HRESULT]
    get_CheckBoxPressedBorderBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                      _type.HRESULT]
    get_CheckBoxDisabledBorderBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]
    get_CheckBoxCornerRadiusProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_SelectionIndicatorCornerRadiusProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                          _type.HRESULT]
    get_SelectionIndicatorVisualEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                           _type.HRESULT]
    get_SelectionIndicatorModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]
    get_SelectionIndicatorBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_SelectionIndicatorPointerOverBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                              _type.HRESULT]
    get_SelectionIndicatorPressedBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                          _type.HRESULT]
    get_SelectionIndicatorDisabledBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                           _type.HRESULT]
    get_SelectedBorderBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_SelectedPressedBorderBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                      _type.HRESULT]
    get_SelectedDisabledBorderBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]
    get_SelectedInnerBorderBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]
    get_PointerOverBorderBrushProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]

    _factory = True


class IListViewItemTemplateSettings(_inspectable.IInspectable):
    get_DragItemsCount: _Callable[[_Pointer[_type.INT32]],  # value
                                  _type.HRESULT]


class ILoopingSelector(_inspectable.IInspectable):
    get_ShouldLoop: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    put_ShouldLoop: _Callable[[_type.boolean],  # value
                              _type.HRESULT]
    get_Items: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_inspectable.IInspectable]]],  # value
                         _type.HRESULT]
    put_Items: _Callable[[_Windows_Foundation_Collections.IVector[_inspectable.IInspectable]],  # value
                         _type.HRESULT]
    get_SelectedIndex: _Callable[[_Pointer[_type.INT32]],  # value
                                 _type.HRESULT]
    put_SelectedIndex: _Callable[[_type.INT32],  # value
                                 _type.HRESULT]
    get_SelectedItem: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                _type.HRESULT]
    put_SelectedItem: _Callable[[_inspectable.IInspectable],  # value
                                _type.HRESULT]
    get_ItemWidth: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]
    put_ItemWidth: _Callable[[_type.INT32],  # value
                             _type.HRESULT]
    get_ItemHeight: _Callable[[_Pointer[_type.INT32]],  # value
                              _type.HRESULT]
    put_ItemHeight: _Callable[[_type.INT32],  # value
                              _type.HRESULT]
    get_ItemTemplate: _Callable[[_Pointer[_Windows_UI_Xaml.IDataTemplate]],  # value
                                _type.HRESULT]
    put_ItemTemplate: _Callable[[_Windows_UI_Xaml.IDataTemplate],  # value
                                _type.HRESULT]
    add_SelectionChanged: _Callable[[_Windows_UI_Xaml_Controls.ISelectionChangedEventHandler,  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_SelectionChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]


class ILoopingSelectorItem(_inspectable.IInspectable):
    pass


class ILoopingSelectorPanel(_inspectable.IInspectable):
    pass


class ILoopingSelectorStatics(_inspectable.IInspectable):
    get_ShouldLoopProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_ItemsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_SelectedIndexProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_SelectedItemProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_ItemWidthProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_ItemHeightProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_ItemTemplateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]

    _factory = True


class IMenuFlyoutItemTemplateSettings(_inspectable.IInspectable):
    get_KeyboardAcceleratorTextMinWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                   _type.HRESULT]


class IMenuFlyoutPresenterTemplateSettings(_inspectable.IInspectable):
    get_FlyoutContentMinWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                         _type.HRESULT]


class INavigationViewItemPresenter(_inspectable.IInspectable):
    get_Icon: _Callable[[_Pointer[_Windows_UI_Xaml_Controls.IIconElement]],  # value
                        _type.HRESULT]
    put_Icon: _Callable[[_Windows_UI_Xaml_Controls.IIconElement],  # value
                        _type.HRESULT]


class INavigationViewItemPresenterFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[INavigationViewItemPresenter]],  # value
                              _type.HRESULT]


class INavigationViewItemPresenterStatics(_inspectable.IInspectable):
    get_IconProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]

    _factory = True


class IOrientedVirtualizingPanel(_inspectable.IInspectable):
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


class IOrientedVirtualizingPanelFactory(_inspectable.IInspectable):
    pass


class IPickerFlyoutBase(_inspectable.IInspectable):
    pass


class IPickerFlyoutBaseFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IPickerFlyoutBase]],  # value
                              _type.HRESULT]


class IPickerFlyoutBaseOverrides(_inspectable.IInspectable):
    OnConfirmed: _Callable[[],
                           _type.HRESULT]
    ShouldShowConfirmationButtons: _Callable[[_Pointer[_type.boolean]],  # result
                                             _type.HRESULT]


class IPickerFlyoutBaseStatics(_inspectable.IInspectable):
    get_TitleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    GetTitle: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                         _Pointer[_type.HSTRING]],  # result
                        _type.HRESULT]
    SetTitle: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                         _type.HSTRING],  # value
                        _type.HRESULT]

    _factory = True


class IPivotHeaderItem(_inspectable.IInspectable):
    pass


class IPivotHeaderItemFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IPivotHeaderItem]],  # value
                              _type.HRESULT]


class IPivotHeaderPanel(_inspectable.IInspectable):
    pass


class IPivotPanel(_inspectable.IInspectable):
    pass


class IPopup(_inspectable.IInspectable):
    get_Child: _Callable[[_Pointer[_Windows_UI_Xaml.IUIElement]],  # value
                         _type.HRESULT]
    put_Child: _Callable[[_Windows_UI_Xaml.IUIElement],  # value
                         _type.HRESULT]
    get_IsOpen: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_IsOpen: _Callable[[_type.boolean],  # value
                          _type.HRESULT]
    get_HorizontalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]
    put_HorizontalOffset: _Callable[[_type.DOUBLE],  # value
                                    _type.HRESULT]
    get_VerticalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    put_VerticalOffset: _Callable[[_type.DOUBLE],  # value
                                  _type.HRESULT]
    get_ChildTransitions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Media_Animation.ITransition]]],  # value
                                    _type.HRESULT]
    put_ChildTransitions: _Callable[[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Media_Animation.ITransition]],  # value
                                    _type.HRESULT]
    get_IsLightDismissEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_IsLightDismissEnabled: _Callable[[_type.boolean],  # value
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


class IPopup2(_inspectable.IInspectable):
    get_LightDismissOverlayMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.LightDismissOverlayMode]],  # value
                                           _type.HRESULT]
    put_LightDismissOverlayMode: _Callable[[_enum.Windows.UI.Xaml.Controls.LightDismissOverlayMode],  # value
                                           _type.HRESULT]


class IPopup3(_inspectable.IInspectable):
    get_ShouldConstrainToRootBounds: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]
    put_ShouldConstrainToRootBounds: _Callable[[_type.boolean],  # value
                                               _type.HRESULT]
    get_IsConstrainedToRootBounds: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]


class IPopup4(_inspectable.IInspectable):
    get_PlacementTarget: _Callable[[_Pointer[_Windows_UI_Xaml.IFrameworkElement]],  # value
                                   _type.HRESULT]
    put_PlacementTarget: _Callable[[_Windows_UI_Xaml.IFrameworkElement],  # value
                                   _type.HRESULT]
    get_DesiredPlacement: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Primitives.PopupPlacementMode]],  # value
                                    _type.HRESULT]
    put_DesiredPlacement: _Callable[[_enum.Windows.UI.Xaml.Controls.Primitives.PopupPlacementMode],  # value
                                    _type.HRESULT]
    get_ActualPlacement: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Primitives.PopupPlacementMode]],  # value
                                   _type.HRESULT]
    add_ActualPlacementChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_ActualPlacementChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]


class IPopupStatics(_inspectable.IInspectable):
    get_ChildProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_IsOpenProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_HorizontalOffsetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_VerticalOffsetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_ChildTransitionsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_IsLightDismissEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]

    _factory = True


class IPopupStatics2(_inspectable.IInspectable):
    get_LightDismissOverlayModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]

    _factory = True


class IPopupStatics3(_inspectable.IInspectable):
    get_ShouldConstrainToRootBoundsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]

    _factory = True


class IPopupStatics4(_inspectable.IInspectable):
    get_PlacementTargetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_DesiredPlacementProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]

    _factory = True


class IProgressBarTemplateSettings(_inspectable.IInspectable):
    get_EllipseDiameter: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                   _type.HRESULT]
    get_EllipseOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                 _type.HRESULT]
    get_EllipseAnimationWellPosition: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                _type.HRESULT]
    get_EllipseAnimationEndPosition: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                               _type.HRESULT]
    get_ContainerAnimationStartPosition: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                   _type.HRESULT]
    get_ContainerAnimationEndPosition: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                 _type.HRESULT]
    get_IndicatorLengthDelta: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                        _type.HRESULT]


class IProgressRingTemplateSettings(_inspectable.IInspectable):
    get_EllipseDiameter: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                   _type.HRESULT]
    get_EllipseOffset: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                                 _type.HRESULT]
    get_MaxSideLength: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                 _type.HRESULT]


class IRangeBase(_inspectable.IInspectable):
    get_Minimum: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    put_Minimum: _Callable[[_type.DOUBLE],  # value
                           _type.HRESULT]
    get_Maximum: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    put_Maximum: _Callable[[_type.DOUBLE],  # value
                           _type.HRESULT]
    get_SmallChange: _Callable[[_Pointer[_type.DOUBLE]],  # value
                               _type.HRESULT]
    put_SmallChange: _Callable[[_type.DOUBLE],  # value
                               _type.HRESULT]
    get_LargeChange: _Callable[[_Pointer[_type.DOUBLE]],  # value
                               _type.HRESULT]
    put_LargeChange: _Callable[[_type.DOUBLE],  # value
                               _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.DOUBLE]],  # value
                         _type.HRESULT]
    put_Value: _Callable[[_type.DOUBLE],  # value
                         _type.HRESULT]
    add_ValueChanged: _Callable[[IRangeBaseValueChangedEventHandler,  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_ValueChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]


class IRangeBaseFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IRangeBase]],  # value
                              _type.HRESULT]


class IRangeBaseOverrides(_inspectable.IInspectable):
    OnMinimumChanged: _Callable[[_type.DOUBLE,  # oldMinimum
                                 _type.DOUBLE],  # newMinimum
                                _type.HRESULT]
    OnMaximumChanged: _Callable[[_type.DOUBLE,  # oldMaximum
                                 _type.DOUBLE],  # newMaximum
                                _type.HRESULT]
    OnValueChanged: _Callable[[_type.DOUBLE,  # oldValue
                               _type.DOUBLE],  # newValue
                              _type.HRESULT]


class IRangeBaseStatics(_inspectable.IInspectable):
    get_MinimumProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_MaximumProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_SmallChangeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_LargeChangeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_ValueProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]

    _factory = True


class IRangeBaseValueChangedEventArgs(_inspectable.IInspectable):
    get_OldValue: _Callable[[_Pointer[_type.DOUBLE]],  # value
                            _type.HRESULT]
    get_NewValue: _Callable[[_Pointer[_type.DOUBLE]],  # value
                            _type.HRESULT]


class IRepeatButton(_inspectable.IInspectable):
    get_Delay: _Callable[[_Pointer[_type.INT32]],  # value
                         _type.HRESULT]
    put_Delay: _Callable[[_type.INT32],  # value
                         _type.HRESULT]
    get_Interval: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    put_Interval: _Callable[[_type.INT32],  # value
                            _type.HRESULT]


class IRepeatButtonStatics(_inspectable.IInspectable):
    get_DelayProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_IntervalProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]

    _factory = True


class IScrollBar(_inspectable.IInspectable):
    get_Orientation: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Orientation]],  # value
                               _type.HRESULT]
    put_Orientation: _Callable[[_enum.Windows.UI.Xaml.Controls.Orientation],  # value
                               _type.HRESULT]
    get_ViewportSize: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    put_ViewportSize: _Callable[[_type.DOUBLE],  # value
                                _type.HRESULT]
    get_IndicatorMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Primitives.ScrollingIndicatorMode]],  # value
                                 _type.HRESULT]
    put_IndicatorMode: _Callable[[_enum.Windows.UI.Xaml.Controls.Primitives.ScrollingIndicatorMode],  # value
                                 _type.HRESULT]
    add_Scroll: _Callable[[IScrollEventHandler,  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Scroll: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]


class IScrollBarStatics(_inspectable.IInspectable):
    get_OrientationProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_ViewportSizeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_IndicatorModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]

    _factory = True


class IScrollEventArgs(_inspectable.IInspectable):
    get_NewValue: _Callable[[_Pointer[_type.DOUBLE]],  # value
                            _type.HRESULT]
    get_ScrollEventType: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Primitives.ScrollEventType]],  # value
                                   _type.HRESULT]


class IScrollSnapPointsInfo(_inspectable.IInspectable):
    get_AreHorizontalSnapPointsRegular: _Callable[[_Pointer[_type.boolean]],  # value
                                                  _type.HRESULT]
    get_AreVerticalSnapPointsRegular: _Callable[[_Pointer[_type.boolean]],  # value
                                                _type.HRESULT]
    add_HorizontalSnapPointsChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                                _Pointer[_struct.EventRegistrationToken]],  # token
                                               _type.HRESULT]
    remove_HorizontalSnapPointsChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                  _type.HRESULT]
    add_VerticalSnapPointsChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                              _Pointer[_struct.EventRegistrationToken]],  # token
                                             _type.HRESULT]
    remove_VerticalSnapPointsChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                _type.HRESULT]
    GetIrregularSnapPoints: _Callable[[_enum.Windows.UI.Xaml.Controls.Orientation,  # orientation
                                       _enum.Windows.UI.Xaml.Controls.Primitives.SnapPointsAlignment,  # alignment
                                       _Pointer[_Windows_Foundation_Collections.IVectorView[_type.FLOAT]]],  # result
                                      _type.HRESULT]
    GetRegularSnapPoints: _Callable[[_enum.Windows.UI.Xaml.Controls.Orientation,  # orientation
                                     _enum.Windows.UI.Xaml.Controls.Primitives.SnapPointsAlignment,  # alignment
                                     _Pointer[_type.FLOAT],  # offset
                                     _Pointer[_type.FLOAT]],  # returnValue
                                    _type.HRESULT]


class ISelector(_inspectable.IInspectable):
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
    get_IsSynchronizedWithCurrentItem: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.boolean]]],  # value
                                                 _type.HRESULT]
    put_IsSynchronizedWithCurrentItem: _Callable[[_Windows_Foundation.IReference[_type.boolean]],  # value
                                                 _type.HRESULT]
    add_SelectionChanged: _Callable[[_Windows_UI_Xaml_Controls.ISelectionChangedEventHandler,  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_SelectionChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]


class ISelectorFactory(_inspectable.IInspectable):
    pass


class ISelectorItem(_inspectable.IInspectable):
    get_IsSelected: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    put_IsSelected: _Callable[[_type.boolean],  # value
                              _type.HRESULT]


class ISelectorItemFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ISelectorItem]],  # value
                              _type.HRESULT]


class ISelectorItemStatics(_inspectable.IInspectable):
    get_IsSelectedProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]

    _factory = True


class ISelectorStatics(_inspectable.IInspectable):
    get_SelectedIndexProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_SelectedItemProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_SelectedValueProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_SelectedValuePathProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_IsSynchronizedWithCurrentItemProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                         _type.HRESULT]
    GetIsSelectionActive: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                     _Pointer[_type.boolean]],  # result
                                    _type.HRESULT]

    _factory = True


class ISettingsFlyoutTemplateSettings(_inspectable.IInspectable):
    get_HeaderBackground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                    _type.HRESULT]
    get_HeaderForeground: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                                    _type.HRESULT]
    get_BorderBrush: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                               _type.HRESULT]
    get_BorderThickness: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                                   _type.HRESULT]
    get_IconSource: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IImageSource]],  # value
                              _type.HRESULT]
    get_ContentTransitions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml_Media_Animation.ITransition]]],  # value
                                      _type.HRESULT]


class ISplitViewTemplateSettings(_inspectable.IInspectable):
    get_OpenPaneLength: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    get_NegativeOpenPaneLength: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                          _type.HRESULT]
    get_OpenPaneLengthMinusCompactLength: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                    _type.HRESULT]
    get_NegativeOpenPaneLengthMinusCompactLength: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                            _type.HRESULT]
    get_OpenPaneGridLength: _Callable[[_Pointer[_struct.Windows.UI.Xaml.GridLength]],  # value
                                      _type.HRESULT]
    get_CompactPaneGridLength: _Callable[[_Pointer[_struct.Windows.UI.Xaml.GridLength]],  # value
                                         _type.HRESULT]


class IThumb(_inspectable.IInspectable):
    get_IsDragging: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    add_DragStarted: _Callable[[IDragStartedEventHandler,  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_DragStarted: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    add_DragDelta: _Callable[[IDragDeltaEventHandler,  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_DragDelta: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    add_DragCompleted: _Callable[[IDragCompletedEventHandler,  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_DragCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    CancelDrag: _Callable[[],
                          _type.HRESULT]


class IThumbStatics(_inspectable.IInspectable):
    get_IsDraggingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]

    _factory = True


class ITickBar(_inspectable.IInspectable):
    get_Fill: _Callable[[_Pointer[_Windows_UI_Xaml_Media.IBrush]],  # value
                        _type.HRESULT]
    put_Fill: _Callable[[_Windows_UI_Xaml_Media.IBrush],  # value
                        _type.HRESULT]


class ITickBarStatics(_inspectable.IInspectable):
    get_FillProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]

    _factory = True


class IToggleButton(_inspectable.IInspectable):
    get_IsChecked: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.boolean]]],  # value
                             _type.HRESULT]
    put_IsChecked: _Callable[[_Windows_Foundation.IReference[_type.boolean]],  # value
                             _type.HRESULT]
    get_IsThreeState: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_IsThreeState: _Callable[[_type.boolean],  # value
                                _type.HRESULT]
    add_Checked: _Callable[[_Windows_UI_Xaml.IRoutedEventHandler,  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Checked: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_Unchecked: _Callable[[_Windows_UI_Xaml.IRoutedEventHandler,  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_Unchecked: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    add_Indeterminate: _Callable[[_Windows_UI_Xaml.IRoutedEventHandler,  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_Indeterminate: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]


class IToggleButtonFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IToggleButton]],  # value
                              _type.HRESULT]


class IToggleButtonOverrides(_inspectable.IInspectable):
    OnToggle: _Callable[[],
                        _type.HRESULT]


class IToggleButtonStatics(_inspectable.IInspectable):
    get_IsCheckedProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_IsThreeStateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]

    _factory = True


class IToggleSwitchTemplateSettings(_inspectable.IInspectable):
    get_KnobCurrentToOnOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                         _type.HRESULT]
    get_KnobCurrentToOffOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                          _type.HRESULT]
    get_KnobOnToOffOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                     _type.HRESULT]
    get_KnobOffToOnOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                     _type.HRESULT]
    get_CurtainCurrentToOnOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                            _type.HRESULT]
    get_CurtainCurrentToOffOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                             _type.HRESULT]
    get_CurtainOnToOffOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                        _type.HRESULT]
    get_CurtainOffToOnOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                        _type.HRESULT]


class IToolTipTemplateSettings(_inspectable.IInspectable):
    get_FromHorizontalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                        _type.HRESULT]
    get_FromVerticalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                      _type.HRESULT]
