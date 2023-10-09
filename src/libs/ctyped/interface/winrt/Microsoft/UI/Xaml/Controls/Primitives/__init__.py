from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Controls as _Microsoft_UI_Xaml_Controls
from ... import Input as _Microsoft_UI_Xaml_Input
from ... import Media as _Microsoft_UI_Xaml_Media
from ...Media import Animation as _Microsoft_UI_Xaml_Media_Animation
from .... import Composition as _Microsoft_UI_Composition
from .... import Input as _Microsoft_UI_Input
from .... import Xaml as _Microsoft_UI_Xaml
from ...... import inspectable as _inspectable
from ......Windows import Foundation as _Windows_Foundation
from ......Windows.Foundation import Collections as _Windows_Foundation_Collections
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
    get_CompactRootMargin: _Callable[[_Pointer[_struct.Microsoft.UI.Xaml.Thickness]],  # value
                                     _type.HRESULT]
    get_MinimalVerticalDelta: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                        _type.HRESULT]
    get_MinimalRootMargin: _Callable[[_Pointer[_struct.Microsoft.UI.Xaml.Thickness]],  # value
                                     _type.HRESULT]
    get_HiddenVerticalDelta: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                       _type.HRESULT]
    get_HiddenRootMargin: _Callable[[_Pointer[_struct.Microsoft.UI.Xaml.Thickness]],  # value
                                    _type.HRESULT]
    get_NegativeCompactVerticalDelta: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                _type.HRESULT]
    get_NegativeMinimalVerticalDelta: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                _type.HRESULT]
    get_NegativeHiddenVerticalDelta: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                               _type.HRESULT]


class IAppBarToggleButtonTemplateSettings(_inspectable.IInspectable):
    get_KeyboardAcceleratorTextMinWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                   _type.HRESULT]


class IAutoSuggestBoxHelper(_inspectable.IInspectable):
    pass


class IAutoSuggestBoxHelperStatics(_inspectable.IInspectable, factory=True):
    get_KeepInteriorCornersSquareProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                     _type.HRESULT]
    SetKeepInteriorCornersSquare: _Callable[[_Microsoft_UI_Xaml_Controls.IAutoSuggestBox,  # autoSuggestBox
                                             _type.boolean],  # value
                                            _type.HRESULT]
    GetKeepInteriorCornersSquare: _Callable[[_Microsoft_UI_Xaml_Controls.IAutoSuggestBox,  # autoSuggestBox
                                             _Pointer[_type.boolean]],  # result
                                            _type.HRESULT]


class IButtonBase(_inspectable.IInspectable):
    get_ClickMode: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Controls.ClickMode]],  # value
                             _type.HRESULT]
    put_ClickMode: _Callable[[_enum.Microsoft.UI.Xaml.Controls.ClickMode],  # value
                             _type.HRESULT]
    get_IsPointerOver: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_IsPressed: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_Command: _Callable[[_Pointer[_Microsoft_UI_Xaml_Input.ICommand]],  # value
                           _type.HRESULT]
    put_Command: _Callable[[_Microsoft_UI_Xaml_Input.ICommand],  # value
                           _type.HRESULT]
    get_CommandParameter: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                    _type.HRESULT]
    put_CommandParameter: _Callable[[_inspectable.IInspectable],  # value
                                    _type.HRESULT]
    add_Click: _Callable[[_Microsoft_UI_Xaml.IRoutedEventHandler,  # handler
                          _Pointer[_struct.EventRegistrationToken]],  # token
                         _type.HRESULT]
    remove_Click: _Callable[[_struct.EventRegistrationToken],  # token
                            _type.HRESULT]


class IButtonBaseFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IButtonBase]],  # value
                              _type.HRESULT]


class IButtonBaseStatics(_inspectable.IInspectable, factory=True):
    get_ClickModeProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_IsPointerOverProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_IsPressedProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_CommandProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_CommandParameterProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]


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
    MakeVisible: _Callable[[_Microsoft_UI_Xaml.IUIElement,  # visual
                            _struct.Windows.Foundation.Rect,  # rectangle
                            _Pointer[_struct.Windows.Foundation.Rect]],  # result
                           _type.HRESULT]


class ICarouselPanelFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ICarouselPanel]],  # value
                              _type.HRESULT]


class IColorPickerSlider(_inspectable.IInspectable):
    get_ColorChannel: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Controls.ColorPickerHsvChannel]],  # value
                                _type.HRESULT]
    put_ColorChannel: _Callable[[_enum.Microsoft.UI.Xaml.Controls.ColorPickerHsvChannel],  # value
                                _type.HRESULT]


class IColorPickerSliderFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IColorPickerSlider]],  # value
                              _type.HRESULT]


class IColorPickerSliderStatics(_inspectable.IInspectable, factory=True):
    get_ColorChannelProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]


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
    get_Shape: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Controls.ColorSpectrumShape]],  # value
                         _type.HRESULT]
    put_Shape: _Callable[[_enum.Microsoft.UI.Xaml.Controls.ColorSpectrumShape],  # value
                         _type.HRESULT]
    get_Components: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Controls.ColorSpectrumComponents]],  # value
                              _type.HRESULT]
    put_Components: _Callable[[_enum.Microsoft.UI.Xaml.Controls.ColorSpectrumComponents],  # value
                              _type.HRESULT]
    add_ColorChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IColorSpectrum, _Microsoft_UI_Xaml_Controls.IColorChangedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_ColorChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]


class IColorSpectrumFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IColorSpectrum]],  # value
                              _type.HRESULT]


class IColorSpectrumStatics(_inspectable.IInspectable, factory=True):
    get_ColorProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_HsvColorProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_MinHueProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_MaxHueProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_MinSaturationProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_MaxSaturationProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_MinValueProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_MaxValueProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_ShapeProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_ComponentsProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]


class IColumnMajorUniformToLargestGridLayout(_inspectable.IInspectable):
    get_MaxColumns: _Callable[[_Pointer[_type.INT32]],  # value
                              _type.HRESULT]
    put_MaxColumns: _Callable[[_type.INT32],  # value
                              _type.HRESULT]
    get_ColumnSpacing: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                 _type.HRESULT]
    put_ColumnSpacing: _Callable[[_type.DOUBLE],  # value
                                 _type.HRESULT]
    get_RowSpacing: _Callable[[_Pointer[_type.DOUBLE]],  # value
                              _type.HRESULT]
    put_RowSpacing: _Callable[[_type.DOUBLE],  # value
                              _type.HRESULT]


class IColumnMajorUniformToLargestGridLayoutFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IColumnMajorUniformToLargestGridLayout]],  # value
                              _type.HRESULT]


class IColumnMajorUniformToLargestGridLayoutStatics(_inspectable.IInspectable, factory=True):
    get_MaxColumnsProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_ColumnSpacingProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_RowSpacingProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]


class IComboBoxHelper(_inspectable.IInspectable):
    pass


class IComboBoxHelperStatics(_inspectable.IInspectable, factory=True):
    get_KeepInteriorCornersSquareProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                     _type.HRESULT]
    SetKeepInteriorCornersSquare: _Callable[[_Microsoft_UI_Xaml_Controls.IComboBox,  # comboBox
                                             _type.boolean],  # value
                                            _type.HRESULT]
    GetKeepInteriorCornersSquare: _Callable[[_Microsoft_UI_Xaml_Controls.IComboBox,  # comboBox
                                             _Pointer[_type.boolean]],  # result
                                            _type.HRESULT]


class IComboBoxTemplateSettings(_inspectable.IInspectable):
    get_DropDownOpenedHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                        _type.HRESULT]
    get_DropDownClosedHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                        _type.HRESULT]
    get_DropDownOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    get_SelectedItemDirection: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Controls.Primitives.AnimationDirection]],  # value
                                         _type.HRESULT]
    get_DropDownContentMinWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                           _type.HRESULT]


class ICommandBarFlyoutCommandBar(_inspectable.IInspectable):
    get_FlyoutTemplateSettings: _Callable[[_Pointer[ICommandBarFlyoutCommandBarTemplateSettings]],  # value
                                          _type.HRESULT]


class ICommandBarFlyoutCommandBar2(_inspectable.IInspectable):
    get_SystemBackdrop: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.ISystemBackdrop]],  # value
                                  _type.HRESULT]
    put_SystemBackdrop: _Callable[[_Microsoft_UI_Xaml_Media.ISystemBackdrop],  # value
                                  _type.HRESULT]


class ICommandBarFlyoutCommandBarAutomationPropertiesStatics(_inspectable.IInspectable, factory=True):
    get_ControlTypeProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    GetControlType: _Callable[[_Microsoft_UI_Xaml.IUIElement,  # element
                               _Pointer[_enum.Microsoft.UI.Xaml.Automation.Peers.AutomationControlType]],  # result
                              _type.HRESULT]
    SetControlType: _Callable[[_Microsoft_UI_Xaml.IUIElement,  # element
                               _enum.Microsoft.UI.Xaml.Automation.Peers.AutomationControlType],  # value
                              _type.HRESULT]


class ICommandBarFlyoutCommandBarFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ICommandBarFlyoutCommandBar]],  # value
                              _type.HRESULT]


class ICommandBarFlyoutCommandBarStatics(_inspectable.IInspectable, factory=True):
    get_SystemBackdropProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
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
    get_OverflowContentMaxWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                           _type.HRESULT]
    get_OverflowContentMaxHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                            _type.HRESULT]
    get_OverflowContentHorizontalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                   _type.HRESULT]
    get_OverflowContentHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                         _type.HRESULT]
    get_NegativeOverflowContentHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                 _type.HRESULT]
    get_EffectiveOverflowButtonVisibility: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Visibility]],  # value
                                                     _type.HRESULT]
    get_OverflowContentCompactYTranslation: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                      _type.HRESULT]
    get_OverflowContentMinimalYTranslation: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                      _type.HRESULT]
    get_OverflowContentHiddenYTranslation: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                     _type.HRESULT]


class ICornerRadiusFilterConverter(_inspectable.IInspectable):
    get_Filter: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Controls.Primitives.CornerRadiusFilterKind]],  # value
                          _type.HRESULT]
    put_Filter: _Callable[[_enum.Microsoft.UI.Xaml.Controls.Primitives.CornerRadiusFilterKind],  # value
                          _type.HRESULT]
    get_Scale: _Callable[[_Pointer[_type.DOUBLE]],  # value
                         _type.HRESULT]
    put_Scale: _Callable[[_type.DOUBLE],  # value
                         _type.HRESULT]


class ICornerRadiusFilterConverterStatics(_inspectable.IInspectable, factory=True):
    get_FilterProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_ScaleProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]


class ICornerRadiusToThicknessConverter(_inspectable.IInspectable):
    get_ConversionKind: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Controls.Primitives.CornerRadiusToThicknessConverterKind]],  # value
                                  _type.HRESULT]
    put_ConversionKind: _Callable[[_enum.Microsoft.UI.Xaml.Controls.Primitives.CornerRadiusToThicknessConverterKind],  # value
                                  _type.HRESULT]
    get_Multiplier: _Callable[[_Pointer[_type.DOUBLE]],  # value
                              _type.HRESULT]
    put_Multiplier: _Callable[[_type.DOUBLE],  # value
                              _type.HRESULT]


class ICornerRadiusToThicknessConverterStatics(_inspectable.IInspectable, factory=True):
    get_ConversionKindProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_MultiplierProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
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
    get_Placement: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Controls.Primitives.FlyoutPlacementMode]],  # value
                             _type.HRESULT]
    put_Placement: _Callable[[_enum.Microsoft.UI.Xaml.Controls.Primitives.FlyoutPlacementMode],  # value
                             _type.HRESULT]
    get_Target: _Callable[[_Pointer[_Microsoft_UI_Xaml.IFrameworkElement]],  # value
                          _type.HRESULT]
    get_AllowFocusOnInteraction: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    put_AllowFocusOnInteraction: _Callable[[_type.boolean],  # value
                                           _type.HRESULT]
    get_LightDismissOverlayMode: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Controls.LightDismissOverlayMode]],  # value
                                           _type.HRESULT]
    put_LightDismissOverlayMode: _Callable[[_enum.Microsoft.UI.Xaml.Controls.LightDismissOverlayMode],  # value
                                           _type.HRESULT]
    get_AllowFocusWhenDisabled: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_AllowFocusWhenDisabled: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    get_ShowMode: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Controls.Primitives.FlyoutShowMode]],  # value
                            _type.HRESULT]
    put_ShowMode: _Callable[[_enum.Microsoft.UI.Xaml.Controls.Primitives.FlyoutShowMode],  # value
                            _type.HRESULT]
    get_InputDevicePrefersPrimaryCommands: _Callable[[_Pointer[_type.boolean]],  # value
                                                     _type.HRESULT]
    get_AreOpenCloseAnimationsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]
    put_AreOpenCloseAnimationsEnabled: _Callable[[_type.boolean],  # value
                                                 _type.HRESULT]
    get_ShouldConstrainToRootBounds: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]
    put_ShouldConstrainToRootBounds: _Callable[[_type.boolean],  # value
                                               _type.HRESULT]
    get_IsConstrainedToRootBounds: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    get_ElementSoundMode: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.ElementSoundMode]],  # value
                                    _type.HRESULT]
    put_ElementSoundMode: _Callable[[_enum.Microsoft.UI.Xaml.ElementSoundMode],  # value
                                    _type.HRESULT]
    get_OverlayInputPassThroughElement: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyObject]],  # value
                                                  _type.HRESULT]
    put_OverlayInputPassThroughElement: _Callable[[_Microsoft_UI_Xaml.IDependencyObject],  # value
                                                  _type.HRESULT]
    get_IsOpen: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    get_XamlRoot: _Callable[[_Pointer[_Microsoft_UI_Xaml.IXamlRoot]],  # value
                            _type.HRESULT]
    put_XamlRoot: _Callable[[_Microsoft_UI_Xaml.IXamlRoot],  # value
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
    add_Closing: _Callable[[_Windows_Foundation.ITypedEventHandler[IFlyoutBase, IFlyoutBaseClosingEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Closing: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    ShowAt: _Callable[[_Microsoft_UI_Xaml.IFrameworkElement],  # placementTarget
                      _type.HRESULT]
    ShowAtWithOptions: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # placementTarget
                                  IFlyoutShowOptions],  # showOptions
                                 _type.HRESULT]
    Hide: _Callable[[],
                    _type.HRESULT]
    TryInvokeKeyboardAccelerator: _Callable[[_Microsoft_UI_Xaml_Input.IProcessKeyboardAcceleratorEventArgs],  # args
                                            _type.HRESULT]


class IFlyoutBase2(_inspectable.IInspectable):
    get_SystemBackdrop: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.ISystemBackdrop]],  # value
                                  _type.HRESULT]
    put_SystemBackdrop: _Callable[[_Microsoft_UI_Xaml_Media.ISystemBackdrop],  # value
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
    CreatePresenter: _Callable[[_Pointer[_Microsoft_UI_Xaml_Controls.IControl]],  # result
                               _type.HRESULT]
    OnProcessKeyboardAccelerators: _Callable[[_Microsoft_UI_Xaml_Input.IProcessKeyboardAcceleratorEventArgs],  # args
                                             _type.HRESULT]


class IFlyoutBaseStatics(_inspectable.IInspectable, factory=True):
    get_TargetProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_PlacementProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_AllowFocusOnInteractionProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_LightDismissOverlayModeProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_AllowFocusWhenDisabledProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]
    get_ShowModeProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_InputDevicePrefersPrimaryCommandsProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                             _type.HRESULT]
    get_AreOpenCloseAnimationsEnabledProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                         _type.HRESULT]
    get_ShouldConstrainToRootBoundsProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]
    get_ElementSoundModeProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_OverlayInputPassThroughElementProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                          _type.HRESULT]
    get_IsOpenProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_AttachedFlyoutProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    GetAttachedFlyout: _Callable[[_Microsoft_UI_Xaml.IFrameworkElement,  # element
                                  _Pointer[IFlyoutBase]],  # result
                                 _type.HRESULT]
    SetAttachedFlyout: _Callable[[_Microsoft_UI_Xaml.IFrameworkElement,  # element
                                  IFlyoutBase],  # value
                                 _type.HRESULT]
    ShowAttachedFlyout: _Callable[[_Microsoft_UI_Xaml.IFrameworkElement],  # flyoutOwner
                                  _type.HRESULT]


class IFlyoutBaseStatics2(_inspectable.IInspectable, factory=True):
    get_SystemBackdropProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]


class IFlyoutShowOptions(_inspectable.IInspectable):
    get_Position: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.Point]]],  # value
                            _type.HRESULT]
    put_Position: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    get_ExclusionRect: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.Rect]]],  # value
                                 _type.HRESULT]
    put_ExclusionRect: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.Rect]],  # value
                                 _type.HRESULT]
    get_ShowMode: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Controls.Primitives.FlyoutShowMode]],  # value
                            _type.HRESULT]
    put_ShowMode: _Callable[[_enum.Microsoft.UI.Xaml.Controls.Primitives.FlyoutShowMode],  # value
                            _type.HRESULT]
    get_Placement: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Controls.Primitives.FlyoutPlacementMode]],  # value
                             _type.HRESULT]
    put_Placement: _Callable[[_enum.Microsoft.UI.Xaml.Controls.Primitives.FlyoutPlacementMode],  # value
                             _type.HRESULT]


class IFlyoutShowOptionsFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IFlyoutShowOptions]],  # value
                              _type.HRESULT]


class IGeneratorPositionHelper(_inspectable.IInspectable):
    pass


class IGeneratorPositionHelperStatics(_inspectable.IInspectable, factory=True):
    FromIndexAndOffset: _Callable[[_type.INT32,  # index
                                   _type.INT32,  # offset
                                   _Pointer[_struct.Microsoft.UI.Xaml.Controls.Primitives.GeneratorPosition]],  # result
                                  _type.HRESULT]


class IGridViewItemPresenter(_inspectable.IInspectable):
    get_SelectionCheckMarkVisualEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                   _type.HRESULT]
    put_SelectionCheckMarkVisualEnabled: _Callable[[_type.boolean],  # value
                                                   _type.HRESULT]
    get_CheckHintBrush: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                  _type.HRESULT]
    put_CheckHintBrush: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                  _type.HRESULT]
    get_CheckSelectingBrush: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                       _type.HRESULT]
    put_CheckSelectingBrush: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                       _type.HRESULT]
    get_CheckBrush: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                              _type.HRESULT]
    put_CheckBrush: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                              _type.HRESULT]
    get_DragBackground: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                  _type.HRESULT]
    put_DragBackground: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                  _type.HRESULT]
    get_DragForeground: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                  _type.HRESULT]
    put_DragForeground: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                  _type.HRESULT]
    get_FocusBorderBrush: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                    _type.HRESULT]
    put_FocusBorderBrush: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                    _type.HRESULT]
    get_PlaceholderBackground: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                         _type.HRESULT]
    put_PlaceholderBackground: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                         _type.HRESULT]
    get_PointerOverBackground: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                         _type.HRESULT]
    put_PointerOverBackground: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                         _type.HRESULT]
    get_SelectedBackground: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                      _type.HRESULT]
    put_SelectedBackground: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                      _type.HRESULT]
    get_SelectedForeground: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                      _type.HRESULT]
    put_SelectedForeground: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                      _type.HRESULT]
    get_SelectedPointerOverBackground: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                                 _type.HRESULT]
    put_SelectedPointerOverBackground: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                                 _type.HRESULT]
    get_SelectedPointerOverBorderBrush: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                                  _type.HRESULT]
    put_SelectedPointerOverBorderBrush: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                                  _type.HRESULT]
    get_SelectedBorderThickness: _Callable[[_Pointer[_struct.Microsoft.UI.Xaml.Thickness]],  # value
                                           _type.HRESULT]
    put_SelectedBorderThickness: _Callable[[_struct.Microsoft.UI.Xaml.Thickness],  # value
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
    GridViewItemPresenterHorizontalContentAlignment: _Callable[[_enum.Microsoft.UI.Xaml.HorizontalAlignment],  # value
                                                               _type.HRESULT]
    GridViewItemPresenterVerticalContentAlignment: _Callable[[_enum.Microsoft.UI.Xaml.VerticalAlignment],  # value
                                                             _type.HRESULT]
    GridViewItemPresenterPadding: _Callable[[_struct.Microsoft.UI.Xaml.Thickness],  # value
                                            _type.HRESULT]
    get_PointerOverBackgroundMargin: _Callable[[_Pointer[_struct.Microsoft.UI.Xaml.Thickness]],  # value
                                               _type.HRESULT]
    put_PointerOverBackgroundMargin: _Callable[[_struct.Microsoft.UI.Xaml.Thickness],  # value
                                               _type.HRESULT]
    get_ContentMargin: _Callable[[_Pointer[_struct.Microsoft.UI.Xaml.Thickness]],  # value
                                 _type.HRESULT]
    put_ContentMargin: _Callable[[_struct.Microsoft.UI.Xaml.Thickness],  # value
                                 _type.HRESULT]


class IGridViewItemPresenterFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IGridViewItemPresenter]],  # value
                              _type.HRESULT]


class IGridViewItemPresenterStatics(_inspectable.IInspectable, factory=True):
    get_SelectionCheckMarkVisualEnabledProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                           _type.HRESULT]
    get_CheckHintBrushProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_CheckSelectingBrushProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_CheckBrushProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_DragBackgroundProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_DragForegroundProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_FocusBorderBrushProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_PlaceholderBackgroundProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_PointerOverBackgroundProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_SelectedBackgroundProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_SelectedForegroundProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_SelectedPointerOverBackgroundProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                         _type.HRESULT]
    get_SelectedPointerOverBorderBrushProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                          _type.HRESULT]
    get_SelectedBorderThicknessProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_DisabledOpacityProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_DragOpacityProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_ReorderHintOffsetProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    GridViewItemPresenterHorizontalContentAlignmentProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                                       _type.HRESULT]
    GridViewItemPresenterVerticalContentAlignmentProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                                     _type.HRESULT]
    GridViewItemPresenterPaddingProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]
    get_PointerOverBackgroundMarginProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]
    get_ContentMarginProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]


class IGridViewItemTemplateSettings(_inspectable.IInspectable):
    get_DragItemsCount: _Callable[[_Pointer[_type.INT32]],  # value
                                  _type.HRESULT]


class IInfoBarPanel(_inspectable.IInspectable):
    get_HorizontalOrientationPadding: _Callable[[_Pointer[_struct.Microsoft.UI.Xaml.Thickness]],  # value
                                                _type.HRESULT]
    put_HorizontalOrientationPadding: _Callable[[_struct.Microsoft.UI.Xaml.Thickness],  # value
                                                _type.HRESULT]
    get_VerticalOrientationPadding: _Callable[[_Pointer[_struct.Microsoft.UI.Xaml.Thickness]],  # value
                                              _type.HRESULT]
    put_VerticalOrientationPadding: _Callable[[_struct.Microsoft.UI.Xaml.Thickness],  # value
                                              _type.HRESULT]


class IInfoBarPanelFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IInfoBarPanel]],  # value
                              _type.HRESULT]


class IInfoBarPanelStatics(_inspectable.IInspectable, factory=True):
    get_HorizontalOrientationPaddingProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                        _type.HRESULT]
    get_VerticalOrientationPaddingProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                      _type.HRESULT]
    SetHorizontalOrientationMargin: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # object
                                               _struct.Microsoft.UI.Xaml.Thickness],  # value
                                              _type.HRESULT]
    GetHorizontalOrientationMargin: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # object
                                               _Pointer[_struct.Microsoft.UI.Xaml.Thickness]],  # result
                                              _type.HRESULT]
    get_HorizontalOrientationMarginProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]
    SetVerticalOrientationMargin: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # object
                                             _struct.Microsoft.UI.Xaml.Thickness],  # value
                                            _type.HRESULT]
    GetVerticalOrientationMargin: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # object
                                             _Pointer[_struct.Microsoft.UI.Xaml.Thickness]],  # result
                                            _type.HRESULT]
    get_VerticalOrientationMarginProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                     _type.HRESULT]


class IItemsChangedEventArgs(_inspectable.IInspectable):
    get_Action: _Callable[[_Pointer[_type.INT32]],  # value
                          _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Microsoft.UI.Xaml.Controls.Primitives.GeneratorPosition]],  # value
                            _type.HRESULT]
    get_OldPosition: _Callable[[_Pointer[_struct.Microsoft.UI.Xaml.Controls.Primitives.GeneratorPosition]],  # value
                               _type.HRESULT]
    get_ItemCount: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]
    get_ItemUICount: _Callable[[_Pointer[_type.INT32]],  # value
                               _type.HRESULT]


class IJumpListItemBackgroundConverter(_inspectable.IInspectable):
    get_Enabled: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                           _type.HRESULT]
    put_Enabled: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                           _type.HRESULT]
    get_Disabled: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                            _type.HRESULT]
    put_Disabled: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                            _type.HRESULT]


class IJumpListItemBackgroundConverterStatics(_inspectable.IInspectable, factory=True):
    get_EnabledProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_DisabledProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]


class IJumpListItemForegroundConverter(_inspectable.IInspectable):
    get_Enabled: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                           _type.HRESULT]
    put_Enabled: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                           _type.HRESULT]
    get_Disabled: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                            _type.HRESULT]
    put_Disabled: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                            _type.HRESULT]


class IJumpListItemForegroundConverterStatics(_inspectable.IInspectable, factory=True):
    get_EnabledProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_DisabledProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]


class ILayoutInformation(_inspectable.IInspectable):
    pass


class ILayoutInformationStatics(_inspectable.IInspectable, factory=True):
    GetLayoutExceptionElement: _Callable[[_inspectable.IInspectable,  # dispatcher
                                          _Pointer[_Microsoft_UI_Xaml.IUIElement]],  # result
                                         _type.HRESULT]
    GetLayoutSlot: _Callable[[_Microsoft_UI_Xaml.IFrameworkElement,  # element
                              _Pointer[_struct.Windows.Foundation.Rect]],  # result
                             _type.HRESULT]
    GetAvailableSize: _Callable[[_Microsoft_UI_Xaml.IUIElement,  # element
                                 _Pointer[_struct.Windows.Foundation.Size]],  # result
                                _type.HRESULT]


class IListViewItemPresenter(_inspectable.IInspectable):
    get_SelectionCheckMarkVisualEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                   _type.HRESULT]
    put_SelectionCheckMarkVisualEnabled: _Callable[[_type.boolean],  # value
                                                   _type.HRESULT]
    get_CheckHintBrush: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                  _type.HRESULT]
    put_CheckHintBrush: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                  _type.HRESULT]
    get_CheckSelectingBrush: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                       _type.HRESULT]
    put_CheckSelectingBrush: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                       _type.HRESULT]
    get_CheckBrush: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                              _type.HRESULT]
    put_CheckBrush: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                              _type.HRESULT]
    get_DragBackground: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                  _type.HRESULT]
    put_DragBackground: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                  _type.HRESULT]
    get_DragForeground: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                  _type.HRESULT]
    put_DragForeground: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                  _type.HRESULT]
    get_FocusBorderBrush: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                    _type.HRESULT]
    put_FocusBorderBrush: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                    _type.HRESULT]
    get_PlaceholderBackground: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                         _type.HRESULT]
    put_PlaceholderBackground: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                         _type.HRESULT]
    get_PointerOverBackground: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                         _type.HRESULT]
    put_PointerOverBackground: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                         _type.HRESULT]
    get_SelectedBackground: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                      _type.HRESULT]
    put_SelectedBackground: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                      _type.HRESULT]
    get_SelectedForeground: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                      _type.HRESULT]
    put_SelectedForeground: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                      _type.HRESULT]
    get_SelectedPointerOverBackground: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                                 _type.HRESULT]
    put_SelectedPointerOverBackground: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                                 _type.HRESULT]
    get_SelectedPointerOverBorderBrush: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                                  _type.HRESULT]
    put_SelectedPointerOverBorderBrush: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                                  _type.HRESULT]
    get_SelectedBorderThickness: _Callable[[_Pointer[_struct.Microsoft.UI.Xaml.Thickness]],  # value
                                           _type.HRESULT]
    put_SelectedBorderThickness: _Callable[[_struct.Microsoft.UI.Xaml.Thickness],  # value
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
    ListViewItemPresenterHorizontalContentAlignment: _Callable[[_enum.Microsoft.UI.Xaml.HorizontalAlignment],  # value
                                                               _type.HRESULT]
    ListViewItemPresenterVerticalContentAlignment: _Callable[[_enum.Microsoft.UI.Xaml.VerticalAlignment],  # value
                                                             _type.HRESULT]
    ListViewItemPresenterPadding: _Callable[[_struct.Microsoft.UI.Xaml.Thickness],  # value
                                            _type.HRESULT]
    get_PointerOverBackgroundMargin: _Callable[[_Pointer[_struct.Microsoft.UI.Xaml.Thickness]],  # value
                                               _type.HRESULT]
    put_PointerOverBackgroundMargin: _Callable[[_struct.Microsoft.UI.Xaml.Thickness],  # value
                                               _type.HRESULT]
    get_ContentMargin: _Callable[[_Pointer[_struct.Microsoft.UI.Xaml.Thickness]],  # value
                                 _type.HRESULT]
    put_ContentMargin: _Callable[[_struct.Microsoft.UI.Xaml.Thickness],  # value
                                 _type.HRESULT]
    get_SelectedPressedBackground: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                             _type.HRESULT]
    put_SelectedPressedBackground: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                             _type.HRESULT]
    get_PressedBackground: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                     _type.HRESULT]
    put_PressedBackground: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                     _type.HRESULT]
    get_CheckBoxBrush: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                 _type.HRESULT]
    put_CheckBoxBrush: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                 _type.HRESULT]
    get_FocusSecondaryBorderBrush: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                             _type.HRESULT]
    put_FocusSecondaryBorderBrush: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                             _type.HRESULT]
    get_CheckMode: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Controls.Primitives.ListViewItemPresenterCheckMode]],  # value
                             _type.HRESULT]
    put_CheckMode: _Callable[[_enum.Microsoft.UI.Xaml.Controls.Primitives.ListViewItemPresenterCheckMode],  # value
                             _type.HRESULT]
    get_PointerOverForeground: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                         _type.HRESULT]
    put_PointerOverForeground: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                         _type.HRESULT]
    get_RevealBackground: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                    _type.HRESULT]
    put_RevealBackground: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                    _type.HRESULT]
    get_RevealBorderBrush: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                     _type.HRESULT]
    put_RevealBorderBrush: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                     _type.HRESULT]
    get_RevealBorderThickness: _Callable[[_Pointer[_struct.Microsoft.UI.Xaml.Thickness]],  # value
                                         _type.HRESULT]
    put_RevealBorderThickness: _Callable[[_struct.Microsoft.UI.Xaml.Thickness],  # value
                                         _type.HRESULT]
    get_RevealBackgroundShowsAboveContent: _Callable[[_Pointer[_type.boolean]],  # value
                                                     _type.HRESULT]
    put_RevealBackgroundShowsAboveContent: _Callable[[_type.boolean],  # value
                                                     _type.HRESULT]
    get_SelectedDisabledBackground: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                              _type.HRESULT]
    put_SelectedDisabledBackground: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                              _type.HRESULT]
    get_CheckPressedBrush: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                     _type.HRESULT]
    put_CheckPressedBrush: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                     _type.HRESULT]
    get_CheckDisabledBrush: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                      _type.HRESULT]
    put_CheckDisabledBrush: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                      _type.HRESULT]
    get_CheckBoxPointerOverBrush: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                            _type.HRESULT]
    put_CheckBoxPointerOverBrush: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                            _type.HRESULT]
    get_CheckBoxPressedBrush: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                        _type.HRESULT]
    put_CheckBoxPressedBrush: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                        _type.HRESULT]
    get_CheckBoxDisabledBrush: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                         _type.HRESULT]
    put_CheckBoxDisabledBrush: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                         _type.HRESULT]
    get_CheckBoxSelectedBrush: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                         _type.HRESULT]
    put_CheckBoxSelectedBrush: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                         _type.HRESULT]
    get_CheckBoxSelectedPointerOverBrush: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                                    _type.HRESULT]
    put_CheckBoxSelectedPointerOverBrush: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                                    _type.HRESULT]
    get_CheckBoxSelectedPressedBrush: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                                _type.HRESULT]
    put_CheckBoxSelectedPressedBrush: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                                _type.HRESULT]
    get_CheckBoxSelectedDisabledBrush: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                                 _type.HRESULT]
    put_CheckBoxSelectedDisabledBrush: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                                 _type.HRESULT]
    get_CheckBoxBorderBrush: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                       _type.HRESULT]
    put_CheckBoxBorderBrush: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                       _type.HRESULT]
    get_CheckBoxPointerOverBorderBrush: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                                  _type.HRESULT]
    put_CheckBoxPointerOverBorderBrush: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                                  _type.HRESULT]
    get_CheckBoxPressedBorderBrush: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                              _type.HRESULT]
    put_CheckBoxPressedBorderBrush: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                              _type.HRESULT]
    get_CheckBoxDisabledBorderBrush: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                               _type.HRESULT]
    put_CheckBoxDisabledBorderBrush: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                               _type.HRESULT]
    get_CheckBoxCornerRadius: _Callable[[_Pointer[_struct.Microsoft.UI.Xaml.CornerRadius]],  # value
                                        _type.HRESULT]
    put_CheckBoxCornerRadius: _Callable[[_struct.Microsoft.UI.Xaml.CornerRadius],  # value
                                        _type.HRESULT]
    get_SelectionIndicatorCornerRadius: _Callable[[_Pointer[_struct.Microsoft.UI.Xaml.CornerRadius]],  # value
                                                  _type.HRESULT]
    put_SelectionIndicatorCornerRadius: _Callable[[_struct.Microsoft.UI.Xaml.CornerRadius],  # value
                                                  _type.HRESULT]
    get_SelectionIndicatorVisualEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                   _type.HRESULT]
    put_SelectionIndicatorVisualEnabled: _Callable[[_type.boolean],  # value
                                                   _type.HRESULT]
    get_SelectionIndicatorMode: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Controls.Primitives.ListViewItemPresenterSelectionIndicatorMode]],  # value
                                          _type.HRESULT]
    put_SelectionIndicatorMode: _Callable[[_enum.Microsoft.UI.Xaml.Controls.Primitives.ListViewItemPresenterSelectionIndicatorMode],  # value
                                          _type.HRESULT]
    get_SelectionIndicatorBrush: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                           _type.HRESULT]
    put_SelectionIndicatorBrush: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                           _type.HRESULT]
    get_SelectionIndicatorPointerOverBrush: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                                      _type.HRESULT]
    put_SelectionIndicatorPointerOverBrush: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                                      _type.HRESULT]
    get_SelectionIndicatorPressedBrush: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                                  _type.HRESULT]
    put_SelectionIndicatorPressedBrush: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                                  _type.HRESULT]
    get_SelectionIndicatorDisabledBrush: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                                   _type.HRESULT]
    put_SelectionIndicatorDisabledBrush: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                                   _type.HRESULT]
    get_SelectedBorderBrush: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                       _type.HRESULT]
    put_SelectedBorderBrush: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                       _type.HRESULT]
    get_SelectedPressedBorderBrush: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                              _type.HRESULT]
    put_SelectedPressedBorderBrush: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                              _type.HRESULT]
    get_SelectedDisabledBorderBrush: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                               _type.HRESULT]
    put_SelectedDisabledBorderBrush: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                               _type.HRESULT]
    get_SelectedInnerBorderBrush: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                            _type.HRESULT]
    put_SelectedInnerBorderBrush: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                            _type.HRESULT]
    get_PointerOverBorderBrush: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                                          _type.HRESULT]
    put_PointerOverBorderBrush: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                                          _type.HRESULT]


class IListViewItemPresenterFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IListViewItemPresenter]],  # value
                              _type.HRESULT]


class IListViewItemPresenterStatics(_inspectable.IInspectable, factory=True):
    get_SelectionCheckMarkVisualEnabledProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                           _type.HRESULT]
    get_CheckHintBrushProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_CheckSelectingBrushProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_CheckBrushProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_DragBackgroundProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_DragForegroundProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_FocusBorderBrushProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_PlaceholderBackgroundProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_PointerOverBackgroundProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_SelectedBackgroundProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_SelectedForegroundProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_SelectedPointerOverBackgroundProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                         _type.HRESULT]
    get_SelectedPointerOverBorderBrushProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                          _type.HRESULT]
    get_SelectedBorderThicknessProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_DisabledOpacityProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_DragOpacityProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_ReorderHintOffsetProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    ListViewItemPresenterHorizontalContentAlignmentProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                                       _type.HRESULT]
    ListViewItemPresenterVerticalContentAlignmentProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                                     _type.HRESULT]
    ListViewItemPresenterPaddingProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]
    get_PointerOverBackgroundMarginProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]
    get_ContentMarginProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_SelectedPressedBackgroundProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                     _type.HRESULT]
    get_PressedBackgroundProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_CheckBoxBrushProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_FocusSecondaryBorderBrushProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                     _type.HRESULT]
    get_CheckModeProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_PointerOverForegroundProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_RevealBackgroundProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_RevealBorderBrushProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_RevealBorderThicknessProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_RevealBackgroundShowsAboveContentProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                             _type.HRESULT]
    get_SelectedDisabledBackgroundProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                      _type.HRESULT]
    get_CheckPressedBrushProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_CheckDisabledBrushProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_CheckBoxPointerOverBrushProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]
    get_CheckBoxPressedBrushProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_CheckBoxDisabledBrushProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_CheckBoxSelectedBrushProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_CheckBoxSelectedPointerOverBrushProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                            _type.HRESULT]
    get_CheckBoxSelectedPressedBrushProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                        _type.HRESULT]
    get_CheckBoxSelectedDisabledBrushProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                         _type.HRESULT]
    get_CheckBoxBorderBrushProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_CheckBoxPointerOverBorderBrushProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                          _type.HRESULT]
    get_CheckBoxPressedBorderBrushProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                      _type.HRESULT]
    get_CheckBoxDisabledBorderBrushProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]
    get_CheckBoxCornerRadiusProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_SelectionIndicatorCornerRadiusProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                          _type.HRESULT]
    get_SelectionIndicatorVisualEnabledProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                           _type.HRESULT]
    get_SelectionIndicatorModeProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]
    get_SelectionIndicatorBrushProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_SelectionIndicatorPointerOverBrushProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                              _type.HRESULT]
    get_SelectionIndicatorPressedBrushProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                          _type.HRESULT]
    get_SelectionIndicatorDisabledBrushProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                           _type.HRESULT]
    get_SelectedBorderBrushProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_SelectedPressedBorderBrushProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                      _type.HRESULT]
    get_SelectedDisabledBorderBrushProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]
    get_SelectedInnerBorderBrushProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]
    get_PointerOverBorderBrushProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]


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
    get_ItemTemplate: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDataTemplate]],  # value
                                _type.HRESULT]
    put_ItemTemplate: _Callable[[_Microsoft_UI_Xaml.IDataTemplate],  # value
                                _type.HRESULT]
    add_SelectionChanged: _Callable[[_Microsoft_UI_Xaml_Controls.ISelectionChangedEventHandler,  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_SelectionChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]


class ILoopingSelectorItem(_inspectable.IInspectable):
    pass


class ILoopingSelectorPanel(_inspectable.IInspectable):
    pass


class ILoopingSelectorStatics(_inspectable.IInspectable, factory=True):
    get_ShouldLoopProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_ItemsProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_SelectedIndexProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_SelectedItemProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_ItemWidthProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_ItemHeightProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_ItemTemplateProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]


class IMenuFlyoutItemTemplateSettings(_inspectable.IInspectable):
    get_KeyboardAcceleratorTextMinWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                   _type.HRESULT]


class IMenuFlyoutPresenterTemplateSettings(_inspectable.IInspectable):
    get_FlyoutContentMinWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                         _type.HRESULT]


class IMonochromaticOverlayPresenter(_inspectable.IInspectable):
    get_SourceElement: _Callable[[_Pointer[_Microsoft_UI_Xaml.IUIElement]],  # value
                                 _type.HRESULT]
    put_SourceElement: _Callable[[_Microsoft_UI_Xaml.IUIElement],  # value
                                 _type.HRESULT]
    get_ReplacementColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                    _type.HRESULT]
    put_ReplacementColor: _Callable[[_struct.Windows.UI.Color],  # value
                                    _type.HRESULT]


class IMonochromaticOverlayPresenterFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IMonochromaticOverlayPresenter]],  # value
                              _type.HRESULT]


class IMonochromaticOverlayPresenterStatics(_inspectable.IInspectable, factory=True):
    get_SourceElementProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_ReplacementColorProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]


class INavigationViewItemPresenter(_inspectable.IInspectable):
    get_Icon: _Callable[[_Pointer[_Microsoft_UI_Xaml_Controls.IIconElement]],  # value
                        _type.HRESULT]
    put_Icon: _Callable[[_Microsoft_UI_Xaml_Controls.IIconElement],  # value
                        _type.HRESULT]
    get_TemplateSettings: _Callable[[_Pointer[INavigationViewItemPresenterTemplateSettings]],  # value
                                    _type.HRESULT]


class INavigationViewItemPresenter2(_inspectable.IInspectable):
    get_InfoBadge: _Callable[[_Pointer[_Microsoft_UI_Xaml_Controls.IInfoBadge]],  # value
                             _type.HRESULT]
    put_InfoBadge: _Callable[[_Microsoft_UI_Xaml_Controls.IInfoBadge],  # value
                             _type.HRESULT]


class INavigationViewItemPresenterFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[INavigationViewItemPresenter]],  # value
                              _type.HRESULT]


class INavigationViewItemPresenterStatics(_inspectable.IInspectable, factory=True):
    get_IconProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]
    get_TemplateSettingsProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]


class INavigationViewItemPresenterStatics2(_inspectable.IInspectable, factory=True):
    get_InfoBadgeProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]


class INavigationViewItemPresenterTemplateSettings(_inspectable.IInspectable):
    get_IconWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                             _type.HRESULT]
    get_SmallerIconWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]


class INavigationViewItemPresenterTemplateSettingsFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[INavigationViewItemPresenterTemplateSettings]],  # value
                              _type.HRESULT]


class INavigationViewItemPresenterTemplateSettingsStatics(_inspectable.IInspectable, factory=True):
    get_IconWidthProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_SmallerIconWidthProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]


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
    MakeVisible: _Callable[[_Microsoft_UI_Xaml.IUIElement,  # visual
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


class IPickerFlyoutBaseStatics(_inspectable.IInspectable, factory=True):
    get_TitleProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    GetTitle: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                         _Pointer[_type.HSTRING]],  # result
                        _type.HRESULT]
    SetTitle: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                         _type.HSTRING],  # value
                        _type.HRESULT]


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
    get_Child: _Callable[[_Pointer[_Microsoft_UI_Xaml.IUIElement]],  # value
                         _type.HRESULT]
    put_Child: _Callable[[_Microsoft_UI_Xaml.IUIElement],  # value
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
    get_ChildTransitions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Microsoft_UI_Xaml_Media_Animation.ITransition]]],  # value
                                    _type.HRESULT]
    put_ChildTransitions: _Callable[[_Windows_Foundation_Collections.IVector[_Microsoft_UI_Xaml_Media_Animation.ITransition]],  # value
                                    _type.HRESULT]
    get_IsLightDismissEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_IsLightDismissEnabled: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]
    get_LightDismissOverlayMode: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Controls.LightDismissOverlayMode]],  # value
                                           _type.HRESULT]
    put_LightDismissOverlayMode: _Callable[[_enum.Microsoft.UI.Xaml.Controls.LightDismissOverlayMode],  # value
                                           _type.HRESULT]
    get_ShouldConstrainToRootBounds: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]
    put_ShouldConstrainToRootBounds: _Callable[[_type.boolean],  # value
                                               _type.HRESULT]
    get_IsConstrainedToRootBounds: _Callable[[_Pointer[_type.boolean]],  # value
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
    get_PlacementTarget: _Callable[[_Pointer[_Microsoft_UI_Xaml.IFrameworkElement]],  # value
                                   _type.HRESULT]
    put_PlacementTarget: _Callable[[_Microsoft_UI_Xaml.IFrameworkElement],  # value
                                   _type.HRESULT]
    get_DesiredPlacement: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Controls.Primitives.PopupPlacementMode]],  # value
                                    _type.HRESULT]
    put_DesiredPlacement: _Callable[[_enum.Microsoft.UI.Xaml.Controls.Primitives.PopupPlacementMode],  # value
                                    _type.HRESULT]
    get_ActualPlacement: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Controls.Primitives.PopupPlacementMode]],  # value
                                   _type.HRESULT]
    add_ActualPlacementChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_ActualPlacementChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]


class IPopup3(_inspectable.IInspectable):
    get_SystemBackdrop: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.ISystemBackdrop]],  # value
                                  _type.HRESULT]
    put_SystemBackdrop: _Callable[[_Microsoft_UI_Xaml_Media.ISystemBackdrop],  # value
                                  _type.HRESULT]


class IPopupStatics(_inspectable.IInspectable, factory=True):
    get_ChildProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_IsOpenProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_HorizontalOffsetProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_VerticalOffsetProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_ChildTransitionsProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_IsLightDismissEnabledProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_LightDismissOverlayModeProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_ShouldConstrainToRootBoundsProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]


class IPopupStatics2(_inspectable.IInspectable, factory=True):
    get_PlacementTargetProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_DesiredPlacementProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]


class IPopupStatics3(_inspectable.IInspectable, factory=True):
    get_SystemBackdropProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
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


class IRangeBaseStatics(_inspectable.IInspectable, factory=True):
    get_MinimumProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_MaximumProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_SmallChangeProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_LargeChangeProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_ValueProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]


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


class IRepeatButtonStatics(_inspectable.IInspectable, factory=True):
    get_DelayProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_IntervalProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]


class IRepeatedScrollSnapPoint(_inspectable.IInspectable):
    get_Offset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                          _type.HRESULT]
    get_Interval: _Callable[[_Pointer[_type.DOUBLE]],  # value
                            _type.HRESULT]
    get_Start: _Callable[[_Pointer[_type.DOUBLE]],  # value
                         _type.HRESULT]
    get_End: _Callable[[_Pointer[_type.DOUBLE]],  # value
                       _type.HRESULT]


class IRepeatedScrollSnapPointFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_type.DOUBLE,  # offset
                               _type.DOUBLE,  # interval
                               _type.DOUBLE,  # start
                               _type.DOUBLE,  # end
                               _enum.Microsoft.UI.Xaml.Controls.Primitives.ScrollSnapPointsAlignment,  # alignment
                               _inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IRepeatedScrollSnapPoint]],  # value
                              _type.HRESULT]


class IRepeatedZoomSnapPoint(_inspectable.IInspectable):
    get_Offset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                          _type.HRESULT]
    get_Interval: _Callable[[_Pointer[_type.DOUBLE]],  # value
                            _type.HRESULT]
    get_Start: _Callable[[_Pointer[_type.DOUBLE]],  # value
                         _type.HRESULT]
    get_End: _Callable[[_Pointer[_type.DOUBLE]],  # value
                       _type.HRESULT]


class IRepeatedZoomSnapPointFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_type.DOUBLE,  # offset
                               _type.DOUBLE,  # interval
                               _type.DOUBLE,  # start
                               _type.DOUBLE,  # end
                               _inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IRepeatedZoomSnapPoint]],  # value
                              _type.HRESULT]


class IScrollBar(_inspectable.IInspectable):
    get_Orientation: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Controls.Orientation]],  # value
                               _type.HRESULT]
    put_Orientation: _Callable[[_enum.Microsoft.UI.Xaml.Controls.Orientation],  # value
                               _type.HRESULT]
    get_ViewportSize: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    put_ViewportSize: _Callable[[_type.DOUBLE],  # value
                                _type.HRESULT]
    get_IndicatorMode: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Controls.Primitives.ScrollingIndicatorMode]],  # value
                                 _type.HRESULT]
    put_IndicatorMode: _Callable[[_enum.Microsoft.UI.Xaml.Controls.Primitives.ScrollingIndicatorMode],  # value
                                 _type.HRESULT]
    add_Scroll: _Callable[[IScrollEventHandler,  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Scroll: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]


class IScrollBarStatics(_inspectable.IInspectable, factory=True):
    get_OrientationProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_ViewportSizeProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_IndicatorModeProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]


class IScrollController(_inspectable.IInspectable):
    get_PanningInfo: _Callable[[_Pointer[IScrollControllerPanningInfo]],  # value
                               _type.HRESULT]
    get_CanScroll: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_IsScrollingWithMouse: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    SetIsScrollable: _Callable[[_type.boolean],  # isScrollable
                               _type.HRESULT]
    SetValues: _Callable[[_type.DOUBLE,  # minOffset
                          _type.DOUBLE,  # maxOffset
                          _type.DOUBLE,  # offset
                          _type.DOUBLE],  # viewportLength
                         _type.HRESULT]
    GetScrollAnimation: _Callable[[_type.INT32,  # correlationId
                                   _struct.Windows.Foundation.Numerics.Vector2,  # startPosition
                                   _struct.Windows.Foundation.Numerics.Vector2,  # endPosition
                                   _Microsoft_UI_Composition.ICompositionAnimation,  # defaultAnimation
                                   _Pointer[_Microsoft_UI_Composition.ICompositionAnimation]],  # result
                                  _type.HRESULT]
    NotifyRequestedScrollCompleted: _Callable[[_type.INT32],  # correlationId
                                              _type.HRESULT]
    add_CanScrollChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IScrollController, _inspectable.IInspectable],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_CanScrollChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    add_IsScrollingWithMouseChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IScrollController, _inspectable.IInspectable],  # handler
                                                _Pointer[_struct.EventRegistrationToken]],  # token
                                               _type.HRESULT]
    remove_IsScrollingWithMouseChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                  _type.HRESULT]
    add_ScrollToRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IScrollController, IScrollControllerScrollToRequestedEventArgs],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_ScrollToRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    add_ScrollByRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IScrollController, IScrollControllerScrollByRequestedEventArgs],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_ScrollByRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    add_AddScrollVelocityRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IScrollController, IScrollControllerAddScrollVelocityRequestedEventArgs],  # handler
                                               _Pointer[_struct.EventRegistrationToken]],  # token
                                              _type.HRESULT]
    remove_AddScrollVelocityRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                 _type.HRESULT]


class IScrollControllerAddScrollVelocityRequestedEventArgs(_inspectable.IInspectable):
    get_OffsetVelocity: _Callable[[_Pointer[_type.FLOAT]],  # value
                                  _type.HRESULT]
    get_InertiaDecayRate: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.FLOAT]]],  # value
                                    _type.HRESULT]
    get_CorrelationId: _Callable[[_Pointer[_type.INT32]],  # value
                                 _type.HRESULT]
    put_CorrelationId: _Callable[[_type.INT32],  # value
                                 _type.HRESULT]


class IScrollControllerAddScrollVelocityRequestedEventArgsFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[_type.FLOAT,  # offsetVelocity
                               _Windows_Foundation.IReference[_type.FLOAT],  # inertiaDecayRate
                               _Pointer[IScrollControllerAddScrollVelocityRequestedEventArgs]],  # value
                              _type.HRESULT]


class IScrollControllerPanRequestedEventArgs(_inspectable.IInspectable):
    get_PointerPoint: _Callable[[_Pointer[_Microsoft_UI_Input.IPointerPoint]],  # value
                                _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class IScrollControllerPanRequestedEventArgsFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[_Microsoft_UI_Input.IPointerPoint,  # pointerPoint
                               _Pointer[IScrollControllerPanRequestedEventArgs]],  # value
                              _type.HRESULT]


class IScrollControllerPanningInfo(_inspectable.IInspectable):
    get_IsRailEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_PanOrientation: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Controls.Orientation]],  # value
                                  _type.HRESULT]
    get_PanningElementAncestor: _Callable[[_Pointer[_Microsoft_UI_Xaml.IUIElement]],  # value
                                          _type.HRESULT]
    SetPanningElementExpressionAnimationSources: _Callable[[_Microsoft_UI_Composition.ICompositionPropertySet,  # propertySet
                                                            _type.HSTRING,  # minOffsetPropertyName
                                                            _type.HSTRING,  # maxOffsetPropertyName
                                                            _type.HSTRING,  # offsetPropertyName
                                                            _type.HSTRING],  # multiplierPropertyName
                                                           _type.HRESULT]
    add_Changed: _Callable[[_Windows_Foundation.ITypedEventHandler[IScrollControllerPanningInfo, _inspectable.IInspectable],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Changed: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_PanRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IScrollControllerPanningInfo, IScrollControllerPanRequestedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_PanRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]


class IScrollControllerScrollByRequestedEventArgs(_inspectable.IInspectable):
    get_OffsetDelta: _Callable[[_Pointer[_type.DOUBLE]],  # value
                               _type.HRESULT]
    get_Options: _Callable[[_Pointer[_Microsoft_UI_Xaml_Controls.IScrollingScrollOptions]],  # value
                           _type.HRESULT]
    get_CorrelationId: _Callable[[_Pointer[_type.INT32]],  # value
                                 _type.HRESULT]
    put_CorrelationId: _Callable[[_type.INT32],  # value
                                 _type.HRESULT]


class IScrollControllerScrollByRequestedEventArgsFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[_type.DOUBLE,  # offsetDelta
                               _Microsoft_UI_Xaml_Controls.IScrollingScrollOptions,  # options
                               _Pointer[IScrollControllerScrollByRequestedEventArgs]],  # value
                              _type.HRESULT]


class IScrollControllerScrollToRequestedEventArgs(_inspectable.IInspectable):
    get_Offset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                          _type.HRESULT]
    get_Options: _Callable[[_Pointer[_Microsoft_UI_Xaml_Controls.IScrollingScrollOptions]],  # value
                           _type.HRESULT]
    get_CorrelationId: _Callable[[_Pointer[_type.INT32]],  # value
                                 _type.HRESULT]
    put_CorrelationId: _Callable[[_type.INT32],  # value
                                 _type.HRESULT]


class IScrollControllerScrollToRequestedEventArgsFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[_type.DOUBLE,  # offset
                               _Microsoft_UI_Xaml_Controls.IScrollingScrollOptions,  # options
                               _Pointer[IScrollControllerScrollToRequestedEventArgs]],  # value
                              _type.HRESULT]


class IScrollEventArgs(_inspectable.IInspectable):
    get_NewValue: _Callable[[_Pointer[_type.DOUBLE]],  # value
                            _type.HRESULT]
    get_ScrollEventType: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Controls.Primitives.ScrollEventType]],  # value
                                   _type.HRESULT]


class IScrollPresenter(_inspectable.IInspectable):
    get_Background: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                              _type.HRESULT]
    put_Background: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                              _type.HRESULT]
    get_Content: _Callable[[_Pointer[_Microsoft_UI_Xaml.IUIElement]],  # value
                           _type.HRESULT]
    put_Content: _Callable[[_Microsoft_UI_Xaml.IUIElement],  # value
                           _type.HRESULT]
    get_ExpressionAnimationSources: _Callable[[_Pointer[_Microsoft_UI_Composition.ICompositionPropertySet]],  # value
                                              _type.HRESULT]
    get_HorizontalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]
    get_VerticalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    get_ZoomFactor: _Callable[[_Pointer[_type.FLOAT]],  # value
                              _type.HRESULT]
    get_ExtentWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                               _type.HRESULT]
    get_ExtentHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    get_ViewportWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                 _type.HRESULT]
    get_ViewportHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    get_ScrollableWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                   _type.HRESULT]
    get_ScrollableHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]
    get_ContentOrientation: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Controls.ScrollingContentOrientation]],  # value
                                      _type.HRESULT]
    put_ContentOrientation: _Callable[[_enum.Microsoft.UI.Xaml.Controls.ScrollingContentOrientation],  # value
                                      _type.HRESULT]
    get_HorizontalScrollChainMode: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Controls.ScrollingChainMode]],  # value
                                             _type.HRESULT]
    put_HorizontalScrollChainMode: _Callable[[_enum.Microsoft.UI.Xaml.Controls.ScrollingChainMode],  # value
                                             _type.HRESULT]
    get_VerticalScrollChainMode: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Controls.ScrollingChainMode]],  # value
                                           _type.HRESULT]
    put_VerticalScrollChainMode: _Callable[[_enum.Microsoft.UI.Xaml.Controls.ScrollingChainMode],  # value
                                           _type.HRESULT]
    get_HorizontalScrollRailMode: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Controls.ScrollingRailMode]],  # value
                                            _type.HRESULT]
    put_HorizontalScrollRailMode: _Callable[[_enum.Microsoft.UI.Xaml.Controls.ScrollingRailMode],  # value
                                            _type.HRESULT]
    get_VerticalScrollRailMode: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Controls.ScrollingRailMode]],  # value
                                          _type.HRESULT]
    put_VerticalScrollRailMode: _Callable[[_enum.Microsoft.UI.Xaml.Controls.ScrollingRailMode],  # value
                                          _type.HRESULT]
    get_HorizontalScrollMode: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Controls.ScrollingScrollMode]],  # value
                                        _type.HRESULT]
    put_HorizontalScrollMode: _Callable[[_enum.Microsoft.UI.Xaml.Controls.ScrollingScrollMode],  # value
                                        _type.HRESULT]
    get_VerticalScrollMode: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Controls.ScrollingScrollMode]],  # value
                                      _type.HRESULT]
    put_VerticalScrollMode: _Callable[[_enum.Microsoft.UI.Xaml.Controls.ScrollingScrollMode],  # value
                                      _type.HRESULT]
    get_ComputedHorizontalScrollMode: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Controls.ScrollingScrollMode]],  # value
                                                _type.HRESULT]
    get_ComputedVerticalScrollMode: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Controls.ScrollingScrollMode]],  # value
                                              _type.HRESULT]
    get_ZoomChainMode: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Controls.ScrollingChainMode]],  # value
                                 _type.HRESULT]
    put_ZoomChainMode: _Callable[[_enum.Microsoft.UI.Xaml.Controls.ScrollingChainMode],  # value
                                 _type.HRESULT]
    get_ZoomMode: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Controls.ScrollingZoomMode]],  # value
                            _type.HRESULT]
    put_ZoomMode: _Callable[[_enum.Microsoft.UI.Xaml.Controls.ScrollingZoomMode],  # value
                            _type.HRESULT]
    get_IgnoredInputKinds: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Controls.ScrollingInputKinds]],  # value
                                     _type.HRESULT]
    put_IgnoredInputKinds: _Callable[[_enum.Microsoft.UI.Xaml.Controls.ScrollingInputKinds],  # value
                                     _type.HRESULT]
    get_MinZoomFactor: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                 _type.HRESULT]
    put_MinZoomFactor: _Callable[[_type.DOUBLE],  # value
                                 _type.HRESULT]
    get_MaxZoomFactor: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                 _type.HRESULT]
    put_MaxZoomFactor: _Callable[[_type.DOUBLE],  # value
                                 _type.HRESULT]
    get_State: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Controls.ScrollingInteractionState]],  # value
                         _type.HRESULT]
    get_HorizontalScrollController: _Callable[[_Pointer[IScrollController]],  # value
                                              _type.HRESULT]
    put_HorizontalScrollController: _Callable[[IScrollController],  # value
                                              _type.HRESULT]
    get_VerticalScrollController: _Callable[[_Pointer[IScrollController]],  # value
                                            _type.HRESULT]
    put_VerticalScrollController: _Callable[[IScrollController],  # value
                                            _type.HRESULT]
    get_HorizontalAnchorRatio: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                         _type.HRESULT]
    put_HorizontalAnchorRatio: _Callable[[_type.DOUBLE],  # value
                                         _type.HRESULT]
    get_VerticalAnchorRatio: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                       _type.HRESULT]
    put_VerticalAnchorRatio: _Callable[[_type.DOUBLE],  # value
                                       _type.HRESULT]
    get_HorizontalSnapPoints: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IScrollSnapPointBase]]],  # value
                                        _type.HRESULT]
    get_VerticalSnapPoints: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IScrollSnapPointBase]]],  # value
                                      _type.HRESULT]
    get_ZoomSnapPoints: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IZoomSnapPointBase]]],  # value
                                  _type.HRESULT]
    ScrollTo: _Callable[[_type.DOUBLE,  # horizontalOffset
                         _type.DOUBLE,  # verticalOffset
                         _Pointer[_type.INT32]],  # result
                        _type.HRESULT]
    ScrollToWithOptions: _Callable[[_type.DOUBLE,  # horizontalOffset
                                    _type.DOUBLE,  # verticalOffset
                                    _Microsoft_UI_Xaml_Controls.IScrollingScrollOptions,  # options
                                    _Pointer[_type.INT32]],  # result
                                   _type.HRESULT]
    ScrollBy: _Callable[[_type.DOUBLE,  # horizontalOffsetDelta
                         _type.DOUBLE,  # verticalOffsetDelta
                         _Pointer[_type.INT32]],  # result
                        _type.HRESULT]
    ScrollByWithOptions: _Callable[[_type.DOUBLE,  # horizontalOffsetDelta
                                    _type.DOUBLE,  # verticalOffsetDelta
                                    _Microsoft_UI_Xaml_Controls.IScrollingScrollOptions,  # options
                                    _Pointer[_type.INT32]],  # result
                                   _type.HRESULT]
    AddScrollVelocity: _Callable[[_struct.Windows.Foundation.Numerics.Vector2,  # offsetsVelocity
                                  _Windows_Foundation.IReference[_struct.Windows.Foundation.Numerics.Vector2],  # inertiaDecayRate
                                  _Pointer[_type.INT32]],  # result
                                 _type.HRESULT]
    ZoomTo: _Callable[[_type.FLOAT,  # zoomFactor
                       _Windows_Foundation.IReference[_struct.Windows.Foundation.Numerics.Vector2],  # centerPoint
                       _Pointer[_type.INT32]],  # result
                      _type.HRESULT]
    ZoomToWithOptions: _Callable[[_type.FLOAT,  # zoomFactor
                                  _Windows_Foundation.IReference[_struct.Windows.Foundation.Numerics.Vector2],  # centerPoint
                                  _Microsoft_UI_Xaml_Controls.IScrollingZoomOptions,  # options
                                  _Pointer[_type.INT32]],  # result
                                 _type.HRESULT]
    ZoomBy: _Callable[[_type.FLOAT,  # zoomFactorDelta
                       _Windows_Foundation.IReference[_struct.Windows.Foundation.Numerics.Vector2],  # centerPoint
                       _Pointer[_type.INT32]],  # result
                      _type.HRESULT]
    ZoomByWithOptions: _Callable[[_type.FLOAT,  # zoomFactorDelta
                                  _Windows_Foundation.IReference[_struct.Windows.Foundation.Numerics.Vector2],  # centerPoint
                                  _Microsoft_UI_Xaml_Controls.IScrollingZoomOptions,  # options
                                  _Pointer[_type.INT32]],  # result
                                 _type.HRESULT]
    AddZoomVelocity: _Callable[[_type.FLOAT,  # zoomFactorVelocity
                                _Windows_Foundation.IReference[_struct.Windows.Foundation.Numerics.Vector2],  # centerPoint
                                _Windows_Foundation.IReference[_type.FLOAT],  # inertiaDecayRate
                                _Pointer[_type.INT32]],  # result
                               _type.HRESULT]
    add_ExtentChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IScrollPresenter, _inspectable.IInspectable],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_ExtentChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_StateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IScrollPresenter, _inspectable.IInspectable],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_StateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    add_ViewChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IScrollPresenter, _inspectable.IInspectable],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_ViewChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    add_ScrollAnimationStarting: _Callable[[_Windows_Foundation.ITypedEventHandler[IScrollPresenter, _Microsoft_UI_Xaml_Controls.IScrollingScrollAnimationStartingEventArgs],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_ScrollAnimationStarting: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]
    add_ZoomAnimationStarting: _Callable[[_Windows_Foundation.ITypedEventHandler[IScrollPresenter, _Microsoft_UI_Xaml_Controls.IScrollingZoomAnimationStartingEventArgs],  # handler
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_ZoomAnimationStarting: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]
    add_ScrollCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IScrollPresenter, _Microsoft_UI_Xaml_Controls.IScrollingScrollCompletedEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_ScrollCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    add_ZoomCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IScrollPresenter, _Microsoft_UI_Xaml_Controls.IScrollingZoomCompletedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_ZoomCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_BringingIntoView: _Callable[[_Windows_Foundation.ITypedEventHandler[IScrollPresenter, _Microsoft_UI_Xaml_Controls.IScrollingBringingIntoViewEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_BringingIntoView: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    add_AnchorRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IScrollPresenter, _Microsoft_UI_Xaml_Controls.IScrollingAnchorRequestedEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_AnchorRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]


class IScrollPresenterFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IScrollPresenter]],  # value
                              _type.HRESULT]


class IScrollPresenterStatics(_inspectable.IInspectable, factory=True):
    get_BackgroundProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_ContentProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_ContentOrientationProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_HorizontalScrollChainModeProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                     _type.HRESULT]
    get_VerticalScrollChainModeProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_HorizontalScrollRailModeProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]
    get_VerticalScrollRailModeProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]
    get_HorizontalScrollModeProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_VerticalScrollModeProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_ComputedHorizontalScrollModeProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                        _type.HRESULT]
    get_ComputedVerticalScrollModeProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                      _type.HRESULT]
    get_ZoomChainModeProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_ZoomModeProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_IgnoredInputKindsProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_MinZoomFactorProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_MaxZoomFactorProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_HorizontalAnchorRatioProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_VerticalAnchorRatioProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]


class IScrollSnapPoint(_inspectable.IInspectable):
    get_Value: _Callable[[_Pointer[_type.DOUBLE]],  # value
                         _type.HRESULT]


class IScrollSnapPointBase(_inspectable.IInspectable):
    get_Alignment: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Controls.Primitives.ScrollSnapPointsAlignment]],  # value
                             _type.HRESULT]


class IScrollSnapPointBaseFactory(_inspectable.IInspectable):
    pass


class IScrollSnapPointFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_type.DOUBLE,  # snapPointValue
                               _enum.Microsoft.UI.Xaml.Controls.Primitives.ScrollSnapPointsAlignment,  # alignment
                               _inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IScrollSnapPoint]],  # value
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
    GetIrregularSnapPoints: _Callable[[_enum.Microsoft.UI.Xaml.Controls.Orientation,  # orientation
                                       _enum.Microsoft.UI.Xaml.Controls.Primitives.SnapPointsAlignment,  # alignment
                                       _Pointer[_Windows_Foundation_Collections.IVectorView[_type.FLOAT]]],  # result
                                      _type.HRESULT]
    GetRegularSnapPoints: _Callable[[_enum.Microsoft.UI.Xaml.Controls.Orientation,  # orientation
                                     _enum.Microsoft.UI.Xaml.Controls.Primitives.SnapPointsAlignment,  # alignment
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
    add_SelectionChanged: _Callable[[_Microsoft_UI_Xaml_Controls.ISelectionChangedEventHandler,  # handler
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


class ISelectorItemStatics(_inspectable.IInspectable, factory=True):
    get_IsSelectedProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]


class ISelectorStatics(_inspectable.IInspectable, factory=True):
    get_SelectedIndexProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_SelectedItemProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_SelectedValueProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_SelectedValuePathProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    get_IsSynchronizedWithCurrentItemProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                         _type.HRESULT]
    GetIsSelectionActive: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                     _Pointer[_type.boolean]],  # result
                                    _type.HRESULT]


class ISnapPointBase(_inspectable.IInspectable):
    pass


class ISnapPointBaseFactory(_inspectable.IInspectable):
    pass


class ISplitViewTemplateSettings(_inspectable.IInspectable):
    get_OpenPaneLength: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    get_NegativeOpenPaneLength: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                          _type.HRESULT]
    get_OpenPaneLengthMinusCompactLength: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                    _type.HRESULT]
    get_NegativeOpenPaneLengthMinusCompactLength: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                            _type.HRESULT]
    get_OpenPaneGridLength: _Callable[[_Pointer[_struct.Microsoft.UI.Xaml.GridLength]],  # value
                                      _type.HRESULT]
    get_CompactPaneGridLength: _Callable[[_Pointer[_struct.Microsoft.UI.Xaml.GridLength]],  # value
                                         _type.HRESULT]


class ITabViewListView(_inspectable.IInspectable):
    pass


class ITabViewListViewFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ITabViewListView]],  # value
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


class IThumbStatics(_inspectable.IInspectable, factory=True):
    get_IsDraggingProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]


class ITickBar(_inspectable.IInspectable):
    get_Fill: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                        _type.HRESULT]
    put_Fill: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                        _type.HRESULT]


class ITickBarStatics(_inspectable.IInspectable, factory=True):
    get_FillProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]


class IToggleButton(_inspectable.IInspectable):
    get_IsChecked: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.boolean]]],  # value
                             _type.HRESULT]
    put_IsChecked: _Callable[[_Windows_Foundation.IReference[_type.boolean]],  # value
                             _type.HRESULT]
    get_IsThreeState: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_IsThreeState: _Callable[[_type.boolean],  # value
                                _type.HRESULT]
    add_Checked: _Callable[[_Microsoft_UI_Xaml.IRoutedEventHandler,  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Checked: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_Unchecked: _Callable[[_Microsoft_UI_Xaml.IRoutedEventHandler,  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_Unchecked: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    add_Indeterminate: _Callable[[_Microsoft_UI_Xaml.IRoutedEventHandler,  # handler
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


class IToggleButtonStatics(_inspectable.IInspectable, factory=True):
    get_IsCheckedProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_IsThreeStateProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]


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


class IZoomSnapPoint(_inspectable.IInspectable):
    get_Value: _Callable[[_Pointer[_type.DOUBLE]],  # value
                         _type.HRESULT]


class IZoomSnapPointBase(_inspectable.IInspectable):
    pass


class IZoomSnapPointBaseFactory(_inspectable.IInspectable):
    pass


class IZoomSnapPointFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_type.DOUBLE,  # snapPointValue
                               _inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IZoomSnapPoint]],  # value
                              _type.HRESULT]
